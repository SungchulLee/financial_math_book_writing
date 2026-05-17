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

The $T$-forward measure $\mathbb{Q}^T$ is defined by its Radon–Nikodym derivative with respect to $\mathbb{Q}$ on $\mathcal{F}_T$:

$$
\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{e^{-\int_0^T r_s\,ds}}{P(0,T)}
$$

The numeraire associated with $\mathbb{Q}^T$ is the zero-coupon bond $P(t,T)$. Under $\mathbb{Q}^T$, any asset price divided by $P(t,T)$ is a martingale. The Radon–Nikodym density process (restricted to $\mathcal{F}_t$) is

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

Recall (see [§ CIR SDE and Square-Root Process](cir_sde_and_square_root_process.md)) the CIR SDE under $\mathbb{Q}$. Substituting $dW_t^{\mathbb{Q}} = dW_t^T - B(\tau)\sigma\sqrt{r_t}\,dt$:

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

??? success "Solution to Exercise 1"

    The CIR bond price is $P(t,T) = A(\tau)e^{-B(\tau)r_t}$ with $\tau = T - t$. Define $F(t,r) = \ln P(t,T) = \ln A(\tau) - B(\tau)r$.

    Since $\tau = T - t$, we have $d\tau = -dt$, so:

    $$
    \frac{\partial F}{\partial t} = -\frac{A'(\tau)}{A(\tau)} + B'(\tau)\,r
    $$

    $$
    \frac{\partial F}{\partial r} = -B(\tau)
    $$

    $$
    \frac{\partial^2 F}{\partial r^2} = 0
    $$

    Applying Ito's lemma to $F = \ln P(t,T)$:

    $$
    d\ln P = \frac{\partial F}{\partial t}\,dt + \frac{\partial F}{\partial r}\,dr + \frac{1}{2}\frac{\partial^2 F}{\partial r^2}(dr)^2
    $$

    The last term vanishes since $\partial^2 F/\partial r^2 = 0$. Substituting $dr = \kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW^{\mathbb{Q}}$:

    $$
    d\ln P = \left[-\frac{A'(\tau)}{A(\tau)} + B'(\tau)r\right]dt + (-B(\tau))\left[\kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW^{\mathbb{Q}}\right]
    $$

    The diffusion (stochastic) part is:

    $$
    -B(\tau)\,\sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}
    $$

    This confirms that the diffusion coefficient of $\ln P$ is $-B(\tau)\sigma\sqrt{r_t}$, which is the Girsanov kernel that drives the measure change from $\mathbb{Q}$ to $\mathbb{Q}^T$.

---

**Exercise 2.** Derive the CIR dynamics under $\mathbb{Q}^T$ step by step. Substitute $dW_t^{\mathbb{Q}} = dW_t^T - B(\tau)\sigma\sqrt{r_t}\,dt$ into the risk-neutral CIR SDE and collect terms to obtain $dr_t = [\kappa\theta - (\kappa + \sigma^2 B(\tau))r_t]\,dt + \sigma\sqrt{r_t}\,dW_t^T$. Verify that $\kappa^T(\tau) = \kappa + \sigma^2 B(\tau)$ and $\theta^T(\tau) = \kappa\theta/\kappa^T(\tau)$.

??? success "Solution to Exercise 2"

    The risk-neutral CIR SDE is:

    $$
    dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}
    $$

    By Girsanov's theorem, $dW_t^{\mathbb{Q}} = dW_t^T - B(\tau)\sigma\sqrt{r_t}\,dt$. Substituting:

    $$
    dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\left(dW_t^T - B(\tau)\sigma\sqrt{r_t}\,dt\right)
    $$

    Expanding:

    $$
    dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^T - \sigma^2 B(\tau)\,r_t\,dt
    $$

    Collecting drift terms:

    $$
    dr_t = \left[\kappa\theta - \kappa r_t - \sigma^2 B(\tau)r_t\right]dt + \sigma\sqrt{r_t}\,dW_t^T
    $$

    $$
    = \left[\kappa\theta - \left(\kappa + \sigma^2 B(\tau)\right)r_t\right]dt + \sigma\sqrt{r_t}\,dW_t^T
    $$

    Define $\kappa^T(\tau) = \kappa + \sigma^2 B(\tau)$. Then the drift becomes:

    $$
    \kappa\theta - \kappa^T(\tau)\,r_t = \kappa^T(\tau)\left(\frac{\kappa\theta}{\kappa^T(\tau)} - r_t\right)
    $$

    Defining $\theta^T(\tau) = \kappa\theta/\kappa^T(\tau)$:

    $$
    dr_t = \kappa^T(\tau)\left(\theta^T(\tau) - r_t\right)dt + \sigma\sqrt{r_t}\,dW_t^T
    $$

    This confirms both adjusted parameters: $\kappa^T(\tau) = \kappa + \sigma^2 B(\tau)$ and $\theta^T(\tau) = \kappa\theta/\kappa^T(\tau)$.

---

**Exercise 3.** For CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, compute $B(\tau)$ for $\tau = 5$ years using the CIR formula. Then compute $\kappa^T(5) = \kappa + \sigma^2 B(5)$ and $\theta^T(5) = \kappa\theta/\kappa^T(5)$. Compare these with the risk-neutral values $\kappa$ and $\theta$. Interpret the economic meaning of the changes.

??? success "Solution to Exercise 3"

    Given $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$.

    **Step 1: Compute $\gamma$ and $B(5)$.**

    $$
    \gamma = \sqrt{0.25 + 0.02} = \sqrt{0.27} \approx 0.5196
    $$

    $$
    e^{\gamma \cdot 5} = e^{2.598} \approx 13.44
    $$

    $$
    B(5) = \frac{2(13.44 - 1)}{(0.5196 + 0.5)(13.44 - 1) + 2(0.5196)} = \frac{24.88}{1.0196 \times 12.44 + 1.039} = \frac{24.88}{12.68 + 1.04} = \frac{24.88}{13.72} \approx 1.813
    $$

    **Step 2: Compute $\kappa^T(5)$.**

    $$
    \kappa^T(5) = \kappa + \sigma^2 B(5) = 0.5 + 0.01 \times 1.813 = 0.5 + 0.01813 = 0.51813
    $$

    **Step 3: Compute $\theta^T(5)$.**

    $$
    \theta^T(5) = \frac{\kappa\theta}{\kappa^T(5)} = \frac{0.5 \times 0.06}{0.51813} = \frac{0.03}{0.51813} \approx 0.05791
    $$

    **Comparison with risk-neutral values:**

    - $\kappa^T(5) = 0.518 > \kappa = 0.5$ (increased by $\sim 3.6\%$)
    - $\theta^T(5) = 0.0579 < \theta = 0.06$ (decreased by $\sim 3.5\%$)

    **Economic interpretation:** The forward measure increases the speed of mean reversion (the process reverts faster to its long-run mean) and lowers the long-run mean level. This reflects the bias introduced by the bond numeraire $P(t,T)$: since bond prices are high when rates are low, the forward measure overweights low-rate scenarios. This tilts the expected rate path downward (lower $\theta^T$) and pulls the process more strongly toward this lower target (higher $\kappa^T$).

---

**Exercise 4.** Show that the Feller condition is preserved under the $T$-forward measure. Specifically, verify that $2\kappa^T(\tau)\theta^T(\tau) = 2\kappa\theta$ for all $\tau$, so the condition $2\kappa\theta \geq \sigma^2$ is equivalent under both measures.

??? success "Solution to Exercise 4"

    We need to show $2\kappa^T(\tau)\theta^T(\tau) = 2\kappa\theta$.

    $$
    2\kappa^T(\tau)\theta^T(\tau) = 2\left(\kappa + \sigma^2 B(\tau)\right) \cdot \frac{\kappa\theta}{\kappa + \sigma^2 B(\tau)} = 2\kappa\theta
    $$

    The $\kappa + \sigma^2 B(\tau)$ factors cancel exactly, leaving $2\kappa\theta$ regardless of $\tau$.

    Therefore, the Feller condition under $\mathbb{Q}^T$ is $2\kappa^T(\tau)\theta^T(\tau) \geq \sigma^2$, which simplifies to $2\kappa\theta \geq \sigma^2$, exactly the same condition as under $\mathbb{Q}$.

    This is a remarkable and useful result: the change of measure modifies $\kappa$ and $\theta$ in a way that preserves their product $\kappa\theta$, and since the diffusion coefficient $\sigma$ is unchanged by the measure change, the Feller condition is invariant. The process under the forward measure has the same boundary behavior as under the risk-neutral measure.

---

**Exercise 5.** The forward measure tilts the rate distribution downward. Explain this economically: the numeraire is the zero-coupon bond $P(t,T)$, which is high when rates are low. How does conditioning on a high numeraire value bias the distribution of $r_T$? Relate this to the decrease in $\theta^T(\tau)$ compared to $\theta$.

??? success "Solution to Exercise 5"

    Under $\mathbb{Q}^T$, the numeraire is the zero-coupon bond $P(t,T)$. Since $P(t,T) = A(\tau)e^{-B(\tau)r_t}$ is a decreasing function of $r_t$ (because $B(\tau) > 0$), the bond price is high when rates are low.

    The forward measure $\mathbb{Q}^T$ is defined by $d\mathbb{Q}^T/d\mathbb{Q} \propto e^{-\int_0^T r_s\,ds} \cdot P(t,T)$, which upweights scenarios where the discount factor $e^{-\int r_s\,ds}$ is large (i.e., where rates are low) and where $P(t,T)$ is large (also when rates are low). This **double bias** toward low-rate states systematically tilts the distribution of $r_T$ downward.

    Quantitatively:

    - The adjusted long-run mean $\theta^T(\tau) = \kappa\theta/(\kappa + \sigma^2 B(\tau)) < \theta$ because $\sigma^2 B(\tau) > 0$. This means the forward-measure process mean-reverts to a lower level.
    - The stronger mean reversion ($\kappa^T > \kappa$) means the process is pulled more forcefully toward this lower target.

    Together, these effects shift the entire distribution of $r_T$ to the left (lower rates), consistent with conditioning on a numeraire that is more valuable in low-rate environments.

---

**Exercise 6.** In the chain $\mathbb{P} \to \mathbb{Q} \to \mathbb{Q}^T$, the diffusion $\sigma\sqrt{r_t}$ is unchanged at each step. Explain why the diffusion coefficient is invariant under measure changes in general (Girsanov's theorem only modifies the drift). If the market price of risk is $\lambda(r_t) = \lambda_0\sqrt{r_t}$, compute the physical-measure drift parameters $\kappa^{\mathbb{P}}$ and $\theta^{\mathbb{P}}$ in terms of $\kappa$, $\theta$, and $\lambda_0$.

??? success "Solution to Exercise 6"

    **Girsanov's theorem and diffusion invariance:** Girsanov's theorem states that changing from measure $\mathbb{P}$ to $\mathbb{Q}$ modifies the drift of a process by adding a term $\sigma(r_t) \cdot \lambda(t)$ (where $\lambda$ is the Girsanov kernel), but the diffusion coefficient $\sigma(r_t)$ remains unchanged. This is a fundamental property: the quadratic variation $\langle r \rangle_t = \int_0^t \sigma^2(r_s)\,ds$ is the same under all equivalent measures. The intuition is that the diffusion coefficient determines the "roughness" of sample paths, which is a pathwise property unaffected by reweighting probabilities.

    **Physical-measure parameters:** If the market price of risk is $\lambda(r_t) = \lambda_0\sqrt{r_t}$, the Girsanov kernel is $\lambda_0\sqrt{r_t}$ and:

    $$
    dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} + \lambda_0\sqrt{r_t}\,dt
    $$

    Under $\mathbb{P}$: $dr_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{P}}$.

    Substituting $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \lambda_0\sqrt{r_t}\,dt$:

    $$
    dr_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)\,dt + \sigma\sqrt{r_t}(dW_t^{\mathbb{Q}} - \lambda_0\sqrt{r_t}\,dt)
    $$

    $$
    = [\kappa^{\mathbb{P}}\theta^{\mathbb{P}} - (\kappa^{\mathbb{P}} + \sigma\lambda_0)r_t]\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}
    $$

    Matching with the $\mathbb{Q}$ dynamics $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}$:

    $$
    \kappa = \kappa^{\mathbb{P}} + \sigma\lambda_0, \qquad \kappa\theta = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}
    $$

    Solving:

    $$
    \kappa^{\mathbb{P}} = \kappa - \sigma\lambda_0, \qquad \theta^{\mathbb{P}} = \frac{\kappa\theta}{\kappa^{\mathbb{P}}} = \frac{\kappa\theta}{\kappa - \sigma\lambda_0}
    $$

---

**Exercise 7.** A European digital bond option pays \$1 if $P(T, S) > K$ and \$0 otherwise, with expiry $T$ and underlying bond maturity $S$. Using the $T$-forward measure, write the price of this digital option as $P(t,T) \cdot \mathbb{Q}^T(r_T < r^*)$. Express this probability in terms of the non-central chi-squared CDF with the appropriate parameters under $\mathbb{Q}^T$.

??? success "Solution to Exercise 7"

    The digital bond option pays \$1 if $P(T,S) > K$ and \$0 otherwise. Under $\mathbb{Q}$:

    $$
    V(t) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}\,\mathbf{1}_{\{P(T,S) > K\}}\,\bigg|\,\mathcal{F}_t\right]
    $$

    Switching to the $T$-forward measure:

    $$
    V(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[\mathbf{1}_{\{P(T,S) > K\}}\,\big|\,\mathcal{F}_t\right] = P(t,T)\,\mathbb{Q}^T(P(T,S) > K \mid \mathcal{F}_t)
    $$

    Since $P(T,S) = A(S-T)e^{-B(S-T)r_T}$ is decreasing in $r_T$, the condition $P(T,S) > K$ is equivalent to $r_T < r^*$ where $r^* = \frac{1}{B(S-T)}\ln\frac{A(S-T)}{K}$.

    Therefore:

    $$
    V(t) = P(t,T)\,\mathbb{Q}^T(r_T < r^* \mid \mathcal{F}_t)
    $$

    Under $\mathbb{Q}^T$, the scaled rate $2c^T r_T$ follows a non-central chi-squared distribution $\chi^2(d, \lambda^T)$ where $d = 4\kappa\theta/\sigma^2$ and $\lambda^T$ and $c^T$ are the forward-measure parameters. The probability is:

    $$
    \mathbb{Q}^T(r_T < r^*) = \mathbb{Q}^T(2c^T r_T < 2c^T r^*) = \chi^2(2c^T r^*;\, d,\, \lambda^T)
    $$

    where $\chi^2(x; d, \lambda)$ denotes the non-central chi-squared CDF. Here $c^T = c^T(t,T)$ and $\lambda^T = 2c^T r_t e^{-\int_t^T \kappa^T(s)\,ds}$ involve the integrated forward-measure drift coefficients.

    In terms of the bond option parameters $\phi$ and $\psi$:

    $$
    V(t) = P(t,T)\,\chi^2\!\left(2r^*(\phi + \psi);\, d,\, \lambda_2\right)
    $$

    where $\lambda_2 = 2\phi^2 r_t e^{\gamma(T-t)}/(\phi + \psi)$ and $\phi$, $\psi$ are as defined in the bond option formula. This is precisely the second term of the CIR call option formula (without the $P(t,S)$ first term and without the strike).
