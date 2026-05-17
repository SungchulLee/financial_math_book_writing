# Interest Rate Swap

## What is Interest Rate Swap?

An interest rate swap (IRS) is an agreement between two parties to exchange interest rate cash flows, based on a specified notional amount from a fixed rate to a floating rate (or vice versa). Throughout, $L(t, T_{k-1}, T_k)$ denotes the simply compounded forward rate (see [§ Forward Rate Agreement](forward_rate_agreement.md)).

## Tenor Structure

The interest rate swap length ($T_n-T_m$ in our notation) is called the tenor of the interest rate swap. Sometimes the set of reset and payment dates is called the tenor structure.

$$\begin{array}{lllllllllllllll}
&&\text{Time}&&\text{Action}\\
\text{Now}&&t&&\text{Enter the contract}\\
\text{Reset Date}&&T_{k-1} > t&&\text{Observe Float Rate}\ L(T_{k-1},T_{k-1},T_k)\\
\text{Payment Date}&&T_k > T_{k-1} > t&&\text{Exchange Fixed and Float Interest on Principal}
\end{array}$$

## Interest Rate Swap Valuation

Recall (see [§ Forward Rate Agreement](forward_rate_agreement.md)): the payer FRA on $[T_{k-1}, T_k]$ has value $N(L(t,T_{k-1},T_k)-K)\tau_k P(t,T_k)$. Summing over the swap tenor gives the swap value. A self-contained leg-by-leg derivation with worked numerics and the par-rate identity appears in the dedicated [§ Swap Valuation](swap_valuation.md) page.

$$\begin{array}{lllllllll}
\displaystyle
{\bf\text{IRS}}^{\text{Payer}}(t,{\cal T},N,K)
&=&
\sum_{k=m+1}^n{\bf\text{FRA}}^{\text{Payer}}(t,T_{k-1},T_k,N,K)\\
&=&
N\sum_{k=m+1}^n\left(L(t,T_{k-1},T_k)-K\right)\tau_kP(t,T_k)\\
&=&
NA_{m,n}(t)\left(S_{m,n}(t)-K\right)\\
&=&
N\left(P(t,T_m)-P(t,T_n)\right)-NK\sum_{k=m+1}^n \tau_k P(t,T_k)
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
S_{m,n}(t)&=&\displaystyle\sum_{k=m+1}^n \omega_k(t)L(t,T_{k-1},T_k)
&=&\displaystyle\frac{P(t,T_{m})-P(t,T_n)}{A_{m,n}(t)}
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
    N\sum_{k=m+1}^n \left(L(t,T_{k-1},T_k)-K\right)\tau_k P(t,T_k)
    \end{array}$$

    We simplify further using the annuity factor or present value of a basis point $A_{m,n}(t)$:

    $$\begin{array}{lll}
    \displaystyle
    S_{m,n}(t)
    &=&\displaystyle
    \sum_{k=m+1}^n \omega_k(t)L(t,T_{k-1},T_k)\\
    &=&\displaystyle
    \frac{\sum_{k=m+1}^n \tau_k P(t,T_k)L(t,T_{k-1},T_k)}{A_{m,n}(t)}\\
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

??? success "Solution to Exercise 1"

    The swap has $T_m = 0$ (start date), $T_n = 3$, annual payments ($\tau_k = 1$ for all $k$), $N = 10{,}000{,}000$, and $K = 3.5\%$.

    Using the formula:

    $$
    \text{IRS}^{\text{Payer}} = N(P(0, T_m) - P(0, T_n)) - NK\sum_{k=1}^{3} \tau_k P(0, T_k)
    $$

    **Floating leg PV** (the first term):

    $$
    N(P(0,0) - P(0,3)) = 10{,}000{,}000 \times (1 - 0.900) = 10{,}000{,}000 \times 0.100 = 1{,}000{,}000
    $$

    **Fixed leg PV** (the second term):

    $$
    NK\sum_{k=1}^{3} \tau_k P(0, T_k) = 10{,}000{,}000 \times 0.035 \times (1 \times 0.970 + 1 \times 0.935 + 1 \times 0.900)
    $$

    $$
    = 10{,}000{,}000 \times 0.035 \times 2.805 = 982{,}750
    $$

    **Swap value:**

    $$
    \text{IRS}^{\text{Payer}} = 1{,}000{,}000 - 982{,}750 = 17{,}250
    $$

    The payer swap has a positive value of $\$17{,}250$. This is positive because the fixed rate $K = 3.5\%$ is below the par swap rate (computed in Exercise 2), so the payer (who pays fixed and receives floating) benefits from the higher market rates.

---

**Exercise 2.** Derive the par swap rate $S_{m,n}(t) = \frac{P(t,T_m) - P(t,T_n)}{A_{m,n}(t)}$ by setting the payer IRS value to zero. Using the discount factors from Exercise 1, compute the par swap rate for a 3-year annual swap.

??? success "Solution to Exercise 2"

    Setting $\text{IRS}^{\text{Payer}} = 0$:

    $$
    N(P(0, T_m) - P(0, T_n)) = NK \sum_{k=1}^{n} \tau_k P(0, T_k)
    $$

    Solving for $K$:

    $$
    S_{m,n}(0) = \frac{P(0, T_m) - P(0, T_n)}{\sum_{k=1}^{n} \tau_k P(0, T_k)} = \frac{P(0, T_m) - P(0, T_n)}{A_{m,n}(0)}
    $$

    With the given discount factors ($T_m = 0$, so $P(0,0) = 1$):

    $$
    A_{0,3}(0) = 1 \times 0.970 + 1 \times 0.935 + 1 \times 0.900 = 2.805
    $$

    $$
    S_{0,3}(0) = \frac{1 - 0.900}{2.805} = \frac{0.100}{2.805} = 0.035650
    $$

    The par swap rate is approximately $3.565\%$. Since the contractual rate in Exercise 1 was $K = 3.5\% < 3.565\%$, the payer underpays relative to par, which is why the swap had positive value to the payer.

---

**Exercise 3.** Show that the swap rate $S_{m,n}(t)$ is a weighted average of forward rates: $S_{m,n}(t) = \sum_k \omega_k(t) L(t,T_{k-1},T_k)$ where $\omega_k(t) = \tau_k P(t,T_k) / A_{m,n}(t)$. Verify that the weights sum to one.

??? success "Solution to Exercise 3"

    Starting from the swap rate definition:

    $$
    S_{m,n}(t) = \frac{P(t, T_m) - P(t, T_n)}{A_{m,n}(t)}
    $$

    We expand the numerator using a telescoping sum. Since $L(t,T_{k-1},T_k) = \frac{1}{\tau_k}\left(\frac{P(t,T_{k-1})}{P(t,T_k)} - 1\right)$, we have $P(t, T_{k-1}) - P(t, T_k) = \tau_k L(t,T_{k-1},T_k) P(t, T_k)$. Therefore:

    $$
    P(t, T_m) - P(t, T_n) = \sum_{k=m+1}^{n} (P(t, T_{k-1}) - P(t, T_k)) = \sum_{k=m+1}^{n} \tau_k L(t,T_{k-1},T_k) P(t, T_k)
    $$

    Dividing by $A_{m,n}(t)$:

    $$
    S_{m,n}(t) = \frac{\sum_{k=m+1}^{n} \tau_k L(t,T_{k-1},T_k) P(t, T_k)}{A_{m,n}(t)} = \sum_{k=m+1}^{n} \frac{\tau_k P(t, T_k)}{A_{m,n}(t)} \cdot L(t,T_{k-1},T_k) = \sum_{k=m+1}^{n} \omega_k(t) \, L(t,T_{k-1},T_k)
    $$

    where $\omega_k(t) = \frac{\tau_k P(t, T_k)}{A_{m,n}(t)}$.

    **Verification that the weights sum to one:**

    $$
    \sum_{k=m+1}^{n} \omega_k(t) = \sum_{k=m+1}^{n} \frac{\tau_k P(t, T_k)}{A_{m,n}(t)} = \frac{1}{A_{m,n}(t)} \sum_{k=m+1}^{n} \tau_k P(t, T_k) = \frac{A_{m,n}(t)}{A_{m,n}(t)} = 1
    $$

    Since each $\omega_k(t) > 0$ and $\sum_k \omega_k(t) = 1$, the swap rate is a weighted average of forward rates, with weights proportional to the present value of a basis point at each payment date. Longer-dated forward rates receive smaller weights because $P(t, T_k)$ decreases with maturity.

---

**Exercise 4.** Given forward rates $L(0, 0, 1) = 3.0\%$, $L(0, 1, 2) = 3.5\%$, $L(0, 2, 3) = 4.0\%$ with annual tenor $\tau = 1$, compute the 3-year par swap rate using the formula $S = \frac{1 - \prod_j(1+\tau_j L_j)^{-1}}{\sum_k \tau_k \prod_j^k(1+\tau_j L_j)^{-1}}$.

??? success "Solution to Exercise 4"

    Given annual forward rates $L_1 = 0.03$, $L_2 = 0.035$, $L_3 = 0.04$ with $\tau = 1$.

    **Step 1: Compute discount factors.** With $P(0,0) = 1$:

    $$
    P(0,1) = \frac{1}{1 + \tau_1 L_1} = \frac{1}{1.03} = 0.97087
    $$

    $$
    P(0,2) = \frac{P(0,1)}{1 + \tau_2 L_2} = \frac{0.97087}{1.035} = 0.93804
    $$

    $$
    P(0,3) = \frac{P(0,2)}{1 + \tau_3 L_3} = \frac{0.93804}{1.04} = 0.90196
    $$

    **Step 2: Apply the formula.** The numerator is:

    $$
    1 - \prod_{j=1}^{3} \frac{1}{1 + \tau_j L_j} = 1 - \frac{1}{1.03 \times 1.035 \times 1.04} = 1 - \frac{1}{1.10872} = 1 - 0.90196 = 0.09804
    $$

    The denominator is:

    $$
    \sum_{k=1}^{3} \tau_k \prod_{j=1}^{k} \frac{1}{1+\tau_j L_j} = 1 \times P(0,1) + 1 \times P(0,2) + 1 \times P(0,3)
    $$

    $$
    = 0.97087 + 0.93804 + 0.90196 = 2.81087
    $$

    The par swap rate is:

    $$
    S_{0,3}(0) = \frac{0.09804}{2.81087} = 0.034878
    $$

    The 3-year par swap rate is approximately $3.488\%$. This lies between the lowest ($3.0\%$) and highest ($4.0\%$) forward rates, as expected for a weighted average. It is closer to the lower forward rates because earlier periods carry larger discount factor weights.

---

**Exercise 5.** The annuity factor $A_{m,n}(t) = \sum_k \tau_k P(t, T_k)$ appears as the numeraire for the swap measure. Explain why the swap rate $S_{m,n}(t)$ is a martingale under the annuity measure $\mathbb{Q}^A$. What is the practical significance of this result for swaption pricing?

??? success "Solution to Exercise 5"

    **Martingale property under the annuity measure.** The annuity measure $\mathbb{Q}^A$ uses the annuity factor $A_{m,n}(t) = \sum_{k=m+1}^{n} \tau_k P(t, T_k)$ as numeraire. By the fundamental theorem of asset pricing, any traded asset price divided by the numeraire is a martingale under the corresponding measure.

    The payer swap value is:

    $$
    \text{IRS}^{\text{Payer}}(t) = N \cdot A_{m,n}(t) \cdot (S_{m,n}(t) - K)
    $$

    Dividing by the numeraire $A_{m,n}(t)$:

    $$
    \frac{\text{IRS}^{\text{Payer}}(t)}{A_{m,n}(t)} = N(S_{m,n}(t) - K)
    $$

    Since $K$ is a constant and the left side must be a $\mathbb{Q}^A$-martingale (as the ratio of a traded asset price to the numeraire), $S_{m,n}(t)$ itself must be a $\mathbb{Q}^A$-martingale:

    $$
    \mathbb{E}^{\mathbb{Q}^A}[S_{m,n}(T) \mid \mathcal{F}(t)] = S_{m,n}(t) \quad \text{for all } T > t
    $$

    **Practical significance for swaption pricing.** A European payer swaption with strike $K$ expiring at $T_m$ has payoff:

    $$
    \text{Swaption payoff} = N \cdot A_{m,n}(T_m) \cdot \max(S_{m,n}(T_m) - K, 0)
    $$

    Its price at time $t$ is:

    $$
    V(t) = N \cdot A_{m,n}(t) \cdot \mathbb{E}^{\mathbb{Q}^A}\!\left[\max(S_{m,n}(T_m) - K, 0) \mid \mathcal{F}(t)\right]
    $$

    Since $S_{m,n}(t)$ is a martingale under $\mathbb{Q}^A$, if we model it as a driftless process (e.g., geometric Brownian motion $dS = \sigma S \, dW^A$), the swaption price reduces to a Black-type formula:

    $$
    V(t) = N \cdot A_{m,n}(t) \cdot \mathrm{Black}(S_{m,n}(t), K, \sigma, T_m - t)
    $$

    This is the standard market model for swaptions. The key insight is that the swap rate's martingale property under $\mathbb{Q}^A$ eliminates the need for a drift term, making the pricing formula tractable and model-independent up to the choice of volatility.

---

**Exercise 6.** A receiver IRS with 5 years remaining has a fixed rate of $K = 4\%$ while the current par swap rate is $S = 3.2\%$. Is this swap an asset or a liability for the receiver? Without computing the exact value, explain qualitatively why and estimate the sign and approximate magnitude of the swap's mark-to-market value for a notional of \$50 million.

??? success "Solution to Exercise 6"

    **Sign of the swap value.** The receiver IRS receives fixed at $K = 4\%$ and pays floating. The current par swap rate is $S = 3.2\%$. Since $K > S$, the receiver is locked into receiving a fixed rate that exceeds the current market rate. This swap is an **asset** for the receiver.

    **Qualitative reasoning.** The receiver swap value is:

    $$
    \text{IRS}^{\text{Receiver}} = N \cdot A_{m,n}(t) \cdot (K - S_{m,n}(t))
    $$

    Since $K - S = 4\% - 3.2\% = 0.8\% = 80$ basis points, and this spread is positive, the swap has positive value.

    **Approximate magnitude.** For a 5-year swap with roughly semi-annual or annual payments, the annuity factor $A_{m,n}(t)$ is approximately the sum of discount factors times the year fractions. For annual payments, $A \approx 5 \times \bar{P}$ where $\bar{P}$ is the average discount factor. With rates around $3\%$--$4\%$, $\bar{P} \approx 0.92$, giving $A \approx 4.6$. For semi-annual payments, $A \approx 10 \times 0.5 \times \bar{P} \approx 4.6$ as well.

    $$
    \text{IRS}^{\text{Receiver}} \approx 50{,}000{,}000 \times 4.6 \times 0.008 = 1{,}840{,}000
    $$

    The swap is worth approximately $\$1.8$ million in favor of the receiver. This represents the present value of receiving 80 basis points above the market rate on \$50 million for 5 years.

---

**Exercise 7.** Show that an interest rate swap can be decomposed as a portfolio of FRAs: $\text{IRS}^{\text{Payer}} = \sum_k \text{FRA}^{\text{Payer}}(t, T_{k-1}, T_k, N, K)$. What does this imply about the replication of a swap using simpler instruments? Can each FRA be hedged independently?

??? success "Solution to Exercise 7"

    **Decomposition.** The payer IRS is valued as:

    $$
    \text{IRS}^{\text{Payer}}(t, \mathcal{T}, N, K) = N\sum_{k=m+1}^{n}(L(t,T_{k-1},T_k) - K)\tau_k P(t, T_k)
    $$

    Each term in the sum is exactly the value of a payer FRA:

    $$
    \text{FRA}^{\text{Payer}}(t, T_{k-1}, T_k, N, K) = N(L(t,T_{k-1},T_k) - K)\tau_k P(t, T_k)
    $$

    Therefore:

    $$
    \text{IRS}^{\text{Payer}}(t, \mathcal{T}, N, K) = \sum_{k=m+1}^{n} \text{FRA}^{\text{Payer}}(t, T_{k-1}, T_k, N, K)
    $$

    **Replication implications.** This decomposition means a swap can be replicated by entering into a strip of FRAs, one for each payment period, all with the same fixed rate $K$. Conversely, a strip of FRAs with the same fixed rate is economically identical to a swap.

    This has practical consequences:

    - **Pricing:** The swap price is the sum of FRA prices. If FRA markets are liquid, swap prices can be inferred directly.
    - **Bootstrapping:** The discount factor curve can be constructed from swap rates by recognizing each swap as a sum of FRAs.
    - **Risk decomposition:** The swap's total risk is the sum of the risks of its component FRAs, allowing period-by-period risk attribution.

    **Can each FRA be hedged independently?** Yes, in principle each FRA can be hedged independently using zero-coupon bonds. The $k$-th FRA has value $N\tau_k(L(t,T_{k-1},T_k) - K)P(t, T_k)$, which depends on $P(t, T_{k-1})$ and $P(t, T_k)$. It can be hedged by trading in the $T_{k-1}$ and $T_k$ maturity bonds.

    However, there is a subtlety: while the valuation decomposes additively, the hedging of each FRA involves positions in adjacent bonds, and these positions overlap between consecutive FRAs ($\text{FRA}_k$ involves $P(t, T_k)$ which also appears in $\text{FRA}_{k+1}$). In practice, the aggregate hedge of the full swap is more efficient than hedging each FRA separately, as overlapping bond positions can be netted. This netting is precisely why swaps are traded as single instruments rather than as strips of individual FRAs.
