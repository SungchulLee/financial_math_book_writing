# Variance Reduction Techniques

Monte Carlo pricing converges at the rate $O(1/\sqrt{N})$, so halving the standard error requires quadrupling the number of paths. Variance reduction techniques exploit problem structure to achieve the same accuracy with fewer paths. In the Hull-White model, the availability of closed-form bond prices and the Gaussian distribution of the short rate provide particularly effective variance reduction opportunities. This section presents the main techniques --- antithetic variates, control variates with the zero-coupon bond as control, and importance sampling --- together with their mathematical justification and practical guidance.

## Antithetic Variates

The antithetic variate method pairs each standard normal draw $Z$ with its mirror $-Z$. Because the Hull-White short rate is driven by Gaussian increments, replacing $Z_i$ with $-Z_i$ at every time step produces a mirror path.

**Definition.** Let $\hat{V}^{(k)}$ denote the discounted payoff on path $k$ driven by $\{Z_1^{(k)}, \ldots, Z_N^{(k)}\}$, and let $\hat{V}^{(k,-)}$ denote the payoff on the antithetic path driven by $\{-Z_1^{(k)}, \ldots, -Z_N^{(k)}\}$. The antithetic estimator is

$$
\hat{V}_{\text{anti}} = \frac{1}{N_{\text{paths}}} \sum_{k=1}^{N_{\text{paths}}} \frac{\hat{V}^{(k)} + \hat{V}^{(k,-)}}{2}
$$

**Proposition (Variance reduction).** The variance of the antithetic estimator satisfies

$$
\text{Var}(\hat{V}_{\text{anti}}) = \frac{1}{2}\text{Var}(\hat{V}) + \frac{1}{2}\text{Cov}(\hat{V}, \hat{V}^{(-)})
$$

When the payoff function $g$ is monotone in the short rate path, the covariance $\text{Cov}(\hat{V}, \hat{V}^{(-)}) < 0$, so the antithetic estimator has strictly lower variance than the standard estimator using the same total number of payoff evaluations.

???+ note "Proof"
    Write $Y = (\hat{V} + \hat{V}^{(-)})/2$. Then $\text{Var}(Y) = \frac{1}{4}[\text{Var}(\hat{V}) + \text{Var}(\hat{V}^{(-)}) + 2\text{Cov}(\hat{V}, \hat{V}^{(-)})]$. Since $Z$ and $-Z$ have the same distribution, $\text{Var}(\hat{V}^{(-)}) = \text{Var}(\hat{V})$, giving $\text{Var}(Y) = \frac{1}{2}\text{Var}(\hat{V}) + \frac{1}{2}\text{Cov}(\hat{V}, \hat{V}^{(-)})$. The covariance is negative when $g$ is monotone because $\hat{V}$ and $\hat{V}^{(-)}$ move in opposite directions. $\square$

!!! warning "When Antithetic Variates Fail"
    For payoffs that are symmetric functions of the rate path (e.g., straddles or variance swaps), $\text{Cov}(\hat{V}, \hat{V}^{(-)}) \approx 0$, and the antithetic method provides negligible benefit. It is most effective for directional payoffs such as caps, floors, and callable bonds.

## Control Variates

Control variates reduce variance by exploiting a correlated random variable whose expectation is known analytically. In the Hull-White model, the zero-coupon bond price is the canonical control variate because $P(0, T)$ is known exactly.

**Definition.** Let $\hat{V}^{(k)}$ be the discounted payoff on path $k$ and let $C^{(k)} = 1/M^{(k)}(T)$ be the Monte Carlo discount factor on the same path. The control variate estimator is

$$
\hat{V}_{\text{CV}} = \frac{1}{N_{\text{paths}}} \sum_{k=1}^{N_{\text{paths}}} \left[\hat{V}^{(k)} - \beta\!\left(C^{(k)} - P(0,T)\right)\right]
$$

where $\beta$ is a coefficient chosen to minimize variance, and $P(0,T)$ is the known analytical bond price.

**Proposition (Optimal beta).** The variance-minimizing coefficient is

$$
\beta^* = \frac{\text{Cov}(\hat{V}, C)}{\text{Var}(C)}
$$

and the resulting variance is

$$
\text{Var}(\hat{V}_{\text{CV}}) = (1 - \rho^2)\,\text{Var}(\hat{V})
$$

where $\rho = \text{Corr}(\hat{V}, C)$. The variance reduction factor is $1 - \rho^2$.

???+ note "Proof"
    The control variate estimator for a single path is $Y = \hat{V} - \beta(C - P(0,T))$. Since $\mathbb{E}[C] = P(0,T)$, we have $\mathbb{E}[Y] = \mathbb{E}[\hat{V}]$, so the estimator is unbiased. The variance is $\text{Var}(Y) = \text{Var}(\hat{V}) - 2\beta\,\text{Cov}(\hat{V}, C) + \beta^2\,\text{Var}(C)$. Minimizing over $\beta$ gives $\beta^* = \text{Cov}(\hat{V}, C)/\text{Var}(C)$. Substituting back yields $\text{Var}(Y) = \text{Var}(\hat{V})(1 - \rho^2)$. $\square$

In practice, $\beta^*$ is estimated from a pilot run or from the same simulation paths, introducing a small bias that vanishes as $N_{\text{paths}} \to \infty$.

### Multiple Control Variates

When pricing a derivative with cash flows at multiple dates $T_1, \ldots, T_n$, each bond price $P(0, T_i)$ serves as a separate control variate. The multi-variate extension uses a vector of controls $\mathbf{C} = (C_1, \ldots, C_n)^{\top}$ with known expectations $\boldsymbol{\mu}_C = (P(0,T_1), \ldots, P(0,T_n))^{\top}$:

$$
\hat{V}_{\text{CV}} = \bar{V} - \boldsymbol{\beta}^{\top}(\bar{\mathbf{C}} - \boldsymbol{\mu}_C)
$$

where $\boldsymbol{\beta}^* = \Sigma_C^{-1}\,\text{Cov}(\hat{V}, \mathbf{C})$ and $\Sigma_C = \text{Var}(\mathbf{C})$.

### Swaption as Control

For swaption pricing on a tree-calibrated model, the European swaption has a known analytical price via Jamshidian's trick. This can serve as a control variate when pricing the Bermudan swaption via Monte Carlo:

$$
\hat{V}_{\text{Berm}} = \hat{V}_{\text{Berm,MC}} - \beta\!\left(\hat{V}_{\text{Euro,MC}} - V_{\text{Euro,analytic}}\right)
$$

The correlation between European and Bermudan swaption payoffs is typically very high, making this an effective variance reduction strategy.

## Importance Sampling

Importance sampling changes the sampling distribution to concentrate paths in regions where the payoff is large. For a derivative with payoff $g(r_T)$ and risk-neutral density $f(r_T)$, the price is

$$
V_0 = \int g(r_T)\,\frac{f(r_T)}{M(T)}\,dr_T = \int g(r_T)\,\frac{f(r_T)}{h(r_T)}\,\frac{h(r_T)}{M(T)}\,dr_T
$$

where $h$ is the importance sampling density. The estimator becomes

$$
\hat{V}_{\text{IS}} = \frac{1}{N_{\text{paths}}} \sum_{k=1}^{N_{\text{paths}}} \frac{g(r_T^{(k)})}{M^{(k)}(T)} \cdot \frac{f(r_T^{(k)})}{h(r_T^{(k)})}
$$

where paths are now sampled from $h$ instead of $f$.

**Application to out-of-the-money options.** For a deep out-of-the-money caplet with strike $K$ far above the forward rate, most paths under the risk-neutral measure produce zero payoff. By shifting the mean of the Gaussian short rate distribution toward $K$:

$$
h(r_T) = \frac{1}{\sigma_r \sqrt{2\pi}} \exp\!\left(-\frac{(r_T - \mu_{\text{IS}})^2}{2\sigma_r^2}\right)
$$

with $\mu_{\text{IS}}$ chosen near $K$, more paths produce non-zero payoffs. The likelihood ratio $f(r_T)/h(r_T) = \exp\!\left(-\frac{(\mu_{\text{IS}} - \mu)(\mu_{\text{IS}} + \mu - 2r_T)}{2\sigma_r^2}\right)$ corrects for the change in measure.

!!! tip "Mean Shift for Hull-White"
    In the Hull-White exact simulation, importance sampling via mean shift is straightforward: replace $Z_i \sim N(0,1)$ with $Z_i \sim N(\theta_{\text{IS}}, 1)$ where $\theta_{\text{IS}}$ is chosen to center the short rate distribution near the payoff region. The likelihood ratio is $\exp(-\theta_{\text{IS}} Z_i + \frac{1}{2}\theta_{\text{IS}}^2)$ per time step.

## Stratified Sampling

Stratified sampling partitions the probability space into strata and samples a fixed number of paths from each stratum. For Hull-White, a natural stratification is on the terminal short rate $r_T$.

Partition the standard normal CDF into $K$ equal-probability strata $[u_{j-1}, u_j)$ where $u_j = j/K$ for $j = 0, 1, \ldots, K$. Within stratum $j$, draw $Z^{(j)} = \Phi^{-1}(U)$ where $U \sim \text{Uniform}(u_{j-1}, u_j)$. The stratified estimator is

$$
\hat{V}_{\text{strat}} = \frac{1}{K} \sum_{j=1}^{K} \frac{1}{n_j} \sum_{i=1}^{n_j} \hat{V}^{(j,i)}
$$

where $n_j$ is the number of paths in stratum $j$. With proportional allocation ($n_j = N_{\text{paths}}/K$), the variance is guaranteed to be no larger than the unstratified variance.

## Combining Techniques

Variance reduction techniques can be combined. A common and effective combination for Hull-White pricing is:

1. **Antithetic variates** for the random draws
2. **Control variates** with the zero-coupon bond as control
3. **Stratification** on the first time step

The combined estimator applies antithetic variates within each stratum and then applies the control variate correction to the aggregate.

???+ example "Variance Reduction Comparison"
    ```python
    def main():
        hw = HullWhite(sigma=0.01, lambd=0.05, P=P_market)
        K = 0.95
        T1 = 5.0
        T2 = 10.0

        # Analytic price for comparison
        V_exact = hw.compute_ZCB_Option_Price(K, T1, T2, CP=OptionType.CALL)

        # Standard MC
        t, R, M = hw.generate_sample_paths(10_000, 500, T1, seed=42)
        P_T = np.array([hw.compute_ZCB(T1, T2, r) for r in R[:, -1]])
        V_std = np.mean(np.maximum(P_T - K, 0) / M[:, -1])

        # Antithetic MC (Z and -Z paths already paired)
        # Control variate MC (use 1/M as control)
        C = 1.0 / M[:, -1]
        beta = np.cov(np.maximum(P_T - K, 0) / M[:, -1], C)[0, 1] / np.var(C)
        V_cv = V_std - beta * (np.mean(C) - P_market(T1))

        print(f"Exact:    {V_exact:.6f}")
        print(f"Std MC:   {V_std:.6f}")
        print(f"CV MC:    {V_cv:.6f}")
    ```

## Summary

Variance reduction is essential for efficient Monte Carlo pricing in the Hull-White model. Antithetic variates exploit the symmetry of Gaussian increments and are most effective for monotone payoffs. Control variates using analytically known bond prices provide substantial variance reduction with minimal implementation overhead, achieving reduction factors of $1 - \rho^2$ where $\rho$ is the correlation between the payoff and the control. Importance sampling shifts the sampling distribution toward the payoff region, particularly useful for out-of-the-money options. These techniques can be combined to achieve multiplicative variance reduction, significantly reducing the computational cost of pricing path-dependent interest rate derivatives.

---

## Exercises

**Exercise 1.** Show that the antithetic estimator $\hat{V}_{\text{anti}} = \frac{1}{N}\sum_{k=1}^N \frac{\hat{V}^{(k)} + \hat{V}^{(k,-)}}{2}$ is unbiased. Then prove that $\text{Var}(\hat{V}_{\text{anti}}) \leq \text{Var}(\hat{V}_{\text{std}})$ when the payoff is a monotone function of the short rate path.

??? success "Solution to Exercise 1"
    **Unbiasedness:** Since $Z$ and $-Z$ have the same distribution ($\mathcal{N}(0,1)$ is symmetric), the discounted payoffs $\hat{V}^{(k)}$ and $\hat{V}^{(k,-)}$ have the same expectation:

    $$
    \mathbb{E}[\hat{V}^{(k,-)}] = \mathbb{E}[\hat{V}^{(k)}] = \mathbb{E}[\hat{V}]
    $$

    Therefore

    $$
    \mathbb{E}[\hat{V}_{\text{anti}}] = \frac{1}{N}\sum_{k=1}^N \mathbb{E}\!\left[\frac{\hat{V}^{(k)} + \hat{V}^{(k,-)}}{2}\right] = \frac{1}{N}\sum_{k=1}^N \mathbb{E}[\hat{V}] = \mathbb{E}[\hat{V}]
    $$

    so the estimator is unbiased.

    **Variance reduction for monotone payoffs:** Let $Y^{(k)} = (\hat{V}^{(k)} + \hat{V}^{(k,-)})/2$. Since the $Y^{(k)}$ are i.i.d.:

    $$
    \text{Var}(\hat{V}_{\text{anti}}) = \frac{1}{N}\text{Var}(Y)
    $$

    Now $\text{Var}(Y) = \frac{1}{4}[\text{Var}(\hat{V}) + \text{Var}(\hat{V}^{(-)}) + 2\text{Cov}(\hat{V}, \hat{V}^{(-)})]$. Since $\text{Var}(\hat{V}^{(-)}) = \text{Var}(\hat{V})$:

    $$
    \text{Var}(Y) = \frac{1}{2}\text{Var}(\hat{V}) + \frac{1}{2}\text{Cov}(\hat{V}, \hat{V}^{(-)})
    $$

    The standard estimator using $2N$ paths has variance $\frac{1}{2N}\text{Var}(\hat{V})$. The antithetic estimator uses $N$ pairs ($2N$ total payoff evaluations) and has variance $\frac{1}{N}\text{Var}(Y) = \frac{1}{2N}\text{Var}(\hat{V}) + \frac{1}{2N}\text{Cov}(\hat{V}, \hat{V}^{(-)})$.

    For a monotone payoff $g$, when the short rate path increases (high $Z$'s), the payoff moves one way; for the antithetic path (low $Z$'s = $-Z$), the rate decreases and the payoff moves the opposite way. This negative correlation gives $\text{Cov}(\hat{V}, \hat{V}^{(-)}) < 0$, so

    $$
    \text{Var}(\hat{V}_{\text{anti}}) < \frac{1}{2N}\text{Var}(\hat{V}) = \text{Var}(\hat{V}_{\text{std}})
    $$

    where $\hat{V}_{\text{std}}$ is the standard estimator with the same $2N$ evaluations.

---

**Exercise 2.** For a caplet with payoff $\max(l_k - K, 0)$ where $l_k$ is a decreasing function of $r_{T_{k-1}}$, explain why antithetic variates are effective. For a straddle with payoff $|l_k - K|$, explain why antithetic variates provide little benefit.

??? success "Solution to Exercise 2"
    **Caplet:** The payoff is $\max(\ell_k - K, 0)$ where $\ell_k$ is a decreasing function of $r_{T_{k-1}}$ (higher rates mean higher discount rates, lower bond prices, and thus higher LIBOR rates --- actually $\ell_k$ is an increasing function of $r_{T_{k-1}}$ via $\ell_k = (1/P(T_{k-1},T_k) - 1)/\delta_k$ and $P$ is decreasing in $r$). More precisely, since $P(T_{k-1}, T_k)$ is decreasing in $r_{T_{k-1}}$, $\ell_k = (1/P - 1)/\delta$ is increasing in $r_{T_{k-1}}$. The caplet payoff is therefore a monotone increasing function of $r_{T_{k-1}}$.

    When $Z$ is replaced by $-Z$, the simulated rate path shifts lower, making $\ell_k$ smaller and the caplet payoff smaller. The original and antithetic payoffs are negatively correlated: $\text{Cov}(\hat{V}, \hat{V}^{(-)}) < 0$. This gives effective variance reduction.

    **Straddle:** The straddle payoff $|\ell_k - K|$ is a V-shaped function: it increases for both $\ell_k > K$ and $\ell_k < K$. When $Z$ is replaced by $-Z$, the rate moves in the opposite direction, but the payoff may move in the same direction (e.g., if the original path gives $\ell_k > K$, the antithetic may give $\ell_k < K$, and both payoffs $|\ell_k - K|$ may be similar in magnitude). The covariance $\text{Cov}(\hat{V}, \hat{V}^{(-)}) \approx 0$ because the payoff is approximately symmetric around $K$, providing little variance reduction.

---

**Exercise 3.** The control variate estimator uses $C^{(k)} = 1/M^{(k)}(T)$ with known expectation $P(0,T)$. Derive the optimal coefficient $\beta^* = \text{Cov}(\hat{V}, C)/\text{Var}(C)$ by minimizing $\text{Var}(\hat{V} - \beta(C - P(0,T)))$ over $\beta$. If $\rho = \text{Corr}(\hat{V}, C) = 0.95$, what is the variance reduction factor?

??? success "Solution to Exercise 3"
    The variance of the control variate estimator for a single path is

    $$
    \text{Var}(\hat{V} - \beta(C - P(0,T))) = \text{Var}(\hat{V}) - 2\beta\,\text{Cov}(\hat{V}, C) + \beta^2\,\text{Var}(C)
    $$

    This is a quadratic function of $\beta$. Taking the derivative and setting it to zero:

    $$
    \frac{d}{d\beta}\text{Var} = -2\,\text{Cov}(\hat{V}, C) + 2\beta\,\text{Var}(C) = 0
    $$

    Solving:

    $$
    \beta^* = \frac{\text{Cov}(\hat{V}, C)}{\text{Var}(C)}
    $$

    Substituting $\beta^*$ back:

    $$
    \text{Var}(\hat{V}_{\text{CV}}) = \text{Var}(\hat{V}) - \frac{[\text{Cov}(\hat{V}, C)]^2}{\text{Var}(C)} = \text{Var}(\hat{V})\!\left(1 - \frac{[\text{Cov}(\hat{V}, C)]^2}{\text{Var}(\hat{V})\,\text{Var}(C)}\right) = (1 - \rho^2)\,\text{Var}(\hat{V})
    $$

    For $\rho = 0.95$:

    $$
    1 - \rho^2 = 1 - 0.9025 = 0.0975
    $$

    The variance reduction factor is $0.0975$, meaning the variance is reduced by approximately 90.25%. This is equivalent to a roughly $10\times$ increase in the effective number of paths.

---

**Exercise 4.** For a Bermudan swaption priced by Monte Carlo, the European swaption (with analytic price via Jamshidian) serves as a control variate. Explain why the correlation between the Bermudan and European payoffs is high, and estimate the expected variance reduction factor.

??? success "Solution to Exercise 4"
    The Bermudan swaption differs from the European swaption only by having additional exercise opportunities. On most paths, the optimal exercise date for the Bermudan swaption coincides with the European exercise date (the first allowed exercise date), because early exercise is optimal only on a subset of paths.

    The payoffs are highly correlated because:

    1. Both depend on the same underlying swap value, driven by the same short rate path.
    2. The Bermudan payoff equals the European payoff on paths where early exercise is not optimal (which is the majority of paths).
    3. On paths where early exercise is optimal, the Bermudan payoff is strictly larger but still correlated with the terminal swap value.

    Typical correlations between Bermudan and European swaption payoffs are $\rho \approx 0.95$--$0.99$.

    **Expected variance reduction:** Using $\rho = 0.97$ as a representative value:

    $$
    1 - \rho^2 = 1 - 0.9409 = 0.0591
    $$

    The variance is reduced by approximately 94%, equivalent to a $\sim 17\times$ increase in effective paths. This makes the European swaption an exceptionally effective control variate for Bermudan swaption pricing.

---

**Exercise 5.** Importance sampling for a deep out-of-the-money caplet shifts the mean of $r_T$ toward the strike $K$. The likelihood ratio per time step is $\exp(-\theta_{\text{IS}} Z_i + \frac{1}{2}\theta_{\text{IS}}^2)$. Derive this formula by computing the Radon–Nikodym derivative between $\mathcal{N}(\theta_{\text{IS}}, 1)$ and $\mathcal{N}(0,1)$ for a single normal draw.

??? success "Solution to Exercise 5"
    Let $Z \sim \mathcal{N}(0, 1)$ under the original measure, and $\tilde{Z} = Z - \theta_{\text{IS}} \sim \mathcal{N}(-\theta_{\text{IS}}, 1)$ under the original measure (equivalently, $Z = \tilde{Z} + \theta_{\text{IS}}$ where $\tilde{Z} \sim \mathcal{N}(0, 1)$ under the importance sampling measure).

    Under the importance sampling measure, $Z \sim \mathcal{N}(\theta_{\text{IS}}, 1)$. The densities are:

    $$
    f(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2} \quad (\text{original})
    $$

    $$
    h(z) = \frac{1}{\sqrt{2\pi}}e^{-(z - \theta_{\text{IS}})^2/2} \quad (\text{importance sampling})
    $$

    The Radon–Nikodym derivative (likelihood ratio) is

    $$
    \frac{f(z)}{h(z)} = \frac{e^{-z^2/2}}{e^{-(z-\theta_{\text{IS}})^2/2}} = \exp\!\left(-\frac{z^2}{2} + \frac{(z - \theta_{\text{IS}})^2}{2}\right)
    $$

    Expanding the exponent:

    $$
    -\frac{z^2}{2} + \frac{z^2 - 2z\theta_{\text{IS}} + \theta_{\text{IS}}^2}{2} = -z\theta_{\text{IS}} + \frac{\theta_{\text{IS}}^2}{2}
    $$

    Therefore

    $$
    \frac{f(z)}{h(z)} = \exp\!\left(-\theta_{\text{IS}}\,z + \frac{\theta_{\text{IS}}^2}{2}\right)
    $$

    When sampling $Z_i \sim \mathcal{N}(\theta_{\text{IS}}, 1)$ at each time step, the per-step likelihood ratio is $\exp(-\theta_{\text{IS}} Z_i + \frac{1}{2}\theta_{\text{IS}}^2)$, and the total likelihood ratio over $N$ steps is the product $\prod_{i=1}^N \exp(-\theta_{\text{IS}} Z_i + \frac{1}{2}\theta_{\text{IS}}^2)$.

---

**Exercise 6.** Stratified sampling partitions the first standard normal draw into $K$ equal-probability strata. For $K = 10$ strata and $N = 1000$ total paths (100 per stratum), describe the sampling procedure. Why is the stratified estimator guaranteed to have variance no larger than the unstratified estimator?

??? success "Solution to Exercise 6"
    **Stratified sampling procedure with $K = 10$ strata and $N = 1000$ paths:**

    1. Partition the unit interval $[0, 1]$ into $K = 10$ equal strata: $[0, 0.1)$, $[0.1, 0.2)$, $\ldots$, $[0.9, 1.0]$.
    2. Allocate $n_j = 1000/10 = 100$ paths to each stratum $j$.
    3. For stratum $j$ ($j = 1, \ldots, 10$):
        - Draw $n_j = 100$ uniform samples $U_1, \ldots, U_{100} \sim \text{Uniform}((j-1)/10,\; j/10)$
        - Transform to normal: $Z_i = \Phi^{-1}(U_i)$, giving samples from the $j$-th quantile range of $\mathcal{N}(0,1)$
        - Use $Z_i$ as the first time step's normal draw; all subsequent time steps use unstratified standard normal draws
        - Simulate each path and compute the discounted payoff $\hat{V}^{(j,i)}$
    4. The stratified estimator is $\hat{V}_{\text{strat}} = \frac{1}{10}\sum_{j=1}^{10}\frac{1}{100}\sum_{i=1}^{100}\hat{V}^{(j,i)}$

    **Why variance is guaranteed to decrease:** The total variance decomposes as

    $$
    \text{Var}(\hat{V}) = \mathbb{E}[\text{Var}(\hat{V} \mid J)] + \text{Var}(\mathbb{E}[\hat{V} \mid J])
    $$

    where $J$ is the stratum index. The stratified estimator eliminates the between-stratum variance $\text{Var}(\mathbb{E}[\hat{V} \mid J])$ by sampling equally from each stratum, so

    $$
    \text{Var}(\hat{V}_{\text{strat}}) = \frac{1}{K}\sum_{j=1}^{K}\frac{\text{Var}_j(\hat{V})}{n_j} \leq \frac{1}{N}\mathbb{E}[\text{Var}(\hat{V} \mid J)] \leq \frac{1}{N}\text{Var}(\hat{V})
    $$

    The inequality is strict whenever the stratum means $\mathbb{E}[\hat{V} \mid J]$ differ across strata.

---

**Exercise 7.** Describe a combined variance reduction strategy using antithetic variates, control variates (with ZCB as control), and stratification on the first time step. In what order should these techniques be applied? Estimate the total variance reduction factor if each technique independently reduces variance by 50%.

??? success "Solution to Exercise 7"
    **Combined strategy and application order:**

    1. **Stratification (applied first):** Partition the first normal draw $Z_1$ into $K$ equal-probability strata. Within each stratum, draw the first time step's $Z_1$ from the restricted range. This ensures representative coverage of the first factor driving rate movements.

    2. **Antithetic variates (applied second):** Within each stratum, for each path driven by $(Z_1, Z_2, \ldots, Z_N)$, generate the antithetic path $(-Z_1, -Z_2, \ldots, -Z_N)$. Note: the antithetic $-Z_1$ will fall in a different stratum, so in practice, pair paths within each stratum or pair strata symmetrically (stratum $j$ with stratum $K+1-j$).

    3. **Control variates (applied last):** After computing the stratified-antithetic estimator, apply the control variate correction using the ZCB discount factor:

        $$
        \hat{V}_{\text{combined}} = \hat{V}_{\text{strat+anti}} - \beta^*\!\left(\bar{C}_{\text{strat+anti}} - P(0, T)\right)
        $$

        where $\beta^*$ is estimated from the same simulation.

    **Order rationale:** Stratification and antithetic variates modify the sampling procedure and must be applied during path generation. Control variates are a post-processing correction applied to the computed payoffs.

    **Total variance reduction factor:** If each technique independently reduces variance by 50% (factor of 0.5), and the techniques operate on approximately independent sources of variance, the combined factor is approximately

    $$
    0.5 \times 0.5 \times 0.5 = 0.125
    $$

    This means the combined strategy reduces variance by about 87.5%, equivalent to an $8\times$ increase in effective paths. In practice, the techniques are not perfectly independent (e.g., control variates may partially capture the same variance as antithetic variates), so the actual combined reduction may be somewhat less than the multiplicative product, but it is still substantially better than any single technique alone.
