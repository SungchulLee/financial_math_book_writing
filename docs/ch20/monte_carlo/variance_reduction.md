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
