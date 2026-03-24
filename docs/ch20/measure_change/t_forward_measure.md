# T-Forward Measure

When pricing a derivative that pays at a fixed future time $T$, the standard risk-neutral expectation $\mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r(s)\,ds}V(T)\,|\,\mathcal{F}(t)]$ involves both the payoff $V(T)$ and the stochastic discount factor. The $T$-forward measure $\mathbb{Q}^T$ eliminates the discount factor by using the zero-coupon bond $P(t,T)$ as numeraire, replacing the expectation with $P(t,T)\,\mathbb{E}^{T}[V(T)\,|\,\mathcal{F}(t)]$. This section defines the $T$-forward measure, derives the change of measure from $\mathbb{Q}$ to $\mathbb{Q}^T$, and establishes the forward rate martingale property.

## Numeraire and Measure Change

The general change-of-numeraire theorem states that if $N(t)$ is a positive, tradable numeraire process, then the measure $\mathbb{Q}^N$ defined by

$$
\frac{d\mathbb{Q}^N}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)} = \frac{N(t)/N(0)}{M(t)/M(0)}
$$

makes the ratio $X(t)/N(t)$ a martingale for any tradable asset $X(t)$. Here $M(t) = \exp(\int_0^t r(s)\,ds)$ is the money market account.

!!! info "Definition: T-Forward Measure"
    The $T$-forward measure $\mathbb{Q}^T$ is the probability measure obtained by choosing $N(t) = P(t,T)$ as numeraire. Its Radon-Nikodym derivative with respect to $\mathbb{Q}$ is

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)} = \frac{P(t,T)/P(0,T)}{M(t)/M(0)} = \frac{P(t,T)}{P(0,T)\,M(t)}
    $$

## Radon-Nikodym Derivative in the Hull-White Model

In the Hull-White model, the zero-coupon bond dynamics under $\mathbb{Q}$ are

$$
\frac{dP(t,T)}{P(t,T)} = r(t)\,dt + \sigma_P(t,T)\,dW^{\mathbb{Q}}(t)
$$

where the bond volatility is

$$
\sigma_P(t,T) = -\frac{\sigma}{\lambda}\left(1 - e^{-\lambda(T-t)}\right) = \sigma\,B(t,T)
$$

with $B(t,T) = -\frac{1}{\lambda}(1 - e^{-\lambda(T-t)})$ using the sign convention from the named functions. Taking the logarithm of the Radon-Nikodym derivative:

$$\begin{array}{lllll}
\displaystyle
\log\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)}
&=&\displaystyle
\log P(t,T) - \log P(0,T) - \int_0^t r(s)\,ds
\\[6pt]
&=&\displaystyle
-\frac{1}{2}\int_0^t \sigma_P(s,T)^2\,ds + \int_0^t \sigma_P(s,T)\,dW^{\mathbb{Q}}(s)
\end{array}$$

???+ note "Proof"

    From the bond price dynamics under $\mathbb{Q}$:

    $$\begin{array}{lllll}
    \displaystyle
    d\log P(t,T)
    &=&\displaystyle
    \left(r(t) - \frac{1}{2}\sigma_P^2(t,T)\right)dt + \sigma_P(t,T)\,dW^{\mathbb{Q}}(t)
    \end{array}$$

    Integrating from $0$ to $t$:

    $$\begin{array}{lllll}
    \displaystyle
    \log P(t,T) - \log P(0,T)
    &=&\displaystyle
    \int_0^t r(s)\,ds - \frac{1}{2}\int_0^t \sigma_P^2(s,T)\,ds + \int_0^t \sigma_P(s,T)\,dW^{\mathbb{Q}}(s)
    \end{array}$$

    Subtracting $\int_0^t r(s)\,ds$ yields the stated expression. $\square$

## Girsanov Transformation

By Girsanov's theorem, the process

$$
dW^{T}(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T)\,dt
$$

is a standard Brownian motion under $\mathbb{Q}^T$. Equivalently,

$$
dW^{\mathbb{Q}}(t) = dW^{T}(t) + \sigma_P(t,T)\,dt
$$

!!! info "Theorem: Girsanov Change from Q to T-Forward"
    Under the $T$-forward measure $\mathbb{Q}^T$, the Brownian motion is

    $$
    dW^{T}(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T)\,dt
    $$

    where $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})$ is the Hull-White bond volatility.

## Pricing Formula Under the T-Forward Measure

The key advantage of the $T$-forward measure is that it absorbs the stochastic discount factor into the measure change. For any $\mathcal{F}(T)$-measurable payoff $V(T)$:

$$\begin{array}{lllll}
\displaystyle
\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(s)\,ds}\,V(T)\,\Big|\,\mathcal{F}(t)\right]
&=&\displaystyle
P(t,T)\,\mathbb{E}^{T}\!\left[V(T)\,\Big|\,\mathcal{F}(t)\right]
\end{array}$$

???+ note "Proof"

    Using the abstract Bayes formula for conditional expectations under a change of measure:

    $$\begin{array}{lllll}
    \displaystyle
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t)}{M(T)}\,V(T)\,\Big|\,\mathcal{F}(t)\right]
    &=&\displaystyle
    \frac{P(t,T)}{1}\,\mathbb{E}^{T}\!\left[V(T)\,\Big|\,\mathcal{F}(t)\right]
    \end{array}$$

    This follows from the identity $\frac{M(t)}{M(T)} = P(t,T)\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\Big|_{\mathcal{F}(T)} / \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\Big|_{\mathcal{F}(t)}$ and the tower property of conditional expectation. $\square$

This formula is particularly powerful for options on zero-coupon bonds, where $V(T) = \max(P(T,S) - K, 0)$ and the expectation under $\mathbb{Q}^T$ involves only the distribution of $r(T)$ without the complicating discount factor.

## Forward Rate as a Martingale

A central property of the $T$-forward measure is that the instantaneous forward rate $f(t,T)$ is a martingale.

!!! info "Theorem: Forward Rate Martingale Property"
    Under $\mathbb{Q}^T$, the instantaneous forward rate satisfies

    $$
    df(t,T) = \sigma(t,T)\,dW^{T}(t)
    $$

    where $\sigma(t,T) = \sigma\,e^{-\lambda(T-t)}$ is the Hull-White forward rate volatility. In particular, $f(t,T)$ is a $\mathbb{Q}^T$-martingale.

???+ note "Proof"

    Under $\mathbb{Q}$, the HJM drift condition gives

    $$
    df(t,T) = \sigma(t,T)\!\left(\int_t^T \sigma(t,u)\,du\right)dt + \sigma(t,T)\,dW^{\mathbb{Q}}(t)
    $$

    Since $\int_t^T \sigma(t,u)\,du = -\sigma_P(t,T)$, substituting $dW^{\mathbb{Q}}(t) = dW^{T}(t) + \sigma_P(t,T)\,dt$:

    $$\begin{array}{lllll}
    \displaystyle
    df(t,T)
    &=&\displaystyle
    -\sigma(t,T)\sigma_P(t,T)\,dt + \sigma(t,T)\bigl(dW^{T}(t) + \sigma_P(t,T)\,dt\bigr)
    \\[4pt]
    &=&\displaystyle
    \sigma(t,T)\,dW^{T}(t)
    \end{array}$$

    The drift terms cancel exactly, confirming the martingale property. $\square$

## Forward Price Martingale

More generally, the forward price of any tradable asset $X(t)$ relative to the $T$-maturity bond is a $\mathbb{Q}^T$-martingale:

$$
\mathbb{E}^{T}\!\left[\frac{X(T)}{P(T,T)}\,\Big|\,\mathcal{F}(t)\right] = \frac{X(t)}{P(t,T)}
$$

Since $P(T,T) = 1$, this simplifies to

$$
\mathbb{E}^{T}\!\left[X(T)\,\Big|\,\mathcal{F}(t)\right] = \frac{X(t)}{P(t,T)}
$$

This result underpins the pricing of all European-style interest rate derivatives in the Hull-White framework.

## Numerical Example

Consider pricing a European call option on a zero-coupon bond. The payoff at $T = 5$ is $\max(P(5,10) - K, 0)$ with $K = 0.75$. Under the $T$-forward measure, the price at $t = 0$ is

$$
V(0) = P(0,5)\,\mathbb{E}^{5}\!\left[\max(P(5,10) - 0.75,\, 0)\,\Big|\,\mathcal{F}(0)\right]
$$

The advantage is clear: instead of computing $\mathbb{E}^{\mathbb{Q}}[e^{-\int_0^5 r(s)\,ds}\max(P(5,10) - 0.75, 0)]$ -- which involves the joint distribution of the discount factor and the payoff -- we need only the distribution of $P(5,10)$ under $\mathbb{Q}^5$. In the Hull-White model, $P(5,10) = e^{A(5,10) + B(5,10)r(5)}$ and $r(5)$ is Gaussian under $\mathbb{Q}^5$, leading directly to the Black-Scholes-type closed-form formula derived in the zero-coupon bond options section.

---

## Summary

The $T$-forward measure $\mathbb{Q}^T$ uses the zero-coupon bond $P(t,T)$ as numeraire and is obtained from $\mathbb{Q}$ via Girsanov's theorem with drift adjustment $\sigma_P(t,T)$. Under $\mathbb{Q}^T$, the discount factor is absorbed into the measure change, simplifying derivative pricing to $P(t,T)\,\mathbb{E}^T[V(T)]$. The instantaneous forward rate $f(t,T)$ becomes a $\mathbb{Q}^T$-martingale, and the Gaussian structure of the Hull-White model is preserved under this measure change.

---

## Exercises

**Exercise 1.** State the general change-of-numeraire theorem. If the numeraire is $N(t) = P(t,T)$ and the base measure is $\mathbb{Q}$ with numeraire $M(t) = e^{\int_0^t r(s)\,ds}$, write down the Radon-Nikodym derivative $\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\big|_{\mathcal{F}(t)}$ and verify that $P(t,S)/P(t,T)$ is a $\mathbb{Q}^T$-martingale for any $S$.

---

**Exercise 2.** Verify the Girsanov transformation $dW^T(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T)\,dt$ by substituting $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})$ and computing the drift adjustment explicitly for $\lambda = 0.05$ and $\sigma = 0.01$ at $t = 3$ and $T = 10$.

---

**Exercise 3.** Show that the forward rate $f(t,T)$ has zero drift under $\mathbb{Q}^T$ by starting from the HJM drift condition under $\mathbb{Q}$ and applying the Girsanov transformation. Explain why the exact cancellation of drift terms is a consequence of the HJM no-arbitrage condition.

---

**Exercise 4.** Prove that the forward price $X(t)/P(t,T)$ is a $\mathbb{Q}^T$-martingale using the abstract Bayes formula. Explain why this martingale property makes the $T$-forward measure the natural choice for pricing European derivatives with payoff at time $T$.

---

**Exercise 5.** In the numerical example, the option price is $V(0) = P(0,5)\,\mathbb{E}^5[\max(P(5,10) - 0.75, 0)]$. Explain why computing this expectation under $\mathbb{Q}^5$ is simpler than computing $\mathbb{E}^{\mathbb{Q}}[e^{-\int_0^5 r(s)\,ds}\max(P(5,10) - 0.75, 0)]$. What correlation structure makes the $\mathbb{Q}$-expectation more difficult?

---

**Exercise 6.** Consider two different $T$-forward measures, $\mathbb{Q}^{T_1}$ and $\mathbb{Q}^{T_2}$ with $T_1 < T_2$. Derive the Radon-Nikodym derivative $\frac{d\mathbb{Q}^{T_2}}{d\mathbb{Q}^{T_1}}\big|_{\mathcal{F}(t)}$ and the corresponding Girsanov transformation between the two measures.

---

**Exercise 7.** The forward LIBOR rate $L(t, T, T+\delta)$ defined by $1 + \delta L(t,T,T+\delta) = P(t,T)/P(t,T+\delta)$ is a martingale under $\mathbb{Q}^{T+\delta}$. Verify this claim for the Hull-White model and explain how this connects to the pricing of caplets.
