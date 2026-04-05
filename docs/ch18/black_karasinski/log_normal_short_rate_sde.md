# Log-Normal Short Rate SDE

The Black-Karasinski (BK) model, introduced by Fischer Black and Piotr Karasinski in 1991, specifies the dynamics of the logarithm of the short rate rather than the short rate itself. This seemingly small modeling choice has profound consequences: rates are guaranteed to be positive (since the exponential of any real number is positive), the model can fit the initial term structure exactly through a time-dependent drift, and the resulting rate distribution is log-normal rather than normal. However, these advantages come at the cost of analytical tractability --- the BK model is not affine, and no closed-form bond price formula exists. This section defines the BK SDE, derives the short rate dynamics via Ito's lemma, characterizes the conditional distribution, and compares the structure with Vasicek and Hull-White.

---

## The Black-Karasinski SDE

The BK model specifies the risk-neutral dynamics of $x_t = \ln r_t$ as a mean-reverting Ornstein-Uhlenbeck process with time-dependent coefficients:

$$
dx_t = \left[\theta(t) - a(t)\,x_t\right]dt + \sigma(t)\,dW_t^{\mathbb{Q}}
$$

where:

- $x_t = \ln r_t$ is the log short rate
- $\theta(t)$ is the time-dependent drift function, calibrated to fit the initial term structure
- $a(t) > 0$ is the speed of mean reversion (may be time-dependent or constant)
- $\sigma(t) > 0$ is the volatility of the log rate
- $W_t^{\mathbb{Q}}$ is a standard Brownian motion under the risk-neutral measure

In the constant-parameter version (most common in practice), $a(t) = a$ and $\sigma(t) = \sigma$ are constants, while $\theta(t)$ remains time-dependent for term structure fitting:

$$
dx_t = \left[\theta(t) - a\,x_t\right]dt + \sigma\,dW_t^{\mathbb{Q}}
$$

The short rate is recovered by $r_t = e^{x_t}$.

!!! note "Notation comparison"
    Some references write the BK SDE as $d(\ln r_t) = [\theta(t) - a\ln r_t]\,dt + \sigma\,dW_t$, which is identical. The log-rate formulation emphasizes that $\ln r_t$ is the fundamental state variable, while $r_t$ is derived from it.

---

## Derivation of the short rate dynamics

To understand the dynamics of $r_t = e^{x_t}$, apply Ito's lemma to the function $r = e^x$:

$$
dr_t = e^{x_t}\,dx_t + \frac{1}{2}e^{x_t}(dx_t)^2
$$

Since $(dx_t)^2 = \sigma^2\,dt$:

$$
dr_t = r_t\left[\theta(t) - a\,\ln r_t + \frac{1}{2}\sigma^2\right]dt + \sigma\,r_t\,dW_t^{\mathbb{Q}}
$$

This reveals several important features:

1. **Multiplicative noise**: The diffusion coefficient is $\sigma r_t$, making the volatility proportional to the level. This is the same multiplicative structure as geometric Brownian motion.

2. **State-dependent drift**: The drift contains $\ln r_t$, which is nonlinear in $r_t$. This nonlinearity is the source of the non-affine structure.

3. **Guaranteed positivity**: Since $r_t = e^{x_t}$ and $x_t$ can take any real value, $r_t > 0$ always. No boundary conditions or Feller-type conditions are needed.

---

## Conditional distribution of the log rate

Since $x_t = \ln r_t$ follows a linear (Ornstein-Uhlenbeck) SDE, its conditional distribution is Gaussian. Given $x_s$ at time $s < t$, with constant parameters $a$ and $\sigma$:

$$
x_t \mid x_s \sim \mathcal{N}\!\left(\mu(s,t),\;\nu^2(s,t)\right)
$$

where the conditional mean and variance are

$$
\mu(s,t) = x_s\,e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta(u)\,du
$$

$$
\nu^2(s,t) = \frac{\sigma^2}{2a}\left(1 - e^{-2a(t-s)}\right)
$$

The short rate $r_t = e^{x_t}$ is therefore **log-normally distributed** conditional on $\mathcal{F}_s$:

$$
r_t \mid r_s \sim \text{LogNormal}\!\left(\mu(s,t),\;\nu^2(s,t)\right)
$$

with conditional moments

$$
\mathbb{E}[r_t\,|\,r_s] = \exp\!\left(\mu(s,t) + \frac{\nu^2(s,t)}{2}\right)
$$

$$
\text{Var}(r_t\,|\,r_s) = \exp\!\left(2\mu(s,t) + \nu^2(s,t)\right)\left(e^{\nu^2(s,t)} - 1\right)
$$

!!! tip "Log-normal vs normal rates"
    The log-normal distribution assigns zero probability to negative rates (desirable) but has a heavier right tail than the normal distribution. Empirically, interest rate distributions often exhibit right skewness, making the log-normal assumption a reasonable first approximation, especially for emerging market rates or during periods of high rates.

---

## Long-run behavior

With constant parameters, the long-run distribution of $x_t$ as $t \to \infty$ is

$$
x_\infty \sim \mathcal{N}\!\left(\frac{\theta}{a},\;\frac{\sigma^2}{2a}\right)
$$

where we have assumed $\theta(t) = \theta$ is constant for this analysis. The long-run short rate distribution is therefore

$$
r_\infty \sim \text{LogNormal}\!\left(\frac{\theta}{a},\;\frac{\sigma^2}{2a}\right)
$$

with long-run mean

$$
\mathbb{E}[r_\infty] = \exp\!\left(\frac{\theta}{a} + \frac{\sigma^2}{4a}\right)
$$

The long-run mean rate increases with volatility (through the $\sigma^2/4a$ correction), reflecting the Jensen's inequality effect inherent in the exponential transformation.

---

## Comparison with other short-rate models

| Feature | Vasicek | Hull-White | CIR | Black-Karasinski |
|---------|---------|------------|-----|------------------|
| **SDE variable** | $r_t$ | $r_t$ | $r_t$ | $\ln r_t$ |
| **Drift** | $\kappa(\theta - r)$ | $\theta(t) - ar$ | $\kappa(\theta - r)$ | $\theta(t) - a\ln r$ |
| **Diffusion** | $\sigma$ | $\sigma$ | $\sigma\sqrt{r}$ | $\sigma r$ (for $r_t$) |
| **Rate distribution** | Normal | Normal | Non-central $\chi^2$ | Log-normal |
| **Negative rates** | Possible | Possible | No (Feller) | Impossible |
| **Affine** | Yes | Yes | Yes | No |
| **Closed-form ZCB** | Yes | Yes | Yes | No |
| **Exact term structure fit** | No | Yes | No | Yes |

The BK model occupies a unique position: it guarantees positive rates (like CIR) and fits the initial term structure exactly (like Hull-White), but sacrifices analytical tractability (unlike all three competitors).

---

## The role of the time-dependent drift

The function $\theta(t)$ is chosen so that the model reproduces the observed initial term structure of interest rates. Given market discount factors $P^{\text{mkt}}(0,T)$, the condition

$$
P^{\text{mkt}}(0,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_0^T r_s\,ds\right)\right]
$$

implicitly determines $\theta(t)$. Unlike the Hull-White model where $\theta(t)$ can be solved in closed form, the BK model requires a numerical procedure --- typically a trinomial tree or forward-induction algorithm --- to extract $\theta(t)$ from market data.

---

## Summary

The Black-Karasinski model specifies the log short rate $x_t = \ln r_t$ as a mean-reverting process $dx_t = [\theta(t) - ax_t]\,dt + \sigma\,dW_t$, making $r_t = e^{x_t}$ strictly positive and log-normally distributed. Ito's lemma reveals that the short rate dynamics $dr_t = r_t[\theta(t) - a\ln r_t + \frac{1}{2}\sigma^2]\,dt + \sigma r_t\,dW_t$ have a nonlinear drift ($\ln r$ term), which destroys the affine structure and prevents closed-form bond pricing. The time-dependent drift $\theta(t)$ enables exact calibration to the initial term structure, compensating for the loss of analytical tractability. The conditional log-normal distribution of $r_t$ guarantees non-negative rates, making the BK model particularly suitable for environments where negative rates are economically unreasonable.

---

## Exercises

**Exercise 1.** Starting from the BK log-rate SDE $dx_t = [\theta(t) - ax_t]\,dt + \sigma\,dW_t$ and the transformation $r_t = e^{x_t}$, apply Ito's lemma step-by-step to derive the short rate dynamics

$$
dr_t = r_t\left[\theta(t) - a\ln r_t + \tfrac{1}{2}\sigma^2\right]dt + \sigma\,r_t\,dW_t
$$

Identify each term in the Ito expansion and explain why the $\frac{1}{2}\sigma^2$ correction appears.

??? success "Solution to Exercise 1"
    We start with $r_t = e^{x_t}$ where $dx_t = [\theta(t) - ax_t]\,dt + \sigma\,dW_t$. Apply Ito's lemma to $r_t = f(x_t) = e^{x_t}$.

    **Step 1**: Compute the required derivatives of $f(x) = e^x$:

    $$
    f'(x) = e^x, \qquad f''(x) = e^x
    $$

    **Step 2**: Apply Ito's formula $dr_t = f'(x_t)\,dx_t + \frac{1}{2}f''(x_t)(dx_t)^2$:

    $$
    dr_t = e^{x_t}\,dx_t + \frac{1}{2}e^{x_t}(dx_t)^2
    $$

    **Step 3**: Compute $(dx_t)^2$. Since $dx_t = [\theta(t) - ax_t]\,dt + \sigma\,dW_t$, the Ito multiplication rules ($dt \cdot dt = 0$, $dt \cdot dW = 0$, $dW \cdot dW = dt$) give

    $$
    (dx_t)^2 = \sigma^2\,dt
    $$

    **Step 4**: Substitute $dx_t$ and $(dx_t)^2$:

    $$
    dr_t = e^{x_t}\left\{[\theta(t) - ax_t]\,dt + \sigma\,dW_t\right\} + \frac{1}{2}e^{x_t}\sigma^2\,dt
    $$

    **Step 5**: Replace $e^{x_t} = r_t$ and $x_t = \ln r_t$, and combine the $dt$ terms:

    $$
    dr_t = r_t\left[\theta(t) - a\ln r_t + \frac{1}{2}\sigma^2\right]dt + \sigma\,r_t\,dW_t
    $$

    The $\frac{1}{2}\sigma^2$ correction is the **Ito correction term**, arising from the second-order term $\frac{1}{2}f''(x)(dx)^2$ in Ito's lemma. It reflects the curvature (convexity) of the exponential function: since $e^x$ is convex, the average of $e^{x_t}$ over small fluctuations exceeds $e^{\mathbb{E}[x_t]}$, and this convexity bias appears as an additional upward drift of $\frac{1}{2}\sigma^2 r_t$ in the dynamics of $r_t$.

---

**Exercise 2.** Suppose the BK model has constant parameters $a = 0.10$, $\sigma = 0.20$, and the current log rate is $x_0 = \ln(0.05)$. Assume $\theta(t) = \theta = -0.25$ (constant for simplicity). Compute the conditional mean $\mu(0,5)$ and variance $\nu^2(0,5)$ of $x_5 = \ln r_5$. Then find the expected short rate $\mathbb{E}[r_5]$ and the probability $\mathbb{P}(r_5 > 0.10)$.

??? success "Solution to Exercise 2"
    With $a = 0.10$, $\sigma = 0.20$, $x_0 = \ln(0.05) \approx -2.9957$, and $\theta = -0.25$:

    **Conditional mean** of $x_5$:

    $$
    \mu(0,5) = x_0 e^{-a \cdot 5} + \frac{\theta}{a}(1 - e^{-a \cdot 5})
    $$

    $$
    = (-2.9957) e^{-0.5} + \frac{-0.25}{0.10}(1 - e^{-0.5})
    $$

    $$
    = (-2.9957)(0.6065) + (-2.5)(1 - 0.6065)
    $$

    $$
    = -1.8164 + (-2.5)(0.3935)
    $$

    $$
    = -1.8164 - 0.9838 = -2.8002
    $$

    **Conditional variance** of $x_5$:

    $$
    \nu^2(0,5) = \frac{\sigma^2}{2a}(1 - e^{-2a \cdot 5}) = \frac{0.04}{0.20}(1 - e^{-1.0}) = 0.20 \times 0.6321 = 0.1264
    $$

    **Expected short rate**:

    $$
    \mathbb{E}[r_5] = \exp\!\left(\mu + \frac{\nu^2}{2}\right) = \exp(-2.8002 + 0.0632) = \exp(-2.7370) = 0.0648
    $$

    So $\mathbb{E}[r_5] \approx 6.48\%$.

    **Probability** $\mathbb{P}(r_5 > 0.10)$: Since $r_5 > 0.10$ if and only if $x_5 > \ln(0.10) = -2.3026$:

    $$
    \mathbb{P}(r_5 > 0.10) = \mathbb{P}\!\left(\frac{x_5 - \mu}{\nu} > \frac{-2.3026 - (-2.8002)}{\sqrt{0.1264}}\right)
    $$

    $$
    = \mathbb{P}\!\left(Z > \frac{0.4976}{0.3555}\right) = \mathbb{P}(Z > 1.3996) = 1 - \Phi(1.40) \approx 0.0808
    $$

    There is approximately an 8.1% probability that the short rate exceeds 10% in 5 years.

---

**Exercise 3.** Using the long-run distribution formula, show that the long-run mean rate $\mathbb{E}[r_\infty]$ is strictly greater than $e^{\theta/a}$ when $\sigma > 0$. Interpret this gap in terms of Jensen's inequality applied to the convex function $e^x$. For $\theta/a = \ln(0.05)$ and $\sigma^2/(2a) = 0.04$, compute both $e^{\theta/a}$ and $\mathbb{E}[r_\infty]$.

??? success "Solution to Exercise 3"
    The long-run mean rate is

    $$
    \mathbb{E}[r_\infty] = \exp\!\left(\frac{\theta}{a} + \frac{\sigma^2}{4a}\right)
    $$

    while $e^{\theta/a}$ is the exponential of the long-run mean of the log rate. The difference is

    $$
    \mathbb{E}[r_\infty] = e^{\theta/a} \cdot e^{\sigma^2/(4a)}
    $$

    Since $\sigma > 0$ implies $\sigma^2/(4a) > 0$, we have $e^{\sigma^2/(4a)} > 1$, and therefore $\mathbb{E}[r_\infty] > e^{\theta/a}$.

    **Jensen's inequality interpretation**: For the convex function $g(x) = e^x$ and the random variable $x_\infty \sim \mathcal{N}(\theta/a, \sigma^2/(2a))$:

    $$
    \mathbb{E}[e^{x_\infty}] > e^{\mathbb{E}[x_\infty]} = e^{\theta/a}
    $$

    The gap $e^{\sigma^2/(4a)} - 1$ is the multiplicative "convexity correction" that arises because the exponential function amplifies upward deviations of $x_\infty$ more than it dampens downward deviations. Higher volatility ($\sigma$) widens the distribution of $x_\infty$, increasing this convexity effect. Stronger mean reversion ($a$) compresses the long-run variance $\sigma^2/(2a)$, reducing the gap.

    **Numerical computation** with $\theta/a = \ln(0.05) \approx -2.9957$ and $\sigma^2/(2a) = 0.04$:

    $$
    e^{\theta/a} = e^{-2.9957} = 0.05
    $$

    $$
    \mathbb{E}[r_\infty] = \exp\!\left(-2.9957 + \frac{0.04}{2}\right) = \exp(-2.9757) = 0.05101
    $$

    The long-run mean rate is $5.101\%$, which is $0.101\%$ (about 10 basis points) higher than the "naive" value of $5\%$. The convexity correction is $e^{0.02} - 1 \approx 2.02\%$ of the naive value.

---

**Exercise 4.** In the comparison table, the CIR model has diffusion $\sigma\sqrt{r}$ while the BK model has effective diffusion $\sigma r$ for the short rate. For a given rate level $r_0 = 5\%$, $\sigma_{CIR} = 0.05$, and $\sigma_{BK} = 0.20$, compute the instantaneous standard deviation of rate changes $dW$ for each model. At what rate level $r^*$ do the two models produce the same instantaneous volatility?

??? success "Solution to Exercise 4"
    **CIR instantaneous volatility**: The diffusion coefficient is $\sigma_{CIR}\sqrt{r_0}$:

    $$
    \text{SD}_{CIR} = \sigma_{CIR}\sqrt{r_0} = 0.05 \times \sqrt{0.05} = 0.05 \times 0.2236 = 0.01118
    $$

    **BK instantaneous volatility**: The diffusion coefficient (for the short rate $r_t$) is $\sigma_{BK} r_0$:

    $$
    \text{SD}_{BK} = \sigma_{BK} \cdot r_0 = 0.20 \times 0.05 = 0.01000
    $$

    At $r_0 = 5\%$, the CIR model produces slightly higher instantaneous rate volatility (1.118% vs 1.000%).

    **Equal volatility level** $r^*$: We need $\sigma_{CIR}\sqrt{r^*} = \sigma_{BK} \cdot r^*$:

    $$
    \sigma_{CIR}\sqrt{r^*} = \sigma_{BK}\,r^*
    $$

    Dividing both sides by $\sqrt{r^*}$ (assuming $r^* > 0$):

    $$
    \sigma_{CIR} = \sigma_{BK}\sqrt{r^*}
    $$

    $$
    r^* = \left(\frac{\sigma_{CIR}}{\sigma_{BK}}\right)^2 = \left(\frac{0.05}{0.20}\right)^2 = 0.0625 = 6.25\%
    $$

    At $r^* = 6.25\%$, both models produce the same instantaneous volatility. For $r < 6.25\%$, CIR has higher volatility (since $\sqrt{r}$ decays slower than $r$ as $r \to 0$). For $r > 6.25\%$, BK has higher volatility (since $r$ grows faster than $\sqrt{r}$). This reflects the fundamental difference in their diffusion scaling: CIR's square-root scaling is intermediate between BK's linear scaling and Hull-White's constant scaling.

---

**Exercise 5.** Explain why the nonlinearity $\ln r_t$ in the drift of the BK short-rate SDE destroys the affine structure. Recall that a model is affine if the zero-coupon bond price takes the form $P(t,T) = \exp(A(t,T) + B(t,T)\,r_t)$. Substitute the BK dynamics into the PDE for $P(t,T)$ and show that the resulting equation cannot be separated into functions of $r$ and $t$ alone.

??? success "Solution to Exercise 5"
    A model is affine if the bond price takes the form $P(t,T) = \exp(A(t,T) + B(t,T)\,r_t)$. Substituting this into the bond pricing PDE, the ansatz works if the PDE separates into terms that depend only on $r$ through powers $r^0$ and $r^1$ (i.e., affine in $r$).

    For the BK model, the bond pricing PDE in the $r$-variable is

    $$
    f_t + r\!\left[\theta(t) - a\ln r + \frac{1}{2}\sigma^2\right]f_r + \frac{1}{2}\sigma^2 r^2 f_{rr} - rf = 0
    $$

    Substituting $f = e^{A + Br}$, we get $f_r = Bf$ and $f_{rr} = B^2 f$. Dividing through by $f$:

    $$
    \dot{A} + \dot{B}r + r\!\left[\theta(t) - a\ln r + \frac{1}{2}\sigma^2\right]B + \frac{1}{2}\sigma^2 r^2 B^2 - r = 0
    $$

    This equation contains:

    - **$r\ln r$ term**: from the drift, producing $-aBr\ln r$. This is neither constant nor linear in $r$ --- it is a transcendental function of $r$ that cannot be expressed as $\alpha_0 + \alpha_1 r$ for any constants.
    - **$r^2$ term**: from the diffusion, producing $\frac{1}{2}\sigma^2 B^2 r^2$. This is quadratic in $r$, not affine.

    For the equation to hold for all $r > 0$, every distinct functional form of $r$ must vanish independently. But $r\ln r$ and $r^2$ are linearly independent from $1$ and $r$ as functions of $r$. There are only two free functions $A(t,T)$ and $B(t,T)$ to absorb terms, but there are at least four independent functional forms ($1$, $r$, $r\ln r$, $r^2$). The system is overdetermined and has no solution. The nonlinearity $\ln r$ in the drift destroys the affine structure by introducing a functional dependence on $r$ that cannot be matched by any finite set of ODEs for $A$ and $B$.

---

**Exercise 6.** The conditional variance of the log rate is $\nu^2(s,t) = \frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})$. Analyze the behavior of $\nu^2$ in two limits: (i) $a \to 0$ (no mean reversion) and (ii) $a \to \infty$ (very strong mean reversion). Interpret each limit economically in terms of rate uncertainty over long horizons.

??? success "Solution to Exercise 6"
    The conditional variance of the log rate is $\nu^2(s,t) = \frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})$.

    **(i) Limit $a \to 0$ (no mean reversion)**:

    Using the Taylor expansion $e^{-2a\tau} \approx 1 - 2a\tau + 2a^2\tau^2 - \cdots$ where $\tau = t - s$:

    $$
    \nu^2 = \frac{\sigma^2}{2a}(1 - 1 + 2a\tau - 2a^2\tau^2 + \cdots) = \sigma^2\tau - \sigma^2 a\tau^2 + \cdots
    $$

    In the limit $a \to 0$:

    $$
    \nu^2 \to \sigma^2(t - s)
    $$

    This is the variance of a standard Brownian motion with volatility $\sigma$. Without mean reversion, the log rate diffuses freely, and uncertainty grows linearly without bound as the horizon increases. Economically, this means there is no long-run anchor for interest rates --- they can drift arbitrarily far from their current level, and the uncertainty about future rates never stabilizes.

    **(ii) Limit $a \to \infty$ (very strong mean reversion)**:

    As $a \to \infty$, $e^{-2a\tau} \to 0$ for any fixed $\tau > 0$, so

    $$
    \nu^2 \to \frac{\sigma^2}{2a} \to 0
    $$

    The variance vanishes. With infinitely strong mean reversion, the log rate is pulled instantaneously to its long-run mean $\theta/a$, and there is no residual uncertainty. Economically, this corresponds to a perfectly anchored rate: the central bank (or market forces) enforces a fixed rate with no fluctuation. The short rate behaves deterministically in this limit.

    For finite but large $a$, the variance saturates quickly at $\sigma^2/(2a)$ (the long-run variance), which is small. This means rate uncertainty reaches its maximum rapidly and stays bounded --- consistent with a strongly mean-reverting economy where rates deviate from the target only briefly.

---

**Exercise 7.** The time-dependent drift $\theta(t)$ is determined implicitly by the condition $P^{\text{mkt}}(0,T) = \mathbb{E}^{\mathbb{Q}}[\exp(-\int_0^T r_s\,ds)]$. Explain why, unlike in the Hull-White model, this equation cannot be solved for $\theta(t)$ in closed form. What specific mathematical property of the expectation $\mathbb{E}^{\mathbb{Q}}[\exp(-\int_0^T e^{x_s}\,ds)]$ prevents analytical inversion?

??? success "Solution to Exercise 7"
    In the Hull-White model, $r_s$ is Gaussian, so the integral $Y = \int_0^T r_s\,ds$ is a sum (integral) of jointly Gaussian random variables, which is itself Gaussian. The moment-generating function of a Gaussian random variable $Y \sim \mathcal{N}(\mu_Y, \sigma_Y^2)$ is known explicitly:

    $$
    \mathbb{E}[e^{-Y}] = \exp\!\left(-\mu_Y + \frac{1}{2}\sigma_Y^2\right)
    $$

    Since $\mu_Y$ and $\sigma_Y^2$ can be computed in closed form from the Hull-White transition density (involving integrals of $e^{-a(t-s)}$ terms), the bond price $P(0,T) = \mathbb{E}[e^{-Y}]$ has an explicit formula. This allows $\theta^{HW}(t)$ to be extracted analytically by differentiating $P^{\text{mkt}}(0,T)$ with respect to $T$.

    In the BK model, $r_s = e^{x_s}$ where $x_s$ is Gaussian, so $r_s$ is log-normal. The integral $Y = \int_0^T e^{x_s}\,ds$ is an integral of correlated log-normal random variables. The key obstruction is that **the distribution of an integral of log-normal random variables has no closed-form expression**. Specifically:

    1. **No closed-form MGF**: The moment-generating function $\mathbb{E}[e^{-\lambda Y}]$ for $Y = \int_0^T e^{x_s}\,ds$ cannot be expressed in terms of elementary or standard special functions. This is because the exponential of a Gaussian process couples all moments in a way that prevents factorization.

    2. **No Gaussian closure**: Unlike the Hull-White case, $Y$ is not Gaussian (or log-normal, or any standard distribution). The sum of log-normals is not log-normal, and the integral of a log-normal process inherits this intractability.

    3. **Path dependence of the exponential**: The bond price requires $\mathbb{E}[\exp(-\int_0^T e^{x_s}\,ds)]$, which is a doubly exponential functional of the Gaussian path $\{x_s\}$. The outer exponential applied to the inner exponential integral creates a non-separable dependence on the entire path.

    Because $P^{\text{mkt}}(0,T)$ cannot be written as an explicit function of $\theta(t)$, the calibration equation is implicit and must be solved numerically (e.g., by forward induction on a tree or by root-finding at each time step).
