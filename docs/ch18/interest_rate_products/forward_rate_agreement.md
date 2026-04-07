# Forward Rate Agreement

Forward rate agreements (FRAs) are the simplest building blocks of interest rate derivatives. They allow two parties to lock in an interest rate for a future period, just as forward contracts lock in a future asset price. Every interest rate swap can be decomposed into a strip of FRAs, making them the atomic unit of the swap market.

---

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

??? success "Solution to Exercise 1"

    **Forward rate.** With $T_0 = 0.5$, $T_1 = 1.0$, and $\tau_1 = T_1 - T_0 = 0.5$:

    $$
    l_1(0) = \frac{1}{\tau_1}\left(\frac{P(0, T_0)}{P(0, T_1)} - 1\right) = \frac{1}{0.5}\left(\frac{0.985}{0.968} - 1\right) = 2 \times (1.017562 - 1) = 2 \times 0.017562 = 0.035124
    $$

    The forward rate is $l_1(0) \approx 3.5124\%$.

    **FRA value at inception.**

    $$
    \text{FRA}^{\text{Payer}}(0, T_0, T_1, N, K) = N\tau_1(l_1(0) - K)P(0, T_1)
    $$

    $$
    = 1{,}000{,}000 \times 0.5 \times (0.035124 - 0.03) \times 0.968
    $$

    $$
    = 1{,}000{,}000 \times 0.5 \times 0.005124 \times 0.968 = 2{,}480.02
    $$

    The payer FRA has a positive initial value of approximately $\$2{,}480$. This is positive because the forward rate ($3.51\%$) exceeds the contractual fixed rate ($3\%$), so the payer (who receives float and pays fixed) expects a net positive cash flow.

---

**Exercise 2.** Show that the fair fixed rate $K$ of a FRA (the rate making its initial value zero) equals the forward rate $l_k(t)$. Starting from $\text{FRA}(t, T_{k-1}, T_k, N, K) = N\tau_k(l_k(t) - K)P(t, T_k) = 0$, derive $K = l_k(t)$.

??? success "Solution to Exercise 2"

    Starting from the FRA valuation formula:

    $$
    \text{FRA}(t, T_{k-1}, T_k, N, K) = N\tau_k(l_k(t) - K)P(t, T_k)
    $$

    Setting the value to zero:

    $$
    N\tau_k(l_k(t) - K)P(t, T_k) = 0
    $$

    Since $N > 0$, $\tau_k > 0$, and $P(t, T_k) > 0$, the equation reduces to:

    $$
    l_k(t) - K = 0 \implies K = l_k(t)
    $$

    The fair fixed rate is:

    $$
    K = l_k(t) = \frac{1}{\tau_k}\left(\frac{P(t, T_{k-1})}{P(t, T_k)} - 1\right)
    $$

    This result is intuitive: the fair fixed rate in a FRA equals the market's implied forward rate for the same period. If $K > l_k(t)$, the fixed payer would overpay relative to the forward, giving the FRA negative value to the payer. If $K < l_k(t)$, the payer underpays, and the FRA has positive value. Equilibrium requires $K = l_k(t)$.

---

**Exercise 3.** Prove that the simply compounded forward rate $l_k(t) = \frac{1}{\tau_k}\left(\frac{P(t,T_{k-1})}{P(t,T_k)} - 1\right)$ is a martingale under the $T_k$-forward measure. Identify the numeraire and explain the economic intuition.

??? success "Solution to Exercise 3"

    We need to show that $l_k(t)$ is a martingale under the $T_k$-forward measure $\mathbb{Q}^{T_k}$, whose numeraire is the zero-coupon bond $P(t, T_k)$.

    **Proof.** The forward rate can be written as:

    $$
    l_k(t) = \frac{1}{\tau_k}\left(\frac{P(t, T_{k-1})}{P(t, T_k)} - 1\right) = \frac{1}{\tau_k}\left(\frac{P(t, T_{k-1}) - P(t, T_k)}{P(t, T_k)}\right)
    $$

    The numerator $P(t, T_{k-1}) - P(t, T_k)$ is the price of a portfolio long a $T_{k-1}$-bond and short a $T_k$-bond, which is a traded asset. Dividing any traded asset price by the numeraire $P(t, T_k)$ yields a martingale under $\mathbb{Q}^{T_k}$ (by the fundamental theorem of asset pricing). Since $l_k(t) = \frac{1}{\tau_k} \cdot \frac{P(t,T_{k-1}) - P(t,T_k)}{P(t,T_k)}$ is a constant multiple of such a ratio, it is also a $\mathbb{Q}^{T_k}$-martingale.

    Formally, for $s < t$:

    $$
    \mathbb{E}^{T_k}[l_k(t) \mid \mathcal{F}(s)] = \frac{1}{\tau_k}\mathbb{E}^{T_k}\!\left[\frac{P(t, T_{k-1}) - P(t, T_k)}{P(t, T_k)} \;\Big|\; \mathcal{F}(s)\right] = \frac{1}{\tau_k} \cdot \frac{P(s, T_{k-1}) - P(s, T_k)}{P(s, T_k)} = l_k(s)
    $$

    **Economic intuition.** The $T_k$-forward measure corresponds to using the $T_k$-maturity zero-coupon bond as numeraire. Under this measure, all asset prices expressed in units of this bond are martingales. The forward rate $l_k(t)$ determines the FRA payoff at $T_k$, and since the FRA payoff is settled at $T_k$ (the maturity of the numeraire bond), the natural pricing measure for this payoff is precisely $\mathbb{Q}^{T_k}$. The forward rate being a martingale under this measure means that its current value is the best (unbiased) predictor of its future value---no drift adjustment is needed when pricing FRA-related derivatives under $\mathbb{Q}^{T_k}$.

---

**Exercise 4.** At the reset date $T_{k-1}$, the payer FRA payoff is $N\tau_k(l_k(T_{k-1}) - K)$ paid at $T_k$, or equivalently $\frac{N\tau_k(l_k(T_{k-1}) - K)}{1 + \tau_k l_k(T_{k-1})}$ paid at $T_{k-1}$. Verify that these two expressions are consistent by discounting the $T_k$ payoff back to $T_{k-1}$ using $P(T_{k-1}, T_k) = \frac{1}{1 + \tau_k l_k(T_{k-1})}$.

??? success "Solution to Exercise 4"

    At the reset date $T_{k-1}$, the floating rate $l_k(T_{k-1})$ is observed. The payer FRA payoff at $T_k$ is:

    $$
    \text{Payoff at } T_k = N\tau_k(l_k(T_{k-1}) - K)
    $$

    To express this as a payment at $T_{k-1}$, we discount using $P(T_{k-1}, T_k)$. At $T_{k-1}$, the simply compounded rate for the period $[T_{k-1}, T_k]$ is $l_k(T_{k-1})$, so:

    $$
    P(T_{k-1}, T_k) = \frac{1}{1 + \tau_k l_k(T_{k-1})}
    $$

    The present value at $T_{k-1}$ of the $T_k$ payoff is:

    $$
    \text{Payoff at } T_{k-1} = N\tau_k(l_k(T_{k-1}) - K) \cdot P(T_{k-1}, T_k) = \frac{N\tau_k(l_k(T_{k-1}) - K)}{1 + \tau_k l_k(T_{k-1})}
    $$

    This confirms that the two expressions are consistent: the payment $N\tau_k(l_k(T_{k-1}) - K)$ at $T_k$ has the same economic value as $\frac{N\tau_k(l_k(T_{k-1}) - K)}{1 + \tau_k l_k(T_{k-1})}$ at $T_{k-1}$.

    We can also verify using the FRA valuation formula at $t = T_{k-1}$:

    $$
    \text{FRA}^{\text{Payer}}(T_{k-1}, T_{k-1}, T_k, N, K) = N\tau_k(l_k(T_{k-1}) - K) \cdot P(T_{k-1}, T_k) = \frac{N\tau_k(l_k(T_{k-1}) - K)}{1 + \tau_k l_k(T_{k-1})}
    $$

    This is the market-standard "discounted FRA" settlement: rather than waiting until $T_k$, the FRA is settled at $T_{k-1}$ by discounting the $T_k$ payoff at the just-observed floating rate.

---

**Exercise 5.** Given a set of traded FRA rates $K_1 = 2.5\%$, $K_2 = 2.8\%$, $K_3 = 3.1\%$ for consecutive 6-month periods starting at $T = 0.5, 1.0, 1.5$ respectively, extract the corresponding continuously compounded forward rates $R(t, T_{k-1}, T_k)$ using the conversion $R = \frac{1}{\tau}\ln(1 + \tau K)$.

??? success "Solution to Exercise 5"

    The conversion from simply compounded FRA rate $K$ to continuously compounded forward rate is:

    $$
    R(t, T_{k-1}, T_k) = \frac{1}{\tau}\ln(1 + \tau K)
    $$

    with $\tau = 0.5$ (6-month periods).

    **Period 1:** $[0.5, 1.0]$ with $K_1 = 2.5\% = 0.025$:

    $$
    R_1 = \frac{1}{0.5}\ln(1 + 0.5 \times 0.025) = 2\ln(1.0125) = 2 \times 0.012422 = 0.024845
    $$

    So $R_1 \approx 2.4845\%$.

    **Period 2:** $[1.0, 1.5]$ with $K_2 = 2.8\% = 0.028$:

    $$
    R_2 = \frac{1}{0.5}\ln(1 + 0.5 \times 0.028) = 2\ln(1.014) = 2 \times 0.013903 = 0.027806
    $$

    So $R_2 \approx 2.7806\%$.

    **Period 3:** $[1.5, 2.0]$ with $K_3 = 3.1\% = 0.031$:

    $$
    R_3 = \frac{1}{0.5}\ln(1 + 0.5 \times 0.031) = 2\ln(1.0155) = 2 \times 0.015381 = 0.030762
    $$

    So $R_3 \approx 3.0762\%$.

    In each case, the continuously compounded rate is slightly lower than the simply compounded rate. This is because continuous compounding generates more frequent interest accrual, so a lower rate is needed to produce the same discount factor over the period: $e^{-R\tau} = (1 + K\tau)^{-1}$. The difference is small for short tenors and low rates but grows with both.

---

**Exercise 6.** A portfolio contains a payer FRA and a receiver FRA on the same reset and payment dates but with different fixed rates $K_1$ and $K_2$ ($K_1 < K_2$). Show that the portfolio value is $N\tau_k(K_2 - K_1)P(t, T_k)$, independent of the forward rate. Interpret this as a deterministic cash flow and explain why it can be perfectly hedged with a zero-coupon bond.

??? success "Solution to Exercise 6"

    The portfolio consists of a payer FRA with fixed rate $K_1$ and a receiver FRA with fixed rate $K_2$, both on the same dates and notional.

    **Payer FRA value:**

    $$
    \text{FRA}^{\text{Payer}}(t, T_{k-1}, T_k, N, K_1) = N\tau_k(l_k(t) - K_1)P(t, T_k)
    $$

    **Receiver FRA value:**

    $$
    \text{FRA}^{\text{Receiver}}(t, T_{k-1}, T_k, N, K_2) = N\tau_k(K_2 - l_k(t))P(t, T_k)
    $$

    **Portfolio value:**

    $$
    V(t) = N\tau_k(l_k(t) - K_1)P(t, T_k) + N\tau_k(K_2 - l_k(t))P(t, T_k)
    $$

    $$
    = N\tau_k P(t, T_k)\bigl[(l_k(t) - K_1) + (K_2 - l_k(t))\bigr]
    $$

    $$
    = N\tau_k(K_2 - K_1)P(t, T_k)
    $$

    The forward rate $l_k(t)$ cancels completely. The portfolio value depends only on the fixed rates $K_1$, $K_2$ and the discount factor $P(t, T_k)$.

    **Interpretation.** The portfolio generates a deterministic cash flow of $N\tau_k(K_2 - K_1)$ at time $T_k$, regardless of where the floating rate fixes. Since $K_2 > K_1$, this cash flow is strictly positive.

    **Hedging.** This deterministic payoff is equivalent to holding $N\tau_k(K_2 - K_1)$ units of a zero-coupon bond maturing at $T_k$. The portfolio can therefore be perfectly replicated (and hedged) by purchasing this quantity of the $T_k$-maturity zero-coupon bond at cost $N\tau_k(K_2 - K_1)P(t, T_k)$, which is exactly the portfolio value. No exposure to future floating rates remains---all interest rate risk has been eliminated by the offsetting floating legs.
