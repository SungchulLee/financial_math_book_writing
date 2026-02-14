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

The Dupire formula can be understood through a deep connection with the Fokker-Planck equation. Under the risk-neutral measure, the stock price evolves as:

$$
dS_t = rS_t dt + \sigma(t, S_t) S_t dW_t
$$

This leads to two equivalent formulations of the local volatility surface:

$$\begin{array}{ccc}
\text{Fokker-Planck} & & \text{Dupire} \\
p(x,t|x_0,t_0) & & C(K,T|S_t,t) \\
\displaystyle dX_t = \sigma dW_t & & \\
\displaystyle \frac{\partial p(x,t)}{\partial t} - \frac{1}{2}\sigma^2\frac{\partial^2 p(x,t)}{\partial x^2} = 0 & & \displaystyle \frac{\partial C(K,T)}{\partial T} + rK\frac{\partial C(K,T)}{\partial K} - \frac{1}{2}\sigma^2(K,T)K^2\frac{\partial^2 C(K,T)}{\partial K^2} = 0 \\
\displaystyle \sigma^2 = \frac{\frac{\partial p(x,t)}{\partial t}}{\frac{1}{2}\frac{\partial^2 p(x,t)}{\partial x^2}} & & \displaystyle \sigma^2(K,T) = \frac{\frac{\partial C(K,T)}{\partial T} + rK\frac{\partial C(K,T)}{\partial K}}{\frac{1}{2}K^2\frac{\partial^2 C(K,T)}{\partial K^2}}
\end{array}$$

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

From the expression above, we can compute the following partial derivatives:

$$\begin{array}{lll}
\displaystyle
C_K &=& -e^{-rT}\int_{K}^{\infty }p \, ds \\
\displaystyle
C_{KK} &=& e^{-rT}p(K,T)
\end{array}$$

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

