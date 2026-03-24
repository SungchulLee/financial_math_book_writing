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

## Libor Rate l_k(t) is a T_k-Martingale

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

---

## Exercises

**Exercise 1.** A payer FRA is entered at time $t = 0$ with reset date $T_0 = 0.5$, payment date $T_1 = 1.0$, notional $N = 1{,}000{,}000$, and fixed rate $K = 3\%$. If $P(0, 0.5) = 0.985$ and $P(0, 1.0) = 0.968$, compute the forward rate $l_1(0)$ and the FRA value at inception.

---

**Exercise 2.** Show that the fair fixed rate $K$ of a FRA (the rate making its initial value zero) equals the forward rate $l_k(t)$. Starting from $\text{FRA}(t, T_{k-1}, T_k, N, K) = N\tau_k(l_k(t) - K)P(t, T_k) = 0$, derive $K = l_k(t)$.

---

**Exercise 3.** Prove that the simply compounded forward rate $l_k(t) = \frac{1}{\tau_k}\left(\frac{P(t,T_{k-1})}{P(t,T_k)} - 1\right)$ is a martingale under the $T_k$-forward measure. Identify the numeraire and explain the economic intuition.

---

**Exercise 4.** At the reset date $T_{k-1}$, the payer FRA payoff is $N\tau_k(l_k(T_{k-1}) - K)$ paid at $T_k$, or equivalently $\frac{N\tau_k(l_k(T_{k-1}) - K)}{1 + \tau_k l_k(T_{k-1})}$ paid at $T_{k-1}$. Verify that these two expressions are consistent by discounting the $T_k$ payoff back to $T_{k-1}$ using $P(T_{k-1}, T_k) = \frac{1}{1 + \tau_k l_k(T_{k-1})}$.

---

**Exercise 5.** Given a set of traded FRA rates $K_1 = 2.5\%$, $K_2 = 2.8\%$, $K_3 = 3.1\%$ for consecutive 6-month periods starting at $T = 0.5, 1.0, 1.5$ respectively, extract the corresponding continuously compounded forward rates $R(t, T_{k-1}, T_k)$ using the conversion $R = \frac{1}{\tau}\ln(1 + \tau K)$.

---

**Exercise 6.** A portfolio contains a payer FRA and a receiver FRA on the same reset and payment dates but with different fixed rates $K_1$ and $K_2$ ($K_1 < K_2$). Show that the portfolio value is $N\tau_k(K_2 - K_1)P(t, T_k)$, independent of the forward rate. Interpret this as a deterministic cash flow and explain why it can be perfectly hedged with a zero-coupon bond.
