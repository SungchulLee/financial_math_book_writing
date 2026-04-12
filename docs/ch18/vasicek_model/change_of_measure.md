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

The $T$-forward measure $\mathbb{Q}^T$ is defined by the Radon–Nikodym derivative

$$
\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{P(t,T)}{P(0,T)\,B_t} = \frac{P(t,T)\,B_0}{P(0,T)\,B_t}
$$

Since $P(t,T)/B_t$ is a $\mathbb{Q}$-martingale (discounted bond price), this Radon–Nikodym process is a well-defined positive martingale.

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

## Exercises

**Exercise 1.** Derive the Girsanov kernel for the Vasicek model. Starting from $P(t,T) = A(T-t)e^{-B(T-t)r_t}$, apply Ito's lemma to find $dP/P$ and identify the volatility of the bond price process. Show that $dW_t^T = dW_t^{\mathbb{Q}} + B(T-t)\sigma\,dt$.

??? success "Solution to Exercise 1"
    The Vasicek bond price is $P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}$ where $\tau = T - t$. Since $\tau = T - t$, we have $\partial \tau / \partial t = -1$.

    Apply Ito's lemma to $P = A(\tau)\,e^{-B(\tau)\,r_t}$. First, compute the partial derivatives:

    $$
    \frac{\partial P}{\partial t} = \left(-\dot{A}(\tau)\,e^{-B(\tau)r_t} + A(\tau)\,\dot{B}(\tau)\,r_t\,e^{-B(\tau)r_t}\right)
    $$

    (using $\partial_t = -\partial_\tau$, but we can work directly with the product). More directly:

    $$
    \frac{\partial P}{\partial r} = -B(\tau)\,P(t,T), \qquad \frac{\partial^2 P}{\partial r^2} = B(\tau)^2\,P(t,T)
    $$

    By Ito's lemma:

    $$
    dP = \frac{\partial P}{\partial t}\,dt + \frac{\partial P}{\partial r}\,dr + \frac{1}{2}\frac{\partial^2 P}{\partial r^2}\,(dr)^2
    $$

    Substituting $dr = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$ and $(dr)^2 = \sigma^2\,dt$:

    $$
    dP = \left[\frac{\partial P}{\partial t} - B(\tau)\,P\,\kappa(\theta - r_t) + \frac{1}{2}B(\tau)^2\,P\,\sigma^2\right]dt + \left[-B(\tau)\,P\,\sigma\right]dW_t^{\mathbb{Q}}
    $$

    The volatility of the bond price process is:

    $$
    \sigma_P(t,T) = -B(T-t)\,\sigma
    $$

    This is negative because bond prices decrease when rates increase ($B > 0$).

    The Girsanov theorem for changing from $\mathbb{Q}$ (numeraire $B_t$) to $\mathbb{Q}^T$ (numeraire $P(t,T)$) gives the new Brownian motion:

    $$
    dW_t^T = dW_t^{\mathbb{Q}} - \sigma_P(t,T)\,dt = dW_t^{\mathbb{Q}} - (-B(T-t)\sigma)\,dt = dW_t^{\mathbb{Q}} + B(T-t)\,\sigma\,dt
    $$

    The Girsanov kernel is $\gamma(t) = -\sigma_P(t,T) = B(T-t)\,\sigma$, which is deterministic.

---

**Exercise 2.** Substitute $dW_t^{\mathbb{Q}} = dW_t^T - B(T-t)\sigma\,dt$ into the Vasicek SDE and derive the dynamics under $\mathbb{Q}^T$. Show that $\theta^T(t) = \theta - (\sigma^2/\kappa)B(T-t)$ and that $\kappa$ is unchanged.

??? success "Solution to Exercise 2"
    Under $\mathbb{Q}$, the Vasicek SDE is $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$.

    From Exercise 1, $dW_t^{\mathbb{Q}} = dW_t^T - B(T-t)\,\sigma\,dt$. Substituting:

    $$
    dr_t = \kappa(\theta - r_t)\,dt + \sigma\left(dW_t^T - B(T-t)\,\sigma\,dt\right)
    $$

    $$
    = \left[\kappa(\theta - r_t) - \sigma^2 B(T-t)\right]dt + \sigma\,dW_t^T
    $$

    Expanding $B(T-t) = (1 - e^{-\kappa(T-t)})/\kappa$:

    $$
    \sigma^2 B(T-t) = \frac{\sigma^2}{\kappa}(1 - e^{-\kappa(T-t)})
    $$

    The drift becomes:

    $$
    \kappa\theta - \kappa r_t - \frac{\sigma^2}{\kappa}(1 - e^{-\kappa(T-t)}) = \kappa\left[\theta - \frac{\sigma^2}{\kappa^2}(1 - e^{-\kappa(T-t)}) - r_t\right]
    $$

    Defining $\theta^T(t) = \theta - \frac{\sigma^2}{\kappa^2}(1 - e^{-\kappa(T-t)}) = \theta - \frac{\sigma^2}{\kappa}B(T-t)$, the SDE under $\mathbb{Q}^T$ is:

    $$
    dr_t = \kappa(\theta^T(t) - r_t)\,dt + \sigma\,dW_t^T
    $$

    The mean-reversion speed $\kappa$ is unchanged---only the target level shifts from $\theta$ to $\theta^T(t) < \theta$. The process remains an OU process with time-varying drift, preserving the Gaussian property.

---

**Exercise 3.** For $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $T = 5$, compute $\theta^T(t)$ at $t = 0, 2, 4$. Is $\theta^T(t)$ above or below $\theta$? Interpret the direction of the shift economically.

??? success "Solution to Exercise 3"
    Using $\theta^T(t) = \theta - \frac{\sigma^2}{\kappa}B(T-t)$ with $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $T = 5$:

    $$
    \frac{\sigma^2}{\kappa} = \frac{0.000225}{0.3} = 0.00075
    $$

    At $t = 0$ ($T - t = 5$):

    $$
    B(5) = \frac{1 - e^{-1.5}}{0.3} = \frac{1 - 0.2231}{0.3} = 2.590
    $$

    $$
    \theta^T(0) = 0.05 - 0.00075 \times 2.590 = 0.05 - 0.001942 = 0.04806
    $$

    At $t = 2$ ($T - t = 3$):

    $$
    B(3) = \frac{1 - e^{-0.9}}{0.3} = \frac{1 - 0.4066}{0.3} = 1.978
    $$

    $$
    \theta^T(2) = 0.05 - 0.00075 \times 1.978 = 0.05 - 0.001483 = 0.04852
    $$

    At $t = 4$ ($T - t = 1$):

    $$
    B(1) = \frac{1 - e^{-0.3}}{0.3} = 0.8640
    $$

    $$
    \theta^T(4) = 0.05 - 0.00075 \times 0.8640 = 0.05 - 0.000648 = 0.04935
    $$

    All values are **below** $\theta = 0.05$: the $T$-forward measure shifts the mean-reversion target downward. Economically, the forward measure overweights states where the discount factor $P(t,T)$ is large, which corresponds to paths where rates are low. This tilts the conditional distribution of $r_T$ downward relative to the risk-neutral measure. The shift vanishes as $t \to T$ ($\theta^T(T) = \theta$) because the numeraire bond matures and the two measures coincide.

---

**Exercise 4.** The comparison table shows that the Gaussian distribution is preserved under all three measures. Explain why the Girsanov kernel is deterministic in the Vasicek model (it depends only on $B(T-t)$ and $\sigma$, not on $r_t$). Contrast this with the CIR model where the kernel is $B(T-t)\sigma\sqrt{r_t}$.

??? success "Solution to Exercise 4"
    In the Vasicek model, the bond price volatility is $\sigma_P(t,T) = -B(T-t)\,\sigma$ where $B(T-t) = (1 - e^{-\kappa(T-t)})/\kappa$ is a deterministic function of $t$ and $T$. The Girsanov kernel for the change from $\mathbb{Q}$ to $\mathbb{Q}^T$ is:

    $$
    \gamma(t) = -\sigma_P(t,T) = B(T-t)\,\sigma
    $$

    This is **deterministic** because both $B(T-t)$ and $\sigma$ are non-random. The reason traces to the affine structure with **constant diffusion**: in the Vasicek SDE, the diffusion coefficient is $\sigma$ (a constant), so the bond price diffusion $\sigma_P = -B(\tau)\sigma$ involves no state variable $r_t$.

    When the Girsanov kernel is deterministic, the change of measure preserves the Gaussian nature of the process. Under $\mathbb{Q}^T$, the SDE $dr_t = \kappa(\theta^T(t) - r_t)\,dt + \sigma\,dW_t^T$ is still linear in $r_t$ with additive Gaussian noise, so $r_T$ remains normally distributed.

    In the **CIR model**, $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$, the bond price volatility is $\sigma_P^{\text{CIR}}(t,T) = -B^{\text{CIR}}(T-t)\,\sigma\sqrt{r_t}$, which depends on $r_t$. The Girsanov kernel $\gamma(t) = B^{\text{CIR}}(T-t)\,\sigma\sqrt{r_t}$ is **stochastic**, depending on the current state. This state-dependent measure change alters the distribution type: $r_t$ follows a non-central chi-squared distribution under $\mathbb{Q}$ but a different non-central chi-squared under $\mathbb{Q}^T$, and the Gaussian property is never present.

---

**Exercise 5.** Under $\mathbb{Q}^T$, the forward bond price $F(t) = P(t,S)/P(t,T)$ is a martingale. Derive the SDE for $F(t)$ in the Vasicek model and show that $dF/F = -[B(S-t) - B(T-t)]\sigma\,dW_t^T$. Why is this log-normal dynamics important for option pricing?

??? success "Solution to Exercise 5"
    The forward bond price is $F(t) = P(t,S)/P(t,T)$ for $S > T$. Under $\mathbb{Q}^T$ with numeraire $P(t,T)$, the ratio $V_t/P(t,T)$ is a martingale for any traded asset $V_t$. Since $P(t,S)$ is a traded asset, $F(t) = P(t,S)/P(t,T)$ is a $\mathbb{Q}^T$-martingale.

    To derive the SDE, note $\ln F(t) = \ln P(t,S) - \ln P(t,T)$. The diffusion of $\ln P(t,\cdot)$ under $\mathbb{Q}^T$ has volatility $\sigma_P(t,\cdot) = -B(\cdot - t)\sigma$. By Ito's lemma applied to the ratio:

    $$
    \frac{dF}{F} = \text{(drift)}\,dt + [-B(S-t)\sigma - (-B(T-t)\sigma)]\,dW_t^T
    $$

    $$
    = \text{(drift)}\,dt - [B(S-t) - B(T-t)]\,\sigma\,dW_t^T
    $$

    Since $F$ is a martingale under $\mathbb{Q}^T$, the drift is zero:

    $$
    \frac{dF}{F} = -[B(S-t) - B(T-t)]\,\sigma\,dW_t^T
    $$

    The volatility $[B(S-t) - B(T-t)]\sigma$ is deterministic (a function of $t$ only), so $F(t)$ follows a geometric Brownian motion with time-dependent but deterministic volatility under $\mathbb{Q}^T$. This means $F(T) = P(T,S)$ is **log-normally distributed** under $\mathbb{Q}^T$.

    This log-normality is the key to closed-form option pricing: the European call on a ZCB has payoff $(P(T,S) - K)^+ = (F(T) - K)^+$ (since $F(T) = P(T,S)/P(T,T) = P(T,S)$), and pricing under $\mathbb{Q}^T$ reduces to the Black-Scholes formula for a log-normal variable, yielding the Vasicek bond option formula.

---

**Exercise 6.** Explain why the $T$-forward measure simplifies the pricing of a European claim $h(r_T)$ from $V(t) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s ds} h(r_T) | \mathcal{F}_t]$ to $V(t) = P(t,T)\mathbb{E}^{\mathbb{Q}^T}[h(r_T) | \mathcal{F}_t]$. What computational advantage does this provide?

??? success "Solution to Exercise 6"
    Under $\mathbb{Q}$ with numeraire $B_t = e^{\int_0^t r_s\,ds}$, the price of a European claim with payoff $h(r_T)$ at time $T$ is:

    $$
    V(t) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,h(r_T)\,\Big|\,\mathcal{F}_t\right]
    $$

    The difficulty is that $e^{-\int_t^T r_s\,ds}$ is stochastic and **correlated** with $h(r_T)$: both depend on the path of $r_s$ over $[t,T]$. The expectation of a product of correlated random variables is not the product of expectations, so the integral and the payoff cannot be separated.

    Under $\mathbb{Q}^T$ with numeraire $P(t,T)$:

    $$
    V(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[h(r_T)\,\Big|\,\mathcal{F}_t\right]
    $$

    Now $P(t,T)$ is a **known quantity** at time $t$ (it is $\mathcal{F}_t$-measurable), and the expectation involves only $h(r_T)$---the discount factor has been absorbed into the measure change.

    **Computational advantage:** Under $\mathbb{Q}^T$, $r_T$ is Gaussian with known mean $m^T(t,T)$ and variance $v^2(t,T)$. The expectation $\mathbb{E}^{\mathbb{Q}^T}[h(r_T)]$ is a one-dimensional integral against a Gaussian density, which can often be evaluated in closed form (e.g., for call/put payoffs via the Black-Scholes formula) or by simple numerical quadrature. Under $\mathbb{Q}$, one would need to evaluate a path integral involving the joint distribution of $\int_t^T r_s\,ds$ and $r_T$, which is considerably more complex even though this joint distribution is also Gaussian in the Vasicek model.

---

**Exercise 7.** The market price of risk connects the physical measure $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$. If $\lambda$ is constant, show that $\kappa = \kappa^{\mathbb{P}} + \lambda$ and $\theta = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa$. Why is $\sigma$ the same under both measures?

??? success "Solution to Exercise 7"
    Under the physical measure $\mathbb{P}$:

    $$
    dr_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)\,dt + \sigma\,dW_t^{\mathbb{P}}
    $$

    The Girsanov theorem with a constant market price of risk $\lambda$ defines $dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} + \lambda\,dt$. Substituting $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \lambda\,dt$:

    $$
    dr_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)\,dt + \sigma(dW_t^{\mathbb{Q}} - \lambda\,dt)
    $$

    $$
    = [\kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t) - \sigma\lambda]\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    $$
    = [\kappa^{\mathbb{P}}\theta^{\mathbb{P}} - \sigma\lambda - \kappa^{\mathbb{P}} r_t]\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    We want to write this in Vasicek form $\kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$, so:

    $$
    \kappa = \kappa^{\mathbb{P}} + \lambda, \qquad \kappa\theta = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} - \sigma\lambda + \lambda\theta^{\mathbb{P}} ..
    $$

    Wait---let us be more careful. Rewriting the drift:

    $$
    \kappa^{\mathbb{P}}\theta^{\mathbb{P}} - \sigma\lambda - \kappa^{\mathbb{P}} r_t
    $$

    To match $\kappa(\theta - r_t) = \kappa\theta - \kappa r_t$, we need $\kappa = \kappa^{\mathbb{P}}$ (the coefficient of $-r_t$). But this contradicts the claim $\kappa = \kappa^{\mathbb{P}} + \lambda$.

    The resolution is that the market price of risk in the Vasicek model is typically specified as $\lambda(r_t) = \lambda_0 + \lambda_1 r_t / \sigma$ (affine in $r_t$). For the specific form where the Girsanov kernel is $\lambda r_t / \sigma$ (proportional to $r_t$), we get $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda$ and $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} / \kappa^{\mathbb{Q}}$.

    With $\lambda(r_t) = \lambda_1 r_t$ as the Girsanov drift, substituting $dW^{\mathbb{P}} = dW^{\mathbb{Q}} - \lambda_1 r_t\,dt$:

    $$
    dr_t = [\kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t) - \sigma\lambda_1 r_t]\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    $$
    = [\kappa^{\mathbb{P}}\theta^{\mathbb{P}} - (\kappa^{\mathbb{P}} + \sigma\lambda_1)r_t]\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    Setting $\kappa = \kappa^{\mathbb{P}} + \sigma\lambda_1$ and $\theta = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} / \kappa$, the SDE becomes $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$.

    **Why $\sigma$ is the same:** The Girsanov theorem changes only the drift of the Brownian motion, not its quadratic variation. Since $\langle W^{\mathbb{Q}} \rangle_t = \langle W^{\mathbb{P}} \rangle_t = t$, the diffusion coefficient $\sigma$ multiplying $dW$ is invariant under the measure change. Volatility is a property of the paths (quadratic variation), which is the same under all equivalent measures.
