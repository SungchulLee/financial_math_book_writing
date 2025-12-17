# ============================================================================
# stock_analysis_CONTINUOUS_VS_DISCRETE_RETURN_WMT.py
# ============================================================================
import matplotlib.pyplot as plt
import scipy.stats as stats
import stock_analysis as sto

ticker = "WMT"
start_date = "2020-01-01"

company = sto.USStock(ticker)
company.get_data(start_date)
company.plot(plot_type='close')
company.compute_returns()
company.compute_mu_and_sigma()

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2,2,figsize=(12,8))

ax0.plot(company.df.index.to_numpy(), company.df["Return"].to_numpy(), label="Return", lw=5, alpha=0.5)
ax0.plot(company.df.index.to_numpy(), company.df["Return_Log"].to_numpy(), label="Return_Log")
ax0.set_title("Time Series of Returns")
ax0.legend()

ax1.plot(company.df["Return_Log"].to_numpy(), company.df["Return"].to_numpy(), "o", label="Return", alpha=0.5)
ax1.plot(company.df["Return_Log"].to_numpy(), company.df["Return_Log"].to_numpy(), label="Return_Log", ls="--", color="red")
ax1.set_xlabel("Return_Log")
ax1.set_ylabel("Return")
ax1.set_title("Return vs Return_Log")
ax1.legend()

mu = company.df["Return"].mean()
sigma = company.df["Return"].std()
_, bins, _ = ax2.hist(company.df["Return"].to_numpy(), density=True, bins=50)
pdf = stats.norm(loc=mu, scale=sigma).pdf(bins)
ax2.plot(bins, pdf) 
ax2.set_title(f"Return Histogram\n{mu = :.4f}, {sigma = :.4f}")

mu = company.df["Return_Log"].mean()
sigma = company.df["Return_Log"].std()
_, bins, _ = ax3.hist(company.df["Return_Log"].to_numpy(), density=True, bins=50)
pdf = stats.norm(loc=mu, scale=sigma).pdf(bins)
ax3.plot(bins, pdf) 
ax3.set_title(f"Return_Log Histogram\n{mu = :.4f}, {sigma = :.4f}")

fig.suptitle(f"{ticker} Returns Overview", fontsize=16)

plt.tight_layout()  
plt.show()

print(f"Annualized Mean of Return                        : {company.statistics['arithmetic']['mu']:.2f}%")
print(f"Annualized Mean of Log Return                    : {company.statistics['logarithmic']['mu']:.2f}%")
print(f"Ito Prediction for Annualized Mean of Log Return : {company.statistics['arithmetic']['mu']-0.5*company.statistics['arithmetic']['sigma']**2:.2f}%", end="\n\n")
print(f"Annualized Std of Return     : {company.statistics['arithmetic']['sigma']:.2f}%")
print(f"Annualized Std of Log Return : {company.statistics['logarithmic']['sigma']:.2f}%")