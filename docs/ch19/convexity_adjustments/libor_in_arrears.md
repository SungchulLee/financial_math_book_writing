# LIBOR in Arrears

In a standard LIBOR-based derivative, the rate $L(T_i)$ is fixed at $T_i$ and paid at the end of the accrual period $T_{i+1}$. In a **LIBOR-in-arrears** structure, the rate is fixed and paid on the **same date** $T_i$. Because the natural measure for $L_i$ is $\mathbb{Q}^{T_{i+1}}$, evaluating the expectation of $L_i(T_i)$ under $\mathbb{Q}^{T_i}$ (the measure appropriate for payment at $T_i$) introduces a **convexity correction**. This section derives the correction formula, explains its financial intuition, and provides a worked numerical example.

---

## Standard vs. Arrears Payment

### Standard (Natural) Payment

A standard floating payment based on LIBOR:

- **Fixing date:** $T_i$ (observe $L_i(T_i)$)
- **Payment date:** $T_{i+1} = T_i + \delta_i$
- **Cashflow:** $\delta_i \, L_i(T_i)$ paid at $T_{i+1}$

Under the $T_{i+1}$-forward measure, $L_i(t)$ is a martingale, so

$$
\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)] = L_i(0)
$$

No adjustment is needed for standard payment.

### Arrears Payment

A LIBOR-in-arrears payment:

- **Fixing date:** $T_i$ (observe $L_i(T_i)$)
- **Payment date:** $T_i$ (same date!)
- **Cashflow:** $\delta_i \, L_i(T_i)$ paid at $T_i$

Pricing requires evaluating $\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)]$. Since $L_i$ is a martingale under $\mathbb{Q}^{T_{i+1}}$ but **not** under $\mathbb{Q}^{T_i}$, this expectation is not equal to $L_i(0)$.

---

## Derivation of the Convexity Correction

### Step 1: Pricing Under the Natural Measure

The present value of the arrears payment is

$$
V_0 = P(0, T_i) \, \mathbb{E}^{\mathbb{Q}^{T_i}}\!\left[\delta_i \, L_i(T_i)\right]
$$

We need to compute $\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)]$.

### Step 2: Change of Measure

Using the Radon--Nikodym derivative from $\mathbb{Q}^{T_{i+1}}$ to $\mathbb{Q}^{T_i}$:

$$
\frac{d\mathbb{Q}^{T_i}}{d\mathbb{Q}^{T_{i+1}}}\bigg|_{\mathcal{F}_{T_i}} = \frac{P(T_i, T_i) / P(0, T_i)}{P(T_i, T_{i+1}) / P(0, T_{i+1})} = \frac{1 / P(0, T_i)}{P(T_i, T_{i+1}) / P(0, T_{i+1})}
$$

Since $P(T_i, T_{i+1}) = 1/(1 + \delta_i L_i(T_i))$:

$$
\frac{d\mathbb{Q}^{T_i}}{d\mathbb{Q}^{T_{i+1}}}\bigg|_{\mathcal{F}_{T_i}} = \frac{P(0, T_{i+1})}{P(0, T_i)} \cdot (1 + \delta_i L_i(T_i))
$$

### Step 3: Compute the Adjusted Expectation

$$
\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[L_i(T_i) \cdot \frac{P(0, T_{i+1})}{P(0, T_i)} \cdot (1 + \delta_i L_i(T_i))\right]
$$

Since $P(0, T_{i+1}) / P(0, T_i) = 1/(1 + \delta_i L_i(0))$ (to first order), this simplifies to

$$
\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = \frac{\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[L_i(T_i)(1 + \delta_i L_i(T_i))\right]}{1 + \delta_i L_i(0)}
$$

### Step 4: Expand the Numerator

$$
\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[L_i(T_i)(1 + \delta_i L_i(T_i))\right] = \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)] + \delta_i \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^2]
$$

Using the martingale property, $\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)] = L_i(0)$.

For the second moment under lognormal dynamics:

$$
\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^2] = L_i(0)^2 \, e^{\sigma_i^2 T_i}
$$

where $\sigma_i$ is the Black implied volatility.

### Step 5: The Convexity Correction Formula

Combining:

$$
\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = \frac{L_i(0) + \delta_i \, L_i(0)^2 \, e^{\sigma_i^2 T_i}}{1 + \delta_i L_i(0)}
$$

For moderate $\sigma_i^2 T_i$, using $e^{\sigma_i^2 T_i} \approx 1 + \sigma_i^2 T_i$:

$$
\boxed{\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] \approx L_i(0) + \frac{\delta_i \, L_i(0)^2 \, \sigma_i^2 \, T_i}{1 + \delta_i L_i(0)}}
$$

The **convexity correction** is

$$
\text{Correction} = \frac{\delta_i \, L_i(0)^2 \, \sigma_i^2 \, T_i}{1 + \delta_i L_i(0)}
$$

---

## Financial Intuition

### Why the Correction Is Positive

The correction is always positive: the arrears expectation exceeds the forward rate. The intuition is:

- When $L_i(T_i)$ is high, the bond $P(T_i, T_{i+1}) = 1/(1 + \delta_i L_i(T_i))$ is low (discount factor is low), so the present value of the arrears payment is higher than the standard payment
- When $L_i(T_i)$ is low, $P(T_i, T_{i+1})$ is high, but the rate itself is low
- The **asymmetry** (rates appear both in the payment and in the discounting) creates a positive bias

This is a manifestation of Jensen's inequality: the function $L \mapsto L(1 + \delta L)$ is convex in $L$.

### Size of the Correction

The correction scales as:

- $L_i(0)^2$ --- larger for higher rate levels
- $\sigma_i^2$ --- larger for higher volatility
- $T_i$ --- larger for longer fixing periods
- $\delta_i$ --- larger for longer accrual periods

---

## Worked Example

??? example "LIBOR-in-Arrears Convexity Correction"

    **Parameters:**

    - Forward rate: $L_i(0) = 5.0\% = 0.05$
    - Volatility: $\sigma_i = 20\%$
    - Fixing time: $T_i = 5.0$ years
    - Accrual fraction: $\delta_i = 0.5$ (semiannual)
    - Discount factor: $P(0, T_i) = 0.78$

    **Step 1: Convexity correction**

    $$
    \text{Correction} = \frac{0.5 \times 0.05^2 \times 0.04 \times 5.0}{1 + 0.5 \times 0.05} = \frac{0.5 \times 0.0025 \times 0.2}{1.025} = \frac{0.000250}{1.025} = 0.000244 = 2.44 \text{ bp}
    $$

    **Step 2: Adjusted expectation**

    $$
    \mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = 5.00\% + 2.44 \text{ bp} = 5.024\%
    $$

    **Step 3: Present value of arrears payment**

    $$
    V_0 = 0.78 \times 0.5 \times 0.05024 = 0.01959
    $$

    **Comparison:** Without the correction, $V_0 = 0.78 \times 0.5 \times 0.05 = 0.01950$. The convexity adjustment adds \$0.93 per \$10,000 notional per period.

---

## Exact Formula (Without Approximation)

The exact result (no Taylor expansion) is

$$
\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = \frac{L_i(0)(1 + \delta_i L_i(0) \, e^{\sigma_i^2 T_i})}{1 + \delta_i L_i(0)}
$$

For the parameters in the example above:

$$
= \frac{0.05 \times (1 + 0.5 \times 0.05 \times e^{0.04 \times 5})}{1.025} = \frac{0.05 \times (1 + 0.025 \times 1.2214)}{1.025} = \frac{0.05 \times 1.03054}{1.025} = 0.05027
$$

The exact value (5.027%) is close to the approximation (5.024%), confirming the accuracy of the first-order expansion.

---

## Arrears Caplet

### Payoff

An **arrears caplet** pays $\delta_i \max(L_i(T_i) - K, 0)$ at time $T_i$ (instead of $T_{i+1}$).

### Pricing

$$
\text{Arrears Caplet} = P(0, T_i) \, \mathbb{E}^{\mathbb{Q}^{T_i}}\!\left[\delta_i \max(L_i(T_i) - K, 0)\right]
$$

Under the change of measure, this can be expressed as

$$
\text{Arrears Caplet} = P(0, T_{i+1}) \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[\delta_i \max(L_i(T_i) - K, 0) \cdot (1 + \delta_i L_i(T_i))\right]
$$

Expanding the product and using properties of the lognormal distribution, the arrears caplet can be decomposed into a standard caplet plus a correction involving the second moment of $L_i$.

---

## Key Takeaways

- **LIBOR-in-arrears** pays the rate on the same date it is fixed, rather than at the end of the accrual period
- The convexity correction is $\delta_i L_i(0)^2 \sigma_i^2 T_i / (1 + \delta_i L_i(0))$, always **positive**
- The correction arises from the measure change between the $T_{i+1}$-forward and $T_i$-forward measures
- Financial intuition: convexity of the payoff in the rate creates a Jensen's inequality effect
- The correction is most significant for long-dated, high-volatility, high-rate environments
- The exact formula uses $e^{\sigma_i^2 T_i}$ rather than the linear approximation $1 + \sigma_i^2 T_i$

---

## Further Reading

- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 13 (In-Arrears Products)
- Hull (2018), *Options, Futures, and Other Derivatives*, Chapter 29
- Pelsser (2000), *Efficient Methods for Valuing Interest Rate Derivatives*, Chapter 5
