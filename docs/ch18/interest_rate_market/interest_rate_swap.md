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

---

## Exercises

**Exercise 1.** A 3-year payer IRS with annual payments has notional $N = 10{,}000{,}000$, fixed rate $K = 3.5\%$, and discount factors $P(0,1) = 0.970$, $P(0,2) = 0.935$, $P(0,3) = 0.900$. Compute the swap value $\text{IRS}^{\text{Payer}}(0, \mathcal{T}, N, K)$ using the formula $N(P(0,T_m) - P(0,T_n)) - NK\sum_k \tau_k P(0, T_k)$.

---

**Exercise 2.** Derive the par swap rate $S_{m,n}(t) = \frac{P(t,T_m) - P(t,T_n)}{A_{m,n}(t)}$ by setting the payer IRS value to zero. Using the discount factors from Exercise 1, compute the par swap rate for a 3-year annual swap.

---

**Exercise 3.** Show that the swap rate $S_{m,n}(t)$ is a weighted average of forward rates: $S_{m,n}(t) = \sum_k \omega_k(t) l_k(t)$ where $\omega_k(t) = \tau_k P(t,T_k) / A_{m,n}(t)$. Verify that the weights sum to one.

---

**Exercise 4.** Given forward rates $L(0, 0, 1) = 3.0\%$, $L(0, 1, 2) = 3.5\%$, $L(0, 2, 3) = 4.0\%$ with annual tenor $\tau = 1$, compute the 3-year par swap rate using the formula $S = \frac{1 - \prod_j(1+\tau_j L_j)^{-1}}{\sum_k \tau_k \prod_j^k(1+\tau_j L_j)^{-1}}$.

---

**Exercise 5.** The annuity factor $A_{m,n}(t) = \sum_k \tau_k P(t, T_k)$ appears as the numeraire for the swap measure. Explain why the swap rate $S_{m,n}(t)$ is a martingale under the annuity measure $\mathbb{Q}^A$. What is the practical significance of this result for swaption pricing?

---

**Exercise 6.** A receiver IRS with 5 years remaining has a fixed rate of $K = 4\%$ while the current par swap rate is $S = 3.2\%$. Is this swap an asset or a liability for the receiver? Without computing the exact value, explain qualitatively why and estimate the sign and approximate magnitude of the swap's mark-to-market value for a notional of \$50 million.

---

**Exercise 7.** Show that an interest rate swap can be decomposed as a portfolio of FRAs: $\text{IRS}^{\text{Payer}} = \sum_k \text{FRA}^{\text{Payer}}(t, T_{k-1}, T_k, N, K)$. What does this imply about the replication of a swap using simpler instruments? Can each FRA be hedged independently?
