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
