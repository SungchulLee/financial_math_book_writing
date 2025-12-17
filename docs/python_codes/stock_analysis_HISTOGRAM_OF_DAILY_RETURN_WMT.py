# ============================================================================
# stock_analysis_HISTOGRAM_OF_DAILY_RETURN_WMT.py
# ============================================================================
import matplotlib.pyplot as plt   
import scipy.stats as stats          
import stock_analysis as sto

# Stock analysis configuration
TICKER = "WMT"                    # Walmart stock ticker symbol
START_DATE = "2020-07-01"         # Starting date for historical data retrieval

# Initialize stock object and fetch data
stock = sto.USStock(TICKER)                    # Create Stock instance for Walmart
stock.get_data(start_date=START_DATE)      # Download historical price data from start date
stock.compute_returns()                    # Calculate simple and log returns
stock.compute_mu_and_sigma()               # Compute mean (mu) and standard deviation (sigma)

fig, axes = plt.subplots(1, 2, figsize=(14, 4))        
for ax, column in zip(axes, ['Return', 'Return_Log']):
    data = stock.df[column]                              
    _, bins, _ = ax.hist(data, bins=50, density=True, alpha=0.7, 
                        color='blue', label='Histogram')    
    mu, sigma = data.mean(), data.std()                  
    pdf = stats.norm(loc=mu, scale=sigma).pdf(bins)      
    ax.plot(bins, pdf, color='red', linestyle='--', 
           label=f'Normal PDF ($\mu={mu:.4f}$, $\sigma={sigma:.4f}$)') 
    ax.legend()                                          
    ax.set_xlabel(column)                               
    ax.set_ylabel('Density')                            
    ax.set_title(f'Histogram of {column}')              
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)    
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero') 
plt.tight_layout()    
plt.show()         