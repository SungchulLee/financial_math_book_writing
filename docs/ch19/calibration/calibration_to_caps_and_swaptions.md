# Calibration to Caps and Swaptions

Caps and swaptions are the two primary families of liquid interest rate options, and together they provide the market information needed to pin down the volatility and correlation parameters of term structure models. A model that correctly reprices vanilla caps and swaptions can then be used with some confidence for exotic products. This section develops the mathematical machinery for extracting caplet volatilities from cap quotes, describes the swaption volatility cube, and presents global and local calibration strategies with their trade-offs.

---

## Market Data and Quoting Conventions

### Cap Quotes

The market quotes interest rate caps in terms of **flat (cap) implied volatilities**. For a cap with strike $K$ and maturity $T_n$, a single number $\sigma_{\text{flat}}(K, T_n)$ is reported. This is the constant Black volatility that, when applied uniformly to every constituent caplet, reproduces the cap price:

$$
C^{\text{mkt}}(K, T_n) = \sum_{i=1}^{n-1} \text{Caplet}_i(K, \sigma_{\text{flat}})
$$

The flat volatility is a market convention, not a model parameter. The underlying caplet volatilities $\sigma_1, \sigma_2, \ldots, \sigma_{n-1}$ generally differ from one another.

### Swaption Quotes

Swaptions are quoted on an **expiry-tenor grid**. A swaption with expiry $T_0$ and tenor $T_n - T_0$ is quoted as a Black (lognormal) or Bachelier (normal) implied volatility:

$$
\sigma_{\text{swpn}}(\text{expiry}, \text{tenor}, K)
$$

The full collection of quotes across expiries, tenors, and strikes forms the **swaption volatility cube**.

### ATM Volatility Grid

The most liquid data consists of ATM volatilities on the standard grid:

| Expiry \ Tenor | 1Y | 2Y | 5Y | 7Y | 10Y | 15Y | 20Y | 30Y |
|---|---|---|---|---|---|---|---|---|
| 1M | | | | | | | | |
| 3M | | | | | | | | |
| 6M | | | | | | | | |
| 1Y | | | | | | | | |
| 2Y | | | | | | | | |
| 5Y | | | | | | | | |
| 10Y | | | | | | | | |

Each cell contains $\sigma_{\text{swpn}}$. Smile information adds a third dimension (strike).

---

## Stripping Caplet Volatilities from Cap Quotes

### The Bootstrap Procedure

Given cap flat volatilities $\sigma_{\text{flat}}(T_1), \sigma_{\text{flat}}(T_2), \ldots, \sigma_{\text{flat}}(T_n)$ for caps of increasing maturity, the individual **spot (caplet) volatilities** $\sigma_1, \sigma_2, \ldots$ are extracted sequentially.

**Step 1.** The shortest cap consists of a single caplet. Its flat volatility directly gives the first caplet volatility:

$$
\sigma_1 = \sigma_{\text{flat}}(T_1)
$$

**Step 2.** For the cap with maturity $T_k$ (containing caplets $1, \ldots, k-1$), all caplet volatilities $\sigma_1, \ldots, \sigma_{k-2}$ are already known. The cap price must satisfy:

$$
\sum_{i=1}^{k-1} \text{Caplet}_i(\sigma_i) = \sum_{i=1}^{k-1} \text{Caplet}_i(\sigma_{\text{flat}}(T_k))
$$

Rearranging for the unknown $\sigma_{k-1}$:

$$
\text{Caplet}_{k-1}(\sigma_{k-1}) = \sum_{i=1}^{k-1} \text{Caplet}_i(\sigma_{\text{flat}}(T_k)) - \sum_{i=1}^{k-2} \text{Caplet}_i(\sigma_i)
$$

Since the Black caplet price is monotonically increasing in volatility, this equation has a unique solution for $\sigma_{k-1}$, found by numerical root-finding (Newton--Raphson or bisection).

**Step 3.** Repeat for each successive maturity.

### Formal Statement

!!! info "Proposition (Caplet Volatility Bootstrap)"
    Given a sequence of cap flat volatilities $\sigma_{\text{flat}}(T_1) \leq \sigma_{\text{flat}}(T_2) \leq \cdots \leq \sigma_{\text{flat}}(T_n)$ with associated cap prices $C_1, C_2, \ldots, C_n$, define the residual price

    $$
    R_k = C_k - \sum_{i=1}^{k-2} \text{Caplet}_i(\sigma_i)
    $$

    Then the caplet volatility $\sigma_{k-1}$ is the unique solution to $\text{Caplet}_{k-1}(\sigma_{k-1}) = R_k$, provided $R_k > 0$.

### Potential Issues

The bootstrap can fail or produce unreliable results when:

- **Negative residual prices** $R_k < 0$ arise from inconsistent cap quotes or interpolation artifacts
- **Very short-dated caplets** have tiny vega, making the inversion numerically unstable
- **Quote gaps** in the maturity spectrum require interpolation of flat volatilities before stripping

!!! warning "Numerical Stability"
    The stripped caplet volatilities amplify noise in the input cap volatilities. A small error in $\sigma_{\text{flat}}(T_k)$ is magnified because it must be absorbed entirely by the marginal caplet. Practitioners often smooth the resulting caplet volatility curve to remove spurious oscillations.

---

## Worked Example: Caplet Stripping

??? example "Bootstrap of Caplet Volatilities"

    **Market data:** ATM cap flat volatilities (USD, quarterly caplets, $\delta = 0.25$)

    | Cap Maturity | Flat Vol | Num Caplets |
    |---|---|---|
    | 1Y | 24.0% | 3 |
    | 2Y | 25.5% | 7 |
    | 3Y | 26.0% | 11 |

    Assume the forward curve is flat at $F = 4.5\%$ and the discount factors are $P(0, T_i) = e^{-0.04 T_i}$.

    **Step 1:** The 1Y cap has 3 caplets (at 3M, 6M, 9M fixing). With flat vol $\sigma = 24.0\%$:

    $C_{\text{1Y}} = \sum_{i=1}^{3} \text{Caplet}_i(24.0\%)$

    Each caplet at $K_{\text{ATM}} = 4.5\%$ with $\sigma = 24.0\%$ and $T_i = 0.25, 0.50, 0.75$.

    For the shortest cap, the stripping gives $\sigma_1 = \sigma_2 = \sigma_3 = 24.0\%$ (a common simplification when only the aggregate cap is available).

    **Step 2:** The 2Y cap adds caplets 4 through 7. Using the cap price at 25.5\% flat vol:

    $R_{\text{2Y}} = C_{\text{2Y}}(25.5\%) - \sum_{i=1}^{3}\text{Caplet}_i(24.0\%)$

    The residual is allocated to caplets 4--7. If only one marginal caplet were unknown, we solve directly. With multiple unknowns, a common approach is to assume caplets 4--7 share the same marginal vol $\sigma_{\text{marginal}}$, then solve:

    $\sum_{i=4}^{7} \text{Caplet}_i(\sigma_{\text{marginal}}) = R_{\text{2Y}}$

    Numerical solution yields $\sigma_{\text{marginal}} \approx 27.1\%$.

    **Result:** The caplet volatility curve is **humped**, rising from 24.0% in the short end to about 27.1% in the 1--2Y region. This is the typical shape observed in USD markets.

---

## The Swaption Volatility Cube

### Structure

The swaption volatility cube is a three-dimensional object:

$$
\sigma_{\text{swpn}} = \sigma_{\text{swpn}}(T_{\text{expiry}}, T_{\text{tenor}}, K)
$$

- **Expiry dimension:** From 1 month to 30 years
- **Tenor dimension:** From 1 year to 30 years
- **Strike dimension:** From deep OTM receivers to deep OTM payers

### ATM Slice

The ATM slice $\sigma_{\text{swpn}}(T_{\text{expiry}}, T_{\text{tenor}}, K_{\text{ATM}})$ is the most liquid and forms a two-dimensional surface. Typical features:

- **Humped term structure:** Volatility initially rises with expiry, then declines for very long expiries
- **Tenor effect:** Short-tenor swaptions (e.g., 1Y into 1Y) often have higher vol than long-tenor (1Y into 30Y) due to diversification among forward rates
- **Decorrelation at long tenors:** As tenor increases, more forward rates contribute to the swap rate, and imperfect correlation reduces the aggregate volatility

### Smile Slice

At each (expiry, tenor) point, the strike dimension reveals:

- **Skew:** Receiver swaptions (low strikes) may have higher vol than payer swaptions (high strikes), or vice versa
- **Smile:** Both wings may trade at higher vol than ATM
- **SABR parameterization:** The market-standard approach fits the SABR model to each (expiry, tenor) smile:

$$
\sigma_B(K) = \frac{\alpha}{(S_0 K)^{(1-\beta)/2}} \cdot \frac{z}{x(z)} \cdot \left[1 + \left(\frac{(1-\beta)^2}{24}\frac{\alpha^2}{(S_0 K)^{1-\beta}} + \frac{\rho\beta\nu\alpha}{4(S_0 K)^{(1-\beta)/2}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
$$

where $z = \frac{\nu}{\alpha}(S_0 K)^{(1-\beta)/2}\ln(S_0/K)$ and $x(z) = \ln\left(\frac{\sqrt{1-2\rho z+z^2}+z-\rho}{1-\rho}\right)$.

---

## Global vs Local Calibration Strategies

### Local Calibration

In **local (instrument-by-instrument) calibration**, the model is calibrated to a selected subset of instruments, typically one at a time or in small groups:

**Advantages:**

- Exact fit to the chosen instruments
- Simple implementation (sequential root-finding)
- Fast execution

**Disadvantages:**

- No guarantee of consistency across instruments
- Different products calibrated separately may imply contradictory parameters
- Out-of-sample instruments may be poorly priced

### Global Calibration

In **global calibration**, the model parameters are chosen to minimize a weighted objective function across all available instruments simultaneously:

$$
\min_{\theta} \sum_{i \in \text{caps}} w_i^c \left(\sigma_i^{\text{model}}(\theta) - \sigma_i^{\text{mkt}}\right)^2 + \sum_{j \in \text{swaptions}} w_j^s \left(\sigma_j^{\text{model}}(\theta) - \sigma_j^{\text{mkt}}\right)^2
$$

where $\theta$ denotes the full parameter vector (volatilities, correlations, mean reversion, etc.).

**Advantages:**

- Consistent parameter set across all instruments
- Better out-of-sample behavior
- Statistically optimal use of market information

**Disadvantages:**

- No single instrument is priced exactly
- Computationally expensive (requires iterative optimization)
- Sensitive to the choice of weights $w_i$

### Weighting Schemes

The weights $w_i$ and $w_j$ in the global objective function can be chosen as:

- **Uniform weights:** All instruments contribute equally
- **Vega-weighted:** $w_i = 1/\mathcal{V}_i^2$, so each instrument contributes equally in terms of price error rather than vol error
- **Liquidity-weighted:** More weight on liquid instruments with tighter bid-ask spreads
- **Instrument-specific:** Higher weight on instruments that the desk trades actively

!!! tip "Practical Recommendation"
    A common approach is to calibrate caplet volatilities first (these are essentially model-independent in the LMM), then fit the correlation structure to swaptions holding caplet vols fixed. This **sequential two-step procedure** combines the exactness of local calibration for caps with the consistency of global calibration for correlations.

---

## Calibration in Specific Models

### Hull--White (One-Factor)

The Hull--White model has two parameters: mean reversion $\kappa$ and volatility $\sigma$ (or a time-dependent $\sigma(t)$).

**To caps:** With piecewise-constant $\sigma(t)$, caplet prices via the bond option formula can be matched exactly by choosing $\sigma(t)$ period by period. This is analogous to caplet stripping.

**To swaptions:** One-factor models have limited ability to match the full swaption matrix because all bond prices are driven by a single factor. Calibrating to co-terminal swaptions (fixed final maturity) is common.

### LIBOR Market Model (LMM)

The LMM has forward rate volatilities $\sigma_i(t)$ and correlations $\rho_{ij}$:

**To caps (exact):** Each caplet depends only on $\sigma_i$, so caplet volatilities from the bootstrap directly determine the forward rate volatilities:

$$
\sigma_i^{\text{Black}} = \sqrt{\frac{1}{T_i}\int_0^{T_i} \sigma_i(t)^2 \, dt}
$$

**To swaptions (approximate):** Using Rebonato's formula:

$$
\sigma_S^2 T_\alpha = \sum_{i,j} \frac{w_i w_j L_i(0) L_j(0)}{S(0)^2} \rho_{ij} \int_0^{T_\alpha} \sigma_i(t) \sigma_j(t) \, dt
$$

the swaption volatility depends on the correlation parameters $\rho_{ij}$, which are then optimized to match market swaption volatilities.

### Multi-Factor Short-Rate Models

Models such as the two-factor Hull--White (G2++) have additional parameters that improve the fit to the swaption matrix but introduce correlation and identifiability challenges.

---

## The Joint Calibration Problem

### Why Caps and Swaptions Together

Neither caps nor swaptions alone determine the model:

- **Caps** pin down individual forward rate volatilities but provide no information about correlations
- **Swaptions** depend on both volatilities and correlations, but cannot disentangle them without cap information

Together they determine the full volatility-correlation structure.

### Mathematical Formulation

For the LMM, the joint calibration seeks parameters $\theta = (\sigma_i(t), \rho_{ij})$ to solve:

$$
\min_{\theta} \; \mathcal{L}(\theta) = \sum_{k} w_k^c \left(\sigma_k^{\text{caplet,model}}(\theta) - \sigma_k^{\text{caplet,mkt}}\right)^2 + \sum_{m} w_m^s \left(\sigma_m^{\text{swpn,model}}(\theta) - \sigma_m^{\text{swpn,mkt}}\right)^2
$$

subject to the constraint that $\rho$ is positive semi-definite.

### Sequential Approach

A widely-used sequential strategy:

1. **Strip caplet volatilities** from the cap curve (exact, model-independent)
2. **Choose a volatility parameterization** $\sigma_i(t)$ consistent with the stripped caplet vols
3. **Calibrate the correlation matrix** $\rho_{ij}$ (within a parametric family) to match swaption volatilities via Rebonato's formula
4. **Verify** that the resulting parameters re-price all caps and swaptions within tolerance

### Objective Function Landscape

!!! warning "Non-Convexity"
    The calibration objective function is generally non-convex, with multiple local minima. Gradient-based optimizers (Levenberg--Marquardt, BFGS) require good initial guesses. Common practices include:

    - Starting from historically calibrated parameters
    - Using grid search for low-dimensional parameter spaces
    - Applying penalty terms for parameter stability across calibration dates

---

## Worked Example: Joint Calibration

??? example "Sequential Cap-Swaption Calibration"

    **Given market data:**

    - Stripped caplet vols: $\sigma_1 = 22\%$, $\sigma_2 = 24\%$, $\sigma_3 = 25\%$, $\sigma_4 = 23\%$
    - Forward rates: $L_1(0) = 4.0\%$, $L_2(0) = 4.2\%$, $L_3(0) = 4.5\%$, $L_4(0) = 4.3\%$
    - Target swaption vol for 1Y into 4Y: $\sigma_S^{\text{mkt}} = 22.0\%$, expiry $T = 1.0$

    **Step 1:** Caplet vols are given. Set $\sigma_i(t) = \sigma_i$ (constant).

    **Step 2:** Compute annuity weights. With equal spacing $\delta = 1$ and flat discounting:

    $w_i = \delta P(0, T_{i+1}) / A(0)$

    For simplicity assume $w_1 = 0.26$, $w_2 = 0.25$, $w_3 = 0.25$, $w_4 = 0.24$ and $S(0) = 4.25\%$.

    **Step 3:** Use Rebonato's formula with exponential correlation $\rho_{ij} = e^{-\beta|i-j|}$:

    $\sigma_S^2 \times 1.0 = \sum_{i,j} \frac{w_i w_j L_i L_j}{S^2}\rho_{ij}\sigma_i\sigma_j \times 1.0$

    **Step 4:** Vary $\beta$ until $\sigma_S = 22.0\%$:

    - $\beta = 0$: $\sigma_S \approx 23.5\%$ (perfect correlation, too high)
    - $\beta = 0.15$: $\sigma_S \approx 22.1\%$ (close)
    - $\beta = 0.16$: $\sigma_S \approx 22.0\%$ (match)

    **Result:** The calibrated decorrelation parameter is $\beta \approx 0.16$, giving correlation $\rho_{ij} = e^{-0.16|i-j|}$ between adjacent forward rates of approximately 0.85.

---

## Calibration Quality Assessment

### In-Sample Fit

Report the pricing errors for all calibration instruments:

$$
\epsilon_i = \sigma_i^{\text{model}} - \sigma_i^{\text{mkt}}
$$

Typical targets:

- **Caps:** Errors below 0.5 bps (effectively exact in the LMM)
- **ATM swaptions:** Errors below 1--2 bps (vol) for the main grid points
- **OTM swaptions:** Larger errors acceptable (3--5 bps) due to smile model limitations

### Out-of-Sample Validation

Test the calibrated model on instruments not included in calibration:

- Interpolated swaptions (non-standard expiries or tenors)
- CMS products (sensitive to correlations)
- Bermudan swaptions (sensitive to multi-factor dynamics)

### Stability

A good calibration should be **stable across time**: small changes in market data should produce small changes in calibrated parameters. Day-to-day parameter jumps indicate overfitting or identifiability problems.

---

## Key Takeaways

- **Cap calibration** proceeds by stripping caplet volatilities from flat cap volatility quotes via a sequential bootstrap
- **Swaption calibration** targets the volatility cube and requires fitting correlation parameters (in the LMM) or multi-factor dynamics (in short-rate models)
- **Global calibration** (weighted least squares across all instruments) provides consistency but no exact fit; **local calibration** provides exact fit to selected instruments but may be inconsistent
- The **sequential two-step approach** (strip caps exactly, then fit correlations to swaptions) is the standard LMM workflow
- The calibration objective is **non-convex**, requiring careful initialization and regularization
- **Calibration quality** is assessed via in-sample errors, out-of-sample validation, and parameter stability

---

## Further Reading

- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapters 6--7
- Rebonato (2002), *Modern Pricing of Interest-Rate Derivatives*, Chapters 8--10
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volumes II--III
- Hagan et al. (2002), "Managing Smile Risk" (SABR calibration)

---

## Exercises

**Exercise 1.** Consider a market that quotes ATM cap flat volatilities of 22.0% for the 1Y cap (containing 3 quarterly caplets) and 24.5% for the 2Y cap (containing 7 quarterly caplets). Assume a flat forward curve at $F = 5.0\%$ and discount factors $P(0, T_i) = e^{-0.045 T_i}$. Describe in detail the bootstrap procedure to extract the marginal caplet volatility for the 1Y--2Y region. Explain under what conditions the residual price $R_k$ can become negative, and what this implies about the input data.

---

**Exercise 2.** In the caplet bootstrap, the stripped caplet volatility $\sigma_{k-1}$ satisfies $\text{Caplet}_{k-1}(\sigma_{k-1}) = R_k$. Show that this equation has a unique solution for $\sigma_{k-1} > 0$ provided $R_k > 0$, by arguing that the Black caplet price is a strictly increasing, continuous function of volatility mapping $(0, \infty) \to (0, \text{intrinsic value})$.

---

**Exercise 3.** Suppose the swaption volatility cube reports $\sigma_{\text{swpn}}(2Y, 5Y, K_{\text{ATM}}) = 18.5\%$ and $\sigma_{\text{swpn}}(5Y, 5Y, K_{\text{ATM}}) = 16.0\%$. Explain why the ATM volatility typically decreases as the expiry lengthens for a fixed tenor. Relate your answer to the **humped term structure** of forward rate volatilities and the diversification effect across forward rates.

---

**Exercise 4.** In a global calibration, the objective function is

$$
\min_{\theta} \sum_{i} w_i^c (\sigma_i^{\text{model}} - \sigma_i^{\text{mkt}})^2 + \sum_{j} w_j^s (\sigma_j^{\text{model}} - \sigma_j^{\text{mkt}})^2
$$

Derive the form of vega-weighted weights $w_i = 1/\mathcal{V}_i^2$ and explain why this choice ensures each instrument contributes equally in terms of **price error** rather than volatility error. What is the potential drawback of uniform weighting?

---

**Exercise 5.** In the Hull--White one-factor model with piecewise-constant volatility $\sigma(t)$, explain why calibration to the full swaption matrix is fundamentally limited. In particular, show that all zero-coupon bond prices $P(t, T)$ can be written as functions of a single state variable $r(t)$, and argue why this implies that swaption correlations are perfectly correlated in this model.

---

**Exercise 6.** Using Rebonato's approximate swaption volatility formula

$$
\sigma_S^2 T_\alpha = \sum_{i,j} \frac{w_i w_j L_i(0) L_j(0)}{S(0)^2} \rho_{ij} \int_0^{T_\alpha} \sigma_i(t) \sigma_j(t) \, dt
$$

consider 3 forward rates with $L_1(0) = L_2(0) = L_3(0) = 4\%$, equal weights $w_i = 1/3$, constant volatilities $\sigma_i = 20\%$, and exponential correlation $\rho_{ij} = e^{-\beta|i-j|}$. Compute the model swaption volatility $\sigma_S$ for $\beta = 0$ (perfect correlation) and $\beta = 0.3$. Verify that decorrelation reduces the swaption volatility.

---

**Exercise 7.** A practitioner calibrates the LMM to caps on Monday and obtains caplet volatilities $\sigma_1 = 22\%$, $\sigma_2 = 25\%$, $\sigma_3 = 24\%$. On Tuesday, a single cap quote shifts by 0.5 bps. After re-calibration, $\sigma_2$ changes by 3\%. Discuss whether this behavior indicates a stable or unstable calibration. What regularization techniques could improve stability? How does the sequential two-step approach (strip caps, then fit correlations) help isolate the source of instability?
