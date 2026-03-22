# Change of Measure: Q to T-Forward

Pricing interest rate derivatives under the risk-neutral measure $\mathbb{Q}$ requires computing expectations of the form $\mathbb{E}^{\mathbb{Q}}_t[e^{-\int_t^T r_s\,ds}\,g(r_T)]$, where the discount factor and the payoff are entangled through their joint dependence on the short rate path. The **$T$-forward measure** $\mathbb{Q}^T$ eliminates this complication by absorbing the discount factor into the change of measure, so that derivative prices become simple expectations of the payoff. For the Vasicek model, the short rate remains an OU process under $\mathbb{Q}^T$---only the drift changes---making the forward measure particularly powerful for deriving closed-form option pricing formulas.

---

## Motivation: why change the numeraire

Under the risk-neutral measure $\mathbb{Q}$ with the money market account $B_t = e^{\int_0^t r_s\,ds}$ as numeraire, the price of a derivative with payoff $g(r_T)$ at time $T$ is

$$
V(t) = \mathbb{E}^{\mathbb{Q}}_t\!\left[e^{-\int_t^T r_s\,ds}\,g(r_T)\right]
$$

The difficulty is that the discount factor $e^{-\int_t^T r_s\,ds}$ is stochastic and correlated with $g(r_T)$, so $\mathbb{E}^{\mathbb{Q}}[e^{-\int r_s\,ds}\,g(r_T)] \neq \mathbb{E}^{\mathbb{Q}}[e^{-\int r_s\,ds}]\,\mathbb{E}^{\mathbb{Q}}[g(r_T)]$.

The $T$-forward measure uses the zero-coupon bond $P(t,T)$ as numeraire instead. By the general change-of-numeraire theorem, for any two numeraires $N^{(1)}_t$ and $N^{(2)}_t$, the price ratios $V_t/N^{(i)}_t$ are martingales under the corresponding measures. Switching from $B_t$ to $P(t,T)$ yields

$$
V(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}_t\!\left[g(r_T)\right]
$$

The discount factor has been replaced by the known quantity $P(t,T)$, and the expectation is now over $g(r_T)$ alone.

---

## Definition of the T-forward measure

The $T$-forward measure $\mathbb{Q}^T$ is defined by the Radon-Nikodym derivative

$$
\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{P(t,T)}{P(0,T)\,B_t} = \frac{P(t,T)\,B_0}{P(0,T)\,B_t}
$$

Since $P(t,T)/B_t$ is a $\mathbb{Q}$-martingale (discounted bond price), this Radon-Nikodym process is a well-defined positive martingale.

For the Vasicek model, the bond price $P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}$ and the dynamics of $P$ under $\mathbb{Q}$ involve the diffusion coefficient

$$
\sigma_P(t,T) = -B(\tau)\,\sigma
$$

where $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$ and $\tau = T - t$.

---

## Girsanov theorem for the OU process

### The Girsanov kernel

By the Girsanov theorem, the change from $\mathbb{Q}$ to $\mathbb{Q}^T$ modifies the Brownian motion via

$$
dW_t^{\mathbb{Q}^T} = dW_t^{\mathbb{Q}} - \sigma_P(t,T)\,dt = dW_t^{\mathbb{Q}} + B(T-t)\,\sigma\,dt
$$

The drift adjustment (Girsanov kernel) is $\gamma(t) = -\sigma_P(t,T) = B(T-t)\,\sigma$, which is deterministic and depends on time only through the remaining time to the numeraire bond's maturity.

### Proof that the kernel is deterministic

In the Vasicek model, the bond price volatility $\sigma_P(t,T) = -B(T-t)\,\sigma$ is a deterministic function of $t$ and $T$. This is a direct consequence of the affine structure: the diffusion of $\ln P$ is $-B(\tau)\,\sigma$, independent of the state $r_t$. Therefore the Girsanov kernel is non-random, which preserves the Gaussian nature of the short rate under the new measure. $\square$

---

## Short rate dynamics under the T-forward measure

Under $\mathbb{Q}$, the Vasicek short rate satisfies

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}
$$

Substituting $dW_t^{\mathbb{Q}} = dW_t^{\mathbb{Q}^T} - B(T-t)\,\sigma\,dt$:

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\!\left(dW_t^{\mathbb{Q}^T} - B(T-t)\,\sigma\,dt\right)
$$

$$
dr_t = \left[\kappa(\theta - r_t) - \sigma^2 B(T-t)\right]dt + \sigma\,dW_t^{\mathbb{Q}^T}
$$

Expanding $B(T-t) = (1 - e^{-\kappa(T-t)})/\kappa$:

$$
dr_t = \kappa\!\left(\theta - \frac{\sigma^2}{\kappa^2}\!\left(1 - e^{-\kappa(T-t)}\right) - r_t\right)dt + \sigma\,dW_t^{\mathbb{Q}^T}
$$

This can be written as

$$
dr_t = \kappa\!\left(\theta^T(t) - r_t\right)dt + \sigma\,dW_t^{\mathbb{Q}^T}
$$

where the **time-dependent mean-reversion level** under $\mathbb{Q}^T$ is

$$
\theta^T(t) = \theta - \frac{\sigma^2}{\kappa^2}\!\left(1 - e^{-\kappa(T-t)}\right) = \theta - \frac{\sigma^2}{\kappa}\,B(T-t)
$$

**Key observations:**

- The mean-reversion speed $\kappa$ is unchanged.
- The volatility $\sigma$ is unchanged.
- Only the mean-reversion level shifts from $\theta$ to a time-dependent $\theta^T(t) < \theta$.
- At $t = T$: $\theta^T(T) = \theta$ (the modification vanishes at the numeraire maturity).
- The short rate remains an OU process, hence Gaussian, under $\mathbb{Q}^T$.

---

## Distribution of the short rate under the T-forward measure

Since the short rate is an OU process under $\mathbb{Q}^T$ with time-varying drift, the conditional distribution of $r_T$ given $r_t$ is Gaussian:

$$
r_T \mid r_t \sim \mathcal{N}\!\left(m^T(t,T),\; v^2(t,T)\right) \quad \text{under } \mathbb{Q}^T
$$

**Conditional mean under $\mathbb{Q}^T$:**

The mean is obtained by solving the OU equation with time-varying target $\theta^T(s)$:

$$
m^T(t,T) = \mathbb{E}^{\mathbb{Q}^T}_t[r_T] = e^{-\kappa\tau}\,r_t + \kappa\int_t^T e^{-\kappa(T-s)}\theta^T(s)\,ds
$$

After evaluating the integral (using $\theta^T(s) = \theta - \frac{\sigma^2}{\kappa}B(T-s)$):

$$
m^T(t,T) = e^{-\kappa\tau}\,r_t + \theta(1 - e^{-\kappa\tau}) - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2
$$

Comparing with the $\mathbb{Q}$-mean $m^{\mathbb{Q}}(t,T) = e^{-\kappa\tau}r_t + \theta(1 - e^{-\kappa\tau})$:

$$
m^T(t,T) = m^{\mathbb{Q}}(t,T) - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2
$$

The forward-measure mean is shifted **downward** by a convexity-type correction.

**Conditional variance:**

The variance is unaffected by the change of measure (Girsanov changes drift, not diffusion):

$$
v^2(t,T) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})
$$

This is the same under $\mathbb{Q}$ and $\mathbb{Q}^T$.

---

## Forward bond price ratio

Under $\mathbb{Q}^T$, the **forward bond price** $P(T, S)/P(t, S) \cdot P(t,T)$ for $S > T$ is a martingale. In the Vasicek model, the ratio $P(T,S)/P(T,T) = P(T,S)$ evaluated at time $T$ depends on $r_T$, which is Gaussian under $\mathbb{Q}^T$. Therefore $P(T,S) = A(S-T)e^{-B(S-T)r_T}$ is log-normally distributed under $\mathbb{Q}^T$.

This log-normality of the forward bond price is the foundation of closed-form bond option pricing in the Vasicek model, as developed in the next section on Jamshidian's decomposition.

---

## Pricing formula under the T-forward measure

For any $\mathcal{F}_T$-measurable payoff $g(r_T)$:

$$
V(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}_t[g(r_T)]
$$

Since $r_T$ is Gaussian under $\mathbb{Q}^T$ with known mean $m^T(t,T)$ and variance $v^2(t,T)$, this expectation can often be computed in closed form.

**Example: European call on a zero-coupon bond.** A call option with strike $K$ and expiry $T$ on a bond maturing at $S > T$ has payoff $g = (P(T,S) - K)^+$. Under $\mathbb{Q}^T$:

$$
V(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}_t\!\left[(P(T,S) - K)^+\right]
$$

Since $P(T,S) = A(S-T)\,e^{-B(S-T)\,r_T}$ and $r_T$ is Gaussian, $P(T,S)$ is log-normal under $\mathbb{Q}^T$, and the expectation evaluates to a Black-Scholes-type formula. The detailed derivation is presented in the section on bond options.

---

## Comparison of measures

The following table summarizes the short rate dynamics under the three commonly used measures.

| Property | Physical $\mathbb{P}$ | Risk-neutral $\mathbb{Q}$ | $T$-forward $\mathbb{Q}^T$ |
|---|---|---|---|
| SDE drift | $\kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)$ | $\kappa(\theta - r_t)$ | $\kappa(\theta^T(t) - r_t)$ |
| Mean-reversion speed | $\kappa^{\mathbb{P}}$ | $\kappa$ | $\kappa$ |
| Long-run level | $\theta^{\mathbb{P}}$ | $\theta$ | $\theta^T(t) = \theta - \frac{\sigma^2}{\kappa}B(T-t)$ |
| Volatility | $\sigma$ | $\sigma$ | $\sigma$ |
| Distribution | Gaussian | Gaussian | Gaussian |
| Numeraire | Not specified | $B_t = e^{\int_0^t r_s\,ds}$ | $P(t,T)$ |

The Gaussian nature of the short rate is preserved across all three measures because the Girsanov kernel is deterministic (a consequence of the affine structure with constant diffusion). This would not hold for the CIR model, where the state-dependent diffusion $\sigma\sqrt{r_t}$ produces a state-dependent Girsanov kernel.

---

## Summary

The $T$-forward measure $\mathbb{Q}^T$ simplifies derivative pricing by replacing the stochastic discount factor with the known bond price $P(t,T)$. In the Vasicek model, the change of measure preserves the OU structure---only the mean-reversion target shifts from $\theta$ to $\theta^T(t) = \theta - (\sigma^2/\kappa)\,B(T-t)$. The short rate remains Gaussian under $\mathbb{Q}^T$, making forward bond prices log-normal and enabling closed-form Black-Scholes-type formulas for bond options, caplets, and swaptions.

---
