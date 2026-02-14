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

## QuantPie Derivation: Hull-White ZCB Option Formula

### ZCB Call ($\alpha=1$) and Put ($\alpha=-1$)

Let $t_0$, $T$, $T_S$ be current, option maturity, ZCB maturity, respectively.
For the call

$$\begin{array}{lllll}
\displaystyle
V^\text{ZCB}(t_0,T)
=
P(t_0,T)e^{A(\tau)}\left[e^{\frac{1}{2}B^2(\tau)v_r^2(t_0,T)+B(\tau)\mu_r(t_0,T)}N(d_1)-\hat{K}N(d_2)\right]\\
\end{array}$$

where $A(\tau)$ and $B(\tau)$ are related with
the underlying ZCB price $P(T,T_s)$ at option maturity $T$, $\tau=T_S-T$, by

$$\begin{array}{lll}
\displaystyle
\theta(t)
&=&\displaystyle
f(0,t)+\frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t}
-
\frac{\sigma^2}{2\lambda^2}\left(e^{-2\lambda t}-1\right)\\
\displaystyle
A(\tau)
&=&\displaystyle
-\frac{\sigma^2}{4\lambda^3}
\left(3-2\lambda\tau-4e^{-\lambda\tau}+e^{-2\lambda\tau}\right)
+
\lambda\int_0^\tau\theta(T_S-\tau')B(\tau')d\tau'
\\
\displaystyle
B(\tau)
&=&\displaystyle
\frac{e^{-\lambda\tau}-1}{\lambda}
\\
\displaystyle
P(T,T_s)
&=&\displaystyle e^{A(\tau)+B(\tau)r(T)}\\
\end{array}$$

where $\mu_r(t_0,T)$ and $v_r^2(t_0,T)$ are related with
the short rate $r(T)$ at option maturity $T$ under $\mathbb{Q}^T$ measure by

$$\begin{array}{lll}
\displaystyle
\theta^T(t)
&=&\displaystyle\theta(t)+\frac{\sigma^2}{\lambda}B(T-t)\\
dr(t)&=&\displaystyle
\lambda\left(\theta^T(t)-r(t)\right) dt+\sigma dW^T(t)\\
\displaystyle
r(T)|r(t_0)&\sim&\displaystyle
N\left(\mu_r(t_0,T),v_r^2(t_0,T)\right)\\
\mu_r(t_0,T)&=&\displaystyle
r(t_0)e^{-\lambda(T-t_0)}
+\lambda\int_{t_0}^{T}\theta^T(t')e^{-\lambda(T-t')}dt'\\
v_r^2(t_0,T)&=&\displaystyle
-\frac{\sigma^2}{2\lambda}\left(e^{-2\lambda(T-t_0)}-1\right)\\
\end{array}$$

and where $\hat{K}$, $d_1$ and $d_2$ are constants from Black Scholes type integration computation:

$$\begin{array}{lll}
\hat{K}&=&Ke^{-A(\tau)}\\
d_2&=&\displaystyle
\frac{\log\hat{K}-B(\tau)\mu_r(t_0,T)}{B(\tau)v_r(t_0,T)}\\
d_1&=&\displaystyle
d_2-B(\tau)v_r(t_0,T)\\
\end{array}$$

### Proof

$$\begin{array}{lllll}
\displaystyle
V^\text{ZCB}(t_0,T)
&=&\displaystyle
\mathbb{E^Q}\left[\frac{M(t_0)}{M(T)}\text{max}\left(\alpha\left(P(T,T_S)-K\right),0\right)\Big{|}{\cal F}(t_0)\right]\\
&=&\displaystyle
P(t_0,T)\mathbb{E}^T\left[\text{max}\left(\alpha\left(P(T,T_S)-K\right),0\right)\Big{|}{\cal F}(t_0)\right]\\
&=&\displaystyle
P(t_0,T)\mathbb{E}^T\left[\text{max}\left(\alpha\left(e^{A(\tau)+B(\tau)r(T)}-K\right),0\right)\Big{|}{\cal F}(t_0)\right]\\
&=&\displaystyle
P(t_0,T)e^{A(\tau)}\mathbb{E}^T\left[\text{max}\left(\alpha\left(e^{B(\tau)r(T)}-\hat{K}\right),0\right)\Big{|}{\cal F}(t_0)\right]\\
\end{array}$$

Now, by solving $dr(t)=\lambda\left(\theta^T(t)-r(t)\right) dt+\sigma dW^T(t)$

$$
\displaystyle
r(T)|r(t_0)\sim N\left(\mu_r(t_0,T),v_r^2(t_0,T)\right)
$$

where

$$\begin{array}{lll}
\displaystyle
\mu_r(t_0,T)&=&\displaystyle
r(t_0)e^{-\lambda(T-t_0)}
+\lambda\int_{t_0}^{T}\theta^T(t')e^{-\lambda(T-t')}dt'\\
\displaystyle
v_r^2(t_0,T)&=&\displaystyle
-\frac{\sigma^2}{2\lambda}\left(e^{-2\lambda(T-t_0)}-1\right)\\
\end{array}$$

With $B(\tau)=(e^{-\lambda\tau}-1)/\lambda$

$$
\displaystyle
B(\tau)r(T)|r(t_0)\sim N\left(B(\tau)\mu_r(t_0,T),B^2(\tau)v_r^2(t_0,T)\right)
$$

Following Black Scholes computation, we have for the call
(remember $B(\tau)=(e^{-\lambda\tau}-1)/\lambda<0$)

$$\begin{array}{lllll}
\displaystyle
V^\text{ZCB}(t_0,T)
&=&\displaystyle
P(t_0,T)e^{A(\tau)}\mathbb{E}^T\left[\text{max}\left(e^{B(\tau)r(T)}-\hat{K},0\right)\Big{|}{\cal F}(t_0)\right]\\
&=&\displaystyle
P(t_0,T)e^{A(\tau)}\int_{e^{B(\tau)\mu_r(t_0,T)+B(\tau)v_r(t_0,T)z}>\hat{K}}\left(e^{B(\tau)\mu_r(t_0,T)+B(\tau)v_r(t_0,T)z}-\hat{K}\right)\frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz\\
&=&\displaystyle
P(t_0,T)e^{A(\tau)}\int^a_{-\infty}
\left(e^{B(\tau)\mu_r(t_0,T)+B(\tau)v_r(t_0,T)z}-\hat{K}\right)\frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz\\
&=&\displaystyle
P(t_0,T)e^{A(\tau)}\left[e^{\frac{1}{2}B^2(\tau)v_r^2(t_0,T)+B(\tau)\mu_r(t_0,T)}N(d_1)-\hat{K}N(d_2)\right]\\
\end{array}$$

where

$$\begin{array}{lll}
a&=&\displaystyle
\frac{\log\hat{K}-B(\tau)\mu_r(t_0,T)}{B(\tau)v_r(t_0,T)}\\
d_1&=&\displaystyle
a-B(\tau)v_r(t_0,T)\\
d_2&=&\displaystyle
a\\
\end{array}$$
