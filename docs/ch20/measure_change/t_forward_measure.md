# T-Forward Measure

When pricing a derivative that pays at a fixed future time $T$, the standard risk-neutral expectation $\mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r(s)\,ds}V(T)\,|\,\mathcal{F}(t)]$ involves both the payoff $V(T)$ and the stochastic discount factor. The $T$-forward measure $\mathbb{Q}^T$ eliminates the discount factor by using the zero-coupon bond $P(t,T)$ as numeraire, replacing the expectation with $P(t,T)\,\mathbb{E}^{T}[V(T)\,|\,\mathcal{F}(t)]$. This section defines the $T$-forward measure, derives the change of measure from $\mathbb{Q}$ to $\mathbb{Q}^T$, and establishes the forward rate martingale property.

## Numeraire and Measure Change

Recall (see [§ T-Forward Measures](../../ch19/forward_measures/t_forward_measures.md) and [§ Numeraire Techniques](../../ch19/forward_measures/numeraire_techniques.md)): given a positive tradable numeraire $N(t)$, the associated measure $\mathbb{Q}^N$ with

$$
\frac{d\mathbb{Q}^N}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)} = \frac{N(t)/N(0)}{M(t)/M(0)}
$$

makes $X(t)/N(t)$ a martingale for every tradable $X$, where $M(t)=\exp(\int_0^t r(s)\,ds)$ is the money-market account.

!!! info "Definition: T-Forward Measure"
    The $T$-forward measure $\mathbb{Q}^T$ is the probability measure obtained by choosing $N(t) = P(t,T)$ as numeraire. Its Radon–Nikodym derivative with respect to $\mathbb{Q}$ is

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)} = \frac{P(t,T)/P(0,T)}{M(t)/M(0)} = \frac{P(t,T)}{P(0,T)\,M(t)}
    $$

## Radon–Nikodym Derivative and Girsanov Transformation

Recall (see [§ Change of Numeraire Q to T](change_of_numeraire_q_to_t.md)): the Hull-White bond volatility is $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)}) = \sigma B(t,T)$, the Radon–Nikodym log is $\log\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\big|_{\mathcal{F}(t)} = -\frac{1}{2}\int_0^t \sigma_P^2(s,T)\,ds + \int_0^t \sigma_P(s,T)\,dW^{\mathbb{Q}}(s)$, and the Girsanov transformation is

$$
dW^{T}(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T)\,dt.
$$

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

    Recall (see [§ Change of Numeraire Q to T](change_of_numeraire_q_to_t.md)): substituting $dW^{\mathbb{Q}} = dW^T + \sigma_P\,dt$ into the HJM forward-rate SDE and using $\int_t^T \sigma(t,u)\,du = -\sigma_P(t,T)$, the drift terms cancel. $\square$

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

**Exercise 1.** State the general change-of-numeraire theorem. If the numeraire is $N(t) = P(t,T)$ and the base measure is $\mathbb{Q}$ with numeraire $M(t) = e^{\int_0^t r(s)\,ds}$, write down the Radon–Nikodym derivative $\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\big|_{\mathcal{F}(t)}$ and verify that $P(t,S)/P(t,T)$ is a $\mathbb{Q}^T$-martingale for any $S$.

??? success "Solution to Exercise 1"
    **General change-of-numeraire theorem:** Let $N(t)$ be a positive, tradable numeraire and $M(t) = e^{\int_0^t r(s)\,ds}$ the money market account. The measure $\mathbb{Q}^N$ defined by

    $$
    \frac{d\mathbb{Q}^N}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)} = \frac{N(t)/N(0)}{M(t)/M(0)} = \frac{N(t)}{N(0)\,M(t)}
    $$

    makes the ratio $X(t)/N(t)$ a $\mathbb{Q}^N$-martingale for every tradable asset $X(t)$.

    **Radon–Nikodym derivative for the T-forward measure:** Setting $N(t) = P(t,T)$:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)} = \frac{P(t,T)}{P(0,T)\,M(t)}
    $$

    **Verification that $P(t,S)/P(t,T)$ is a $\mathbb{Q}^T$-martingale:** By the change-of-numeraire theorem, for any tradable asset $X(t)$, the ratio $X(t)/P(t,T)$ is a $\mathbb{Q}^T$-martingale. Taking $X(t) = P(t,S)$ (which is a tradable asset — it is the price of the $S$-maturity zero-coupon bond):

    $$
    \mathbb{E}^T\!\left[\frac{P(u,S)}{P(u,T)}\,\Big|\,\mathcal{F}(t)\right] = \frac{P(t,S)}{P(t,T)} \qquad \text{for all } t \leq u
    $$

    This confirms that $P(t,S)/P(t,T)$ is a $\mathbb{Q}^T$-martingale. In particular, at $u = T$ where $P(T,T) = 1$:

    $$
    \mathbb{E}^T\!\left[P(T,S)\,\Big|\,\mathcal{F}(t)\right] = \frac{P(t,S)}{P(t,T)}
    $$

---

**Exercise 2.** Verify the Girsanov transformation $dW^T(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T)\,dt$ by substituting $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})$ and computing the drift adjustment explicitly for $\lambda = 0.05$ and $\sigma = 0.01$ at $t = 3$ and $T = 10$.

??? success "Solution to Exercise 2"
    The Girsanov transformation is $dW^T(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T)\,dt$ where

    $$
    \sigma_P(t,T) = -\frac{\sigma}{\lambda}\left(1 - e^{-\lambda(T-t)}\right)
    $$

    For $\lambda = 0.05$, $\sigma = 0.01$, $t = 3$, $T = 10$:

    $$
    \sigma_P(3, 10) = -\frac{0.01}{0.05}\left(1 - e^{-0.05 \times 7}\right) = -0.2\left(1 - e^{-0.35}\right)
    $$

    Computing $e^{-0.35} \approx 0.7047$:

    $$
    \sigma_P(3, 10) = -0.2 \times (1 - 0.7047) = -0.2 \times 0.2953 = -0.05906
    $$

    The drift adjustment in the Girsanov transformation is therefore $-\sigma_P(3, 10) = 0.05906$. This means

    $$
    dW^T(t)\big|_{t=3} = dW^{\mathbb{Q}}(t)\big|_{t=3} + 0.05906\,dt
    $$

    or equivalently $dW^{\mathbb{Q}}(t)\big|_{t=3} = dW^T(t)\big|_{t=3} - 0.05906\,dt$. The drift adjustment is positive (subtracting a negative quantity), reflecting the fact that under the $T$-forward measure, the Brownian motion has an upward drift relative to the $\mathbb{Q}$-Brownian motion. Since the bond volatility $\sigma_P$ is negative (bond prices move inversely to rates), this adjustment shifts probability toward lower interest rate paths, consistent with using the bond as numeraire.

---

**Exercise 3.** Show that the forward rate $f(t,T)$ has zero drift under $\mathbb{Q}^T$ by starting from the HJM drift condition under $\mathbb{Q}$ and applying the Girsanov transformation. Explain why the exact cancellation of drift terms is a consequence of the HJM no-arbitrage condition.

??? success "Solution to Exercise 3"
    Under $\mathbb{Q}$, the HJM drift condition gives the forward rate dynamics:

    $$
    df(t,T) = \sigma(t,T)\!\left(\int_t^T \sigma(t,u)\,du\right)dt + \sigma(t,T)\,dW^{\mathbb{Q}}(t)
    $$

    The key identity is $\int_t^T \sigma(t,u)\,du = -\sigma_P(t,T)$, which follows from $\sigma_P(t,T) = -\int_t^T \sigma(t,u)\,du$ (the bond volatility is minus the integral of forward rate volatilities). Therefore:

    $$
    df(t,T) = -\sigma(t,T)\,\sigma_P(t,T)\,dt + \sigma(t,T)\,dW^{\mathbb{Q}}(t)
    $$

    Now apply the Girsanov transformation $dW^{\mathbb{Q}}(t) = dW^T(t) + \sigma_P(t,T)\,dt$:

    $$\begin{array}{lllll}
    \displaystyle
    df(t,T)
    &=&\displaystyle
    -\sigma(t,T)\,\sigma_P(t,T)\,dt + \sigma(t,T)\!\left(dW^T(t) + \sigma_P(t,T)\,dt\right)
    \\[6pt]
    &=&\displaystyle
    -\sigma(t,T)\,\sigma_P(t,T)\,dt + \sigma(t,T)\,\sigma_P(t,T)\,dt + \sigma(t,T)\,dW^T(t)
    \\[6pt]
    &=&\displaystyle
    \sigma(t,T)\,dW^T(t)
    \end{array}$$

    The drift terms cancel exactly, confirming that $f(t,T)$ is driftless under $\mathbb{Q}^T$.

    **Why the cancellation occurs:** The HJM no-arbitrage condition under $\mathbb{Q}$ is precisely the statement that the drift of $f(t,T)$ equals $\sigma(t,T)\int_t^T \sigma(t,u)\,du$. This drift is exactly what is needed to cancel against the Girsanov adjustment $\sigma(t,T)\sigma_P(t,T)$ when changing to $\mathbb{Q}^T$. In other words, the HJM drift condition was designed (via the no-arbitrage requirement) so that the forward rate becomes a martingale under the measure that uses $P(t,T)$ as numeraire. This is not a coincidence but a fundamental consequence of the absence of arbitrage.

---

**Exercise 4.** Prove that the forward price $X(t)/P(t,T)$ is a $\mathbb{Q}^T$-martingale using the abstract Bayes formula. Explain why this martingale property makes the $T$-forward measure the natural choice for pricing European derivatives with payoff at time $T$.

??? success "Solution to Exercise 4"
    **Proof using the abstract Bayes formula:** Let $X(t)$ be a tradable asset. Under $\mathbb{Q}$, the discounted price $X(t)/M(t)$ is a $\mathbb{Q}$-martingale:

    $$
    \frac{X(t)}{M(t)} = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{X(T)}{M(T)}\,\Big|\,\mathcal{F}(t)\right]
    $$

    The abstract Bayes formula for conditional expectations states that for any random variable $Y$ and Radon–Nikodym derivative $L_T = \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\big|_{\mathcal{F}(T)}$:

    $$
    \mathbb{E}^T\!\left[Y\,|\,\mathcal{F}(t)\right] = \frac{\mathbb{E}^{\mathbb{Q}}\!\left[L_T\,Y\,|\,\mathcal{F}(t)\right]}{L_t}
    $$

    Setting $Y = X(T)/P(T,T) = X(T)$ and using $L_t = \frac{P(t,T)}{P(0,T)M(t)}$:

    $$\begin{array}{lllll}
    \displaystyle
    \mathbb{E}^T\!\left[X(T)\,|\,\mathcal{F}(t)\right]
    &=&\displaystyle
    \frac{\mathbb{E}^{\mathbb{Q}}\!\left[\frac{P(T,T)}{P(0,T)M(T)} X(T)\,\Big|\,\mathcal{F}(t)\right]}{\frac{P(t,T)}{P(0,T)M(t)}}
    \\[10pt]
    &=&\displaystyle
    \frac{M(t)}{P(t,T)}\,\mathbb{E}^{\mathbb{Q}}\!\left[\frac{X(T)}{M(T)}\,\Big|\,\mathcal{F}(t)\right]
    \\[10pt]
    &=&\displaystyle
    \frac{M(t)}{P(t,T)} \cdot \frac{X(t)}{M(t)} = \frac{X(t)}{P(t,T)}
    \end{array}$$

    This confirms $X(t)/P(t,T)$ is a $\mathbb{Q}^T$-martingale.

    **Why this is the natural choice for European derivatives:** A European derivative pays $V(T)$ at time $T$. Its price is $V(t) = P(t,T)\,\mathbb{E}^T[V(T)\,|\,\mathcal{F}(t)]$. Under $\mathbb{Q}^T$, the stochastic discount factor $e^{-\int_t^T r(s)\,ds}$ is absorbed into the measure change, so one only needs the distribution of $V(T)$ under $\mathbb{Q}^T$ — not the joint distribution of the payoff and the discount factor. This separation dramatically simplifies computations, especially when the payoff depends on the same interest rate driving the discount factor.

---

**Exercise 5.** In the numerical example, the option price is $V(0) = P(0,5)\,\mathbb{E}^5[\max(P(5,10) - 0.75, 0)]$. Explain why computing this expectation under $\mathbb{Q}^5$ is simpler than computing $\mathbb{E}^{\mathbb{Q}}[e^{-\int_0^5 r(s)\,ds}\max(P(5,10) - 0.75, 0)]$. What correlation structure makes the $\mathbb{Q}$-expectation more difficult?

??? success "Solution to Exercise 5"
    Under $\mathbb{Q}$, the expectation $\mathbb{E}^{\mathbb{Q}}[e^{-\int_0^5 r(s)\,ds}\max(P(5,10) - 0.75, 0)]$ involves two correlated stochastic quantities:

    1. The stochastic discount factor $e^{-\int_0^5 r(s)\,ds}$, which depends on the entire path of $r(s)$ for $s \in [0, 5]$.
    2. The bond price $P(5,10) = e^{A(5,10) + B(5,10)r(5)}$, which depends on $r(5)$.

    These are correlated because $r(5)$ is determined by the path $\{r(s)\}_{s \in [0,5]}$, and the discount factor is a functional of the same path. The payoff is large when $P(5,10)$ is high, i.e., when $r(5)$ is low. But when rates are low, the discount factor $e^{-\int_0^5 r(s)\,ds}$ is close to 1 (less discounting). So the discount factor and the payoff are positively correlated, making the $\mathbb{Q}$-expectation harder to evaluate because one must account for this dependence.

    Under $\mathbb{Q}^5$, the expectation $\mathbb{E}^5[\max(P(5,10) - 0.75, 0)]$ involves only the distribution of $r(5)$ under $\mathbb{Q}^5$, which is Gaussian. Since $P(5,10) = e^{A(5,10) + B(5,10)r(5)}$ is log-linear in the Gaussian variable $r(5)$, the payoff is the maximum of a lognormal variable minus a constant. This is a standard Black-Scholes-type integral with a known closed-form solution. The correlation structure is completely absorbed into the measure change, eliminating the need to handle the joint distribution.

---

**Exercise 6.** Consider two different $T$-forward measures, $\mathbb{Q}^{T_1}$ and $\mathbb{Q}^{T_2}$ with $T_1 < T_2$. Derive the Radon–Nikodym derivative $\frac{d\mathbb{Q}^{T_2}}{d\mathbb{Q}^{T_1}}\big|_{\mathcal{F}(t)}$ and the corresponding Girsanov transformation between the two measures.

??? success "Solution to Exercise 6"
    **Radon–Nikodym derivative between two forward measures:** Starting from their respective definitions relative to $\mathbb{Q}$:

    $$
    \frac{d\mathbb{Q}^{T_i}}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)} = \frac{P(t,T_i)}{P(0,T_i)\,M(t)}, \qquad i = 1, 2
    $$

    The Radon–Nikodym derivative from $\mathbb{Q}^{T_1}$ to $\mathbb{Q}^{T_2}$ is:

    $$
    \frac{d\mathbb{Q}^{T_2}}{d\mathbb{Q}^{T_1}}\Bigg|_{\mathcal{F}(t)} = \frac{d\mathbb{Q}^{T_2}/d\mathbb{Q}\big|_{\mathcal{F}(t)}}{d\mathbb{Q}^{T_1}/d\mathbb{Q}\big|_{\mathcal{F}(t)}} = \frac{P(t,T_2)/P(0,T_2)}{P(t,T_1)/P(0,T_1)} = \frac{P(t,T_2)\,P(0,T_1)}{P(t,T_1)\,P(0,T_2)}
    $$

    **Girsanov transformation:** Under $\mathbb{Q}^{T_1}$, the Brownian motion is $dW^{T_1}(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T_1)\,dt$. Under $\mathbb{Q}^{T_2}$, it is $dW^{T_2}(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T_2)\,dt$. Therefore the relationship between the two forward measure Brownian motions is:

    $$
    dW^{T_2}(t) = dW^{T_1}(t) - \left(\sigma_P(t,T_2) - \sigma_P(t,T_1)\right)dt
    $$

    In the Hull-White model, the drift adjustment is:

    $$
    \sigma_P(t,T_2) - \sigma_P(t,T_1) = -\frac{\sigma}{\lambda}\left(e^{-\lambda(T_1-t)} - e^{-\lambda(T_2-t)}\right)
    $$

    This is the Girsanov kernel for moving between the two forward measures, and it is deterministic, preserving the Gaussian framework.

---

**Exercise 7.** The forward LIBOR rate $L(t, T, T+\delta)$ defined by $1 + \delta L(t,T,T+\delta) = P(t,T)/P(t,T+\delta)$ is a martingale under $\mathbb{Q}^{T+\delta}$. Verify this claim for the Hull-White model and explain how this connects to the pricing of caplets.

??? success "Solution to Exercise 7"
    The forward LIBOR rate is defined by $1 + \delta L(t,T,T+\delta) = P(t,T)/P(t,T+\delta)$, so

    $$
    L(t,T,T+\delta) = \frac{1}{\delta}\!\left(\frac{P(t,T)}{P(t,T+\delta)} - 1\right)
    $$

    **Martingale property:** By the change-of-numeraire theorem, using $P(t,T+\delta)$ as numeraire, the ratio $P(t,T)/P(t,T+\delta)$ is a $\mathbb{Q}^{T+\delta}$-martingale. Since $L(t,T,T+\delta) = \frac{1}{\delta}(P(t,T)/P(t,T+\delta) - 1)$ is an affine transformation of a martingale (with constants $1/\delta$ and $-1/\delta$), it is also a $\mathbb{Q}^{T+\delta}$-martingale:

    $$
    \mathbb{E}^{T+\delta}\!\left[L(u,T,T+\delta)\,\Big|\,\mathcal{F}(t)\right] = L(t,T,T+\delta) \qquad \text{for all } t \leq u \leq T
    $$

    **Verification in the Hull-White model:** In the Hull-White model, $P(t,T)/P(t,T+\delta)$ can be written as $\exp(A^* + B^* r(t))$ for appropriate deterministic functions $A^*$ and $B^*$. Under $\mathbb{Q}^{T+\delta}$, $r(t)$ is Gaussian with a drift adjusted by $\sigma_P(t, T+\delta)$. The ratio $P(t,T)/P(t,T+\delta)$ is the discounted value of $P(T,T)/P(T,T+\delta) = 1/P(T,T+\delta)$ using $P(t,T+\delta)$ as numeraire, so it is indeed a martingale.

    **Connection to caplet pricing:** A caplet pays $\delta\max(L(T,T,T+\delta) - K, 0)$ at time $T+\delta$. Its price at time $t$ is:

    $$
    \text{Caplet}(t) = \delta\,P(t,T+\delta)\,\mathbb{E}^{T+\delta}\!\left[\max(L(T,T,T+\delta) - K, 0)\,\Big|\,\mathcal{F}(t)\right]
    $$

    Since $L(t,T,T+\delta)$ is a $\mathbb{Q}^{T+\delta}$-martingale and (in the Hull-White model) is a function of the Gaussian variable $r(T)$, this expectation can be evaluated in closed form, yielding a Black-type formula for the caplet price. The martingale property ensures that the forward LIBOR rate is the "correct" underlying for the option pricing formula, with $L(t,T,T+\delta)$ serving as the forward price of the caplet payoff.
