# Hull-White Caplet and Floor Formula

## Caplet/Floorlet Payoff

$$\begin{array}{lll}
\text{Time}&\text{Action}\\
T_{k-1}&\text{Forward Rate Determined $l_k(T_{k−1})=l(T_{k−1}; T_{k−1}, T_k)$ }\\
T_k&\text{Caplet Paid $N\tau_k \max(l_k(T_{k−1})-K,0))$}\\
&\text{Floorlet Paid $N\tau_k \max(K-l_k(T_{k−1}),0))$}
\end{array}$$

where $\tau_k=T_k-T_{k-1}$.

## Change of Numeraire

$$\begin{array}{llllllll}
\displaystyle
V^\text{CL}(t_0)
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[
\frac{N\tau_k\text{max}(l_k(T_{k-1})-K,0)}{M(T_k)}\Big{|}{\cal F}(t_0)
\right]
&=&\displaystyle
N\tau_kP(t_0,T_k)\mathbb{E}^{\mathbb{T_k}}\left[
\text{max}(l_k(T_{k-1})-K,0)\Big{|}{\cal F}(t_0)
\right]
\end{array}$$

## Forward Rate $l_k$ is a $\mathbb{T_k}$-Martingale

Since $l_k(t)=\frac{1}{\tau_k}\frac{P(t,T_{k-1})-P(t,T_k)}{P(t,T_k)}$ and since $P(t,T_{k-1})$ and $P(t,T_{k})$ are prices of tradable assets,

$$\begin{array}{lll}
\displaystyle
\mathbb{E}^{\mathbb{T_k}}\left[l_k(t)\Big{|}{\cal F}(s)\right]
=l_k(s)
\end{array}$$

## Black's Formula

Assume that the libor rate follows a lognormal distribution:

$$\begin{array}{lll}
\displaystyle
dl_k(t)
=
\sigma_kl_k(t)dW^{\mathbb{T_k}}(t)
\end{array}$$

Then, we can use the Black–Scholes computation with interest rate 0:

$$\begin{array}{lll}
\displaystyle
{\bf\text{Caplet}}^{\text{Black}}(t,T_{k-1},T_k,N,K,\sigma_k)
&=&\displaystyle
N\tau_kP(t,T_k)\left[
l_k(t)N(d_1)-KN(d_2)
\right]\\
\displaystyle
{\bf\text{Floorlet}}^{\text{Black}}(t,T_{k-1},T_k,N,K,\sigma_k)
&=&\displaystyle
N\tau_kP(t,T_k)\left[
-l_k(t)N(-d_1)+KN(-d_2)
\right]\\
\end{array}$$

where

$$\begin{array}{lll}
\displaystyle
d_1
&=&\displaystyle
\frac{1}{v_k}\log\left(\frac{l_k(t)}{K}\right)+\frac{1}{2}v_k\\
\displaystyle
d_2&=&\displaystyle
\frac{1}{v_k}\log\left(\frac{l_k(t)}{K}\right)-\frac{1}{2}v_k\\
v_k&=&\sigma_k\sqrt{T_{k-1}-t}\\
\end{array}$$

## Hull-White Caplet Formula (Using $\mathbb{T_{k}}$ Measure)

Let $t_0$, $T_{k-1}$, $T_k$ be current, reset date, maturity, respectively.

$$\begin{array}{lllll}
\displaystyle
V^\text{CPL}(t_0,T)
=
N P(t_0,T_k)e^{-A(\tau_k)}\left[e^{\frac{1}{2}B^2(\tau_k)\sigma_r^2(t_0,T_{k-1})-B(\tau_k)\mu^{\mathbb{T_k}}_r(t_0,T_{k-1})}N(d_1)-K_{\text{hat}}N(d_2)\right]
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lll}
    \displaystyle
    V^\text{CPL}(t_0)
    &=&\displaystyle
    N\tau_kP(t_0,T_k)\mathbb{E}^{\mathbb{T_{k}}}\left[
    \text{max}(l_k(T_{k-1})-K,0)\Big{|}{\cal F}(t_0)
    \right]\\
    &=&\displaystyle
    N(1+\tau_k K)P(t_0,T_k)\mathbb{E}^{\mathbb{T_{k}}}\left[
    \text{max}\left(\frac{1}{1+\tau_k K}-P(T_{k-1},T_k),0\right)\Big{|}{\cal F}(t_0)
    \right]
    \end{array}$$

    This is a put option on the ZCB $P(T_{k-1},T_k)$ with strike $\frac{1}{1+\tau_k K}$, which can be priced using the Hull-White ZCB option formula.

## Cap and Floor

$$\begin{array}{lll}
\displaystyle\text{Cap}&=&\displaystyle\sum\text{Caplet}\\
\displaystyle\text{Floor}&=&\displaystyle\sum\text{Floorlet}\\
\end{array}$$

## Effect of Hull-White Model Parameters on Implied Volatilities

```python
def main():
    # Vary sigma and lambda to see effect on implied vol
    hw = HullWhite(sigma=0.01, lambd=0.01, P=P_market)

    K_grid = np.linspace(0.01, 0.10, 20)
    T_reset = 5.0
    T_pay = 5.5

    for sigma in [0.005, 0.01, 0.02]:
        hw.sigma = sigma
        implied_vols = []
        for K in K_grid:
            price = hw.compute_Caplet_Floorlet_Price(1, K, T_reset, T_pay, OptionType.CALL)
            iv = compute_Implied_Volatility_using_Black76(price, K, T_reset, S_0, OptionType.CALL)
            implied_vols.append(iv)
        plt.plot(K_grid, implied_vols, label=f'sigma={sigma}')
```

## QuantPie Derivation: Caplet as ZCB Put

### Caplet is ZCB Put (Using $T_{k-1}$ Measure)

$$\begin{array}{lll}
\displaystyle
V^\text{CPL}(t_0)
=
\hat{N}P(t_0,T_{k-1})\mathbb{E}^{T_{k-1}}\left[
\text{max}\left(\hat{K}-P(T_{k-1},T_k),0\right)\Big{|}{\cal F}(t_0)
\right]\\
\end{array}$$

where

$$\begin{array}{lll}
\displaystyle
\hat{N}
&:=&\displaystyle
N(1+\tau_k K)\\
\displaystyle
\hat{K}&:=&\displaystyle
\frac{1}{1+\tau_k K}\\
\end{array}$$

### Proof

$$\begin{array}{lll}
\displaystyle
V^\text{CPL}(t_0)
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[
\frac{N\tau_k\text{max}(l_k(T_{k-1})-K,0)}{M(T_k)}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[\mathbb{E^Q}\left[
\frac{N\tau_k\text{max}(l_k(T_{k-1})-K,0)}{M(T_k)}\Big{|}{\cal F}(T_{k-1})
\right]\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\tau_k\text{max}(l_k(T_{k-1})-K,0)\mathbb{E^Q}\left[
\frac{1}{M(T_k)}\Big{|}{\cal F}(T_{k-1})
\right]\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\tau_k\text{max}(l_k(T_{k-1})-K,0)
\frac{P(T_{k-1},T_k)}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\tau_k\text{max}\left(\frac{1}{\tau_k}\left(\frac{1}{P(T_{k-1},T_k)}-1\right)-K,0\right)
\frac{P(T_{k-1},T_k)}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\text{max}\left(\frac{1}{P(T_{k-1},T_k)}-(1+\tau_k K),0\right)
\frac{P(T_{k-1},T_k)}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\text{max}\left(1-(1+\tau_k K)P(T_{k-1},T_k),0\right)
\frac{1}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[
N(1+\tau_k K)\text{max}\left(\frac{1}{(1+\tau_k K)}-P(T_{k-1},T_k),0\right)\frac{1}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E}^{T_{k-1}}\left[
N(1+\tau_k K)\text{max}\left(\frac{1}{(1+\tau_k K)}-P(T_{k-1},T_k),0\right)\frac{1}{M(T_{k-1})}\frac{M(T_{k-1})/M(t_0)}{1/P(t_0,T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N(1+\tau_k K)P(t_0,T_{k-1})\mathbb{E}^{T_{k-1}}\left[
\text{max}\left(\frac{1}{(1+\tau_k K)}-P(T_{k-1},T_k),0\right)\Big{|}{\cal F}(t_0)
\right]\\
&:=&\displaystyle
\hat{N}P(t_0,T_{k-1})\mathbb{E}^{T_{k-1}}\left[
\text{max}\left(\hat{K}-P(T_{k-1},T_k),0\right)\Big{|}{\cal F}(t_0)
\right]
\end{array}$$

## QuantPie Derivation: Hull-White Caplet Formula (Using $T_k$ Measure)

### Hull-White Caplet Formula (Using $T_k$ Measure)

Let $t_0$, $T_{k-1}$, $T_k$ be current, reset date, maturity, respectively.

$$\begin{array}{lllll}
\displaystyle
V^\text{CPL}(t_0,T)
=
N P(t_0,T_k)e^{-A(\tau_k)}\left[e^{\frac{1}{2}B^2(\tau_k)v_r^2(t_0,T_{k-1})-B(\tau_k)\mu_r(t_0,T_{k-1},\color{red}{T_k})}N(d_1)-\hat{K}N(d_2)\right]\\
\end{array}$$

where $A(\tau_k)$ and $B(\tau_k)$ are related with
the underlying ZCB price $P(T_{k-1},T_k)$ at option maturity $T_{k-1}$,
$\tau_k=T_k-T_{k-1}$, by

$$\begin{array}{lll}
\displaystyle
\theta(t)
&=&\displaystyle
f(0,t)+\frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t}
-
\frac{\sigma^2}{2\lambda^2}\left(e^{-2\lambda t}-1\right)\\
\displaystyle
A(\tau_k)
&=&\displaystyle
-\frac{\sigma^2}{4\lambda^3}
\left(3-2\lambda\tau_k-4e^{-\lambda\tau_k}+e^{-2\lambda\tau_k}\right)
+
\lambda\int_0^{\tau_k}\theta(T_k-\tau')B(\tau')d\tau'
\\
\displaystyle
B(\tau_k)
&=&\displaystyle
\frac{e^{-\lambda\tau_k}-1}{\lambda}
\\
\displaystyle
P(T_{k-1},T_k)
&=&\displaystyle e^{A(\tau_k)+B(\tau_k)r(T_{k-1})}\\
\end{array}$$

where $\mu_r(t_0,T_{k-1},\color{red}{T_k})$ and $v_r^2(t_0,T_{k-1})$ are related with
the short rate $r(T_{k-1})$ at option maturity $T_{k-1}$
under $\mathbb{Q}^{\color{red}{T_{k}}}$, not $\mathbb{Q}^{\color{black}{T_{k-1}}}$ measure by

$$\begin{array}{lll}
\displaystyle
\theta^{\color{red}{T_{k}}}(t)
&=&\displaystyle\theta(t)+\frac{\sigma^2}{\lambda}B(\color{red}{T_{k}}-t)\\
dr(t)&=&\displaystyle
\lambda\left(\theta^{\color{red}{T_{k}}}(t)-r(t)\right) dt+\sigma dW^{\color{red}{T_{k}}}(t)\\
\displaystyle
r(T_{k-1})|r(t_0)&\sim&\displaystyle
N\left(\mu_r(t_0,T_{k-1},\color{red}{T_k}),v_r^2(t_0,T_{k-1})\right)\\
\mu_r(t_0,T_{k-1},\color{red}{T_k})&=&\displaystyle
r(t_0)e^{-\lambda(T_{k-1}-t_0)}
+\lambda\int_{t_0}^{T_{k-1}}\theta^{\color{red}{T_{k}}}(t')e^{-\lambda(T_{k-1}-t')}dt'\\
v_r^2(t_0,T_{k-1})&=&\displaystyle
-\frac{\sigma^2}{2\lambda}\left(e^{-2\lambda(T_{k-1}-t_0)}-1\right)\\
\end{array}$$

and where $\hat{K}$, $d_1$ and $d_2$ are constants from Black Scholes type integration computation:

$$\begin{array}{lll}
\hat{K}&=&(1+\tau_k K)e^{A(\tau_k)}\\
d_2&=&\displaystyle
\frac{\log\hat{K}+B(\tau_k)\mu_r(t_0,T_{k-1},\color{red}{T_k})}{B(\tau_k)v_r(t_0,T_{k-1})}\\
d_1&=&\displaystyle
d_2-B(\tau_k)v_r(t_0,T_{k-1})
\end{array}$$

### Proof

$$\begin{array}{lll}
\displaystyle
V^\text{CPL}(t_0)
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[
\frac{N\tau_k\text{max}(l_k(T_{k-1})-K,0)}{M(T_k)}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N\tau_kP(t_0,T_k)\mathbb{E}^{T_k}\left[
\text{max}(l_k(T_{k-1})-K,0)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N\tau_kP(t_0,T_k)\mathbb{E}^{T_k}\left[
\text{max}\left(\frac{1}{\tau_k}\left(\frac{1}{P(T_{k-1},T_k)}-1\right)-K,0\right)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N P(t_0,T_k)\mathbb{E}^{T_k}\left[
\text{max}\left(\frac{1}{P(T_{k-1},T_k)}-1-\tau_k K,0\right)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N P(t_0,T_k)\mathbb{E}^{T_k}\left[
\text{max}\left(e^{-A(\tau_k)-B(\tau_k)r(T_{k-1})}-1-\tau_k K,0\right)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}\mathbb{E}^{T_k}\left[
\text{max}\left(e^{-B(\tau_k)r(T_{k-1})}-(1+\tau_k K)e^{A(\tau_k)},0\right)\Big{|}{\cal F}(t_0)
\right]\\
&:=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}\mathbb{E}^{T_k}\left[
\text{max}\left(e^{-B(\tau_k)r(T_{k-1})}-\hat{K},0\right)\Big{|}{\cal F}(t_0)
\right]\\
\end{array}$$

Now, by solving $dr(t)=\lambda\left(\theta^{\color{red}{T_k}}(t)-r(t)\right) dt+\sigma dW^{\color{red}{T_k}}(t)$

$$
\displaystyle
r(T_{k-1})|r(t_0)\sim N\left(\mu_r(t_0,T_{k-1},\color{red}{T_k}),v_r^2(t_0,T_{k-1})\right)
$$

With $B(\tau_k)=(e^{-\lambda\tau_k}-1)/\lambda$

$$
\displaystyle
-B(\tau_k)r(T_{k-1})\sim N\left(-B(\tau_k)\mu_r(t_0,T_{k-1},\color{red}{T_k}),B^2(\tau_k)v_r^2(t_0,T_{k-1})\right)
$$

Following Black Scholes computation, we have for the call
(remember $B(\tau)=(e^{-\lambda\tau}-1)/\lambda<0$)

$$\begin{array}{lll}
\displaystyle
V^\text{CPL}(t_0)
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}\mathbb{E}^{T_k}\left[
\text{max}\left(e^{-B(\tau_k)r(T_{k-1})}-\hat{K},0\right)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}
\int_{e^{-B(\tau_k)\mu_r(t_0,T_{k-1})+B(\tau_k)v_r(t_0,T_{k-1})z}>\hat{K}}
\left(e^{-B(\tau_k)\mu_r(t_0,T_{k-1})+B(\tau_k)v_r(t_0,T_{k-1})z}-\hat{K}\right)\frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz\\
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}
\int^a_{-\infty}
\left(e^{-B(\tau_k)\mu_r(t_0,T_{k-1})+B(\tau_k)v_r(t_0,T_{k-1})z}-\hat{K}\right)\frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz\\
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}\left[e^{\frac{1}{2}B^2(\tau_k)v_r^2(t_0,T_{k-1})-B(\tau_k)\mu_r(t_0,T_{k-1})}N(d_1)-\hat{K}N(d_2)\right]\\
\end{array}$$

where

$$\begin{array}{lll}
\hat{K}&=&(1+\tau_k K)e^{A(\tau_k)}\\
a&=&\displaystyle
\frac{\log\hat{K}+B(\tau_k)\mu_r(t_0,T_{k-1},\color{red}{T_k})}{B(\tau_k)v_r(t_0,T_{k-1})}\\
d_1&=&\displaystyle
a-B(\tau_k)v_r(t_0,T_{k-1})\\
d_2&=&a
\end{array}$$
