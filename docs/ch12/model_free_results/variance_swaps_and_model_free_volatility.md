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

---

## Exercises

**Exercise 1.** A variance swap has notional $N = \$100{,}000$ per variance point, maturity $T = 0.25$ years, and strike $K_{\text{var}} = 0.04$ (corresponding to 20% volatility). If the realized variance over the period is $\text{RV} = 0.0625$ (25% volatility), compute the payoff to the long variance position.

---

**Exercise 2.** The model-free replication formula for variance swap fair strike involves the integral $\frac{2}{T}\int_0^\infty \frac{C(K)}{K^2} dK$, split at the forward $F$ into put and call components. Explain why the $1/K^2$ weighting gives more weight to low-strike (OTM put) options. What does this imply about the sensitivity of variance swap pricing to left-tail events?

---

**Exercise 3.** The variance risk premium is defined as $\text{VRP} = \sigma_{\text{IV}}^2 - \mathbb{E}^P[\text{RV}]$. Empirical studies find that VRP is typically positive for equity indices (implied variance exceeds expected realized variance). (a) What economic explanation accounts for this premium? (b) How can a trader profit from a consistently positive VRP? (c) What are the risks of such a strategy?

---

**Exercise 4.** Given the variance swap formula, explain why the VIX index can be interpreted as the square root of the fair variance swap strike (with a small adjustment). If VIX = 22, what is the implied annualized variance? What is the market's expectation for 30-day realized volatility (ignoring the variance risk premium)?

---

**Exercise 5.** The variance curve plots $K_{\text{var}}(T)$ versus maturity $T$. During a market crisis, the variance curve typically inverts (short-dated variance higher than long-dated). (a) What does this imply about the market's expectation for near-term versus long-term volatility? (b) How does this relate to the mean-reversion property of volatility?

---

**Exercise 6.** A forward-starting variance swap covers the period $[T_1, T_2]$ with fair strike $\sigma_{\text{fwd}}^2 = \frac{K_{\text{var}}(T_2) T_2 - K_{\text{var}}(T_1) T_1}{T_2 - T_1}$. Given $K_{\text{var}}(0.25) = 0.04$ and $K_{\text{var}}(0.50) = 0.036$, compute the forward variance for the period $[0.25, 0.50]$. Is the forward variance higher or lower than the spot variance?

---

**Exercise 7.** In practice, the variance swap replication integral is approximated by a discrete sum over traded strikes. Describe the discretization procedure and identify two sources of error: (a) truncation error from the finite strike range and (b) interpolation error between observed strikes. How does each error affect the accuracy of the VIX calculation?
