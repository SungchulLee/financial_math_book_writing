# Volatility Structure Calibration


Beyond fitting today’s curve, interest-rate models must specify and calibrate a **volatility structure** that governs the dynamics of rates and prices of interest-rate options.

---

## What is being calibrated?


Depending on the model, calibration targets include:

- short-rate volatility parameters,
- forward-rate volatilities (HJM),
- cap/floor and swaption implied volatilities.

The volatility structure determines smile, skew, and term-structure dynamics.

---

## Typical calibration instruments


Common calibration instruments are:

- caplets and floorlets,
- caps/floors across maturities,
- swaptions across expiries and tenors.

These instruments are liquid and sensitive to rate volatility.

---

## Model-dependent considerations


- **Short-rate models:** limited flexibility, often need extensions or multi-factor versions.
- **HJM models:** volatility functions calibrated directly to market data.
- **Market models (LMM):** volatilities tied to forward LIBOR rates.

Model choice strongly affects calibration quality.

---

## Regularization and smoothing


Volatility calibration is an inverse problem and often ill-posed.
Stability is improved by:

- smoothness penalties across maturity,
- parsimonious parametrizations,
- restricting factor dimensionality.

Overfitting leads to poor out-of-sample behavior.

---

## Key takeaways


- Volatility structure drives option prices and dynamics.
- Calibration relies on caps and swaptions.
- Regularization is essential for stable volatility surfaces.

---

## Further reading


- Rebonato, *Interest-Rate Option Models*.
- Brigo & Mercurio, volatility calibration.

---

## Exercises

**Exercise 1.** A one-factor Hull--White model has volatility parameter $\sigma$ and mean-reversion speed $a$. You observe at-the-money caplet implied volatilities for maturities 1Y through 10Y. Explain why a single constant $\sigma$ cannot reproduce a humped caplet volatility term structure and describe the minimal extension (e.g., piecewise-constant $\sigma(t)$) needed to fit the observed caplet volatilities exactly.

??? success "Solution to Exercise 1"
    In the one-factor Hull--White model, the short-rate volatility $\sigma$ and mean-reversion speed $a$ determine the caplet implied volatility through the bond option formula. The model-implied Black caplet volatility for a caplet fixing at time $T$ with payment at $T + \delta$ is:

    $$
    \sigma_{\text{caplet}}^{\text{HW}}(T) = \sigma \cdot \frac{1 - e^{-a\delta}}{a} \cdot \sqrt{\frac{1 - e^{-2aT}}{2aT}}
    $$

    When $\sigma$ is a constant, this expression is a **monotonically decreasing** function of $T$ for typical values of $a > 0$. Specifically, the term $\sqrt{(1 - e^{-2aT})/(2aT)}$ decreases from 1 (as $T \to 0$) toward $1/\sqrt{2aT}$ for large $T$. This means the model can only produce a **downward-sloping** caplet volatility term structure.

    In reality, the market caplet volatility curve is typically **humped**: it rises from short maturities, peaks around 2--5 years, and then declines. A constant $\sigma$ cannot reproduce this hump because the model's caplet volatility is a strictly decreasing function of maturity once $a$ is fixed.

    **Minimal extension:** The simplest extension is to allow $\sigma(t)$ to be **piecewise-constant** over time intervals aligned with caplet maturities:

    $$
    \sigma(t) = \sigma_k \quad \text{for } t \in [T_{k-1}, T_k)
    $$

    With this parameterization, the model-implied caplet volatility for each maturity depends on the volatility values in all preceding intervals:

    $$
    (\sigma_{\text{caplet}}^{\text{HW}}(T_k))^2 \propto \sum_{j=1}^{k} \sigma_j^2 \cdot g_j(a, T_k)
    $$

    where $g_j$ are known functions of $a$ and the time grid. By choosing $\sigma_k$ sequentially (stripping from short to long maturities), one can match each caplet volatility exactly, including the hump. This gives $n-1$ free parameters for $n-1$ caplet volatilities, providing an exact fit.

---

**Exercise 2.** Suppose the market quotes at-the-money cap volatilities (flat volatilities) for maturities $T = 2, 3, 5, 7, 10$ years. Describe the stripping procedure to extract individual caplet volatilities from these flat cap volatilities. If the 5Y flat cap volatility is 18.5% and the 3Y flat cap volatility is 17.0%, is it possible for all caplet volatilities between years 3 and 5 to be below 17.0%? Justify your answer.

??? success "Solution to Exercise 2"
    **Stripping procedure:**

    A flat cap volatility $\sigma_{\text{flat}}(T)$ means that the cap price equals the sum of caplet prices when each caplet uses the same Black volatility $\sigma_{\text{flat}}(T)$:

    $$
    C(T) = \sum_{i=1}^{n(T)} \text{Caplet}_i(\sigma_{\text{flat}}(T))
    $$

    To extract individual caplet volatilities from flat cap volatilities:

    1. **3Y cap:** Using $\sigma_{\text{flat}}(3\text{Y}) = 17.0\%$, compute the 3Y cap price $C_{3Y}$. The caplet volatilities for years 1--3 are extracted (or if only the 3Y flat vol is the first data point, all caplets up to 3Y share this vol, or one uses shorter caps if available).

    2. **5Y cap:** Compute $C_{5Y}$ using $\sigma_{\text{flat}}(5\text{Y}) = 18.5\%$. The residual price for the 3Y--5Y caplets is:

    $$
    R = C_{5Y}(\sigma_{\text{flat}} = 18.5\%) - \sum_{i=1}^{n(3Y)} \text{Caplet}_i(\sigma_i^{\text{stripped}})
    $$

    3. The marginal caplets (years 3--5) must absorb this residual. Their caplet volatilities are found by solving:

    $$
    \sum_{i \in [3Y,5Y]} \text{Caplet}_i(\sigma_i) = R
    $$

    **Can all caplet volatilities between years 3 and 5 be below 17.0%?**

    **No.** Here is the argument. The 5Y flat vol (18.5%) is higher than the 3Y flat vol (17.0%). This means the 5Y cap price is **more than proportionally** larger than the 3Y cap price. Formally, the residual $R$ satisfies:

    $$
    R = C_{5Y}(18.5\%) - C_{3Y}(17.0\%) > C_{5Y}(17.0\%) - C_{3Y}(17.0\%)
    $$

    The right-hand side equals $\sum_{i \in [3Y,5Y]} \text{Caplet}_i(17.0\%)$, which is the price of the marginal caplets at 17.0% vol. Since $R$ exceeds this amount, the marginal caplets must be priced at a volatility **higher** than 17.0% on average. Therefore it is impossible for all marginal caplet volatilities to be below 17.0%. At least some (and in fact the weighted average) must exceed 17.0%.

    This is consistent with the rising flat cap volatility curve: as the flat vol increases from 3Y to 5Y, the incremental caplets must have higher-than-average volatilities to pull the flat average upward.

---

**Exercise 3.** In the LIBOR Market Model, the instantaneous volatility of forward rate $L_i$ is given by a function $\sigma_i(t)$ of time. Consider the abcd parameterization

$$
\sigma_i(t) = \bigl(a + b(T_i - t)\bigr)e^{-c(T_i - t)} + d
$$

Derive the model Black caplet volatility

$$
v_i^2 = \frac{1}{T_i}\int_0^{T_i} \sigma_i(t)^2\,dt
$$

as a closed-form expression in $(a,b,c,d)$. Verify that for $b = 0$ and $c = 0$ the caplet volatility reduces to $v_i = a + d$.

??? success "Solution to Exercise 3"
    The model Black caplet volatility for forward rate $L_i$ under the abcd parameterization is:

    $$
    v_i^2 = \frac{1}{T_i}\int_0^{T_i} \bigl[(a + b(T_i - t))e^{-c(T_i - t)} + d\bigr]^2\,dt
    $$

    Substituting $\tau = T_i - t$ (so $d\tau = -dt$, and limits change from $\tau = T_i$ to $\tau = 0$):

    $$
    v_i^2 = \frac{1}{T_i}\int_0^{T_i} \bigl[(a + b\tau)e^{-c\tau} + d\bigr]^2\,d\tau
    $$

    Expanding the square:

    $$
    \bigl[(a+b\tau)e^{-c\tau} + d\bigr]^2 = (a+b\tau)^2 e^{-2c\tau} + 2d(a+b\tau)e^{-c\tau} + d^2
    $$

    **Term 1:** $(a+b\tau)^2 e^{-2c\tau} = (a^2 + 2ab\tau + b^2\tau^2)e^{-2c\tau}$

    Using standard integrals $\int_0^T \tau^n e^{-\alpha\tau}\,d\tau$:

    $$
    \int_0^T e^{-2c\tau}\,d\tau = \frac{1 - e^{-2cT}}{2c}
    $$

    $$
    \int_0^T \tau e^{-2c\tau}\,d\tau = \frac{1}{(2c)^2}\bigl(1 - (1+2cT)e^{-2cT}\bigr)
    $$

    $$
    \int_0^T \tau^2 e^{-2c\tau}\,d\tau = \frac{1}{(2c)^3}\bigl(2 - (2 + 4cT + 4c^2T^2)e^{-2cT}\bigr)
    $$

    **Term 2:** $2d(a+b\tau)e^{-c\tau}$ uses the same formulas with $2c$ replaced by $c$.

    **Term 3:** $\int_0^T d^2\,d\tau = d^2 T$.

    The full closed-form expression is:

    $$
    v_i^2 = \frac{1}{T_i}\Biggl[a^2 \frac{1-e^{-2cT_i}}{2c} + 2ab\frac{1-(1+2cT_i)e^{-2cT_i}}{4c^2} + b^2\frac{2-(2+4cT_i+4c^2T_i^2)e^{-2cT_i}}{8c^3}
    $$

    $$

    + 2da\frac{1-e^{-cT_i}}{c} + 2db\frac{1-(1+cT_i)e^{-cT_i}}{c^2} + d^2 T_i\Biggr]
    $$

    **Verification for $b = 0$, $c = 0$:**

    When $b = 0$, $\sigma_i(t) = a\,e^{-c(T_i - t)} + d$. When additionally $c = 0$ (taking the limit $c \to 0$), $e^{-c\tau} \to 1$, so $\sigma_i(t) = a + d$ (a constant). Then:

    $$
    v_i^2 = \frac{1}{T_i}\int_0^{T_i}(a+d)^2\,d\tau = (a+d)^2
    $$

    Hence $v_i = |a + d| = a + d$ (assuming $a + d > 0$), as required.

---

**Exercise 4.** A trader calibrates a two-factor HJM model with volatility functions $\sigma_1(t,T) = \sigma_1 e^{-\kappa_1(T-t)}$ and $\sigma_2(t,T) = \sigma_2 e^{-\kappa_2(T-t)}$ to a grid of swaption prices. The calibrated parameters are $\sigma_1 = 1.2\%$, $\kappa_1 = 0.05$, $\sigma_2 = 0.8\%$, $\kappa_2 = 0.50$. Interpret each factor economically (level vs curvature). Explain how the two factors combine to produce a richer volatility term structure than a single-factor model.

??? success "Solution to Exercise 4"
    **Economic interpretation of the two factors:**

    - **Factor 1** ($\sigma_1 = 1.2\%$, $\kappa_1 = 0.05$): This factor has a **large volatility** and a **small mean-reversion speed**. The low decay rate $\kappa_1 = 0.05$ means the volatility function $\sigma_1 e^{-\kappa_1(T-t)}$ decays very slowly with maturity. This factor represents **parallel (level) shifts** in the yield curve --- movements that affect all maturities approximately equally. It dominates the long end of the curve.

    - **Factor 2** ($\sigma_2 = 0.8\%$, $\kappa_2 = 0.50$): This factor has a **smaller volatility** but a **much faster decay**. The function $\sigma_2 e^{-\kappa_2(T-t)}$ decays rapidly, meaning this factor has a strong effect on short-maturity rates but negligible impact on long maturities. This factor represents **slope or curvature** movements --- it tilts the short end relative to the long end.

    **How the two factors produce a richer volatility structure:**

    The total variance of a zero-coupon bond at maturity $T$ involves contributions from both factors:

    $$
    \text{Var}[\ln P(t,T)] \propto \sigma_1^2 \frac{(1-e^{-\kappa_1(T-t)})^2}{\kappa_1^2} + \sigma_2^2 \frac{(1-e^{-\kappa_2(T-t)})^2}{\kappa_2^2}
    $$

    - For **short maturities** ($T - t$ small), both factors contribute significantly, and the fast-decaying factor 2 adds extra short-end volatility.
    - For **long maturities**, factor 1 dominates because factor 2 has decayed to near zero.

    The resulting volatility term structure can be **humped**: rising initially (both factors active) and then declining (only factor 1 remains). A single-factor model with one exponential decay can only produce a monotonically shaped volatility curve, unable to capture the hump. The two-factor model also generates **imperfect correlations** between forward rates at different maturities, which is critical for pricing swaptions and other correlation-sensitive products.

---

**Exercise 5.** You are given a $5 \times 5$ swaption volatility matrix (expiries: 1Y, 2Y, 3Y, 5Y, 7Y; tenors: 1Y, 2Y, 3Y, 5Y, 7Y). Describe a calibration strategy that first targets the ATM diagonal (expiry = tenor) and then uses residual degrees of freedom to match off-diagonal entries. Why might the off-diagonal swaptions be harder to fit, and what does a poor off-diagonal fit reveal about the correlation structure?

??? success "Solution to Exercise 5"
    **Calibration strategy targeting the ATM diagonal first:**

    1. **Diagonal calibration:** The ATM diagonal consists of swaptions where expiry equals tenor: $1\text{Y}\times 1\text{Y}$, $2\text{Y}\times 2\text{Y}$, $3\text{Y}\times 3\text{Y}$, $5\text{Y}\times 5\text{Y}$, $7\text{Y}\times 7\text{Y}$. These swaptions are often co-terminal (or close to it) and span a range of expiries. Calibrate the primary model parameters (forward rate volatilities, or the abcd parameters, and one or two correlation parameters) to match these diagonal entries first. This anchors the overall volatility level and its term structure.

    2. **Off-diagonal fitting:** With the core parameters fixed (or nearly fixed) from the diagonal, use residual degrees of freedom --- additional correlation parameters, time-dependent volatility adjustments, or multi-factor extensions --- to match off-diagonal entries such as $1\text{Y}\times 5\text{Y}$, $5\text{Y}\times 2\text{Y}$, etc.

    **Why off-diagonal swaptions are harder to fit:**

    Off-diagonal swaptions probe the **correlation structure** between forward rates more deeply than diagonal ones. A swaption with expiry $T_0$ and tenor $T_n - T_0$ depends on the joint behavior of forward rates $L_{k}$ for $k$ in the swap's coverage period. Specifically, Rebonato's formula shows:

    $$
    \sigma_S^2 T_0 = \sum_{i,j} \frac{w_i w_j L_i L_j}{S^2}\rho_{ij}\int_0^{T_0}\sigma_i(t)\sigma_j(t)\,dt
    $$

    - **Short-expiry, long-tenor** swaptions (e.g., $1\text{Y}\times 7\text{Y}$) depend on correlations among many forward rates, weighted by a broad set of $\rho_{ij}$. A simple parametric correlation (e.g., single-parameter exponential) may be too rigid.
    - **Long-expiry, short-tenor** swaptions (e.g., $7\text{Y}\times 1\text{Y}$) are nearly equivalent to caplets and mainly test the volatility level.

    A **poor off-diagonal fit** reveals that the assumed correlation structure is too restrictive. It indicates that the actual decorrelation pattern in the market is more complex than the parametric family can represent. For example, a single-parameter exponential correlation treats all pairs of forward rates at the same distance as equally correlated, which may not hold empirically. Upgrading to a two-parameter correlation model or an angle-based parameterization can improve the off-diagonal fit.

---

**Exercise 6.** Consider adding a smoothness penalty to the volatility calibration objective:

$$
\min_{\sigma(\cdot)} \sum_i w_i\bigl(V_i^{\text{model}} - V_i^{\text{mkt}}\bigr)^2 + \lambda \int_0^T \!\left(\frac{d^2\sigma}{dt^2}\right)^2 dt
$$

Explain the role of $\lambda$ and how you would choose it in practice. What happens if $\lambda$ is too large? What if it is too small?

??? success "Solution to Exercise 6"
    The regularized objective function is:

    $$
    \min_{\sigma(\cdot)} \sum_i w_i\bigl(V_i^{\text{model}} - V_i^{\text{mkt}}\bigr)^2 + \lambda \int_0^T \left(\frac{d^2\sigma}{dt^2}\right)^2 dt
    $$

    **Role of $\lambda$:**

    The parameter $\lambda \geq 0$ controls the trade-off between two competing objectives:

    - **First term** (data fidelity): penalizes deviations between model and market prices. Minimizing this alone yields the best possible fit to market data.
    - **Second term** (smoothness penalty): penalizes the curvature of $\sigma(t)$, measured by the squared second derivative. This discourages rapid oscillations in the volatility function.

    **Choosing $\lambda$ in practice:**

    - **Cross-validation:** Split the instruments into calibration and validation sets. Choose $\lambda$ to minimize the validation error.
    - **L-curve method:** Plot the data fidelity term versus the smoothness term for various $\lambda$. The optimal $\lambda$ lies at the "elbow" of this curve, balancing fit and smoothness.
    - **Discrepancy principle:** Set $\lambda$ so that the calibration residuals are comparable to the bid-ask uncertainty in market quotes (e.g., 0.5--1 bp in vol terms).

    **If $\lambda$ is too large:**

    The smoothness penalty dominates. The calibrated $\sigma(t)$ is forced to be nearly linear (minimal curvature), even at the cost of large pricing errors. Market features such as the volatility hump are smoothed away. In the extreme $\lambda \to \infty$, $\sigma(t)$ becomes a straight line (zero curvature), regardless of the data. This leads to **underfitting**: the model fails to capture the information in the market quotes.

    **If $\lambda$ is too small:**

    The data fidelity term dominates. The optimizer is free to introduce rapid oscillations in $\sigma(t)$ to match every market quote exactly. This can produce a volatility function with large spikes and dips between calibration maturities. Such **overfitting** leads to poor out-of-sample behavior: instruments not in the calibration set are mispriced, and Monte Carlo simulations using this $\sigma(t)$ produce unrealistic rate dynamics. Parameters become unstable across calibration dates.

---

**Exercise 7.** A practitioner observes that a calibrated volatility surface reprices all caps and swaptions within 0.5 bps but produces unrealistic forward-rate dynamics when used for Monte Carlo simulation of exotic products (e.g., CMS spread options). Explain why good static calibration does not guarantee good dynamic behavior and discuss at least two diagnostics the practitioner should perform to assess the quality of the calibrated dynamics.

??? success "Solution to Exercise 7"
    **Why good static calibration does not guarantee good dynamics:**

    Static calibration means the model reproduces today's market prices of European options (caps and swaptions) at time $t = 0$. This constrains the **marginal distributions** of forward rates (or swap rates) at their respective fixing dates. However, it does not constrain:

    1. **Joint distributions across time:** The correlation between rates at different times, which matters for path-dependent and early-exercise products.
    2. **Conditional distributions:** How rates evolve given information at intermediate times.
    3. **Smile dynamics:** Whether the model-implied smile moves realistically as the underlying rate changes (sticky strike vs. sticky delta behavior).

    A CMS spread option depends on the **joint distribution** of two swap rates (e.g., the 10Y rate and the 2Y rate) and their **correlation dynamics**. Two models can match all vanilla swaption prices identically yet produce very different CMS spread prices because they imply different correlations between the 10Y and 2Y rates.

    Furthermore, the model's **forward smile** --- the implied volatility surface at a future date as seen from today --- is not constrained by today's vanilla calibration. Different volatility and correlation structures consistent with today's static prices can produce vastly different forward smiles, leading to different prices for forward-starting and exotic options.

    **Diagnostics for assessing calibrated dynamics:**

    **Diagnostic 1: Forward smile analysis.** Compute the model-implied volatility smile at future dates (e.g., 1Y and 2Y forward) by simulating the model forward and pricing European options on each path. Compare the shape and level of these forward smiles against historical data or market-implied forward volatilities (from forward-starting options, if available). Unrealistic forward smiles (e.g., flat or inverted) signal problems with the dynamic specification.

    **Diagnostic 2: Terminal correlation analysis.** Compute the model-implied **terminal correlation** between pairs of swap rates (e.g., $\text{Corr}(S_{2Y}(T), S_{10Y}(T))$) from Monte Carlo simulation. Compare with historically realized correlations and with correlation levels implied by CMS spread option markets. A model that produces correlations near 1.0 (e.g., a one-factor model) will systematically misprice CMS spread options regardless of static fit quality.

    **Additional diagnostics** include: (i) checking the serial autocorrelation of model-implied rate changes (to detect unrealistic mean-reversion behavior), and (ii) pricing simple path-dependent payoffs (e.g., Asian-style rate averages) and comparing across alternative calibrations to gauge the sensitivity of exotic prices to dynamic assumptions.
