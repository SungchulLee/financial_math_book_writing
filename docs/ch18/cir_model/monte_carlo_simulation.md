# Monte Carlo Simulation for the CIR Model

While the CIR model provides closed-form formulas for zero-coupon bonds and European bond options, many practical applications require pricing path-dependent derivatives --- such as range accruals, barrier options on rates, or mortgage-backed securities --- for which no analytical solution exists. Monte Carlo simulation fills this gap by generating a large number of CIR rate paths and averaging discounted payoffs. This section develops the Monte Carlo framework for CIR bond pricing, presents variance reduction techniques that dramatically improve efficiency, and quantifies convergence through standard errors and confidence intervals.

---

## Monte Carlo bond pricing estimator

Under the risk-neutral measure $\mathbb{Q}$, the zero-coupon bond price is

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\,\bigg|\,\mathcal{F}_t\right]
$$

The Monte Carlo estimator replaces the expectation with a sample average over $M$ independent paths:

$$
\hat{P}(t,T) = \frac{1}{M}\sum_{m=1}^{M}\exp\!\left(-\sum_{k=0}^{N-1} r_{t_k}^{(m)}\,\Delta t_k\right)
$$

where $r_{t_0}^{(m)}, r_{t_1}^{(m)}, \ldots, r_{t_N}^{(m)}$ is the $m$-th simulated path on the time grid $t = t_0 < t_1 < \cdots < t_N = T$, and $\Delta t_k = t_{k+1} - t_k$. The integral $\int_t^T r_s\,ds$ is approximated by the left-point Riemann sum; the trapezoidal rule

$$
\int_t^T r_s\,ds \approx \sum_{k=0}^{N-1}\frac{r_{t_k}^{(m)} + r_{t_{k+1}}^{(m)}}{2}\,\Delta t_k
$$

provides higher-order accuracy for smooth paths.

---

## Path generation

Recall (see [§ Exact Simulation and Euler Pitfalls](exact_simulation_and_euler_pitfalls.md)) the two simulation schemes: exact non-central chi-squared sampling (no discretization bias) and Euler-Maruyama with truncation (simple, biased). For bond pricing, exact simulation is strongly preferred.

### Time grid design

The time grid should include:

- All payoff observation dates (coupon dates, barrier monitoring dates)
- Sufficient intermediate points for accurate integral approximation
- For exact simulation, only the dates needed by the payoff (minimal grid)

!!! tip "Minimal grids with exact simulation"
    Since exact simulation produces the correct conditional distribution regardless of step size, a zero-coupon bond price can be estimated with a single time step from $t$ to $T$ if only the terminal discount factor $e^{-\int_t^T r_s\,ds}$ is needed. However, approximating the integral requires intermediate points. A grid of 50--100 steps per year typically suffices for bond pricing.

---

## Standard error and confidence intervals

The sample mean $\hat{P}$ has standard error

$$
\text{SE} = \frac{\hat{s}}{\sqrt{M}}
$$

where $\hat{s}^2 = \frac{1}{M-1}\sum_{m=1}^M(Y_m - \hat{P})^2$ and $Y_m = \exp(-\sum_k r_{t_k}^{(m)}\Delta t_k)$. An approximate 95% confidence interval is

$$
\hat{P} \pm 1.96\,\frac{\hat{s}}{\sqrt{M}}
$$

By the central limit theorem, the error decreases as $O(1/\sqrt{M})$: halving the standard error requires quadrupling the number of paths.

---

## Variance reduction techniques

### Antithetic variates

For each path generated with random inputs $Z_1, Z_2, \ldots, Z_N$, generate a second path using $-Z_1, -Z_2, \ldots, -Z_N$. The antithetic estimator is

$$
\hat{P}_{\text{anti}} = \frac{1}{M}\sum_{m=1}^{M}\frac{Y_m + Y_m'}{2}
$$

where $Y_m'$ is the discount factor from the antithetic path. Since the CIR discount factor is a convex function of the driving noise (through the exponential), $Y_m$ and $Y_m'$ are negatively correlated, and the variance of the average $(Y_m + Y_m')/2$ is less than the variance of $Y_m$ alone.

**Variance reduction factor**: Typically 30--60% for bond pricing.

### Control variates

Use the known closed-form bond price $P^{\text{exact}}(t,T)$ as a control. For each path $m$, define

$$
\hat{Y}_m^{\text{CV}} = Y_m - \beta\left(\bar{r}^{(m)} - \mathbb{E}^{\mathbb{Q}}[\bar{r}]\right)
$$

where $\bar{r}^{(m)} = \frac{1}{N}\sum_k r_{t_k}^{(m)}$ is the average rate along path $m$, and $\beta$ is the optimal control coefficient estimated by regression. The conditional mean $\mathbb{E}^{\mathbb{Q}}[\bar{r}]$ can be computed from the CIR moment formulas:

$$
\mathbb{E}^{\mathbb{Q}}[r_s\,|\,r_t] = r_t\,e^{-\kappa(s-t)} + \theta(1 - e^{-\kappa(s-t)})
$$

**Variance reduction factor**: Typically 80--95% for bond pricing, making it the most effective single technique.

### Combined approach

Antithetic variates and control variates can be combined: first generate antithetic pairs, then apply the control variate correction to each pair average. The combined reduction is multiplicative, often achieving 90--98% variance reduction.

---

## Pricing path-dependent derivatives

Monte Carlo is indispensable for derivatives whose payoffs depend on the entire rate path.

### Example: discretely monitored range accrual

A range accrual note pays a coupon proportional to the fraction of fixing dates on which the rate falls within a range $[L, U]$:

$$
\text{Payoff} = N\,c\,\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}_{\{L \leq r_{T_i} \leq U\}}
$$

The Monte Carlo price is

$$
V(0) = \frac{1}{M}\sum_{m=1}^{M}\exp\!\left(-\sum_k r_{t_k}^{(m)}\Delta t_k\right)\cdot Nc\,\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}_{\{L \leq r_{T_i}^{(m)} \leq U\}}
$$

No closed-form solution exists for this product under CIR, making Monte Carlo the standard approach.

### Example: interest rate cap with discrete monitoring

While individual caplets have closed-form CIR prices, a cap with knock-out barriers or path-dependent features requires Monte Carlo:

$$
\text{Caplet}_i^{\text{KO}} = N\delta_i(L(T_i, T_{i+1}) - K)^+\,\mathbf{1}_{\{r_s < H \;\forall\; s \in [0, T_i]\}}
$$

The knock-out condition requires monitoring the rate path, which is naturally handled by path simulation.

---

## Convergence verification

A reliable Monte Carlo implementation should be verified against known analytical results before being applied to exotic products.

**Verification protocol**:

1. Price a zero-coupon bond using MC and compare to the closed-form CIR formula
2. Price a European bond option using MC and compare to the chi-squared formula
3. For each test, verify that the closed-form price falls within the 95% confidence interval
4. Check that the standard error scales as $O(1/\sqrt{M})$ by doubling $M$

| $M$ (paths) | $\hat{P}(0,5)$ | SE | 95% CI | $P^{\text{exact}}$ |
|:-----------:|:---------------:|:---:|:------:|:------------------:|
| 1,000 | 0.7685 | 0.0028 | [0.7630, 0.7740] | 0.7700 |
| 10,000 | 0.7703 | 0.0009 | [0.7685, 0.7721] | 0.7700 |
| 100,000 | 0.7699 | 0.0003 | [0.7693, 0.7705] | 0.7700 |

The exact price falls within all three confidence intervals, and the SE decreases by a factor of $\approx \sqrt{10}$ with each 10-fold increase in $M$.

---

## Summary

Monte Carlo simulation for the CIR model combines path generation (preferably exact via non-central chi-squared sampling) with discounted payoff averaging. The method converges at rate $O(1/\sqrt{M})$, with standard errors quantifying the statistical uncertainty. Antithetic variates provide 30--60% variance reduction, while control variates using the known CIR moments achieve 80--95% reduction. For path-dependent derivatives --- range accruals, barrier products, callable bonds --- Monte Carlo is the only feasible pricing approach. Verification against closed-form bond and option prices should always precede application to exotic products.

---

## Exercises

**Exercise 1.** For CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, and $r_0 = 0.04$, compute the exact 5-year zero-coupon bond price $P^{\text{exact}}(0,5)$ using the CIR formula. If a Monte Carlo estimate gives $\hat{P} = 0.7703$ with standard error $\text{SE} = 0.0009$ using $M = 10{,}000$ paths, construct the 95% confidence interval. Does $P^{\text{exact}}$ fall within this interval?

??? success "Solution to Exercise 1"

    First compute the exact price using the CIR formula with $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $r_0 = 0.04$, $\tau = 5$.

    $$
    \gamma = \sqrt{0.25 + 0.02} = \sqrt{0.27} \approx 0.5196
    $$

    $$
    e^{\gamma \cdot 5} = e^{2.598} \approx 13.44
    $$

    $$
    B(5) = \frac{2(13.44 - 1)}{(0.5196 + 0.5)(13.44 - 1) + 2(0.5196)} = \frac{24.88}{12.68 + 1.039} = \frac{24.88}{13.72} \approx 1.813
    $$

    $$
    A(5) = \left(\frac{2(0.5196)e^{(1.0196)(2.5)}}{13.72}\right)^6 = \left(\frac{1.039 \times 12.80}{13.72}\right)^6 \approx (0.969)^6 \approx 0.828
    $$

    $$
    P^{\text{exact}}(0,5) = 0.828 \times e^{-1.813 \times 0.04} = 0.828 \times 0.930 \approx 0.7700
    $$

    **95% confidence interval from MC:**

    $$
    \hat{P} \pm 1.96 \times \text{SE} = 0.7703 \pm 1.96 \times 0.0009 = 0.7703 \pm 0.00176 = [0.7685,\, 0.7721]
    $$

    Since $P^{\text{exact}} \approx 0.7700 \in [0.7685, 0.7721]$, **yes**, the exact price falls within the 95% CI. This confirms the Monte Carlo implementation is working correctly.

---

**Exercise 2.** Explain why the trapezoidal rule for approximating $\int_0^T r_s\,ds$ provides higher accuracy than the left-point Riemann sum. For a smooth path where $r_t$ has bounded second derivative $|r''(t)| \leq C$, what is the error bound for each method with $N$ equal steps over $[0, T]$?

??? success "Solution to Exercise 2"

    The **left-point Riemann sum** approximates $\int_0^T r_s\,ds \approx \sum_{k=0}^{N-1} r_{t_k}\Delta t$. For a smooth function $r(t)$ with bounded first derivative $|r'(t)| \leq C_1$, the error per subinterval is $O(\Delta t^2)$ and the total error over $N = T/\Delta t$ intervals is:

    $$
    \left|\int_0^T r_s\,ds - \sum_{k=0}^{N-1} r_{t_k}\Delta t\right| \leq \frac{C_1 T}{2}\Delta t = O(\Delta t) = O\left(\frac{T^2}{2N}\right)
    $$

    The **trapezoidal rule** approximates $\int_0^T r_s\,ds \approx \sum_{k=0}^{N-1}\frac{r_{t_k} + r_{t_{k+1}}}{2}\Delta t$. For a function with bounded second derivative $|r''(t)| \leq C_2$, the error is:

    $$
    \left|\int_0^T r_s\,ds - \text{trap. sum}\right| \leq \frac{C_2 T}{12}\Delta t^2 = O(\Delta t^2) = O\left(\frac{T^3}{12N^2}\right)
    $$

    The trapezoidal rule has error $O(1/N^2)$ versus $O(1/N)$ for the left-point rule, providing **one additional order** of accuracy. This means the trapezoidal rule achieves the same accuracy with $\sqrt{10}$ times fewer steps, which is significant for Monte Carlo where each path evaluation contributes to computational cost.

---

**Exercise 3.** In the antithetic variate method, each path uses innovations $Z_1, \ldots, Z_N$ and the antithetic path uses $-Z_1, \ldots, -Z_N$. For exact CIR simulation, where each step draws from a non-central chi-squared distribution, describe how antithetic variates would be implemented. (Hint: the non-central chi-squared draw uses Gaussian inputs internally.)

??? success "Solution to Exercise 3"

    For exact CIR simulation, each step draws from a non-central chi-squared distribution. The standard implementation of `numpy.random.noncentral_chisquare(d, lam)` internally uses Gaussian random variables:

    - For $d > 1$: Draw $Z \sim \mathcal{N}(0,1)$, compute $N = Z + \sqrt{\lambda}$, draw $Y \sim \chi^2(d-1)$ (which uses $d-1$ independent standard normals), and set $X = N^2 + Y$.
    - For $d \leq 1$: Draw $J \sim \text{Poisson}(\lambda/2)$, then $X \sim \chi^2(d + 2J)$.

    **Antithetic implementation for exact simulation:** At each time step $k$:

    1. Generate the underlying Gaussian inputs $Z_k^{(1)}, \ldots$ used internally by the chi-squared sampler.
    2. For the antithetic path, negate these inputs: $-Z_k^{(1)}, \ldots$

    In practice, this means implementing the non-central chi-squared sampling manually rather than using the library black-box. For the $d > 1$ case, the primary path uses $Z_k$ and the antithetic uses $-Z_k$:

    - Primary: $N_k = Z_k + \sqrt{\lambda_k}$, so $N_k^2 = Z_k^2 + 2Z_k\sqrt{\lambda_k} + \lambda_k$.
    - Antithetic: $\tilde{N}_k = -Z_k + \sqrt{\lambda_k}$, so $\tilde{N}_k^2 = Z_k^2 - 2Z_k\sqrt{\lambda_k} + \lambda_k$.

    The average $(N_k^2 + \tilde{N}_k^2)/2 = Z_k^2 + \lambda_k$ eliminates the linear term in $Z_k$, reducing variance. The chi-squared component $Y$ would be handled similarly by negating its underlying normals.

---

**Exercise 4.** The control variate uses $\bar{r}^{(m)} = \frac{1}{N}\sum_k r_{t_k}^{(m)}$ with known mean $\mathbb{E}[\bar{r}] = \frac{1}{N}\sum_k \mathbb{E}[r_{t_k}]$. Using the CIR conditional mean formula $\mathbb{E}[r_s | r_0] = r_0 e^{-\kappa s} + \theta(1 - e^{-\kappa s})$, compute $\mathbb{E}[\bar{r}]$ for $r_0 = 0.04$, $\kappa = 0.5$, $\theta = 0.06$, $T = 5$ years, and $N = 250$ equally spaced steps.

??? success "Solution to Exercise 4"

    The CIR conditional mean is $\mathbb{E}[r_s \mid r_0] = r_0 e^{-\kappa s} + \theta(1 - e^{-\kappa s})$ with $r_0 = 0.04$, $\kappa = 0.5$, $\theta = 0.06$.

    With $N = 250$ steps over $T = 5$ years, $\Delta t = 5/250 = 0.02$, and time points $t_k = k\Delta t$ for $k = 0, 1, \ldots, 250$.

    $$
    \mathbb{E}[\bar{r}] = \frac{1}{N}\sum_{k=0}^{N-1}\mathbb{E}[r_{t_k}] = \frac{1}{250}\sum_{k=0}^{249}\left[0.04\,e^{-0.5 \cdot 0.02k} + 0.06(1 - e^{-0.5 \cdot 0.02k})\right]
    $$

    $$
    = \frac{1}{250}\sum_{k=0}^{249}\left[0.06 - 0.02\,e^{-0.01k}\right]
    $$

    $$
    = 0.06 - \frac{0.02}{250}\sum_{k=0}^{249}e^{-0.01k}
    $$

    The geometric sum: $\sum_{k=0}^{249}e^{-0.01k} = \frac{1 - e^{-2.5}}{1 - e^{-0.01}} = \frac{1 - 0.0821}{1 - 0.99005} = \frac{0.9179}{0.00995} \approx 92.25$.

    $$
    \mathbb{E}[\bar{r}] = 0.06 - 0.02 \times \frac{92.25}{250} = 0.06 - 0.02 \times 0.369 = 0.06 - 0.00738 = 0.05262
    $$

    The expected average rate along the path is approximately 5.26%, between the starting rate of 4% and the long-run mean of 6%.

---

**Exercise 5.** You run $M = 1{,}000$ Monte Carlo paths and obtain $\hat{P}(0,5) = 0.7685$ with $\text{SE} = 0.0028$. How many paths $M'$ are needed to achieve $\text{SE} = 0.0003$? If applying control variates reduces variance by 90%, how many paths are needed with the control variate to achieve the same $\text{SE} = 0.0003$?

??? success "Solution to Exercise 5"

    With $M = 1{,}000$ paths and $\text{SE} = 0.0028$, the sample standard deviation is $\hat{s} = \text{SE} \times \sqrt{M} = 0.0028 \times \sqrt{1000} = 0.0028 \times 31.62 = 0.08854$.

    **Paths needed for $\text{SE} = 0.0003$ without variance reduction:**

    $$
    M' = \left(\frac{\hat{s}}{0.0003}\right)^2 = \left(\frac{0.08854}{0.0003}\right)^2 = (295.1)^2 \approx 87{,}111
    $$

    So approximately $M' \approx 87{,}000$ paths are needed.

    **With control variates reducing variance by 90%:** The reduced standard deviation is $\hat{s}_{\text{CV}} = \hat{s}\sqrt{1 - 0.90} = 0.08854\sqrt{0.10} = 0.08854 \times 0.3162 = 0.02799$.

    $$
    M'_{\text{CV}} = \left(\frac{0.02799}{0.0003}\right)^2 = (93.3)^2 \approx 8{,}705
    $$

    With the control variate, only about $M' \approx 8{,}700$ paths are needed --- a 10-fold reduction in computational effort. This illustrates the enormous practical value of control variates.

---

**Exercise 6.** A range accrual note has notional \$1,000,000, annual coupon 5%, and pays based on the fraction of quarterly observation dates where $r_t \in [3\%, 7\%]$ over a 3-year period. Write out the Monte Carlo pricing formula explicitly, specifying the discount factor, the indicator sum, and the number of observation dates. How would you estimate the standard error of this price?

??? success "Solution to Exercise 6"

    The range accrual note has:

    - Notional $N = \$1{,}000{,}000$
    - Annual coupon $c = 5\%$
    - Maturity: 3 years
    - Quarterly observations: $n = 12$ observation dates at $T_i = 0.25, 0.50, \ldots, 3.00$
    - Range: $[L, U] = [0.03, 0.07]$

    The payoff at maturity is:

    $$
    N \cdot c \cdot \frac{1}{n}\sum_{i=1}^{12}\mathbf{1}_{\{0.03 \leq r_{T_i} \leq 0.07\}}
    $$

    The Monte Carlo price is:

    $$
    V(0) = \frac{1}{M}\sum_{m=1}^{M}\exp\!\left(-\sum_{k=0}^{N_{\text{steps}}-1} \frac{r_{t_k}^{(m)} + r_{t_{k+1}}^{(m)}}{2}\Delta t_k\right) \cdot 1{,}000{,}000 \times 0.05 \times \frac{1}{12}\sum_{i=1}^{12}\mathbf{1}_{\{0.03 \leq r_{T_i}^{(m)} \leq 0.07\}}
    $$

    For each path $m$, let $Y_m = D_m \cdot 50{,}000 \times \frac{1}{12}\sum_{i=1}^{12}\mathbf{1}_{\{0.03 \leq r_{T_i}^{(m)} \leq 0.07\}}$ where $D_m$ is the path discount factor.

    Then $V(0) = \frac{1}{M}\sum_m Y_m$.

    **Standard error estimation:**

    $$
    \text{SE} = \frac{\hat{s}_Y}{\sqrt{M}}, \qquad \hat{s}_Y^2 = \frac{1}{M-1}\sum_{m=1}^{M}(Y_m - \bar{Y})^2
    $$

    The number of observation dates is 12 (quarterly over 3 years). The time grid for the simulation must include at least these 12 dates plus intermediate points for accurate discount factor computation.

---

**Exercise 7.** Explain the convergence verification protocol: why is it important to check that the closed-form price falls within the Monte Carlo confidence interval before pricing exotic products? If the closed-form price consistently falls outside the 95% CI, what are the possible causes (enumerate at least three)?

??? success "Solution to Exercise 7"

    **Why verification is important:** The convergence verification protocol tests that the Monte Carlo machinery (path generation, integration, discounting, averaging) is correctly implemented by comparing against a known analytical benchmark. If the implementation has bugs (e.g., incorrect scaling in the non-central chi-squared sampling, wrong integration formula, off-by-one errors in the time grid), these will cause the MC price to be systematically biased, and the exact price will fall outside the confidence interval.

    For exotic products with no closed-form solution, there is no benchmark to check against. If the MC implementation is flawed, the pricing error will go undetected. Verifying on vanilla products first establishes confidence in the simulation infrastructure before applying it to complex derivatives.

    **If the closed-form price consistently falls outside the 95% CI, possible causes include:**

    1. **Implementation bug in path generation:** Incorrect parameters in the non-central chi-squared sampling (e.g., wrong formula for $c$, $d$, or $\lambda$), producing paths with incorrect conditional distributions.

    2. **Discretization bias:** Using Euler-Maruyama instead of exact simulation without sufficiently small time steps, introducing systematic bias from truncation/reflection of negative values.

    3. **Integration error:** Using a coarse time grid for the numerical approximation of $\int_0^T r_s\,ds$, or using the wrong integration rule (e.g., left-point instead of trapezoidal), producing a biased discount factor.

    4. **Bug in the analytical formula:** The closed-form CIR bond price implementation itself may have an error (e.g., incorrect formula for $A(\tau)$ or $B(\tau)$).

    5. **Random seed / insufficient paths:** If $M$ is too small, the confidence interval may be too wide or the sample mean may not be representative. However, this would cause the exact price to fall outside the CI only 5% of the time, not consistently.

    6. **Inconsistent parameter usage:** Different parameters used in the MC simulation versus the analytical formula (e.g., using physical parameters in one and risk-neutral in the other).
