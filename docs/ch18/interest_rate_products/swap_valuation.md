# Swap Valuation

!!! tip "Key Idea"
    A swap is a portfolio of forward rate agreements. Its value is the difference between the present values of its fixed and floating legs. The swap rate is determined by no-arbitrage, not by forecasting future rates.

All interest rate derivatives are ultimately priced using discount factors. Forward rates, swaps, and swaptions are simply different ways of organizing these discounted cash flows. An interest rate swap exchanges a sequence of fixed payments for a sequence of floating payments. To determine its value, we compute the present value of each leg separately and take their difference.

Recall (see [§ Interest Rate Swap](interest_rate_swap.md)): the payer IRS admits the closed forms

$$
{\bf\text{IRS}}^{\text{Payer}}(t,{\cal T},N,K) = N A_{m,n}(t)(S_{m,n}(t) - K) = N(P(t,T_m) - P(t,T_n)) - N K A_{m,n}(t)
$$

The leg-by-leg derivation below recovers the second of these identities.

---

## Structure of a Swap

Recall (see [§ Interest Rate Swap](interest_rate_swap.md)): the swap has notional $N$, fixed rate $K$, payment dates $T_1, \dots, T_n$ with year fractions $\tau_i$. The fixed leg pays $NK\tau_i$ at each $T_i$; the floating leg pays $NL(T_{i-1}, T_{i-1}, T_i)\tau_i$.

---

## Present Value of the Fixed Leg

Let $P(0,T)$ denote the discount factor.

The value of the fixed leg is:

$$
\text{PV}_{\text{fixed}} = N K \sum_{i=1}^n \tau_i P(0, T_i)
$$

Define the **annuity factor**:

$$
A = \sum_{i=1}^n \tau_i P(0, T_i)
$$

Then:

$$
\text{PV}_{\text{fixed}} = N K A
$$

---

## Present Value of the Floating Leg

A key result simplifies the floating leg dramatically:

$$
\text{PV}_{\text{floating}} = N \bigl(1 - P(0, T_n)\bigr)
$$

**Interpretation.** Recall (see [§ Coupon-Bearing Bond and Floating-Rate Note](coupon_bond_and_frn.md)): an FRN with notional repayment is worth par at each reset. The floating leg equals the FRN minus the present value of the terminal principal, $N \cdot P(0, T_n)$, yielding the formula above.

---

## Value of the Swap

The value of a payer swap (pay fixed, receive floating) is:

$$
V_{\text{swap}} = \text{PV}_{\text{floating}} - \text{PV}_{\text{fixed}}
$$

Substituting:

$$
V_{\text{swap}} = N \bigl(1 - P(0, T_n)\bigr) - N K A
$$

---

## Par Swap Rate

At inception, the swap is typically priced to have zero value:

$$
V_{\text{swap}} = 0
$$

This determines the **par swap rate**:

$$
K^* = \frac{1 - P(0, T_n)}{A}
$$

---

## Interpretation

- If $K > K^*$: fixed leg is expensive → swap has negative value to payer  
- If $K < K^*$: fixed leg is cheap → swap has positive value to payer  

---

## Connection to FRA

Recall (see [§ Forward Rate Agreement](forward_rate_agreement.md) and [§ Interest Rate Swap](interest_rate_swap.md)): a swap decomposes into a strip of FRAs, $\text{Swap} = \sum_k \text{FRA}_k$. Each payment period corresponds to one forward rate contract, which is why swap valuation depends on forward rates derived from the yield curve.

---

## Bridge to Options

The swap value depends on the future evolution of interest rates through discount factors and forward rates. If we introduce optionality — the right but not the obligation to enter a swap — we obtain a **swaption** (see [§ From Swaps to Swaptions](bridge_to_swaptions.md)).

This transition from deterministic cash flow valuation to optionality mirrors the transition from forwards to options studied earlier.

!!! quote "Big Picture"
    All interest rate derivatives can be expressed in terms of discount factors. Bonds define the discount curve, FRAs extract forward rates, and swaps combine these into structured cash flows. Pricing reduces to present value under no-arbitrage.

---

## Exercises

**Exercise 1.** A 3-year payer swap has annual payments, notional $N = 1{,}000{,}000$, and fixed rate $K = 4\%$. The discount factors are $P(0,1) = 0.9615$, $P(0,2) = 0.9246$, $P(0,3) = 0.8890$. Compute the present values of the fixed and floating legs, and determine the swap value.

??? success "Solution to Exercise 1"
    With annual payments, $\tau_i = 1$ for all $i$.

    **Annuity factor**:

    $$
    A = P(0,1) + P(0,2) + P(0,3) = 0.9615 + 0.9246 + 0.8890 = 2.7751
    $$

    **Fixed leg PV**:

    $$
    \text{PV}_{\text{fixed}} = N K A = 1{,}000{,}000 \times 0.04 \times 2.7751 = 111{,}004
    $$

    **Floating leg PV**:

    $$
    \text{PV}_{\text{floating}} = N(1 - P(0, T_n)) = 1{,}000{,}000 \times (1 - 0.8890) = 111{,}000
    $$

    **Swap value (payer)**:

    $$
    V_{\text{swap}} = 111{,}000 - 111{,}004 = -4
    $$

    The swap has a negligible negative value, indicating the fixed rate is very close to the par swap rate.

---

**Exercise 2.** Using the discount factors from Exercise 1, compute the par swap rate $K^*$. Verify that setting $K = K^*$ gives $V_{\text{swap}} = 0$.

??? success "Solution to Exercise 2"
    The par swap rate is:

    $$
    K^* = \frac{1 - P(0, T_n)}{A} = \frac{1 - 0.8890}{2.7751} = \frac{0.1110}{2.7751} = 0.03999 \approx 4.00\%
    $$

    Setting $K = K^*$:

    $$
    V_{\text{swap}} = N(1 - P(0,T_n)) - NK^* A = 1{,}000{,}000 \times 0.1110 - 1{,}000{,}000 \times 0.03999 \times 2.7751 = 111{,}000 - 111{,}000 = 0
    $$

    Verified. $\square$

---

**Exercise 3.** Explain why the floating leg of a swap with notional $N$ has present value $N(1 - P(0, T_n))$. Start from the fact that a floating-rate note that resets at each payment date is worth par immediately after a reset.

??? success "Solution to Exercise 3"
    A floating-rate note (FRN) pays $N L(T_{i-1}, T_{i-1}, T_i) \tau_i$ at each $T_i$ plus the notional $N$ at $T_n$. Immediately after each coupon reset, the FRN reprices to par because its future coupons will reset to the prevailing market rate. Therefore at $t = 0$, a FRN paying coupons plus notional is worth $N$.

    The floating leg of the swap pays only the coupons, not the final notional. Its value is therefore the value of the full FRN minus the present value of the notional repayment:

    $$
    \text{PV}_{\text{floating}} = N - N P(0, T_n) = N(1 - P(0, T_n))
    $$

    This result holds regardless of the shape of the yield curve and does not require knowledge of individual forward rates. $\square$

---

**Exercise 4.** A swap has a fixed rate of 5% and the current par swap rate is 4.2%. Without computing exact numbers, determine the sign of the swap value for the payer and for the receiver. Explain your reasoning using the par swap rate interpretation.

??? success "Solution to Exercise 4"
    The payer pays fixed at $K = 5\%$ while the market rate is $K^* = 4.2\%$. The payer is overpaying relative to fair value, so the payer swap has **negative value**.

    $$
    V_{\text{payer}} = N(1 - P(0,T_n)) - NKA = N(K^* - K)A < 0
    $$

    since $K > K^*$.

    The receiver swap has the opposite sign: the receiver is receiving an above-market fixed rate, so the receiver swap has **positive value**.

    $$
    V_{\text{receiver}} = -V_{\text{payer}} > 0
    $$

    This is analogous to holding a forward contract that is in- or out-of-the-money relative to the current forward price.

---

**Exercise 5.** A 5-year payer swap with semi-annual payments has notional $N = 10{,}000{,}000$ and fixed rate $K = 3\%$. The annuity factor is $A = 4.55$ and the par swap rate is $S = 3.4\%$. Use the identity $V_{\text{payer}} = N A (S - K)$ to compute the mark-to-market value. Then verify your answer by computing $V = N(1 - P(0, T_n)) - N K A$, assuming $P(0, T_n) = 0.845$.

??? success "Solution to Exercise 5"

    Using the compact identity:

    $$
    V_{\text{payer}} = N A (S - K) = 10{,}000{,}000 \times 4.55 \times (0.034 - 0.030) = 10{,}000{,}000 \times 4.55 \times 0.004 = 182{,}000
    $$

    Verifying with the leg-by-leg form, $V = N(1 - P(0,T_n)) - N K A$:

    $$
    N(1 - P(0, T_n)) = 10{,}000{,}000 \times (1 - 0.845) = 1{,}550{,}000
    $$

    $$
    N K A = 10{,}000{,}000 \times 0.03 \times 4.55 = 1{,}365{,}000
    $$

    $$
    V_{\text{payer}} = 1{,}550{,}000 - 1{,}365{,}000 = 185{,}000
    $$

    The two methods give $\$182{,}000$ vs $\$185{,}000$; the small discrepancy reflects rounding in the given annuity factor and terminal discount factor (the two are not exactly consistent with the stated par rate). In practice both identities hold exactly because $S = (1 - P(0,T_n))/A$ by definition.

---

**Exercise 6.** Show that the par swap rate $K^* = (1 - P(0,T_n))/A$ is a weighted average of forward rates. Using $L_1 = 2.5\%$, $L_2 = 3.0\%$, $L_3 = 3.5\%$ for three annual periods, compute the par swap rate two ways: (i) bootstrap discount factors then apply $K^* = (1-P(0,T_3))/A$; (ii) use the weighted-average representation $S_{m,n}(t) = \sum_k \omega_k(t) L_k$ from [§ Interest Rate Swap](interest_rate_swap.md). Verify the two answers agree.

??? success "Solution to Exercise 6"

    **Bootstrap discount factors.** With annual tenor $\tau_k = 1$ and $P(0,0) = 1$:

    $$
    P(0,1) = \frac{1}{1.025} = 0.97561, \quad P(0,2) = \frac{0.97561}{1.030} = 0.94720, \quad P(0,3) = \frac{0.94720}{1.035} = 0.91516
    $$

    **Method (i): direct formula.**

    $$
    A = P(0,1) + P(0,2) + P(0,3) = 0.97561 + 0.94720 + 0.91516 = 2.83797
    $$

    $$
    K^* = \frac{1 - P(0,3)}{A} = \frac{1 - 0.91516}{2.83797} = \frac{0.08484}{2.83797} = 0.02990
    $$

    So $K^* \approx 2.990\%$.

    **Method (ii): weighted average of forward rates.** The weights are $\omega_k = \tau_k P(0, T_k)/A$:

    $$
    \omega_1 = \frac{0.97561}{2.83797} = 0.34378, \quad \omega_2 = \frac{0.94720}{2.83797} = 0.33377, \quad \omega_3 = \frac{0.91516}{2.83797} = 0.32247
    $$

    Note $\sum_k \omega_k = 1.00002 \approx 1$ (rounding).

    $$
    S = 0.34378 \times 0.025 + 0.33377 \times 0.030 + 0.32247 \times 0.035 = 0.008594 + 0.010013 + 0.011286 = 0.02989
    $$

    Both methods give $K^* \approx 2.99\%$, confirming the par swap rate is a weighted average of forward rates with weights proportional to the present value of a basis point at each payment date.