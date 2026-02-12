# Variance Swaps and Model-Free Volatility

Variance swaps provide direct exposure to realized volatility and enable model-free pricing of volatility. These instruments reveal the market's volatility expectations independent of any specific pricing model and form the foundation for variance curve construction and volatility derivatives trading.

## Key Concepts

**Variance Swap Definition**
A variance swap exchanges realized variance for a fixed strike:
$$\text{Payoff} = N \times \left(\sum_i \ln^2\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right) - K_{\text{var}}^2\right) \times \Delta t$$

Key features:
- Long variance position: profits when realized volatility exceeds strike
- Cash settlement: no need to hold underlying asset
- Fair strike $K_{\text{var}}^*$ determined by replication arguments

**Model-Free Replication**
Under risk-neutral measure, realized variance can be replicated using:
1. A log contract (payoff = $\ln S_T / S_0$) for the mean term
2. A continuum of out-of-the-money options across all strikes for the variance term

The replication formula:
$$\text{Var}(S) = 2 \int_0^{\infty} \frac{C(K)}{K^2} dK - \frac{1}{T}\ln^2(F/S_0)$$

where $C(K)$ are European call prices and $F$ is the forward.

**Relating Variance to Volatility**
Realized variance: $\text{RV} = \frac{1}{T}\sum_i r_i^2$

Implied variance from options: $\sigma_{\text{IV}}^2 = E^Q[\text{RV}]$ (risk-neutral expectation)

The variance risk premium: $\text{VRP} = \sigma_{\text{IV}}^2 - E^P[\text{RV}]$
where the superscript denotes risk-neutral (Q) vs physical (P) measure.

**Model-Free Implied Volatility**
The VIX index computes model-free implied volatility from options:
$$\text{VIX}^2 = \frac{2}{T}\int_0^{\infty} \frac{C(K)}{K^2} dK - \frac{1}{T}\ln^2(F/K_0)$$
This is model-independent and directly observable from market option prices.

**Volatility Curve Construction**
Variance swaps at different maturities trace out the variance curve:
- Short-dated: influenced by near-term uncertainty and momentum
- Long-dated: approach long-run volatility forecast
- Term structure shape: upward sloping (near trough) or downward sloping (elevated stress)

!!! note "Market Applications"
    Variance swaps enable:
    - Pure volatility trading without directional bet
    - Volatility curve construction from traded instruments
    - Hedging volatility exposure (vega neutral portfolio construction)
    - Arbitrage between realized and implied volatility
    - Model-free calibration targets for stochastic vol models
