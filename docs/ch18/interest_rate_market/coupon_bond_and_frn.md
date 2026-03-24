# Coupon-Bearing Bond and Floating-Rate Note

## Coupon-Bearing Bond

$$\begin{array}{ccccccccccccccccc}
\displaystyle
{\bf\text{CB}}(t,{\cal T},N,{\cal C})
=
N\sum_{k=m+1}^n c_iP(t,T_i)\\
\end{array}$$

## Floating-Rate Note

$$\begin{array}{ccccccccccccccccc}
\displaystyle
{\bf\text{FRN}}(t,{\cal T},N)
=
NP(t,T_m)\\
\end{array}$$

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

---

**Exercise 2.** Prove that the value of a floating-rate note (FRN) at any reset date equals par (the face value $N$). Use a backward induction argument starting from the last payment date. What happens to the FRN value between reset dates?

---

**Exercise 3.** Using the relationship $\text{IRS}^{\text{Payer}} = \text{FRN} - \text{CB}$, show that a payer interest rate swap has zero value at inception if and only if the fixed rate $K$ equals the par swap rate. Derive the par swap rate in terms of discount factors.

---

**Exercise 4.** Consider a 2-year swap with semi-annual payments, notional $N = 1{,}000{,}000$, and discount factors $P(0, 0.5) = 0.988$, $P(0, 1.0) = 0.975$, $P(0, 1.5) = 0.960$, $P(0, 2.0) = 0.945$. Compute the par swap rate $K$ such that the IRS has zero initial value.

---

**Exercise 5.** An investor holds a floating-rate note that resets quarterly. The most recent fixing was $L = 3.2\%$ and the next reset is in 60 days out of a 90-day accrual period. If $P(0, T_{\text{next}}) = 0.9975$ and $N = 100$, compute the current dirty price of the FRN using the fact that the FRN is worth par at the next reset date plus the accrued floating coupon.

---

**Exercise 6.** Explain why the identity $\text{IRS}^{\text{Payer}} = \text{FRN} - \text{CB}$ implies that entering a payer swap is economically equivalent to being long a floating-rate note and short a fixed-rate bond (both without principal exchange at inception). How does this decomposition help in understanding the interest rate risk of a swap position?
