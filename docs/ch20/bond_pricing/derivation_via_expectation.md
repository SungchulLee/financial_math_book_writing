# Bond Price via Expectation

Under the risk-neutral measure $\mathbb{Q}$, the price of a zero-coupon bond equals the expected discounted payoff. In the Hull-White model the short rate $r(t)$ is Gaussian, so the integral $\int_t^T r(s)\,ds$ is also Gaussian. This section derives the closed-form bond price $P(t,T) = A(t,T)e^{-B(t,T)r(t)}$ by computing the expectation of the exponential of a Gaussian random variable directly, without appealing to PDE methods.

## Risk-Neutral Pricing Formula

Recall (see [§ Risk-Neutral Pricing](../../ch04/risk_neutral/construction.md)) the identity $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r(s)\,ds}\mid\mathcal{F}(t)]$. Recall (see [HW SDE](../model_definition/hull_white_sde_and_mean_reversion.md)) the dynamics $dr(s) = \lambda(\theta^{\mathbb{Q}}(s) - r(s))\,ds + \sigma\,dW^{\mathbb{Q}}(s)$; the integral $\int_t^T r(s)\,ds$ is Gaussian conditional on $\mathcal{F}(t)$. This Gaussian structure allows us to evaluate the expectation in closed form using the moment generating function of the normal distribution.

## Conditional Distribution of the Integral

Recall (see [HW short rate solution](../short_rate/short_rate_solution.md)) that for $s \ge t$, $r(s) = r(t)e^{-\lambda(s-t)} + \alpha(s) - \alpha(t)e^{-\lambda(s-t)} + \sigma\int_t^s e^{-\lambda(s-u)}\,dW^{\mathbb{Q}}(u)$, where $\alpha(s)$ is the named function from [§ Named Functions](../named_functions/named_functions_definition.md). Integrating $r(s)$ from $t$ to $T$, the random variable $I(t,T) := \int_t^T r(s)\,ds$ conditional on $\mathcal{F}(t)$ is normally distributed.

!!! info "Proposition: Conditional Gaussian Integral"
    The integrated short rate $I(t,T) = \int_t^T r(s)\,ds$ conditional on $\mathcal{F}(t)$ satisfies

    $$
    I(t,T)\,\Big|\,\mathcal{F}(t) \;\sim\; \mathcal{N}\!\left(M(t,T),\; V(t,T)\right)
    $$

    where the conditional mean and variance are given below.

**Conditional mean.** Separating the deterministic and stochastic parts of $r(s)$ and integrating from $t$ to $T$:

$$
M(t,T) = B(t,T)\bigl[r(t) - \alpha(t)\bigr] + \int_t^T \alpha(s)\,ds
$$

where $B(t,T) = \frac{1}{\lambda}\left[1 - e^{-\lambda(T-t)}\right]$ collects the contribution of the current short rate $r(t)$.

???+ note "Derivation of Conditional Mean"

    Integrating the short rate solution over $[t,T]$:

    $$\begin{array}{lllll}
    \displaystyle
    \int_t^T r(s)\,ds
    &=&\displaystyle
    \bigl[r(t) - \alpha(t)\bigr]\int_t^T e^{-\lambda(s-t)}\,ds + \int_t^T \alpha(s)\,ds + \sigma\int_t^T\!\int_t^s e^{-\lambda(s-u)}\,dW^{\mathbb{Q}}(u)\,ds
    \end{array}$$

    The first integral evaluates to

    $$
    \int_t^T e^{-\lambda(s-t)}\,ds = \frac{1}{\lambda}\left[1 - e^{-\lambda(T-t)}\right] = B(t,T)
    $$

    Taking the conditional expectation, the stochastic integral vanishes and we obtain $M(t,T)$.

**Conditional variance.** The variance arises entirely from the stochastic integral term. Using the Fubini-type interchange of integration order:

$$
V(t,T) = \frac{\sigma^2}{\lambda^2}\left[T - t + \frac{2}{\lambda}e^{-\lambda(T-t)} - \frac{1}{2\lambda}e^{-2\lambda(T-t)} - \frac{3}{2\lambda}\right]
$$

???+ note "Derivation of Conditional Variance"

    Starting from the double integral in the stochastic part:

    $$\begin{array}{lllll}
    \displaystyle
    \sigma\int_t^T\!\int_t^s e^{-\lambda(s-u)}\,dW^{\mathbb{Q}}(u)\,ds
    &=&\displaystyle
    \sigma\int_t^T\!\left(\int_u^T e^{-\lambda(s-u)}\,ds\right)dW^{\mathbb{Q}}(u)
    \end{array}$$

    The inner integral equals $B(u,T) = \frac{1}{\lambda}\left[1 - e^{-\lambda(T-u)}\right]$, so

    $$\begin{array}{lllll}
    \displaystyle
    V(t,T)
    &=&\displaystyle
    \sigma^2\int_t^T B(u,T)^2\,du
    \;=\;
    \frac{\sigma^2}{\lambda^2}\int_t^T \left[1 - e^{-\lambda(T-u)}\right]^2 du
    \end{array}$$

    Expanding the square and integrating term by term with the substitution $v = T - u$:

    $$\begin{array}{lllll}
    \displaystyle
    V(t,T)
    &=&\displaystyle
    \frac{\sigma^2}{\lambda^2}\left[(T-t) - \frac{2}{\lambda}\left(1 - e^{-\lambda(T-t)}\right) + \frac{1}{2\lambda}\left(1 - e^{-2\lambda(T-t)}\right)\right]
    \end{array}$$

    which simplifies to the stated formula.

## Gaussian Moment Generating Function

For any Gaussian random variable $X \sim \mathcal{N}(\mu, \sigma^2)$, the moment generating function evaluated at $u = -1$ gives

$$
\mathbb{E}\!\left[e^{-X}\right] = e^{-\mu + \frac{1}{2}\sigma^2}
$$

This identity is the central tool for converting the conditional Gaussian distribution of $I(t,T)$ into a closed-form bond price.

## Bond Price Formula

Applying the moment generating function identity to $I(t,T) \sim \mathcal{N}(M(t,T), V(t,T))$ yields the Hull-White affine bond pricing formula.

!!! info "Theorem: Hull-White Bond Price via Expectation"
    The zero-coupon bond price in the Hull-White model is

    $$
    P(t,T) = A(t,T)\,e^{-B(t,T)\,r(t)}
    $$

    where

    $$\begin{array}{lllll}
    \displaystyle
    B(t,T)
    &=&\displaystyle
    \frac{1}{\lambda}\left[1 - e^{-\lambda(T-t)}\right]
    \\[8pt]
    \displaystyle
    A(t,T)
    &=&\displaystyle
    \frac{P^M(0,T)}{P^M(0,t)}\exp\!\left\{B(t,T)f^M(0,t) - \frac{\sigma^2}{4\lambda}B(t,T)^2\left(1 - e^{-2\lambda t}\right)\right\}
    \end{array}$$

???+ note "Proof"

    Starting from the pricing formula:

    $$\begin{array}{lllll}
    \displaystyle
    P(t,T)
    &=&\displaystyle
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-I(t,T)}\,\Big|\,\mathcal{F}(t)\right]
    \;=\;
    e^{-M(t,T) + \frac{1}{2}V(t,T)}
    \end{array}$$

    Substituting the expressions for $M(t,T)$ and $V(t,T)$ and collecting terms:

    $$\begin{array}{lllll}
    \displaystyle
    P(t,T)
    &=&\displaystyle
    \exp\!\left\{-B(t,T)\bigl[r(t) - \alpha(t)\bigr] - \int_t^T \alpha(s)\,ds + \frac{1}{2}V(t,T)\right\}
    \end{array}$$

    The terms not involving $r(t)$ combine into $\log A(t,T)$, and the $r(t)$-dependent part gives $-B(t,T)r(t)$. Using the relation

    $$
    \alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}\left(1 - e^{-\lambda t}\right)^2
    $$

    and the market bond price identity $P^M(0,T) = \exp\!\left(-\int_0^T f^M(0,s)\,ds\right)$, the deterministic factor simplifies to

    $$\begin{array}{lllll}
    \displaystyle
    A(t,T)
    &=&\displaystyle
    \frac{P^M(0,T)}{P^M(0,t)}\exp\!\left\{B(t,T)f^M(0,t) - \frac{\sigma^2}{4\lambda}B(t,T)^2\left(1 - e^{-2\lambda t}\right)\right\}
    \end{array}$$

    which completes the derivation. $\square$

## Interpretation of the Formula

The bond price formula $P(t,T) = A(t,T)e^{-B(t,T)r(t)}$ has the affine structure characteristic of Gaussian short rate models. Two features deserve emphasis:

- **Factor $B(t,T)$**: This function measures the sensitivity of the bond price to changes in the current short rate $r(t)$. For small mean reversion $\lambda \to 0$, we recover $B(t,T) \to T - t$, the duration of the bond. For large $\lambda$, the exponential decay dampens the effect of $r(t)$ on long-dated bonds.

- **Factor $A(t,T)$**: This deterministic function encodes the initial market term structure through $P^M(0,T)/P^M(0,t)$ and the instantaneous forward rate $f^M(0,t)$. The correction term involving $\sigma^2$ accounts for the convexity adjustment due to the volatility of the short rate.

## Numerical Example

Consider a Hull-White model with parameters $\lambda = 0.05$, $\sigma = 0.01$, and a flat initial forward rate curve $f^M(0,t) = 0.03$ for all $t$. We compute the 10-year zero-coupon bond price at time $t = 0$.

With $r(0) = f^M(0,0) = 0.03$, the function values are:

$$\begin{array}{lllll}
\displaystyle
B(0,10)
&=&\displaystyle
\frac{1}{0.05}\left[1 - e^{-0.05 \times 10}\right]
\;=\;
20\left(1 - e^{-0.5}\right) \;\approx\; 7.8694
\end{array}$$

Since $P^M(0,T) = e^{-0.03T}$ for a flat curve:

$$\begin{array}{lllll}
\displaystyle
A(0,10)
&=&\displaystyle
e^{-0.03 \times 10}\exp\!\left\{7.8694 \times 0.03 - \frac{0.01^2}{4 \times 0.05}\times 7.8694^2 \times 0\right\}
\;=\;
e^{-0.3}\,e^{0.2361}
\end{array}$$

At $t=0$ the exponential correction term involving $(1 - e^{-2\lambda t})$ vanishes, giving

$$
P(0,10) = A(0,10)\,e^{-B(0,10) \times 0.03} = e^{-0.03 \times 10} \approx 0.7408
$$

This recovers the market discount factor, confirming the model's consistency with the initial term structure at $t = 0$.

## Connection to PDE Derivation

The expectation-based derivation and the PDE-based derivation yield identical bond price formulas. The PDE approach substitutes the affine ansatz $P(t,T) = e^{A(\tau) + B(\tau)r(t)}$ into the fundamental PDE and solves the resulting Riccati ODEs for $A$ and $B$. The expectation approach instead evaluates the Gaussian integral directly. Both methods exploit the affine (linear-in-$r$) structure of the Hull-White drift, which ensures that all relevant conditional distributions remain Gaussian.

---

## Summary

This section derived the Hull-White zero-coupon bond price by computing $\mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r(s)\,ds}\,|\,\mathcal{F}(t)]$ directly. The Gaussian property of the OU-type short rate process implies that the integrated short rate is conditionally normal, and the moment generating function of the normal distribution delivers the closed-form result $P(t,T) = A(t,T)e^{-B(t,T)r(t)}$. The function $A(t,T)$ encodes the initial market term structure and a volatility convexity correction, while $B(t,T)$ captures the mean-reversion-adjusted duration.

---

## Exercises

**Exercise 1.** Verify the conditional variance formula by computing $\sigma^2 \int_t^T B(u,T)^2\,du$ directly. Expand the square $(1 - e^{-\lambda(T-u)})^2$, integrate each term, and confirm the result matches $V(t,T)$.

??? success "Solution to Exercise 1"
    We need to compute $V(t,T) = \sigma^2 \int_t^T B(u,T)^2\,du$ where $B(u,T) = \frac{1}{\lambda}(1 - e^{-\lambda(T-u)})$.

    Substituting $v = T - u$ (so $du = -dv$, and the limits change from $u = t$ to $v = \tau = T-t$ and from $u = T$ to $v = 0$):

    $$
    V(t,T) = \frac{\sigma^2}{\lambda^2}\int_0^{\tau}(1 - e^{-\lambda v})^2\,dv
    $$

    Expand the square:

    $$
    (1 - e^{-\lambda v})^2 = 1 - 2e^{-\lambda v} + e^{-2\lambda v}
    $$

    Integrate term by term:

    $$
    \int_0^{\tau} 1\,dv = \tau
    $$

    $$
    \int_0^{\tau} 2e^{-\lambda v}\,dv = 2\left[-\frac{1}{\lambda}e^{-\lambda v}\right]_0^{\tau} = \frac{2}{\lambda}(1 - e^{-\lambda\tau})
    $$

    $$
    \int_0^{\tau} e^{-2\lambda v}\,dv = \left[-\frac{1}{2\lambda}e^{-2\lambda v}\right]_0^{\tau} = \frac{1}{2\lambda}(1 - e^{-2\lambda\tau})
    $$

    Combining:

    $$
    V(t,T) = \frac{\sigma^2}{\lambda^2}\left[\tau - \frac{2}{\lambda}(1 - e^{-\lambda\tau}) + \frac{1}{2\lambda}(1 - e^{-2\lambda\tau})\right]
    $$

    Rewriting by distributing the negative signs:

    $$
    = \frac{\sigma^2}{\lambda^2}\left[\tau + \frac{2}{\lambda}e^{-\lambda\tau} - \frac{1}{2\lambda}e^{-2\lambda\tau} - \frac{2}{\lambda} + \frac{1}{2\lambda}\right]
    $$

    $$
    = \frac{\sigma^2}{\lambda^2}\left[\tau + \frac{2}{\lambda}e^{-\lambda\tau} - \frac{1}{2\lambda}e^{-2\lambda\tau} - \frac{3}{2\lambda}\right]
    $$

    This confirms the stated formula for $V(t,T)$.

---

**Exercise 2.** Show that $V(t,T) \to \frac{\sigma^2}{\lambda^2}(T-t)$ in the limit $\lambda \to 0$ by applying L'Hopital's rule or Taylor expanding the exponentials. Interpret this limiting variance in terms of the integrated Brownian motion.

??? success "Solution to Exercise 2"
    Taylor expand each exponential in $V(t,T)$ around $\lambda = 0$ using $\tau = T - t$:

    $$
    e^{-\lambda\tau} = 1 - \lambda\tau + \frac{(\lambda\tau)^2}{2} - \frac{(\lambda\tau)^3}{6} + \cdots
    $$

    $$
    e^{-2\lambda\tau} = 1 - 2\lambda\tau + 2(\lambda\tau)^2 - \frac{4(\lambda\tau)^3}{3} + \cdots
    $$

    Substituting into $V(t,T) = \frac{\sigma^2}{\lambda^2}\left[\tau + \frac{2}{\lambda}e^{-\lambda\tau} - \frac{1}{2\lambda}e^{-2\lambda\tau} - \frac{3}{2\lambda}\right]$:

    $$
    \frac{2}{\lambda}e^{-\lambda\tau} = \frac{2}{\lambda} - 2\tau + \lambda\tau^2 - \frac{\lambda^2\tau^3}{3} + \cdots
    $$

    $$
    \frac{1}{2\lambda}e^{-2\lambda\tau} = \frac{1}{2\lambda} - \tau + \lambda\tau^2 - \frac{2\lambda^2\tau^3}{3} + \cdots
    $$

    Combining:

    $$
    \tau + \frac{2}{\lambda} - 2\tau + \lambda\tau^2 - \frac{1}{2\lambda} + \tau - \lambda\tau^2 - \frac{3}{2\lambda} + O(\lambda^2)
    $$

    $$
    = \tau - 2\tau + \tau + \frac{2}{\lambda} - \frac{1}{2\lambda} - \frac{3}{2\lambda} + \lambda\tau^2 - \lambda\tau^2 + O(\lambda^2)
    $$

    The constant terms cancel: $\frac{2}{\lambda} - \frac{1}{2\lambda} - \frac{3}{2\lambda} = 0$. The $\tau$ terms cancel: $\tau - 2\tau + \tau = 0$. The leading surviving term is $\frac{\lambda^2\tau^3}{3}$ (from detailed expansion of cubic terms).

    Therefore:

    $$
    V(t,T) = \frac{\sigma^2}{\lambda^2} \cdot \frac{\lambda^2\tau^3}{3} + O(\lambda^2) = \frac{\sigma^2\tau^3}{3}
    $$

    Wait -- let us redo this more carefully. Actually $V(t,T) \to \sigma^2 \tau^3/3$ for $\lambda \to 0$, not $\sigma^2\tau/\lambda^2$. Let us verify: in the Ho-Lee model ($\lambda = 0$), $r(s) = r(t) + \theta s + \sigma W(s)$, and

    $$
    \text{Var}\left(\int_t^T r(s)ds\right) = \sigma^2\int_t^T\int_t^T \min(s-t,u-t)\,ds\,du = \frac{\sigma^2(T-t)^3}{3}
    $$

    This is consistent with $V(t,T) \to \sigma^2\tau^3/3$ as $\lambda \to 0$.

    **Interpretation:** In the limit $\lambda \to 0$ there is no mean reversion, so the short rate performs a random walk. The integrated Brownian motion $\int_t^T W(s)\,ds$ has variance proportional to $\tau^3/3$, growing cubically with the integration horizon. Mean reversion ($\lambda > 0$) dampens the variance, transitioning the growth from cubic to approximately linear for large $\tau$.

---

**Exercise 3.** For a Hull-White model with $\lambda = 0.1$, $\sigma = 0.015$, and $f^M(0,t) = 0.04$, compute the conditional mean $M(0, 10)$ and variance $V(0, 10)$ of the integrated short rate $\int_0^{10} r(s)\,ds$ given $r(0) = 0.04$.

??? success "Solution to Exercise 3"
    With $\lambda = 0.1$, $\sigma = 0.015$, $f^M(0,t) = 0.04$, $r(0) = 0.04$, and $\tau = T - t = 10$:

    **Conditional mean $M(0,10)$:** Using $M(t,T) = B(t,T)[r(t) - \alpha(t)] + \int_t^T \alpha(s)\,ds$:

    $$
    B(0,10) = \frac{1}{0.1}(1 - e^{-1}) = 10(1 - 0.3679) = 6.321
    $$

    $$
    \alpha(0) = f^M(0,0) + \frac{\sigma^2}{2\lambda^2}(1 - e^0)^2 = 0.04 + 0 = 0.04
    $$

    Since $r(0) = \alpha(0) = 0.04$, the first term is zero: $B(0,10)[r(0) - \alpha(0)] = 0$.

    For the integral $\int_0^{10}\alpha(s)\,ds$ with $\alpha(s) = 0.04 + \frac{0.000225}{0.02}(1 - e^{-0.1s})^2 = 0.04 + 0.01125(1 - e^{-0.1s})^2$:

    $$
    \int_0^{10}\alpha(s)\,ds = 0.4 + 0.01125\int_0^{10}(1 - e^{-0.1s})^2\,ds
    $$

    $$
    \int_0^{10}(1-e^{-0.1s})^2\,ds = 10 - \frac{2}{0.1}(1-e^{-1}) + \frac{1}{0.2}(1-e^{-2})
    $$

    $$
    = 10 - 20(0.6321) + 5(0.8647) = 10 - 12.642 + 4.3235 = 1.6815
    $$

    $$
    M(0,10) = 0.4 + 0.01125 \times 1.6815 \approx 0.4 + 0.01892 = 0.41892
    $$

    **Conditional variance $V(0,10)$:**

    $$
    V(0,10) = \frac{0.015^2}{0.01}\left[10 + \frac{2}{0.1}e^{-1} - \frac{1}{0.2}e^{-2} - \frac{3}{0.2}\right]
    $$

    $$
    = 0.0225\left[10 + 20(0.3679) - 5(0.1353) - 15\right]
    $$

    $$
    = 0.0225\left[10 + 7.358 - 0.6767 - 15\right] = 0.0225 \times 1.6813 \approx 0.03783
    $$

    The standard deviation is $\sqrt{0.03783} \approx 0.1946$.

---

**Exercise 4.** The moment generating function identity $\mathbb{E}[e^{-X}] = e^{-\mu + \frac{1}{2}\sigma^2}$ for $X \sim \mathcal{N}(\mu, \sigma^2)$ is central to the derivation. Prove this identity by completing the square in the integral

$$
\int_{-\infty}^{\infty} e^{-x} \frac{1}{\sqrt{2\pi}\sigma} e^{-(x-\mu)^2/(2\sigma^2)}\,dx
$$

??? success "Solution to Exercise 4"
    We need to evaluate:

    $$
    I = \int_{-\infty}^{\infty} e^{-x}\,\frac{1}{\sqrt{2\pi}\sigma}\,e^{-(x-\mu)^2/(2\sigma^2)}\,dx
    $$

    Combine the exponents:

    $$
    -x - \frac{(x-\mu)^2}{2\sigma^2} = -x - \frac{x^2 - 2\mu x + \mu^2}{2\sigma^2}
    $$

    $$
    = -\frac{1}{2\sigma^2}\left[x^2 - 2\mu x + \mu^2 + 2\sigma^2 x\right] = -\frac{1}{2\sigma^2}\left[x^2 - 2(\mu - \sigma^2)x + \mu^2\right]
    $$

    Complete the square in $x$:

    $$
    x^2 - 2(\mu-\sigma^2)x + \mu^2 = \left[x - (\mu-\sigma^2)\right]^2 - (\mu-\sigma^2)^2 + \mu^2
    $$

    $$
    = \left[x - (\mu-\sigma^2)\right]^2 + 2\mu\sigma^2 - \sigma^4
    $$

    Therefore the exponent becomes:

    $$
    -\frac{[x-(\mu-\sigma^2)]^2}{2\sigma^2} - \mu + \frac{\sigma^2}{2}
    $$

    Substituting back:

    $$
    I = e^{-\mu + \sigma^2/2}\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}\sigma}\,e^{-[x-(\mu-\sigma^2)]^2/(2\sigma^2)}\,dx
    $$

    The integral is the total probability of a $\mathcal{N}(\mu - \sigma^2, \sigma^2)$ density, which equals 1. Therefore:

    $$
    \mathbb{E}[e^{-X}] = e^{-\mu + \sigma^2/2}
    $$

---

**Exercise 5.** The factor $B(t,T)$ has the interpretation of a mean-reversion-adjusted duration. Compare $B(0,T) = \frac{1}{\lambda}(1 - e^{-\lambda T})$ with the Macaulay duration $T$ for a zero-coupon bond. For which values of $\lambda$ and $T$ does the difference exceed 10%?

??? success "Solution to Exercise 5"
    The Macaulay duration of a zero-coupon bond is simply $T$ (the time to maturity). The mean-reversion-adjusted duration is $B(0,T) = \frac{1}{\lambda}(1 - e^{-\lambda T})$.

    The relative difference is:

    $$
    \frac{T - B(0,T)}{T} = 1 - \frac{1 - e^{-\lambda T}}{\lambda T}
    $$

    We want this to exceed 10%, i.e.:

    $$
    1 - \frac{1 - e^{-\lambda T}}{\lambda T} > 0.1 \quad\Longleftrightarrow\quad \frac{1 - e^{-\lambda T}}{\lambda T} < 0.9
    $$

    Let $x = \lambda T$. The condition becomes $\frac{1 - e^{-x}}{x} < 0.9$.

    For small $x$: $\frac{1-e^{-x}}{x} \approx 1 - x/2 + x^2/6 - \cdots < 0.9$ when $x/2 > 0.1$, i.e., $x > 0.2$ approximately. Numerically solving $\frac{1-e^{-x}}{x} = 0.9$: at $x = 0.2$, $\frac{1-e^{-0.2}}{0.2} = \frac{0.1813}{0.2} = 0.9066$; at $x = 0.22$, $\frac{1-e^{-0.22}}{0.22} = \frac{0.1975}{0.22} = 0.8977$. So $x \approx 0.21$.

    Examples where the 10% threshold is exceeded:

    - $\lambda = 0.05$, $T = 5$: $x = 0.25$, difference $\approx 11.6\%$
    - $\lambda = 0.1$, $T = 3$: $x = 0.3$, difference $\approx 13.7\%$
    - $\lambda = 0.02$, $T = 15$: $x = 0.3$, difference $\approx 13.7\%$

    In general, whenever $\lambda T \gtrsim 0.21$, the relative difference exceeds 10%. Higher mean reversion or longer maturities amplify the discrepancy between the standard duration $T$ and the mean-reversion-adjusted duration $B(0,T)$.

---

**Exercise 6.** Show that the bond price formula satisfies $P(t,t) = 1$ for all $t$ by verifying that $A(t,t) = 0$ and $B(t,t) = 0$. What does this boundary condition represent financially?

??? success "Solution to Exercise 6"
    At $\tau = T - t = 0$:

    **$B(t,t) = 0$:** From $B(t,T) = \frac{1}{\lambda}(1 - e^{-\lambda(T-t)})$, setting $T = t$:

    $$
    B(t,t) = \frac{1}{\lambda}(1 - e^{0}) = \frac{1}{\lambda}(1 - 1) = 0
    $$

    **$A(t,t) = 1$:** From the formula:

    $$
    A(t,t) = \frac{P^M(0,t)}{P^M(0,t)}\exp\left\{0 \cdot f^M(0,t) - \frac{\sigma^2}{4\lambda} \cdot 0^2 \cdot (\cdots)\right\} = 1 \cdot e^0 = 1
    $$

    Therefore (note $\log A(t,t) = 0$):

    $$
    P(t,t) = A(t,t)\,e^{-B(t,t)\,r(t)} = 1 \cdot e^{0} = 1
    $$

    **Financial interpretation:** The bond price $P(t,t) = 1$ means that a zero-coupon bond at its maturity date pays exactly its face value of one unit of currency. This is the terminal (or boundary) condition: there is no discounting needed when the payment is immediate.

---

**Exercise 7.** Explain why the expectation-based derivation and the PDE-based derivation must produce the same bond price formula. Under what conditions could the two approaches give different results (hint: consider models where the short rate is not affine)?

??? success "Solution to Exercise 7"
    **Why both derivations agree:** The Feynman-Kac theorem establishes a rigorous equivalence between the conditional expectation $\mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r(s)ds} \mid \mathcal{F}(t)]$ and the solution of the backward PDE $\frac{\partial P}{\partial t} + \mu\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2\frac{\partial^2 P}{\partial r^2} - rP = 0$ with terminal condition $P(T,T) = 1$. Under standard regularity conditions (the Hull-White model satisfies these because the drift is affine and the diffusion is bounded), the Feynman-Kac theorem guarantees that the PDE solution and the expectation yield the same function $P(t,T)$. Therefore, any correct computation of either one must produce the same answer.

    **When the two approaches could diverge in practice:**

    1. *Non-affine models:* In models like the Black-Karasinski model ($d\log r = a(\theta - \log r)dt + \sigma\,dW$), the short rate dynamics are not affine. The exponential-affine ansatz fails, and the PDE cannot be reduced to ODEs. The expectation approach also fails to produce a closed form because $\int_t^T r(s)ds$ is not Gaussian. Both approaches still give the same theoretical answer (by Feynman-Kac), but neither yields a closed-form solution -- both require numerical methods.

    2. *Numerical approximation:* When solving numerically, the PDE approach (finite differences) and the expectation approach (Monte Carlo) use different approximations with different error characteristics. Finite differences introduce grid truncation and discretization error; Monte Carlo introduces statistical sampling error and time-stepping bias. These can produce different numerical values that converge to the same limit as resolution increases.

    3. *Regularity failures:* If the Feynman-Kac conditions fail (e.g., the diffusion coefficient degenerates, or the solution grows too fast), the PDE may have multiple solutions or the expectation may not be well-defined, potentially leading to discrepancies. The Hull-White model does not suffer from these issues.
