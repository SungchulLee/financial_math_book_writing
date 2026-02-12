# Hull-White Zero Bond Options

## $x(t)$ under $\mathbb{Q}$

$$\begin{array}{lllll}
\displaystyle
dx(t)=-\lambda x(t)dt+\sigma dW^{\mathbb{Q}}(t),
\quad x(0)=0
\end{array}$$

can be solved as

$$\begin{array}{lllll}
\displaystyle
x(t)
=
x(s)e^{-\lambda (t-s)}+\sigma \int_{s}^t e^{-\lambda (t-t')} dW^{\mathbb{Q}}(t')
\end{array}$$

## $x(t)$ under $\mathbb{T}$

$$\begin{array}{lllll}
\displaystyle
dx(t)=\left(-B(t,T)\sigma^2-\lambda x(t)\right)dt+\sigma dW^{\mathbb{T}}(t),
\quad x(0)=0
\end{array}$$

where

$$
\displaystyle
dW^{\mathbb{T}}(t)
=
\sigma B(t,T)dt+
dW^{\mathbb{Q}}(t)
$$

## $r(t)$ under $\mathbb{T}$

$$\begin{array}{lllll}
\displaystyle
r(t)=x(t)+\alpha(t)
\end{array}$$

Therefore, $r(t)$ conditional on ${\cal F}(s)$ is normally distributed with mean and variance:

$$\begin{array}{lllll}
\displaystyle
\mathbb{E}\left(r(t)|{\cal F}(s)\right)
&=&\displaystyle
\mu^\mathbb{T}_r(s,t)\\
\mathbb{Var}\left(r(t)|{\cal F}(s)\right)
&=&\displaystyle
\sigma_r^2(s,t)
\end{array}$$

## ZCB Call ($\alpha=1$) and Put ($\alpha=-1$)

Let $t_0$, $T$, $T_S$ be current, ZCB option maturity, ZCB maturity, respectively.
For the call:

$$\begin{array}{lllll}
\displaystyle
V^\text{ZCB}(t_0,T)
=
P(t_0,T)e^{A(\tau)}\left[e^{\frac{1}{2}B^2(\tau)\sigma_r^2(t_0,T)+B(\tau)\mu^\mathbb{T}_r(t_0,T)}N(d_1)-K_{\text{hat}}N(d_2)\right]
\end{array}$$

where

$$\begin{array}{lll}
K_{\text{hat}}&=&Ke^{-A(\tau)}\\
a&=&\frac{\log(K_{\text{hat}})-B(\tau)\mu^\mathbb{T}_r(t_0,T)}{B(\tau)\sigma_r(t_0,T)}\\
d_1&=&a-B(\tau)\sigma_r(t_0,T)\\
d_2&=&d_1+B(\tau)\sigma_r(t_0,T)
\end{array}$$

with $\tau = T_S - T$.

???+ note "Proof"

    $$\begin{array}{lllll}
    \displaystyle
    V^\text{ZCB}(t_0,T)
    &=&\displaystyle
    \mathbb{E^Q}\left[\frac{M(t_0)}{M(T)}\text{max}\left(\alpha\left(P(T,T_S)-K\right),0\right)\Big{|}{\cal F}(t_0)\right]\\
    &=&\displaystyle
    P(t_0,T)\mathbb{E}^T\left[\text{max}\left(\alpha\left(P(T,T_S)-K\right),0\right)\Big{|}{\cal F}(t_0)\right]\\
    \end{array}$$

    Since $P(T,T_S)=e^{A(\tau)+B(\tau)r(T)}$ and $r(T)\sim N(\mu^\mathbb{T}_r(t_0,T), \sigma_r^2(t_0,T))$ under $\mathbb{T}$, the expectation reduces to a standard lognormal integral, yielding a Black-Scholes-type formula.

## Discounted Characteristic Function of $r(T)$

$$\begin{array}{lllll}
\displaystyle
\phi(u;t,T)
=
\mathbb{E}^\mathbb{Q}\left[e^{-\int_t^Tr(t')dt'+iur(T)}\Big{|}{\cal F}(t)\right]
=
e^{A(u,\tau)+B(u,\tau)r(t)}
\end{array}$$

## Hull-White MC Agrees with Hull-White ZCB Option Formula

```python
def main():
    hw = HullWhite(sigma=0.02, lambd=0.02, P=P_market)

    K = 0.95
    T1 = 5.0   # option maturity
    T2 = 10.0  # ZCB maturity

    # Analytic price
    price_analytic = hw.compute_ZCB_Option_Price(K, T1, T2, CP=OptionType.CALL)

    # Monte Carlo price
    t, R, M = hw.generate_sample_paths(num_paths=50_000, num_steps=500, T=T1)
    P_T1_T2 = np.array([hw.compute_ZCB(T1, T2, r) for r in R[:, -1]])
    payoff = np.maximum(P_T1_T2 - K, 0)
    price_mc = np.mean(payoff / M[:, -1])

    print(f"Analytic: {price_analytic:.6f}")
    print(f"Monte Carlo: {price_mc:.6f}")
```
