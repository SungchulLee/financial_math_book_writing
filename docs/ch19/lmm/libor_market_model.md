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

### Terminal Measure Q^T_n

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

### The Spot Measure Q^B

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

### T_i+1-Forward Measure

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

---

## Exercises

**Exercise 1.** In the LMM, the forward rate $L_i(t)$ is a martingale under $\mathbb{Q}^{T_{i+1}}$ and follows $dL_i(t)/L_i(t) = \sigma_i(t)\,dW_i^{T_{i+1}}(t)$. Explain why $L_i(t)$ is not a martingale under $\mathbb{Q}^{T_{j+1}}$ for $j \neq i$, and describe the drift correction that arises when changing from $\mathbb{Q}^{T_{i+1}}$ to $\mathbb{Q}^{T_{j+1}}$.

??? success "Solution to Exercise 1"
    Under the $T_{i+1}$-forward measure $\mathbb{Q}^{T_{i+1}}$, the numéraire is $P(t, T_{i+1})$. The forward rate $L_i(t)$ is a martingale under this measure because $\delta_i L_i(t) P(t, T_{i+1}) = P(t, T_i) - P(t, T_{i+1})$ is the value of a self-financing portfolio, and dividing by the numéraire $P(t, T_{i+1})$ yields a martingale. Therefore $L_i(t)$ has **zero drift** under $\mathbb{Q}^{T_{i+1}}$:

    $$
    \frac{dL_i(t)}{L_i(t)} = \sigma_i(t)\,dW_i^{T_{i+1}}(t)
    $$

    Under a different measure $\mathbb{Q}^{T_{j+1}}$ with $j \neq i$, $L_i(t)$ is **not** a martingale because the numéraire has changed from $P(t, T_{i+1})$ to $P(t, T_{j+1})$. The ratio $P(t, T_{i+1})/P(t, T_{j+1})$ is stochastic (it depends on the forward rates between $T_{i+1}$ and $T_{j+1}$), so dividing the tradable portfolio by $P(t, T_{j+1})$ introduces an additional drift.

    **Drift correction via Girsanov's theorem:** The Brownian motions under the two measures are related by

    $$
    dW_i^{T_{i+1}}(t) = dW_i^{T_{j+1}}(t) - \sum_{k=i+1}^{j} \frac{\delta_k \rho_{ik} \sigma_k(t) L_k(t)}{1 + \delta_k L_k(t)}\,dt \quad \text{(for } j > i\text{)}
    $$

    Substituting into the driftless dynamics under $\mathbb{Q}^{T_{i+1}}$, the dynamics under $\mathbb{Q}^{T_{j+1}}$ become:

    $$
    \frac{dL_i(t)}{L_i(t)} = -\sigma_i(t)\sum_{k=i+1}^{j} \frac{\delta_k \rho_{ik} \sigma_k(t) L_k(t)}{1 + \delta_k L_k(t)}\,dt + \sigma_i(t)\,dW_i^{T_{j+1}}(t)
    $$

    The drift is **negative** when moving to a later terminal measure ($j > i$), reflecting the fact that the ratio $P(t, T_{i+1})/P(t, T_{j+1})$ tends to drift upward (as a product of $(1 + \delta_k L_k)$ terms), which pushes $L_i$ downward relative to the new numéraire. For $j < i$, the drift would be positive.

---

**Exercise 2.** Consider a simple LMM with two forward rates $L_0$ and $L_1$ on a semiannual grid. The initial rates are $L_0(0) = 4.5\%$ and $L_1(0) = 4.8\%$, with constant volatilities $\sigma_0 = 18\%$ and $\sigma_1 = 20\%$, and correlation $\rho_{01} = 0.85$. The zero-coupon bond prices are $P(0, 0.5) = 0.978$ and $P(0, 1.0) = 0.954$. Compute the annuity $A(0) = 0.5 \cdot P(0, 0.5) + 0.5 \cdot P(0, 1.0)$ and the forward swap rate $S(0)$.

??? success "Solution to Exercise 2"
    **Step 1: Compute the annuity.**

    $$
    A(0) = 0.5 \cdot P(0, 0.5) + 0.5 \cdot P(0, 1.0) = 0.5 \times 0.978 + 0.5 \times 0.954 = 0.489 + 0.477 = 0.966
    $$

    **Step 2: Compute $P(0, T_0) = P(0, 0) = 1$** (discount factor to today).

    **Step 3: Compute the forward swap rate.**

    The swap rate for a swap with payments at $T_1 = 0.5$ and $T_2 = 1.0$ is:

    $$
    S(0) = \frac{P(0, T_0) - P(0, T_2)}{A(0)} = \frac{1 - 0.954}{0.966} = \frac{0.046}{0.966} \approx 0.04762 = 4.762\%
    $$

    **Verification:** We can also express the swap rate as a weighted average of forward rates:

    $$
    S(0) = w_0 L_0(0) + w_1 L_1(0)
    $$

    where $w_i = \delta_i P(0, T_{i+1})/A(0)$. Computing:

    $$
    w_0 = \frac{0.5 \times 0.978}{0.966} = \frac{0.489}{0.966} \approx 0.5062
    $$

    $$
    w_1 = \frac{0.5 \times 0.954}{0.966} = \frac{0.477}{0.966} \approx 0.4938
    $$

    $$
    S(0) \approx 0.5062 \times 0.045 + 0.4938 \times 0.048 = 0.02278 + 0.02370 = 0.04648 \approx 4.65\%
    $$

    Note: The slight discrepancy arises because the bond prices $P(0, 0.5)$ and $P(0, 1.0)$ are not exactly consistent with the forward rates $L_0(0) = 4.5\%$ and $L_1(0) = 4.8\%$ via the formula $P(0, T_{i+1}) = P(0, T_i)/(1 + \delta_i L_i(0))$. The exact swap rate from the bond prices is $S(0) = 4.762\%$.

---

**Exercise 3.** The LMM is described as a "market model" because it models directly observable market rates (forward LIBOR rates) rather than latent state variables (like the short rate). Explain why this property is advantageous for calibration. In particular, discuss why a caplet in the LMM is priced exactly by Black's formula, while in the Hull--White model, caplet pricing requires a separate derivation.

??? success "Solution to Exercise 3"
    **Why the LMM is advantageous for calibration:**

    In the LMM, the state variables are forward LIBOR rates $L_i(t)$, which are directly observable market quantities. This has several calibration advantages:

    1. **Direct parameter mapping.** Each forward rate $L_i(t)$ has its own volatility parameter $\sigma_i(t)$. Market-quoted caplet implied volatilities $\sigma_i^{\text{Black}}$ map directly to these model parameters. Specifically, if $\sigma_i(t) = \sigma_i$ is constant, then $\sigma_i^{\text{Black}} = \sigma_i$. No transformation or inversion is needed.

    2. **Exact caplet pricing.** Under the $T_{i+1}$-forward measure, $L_i(t)$ is a martingale with lognormal dynamics:

        $$
        \frac{dL_i(t)}{L_i(t)} = \sigma_i(t)\,dW_i^{T_{i+1}}(t)
        $$

        This means $L_i(T_i)$ is lognormally distributed, and the caplet price is **exactly** given by Black's formula:

        $$
        \text{Caplet}_i = \delta_i P(0, T_{i+1})\bigl[L_i(0)N(d_1) - KN(d_2)\bigr]
        $$

        This is not an approximation --- it follows directly from the model specification. Each caplet involves only a single forward rate under its natural measure, so there are no multi-rate interactions or approximation errors.

    3. **In the Hull--White model**, by contrast, the state variable is the short rate $r(t)$, which is not directly quoted. Caplet pricing requires:
        - Computing the bond price $P(t, T) = A(t,T)e^{-B(t,T)r(t)}$ as a function of $r$
        - Expressing the forward LIBOR rate as a function of bond prices
        - Deriving the distribution of this composite quantity under the relevant measure
        - The result involves Jamshidian's trick or a separate analytical derivation, and the implied volatility structure depends on the model parameters ($\kappa$, $\sigma$, $\theta$) in a complex, non-transparent way

    In summary, the LMM's advantage is that market-observable quantities are modeled directly, making calibration a one-to-one mapping for caplets rather than a complex inversion problem.

---

**Exercise 4.** In the LMM, the number of state variables equals the number of forward rates (e.g., 120 for a 30-year quarterly model). Discuss the computational challenges this poses for Monte Carlo simulation. How does the "frozen drift" approximation reduce computational cost, and what accuracy trade-offs does it introduce?

??? success "Solution to Exercise 4"
    **Computational challenges of Monte Carlo simulation in the LMM:**

    For a 30-year quarterly model, there are $n = 120$ forward rates, each with its own SDE. At each time step, the simulator must:

    1. **Generate correlated random variables.** The $120 \times 120$ correlation matrix requires Cholesky decomposition ($O(n^3) = O(120^3) \approx 1.7 \times 10^6$ operations once, then $O(n^2)$ per step for the matrix-vector multiply).

    2. **Compute state-dependent drifts.** Under the spot measure, the drift of $L_i$ involves a sum of up to $i$ terms:

        $$
        \mu_i(t) = \sum_{j=\eta(t)}^{i} \frac{\delta_j \rho_{ij} \sigma_i(t)\sigma_j(t) L_j(t)}{1 + \delta_j L_j(t)}
        $$

        Computing all drifts costs $O(n^2)$ per time step. With 120 time steps (one per tenor), the total drift computation per path is $O(n^3)$.

    3. **Update all forward rates.** Each update requires $O(1)$ work, totaling $O(n \times \text{steps})$ per path.

    4. **Path-wise cost.** The total cost per path is dominated by drift computation: $O(n^2 \times \text{steps}) \approx O(n^3)$. For $10^5$ paths: $\sim 10^5 \times 120^3 \approx 10^{11}$ operations.

    **Frozen drift approximation:** Replace the state-dependent drift by its value at time 0:

    $$
    \mu_i^{\text{frozen}} = \sum_{j=\eta(t)}^{i} \frac{\delta_j \rho_{ij} \sigma_i(t)\sigma_j(t) L_j(0)}{1 + \delta_j L_j(0)}
    $$

    The drift becomes **deterministic** (precomputable), eliminating the $O(n^2)$ per-step cost. The drift can be computed once and stored.

    **Accuracy trade-offs:**

    - The frozen drift ignores the feedback between forward rate evolution and drift magnitude
    - It introduces bias of order $O(\Delta t)$ in the drift, degrading weak convergence from the potential $O(\Delta t)$ (with predictor--corrector) to $O(\sqrt{\Delta t})$
    - The approximation is reasonable for short-dated products and moderate volatilities, but can produce significant errors for long-dated or path-dependent products where forward rates deviate substantially from their initial values
    - The error is largest for forward rates far from the numéraire date, where drift corrections accumulate

---

**Exercise 5.** A displaced diffusion extension of the LMM models the forward rate as $dL_i(t) = \sigma_i(t)(L_i(t) + s_i)\,dW_i(t)$, where $s_i > 0$ is a displacement. Explain how this extension allows the model to accommodate negative rates while preserving the analytical tractability of Black-type caplet pricing. What is the effective lower bound on $L_i(t)$ in this model?

??? success "Solution to Exercise 5"
    **Displaced diffusion dynamics:**

    The displaced diffusion LMM models the forward rate as:

    $$
    dL_i(t) = \sigma_i(t)(L_i(t) + s_i)\,dW_i(t)
    $$

    where $s_i > 0$ is the displacement parameter.

    **Accommodating negative rates:** Define the shifted forward rate $\tilde{L}_i(t) = L_i(t) + s_i$. The SDE becomes:

    $$
    d\tilde{L}_i(t) = \sigma_i(t)\tilde{L}_i(t)\,dW_i(t)
    $$

    This is a geometric Brownian motion for $\tilde{L}_i$, which means $\tilde{L}_i(t) > 0$ for all $t$ (a.s.) if $\tilde{L}_i(0) > 0$. Therefore:

    $$
    L_i(t) = \tilde{L}_i(t) - s_i > -s_i
    $$

    **The effective lower bound on $L_i(t)$ is $-s_i$.** Forward rates can become negative, but they cannot fall below $-s_i$. By choosing $s_i$ appropriately (e.g., $s_i = 2\%$), the model can accommodate moderately negative rates.

    **Preserving analytical tractability:** Since $\tilde{L}_i(t)$ is lognormal under the forward measure $\mathbb{Q}^{T_{i+1}}$, caplet pricing on $L_i$ reduces to a shifted Black formula. A caplet paying $\delta_i\max(L_i(T_i) - K, 0) = \delta_i\max(\tilde{L}_i(T_i) - (K + s_i), 0)$ is priced as:

    $$
    \text{Caplet}_i = \delta_i P(0, T_{i+1})\bigl[(L_i(0) + s_i)N(d_1) - (K + s_i)N(d_2)\bigr]
    $$

    where $d_1$ and $d_2$ use the shifted forward $(L_i(0) + s_i)$ and shifted strike $(K + s_i)$, with the same integrated variance $v_i^2$. This is a standard Black formula applied to the shifted quantities.

    Additionally, the displacement introduces **skew** in the implied volatility smile: the lognormal volatility of the shifted process translates to a volatility that varies with strike $K$ when expressed in terms of the original (unshifted) rate.

---

**Exercise 6.** Explain the distinction between the "spot measure" (rolling money-market numéraire) and the "terminal measure" (fixed-maturity bond numéraire) in the LMM. Under each measure, write down the drift of $L_i(t)$ schematically and discuss which measure is preferred for Monte Carlo simulation of long-dated products.

??? success "Solution to Exercise 6"
    **Spot Measure $\mathbb{Q}^B$:**

    The numéraire is the discretely-compounded rolling money market account $B(t) = \prod_{j: T_j \leq t}(1 + \delta_j L_j(T_j)) \cdot P(t, T_{\eta(t)})$, where $\eta(t) = \min\{k : T_k > t\}$.

    Under $\mathbb{Q}^B$, the drift of $L_i(t)$ is:

    $$
    \mu_i^{(B)}(t) = \sum_{j=\eta(t)}^{i} \frac{\delta_j \rho_{ij}\sigma_i(t)\sigma_j(t) L_j(t)}{1 + \delta_j L_j(t)}
    $$

    Key features: the drift is **positive**, and the summation runs from the next reset date up to index $i$. For short-maturity rates (small $i$), the drift involves few terms.

    **Terminal Measure $\mathbb{Q}^{T_n}$:**

    The numéraire is $P(t, T_n)$, the zero-coupon bond maturing at the terminal date.

    Under $\mathbb{Q}^{T_n}$, the drift of $L_i(t)$ is:

    $$
    \mu_i^{(n)}(t) = -\sum_{j=i+1}^{n-1} \frac{\delta_j \rho_{ij}\sigma_i(t)\sigma_j(t) L_j(t)}{1 + \delta_j L_j(t)}
    $$

    Key features: the drift is **negative**, and the summation runs from $i+1$ to $n-1$. The last forward rate $L_{n-1}$ is a martingale (drift = 0). For short-maturity rates (small $i$), the drift involves many terms and can be large.

    **Which measure is preferred for long-dated products?**

    The **spot measure** is generally preferred for Monte Carlo simulation of long-dated products for several reasons:

    1. **Positive drifts** are more numerically stable than the negative drifts under the terminal measure, which can push short-dated forward rates toward zero
    2. **Natural discounting:** the money market account provides the discounting mechanism directly, so the simulated payoff is discounted by the simulated bank account value
    3. **Drift accumulation:** under the terminal measure, short-maturity rates have drift corrections that sum over many forward rates (up to $n-1$ terms), leading to large corrections and discretization errors. Under the spot measure, each rate's drift involves only rates with lower indices, and the drift grows gradually with $i$
    4. **Dimension reduction:** as the simulation progresses, expired forward rates drop out of the drift computation under the spot measure (because $\eta(t)$ advances), reducing computational cost naturally

---

**Exercise 7.** The LMM was originally developed for LIBOR rates but must be adapted for the post-LIBOR world based on risk-free rates (e.g., SOFR). Describe the key modifications needed: (a) replacing forward LIBOR rates with forward compounded SOFR rates, (b) adjusting the tenor structure, and (c) handling the backward-looking nature of compounded rates. Does the fundamental mathematical structure of the model change?

??? success "Solution to Exercise 7"
    **Key modifications for post-LIBOR (RFR-based) LMM:**

    **(a) Replacing forward LIBOR with forward compounded SOFR rates:**

    LIBOR is a single forward-looking rate fixed at $T_i$. SOFR-based rates are backward-looking compounded averages:

    $$
    \bar{R}_i = \frac{1}{\delta_i}\left[\prod_{k \in [T_i, T_{i+1}]}\left(1 + r_k \delta_k^{\text{daily}}\right) - 1\right]
    $$

    where $r_k$ are daily SOFR fixings. The forward compounded rate is:

    $$
    \bar{R}_i(t) = \frac{1}{\delta_i}\left(\frac{P(t, T_i)}{P(t, T_{i+1})} - 1\right)
    $$

    This has the **same functional form** as the forward LIBOR rate in terms of bond prices. The difference is that $\bar{R}_i$ is only fully observed at $T_{i+1}$ (not $T_i$), since it depends on daily fixings throughout the accrual period.

    **(b) Adjusting the tenor structure:**

    - SOFR is an overnight rate, so the natural compounding frequency is daily
    - However, interest rate swaps and derivatives reference term SOFR rates or compounded SOFR over standard periods (1M, 3M, 6M)
    - The tenor structure $\{T_0, T_1, \ldots, T_n\}$ remains similar, but the accrual conventions change
    - The model may need to incorporate more granular tenor spacing to capture the daily compounding effect

    **(c) Handling the backward-looking nature:**

    - LIBOR: fixed at the beginning of the accrual period ($T_i$), paid at the end ($T_{i+1}$). The rate is known when the period starts.
    - SOFR compounded rate: determined by fixings throughout $[T_i, T_{i+1}]$, known only at $T_{i+1}$.
    - This affects:
        - **Convexity adjustments:** The payment timing is the same ($T_{i+1}$), but the rate observation occurs throughout the period rather than at the start. This introduces timing convexity.
        - **Hedging:** Since the rate is not known at $T_i$, hedging instruments must account for the uncertainty of daily fixings during the accrual period.
        - **Caplet payoffs:** A SOFR caplet pays $\delta_i\max(\bar{R}_i - K, 0)$ at $T_{i+1}$, but $\bar{R}_i$ is not known until $T_{i+1}$, so the exercise decision and payoff are simultaneous.

    **Does the fundamental mathematical structure change?**

    **No.** The core LMM structure is preserved:

    - The forward compounded rate $\bar{R}_i(t) = \frac{1}{\delta_i}\left(\frac{P(t,T_i)}{P(t,T_{i+1})} - 1\right)$ has the same bond-price representation as forward LIBOR
    - Under $\mathbb{Q}^{T_{i+1}}$, $\bar{R}_i(t)$ is a martingale for $t \leq T_i$
    - Lognormal dynamics can be assumed: $d\bar{R}_i/\bar{R}_i = \sigma_i\,dW_i^{T_{i+1}}$
    - The drift corrections under terminal/spot measures retain the same form
    - Caplet pricing via Black's formula remains valid for $t \leq T_i$

    The main mathematical subtlety is that for $T_i < t < T_{i+1}$, the forward rate $\bar{R}_i(t)$ partially fixes as daily SOFR values are observed, requiring a different treatment of the "in-progress" rate. This is a modeling detail rather than a structural change.
