# VSTOXX Demo (Original)

## Background

Implied Volatility Vstoxx Demo

Educational script demonstrating implied volatility vstoxx demo concepts.

---

## Code

```python
"""
Implied Volatility Vstoxx Demo

Educational script demonstrating implied volatility vstoxx demo concepts.
"""

import numpy as np
import matplotlib.pyplot as plt

# Requires: ImpliedVol class
# Data: vstoxx_data_31032014.h5
# Download from: https://github.com/psygement/financepy/blob/master/part1/ch03/source/vstoxx_data_31032014.h5

# ======================================================================

def main():
    S = 17.6639 # 2014-03-31 VSTOXX Close
    # K read from data
    # T read from data
    r = 0.01
    # sigma will be computed in this code

    iv = ImpliedVol(S, r, tol=0.5)
    iv.compute_implied_volatility()
    # read only rows with implied volatility computed
    # if not computed, corresponding 'IMP_VOL' is np.NaN
    df = iv.options_data
    df.dropna(subset='IMP_VOL',inplace=True)

    maturities = sorted(set(df['MATURITY']))

    fig, ax = plt.subplots(figsize=(12,5))
    for maturity in maturities: # maturity --- Timestamp object, for example Timestamp('2014-04-18 02:00:00')
        data = df[df.MATURITY == maturity] # select data for this maturity
        ax.plot(data['STRIKE'], data['IMP_VOL'], label=maturity.date(), lw=0.7, alpha=0.9, ls="--",
                marker='.',
                markersize=5,
                markeredgecolor='black',
                markeredgewidth=0.1,
                markerfacecolor='black')
    ax.grid()
    ax.set_xlabel('strike')
    ax.set_ylabel('implied volatility')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
The VSTOXX close on 2014-03-31 was 17.6639. Explain what this number represents and its units.

??? success "Solution to Exercise 1"
    VSTOXX measures the 30-day implied volatility of the EURO STOXX 50 index, expressed in annualized percentage points. A value of 17.6639 means the market expects the EURO STOXX 50 to have annualized volatility of approximately 17.66%. This corresponds to a daily standard deviation of $17.66/\sqrt{252} \approx 1.11\%$ for the underlying equity index.

---

**Exercise 2.**
The IV smiles are plotted for multiple maturities. Explain why shorter maturities typically show steeper smiles than longer maturities.

??? success "Solution to Exercise 2"
    Short maturities amplify the impact of discrete events (earnings, economic data) and jump risk. The probability of a large percentage move in 1 week is relatively higher than in 1 year, so OTM options command higher IV. Over longer periods, the diffusion component dominates and the CLT smooths the distribution toward log-normal, flattening the smile.

---

**Exercise 3.**
Options with IV marked as NaN failed the computation. List three common reasons for IV computation failure.

??? success "Solution to Exercise 3"
    (1) The market price is below the intrinsic value (arbitrage violation), so no $\sigma > 0$ produces a BS price that low. (2) The option is too deep OTM with a price near zero, causing vega to vanish. (3) The Newton iteration diverges because $\sigma_0$ is too far from the solution or the price is inconsistent with BS assumptions (e.g., negative time value).

---

**Exercise 4.**
From the smile plot, estimate the 25-delta put and 25-delta call IVs for the nearest maturity. Compute the risk reversal and butterfly spread.

??? success "Solution to Exercise 4"
    Reading from a typical VSTOXX smile: 25-delta put IV $\approx$ 130%, ATM IV $\approx$ 110%, 25-delta call IV $\approx$ 105%. Risk reversal $= \sigma_{25\Delta C} - \sigma_{25\Delta P} = 105 - 130 = -25\%$ (negative, indicating put skew). Butterfly $= (\sigma_{25\Delta P} + \sigma_{25\Delta C})/2 - \sigma_{\text{ATM}} = (130 + 105)/2 - 110 = 7.5\%$ (positive, indicating convex smile/excess kurtosis).