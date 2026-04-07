# Coupon-Bearing Bond and Floating-Rate Note

A **coupon-bearing bond** (CB) pays a fixed coupon at regular intervals plus the principal at maturity. Its value is the present value of these known cash flows. A **floating-rate note** (FRN) is a bond whose coupon resets to the current market rate at each payment date. Because the coupon always reflects prevailing rates, the FRN reprices to par immediately after each reset — a key property that simplifies swap valuation.

---

## Coupon-Bearing Bond

A coupon bond with face value $N$, coupon rate $c$, and payment dates $T_{m+1}, \ldots, T_n$ pays $Nc\tau_k$ at each $T_k$ plus principal $N$ at maturity $T_n$. Its value is the present value of all cash flows:

$$
\text{CB}(t, \mathcal{T}, N, c) = Nc\sum_{k=m+1}^{n} \tau_k P(t, T_k) + N P(t, T_n)
$$

Equivalently, defining the total cash flow at each date as $C_k = Nc\tau_k$ for $k < n$ and $C_n = Nc\tau_n + N$:

$$
\text{CB}(t, \mathcal{T}, N, c) = \sum_{k=m+1}^{n} C_k P(t, T_k)
$$

## Floating-Rate Note

At any reset date $T_m$, the FRN is worth par because its future coupons will reset to the prevailing market rate. At time $t$, its value is that par value discounted back from the next reset date:

$$
\text{FRN}(t, \mathcal{T}, N) = N P(t, T_m)
$$

???+ note "Proof"

    A floating-rate note is a Payer IRS with $K=0$ plus the principle $N$ available at $T_n$. So the value of this floating-rate note is

    $$\begin{array}{lll}
    {\bf\text{FRN}}(t,{\cal T},N)
    &=&
    {\bf\text{IRS}}^{\text{Payer}}(t,{\cal T},N,K=0)+NP(t,T_n)\\
    &=&
    N(P(t,T_m)-P(t,T_n))+NP(t,T_n)\\
    &=&
    NP(t,T_m)
    \end{array}$$

## Interest Rate Swap Valuation in Terms of FRN and CB

$$\begin{array}{lllllllll}
\displaystyle
{\bf\text{IRS}}^{\text{Payer}}(t,{\cal T},N,K)
&=&
N\sum_{k=m+1}^n\left(l_k(t)-K\right)\tau_kP(t,T_k)\\
&=&
NP(t,T_m)-N\left(P(t,T_n)+\sum_{k=m+1}^n K\tau_k P(t,T_k)\right)\\
&=&
{\bf\text{FRN}}(t,{\cal T},N)-{\bf\text{CB}}(t,{\cal T},N,{\cal C}=(K\tau_k))\\
\end{array}$$

The two legs of an IRS are two fundamental interest rate contracts. The fixed leg is a coupon-bearing bond (minus the principle at the end), and the floating leg is a floating-rate note (minus the principle at the end). Thus, an IRS is a swap contract exchanging the coupon-bearing bond for the floating-rate note.

*Adopted from Page 14 of Interest Rate Models - Theory and Practice by Damiano Brigo & Fabio Mercurio*

---

## Exercises

**Exercise 1.** A coupon-bearing bond has face value $N = 100$, annual coupon payments $c_k = 4$, and maturity in 3 years. Given discount factors $P(0,1) = 0.97$, $P(0,2) = 0.93$, $P(0,3) = 0.89$, compute the bond price $\text{CB}(0, \mathcal{T}, N, \mathcal{C})$ using the formula $N\sum_k c_k P(0, T_k)$ where the final coupon includes principal repayment.

??? success "Solution to Exercise 1"

    The bond pays annual coupons of $c_k = 4$ at $T = 1, 2, 3$ and returns the principal $N = 100$ at $T = 3$. The final cash flow at $T = 3$ is $c_3 + N = 4 + 100 = 104$.

    $$
    \text{CB}(0, \mathcal{T}, N, \mathcal{C}) = 4 \times P(0,1) + 4 \times P(0,2) + 104 \times P(0,3)
    $$

    $$
    = 4 \times 0.97 + 4 \times 0.93 + 104 \times 0.89
    $$

    $$
    = 3.88 + 3.72 + 92.56 = 100.16
    $$

    The bond price is $\$100.16$, slightly above par. This is consistent with the coupon rate ($4\%$) being slightly above the implied par yield. Indeed, the par yield for a 3-year annual bond with these discount factors is:

    $$
    c_{\mathrm{par}} = \frac{1 - P(0,3)}{P(0,1) + P(0,2) + P(0,3)} = \frac{1 - 0.89}{0.97 + 0.93 + 0.89} = \frac{0.11}{2.79} = 0.03943
    $$

    Since $4\% > 3.943\%$, the bond trades above par as expected.

---

**Exercise 2.** Prove that the value of a floating-rate note (FRN) at any reset date equals par (the face value $N$). Use a backward induction argument starting from the last payment date. What happens to the FRN value between reset dates?

??? success "Solution to Exercise 2"

    **Backward induction argument.** Let the FRN have face value $N$, payment dates $T_1, T_2, \ldots, T_n$ with $\tau_k = T_k - T_{k-1}$, and floating rate $l_k(T_{k-1})$ set at $T_{k-1}$ and paid at $T_k$.

    *Step 1 (terminal value).* At $T_n$, the FRN pays $N + N\tau_n l_n(T_{n-1})$. Just before this payment, the value is $N(1 + \tau_n l_n(T_{n-1}))$.

    *Step 2 (at $T_{n-1}$).* The present value of the $T_n$ cash flow, discounted at the prevailing rate $l_n(T_{n-1})$, is:

    $$
    V(T_{n-1}) = \frac{N(1 + \tau_n l_n(T_{n-1}))}{1 + \tau_n l_n(T_{n-1})} = N
    $$

    *Step 3 (induction).* At any reset date $T_{k-1}$, the FRN holder receives the coupon $N\tau_k l_k(T_{k-1})$ at $T_k$ and the FRN is again worth $N$ at $T_k$ (by induction). Therefore:

    $$
    V(T_{k-1}) = \frac{N\tau_k l_k(T_{k-1}) + N}{1 + \tau_k l_k(T_{k-1})} = N
    $$

    By induction, $V(T_k) = N$ at every reset date.

    **Between reset dates.** At time $t$ where $T_{k-1} < t < T_k$, the next cash flow at $T_k$ is already fixed at $N(1 + \tau_k l_k(T_{k-1}))$. The FRN value is:

    $$
    V(t) = N(1 + \tau_k l_k(T_{k-1})) \cdot P(t, T_k)
    $$

    This generally differs from $N$ because the discount factor $P(t, T_k)$ reflects current rates, while the coupon was fixed at $T_{k-1}$. The FRN trades at a "dirty price" that includes accrued floating interest, and it returns to par at each reset date.

---

**Exercise 3.** Using the relationship $\text{IRS}^{\text{Payer}} = \text{FRN} - \text{CB}$, show that a payer interest rate swap has zero value at inception if and only if the fixed rate $K$ equals the par swap rate. Derive the par swap rate in terms of discount factors.

??? success "Solution to Exercise 3"

    From the IRS decomposition:

    $$
    \text{IRS}^{\text{Payer}}(t, \mathcal{T}, N, K) = \text{FRN}(t, \mathcal{T}, N) - \text{CB}(t, \mathcal{T}, N, \mathcal{C})
    $$

    At inception ($t = T_m$, the first reset date), the FRN is worth par: $\text{FRN}(T_m, \mathcal{T}, N) = N P(T_m, T_m) = N$. The coupon bond with fixed rate $K$ and coupons $c_k = K\tau_k$ is valued as:

    $$
    \text{CB}(T_m, \mathcal{T}, N, \mathcal{C}) = N\sum_{k=m+1}^{n} K\tau_k P(T_m, T_k) + N \cdot P(T_m, T_n)
    $$

    Setting $\text{IRS}^{\text{Payer}} = 0$:

    $$
    N = N\sum_{k=m+1}^{n} K\tau_k P(T_m, T_k) + N \cdot P(T_m, T_n)
    $$

    $$
    1 - P(T_m, T_n) = K \sum_{k=m+1}^{n} \tau_k P(T_m, T_k) = K \cdot A_{m,n}(T_m)
    $$

    Solving for the par swap rate:

    $$
    K = S_{m,n}(T_m) = \frac{P(T_m, T_m) - P(T_m, T_n)}{A_{m,n}(T_m)} = \frac{1 - P(T_m, T_n)}{\sum_{k=m+1}^{n} \tau_k P(T_m, T_k)}
    $$

    The swap has zero value at inception if and only if $K$ equals this par swap rate, which makes the fixed-rate bond worth exactly par, matching the FRN value.

---

**Exercise 4.** Consider a 2-year swap with semi-annual payments, notional $N = 1{,}000{,}000$, and discount factors $P(0, 0.5) = 0.988$, $P(0, 1.0) = 0.975$, $P(0, 1.5) = 0.960$, $P(0, 2.0) = 0.945$. Compute the par swap rate $K$ such that the IRS has zero initial value.

??? success "Solution to Exercise 4"

    We have semi-annual payments with $\tau_k = 0.5$ for $k = 1, 2, 3, 4$ and discount factors $P(0, 0.5) = 0.988$, $P(0, 1.0) = 0.975$, $P(0, 1.5) = 0.960$, $P(0, 2.0) = 0.945$.

    The annuity factor is:

    $$
    A_{0,4}(0) = \sum_{k=1}^{4} \tau_k P(0, T_k) = 0.5(0.988 + 0.975 + 0.960 + 0.945) = 0.5 \times 3.868 = 1.934
    $$

    The par swap rate satisfies $\text{IRS} = 0$, so:

    $$
    K = S_{0,4}(0) = \frac{P(0, T_0) - P(0, T_4)}{A_{0,4}(0)} = \frac{1 - 0.945}{1.934} = \frac{0.055}{1.934} = 0.028438
    $$

    The par swap rate is $K \approx 2.844\%$ (annualized). This is the fixed rate at which the 2-year semi-annual swap has zero initial value.

    **Verification.** With this rate, the fixed leg PV is $N \cdot K \cdot A_{0,4}(0) = 1{,}000{,}000 \times 0.028438 \times 1.934 = 54{,}999$, and the floating leg PV is $N(P(0,T_0) - P(0,T_4)) = 1{,}000{,}000 \times 0.055 = 55{,}000$, confirming the swap value is approximately zero (the small difference is due to rounding).

---

**Exercise 5.** An investor holds a floating-rate note that resets quarterly. The most recent fixing was $L = 3.2\%$ and the next reset is in 60 days out of a 90-day accrual period. If $P(0, T_{\text{next}}) = 0.9975$ and $N = 100$, compute the current dirty price of the FRN using the fact that the FRN is worth par at the next reset date plus the accrued floating coupon.

??? success "Solution to Exercise 5"

    At the next reset date $T_{\text{next}}$, the FRN will be worth par: $V(T_{\text{next}}) = N = 100$. Additionally, at $T_{\text{next}}$ the holder receives the floating coupon that was fixed at the previous reset:

    $$
    \text{coupon} = N \times L \times \tau = 100 \times 0.032 \times \frac{90}{360} = 0.80
    $$

    (using ACT/360 day count convention with $\tau = 90/360$).

    The total cash flow at $T_{\text{next}}$ is $100 + 0.80 = 100.80$. Discounting back to today:

    $$
    V(0) = 100.80 \times P(0, T_{\text{next}}) = 100.80 \times 0.9975 = 100.548
    $$

    This is the dirty price. It exceeds par because the accrued floating coupon has been accumulating. Of the 90-day accrual period, 30 days have elapsed (since the next reset is 60 days away), so the accrued interest portion is:

    $$
    AI = 0.80 \times \frac{30}{90} = 0.2667
    $$

    The clean price is $V(0) - AI = 100.548 - 0.267 = 100.281$.

---

**Exercise 6.** Explain why the identity $\text{IRS}^{\text{Payer}} = \text{FRN} - \text{CB}$ implies that entering a payer swap is economically equivalent to being long a floating-rate note and short a fixed-rate bond (both without principal exchange at inception). How does this decomposition help in understanding the interest rate risk of a swap position?

??? success "Solution to Exercise 6"

    **Decomposition.** The identity $\text{IRS}^{\text{Payer}} = \text{FRN} - \text{CB}$ states that the payer swap replicates a portfolio that is long a floating-rate note and short a coupon bond, both with the same notional $N$ and payment schedule. The principal payments of $N$ at maturity cancel (long FRN receives $N$, short CB pays $N$), so only the interest payments remain---exactly the swap cash flows.

    Specifically:

    - The **floating leg** of the swap (receiving floating) corresponds to holding the FRN, which pays $N\tau_k l_k(T_{k-1})$ at each $T_k$.
    - The **fixed leg** of the swap (paying fixed) corresponds to shorting the coupon bond, which requires paying $NK\tau_k$ at each $T_k$.

    **Interest rate risk implications.** This decomposition reveals the risk profile of a payer swap:

    - The FRN resets to par at each fixing date, so it has very low duration (at most one period). Being long the FRN contributes negligible interest rate risk.
    - The coupon bond has substantial duration (approximately equal to the swap tenor for a par bond). Being short the CB means the payer swap has **negative duration** with respect to the fixed rate: when rates rise, the CB value falls, and the short CB position gains.

    Therefore, the payer swap behaves like a short position in a fixed-rate bond: it profits from rising rates and loses from falling rates. The duration of the swap approximately equals the negative of the coupon bond's duration, which is why swaps are widely used for interest rate hedging. A receiver swap, conversely, has positive duration analogous to holding a fixed-rate bond.
