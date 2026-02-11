import os
import json
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from io import StringIO

class KRX:
    TICKER_TYPES = ["KOSPI200", "KOSPI", "KOSDAQ"]

    def __init__(self, tickers="KOSPI", refresh_tickers=False, refresh_data=False):
        assert tickers in self.TICKER_TYPES, f"Invalid tickers argument. Choose from {self.TICKER_TYPES}"
        self.data = pd.DataFrame()
        self.tickers_dict = {}
        self.ticker_source = tickers

        os.makedirs("data", exist_ok=True)
        dict_file = f"data/{tickers.lower()}_dict.json"
        data_file = f"data/{tickers.lower()}_data.csv"

        if not refresh_tickers and os.path.exists(dict_file):
            print("📂 Loading cached ticker map...")
            with open(dict_file, "r", encoding="utf-8") as f:
                self.tickers_dict = json.load(f)
        else:
            if tickers == "KOSPI200":
                print("🌐 Fetching KOSPI 200 tickers from Wikipedia...")
                self._get_kospi200_tickers()
            elif tickers == "KOSPI":
                self._get_kospi_tickers()
            elif tickers == "KOSDAQ":
                self._get_kosdaq_tickers()

            with open(dict_file, "w", encoding="utf-8") as f:
                json.dump(self.tickers_dict, f, ensure_ascii=False, indent=2)
            print("✅ Saved ticker map to", dict_file)

        if not refresh_data and os.path.exists(data_file):
            print("📂 Loading cached financial data...")
            self.data = pd.read_csv(data_file, dtype={"Ticker": "string"})
        else:
            print("🌐 Scraping financial data...")
            self._scrape_data()
            self.data.to_csv(data_file, index=False)
            print("✅ Saved financial data to", data_file)

    def _get_kospi200_tickers(self):
        url = "https://en.wikipedia.org/wiki/KOSPI_200"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all("table", {"class": "wikitable"})
        company_names, tickers = [], []
        for table in tables:
            df = pd.read_html(StringIO(str(table)))[0]
            for col in df.columns:
                if "Company" in col:
                    company_names.extend(df[col].dropna().tolist())
                if "Symbol" in col:
                    tickers.extend(df[col].dropna().tolist())
        self.tickers_dict = {
            name.strip(): str(ticker).zfill(6)
            for name, ticker in zip(company_names, tickers)
        }

    def _get_kospi_tickers(self):
        self._get_market_tickers(market="KOSPI", sosok="0", pages=47)

    def _get_kosdaq_tickers(self):
        self._get_market_tickers(market="KOSDAQ", sosok="1", pages=33)

    def _get_market_tickers(self, market, sosok, pages):
        print(f"🌐 Scraping {market} tickers from Naver Finance...")
        headers = {"User-Agent": "Mozilla/5.0"}
        tickers_dict = {}
        for page in range(1, pages + 1):
            url = f"https://finance.naver.com/sise/sise_market_sum.naver?sosok={sosok}&page={page}"
            try:
                html = requests.get(url, headers=headers).text
                tables = pd.read_html(html)
                df = tables[1].dropna(subset=["종목명"])
                soup = BeautifulSoup(html, "html.parser")
                raw_tickers = [a["href"].split("=")[-1] for a in soup.select("a.tltle")]
                for name, ticker in zip(df["종목명"], raw_tickers):
                    tickers_dict[name.strip()] = str(ticker).zfill(6)
            except Exception as e:
                print(f"❌ Failed to parse page {page}: {e}")
            time.sleep(0.1)
        self.tickers_dict = tickers_dict

    def _scrape_data(self, sleep_sec=0.5):
        records = []
        for name, ticker in self.tickers_dict.items():
            try:
                url = f"https://finance.naver.com/item/main.naver?code={ticker}"
                headers = {"User-Agent": "Mozilla/5.0"}
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, "html.parser")

                def clean_number(text):
                    return float(text.replace(',', '').replace('%', '').replace('\u00a0', '').strip())

                info = {
                    "Company": name,
                    "Ticker": str(ticker).zfill(6),
                    "Market Cap (억)": None,
                    "Current Price (원)": None,
                    "Face Value (원)": None,
                    "PER": None,
                    "PBR": None,
                    "Dividend Yield (%)": None,
                    "Industry PER": None
                }

                section = soup.find("div", class_="aside_invest_info")
                rows = section.find_all("tr") if section else []
                for row in rows:
                    th, td = row.find("th"), row.find("td")
                    if not th or not td:
                        continue
                    label = th.text.strip()
                    value = td.get_text(separator="", strip=True)
                    if "시가총액" in label and "순위" not in label:
                        info["Market Cap (억)"] = self.parse_market_cap_korean(value)
                    elif "액면가" in label:
                        raw = value.split('|')[0].strip()[:-3]
                        info["Face Value (원)"] = self.parse_won_to_int(raw)

                price_block = soup.find("div", class_="rate_info")
                if price_block:
                    dd_tags = price_block.find_all("dd")
                    for dd in dd_tags:
                        if "오늘의시세" in dd.text:
                            try:
                                info["Current Price (원)"] = int(dd.text.strip().split(" ")[-2].replace(",", ""))
                            except:
                                pass

                for tag, key in [("_per", "PER"), ("_pbr", "PBR"), ("_dvr", "Dividend Yield (%)")]:
                    em = soup.find("em", id=tag)
                    if em:
                        try:
                            val = clean_number(em.text)
                            info[key] = val if val >= 0 else None
                        except:
                            pass

                industry_per = None
                tables = soup.find_all("table", summary="동일업종 PER 정보")
                for table in tables:
                    rows = table.find_all("tr")
                    for row in rows:
                        th, td = row.find("th"), row.find("td")
                        if th and td and "동일업종 PER" in th.text:
                            em = td.find("em")
                            if em:
                                try:
                                    val = float(em.text.strip().replace(",", ""))
                                    industry_per = val if val > 0 else None
                                except:
                                    pass
                info["Industry PER"] = industry_per

                records.append(info)
                time.sleep(sleep_sec)

            except Exception as e:
                print(f"⚠️ Failed for {name} ({ticker}): {e}")

        self.data = pd.DataFrame(records)
        self.data["Ticker"] = self.data["Ticker"].astype("string")

    @staticmethod
    def parse_market_cap_korean(text):
        try:
            text = text.replace(",", "")
            trillion = 0
            billion = 0
            if "조" in text:
                parts = text.split("조")
                trillion = int(parts[0])
                if "억" in parts[1]:
                    billion = int(parts[1].split("억")[0])
            elif "억" in text:
                billion = int(text.split("억")[0])
            return trillion * 10000 + billion
        except:
            return None

    @staticmethod
    def parse_won_to_int(text):
        try:
            return int(text.replace(",", "").replace("원", "").strip())
        except:
            return None

    def print_summary(self, n=10):
        """
        Print summary with all numeric fields aligned and Company moved to the last column.
        """
        df = self.data.copy()
        df["Ticker"] = df["Ticker"].astype(str).apply(lambda x: x.zfill(6))

        display_df = df[[
            "Ticker", "Market Cap (억)", "Current Price (원)",
            "Face Value (원)", "PER", "PBR", "Dividend Yield (%)", "Industry PER", "Company"
        ]].head(n).fillna("")

        header_fmt = (
            f"{{:>8}} {{:>15}} {{:>18}} {{:>15}} {{:>8}} {{:>6}} {{:>12}} {{:>12}}  {{:<22}}"
        )
        row_fmt = (
            f"{{:>8}} {{:>15}} {{:>18}} {{:>15}} {{:>8}} {{:>6}} {{:>12}} {{:>12}}  {{:<22}}"
        )

        print("\n📋 Full Financial Summary (first {} rows):\n".format(n))
        print(header_fmt.format(
            "Ticker", "Market Cap (억)", "Current Price (원)", "Face Value (원)",
            "PER", "PBR", "Dividend (%)", "Industry PER", "Company"
        ))
        print("=" * 140)

        for _, row in display_df.iterrows():
            def fmt(x, digits=2, suffix=""):
                if x == "" or pd.isna(x): return ""
                try: return f"{float(x):,.{digits}f}{suffix}"
                except: return str(x)

            def fmt_int(x):
                if x == "" or pd.isna(x): return ""
                try: return f"{int(float(x)):,}"
                except: return str(x)

            print(row_fmt.format(
                row["Ticker"],
                fmt_int(row["Market Cap (억)"]),
                fmt_int(row["Current Price (원)"]),
                fmt_int(row["Face Value (원)"]),
                fmt(row["PER"]),
                fmt(row["PBR"]),
                fmt(row["Dividend Yield (%)"], suffix="%"),
                fmt(row["Industry PER"]),
                str(row["Company"])[:22]
            ))

    def print_sorted(self, column, ascending=True,
                    trim_bottom_percentile=0.03,
                    trim_top_percentile=0.03,
                    sigma_band: int = 3,
                    num_print: int = 20,
                    plot_only: bool = False):
        """
        Plot a histogram and print the sorted data for a given financial metric.
        Now prints with company name at the end to avoid misalignment from Korean characters.
        """
        if column not in self.data.columns:
            print(f"❌ Column '{column}' not found.")
            return

        df = self.data.dropna(subset=[column]).copy()

        try:
            df[column] = pd.to_numeric(df[column], errors='coerce')
            df = df.dropna(subset=[column])
        except:
            print(f"❌ Column '{column}' is not numeric.")
            return

        lower = df[column].quantile(trim_bottom_percentile)
        upper = df[column].quantile(1 - trim_top_percentile)
        trimmed_df = df[(df[column] >= lower) & (df[column] <= upper)]
        kept_pct = int((1 - trim_bottom_percentile - trim_top_percentile) * 100)

        stats = trimmed_df[column].agg(["mean", "std", "min", "max", "median"]).round(3)
        mean, std = stats["mean"], stats["std"]
        low_bound = mean - sigma_band * std
        high_bound = mean + sigma_band * std

        fig, ax = plt.subplots(figsize=(12, 4))
        ax.hist(trimmed_df[column], bins=15, color='skyblue', edgecolor='black', density=True)
        ax.axvline(mean, color='red', linestyle='-', linewidth=2, label=f"Mean: {mean:.2f}")
        ax.axvline(low_bound, color='orange', linestyle='--', linewidth=1.5, label=f"-{sigma_band}σ: {low_bound:.2f}")
        ax.axvline(high_bound, color='orange', linestyle='--', linewidth=1.5, label=f"+{sigma_band}σ: {high_bound:.2f}")
        ax.axvspan(low_bound, high_bound, color='orange', alpha=0.2)

        ax.set_title(
            f"{column} Distribution (Trimmed Middle {kept_pct}%)\n"
            f"Mean: {mean}, Std: {std}, Min: {stats['min']}, Max: {stats['max']}, Median: {stats['median']}",
            fontsize=11
        )
        ax.set_xlabel(column)
        ax.set_ylabel("Density")
        ax.legend()
        plt.tight_layout()
        plt.show()

        if not plot_only:
            trimmed_df = trimmed_df.copy()
            trimmed_df["Ticker"] = trimmed_df["Ticker"].astype(str).apply(lambda x: x.zfill(6))
            sorted_df = trimmed_df.sort_values(by=column, ascending=ascending)
            top_df = sorted_df[["Ticker", column, "Company"]].head(num_print)

            print(f"\n📊 Top {num_print} companies sorted by {column} ({'Asc' if ascending else 'Desc'}):\n")

            # Header
            print(f"{'Ticker':>8} {column:>15}  {'Company':<22}")
            print("=" * (8 + 1 + 15 + 2 + 22))

            for _, row in top_df.iterrows():
                ticker = row["Ticker"]
                value = f"{float(row[column]):,.2f}"
                company = str(row["Company"])[:22]
                print(f"{ticker:>8} {value:>15}  {company:<22}")

    def plot_per_vs_dividend(self, mode="low_per", n=20, exclude=None):
        """
        Plot a scatterplot of PER vs. Dividend Yield for selected companies and
        print their details with 'Company' as the last column for alignment.
        """
        if "PER" not in self.data.columns or "Dividend Yield (%)" not in self.data.columns:
            print("❌ Required columns ('PER', 'Dividend Yield (%)') not found.")
            return

        df = self.data[["Company", "PER", "Dividend Yield (%)"]].dropna()

        try:
            df["PER"] = pd.to_numeric(df["PER"], errors="coerce")
            df["Dividend Yield (%)"] = pd.to_numeric(df["Dividend Yield (%)"], errors="coerce")
            df = df.dropna()
        except:
            print("❌ Numeric conversion failed.")
            return

        if exclude:
            df = df[~df["Company"].isin(exclude)]

        if mode == "low_per":
            selected = df.nsmallest(n, "PER")
            title = f"Top {n} Companies with Lowest PER"
        elif mode == "high_dividend":
            selected = df.nlargest(n, "Dividend Yield (%)")
            title = f"Top {n} Companies with Highest Dividend Yield"
        else:
            print("❌ Invalid mode. Choose 'low_per' or 'high_dividend'.")
            return

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(selected["PER"], selected["Dividend Yield (%)"], color="teal", edgecolor="black")

        for _, row in selected.iterrows():
            ax.text(row["PER"], row["Dividend Yield (%)"], row["Company"], fontsize=9, ha='right', va='bottom', fontproperties=fontproperties)

        ax.set_title(title + "\nPER vs. Dividend Yield (%)", fontsize=13)
        ax.set_xlabel("PER")
        ax.set_ylabel("Dividend Yield (%)")
        ax.grid(True)
        plt.tight_layout()
        plt.show()

        # Print company info
        print("\n📋 Company Info in Plot:\n")
        print(f"{'PER':>8} {'Dividend (%)':>15}  {'Company':<22}")
        print("=" * 50)

        for _, row in selected.iterrows():
            per = f"{row['PER']:.2f}"
            div_yield = f"{row['Dividend Yield (%)']:.2f}%"
            company = str(row['Company'])[:22]
            print(f"{per:>8} {div_yield:>15}  {company:<22}")

    def print_info_for_ticker(self, ticker):
        """
        Print all available financial information for the given ticker.
        """
        ticker = str(ticker).zfill(6)  # Normalize ticker format
        df = self.data.copy()

        if "Ticker" not in df.columns:
            print("❌ Financial data not loaded.")
            return

        row = df[df["Ticker"] == ticker]
        if row.empty:
            raise ValueError(f"❌ Ticker '{ticker}' not found in the dataset.")

        row = row.iloc[0]
        print(f"\n📘 Financial Information for {row['Company']} ({ticker})\n" + "="*50)
        for col in df.columns:
            if col == "Ticker":
                continue  # Already displayed
            val = row[col]
            if pd.isna(val):
                val_str = "N/A"
            elif isinstance(val, float):
                if abs(val) >= 1e9:
                    val_str = f"{val:,.2e}"
                elif "%" in col or "Yield" in col:
                    val_str = f"{val:.2f}%"
                else:
                    val_str = f"{val:,.2f}"
            else:
                val_str = str(val)
            print(f"{col:<25}: {val_str}")