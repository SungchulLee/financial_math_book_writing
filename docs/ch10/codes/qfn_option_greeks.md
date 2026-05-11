# Option Greeks (qfn)

## Background

Option Greeks
=============

Exploration of the option Greeks (Delta, Gamma, Theta, Vega, Rho) under the
Black-Scholes model, with reference to Chapter 6 from *Option Volatility &
Pricing: Advanced Trading Strategies and Techniques* (Natenberg, 1994).

Each Greek is derived as a partial derivative of the option value with respect
to an underlying parameter (spot price, time, volatility, interest rate) and
is implemented here in closed form for European options.

Source
------
From the "quantitative-finance-notebooks" collection, notebook 4.6.

---

## Code

```python
"""
Option Greeks
=============

Exploration of the option Greeks (Delta, Gamma, Theta, Vega, Rho) under the
Black-Scholes model, with reference to Chapter 6 from *Option Volatility &
Pricing: Advanced Trading Strategies and Techniques* (Natenberg, 1994).

Each Greek is derived as a partial derivative of the option value with respect
to an underlying parameter (spot price, time, volatility, interest rate) and
is implemented here in closed form for European options.

Source
------
From the "quantitative-finance-notebooks" collection, notebook 4.6.
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import numpy as np
import scipy.stats as ss

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    S0 = 100.0      # spot price
    K = 100.0       # strike price
    T = 1.0         # time to expiration (in years)
    r = 0.04        # annual risk-free rate
    sigma = 0.2     # annual volatility rate


    # ===================================================================
    # 1. The Greeks
    # ===================================================================
    #
    # In mathematical finance, the Greeks are the quantities (known in
    # calculus as partial derivatives; first-order or higher) representing
    # the sensitivity of the price of a derivative instrument such as an
    # option to changes in one or more underlying parameters on which the
    # value of an instrument or portfolio of financial instruments is
    # dependent.
    # ===================================================================

    # ---------------------------------------------------------------------------
    # Black-Scholes closed-form price
    # ---------------------------------------------------------------------------
    def closed_formula(S0, K, T, r, sigma, payoff='call'):
        d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        if payoff == 'call':
            return S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)
        elif payoff == 'put':
            return K * np.exp(-r * T) * ss.norm.cdf(-d2) - S0 * ss.norm.cdf(-d1)


    # Calculate option prices using the Black-Scholes closed formula
    call = closed_formula(S0, K, T, r, sigma, 'call')
    put = closed_formula(S0, K, T, r, sigma, 'put')

    print(f"Call price: {call:.3f}")
    print(f"Put price: {put:.3f}")


    # ===================================================================
    # 1.1 Delta
    # ===================================================================
    #
    # Delta is the first derivative of the option value V with respect to
    # the underlying asset price S:
    #
    #   Delta = dV / dS
    #
    # For European options under Black-Scholes:
    #
    #   Delta_call = N(d1)
    #   Delta_put  = N(d1) - 1
    #
    # The delta of a call is bounded in [0, 1].  A delta of 1.00 means
    # the option moves point-for-point with the underlying.  A call with
    # delta 0.25 changes value at 25% of the rate of the underlying.
    #
    # Puts always have negative deltas (range from 0.00 for far OTM to
    # -1.00 for deeply ITM) because put values move in the opposite
    # direction of the underlying market.
    #
    # Delta also tells us the proper hedge ratio: the ratio of the
    # position in the underlying asset to options required to establish a
    # neutral hedge.
    #
    # As a rough approximation, the delta equals the probability that the
    # option will finish in-the-money.
    # ===================================================================

    def calculate_delta(S0, K, T, r, sigma, payoff='call'):
        d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        if payoff.lower() == 'call':
            return ss.norm.cdf(d1)
        elif payoff.lower() == 'put':
            return ss.norm.cdf(d1) - 1


    # Calculate option delta
    call_delta = calculate_delta(S0, K, T, r, sigma, payoff='call')
    put_delta = calculate_delta(S0, K, T, r, sigma, payoff='put')

    print(f"Call Delta: {call_delta:.3f}")
    print(f"Put Delta: {put_delta:.3f}")


    # ===================================================================
    # 1.2 Gamma
    # ===================================================================
    #
    # Gamma is the rate at which an option's delta changes as the price
    # of the underlying changes (the second derivative of V w.r.t. S):
    #
    #   Gamma = d(Delta) / dS = d^2 V / dS^2
    #
    # For European options under Black-Scholes:
    #
    #   Gamma = N'(d1) / (S0 * sigma * sqrt(T))
    #
    # Gamma is usually expressed in deltas gained or lost per one-point
    # change in the underlying.  The delta increases by gamma when the
    # underlying rises and decreases by gamma when it falls.
    #
    # Long options (calls or puts) have positive gamma; short options
    # have negative gamma.  A large gamma indicates high risk.
    #
    # Gamma is greatest for at-the-money options and becomes
    # progressively smaller as the option moves into- or out-of-the-money.
    # ===================================================================

    def calculate_gamma(S0, K, T, r, sigma):
        d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        return ss.norm.pdf(d1) / (S0 * sigma * np.sqrt(T))


    # Calculate option gamma
    call_gamma = calculate_gamma(S0, K, T, r, sigma)
    put_gamma = calculate_gamma(S0, K, T, r, sigma)

    print(f"Call Gamma: {call_gamma:.3f}")
    print(f"Put Gamma: {put_gamma:.3f}")


    # ===================================================================
    # 1.3 Theta
    # ===================================================================
    #
    # Theta is the rate at which an option loses value as time passes:
    #
    #   Theta = -dV / d(tau)
    #
    # For European options under Black-Scholes:
    #
    #   Theta_call = -S0 N'(d1) sigma / (2 sqrt(T)) - r K e^{-rT} N(d2)
    #   Theta_put  = -S0 N'(d1) sigma / (2 sqrt(T)) + r K e^{-rT} N(-d2)
    #
    # Theta here is computed per year; dividing by 365 gives theta per
    # day.  It is usually expressed in points lost per day when all other
    # conditions remain the same.
    #
    # Theta is written as a negative number to remind us that time runs
    # in only one direction.
    #
    # As a general principle, gamma and theta have opposite signs.  Every
    # option position is a tradeoff between market movement (gamma) and
    # time decay (theta).
    # ===================================================================

    def calculate_theta(S0, K, T, r, sigma, payoff='call'):
        d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        if payoff == 'call':
            return (-S0 * ss.norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                    - r * K * np.exp(-r * T) * ss.norm.cdf(d2)) / 365.0
        elif payoff == 'put':
            return (-S0 * ss.norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                    + r * K * np.exp(-r * T) * ss.norm.cdf(-d2)) / 365.0


    # Calculate option theta
    call_theta = calculate_theta(S0, K, T, r, sigma, payoff='call')
    put_theta = calculate_theta(S0, K, T, r, sigma, payoff='put')

    print(f"Call Theta: {call_theta:.3f}")
    print(f"Put Theta: {put_theta:.3f}")


    # ===================================================================
    # 1.4 Vega
    # ===================================================================
    #
    # Vega is the derivative of the option value with respect to the
    # volatility of the underlying asset price:
    #
    #   Vega = dV / d(sigma)
    #
    # For European options under Black-Scholes:
    #
    #   Vega = S0 sqrt(T) N'(d1)
    #
    # All options gain value with rising volatility, so vega is positive
    # for both calls and puts.  If an option has a vega of 0.15, for each
    # percentage point increase (decrease) in volatility the option gains
    # (loses) 0.15 in value.
    # ===================================================================

    def calculate_vega(S0, K, T, r, sigma):
        d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        return (S0 * np.sqrt(T) * ss.norm.pdf(d1)) / 100


    # Calculate option vega
    call_vega = calculate_vega(S0, K, T, r, sigma)
    put_vega = calculate_vega(S0, K, T, r, sigma)

    print(f"Call Vega: {call_vega:.3f}")
    print(f"Put Vega: {put_vega:.3f}")


    # ===================================================================
    # 1.5 Rho
    # ===================================================================
    #
    # Rho measures the sensitivity of an option's value to a change in
    # interest rates:
    #
    #   rho = dV / dr
    #
    # For European options under Black-Scholes:
    #
    #   rho_call =  K T e^{-rT} N(d2)
    #   rho_put  = -K T e^{-rT} N(-d2)
    #
    # Unlike the other Greeks, one cannot generalise about rho since its
    # characteristics depend on the type of underlying instrument and the
    # settlement procedure for the options.
    #
    # A call can be thought of as a substitute for purchasing the
    # underlying stock.  Rising interest rates make the call more
    # attractive (lower carrying cost vs outright purchase), so call
    # values increase.
    #
    # Conversely, selling stock becomes more attractive than buying a put
    # in a high-rate environment (the cash credit earns greater interest),
    # so rising rates cause put values to fall.
    # ===================================================================

    def calculate_rho(S0, K, T, r, sigma, payoff='call'):
        d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        if payoff == 'call':
            return (K * T * np.exp(-r * T) * ss.norm.cdf(d2)) / 100
        elif payoff == 'put':
            return (-K * T * np.exp(-r * T) * ss.norm.cdf(-d2)) / 100


    # Calculate option rho
    call_rho = calculate_rho(S0, K, T, r, sigma, payoff='call')
    put_rho = calculate_rho(S0, K, T, r, sigma, payoff='put')

    print(f"Call Rho: {call_rho:.3f}")
    print(f"Put Rho: {put_rho:.3f}")
```


## Exercises

**Exercise 1.**
Delta can be interpreted as the probability of finishing ITM (approximately). For $S_0 = K = 100$, $T = 1$, $r = 0.04$, $\sigma = 0.2$, compute call delta and explain why it exceeds the true risk-neutral probability $N(d_2)$.

??? success "Solution to Exercise 1"
    $d_1 = (0 + 0.06)/0.2 = 0.3$. Delta $= N(0.3) = 0.6179$. The risk-neutral probability is $N(d_2) = N(0.1) = 0.5398$. Delta exceeds $N(d_2)$ because delta is the probability under the stock-price measure, which tilts the distribution upward. The relationship is $\Delta = e^{qT}N(d_1)$ vs $\Pr(S_T > K) = N(d_2)$, and $d_1 > d_2$ always.

---

**Exercise 2.**
Compute vega for the same parameters. If implied volatility increases from 20% to 22%, estimate the change in call price.

??? success "Solution to Exercise 2"
    Vega $= S_0\sqrt{T} \cdot n(d_1) / 100 = 100 \cdot 1 \cdot 0.3814 / 100 = 0.3814$ per 1% vol change. For a 2% increase: $\Delta C \approx 2 \times 0.3814 = \$0.763$. Note that vega is typically quoted per 1% (not per 100%) volatility change, so this is the dollar change in the option price.

---

**Exercise 3.**
Rho for a call is $\rho_C = KTe^{-rT}N(d_2)/100$. Explain why rho is relatively small for short-dated options.

??? success "Solution to Exercise 3"
    Rho is proportional to $T$: $\rho_C = KTe^{-rT}N(d_2)/100$. For $T = 0.25$ (3 months): $\rho_C = 100(0.25)(0.99)(0.54)/100 = 0.134$. For $T = 5$ years: $\rho_C = 100(5)(0.82)(0.54)/100 = 2.21$. The factor $T$ makes rho negligible for short-dated options because a small change in $r$ affects the discounting by only $rT$, which is tiny for small $T$.

---

**Exercise 4.**
The gamma-theta relationship implies $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma \approx rV$ for delta-neutral portfolios. Verify this numerically for the given parameters.

??? success "Solution to Exercise 4"
    $\Gamma = n(d_1)/(S\sigma\sqrt{T}) = 0.3814/(100 \times 0.2) = 0.01907$. $\frac{1}{2}\sigma^2 S^2 \Gamma = 0.5(0.04)(10000)(0.01907) = 3.814$. $\Theta_{\text{call}} \approx -Sn(d_1)\sigma/(2\sqrt{T}) - rKe^{-rT}N(d_2) = -3.814 - 0.04(96.08)(0.54) = -3.814 - 2.075 = -5.889$. $rV = 0.04 \times 10.45 = 0.418$. Check: $-5.889 + 3.814 + r \cdot S \cdot \Delta = -5.889 + 3.814 + 0.04(100)(0.618) = -5.889 + 3.814 + 2.472 = 0.397 \approx 0.418$. Close (rounding).