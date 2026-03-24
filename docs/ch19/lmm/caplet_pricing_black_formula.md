# Caplet Pricing and Black's Formula

The caplet is the fundamental building block of the interest rate cap market. In the LIBOR Market Model, each forward LIBOR rate is a martingale under its natural forward measure, and its lognormal dynamics lead directly to **Black's formula** for caplet prices. This section derives the formula from first principles, explains the relationship between caplets and caps, and covers the market conventions for quoting implied volatilities.

---

## Caplet Payoff and Market Convention

### Definition

A **caplet** on the forward rate $L_i(t)$ for the accrual period $[T_i, T_{i+1}]$ with strike $K$ pays

$$
\delta_i \max(L_i(T_i) - K, 0)
$$

at time $T_{i+1}$, where $\delta_i = T_{i+1} - T_i$ is the day count fraction and $L_i(T_i)$ is the LIBOR rate observed (fixed) at $T_i$.

### Caps as Portfolios of Caplets

An interest rate **cap** with tenor $[T_0, T_n]$ and strike $K$ is a portfolio of caplets:

$$
\text{Cap} = \sum_{i=0}^{n-1} \text{Caplet}_i
$$

Each caplet protects the holder against the rate $L_i(T_i)$ exceeding $K$ during the corresponding accrual period. Similarly, a **floor** is a portfolio of **floorlets**, each paying $\delta_i \max(K - L_i(T_i), 0)$ at $T_{i+1}$.

### Cap--Floor Parity

$$
\text{Cap}(K) - \text{Floor}(K) = \text{Payer Swap}(K)
$$

This follows from $\max(L - K, 0) - \max(K - L, 0) = L - K$.

---

## Forward LIBOR Dynamics

### The Natural Measure for Caplet Pricing

The forward LIBOR rate $L_i(t)$ for period $[T_i, T_{i+1}]$ is defined by

$$
L_i(t) = \frac{1}{\delta_i}\left(\frac{P(t, T_i)}{P(t, T_{i+1})} - 1\right)
$$

Under the $T_{i+1}$-forward measure $\mathbb{Q}^{T_{i+1}}$ (numéraire $P(t, T_{i+1})$), the forward rate $L_i(t)$ is a **martingale**. This follows because $\delta_i L_i(t) P(t, T_{i+1}) = P(t, T_i) - P(t, T_{i+1})$ is the price of a tradable portfolio, so dividing by the numéraire $P(t, T_{i+1})$ produces a martingale.

### Lognormal Dynamics

In the standard LIBOR Market Model, the forward rate follows geometric Brownian motion under $\mathbb{Q}^{T_{i+1}}$:

$$
\frac{dL_i(t)}{L_i(t)} = \sigma_i(t) \, dW_i^{T_{i+1}}(t)
$$

where $\sigma_i(t)$ is the instantaneous volatility of $L_i$ and $W_i^{T_{i+1}}$ is a Brownian motion under $\mathbb{Q}^{T_{i+1}}$. The drift is zero because $L_i$ is a martingale.

### Solution

Integrating the SDE:

$$
L_i(T_i) = L_i(0) \exp\!\left(-\frac{1}{2}\int_0^{T_i} \sigma_i(t)^2 \, dt + \int_0^{T_i} \sigma_i(t) \, dW_i^{T_{i+1}}(t)\right)
$$

The terminal rate $L_i(T_i)$ is **lognormally distributed** under $\mathbb{Q}^{T_{i+1}}$:

$$
\ln L_i(T_i) \sim N\!\left(\ln L_i(0) - \frac{1}{2} v_i^2, \; v_i^2\right)
$$

where the **integrated variance** is

$$
v_i^2 = \int_0^{T_i} \sigma_i(t)^2 \, dt
$$

---

## Derivation of Black's Formula

### Caplet Pricing Under the Forward Measure

The caplet price at time $0$ is

$$
\text{Caplet}_i = P(0, T_{i+1}) \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[\delta_i \max(L_i(T_i) - K, 0)\right]
$$

The factor $P(0, T_{i+1})$ comes from the numéraire change: $V_0 = P(0, T_{i+1}) \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[V_{T_{i+1}} / P(T_{i+1}, T_{i+1})]$ with $P(T_{i+1}, T_{i+1}) = 1$.

### Evaluating the Expectation

Since $L_i(T_i)$ is lognormal under $\mathbb{Q}^{T_{i+1}}$ with $\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)] = L_i(0)$ (martingale property), the expectation of $\max(L_i(T_i) - K, 0)$ is computed by the standard Black--Scholes lognormal integral:

$$
\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[\max(L_i(T_i) - K, 0)\right] = L_i(0) \, N(d_1) - K \, N(d_2)
$$

where $N(\cdot)$ is the standard normal CDF and

$$
d_1 = \frac{\ln(L_i(0)/K) + \tfrac{1}{2} v_i^2}{v_i}, \qquad d_2 = d_1 - v_i
$$

### Black's Caplet Formula

$$
\boxed{\text{Caplet}_i = \delta_i \, P(0, T_{i+1}) \bigl[L_i(0) \, N(d_1) - K \, N(d_2)\bigr]}
$$

This is **Black's formula** (1976) applied to caplets. The key insight is that the forward measure eliminates the stochastic discount factor, and the lognormal martingale property of $L_i$ produces the Black--Scholes--type result directly.

### Floorlet Formula

By analogous reasoning (or by put--call parity):

$$
\text{Floorlet}_i = \delta_i \, P(0, T_{i+1}) \bigl[K \, N(-d_2) - L_i(0) \, N(-d_1)\bigr]
$$

---

## Implied Volatility

### Black Implied Volatility

The **Black implied volatility** $\sigma_i^{\text{Black}}$ is the constant volatility that, when substituted into Black's formula, reproduces the market caplet price:

$$
v_i = \sigma_i^{\text{Black}} \sqrt{T_i}
$$

For constant instantaneous volatility $\sigma_i(t) = \sigma_i$, the Black implied volatility equals the instantaneous volatility: $\sigma_i^{\text{Black}} = \sigma_i$.

For time-dependent volatility, the Black implied volatility is an average:

$$
\sigma_i^{\text{Black}} = \sqrt{\frac{1}{T_i} \int_0^{T_i} \sigma_i(t)^2 \, dt}
$$

### Flat Volatility vs. Spot Volatility

Markets quote cap prices using two volatility conventions:

- **Flat (cap) volatility** $\sigma^{\text{flat}}$: A single volatility applied to all caplets within the cap, chosen so that the resulting cap price matches the market
- **Spot (caplet) volatility** $\sigma_i^{\text{spot}}$: The individual Black implied volatility for each caplet

The flat volatility is the market quote convention; spot volatilities are extracted by **bootstrapping** (stripping) the cap curve.

### Stripping Caplet Volatilities

Given cap prices $C_1, C_2, \ldots$ for increasing maturities:

1. The first cap (single caplet) directly gives $\sigma_1^{\text{spot}}$
2. For cap with maturity $T_{k+1}$: solve for $\sigma_k^{\text{spot}}$ from

$$
C_k = \sum_{i=0}^{k-1} \text{Caplet}_i(\sigma_i^{\text{spot}})
$$

where all $\sigma_i^{\text{spot}}$ for $i < k$ are already known.

This is a **sequential bootstrap** procedure, analogous to yield curve stripping.

---

## Worked Example

??? example "Caplet Pricing Calculation"

    **Parameters:**

    - $T_i = 1.0$ (fixing date), $T_{i+1} = 1.25$ (payment date), $\delta_i = 0.25$
    - Forward rate: $L_i(0) = 5.0\% = 0.05$
    - Strike: $K = 4.5\% = 0.045$
    - Black implied vol: $\sigma_i^{\text{Black}} = 20\%$
    - Discount factor: $P(0, 1.25) = 0.9388$
    - Notional: \$1,000,000

    **Step 1:** Integrated volatility: $v_i = 0.20 \times \sqrt{1.0} = 0.20$.

    **Step 2:** $d_1 = [\ln(0.05/0.045) + 0.5 \times 0.04] / 0.20 = [0.10536 + 0.02] / 0.20 = 0.6268$.

    **Step 3:** $d_2 = 0.6268 - 0.20 = 0.4268$.

    **Step 4:** $N(0.6268) = 0.7346$, $N(0.4268) = 0.6653$.

    **Step 5:** $\text{Caplet} = 0.25 \times 0.9388 \times [0.05 \times 0.7346 - 0.045 \times 0.6653]$.

    **Step 6:** $= 0.2347 \times [0.03673 - 0.02994] = 0.2347 \times 0.00679 = 0.001594$.

    **Result:** The caplet is worth 0.1594% of notional, or \$1,594 per \$1,000,000.

---

## Volatility Smile and Extensions

### Limitations of Black's Formula

Black's formula assumes lognormal forward rates, which implies:

- **No volatility smile/skew:** All strikes have the same implied volatility
- **Non-negative rates:** $L_i(T_i) > 0$ almost surely

Market data shows both a volatility smile (OTM caplets trade at higher implied vol than ATM) and, since 2014, negative LIBOR/EURIBOR rates in some currencies.

### SABR Model for Caplets

The SABR model extends the dynamics:

$$
dL_i = \alpha_i L_i^{\beta} \, dW_1, \qquad d\alpha_i = \nu \alpha_i \, dW_2, \qquad dW_1 \cdot dW_2 = \rho \, dt
$$

with $0 \leq \beta \leq 1$. The Hagan et al. approximation provides an analytical formula for the implied volatility as a function of strike, capturing smile and skew.

### Normal (Bachelier) Model

For negative rate environments, the Bachelier model assumes normal (rather than lognormal) dynamics:

$$
dL_i(t) = \sigma_i^{(n)} \, dW_i^{T_{i+1}}(t)
$$

The Bachelier caplet formula is

$$
\text{Caplet}_i = \delta_i \, P(0, T_{i+1}) \bigl[(L_i(0) - K) \, N(d) + \sigma_i^{(n)} \sqrt{T_i} \, \phi(d)\bigr]
$$

where $d = (L_i(0) - K) / (\sigma_i^{(n)} \sqrt{T_i})$ and $\phi(\cdot)$ is the standard normal PDF.

---

## Greeks for Caplets

### Delta

$$
\Delta_i = \frac{\partial \, \text{Caplet}_i}{\partial L_i(0)} = \delta_i \, P(0, T_{i+1}) \, N(d_1)
$$

### Vega

$$
\mathcal{V}_i = \frac{\partial \, \text{Caplet}_i}{\partial \sigma_i^{\text{Black}}} = \delta_i \, P(0, T_{i+1}) \, L_i(0) \, \sqrt{T_i} \, \phi(d_1)
$$

### Gamma

$$
\Gamma_i = \frac{\partial^2 \, \text{Caplet}_i}{\partial L_i(0)^2} = \delta_i \, P(0, T_{i+1}) \, \frac{\phi(d_1)}{L_i(0) \, v_i}
$$

---

## Key Takeaways

- Under the $T_{i+1}$-forward measure, the forward LIBOR rate $L_i(t)$ is a martingale with lognormal dynamics
- **Black's caplet formula:** $\text{Caplet}_i = \delta_i P(0,T_{i+1})[L_i(0)N(d_1) - KN(d_2)]$, with $d_1, d_2$ depending on the integrated variance $v_i^2 = \int_0^{T_i} \sigma_i^2\,dt$
- The formula is exact in the LMM (not an approximation) because each caplet depends on a single forward rate under its natural measure
- **Flat cap volatility** is the market quote convention; **spot caplet volatility** is extracted by bootstrapping
- Extensions (SABR, Bachelier) handle the smile/skew and negative rates that the basic lognormal model cannot capture

---

## Further Reading

- Black (1976), "The Pricing of Commodity Contracts"
- Brace, Gatarek & Musiela (1997), "The Market Model of Interest Rate Dynamics"
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 6
- Hagan et al. (2002), "Managing Smile Risk" (SABR model)

---

## Exercises

**Exercise 1.** A caplet on 3-month LIBOR has the following parameters: $L_i(0) = 3.8\%$, $K = 4.0\%$, $\sigma_i^{\text{Black}} = 24\%$, $T_i = 2$ years, $\delta_i = 0.25$, and $P(0, T_{i+1}) = 0.925$. Compute $d_1$, $d_2$, and the caplet price. Is this caplet in-the-money or out-of-the-money?

---

**Exercise 2.** The market quotes flat cap volatilities for 2Y, 3Y, and 5Y caps as 19.5%, 20.2%, and 21.0% respectively, with annual caplets. Describe the bootstrapping procedure to extract spot caplet volatilities from these flat cap quotes. If the 2Y caplet vol is 19.5%, what equation determines the 3Y spot caplet vol?

---

**Exercise 3.** Show that in the LMM, the Black caplet formula is exact (not an approximation). Specifically, explain why the forward rate $L_i(t)$ is exactly lognormal under $\mathbb{Q}^{T_{i+1}}$, even though $L_i(t)$ interacts with other forward rates under the terminal measure. What property of the $T_{i+1}$-forward measure makes this possible?

---

**Exercise 4.** Derive the caplet vega $\mathcal{V}_i = \delta_i P(0, T_{i+1}) L_i(0) \sqrt{T_i}\,\phi(d_1)$ by differentiating the Black caplet formula with respect to $\sigma_i^{\text{Black}}$. Use this to estimate the price change of the caplet in Exercise 1 if the volatility increases by 1 percentage point (from 24% to 25%).

---

**Exercise 5.** Put-call parity for caplets and floorlets states that $\text{Caplet} - \text{Floorlet} = \delta_i P(0, T_{i+1})(L_i(0) - K)$. Verify this identity algebraically using the Black formulas for caplets and floorlets. Then compute the floorlet price corresponding to Exercise 1.

---

**Exercise 6.** A trader observes that the ATM caplet implied volatility for 1-year expiry is 18% while the 10-year expiry is 24%. The forward rates are roughly constant at 4%. Compare the caplet prices per unit notional and per basis point of vega at the two maturities. Which caplet is more sensitive to volatility changes in absolute terms?

---

**Exercise 7.** The SABR model extends Black's formula to capture the volatility smile. In the SABR framework, the ATM Black volatility is approximately $\sigma^{\text{Black}}(K = F) \approx \alpha / F^{1-\beta}$, where $\alpha$ is the initial stochastic vol level and $\beta$ controls the backbone. For $\beta = 0.5$, $\alpha = 0.03$, and $F = 4\%$, compute the approximate ATM Black vol. How does this compare to the Bachelier (normal) vol $\sigma_N \approx \alpha\,F^\beta$?
