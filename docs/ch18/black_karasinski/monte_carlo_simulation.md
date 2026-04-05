# Monte Carlo Simulation for the Black-Karasinski Model

Monte Carlo simulation is the natural complement to the trinomial tree for Black-Karasinski pricing. While trees excel at Bermudan-style products, Monte Carlo handles high-dimensional path-dependent derivatives and scales well to multi-factor extensions. A key advantage of the BK model for Monte Carlo is that the log-rate $x_t = \ln r_t$ follows a linear OU process, enabling exact simulation without any discretization error in the state variable. The only approximation arises from the numerical integration of the discount factor. This section develops the simulation algorithm, presents variance reduction techniques, and demonstrates convergence through benchmark comparisons.

---

## Exact simulation of the log-rate process

The BK log-rate satisfies the OU SDE

$$
dx_t = [\theta(t) - ax_t]\,dt + \sigma\,dW_t
$$

Given $x_s$ at time $s$, the conditional distribution at time $t > s$ is

$$
x_t \mid x_s \sim \mathcal{N}\!\left(x_s\,e^{-a(t-s)} + \mu_\theta(s,t),\;\frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})\right)
$$

where $\mu_\theta(s,t) = \int_s^t e^{-a(t-u)}\theta(u)\,du$ depends on the time-dependent drift.

### Handling the time-dependent drift

When $\theta(t)$ is piecewise constant (as extracted from a calibrated tree), the integral simplifies on each interval $[t_k, t_{k+1}]$:

$$
\mu_\theta(t_k, t_{k+1}) = \frac{\theta_k}{a}(1 - e^{-a\Delta t})
$$

where $\theta_k = \theta(t_k)$ is the constant value on $[t_k, t_{k+1}]$.

### Simulation step

For each time step $t_k \to t_{k+1}$:

$$
x_{t_{k+1}} = x_{t_k}\,e^{-a\Delta t} + \frac{\theta_k}{a}(1 - e^{-a\Delta t}) + \sigma\sqrt{\frac{1 - e^{-2a\Delta t}}{2a}}\,Z_k
$$

where $Z_k \sim \mathcal{N}(0,1)$. The short rate is $r_{t_k} = e^{x_{t_k}}$.

!!! tip "Exact vs Euler for BK"
    The exact OU simulation has zero discretization error in $x_t$. This is a significant advantage over models where exact simulation requires special distributions (like the non-central chi-squared for CIR). Only standard Gaussian random numbers are needed, making BK Monte Carlo both simple and unbiased in the state variable.

---

## Bond pricing estimator

The zero-coupon bond price is estimated by

$$
\hat{P}(0, T) = \frac{1}{M}\sum_{m=1}^{M}\exp\!\left(-\int_0^T r_s^{(m)}\,ds\right)
$$

The integral is approximated numerically. The trapezoidal rule gives

$$
\int_0^T r_s\,ds \approx \sum_{k=0}^{N-1}\frac{r_{t_k} + r_{t_{k+1}}}{2}\Delta t_k = \sum_{k=0}^{N-1}\frac{e^{x_{t_k}} + e^{x_{t_{k+1}}}}{2}\Delta t_k
$$

!!! warning "Integration accuracy matters"
    Although the simulation of $x_t$ is exact, the numerical integration of $\int e^{x_s}\,ds$ introduces an $O(\Delta t^2)$ error per step (trapezoidal) or $O(\Delta t)$ (left-point Riemann). For short time steps ($\Delta t \leq 0.01$ year), the trapezoidal error is negligible. For larger steps, Simpson's rule or Gaussian quadrature may be needed.

---

## Standard error and convergence

The Monte Carlo estimator converges as $O(1/\sqrt{M})$:

$$
\text{SE} = \frac{\hat{s}}{\sqrt{M}}, \qquad 95\% \text{ CI}: \hat{P} \pm 1.96\cdot\text{SE}
$$

The total error combines statistical error ($O(1/\sqrt{M})$) and integration error ($O(\Delta t^p)$ with $p = 1$ or $2$).

---

## Variance reduction

### Antithetic variates

For each path with innovations $Z_1, \ldots, Z_N$, generate an antithetic path with $-Z_1, \ldots, -Z_N$:

$$
\hat{P}_{\text{anti}} = \frac{1}{M}\sum_{m=1}^{M}\frac{Y_m + Y_m'}{2}
$$

Since the discount factor $e^{-\int r\,ds}$ is convex in the driving noise, the antithetic estimator has lower variance. Typical reduction: 30--50%.

### Control variates using moments

The conditional mean of $r_t = e^{x_t}$ is

$$
\mathbb{E}[r_t] = \exp\!\left(\mathbb{E}[x_t] + \frac{1}{2}\text{Var}(x_t)\right)
$$

where $\mathbb{E}[x_t]$ and $\text{Var}(x_t)$ are known in closed form from the OU transition density. Use $\bar{r}^{(m)} = \frac{1}{N}\sum_k r_{t_k}^{(m)}$ as a control variate with known mean:

$$
\hat{P}^{\text{CV}} = \hat{P} - \beta\left(\frac{1}{M}\sum_m \bar{r}^{(m)} - \mathbb{E}[\bar{r}]\right)
$$

The optimal $\beta$ is estimated by regression. Typical reduction: 60--80%.

### Importance sampling

Shift the drift of $x_t$ to concentrate paths in regions where the discount factor is most variable. A common choice shifts the long-run mean downward (emphasizing high-discount-factor paths), with the likelihood ratio correction:

$$
\hat{P}_{\text{IS}} = \frac{1}{M}\sum_{m=1}^{M}Y_m\cdot L_m
$$

where $L_m$ is the Radon-Nikodym derivative between the shifted and original measures. When well-tuned, importance sampling can reduce variance by 90% or more, but a poorly chosen shift can increase it.

---

## Path-dependent derivatives

Monte Carlo is indispensable for products whose payoffs depend on the rate path.

### Range accrual

A range accrual note pays coupon proportional to the time the rate spends in $[L, U]$:

$$
V(0) = \frac{1}{M}\sum_{m=1}^{M}\exp\!\left(-\sum_k r_{t_k}^{(m)}\Delta t\right)\cdot Nc\,\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}_{\{L \leq r_{T_i}^{(m)} \leq U\}}
$$

### Callable bond (with Longstaff-Schwartz)

For callable bonds with early exercise, the **Longstaff-Schwartz** algorithm combines forward simulation with backward regression:

1. Simulate $M$ paths forward
2. At each exercise date $t_k$ (starting from the last), regress the continuation value on basis functions of $x_{t_k}$
3. Exercise if the immediate payoff exceeds the estimated continuation value

This approach extends the BK Monte Carlo to American-style products that are traditionally priced on trees.

---

## Convergence verification

Verify the MC implementation against tree prices for zero-coupon bonds.

| $M$ | $N_t$ | $\hat{P}(0,5)$ | SE | Tree price |
|:---:|:-----:|:---------------:|:---:|:----------:|
| 10,000 | 250 | 0.7698 | 0.0009 | 0.7700 |
| 100,000 | 250 | 0.7701 | 0.0003 | 0.7700 |
| 100,000 | 50 | 0.7695 | 0.0003 | 0.7700 |

The first two rows show the statistical error decreasing with $M$. The third row shows a larger integration error from fewer time steps ($N_t = 50$), demonstrating the importance of adequate time grid resolution.

---

## Summary

Monte Carlo simulation for the Black-Karasinski model benefits from the exact Gaussian simulation of the log-rate $x_t = \ln r_t$, eliminating discretization error in the state variable. The only numerical approximation is the integration of the discount factor $\int e^{x_s}\,ds$, which is controlled by the time step size. Antithetic variates and control variates provide substantial variance reduction (30--80%), and the Longstaff-Schwartz algorithm extends the method to American-style exercise. Monte Carlo complements the trinomial tree by handling path-dependent and high-dimensional products, and convergence should be verified against tree prices for plain-vanilla bonds before applying to exotic derivatives.

---

## Exercises

**Exercise 1.** Given BK parameters $a = 0.10$, $\sigma = 0.20$, piecewise-constant $\theta_k = -0.25$, and current log rate $x_0 = \ln(0.05)$, write out the exact simulation update for $x_{\Delta t}$ with $\Delta t = 0.01$ year. Compute the numerical values of the conditional mean, conditional standard deviation, and express $x_{\Delta t}$ in terms of a single standard normal draw $Z$.

??? success "Solution to Exercise 1"
    With $a = 0.10$, $\sigma = 0.20$, $\theta_k = -0.25$, $x_0 = \ln(0.05) \approx -2.9957$, and $\Delta t = 0.01$:

    The exact simulation update is

    $$
    x_{\Delta t} = x_0 e^{-a\Delta t} + \frac{\theta_k}{a}(1 - e^{-a\Delta t}) + \sigma\sqrt{\frac{1 - e^{-2a\Delta t}}{2a}}\,Z
    $$

    **Conditional mean** (deterministic part):

    $$
    e^{-a\Delta t} = e^{-0.001} = 0.999000
    $$

    $$
    x_0 e^{-a\Delta t} = (-2.9957)(0.999000) = -2.9927
    $$

    $$
    \frac{\theta_k}{a}(1 - e^{-a\Delta t}) = \frac{-0.25}{0.10}(1 - 0.999000) = (-2.5)(0.001000) = -0.002500
    $$

    $$
    \mathbb{E}[x_{\Delta t}] = -2.9927 + (-0.002500) = -2.9952
    $$

    **Conditional standard deviation**:

    $$
    e^{-2a\Delta t} = e^{-0.002} = 0.998004
    $$

    $$
    \frac{1 - e^{-2a\Delta t}}{2a} = \frac{1 - 0.998004}{0.20} = \frac{0.001996}{0.20} = 0.009980
    $$

    $$
    \sigma\sqrt{0.009980} = 0.20 \times 0.09990 = 0.019980
    $$

    **Complete expression**:

    $$
    x_{\Delta t} = -2.9952 + 0.019980\,Z
    $$

    where $Z \sim \mathcal{N}(0,1)$. The conditional mean is approximately $-2.9952$ (very close to $x_0$ since $\Delta t$ is small), and the conditional standard deviation is approximately $0.0200$.

---

**Exercise 2.** Consider approximating $\int_0^T r_s\,ds$ with the trapezoidal rule using $N$ equal steps of size $\Delta t = T/N$. If $T = 5$ years and $r_t$ has an approximate second derivative $|r''(t)| \leq C = 0.002$, bound the absolute integration error using the classical trapezoidal error formula $|E| \leq \frac{C T (\Delta t)^2}{12}$ for $N = 50$ and $N = 250$. By what factor does the error decrease?

??? success "Solution to Exercise 2"
    The classical trapezoidal rule error bound for $\int_0^T f(s)\,ds$ with $N$ equal steps is

    $$
    |E| \leq \frac{C\,T\,(\Delta t)^2}{12}
    $$

    where $C = \max|f''(t)|$ and $\Delta t = T/N$.

    With $T = 5$, $C = 0.002$:

    **For $N = 50$**: $\Delta t = 5/50 = 0.10$

    $$
    |E_{50}| \leq \frac{0.002 \times 5 \times 0.01}{12} = \frac{0.0001}{12} = 8.33 \times 10^{-6}
    $$

    **For $N = 250$**: $\Delta t = 5/250 = 0.02$

    $$
    |E_{250}| \leq \frac{0.002 \times 5 \times 0.0004}{12} = \frac{0.000004}{12} = 3.33 \times 10^{-7}
    $$

    The **error reduction factor** is

    $$
    \frac{|E_{50}|}{|E_{250}|} = \frac{8.33 \times 10^{-6}}{3.33 \times 10^{-7}} = 25 = \left(\frac{250}{50}\right)^2 = 5^2
    $$

    The error decreases by a factor of 25 when the number of steps increases by a factor of 5, consistent with the $O(\Delta t^2)$ convergence rate of the trapezoidal rule. Both error bounds are very small (less than 1 basis point of bond price), confirming that the trapezoidal rule is adequate for typical BK simulations.

---

**Exercise 3.** You run $M = 10{,}000$ Monte Carlo paths and obtain $\hat{P}(0,5) = 0.7698$ with standard error $\text{SE} = 0.0009$. Construct the 95% confidence interval. How many paths $M'$ would be needed to reduce the standard error to $0.0001$? If each path takes $10^{-4}$ seconds, what is the total computation time for $M'$ paths?

??? success "Solution to Exercise 3"
    The 95% confidence interval is

    $$
    \hat{P} \pm 1.96 \times \text{SE} = 0.7698 \pm 1.96 \times 0.0009 = 0.7698 \pm 0.00176
    $$

    $$
    \text{95\% CI} = [0.7680,\; 0.7716]
    $$

    The tree price of 0.7700 falls within this interval, confirming consistency.

    To reduce the standard error to $\text{SE}' = 0.0001$, use the relationship $\text{SE} \propto 1/\sqrt{M}$:

    $$
    \frac{\text{SE}'}{\text{SE}} = \sqrt{\frac{M}{M'}} \implies M' = M \left(\frac{\text{SE}}{\text{SE}'}\right)^2
    $$

    $$
    M' = 10{,}000 \times \left(\frac{0.0009}{0.0001}\right)^2 = 10{,}000 \times 81 = 810{,}000
    $$

    The total computation time at $10^{-4}$ seconds per path:

    $$
    \text{Time} = 810{,}000 \times 10^{-4}\text{ s} = 81\text{ seconds}
    $$

    This is feasible for a single bond price but would be expensive if repeated for many instruments in a calibration loop. Variance reduction techniques (antithetic variates or control variates) could reduce the required number of paths by a factor of 3--5, bringing the time down to 15--25 seconds.

---

**Exercise 4.** Explain why the antithetic variate estimator is effective for the discount factor $Y = \exp(-\int_0^T r_s\,ds)$. Specifically, argue that $Y$ is a convex function of the Gaussian innovations, and use Jensen's inequality to show that $\text{Var}\!\left(\frac{Y + Y'}{2}\right) \leq \text{Var}(Y)$, where $Y'$ is the antithetic path.

??? success "Solution to Exercise 4"
    The discount factor is $Y = \exp(-\int_0^T r_s\,ds)$ and the antithetic counterpart (with innovations $-Z_k$) is $Y' = \exp(-\int_0^T r_s'\,ds)$.

    **Convexity argument**: The log rate $x_t$ is a linear (affine) function of the Gaussian innovations $Z_1, \ldots, Z_N$, so we can write $x_t = \alpha_t + \sum_k \beta_{tk} Z_k$ for deterministic coefficients. The short rate is $r_t = e^{x_t}$, which is a convex function of the $Z_k$ (since the exponential of an affine function is log-convex, hence convex). The integral $\int_0^T r_s\,ds$ is a sum of convex functions, hence convex in the $Z_k$. Finally, $Y = e^{-\int r_s\,ds}$ is the exponential of the negative of a convex function, which is a convex function composed with a decreasing convex function --- making $Y$ itself convex in the innovations.

    **Variance reduction via Jensen**: For the antithetic estimator $\bar{Y} = (Y + Y')/2$, note that $Y'$ corresponds to replacing $Z$ by $-Z$. By the convexity of $Y$ in $Z$:

    $$
    \frac{Y(Z) + Y(-Z)}{2} \geq Y(0) \quad \text{(Jensen's inequality)}
    $$

    but more importantly, the variance satisfies

    $$
    \text{Var}\!\left(\frac{Y + Y'}{2}\right) = \frac{1}{4}\left[\text{Var}(Y) + \text{Var}(Y') + 2\text{Cov}(Y, Y')\right]
    $$

    Since $Y$ and $Y'$ use the same innovations with opposite signs, they are negatively correlated when $Y$ is a monotone function of the innovations. For a convex function, $Y(Z)$ tends to be large when $Y(-Z)$ is small (and vice versa), so $\text{Cov}(Y, Y') < 0$. This gives

    $$
    \text{Var}\!\left(\frac{Y + Y'}{2}\right) = \frac{1}{2}\text{Var}(Y) + \frac{1}{2}\text{Cov}(Y, Y') < \frac{1}{2}\text{Var}(Y) \leq \text{Var}(Y)
    $$

    The negative covariance is the mechanism by which antithetic variates reduce variance. The stronger the convexity (i.e., the more nonlinear the payoff), the more negative the covariance and the greater the variance reduction.

---

**Exercise 5.** In the control variate approach, the closed-form expression $\mathbb{E}[r_t] = \exp(\mathbb{E}[x_t] + \frac{1}{2}\text{Var}(x_t))$ is used. For the parameters $a = 0.10$, $\sigma = 0.20$, $x_0 = \ln(0.05)$, and constant $\theta = -0.25$, compute $\mathbb{E}[r_1]$ and $\mathbb{E}[r_5]$. Discuss why the sample average rate $\bar{r}^{(m)}$ is a good control variate for bond pricing and what determines the optimal regression coefficient $\beta$.

??? success "Solution to Exercise 5"
    With $a = 0.10$, $\sigma = 0.20$, $x_0 = \ln(0.05) \approx -2.9957$, and $\theta = -0.25$:

    The conditional mean and variance of $x_t$ are

    $$
    \mathbb{E}[x_t] = x_0 e^{-at} + \frac{\theta}{a}(1 - e^{-at})
    $$

    $$
    \text{Var}(x_t) = \frac{\sigma^2}{2a}(1 - e^{-2at})
    $$

    **At $t = 1$**:

    $$
    \mathbb{E}[x_1] = (-2.9957)e^{-0.10} + (-2.5)(1 - e^{-0.10}) = (-2.9957)(0.9048) + (-2.5)(0.0952)
    $$

    $$
    = -2.7103 - 0.2381 = -2.9484
    $$

    $$
    \text{Var}(x_1) = \frac{0.04}{0.20}(1 - e^{-0.20}) = 0.20 \times 0.1813 = 0.03626
    $$

    $$
    \mathbb{E}[r_1] = \exp(-2.9484 + 0.01813) = \exp(-2.9303) = 0.05332
    $$

    So $\mathbb{E}[r_1] \approx 5.33\%$.

    **At $t = 5$**:

    $$
    \mathbb{E}[x_5] = (-2.9957)(0.6065) + (-2.5)(0.3935) = -1.8164 - 0.9838 = -2.8002
    $$

    $$
    \text{Var}(x_5) = 0.20(1 - e^{-1.0}) = 0.20 \times 0.6321 = 0.1264
    $$

    $$
    \mathbb{E}[r_5] = \exp(-2.8002 + 0.0632) = \exp(-2.7370) = 0.06484
    $$

    So $\mathbb{E}[r_5] \approx 6.48\%$.

    **Why $\bar{r}^{(m)}$ is a good control variate**: The sample average rate $\bar{r}^{(m)} = \frac{1}{N}\sum_k r_{t_k}^{(m)}$ is strongly correlated with the bond price $Y^{(m)} = \exp(-\Delta t \sum_k r_{t_k}^{(m)})$ because the bond price is a monotone decreasing function of the integrated rate. Paths with high average rates produce low bond prices and vice versa. The known mean $\mathbb{E}[\bar{r}]$ can be computed from the closed-form moments $\mathbb{E}[r_{t_k}]$ as $\mathbb{E}[\bar{r}] = \frac{1}{N}\sum_k \mathbb{E}[r_{t_k}]$.

    The optimal regression coefficient $\beta$ is

    $$
    \beta^* = \frac{\text{Cov}(Y, \bar{r})}{\text{Var}(\bar{r})}
    $$

    Since $Y$ is a decreasing function of $\bar{r}$, $\beta^* < 0$ (high $\bar{r}$ correlates with low $Y$). The magnitude of $|\beta^*|$ depends on how tightly $Y$ tracks $\bar{r}$ --- for bond pricing, the correlation is typically very high ($|\rho| > 0.9$), yielding variance reductions of 60--80%.

---

**Exercise 6.** A range accrual note pays an annual coupon of 5% multiplied by the fraction of quarterly observation dates where $r_t \in [2\%, 6\%]$, on a notional of \$1,000,000, maturing in 3 years. Describe the Monte Carlo algorithm to price this note under BK, including: (i) the number of observation dates, (ii) the discount factor computation, and (iii) how the payoff indicator function is evaluated along each path.

??? success "Solution to Exercise 6"
    The range accrual note specifications: 5% annual coupon, quarterly observations, notional $N = \$1{,}000{,}000$, maturity $T = 3$ years, range $[L, U] = [2\%, 6\%]$.

    **(i) Number of observation dates**: With quarterly observations over 3 years, there are $n = 3 \times 4 = 12$ observation dates at $T_i = 0.25, 0.50, 0.75, \ldots, 3.00$ years.

    **(ii) Monte Carlo algorithm**:

    For each of $M$ simulated paths $m = 1, \ldots, M$:

    1. **Simulate the log-rate path**: Using the exact OU simulation, generate $x_{t_1}^{(m)}, x_{t_2}^{(m)}, \ldots, x_{t_n}^{(m)}$ at each observation date (and possibly at finer intermediate steps for discount factor accuracy). Compute $r_{t_k}^{(m)} = e^{x_{t_k}^{(m)}}$.

    2. **Compute the discount factor**: Using the trapezoidal rule on a fine time grid (e.g., $\Delta t = 0.01$ year),

        $$
        D^{(m)} = \exp\!\left(-\sum_{k=0}^{N_t - 1} \frac{r_{t_k}^{(m)} + r_{t_{k+1}}^{(m)}}{2}\Delta t\right)
        $$

    3. **Evaluate the range accrual payoff**: For each annual coupon period $y = 1, 2, 3$, the coupon paid at year $y$ is

        $$
        C_y^{(m)} = N \times 0.05 \times \frac{1}{4}\sum_{i \in \text{year } y} \mathbf{1}_{\{L \leq r_{T_i}^{(m)} \leq U\}}
        $$

        where the sum is over the 4 quarterly observation dates in year $y$. The indicator function is evaluated by checking $0.02 \leq e^{x_{T_i}^{(m)}} \leq 0.06$, equivalently $\ln(0.02) \leq x_{T_i}^{(m)} \leq \ln(0.06)$.

    4. **Discount each coupon**: Discount each annual coupon to time 0 using the path-dependent discount factor accumulated to the coupon payment date. Also discount the notional repayment at maturity.

    **(iii) The indicator function**: At each observation date $T_i$, the indicator $\mathbf{1}_{\{L \leq r_{T_i} \leq U\}}$ equals 1 if the simulated short rate falls within $[2\%, 6\%]$ and 0 otherwise. This creates a discontinuous payoff, which can increase MC variance. Possible variance reduction: use a smoothed indicator (sigmoid approximation) for regression in continuation value estimation if early exercise is present, but for this European-style note, the standard indicator suffices.

    The final price estimate is $\hat{V} = \frac{1}{M}\sum_{m=1}^{M} \left[\sum_{y=1}^{3} D_y^{(m)} C_y^{(m)} + D_T^{(m)} N\right]$.

---

**Exercise 7.** The convergence table shows that $\hat{P}(0,5)$ with $M = 100{,}000$ and $N_t = 50$ is 0.7695 versus the tree price of 0.7700, while the same $M$ with $N_t = 250$ gives 0.7701. Decompose the total error into statistical error and integration (bias) error for each case. Which source of error dominates when $N_t = 50$? Propose a strategy using Richardson extrapolation to reduce the integration bias without increasing $N_t$.

??? success "Solution to Exercise 7"
    **Error decomposition**:

    The total error in the MC estimator has two components: statistical error (random, zero-mean) and integration bias (systematic). The tree price $P_{\text{tree}} = 0.7700$ serves as the reference.

    **Case 1**: $M = 100{,}000$, $N_t = 250$: $\hat{P} = 0.7701$, SE $= 0.0003$.

    - Total error: $\hat{P} - P_{\text{tree}} = 0.7701 - 0.7700 = +0.0001$
    - Statistical error: $\text{SE} = 0.0003$ (95% CI width $\approx \pm 0.0006$)
    - Integration bias: $\text{bias} \approx \hat{P} - P_{\text{true}} \approx 0.0001$ (within statistical noise)
    - The total error is within one standard error, so the integration bias with $N_t = 250$ is negligible compared to the statistical error. **Statistical error dominates**.

    **Case 2**: $M = 100{,}000$, $N_t = 50$: $\hat{P} = 0.7695$, SE $= 0.0003$.

    - Total error: $\hat{P} - P_{\text{tree}} = 0.7695 - 0.7700 = -0.0005$
    - Statistical error: $\text{SE} = 0.0003$
    - Integration bias: $\text{bias} \approx -0.0005$ (the estimate is 1.67 standard errors below the reference)
    - The bias ($-0.0005$) exceeds the standard error ($0.0003$), so **integration bias dominates** when $N_t = 50$.

    The bias is negative because the trapezoidal rule applied to the convex function $e^x$ slightly overestimates $\int r_s\,ds$, leading to an underestimate of $e^{-\int r_s\,ds}$.

    **Richardson extrapolation strategy**: The trapezoidal integration bias is $O(\Delta t^2)$. If we run the MC simulation at two step sizes $\Delta t_1$ and $\Delta t_2 = \Delta t_1/2$ (i.e., $N_1 = 50$ and $N_2 = 100$) using the **same random numbers** (common random numbers), the bias terms satisfy $\text{bias}_1 \approx 4 \cdot \text{bias}_2$. The Richardson extrapolation combines the two estimates:

    $$
    \hat{P}_{\text{Rich}} = \frac{4\hat{P}_2 - \hat{P}_1}{3}
    $$

    This eliminates the leading-order $O(\Delta t^2)$ bias, leaving only $O(\Delta t^4)$ residual bias. By using common random numbers for both runs, the statistical errors are highly correlated, and the extrapolated estimate has nearly the same statistical precision as the individual runs. This achieves the accuracy of a much finer grid (effectively $O(\Delta t^4)$) without actually increasing $N_t$ beyond 100, saving significant computation.
