# Bond Options and Jamshidian's Decomposition

Options on bonds are among the most important interest rate derivatives, serving as building blocks for caps, floors, and callable bonds. In the Vasicek model, the Gaussian distribution of the short rate under the $T$-forward measure makes forward bond prices log-normal, leading to Black-Scholes-type closed-form formulas for zero-coupon bond (ZCB) options. Jamshidian's trick extends these formulas to coupon bond options by decomposing a single option on a portfolio of bonds into a portfolio of options on individual bonds. This decomposition relies on the **monotonicity** of Vasicek bond prices in the short rate---a property specific to one-factor models.

---

## European option on a zero-coupon bond

### Setup

Consider a European call option with:

- **Expiry**: $T$
- **Strike**: $K$
- **Underlying**: a zero-coupon bond maturing at $S > T$

The payoff at time $T$ is $(P(T,S) - K)^+$.

### Pricing under the T-forward measure

Using the $T$-forward measure:

$$
C(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}_t\!\left[(P(T,S) - K)^+\right]
$$

Under $\mathbb{Q}^T$, the short rate $r_T$ is Gaussian with mean $m^T$ and variance $v^2$:

$$
m^T = e^{-\kappa\tau}\,r_t + \theta(1 - e^{-\kappa\tau}) - \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2
$$

$$
v^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})
$$

where $\tau = T - t$.

The bond price at expiry is $P(T,S) = A(S-T)\,e^{-B(S-T)\,r_T}$, which is a decreasing function of the Gaussian random variable $r_T$. Therefore $\ln P(T,S)$ is normally distributed under $\mathbb{Q}^T$, and $P(T,S)$ is log-normal.

### Derivation of the ZCB call formula

Define the **critical rate** $r^*$ as the value of $r_T$ at which the option is exactly at the money:

$$
P(T,S)\big|_{r_T = r^*} = K \quad \Longleftrightarrow \quad r^* = \frac{\ln A(S-T) - \ln K}{B(S-T)}
$$

Since $P(T,S)$ is strictly decreasing in $r_T$, the option is in the money when $r_T < r^*$.

The call price becomes

$$
C(t) = P(t,T)\int_{-\infty}^{r^*}\!\left(A(S-T)\,e^{-B(S-T)\,r} - K\right)\phi\!\left(\frac{r - m^T}{v}\right)\frac{dr}{v}
$$

where $\phi$ is the standard normal density. Substituting $z = (r - m^T)/v$:

$$
C(t) = P(t,T)\!\left[A(S-T)\,e^{-B(S-T)\,m^T + \frac{1}{2}B(S-T)^2 v^2}\,\Phi(d_1) - K\,\Phi(d_2)\right]
$$

where $\Phi$ is the standard normal CDF. The key step uses the identity $\int_{-\infty}^a e^{-\beta z}\phi(z)\,dz = e^{\beta^2/2}\Phi(a + \beta)$.

Recognizing that $A(S-T)\,e^{-B(S-T)\,m^T + \frac{1}{2}B(S-T)^2 v^2}$ can be related to the forward bond price, the formula simplifies to

$$
\boxed{C(t) = P(t,S)\,\Phi(d_1) - K\,P(t,T)\,\Phi(d_2)}
$$

where

$$
d_1 = \frac{\ln\!\left(\frac{P(t,S)}{K\,P(t,T)}\right)}{\sigma_P} + \frac{\sigma_P}{2}, \qquad d_2 = d_1 - \sigma_P
$$

and the **bond option volatility** is

$$
\sigma_P = B(S-T)\,\sigma\,\sqrt{\frac{1 - e^{-2\kappa(T-t)}}{2\kappa}} = B(S-T)\,v
$$

### Put formula by put-call parity

The European put on the same ZCB is

$$
\boxed{P_{\text{put}}(t) = K\,P(t,T)\,\Phi(-d_2) - P(t,S)\,\Phi(-d_1)}
$$

**Verification.** Call minus put gives $P(t,S) - K\,P(t,T)$, which is the forward value of the bond minus the discounted strike---the correct put-call parity for bond options. $\square$

---

## Interpretation and structure of the formula

The ZCB option formula is structurally identical to the Black-Scholes formula:

| Black-Scholes | Vasicek ZCB option |
|---|---|
| Spot price $S_t$ | Forward bond price $P(t,S)/P(t,T)$ |
| Strike $K$ | Strike $K$ |
| Discount factor $e^{-r(T-t)}$ | Bond price $P(t,T)$ |
| Volatility $\sigma\sqrt{T-t}$ | Bond vol $\sigma_P$ |

The analogy arises because the forward bond price $P(T,S)$ is log-normal under $\mathbb{Q}^T$, just as the stock price is log-normal under $\mathbb{Q}$ in the Black-Scholes model.

The bond option volatility $\sigma_P = B(S-T) \cdot v$ has two components:

1. **$B(S-T)$**: the sensitivity of the underlying bond to the short rate (duration effect)
2. **$v = \sigma\sqrt{(1 - e^{-2\kappa\tau})/(2\kappa)}$**: the standard deviation of $r_T$ under $\mathbb{Q}^T$

---

## Jamshidian's trick for coupon bond options

### The problem

A European call on a coupon bond with cash flows $c_i$ at times $S_i > T$ (for $i = 1, \ldots, n$) has payoff

$$
\left(\sum_{i=1}^n c_i\,P(T, S_i) - K\right)^+
$$

This is an option on a **portfolio** of ZCBs, not a portfolio of options. In general, options on portfolios cannot be decomposed into portfolios of options.

### The monotonicity argument

In the Vasicek model, each bond price $P(T, S_i) = A(S_i - T)\,e^{-B(S_i - T)\,r_T}$ is a **strictly decreasing** function of $r_T$. Therefore the coupon bond value

$$
CB(r_T) = \sum_{i=1}^n c_i\,P(T, S_i)
$$

is also strictly decreasing in $r_T$, since it is a positive linear combination of strictly decreasing functions.

### The critical rate

Define $r^*$ as the unique solution of

$$
\sum_{i=1}^n c_i\,P(T, S_i)\big|_{r_T = r^*} = K
$$

The option is in the money when $r_T < r^*$ (because $CB$ decreases in $r_T$).

### Decomposition

Define the **individual strikes** $K_i = P(T, S_i)\big|_{r_T = r^*} = A(S_i - T)\,e^{-B(S_i - T)\,r^*}$. Note that $\sum_i c_i K_i = K$ by construction.

Since each $P(T, S_i)$ is decreasing in $r_T$, we have $P(T, S_i) > K_i$ if and only if $r_T < r^*$. Therefore:

$$
\left(\sum_i c_i\,P(T,S_i) - K\right)^+ = \sum_i c_i\,\left(P(T,S_i) - K_i\right)^+
$$

???+ note "Proof of the decomposition"
    When $r_T < r^*$: both sides equal $\sum_i c_i(P(T,S_i) - K_i) = CB(r_T) - K > 0$.
    When $r_T \geq r^*$: the left side is zero because $CB(r_T) \leq K$. On the right side, each $P(T,S_i) \leq K_i$ (by monotonicity), so each term is zero. $\square$

### Result

The coupon bond call decomposes into a portfolio of ZCB calls:

$$
\boxed{C_{\text{CB}}(t) = \sum_{i=1}^n c_i\,C_{\text{ZCB}}(t;\, K_i,\, T,\, S_i)}
$$

where $C_{\text{ZCB}}(t; K_i, T, S_i) = P(t,S_i)\,\Phi(d_1^{(i)}) - K_i\,P(t,T)\,\Phi(d_2^{(i)})$ with

$$
d_1^{(i)} = \frac{\ln\!\left(\frac{P(t,S_i)}{K_i\,P(t,T)}\right)}{\sigma_{P,i}} + \frac{\sigma_{P,i}}{2}, \qquad \sigma_{P,i} = B(S_i - T)\,v
$$

The only numerical step is finding $r^*$, which requires a one-dimensional root search (e.g., bisection or Newton's method).

---

## Numerical example

Consider a 3-year European call on a 5-year annual coupon bond with face value \$100 and 4% coupon rate. Vasicek parameters: $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $r_0 = 0.04$. Strike $K = \$100$.

**Step 1**: Cash flows at years 4 and 5: $c_1 = \$4$ at $S_1 = 4$, $c_2 = \$104$ at $S_2 = 5$.

**Step 2**: Compute $P(0,3)$, $P(0,4)$, $P(0,5)$ using the Vasicek formula.

| Bond | $B(\tau)$ | $\ln A(\tau)$ | $P(0,\tau)$ |
|:-:|:-:|:-:|:-:|
| $P(0,3)$ | 2.222 | $-0.0151$ | 0.8972 |
| $P(0,4)$ | 2.637 | $-0.0237$ | 0.8750 |
| $P(0,5)$ | 2.940 | $-0.0327$ | 0.8530 |

**Step 3**: Find $r^*$ by solving $4\,P(3,4;r^*) + 104\,P(3,5;r^*) = 100$.

Numerically, $r^* \approx 0.0453$.

**Step 4**: Compute individual strikes: $K_1 = P(3,4;r^*) \approx 0.9706$, $K_2 = P(3,5;r^*) \approx 0.9249$. Verify: $4 \times 0.9706 + 104 \times 0.9249 \approx 100$.

**Step 5**: Price each ZCB call and sum: $C_{\text{CB}} = 4\,C(K_1, 3, 4) + 104\,C(K_2, 3, 5)$.

---

## Limitations of Jamshidian's trick

Jamshidian's decomposition requires:

1. **One-factor model**: The monotonicity of each $P(T, S_i)$ in a single state variable is essential. In multi-factor models, bond prices are not monotone in any single variable, and the decomposition fails.

2. **Monotone bond prices**: The decomposition uses the fact that $\partial P / \partial r < 0$, which holds for affine models. In models where bond prices are not monotone (e.g., certain non-affine specifications), the trick does not apply.

3. **European exercise**: The decomposition applies at a single exercise date. American or Bermudan bond options require tree or PDE methods.

For multi-factor models, alternative approaches include Monte Carlo simulation with regression (Longstaff-Schwartz) or Fourier transform methods.

---

## Summary

The Vasicek model delivers closed-form European bond option prices through two key ingredients. First, the Gaussian distribution of $r_T$ under the $T$-forward measure makes ZCB forward prices log-normal, producing Black-Scholes-type call and put formulas with bond option volatility $\sigma_P = B(S-T)\,\sigma\sqrt{(1-e^{-2\kappa\tau})/(2\kappa)}$. Second, Jamshidian's trick exploits the monotonicity of bond prices in the short rate to decompose coupon bond options into portfolios of ZCB options, each priced by the same formula with individual strikes determined by a single critical rate $r^*$.

---
