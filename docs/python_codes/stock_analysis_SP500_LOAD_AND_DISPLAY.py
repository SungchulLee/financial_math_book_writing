# ============================================================================
# stock_analysis_SP500_LOAD_AND_DISPLAY.py
# ============================================================================
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = './stock_analysis/sp500/sp500_data/sp500_2021.csv'
df = pd.read_csv(file_path)

# Display basic info about the dataset
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())

# Convert date column to datetime if needed
# Adjust the date column name based on your CSV structure
date_column = 'Date'  # Common names: 'Date', 'date', 'DATE', 'timestamp'
if date_column in df.columns:
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(date_column)
elif 'date' in df.columns:
    date_column = 'date'
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(date_column)

# Filter for AAPL and WMT data
# Adjust column names based on your CSV structure
# Common patterns: 'AAPL_Close', 'AAPL', 'Close_AAPL', etc.
aapl_col = None
wmt_col = None

# Try to find AAPL and WMT columns
for col in df.columns:
    if 'AAPL' in col.upper() and ('CLOSE' in col.upper() or col.upper() == 'AAPL'):
        aapl_col = col
    elif 'WMT' in col.upper() and ('CLOSE' in col.upper() or col.upper() == 'WMT'):
        wmt_col = col

if aapl_col is None or wmt_col is None:
    print("Available columns:", df.columns.tolist())
    print("Please adjust the column names in the code based on your CSV structure")
    # Fallback - assume the CSV has columns named exactly 'AAPL' and 'WMT'
    aapl_col = 'AAPL'
    wmt_col = 'WMT'

# Extract the close prices for both stocks
aapl_prices = df[aapl_col].dropna()
wmt_prices = df[wmt_col].dropna()

# Get corresponding dates (ensure alignment)
if date_column in df.columns:
    dates = df[date_column]
else:
    # If no date column, create a simple index
    dates = range(len(df))

# Normalize prices to start at 100
aapl_normalized = (aapl_prices / aapl_prices.iloc[0]) * 100
wmt_normalized = (wmt_prices / wmt_prices.iloc[0]) * 100

# Create the plot
plt.figure(figsize=(12, 8))

# Convert to numpy arrays to avoid pandas indexing issues
aapl_dates = dates[:len(aapl_normalized)].values if hasattr(dates, 'values') else dates[:len(aapl_normalized)]
wmt_dates = dates[:len(wmt_normalized)].values if hasattr(dates, 'values') else dates[:len(wmt_normalized)]

# Plot normalized prices
plt.plot(aapl_dates, aapl_normalized.values, 
         label='AAPL', linewidth=2, color='#1f77b4')
plt.plot(wmt_dates, wmt_normalized.values, 
         label='WMT', linewidth=2, color='#ff7f0e')

# Add horizontal line at 100 (starting point)
plt.axhline(y=100, color='gray', linestyle='--', alpha=0.7, label='Base (100)')

# Customize the plot
plt.title('Normalized Stock Price Comparison - AAPL vs WMT (2021)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Normalized Price (Base = 100)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Format x-axis if using dates
if date_column in df.columns:
    plt.xticks(rotation=45)
    plt.tight_layout()

# Add some styling
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Show the plot
plt.show()

# Print summary statistics
print(f"\nSummary Statistics:")
print(f"AAPL - Starting price: ${aapl_prices.iloc[0]:.2f}")
print(f"AAPL - Ending price: ${aapl_prices.iloc[-1]:.2f}")
print(f"AAPL - Total return: {((aapl_prices.iloc[-1] / aapl_prices.iloc[0]) - 1) * 100:.1f}%")

print(f"\nWMT - Starting price: ${wmt_prices.iloc[0]:.2f}")
print(f"WMT - Ending price: ${wmt_prices.iloc[-1]:.2f}")
print(f"WMT - Total return: {((wmt_prices.iloc[-1] / wmt_prices.iloc[0]) - 1) * 100:.1f}%")

# Optional: Save the plot
# plt.savefig('normalized_stock_comparison.png', dpi=300, bbox_inches='tight')
    