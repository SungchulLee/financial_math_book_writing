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
