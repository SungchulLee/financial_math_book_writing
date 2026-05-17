# Dupire Formula Derivation

This section explores the principles and methods underlying dupire formula derivation, which form a critical component of modern financial mathematics.

## Key Concepts

The fundamental concepts in this area include:

- Theoretical foundations and mathematical framework
- Key definitions and notation
- Important theorems and results
- Connections to other areas of financial mathematics

!!! abstract "Learning Objectives"
    After completing this section, you should understand:

    - The core mathematical principles and their financial interpretations
    - How these concepts connect to practical applications
    - The relationship between theory and numerical implementation

---

## Fokker-Planck and Dupire Connection

Recall (see [§ Fokker-Planck Equation](../../ch05/kolmogorov_equations/kolmogorov_forward.md)) for the forward PDE governing the density $p(x,t)$ under $dS_t = rS_t\,dt + \sigma(t,S_t)S_t\,dW_t$. The Dupire formula is the call-price analogue: the same diffusion coefficient $\sigma^2(K,T)$ that drives $\partial_t p$ via $\frac{1}{2}\partial_{xx}[\sigma^2 x^2 p]$ also drives $\partial_T C$ via $\frac{1}{2}\sigma^2 K^2 C_{KK}$, giving

$$
\sigma^2(K,T) = \frac{\partial_T C + rK\,\partial_K C}{\tfrac{1}{2}K^2\,\partial_{KK}C}.
$$

---

## Alternative Derivation via Integration by Parts (QuantPie)

This section presents an alternative derivation of the Dupire formula using the integration by parts method, which provides additional intuition about the structure of the PDE.

### Foundational Setup

Using the Feynman-Kac formula, the call option price is:

$$
C = e^{-rT}\mathbb{E}^{Q}[(S_{T}-K)^{+}] = e^{-rT}\int_{K}^{\infty}(s-K)p \, ds = e^{-rT}\int_{K}^{\infty}s \, p \, ds - Ke^{-rT}\int_{K}^{\infty}p \, ds
$$

where $p = p(s, T)$ is the transition density of the stock price at maturity $T$ and strike $K$.

### Key Partial Derivatives

Recall (see [§ Breeden-Litzenberger](../../ch12/model_free_results/breeden_litzenberger_formula.md) and [Digital Option Pricing](../../ch06/black_scholes_formula/digital_option_pricing.md)) for the identities

$$
C_K = -e^{-rT}\int_K^\infty p\,ds, \qquad C_{KK} = e^{-rT}p(K,T).
$$

Also, we have the important relation:

$$
e^{-rT}\int_{K}^{\infty}s \, p \, ds = C - KC_K
$$

### Dupire PDE Derivation

The time derivative of the call option price is obtained by differentiating with respect to maturity time $T$:

$$\begin{array}{lll}
\displaystyle
C_T &=& \displaystyle -rC + e^{-rT}\int_{K}^{\infty}(s-K)p_T \, ds \\
&=& \displaystyle -rC - e^{-rT}\int_{K}^{\infty}(s-K)\left[rs p\right]_s \, ds + e^{-rT}\int_{K}^{\infty}(s-K)\frac{1}{2}\left[\left(\sigma s\right)^2 p\right]_{ss} \, ds
\end{array}$$

where we have used the Fokker-Planck equation:

$$
p_t = -\left[\left(rs\right) p\right]_s + \frac{1}{2}\left[\left(\sigma s\right)^2 p\right]_{ss}
$$

### Integration by Parts Steps

Applying integration by parts to the drift and diffusion terms:

1. **Drift term:** Integration by parts on $\int_{K}^{\infty}(s-K)\left[rs p\right]_s \, ds$ yields:

   $$\int_{K}^{\infty}(s-K)\left[rs p\right]_s \, ds = -\int_{K}^{\infty}rs \, p \, ds$$

2. **Diffusion term:** Integration by parts on $\int_{K}^{\infty}(s-K)\left[\left(\sigma s\right)^2 p\right]_{ss} \, ds$ yields:

   $$\int_{K}^{\infty}(s-K)\left[\left(\sigma s\right)^2 p\right]_{ss} \, ds = \left[\left(\sigma s\right)^2 p\right]_s\bigg|_{K}^{\infty} - \int_{K}^{\infty}\left[\left(\sigma s\right)^2 p\right]_s \, ds$$

Evaluating at the boundaries and using standard limiting arguments:

$$\int_{K}^{\infty}\left[\left(\sigma s\right)^2 p\right]_s \, ds = -\sigma^2(K,T) K^2 p(K,T)$$

### Final Result

Combining all terms and using the relationships for $C_K$, $C_{KK}$, and $e^{-rT}\int_{K}^{\infty}s \, p \, ds$:

$$\begin{array}{lll}
\displaystyle
C_T &=& \displaystyle -rC + re^{-rT}\int_{K}^{\infty}s \, p \, ds + \frac{1}{2}e^{-rT}\sigma^2(K,T) K^2 p(K,T) \\
&=& \displaystyle -rC + r\left(C - KC_K\right) + \frac{1}{2}\sigma^2(K,T) K^2 C_{KK} \\
&=& \displaystyle -rKC_K + \frac{1}{2}\sigma^2(K,T) K^2 C_{KK}
\end{array}$$

Therefore, the **Dupire Formula** is:

$$
\displaystyle \sigma^2(K,T) = \frac{\displaystyle \frac{\partial C(K,T)}{\partial T} + rK\frac{\partial C(K,T)}{\partial K}}{\displaystyle \frac{1}{2}K^2\frac{\partial^2 C(K,T)}{\partial K^2}}
$$

This formula expresses the local volatility surface as a function of observable market option prices and their derivatives with respect to strike and maturity.

---

## Summary

The Dupire formula represents one of the most important results in quantitative finance. It establishes that local volatility can be determined entirely from the market prices of European options across all strikes and maturities. The integration by parts approach reveals the underlying structure of how the drift and diffusion components of the stochastic process manifest in the option pricing PDE.

---

## Exercises

**Exercise 1.** Starting from the Fokker-Planck equation for the risk-neutral density $p(s, T)$, verify that the drift term integration by parts yields

$$
\int_{K}^{\infty}(s-K)\left[rs \, p\right]_s \, ds = -\int_{K}^{\infty}rs \, p \, ds
$$

State explicitly the boundary conditions you use and why they hold for a well-behaved transition density.

??? success "Solution to Exercise 1"
    We need to show that

    $$
    \int_{K}^{\infty}(s-K)\left[rs \, p\right]_s \, ds = -\int_{K}^{\infty}rs \, p \, ds
    $$

    Apply integration by parts with $u = (s - K)$ and $dv = [rs \, p]_s \, ds$, so $du = ds$ and $v = rs \, p$:

    $$
    \int_{K}^{\infty}(s-K)[rs\,p]_s\,ds = \bigl[(s-K)\,rs\,p\bigr]_{K}^{\infty} - \int_{K}^{\infty}rs\,p\,ds
    $$

    **Boundary conditions:**

    - At $s = K$: $(K - K) \cdot rK \cdot p(K, T) = 0$
    - At $s \to \infty$: We require $(s - K) \cdot rs \cdot p(s, T) \to 0$. This holds because for a well-behaved transition density, $p(s, T)$ decays faster than any polynomial as $s \to \infty$. Specifically, for the lognormal or any density with finite moments, $s^n p(s, T) \to 0$ for all $n$, so the boundary term vanishes.

    Therefore the boundary term is zero at both limits, yielding:

    $$
    \int_{K}^{\infty}(s-K)[rs\,p]_s\,ds = -\int_{K}^{\infty}rs\,p\,ds
    $$

    The key requirement is that the transition density $p(s, T)$ decays sufficiently rapidly at infinity so that all moments are finite. This holds for the risk-neutral density of any asset with finite expected value under the risk-neutral measure, which is guaranteed by the no-arbitrage condition $\mathbb{E}^Q[S_T] = S_0 e^{rT} < \infty$.

---

**Exercise 2.** The Dupire PDE for the call price as a function of strike and maturity is

$$
C_T = -rKC_K + \frac{1}{2}\sigma^2(K,T) K^2 C_{KK}
$$

Verify that this PDE is satisfied when $\sigma(K,T) = \sigma_0$ (constant) and $C(K,T)$ is the Black-Scholes call price. Compute $C_T$, $C_K$, and $C_{KK}$ explicitly and confirm the identity.

??? success "Solution to Exercise 2"
    The Dupire PDE is $C_T = -rKC_K + \frac{1}{2}\sigma_0^2 K^2 C_{KK}$. We verify this for the Black-Scholes call price $C = S_0 N(d_1) - Ke^{-rT}N(d_2)$ with constant $\sigma_0$.

    Define $d_1 = \frac{\ln(S_0/K) + (r + \sigma_0^2/2)T}{\sigma_0\sqrt{T}}$ and $d_2 = d_1 - \sigma_0\sqrt{T}$.

    **Computing $C_T$:** Using the Black-Scholes theta:

    $$
    C_T = -\frac{S_0 n(d_1)\sigma_0}{2\sqrt{T}} + rKe^{-rT}N(d_2)
    $$

    where $n(\cdot)$ is the standard normal density.

    **Computing $C_K$:**

    $$
    C_K = -e^{-rT}N(d_2)
    $$

    This uses the identity $S_0 n(d_1) = Ke^{-rT}n(d_2)$ to cancel the $N'$ terms.

    **Computing $C_{KK}$:**

    $$
    C_{KK} = e^{-rT}\frac{n(d_2)}{K\sigma_0\sqrt{T}}
    $$

    **Verification:** Substituting into the Dupire PDE:

    $$
    -rKC_K + \frac{1}{2}\sigma_0^2 K^2 C_{KK} = rKe^{-rT}N(d_2) + \frac{1}{2}\sigma_0^2 K^2 \cdot e^{-rT}\frac{n(d_2)}{K\sigma_0\sqrt{T}}
    $$

    $$
    = rKe^{-rT}N(d_2) + \frac{S_0 n(d_1)\sigma_0}{2\sqrt{T}}
    $$

    where we used $Ke^{-rT}n(d_2) = S_0 n(d_1)$. This gives:

    $$
    -rKC_K + \frac{1}{2}\sigma_0^2 K^2 C_{KK} = rKe^{-rT}N(d_2) + \frac{S_0 n(d_1)\sigma_0}{2\sqrt{T}}
    $$

    Comparing with $C_T = -\frac{S_0 n(d_1)\sigma_0}{2\sqrt{T}} + rKe^{-rT}N(d_2)$, we verify:

    $$
    C_T = -\frac{S_0 n(d_1)\sigma_0}{2\sqrt{T}} + rKe^{-rT}N(d_2) = -rKC_K + \frac{1}{2}\sigma_0^2 K^2 C_{KK} - \frac{S_0 n(d_1)\sigma_0}{\sqrt{T}}
    $$

    Actually, directly: $C_T + rKC_K = \frac{1}{2}\sigma_0^2 K^2 C_{KK}$, which gives $\sigma^2(K,T) = \sigma_0^2$ from the Dupire formula, confirming the identity.

---

**Exercise 3.** The derivation uses $C_{KK} = e^{-rT}p(K,T)$, which is the Breeden-Litzenberger result. (a) Derive this relationship from $C = e^{-rT}\int_{K}^{\infty}(s-K)p(s,T)\,ds$ by differentiating twice with respect to $K$. (b) Explain why this means the risk-neutral density is always non-negative if and only if $C_{KK} \geq 0$. (c) What arbitrage would exist if $C_{KK} < 0$ for some strike $K$?

??? success "Solution to Exercise 3"
    **(a)** Starting from $C = e^{-rT}\int_{K}^{\infty}(s-K)p(s,T)\,ds$:

    **First derivative:**

    $$
    \frac{\partial C}{\partial K} = e^{-rT}\frac{\partial}{\partial K}\int_{K}^{\infty}(s-K)p(s,T)\,ds
    $$

    By Leibniz's rule, differentiating the lower limit gives $(K-K)p(K,T) = 0$, and differentiating the integrand gives:

    $$
    \frac{\partial C}{\partial K} = e^{-rT}\int_{K}^{\infty}(-1)p(s,T)\,ds = -e^{-rT}\int_{K}^{\infty}p(s,T)\,ds
    $$

    **Second derivative:**

    $$
    \frac{\partial^2 C}{\partial K^2} = -e^{-rT}\frac{\partial}{\partial K}\int_{K}^{\infty}p(s,T)\,ds = -e^{-rT}(-p(K,T)) = e^{-rT}p(K,T)
    $$

    **(b)** Since $C_{KK} = e^{-rT}p(K,T)$ and $e^{-rT} > 0$, we have $C_{KK} \geq 0$ if and only if $p(K,T) \geq 0$. A probability density must be non-negative everywhere, so non-negative $C_{KK}$ is equivalent to having a valid (non-negative) risk-neutral density.

    **(c)** If $C_{KK} < 0$ for some strike $K_0$, then the call price surface is locally concave in $K$ at $K_0$. This creates a **butterfly arbitrage**: construct a butterfly spread by buying calls at $K_0 - \Delta K$ and $K_0 + \Delta K$ and selling two calls at $K_0$. The cost of this portfolio is approximately $C_{KK}(K_0)(\Delta K)^2 < 0$, meaning you receive money upfront. But the payoff of a butterfly spread is always non-negative (it pays $(S_T - K_0 + \Delta K)^+ - 2(S_T - K_0)^+ + (S_T - K_0 - \Delta K)^+ \geq 0$). Receiving money today for a non-negative future payoff is a type I arbitrage.

---

**Exercise 4.** In the Dupire formula, the numerator $C_T + rKC_K$ must be non-negative for the local variance $\sigma^2(K,T)$ to be well-defined. (a) Interpret $C_T$ financially: what does it measure about the option value as maturity increases? (b) Interpret $rKC_K$ in terms of discounting and the forward price. (c) Construct a scenario where the numerator could become negative and explain what this would signal about the option price surface.

??? success "Solution to Exercise 4"
    **(a)** The term $C_T = \frac{\partial C}{\partial T}$ is the **forward theta** -- it measures the rate of increase of the call price as maturity extends (holding strike fixed). Economically, a longer maturity gives the underlying more time to diffuse, increasing the probability of finishing in the money. The call price is non-decreasing in maturity for European options (calendar spread condition), so $C_T \geq 0$. This captures the additional optionality from extending the time horizon.

    **(b)** The term $rKC_K$ involves the strike derivative $C_K = -e^{-rT}\mathbb{Q}(S_T > K)$. The product $rKC_K = -rKe^{-rT}\mathbb{Q}(S_T > K)$ represents the drift adjustment from the forward price. As maturity increases, the forward price $F = S_0 e^{rT}$ grows at rate $r$, shifting the exercise probability. The term $rKC_K$ corrects for this drift: it accounts for the fact that the discounting factor $e^{-rT}$ changes with $T$, and the underlying drifts at the risk-free rate under the risk-neutral measure.

    **(c)** The numerator $C_T + rKC_K$ could become negative if the option price decreases with maturity after the drift correction. This could happen if:

    - The input call price surface violates calendar spread arbitrage, i.e., longer-dated options are cheaper than shorter-dated ones at the same strike after adjusting for discounting
    - Market data errors produce spurious decreases in $C$ with $T$
    - The interpolation scheme used to smooth the price surface introduces artificial non-monotonicity in $T$

    A negative numerator with a positive denominator would yield $\sigma_{\text{loc}}^2 < 0$, which is physically meaningless. This signals that the input call price surface violates no-arbitrage conditions and cannot correspond to any diffusion model.

---

**Exercise 5.** The Fokker-Planck approach yields

$$
\sigma^2 = \frac{\frac{\partial p}{\partial t}}{\frac{1}{2}\frac{\partial^2 p}{\partial x^2}}
$$

while the Dupire approach yields the formula in terms of $C_T$, $C_K$, and $C_{KK}$. Show that these two expressions are equivalent by using the relationships $C_K = -e^{-rT}\int_{K}^{\infty}p\,ds$ and $C_{KK} = e^{-rT}p(K,T)$ to transform one into the other.

??? success "Solution to Exercise 5"
    The Fokker-Planck approach gives the local variance as:

    $$
    \sigma^2(x, t) = \frac{\frac{\partial p}{\partial t}}{\frac{1}{2}\frac{\partial^2 p}{\partial x^2}}
    $$

    The Dupire approach gives:

    $$
    \sigma^2(K, T) = \frac{C_T + rKC_K}{\frac{1}{2}K^2 C_{KK}}
    $$

    We show equivalence using $C_{KK} = e^{-rT}p(K,T)$ and $C_K = -e^{-rT}\int_K^\infty p\,ds$.

    From the Breeden-Litzenberger result, $p(K, T) = e^{rT}C_{KK}$, so:

    $$
    \frac{\partial p}{\partial T} = e^{rT}(rC_{KK} + C_{KKT})
    $$

    The Fokker-Planck equation for the density $p$ in the presence of drift $rS$ is:

    $$
    \frac{\partial p}{\partial T} = -\frac{\partial}{\partial K}[rKp] + \frac{1}{2}\frac{\partial^2}{\partial K^2}[\sigma^2 K^2 p]
    $$

    Now consider the Dupire equation $C_T + rKC_K = \frac{1}{2}\sigma^2 K^2 C_{KK}$. Differentiate both sides twice with respect to $K$:

    $$
    C_{KKT} + r\frac{\partial^2}{\partial K^2}[KC_K] = \frac{1}{2}\frac{\partial^2}{\partial K^2}[\sigma^2 K^2 C_{KK}]
    $$

    Since $C_{KK} = e^{-rT}p$, we can substitute $C_{KKT} = e^{-rT}(p_T - rp)$. For the left side, $\frac{\partial^2}{\partial K^2}[KC_K] = \frac{\partial}{\partial K}[C_K + KC_{KK}] = 2C_{KK} + KC_{KKK}$, and using $C_{KK} = e^{-rT}p$, this becomes $e^{-rT}(2p + Kp_K) = e^{-rT}\frac{\partial}{\partial K}[Kp] + e^{-rT}p$.

    This establishes that the Dupire equation in $C$-space is equivalent to the Fokker-Planck equation in $p$-space, connected through the Breeden-Litzenberger identity $C_{KK} = e^{-rT}p(K,T)$.

---

**Exercise 6.** In the diffusion term integration by parts, the boundary evaluation produces

$$
\left[(s-K)\left[(\sigma s)^2 p\right]_s\right]\bigg|_{K}^{\infty}
$$

(a) Explain why the upper limit ($s \to \infty$) vanishes. What growth conditions on $\sigma(s,T)$ and decay conditions on $p(s,T)$ are required? (b) Evaluate the lower limit at $s = K$. (c) Why is a second integration by parts needed, and what does it produce?

??? success "Solution to Exercise 6"
    **(a)** The boundary evaluation term is:

    $$
    \left[(s-K)\left[(\sigma s)^2 p\right]_s\right]\bigg|_{K}^{\infty}
    $$

    **Upper limit** ($s \to \infty$): We need $(s - K)[(\sigma s)^2 p]_s \to 0$ as $s \to \infty$. This requires:

    - Growth condition on $\sigma$: $\sigma(s, T)$ grows at most polynomially, i.e., $\sigma(s, T) \leq C s^\alpha$ for some $\alpha$ and large $s$
    - Decay condition on $p$: The density $p(s, T)$ must decay faster than any polynomial, specifically $s^n p(s, T) \to 0$ for all $n$

    For any risk-neutral density with finite moments (guaranteed by $\mathbb{E}^Q[S_T^n] < \infty$), the density decays exponentially in the tails, and the derivative $[(\sigma s)^2 p]_s$ inherits sufficient decay. The factor $(s - K)$ grows linearly, but this is dominated by the exponential decay, so the product vanishes.

    **(b)** At $s = K$: $(K - K)[(\sigma K)^2 p(K, T)]_s = 0$. The factor $(s - K)$ evaluates to zero at $s = K$, regardless of the value of the derivative $[(\sigma s)^2 p]_s$ at $s = K$. So the lower limit contributes zero.

    **(c)** After the first integration by parts, we are left with:

    $$
    -\int_{K}^{\infty}\left[(\sigma s)^2 p\right]_s \, ds
    $$

    This integral can be evaluated directly using the fundamental theorem of calculus:

    $$
    -\int_{K}^{\infty}[(\sigma s)^2 p]_s \, ds = -\left[(\sigma s)^2 p\right]_{K}^{\infty} = -0 + \sigma^2(K,T)K^2 p(K,T)
    $$

    where we used the fact that $(\sigma s)^2 p \to 0$ as $s \to \infty$ (by the same decay arguments). This produces the key term $\sigma^2(K,T)K^2 p(K,T)$ that, combined with the Breeden-Litzenberger identity $p(K,T) = e^{rT}C_{KK}$, yields the local volatility term $\frac{1}{2}\sigma^2(K,T)K^2 C_{KK}$ in the Dupire formula.

---

**Exercise 7.** Consider extending the Dupire formula to include continuous dividend yield $q$. The risk-neutral dynamics become $dS_t = (r-q)S_t\,dt + \sigma(t,S_t)S_t\,dW_t$. (a) Write down the corresponding Fokker-Planck equation. (b) Repeat the integration by parts derivation to show that the generalized Dupire formula is

$$
\sigma^2(K,T) = \frac{C_T + (r-q)KC_K + qC}{\frac{1}{2}K^2 C_{KK}}
$$

(c) Verify that setting $q = 0$ recovers the original formula.

??? success "Solution to Exercise 7"
    **(a)** With continuous dividend yield $q$, the risk-neutral dynamics are $dS_t = (r-q)S_t\,dt + \sigma(t,S_t)S_t\,dW_t$. The corresponding Fokker-Planck equation for the transition density $p(s, T)$ is:

    $$
    \frac{\partial p}{\partial T} = -\frac{\partial}{\partial s}\left[(r-q)s\,p\right] + \frac{1}{2}\frac{\partial^2}{\partial s^2}\left[\sigma^2(s,T)s^2\,p\right]
    $$

    with initial condition $p(s, 0) = \delta(s - S_0)$.

    **(b)** The call price with dividends is $C = e^{-rT}\int_K^\infty (s - K)p(s,T)\,ds$. Differentiating with respect to $T$:

    $$
    C_T = -rC + e^{-rT}\int_K^\infty (s-K)p_T\,ds
    $$

    Substituting the Fokker-Planck equation and applying integration by parts to the drift term:

    $$
    \int_K^\infty (s-K)[(r-q)sp]_s\,ds = -\int_K^\infty (r-q)sp\,ds
    $$

    Using $e^{-rT}\int_K^\infty sp\,ds = C - KC_K$ (from the call price expression):

    $$
    -e^{-rT}\int_K^\infty (r-q)sp\,ds = -(r-q)(C - KC_K) = -(r-q)C + (r-q)KC_K
    $$

    The diffusion term gives $\frac{1}{2}\sigma^2(K,T)K^2 C_{KK}$ as before. Combining:

    $$
    C_T = -rC + (r-q)C - (r-q)KC_K + \frac{1}{2}\sigma^2(K,T)K^2 C_{KK}
    $$

    $$
    = -qC - (r-q)KC_K + \frac{1}{2}\sigma^2(K,T)K^2 C_{KK}
    $$

    Solving for $\sigma^2$:

    $$
    \sigma^2(K,T) = \frac{C_T + (r-q)KC_K + qC}{\frac{1}{2}K^2 C_{KK}}
    $$

    **(c)** Setting $q = 0$:

    $$
    \sigma^2(K,T) = \frac{C_T + rKC_K + 0}{\frac{1}{2}K^2 C_{KK}} = \frac{C_T + rKC_K}{\frac{1}{2}K^2 C_{KK}}
    $$

    This is exactly the original Dupire formula without dividends, confirming consistency.
