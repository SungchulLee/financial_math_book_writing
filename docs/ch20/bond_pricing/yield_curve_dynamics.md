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

---

## Exercises

**Exercise 1.** Compute the loading function $b(\tau)$ for $\tau = 1, 5, 10, 20, 30$ with $\lambda = 0.03$ and compare with the values in the text (which use $\lambda = 0.05$). How does a smaller mean reversion speed affect the yield curve's sensitivity to short rate changes?

??? success "Solution to Exercise 1"
    With $\lambda = 0.03$, the loading function is $b(\tau) = \frac{1 - e^{-0.03\tau}}{0.03\tau}$.

    | $\tau$ (years) | $b(\tau)$, $\lambda=0.03$ | $b(\tau)$, $\lambda=0.05$ |
    |:---:|:---:|:---:|
    | 1 | $\frac{1-e^{-0.03}}{0.03} = \frac{0.02956}{0.03} = 0.985$ | 0.975 |
    | 5 | $\frac{1-e^{-0.15}}{0.15} = \frac{0.1393}{0.15} = 0.929$ | 0.885 |
    | 10 | $\frac{1-e^{-0.3}}{0.3} = \frac{0.2592}{0.3} = 0.864$ | 0.787 |
    | 20 | $\frac{1-e^{-0.6}}{0.6} = \frac{0.4512}{0.6} = 0.752$ | 0.632 |
    | 30 | $\frac{1-e^{-0.9}}{0.9} = \frac{0.5934}{0.9} = 0.659$ | 0.554 |

    A smaller mean reversion speed ($\lambda = 0.03$ vs. $\lambda = 0.05$) produces higher loading values at every maturity. This means the yield curve is more sensitive to short rate changes across all maturities. Intuitively, weaker mean reversion allows short rate shocks to persist longer, so they propagate more strongly to medium and long-term yields. In the extreme $\lambda \to 0$ (Ho-Lee), $b(\tau) = 1$ for all $\tau$ and the yield curve shifts perfectly in parallel.

---

**Exercise 2.** Prove that $b(\tau) = \frac{1 - e^{-\lambda\tau}}{\lambda\tau}$ is strictly decreasing for $\tau > 0$. (Hint: show that $b'(\tau) < 0$ by differentiating and analyzing the sign.)

??? success "Solution to Exercise 2"
    Compute the derivative of $b(\tau) = \frac{1-e^{-\lambda\tau}}{\lambda\tau}$ with respect to $\tau$:

    $$
    b'(\tau) = \frac{d}{d\tau}\left[\frac{1-e^{-\lambda\tau}}{\lambda\tau}\right] = \frac{\lambda e^{-\lambda\tau} \cdot \lambda\tau - (1-e^{-\lambda\tau}) \cdot \lambda}{(\lambda\tau)^2}
    $$

    $$
    = \frac{\lambda^2\tau\,e^{-\lambda\tau} - \lambda(1-e^{-\lambda\tau})}{\lambda^2\tau^2} = \frac{\lambda\tau\,e^{-\lambda\tau} - 1 + e^{-\lambda\tau}}{\lambda\tau^2}
    $$

    $$
    = \frac{(1+\lambda\tau)e^{-\lambda\tau} - 1}{\lambda\tau^2}
    $$

    We need to show that the numerator $h(x) = (1+x)e^{-x} - 1 < 0$ for $x = \lambda\tau > 0$.

    Note that $h(0) = 0$ and:

    $$
    h'(x) = e^{-x} - (1+x)e^{-x} = -xe^{-x} < 0 \quad\text{for } x > 0
    $$

    Since $h(0) = 0$ and $h'(x) < 0$ for $x > 0$, we conclude $h(x) < 0$ for all $x > 0$.

    Therefore $b'(\tau) < 0$ for all $\tau > 0$, proving that $b(\tau)$ is strictly decreasing.

---

**Exercise 3.** The yield volatility at maturity $\tau$ is $\text{vol}(R(t,T)) = b(\tau)\sigma$. For $\lambda = 0.05$ and $\sigma = 0.01$, compute the yield volatility at $\tau = 2$ and $\tau = 20$. Express the ratio $\text{vol}(R_{20})/\text{vol}(R_2)$ and explain why long-term yields are less volatile than short-term yields.

??? success "Solution to Exercise 3"
    With $\lambda = 0.05$ and $\sigma = 0.01$:

    **At $\tau = 2$:**

    $$
    b(2) = \frac{1 - e^{-0.1}}{0.1} = \frac{1 - 0.9048}{0.1} = \frac{0.0952}{0.1} = 0.952
    $$

    $$
    \text{vol}(R_2) = 0.952 \times 0.01 = 0.00952
    $$

    **At $\tau = 20$:**

    $$
    b(20) = \frac{1 - e^{-1}}{1} = 1 - 0.3679 = 0.632
    $$

    $$
    \text{vol}(R_{20}) = 0.632 \times 0.01 = 0.00632
    $$

    **Ratio:**

    $$
    \frac{\text{vol}(R_{20})}{\text{vol}(R_2)} = \frac{0.632}{0.952} \approx 0.664
    $$

    The 20-year yield volatility is only about 66% of the 2-year yield volatility. Long-term yields are less volatile because mean reversion pulls the short rate back toward its long-run level $\theta(t)$, dampening the effect of current shocks on cumulative future rates. The exponential decay $e^{-\lambda\tau}$ in the loading function captures this dampening: shocks to the short rate today have diminishing influence on the average rate over longer horizons.

---

**Exercise 4.** In principal component analysis of yield curve movements, the first component (level) typically explains 80-90% of total variance. Explain why a single-factor Hull-White model can capture this component. What types of yield curve movements (steepening, butterfly) can it not produce?

??? success "Solution to Exercise 4"
    In principal component analysis (PCA), the first principal component (PC1, "level") captures parallel or near-parallel shifts of the yield curve. Empirically, it explains 80-90% of yield curve variance.

    The Hull-White model produces yield changes $\Delta R(t,T) = b(\tau)\,\Delta r(t)$, where all maturities move in the same direction (since $b(\tau) > 0$), driven by the single shock $\Delta r$. For maturities with $\lambda\tau \ll 1$, $b(\tau) \approx 1$ and the shift is approximately parallel. Even for longer maturities where $b(\tau) < 1$, the movements remain co-directional. This structure closely resembles the empirical level factor.

    **Movements the model cannot produce:**

    - *Steepening/flattening (PC2):* This requires short and long rates to move in opposite directions. Since $b(\tau) > 0$ for all $\tau$, the single-factor model cannot produce opposite movements at different maturities from a single shock.

    - *Butterfly/curvature (PC3):* This requires the intermediate part of the curve to move differently from both the short and long ends (e.g., a "humped" response). A single monotonically decreasing loading function $b(\tau)$ cannot generate such non-monotone patterns.

    Multi-factor models (e.g., two-factor Hull-White with a short rate and a slope factor) introduce additional stochastic drivers with different loading functions, enabling these richer yield curve dynamics.

---

**Exercise 5.** Show that the long yield $\lim_{\tau \to \infty} R(t,T)$ is deterministic (independent of $r(t)$) in the Hull-White model. Why is this a potential limitation for pricing very long-dated derivatives?

??? success "Solution to Exercise 5"
    The yield at maturity $\tau$ is:

    $$
    R(t,T) = a(\tau,t) + b(\tau)\,r(t)
    $$

    As $\tau \to \infty$, the loading function satisfies:

    $$
    b(\tau) = \frac{1-e^{-\lambda\tau}}{\lambda\tau} \to \frac{1}{\lambda\tau} \to 0
    $$

    Therefore:

    $$
    \lim_{\tau\to\infty} R(t,T) = \lim_{\tau\to\infty} a(\tau,t)
    $$

    This limit is deterministic: it depends only on the market curve $P^M(0,\cdot)$ and model parameters $\lambda,\sigma$, but not on the random variable $r(t)$.

    **Limitation for long-dated derivatives:** Since the long yield is deterministic, the model implies that very long-term interest rates have zero volatility. This contradicts empirical evidence: even 30-year yields exhibit meaningful fluctuations. For pricing long-dated derivatives (e.g., 30-year swaptions, long-term guarantees in insurance), the model underestimates uncertainty at the long end. This leads to underpricing of options on long-term rates and understating the risk of long-dated liabilities. Multi-factor models or models with slower mean reversion are needed to capture realistic long-end dynamics.

---

**Exercise 6.** Consider two yield curves simulated at time $t = 5$ from initial short rates $r_1(5) = 0.03$ and $r_2(5) = 0.06$. Using $\lambda = 0.05$, compute the yield difference $R_1(5, 5+\tau) - R_2(5, 5+\tau)$ at $\tau = 1$ and $\tau = 30$. Verify that the difference is proportional to $b(\tau) \times (r_1 - r_2)$.

??? success "Solution to Exercise 6"
    The yield difference at maturity $\tau$ is:

    $$
    R_1(5,5+\tau) - R_2(5,5+\tau) = b(\tau)(r_1(5) - r_2(5)) = b(\tau)(0.03 - 0.06) = -0.03\,b(\tau)
    $$

    **At $\tau = 1$** ($\lambda\tau = 0.05$):

    $$
    b(1) = \frac{1-e^{-0.05}}{0.05} = \frac{0.04877}{0.05} = 0.9754
    $$

    $$
    R_1 - R_2 = -0.03 \times 0.9754 = -0.02926
    $$

    The 1-year yield difference is approximately $-293$ basis points.

    **At $\tau = 30$** ($\lambda\tau = 1.5$):

    $$
    b(30) = \frac{1-e^{-1.5}}{1.5} = \frac{1-0.2231}{1.5} = \frac{0.7769}{1.5} = 0.5179
    $$

    $$
    R_1 - R_2 = -0.03 \times 0.5179 = -0.01554
    $$

    The 30-year yield difference is approximately $-155$ basis points.

    **Verification:** The difference $R_1 - R_2 = b(\tau)(r_1 - r_2)$ is confirmed by the affine structure $R = a(\tau,t) + b(\tau)r$, where $a(\tau,t)$ is the same for both curves (it depends on $t$ and the market curve, not on $r$). The yield difference shrinks with maturity because $b(\tau)$ is decreasing: mean reversion ensures that different short rate realizations converge toward the same long-run level, reducing the spread between yield curves at longer horizons.

---

**Exercise 7.** The two-factor Hull-White extension introduces a second stochastic factor to generate steepening movements. Describe qualitatively how a second factor with fast mean reversion could produce yield curve curvature changes that the single-factor model cannot.

??? success "Solution to Exercise 7"
    In the two-factor Hull-White model, the short rate is decomposed as $r(t) = x(t) + y(t) + \phi(t)$, where $x(t)$ and $y(t)$ are two mean-reverting factors with different speeds $\lambda_x$ and $\lambda_y$, and $\phi(t)$ is a deterministic function for calibration.

    If the second factor $y(t)$ has fast mean reversion ($\lambda_y \gg \lambda_x$), its loading function $b_y(\tau) = \frac{1-e^{-\lambda_y\tau}}{\lambda_y\tau}$ decays rapidly with maturity. This means:

    - At short maturities ($\tau$ small), both $b_x(\tau) \approx 1$ and $b_y(\tau) \approx 1$, so both factors contribute equally.
    - At intermediate maturities, $b_y(\tau)$ has already decayed significantly while $b_x(\tau)$ is still close to 1.
    - At long maturities, both have decayed, but $b_y(\tau) \approx 0$ while $b_x(\tau)$ is still positive.

    A positive shock to $y(t)$ raises short-term yields (where $b_y$ is large) but has little effect on long-term yields (where $b_y \approx 0$). Combined with an offsetting shock to $x(t)$, this can produce a hump-shaped yield curve response: short and long ends move down (driven by negative $\Delta x$) while the intermediate segment moves up (driven by the net effect of $b_y\Delta y - b_x|\Delta x|$ being positive for intermediate $\tau$).

    This non-monotone response across maturities is precisely the butterfly/curvature movement (PC3) that the single-factor model cannot generate. The fast mean-reverting factor acts as a "curvature factor" that primarily affects short-to-intermediate maturities, enabling independent control of the yield curve shape beyond simple level shifts.
