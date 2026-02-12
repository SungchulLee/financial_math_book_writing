# Forward Rate Agreement

## Payer/Receiver Forward Rate Agreement

$$\begin{array}{lllllllllllllll}
&&\text{Time}&&\text{Action}&&\text{Value}\\
\text{Now}&&t&&\text{Enter Payer FRA with Fixed Rate $K$ and Principle $N$}&&{\bf\text{FRA}}^{\text{Payer}}(t,T_{k-1},T_k,N,K)=N\left(l_k(t)-K\right)\tau_k P(t,T_k)\\
&&&&\text{Enter Receiver FRA with Fixed Rate $K$ and Principle $N$}&&{\bf\text{FRA}}^{\text{Receiver}}(t,T_{k-1},T_k,N,K)=N\left(K-l_k(t)\right)\tau_k P(t,T_k)\\
\\
\text{Reset Date}&&T_{k-1} > t&&\text{Observe Float Rate}\ l_k(T_{k-1})\ \text{and Fix Payer FRA Payment at $T_k$}&&\displaystyle {\bf\text{FRA}}^{\text{Payer}}(T_{k-1},T_{k-1},T_k,N,K)=\frac{N\tau_k(l_k(T_{k-1})-K)}{1+\tau_kl_k(T_{k-1})}=N\left(l_k(T_{k-1})-K\right)\tau_kP(T_{k-1},T_k)\\
\\
\text{Payment Date}&&T_k > T_{k-1} > t&&\text{Exchange Fixed and Float Interest on Principle}&&{\bf\text{FRA}}^{\text{Payer}}(T_{k-1},T_{k-1},T_k,N,K)=N(l_k(T_{k-1})-K)\tau_k\\
\end{array}$$

where

$$\begin{array}{lll}
\tau_k&=&\tau(T_{k-1},T_k)\\
l_k(t)&=&\displaystyle\frac{1}{\tau_k}\left(\frac{P(t,T_{k-1})}{P(t,T_k)}-1\right)\\
\end{array}$$

## Forward Rate from FRA

If we have a traded FRA, meaning ${\bf\text{FRA}}(t, T_{k-1}, T_k, N, K)=0$ or $l_k(t)=K$, then we can extract the forward rate from this market data:

$$
\displaystyle
\frac{1}{\tau_k}\left(\frac{P(t,T_{k-1})}{P(t,T_{k})}-1\right)=K
\quad\Rightarrow\quad
R(t,T_{k-1},T_k)=\frac{1}{T_k-T_{k-1}}\log(1+\tau_kK)
$$

## Libor Rate $l_k(t)$ is a $\mathbb{T_k}$-Martingale

With tenor $\tau_k=T_k-T_{k-1}$

$$\begin{array}{lll}
\displaystyle
l_k(t)=l(t;T_{k-1},T_k)=\frac{1}{\tau_k}\left(\frac{P(t,T_{k-1})}{P(t,T_k)}-1\right)
=\frac{1}{\tau_k}\left(\frac{P(t,T_{k-1})-P(t,T_k)}{P(t,T_k)}\right)
\end{array}$$

is a $\mathbb{T_k}$-martingale.

???+ note "Proof"

    $$\begin{array}{lll}
    \displaystyle
    \mathbb{E}^{\mathbb{T_k}}\left[l\left(T_{k-1};T_{k-1},T_k\right)|{\cal F}(t)\right]
    &=&\displaystyle
    \frac{1}{\tau_k}\mathbb{E}^{\mathbb{T_k}}\left[\frac{P(T_{k-1},T_{k-1})-P(T_{k-1},T_k)}{P(T_{k-1},T_k)}\Big{|}{\cal F}(t)\right]\\
    &=&\displaystyle
    \frac{1}{\tau_k}\frac{P(t,T_{k-1})-P(t,T_k)}{P(t,T_k)}\\
    &=&\displaystyle
    l\left(t;T_{k-1},T_k\right)\\
    \end{array}$$

## FRA Valuation via Change of Numeraire

$$\begin{array}{lll}
\displaystyle
{\bf\text{FRA}}(t,T_{k-1},T_k,N,K)=N\tau_k\left(l_k(t)-K\right) P(t,T_k)\\
\end{array}$$

The fair value $K$, which makes $V(t)=0$, is given by

$$\begin{array}{lll}
\displaystyle
K=l_k(t)=l(t,T_{k-1},T_k)
\end{array}$$

???+ note "Proof"

    Since $l_k(t)=\frac{1}{\tau_k}(\frac{P(t,T_{k-1})}{P(t,T_k)}-1)$,
    we have

    $$
    \displaystyle
    \frac{1}{1+\tau_k l_k(T_{k-1})}= P(T_{k-1},T_k)
    $$

    Therefore,

    $$\begin{array}{lll}
    \displaystyle
    {\bf\text{FRA}}(t,T_{k-1},T_k,N,K)
    &=&\displaystyle
    NM(t)
    \mathbb{E^{\mathbb{Q}}}\left[\frac{P(T_{k-1},T_k)\tau_k(l(T_{k-1};T_{k-1},T_k)-K)}{M(T_{k-1})}\Big{|}{\cal F}(t)\right]\\
    &=&\displaystyle
    NM(t)
    \mathbb{E^{\mathbb{Q}}}\left[\frac{\left(P(T_{k-1},T_{k-1})-P(T_{k-1},T_k)\right)-K\tau_k P(T_{k-1},T_k)}{M(T_{k-1})}\Big{|}{\cal F}(t)\right]\\
    &=&\displaystyle
    NM(t)
    \frac{\left(P(t,T_{k-1})-P(t,T_k)\right)-K\tau_k P(t,T_k)}{M(t)}\\
    &=&\displaystyle
    N\tau_k \left(l_k(t)-K\right)P(t,T_k)\\
    \end{array}$$
