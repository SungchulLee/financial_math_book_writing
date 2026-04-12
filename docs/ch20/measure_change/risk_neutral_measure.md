# Risk-Neutral Measure in the Hull-White Model

The Hull-White model is typically specified directly under the risk-neutral measure $\mathbb{Q}$, where the short rate dynamics take the familiar mean-reverting form. However, understanding how this measure relates to the physical (real-world) measure $\mathbb{P}$ through the market price of risk is essential for interpreting model parameters and connecting to observable data. This section presents the Hull-White dynamics under both measures and derives the Girsanov transformation that links them.

## Physical Measure Dynamics

Under the real-world (physical) measure $\mathbb{P}$, the short rate in the Hull-White framework satisfies

$$
dr(t) = \lambda^{\mathbb{P}}\!\left(\theta^{\mathbb{P}}(t) - r(t)\right)dt + \sigma\,dW^{\mathbb{P}}(t)
$$

where $\lambda^{\mathbb{P}}$ is the physical mean reversion speed, $\theta^{\mathbb{P}}(t)$ is the physical mean reversion level, and $W^{\mathbb{P}}(t)$ is a standard Brownian motion under $\mathbb{P}$. These parameters govern the actual statistical behavior of the short rate observed in the market.

The volatility parameter $\sigma$ is the same under both measures because Girsanov's theorem changes the drift but not the diffusion coefficient.

## Market Price of Interest Rate Risk

To move from $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$, we introduce the market price of interest rate risk $\gamma(t)$, which quantifies the excess return per unit of volatility that the market demands for bearing interest rate risk.

!!! info "Definition: Market Price of Risk"
    The market price of interest rate risk $\gamma(t)$ is a (possibly time-dependent) adapted process such that

    $$
    dW^{\mathbb{Q}}(t) = dW^{\mathbb{P}}(t) + \gamma(t)\,dt
    $$

    defines a standard Brownian motion $W^{\mathbb{Q}}(t)$ under the risk-neutral measure $\mathbb{Q}$.

The Radon–Nikodym derivative that defines the change of measure is

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\Bigg|_{\mathcal{F}(t)} = \exp\!\left(-\int_0^t \gamma(s)\,dW^{\mathbb{P}}(s) - \frac{1}{2}\int_0^t \gamma(s)^2\,ds\right)
$$

By Girsanov's theorem, this is a valid change of measure provided the Novikov condition $\mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \gamma(s)^2\,ds\right)\right] < \infty$ is satisfied.

## Hull-White Dynamics Under Q

Substituting $dW^{\mathbb{P}}(t) = dW^{\mathbb{Q}}(t) - \gamma(t)\,dt$ into the physical dynamics:

$$\begin{array}{lllll}
\displaystyle
dr(t)
&=&\displaystyle
\lambda^{\mathbb{P}}\!\left(\theta^{\mathbb{P}}(t) - r(t)\right)dt + \sigma\left(dW^{\mathbb{Q}}(t) - \gamma(t)\,dt\right)
\\[6pt]
&=&\displaystyle
\left[\lambda^{\mathbb{P}}\!\left(\theta^{\mathbb{P}}(t) - r(t)\right) - \sigma\gamma(t)\right]dt + \sigma\,dW^{\mathbb{Q}}(t)
\end{array}$$

!!! info "Theorem: Risk-Neutral Hull-White SDE"
    Under the risk-neutral measure $\mathbb{Q}$, the Hull-White short rate satisfies

    $$
    dr(t) = \lambda\!\left(\theta^{\mathbb{Q}}(t) - r(t)\right)dt + \sigma\,dW^{\mathbb{Q}}(t)
    $$

    where the risk-neutral parameters relate to the physical parameters and the market price of risk through

    $$\begin{array}{lllll}
    \displaystyle
    \lambda &=& \lambda^{\mathbb{P}}
    \\[4pt]
    \displaystyle
    \lambda\,\theta^{\mathbb{Q}}(t)
    &=&\displaystyle
    \lambda^{\mathbb{P}}\theta^{\mathbb{P}}(t) - \sigma\gamma(t)
    \end{array}$$

???+ note "Proof"

    Comparing the $\mathbb{Q}$-dynamics

    $$
    dr(t) = \left[\lambda^{\mathbb{P}}\theta^{\mathbb{P}}(t) - \lambda^{\mathbb{P}}r(t) - \sigma\gamma(t)\right]dt + \sigma\,dW^{\mathbb{Q}}(t)
    $$

    with the standard form $dr(t) = \lambda(\theta^{\mathbb{Q}}(t) - r(t))dt + \sigma\,dW^{\mathbb{Q}}(t)$, matching the $r(t)$ coefficient gives $\lambda = \lambda^{\mathbb{P}}$ (the mean reversion speed is unchanged). Matching the remaining drift terms gives $\lambda\theta^{\mathbb{Q}}(t) = \lambda^{\mathbb{P}}\theta^{\mathbb{P}}(t) - \sigma\gamma(t)$. $\square$

## Affine Market Price of Risk

A common specification assumes the market price of risk is affine in the short rate:

$$
\gamma(t) = \gamma_0 + \gamma_1\,r(t)
$$

Under this assumption the risk-neutral drift becomes

$$\begin{array}{lllll}
\displaystyle
\lambda\theta^{\mathbb{Q}}(t) - \lambda r(t)
&=&\displaystyle
\lambda^{\mathbb{P}}\theta^{\mathbb{P}}(t) - \sigma\gamma_0 - (\lambda^{\mathbb{P}} + \sigma\gamma_1)r(t)
\end{array}$$

This implies that the risk-neutral mean reversion speed is $\lambda = \lambda^{\mathbb{P}} + \sigma\gamma_1$, which generally differs from $\lambda^{\mathbb{P}}$ when $\gamma_1 \neq 0$. In particular:

- **Constant market price of risk** ($\gamma_1 = 0$): The mean reversion speed is the same under $\mathbb{P}$ and $\mathbb{Q}$. Only $\theta$ shifts.
- **Rate-dependent market price of risk** ($\gamma_1 \neq 0$): Both the mean reversion speed and level change under the measure change.

!!! warning "Common Convention"
    In practice, the Hull-White model is almost always specified directly under $\mathbb{Q}$ with $\lambda$ and $\theta^{\mathbb{Q}}(t)$ as primary parameters. The physical measure parameters and market price of risk are then inferred from time series data if needed. The calibration to the initial yield curve determines $\theta^{\mathbb{Q}}(t)$ without any reference to $\mathbb{P}$.

## Bond Pricing Under Q

Under $\mathbb{Q}$, the discounted bond price process $P(t,T)/M(t)$ is a martingale, where $M(t) = \exp(\int_0^t r(s)\,ds)$ is the money market account. This martingale property is the fundamental reason the risk-neutral measure is the natural setting for derivative pricing:

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t)}{M(T)}\,\Big|\,\mathcal{F}(t)\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(s)\,ds}\,\Big|\,\mathcal{F}(t)\right]
$$

Any derivative with payoff $V(T)$ at time $T$ is priced as

$$
V(t) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(s)\,ds}\,V(T)\,\Big|\,\mathcal{F}(t)\right]
$$

## Numerical Example

Suppose the physical dynamics have $\lambda^{\mathbb{P}} = 0.03$, $\theta^{\mathbb{P}}(t) = 0.05$, and $\sigma = 0.01$. If the market price of risk is constant at $\gamma = -0.15$ (negative, reflecting a positive risk premium for interest rate risk), then the risk-neutral parameters are

$$\begin{array}{lllll}
\displaystyle
\lambda &=& 0.03
\\[4pt]
\displaystyle
\theta^{\mathbb{Q}}(t) &=& 0.05 - \frac{0.01 \times (-0.15)}{0.03} = 0.05 + 0.05 = 0.10
\end{array}$$

The risk-neutral mean reversion level is higher than the physical level, reflecting the fact that the market demands compensation for bearing interest rate risk, which shifts the drift upward under $\mathbb{Q}$.

In practice, $\theta^{\mathbb{Q}}(t)$ is not set this way but is instead calibrated to match the observed term structure $P^M(0,T)$, yielding the time-dependent function derived in the consistency section.

## From HJM to Risk-Neutral Hull-White

An alternative route to the risk-neutral Hull-White SDE starts from the HJM framework. Under $\mathbb{Q}$, the HJM drift condition ensures no-arbitrage:

$$
\mu^{\mathbb{Q}}(t,T) = \sigma(t,T)\int_t^T \sigma(t,u)\,du
$$

For the Hull-White volatility specification $\sigma(t,T) = \sigma\,e^{-\lambda(T-t)}$, the HJM drift condition determines the forward rate dynamics uniquely under $\mathbb{Q}$, and the short rate process $r(t) = f(t,t)$ inherits the Hull-White SDE.

---

## Summary

The Hull-White model under $\mathbb{Q}$ is obtained from the physical measure $\mathbb{P}$ via Girsanov's theorem with market price of risk $\gamma(t)$. The mean reversion speed is preserved (for constant $\gamma$), while the mean reversion level shifts according to $\lambda\theta^{\mathbb{Q}}(t) = \lambda^{\mathbb{P}}\theta^{\mathbb{P}}(t) - \sigma\gamma(t)$. In practice, the model is calibrated directly under $\mathbb{Q}$ by fitting $\theta^{\mathbb{Q}}(t)$ to the market term structure, bypassing explicit specification of the physical measure.

---

## Exercises

**Exercise 1.** The Novikov condition requires $\mathbb{E}^{\mathbb{P}}[\exp(\frac{1}{2}\int_0^T \gamma(s)^2\,ds)] < \infty$. For a constant market price of risk $\gamma$, show that this condition is always satisfied and compute the Radon–Nikodym derivative explicitly.

??? success "Solution to Exercise 1"
    For a constant market price of risk $\gamma$, the Novikov condition becomes

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \gamma^2\,ds\right)\right] = \exp\!\left(\frac{1}{2}\gamma^2 T\right) < \infty
    $$

    Since $\gamma$ is a finite constant and $T < \infty$, the exponential of a finite number is always finite. Therefore the Novikov condition is automatically satisfied for any constant $\gamma$.

    The Radon–Nikodym derivative simplifies to

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\Bigg|_{\mathcal{F}(t)} = \exp\!\left(-\gamma\,W^{\mathbb{P}}(t) - \frac{1}{2}\gamma^2 t\right)
    $$

    This is a standard exponential martingale $\mathcal{E}(-\gamma W^{\mathbb{P}})_t$. One can verify it is a martingale by checking that $\mathbb{E}^{\mathbb{P}}[\frac{d\mathbb{Q}}{d\mathbb{P}}\big|_{\mathcal{F}(t)}] = 1$, which follows from the moment generating function of the normal distribution: $W^{\mathbb{P}}(t) \sim \mathcal{N}(0, t)$, so

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[e^{-\gamma W^{\mathbb{P}}(t) - \frac{1}{2}\gamma^2 t}\right] = e^{-\frac{1}{2}\gamma^2 t}\,e^{\frac{1}{2}\gamma^2 t} = 1
    $$

---

**Exercise 2.** Suppose $\lambda^{\mathbb{P}} = 0.04$, $\theta^{\mathbb{P}}(t) = 0.06$, $\sigma = 0.012$, and $\gamma = -0.20$. Compute $\lambda$ and $\theta^{\mathbb{Q}}(t)$ under the risk-neutral measure. Is $\theta^{\mathbb{Q}}(t)$ higher or lower than $\theta^{\mathbb{P}}(t)$, and why?

??? success "Solution to Exercise 2"
    With $\lambda^{\mathbb{P}} = 0.04$, $\theta^{\mathbb{P}}(t) = 0.06$, $\sigma = 0.012$, and constant $\gamma = -0.20$:

    **Mean reversion speed:** Since $\gamma$ is constant (i.e., $\gamma_1 = 0$ in the affine specification), the mean reversion speed is preserved:

    $$
    \lambda = \lambda^{\mathbb{P}} = 0.04
    $$

    **Mean reversion level:** From $\lambda\theta^{\mathbb{Q}}(t) = \lambda^{\mathbb{P}}\theta^{\mathbb{P}}(t) - \sigma\gamma$:

    $$
    \theta^{\mathbb{Q}}(t) = \theta^{\mathbb{P}}(t) - \frac{\sigma\gamma}{\lambda} = 0.06 - \frac{0.012 \times (-0.20)}{0.04} = 0.06 + 0.06 = 0.12
    $$

    So $\theta^{\mathbb{Q}}(t) = 0.12 > 0.06 = \theta^{\mathbb{P}}(t)$.

    The risk-neutral mean reversion level is higher because $\gamma < 0$, which means the market demands a positive risk premium for bearing interest rate risk. Under $\mathbb{Q}$, the drift is shifted upward to compensate investors for this risk. The negative market price of risk implies that bond investors require extra compensation (higher expected rates under $\mathbb{Q}$) relative to the physical dynamics.

---

**Exercise 3.** For the affine market price of risk $\gamma(t) = \gamma_0 + \gamma_1 r(t)$, show that the risk-neutral mean reversion speed is $\lambda = \lambda^{\mathbb{P}} + \sigma\gamma_1$, which differs from $\lambda^{\mathbb{P}}$. Give a financial interpretation of why the mean reversion speed can change under a measure change when $\gamma_1 \neq 0$.

??? success "Solution to Exercise 3"
    With $\gamma(t) = \gamma_0 + \gamma_1 r(t)$, substituting into the $\mathbb{Q}$-drift:

    $$\begin{array}{lllll}
    \displaystyle
    dr(t)
    &=&\displaystyle
    \left[\lambda^{\mathbb{P}}(\theta^{\mathbb{P}}(t) - r(t)) - \sigma(\gamma_0 + \gamma_1 r(t))\right]dt + \sigma\,dW^{\mathbb{Q}}(t)
    \\[6pt]
    &=&\displaystyle
    \left[\lambda^{\mathbb{P}}\theta^{\mathbb{P}}(t) - \sigma\gamma_0 - (\lambda^{\mathbb{P}} + \sigma\gamma_1)r(t)\right]dt + \sigma\,dW^{\mathbb{Q}}(t)
    \end{array}$$

    Matching to the standard form $dr(t) = \lambda(\theta^{\mathbb{Q}}(t) - r(t))dt + \sigma\,dW^{\mathbb{Q}}(t)$, the coefficient of $r(t)$ gives

    $$
    \lambda = \lambda^{\mathbb{P}} + \sigma\gamma_1
    $$

    which differs from $\lambda^{\mathbb{P}}$ whenever $\gamma_1 \neq 0$.

    **Financial interpretation:** When $\gamma_1 \neq 0$, the market price of risk depends on the level of the short rate. This means the risk premium that investors demand varies with the interest rate environment. A positive $\gamma_1$ increases the risk-neutral mean reversion speed relative to the physical speed: when rates are high, the larger risk premium creates stronger downward pressure under $\mathbb{Q}$, and when rates are low, the smaller risk premium creates less upward pressure. This state-dependent adjustment to the drift effectively modifies how quickly the process reverts, changing the mean reversion speed under the new measure. By contrast, a constant market price of risk ($\gamma_1 = 0$) shifts the drift uniformly, affecting only the level to which the process reverts, not the speed.

---

**Exercise 4.** Explain why the volatility parameter $\sigma$ is the same under both $\mathbb{P}$ and $\mathbb{Q}$. What theorem guarantees this invariance, and what property of the diffusion coefficient is required?

??? success "Solution to Exercise 4"
    The volatility parameter $\sigma$ is the same under $\mathbb{P}$ and $\mathbb{Q}$ because of **Girsanov's theorem**, which guarantees that a change of measure modifies only the drift of an Ito process, not the diffusion coefficient.

    Specifically, Girsanov's theorem constructs the new Brownian motion $W^{\mathbb{Q}}(t) = W^{\mathbb{P}}(t) + \int_0^t \gamma(s)\,ds$, so

    $$
    dW^{\mathbb{P}}(t) = dW^{\mathbb{Q}}(t) - \gamma(t)\,dt
    $$

    Substituting into $dr(t) = \mu^{\mathbb{P}}(t)\,dt + \sigma\,dW^{\mathbb{P}}(t)$:

    $$
    dr(t) = \left[\mu^{\mathbb{P}}(t) - \sigma\gamma(t)\right]dt + \sigma\,dW^{\mathbb{Q}}(t)
    $$

    The $dt$ coefficient (drift) changes, but the $dW$ coefficient (diffusion) remains exactly $\sigma$. This invariance holds because Girsanov's theorem operates by an absolutely continuous change of measure, which preserves the quadratic variation $\langle r \rangle_t = \int_0^t \sigma^2\,ds$. The quadratic variation is a path-by-path property that does not depend on the probability measure, so the diffusion coefficient $\sigma$ is measure-invariant.

---

**Exercise 5.** Under $\mathbb{Q}$, the discounted bond price $P(t,T)/M(t)$ is a martingale. Verify this for the Hull-White model by showing that the drift of $d(P(t,T)/M(t))$ vanishes. (Hint: use the bond dynamics $dP/P = r\,dt + \sigma_P dW^{\mathbb{Q}}$ and the money market dynamics $dM = rM\,dt$.)

??? success "Solution to Exercise 5"
    Define $Z(t) = P(t,T)/M(t)$, the discounted bond price. We need to show $Z(t)$ is a $\mathbb{Q}$-martingale, i.e., its drift under $\mathbb{Q}$ vanishes.

    The bond dynamics under $\mathbb{Q}$ are $dP = r P\,dt + \sigma_P P\,dW^{\mathbb{Q}}$ and the money market dynamics are $dM = rM\,dt$.

    Using the quotient rule (Ito's formula for $Z = P/M$):

    $$\begin{array}{lllll}
    \displaystyle
    dZ
    &=&\displaystyle
    \frac{1}{M}\,dP - \frac{P}{M^2}\,dM + \frac{P}{M^3}(dM)^2 - \frac{1}{M^2}\,dP\,dM
    \end{array}$$

    Since $dM = rM\,dt$ has no Brownian component, $(dM)^2 = 0$ and $dP\,dM = 0$. Therefore:

    $$\begin{array}{lllll}
    \displaystyle
    dZ
    &=&\displaystyle
    \frac{1}{M}\!\left(rP\,dt + \sigma_P P\,dW^{\mathbb{Q}}\right) - \frac{P}{M^2}(rM\,dt)
    \\[6pt]
    &=&\displaystyle
    \frac{P}{M}\!\left(r\,dt + \sigma_P\,dW^{\mathbb{Q}} - r\,dt\right)
    \\[6pt]
    &=&\displaystyle
    Z\,\sigma_P\,dW^{\mathbb{Q}}
    \end{array}$$

    The drift vanishes, so $Z(t) = P(t,T)/M(t)$ is indeed a $\mathbb{Q}$-martingale.

---

**Exercise 6.** Describe the alternative route from HJM to the risk-neutral Hull-White SDE. Starting from the HJM volatility $\sigma(t,T) = \sigma e^{-\lambda(T-t)}$, derive the HJM drift condition and show that the short rate $r(t) = f(t,t)$ satisfies the Hull-White SDE.

??? success "Solution to Exercise 6"
    **Step 1: HJM forward rate dynamics.** Under $\mathbb{Q}$, the HJM framework specifies:

    $$
    df(t,T) = \mu^{\mathbb{Q}}(t,T)\,dt + \sigma(t,T)\,dW^{\mathbb{Q}}(t)
    $$

    The HJM drift condition (no-arbitrage under $\mathbb{Q}$) requires:

    $$
    \mu^{\mathbb{Q}}(t,T) = \sigma(t,T)\int_t^T \sigma(t,u)\,du
    $$

    **Step 2: Hull-White volatility specification.** For $\sigma(t,T) = \sigma e^{-\lambda(T-t)}$:

    $$
    \int_t^T \sigma(t,u)\,du = \int_t^T \sigma e^{-\lambda(u-t)}\,du = \frac{\sigma}{\lambda}\left(1 - e^{-\lambda(T-t)}\right)
    $$

    So the drift is:

    $$
    \mu^{\mathbb{Q}}(t,T) = \sigma e^{-\lambda(T-t)} \cdot \frac{\sigma}{\lambda}\left(1 - e^{-\lambda(T-t)}\right) = \frac{\sigma^2}{\lambda}e^{-\lambda(T-t)}\left(1 - e^{-\lambda(T-t)}\right)
    $$

    **Step 3: Extract the short rate.** Set $r(t) = f(t,t)$. Using the chain rule:

    $$
    dr(t) = \left[\frac{\partial f}{\partial t}(t,t) + \frac{\partial f}{\partial T}(t,t)\right]dt + \text{(evaluated at } T = t\text{)}
    $$

    Integrating the forward rate dynamics and differentiating with respect to $T$, one obtains:

    $$
    dr(t) = \left[\frac{\partial f^M}{\partial T}(0,t) + \frac{\sigma^2}{2\lambda^2}\frac{\partial}{\partial t}(1 - e^{-\lambda t})^2 + \lambda(f^M(0,t) - r(t)) + \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda t})\right]dt + \sigma\,dW^{\mathbb{Q}}(t)
    $$

    Collecting terms and defining $\theta^{\mathbb{Q}}(t)$ appropriately, this reduces to the Hull-White SDE $dr(t) = \lambda(\theta^{\mathbb{Q}}(t) - r(t))dt + \sigma\,dW^{\mathbb{Q}}(t)$. The HJM drift condition uniquely determines the drift, ensuring no-arbitrage.

---

**Exercise 7.** In practice, $\theta^{\mathbb{Q}}(t)$ is calibrated to the market term structure rather than derived from $\theta^{\mathbb{P}}(t)$ and $\gamma(t)$. Discuss the advantages and disadvantages of this approach. Under what circumstances would you need to estimate $\gamma(t)$ explicitly?

??? success "Solution to Exercise 7"
    **Advantages of direct calibration under $\mathbb{Q}$:**

    - The function $\theta^{\mathbb{Q}}(t)$ is uniquely determined by the observed market term structure $P^M(0,T)$ through the relation $\theta^{\mathbb{Q}}(t) = \frac{1}{\lambda}\frac{\partial f^M}{\partial T}(0,t) + f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2$. This ensures the model exactly reproduces all observed bond prices.
    - No estimation of the market price of risk $\gamma(t)$ or physical dynamics is needed, avoiding the statistical challenges of estimating drift parameters from noisy time series data.
    - The approach is model-consistent for pricing: all derivative prices are expectations under $\mathbb{Q}$, so only $\mathbb{Q}$-parameters matter.

    **Disadvantages:**

    - Physical dynamics are unknown, so the model cannot generate realistic rate scenarios for risk management (VaR, stress testing) without additional assumptions.
    - The model provides no information about expected returns on bonds or risk premia.
    - Changes in the yield curve over time lead to recalibration of $\theta^{\mathbb{Q}}(t)$, and the time-series behavior of recalibrated parameters may be unrealistic.

    **When explicit estimation of $\gamma(t)$ is needed:**

    - **Risk management and scenario generation:** Simulating future rate paths for VaR or expected shortfall requires the physical measure $\mathbb{P}$.
    - **Real-world forecasting:** Predicting future interest rate levels or evaluating investment strategies.
    - **Relative value analysis:** Comparing model-implied risk premia to historical norms to identify mispriced securities.
    - **Multi-period portfolio optimization:** Utility-based optimization requires expected returns under $\mathbb{P}$, not $\mathbb{Q}$.
