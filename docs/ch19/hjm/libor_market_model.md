# LIBOR Market Model

The **LIBOR Market Model** (LMM), also known as the **Brace–Gatarek–Musiela (BGM) model**, is a market model for interest rates that directly models observable forward LIBOR rates rather than instantaneous forward rates or short rates. It is the most widely used model for pricing and hedging interest rate derivatives, particularly caps and swaptions.

---

## Motivation

### Limitations of Short-Rate and HJM Models

Short-rate models (Vasicek, CIR, Hull-White) and the general HJM framework have theoretical elegance but practical limitations:

- **Unobservable quantities:** Short rates and instantaneous forward rates are not directly quoted in markets
- **Calibration difficulty:** Mapping model parameters to liquid instruments requires transformation
- **Volatility mismatch:** Market quotes use Black volatilities for caps/swaptions; translating to model volatilities introduces approximation

### The Market Model Philosophy

The LMM takes a different approach:

> **Model directly what the market quotes: forward LIBOR rates.**

This provides:
- Natural calibration to caplets (each forward rate has its own volatility)
- Direct connection to Black's formula
- Market-consistent pricing of vanilla derivatives

---

## Model Setup

### Tenor Structure

Fix a tenor structure:

$$
0 = T_0 < T_1 < T_2 < \cdots < T_n
$$

with accrual periods $\delta_i = T_{i+1} - T_i$ (typically 3 months or 6 months).

### Forward LIBOR Rates

The **forward LIBOR rate** $L_i(t)$ is the simply-compounded forward rate at time $t$ for the period $[T_i, T_{i+1}]$:

$$
L_i(t) = \frac{1}{\delta_i}\left(\frac{P(t, T_i)}{P(t, T_{i+1})} - 1\right)
$$

Equivalently:

$$
P(t, T_{i+1}) = \frac{P(t, T_i)}{1 + \delta_i L_i(t)}
$$

At reset date $T_i$, the rate $L_i(T_i)$ is the spot LIBOR rate observed and used for payment at $T_{i+1}$.

### Key Relationship

Bond prices can be expressed in terms of forward rates:

$$
P(t, T_n) = P(t, T_0) \prod_{i=0}^{n-1} \frac{1}{1 + \delta_i L_i(t)}
$$

---

## Dynamics Under the Terminal Measure

### Terminal Measure $\mathbb{Q}^{T_n}$

Under the **terminal forward measure** $\mathbb{Q}^{T_n}$ (with numéraire $P(t, T_n)$), the forward rates have lognormal dynamics:

$$
\boxed{\frac{dL_i(t)}{L_i(t)} = \sigma_i(t) \, dW_i^{T_n}(t)}
$$

where:
- $\sigma_i(t)$ is the **instantaneous volatility** of forward rate $L_i$
- $W_i^{T_n}$ are correlated Brownian motions under $\mathbb{Q}^{T_n}$

### Correlation Structure

The driving Brownian motions are correlated:

$$
dW_i^{T_n} \cdot dW_j^{T_n} = \rho_{ij} \, dt
$$

where $\rho_{ij}$ is the instantaneous correlation between forward rates $L_i$ and $L_j$.

### Why Lognormal?

Under $\mathbb{Q}^{T_n}$, the forward rate $L_i(t)$ is a **martingale** for $i = n-1$ (the rate for period $[T_{n-1}, T_n]$). For other rates, there is a drift term that depends on the measure.

---

## Dynamics Under the Spot Measure

### The Spot Measure $\mathbb{Q}^B$

A practically useful measure is the **spot (rolling) measure** $\mathbb{Q}^B$, which uses the continuously-rolled money market account as numéraire.

Under $\mathbb{Q}^B$, the forward rate $L_i(t)$ satisfies:

$$
\frac{dL_i(t)}{L_i(t)} = \mu_i(t) \, dt + \sigma_i(t) \, dW_i^B(t)
$$

where the drift is:

$$
\mu_i(t) = \sum_{j=\eta(t)}^{i} \frac{\delta_j \rho_{ij} \sigma_i(t) \sigma_j(t) L_j(t)}{1 + \delta_j L_j(t)}
$$

and $\eta(t) = \min\{k : T_k > t\}$ is the index of the next reset date.

### Interpretation

- The drift involves a **sum over all forward rates** between the next reset and the rate being modeled
- Correlation enters through $\rho_{ij}$
- The drift is **state-dependent** (depends on current forward rates)

---

## Dynamics Under Individual Forward Measures

### $T_{i+1}$-Forward Measure

Under the measure $\mathbb{Q}^{T_{i+1}}$ (with numéraire $P(t, T_{i+1})$), the forward rate $L_i(t)$ is a **martingale**:

$$
\boxed{\frac{dL_i(t)}{L_i(t)} = \sigma_i(t) \, dW_i^{T_{i+1}}(t)}
$$

This is the **natural measure** for pricing caplets on $L_i$.

### Measure Change

Moving between forward measures involves Girsanov transformations. From $\mathbb{Q}^{T_{j+1}}$ to $\mathbb{Q}^{T_{i+1}}$ (for $j > i$):

$$
dW_i^{T_{i+1}}(t) = dW_i^{T_{j+1}}(t) - \sum_{k=i+1}^{j} \frac{\delta_k \rho_{ik} \sigma_k(t) L_k(t)}{1 + \delta_k L_k(t)} \, dt
$$

---

## Connection to HJM

### LMM as a Special Case of HJM

The LIBOR market model can be derived from HJM by choosing a specific volatility structure for instantaneous forward rates that:

1. Leads to lognormal dynamics for discrete forward LIBOR rates
2. Satisfies the HJM no-arbitrage drift condition

### Volatility Specification

If HJM volatility is chosen as:

$$
\sigma_{\text{HJM}}(t, T) = \sum_{i} \sigma_i(t) \cdot \mathbf{1}_{T_i < T \leq T_{i+1}} \cdot \frac{\delta_i L_i(t)}{1 + \delta_i L_i(t)}
$$

then the discrete forward rates follow lognormal LMM dynamics.

---

## Caplet Pricing

### Black's Formula in LMM

Under $\mathbb{Q}^{T_{i+1}}$, $L_i$ is lognormal with terminal distribution:

$$
L_i(T_i) \sim L_i(0) \exp\left(-\frac{1}{2}v_i^2 + v_i Z\right), \quad Z \sim N(0,1)
$$

where the **integrated variance** is:

$$
v_i^2 = \int_0^{T_i} \sigma_i(t)^2 \, dt
$$

### Caplet Formula

The caplet paying $\delta_i \max(L_i(T_i) - K, 0)$ at $T_{i+1}$ has price:

$$
\boxed{\text{Caplet}_i = \delta_i P(0, T_{i+1}) \left[L_i(0) N(d_1) - K N(d_2)\right]}
$$

where:

$$
d_1 = \frac{\ln(L_i(0)/K) + \frac{1}{2}v_i^2}{v_i}, \quad d_2 = d_1 - v_i
$$

### Implied Volatility

The **Black implied volatility** $\sigma_i^{\text{Black}}$ satisfies:

$$
v_i = \sigma_i^{\text{Black}} \sqrt{T_i}
$$

For constant instantaneous volatility $\sigma_i(t) = \sigma_i$:

$$
\sigma_i^{\text{Black}} = \sigma_i
$$

---

## Swaption Pricing

### The Challenge

Unlike caplets, swaptions depend on **multiple forward rates** and their **correlations**. The swap rate:

$$
S(t) = \frac{P(t, T_0) - P(t, T_n)}{\sum_{j=1}^{n} \delta_j P(t, T_j)}
$$

is **not lognormal** under any standard measure in the LMM.

### Approximation Methods

Several approaches exist:

**1. Frozen Drift Approximation:**

Approximate the swap rate volatility by "freezing" forward rates at their initial values:

$$
\sigma_S \approx \sqrt{\sum_{i,j} w_i w_j \rho_{ij} \sigma_i \sigma_j}
$$

where $w_i$ are weights derived from the swap rate's dependence on each forward rate.

**2. Rebonato's Formula:**

$$
\sigma_S^2 T_0 \approx \sum_{i,j=\alpha}^{\beta-1} \frac{w_i(0) w_j(0) L_i(0) L_j(0)}{S(0)^2} \rho_{ij} \int_0^{T_0} \sigma_i(t) \sigma_j(t) \, dt
$$

where $\alpha, \beta$ index the swap period.

**3. Monte Carlo Simulation:**

Simulate the full dynamics of all forward rates and compute swaption payoffs numerically.

---

## Calibration

### Calibration to Caps

Since each caplet depends on a single forward rate:

1. **Bootstrap caplet volatilities** from market cap prices
2. **Match** $\sigma_i$ to reproduce each caplet price
3. For time-dependent $\sigma_i(t)$, additional constraints are needed

### Calibration to Swaptions

Joint calibration to caps and swaptions determines:
- Individual forward rate volatilities $\sigma_i$
- Correlation structure $\rho_{ij}$

**Optimization problem:**

$$
\min_{\sigma, \rho} \sum_{\text{caps}} w_c (C^{\text{LMM}} - C^{\text{mkt}})^2 + \sum_{\text{swaptions}} w_s (S^{\text{LMM}} - S^{\text{mkt}})^2
$$

### Correlation Parametrization

Common parametrizations include:

**Exponential decay:**

$$
\rho_{ij} = \exp(-\beta |T_i - T_j|)
$$

**Two-factor:**

$$
\rho_{ij} = \rho_\infty + (1 - \rho_\infty) \exp(-\beta |T_i - T_j|)
$$

---

## Volatility Specifications

### Time-Homogeneous Volatility

$$
\sigma_i(t) = \sigma(T_i - t)
$$

The volatility depends only on time-to-maturity. This produces a **stationary** volatility structure.

### Separable Volatility

$$
\sigma_i(t) = g(t) \cdot h(T_i)
$$

Factors into time and maturity components.

### Piecewise Constant

$$
\sigma_i(t) = \sigma_{i,k} \quad \text{for } T_{k-1} \leq t < T_k
$$

Most flexible for calibration but introduces many parameters.

### Volatility Term Structure

Typical features observed in markets:
- **Humped shape:** Volatility peaks at intermediate maturities (2-5 years)
- **Decay:** Long-dated rates have lower volatility
- **Near-expiry effect:** Volatility may increase as reset approaches

---

## Simulation

### Euler Discretization

For Monte Carlo pricing, discretize the SDE:

$$
L_i(t + \Delta t) = L_i(t) \exp\left[\left(\mu_i(t) - \frac{1}{2}\sigma_i(t)^2\right)\Delta t + \sigma_i(t) \sqrt{\Delta t} \, Z_i\right]
$$

where $Z_i$ are correlated normal random variables satisfying $\text{Corr}(Z_i, Z_j) = \rho_{ij}$.

### Correlation via Cholesky

Generate correlated normals via Cholesky decomposition:

$$
\mathbf{Z} = L \mathbf{\xi}
$$

where $LL^T = \rho$ and $\xi_i \sim N(0,1)$ are independent.

### Drift Calculation

At each time step, compute the drift using current forward rate values:

$$
\mu_i(t) = \sum_{j=\eta(t)}^{i} \frac{\delta_j \rho_{ij} \sigma_i(t) \sigma_j(t) L_j(t)}{1 + \delta_j L_j(t)}
$$

This requires simulating all forward rates together.

---

## Extensions and Variants

### Stochastic Volatility LMM

Add dynamics for volatility:

$$
\frac{dL_i(t)}{L_i(t)} = \mu_i(t) \, dt + \sigma_i(t) V(t) \, dW_i(t)
$$

$$
dV(t) = \kappa(\theta - V(t)) \, dt + \xi V(t)^\gamma \, dW_V(t)
$$

This captures:
- Volatility smile/skew
- Time-varying implied volatility

### SABR-LMM

Each forward rate follows SABR dynamics:

$$
dL_i = \alpha_i L_i^\beta \, dW_i, \quad d\alpha_i = \nu \alpha_i \, dZ_i
$$

Provides analytical approximations for the smile.

### Displaced Diffusion LMM

$$
d(L_i + s) = \sigma_i (L_i + s) \, dW_i
$$

The shift parameter $s$ allows negative rates and generates skew.

---

## Transition from LIBOR to RFR

### LIBOR Discontinuation

LIBOR (London Interbank Offered Rate) has been largely discontinued:
- USD LIBOR: Ceased June 2023 (most tenors)
- Other currencies: Earlier transitions

### Risk-Free Rate (RFR) Models

The LMM framework adapts to backward-looking rates like SOFR:

$$
\bar{R}_i = \frac{1}{\delta_i}\left[\prod_{k \in [T_i, T_{i+1}]} (1 + r_k \delta_k) - 1\right]
$$

where $r_k$ are daily compounded rates.

### Forward-Looking vs. Backward-Looking

- **LIBOR:** Forward-looking, known at period start
- **SOFR:** Backward-looking, known at period end

This changes:
- Timing of rate fixing
- Convexity adjustments
- Hedging strategies

---

## Practical Considerations

### Dimensionality

For a 30-year tenor with quarterly resets:
- 120 forward rates
- 120 volatilities
- 7,140 correlations (120 × 119 / 2)

**Dimension reduction** is essential:
- Factor models (2-3 principal components)
- Parametric correlation
- Time-homogeneous volatility

### Numerical Efficiency

- **Predictor-corrector schemes** improve accuracy
- **Quasi-Monte Carlo** reduces variance
- **Variance reduction:** Antithetic variates, control variates

### Model Risk

- Correlation assumptions significantly affect exotic pricing
- Volatility smile/skew requires extensions
- Calibration stability over time

---

## Comparison with Other Models

| Feature | Short-Rate | HJM | LMM |
|---------|------------|-----|-----|
| State variable | $r_t$ | $f(t,T)$ | $L_i(t)$ |
| Dimension | 1-2 | $\infty$ | $n$ (finite) |
| Market observability | No | No | Yes |
| Cap calibration | Indirect | Indirect | Direct |
| Swaption calibration | Jamshidian | Approximation | Approximation |
| Smile | Extensions | Extensions | Extensions |

---

## Key Takeaways

- LMM models discrete forward LIBOR rates directly
- Each forward rate is lognormal under its own forward measure
- Caplet pricing recovers Black's formula exactly
- Swaption pricing requires approximation (correlation-dependent)
- Calibration matches cap volatilities term structure
- Correlation structure from swaption calibration
- Extensions: stochastic volatility, SABR, displaced diffusion
- Post-LIBOR: framework adapts to RFR-based rates

---

## Further Reading

- Brace, Gatarek & Musiela (1997), "The Market Model of Interest Rate Dynamics"
- Jamshidian (1997), "LIBOR and Swap Market Models and Measures"
- Rebonato (2002), *Modern Pricing of Interest-Rate Derivatives*
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapters 6-7
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volumes 1-3
