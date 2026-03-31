# Digital Option Pricing via Girsanov's Theorem

## Payoff Structure

A **digital (cash-or-nothing) call option** pays a fixed amount $1$ if the underlying asset exceeds the strike price $K$ at maturity $T$:

$$
\text{Payoff at } T: \quad \mathbf{1}_{\{S_T > K\}}
$$

Unlike a standard European call, which pays the excess $(S_T - K)^+$, the digital call pays a **flat amount** regardless of how far in the money it finishes.

---

## Risk-Neutral Pricing

Under the risk-neutral measure $\mathbb{Q}$, the price of any derivative is the discounted expected payoff:

$$
D_0 := \mathbb{E}^{\mathbb{Q}}\left[ e^{-rT} \mathbf{1}_{\{S_T > K\}} \right]
= e^{-rT} \mathbb{Q}(S_T > K)
$$

### Distribution of S_T under Q

By Girsanov's theorem, the stock price dynamics under $\mathbb{Q}$ are:

$$
dS_t = r S_t \, dt + \sigma S_t \, d\tilde{W}_t
$$

where $\tilde{W}_t$ is a $\mathbb{Q}$-Brownian motion. Solving this SDE via Itô's lemma:

$$
S_T = S_0 \exp\left[\left(r - \tfrac{1}{2}\sigma^2\right)T + \sigma \tilde{W}_T\right]
$$

Therefore:

$$
\log S_T \sim \mathcal{N}\left(\log S_0 + \left(r - \tfrac{1}{2}\sigma^2\right)T, \; \sigma^2 T\right)
$$

### Computing Q(S_T > K)

$$
\mathbb{Q}(S_T > K) = \mathbb{Q}(\log S_T > \log K)
$$

Standardizing:

$$
\mathbb{Q}\left(\frac{\log S_T - \left[\log S_0 + (r - \frac{1}{2}\sigma^2)T\right]}{\sigma\sqrt{T}} > \frac{\log K - \left[\log S_0 + (r - \frac{1}{2}\sigma^2)T\right]}{\sigma\sqrt{T}}\right)
$$

$$
= \mathbb{Q}\left(Z > -d_2\right) = \Phi(d_2)
$$

where $Z \sim \mathcal{N}(0,1)$ and:

$$
d_2 = \frac{\log(S_0 / K) + \left(r - \frac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}}
$$

---

## Final Result

$$
\boxed{D_0 = e^{-rT}\,\Phi(d_2)}
$$

This is the fair price of a digital call option paying $1$ at maturity $T$ if $S_T > K$.

---

## Connection to Black–Scholes Formula

The Black–Scholes formula for a European call can be written as:

$$
C_0 = S_0\,\Phi(d_1) - K e^{-rT}\,\Phi(d_2)
$$

The second term $K e^{-rT}\,\Phi(d_2)$ is exactly $K$ times the digital call price. This reveals an important decomposition:

- $\Phi(d_2) = \mathbb{Q}(S_T > K)$: the **risk-neutral probability** that the call finishes in the money.
- $\Phi(d_1) = \mathbb{Q}^S(S_T > K)$: the probability under the **stock numéraire measure**.

The digital call price thus appears naturally as a component of the standard Black–Scholes formula.

---

## Digital Put Option

By symmetry, a digital put paying $1$ if $S_T < K$ has price:

$$
D_0^{\text{put}} = e^{-rT}\,\Phi(-d_2) = e^{-rT}\left[1 - \Phi(d_2)\right]
$$

The sum of digital call and digital put prices equals the price of a zero-coupon bond:

$$
D_0^{\text{call}} + D_0^{\text{put}} = e^{-rT}
$$

---

## Hedging Considerations

The delta of a digital call is:

$$
\Delta_{\text{digital}} = \frac{\partial D_0}{\partial S_0} = e^{-rT} \frac{\phi(d_2)}{S_0 \sigma \sqrt{T}}
$$

where $\phi$ is the standard normal density. Near expiry ($T \to 0$) and near the strike ($S_0 \approx K$), this delta becomes extremely large, making digital options **notoriously difficult to hedge** in practice. This discontinuity in the payoff creates significant gamma risk near maturity.

---

## Exercises

**Exercise 1.** Derive the price of a digital call option that pays an amount $Q$ (instead of $1$) at maturity if $S_T > K$. Express the result in terms of $d_2$ and verify that your formula reduces to the standard result when $Q = 1$.

---

**Exercise 2.** Show that the digital call price $D_0 = e^{-rT}\Phi(d_2)$ can be recovered by differentiating the Black-Scholes call price with respect to the strike:

$$
D_0 = -\frac{\partial C_0}{\partial K}
$$

Carry out the differentiation explicitly, using the relationship $\frac{\partial d_1}{\partial K} = \frac{\partial d_2}{\partial K} = -\frac{1}{K \sigma \sqrt{T}}$ and the identity $S_0 \phi(d_1) = K e^{-rT} \phi(d_2)$.

---

**Exercise 3.** A digital call and a digital put on the same underlying with the same strike and maturity have prices $D_0^{\text{call}}$ and $D_0^{\text{put}}$. Prove that their sum equals $e^{-rT}$. What is the financial interpretation of this identity?

---

**Exercise 4.** Compute the gamma of a digital call option. Show that the gamma is:

$$
\Gamma_{\text{digital}} = -e^{-rT} \frac{\phi(d_2) \, d_1}{S_0^2 \sigma^2 T}
$$

At what value of $S_0$ (in terms of $K$, $r$, $\sigma$, $T$) does the digital call gamma equal zero?

---

**Exercise 5.** Consider a **double digital option** (also called a digital range option) that pays $1$ at maturity if $K_1 < S_T < K_2$ for $K_1 < K_2$. Express the price of this option in terms of the standard normal CDF $\Phi$. Compute its price when $S_0 = 100$, $K_1 = 95$, $K_2 = 105$, $r = 5\%$, $\sigma = 20\%$, and $T = 0.5$.

---

**Exercise 6.** A trader replicates a digital call by constructing a **call spread**: buying a call at strike $K - \epsilon$ and selling a call at strike $K$, then scaling by $1/\epsilon$. Show that in the limit $\epsilon \to 0$, this replicating portfolio converges to the digital call payoff. What practical difficulties arise for small but nonzero $\epsilon$?

---

**Exercise 7.** The digital call delta $\Delta_{\text{digital}} = e^{-rT} \frac{\phi(d_2)}{S_0 \sigma \sqrt{T}}$ diverges as $T \to 0$ when $S_0 = K$. Compute the delta explicitly for $S_0 = K = 100$, $\sigma = 25\%$, $r = 3\%$, and $T \in \{1, 0.1, 0.01, 0.001\}$. Discuss why this behavior makes near-expiry digital options extremely difficult to delta-hedge in practice.

---

## Solutions

??? success "Solution to Exercise 1"
    The digital call paying $1$ at maturity has price $D_0 = e^{-rT}\Phi(d_2)$. By linearity of expectation, a digital call paying $Q$ has price:

    $$
    D_0^{(Q)} = Q \cdot e^{-rT}\Phi(d_2)
    $$

    This follows because the payoff is $Q \cdot \mathbf{1}_{\{S_T > K\}}$, so:

    $$
    D_0^{(Q)} = e^{-rT}\mathbb{E}^{\mathbb{Q}}[Q \cdot \mathbf{1}_{\{S_T > K\}}] = Q \cdot e^{-rT}\mathbb{Q}(S_T > K) = Q \cdot e^{-rT}\Phi(d_2)
    $$

    When $Q = 1$: $D_0^{(1)} = e^{-rT}\Phi(d_2)$, which is the standard result. ✓

??? success "Solution to Exercise 2"
    The Black-Scholes call price is $C_0 = S_0\Phi(d_1) - Ke^{-rT}\Phi(d_2)$.

    Differentiating with respect to $K$:

    $$
    \frac{\partial C_0}{\partial K} = S_0 \phi(d_1)\frac{\partial d_1}{\partial K} - e^{-rT}\Phi(d_2) - Ke^{-rT}\phi(d_2)\frac{\partial d_2}{\partial K}
    $$

    Using $\frac{\partial d_1}{\partial K} = \frac{\partial d_2}{\partial K} = -\frac{1}{K\sigma\sqrt{T}}$:

    $$
    \frac{\partial C_0}{\partial K} = -\frac{S_0\phi(d_1)}{K\sigma\sqrt{T}} - e^{-rT}\Phi(d_2) + \frac{Ke^{-rT}\phi(d_2)}{K\sigma\sqrt{T}}
    $$

    $$
    = -e^{-rT}\Phi(d_2) + \frac{1}{\sigma\sqrt{T}}\left[-S_0\phi(d_1)/K + e^{-rT}\phi(d_2)\right]
    $$

    Now we use the identity $S_0\phi(d_1) = Ke^{-rT}\phi(d_2)$. This identity follows from:

    $$
    \frac{\phi(d_1)}{\phi(d_2)} = \exp\left(-\frac{d_1^2 - d_2^2}{2}\right) = \exp\left(-\frac{(d_1-d_2)(d_1+d_2)}{2}\right)
    $$

    Since $d_1 - d_2 = \sigma\sqrt{T}$ and $d_1 + d_2 = \frac{2\ln(S_0/K) + 2rT}{\sigma\sqrt{T}} - \sigma\sqrt{T} + \sigma\sqrt{T}$... more directly, one can verify $S_0\phi(d_1) = Ke^{-rT}\phi(d_2)$ by showing $\ln(S_0/K) + rT = \frac{1}{2}(d_1^2 - d_2^2)$.

    With this identity, $S_0\phi(d_1)/K = e^{-rT}\phi(d_2)$, so the bracketed term vanishes:

    $$
    \frac{\partial C_0}{\partial K} = -e^{-rT}\Phi(d_2)
    $$

    Therefore:

    $$
    D_0 = e^{-rT}\Phi(d_2) = -\frac{\partial C_0}{\partial K}
    $$

??? success "Solution to Exercise 3"
    The digital call price is $D_0^{\text{call}} = e^{-rT}\Phi(d_2)$ and the digital put price is $D_0^{\text{put}} = e^{-rT}\Phi(-d_2)$.

    Their sum:

    $$
    D_0^{\text{call}} + D_0^{\text{put}} = e^{-rT}\Phi(d_2) + e^{-rT}\Phi(-d_2) = e^{-rT}[\Phi(d_2) + \Phi(-d_2)]
    $$

    Using the symmetry property $\Phi(x) + \Phi(-x) = 1$:

    $$
    D_0^{\text{call}} + D_0^{\text{put}} = e^{-rT} \cdot 1 = e^{-rT}
    $$

    **Financial interpretation**: Holding both a digital call and a digital put with the same strike guarantees a payment of $1$ at maturity regardless of where $S_T$ ends up (either $S_T > K$ or $S_T \leq K$ must hold). This is equivalent to holding a zero-coupon bond that pays $1$ at time $T$, whose present value is $e^{-rT}$.

??? success "Solution to Exercise 4"
    The digital call delta is:

    $$
    \Delta_{\text{digital}} = \frac{\partial D_0}{\partial S_0} = e^{-rT}\frac{\phi(d_2)}{S_0\sigma\sqrt{T}}
    $$

    Differentiating again with respect to $S_0$:

    $$
    \Gamma_{\text{digital}} = \frac{\partial \Delta_{\text{digital}}}{\partial S_0} = e^{-rT}\frac{\partial}{\partial S_0}\left[\frac{\phi(d_2)}{S_0\sigma\sqrt{T}}\right]
    $$

    Using the product rule with $\frac{\partial d_2}{\partial S_0} = \frac{1}{S_0\sigma\sqrt{T}}$ and $\phi'(x) = -x\phi(x)$:

    $$
    \frac{\partial}{\partial S_0}\left[\frac{\phi(d_2)}{S_0\sigma\sqrt{T}}\right] = \frac{1}{S_0\sigma\sqrt{T}}\left[\phi'(d_2)\frac{1}{S_0\sigma\sqrt{T}}\right] - \frac{\phi(d_2)}{S_0^2\sigma\sqrt{T}}
    $$

    $$
    = \frac{-d_2\phi(d_2)}{S_0^2\sigma^2 T} - \frac{\phi(d_2)}{S_0^2\sigma\sqrt{T}}
    $$

    Factoring out $\frac{\phi(d_2)}{S_0^2\sigma\sqrt{T}}$... after careful algebra:

    $$
    \Gamma_{\text{digital}} = -e^{-rT}\frac{\phi(d_2)\,d_1}{S_0^2\sigma^2 T}
    $$

    This uses the relation $d_2/(S_0\sigma\sqrt{T}) + 1/(S_0) = d_1/(S_0\sigma\sqrt{T}) \cdot \sigma\sqrt{T}/S_0$... more directly, one can show the result by noting that $d_2 + \frac{1}{\sigma\sqrt{T}} \cdot \sigma\sqrt{T} = d_2 + 1$ leads to $d_1$ appearing via $d_1 = d_2 + \sigma\sqrt{T}$ and the chain rule.

    **Gamma equals zero** when $d_1 = 0$, which occurs when:

    $$
    \ln(S_0/K) + \left(r + \frac{1}{2}\sigma^2\right)T = 0
    $$

    $$
    S_0 = K\exp\left[-\left(r + \frac{1}{2}\sigma^2\right)T\right]
    $$

    At this stock price, the digital call delta reaches its maximum (or minimum), and the gamma changes sign.

??? success "Solution to Exercise 5"
    The double digital pays $1$ if $K_1 < S_T < K_2$. This can be decomposed as:

    $$
    \mathbf{1}_{\{K_1 < S_T < K_2\}} = \mathbf{1}_{\{S_T > K_1\}} - \mathbf{1}_{\{S_T > K_2\}}
    $$

    (a digital call at $K_1$ minus a digital call at $K_2$). Therefore:

    $$
    D_0^{\text{range}} = e^{-rT}[\Phi(d_2(K_1)) - \Phi(d_2(K_2))]
    $$

    where $d_2(K) = \frac{\ln(S_0/K) + (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$.

    **Numerical computation** with $S_0 = 100$, $K_1 = 95$, $K_2 = 105$, $r = 0.05$, $\sigma = 0.20$, $T = 0.5$:

    For $K_1 = 95$:

    $$
    d_2(95) = \frac{\ln(100/95) + (0.05 - 0.02) \times 0.5}{0.20\sqrt{0.5}} = \frac{0.05129 + 0.015}{0.14142} = \frac{0.06629}{0.14142} = 0.4688
    $$

    For $K_2 = 105$:

    $$
    d_2(105) = \frac{\ln(100/105) + 0.015}{0.14142} = \frac{-0.04879 + 0.015}{0.14142} = \frac{-0.03379}{0.14142} = -0.2390
    $$

    $$
    \Phi(0.4688) = 0.6804, \quad \Phi(-0.2390) = 0.4055
    $$

    $$
    D_0^{\text{range}} = e^{-0.05 \times 0.5}(0.6804 - 0.4055) = 0.9753 \times 0.2749 = 0.2681
    $$

    The double digital option is worth approximately $\$0.27$.

??? success "Solution to Exercise 6"
    The call spread replicating portfolio has payoff:

    $$
    \Pi_T = \frac{1}{\epsilon}\left[(S_T - (K-\epsilon))^+ - (S_T - K)^+\right]
    $$

    **Case 1: $S_T \leq K - \epsilon$**: Both calls expire worthless. $\Pi_T = 0$.

    **Case 2: $K - \epsilon < S_T \leq K$**: Only the first call is ITM. $\Pi_T = \frac{S_T - K + \epsilon}{\epsilon} \in (0, 1]$.

    **Case 3: $S_T > K$**: Both calls are ITM. $\Pi_T = \frac{(S_T - K + \epsilon) - (S_T - K)}{\epsilon} = 1$.

    As $\epsilon \to 0$, in Case 2 the region $(K-\epsilon, K]$ shrinks to the single point $\{K\}$ (measure zero under continuous distributions), so:

    $$
    \lim_{\epsilon \to 0} \Pi_T = \begin{cases} 0 & \text{if } S_T < K \\ 1 & \text{if } S_T > K \end{cases} = \mathbf{1}_{\{S_T > K\}}
    $$

    This is exactly the digital call payoff.

    **Practical difficulties for small but nonzero $\epsilon$**:

    1. The position involves $1/\epsilon$ units of each call, so the notional size becomes very large.
    2. The hedge requires frequent rebalancing near the strike, with large position sizes amplifying transaction costs.
    3. The payoff is not exactly $0$ or $1$ in the region $(K-\epsilon, K]$, creating basis risk.
    4. Near expiry, the gamma of the call spread becomes extremely large, making delta-hedging unstable.

??? success "Solution to Exercise 7"
    With $S_0 = K = 100$, $\sigma = 0.25$, $r = 0.03$:

    $$
    d_2 = \frac{\ln(1) + (0.03 - 0.03125)T}{0.25\sqrt{T}} = \frac{-0.00125\,T}{0.25\sqrt{T}} = \frac{-0.005\sqrt{T}}{1} = -0.005\sqrt{T}
    $$

    For small $T$, $d_2 \approx 0$, so $\phi(d_2) \approx \phi(0) = \frac{1}{\sqrt{2\pi}} \approx 0.3989$.

    $$
    \Delta_{\text{digital}} = e^{-rT}\frac{0.3989}{100 \times 0.25 \times \sqrt{T}} = \frac{e^{-rT} \times 0.3989}{25\sqrt{T}}
    $$

    | $T$ | $\sqrt{T}$ | $e^{-rT}$ | $\Delta_{\text{digital}}$ |
    |---|---|---|---|
    | 1.000 | 1.0000 | 0.9704 | 0.01548 |
    | 0.100 | 0.3162 | 0.9970 | 0.05029 |
    | 0.010 | 0.1000 | 0.9997 | 0.15956 |
    | 0.001 | 0.03162 | 1.0000 | 0.50451 |

    As $T \to 0$, $\Delta \propto 1/\sqrt{T} \to \infty$.

    **Why this makes hedging extremely difficult**: The diverging delta means that to maintain a delta-neutral hedge, the trader must hold an increasingly large number of shares as expiry approaches. A tiny move in the stock price around $K$ flips the digital payoff from $0$ to $1$ (or vice versa), requiring the hedge to swing from $0$ shares to a very large position. In practice, this means enormous transaction costs, as the hedge must be rebalanced constantly with large position changes. Any discrete rebalancing interval results in significant hedging error, and bid-ask spreads make the rebalancing prohibitively expensive. This is the fundamental reason why digital options near expiry are among the most difficult derivatives to manage.
