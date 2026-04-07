# Implied Volatility and Market Quotes

!!! tip "Key Idea"
    Swaptions are not quoted by price, but by implied volatility. The Black formula is used in reverse to extract the volatility consistent with market prices.

---

## Market Quoting Convention

In practice, swaption markets do not quote prices directly. Instead, they quote:

- **Implied volatility** $\sigma_{\text{imp}}$
- For a given:
  - option expiry $T_m$
  - swap tenor $[T_m, T_n]$
  - strike $K$

A typical quote might be:

> "5Y × 10Y payer swaption: 20% vol"

This means:
- option expires in 5 years
- underlying is a 10-year swap starting in 5 years
- Black implied volatility is 20%

---

## From Price to Implied Volatility

Given a market price $V^{\text{mkt}}$, implied volatility is defined as the solution $\sigma$ to:

$$
V^{\text{mkt}} = N A(t)\, \text{Black}\bigl(S(t), K, \sigma, T_m - t\bigr)
$$

where:
- $S(t)$ is the forward swap rate
- $A(t)$ is the annuity

---

### Numerical Inversion

There is no closed-form solution for $\sigma_{\text{imp}}$. It is obtained by:

- Newton–Raphson method
- bisection
- or other root-finding algorithms

---

## Why Volatility Instead of Price?

There are several reasons why markets quote volatility:

---

### 1. Normalization

Prices depend on:

- notional $N$
- annuity $A(t)$

Volatility removes these scaling effects.

---

### 2. Comparability

Volatility allows comparison across:

- maturities
- tenors
- currencies

---

### 3. Stability

Prices can change due to:

- level of rates
- discounting

Volatility is more stable and reflects:

> **uncertainty of future rates**

---

## Volatility Surface

Implied volatility is not constant. It depends on:

- option expiry $T_m$
- swap tenor $[T_m, T_n]$
- strike $K$

This defines a **volatility surface**:

$$
\sigma_{\text{imp}} = \sigma(T_m, T_n, K)
$$

---

### Market Structure

Quotes are typically organized as:

- **ATM volatility** (at-the-money)
- **smile quotes**:
  - payer skew
  - receiver skew

---

## ATM Convention

At-the-money (ATM) swaptions are defined by:

$$
K = S_{m,n}(t)
$$

In this case, the Black formula simplifies, and ATM volatility is the most liquid quote.

---

## Normal vs Lognormal Volatility

Two conventions are used:

---

### Lognormal (Black) Volatility

- Assumes:

$$
dS = \sigma S\, dW
$$

- Used in Black swaption formula

---

### Normal (Bachelier) Volatility

- Assumes:

$$
dS = \sigma\, dW
$$

- Used in low or negative rate environments

---

!!! tip "Key Idea"
    Black volatility assumes rates are strictly positive, while normal volatility allows negative rates and is widely used in modern interest rate markets.

---

## Practical Interpretation

Implied volatility represents:

> the market's consensus uncertainty about future swap rates

It is not a direct measure of historical volatility, but a forward-looking quantity inferred from prices.

---

## Connection to Risk Management

Implied volatility is central to:

- hedging (vega exposure)
- model calibration
- risk reporting

---

## Bridge to Smile Models

The volatility surface is not flat. It exhibits patterns such as:

- skew
- smile

These patterns cannot be explained by the Black model alone.

They motivate more advanced models, such as:

- SABR
- stochastic volatility models

which we discuss next.

---

## Exercises

**Exercise 1.** A 5Y × 10Y payer swaption has a market price of $V^{\text{mkt}} = 0.0342$ (as a fraction of notional). The forward swap rate is $S = 0.045$, the annuity is $A = 7.82$, and the strike is $K = 0.045$ (ATM). Use the bisection method to find the Black implied volatility $\sigma_{\text{imp}}$. Search in the interval $[0.01, 1.00]$ and iterate until the absolute error is below $10^{-6}$.

??? success "Solution to Exercise 1"

    We seek $\sigma$ such that

    $$
    A \cdot \text{Black}(S, K, \sigma, T) = V^{\text{mkt}}
    $$

    where $T = 5$, $S = K = 0.045$, and $A = 7.82$.

    **Bisection algorithm:**

    1. Set $\sigma_{\text{lo}} = 0.01$, $\sigma_{\text{hi}} = 1.00$.
    2. Compute the midpoint $\sigma_{\text{mid}} = (\sigma_{\text{lo}} + \sigma_{\text{hi}}) / 2$.
    3. Evaluate $f(\sigma_{\text{mid}}) = A \cdot \text{Black}(S, K, \sigma_{\text{mid}}, T) - V^{\text{mkt}}$.
    4. If $f(\sigma_{\text{mid}}) > 0$, set $\sigma_{\text{hi}} = \sigma_{\text{mid}}$; otherwise set $\sigma_{\text{lo}} = \sigma_{\text{mid}}$.
    5. Repeat until $|\sigma_{\text{hi}} - \sigma_{\text{lo}}| < 10^{-6}$.

    Since $S = K$ (ATM), the Black formula simplifies to

    $$
    \text{Black}(S, K, \sigma, T) = S \bigl[2\Phi(\tfrac{1}{2}\sigma\sqrt{T}) - 1\bigr]
    $$

    Substituting $S = 0.045$ and $T = 5$, each bisection step halves the interval. Starting from an interval of width $0.99$, approximately $\lceil \log_2(0.99 / 10^{-6}) \rceil = 20$ iterations suffice.

    Running the bisection yields $\sigma_{\text{imp}} \approx 0.20$ (i.e., 20%), confirming the market quote.

---

**Exercise 2.** Explain why implied volatility is a more stable and useful quantity for quoting swaptions than the option price itself. In particular, address the roles of notional, annuity, and rate level.

??? success "Solution to Exercise 2"

    Swaption prices depend on several factors beyond the market's view of rate uncertainty:

    - **Notional $N$**: The price scales linearly with notional. Two traders looking at the same swaption but with different notionals see different prices for the same market condition.
    - **Annuity $A(t)$**: The annuity depends on the current discount curve and acts as a numeraire. As the yield curve shifts, the annuity changes, causing the price to move even if the market's uncertainty about rates has not changed.
    - **Rate level**: When rates are higher, the forward swap rate $S(t)$ is larger, and ATM option prices are mechanically larger in absolute terms.

    Implied volatility strips away all of these effects. By inverting the Black formula, we obtain a single number $\sigma_{\text{imp}}$ that reflects only the market's consensus on the magnitude of future rate fluctuations. This makes volatility:

    - **Comparable** across different maturities, tenors, and currencies.
    - **Stable** over time, changing only when the market's view of uncertainty changes, not when the curve shifts or notionals differ.
    - **Convenient** for interpolation and risk management, since volatility surfaces are smoother than price surfaces.

---

**Exercise 3.** A swaption has a Black (lognormal) implied volatility of $\sigma_{\text{LN}} = 0.20$ and the ATM forward swap rate is $S = 0.04$. Estimate the corresponding normal (Bachelier) implied volatility $\sigma_N$. State the approximation you use and explain when it breaks down.

??? success "Solution to Exercise 3"

    For ATM or near-ATM swaptions, the standard approximation relating lognormal and normal volatilities is

    $$
    \sigma_N \approx \sigma_{\text{LN}} \cdot S
    $$

    This follows from equating the instantaneous standard deviations of the two models:

    - Lognormal: $dS = \sigma_{\text{LN}} S\, dW$ gives instantaneous volatility $\sigma_{\text{LN}} S$.
    - Normal: $dS = \sigma_N\, dW$ gives instantaneous volatility $\sigma_N$.

    Setting them equal at the ATM level:

    $$
    \sigma_N = \sigma_{\text{LN}} \times S = 0.20 \times 0.04 = 0.008 = 80 \text{ bps}
    $$

    So the normal implied volatility is approximately 80 basis points.

    **When it breaks down:**

    - For deep out-of-the-money or in-the-money strikes, higher-order terms in the conversion become significant and the linear approximation is inaccurate.
    - When rates are very low or negative, the lognormal model itself is not well-defined (since $S$ must be positive), and the conversion formula loses meaning. In such environments, the normal model is used directly.

---

**Exercise 4.** Explain why the ATM (at-the-money) implied volatility is the most liquid quote in swaption markets, and describe how the volatility surface is constructed around it.

??? success "Solution to Exercise 4"

    **Why ATM is most liquid:**

    - **Hedging demand**: Most interest rate risk management involves hedging exposures near current market levels, so ATM swaptions are the most actively traded.
    - **Model independence**: At the money, the Black formula is least sensitive to model assumptions. The price depends primarily on the volatility parameter and is relatively insensitive to the exact distributional assumption (lognormal vs. normal vs. shifted lognormal), making ATM quotes robust across models.
    - **Simplicity**: At $K = S$, the Black formula simplifies significantly. The $d_1$ and $d_2$ terms become $\pm \tfrac{1}{2}\sigma\sqrt{T}$, making the relationship between price and volatility nearly linear for small volatilities. This makes ATM volatility easy to extract and interpret.
    - **Two-way markets**: Dealers quote tight bid-ask spreads for ATM swaptions because of high turnover and hedging flow, reinforcing liquidity.

    **Constructing the volatility surface around ATM:**

    1. The **ATM volatility matrix** is quoted as a grid indexed by option expiry $T_m$ (rows) and swap tenor $T_n - T_m$ (columns). For example, $\sigma_{\text{ATM}}(5\text{Y}, 10\text{Y}) = 20\%$.
    2. **Smile or skew quotes** are given as offsets from the ATM level for strikes away from the money. These are typically expressed as:
        - receiver spreads (strikes below ATM)
        - payer spreads (strikes above ATM)
    3. The full surface $\sigma(T_m, T_n, K)$ is built by interpolating the ATM grid across expiry and tenor, and adding the smile adjustments at each grid point.
    4. Advanced models such as SABR are calibrated to these smile quotes to provide a smooth, arbitrage-free interpolation across strikes.
