# Interest Rate Swap

## What is Interest Rate Swap?

An interest rate swap (IRS) is an agreement between two parties to exchange interest rate cash flows, based on a specified notional amount from a fixed rate to a floating rate (or vice versa).

## Tenor Structure

The interest rate swap length ($T_n-T_m$ in our notation) is called the tenor of the interest rate swap. Sometimes the set of reset and payment dates is called the tenor structure.

$$\begin{array}{lllllllllllllll}
&&\text{Time}&&\text{Action}\\
\text{Now}&&t&&\text{Enter the contract}\\
\text{Reset Date}&&T_{k-1} > t&&\text{Observe Float Rate}\ l_k(T_{k-1})\\
\text{Payment Date}&&T_k > T_{k-1} > t&&\text{Exchange Fixed and Float Interest on Principle}\\
\end{array}$$

## Interest Rate Swap Valuation

$$\begin{array}{lllllllll}
\displaystyle
{\bf\text{IRS}}^{\text{Payer}}(t,{\cal T},N,K)
&=&
\sum_{k=m+1}^n{\bf\text{FRA}}^{\text{Payer}}(t,T_{k-1},T_k,N,K)\\
&=&
N\sum_{k=m+1}^n\left(l_k(t)-K\right)\tau_kP(t,T_k)\\
&=&
NA_{m,n}(t)\left(S_{m,n}(t)-K\right)\\
&=&
N\left(P(t,T_m)-P(t,T_n)\right)-NK\sum_{k=m+1}^n \tau_k P(t,T_k)\\
\end{array}$$

and

$$\begin{array}{lllllllll}
\displaystyle
{\bf\text{IRS}}^{\text{Receiver}}(t,{\cal T},N,K)
&=&
-{\bf\text{IRS}}^{\text{Payer}}(t,{\cal T},N,K)
\end{array}$$

where

$$\begin{array}{llllll}
A_{m,n}(t)&=&\displaystyle\sum_{k=m+1}^n \tau_k P(t,T_k)\\
\omega_k(t)
&=&\displaystyle\frac{\tau_k P(t,T_k)}{\sum_{k'=m+1}^n\tau_{k'} P(t,T_{k'})}
&=&\displaystyle\frac{\tau_k P(t,T_k)}{A_{m,n}(t)}\\
S_{m,n}(t)&=&\displaystyle\sum_{k=m+1}^n \omega_k(t)l_k(t)
&=&\displaystyle\frac{P(t,T_{m})-P(t,T_n)}{A_{m,n}(t)}\\
\end{array}$$

As a byproduct, we have

$$\begin{array}{llllll}
A_{m,n}(t)S_{m,n}(t)
=P(t,T_{m})-P(t,T_n)
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lll}
    \displaystyle
    {\bf\text{IRS}}^{\text{Payer}}(t,{\cal T},N,K)
    &=&\displaystyle
    \sum_{k=m+1}^n {\bf\text{FRA}}^{\text{Payer}}(t,T_{k-1},T_k,N,K)\\
    &=&\displaystyle
    N\sum_{k=m+1}^n \left(l_k(t)-K\right)\tau_k P(t,T_k)
    \end{array}$$

    We simplify further using the annuity factor or present value of a basis point $A_{m,n}(t)$:

    $$\begin{array}{lll}
    \displaystyle
    S_{m,n}(t)
    &=&\displaystyle
    \sum_{k=m+1}^n \omega_k(t)l_k(t)\\
    &=&\displaystyle
    \frac{\sum_{k=m+1}^n \tau_k P(t,T_k)l_k(t)}{A_{m,n}(t)}\\
    &=&\displaystyle
    \frac{\sum_{k=m+1}^n \tau_k P(t,T_k)\frac{1}{\tau_k}\left(\frac{P(t,T_{k-1})}{P(t,T_k)}-1\right)}{A_{m,n}(t)}\\
    &=&\displaystyle
    \frac{\sum_{k=m+1}^n  \left(P(t,T_{k-1})-P(t,T_k)\right)}{A_{m,n}(t)}\\
    &=&\displaystyle
    \frac{P(t,T_{m})-P(t,T_n)}{A_{m,n}(t)}\\
    \end{array}$$

## Swap Rate in Terms of Discrete Forward Rates

$$\begin{array}{lll}
\displaystyle
S_{m,n}(t)
&=&\displaystyle
\frac{1-\prod_{j=m+1}^n\frac{1}{1+\tau_jL(t,T_{j-1},T_j)}}{\sum_{k=m+1}^n \tau_k \prod_{j=m+1}^k\frac{1}{1+\tau_jL(t,T_{j-1},T_j)}}\\
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lll}
    \displaystyle
    S_{m,n}(t)
    &=&\displaystyle
    \frac{P(t,T_{m})-P(t,T_n)}{A_{m,n}(t)}\\
    &=&\displaystyle
    \frac{1-\frac{P(t,T_n)}{P(t,T_{m})}}{\sum_{k=m+1}^n \tau_k \frac{P(t,T_k)}{P(t,T_{m})}}\\
    &=&\displaystyle
    \frac{1-\prod_{j=m+1}^n\frac{P(t,T_j)}{P(t,T_{j-1})}}{\sum_{k=m+1}^n \tau_k \prod_{j=m+1}^k\frac{P(t,T_j)}{P(t,T_{j-1})}}\\
    &=&\displaystyle
    \frac{1-\prod_{j=m+1}^n\frac{1}{1+\tau_jL(t,T_{j-1},T_j)}}{\sum_{k=m+1}^n \tau_k \prod_{j=m+1}^k\frac{1}{1+\tau_jL(t,T_{j-1},T_j)}}\\
    \end{array}$$
