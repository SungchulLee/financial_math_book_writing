# Hull-White Swaption Formula

## Swaption Payoff and Change of Numeraire

$$\begin{array}{lll}
\displaystyle
\text{PAYOFF}^\text{Swaption}(T_m)
&=&\displaystyle
N\max\left(A_{mn}(T_m)\left(S_{mn}(T_m)-K\right),0\right)
\end{array}$$

$$\begin{array}{lll}
\displaystyle
V^\text{Swaption}(t_0)
&=&\displaystyle
\mathbb{E}^\mathbb{Q}\left[\frac{M(t_0)}{M(T_m)}N\max\left(A_{mn}(T_m)(S_{mn}(T_m)-K),0\right)\Big{|}{\cal F}(t_0)\right]
\end{array}$$

## Swap Rate $S_{mn}$ is a $\mathbb{Q}^{mn}$-Martingale

Since $S_{mn}(t)=\sum_{k=m+1}^n \omega_k(t)l_k(t)=\frac{P(t,T_{m})-P(t,T_n)}{A_{mn}(t)}$ and since $P(t,T_{m})$ and $P(t,T_{n})$ are prices of tradable assets,

$$\begin{array}{lll}
\displaystyle
\mathbb{E}^{mn}\left[S_{mn}(t)\Big{|}{\cal F}(s)\right]
=S_{mn}(s)
\end{array}$$

## Black Type Formula

Assume that the swap rate follows a lognormal distribution:

$$\begin{array}{lll}
\displaystyle
dS_{mn}(t)
=
\sigma_{mn}S_{mn}(t)dW^{mn}(t)
\end{array}$$

Then, we can use the Black–Scholes computation with interest rate 0:

$$\begin{array}{lll}
\displaystyle
V^\text{Swaption,Payer}(t_0)
&=&\displaystyle
NA_{mn}(t_0)\left[S_{mn}(t_0)N(d_1)-KN(d_2)\right]\\
\displaystyle
V^\text{Swaption,Receiver}(t_0)
&=&\displaystyle
NA_{mn}(t_0)\left[-S_{mn}(t_0)N(-d_1)+KN(-d_2)\right]\\
\end{array}$$

where

$$\begin{array}{lll}
d_1&=&\displaystyle
\frac{1}{v}\log\frac{S_{mn}(t_0)}{K}+\frac{1}{2}v\\
d_2&=&\displaystyle
\frac{1}{v}\log\frac{S_{mn}(t_0)}{K}-\frac{1}{2}v\\
v&=&\sigma_{mn}\sqrt{T_m-t_0}
\end{array}$$

## Hull-White Swaption Formula

$$\begin{array}{lll}
\displaystyle
V^\text{Swaption}(t_0)
=
N\sum_{k=m+1}^n c_k V^{\text{ZCB}}_{p}(t_0,T_m,T_k;K_k)\\
\end{array}$$

where

$$\begin{array}{lll}
c_k&=&
\left\{\begin{array}{lll}
K\tau_k&&\text{for $k\neq n$}\\
K\tau_k+1&&\text{for $k= n$}\\
\end{array}\right.\\
K_k&=&A(T_m,T_k)e^{-B(T_m,T_k)r^*}
\end{array}$$

## Crucial Expression

$$\begin{array}{lll}
\displaystyle
\sum_{k=m+1}^n
\tau_k P(T_m,T_k)
\left(l_k(T_m)-K\right)
&=&\displaystyle
\sum_{k=m+1}^n
\left(P(T_m,T_{k-1})-P(T_m,T_k)\right)
-\sum_{k=m+1}^n K\tau_k P(T_m,T_k)\\
&=&\displaystyle
1-\sum_{k=m+1}^n c_k P(T_m,T_k)
\end{array}$$

## Jamshidian Trick

The ZCB price $P(T_m,T_k)=e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)}$ at the swaption maturity $T_m$ is a function of the short rate $r(T_m)$ at $T_m$. Actually, the functions $r(T_m)\rightarrow P(T_m,T_k)$ are strictly decreasing. So, there exists a unique $r^*$ such that

$$
\displaystyle
\sum_{k=m+1}^nc_kP(T_m,T_k,r^*)=1
$$

Using this, the swaption payoff can be decomposed into a sum of ZCB put options:

$$\begin{array}{lll}
\displaystyle
V^\text{Swaption}(t_0)
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\max\left(
1-\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
\Big{|}{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\sum_{k=m+1}^n c_k\left(K_k-P(T_m,T_k)\right)^+
\Big{|}{\cal F}(t_0)\right]\\
&=&\displaystyle
N\sum_{k=m+1}^n c_k\cdot{\bf\text{ZBP}}(t_0,T_m,T_k;K_k)
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lll}
    \displaystyle
    V^\text{Swaption}(t_0)
    &=&\displaystyle
    NP(t_0,T_m)\mathbb{E}^{T_m}
    \left[
    \max\left(
    1-\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
    \Big{|}{\cal F}(t_0)\right]\\
    &=&\displaystyle
    NP(t_0,T_m)\mathbb{E}^{T_m}
    \left[
    \max\left(
    \sum_{k=m+1}^n c_k K_k
    -\sum_{k=m+1}^n c_k P(T_m,T_k),0\right)
    \Big{|}{\cal F}(t_0)\right]\\
    \end{array}$$

    Since all $P(T_m,T_k)$ are decreasing functions of $r(T_m)$, the sign of each term $K_k - P(T_m,T_k)$ changes at the same $r^*$. Therefore the max of the sum equals the sum of the maxes:

    $$\begin{array}{lll}
    &=&\displaystyle
    NP(t_0,T_m)\sum_{k=m+1}^n c_k\mathbb{E}^{T_m}
    \left[\left(K_k-P(T_m,T_k)\right)^+
    \Big{|}{\cal F}(t_0)\right]\\
    &=&\displaystyle
    N\sum_{k=m+1}^n c_k\cdot{\bf\text{ZBP}}(t_0,T_m,T_k;K_k)
    \end{array}$$
