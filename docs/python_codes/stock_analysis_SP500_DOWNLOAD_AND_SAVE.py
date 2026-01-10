# ============================================================================
# stock_analysis_SP500_DOWNLOAD_AND_SAVE.py
# ============================================================================
import stock_analysis as sto


if __name__ == "__main__":
    # Run the download
    result = sto.download_sp500_csv_bulletproof('2019')
    
    if result:
        combined_df, saved_file = result
        print(f"\n🎉 SUCCESS! Your S&P 500 2020 data is saved at:")
        print(f"   📄 {saved_file}")
    else:
        print("\n❌ Download failed")
    