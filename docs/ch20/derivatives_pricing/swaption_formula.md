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

## Swap Rate S_mn is a Q^mn-Martingale

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

## QuantPie Derivation: Hull-White Swaption Formula

### Change of Numeraire

$$\begin{array}{lll}
\displaystyle
\text{PAYOFF}^\text{Swaption}(T_m)
&=&\displaystyle
N\max\left(
\sum_{k=m+1}^n
\tau_k P(T_m,T_k)
\left(l_k(T_m)-K\right),0\right)
\end{array}$$

$$\begin{array}{lll}
\displaystyle
V^\text{Swaption}(t_0)
&=&\displaystyle
\mathbb{E}^\mathbb{Q}
\left[
\frac{M(t_0)}{M(T_m)}N\max\left(
\sum_{k=m+1}^n
\tau_k P(T_m,T_k)
\left(l_k(T_m)-K\right),0\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\max\left(
\sum_{k=m+1}^n
\tau_k P(T_m,T_k)
\left(l_k(T_m)-K\right),0\right)
\Big|{\cal F}(t_0)\right]\\
\end{array}$$

### Crucial Expression

$$\begin{array}{lll}
\displaystyle
\sum_{k=m+1}^n
\tau_k P(T_m,T_k)
\left(l_k(T_m)-K\right)
&=&\displaystyle
\sum_{k=m+1}^n
\tau_k P(T_m,T_k)
\left(\frac{1}{\tau_k}\left(\frac{P(T_m,T_{k-1})}{P(T_m,T_{k}))}-1\right)-K\right)\\
&=&\displaystyle
\sum_{k=m+1}^n
P(T_m,T_k)
\left(\left(\frac{P(T_m,T_{k-1})}{P(T_m,T_{k}))}-1\right)-K\tau_k\right)\\
&=&\displaystyle
\sum_{k=m+1}^n
\left(\left(P(T_m,T_{k-1})-P(T_m,T_k)\right)-K\tau_k P(T_m,T_k)\right)\\
&=&\displaystyle
1-P(T_m,T_n)
-K\sum_{k=m+1}^n \tau_k P(T_m,T_k)\\
&=&\displaystyle
1-\sum_{k=m+1}^n c_k P(T_m,T_k)\\
\end{array}$$

where

$$\begin{array}{lll}
c_k&=&
\left\{\begin{array}{lll}
K\tau_k&&\text{for $k\neq n$}\\
K\tau_k+1&&\text{for $k= n$}\\
\end{array}\right.
\end{array}$$

### Hull-White ZCB Price

$$\begin{array}{lll}
\displaystyle
V^\text{Swaption}(t_0)
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\max\left(
\sum_{k=m+1}^n
\tau_k P(T_m,T_k)
\left(l_k(T_m)-K\right),0\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\max\left(
1-\sum_{k=m+1}^n c_k P(T_m,T_k),0\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\max\left(
1-\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
\Big|{\cal F}(t_0)\right]\\
\end{array}$$

### Jamshidian Trick

The ZCB price $P(T_m,T_k)=e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)}$ at the swaption maturity $T_m$ is a function of the short rate $r(T_m)$ at $T_m$. Actually, the functions $r(T_m)\rightarrow P(T_m,T_k)$ are strictly decreasing. So, there is an $r^*$ such that

$$
\displaystyle
1=\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r^*}
$$

Then

$$\begin{array}{lll}
&&\displaystyle
\max\left(
1-\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)\\
&=&\displaystyle
\max\left(
\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r^*}-\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)\\
&=&\displaystyle
\left(
\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r^*}-\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)}\right)
1\left(r(T_m)>r^*\right)\\
&=&\displaystyle
\sum_{k=m+1}^n
c_k\left(e^{A(T_k-T_m)+B(T_k-T_m)r^*}-e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)}\right)
1\left(r(T_m)>r^*\right)\\
\end{array}$$

### Proof

$$\begin{array}{lll}
\displaystyle
V^\text{Swaption}(t_0)
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\max\left(
1-\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\max\left(
\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r^*}-\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\max\left(
\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r^*}-\sum_{k=m+1}^n c_k e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\mathbb{E}^{T_m}
\left[
\sum_{k=m+1}^n
c_k\left(e^{A(T_k-T_m)+B(T_k-T_m)r^*}-e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)}\right)
1\left(r(T_m)>r^*\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\sum_{k=m+1}^n c_k\mathbb{E}^{T_m}
\left[
\left(e^{A(T_k-T_m)+B(T_k-T_m)r^*}-e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)}\right)
1\left(r(T_m)>r^*\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\sum_{k=m+1}^n c_k\mathbb{E}^{T_m}
\left[
\max\left(
e^{A(T_k-T_m)+B(T_k-T_m)r^*}-e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
NP(t_0,T_m)\sum_{k=m+1}^n c_k\mathbb{E}^{T_m}
\left[
\max\left(
K_k-e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
\Big|{\cal F}(t_0)\right]\\
\end{array}$$

where

$$
\displaystyle
K_k=e^{A(T_k-T_m)+B(T_k-T_m)r^*}
$$

Note that

$$\begin{array}{lll}
\displaystyle
V^{\text{ZCB}}_{p}(t_0,T_m,T_k;K_k)=P(t_0,T_m)\mathbb{E}^{T_m}
\left[
\max\left(
K_k-e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
\Big|{\cal F}(t_0)\right]\\
\end{array}$$

is a European put option price on a zero-coupon bond with
option maturity $T_m$, bond maturity $T_k$, and strike $K_k$.
So,

$$\begin{array}{lll}
\displaystyle
V^\text{Swaption}(t_0)
&=&\displaystyle
NP(t_0,T_m)\sum_{k=m+1}^n c_k\mathbb{E}^{T_m}
\left[
\max\left(
K_k-e^{A(T_k-T_m)+B(T_k-T_m)r(T_m)},0\right)
\Big|{\cal F}(t_0)\right]\\
&=&\displaystyle
N\sum_{k=m+1}^n c_k V^{\text{ZCB}}_{p}(t_0,T_m,T_k;K_k)\\
\end{array}$$

---

## Exercises

**Exercise 1.** Explain why Jamshidian's trick works: show that since each $P(T_m, T_k) = e^{A(T_k - T_m) + B(T_k - T_m)r(T_m)}$ is a strictly decreasing function of $r(T_m)$, the max of the sum equals the sum of the maxes when all terms change sign at the same critical rate $r^*$.

??? success "Solution to Exercise 1"
    In the Hull-White model, each ZCB price at time $T_m$ has the form:

    $$
    P(T_m, T_k) = e^{A(T_k - T_m) + B(T_k - T_m)\,r(T_m)}
    $$

    Since $B(\tau) = \frac{e^{-\lambda\tau} - 1}{\lambda} < 0$ for $\tau > 0$, the exponent $A + B\,r$ is a decreasing linear function of $r(T_m)$. Therefore $P(T_m, T_k)$ is a strictly decreasing function of $r(T_m)$ for every $k$.

    The swaption payoff is $\max\!\left(1 - \sum_k c_k P(T_m, T_k),\, 0\right)$. Since each $P(T_m, T_k)$ is decreasing in $r(T_m)$, the sum $\sum_k c_k P(T_m, T_k)$ is also strictly decreasing in $r(T_m)$ (with $c_k > 0$). Therefore $1 - \sum_k c_k P(T_m, T_k)$ is strictly increasing in $r(T_m)$.

    There exists a unique $r^*$ where $\sum_k c_k P(T_m, T_k; r^*) = 1$, which is the boundary between exercise ($r < r^*$ for a payer swaption, since low rates make the payoff positive) and no exercise.

    At this critical point, we define $K_k = P(T_m, T_k; r^*) = e^{A(T_k-T_m)+B(T_k-T_m)r^*}$, and by construction $\sum_k c_k K_k = 1$.

    Since all terms $K_k - P(T_m, T_k)$ change sign simultaneously at $r^* = r(T_m)$ (because each $P(T_m,T_k)$ is monotonically decreasing), the region where $1 - \sum c_k P > 0$ is exactly the same as the region where every $K_k - P(T_m,T_k) > 0$. Therefore:

    $$
    \max\!\left(1 - \sum_k c_k P(T_m,T_k),\,0\right) = \sum_k c_k \max(K_k - P(T_m,T_k),\,0)
    $$

    This decomposition converts the max of a sum into a sum of maxes, each of which is a standard ZCB put option.

---

**Exercise 2.** For a payer swaption with $T_m = 5$, $T_n = 10$, annual payments, $K = 0.04$, and $N = 1{,}000{,}000$, write out the coefficients $c_k$ for $k = 6, 7, 8, 9, 10$. Verify that $c_{10} = K\tau_{10} + 1 = 1.04$.

??? success "Solution to Exercise 2"
    For a payer swaption with $K = 0.04$, $\tau_k = 1$ (annual payments), and $n = 10$:

    $$
    c_k = K\tau_k = 0.04 \times 1 = 0.04 \quad \text{for } k = 6, 7, 8, 9
    $$

    $$
    c_{10} = K\tau_{10} + 1 = 0.04 \times 1 + 1 = 1.04
    $$

    **Verification of $c_{10}$:** The coefficient $c_{10} = 1.04$ accounts for both the final fixed coupon payment ($K\tau_{10} = 0.04$) and the principal repayment (1) at the last payment date. This arises because the swap's floating leg at the last date pays $l_{10}\tau_{10}$ plus returns the notional, while the fixed leg pays $K\tau_{10}$ plus the notional. The "crucial expression" absorbs the notional exchange into $c_n$.

    Summary:

    | $k$ | $c_k$ |
    |:----|:------|
    | 6   | 0.04  |
    | 7   | 0.04  |
    | 8   | 0.04  |
    | 9   | 0.04  |
    | 10  | 1.04  |

---

**Exercise 3.** The critical rate $r^*$ satisfies $\sum_{k=m+1}^n c_k e^{A(T_k - T_m) + B(T_k - T_m)r^*} = 1$. Describe a numerical method (e.g., Newton-Raphson) for solving this equation. Why is the solution unique?

??? success "Solution to Exercise 3"
    The equation $\sum_{k=m+1}^n c_k e^{A(T_k - T_m) + B(T_k - T_m)r^*} = 1$ must be solved for $r^*$.

    Define $f(r) = \sum_{k=m+1}^n c_k e^{A(T_k - T_m) + B(T_k - T_m)r} - 1$.

    **Newton-Raphson iteration:**

    $$
    r^{(j+1)} = r^{(j)} - \frac{f(r^{(j)})}{f'(r^{(j)})}
    $$

    where

    $$
    f'(r) = \sum_{k=m+1}^n c_k B(T_k - T_m)\,e^{A(T_k - T_m) + B(T_k - T_m)r}
    $$

    A good initial guess is the par swap rate implied by the forward curve at $T_m$.

    **Uniqueness:** The function $f(r)$ is strictly monotone. Since $B(\tau) < 0$ for $\tau > 0$ and $c_k > 0$, each term $c_k e^{A+Br}$ is strictly decreasing in $r$, so $f(r)$ is strictly decreasing. Furthermore, $f(r) \to +\infty$ as $r \to -\infty$ and $f(r) \to -1$ as $r \to +\infty$. By the intermediate value theorem and strict monotonicity, there is exactly one root.

    Newton-Raphson converges rapidly (typically 3-5 iterations to machine precision) due to the smoothness of $f$.

---

**Exercise 4.** Compare the Black swaption formula (assuming lognormal swap rates) with the Hull-White swaption formula (sum of ZCB puts). Under what market conditions might the two formulas produce significantly different prices?

??? success "Solution to Exercise 4"
    **Black's swaption formula** assumes the swap rate $S_{mn}(t)$ is lognormal under the annuity measure $\mathbb{Q}^{mn}$, giving the standard Black-Scholes-type expression. This formula treats the swaption as a single option on the swap rate.

    **Hull-White swaption formula** decomposes the swaption into a portfolio of ZCB puts via Jamshidian's trick. The short rate is Gaussian, and each ZCB put has a closed-form solution.

    The two formulas produce different prices when:

    1. **Far from ATM strikes:** The lognormal and Gaussian-exponential distributions differ in their tails. Black's formula implies a flat smile (constant implied vol across strikes), while the Hull-White model generates a skew.

    2. **High vol-of-vol or long maturities:** For long-dated swaptions, the cumulative effect of the different distributional assumptions becomes more pronounced. The mean reversion in Hull-White reduces effective volatility for long maturities, while Black's formula applies a constant percentage volatility.

    3. **Strongly mean-reverting environments:** When $\lambda$ is large, the Hull-White model dampens rate movements substantially, producing lower prices than Black's formula calibrated to short-term ATM vols.

    At ATM, the two formulas typically agree closely because the distributional differences are minimized near the center of the distribution.

---

**Exercise 5.** Show that the swap rate $S_{mn}(t)$ is a martingale under the annuity measure $\mathbb{Q}^{mn}$. What is the numeraire for this measure, and why is this martingale property useful for Black's swaption formula?

??? success "Solution to Exercise 5"
    The annuity (or present value of a basis point, PVBP) is:

    $$
    A_{mn}(t) = \sum_{k=m+1}^n \tau_k P(t, T_k)
    $$

    The swap rate is defined as:

    $$
    S_{mn}(t) = \frac{P(t, T_m) - P(t, T_n)}{A_{mn}(t)}
    $$

    The numeraire for the annuity measure $\mathbb{Q}^{mn}$ is $A_{mn}(t)$. To show $S_{mn}$ is a martingale, note that the value of the payer swap at time $t$ is:

    $$
    \text{IRS}^{\text{Payer}}(t) = N\,A_{mn}(t)\,(S_{mn}(t) - K)
    $$

    Since the swap value divided by the numeraire $A_{mn}(t)$ must be a martingale under $\mathbb{Q}^{mn}$ (by the general change-of-numeraire theorem):

    $$
    \frac{\text{IRS}^{\text{Payer}}(t)}{A_{mn}(t)} = N(S_{mn}(t) - K)
    $$

    is a $\mathbb{Q}^{mn}$-martingale. Since $K$ is a constant, $S_{mn}(t)$ itself must be a $\mathbb{Q}^{mn}$-martingale:

    $$
    \mathbb{E}^{mn}[S_{mn}(t)\,|\,\mathcal{F}(s)] = S_{mn}(s) \quad \text{for } s \le t
    $$

    This martingale property is essential for Black's swaption formula because it allows us to model $dS_{mn} = \sigma_{mn} S_{mn}\,dW^{mn}$ under the annuity measure, apply Black-Scholes pricing with zero interest rate (the numeraire absorbs the discounting), and obtain the closed-form swaption price.

---

**Exercise 6.** The "crucial expression" rewrites the swaption payoff as $1 - \sum_{k=m+1}^n c_k P(T_m, T_k)$. Derive this step by step from $\sum_{k=m+1}^n \tau_k P(T_m, T_k)(l_k(T_m) - K)$, using the definition of the forward rate $l_k$.

??? success "Solution to Exercise 6"
    Starting from the swaption payoff:

    $$
    \sum_{k=m+1}^n \tau_k P(T_m, T_k)(l_k(T_m) - K)
    $$

    Using $l_k(T_m) = \frac{1}{\tau_k}\!\left(\frac{P(T_m, T_{k-1})}{P(T_m, T_k)} - 1\right)$:

    $$
    = \sum_{k=m+1}^n \tau_k P(T_m, T_k)\!\left(\frac{1}{\tau_k}\!\left(\frac{P(T_m, T_{k-1})}{P(T_m, T_k)} - 1\right) - K\right)
    $$

    $$
    = \sum_{k=m+1}^n \left(P(T_m, T_{k-1}) - P(T_m, T_k) - K\tau_k P(T_m, T_k)\right)
    $$

    The first two terms telescope:

    $$
    \sum_{k=m+1}^n (P(T_m, T_{k-1}) - P(T_m, T_k)) = P(T_m, T_m) - P(T_m, T_n) = 1 - P(T_m, T_n)
    $$

    So the expression becomes:

    $$
    1 - P(T_m, T_n) - K\sum_{k=m+1}^n \tau_k P(T_m, T_k)
    $$

    Now define $c_k = K\tau_k$ for $k \neq n$ and $c_n = K\tau_n + 1$. Then:

    $$
    \sum_{k=m+1}^n c_k P(T_m, T_k) = K\sum_{k=m+1}^n \tau_k P(T_m, T_k) + P(T_m, T_n)
    $$

    Therefore:

    $$
    1 - P(T_m, T_n) - K\sum_{k=m+1}^n \tau_k P(T_m, T_k) = 1 - \sum_{k=m+1}^n c_k P(T_m, T_k)
    $$

    This is the "crucial expression" used in Jamshidian's trick.

---

**Exercise 7.** In Jamshidian's trick, each ZCB put has its own strike $K_k = A(T_m, T_k)e^{-B(T_m, T_k)r^*}$. Explain why these strikes depend on $r^*$ and how an error in the root-finding for $r^*$ propagates to the swaption price.

??? success "Solution to Exercise 7"
    The strikes $K_k = e^{A(T_k - T_m) + B(T_k - T_m)r^*}$ depend on $r^*$ because they represent the ZCB prices evaluated at the critical short rate. Each $K_k$ is the bond price $P(T_m, T_k)$ when $r(T_m) = r^*$, which is the rate at which the holder is indifferent between exercising and not exercising the swaption.

    **Why they depend on $r^*$:** The decomposition into ZCB puts requires that all put options switch from in-the-money to out-of-the-money at the same short rate $r^*$. The strikes are chosen precisely to make this happen: $K_k = P(T_m, T_k; r^*)$ ensures that $K_k - P(T_m, T_k) > 0$ if and only if $r(T_m) > r^*$.

    **Error propagation:** If $r^*$ is computed with error $\delta r$, then:

    $$
    K_k^{\text{err}} = e^{A(T_k-T_m) + B(T_k-T_m)(r^* + \delta r)} = K_k \cdot e^{B(T_k-T_m)\,\delta r}
    $$

    Since each $K_k$ enters the ZCB put pricing formula, an error in $r^*$ shifts all strikes simultaneously. The swaption price error is approximately:

    $$
    \delta V \approx N\sum_{k=m+1}^n c_k \frac{\partial V_p^{\text{ZCB}}}{\partial K_k}\,B(T_k - T_m)\,K_k\,\delta r
    $$

    The sensitivity $\frac{\partial V_p^{\text{ZCB}}}{\partial K}$ is largest for near-ATM puts. Because $B(\tau) < 0$ and grows in magnitude with $\tau$, longer-dated ZCB puts are more affected. In practice, Newton-Raphson converges to machine precision in a few iterations, so the error from root-finding is negligible compared to model error.
