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

The Radon-Nikodym derivative that defines the change of measure is

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
