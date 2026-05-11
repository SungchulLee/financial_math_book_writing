# Geometric Brownian Motion Simulation

## Background

Black Scholes Gbm

Educational script demonstrating black scholes gbm concepts.

---

## Code

```python
"""
Black Scholes Gbm

Educational script demonstrating black scholes gbm concepts.
"""

# ============================================================================
# black_scholes_GEOMETRIC_BROWNIAN_MOTION.py
# ============================================================================
import black_scholes as bs

# Model parameters


if __name__ == "__main__":
    S0 = 100      # Current stock price
    K = 105       # Strike price
    T = 1         # 1 year to expiration
    r = 0.05      # 5% risk-free rate
    sigma = 0.2   # 20% volatility
    q = 0.02      # 2% dividend yield
    
    # Create the unified Black-Scholes interface
    bs_model = bs.BlackScholes(S0=S0, K=K, T=T, r=r, sigma=sigma, q=q)

    # risk neutral path simulation and visualization 
    bs_model.plot_paths_and_histogram(
        num_paths=1000, 
        max_paths_display=50, 
        seed=42, 
        title=f'Sample GBM Paths with Final Price Distribution\nunder Risk Neutral Measure r = {r}'
        )
    
    # risk neutral vs real world path simulation and visualization 
    mu = 0.08  # 8% real-world drift
    bs_model.plot_gbm_comparison(
        num_paths=1000, 
        max_paths_display=50, 
        seed=42, 
        mu=mu
        )
```

## Exercises

**Exercise 1.**
Write the SDE for geometric Brownian motion under the risk-neutral measure and under the real-world measure. What is the key difference?

??? success "Solution to Exercise 1"
    Under the **real-world measure** $\mathbb{P}$: $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$

    Under the **risk-neutral measure** $\mathbb{Q}$: $dS_t = (r - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$

    The key difference is the drift: $\mu$ (expected return) under $\mathbb{P}$ versus $r - q$ (risk-free rate minus dividends) under $\mathbb{Q}$. The volatility $\sigma$ is the same under both measures. The change from $\mathbb{P}$ to $\mathbb{Q}$ is accomplished by the Girsanov theorem: $dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} + \frac{\mu - r + q}{\sigma}\,dt$.

---

**Exercise 2.**
Simulate 5 GBM paths with $S_0 = 100$, $\mu = 0.08$, $\sigma = 0.20$, $T = 1$ using 252 daily steps. Describe the expected range of terminal values.

??? success "Solution to Exercise 2"
    The terminal value is $S_T = 100\exp\bigl((0.08 - 0.02)T + 0.20\sqrt{T}\,Z\bigr) = 100\exp(0.06 + 0.20Z)$ where $Z \sim \mathcal{N}(0,1)$.

    The mean is $E[S_T] = 100 e^{0.08} \approx 108.33$. For a 95% range: $Z \in [-1.96, 1.96]$, giving $S_T \in [100 e^{0.06 - 0.392}, 100 e^{0.06 + 0.392}] = [100 e^{-0.332}, 100 e^{0.452}] \approx [71.7, 157.2]$.

    Five paths will show diverse behavior: some trending up, some down, all with the characteristic jagged appearance of random walks.

---

**Exercise 3.**
Compare risk-neutral and real-world path simulations. Why do risk-neutral paths have a lower expected return, and why is this correct for pricing?

??? success "Solution to Exercise 3"
    Risk-neutral paths use drift $r - q$ (typically 3--5%) instead of $\mu$ (typically 8--12%). The expected terminal stock price is $S_0 e^{(r-q)T}$ under $\mathbb{Q}$ versus $S_0 e^{\mu T}$ under $\mathbb{P}$.

    This is correct for pricing because the risk-neutral measure incorporates the market price of risk. Under $\mathbb{Q}$, the discounted stock price $e^{-(r-q)t}S_t$ is a martingale, so $e^{-rT}E^{\mathbb{Q}}[\text{payoff}]$ gives the arbitrage-free price. Using $\mathbb{P}$ instead would require knowing the market price of risk $\lambda = (\mu - r)/\sigma$, which is model-dependent and hard to estimate.

---

**Exercise 4.**
The code plots GBM paths with a final price distribution. Explain why the distribution is right-skewed (log-normal) and how this relates to the Black-Scholes model.

??? success "Solution to Exercise 4"
    The terminal price $S_T = S_0 e^X$ where $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$ follows a log-normal distribution. Log-normal distributions are right-skewed because the exponential function maps the symmetric normal onto a positive, asymmetric domain: values can be arbitrarily large but cannot go below zero.

    This is a fundamental assumption of Black-Scholes: stock prices are always positive, and log returns are normally distributed. The right skewness means large upward moves are possible (but rare), while the stock cannot lose more than 100%. The BS formula is derived by integrating the payoff against this log-normal distribution.
