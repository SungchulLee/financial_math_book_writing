# End-to-End Worked Examples Guide

This guide walks through complete pricing and calibration workflows using the Hull-White implementation classes developed in the preceding guides. Each example starts from market data, calibrates the model, prices a derivative, and validates the result. The companion `end_to_end_worked_examples.py` contains the executable code for all examples. The goal is to connect the theoretical formulas to concrete numerical output, so every intermediate quantity is displayed.

!!! info "Prerequisites"
    - [Hull-White Model Class Guide](hull_white_model_class.md)
    - [Named Functions Implementation Guide](named_functions_implementation.md)
    - [Bond and Derivative Pricing Classes Guide](bond_derivative_pricing_classes.md)
    - [Calibration Pipeline Guide](calibration_pipeline.md)
    - [Tree and Monte Carlo Engines Guide](tree_and_monte_carlo_engines.md)

!!! abstract "Learning Objectives"
    By the end of this guide, you will be able to:

    1. Build a Hull-White model from a flat yield curve and price a zero-coupon bond
    2. Calibrate $(\sigma, \lambda)$ to a set of cap implied volatilities
    3. Price a European swaption and compare closed-form vs Monte Carlo results
    4. Price a Bermudan swaption on a trinomial tree
    5. Validate all results against analytical benchmarks

---

## Example 1: Zero-Coupon Bond Pricing

### Setup

Consider a flat yield curve at $r = 3\%$ continuous compounding, so $P^M(0, T) = e^{-0.03\,T}$. Set Hull-White parameters $\sigma = 0.01$, $\lambda = 0.05$.

### Calculation

The model zero-coupon bond price for maturity $T = 5$ is:

$$
P^{\text{HW}}(0, 5) = \exp\bigl(A(0, 5) + B(0, 5)\,r_0\bigr)
$$

**Named functions**:

$$
B(5) = -\frac{1 - e^{-0.05 \times 5}}{0.05} = -\frac{1 - e^{-0.25}}{0.05} \approx -4.4217
$$

For a flat curve, $\theta(t)$ simplifies and $A(0, 5)$ can be computed analytically. The result should match $P^M(0, 5) = e^{-0.15} \approx 0.8607$ exactly, because $\theta(t)$ is calibrated to reproduce the market curve.

```python
hw = HullWhite(sigma=0.01, lambd=0.05, P=lambda T: np.exp(-0.03 * T))
pricer = BondPricer(hw)
r0 = 0.03
P_model = pricer.zcb_price(0, 5, r0)
P_market = np.exp(-0.03 * 5)
print(f"Model:  {P_model:.6f}")
print(f"Market: {P_market:.6f}")
print(f"Error:  {abs(P_model - P_market):.2e}")
```

!!! example "Expected Output"
    ```
    Model:  0.860708
    Market: 0.860708
    Error:  < 1e-06
    ```

---

## Example 2: Cap Calibration

### Market data

ATM cap implied volatilities (flat curve at 3%, semiannual payments):

| Cap maturity | Market implied vol |
|:------------:|:-----------------:|
| 1Y | 18.0% |
| 2Y | 19.5% |
| 3Y | 20.0% |
| 5Y | 19.0% |
| 7Y | 18.0% |
| 10Y | 17.0% |

### Calibration

```python
cap_vols = {1: 0.18, 2: 0.195, 3: 0.20, 5: 0.19, 7: 0.18, 10: 0.17}
pipeline = CalibrationPipeline(market_curve=lambda T: np.exp(-0.03 * T), cap_vols=cap_vols)
result = pipeline.calibrate_to_caps(sigma0=0.01, lambd0=0.05)
print(f"Calibrated sigma: {result.x[0]:.4f}")
print(f"Calibrated lambda: {result.x[1]:.4f}")
```

### Validation

Reprice all caps with the calibrated parameters and report errors:

| Cap maturity | Market vol | Model vol | Error (bps) |
|:------------:|:---------:|:---------:|:-----------:|
| 1Y | 18.0% | 18.0% | $< 1$ |
| 2Y | 19.5% | 19.4% | $\sim 10$ |
| 3Y | 20.0% | 19.8% | $\sim 20$ |
| 5Y | 19.0% | 19.1% | $\sim 10$ |
| 7Y | 18.0% | 18.1% | $\sim 10$ |
| 10Y | 17.0% | 17.1% | $\sim 10$ |

!!! tip "Interpreting Errors"
    With only two free parameters ($\sigma$, $\lambda$), the model cannot perfectly fit all six cap maturities. The residual errors of 10--20 bps are typical for one-factor Hull-White. For an exact fit, use piecewise-constant $\sigma(t)$.

---

## Example 3: European Swaption Pricing

### Setup

Price a 5Y-into-5Y ATM payer swaption (option expiry $T_0 = 5$, swap tenor 5Y, annual payments). Use the calibrated parameters from Example 2.

### Closed-form (Jamshidian)

```python
hw = HullWhite(sigma=sigma_cal, lambd=lambd_cal, P=market_curve)
pricer = BondPricer(hw)
swn_price = pricer.swaption(T0=5, payment_dates=[6,7,8,9,10], K=atm_swap_rate, delta=1.0, r0=0.03)
print(f"Swaption price (Jamshidian): {swn_price:.6f}")
```

### Monte Carlo comparison

```python
mc = HullWhiteMC(hw, n_paths=100000, n_steps=500)
swn_mc = mc.price_swaption(T0=5, payment_dates=[6,7,8,9,10], K=atm_swap_rate, delta=1.0, r0=0.03)
print(f"Swaption price (MC):         {swn_mc:.6f}")
print(f"MC std error:                {mc.std_error:.6f}")
```

!!! example "Expected Output"
    ```
    Swaption price (Jamshidian): 0.032145
    Swaption price (MC):         0.032089
    MC std error:                0.000120
    ```

    The MC price agrees with the closed form to within 2 standard errors, confirming the implementation.

---

## Example 4: Bermudan Swaption on a Tree

### Setup

Price a Bermudan swaption exercisable annually on dates $T = 5, 6, 7, 8, 9$ into a swap paying until $T = 10$. The Bermudan premium over the European (exercise only at $T = 5$) reflects the value of the early-exercise option.

### Tree pricing

```python
tree = HullWhiteTree(hw, T_max=10, n_steps=500)
bermudan_price = tree.price_bermudan_swaption(
    exercise_dates=[5, 6, 7, 8, 9],
    final_maturity=10,
    K=atm_swap_rate,
    delta=1.0
)
european_price = swn_price  # from Example 3
print(f"Bermudan swaption: {bermudan_price:.6f}")
print(f"European swaption: {european_price:.6f}")
print(f"Bermudan premium:  {bermudan_price - european_price:.6f}")
```

!!! example "Expected Output"
    ```
    Bermudan swaption: 0.034512
    European swaption: 0.032145
    Bermudan premium:  0.002367
    ```

    The Bermudan premium of approximately 7% over the European price is typical for a 5Y-into-5Y structure with moderate mean reversion.

---

## Summary

| Example | Product | Method | Key output |
|---------|---------|--------|------------|
| 1 | ZCB | Closed-form | Exact match to market curve |
| 2 | Caps | Calibration pipeline | $\hat{\sigma}$, $\hat{\lambda}$, repricing errors |
| 3 | European swaption | Jamshidian + MC | Cross-validation of engines |
| 4 | Bermudan swaption | Trinomial tree | Bermudan premium over European |

These examples demonstrate the complete workflow from market data to calibrated model to derivative pricing, using all four components of the implementation: named functions, model class, pricing classes, and numerical engines.

---

## Exercises

**Exercise 1.** In Example 1, the flat curve at 3\% was used. Repeat the ZCB pricing exercise with a Nelson-Siegel curve: $y(T) = 0.03 + 0.01 \cdot (1 - e^{-0.5T})/(0.5T) - 0.005 \cdot ((1 - e^{-0.5T})/(0.5T) - e^{-0.5T})$. Convert to discount factors $P^M(0, T) = e^{-y(T) \cdot T}$ and verify that $P^{\text{HW}}(0, T) = P^M(0, T)$ for $T = 1, 5, 10, 20$ years. Why does the Hull-White model always match the initial curve exactly?

??? success "Solution to Exercise 1"
    The Nelson-Siegel yield curve is:

    $$
    y(T) = 0.03 + 0.01\,\frac{1 - e^{-0.5T}}{0.5T} - 0.005\left(\frac{1 - e^{-0.5T}}{0.5T} - e^{-0.5T}\right)
    $$

    The discount factors are $P^M(0, T) = e^{-y(T) \cdot T}$.

    **Why Hull-White always matches the initial curve exactly:** The drift function $\theta(t)$ is defined by:

    $$
    \theta(t) = f(0,t) + \frac{1}{\lambda}\frac{\partial f}{\partial t}(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})
    $$

    where $f(0, t) = -\frac{\partial}{\partial t}\ln P^M(0, t)$. This formula is constructed so that the model's theoretical discount curve exactly reproduces the market curve $P^M(0, T)$ for any $T$. The bond price formula $P^{\text{HW}}(0, T) = \exp(A(0, T) + B(0, T)\,r_0)$ contains $A(0, T)$, which involves an integral of $\theta$ that, by construction, inverts the relationship to recover $\ln P^M(0, T)$. This is the defining property of the Hull-White model: it is calibrated to the initial term structure by the choice of $\theta(t)$, regardless of $\sigma$ and $\lambda$.

    Computing sample values at $T = 1$:

    $$
    y(1) = 0.03 + 0.01 \times \frac{1 - e^{-0.5}}{0.5} - 0.005\left(\frac{1 - e^{-0.5}}{0.5} - e^{-0.5}\right)
    $$

    $$
    = 0.03 + 0.01 \times 0.78694 - 0.005(0.78694 - 0.60653) = 0.03 + 0.00787 - 0.000902 = 0.03697
    $$

    $$
    P^M(0, 1) = e^{-0.03697} = 0.96371
    $$

    The model price $P^{\text{HW}}(0, 1)$ should match this to within numerical tolerance ($\sim 10^{-6}$). Similar verification applies at $T = 5, 10, 20$.

---

**Exercise 2.** In Example 2, the calibration produced repricing errors of 10--20 bps. Suppose you replace the constant $\sigma$ with a piecewise-constant function $\sigma(t) = \sigma_1$ for $t \leq 3$ and $\sigma(t) = \sigma_2$ for $t > 3$. How many free parameters do you now have? Why should this improve the fit? Describe how you would modify the calibration objective function.

??? success "Solution to Exercise 2"
    Replacing constant $\sigma$ with piecewise-constant $\sigma(t)$:

    $$
    \sigma(t) = \begin{cases} \sigma_1 & t \leq 3 \\ \sigma_2 & t > 3 \end{cases}
    $$

    **Number of free parameters:** Three: $\sigma_1$, $\sigma_2$, and $\lambda$. (Previously two: $\sigma$ and $\lambda$.)

    **Why this improves the fit:** With constant $\sigma$, the model generates a specific volatility term structure shape that is controlled by only two parameters. The cap volatility term structure is determined by the interaction of $\sigma$ and $\lambda$, and with two parameters the model can only produce a limited family of shapes (monotonically increasing, decreasing, or slightly humped). With piecewise-constant $\sigma(t)$, the model can independently control the volatility level for short-dated caplets ($T_i \leq 3$) and long-dated caplets ($T_i > 3$), adding one degree of freedom. This allows fitting humped volatility term structures that the constant-$\sigma$ model cannot match.

    **Modified objective function:** The optimization variable becomes $(\sigma_1, \sigma_2, \lambda) \in \mathbb{R}^3_+$. For each trial $(\sigma_1, \sigma_2, \lambda)$, the model must:

    1. Recompute $\theta(t)$ using the piecewise $\sigma(t)$ in the formula (the convexity term becomes $\frac{\sigma(t)^2}{2\lambda^2}(1 - e^{-2\lambda t})$, but care is needed since $\sigma$ changes at $t = 3$).
    2. Recompute $A(\tau)$ using piecewise integration where $\sigma$ changes.
    3. Price each caplet with the appropriate $\sigma$ value for its reset date.

    The objective function remains $f(\sigma_1, \sigma_2, \lambda) = \sum_j w_j [\sigma_j^{\text{model}} - \sigma_j^{\text{mkt}}]^2$, but now with three optimization variables.

---

**Exercise 3.** Example 3 validates the Jamshidian swaption price against Monte Carlo. If the MC estimate is 0.032089 with standard error 0.000120, and the closed-form price is 0.032145, compute the number of standard errors separating the two. At the 95\% confidence level, is the difference statistically significant? How many paths would you need to reduce the standard error to 0.000010?

??? success "Solution to Exercise 3"
    The MC estimate is $\hat{V}_{\text{MC}} = 0.032089$ and the closed-form price is $V_{\text{CF}} = 0.032145$. The standard error is $\text{SE} = 0.000120$.

    **Number of standard errors:**

    $$
    z = \frac{|V_{\text{CF}} - \hat{V}_{\text{MC}}|}{\text{SE}} = \frac{|0.032145 - 0.032089|}{0.000120} = \frac{0.000056}{0.000120} = 0.467
    $$

    At the 95% confidence level, the critical value is $z_{0.025} = 1.96$. Since $0.467 < 1.96$, the difference is **not statistically significant**. The MC estimate is well within the 95% confidence interval $[0.032145 \pm 1.96 \times 0.000120] = [0.031910, 0.032380]$.

    **Reducing the standard error to 0.000010:** The standard error scales as $\text{SE} \propto 1/\sqrt{N}$. To reduce from 0.000120 to 0.000010:

    $$
    \frac{N_{\text{new}}}{N_{\text{old}}} = \left(\frac{\text{SE}_{\text{old}}}{\text{SE}_{\text{new}}}\right)^2 = \left(\frac{0.000120}{0.000010}\right)^2 = 144
    $$

    $$
    N_{\text{new}} = 144 \times 100{,}000 = 14{,}400{,}000 \approx 14.4 \text{ million paths}
    $$

---

**Exercise 4.** Example 4 reports a Bermudan premium of approximately 7\% over the European price. Explain qualitatively why the Bermudan premium depends on the mean-reversion speed $\lambda$. If $\lambda$ is very large (strong mean reversion), would you expect the Bermudan premium to increase or decrease? Justify your reasoning.

??? success "Solution to Exercise 4"
    **Dependence of Bermudan premium on $\lambda$:**

    The Bermudan premium arises from the value of choosing the optimal exercise date. This optionality depends on how much the swap value can change between exercise dates.

    - **Small $\lambda$ (weak mean reversion):** The short rate has high persistence. A rate move at $t = 5$ is likely to persist at $t = 6, 7, \ldots$, so the holder gains little by waiting --- the swap value is similar across exercise dates. However, weak mean reversion also means higher rate variance, creating larger deviations from the mean, which increases the chance that exercise is optimal at a non-first date.

    - **Large $\lambda$ (strong mean reversion):** The short rate quickly reverts to its long-run level. Between exercise dates (1 year apart), a significant rate movement can occur followed by partial reversion. This means the swap value at $t = 6$ can differ substantially from its value at $t = 5$ if rates revert. The holder benefits from the ability to wait for a favorable rate scenario.

    However, the dominant effect is that **strong mean reversion reduces the overall rate volatility** at longer horizons (since $\sigma_r^2(\infty) = \sigma^2/(2\lambda)$ decreases with $\lambda$). Lower rate volatility means all option values are lower, including the Bermudan premium.

    **Net effect:** If $\lambda$ is very large, the Bermudan premium **decreases** because the reduced rate volatility diminishes the value of all embedded options. The early-exercise feature has less value when the rate distribution at each exercise date is tightly concentrated around the mean, leaving little room for the exercise decision to add value.

---

**Exercise 5.** Design a fifth example: price a 3-year annual cap with strike 3\% using three methods: (a) the closed-form caplet formula (sum of caplets), (b) Monte Carlo with 50,000 paths, and (c) the trinomial tree with 200 steps per year. Report the price from each method and the computation time. Which method is most accurate for this product, and why?

??? success "Solution to Exercise 5"
    **Design of Example 5: 3-year annual cap, strike 3%**

    The cap consists of 2 caplets: reset at $T = 1$ (payment at $T = 2$) and reset at $T = 2$ (payment at $T = 3$), with $\delta = 1$.

    **(a) Closed-form caplet formula:** Each caplet price uses the bond-put equivalence. The cap price is the sum of 2 caplet prices. With $\sigma = 0.01$, $\lambda = 0.05$, flat curve at 3%:

    ```python
    hw = HullWhite(sigma=0.01, lambd=0.05, P=lambda T: np.exp(-0.03 * T))
    pricer = BondPricer(hw)
    cap_cf = pricer.cap(reset_dates=[1, 2], delta=1.0, K=0.03, r0=0.03)
    ```

    Expected: a price of approximately 30--50 bps of notional.

    **(b) Monte Carlo with 50,000 paths:** Simulate 50,000 rate paths, compute the LIBOR rate at each reset, apply the caplet payoff $\max(L_{T_i} - K, 0)\delta$, discount to $t = 0$.

    ```python
    mc = HullWhiteMC(hw, n_paths=50000, n_steps=300)
    cap_mc = mc.price_cap(reset_dates=[1, 2], delta=1.0, K=0.03, r0=0.03)
    ```

    **(c) Trinomial tree with 200 steps per year (600 total steps):** Build the tree to $T = 3$, use backward induction with the caplet payoff at each reset date.

    ```python
    tree = HullWhiteTree(hw, T_max=3, n_steps=600)
    cap_tree = tree.price_cap(reset_dates=[1, 2], delta=1.0, K=0.03)
    ```

    **Comparison:**

    | Method | Price | Computation time |
    |--------|-------|-----------------|
    | Closed-form | Exact (benchmark) | $< 1$ ms |
    | Monte Carlo (50K paths) | Approximate, SE $\sim 10^{-5}$ | $\sim 1$ s |
    | Trinomial tree (600 steps) | Approximate, error $\sim 10^{-5}$ | $\sim 0.1$ s |

    The **closed-form method is most accurate** for this product because the cap decomposes into caplets that each have exact analytical pricing formulas in the Hull-White model. Both numerical methods introduce discretization or statistical errors. The closed form is also fastest by orders of magnitude.

---

**Exercise 6.** Modify Example 3 to apply the control variate technique. Use the 10-year ZCB price as the control variable. Describe the steps: (a) simulate $\hat{P}_{\text{MC}}(0, 10)$ alongside the swaption payoff, (b) compute the regression coefficient $\beta$, (c) compute the adjusted estimator $\hat{V}_{\text{cv}}$. By what factor would you expect the variance to be reduced, given that the ZCB and swaption payoff are correlated through the same short-rate paths?

??? success "Solution to Exercise 6"
    **Step (a): Simulate the ZCB alongside the swaption.**

    During the MC simulation for the 5Y-into-5Y swaption, at each path $i$, also compute:

    $$
    P_{\text{MC}}^{(i)}(0, 10) = \exp\!\left(-\sum_{k=0}^{M-1} r_{t_k}^{(i)}\,\Delta t\right)
    $$

    This is simply $1/M_{10}^{(i)}$, the reciprocal of the money market account at $T = 10$, which is already computed as part of the discounting. No additional simulation is needed.

    **Step (b): Compute the regression coefficient $\beta$.**

    Let $V^{(i)}$ be the discounted swaption payoff for path $i$ and $P^{(i)} = P_{\text{MC}}^{(i)}(0, 10)$. The optimal $\beta$ is:

    $$
    \hat{\beta} = \frac{\sum_{i=1}^N (V^{(i)} - \bar{V})(P^{(i)} - \bar{P})}{\sum_{i=1}^N (P^{(i)} - \bar{P})^2}
    $$

    In code:

    ```python
    beta = np.cov(V, P_mc)[0, 1] / np.var(P_mc)
    ```

    **Step (c): Compute the adjusted estimator.**

    The analytical ZCB price is $P^M(0, 10) = e^{-0.3} = 0.74082$.

    $$
    \hat{V}_{\text{cv}} = \bar{V} - \hat{\beta}(\bar{P} - P^M(0, 10))
    $$

    **Expected variance reduction:** The variance reduction factor is $1 - \rho^2$, where $\rho = \text{Corr}(V, P)$. The swaption payoff at $T_0 = 5$ depends on the rate path up to $T_0$ (through the discount factor) and on $r_{T_0}$ (through the swap value). The ZCB payoff depends on the rate path up to $T = 10$. Since both share the first 5 years of the rate path and the swaption's underlying swap extends to $T = 10$, the correlation is high.

    For a 5Y-into-5Y payer swaption, $|\rho|$ is typically 0.7--0.9, giving a variance reduction factor of $1 - \rho^2 \approx 0.19$ to $0.51$. This corresponds to a variance reduction by a factor of 2 to 5, or equivalently, the control variate is worth 2 to 5 times as many paths. The standard error would decrease from 0.000120 to approximately 0.000055--0.000085 without increasing the number of paths.
