import os
import json
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from io import StringIO

class KOSPI200:
    def __init__(self, refresh_tickers=False, refresh_data=False):
        """
        Initialize the KOSPI200 class.

        Args:
            refresh_kospi_list (bool): If True, refresh the ticker list from Wikipedia.
            refresh_kospi_data (bool): If True, refresh financial data from Naver Finance.
        """
        self.data = pd.DataFrame()
        self.kospi200_dict = {}

        os.makedirs("data", exist_ok=True)
        dict_file = "data/kospi200_dict.json"
        data_file = "data/kospi200_data.csv"

        if not refresh_tickers and os.path.exists(dict_file):
            print("📂 Loading cached KOSPI 200 ticker map...")
            with open(dict_file, "r", encoding="utf-8") as f:
                self.kospi200_dict = json.load(f)
        else:
            print("🌐 Fetching KOSPI 200 tickers from Wikipedia...")
            self._get_kospi200_tickers()
            with open(dict_file, "w", encoding="utf-8") as f:
                json.dump(self.kospi200_dict, f, ensure_ascii=False, indent=2)
            print("✅ Saved ticker map to", dict_file)

        if not refresh_data and os.path.exists(data_file):
            print("📂 Loading cached KOSPI 200 financial data...")
            self.data = pd.read_csv(data_file, dtype={"Ticker": "string"})
        else:
            print("🌐 Scraping KOSPI 200 financial data...")
            self._scrape_data()
            self.data.to_csv(data_file, index=False)
            print("✅ Saved financial data to", data_file)

    def _get_kospi200_tickers(self):
        """
        Scrape the KOSPI 200 ticker symbols and company names from Wikipedia
        and populate self.kospi200_dict.
        """
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

        self.kospi200_dict = {
            name.strip(): str(ticker).zfill(6)
            for name, ticker in zip(company_names, tickers)
        }

    def _scrape_data(self, sleep_sec=0.5):
        """
        Scrape financial data for KOSPI 200 companies from Naver Finance
        and populate self.data.

        Args:
            sleep_sec (float): Seconds to sleep between requests to avoid blocking.
        """
        records = []
        for name, ticker in self.kospi200_dict.items():
            try:
                url = f"https://finance.naver.com/item/main.naver?code={ticker}"
                headers = {"User-Agent": "Mozilla/5.0"}
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, "html.parser")

                def clean_number(text):
                    return float(text.replace(',', '').replace('%', '').replace('\u00a0', '').strip())

                section = soup.find("div", class_="aside_invest_info")
                rows = section.find_all("tr") if section else []

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

                for row in rows:
                    th = row.find("th")
                    td = row.find("td")
                    if not th or not td:
                        continue
                    label = th.text.strip()
                    value = td.get_text(separator="", strip=True)

                    if "시가총액" in label and "순위" not in label:
                        clean_value = td.get_text(separator="", strip=True).replace("\n", "").replace("\t", "").replace("\xa0", "")
                        info["Market Cap (억)"] = self.parse_market_cap_korean(clean_value)
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
                            break

                for tag, key in [("_per", "PER"), ("_pbr", "PBR"), ("_dvr", "Dividend Yield (%)")]:
                    em = soup.find("em", id=tag)
                    if em:
                        try:
                            info[key] = clean_number(em.text)
                        except:
                            pass

                industry_per = None
                tables = soup.find_all("table", summary="동일업종 PER 정보")
                for table in tables:
                    rows = table.find_all("tr")
                    for row in rows:
                        th = row.find("th")
                        td = row.find("td")
                        if th and td and "동일업종 PER" in th.text:
                            em = td.find("em")
                            if em:
                                try:
                                    industry_per = float(em.text.strip().replace(",", ""))
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
        """
        Convert Korean-formatted market capitalization text to numeric value.

        Args:
            text (str): Market cap text like '2조4,726억원'.

        Returns:
            int or None: Market cap in 억 (100 million) KRW.
        """
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
        """
        Convert won-formatted string to integer value.

        Args:
            text (str): String with Korean won symbol (e.g., '5,000원').

        Returns:
            int or None: Numeric integer value.
        """
        try:
            return int(text.replace(",", "").replace("원", "").strip())
        except:
            return None

    def print_summary(self):
        """
        Print the first 10 rows of the financial data summary.
        """
        df = self.data.copy()
        df["Ticker"] = df["Ticker"].astype("string").apply(lambda x: x.zfill(6))
        print("\n📋 Full Financial Summary (first 10 rows):\n")
        print(df.head(10).to_string(index=False))

    def print_sorted(self, column, ascending=True,
                     trim_bottom_percentile=0.03,
                     trim_top_percentile=0.03,
                     sigma_band: int = 3,
                     num_print: int = 20,
                     plot_only: bool = False):
        """
        Plot a histogram and print the sorted data for a given financial metric.

        Args:
            column (str): Column to analyze.
            ascending (bool): Whether to sort in ascending order.
            trim_bottom_percentile (float): Lower quantile for outlier trimming.
            trim_top_percentile (float): Upper quantile for outlier trimming.
            sigma_band (int): Standard deviation band to highlight.
            num_print (int): Number of companies to display.
            plot_only (bool): If True, only show the plot.
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
            trimmed_df["Ticker"] = trimmed_df["Ticker"].astype("string").apply(lambda x: x.zfill(6))
            sorted_df = trimmed_df.sort_values(by=column, ascending=ascending)
            print(f"\n📊 Top {num_print} companies sorted by {column} ({'Asc' if ascending else 'Desc'}):\n")
            print(sorted_df[["Company", "Ticker", column]].head(num_print).to_string(index=False))

    def plot_per_vs_dividend(self, mode="low_per", n=20, exclude=None):
        """
        Plot a scatterplot of PER vs. Dividend Yield for selected companies and
        print their details below the plot.

        Args:
            mode (str): Either 'low_per' or 'high_dividend' to determine selection.
            n (int): Number of companies to plot.
            exclude (list): List of company names to exclude from the plot.
        """
        """
        Plot a scatterplot of PER vs. Dividend Yield for selected companies.

        Args:
            mode (str): Either 'low_per' or 'high_dividend' to determine selection.
            n (int): Number of companies to plot.
            exclude (list): List of company names to exclude from the plot.
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

        # Print company info after the plot
        print("📋 Company Info in Plot:")
        print(self.data[self.data["Company"].isin(selected["Company"])]
              .set_index("Company")
              .loc[selected.set_index("Company").index]
              .reset_index()
              .to_string(index=False))