# Caplet and Swaption Formulas

Caps, floors, and swaptions are the primary volatility instruments in interest rate markets. A **cap** is a strip of caplets, each protecting against a floating rate exceeding a strike, while a **swaption** is an option to enter an interest rate swap. In the Vasicek model, both reduce to portfolios of zero-coupon bond options, which have closed-form solutions. This section derives the caplet formula by showing it is equivalent to a put on a ZCB, extends the result to caps and floors, and applies Jamshidian's trick to obtain swaption prices.

---

## Caplet as a bond option

Recall (see [§ IR products](../interest_rate_products/bond_pricing.md)) for the caplet definition and payoff $\delta_k(L(T_{k-1},T_k) - \kappa_{\text{cap}})^+$ at $T_k$.

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

where $\text{Put}_{\text{ZCB}}(t; K, T, S) = K\,P(t,T)\,\mathcal{N}(-d_2) - P(t,S)\,\mathcal{N}(-d_1)$ is the Vasicek ZCB put formula.

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

Recall (see [§ Swaption pricing](../swaption_pricing/annuity_measure_and_change_of_numeraire.md)) for the payer swaption payoff structure. The payoff at $T_0$ admits the coupon-bond representation

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

??? success "Solution to Exercise 1"
    Start with the caplet payoff at $T_1$ (setting notional $N = 1$ for simplicity):

    $$
    \delta\,(L(T_0, T_1) - K_{\text{cap}})^+
    $$

    Substitute the definition of the simply compounded rate $L(T_0, T_1) = \frac{1}{\delta}\left(\frac{1}{P(T_0, T_1)} - 1\right)$:

    $$
    \delta\left(\frac{1}{\delta}\left(\frac{1}{P(T_0, T_1)} - 1\right) - K_{\text{cap}}\right)^+ = \left(\frac{1}{P(T_0, T_1)} - 1 - \delta K_{\text{cap}}\right)^+
    $$

    Factor out $1/P(T_0, T_1)$ inside the max:

    $$
    = \left(\frac{1 - P(T_0, T_1)(1 + \delta K_{\text{cap}})}{P(T_0, T_1)}\right)^+
    $$

    Since $P(T_0, T_1) > 0$, we can write this as:

    $$
    = \frac{1}{P(T_0, T_1)} \left(1 - P(T_0, T_1)(1 + \delta K_{\text{cap}})\right)^+
    $$

    However, it is more useful to multiply and divide by $(1 + \delta K_{\text{cap}})$:

    $$
    = (1 + \delta K_{\text{cap}}) \cdot \frac{1}{P(T_0, T_1)} \left(\frac{1}{1 + \delta K_{\text{cap}}} - P(T_0, T_1)\right)^+ \cdot P(T_0, T_1)
    $$

    Wait---let us redo this more carefully. From the expression $\frac{1}{P} - 1 - \delta K_{\text{cap}}$, multiply through by $P > 0$:

    $$
    \left(\frac{1}{P} - 1 - \delta K_{\text{cap}}\right)^+ = \frac{(1 - (1 + \delta K_{\text{cap}})P)^+}{P}
    $$

    Now factor out $(1 + \delta K_{\text{cap}})$ from the numerator:

    $$
    = \frac{(1 + \delta K_{\text{cap}})}{P}\left(\frac{1}{1 + \delta K_{\text{cap}}} - P\right)^+
    $$

    Define $\tilde{K} = \frac{1}{1 + \delta K_{\text{cap}}}$. The payoff at $T_1$ is:

    $$
    \frac{(1 + \delta K_{\text{cap}})}{P(T_0, T_1)}\left(\tilde{K} - P(T_0, T_1)\right)^+
    $$

    Discounting from $T_1$ to $T_0$ by multiplying by $P(T_0, T_1)$, the value at $T_0$ of the $T_1$-payoff is:

    $$
    (1 + \delta K_{\text{cap}})\left(\tilde{K} - P(T_0, T_1)\right)^+
    $$

    This is $(1 + \delta K_{\text{cap}})$ units of a European put on $P(T_0, T_1)$ with strike $\tilde{K}$ and expiry $T_0$, as claimed.

---

**Exercise 2.** Using the numerical example parameters ($\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $r_0 = 0.04$), compute the caplet price for a 6-month caplet with reset $T_0 = 1$, payment $T_1 = 1.5$, and strike 5%. Follow all intermediate steps: adjusted strike, bond prices, bond option volatility, and put price.

??? success "Solution to Exercise 2"
    **Parameters:** $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.015$, $r_0 = 0.04$, $T_0 = 1$, $T_1 = 1.5$, $\delta = 0.5$, $K_{\text{cap}} = 0.05$.

    **Adjusted strike:**

    $$
    K = \frac{1}{1 + 0.5 \times 0.05} = \frac{1}{1.025} = 0.97561
    $$

    **Bond prices.** For $P(0,1)$ with $\tau = 1$:

    $$
    B(1) = \frac{1 - e^{-0.3}}{0.3} = \frac{0.2592}{0.3} = 0.8640
    $$

    $$
    \ln A(1) = (0.05 - 0.00125)(0.8640 - 1) - \frac{0.000225}{1.2} \times 0.8640^2 = 0.04875 \times (-0.136) - 0.0001875 \times 0.7465
    $$

    $$
    = -0.006630 - 0.000140 = -0.006770
    $$

    $$
    P(0,1) = e^{-0.006770 - 0.8640 \times 0.04} = e^{-0.006770 - 0.03456} = e^{-0.04133} = 0.9595
    $$

    For $P(0,1.5)$ with $\tau = 1.5$:

    $$
    B(1.5) = \frac{1 - e^{-0.45}}{0.3} = \frac{1 - 0.6376}{0.3} = 1.2080
    $$

    $$
    \ln A(1.5) = 0.04875 \times (1.2080 - 1.5) - 0.0001875 \times 1.4593 = 0.04875 \times (-0.2920) - 0.000274
    $$

    $$
    = -0.01424 - 0.000274 = -0.01451
    $$

    $$
    P(0,1.5) = e^{-0.01451 - 1.2080 \times 0.04} = e^{-0.01451 - 0.04832} = e^{-0.06283} = 0.9391
    $$

    **Bond option volatility.** With $\delta = T_1 - T_0 = 0.5$:

    $$
    B(0.5) = \frac{1 - e^{-0.15}}{0.3} = \frac{1 - 0.8607}{0.3} = 0.4643
    $$

    $$
    v = 0.015 \times \sqrt{\frac{1 - e^{-0.6}}{0.6}} = 0.015 \times \sqrt{\frac{0.4512}{0.6}} = 0.015 \times \sqrt{0.7520} = 0.015 \times 0.8672 = 0.01301
    $$

    $$
    \sigma_P = B(0.5) \times v = 0.4643 \times 0.01301 = 0.006042
    $$

    **Put price.** $\text{Put}(K, T_0, T_1) = K\,P(0,T_0)\,\mathcal{N}(-d_2) - P(0,T_1)\,\mathcal{N}(-d_1)$ where:

    $$
    d_1 = \frac{\ln\!\left(\frac{P(0,1.5)}{K \cdot P(0,1)}\right)}{\sigma_P} + \frac{\sigma_P}{2} = \frac{\ln\!\left(\frac{0.9391}{0.97561 \times 0.9595}\right)}{0.006042} + 0.003021
    $$

    $$
    = \frac{\ln(1.00296)}{0.006042} + 0.003021 = \frac{0.002956}{0.006042} + 0.003021 = 0.4892 + 0.003021 = 0.4922
    $$

    $$
    d_2 = 0.4922 - 0.006042 = 0.4862
    $$

    $$
    \text{Put} = 0.97561 \times 0.9595 \times \Phi(-0.4862) - 0.9391 \times \Phi(-0.4922)
    $$

    $$
    = 0.93616 \times 0.3134 - 0.9391 \times 0.3113 = 0.29340 - 0.29234 = 0.00106
    $$

    **Caplet price:**

    $$
    \text{Caplet} = 1.025 \times 0.00106 = 0.001087
    $$

    The caplet price is approximately 10.9 basis points of notional.

---

**Exercise 3.** Explain why the Vasicek model produces a flat implied volatility smile for caplets. What property of the Gaussian distribution causes this? How does this compare with the Black-Karasinski model?

??? success "Solution to Exercise 3"
    The Vasicek model produces a **flat implied volatility smile** for caplets because the underlying forward rate $L(T_0, T_1)$ is approximately **Gaussian** (not log-normal) under the forward measure.

    In the Vasicek model, $r_T$ is normally distributed under $\mathbb{Q}^T$. The forward LIBOR rate $L = (1/P(T_0,T_1) - 1)/\delta$ is a function of $r_{T_0}$, and since $P(T_0,T_1) = A(\delta)\,e^{-B(\delta)\,r_{T_0}}$ with $r_{T_0}$ Gaussian, the rate $L$ is approximately linear in $r_{T_0}$ for small $\delta$, hence approximately Gaussian. When a Gaussian variable is priced using the Black (log-normal) formula, the resulting implied volatility is approximately constant across strikes---the smile is flat.

    More precisely, the Black formula assumes log-normality of the forward rate, which generates a symmetric smile in log-moneyness. Since the Vasicek forward rate is (approximately) normal rather than log-normal, its distribution is symmetric in the rate itself, producing no skew or smile when mapped through the Black formula.

    The **Black-Karasinski model** $d\ln r_t = \kappa(\ln\theta - \ln r_t)\,dt + \sigma\,dW_t$ models the log of the short rate as an OU process, making $r_t$ log-normally distributed. This generates a non-trivial implied volatility smile because the forward rate distribution under the forward measure is no longer Gaussian. The log-normal specification introduces positive skewness (rates cannot be negative and have a fat right tail), which translates into an upward-sloping volatility skew for out-of-the-money caplets.

---

**Exercise 4.** For a 2Y-into-3Y payer swaption at strike 5%, write out the cash flow structure ($c_1$, $c_2$, $c_3$) and the Jamshidian decomposition. How many ZCB put options appear? What equation determines $r^*$?

??? success "Solution to Exercise 4"
    **Cash flow structure.** A 2Y-into-3Y payer swaption gives the right at $T_0 = 2$ to enter a 3-year annual payer swap at strike $K = 5\%$. The swap has payment dates $T_1 = 3$, $T_2 = 4$, $T_3 = 5$ with $\delta_k = 1$ for all $k$.

    The swaption payoff at $T_0 = 2$ can be written as a put on a coupon bond:

    $$
    \left(1 - \sum_{k=1}^3 c_k\,P(2, T_k)\right)^+
    $$

    where the cash flows are:

    - $c_1 = K\delta_1 = 0.05$ at $T_1 = 3$
    - $c_2 = K\delta_2 = 0.05$ at $T_2 = 4$
    - $c_3 = 1 + K\delta_3 = 1.05$ at $T_3 = 5$

    **Jamshidian decomposition.** Three ZCB put options appear, one for each payment date.

    **Step 1:** Find $r^*$ solving:

    $$
    0.05\,P(2,3;r^*) + 0.05\,P(2,4;r^*) + 1.05\,P(2,5;r^*) = 1
    $$

    This is a one-dimensional root-finding problem (e.g., bisection or Brent's method).

    **Step 2:** Compute strikes $K_k = P(2, T_k;r^*)$ for $k = 1, 2, 3$.

    **Step 3:** The payer swaption price is:

    $$
    \text{PSwaption}(t) = 0.05\,\text{Put}_{\text{ZCB}}(t; K_1, 2, 3) + 0.05\,\text{Put}_{\text{ZCB}}(t; K_2, 2, 4) + 1.05\,\text{Put}_{\text{ZCB}}(t; K_3, 2, 5)
    $$

    where each put is priced using the Vasicek ZCB put formula with bond option volatility $\sigma_{P,k} = B(T_k - 2)\,\sigma\sqrt{(1 - e^{-2\kappa \cdot 2})/(2\kappa)}$.

---

**Exercise 5.** Prove cap-floor parity: $\text{Cap}(t) - \text{Floor}(t) = \text{Swap}(t)$. Use the identity $(x-K)^+ - (K-x)^+ = x - K$ applied to each caplet-floorlet pair.

??? success "Solution to Exercise 5"
    For each caplet-floorlet pair at payment date $T_k$, the caplet pays $\delta(L_k - K)^+$ and the floorlet pays $\delta(K - L_k)^+$ where $L_k = L(T_{k-1}, T_k)$. Using the identity for any real number $x$:

    $$
    (x - K)^+ - (K - x)^+ = x - K
    $$

    Applied with $x = L_k$:

    $$
    \delta(L_k - K)^+ - \delta(K - L_k)^+ = \delta(L_k - K)
    $$

    The left side is $\text{Caplet}_k - \text{Floorlet}_k$. The right side $\delta(L_k - K)$ is the net payment at $T_k$ of a payer swap (receiving floating $L_k$, paying fixed $K$).

    Summing over all $k = 1, \ldots, n$:

    $$
    \sum_{k=1}^n (\text{Caplet}_k - \text{Floorlet}_k) = \sum_{k=1}^n \delta_k(L_k - K)
    $$

    Taking present values:

    $$
    \text{Cap}(t) - \text{Floor}(t) = \sum_{k=1}^n \mathbb{E}^{\mathbb{Q}}_t\!\left[e^{-\int_t^{T_k} r_s\,ds}\,\delta_k(L(T_{k-1},T_k) - K)\right] = \text{Swap}_{\text{payer}}(t)
    $$

    This is **cap-floor parity**. It holds model-independently (it is a consequence of the algebraic identity $(x-K)^+ - (K-x)^+ = x - K$) and serves as a consistency check for any implementation of cap and floor pricing.

---

**Exercise 6.** The bond option volatility for a caplet is $\sigma_P = B(\delta)\sigma\sqrt{(1 - e^{-2\kappa T_0})/(2\kappa)}$. Analyze how this volatility depends on (i) the accrual period $\delta$, (ii) the reset date $T_0$, and (iii) the mean reversion $\kappa$. For large $T_0$, what does $\sigma_P$ converge to?

??? success "Solution to Exercise 6"
    The bond option volatility for the $k$-th caplet is:

    $$
    \sigma_P = B(\delta)\,\sigma\,\sqrt{\frac{1 - e^{-2\kappa T_0}}{2\kappa}}
    $$

    **(i) Dependence on accrual period $\delta$.** Since $B(\delta) = (1 - e^{-\kappa\delta})/\kappa \approx \delta - \frac{1}{2}\kappa\delta^2$ for small $\delta$, we have $\sigma_P \approx \delta\,\sigma\sqrt{(1-e^{-2\kappa T_0})/(2\kappa)}$. The bond option volatility is approximately proportional to $\delta$: longer accrual periods produce larger bond option volatilities because the underlying ZCB has more rate sensitivity.

    **(ii) Dependence on reset date $T_0$.** The factor $\sqrt{(1 - e^{-2\kappa T_0})/(2\kappa)}$ is an increasing function of $T_0$ that saturates at $1/\sqrt{2\kappa}$ as $T_0 \to \infty$. For short reset dates, $\sigma_P$ grows approximately as $\sigma_P \propto \sqrt{T_0}$, reflecting the accumulation of rate uncertainty. For large $T_0$, the variance of $r_{T_0}$ under the forward measure approaches its stationary value, and $\sigma_P$ flattens.

    **(iii) Dependence on mean reversion $\kappa$.** Both $B(\delta)$ and $\sqrt{(1-e^{-2\kappa T_0})/(2\kappa)}$ are decreasing in $\kappa$. Stronger mean reversion reduces rate uncertainty and bond sensitivity, thereby reducing $\sigma_P$.

    **Limit for large $T_0$:**

    $$
    \lim_{T_0 \to \infty} \sigma_P = B(\delta)\,\sigma\,\frac{1}{\sqrt{2\kappa}} = \frac{(1 - e^{-\kappa\delta})\,\sigma}{\kappa\sqrt{2\kappa}}
    $$

    This finite limit reflects the bounded stationary variance of the OU process.

---

**Exercise 7.** A receiver swaption with expiry $T_0$ into a swap with payment dates $T_1, \ldots, T_n$ decomposes into a portfolio of ZCB calls via Jamshidian's trick. Write the pricing formula analogous to the payer swaption decomposition. Verify swaption parity: Payer $-$ Receiver $=$ Swap value.

??? success "Solution to Exercise 7"
    The **receiver swaption** gives the right to receive fixed rate $K$ and pay floating. Its payoff at $T_0$ is:

    $$
    \left(\sum_{k=1}^n c_k\,P(T_0, T_k) - 1\right)^+
    $$

    where $c_k = K\delta_k$ for $k < n$ and $c_n = 1 + K\delta_n$. This is a **call** on the coupon bond with strike 1.

    By Jamshidian's trick, using the same critical rate $r^*$ (solving $\sum c_k P(T_0, T_k; r^*) = 1$) and individual strikes $K_k = P(T_0, T_k; r^*)$:

    $$
    \text{RSwaption}(t) = \sum_{k=1}^n c_k\,\text{Call}_{\text{ZCB}}(t;\, K_k,\, T_0,\, T_k)
    $$

    where $\text{Call}_{\text{ZCB}}(t; K_k, T_0, T_k) = P(t, T_k)\,\Phi(d_1^{(k)}) - K_k\,P(t, T_0)\,\Phi(d_2^{(k)})$.

    **Swaption parity verification.** We need $\text{PSwaption} - \text{RSwaption} = \text{Swap}_{\text{payer}}$.

    $$
    \text{PSwaption} - \text{RSwaption} = \sum_{k=1}^n c_k\left[\text{Put}_{\text{ZCB}}(t; K_k, T_0, T_k) - \text{Call}_{\text{ZCB}}(t; K_k, T_0, T_k)\right]
    $$

    By put-call parity for ZCB options: $\text{Put} - \text{Call} = K_k\,P(t, T_0) - P(t, T_k)$. Therefore:

    $$
    = \sum_{k=1}^n c_k\left[K_k\,P(t, T_0) - P(t, T_k)\right] = P(t, T_0)\sum_{k=1}^n c_k K_k - \sum_{k=1}^n c_k\,P(t, T_k)
    $$

    Since $\sum c_k K_k = 1$ (by definition of $r^*$), this equals:

    $$
    = P(t, T_0) - \sum_{k=1}^n c_k\,P(t, T_k) = \text{Swap}_{\text{payer}}(t)
    $$

    confirming swaption parity.
