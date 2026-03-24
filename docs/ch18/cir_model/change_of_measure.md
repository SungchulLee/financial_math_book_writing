# Change of Measure for the CIR Model

Pricing interest rate derivatives often requires computing expectations of the form $\mathbb{E}^{\mathbb{Q}}[D(t,T)\,h(r_T)]$, where $D(t,T) = \exp(-\int_t^T r_s\,ds)$ is the stochastic discount factor and $h$ is a payoff function. Direct evaluation of this expectation is difficult because both the discount factor and the payoff depend on the entire path of $r_s$. The **$T$-forward measure** $\mathbb{Q}^T$ eliminates this coupling by absorbing the discount factor into the change of measure, reducing the problem to a simple expectation of the payoff. This section defines the $T$-forward measure, derives the CIR dynamics under this new measure, and shows that the process remains in the CIR family with modified parameters --- a key property that enables closed-form bond option pricing.

---

## Motivation: simplifying derivative pricing

Under the risk-neutral measure $\mathbb{Q}$, the time-$t$ price of a European claim paying $h(r_T)$ at time $T$ is

$$
V(t) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,h(r_T)\,\bigg|\,\mathcal{F}_t\right]
$$

The stochastic discount factor and the payoff are correlated (both depend on the rate path), making this expectation analytically intractable in general. The $T$-forward measure removes the discount factor from inside the expectation by rewriting

$$
V(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[h(r_T)\,\big|\,\mathcal{F}_t\right]
$$

where $P(t,T)$ is the known zero-coupon bond price. The pricing problem thus reduces to computing an expectation of $h(r_T)$ alone, without the path-dependent discount factor.

---

## Definition of the T-forward measure

The $T$-forward measure $\mathbb{Q}^T$ is defined by its Radon-Nikodym derivative with respect to $\mathbb{Q}$ on $\mathcal{F}_T$:

$$
\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{e^{-\int_0^T r_s\,ds}}{P(0,T)}
$$

The numeraire associated with $\mathbb{Q}^T$ is the zero-coupon bond $P(t,T)$. Under $\mathbb{Q}^T$, any asset price divided by $P(t,T)$ is a martingale. The Radon-Nikodym density process (restricted to $\mathcal{F}_t$) is

$$
L_t = \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{e^{-\int_0^t r_s\,ds}\,P(t,T)}{P(0,T)}
$$

---

## Girsanov kernel for the CIR model

To apply Girsanov's theorem, we need the volatility of $L_t$. Since $P(t,T) = A(\tau)e^{-B(\tau)r_t}$ with $\tau = T - t$, applying Ito's lemma to $\ln P(t,T)$ and extracting the diffusion coefficient:

$$
d\ln P(t,T) = (\cdots)\,dt - B(\tau)\,\sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}
$$

The martingale $L_t$ satisfies

$$
\frac{dL_t}{L_t} = -B(\tau)\,\sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}
$$

By Girsanov's theorem, the process

$$
dW_t^T = dW_t^{\mathbb{Q}} + B(\tau)\,\sigma\sqrt{r_t}\,dt
$$

is a standard Brownian motion under $\mathbb{Q}^T$.

---

## CIR dynamics under the T-forward measure

The CIR SDE under $\mathbb{Q}$ is

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}
$$

Substituting $dW_t^{\mathbb{Q}} = dW_t^T - B(\tau)\sigma\sqrt{r_t}\,dt$:

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\left(dW_t^T - B(\tau)\sigma\sqrt{r_t}\,dt\right)
$$

$$
= \left[\kappa(\theta - r_t) - \sigma^2 B(\tau)\,r_t\right]dt + \sigma\sqrt{r_t}\,dW_t^T
$$

$$
= \left[\kappa\theta - (\kappa + \sigma^2 B(\tau))\,r_t\right]dt + \sigma\sqrt{r_t}\,dW_t^T
$$

Defining the time-dependent adjusted parameters:

$$
\kappa^T(\tau) = \kappa + \sigma^2 B(\tau), \qquad \theta^T(\tau) = \frac{\kappa\theta}{\kappa + \sigma^2 B(\tau)}
$$

the dynamics become

$$
dr_t = \kappa^T(\tau)\!\left(\theta^T(\tau) - r_t\right)dt + \sigma\sqrt{r_t}\,dW_t^T
$$

!!! tip "CIR stays CIR"
    The crucial observation is that the short rate under $\mathbb{Q}^T$ still follows a CIR-type process --- the diffusion coefficient $\sigma\sqrt{r_t}$ is unchanged, and only the drift parameters are modified. However, these modified parameters are now **time-dependent** through $B(\tau) = B(T-t)$, so the process is a time-inhomogeneous CIR process. This preservation of the square-root structure is essential for obtaining closed-form bond option formulas.

---

## Properties of the adjusted parameters

The adjusted mean-reversion speed $\kappa^T(\tau) = \kappa + \sigma^2 B(\tau)$ satisfies:

- $\kappa^T(0) = \kappa$ (at maturity, no adjustment)
- $\kappa^T(\tau) > \kappa$ for all $\tau > 0$ (the forward measure increases mean reversion)
- $\kappa^T(\tau) \to \kappa + \sigma^2 B_\infty$ as $\tau \to \infty$

The adjusted long-run mean $\theta^T(\tau) = \kappa\theta/\kappa^T(\tau)$ satisfies:

- $\theta^T(0) = \theta$ (no adjustment at maturity)
- $\theta^T(\tau) < \theta$ for all $\tau > 0$ (the forward measure lowers the long-run mean)

The economic interpretation is that the $T$-forward measure tilts the rate distribution downward: since bond prices decrease in rates, conditioning on the bond numeraire (which favors states with low rates) pulls the expected rate path lower.

### Feller condition under the forward measure

The Feller condition under $\mathbb{Q}^T$ requires $2\kappa^T(\tau)\theta^T(\tau) \geq \sigma^2$, which simplifies to $2\kappa\theta \geq \sigma^2$ --- the same condition as under $\mathbb{Q}$. The change of measure preserves the Feller condition.

---

## Application to derivative pricing

The forward-measure pricing formula

$$
V(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[h(r_T)\,\big|\,\mathcal{F}_t\right]
$$

reduces derivative pricing to computing expectations under the $\mathbb{Q}^T$ dynamics. For European-style payoffs $h(r_T)$:

1. **Bond options**: $h(r_T) = (P(T,S) - K)^+$ for a call on a zero-coupon bond maturing at $S > T$. Since $P(T,S)$ is a known function of $r_T$, this reduces to computing the distribution of $r_T$ under $\mathbb{Q}^T$.

2. **Caplets**: A caplet with strike $K$ on the rate over $[T, T+\delta]$ has payoff $\delta(L(T,T+\delta) - K)^+$, which is equivalent to a put on a zero-coupon bond.

3. **General European claims**: Any payoff that depends on $r_T$ alone (not the entire path) can be priced using the $\mathbb{Q}^T$ transition density.

---

## Transition density under the forward measure

Under $\mathbb{Q}^T$, the short rate $r_T$ given $r_t$ follows a **non-central chi-squared** distribution with time-dependent parameters. The conditional distribution has the form

$$
r_T \mid r_t \sim \frac{1}{2c^T}\,\chi^2\!\left(d^T,\,\lambda^T\right)
$$

where the scaling, degrees of freedom, and non-centrality parameters are

$$
c^T = c^T(t,T), \qquad d^T = \frac{4\kappa\theta}{\sigma^2}, \qquad \lambda^T = \lambda^T(t,T,r_t)
$$

The degrees-of-freedom parameter $d^T = 4\kappa\theta/\sigma^2$ is the same as under $\mathbb{Q}$ (because the Feller condition is preserved), but the scaling and non-centrality parameters differ due to the time-dependent drift. The explicit computation of these parameters involves integrating the time-dependent coefficients $\kappa^T(\tau)$ and $\theta^T(\tau)$, which can be carried out in terms of the CIR bond price functions $A$ and $B$.

---

## Physical to risk-neutral to forward measure

The full chain of measure changes in the CIR framework is:

| Measure | Drift of $r_t$ | Volatility | Numeraire |
|---------|----------------|------------|-----------|
| $\mathbb{P}$ (physical) | $\kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)$ | $\sigma\sqrt{r_t}$ | None |
| $\mathbb{Q}$ (risk-neutral) | $\kappa(\theta - r_t)$ | $\sigma\sqrt{r_t}$ | Money market account |
| $\mathbb{Q}^T$ ($T$-forward) | $\kappa^T(\tau)(\theta^T(\tau) - r_t)$ | $\sigma\sqrt{r_t}$ | $P(t,T)$ |

In each case, the square-root diffusion structure is preserved. The physical-to-risk-neutral change adjusts $\kappa^{\mathbb{P}}$ and $\theta^{\mathbb{P}}$ (via the market price of risk), and the risk-neutral-to-forward change further adjusts these parameters through $B(\tau)$.

!!! note "Market price of risk in CIR"
    The standard choice for the CIR market price of risk is $\lambda(r_t) = \lambda_0 \sqrt{r_t}$, which ensures the process remains CIR under $\mathbb{Q}$. Under this specification, $\kappa = \kappa^{\mathbb{P}} + \lambda_0$ and $\theta = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa$. The state-dependent form $\lambda_0\sqrt{r_t}$ is required (rather than a constant) to preserve the CIR structure.

---

## Summary

The $T$-forward measure $\mathbb{Q}^T$ simplifies CIR derivative pricing by removing the stochastic discount factor from the pricing expectation. Under this measure, the CIR process retains its square-root diffusion structure with time-dependent drift parameters $\kappa^T(\tau) = \kappa + \sigma^2 B(\tau)$ and $\theta^T(\tau) = \kappa\theta/\kappa^T(\tau)$. The forward measure increases the speed of mean reversion and lowers the long-run mean, reflecting the bias toward low-rate states introduced by the bond numeraire. The Feller condition is preserved, and the transition density remains non-central chi-squared with modified parameters. This framework provides the foundation for the closed-form CIR bond option formulas developed in the next section.

---

## Exercises

**Exercise 1.** Starting from the CIR bond price $P(t,T) = A(\tau)e^{-B(\tau)r_t}$ with $\tau = T - t$, apply Ito's lemma to $\ln P(t,T)$ and identify the drift and diffusion terms. Confirm that the diffusion coefficient of $\ln P$ is $-B(\tau)\sigma\sqrt{r_t}$, which gives rise to the Girsanov kernel.

---

**Exercise 2.** Derive the CIR dynamics under $\mathbb{Q}^T$ step by step. Substitute $dW_t^{\mathbb{Q}} = dW_t^T - B(\tau)\sigma\sqrt{r_t}\,dt$ into the risk-neutral CIR SDE and collect terms to obtain $dr_t = [\kappa\theta - (\kappa + \sigma^2 B(\tau))r_t]\,dt + \sigma\sqrt{r_t}\,dW_t^T$. Verify that $\kappa^T(\tau) = \kappa + \sigma^2 B(\tau)$ and $\theta^T(\tau) = \kappa\theta/\kappa^T(\tau)$.

---

**Exercise 3.** For CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, compute $B(\tau)$ for $\tau = 5$ years using the CIR formula. Then compute $\kappa^T(5) = \kappa + \sigma^2 B(5)$ and $\theta^T(5) = \kappa\theta/\kappa^T(5)$. Compare these with the risk-neutral values $\kappa$ and $\theta$. Interpret the economic meaning of the changes.

---

**Exercise 4.** Show that the Feller condition is preserved under the $T$-forward measure. Specifically, verify that $2\kappa^T(\tau)\theta^T(\tau) = 2\kappa\theta$ for all $\tau$, so the condition $2\kappa\theta \geq \sigma^2$ is equivalent under both measures.

---

**Exercise 5.** The forward measure tilts the rate distribution downward. Explain this economically: the numeraire is the zero-coupon bond $P(t,T)$, which is high when rates are low. How does conditioning on a high numeraire value bias the distribution of $r_T$? Relate this to the decrease in $\theta^T(\tau)$ compared to $\theta$.

---

**Exercise 6.** In the chain $\mathbb{P} \to \mathbb{Q} \to \mathbb{Q}^T$, the diffusion $\sigma\sqrt{r_t}$ is unchanged at each step. Explain why the diffusion coefficient is invariant under measure changes in general (Girsanov's theorem only modifies the drift). If the market price of risk is $\lambda(r_t) = \lambda_0\sqrt{r_t}$, compute the physical-measure drift parameters $\kappa^{\mathbb{P}}$ and $\theta^{\mathbb{P}}$ in terms of $\kappa$, $\theta$, and $\lambda_0$.

---

**Exercise 7.** A European digital bond option pays \$1 if $P(T, S) > K$ and \$0 otherwise, with expiry $T$ and underlying bond maturity $S$. Using the $T$-forward measure, write the price of this digital option as $P(t,T) \cdot \mathbb{Q}^T(r_T < r^*)$. Express this probability in terms of the non-central chi-squared CDF with the appropriate parameters under $\mathbb{Q}^T$.
