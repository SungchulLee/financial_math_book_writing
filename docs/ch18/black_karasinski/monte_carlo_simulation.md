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

---

**Exercise 2.** Consider approximating $\int_0^T r_s\,ds$ with the trapezoidal rule using $N$ equal steps of size $\Delta t = T/N$. If $T = 5$ years and $r_t$ has an approximate second derivative $|r''(t)| \leq C = 0.002$, bound the absolute integration error using the classical trapezoidal error formula $|E| \leq \frac{C T (\Delta t)^2}{12}$ for $N = 50$ and $N = 250$. By what factor does the error decrease?

---

**Exercise 3.** You run $M = 10{,}000$ Monte Carlo paths and obtain $\hat{P}(0,5) = 0.7698$ with standard error $\text{SE} = 0.0009$. Construct the 95% confidence interval. How many paths $M'$ would be needed to reduce the standard error to $0.0001$? If each path takes $10^{-4}$ seconds, what is the total computation time for $M'$ paths?

---

**Exercise 4.** Explain why the antithetic variate estimator is effective for the discount factor $Y = \exp(-\int_0^T r_s\,ds)$. Specifically, argue that $Y$ is a convex function of the Gaussian innovations, and use Jensen's inequality to show that $\text{Var}\!\left(\frac{Y + Y'}{2}\right) \leq \text{Var}(Y)$, where $Y'$ is the antithetic path.

---

**Exercise 5.** In the control variate approach, the closed-form expression $\mathbb{E}[r_t] = \exp(\mathbb{E}[x_t] + \frac{1}{2}\text{Var}(x_t))$ is used. For the parameters $a = 0.10$, $\sigma = 0.20$, $x_0 = \ln(0.05)$, and constant $\theta = -0.25$, compute $\mathbb{E}[r_1]$ and $\mathbb{E}[r_5]$. Discuss why the sample average rate $\bar{r}^{(m)}$ is a good control variate for bond pricing and what determines the optimal regression coefficient $\beta$.

---

**Exercise 6.** A range accrual note pays an annual coupon of 5% multiplied by the fraction of quarterly observation dates where $r_t \in [2\%, 6\%]$, on a notional of \$1,000,000, maturing in 3 years. Describe the Monte Carlo algorithm to price this note under BK, including: (i) the number of observation dates, (ii) the discount factor computation, and (iii) how the payoff indicator function is evaluated along each path.

---

**Exercise 7.** The convergence table shows that $\hat{P}(0,5)$ with $M = 100{,}000$ and $N_t = 50$ is 0.7695 versus the tree price of 0.7700, while the same $M$ with $N_t = 250$ gives 0.7701. Decompose the total error into statistical error and integration (bias) error for each case. Which source of error dominates when $N_t = 50$? Propose a strategy using Richardson extrapolation to reduce the integration bias without increasing $N_t$.
