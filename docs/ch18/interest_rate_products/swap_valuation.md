# Swap Valuation

!!! tip "Key Idea"
    A swap is a portfolio of forward rate agreements. Its value is the difference between the present values of its fixed and floating legs. The swap rate is determined by no-arbitrage, not by forecasting future rates.

An interest rate swap exchanges a sequence of fixed payments for a sequence of floating payments. To determine its value, we compute the present value of each leg separately and take their difference.

---

## Structure of a Swap

Consider a plain vanilla interest rate swap with:

- Notional: $N$
- Fixed rate: $K$
- Payment dates: $T_1, T_2, \dots, T_n$
- Year fractions: $\tau_i = T_i - T_{i-1}$

The two legs are:

- **Fixed leg:** pays $N K \tau_i$ at each $T_i$
- **Floating leg:** pays $N l(T_{i-1}, T_i) \tau_i$, where $l$ is the reference rate (simply compounded forward rate)

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

**Interpretation:**  
The floating leg is equivalent to holding a floating-rate note, which always resets to par. Its value is therefore close to the notional, adjusted for the final discount factor.

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

A swap can be decomposed into a portfolio of forward rate agreements:

$$
\text{Swap} = \sum \text{FRA}_i
$$

Each payment period corresponds to one forward rate contract. This decomposition explains why swap valuation depends on forward rates derived from the yield curve.

---

## Bridge to Options

The swap value depends on the future evolution of interest rates through discount factors and forward rates. If we introduce optionality — the right but not the obligation to enter a swap — we obtain a **swaption**.

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
    A floating-rate note (FRN) pays $N L(T_{i-1}, T_i) \tau_i$ at each $T_i$ plus the notional $N$ at $T_n$. Immediately after each coupon reset, the FRN reprices to par because its future coupons will reset to the prevailing market rate. Therefore at $t = 0$, a FRN paying coupons plus notional is worth $N$.

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