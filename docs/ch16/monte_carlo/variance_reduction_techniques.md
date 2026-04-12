# Variance Reduction Techniques

Monte Carlo estimators converge at rate $\mathcal{O}(M^{-1/2})$ regardless of the simulation scheme: doubling the number of paths only reduces the standard error by a factor of $\sqrt{2}$. **Variance reduction** techniques attack the constant in this bound rather than the rate, producing estimators with the same expected value but much smaller variance. In the Heston model, three methods are particularly effective: **antithetic variates** exploit the symmetry of Gaussian increments, **control variates** use the Black-Scholes price as a cheap proxy with known expectation, and **importance sampling** shifts the simulation measure toward the region where the payoff contributes most to the price.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Implement antithetic variates for the correlated two-dimensional Heston system
    2. Construct a control variate estimator using the Black-Scholes price as the control
    3. Derive the optimal control variate coefficient and its variance reduction factor
    4. Apply importance sampling via exponential tilting of the log-price drift

!!! tip "Prerequisites"
    This section builds on the Monte Carlo simulation schemes in this chapter, particularly the [QE scheme](quadratic_exponential_scheme.md) and the [Euler discretization](euler_discretization_and_pitfalls.md).

---

## The Baseline Problem

A Monte Carlo estimator for a European option under Heston takes the form:

$$
\hat{V} = e^{-rT} \frac{1}{M} \sum_{m=1}^{M} g\!\left(S_T^{(m)}\right)
$$

where $g$ is the payoff function and $S_T^{(m)}$ are independent samples from the risk-neutral terminal distribution. The variance of this estimator is:

$$
\text{Var}(\hat{V}) = \frac{\sigma_g^2}{M}, \qquad \sigma_g^2 = \text{Var}\!\left(e^{-rT} g(S_T)\right)
$$

The 95% confidence interval has half-width $1.96 \, \sigma_g / \sqrt{M}$. Reducing $\sigma_g^2$ by a factor of $k$ is equivalent to using $kM$ paths---a direct computational saving.

---

## Antithetic Variates

### Idea

Every Heston path is driven by two sequences of independent standard normals $(Z_1^{(n)}, Z_2^{(n)})_{n=0}^{N-1}$. The **antithetic** path uses the negated normals $(-Z_1^{(n)}, -Z_2^{(n)})$. Since $-Z \sim N(0,1)$ when $Z \sim N(0,1)$, the antithetic path is equally valid. The antithetic estimator averages each path with its mirror:

$$
\hat{V}_{\text{anti}} = e^{-rT} \frac{1}{M} \sum_{m=1}^{M} \frac{g(S_T^{(m)}) + g(\tilde{S}_T^{(m)})}{2}
$$

where $\tilde{S}_T^{(m)}$ is the terminal price from the antithetic path.

### Variance Reduction

The variance of the antithetic estimator is:

$$
\text{Var}(\hat{V}_{\text{anti}}) = \frac{1}{M} \cdot \frac{\sigma_g^2 + \text{Cov}(g(S_T), g(\tilde{S}_T))}{2}
$$

Variance reduction occurs when $\text{Cov}(g(S_T), g(\tilde{S}_T)) < 0$, i.e., when paths with large payoffs tend to pair with antithetic paths having small payoffs. For convex payoffs like calls, high stock prices (driven by positive $Z_1$ shocks) pair with low antithetic prices (driven by negative $Z_1$ shocks), producing strong negative correlation.

### Heston-Specific Considerations

In the Heston model, negating both $(Z_1, Z_2)$ simultaneously negates the log-price increment **and** the variance increment. The variance path under the antithetic becomes:

$$
v_{n+1}^{\text{anti}} = v_n^{\text{anti}} + \kappa(\theta - v_n^{\text{anti}})\Delta t + \xi\sqrt{(v_n^{\text{anti}})^+}(-\Delta W_n^{(2)})
$$

Because the CIR drift is mean-reverting, the antithetic variance path tends to mirror the original around the long-run level $\theta$, though the reflection is imperfect due to the nonlinear square-root diffusion.

!!! note "Typical Efficiency Gain"
    For ATM European calls under typical Heston parameters, antithetic variates reduce variance by a factor of 2--4, effectively doubling to quadrupling the number of useful paths at negligible additional cost (one extra payoff evaluation per original path).

---

## Control Variates

### Idea

A **control variate** is a random variable $C$ whose expectation $\mathbb{E}[C]$ is known analytically and that is correlated with the payoff $g(S_T)$. The control variate estimator is:

$$
\hat{V}_{\text{cv}} = \hat{V} - \beta\left(\hat{C} - \mathbb{E}[C]\right)
$$

where $\hat{C} = \frac{1}{M}\sum_{m=1}^M C^{(m)}$ and $\beta$ is a coefficient to be optimized.

### Black-Scholes as Control

The most natural control for Heston is the **Black-Scholes price** computed along the same paths. For each simulated path, evaluate the Black-Scholes payoff using the same terminal stock price but with a constant volatility $\bar{\sigma}$ (e.g., the implied volatility of the option being priced):

$$
C^{(m)} = g\!\left(S_T^{(m),\text{BS}}\right)
$$

where $S_T^{(m),\text{BS}}$ is the terminal price under the same Brownian path but with constant volatility $\bar{\sigma}$.

The expectation $\mathbb{E}[C]$ is the known Black-Scholes price $V_{\text{BS}}(S_0, K, T, r, q, \bar{\sigma})$.

### Optimal Coefficient

The **optimal** $\beta$ minimizes the variance of $\hat{V}_{\text{cv}}$:

$$
\beta^* = \frac{\text{Cov}(g(S_T), C)}{\text{Var}(C)}
$$

In practice, $\beta^*$ is estimated from a pilot run or computed alongside the main simulation:

$$
\hat{\beta} = \frac{\sum_{m=1}^M (g^{(m)} - \bar{g})(C^{(m)} - \bar{C})}{\sum_{m=1}^M (C^{(m)} - \bar{C})^2}
$$

### Variance Reduction Factor

The variance reduction factor is:

$$
\frac{\text{Var}(\hat{V}_{\text{cv}})}{\text{Var}(\hat{V})} = 1 - \rho_{g,C}^2
$$

where $\rho_{g,C}$ is the correlation between $g(S_T)$ and $C$. When $|\rho_{g,C}|$ is close to 1, the reduction is dramatic.

!!! tip "Choosing the Control Volatility"
    Set $\bar{\sigma}$ to the Heston model's ATM implied volatility. This maximizes the correlation between the Heston payoff and the Black-Scholes control. For far OTM options, the correlation drops and the control variate becomes less effective; in that regime, importance sampling is more powerful.

---

## Importance Sampling

### Idea

**Importance sampling** changes the probability measure under which paths are simulated, concentrating sampling effort in the region of the payoff space that contributes most to the price. The exact expectation is preserved by reweighting each path with a **likelihood ratio** (Radon–Nikodym derivative).

### Drift Shifting for the Log-Price

The simplest importance sampling strategy shifts the drift of the log-price process. Under the original measure $\mathbb{Q}$:

$$
x_T = x_0 + (r - q - \tfrac{1}{2}\bar{v})T + \sqrt{\bar{v}} \, W_T^{(1)}
$$

where $\bar{v}$ is an effective average variance. Under the **tilted measure** $\tilde{\mathbb{Q}}$ with drift shift $\mu$:

$$
x_T = x_0 + (r - q - \tfrac{1}{2}\bar{v} + \mu)T + \sqrt{\bar{v}} \, \tilde{W}_T^{(1)}
$$

The likelihood ratio is:

$$
\frac{d\mathbb{Q}}{d\tilde{\mathbb{Q}}} = \exp\!\left(-\frac{\mu}{\sqrt{\bar{v}}} W_T^{(1)} - \frac{\mu^2}{2\bar{v}} T\right)
$$

The importance sampling estimator is:

$$
\hat{V}_{\text{IS}} = e^{-rT} \frac{1}{M}\sum_{m=1}^M g(S_T^{(m)}) \cdot \frac{d\mathbb{Q}}{d\tilde{\mathbb{Q}}}^{(m)}
$$

### Optimal Shift for OTM Options

For a deep out-of-the-money call with strike $K \gg S_0 e^{rT}$, most paths under $\mathbb{Q}$ finish below $K$ and contribute zero to the price. Shifting the drift by:

$$
\mu^* \approx \frac{\ln(K/S_0) - (r - q - \bar{v}/2)T}{T}
$$

centers the simulated log-price distribution around $\ln K$, ensuring roughly half the paths finish in-the-money under $\tilde{\mathbb{Q}}$.

!!! warning "Variance Explosion Risk"
    Poorly chosen importance sampling shifts can **increase** variance instead of reducing it. The likelihood ratio $d\mathbb{Q}/d\tilde{\mathbb{Q}}$ has heavy tails when $\mu$ is too large, causing a few paths to dominate the estimator. Always verify that the effective sample size $\text{ESS} = (\sum w_m)^2 / \sum w_m^2$ remains close to $M$.

---

## Combining Methods

The three techniques can be combined for maximum effect:

1. **Antithetic + control variate**: Apply antithetic variates first (negating the normals), then use the Black-Scholes control on the averaged payoff. This is the most common production combination.
2. **Importance sampling + control variate**: Shift the drift for OTM options and use the Black-Scholes control to further reduce variance. The control variate coefficient $\beta$ must be re-estimated under the tilted measure.

The combined estimator is:

$$
\hat{V}_{\text{combined}} = e^{-rT} \frac{1}{M}\sum_{m=1}^M \left[\frac{g^{(m)} + g^{(\text{anti},m)}}{2} - \beta\left(\frac{C^{(m)} + C^{(\text{anti},m)}}{2} - V_{\text{BS}}\right)\right]
$$

---

## Efficiency Comparison

The following table shows typical variance reduction factors for ATM and OTM European calls:

| Method | ATM Factor | OTM Factor ($K = 1.5 S_0$) |
|--------|-----------|---------------------------|
| No reduction | 1 | 1 |
| Antithetic | 2--4 | 1.5--2 |
| Control variate (BS) | 5--20 | 2--5 |
| Importance sampling | 1--2 | 10--100 |
| Anti + CV | 10--50 | 3--8 |
| IS + CV | 5--20 | 50--500 |

!!! note "Interpreting the Factors"
    A variance reduction factor of 50 means that 1,000 variance-reduced paths produce the same standard error as 50,000 naive paths. The factor depends on the specific Heston parameters, the moneyness, and the maturity.

---

## Worked Example

Consider a European call with $S_0 = \$100$, $K = \$100$, $T = 1$, $r = 0.05$ under Heston with $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$.

??? example "Control Variate with Black-Scholes"
    Using $\bar{\sigma} = 0.20$ (approximately the ATM implied vol):

    1. **Naive MC** (10,000 QE paths): $\hat{V} = \$10.38$, std error $= \$0.15$
    2. **With BS control**: $\hat{V}_{\text{cv}} = \$10.36$, std error $= \$0.02$, reduction factor $\approx 56$
    3. **With antithetic + BS control**: $\hat{V}_{\text{combined}} = \$10.36$, std error $= \$0.009$, reduction factor $\approx 278$

    The combined method achieves sub-penny accuracy with only 10,000 paths, compared to roughly 2.8 million paths needed for naive MC.

---

## Summary

Variance reduction techniques improve Monte Carlo efficiency by factors of 10--500 depending on the method and the payoff structure. Antithetic variates provide a simple 2--4 fold improvement by pairing each path with its mirror. Control variates using the Black-Scholes price exploit the strong correlation between Heston and Black-Scholes payoffs, achieving 5--50 fold improvements for ATM options. Importance sampling targets OTM options by shifting the drift toward the exercise region, delivering the largest gains for deep OTM pricing. Combining antithetic variates with control variates is the standard production approach; adding importance sampling provides further benefit for tail-risk pricing and OTM Greeks.

---

## Exercises

**Exercise 1.**
Antithetic variates negate both $Z_1$ and $Z_2$ to create the mirror path. Show that for the log-price under constant variance ($v_t = v_0$ for all $t$), the antithetic terminal value is $\ln\tilde{S}_T = 2\ln S_0 + 2(r - q - v_0/2)T - \ln S_T$, so $\tilde{S}_T = S_0^2 e^{2(r-q-v_0/2)T}/S_T$. For a call payoff $g(S_T) = (S_T - K)^+$, explain why the correlation between $g(S_T)$ and $g(\tilde{S}_T)$ is strongly negative, leading to effective variance reduction.

??? success "Solution to Exercise 1"
    Under constant variance $v_t = v_0$, the log-price follows:

    $$
    \ln S_T = \ln S_0 + (r - q - v_0/2)T + \sqrt{v_0}\,W_T^{(1)}
    $$

    The antithetic path uses $-W_T^{(1)}$:

    $$
    \ln\tilde{S}_T = \ln S_0 + (r - q - v_0/2)T - \sqrt{v_0}\,W_T^{(1)}
    $$

    Adding the two:

    $$
    \ln S_T + \ln\tilde{S}_T = 2\ln S_0 + 2(r - q - v_0/2)T
    $$

    Therefore:

    $$
    \ln\tilde{S}_T = 2\ln S_0 + 2(r - q - v_0/2)T - \ln S_T
    $$

    Exponentiating:

    $$
    \tilde{S}_T = \exp\!\left(2\ln S_0 + 2(r - q - v_0/2)T - \ln S_T\right) = \frac{S_0^2 e^{2(r-q-v_0/2)T}}{S_T}
    $$

    **Negative correlation of call payoffs:** For the call payoff $g(S) = (S - K)^+$, consider the relationship between $S_T$ and $\tilde{S}_T = C/S_T$ where $C = S_0^2 e^{2(r-q-v_0/2)T}$ is a constant. This is a **decreasing** function: when $S_T$ is large, $\tilde{S}_T = C/S_T$ is small, and vice versa.

    When $S_T > K$ (the original path finishes in the money), $\tilde{S}_T = C/S_T < C/K$. For typical ATM parameters, $C/K$ is close to $K$ (since $C \approx K^2$), so $\tilde{S}_T$ is near or below $K$, and the antithetic path finishes near or out of the money.

    Conversely, when $S_T \ll K$ (original path deep OTM), $\tilde{S}_T = C/S_T \gg K$, and the antithetic path finishes deep ITM.

    This creates a strong **negative correlation** between $g(S_T)$ and $g(\tilde{S}_T)$: large payoffs on one path pair with small or zero payoffs on the antithetic. Since $\text{Cov}(g, \tilde{g}) < 0$, the antithetic estimator's variance $\frac{1}{2}(\sigma_g^2 + \text{Cov}(g, \tilde{g}))$ is significantly less than $\sigma_g^2$, producing effective variance reduction.

---

**Exercise 2.**
The variance of the antithetic estimator is $\text{Var}(\hat{V}_{\text{anti}}) = \frac{1}{M}\cdot\frac{\sigma_g^2 + \text{Cov}(g, \tilde{g})}{2}$. If $\text{Cov}(g, \tilde{g}) = -0.8\sigma_g^2$, compute the variance reduction factor $\sigma_g^2/\text{Var}(\hat{V}_{\text{anti}} \cdot M) = 2/(1 + \text{Corr}(g, \tilde{g}))$. How many naive paths would be needed to match the precision of $M = 10{,}000$ antithetic paths?

??? success "Solution to Exercise 2"
    Given $\text{Cov}(g, \tilde{g}) = -0.8\sigma_g^2$, the correlation is $\text{Corr}(g, \tilde{g}) = -0.8$.

    The variance of the antithetic estimator (per-path contribution) is:

    $$
    \text{Var}\!\left(\frac{g + \tilde{g}}{2}\right) = \frac{\sigma_g^2 + \text{Cov}(g, \tilde{g})}{2} = \frac{\sigma_g^2 - 0.8\sigma_g^2}{2} = \frac{0.2\sigma_g^2}{2} = 0.1\sigma_g^2
    $$

    The variance reduction factor is:

    $$
    \frac{\sigma_g^2}{0.1\sigma_g^2} = 10
    $$

    Equivalently, using the formula $\text{factor} = 2/(1 + \text{Corr}(g, \tilde{g}))$:

    $$
    \frac{2}{1 + (-0.8)} = \frac{2}{0.2} = 10
    $$

    **Equivalent naive paths:** $M = 10{,}000$ antithetic paths produce the same precision as $10 \times 10{,}000 = 100{,}000$ naive paths.

    Note that each antithetic "path" actually requires simulating two trajectories (original and mirror), so the computational cost is $2M = 20{,}000$ path simulations. The effective speedup is therefore $100{,}000 / 20{,}000 = 5$, which is still substantial. The factor of 10 in variance corresponds to a factor of $\sqrt{10} \approx 3.16$ in standard error.

---

**Exercise 3.**
The Black-Scholes control variate uses $\bar{\sigma}$ as the control volatility. Explain why setting $\bar{\sigma}$ equal to the Heston ATM implied volatility maximizes the correlation $\rho_{g,C}$ between the Heston and Black-Scholes payoffs. For an ATM call, estimate $\rho_{g,C}$ heuristically: since the Heston and BS models differ primarily in the randomness of variance, and the call payoff is primarily sensitive to the total integrated variance, the correlation should be close to

$$
\rho_{g,C} \approx \frac{\mathbb{E}[\bar{v}]}{\sqrt{\mathbb{E}[\bar{v}^2]}}
$$

where $\bar{v} = \frac{1}{T}\int_0^T v_s\,ds$. Is this ratio close to 1 for typical Heston parameters?

??? success "Solution to Exercise 3"
    The control volatility $\bar{\sigma}$ should maximize the correlation $\rho_{g,C}$ between the Heston payoff $g(S_T^{\text{Heston}})$ and the Black-Scholes payoff $g(S_T^{\text{BS}})$. The two terminal prices are driven by the same Brownian path $W^{(1)}$, but differ in how volatility enters:

    - Heston: $\ln S_T = \ln S_0 + (r-q)T - \frac{1}{2}\int_0^T v_s\,ds + \int_0^T \sqrt{v_s}\,dW_s^{(1)}$
    - Black-Scholes: $\ln S_T^{\text{BS}} = \ln S_0 + (r-q-\bar{\sigma}^2/2)T + \bar{\sigma}\,W_T^{(1)}$

    For an ATM call, the payoff is most sensitive to the total "effective volatility" experienced over $[0,T]$. In the Heston model, this is $\sqrt{\frac{1}{T}\int_0^T v_s\,ds}$, while in Black-Scholes it is the constant $\bar{\sigma}$. Setting $\bar{\sigma}$ equal to the Heston ATM implied volatility aligns the two distributions' centers as closely as possible, maximizing the probability that both payoffs are in the money (or out of the money) on the same paths.

    **Heuristic estimate of** $\rho_{g,C}$: The call payoff depends primarily on the terminal stock price, which in turn depends on the integrated variance $\bar{v} = \frac{1}{T}\int_0^T v_s\,ds$. With $\bar{\sigma}^2 \approx \mathbb{E}[\bar{v}]$, the correlation is related to:

    $$
    \rho_{g,C} \approx \frac{\mathbb{E}[\bar{v}]}{\sqrt{\mathbb{E}[\bar{v}^2]}}
    $$

    By Jensen's inequality (since $\sqrt{\cdot}$ is concave), this ratio satisfies:

    $$
    \frac{\mathbb{E}[\bar{v}]}{\sqrt{\mathbb{E}[\bar{v}^2]}} = \frac{1}{\sqrt{1 + \text{CV}^2(\bar{v})}}
    $$

    where $\text{CV}(\bar{v}) = \text{Std}(\bar{v})/\mathbb{E}[\bar{v}]$ is the coefficient of variation of the integrated variance.

    For typical Heston parameters ($v_0 = 0.04$, $\theta = 0.04$, $\xi = 0.3$, $\kappa = 1.5$), the mean integrated variance is approximately $\theta = 0.04$ and its standard deviation is relatively small (of order $\xi\sqrt{\theta/(2\kappa)} \approx 0.3\sqrt{0.04/3} \approx 0.035$). So $\text{CV} \approx 0.035/0.04 \approx 0.87$ for the instantaneous variance, but the time averaging in $\bar{v}$ reduces this substantially (by roughly $1/\sqrt{T \cdot 2\kappa} \approx 1/\sqrt{3}$), giving $\text{CV}(\bar{v}) \approx 0.5$.

    This yields $\rho_{g,C} \approx 1/\sqrt{1 + 0.25} \approx 0.89$. The actual correlation is typically in the range 0.95--0.99 for ATM options, somewhat higher than this rough estimate because the call payoff is less sensitive to variance fluctuations than the heuristic suggests. The ratio is indeed close to 1 for typical parameters, confirming that the Black-Scholes control is highly effective.

---

**Exercise 4.**
The optimal control variate coefficient is $\beta^* = \text{Cov}(g, C)/\text{Var}(C)$. In the worked example, the control variate reduces the standard error from $\$0.15$ to $\$0.02$, a factor of 7.5 in standard error (factor of $\approx 56$ in variance). Compute $\rho_{g,C}$ from the variance reduction formula $1 - \rho_{g,C}^2 = 1/56$. Is this correlation value realistic for a Black-Scholes control on an ATM Heston call?

??? success "Solution to Exercise 4"
    The variance reduction formula gives:

    $$
    1 - \rho_{g,C}^2 = \frac{\text{Var}(\hat{V}_{\text{cv}})}{\text{Var}(\hat{V})} = \frac{1}{56}
    $$

    Solving for $\rho_{g,C}$:

    $$
    \rho_{g,C}^2 = 1 - \frac{1}{56} = \frac{55}{56} \approx 0.9821
    $$

    $$
    \rho_{g,C} = \sqrt{0.9821} \approx 0.991
    $$

    **Is this realistic?** Yes, a correlation of $0.991$ between the Heston and Black-Scholes payoffs for an ATM call is entirely plausible. The two models share the same underlying Brownian motion $W^{(1)}$ driving the stock price. The only difference is that Heston has stochastic volatility while Black-Scholes has constant volatility. For ATM options:

    - The call payoff is primarily determined by whether the terminal stock price exceeds the strike, which is driven by the same Brownian realization in both models.
    - The volatility difference between the models affects the magnitude of the payoff but rarely changes its sign (ITM vs OTM).
    - Setting $\bar{\sigma}$ to the Heston implied vol aligns the distributions so that the mean payoffs are nearly identical.

    Correlations above 0.99 are routinely observed in practice for ATM options with moderate Heston parameters. The correlation decreases for OTM options (where the payoff is more sensitive to the tail of the distribution, which is where the models differ most) and for longer maturities (where variance randomness accumulates).

---

**Exercise 5.**
For a deep OTM call ($K = 150$, $S_0 = 100$), most naive Monte Carlo paths finish out of the money. The importance sampling shift $\mu^* = [\ln(K/S_0) - (r - q - \bar{v}/2)T]/T$ centers the log-price distribution around $\ln K$. With $r = 0.05$, $\bar{v} = 0.04$, $T = 1$, compute $\mu^*$. What fraction of shifted paths finish in the money versus the fraction under the original measure? Estimate the variance reduction factor for this OTM option.

??? success "Solution to Exercise 5"
    With $K = 150$, $S_0 = 100$, $r = 0.05$, $\bar{v} = 0.04$, $T = 1$:

    $$
    \mu^* = \frac{\ln(150/100) - (0.05 - 0 - 0.02) \times 1}{1} = \frac{\ln(1.5) - 0.03}{1} = \frac{0.4055 - 0.03}{1} = 0.3755
    $$

    **Fraction of paths finishing ITM:**

    Under the **original measure** $\mathbb{Q}$: $\ln S_T \sim N(\ln 100 + 0.03, \, 0.04)$, so $\ln S_T \sim N(4.6352, 0.04)$ with standard deviation $\sqrt{0.04} = 0.2$. The probability of finishing ITM:

    $$
    \mathbb{P}(S_T > 150) = \mathbb{P}\!\left(\ln S_T > \ln 150\right) = \mathbb{P}\!\left(Z > \frac{5.0106 - 4.6352}{0.2}\right) = \mathbb{P}(Z > 1.877) \approx 0.030
    $$

    Only about 3% of paths finish in the money.

    Under the **shifted measure** $\tilde{\mathbb{Q}}$: The drift is increased by $\mu^* = 0.3755$, so $\ln S_T \sim N(4.6352 + 0.3755, 0.04) = N(5.0107, 0.04)$. The probability of finishing ITM:

    $$
    \mathbb{P}(\ln S_T > 5.0106) = \mathbb{P}\!\left(Z > \frac{5.0106 - 5.0107}{0.2}\right) = \mathbb{P}(Z > -0.0005) \approx 0.500
    $$

    Approximately 50% of shifted paths finish in the money, as intended.

    **Variance reduction estimate:** Under the original measure, about 97% of paths contribute zero payoff and are "wasted." The effective sample size is roughly $0.03M$. Under importance sampling, about 50% of paths contribute to the estimator, giving an effective sample size of roughly $0.5M$. The variance reduction factor is approximately:

    $$
    \text{factor} \approx \frac{0.5}{0.03} \approx 17
    $$

    In practice, the reduction factor for deep OTM options is often larger (10--100) because the likelihood ratio reweighting concentrates the estimator on the most informative paths. The exact factor depends on the relationship between the variance of the likelihood-reweighted payoff and the variance of the original payoff, but the order of magnitude is correct.

---

**Exercise 6.**
The warning about variance explosion in importance sampling states that poorly chosen shifts can increase variance. Consider an extreme shift $\mu = 3\mu^*$ (three times the optimal). The likelihood ratio $\exp(-\mu W_T/\sqrt{\bar{v}} - \mu^2 T/(2\bar{v}))$ has very heavy tails. Compute the effective sample size $\text{ESS} = (\sum w_m)^2/\sum w_m^2$ for $M = 1{,}000$ paths and explain why ESS $\ll M$ indicates the estimator is unreliable. What is the maximum safe drift shift as a rule of thumb?

??? success "Solution to Exercise 6"
    With an extreme shift $\mu = 3\mu^*$, the log-price distribution is shifted far beyond the strike. The likelihood ratio for each path is:

    $$
    w_m = \exp\!\left(-\frac{\mu}{\sqrt{\bar{v}}} W_T^{(1),(m)} - \frac{\mu^2}{2\bar{v}} T\right)
    $$

    With $\mu = 3 \times 0.3755 = 1.127$, $\bar{v} = 0.04$, $T = 1$:

    $$
    \frac{\mu}{\sqrt{\bar{v}}} = \frac{1.127}{0.2} = 5.633, \qquad \frac{\mu^2}{2\bar{v}} = \frac{1.270}{0.08} = 15.87
    $$

    The likelihood ratio becomes $w_m = \exp(-5.633 W_T^{(m)} - 15.87)$. Since $W_T^{(m)}$ under the shifted measure has mean $\mu T/\sqrt{\bar{v}} = 5.633$ and standard deviation 1, the exponent $-5.633 W_T^{(m)} - 15.87$ has:

    - Mean: $-5.633 \times 5.633 - 15.87 = -31.73 - 15.87 = -47.6$
    - Standard deviation: $5.633$

    The weights are approximately $\exp(-47.6 + 5.633 Z)$ where $Z \sim N(0,1)$. A $+3\sigma$ event gives weight $\exp(-47.6 + 16.9) = \exp(-30.7) \approx 4.6 \times 10^{-14}$, while a $-3\sigma$ event gives weight $\exp(-47.6 - 16.9) = \exp(-64.5) \approx 10^{-28}$.

    The effective sample size (ESS) measures the number of paths effectively contributing:

    $$
    \text{ESS} = \frac{\left(\sum_{m=1}^M w_m\right)^2}{\sum_{m=1}^M w_m^2}
    $$

    When the weights vary enormously (spanning many orders of magnitude), a few paths with the largest weights dominate both sums. With $M = 1{,}000$ paths and weights varying over $10^{14}$ orders of magnitude, the ESS is typically on the order of $1$--$10$, meaning $\text{ESS} \ll M = 1{,}000$. The estimator effectively relies on just a handful of paths, making it unreliable with enormous variance.

    **Rule of thumb for safe drift shifts:** The optimal shift $\mu^*$ is calibrated so that roughly half the paths contribute to the estimator. Shifts much beyond $\mu^*$ push too many paths into the irrelevant region and create extreme likelihood ratios. A safe rule is to keep $\mu \leq 1.5\mu^*$. Beyond this, the ESS should be monitored: if $\text{ESS} < M/5$, the shift is too aggressive and should be reduced. Some practitioners also use a soft cap: if any single weight exceeds $10\%$ of the total weight sum, the estimator is deemed unreliable.

---

**Exercise 7.**
The combined estimator uses antithetic variates with a Black-Scholes control variate. In the worked example, this achieves a reduction factor of 278. Decompose this into the antithetic contribution and the control variate contribution. If antithetic variates alone give a factor of 3 and control variates alone give a factor of 56, explain why the combined factor ($278 \approx 3 \times 93$) exceeds the product of individual factors. Hint: the antithetic averaging smooths the payoff, increasing the correlation with the control variate.

??? success "Solution to Exercise 7"
    The combined reduction factor of 278 decomposes as follows. If the individual factors were independent, the combined factor would be approximately the product $3 \times 56 = 168$. However, the observed factor of 278 is larger, which indicates a **synergistic interaction** between the two techniques.

    **Decomposition:** Let $\sigma_{\text{naive}}^2$ be the naive variance, $\sigma_{\text{anti}}^2 = \sigma_{\text{naive}}^2/3$ the antithetic variance, and $\sigma_{\text{cv}}^2 = \sigma_{\text{naive}}^2/56$ the control variate variance. The combined variance is $\sigma_{\text{combined}}^2 = \sigma_{\text{naive}}^2/278$.

    - Antithetic contribution to the combined method: factor $= 278/93 = 2.99 \approx 3$ (consistent with antithetic alone)
    - Control variate contribution on the antithetic-averaged payoff: factor $= 93$

    The control variate factor improves from 56 (applied to the raw payoff) to 93 (applied to the antithetic-averaged payoff). This is the synergy.

    **Why the synergy occurs:** The antithetic averaging replaces the payoff $g(S_T)$ with the smoothed payoff $\bar{g} = [g(S_T) + g(\tilde{S}_T)]/2$. This smoothed payoff has several properties that enhance the control variate:

    1. **Reduced kurtosis:** The raw call payoff has a kink at $S_T = K$ (the max function). Antithetic averaging smooths this kink: $\bar{g}$ is closer to a linear function of $\ln S_T$ near the strike, because the antithetic path fills in the gaps. A smoother payoff is better approximated by the Black-Scholes control, increasing $|\rho_{\bar{g}, C}|$.

    2. **Higher correlation with BS control:** The raw correlation is $\rho_{g,C} \approx 0.991$ (from Exercise 4), giving a control variate factor of $1/(1 - 0.991^2) = 56$. The antithetic-averaged payoff has a higher correlation with the antithetic-averaged BS control, say $\rho_{\bar{g},\bar{C}} \approx 0.9946$, giving a factor of $1/(1 - 0.9946^2) \approx 93$.

    3. **Variance stabilization:** Antithetic averaging reduces the variance of the payoff, particularly in the tails. The control variate is most effective when the residual variance (after removing the control) is small. By first reducing the variance through antithetic averaging, the control variate operates on a less noisy signal and achieves higher proportional reduction.

    The lesson is that variance reduction techniques are not merely additive---they interact, and the optimal strategy applies them in the right order: antithetic averaging first (to smooth the payoff), then control variates (to exploit the enhanced correlation).
