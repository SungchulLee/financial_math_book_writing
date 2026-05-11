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

---

## Exercises

**Exercise 1.** A LIBOR-in-arrears payment fixes and pays at $T_i = 3$ years. The forward LIBOR rate is $L_i(0) = 4.2\%$, the Black implied volatility is $\sigma_i = 18\%$, and the accrual fraction is $\delta_i = 0.25$ (quarterly). Compute both the approximate and exact convexity corrections and the corresponding adjusted forward rates. What is the percentage error of the approximation?

??? success "Solution to Exercise 1"

    **Given:** $L_i(0) = 0.042$, $\sigma_i = 0.18$, $T_i = 3$, $\delta_i = 0.25$.

    **Approximate convexity correction:**

    $$
    \text{Correction}_{\text{approx}} = \frac{\delta_i \, L_i(0)^2 \, \sigma_i^2 \, T_i}{1 + \delta_i L_i(0)}
    $$

    Substituting:

    $$
    = \frac{0.25 \times 0.042^2 \times 0.18^2 \times 3}{1 + 0.25 \times 0.042} = \frac{0.25 \times 0.001764 \times 0.0324 \times 3}{1.0105}
    $$

    Numerator: $0.25 \times 0.001764 \times 0.0324 \times 3 = 0.25 \times 0.001764 \times 0.0972 = 0.000042866$.

    $$
    \text{Correction}_{\text{approx}} = \frac{0.000042866}{1.0105} = 0.00004242 = 0.4242 \text{ bp}
    $$

    Approximate adjusted forward rate: $L_i(0) + 0.4242 \text{ bp} = 4.2000\% + 0.0424\% = 4.2424\%$.

    **Exact convexity correction:**

    Using the exact formula:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = \frac{L_i(0)\bigl(1 + \delta_i L_i(0) \, e^{\sigma_i^2 T_i}\bigr)}{1 + \delta_i L_i(0)}
    $$

    We compute $e^{\sigma_i^2 T_i} = e^{0.0324 \times 3} = e^{0.0972} = 1.10208$.

    $$
    = \frac{0.042 \times (1 + 0.25 \times 0.042 \times 1.10208)}{1.0105} = \frac{0.042 \times (1 + 0.011571)}{1.0105} = \frac{0.042 \times 1.011571}{1.0105}
    $$

    $$
    = \frac{0.042486}{1.0105} = 0.042044
    $$

    Exact correction: $0.042044 - 0.042000 = 0.000044 = 0.44$ bp.

    Exact adjusted forward rate: $4.2044\%$.

    **Percentage error of approximation:**

    $$
    \text{Error} = \frac{|0.4242 - 0.44|}{0.44} \times 100\% \approx 3.6\%
    $$

    The approximation underestimates the exact correction by about 3.6%, which is small because $\sigma_i^2 T_i = 0.0972$ is modest, so the linear Taylor expansion $e^x \approx 1 + x$ is accurate.

---

**Exercise 2.** Starting from the Radon--Nikodym derivative

$$
\frac{d\mathbb{Q}^{T_i}}{d\mathbb{Q}^{T_{i+1}}}\bigg|_{\mathcal{F}_{T_i}} = \frac{P(0, T_{i+1})}{P(0, T_i)} \cdot (1 + \delta_i L_i(T_i))
$$

derive the exact formula

$$
\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = \frac{L_i(0)\bigl(1 + \delta_i L_i(0)\,e^{\sigma_i^2 T_i}\bigr)}{1 + \delta_i L_i(0)}
$$

by computing $\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^2]$ explicitly under lognormal dynamics. State all assumptions used.

??? success "Solution to Exercise 2"

    **Assumptions:**

    1. Under $\mathbb{Q}^{T_{i+1}}$, the forward LIBOR rate $L_i(t)$ follows lognormal (Black) dynamics: $dL_i/L_i = \sigma_i \, dW^{T_{i+1}}$.
    2. $\sigma_i$ is constant.
    3. The relation $P(T_i, T_{i+1}) = 1/(1 + \delta_i L_i(T_i))$ holds (simple compounding).
    4. $P(0, T_{i+1})/P(0, T_i) = 1/(1 + \delta_i L_i(0))$ (consistent with the forward rate definition).

    **Derivation:**

    Starting from the Radon--Nikodym derivative:

    $$
    \frac{d\mathbb{Q}^{T_i}}{d\mathbb{Q}^{T_{i+1}}}\bigg|_{\mathcal{F}_{T_i}} = \frac{P(0, T_{i+1})}{P(0, T_i)} \cdot (1 + \delta_i L_i(T_i))
    $$

    The change-of-measure formula gives:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[L_i(T_i) \cdot \frac{P(0, T_{i+1})}{P(0, T_i)} \cdot (1 + \delta_i L_i(T_i))\right]
    $$

    Since $P(0, T_{i+1})/P(0, T_i) = 1/(1 + \delta_i L_i(0))$:

    $$
    = \frac{1}{1 + \delta_i L_i(0)} \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[L_i(T_i)(1 + \delta_i L_i(T_i))\right]
    $$

    Expanding:

    $$
    = \frac{1}{1 + \delta_i L_i(0)} \left(\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)] + \delta_i \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^2]\right)
    $$

    **Computing $\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^2]$:**

    Under lognormal dynamics, $L_i(T_i) = L_i(0) \exp\!\left(-\tfrac{1}{2}\sigma_i^2 T_i + \sigma_i W(T_i)\right)$ where $W(T_i) \sim \mathcal{N}(0, T_i)$.

    For a lognormal variable $X = e^{\mu + \sigma Z}$ with $Z \sim \mathcal{N}(0,1)$:

    $$
    \mathbb{E}[X^2] = e^{2\mu + 2\sigma^2}
    $$

    Here $\mu = \ln L_i(0) - \tfrac{1}{2}\sigma_i^2 T_i$ and $\sigma^2 = \sigma_i^2 T_i$, so:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^2] = \exp\!\left(2\ln L_i(0) - \sigma_i^2 T_i + 2\sigma_i^2 T_i\right) = L_i(0)^2 \, e^{\sigma_i^2 T_i}
    $$

    **Combining:** Using the martingale property $\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)] = L_i(0)$:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = \frac{L_i(0) + \delta_i \, L_i(0)^2 \, e^{\sigma_i^2 T_i}}{1 + \delta_i L_i(0)} = \frac{L_i(0)\bigl(1 + \delta_i L_i(0) \, e^{\sigma_i^2 T_i}\bigr)}{1 + \delta_i L_i(0)}
    $$

    This is the exact formula. $\square$

---

**Exercise 3.** Explain why the map $L \mapsto L(1 + \delta L)$ is convex in $L$ for $\delta > 0$, and use Jensen's inequality to give a one-line proof that $\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] > L_i(0)$ without performing any measure-change calculation.

??? success "Solution to Exercise 3"

    Define $f(L) = L(1 + \delta L) = L + \delta L^2$. We compute the second derivative:

    $$
    f'(L) = 1 + 2\delta L, \qquad f''(L) = 2\delta
    $$

    Since $\delta > 0$, we have $f''(L) = 2\delta > 0$ for all $L$, so $f$ is strictly convex.

    **One-line proof via Jensen's inequality:**

    The present value of the arrears payment can be written as $P(0, T_{i+1}) \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[f(L_i(T_i))]/(1+\delta_i L_i(0))$, and since $f$ is convex and $L_i$ is a martingale under $\mathbb{Q}^{T_{i+1}}$, Jensen's inequality gives:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[f(L_i(T_i))] > f\!\left(\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)]\right) = f(L_i(0)) = L_i(0)(1 + \delta_i L_i(0))
    $$

    (strict inequality holds whenever $L_i(T_i)$ is non-degenerate). Since $\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)]$ equals $\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[f(L_i(T_i))]/(1+\delta_i L_i(0))$ (from the measure change), we get:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] > \frac{L_i(0)(1+\delta_i L_i(0))}{1+\delta_i L_i(0)} = L_i(0)
    $$

    No explicit measure-change calculation is needed; the convexity of $f$ and the martingale property suffice. $\square$

---

**Exercise 4.** Consider a swap that pays LIBOR-in-arrears quarterly for 5 years on a notional of \$100 million. The forward LIBOR rates for each quarterly period are approximately $L_i(0) = 5\%$, the implied volatilities are $\sigma_i = 20\%$, and the accrual fractions are $\delta_i = 0.25$. Estimate the total convexity adjustment (summed over all 20 periods) in dollar terms. How does this compare to a single basis point on the fixed leg?

??? success "Solution to Exercise 4"

    **Given:** 20 quarterly periods, $L_i(0) = 0.05$, $\sigma_i = 0.20$, $\delta_i = 0.25$, notional $N = \$100{,}000{,}000$.

    The convexity correction for period $i$ (fixing at $T_i = 0.25 i$) is:

    $$
    C_i = \frac{\delta_i \, L_i(0)^2 \, \sigma_i^2 \, T_i}{1 + \delta_i L_i(0)} = \frac{0.25 \times 0.0025 \times 0.04 \times T_i}{1 + 0.0125} = \frac{0.000025 \, T_i}{1.0125}
    $$

    The total correction summed over all periods:

    $$
    \sum_{i=1}^{20} C_i = \frac{0.000025}{1.0125} \sum_{i=1}^{20} T_i = \frac{0.000025}{1.0125} \sum_{i=1}^{20} 0.25i
    $$

    $$
    \sum_{i=1}^{20} 0.25i = 0.25 \times \frac{20 \times 21}{2} = 0.25 \times 210 = 52.5
    $$

    $$
    \sum_{i=1}^{20} C_i = \frac{0.000025 \times 52.5}{1.0125} = \frac{0.0013125}{1.0125} = 0.001296
    $$

    This is the sum of the rate adjustments (in absolute terms). The dollar value of each period's correction is $N \times \delta_i \times C_i$. The total dollar convexity adjustment (undiscounted) is:

    $$
    \text{Total} = N \times \delta_i \times \sum_{i=1}^{20} C_i = 100{,}000{,}000 \times 0.25 \times 0.001296 = \$32{,}407
    $$

    **Comparison to one basis point on the fixed leg:**

    One basis point on the fixed leg over 5 years (20 quarterly periods) is:

    $$
    \text{1 bp} = N \times 0.0001 \times \sum_{i=1}^{20} \delta_i \times P(0, T_{i+1}) \approx N \times 0.0001 \times 20 \times 0.25 \times \bar{P}
    $$

    Assuming an average discount factor $\bar{P} \approx 0.95$:

    $$
    \text{1 bp} \approx 100{,}000{,}000 \times 0.0001 \times 5 \times 0.95 = \$47{,}500
    $$

    The total convexity adjustment of approximately \$32,400 is about **0.68 basis points** on the fixed leg. This is material for a \$100 million swap and would need to be incorporated in pricing.

---

**Exercise 5.** An arrears caplet pays $\delta_i \max(L_i(T_i) - K, 0)$ at time $T_i$ with $K = 5\%$, $L_i(0) = 5\%$, $\sigma_i = 22\%$, $T_i = 2$, and $\delta_i = 0.5$. The standard (non-arrears) caplet with the same parameters pays at $T_{i+1}$. Explain qualitatively why the arrears caplet is more expensive than the standard caplet. Write down the pricing formula for the arrears caplet in terms of an expectation under $\mathbb{Q}^{T_{i+1}}$ and identify the additional term compared to the standard Black caplet formula.

??? success "Solution to Exercise 5"

    **Qualitative explanation of why the arrears caplet is more expensive:**

    The standard caplet pays $\delta_i \max(L_i(T_i) - K, 0)$ at $T_{i+1}$, while the arrears caplet pays the same amount at $T_i$ (earlier). Receiving a positive cashflow earlier is always more valuable due to time-value of money, but the effect here is subtler: the cashflow is large precisely when rates are high (i.e., when $L_i(T_i) > K$), and high rates mean that discounting from $T_{i+1}$ back to $T_i$ provides a larger benefit. This positive correlation between the payoff magnitude and the discount-factor advantage creates an additional convexity premium.

    **Pricing formula under $\mathbb{Q}^{T_{i+1}}$:**

    $$
    \text{Arrears Caplet} = P(0, T_i) \, \mathbb{E}^{\mathbb{Q}^{T_i}}\!\left[\delta_i (L_i(T_i) - K)^+\right]
    $$

    Using the change of measure:

    $$
    = P(0, T_{i+1}) \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[\delta_i (L_i(T_i) - K)^+ \cdot (1 + \delta_i L_i(T_i))\right]
    $$

    Expanding the product:

    $$
    = P(0, T_{i+1}) \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[\delta_i (L_i - K)^+\right] + P(0, T_{i+1}) \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[\delta_i^2 \, L_i \, (L_i - K)^+\right]
    $$

    The first term is exactly the standard Black caplet price. The second term, $P(0, T_{i+1}) \, \delta_i^2 \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)(L_i(T_i) - K)^+]$, is the **additional term** that makes the arrears caplet more expensive. This term involves $\mathbb{E}[L \cdot (L-K)^+]$, which under lognormal dynamics can be computed in terms of the second moment of $L$ conditional on $L > K$. It is always positive, confirming that the arrears caplet price exceeds the standard caplet price.

---

**Exercise 6.** Suppose interest rates are modeled under a normal (Bachelier) framework instead of the lognormal (Black) framework, so that $L_i(T_i) \sim \mathcal{N}(L_i(0), \sigma_N^2 T_i)$ under $\mathbb{Q}^{T_{i+1}}$. Rederive the LIBOR-in-arrears convexity correction under normal dynamics and show that it takes the form

$$
\text{Correction}_{\text{normal}} = \frac{\delta_i \, \sigma_N^2 \, T_i}{1 + \delta_i L_i(0)}
$$

Compare this to the lognormal correction and discuss when the two formulas give materially different results.

??? success "Solution to Exercise 6"

    **Setup:** Under normal dynamics, $L_i(T_i) = L_i(0) + \sigma_N \sqrt{T_i} \, Z$ where $Z \sim \mathcal{N}(0,1)$ under $\mathbb{Q}^{T_{i+1}}$.

    Under $\mathbb{Q}^{T_{i+1}}$, $L_i$ is a martingale: $\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)] = L_i(0)$.

    **Compute the second moment:**

    $$
    \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^2] = \text{Var}(L_i(T_i)) + \left(\mathbb{E}[L_i(T_i)]\right)^2 = \sigma_N^2 T_i + L_i(0)^2
    $$

    **Apply the same measure change formula:**

    $$
    \mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = \frac{\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)(1 + \delta_i L_i(T_i))]}{1 + \delta_i L_i(0)}
    $$

    Expanding:

    $$
    = \frac{L_i(0) + \delta_i(\sigma_N^2 T_i + L_i(0)^2)}{1 + \delta_i L_i(0)} = \frac{L_i(0)(1 + \delta_i L_i(0)) + \delta_i \sigma_N^2 T_i}{1 + \delta_i L_i(0)}
    $$

    $$
    = L_i(0) + \frac{\delta_i \, \sigma_N^2 \, T_i}{1 + \delta_i L_i(0)}
    $$

    Therefore:

    $$
    \text{Correction}_{\text{normal}} = \frac{\delta_i \, \sigma_N^2 \, T_i}{1 + \delta_i L_i(0)}
    $$

    **Comparison with the lognormal correction:**

    The lognormal correction is $\delta_i L_i(0)^2 \sigma_i^2 T_i / (1 + \delta_i L_i(0))$, while the normal correction is $\delta_i \sigma_N^2 T_i / (1 + \delta_i L_i(0))$.

    The two agree when $\sigma_N = L_i(0) \sigma_i$ (i.e., when the normal volatility equals the lognormal volatility times the rate level), which is the standard at-the-money volatility equivalence.

    The formulas give materially different results when rates move far from their initial level. If rates double from $L_i(0)$ to $2L_i(0)$, the lognormal correction would scale as $(2L_i(0))^2 \sigma_i^2 = 4 L_i(0)^2 \sigma_i^2$ (quadratic in the rate level), while the normal correction remains $\sigma_N^2$ (independent of the rate level). In a low-rate environment (e.g., $L_i(0) = 0.5\%$), the lognormal correction is tiny ($\propto L_i(0)^2$) while the normal correction can still be significant if $\sigma_N$ is non-negligible. Conversely, in a high-rate environment, the lognormal correction dominates.

---

**Exercise 7.** A structured note pays $\delta_i \, L_i(T_i)^2$ at time $T_i$ (a "LIBOR-squared" in-arrears payment). Using the change of measure from $\mathbb{Q}^{T_{i+1}}$ to $\mathbb{Q}^{T_i}$, derive the convexity-adjusted expectation $\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)^2]$ under lognormal dynamics. You will need the third moment of a lognormal random variable. Express your result in terms of $L_i(0)$, $\sigma_i$, $T_i$, and $\delta_i$.

??? success "Solution to Exercise 7"

    **LIBOR-squared in arrears:** We need $\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)^2]$.

    Using the change of measure:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)^2] = \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[L_i(T_i)^2 \cdot \frac{P(0, T_{i+1})}{P(0, T_i)} \cdot (1 + \delta_i L_i(T_i))\right]
    $$

    $$
    = \frac{1}{1 + \delta_i L_i(0)} \left(\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^2] + \delta_i \, \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^3]\right)
    $$

    **Second moment (computed in Exercise 2):**

    $$
    \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^2] = L_i(0)^2 \, e^{\sigma_i^2 T_i}
    $$

    **Third moment of a lognormal variable:**

    If $L_i(T_i) = L_i(0) \exp(-\frac{1}{2}\sigma_i^2 T_i + \sigma_i W(T_i))$, then for any integer $k$:

    $$
    \mathbb{E}[L_i(T_i)^k] = L_i(0)^k \exp\!\left(\frac{k(k-1)}{2}\sigma_i^2 T_i\right)
    $$

    For $k = 3$:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)^3] = L_i(0)^3 \, e^{3\sigma_i^2 T_i}
    $$

    **Combining:**

    $$
    \mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)^2] = \frac{L_i(0)^2 \, e^{\sigma_i^2 T_i} + \delta_i \, L_i(0)^3 \, e^{3\sigma_i^2 T_i}}{1 + \delta_i L_i(0)}
    $$

    Factoring:

    $$
    = \frac{L_i(0)^2 \, e^{\sigma_i^2 T_i}\!\left(1 + \delta_i \, L_i(0) \, e^{2\sigma_i^2 T_i}\right)}{1 + \delta_i L_i(0)}
    $$

    The convexity correction for the LIBOR-squared payment is the difference between this expression and the "natural" second moment:

    $$
    \text{Correction} = \mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)^2] - L_i(0)^2 \, e^{\sigma_i^2 T_i}
    $$

    $$
    = L_i(0)^2 \, e^{\sigma_i^2 T_i} \left(\frac{1 + \delta_i L_i(0) \, e^{2\sigma_i^2 T_i}}{1 + \delta_i L_i(0)} - 1\right) = \frac{\delta_i \, L_i(0)^3 \, e^{\sigma_i^2 T_i}(e^{2\sigma_i^2 T_i} - 1)}{1 + \delta_i L_i(0)}
    $$

    Note that this correction involves the third moment through the $e^{3\sigma_i^2 T_i}$ term, and it scales as $L_i(0)^3$ (compared to $L_i(0)^2$ for the standard LIBOR-in-arrears correction), making it more sensitive to the rate level.
