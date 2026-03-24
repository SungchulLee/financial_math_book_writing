# Caplet and Swaption Formulas

Caps, floors, and swaptions are the primary volatility instruments in interest rate markets. A **cap** is a strip of caplets, each protecting against a floating rate exceeding a strike, while a **swaption** is an option to enter an interest rate swap. In the Vasicek model, both reduce to portfolios of zero-coupon bond options, which have closed-form solutions. This section derives the caplet formula by showing it is equivalent to a put on a ZCB, extends the result to caps and floors, and applies Jamshidian's trick to obtain swaption prices.

---

## Caplet as a bond option

### Caplet payoff

A caplet on the simply compounded rate $L(T_{k-1}, T_k)$ over the accrual period $[T_{k-1}, T_k]$ with day count fraction $\delta_k = T_k - T_{k-1}$ and strike rate $\kappa_{\text{cap}}$ pays at time $T_k$:

$$
\delta_k\,(L(T_{k-1}, T_k) - \kappa_{\text{cap}})^+
$$

### Reduction to a ZCB put

The simply compounded rate satisfies $L(T_{k-1}, T_k) = (1/P(T_{k-1}, T_k) - 1)/\delta_k$, so

$$
\delta_k\,(L(T_{k-1}, T_k) - \kappa_{\text{cap}})^+ = \left(\frac{1}{P(T_{k-1}, T_k)} - 1 - \delta_k\,\kappa_{\text{cap}}\right)^+ \cdot P(T_{k-1}, T_k)
$$

Multiplying and dividing:

$$
= (1 + \delta_k\,\kappa_{\text{cap}})\!\left(\frac{1}{1 + \delta_k\,\kappa_{\text{cap}}} - P(T_{k-1}, T_k)\right)^+
$$

Define the **adjusted strike** $K_k = \frac{1}{1 + \delta_k\,\kappa_{\text{cap}}}$. Then the caplet payoff at $T_k$ is

$$
(1 + \delta_k\,\kappa_{\text{cap}})\,(K_k - P(T_{k-1}, T_k))^+
$$

This is $(1 + \delta_k\,\kappa_{\text{cap}})$ units of a European **put** on the ZCB $P(T_{k-1}, T_k)$ with strike $K_k$ and expiry $T_{k-1}$, but with the payoff received at $T_k$.

Discounting the $T_k$-payoff to $T_{k-1}$, the value at time $t$ is

$$
\boxed{\text{Caplet}(t) = (1 + \delta_k\,\kappa_{\text{cap}})\,\text{Put}_{\text{ZCB}}(t;\, K_k,\, T_{k-1},\, T_k)}
$$

where $\text{Put}_{\text{ZCB}}(t; K, T, S) = K\,P(t,T)\,\Phi(-d_2) - P(t,S)\,\Phi(-d_1)$ is the Vasicek ZCB put formula.

---

## Cap and floor formulas

### Cap

A **cap** with strike $\kappa_{\text{cap}}$ on reset dates $T_0, T_1, \ldots, T_{n-1}$ and payment dates $T_1, \ldots, T_n$ is a strip of caplets:

$$
\text{Cap}(t) = \sum_{k=1}^n (1 + \delta_k\,\kappa_{\text{cap}})\,\text{Put}_{\text{ZCB}}(t;\, K_k,\, T_{k-1},\, T_k)
$$

### Floor

By analogous reasoning, a **floorlet** (paying $\delta_k(\kappa_{\text{floor}} - L(T_{k-1}, T_k))^+$ at $T_k$) is equivalent to a ZCB call:

$$
\text{Floorlet}(t) = (1 + \delta_k\,\kappa_{\text{floor}})\,\text{Call}_{\text{ZCB}}(t;\, K_k,\, T_{k-1},\, T_k)
$$

A **floor** is the sum of floorlets:

$$
\text{Floor}(t) = \sum_{k=1}^n (1 + \delta_k\,\kappa_{\text{floor}})\,\text{Call}_{\text{ZCB}}(t;\, K_k,\, T_{k-1},\, T_k)
$$

### Cap-floor parity

Cap minus floor equals a payer swap when both use the same strike:

$$
\text{Cap}(t) - \text{Floor}(t) = \text{Swap}_{\text{payer}}(t)
$$

This identity serves as a consistency check for implementations.

---

## Forward rate volatility

The volatility parameter entering the caplet formula is the **bond option volatility**

$$
\sigma_{P,k} = B(T_k - T_{k-1})\,\sigma\,\sqrt{\frac{1 - e^{-2\kappa(T_{k-1} - t)}}{2\kappa}}
$$

For short accrual periods $\delta_k \ll 1$, $B(\delta_k) \approx \delta_k$, and the bond option volatility becomes

$$
\sigma_{P,k} \approx \delta_k\,\sigma\,\sqrt{\frac{1 - e^{-2\kappa(T_{k-1} - t)}}{2\kappa}}
$$

The **implied forward rate volatility** (the volatility of $L(T_{k-1}, T_k)$ under the $T_k$-forward measure) can be extracted by matching the Vasicek caplet price to the Black formula:

$$
\sigma_{\text{Black},k} = \frac{\sigma_{P,k}}{\delta_k\,F_k(t)\,\sqrt{T_{k-1} - t}}
$$

where $F_k(t) = (P(t, T_{k-1})/P(t, T_k) - 1)/\delta_k$ is the forward rate. In the Vasicek model, this implied volatility is approximately

$$
\sigma_{\text{Black},k} \approx \frac{B(\delta_k)\,\sigma}{F_k(t)\,\delta_k}\,\sqrt{\frac{1 - e^{-2\kappa(T_{k-1} - t)}}{2\kappa(T_{k-1} - t)}}
$$

!!! warning "Vasicek produces a flat volatility smile"
    Since the Vasicek short rate is Gaussian, forward rates are approximately Gaussian (not log-normal), and the implied Black volatility from the Vasicek formula is approximately strike-independent. The model therefore produces a **flat** implied volatility smile for caplets, which is inconsistent with the observed cap volatility skew. Stochastic volatility or local volatility extensions are needed to capture smile effects.

---

## Swaption pricing via Jamshidian

### Swaption payoff

A **payer swaption** with expiry $T_0$ gives the holder the right to enter a payer swap with fixed rate $K$ on a swap with payment dates $T_1, \ldots, T_n$. The payoff at $T_0$ is

$$
\left(\sum_{k=1}^n \delta_k\,(S_{0,n}(T_0) - K)\,P(T_0, T_k)\right)^+ = \left(\sum_{k=1}^n \delta_k\,P(T_0, T_k)\right)\!(S_{0,n}(T_0) - K)^+
$$

An equivalent representation uses the coupon bond decomposition. The payer swaption payoff is

$$
\left(1 - P(T_0, T_n) - K\sum_{k=1}^n \delta_k\,P(T_0, T_k)\right)^+
$$

which can be rewritten as

$$
\left(1 - \sum_{k=1}^n c_k\,P(T_0, T_k)\right)^+
$$

where $c_k = K\,\delta_k$ for $k = 1, \ldots, n-1$ and $c_n = 1 + K\,\delta_n$. This is a **put** on a coupon bond with cash flows $c_k$ at times $T_k$ and strike $1$.

### Application of Jamshidian's trick

Since the swaption payoff is a put on a coupon bond, Jamshidian's trick decomposes it into a portfolio of ZCB puts.

**Step 1**: Find the critical rate $r^*$ solving

$$
\sum_{k=1}^n c_k\,P(T_0, T_k)\big|_{r_{T_0} = r^*} = 1
$$

**Step 2**: Compute individual strikes $K_k = P(T_0, T_k)\big|_{r_{T_0} = r^*}$.

**Step 3**: The payer swaption price is

$$
\boxed{\text{PSwaption}(t) = \sum_{k=1}^n c_k\,\text{Put}_{\text{ZCB}}(t;\, K_k,\, T_0,\, T_k)}
$$

A **receiver swaption** (the right to receive fixed) is a call on the same coupon bond:

$$
\text{RSwaption}(t) = \sum_{k=1}^n c_k\,\text{Call}_{\text{ZCB}}(t;\, K_k,\, T_0,\, T_k)
$$

### Swaption parity

$$
\text{PSwaption}(t) - \text{RSwaption}(t) = \text{Swap}_{\text{payer}}(t)
$$

---

## Numerical example

**Caplet pricing.** Consider a caplet on the 6-month rate, resetting at $T_0 = 1$ year, paying at $T_1 = 1.5$ years, with strike $\kappa_{\text{cap}} = 5\%$ and $\delta = 0.5$. Vasicek parameters: $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $r_0 = 0.04$.

- Adjusted strike: $K = 1/(1 + 0.5 \times 0.05) = 0.97561$
- Bond prices: $P(0, 1) = 0.9617$, $P(0, 1.5) = 0.9411$
- Bond option volatility: $\sigma_P = B(0.5) \cdot 0.015 \cdot \sqrt{(1 - e^{-0.6})/(0.6)} = 0.4758 \times 0.015 \times 0.8511 = 0.00607$
- Caplet = $1.025 \times \text{Put}(K = 0.97561, T = 1, S = 1.5)$

**Swaption pricing.** A 2-year expiry payer swaption on a 3-year annual swap at strike 5%. Cash flows: $c_1 = 0.05$, $c_2 = 0.05$, $c_3 = 1.05$ at years 3, 4, 5.

- Find $r^*$ solving $0.05\,P(2,3;r^*) + 0.05\,P(2,4;r^*) + 1.05\,P(2,5;r^*) = 1$
- Compute $K_1, K_2, K_3$ at $r^*$
- Sum three ZCB put prices

---

## Summary

In the Vasicek framework, caplets reduce to puts on zero-coupon bonds via the identity $\delta(L - \kappa_{\text{cap}})^+ = (1 + \delta\kappa_{\text{cap}})(K - P)^+$, and swaptions reduce to portfolios of ZCB puts (or calls) via Jamshidian's trick. All pricing is therefore reduced to the single ZCB option formula derived from the log-normality of forward bond prices under the $T$-forward measure. The model produces a flat implied volatility smile, which is its main limitation for calibrating to market cap and swaption volatilities.

---

## Exercises

**Exercise 1.** Derive the caplet-put equivalence step by step. Starting from the caplet payoff $N\delta(L(T_0, T_1) - K_{\text{cap}})^+$, substitute $L = (1/P - 1)/\delta$ and show the result is $N(1 + K_{\text{cap}}\delta)(\tilde{K} - P(T_0, T_1))^+$ with $\tilde{K} = 1/(1 + K_{\text{cap}}\delta)$.

---

**Exercise 2.** Using the numerical example parameters ($\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $r_0 = 0.04$), compute the caplet price for a 6-month caplet with reset $T_0 = 1$, payment $T_1 = 1.5$, and strike 5%. Follow all intermediate steps: adjusted strike, bond prices, bond option volatility, and put price.

---

**Exercise 3.** Explain why the Vasicek model produces a flat implied volatility smile for caplets. What property of the Gaussian distribution causes this? How does this compare with the Black-Karasinski model?

---

**Exercise 4.** For a 2Y-into-3Y payer swaption at strike 5%, write out the cash flow structure ($c_1$, $c_2$, $c_3$) and the Jamshidian decomposition. How many ZCB put options appear? What equation determines $r^*$?

---

**Exercise 5.** Prove cap-floor parity: $\text{Cap}(t) - \text{Floor}(t) = \text{Swap}(t)$. Use the identity $(x-K)^+ - (K-x)^+ = x - K$ applied to each caplet-floorlet pair.

---

**Exercise 6.** The bond option volatility for a caplet is $\sigma_P = B(\delta)\sigma\sqrt{(1 - e^{-2\kappa T_0})/(2\kappa)}$. Analyze how this volatility depends on (i) the accrual period $\delta$, (ii) the reset date $T_0$, and (iii) the mean reversion $\kappa$. For large $T_0$, what does $\sigma_P$ converge to?

---

**Exercise 7.** A receiver swaption with expiry $T_0$ into a swap with payment dates $T_1, \ldots, T_n$ decomposes into a portfolio of ZCB calls via Jamshidian's trick. Write the pricing formula analogous to the payer swaption decomposition. Verify swaption parity: Payer $-$ Receiver $=$ Swap value.
