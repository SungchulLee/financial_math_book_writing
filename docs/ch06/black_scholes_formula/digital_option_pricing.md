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
