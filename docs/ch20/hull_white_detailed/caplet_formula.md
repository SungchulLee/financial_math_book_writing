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
