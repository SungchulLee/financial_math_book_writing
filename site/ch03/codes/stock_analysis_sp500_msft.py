"""
Stock Analysis Sp500 Msft

Educational script demonstrating stock analysis sp500 msft concepts.
"""

# ============================================================================
# stock_analysis_SP500_DOWNLOAD_FINANTIAL_DATA_MSFT.py
# ============================================================================
import yfinance as yf

# Initialize ticker


if __name__ == "__main__":
    msft = yf.Ticker("MSFT")

    # ------------------------
    # 📌 Basic Company Info
    # ------------------------
    print("\n📈 Company Profile")
    print("-" * 40)
    info = msft.info
    info_keys = ['longName', 'sector', 'industry', 'marketCap', 'forwardPE', 'dividendYield']
    for key in info_keys:
        print(f"{key:20}: {info.get(key)}")

    # ------------------------
    # 📅 Earnings Calendar
    # ------------------------
    print("\n📅 Earnings Calendar")
    print("-" * 40)
    print(msft.calendar)

    # ------------------------
    # 🧾 Income Statement (Quarterly)
    # ------------------------
    print("\n🧾 Quarterly Income Statement")
    print("-" * 40)
    income = msft.quarterly_income_stmt
    print(income)

    # Show Net Income only
    if "Net Income" in income.index:
        print("\n💰 Quarterly Net Income")
        print("-" * 40)
        print(income.loc["Net Income"])

    # ------------------------
    # 📊 Balance Sheet (Quarterly)
    # ------------------------
    print("\n📊 Quarterly Balance Sheet")
    print("-" * 40)
    print(msft.quarterly_balance_sheet)

    # ------------------------
    # 💵 Cash Flow (Quarterly)
    # ------------------------
    print("\n💵 Quarterly Cash Flow")
    print("-" * 40)
    print(msft.quarterly_cashflow)

    # ------------------------
    # 💸 Dividends (Most Recent)
    # ------------------------
    print("\n💸 Recent Dividends")
    print("-" * 40)
    print(msft.dividends.tail())

    # ------------------------
    # 💬 Analyst Recommendations
    # ------------------------
    print("\n💬 Analyst Recommendations")
    print("-" * 40)
    print(msft.recommendations.tail())

    # ------------------------
    # 🔁 Stock Splits
    # ------------------------
    print("\n🔁 Historical Stock Splits")
    print("-" * 40)
    print(msft.splits.tail())
    