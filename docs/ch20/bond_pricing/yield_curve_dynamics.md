# Yield Curve Dynamics Under Hull-White

The Hull-White model is a single-factor model: the entire yield curve at any future time $t$ is determined by the single state variable $r(t)$. This section derives how the yield curve evolves over time, establishes the affine relationship between yields and the short rate, and shows that yield curve movements are driven by a single "level" factor that produces approximate parallel shifts in the short-maturity region.

## Yield-to-Maturity in the Hull-White Model

The continuously compounded yield $R(t,T)$ for a zero-coupon bond maturing at $T$ is defined through the bond price as $P(t,T) = e^{-R(t,T)(T-t)}$. Since the Hull-White bond price has the affine form $P(t,T) = A(t,T)e^{-B(t,T)r(t)}$, the yield inherits a corresponding affine structure in $r(t)$.

!!! info "Definition: Hull-White Yield"
    The continuously compounded yield is

    $$
    R(t,T) = -\frac{\log P(t,T)}{T - t} = -\frac{\log A(t,T)}{T - t} + \frac{B(t,T)}{T - t}\,r(t)
    $$

    where $\tau = T - t$ is the time to maturity.

Writing $a(\tau, t) = -\frac{\log A(t,T)}{T-t}$ and $b(\tau) = \frac{B(t,T)}{T-t}$, the yield becomes

$$
R(t,T) = a(\tau, t) + b(\tau)\,r(t)
$$

The function $b(\tau)$ depends only on time-to-maturity $\tau$ and the mean reversion speed $\lambda$:

$$
b(\tau) = \frac{B(t,T)}{\tau} = \frac{1}{\lambda\tau}\left[1 - e^{-\lambda\tau}\right]
$$

This function equals 1 at $\tau = 0$ and decays toward zero as $\tau \to \infty$, quantifying how much the short rate influences yields at different maturities.

## Single-Factor Structure

Since $R(t,T) = a(\tau, t) + b(\tau)\,r(t)$ and $r(t)$ is the only stochastic variable, a change in the short rate $\Delta r$ shifts the entire yield curve by

$$
\Delta R(t,T) = b(\tau)\,\Delta r
$$

This is the defining property of a single-factor affine model: all yield movements are proportional to a single random shock, with the loading function $b(\tau)$ determining the magnitude at each maturity.

!!! info "Proposition: Yield Curve Shift"
    In the Hull-White model, the instantaneous change in the yield curve satisfies

    $$
    dR(t,T) = \frac{\partial a(\tau, t)}{\partial t}\,dt + b(\tau)\,dr(t)
    $$

    The stochastic component is

    $$
    b(\tau)\,\sigma\,dW^{\mathbb{Q}}(t) = \frac{1 - e^{-\lambda\tau}}{\lambda\tau}\,\sigma\,dW^{\mathbb{Q}}(t)
    $$

    so yields at all maturities are driven by the same Brownian motion, differing only in the loading $b(\tau)$.

## Parallel Shifts and the Level Factor

For short maturities ($\lambda\tau \ll 1$), a Taylor expansion gives

$$
b(\tau) = \frac{1 - e^{-\lambda\tau}}{\lambda\tau} \approx 1 - \frac{\lambda\tau}{2} + \frac{(\lambda\tau)^2}{6} - \cdots
$$

When $\lambda$ is small or $\tau$ is small, $b(\tau) \approx 1$ and $\Delta R \approx \Delta r$. In this regime the yield curve shifts approximately in parallel, consistent with the empirical observation that the first principal component of yield curve movements (the "level" factor) explains the majority of variance.

!!! tip "Interpretation"
    The Hull-White model captures the dominant "level" mode of yield curve movements. However, because $b(\tau)$ is strictly decreasing, the model cannot produce pure steepening or curvature movements independently. Two-factor extensions of Hull-White address this limitation by introducing a second stochastic factor.

## Long-Maturity Behavior

As $\tau \to \infty$, the loading function $b(\tau) \to 0$, meaning that the long end of the yield curve becomes insensitive to the current short rate. The long yield converges to a deterministic limit:

$$
\lim_{\tau \to \infty} R(t,T) = \lim_{\tau \to \infty} a(\tau, t)
$$

???+ note "Derivation"

    Since $B(t,T) = \frac{1}{\lambda}(1 - e^{-\lambda\tau})$ is bounded above by $1/\lambda$, we have $b(\tau) = B(t,T)/\tau \to 0$ as $\tau \to \infty$. Therefore the $r(t)$-dependent term vanishes and only the deterministic component $a(\tau,t)$ survives.

    The long yield is determined by the asymptotic behavior of $A(t,T)$:

    $$\begin{array}{lllll}
    \displaystyle
    \lim_{\tau\to\infty} a(\tau,t)
    &=&\displaystyle
    \lim_{\tau\to\infty}\left[-\frac{1}{\tau}\log\frac{P^M(0,T)}{P^M(0,t)} - \frac{B(t,T)}{\tau}f^M(0,t) + \frac{\sigma^2}{4\lambda\tau}B(t,T)^2(1-e^{-2\lambda t})\right]
    \end{array}$$

    For standard market curves where $\log P^M(0,T) \sim -\bar{f}\,T$ for large $T$, this limit equals $\bar{f}$, the asymptotic forward rate.

## Yield Volatility Term Structure

The volatility of yields at different maturities forms the yield volatility term structure. From the diffusion coefficient:

$$
\text{vol}(R(t,T)) = b(\tau)\,\sigma = \frac{1 - e^{-\lambda\tau}}{\lambda\tau}\,\sigma
$$

This function is maximized at $\tau = 0$ (where it equals $\sigma$) and decays monotonically with maturity. The implication is that short-term yields are more volatile than long-term yields, a feature broadly consistent with empirical data.

!!! info "Proposition: Yield Volatility Ratio"
    The ratio of the volatility of the $\tau$-year yield to the short rate volatility is

    $$
    \frac{\text{vol}(R(t,T))}{\sigma} = \frac{1 - e^{-\lambda\tau}}{\lambda\tau}
    $$

    For $\lambda = 0.05$ and $\tau = 10$: ratio $\approx 0.787$. For $\tau = 30$: ratio $\approx 0.554$.

## Numerical Example

Consider a Hull-White model with $\lambda = 0.05$, $\sigma = 0.01$, and a flat initial forward rate $f^M(0,t) = 0.04$. At time $t$, given a short rate realization $r(t) = 0.05$, the yield at maturity $\tau$ is

$$
R(t,T) = a(\tau,t) + b(\tau) \times 0.05
$$

The loading function values at selected maturities are:

| $\tau$ (years) | $b(\tau)$ | Yield volatility $b(\tau)\sigma$ |
|:---:|:---:|:---:|
| 1 | 0.975 | 0.00975 |
| 5 | 0.885 | 0.00885 |
| 10 | 0.787 | 0.00787 |
| 20 | 0.632 | 0.00632 |
| 30 | 0.554 | 0.00554 |

The table confirms that the short rate's influence on yields diminishes with maturity, and that yield volatility declines from nearly $\sigma$ at the short end to roughly $0.55\sigma$ at the 30-year point.

## Simulated Yield Curves

The following code simulates multiple short rate paths and plots the resulting yield curves at a future time $t$, illustrating the single-factor shift property.

```python
def main():
    hw = HullWhite(sigma=0.01, lambd=0.05, P=P_market)
    t, R, M = hw.generate_sample_paths(
        num_paths=7, num_steps=100, T=5, seed=42
    )

    # For each path, compute the yield curve at t = 5
    tau_grid = np.linspace(0.5, 30, 60)
    for path_idx in range(7):
        r_T = R[path_idx, -1]
        yields = []
        for tau in tau_grid:
            P_val = hw.compute_ZCB(5, 5 + tau, r_T)
            y = -np.log(P_val) / tau
            yields.append(y)
        plt.plot(tau_grid, yields, alpha=0.7)

    plt.xlabel("Time to Maturity (years)")
    plt.ylabel("Yield R(5, 5+tau)")
    plt.title("Simulated Yield Curves at t=5: Single-Factor Shifts")
    plt.grid(True)
    plt.show()
```

---

## Summary

In the Hull-White model, the yield curve at time $t$ is an affine function of the short rate $r(t)$ through the relation $R(t,T) = a(\tau,t) + b(\tau)\,r(t)$. The loading function $b(\tau) = (1 - e^{-\lambda\tau})/(\lambda\tau)$ decays from 1 to 0 as maturity increases, producing approximate parallel shifts at the short end and vanishing sensitivity at the long end. This single-factor structure explains the dominant level mode of yield curve movements but cannot independently generate steepening or curvature changes.
