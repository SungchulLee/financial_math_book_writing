# Swaptions

A **swaption** is an option to enter into an interest rate swap at a future date. Swaptions are among the most liquid interest rate derivatives and serve as primary calibration instruments for term structure models.

---

## Definitions

### Payer Swaption

A **payer swaption** gives the holder the right (but not obligation) to enter into a **payer swap** (pay fixed, receive floating) at a future date.

**Specification:**
- **Expiry:** $T_0$ (option maturity)
- **Underlying swap:** Start at $T_0$, payments at $T_1, \ldots, T_n$
- **Strike:** $K$ (fixed rate)
- **Notional:** $N$

**Payoff at expiry $T_0$:**

$$
\max\left(\text{Value of payer swap at } T_0, 0\right) = \max\left(\sum_{i=1}^{n} \delta_i P(T_0, T_i)(S_{T_0} - K), 0\right)
$$

where $S_{T_0}$ is the swap rate prevailing at $T_0$.

Simplified:

$$
\text{Payoff} = A(T_0) \cdot \max(S_{T_0} - K, 0)
$$

where $A(T_0) = \sum_{i=1}^{n} \delta_i P(T_0, T_i)$ is the **swap annuity**.

### Receiver Swaption

A **receiver swaption** gives the right to enter a **receiver swap** (receive fixed, pay floating):

$$
\text{Payoff} = A(T_0) \cdot \max(K - S_{T_0}, 0)
$$

### Put-Call Parity

$$
\text{Payer Swaption} - \text{Receiver Swaption} = \text{Forward Swap}
$$

The forward swap has zero value when $K$ equals the forward swap rate $S_0$.

---

## Notation and Conventions

### Swaption Naming

"$m \times n$" swaption means:
- $m$ years to expiry
- $n$ years swap tenor

Example: "5y × 10y" = option expiring in 5 years on a 10-year swap

### The Swap Rate

The **forward swap rate** observed at time $t$ for a swap starting at $T_0$ is:

$$
S(t; T_0, T_n) = \frac{P(t, T_0) - P(t, T_n)}{\sum_{i=1}^{n} \delta_i P(t, T_i)}
$$

At time 0:

$$
S_0 = S(0; T_0, T_n) = \frac{P(0, T_0) - P(0, T_n)}{A_0}
$$

where $A_0 = \sum_{i=1}^{n} \delta_i P(0, T_i)$ is the **present value of the annuity**.

---

## Black's Model for Swaptions

### Model Assumption

Under the **annuity (swap) measure** $\mathbb{Q}^A$, the forward swap rate is a **martingale** with lognormal dynamics:

$$
\frac{dS_t}{S_t} = \sigma \, dW_t^A
$$

where $\sigma$ is the **swaption volatility**.

### Change of Numéraire

The annuity $A(t)$ serves as the numéraire. Under $\mathbb{Q}^A$:

$$
\text{Swaption Value} = A_0 \cdot \mathbb{E}^{\mathbb{Q}^A}[\max(S_{T_0} - K, 0)]
$$

Since $S_{T_0}$ is lognormal under $\mathbb{Q}^A$, this is a standard Black-Scholes expectation.

### Black's Formula (Payer Swaption)

$$
\boxed{\text{Payer Swaption} = A_0 \cdot [S_0 N(d_1) - K N(d_2)]}
$$

where:

$$
d_1 = \frac{\ln(S_0/K) + \frac{1}{2}\sigma^2 T_0}{\sigma \sqrt{T_0}}
$$

$$
d_2 = d_1 - \sigma \sqrt{T_0}
$$

### Receiver Swaption

$$
\text{Receiver Swaption} = A_0 \cdot [K N(-d_2) - S_0 N(-d_1)]
$$

### ATM Swaption

When $K = S_0$ (at-the-money forward):

$$
\text{ATM Swaption} \approx A_0 \cdot S_0 \cdot \sigma \sqrt{T_0} \cdot \sqrt{\frac{2}{\pi}}
$$

using the approximation $N(d_1) - N(d_2) \approx \sigma\sqrt{T}/\sqrt{2\pi}$ for small $\sigma\sqrt{T}$.

---

## Swaption Pricing in Short-Rate Models

### Jamshidian's Trick

In one-factor models (Vasicek, Hull-White, CIR), bond prices are monotonic in the short rate $r$.

**Key insight:** There exists a unique $r^*$ such that the swap value equals zero:

$$
\sum_{i=1}^{n} c_i P(T_0, T_i, r^*) = P(T_0, T_0, r^*) = 1
$$

where $c_i = K \delta_i$ for $i < n$ and $c_n = 1 + K \delta_n$.

### Decomposition

The payer swaption decomposes into:

$$
\text{Payer Swaption} = \sum_{i=1}^{n} c_i \cdot \text{Put}(P(T_0, T_i), K_i)
$$

where $K_i = P(T_0, T_i, r^*)$.

Each put option has an analytical formula (in Vasicek/Hull-White/CIR), so the swaption price is semi-analytical.

### Algorithm

1. **Find $r^*$:** Solve $\sum_i c_i P(T_0, T_i, r^*) = 1$ via root-finding
2. **Compute strikes:** $K_i = P(T_0, T_i, r^*)$
3. **Price puts:** Use bond option formulas
4. **Sum:** Swaption price = $\sum_i c_i \cdot \text{Put}_i$

---

## Normal (Bachelier) Model

### Motivation

For low or negative rates, lognormal models break down. The Bachelier model assumes:

$$
dS_t = \sigma^{(n)} \, dW_t^A
$$

### Bachelier Swaption Formula

$$
\text{Payer Swaption} = A_0 \cdot \left[(S_0 - K) N(d) + \sigma^{(n)} \sqrt{T_0} \phi(d)\right]
$$

where:

$$
d = \frac{S_0 - K}{\sigma^{(n)} \sqrt{T_0}}
$$

### Conversion (ATM Approximation)

$$
\sigma^{(n)} \approx S_0 \cdot \sigma^{(\text{Black})}
$$

---

## Swaption Volatility Cube

### Structure

The swaption market quotes volatilities across three dimensions:

1. **Expiry:** Option maturity ($T_0$)
2. **Tenor:** Underlying swap length ($T_n - T_0$)
3. **Strike:** Moneyness (ATM, ITM, OTM)

### The Volatility Cube

$$
\sigma = \sigma(\text{expiry}, \text{tenor}, \text{strike})
$$

### Typical Features

- **Smile:** OTM puts and calls have higher vol than ATM
- **Skew:** Asymmetry between payer and receiver wings
- **Term structure:** Vol may increase or decrease with expiry
- **Tenor effect:** Longer swaps may have different vol dynamics

---

## Calibration to Swaptions

### Market Data

Standard quotes include:
- ATM swaption volatilities (expiry × tenor grid)
- Sometimes smile data (multiple strikes)

### Calibration Approaches

**For Black's model:**
- Direct use of market vols
- Interpolation/extrapolation for missing points

**For short-rate models (Hull-White):**
- Fit $\kappa$ and $\sigma$ (or $\sigma(t)$) to swaption grid
- Often done jointly with caps

**For multi-factor models:**
- More parameters allow better smile fit
- Risk of overfitting

### Joint Calibration

Calibrate to both caps and swaptions:

$$
\min_{\theta} \sum_{\text{caps}} w_c (C^{\text{model}} - C^{\text{mkt}})^2 + \sum_{\text{swaptions}} w_s (S^{\text{model}} - S^{\text{mkt}})^2
$$

---

## Greeks for Swaptions

### Delta

Sensitivity to the forward swap rate:

$$
\Delta = A_0 \cdot N(d_1)
$$

### Vega

Sensitivity to volatility:

$$
\mathcal{V} = A_0 \cdot S_0 \sqrt{T_0} \phi(d_1)
$$

### Gamma

$$
\Gamma = \frac{A_0 \phi(d_1)}{S_0 \sigma \sqrt{T_0}}
$$

### Annuity Delta

Sensitivity to shifts in the discount curve (affects $A_0$):

$$
\frac{\partial V}{\partial A_0} = S_0 N(d_1) - K N(d_2)
$$

---

## Physical vs. Cash Settlement

### Physical Settlement

At expiry, the holder physically enters the underlying swap. Most common for longer-dated swaptions.

### Cash Settlement

At expiry, the holder receives cash equal to the swap value, typically using a standardized formula based on the prevailing swap rate.

**Cash settlement amount:**

$$
\text{Cash} = A_{\text{ref}} \cdot \max(S_{T_0} - K, 0)
$$

where $A_{\text{ref}}$ is computed using a reference curve (often ISDA methodology).

### Difference

Cash and physical settlement can produce different values due to:
- Annuity computation differences
- Exercise timing
- Basis risk

---

## Bermudan Swaptions

### Definition

A **Bermudan swaption** allows exercise on multiple dates (e.g., each reset date of the underlying swap).

### Valuation

Bermudan swaptions require numerical methods:
- **Trees:** Backward induction with early exercise check
- **Monte Carlo:** American/Bermudan methods (Longstaff-Schwartz)
- **PDE:** With multiple exercise boundaries

### Relationship to European

$$
\text{Bermudan} \geq \text{European}
$$

The early exercise premium is typically 5-20 bps on implied vol for typical structures.

---

## Practical Considerations

### Liquidity

| Structure | Liquidity |
|-----------|-----------|
| ATM 1y×1y to 10y×10y | Very liquid |
| ATM 20y×20y, 30y×30y | Less liquid |
| OTM/ITM swaptions | Moderate to low |
| Bermudan | OTC, less standardized |

### Hedging

- **Delta hedge:** Pay/receive swaps
- **Vega hedge:** Other swaptions
- **Gamma hedge:** Dynamic rebalancing

### Model Risk

- One-factor models underestimate correlation across maturities
- Smile models (SABR) needed for accurate OTM pricing
- Bermudan exercise boundaries depend on model choice

---

## Connection to Caps

### Caplet vs. Swaption

| Feature | Caplet | Swaption |
|---------|--------|----------|
| Underlying | Single forward rate | Swap rate (basket of forwards) |
| Measure | $T$-forward | Annuity |
| Correlation | N/A (single rate) | Implicit (bundled forwards) |
| Liquidity | Via caps | Direct |

### Arbitrage Bounds

Swaptions and caps are connected via correlation:
- Perfect correlation: swaption vol ≈ cap vol
- Imperfect correlation: swaption vol < cap vol

---

## Key Takeaways

- Swaption = option on interest rate swap
- Payer swaption: $A_0 \cdot [S_0 N(d_1) - K N(d_2)]$
- Annuity measure: swap rate is martingale
- Jamshidian decomposition: swaption = portfolio of bond puts
- Swaption cube: vol varies with expiry, tenor, strike
- Cash vs. physical settlement matters
- Calibration: primary instrument for term structure models

---

## Further Reading

- Black (1976), "The Pricing of Commodity Contracts"
- Jamshidian (1997), "LIBOR and Swap Market Models"
- Brigo & Mercurio, *Interest Rate Models*, Chapters 6-7
- Rebonato, *Modern Pricing of Interest-Rate Derivatives*

---

## Exercises

**Exercise 1.** Price a 2Y-into-3Y ATM payer swaption using Black's formula. The current forward swap rate is $S_0 = 4.5\%$, the swaption volatility is $\sigma = 18\%$, and the present value of the annuity is $A_0 = 2.72$ (with annual payments and discount factors consistent with a flat 4.5\% curve). Verify put-call parity by also pricing the receiver swaption.

??? success "Solution to Exercise 1"

    **Given:** 2Y-into-3Y ATM payer swaption, $S_0 = K = 0.045$, $\sigma = 0.18$, $A_0 = 2.72$, $T_0 = 2$.

    Since $S_0 = K$ (ATM), $\ln(S_0/K) = 0$, so:

    $$
    d_1 = \frac{0 + \frac{1}{2}(0.18)^2 \times 2}{0.18\sqrt{2}} = \frac{\frac{1}{2}(0.0324)(2)}{0.18 \times 1.4142} = \frac{0.0324}{0.25456} = 0.12728
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T_0} = 0.12728 - 0.25456 = -0.12728
    $$

    $$
    N(0.12728) = 0.5506, \qquad N(-0.12728) = 0.4494
    $$

    **Payer swaption:**

    $$
    V_{\text{payer}} = A_0[S_0 N(d_1) - K N(d_2)] = 2.72[0.045 \times 0.5506 - 0.045 \times 0.4494]
    $$

    $$
    = 2.72 \times 0.045 \times (0.5506 - 0.4494) = 2.72 \times 0.045 \times 0.1012 = 0.01239
    $$

    The payer swaption price is approximately **1.239%** of notional (or 123.9 bps running on the annuity).

    **Receiver swaption:**

    $$
    V_{\text{receiver}} = A_0[K N(-d_2) - S_0 N(-d_1)] = 2.72[0.045 \times 0.5506 - 0.045 \times 0.4494]
    $$

    $$
    = 2.72 \times 0.045 \times (0.5506 - 0.4494) = 0.01239
    $$

    Since $K = S_0$, the ATM payer and receiver swaptions have **equal value**: $V_{\text{payer}} = V_{\text{receiver}} = 0.01239$.

    **Put-call parity verification:**

    $$
    V_{\text{payer}} - V_{\text{receiver}} = 0.01239 - 0.01239 = 0
    $$

    The forward swap value is $A_0(S_0 - K) = 2.72 \times 0 = 0$, consistent with an ATM forward swap having zero value. Parity is verified.

---

**Exercise 2.** Prove the put-call parity relation for swaptions: Payer Swaption $-$ Receiver Swaption $=$ Forward Swap. Start from the payoff definitions and show that the forward swap value at $T_0$ is $A(T_0)(S_{T_0} - K)$. Deduce that when $K = S_0$, the payer and receiver swaptions have equal value.

??? success "Solution to Exercise 2"

    **Payoff definitions:**

    - Payer swaption payoff at $T_0$: $\max(A(T_0)(S_{T_0} - K), 0) = A(T_0)\max(S_{T_0} - K, 0)$
    - Receiver swaption payoff at $T_0$: $\max(A(T_0)(K - S_{T_0}), 0) = A(T_0)\max(K - S_{T_0}, 0)$

    **Difference:**

    $$
    \text{Payer} - \text{Receiver} = A(T_0)[\max(S_{T_0} - K, 0) - \max(K - S_{T_0}, 0)]
    $$

    Using the identity $\max(x,0) - \max(-x,0) = x$ for all real $x$:

    $$
    = A(T_0)(S_{T_0} - K)
    $$

    This is exactly the value at $T_0$ of a forward-starting payer swap with fixed rate $K$, since the swap value at $T_0$ is $\sum_{i=1}^n \delta_i P(T_0, T_i)(S_{T_0} - K) = A(T_0)(S_{T_0} - K)$.

    **Present value at time 0:**

    Since $A(T_0)(S_{T_0} - K)$ is the swap payoff at $T_0$, its time-0 value is:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{T_0} r_s\,ds} A(T_0)(S_{T_0} - K)\right] = A_0(S_0 - K)
    $$

    The last equality follows because $S_t$ is a martingale under the annuity measure $\mathbb{Q}^A$ (with numéraire $A(t)$), so $\mathbb{E}^{\mathbb{Q}^A}[S_{T_0}] = S_0$, and changing back to the risk-neutral measure yields $A_0(S_0 - K)$.

    **Deduction:** When $K = S_0$, the forward swap value is $A_0(S_0 - S_0) = 0$, so:

    $$
    V_{\text{payer}} - V_{\text{receiver}} = 0 \implies V_{\text{payer}} = V_{\text{receiver}}
    $$

    ATM payer and receiver swaptions have equal value.

---

**Exercise 3.** Explain Jamshidian's trick in detail. For a 1Y-into-2Y payer swaption (annual payments) in the Hull-White model with $\lambda = 0.05$, $\sigma = 0.01$, and strike $K = 5\%$: (a) Write down the equation that determines $r^*$. (b) Explain why the decomposition into bond puts requires the bond price to be monotonic in $r$. (c) In what models does Jamshidian's trick fail, and why?

??? success "Solution to Exercise 3"

    **Jamshidian's trick in detail:**

    In the Hull-White model, the short rate $r_t$ is the single state variable. Bond prices $P(T_0, T_i) = P(T_0, T_i, r_{T_0})$ are deterministic decreasing functions of $r_{T_0}$.

    A payer swaption with strike $K$ pays $\max(1 - \sum_{i=1}^n c_i P(T_0, T_i), 0)$ at $T_0$, where $c_i = K\delta_i$ for $i < n$ and $c_n = 1 + K\delta_n$.

    **(a) Equation for $r^*$:**

    The critical rate $r^*$ satisfies:

    $$
    \sum_{i=1}^{2} c_i P(T_0, T_i, r^*) = 1
    $$

    For a 1Y-into-2Y swaption with annual payments and $K = 5\%$:

    - $c_1 = 0.05$ at $T_1 = 2$ (coupon at year 2)
    - $c_2 = 1.05$ at $T_2 = 3$ (coupon + principal at year 3)

    So:

    $$
    0.05 \cdot P(1, 2, r^*) + 1.05 \cdot P(1, 3, r^*) = 1
    $$

    where $P(1, T_i, r^*) = A(T_i - 1)\exp(-B(T_i - 1)r^*)$ in the Hull-White model, with $A$ and $B$ determined by the model parameters $\kappa = 0.05$, $\sigma = 0.01$, and the initial yield curve.

    **(b) Monotonicity requirement:**

    The decomposition works because $P(T_0, T_i, r)$ is strictly decreasing in $r$ for each $T_i > T_0$. In the Hull-White model:

    $$
    \frac{\partial P}{\partial r} = -B(T_i - T_0) P < 0
    $$

    since $B(\tau) > 0$ for $\tau > 0$. This ensures:

    - The function $r \mapsto \sum c_i P(T_0, T_i, r)$ is strictly decreasing
    - There is a unique $r^*$ solving $\sum c_i P(T_0, T_i, r^*) = 1$
    - The swaption is in the money precisely when $r_{T_0} < r^*$
    - For each $i$: $P(T_0, T_i, r_{T_0}) > P(T_0, T_i, r^*)$ iff $r_{T_0} < r^*$

    Therefore the swaption payoff equals $\sum c_i \max(K_i - P(T_0, T_i, r_{T_0}), 0)$ with $K_i = P(T_0, T_i, r^*)$, decomposing into bond puts.

    **(c) Where Jamshidian fails:**

    Jamshidian's trick fails in **multi-factor models** (e.g., two-factor Hull-White, the LIBOR market model). In a two-factor model, bond prices $P(T_0, T_i)$ depend on two state variables $(r_1, r_2)$. The exercise region $\{(r_1, r_2) : \sum c_i P(T_0, T_i, r_1, r_2) > 1\}$ is a two-dimensional set, not a simple half-line. Different bonds can be in or out of the money simultaneously, so the decomposition into individual bond options is no longer valid. In multi-factor models, numerical methods (Monte Carlo, PDE on a 2D grid) must be used directly.

---

**Exercise 4.** An ATM swaption has the approximate value $V \approx A_0 \cdot S_0 \cdot \sigma\sqrt{T_0} \cdot \sqrt{2/\pi}$. For a 5Y-into-10Y ATM swaption with $S_0 = 3.5\%$, $A_0 = 8.2$, and $\sigma = 15\%$, compute the approximate price. Compare with the exact Black's formula result and discuss when the approximation breaks down.

??? success "Solution to Exercise 4"

    **Given:** 5Y-into-10Y ATM swaption, $S_0 = 0.035$, $A_0 = 8.2$, $\sigma = 0.15$, $T_0 = 5$.

    **Approximate formula:**

    $$
    V \approx A_0 \cdot S_0 \cdot \sigma\sqrt{T_0} \cdot \sqrt{\frac{2}{\pi}}
    $$

    $$
    = 8.2 \times 0.035 \times 0.15 \times \sqrt{5} \times \sqrt{0.6366}
    $$

    $$
    = 8.2 \times 0.035 \times 0.15 \times 2.2361 \times 0.7979
    $$

    $$
    = 8.2 \times 0.035 \times 0.15 \times 1.7841 = 8.2 \times 0.035 \times 0.26761
    $$

    $$
    = 8.2 \times 0.009366 = 0.07680
    $$

    The approximate price is **7.68%** of the annuity, or about **0.0768** in dollar terms per unit notional.

    **Exact Black's formula:**

    With $K = S_0 = 0.035$:

    $$
    d_1 = \frac{\sigma\sqrt{T_0}}{2} = \frac{0.15 \times 2.2361}{2} = 0.16771
    $$

    $$
    d_2 = -0.16771
    $$

    $$
    N(0.16771) = 0.5666, \qquad N(-0.16771) = 0.4334
    $$

    $$
    V_{\text{exact}} = 8.2 \times 0.035 \times (0.5666 - 0.4334) = 8.2 \times 0.035 \times 0.1332 = 0.03822
    $$

    Wait --- let me recompute. The exact formula gives:

    $$
    V_{\text{exact}} = A_0[S_0 N(d_1) - K N(d_2)] = 8.2[0.035 \times 0.5666 - 0.035 \times 0.4334]
    $$

    $$
    = 8.2 \times 0.035 \times 0.1332 = 0.03822
    $$

    And the approximation gives $0.07680$. These should agree for ATM. Let me recheck the approximation formula.

    The standard ATM approximation is $V \approx A_0 S_0 \sigma\sqrt{T_0/2\pi}$ (not $A_0 S_0 \sigma\sqrt{T_0}\sqrt{2/\pi}$). The correct version:

    $$
    N(d_1) - N(d_2) \approx \phi(0) \cdot 2d_1 = \frac{2}{\sqrt{2\pi}} \cdot \frac{\sigma\sqrt{T_0}}{2} = \frac{\sigma\sqrt{T_0}}{\sqrt{2\pi}}
    $$

    So:

    $$
    V \approx A_0 S_0 \frac{\sigma\sqrt{T_0}}{\sqrt{2\pi}} = 8.2 \times 0.035 \times \frac{0.15 \times 2.2361}{2.5066}
    $$

    $$
    = 0.287 \times 0.13377 = 0.03839
    $$

    This matches the exact value of 0.03822 well (difference of 0.4%).

    The approximate price is **3.84%** of the annuity factor, or approximately **0.0384** per unit notional.

    **When the approximation breaks down:** The linearization $N(d_1) - N(d_2) \approx \sigma\sqrt{T_0}/\sqrt{2\pi}$ is accurate when $\sigma\sqrt{T_0}$ is small. Here $\sigma\sqrt{T_0} = 0.335$, which is moderate. For very long-dated swaptions or high volatility (e.g., $\sigma\sqrt{T_0} > 1$), the linear approximation deteriorates because $\phi(d)$ is no longer approximately constant over the interval $[d_2, d_1]$. Deep OTM/ITM swaptions also violate the approximation since it assumes $K \approx S_0$.

---

**Exercise 5.** A swaption desk observes the following ATM implied volatilities for the swaption matrix (in percent):

|  | 1Y Tenor | 5Y Tenor | 10Y Tenor |
|---|---|---|---|
| 1Y Expiry | 25.0 | 22.0 | 19.0 |
| 5Y Expiry | 20.0 | 18.5 | 17.0 |
| 10Y Expiry | 16.0 | 15.5 | 15.0 |

Describe the qualitative features of this matrix (term structure in expiry, term structure in tenor). Is a one-factor short-rate model likely to fit this matrix well? Justify your answer.

??? success "Solution to Exercise 5"

    **Qualitative features of the swaption matrix:**

    *Term structure in expiry (reading down each column):* Volatility **decreases** with expiry for all tenors (e.g., 1Y tenor: 25% -> 20% -> 16%). This is typical: short-term rates are more uncertain over the near term than the long term, reflecting mean reversion of interest rates.

    *Term structure in tenor (reading across each row):* Volatility **decreases** with swap tenor for all expiries (e.g., 1Y expiry: 25% -> 22% -> 19%). Longer swaps average over more forward rates, and this diversification reduces the effective volatility of the swap rate.

    *Overall pattern:* The highest volatility is at the short-expiry, short-tenor corner (1Y x 1Y = 25%) and the lowest at the long-expiry, long-tenor corner (10Y x 10Y = 15%). The vol surface slopes downward in both directions.

    **Can a one-factor model fit this matrix?**

    A one-factor short-rate model (e.g., Hull-White) has limited ability to fit the full swaption matrix because:

    1. **One-factor constraint:** With a single time-dependent volatility $\sigma(t)$, the model produces a specific relationship between caplet/swaption volatilities. The ratio of swaption vols across tenors is determined by the function $B(\tau) = (1-e^{-\kappa\tau})/\kappa$, which cannot be independently adjusted for each expiry-tenor pair.

    2. **Tenor effect:** In a one-factor model, the swap rate volatility for a $T_0$-into-$n$-year swaption is approximately $\sigma \cdot B(n)/n$ (normalized by duration). The decrease in vol with tenor is captured by $B(n)/n$ being decreasing, but the **rate** of decrease is rigidly determined by $\kappa$.

    3. **Expiry-tenor interaction:** The matrix shows that the vol decline along tenor is steeper for short expiries (25 -> 19 = 6pp for 1Y expiry) than for long expiries (16 -> 15 = 1pp for 10Y expiry). A one-factor model produces a more uniform pattern.

    A one-factor model can be calibrated to match one row or one column reasonably well, but fitting the entire matrix simultaneously is generally poor. Multi-factor models or stochastic volatility models provide the additional degrees of freedom needed.

---

**Exercise 6.** Compute the delta, vega, and gamma of a 3Y-into-5Y payer swaption with $K = S_0 = 4\%$, $\sigma = 20\%$, and $A_0 = 4.35$. If the swap rate increases by 50 bps, estimate the new swaption value using (a) delta only, and (b) delta plus gamma.

??? success "Solution to Exercise 6"

    **Given:** 3Y-into-5Y payer swaption, $K = S_0 = 0.04$ (ATM), $\sigma = 0.20$, $A_0 = 4.35$, $T_0 = 3$.

    **Step 1: Compute $d_1$ and $d_2$.**

    $$
    d_1 = \frac{\sigma\sqrt{T_0}}{2} = \frac{0.20 \times \sqrt{3}}{2} = \frac{0.20 \times 1.7321}{2} = 0.17321
    $$

    $$
    d_2 = -0.17321
    $$

    $$
    N(0.17321) = 0.5688, \qquad \phi(0.17321) = 0.3930
    $$

    **Delta:**

    $$
    \Delta = A_0 \cdot N(d_1) = 4.35 \times 0.5688 = 2.4743
    $$

    **Vega:**

    $$
    \mathcal{V} = A_0 \cdot S_0\sqrt{T_0}\,\phi(d_1) = 4.35 \times 0.04 \times 1.7321 \times 0.3930 = 4.35 \times 0.02723 = 0.11845
    $$

    **Gamma:**

    $$
    \Gamma = \frac{A_0\,\phi(d_1)}{S_0\,\sigma\sqrt{T_0}} = \frac{4.35 \times 0.3930}{0.04 \times 0.20 \times 1.7321} = \frac{1.7096}{0.013857} = 123.37
    $$

    **Current swaption value:**

    $$
    V_0 = A_0 \cdot S_0 \cdot [N(d_1) - N(d_2)] = 4.35 \times 0.04 \times (0.5688 - 0.4312) = 4.35 \times 0.04 \times 0.1376 = 0.02394
    $$

    **If the swap rate increases by 50 bps** ($\Delta S = 0.005$):

    **(a) Delta-only approximation:**

    $$
    \Delta V \approx \Delta \cdot \Delta S = 2.4743 \times 0.005 = 0.01237
    $$

    $$
    V_{\text{new}} \approx 0.02394 + 0.01237 = 0.03631
    $$

    **(b) Delta + gamma approximation:**

    $$
    \Delta V \approx \Delta \cdot \Delta S + \frac{1}{2}\Gamma \cdot (\Delta S)^2 = 2.4743 \times 0.005 + \frac{1}{2} \times 123.37 \times (0.005)^2
    $$

    $$
    = 0.01237 + 0.001542 = 0.01391
    $$

    $$
    V_{\text{new}} \approx 0.02394 + 0.01391 = 0.03785
    $$

    The gamma correction adds about 1.5 bps, reflecting the convexity of the option payoff. The delta-plus-gamma estimate is more accurate for this 50 bp move.

---

**Exercise 7.** A Bermudan swaption exercisable at years 1, 2, 3, 4, 5 into a swap paying until year 10 is worth more than the corresponding 1Y-into-9Y European swaption. Explain the source of the early exercise premium. Describe how you would price this Bermudan swaption using backward induction on a trinomial tree, specifying the exercise decision rule at each exercise date.

??? success "Solution to Exercise 7"

    **Source of the early exercise premium:**

    A Bermudan swaption is worth more than any single European swaption because it provides **optionality at multiple exercise dates**. The holder can choose the optimal time to exercise based on the prevailing interest rate environment:

    1. If rates move favorably early (e.g., swap rates rise significantly above the strike for a payer swaption), the holder can exercise early and lock in a valuable swap for a longer remaining tenor (e.g., exercising at year 1 gives a 9-year swap, which has more value than a 5-year swap from exercising at year 5).

    2. If rates have not moved enough, the holder can wait and preserve the option for a later date. The ability to wait is itself valuable.

    3. The early exercise premium reflects the value of this timing flexibility. It is highest when the yield curve is steep or when rates are volatile, as these conditions create more opportunities for profitable early exercise.

    **Pricing via backward induction on a trinomial tree:**

    **Step 1: Build the tree.** Construct a trinomial tree for the short rate $r_t$ over the interval $[0, 10]$ with time steps $\Delta t$ (e.g., $\Delta t = 0.5$ years). At each node $(i, j)$ (time step $i$, state $j$), the short rate is $r_{i,j}$, and three branches lead to nodes at step $i+1$.

    **Step 2: Compute bond prices.** At each node, compute the zero-coupon bond prices $P(t_i, T_k, r_{i,j})$ for all relevant payment dates $T_k$ using the tree or analytical formulas.

    **Step 3: Terminal values.** At the final time step ($t = 10$), the swap has expired and the swaption value is zero.

    **Step 4: Backward induction.** Moving backward from $t = 10$ to $t = 0$:

    - **At non-exercise dates:** The swaption value at node $(i,j)$ is the discounted expected value from the three successor nodes:

        $$
        V_{i,j} = e^{-r_{i,j}\Delta t}\left[p_u V_{i+1,j+1} + p_m V_{i+1,j} + p_d V_{i+1,j-1}\right]
        $$

        where $p_u, p_m, p_d$ are the trinomial probabilities.

    - **At exercise dates** ($t = 1, 2, 3, 4, 5$): Compute the **exercise value** --- the value of the underlying swap from the exercise date to year 10:

        $$
        \text{ExVal}_{i,j} = \sum_{k} c_k P(t_i, T_k, r_{i,j}) - 1
        $$

        for a payer swaption (where $c_k$ are the swap cashflows). The swaption value is the **maximum** of the continuation value and the exercise value:

        $$
        V_{i,j} = \max(\text{ExVal}_{i,j},\; \text{ContVal}_{i,j})
        $$

        where $\text{ContVal}_{i,j}$ is the discounted expected value from successor nodes.

    **Step 5: The exercise decision rule** at each exercise date is: exercise if and only if $\text{ExVal}_{i,j} > \text{ContVal}_{i,j}$. This defines an exercise boundary in the $(t, r)$ space.

    **Step 6:** The value at the root node $(0, j_0)$ is the Bermudan swaption price. It should satisfy $V_{\text{Bermudan}} \geq V_{\text{European}}$ for every European swaption with the same strike whose expiry is one of the exercise dates.
