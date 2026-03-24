# Bond Price via Expectation

Under the risk-neutral measure $\mathbb{Q}$, the price of a zero-coupon bond equals the expected discounted payoff. In the Hull-White model the short rate $r(t)$ is Gaussian, so the integral $\int_t^T r(s)\,ds$ is also Gaussian. This section derives the closed-form bond price $P(t,T) = A(t,T)e^{-B(t,T)r(t)}$ by computing the expectation of the exponential of a Gaussian random variable directly, without appealing to PDE methods.

## Risk-Neutral Pricing Formula

The fundamental pricing identity for a zero-coupon bond paying one unit at maturity $T$ states that its time-$t$ price equals the conditional expectation of the stochastic discount factor under $\mathbb{Q}$.

!!! info "Definition: Zero-Coupon Bond Price"
    Under the risk-neutral measure $\mathbb{Q}$, the zero-coupon bond price is

    $$
    P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(s)\,ds}\,\Big|\,\mathcal{F}(t)\right]
    $$

    where $r(s)$ is the short rate process and $\mathcal{F}(t)$ is the filtration at time $t$.

The key observation is that when $r(s)$ follows the Hull-White process

$$
dr(s) = \lambda\bigl(\theta^{\mathbb{Q}}(s) - r(s)\bigr)\,ds + \sigma\,dW^{\mathbb{Q}}(s)
$$

the integral $\int_t^T r(s)\,ds$ is a Gaussian random variable conditional on $\mathcal{F}(t)$. This Gaussian structure allows us to evaluate the expectation in closed form using the moment generating function of the normal distribution.

## Conditional Distribution of the Integral

Recall from the short rate solution that for $s \ge t$,

$$
r(s) = r(t)e^{-\lambda(s-t)} + \alpha(s) - \alpha(t)e^{-\lambda(s-t)} + \sigma\int_t^s e^{-\lambda(s-u)}\,dW^{\mathbb{Q}}(u)
$$

where

$$
\alpha(s) = f^M(0,s) + \frac{\sigma^2}{2\lambda^2}\left(1 - e^{-\lambda s}\right)^2
$$

Integrating $r(s)$ from $t$ to $T$ and interchanging the order of integration with the stochastic integral, the random variable $I(t,T) := \int_t^T r(s)\,ds$ conditional on $\mathcal{F}(t)$ is normally distributed.

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

---

**Exercise 2.** Show that $V(t,T) \to \frac{\sigma^2}{\lambda^2}(T-t)$ in the limit $\lambda \to 0$ by applying L'Hopital's rule or Taylor expanding the exponentials. Interpret this limiting variance in terms of the integrated Brownian motion.

---

**Exercise 3.** For a Hull-White model with $\lambda = 0.1$, $\sigma = 0.015$, and $f^M(0,t) = 0.04$, compute the conditional mean $M(0, 10)$ and variance $V(0, 10)$ of the integrated short rate $\int_0^{10} r(s)\,ds$ given $r(0) = 0.04$.

---

**Exercise 4.** The moment generating function identity $\mathbb{E}[e^{-X}] = e^{-\mu + \frac{1}{2}\sigma^2}$ for $X \sim \mathcal{N}(\mu, \sigma^2)$ is central to the derivation. Prove this identity by completing the square in the integral

$$
\int_{-\infty}^{\infty} e^{-x} \frac{1}{\sqrt{2\pi}\sigma} e^{-(x-\mu)^2/(2\sigma^2)}\,dx
$$

---

**Exercise 5.** The factor $B(t,T)$ has the interpretation of a mean-reversion-adjusted duration. Compare $B(0,T) = \frac{1}{\lambda}(1 - e^{-\lambda T})$ with the Macaulay duration $T$ for a zero-coupon bond. For which values of $\lambda$ and $T$ does the difference exceed 10%?

---

**Exercise 6.** Show that the bond price formula satisfies $P(t,t) = 1$ for all $t$ by verifying that $A(t,t) = 0$ and $B(t,t) = 0$. What does this boundary condition represent financially?

---

**Exercise 7.** Explain why the expectation-based derivation and the PDE-based derivation must produce the same bond price formula. Under what conditions could the two approaches give different results (hint: consider models where the short rate is not affine)?
