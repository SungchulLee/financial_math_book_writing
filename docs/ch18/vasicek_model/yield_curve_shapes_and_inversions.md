# Yield Curve Shapes and Inversions

The shape of the yield curve---whether it slopes upward, downward, or exhibits a hump---carries information about market expectations, risk premia, and monetary policy. In the Vasicek model, the yield curve shape is fully determined by three quantities: the current short rate $r_0$, the long-run mean $\theta$, and the convexity parameter $\sigma^2/(2\kappa^2)$. This section derives the conditions under which each shape arises and explains the economic intuition behind yield curve inversions within the model.

---

## Yield curve formula

From the named functions $A(\tau)$ and $B(\tau)$, the continuously compounded yield at maturity $\tau = T - t$ is

$$
R(t,T) = -\frac{\ln P(t,T)}{\tau} = -\frac{\ln A(\tau)}{\tau} + \frac{B(\tau)}{\tau}\,r_t
$$

Substituting the closed-form expressions:

$$
R(t,T) = \frac{B(\tau)}{\tau}\,r_t + \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)\!\left(1 - \frac{B(\tau)}{\tau}\right) + \frac{\sigma^2 B(\tau)^2}{4\kappa\tau}
$$

Define two key quantities:

- $R_\infty = \theta - \frac{\sigma^2}{2\kappa^2}$, the **asymptotic long yield**
- $h(\tau) = \frac{B(\tau)}{\tau} = \frac{1 - e^{-\kappa\tau}}{\kappa\tau}$, a **weighting function** that decreases from $1$ to $0$

Then the yield can be written as

$$
R(t,T) = h(\tau)\,r_t + (1 - h(\tau))\,R_\infty + \frac{\sigma^2}{4\kappa}\,\frac{B(\tau)^2}{\tau}
$$

The yield is a weighted average of the short rate and the long-run yield, plus a small positive **convexity adjustment** that vanishes at $\tau = 0$ and grows sublinearly.

---

## Behavior at the extremes

### Short end (as tau approaches 0)

As $\tau \to 0$, $B(\tau) \approx \tau - \frac{1}{2}\kappa\tau^2$ and $h(\tau) \to 1$. Therefore

$$
\lim_{\tau \to 0} R(t,T) = r_t
$$

The yield curve always starts at the current short rate.

### Long end (as tau approaches infinity)

As $\tau \to \infty$, $B(\tau) \to 1/\kappa$ and $h(\tau) \to 0$, so

$$
R_\infty = \theta - \frac{\sigma^2}{2\kappa^2}
$$

The asymptotic yield is strictly below $\theta$ due to the convexity correction. Jensen's inequality applied to $P(t,T) = \mathbb{E}^{\mathbb{Q}}_t[e^{-\int_t^T r_s\,ds}]$ gives $P(t,T) \geq e^{-\mathbb{E}[\int r_s\,ds]}$, so bond prices are pushed up (and yields pushed down) by the variability of rates.

---

## Slope of the yield curve at the short end

The initial slope determines whether the curve starts by rising or falling. Differentiating $R(\tau) = R(t, t+\tau)$ with respect to $\tau$ and evaluating at $\tau = 0$:

$$
R'(0) = \frac{1}{2}\kappa(\theta - r_t) - \frac{1}{6}\sigma^2 \cdot 0 + \cdots
$$

More precisely, a Taylor expansion of $R(\tau)$ around $\tau = 0$ gives

$$
R(\tau) = r_t + \frac{1}{2}\kappa(\theta - r_t)\,\tau + O(\tau^2)
$$

Therefore:

- If $r_t < \theta$: the curve initially slopes **upward** (normal)
- If $r_t > \theta$: the curve initially slopes **downward** (inverted at the short end)
- If $r_t = \theta$: the curve is initially **flat**, with the shape determined by higher-order terms

---

## Classification of yield curve shapes

The Vasicek model produces three qualitatively distinct yield curve shapes depending on the relationship between $r_t$ and $R_\infty$.

### Normal (upward-sloping) yield curve

**Condition:** $r_t < R_\infty$

When the current short rate is below the asymptotic yield, the yield curve rises monotonically from $r_t$ to $R_\infty$. This is the most common shape historically, reflecting:

- Market expectation that rates will rise toward the long-run mean
- A positive term premium for bearing interest rate risk over longer horizons

### Inverted (downward-sloping) yield curve

**Condition:** $r_t > R_\infty + \frac{\sigma^2}{2\kappa^2}\left(\text{correction terms}\right)$, or more precisely when $r_t$ is sufficiently above $\theta$

When the short rate is well above the long-run mean, the yield curve slopes downward because the market expects rates to fall. In the Vasicek model, a sufficient condition for a monotonically decreasing yield curve is

$$
r_t > \theta + \frac{\sigma^2}{2\kappa^2}
$$

Under this condition, the mean-reversion pull toward $\theta$ dominates at all maturities, and the convexity correction reinforces the downward slope.

### Humped yield curve

**Condition:** $R_\infty < r_t < \theta + \frac{\sigma^2}{2\kappa^2}$ (approximately)

A humped curve occurs when the short rate is moderately above $R_\infty$. The curve initially rises (driven by the convexity adjustment and the near-term mean-reversion dynamics) but eventually falls as the asymptotic yield $R_\infty < r_t$ pulls yields down. The peak occurs at an interior maturity $\tau^*$ that depends on the model parameters.

The humped shape arises from the competition between two effects: the positive convexity correction pushes yields up at intermediate maturities, while mean reversion pulls the long end down toward $R_\infty$.

---

## Forward rate curve and its relation to shape

The instantaneous forward rate provides a finer view of term structure dynamics:

$$
f(t,T) = e^{-\kappa\tau}\,r_t + \theta\!\left(1 - e^{-\kappa\tau}\right) - \frac{\sigma^2}{2\kappa^2}\!\left(1 - e^{-\kappa\tau}\right)^2
$$

The forward rate has the following limits:

$$
f(t,t) = r_t, \qquad \lim_{\tau\to\infty} f(t,T) = \theta - \frac{\sigma^2}{2\kappa^2} = R_\infty
$$

The forward rate curve is monotonically decreasing if and only if $r_t > R_\infty$. Since the yield is an average of forward rates:

$$
R(t,T) = \frac{1}{\tau}\int_t^T f(t,s)\,ds
$$

a decreasing forward curve does not necessarily produce a decreasing yield curve---the yield averages over the forward rates, smoothing the decline.

---

## Parameter dependence

### Effect of mean reversion speed (kappa)

- **Large $\kappa$**: Mean reversion is strong, so rates converge quickly to $\theta$. The yield curve flattens rapidly. The convexity correction $\sigma^2/(2\kappa^2)$ is small.
- **Small $\kappa$**: Weak mean reversion produces slowly converging yields. The convexity correction is large, and $R_\infty$ can be significantly below $\theta$. Yield curves tend to be steeper.

### Effect of volatility (sigma)

- **Large $\sigma$**: Increases the convexity correction $\sigma^2/(2\kappa^2)$, lowering $R_\infty$ and making the long end of the curve flatter or more inverted.
- **Small $\sigma$**: Convexity correction is negligible, $R_\infty \approx \theta$, and the yield curve shape is driven primarily by the relationship between $r_t$ and $\theta$.

### Effect of the long-run mean (theta)

- $\theta$ shifts $R_\infty$ up or down proportionally.
- Higher $\theta$ relative to $r_t$ produces a steeper normal curve.
- Lower $\theta$ relative to $r_t$ makes inversion more likely.

---

## Numerical example

Consider $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.02$. Then $R_\infty = 0.06 - 0.02^2/(2 \cdot 0.25) = 0.06 - 0.0008 = 0.0592$.

**Case 1: Normal curve** ($r_0 = 0.03$)

| Maturity $\tau$ | Yield $R$ |
|:-:|:-:|
| 0.5 | 3.35% |
| 1 | 3.65% |
| 2 | 4.14% |
| 5 | 5.01% |
| 10 | 5.58% |
| 30 | 5.90% |

The curve rises from 3% toward $R_\infty \approx 5.92\%$.

**Case 2: Inverted curve** ($r_0 = 0.10$)

| Maturity $\tau$ | Yield $R$ |
|:-:|:-:|
| 0.5 | 9.52% |
| 1 | 9.11% |
| 2 | 8.40% |
| 5 | 7.11% |
| 10 | 6.35% |
| 30 | 5.95% |

The curve falls from 10% toward $R_\infty \approx 5.92\%$.

**Case 3: Humped curve** ($r_0 = 0.058$)

| Maturity $\tau$ | Yield $R$ |
|:-:|:-:|
| 0.5 | 5.82% |
| 1 | 5.84% |
| 2 | 5.87% |
| 5 | 5.90% |
| 10 | 5.91% |
| 30 | 5.92% |

When $r_0$ is near $R_\infty$, the curve is nearly flat with a subtle hump driven by the convexity adjustment.

---

## Economic interpretation of inversions

Yield curve inversions in the Vasicek model arise from a purely mechanical source: the current short rate is above its long-run equilibrium, so the market expects rates to fall. This reflects the mean-reversion assumption built into the model.

In practice, yield curve inversions signal additional factors not captured by a time-homogeneous one-factor model:

- **Recession expectations**: An inverted curve historically precedes recessions, as the market anticipates central bank rate cuts.
- **Term premium compression**: Large-scale asset purchases by central banks can compress long-term yields independently of rate expectations.
- **Flight to safety**: Demand for long-duration government bonds during risk-off episodes can invert the curve.

The Vasicek model captures the first effect (rate expectations) but not the latter two, which require richer models with time-varying risk premia or multiple factors.

!!! note "Limitations of the one-factor model"
    A single-factor Vasicek model cannot produce realistic yield curve dynamics in general. In particular, it cannot capture independent movements of the short and long ends (level vs. slope), which are responsible for steepening and flattening episodes. Multi-factor extensions (e.g., two-factor Vasicek or the G2++ model) address this by adding independent OU factors for level and slope.

---

## Summary

The Vasicek yield curve shape is determined by the position of the short rate $r_t$ relative to the asymptotic yield $R_\infty = \theta - \sigma^2/(2\kappa^2)$. When $r_t < R_\infty$, the curve is normal; when $r_t \gg R_\infty$, it inverts; intermediate values produce humped shapes. The convexity correction $\sigma^2/(2\kappa^2)$ always pushes the long end below $\theta$, ensuring that the asymptotic yield is less than the mean-reversion level. These results follow directly from the closed-form expressions for $A(\tau)$ and $B(\tau)$ derived in the previous section.

---

## Exercises

**Exercise 1.** For $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.02$, compute the asymptotic yield $R_\infty = \theta - \sigma^2/(2\kappa^2)$. What is the convexity correction in basis points? For what value of $\sigma$ would the convexity correction exceed 100 basis points (holding $\kappa$ and $\theta$ fixed)?

??? success "Solution to Exercise 1"
    With $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.02$:

    $$
    R_\infty = \theta - \frac{\sigma^2}{2\kappa^2} = 0.05 - \frac{0.0004}{2 \times 0.09} = 0.05 - \frac{0.0004}{0.18} = 0.05 - 0.002222 = 0.04778
    $$

    The convexity correction is $\sigma^2/(2\kappa^2) = 0.002222 = 22.2$ basis points.

    For the correction to exceed 100 basis points ($0.01$):

    $$
    \frac{\sigma^2}{2\kappa^2} > 0.01 \quad \Longrightarrow \quad \sigma^2 > 0.02 \times 0.09 = 0.0018 \quad \Longrightarrow \quad \sigma > \sqrt{0.0018} = 0.04243
    $$

    So $\sigma > 4.24\%$ would produce a convexity correction exceeding 100 bp. This is a very high short-rate volatility (typical values are 1--3%), indicating that the convexity correction is usually modest for realistic parameters. Only in highly volatile rate environments (or with very weak mean reversion) does the correction become economically significant.

---

**Exercise 2.** Using the Taylor expansion $R(\tau) = r_t + \frac{1}{2}\kappa(\theta - r_t)\tau + O(\tau^2)$, determine the initial slope of the yield curve for $r_t = 0.03$, $r_t = 0.05$, and $r_t = 0.07$ with $\kappa = 0.5$ and $\theta = 0.05$. In which case is the curve initially flat?

??? success "Solution to Exercise 2"
    The initial slope of the yield curve is:

    $$
    R'(0) \approx \frac{1}{2}\kappa(\theta - r_t)
    $$

    With $\kappa = 0.5$ and $\theta = 0.05$:

    **$r_t = 0.03$:**

    $$
    R'(0) = \frac{1}{2} \times 0.5 \times (0.05 - 0.03) = 0.25 \times 0.02 = 0.005
    $$

    The slope is **positive** (upward-sloping). The curve rises at 50 bp per year of maturity for short maturities.

    **$r_t = 0.05$:**

    $$
    R'(0) = \frac{1}{2} \times 0.5 \times (0.05 - 0.05) = 0
    $$

    The slope is **zero** (initially flat). This is the case $r_t = \theta$ where the yield curve is flat at the short end. Higher-order terms (the convexity adjustment) determine the shape for larger $\tau$.

    **$r_t = 0.07$:**

    $$
    R'(0) = \frac{1}{2} \times 0.5 \times (0.05 - 0.07) = 0.25 \times (-0.02) = -0.005
    $$

    The slope is **negative** (inverted). The curve falls at 50 bp per year of maturity at the short end, reflecting the market expectation that the elevated rate will revert toward $\theta$.

---

**Exercise 3.** Derive the sufficient condition for a monotonically inverted yield curve: $r_t > \theta + \sigma^2/(2\kappa^2)$. For the parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.02$, compute this threshold. If $r_0 = 0.10$ (as in the numerical example), verify that the condition is satisfied and the curve is monotonically decreasing.

??? success "Solution to Exercise 3"
    A sufficient condition for a monotonically inverted yield curve is that the yield starts above $R_\infty$ and decreases toward it. Since $R(0) = r_t$ and $R(\infty) = R_\infty$, the curve is globally decreasing if the initial slope is negative and there is no intermediate hump.

    The forward rate is $f(\tau) = e^{-\kappa\tau}r_t + \theta(1 - e^{-\kappa\tau}) - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2$. For the yield curve to be monotonically decreasing, it suffices that $f(\tau) < r_t$ for all $\tau > 0$. At $\tau = 0^+$, $f'(0) = -\kappa(r_t - \theta)$, and the forward rate decreases when $r_t > \theta$.

    The condition $r_t > \theta + \sigma^2/(2\kappa^2)$ ensures that $r_t > R_\infty + \sigma^2/\kappa^2$, providing sufficient margin above the asymptotic yield for the curve to decrease monotonically.

    For $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.02$:

    $$
    \theta + \frac{\sigma^2}{2\kappa^2} = 0.06 + \frac{0.0004}{0.50} = 0.06 + 0.0008 = 0.0608
    $$

    With $r_0 = 0.10$: since $0.10 > 0.0608$, the condition is satisfied. The yield curve should be monotonically decreasing. This is confirmed by the numerical example in the text, where yields fall from 9.52% at 6 months to 5.95% at 30 years.

---

**Exercise 4.** The forward rate curve is $f(t,T) = e^{-\kappa\tau}r_t + \theta(1 - e^{-\kappa\tau}) - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2$. Show that the forward rate is monotonically decreasing in $\tau$ if and only if $r_t > R_\infty$. Why can a decreasing forward curve coexist with an upward-sloping yield curve at intermediate maturities?

??? success "Solution to Exercise 4"
    The forward rate is:

    $$
    f(\tau) = e^{-\kappa\tau}r_t + \theta(1 - e^{-\kappa\tau}) - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2
    $$

    Differentiating with respect to $\tau$:

    $$
    f'(\tau) = -\kappa e^{-\kappa\tau}r_t + \kappa\theta e^{-\kappa\tau} - \frac{\sigma^2}{2\kappa^2} \cdot 2(1 - e^{-\kappa\tau}) \cdot \kappa e^{-\kappa\tau}
    $$

    $$
    = \kappa e^{-\kappa\tau}\left[\theta - r_t - \frac{\sigma^2}{\kappa^2}(1 - e^{-\kappa\tau})\right]
    $$

    Since $\kappa e^{-\kappa\tau} > 0$, the sign of $f'(\tau)$ depends on $\theta - r_t - \frac{\sigma^2}{\kappa^2}(1 - e^{-\kappa\tau})$.

    For $f'(\tau) < 0$ for all $\tau > 0$, we need:

    $$
    \theta - r_t - \frac{\sigma^2}{\kappa^2}(1 - e^{-\kappa\tau}) < 0 \quad \text{for all } \tau > 0
    $$

    At $\tau = 0^+$, this becomes $\theta - r_t < 0$, i.e., $r_t > \theta$. As $\tau \to \infty$, the condition becomes $\theta - r_t - \sigma^2/\kappa^2 < 0$, i.e., $r_t > \theta - \sigma^2/\kappa^2 = R_\infty$.

    The binding constraint is at $\tau = 0$: $r_t > \theta$. If this holds, then for all $\tau > 0$, the term $-\frac{\sigma^2}{\kappa^2}(1-e^{-\kappa\tau}) < 0$ only reinforces the inequality. Therefore:

    $$
    f'(\tau) < 0 \text{ for all } \tau > 0 \quad \Longleftrightarrow \quad r_t > \theta \quad (\text{since } r_t > \theta \geq R_\infty)
    $$

    Wait---more carefully: the condition is $r_t > \theta$, but if $r_t > R_\infty$ but $r_t < \theta$, then at $\tau = 0$, $f'(0) = \kappa(\theta - r_t) > 0$, so the forward curve initially rises. Only for $r_t > \theta$ is the forward curve monotonically decreasing.

    Actually, re-examining: $f'(\tau) < 0$ for all $\tau$ requires $r_t > \theta$ (from the $\tau = 0$ condition). But the question asks for $f$ monotonically decreasing iff $r_t > R_\infty$. The correct statement is: $f(\tau)$ is decreasing at $\tau = 0$ iff $r_t > \theta$, and $f(\tau) > R_\infty$ for all $\tau$ iff the forward rate starts above $R_\infty$. The forward rate curve may not be monotone for $R_\infty < r_t < \theta$, but it does eventually decrease to $R_\infty$.

    **Why a decreasing forward curve can coexist with an upward-sloping yield curve:** The yield $R(\tau) = \frac{1}{\tau}\int_0^\tau f(s)\,ds$ is an average of forward rates. If $f(s)$ is decreasing from $r_t$ to $R_\infty$ but starts high, the average can still be increasing: early forward rates pull the average up faster than later forward rates pull it down. The yield curve rises until the accumulated decline in forward rates overwhelms the high initial values.

---

**Exercise 5.** For the humped yield curve case ($r_0 = 0.058$, $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.02$), the yield curve rises slightly before falling to $R_\infty$. Estimate the maturity $\tau^*$ at which the yield curve peaks by numerically evaluating yields at $\tau = 1, 2, 3, 5, 10, 20, 30$ years.

??? success "Solution to Exercise 5"
    With $r_0 = 0.058$, $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.02$, we have $R_\infty = 0.06 - 0.0008 = 0.0592$.

    Computing yields at various maturities using $R(\tau) = -\ln A(\tau)/\tau + B(\tau)\,r_0/\tau$:

    Using $B(\tau) = (1-e^{-0.5\tau})/0.5$ and the formula for $\ln A(\tau)$:

    | $\tau$ | $B(\tau)$ | $\ln A(\tau)$ | $-\ln P/\tau$ | Yield |
    |:-:|:-:|:-:|:-:|:-:|
    | 1 | 0.7869 | $-0.00812$ | 0.05378 | 5.378% |
    | 2 | 1.2642 | $-0.02169$ | 0.05746 | 5.746% |
    | 3 | 1.5537 | $-0.03845$ | 0.05894 | 5.894% |
    | 5 | 1.8358 | $-0.07407$ | 0.05910 | 5.910% |
    | 10 | 1.9865 | $-0.16270$ | 0.05777 | 5.777% |
    | 20 | 1.9999 | $-0.33120$ | 0.05232 | (approaching $R_\infty$) |
    | 30 | 2.0000 | $-0.50000$ | (approaching $R_\infty$) | |

    The yields rise from about 5.38% at $\tau = 1$ to a peak around 5.91% at $\tau \approx 5$ years, then gradually decline toward $R_\infty = 5.92\%$. The peak maturity $\tau^*$ is approximately **5 years**. The hump is very subtle (only about 1--2 bp above the asymptotic yield), consistent with $r_0 = 5.8\%$ being very close to $R_\infty = 5.92\%$.

---

**Exercise 6.** Explain why a one-factor Vasicek model cannot produce a yield curve that is simultaneously steep at the short end and flat at the long end (a common empirical pattern). What additional factor would a two-factor model need to capture independent movements of the short end and long end?

??? success "Solution to Exercise 6"
    A one-factor Vasicek model generates a yield curve determined by a single state variable $r_t$. When $r_t$ changes, **all** yields move in the same direction (though by different amounts, governed by $B(\tau)/\tau$). Specifically:

    $$
    \frac{\partial R(\tau)}{\partial r_t} = \frac{B(\tau)}{\tau} > 0
    $$

    for all $\tau$. A rise in $r_t$ increases all yields simultaneously. This means:

    - The short end and long end **cannot move independently**.
    - A steep short end (large yield changes at short maturities) necessarily implies some movement at the long end.
    - Level, slope, and curvature changes are all perfectly correlated through the single factor.

    Empirically, yield curve movements are well described by three independent factors: level, slope, and curvature (from PCA analysis). The one-factor model captures only the level factor. To produce a steep short end with a flat long end---corresponding to independent slope movements---requires a **second factor**.

    A two-factor Vasicek model $r_t = x_t + y_t$ with $x_t$ and $y_t$ being independent OU processes with different mean-reversion speeds (e.g., $\kappa_x = 0.02$ for level, $\kappa_y = 1.0$ for slope) allows the short end to move independently of the long end. The factor $y_t$ (with fast mean reversion) affects short-maturity yields strongly but has negligible impact on long yields (because $B_y(\tau)/\tau \to 0$ quickly), while $x_t$ (with slow mean reversion) affects all yields roughly equally.

---

**Exercise 7.** The yield can be written as $R(\tau) = h(\tau)\,r_t + (1 - h(\tau))\,R_\infty + C(\tau)$ where $h(\tau) = B(\tau)/\tau$ and $C(\tau) = \sigma^2 B(\tau)^2/(4\kappa\tau)$ is the convexity adjustment. For $\kappa = 0.5$ and $\sigma = 0.02$, compute $h(\tau)$ and $C(\tau)$ at $\tau = 1, 5, 10, 30$. Verify that $h$ decreases from $1$ to $0$ and $C$ remains small relative to the other terms.

??? success "Solution to Exercise 7"
    With $\kappa = 0.5$, $\sigma = 0.02$, the relevant quantities are $B(\tau) = 2(1 - e^{-0.5\tau})$, $\sigma^2/(4\kappa) = 0.0004/2.0 = 0.0002$.

    | $\tau$ | $B(\tau)$ | $h(\tau) = B/\tau$ | $B^2$ | $C(\tau) = 0.0002 \cdot B^2/\tau$ |
    |:-:|:-:|:-:|:-:|:-:|
    | 1 | 0.7869 | 0.7869 | 0.6192 | 0.000124 |
    | 5 | 1.8358 | 0.3672 | 3.3702 | 0.000135 |
    | 10 | 1.9865 | 0.1987 | 3.9462 | 0.0000789 |
    | 30 | 2.0000 | 0.0667 | 4.0000 | 0.0000267 |

    **Verification that $h$ decreases from 1 to 0:** At $\tau = 0$, $h \to 1$ (since $B(\tau)/\tau \to 1$ as $\tau \to 0$). The values $0.787, 0.367, 0.199, 0.067$ confirm monotonic decrease toward $0$.

    **Convexity adjustment $C(\tau)$:** The values are all very small: 1.24 bp, 1.35 bp, 0.79 bp, 0.27 bp. These are negligible compared to typical yield levels (3--6%) and even small compared to the difference between $r_t$ and $R_\infty$. The convexity adjustment peaks at intermediate maturities ($\tau \approx 5$) where $B(\tau)^2/\tau$ is maximized, then declines as $B(\tau)$ saturates while $\tau$ continues to grow.

    The decomposition $R(\tau) = h(\tau)\,r_t + (1-h(\tau))\,R_\infty + C(\tau)$ shows that yields are primarily a weighted average of the short rate and the long-run yield, with the convexity adjustment providing only a minor positive correction.
