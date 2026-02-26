# ============================================================================
# stock_analysis_COMPUTE_BASIC_STATISTICS_WMT.py
# ============================================================================
import stock_analysis as sto

# Stock analysis configuration
TICKER = "WMT"                    # Walmart stock ticker symbol
START_DATE = "2020-07-01"         # Starting date for historical data retrieval

# Initialize stock object and perform comprehensive analysis
stock = sto.USStock(TICKER)                          # Create USStock instance for Walmart
stock.get_data(start_date=START_DATE)            # Download historical data 
stock.compute_returns()                          # Calculate simple and log returns
stock.compute_mu_and_sigma()                     # Compute mean (mu) and standard deviation (sigma)

# Extract statistics from the nested statistics dictionary
stats = stock.statistics
arithmetic_stats = stats['arithmetic']          # Statistics for simple returns
logarithmic_stats = stats['logarithmic']        # Statistics for log returns

# Calculate Ito-corrected Mean Return (adjusts for Jensen's inequality)
mu_log_ito = arithmetic_stats['mu'] - 0.5 * arithmetic_stats['sigma']**2

# Display comprehensive statistical results
results = {
    "Annualized Return Volatility": arithmetic_stats['sigma'],        # Standard deviation of simple returns
    "Annualized Log Return Volatility": logarithmic_stats['sigma'],   # Standard deviation of log returns
    "Annualized Mean Return": arithmetic_stats['mu'],                 # Mean of simple returns
    "Annualized Mean Log Return": logarithmic_stats['mu'],            # Mean of log returns
    "Annualized Mean (Ito-Modified) Return": mu_log_ito               # Ito-corrected mean return
}

# Print results with formatted output
for i, (key, value) in enumerate(results.items()):
    print(f'{key:40}: {value:.2%}')                       # Format as percentage with 2 decimals
    if i == 1:                                            # Add blank line after volatility metrics
        print()