# CMS Convexity Adjustment

A **Constant Maturity Swap (CMS)** rate is the par swap rate for a fixed tenor (e.g., the 10-year swap rate), observed at some future date and paid at a different date. The CMS rate is a martingale under the **annuity measure** associated with the underlying swap, but CMS coupons are typically paid under a **different measure** (e.g., the forward measure of the payment date). This measure mismatch produces a **CMS convexity adjustment** that can be several basis points for long-tenor CMS rates. This section derives the adjustment using both the direct measure-change approach and the replication argument, and presents Hagan's widely-used formula.

---

## CMS Products

### CMS Coupon

A **CMS coupon** pays the swap rate $S(T_f)$ observed at fixing date $T_f$ at payment date $T_p$:

$$
\text{CMS Coupon} = \delta \, S(T_f) \quad \text{paid at } T_p
$$

where $\delta$ is the day count fraction. The swap rate $S(T_f)$ is the par rate for a swap of specified tenor (e.g., 10 years) starting at $T_f$.

### CMS Cap/Floor

A **CMS caplet** pays $\delta \max(S(T_f) - K, 0)$ at $T_p$.

### The Measure Mismatch

The swap rate $S(t)$ is a martingale under the annuity measure $\mathbb{Q}^A$ (numéraire $A(t)$), but the CMS coupon is paid at $T_p$ with discount factor $P(0, T_p)$. The relevant pricing measure is $\mathbb{Q}^{T_p}$ (numéraire $P(t, T_p)$).

Since $\mathbb{Q}^A \neq \mathbb{Q}^{T_p}$ in general:

$$
\mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] \neq S(0)
$$

The difference $\mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] - S(0)$ is the **CMS convexity adjustment**.

---

## Derivation via Measure Change

### Pricing the CMS Coupon

The present value of the CMS coupon is

$$
V_0 = P(0, T_p) \, \mathbb{E}^{\mathbb{Q}^{T_p}}[\delta \, S(T_f)]
$$

### Change from Annuity to Forward Measure

The Radon--Nikodym derivative from $\mathbb{Q}^A$ to $\mathbb{Q}^{T_p}$ is

$$
\frac{d\mathbb{Q}^{T_p}}{d\mathbb{Q}^A}\bigg|_{\mathcal{F}_t} = \frac{P(t, T_p) \cdot A(0)}{A(t) \cdot P(0, T_p)}
$$

Therefore:

$$
\mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] = \frac{A(0)}{P(0, T_p)} \, \mathbb{E}^{\mathbb{Q}^A}\!\left[S(T_f) \cdot \frac{P(T_f, T_p)}{A(T_f)}\right]
$$

### The Annuity Mapping Function

Define the **annuity mapping function** $G(S) = P(T_f, T_p) / A(T_f)$ as a function of the swap rate $S = S(T_f)$. Under simplifying assumptions (e.g., parallel shift of the yield curve), $G$ depends on $S$ alone.

Then:

$$
\mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] = \frac{A(0)}{P(0, T_p)} \, \mathbb{E}^{\mathbb{Q}^A}\!\left[S(T_f) \cdot G(S(T_f))\right]
$$

### First-Order Expansion

Expanding $G(S)$ around $S_0 = S(0)$:

$$
G(S) \approx G(S_0) + G'(S_0)(S - S_0) + \frac{1}{2}G''(S_0)(S - S_0)^2
$$

Since $S(t)$ is a martingale under $\mathbb{Q}^A$, $\mathbb{E}^A[S(T_f)] = S_0$ and $\mathbb{E}^A[(S - S_0)] = 0$:

$$
\mathbb{E}^A[S \cdot G(S)] \approx S_0 \, G(S_0) + S_0 \, G'(S_0) \cdot 0 + \text{Var}^A(S) \cdot \left[\frac{1}{2}S_0 G''(S_0) + G'(S_0)\right]
$$

where $\text{Var}^A(S(T_f)) = S_0^2(e^{\sigma_S^2 T_f} - 1) \approx S_0^2 \sigma_S^2 T_f$.

---

## The CMS Convexity Adjustment Formula

### Result

$$
\boxed{\mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] \approx S(0) + S(0)^2 \sigma_S^2 T_f \cdot \frac{A(0)}{P(0, T_p)} \left[G'(S_0) + \frac{1}{2}S_0 G''(S_0)\right]}
$$

The convexity adjustment is

$$
\text{CMS Adj} = S(0)^2 \sigma_S^2 T_f \cdot \frac{A(0)}{P(0, T_p)} \left[G'(S_0) + \frac{1}{2}S_0 G''(S_0)\right]
$$

### Computing G'(S) and G''(S)

For a swap with equal payment periods $\delta$ and $n$ payments, the annuity as a function of the swap rate (under a flat yield assumption) is

$$
A(S) = \delta \sum_{j=1}^{n} \frac{1}{(1 + \delta S)^j} = \frac{1 - (1 + \delta S)^{-n}}{S}
$$

The function $G(S) = P(T_f, T_p)/A(S)$, where $P(T_f, T_p) = (1 + \delta S)^{-k}$ for some index $k$, is a ratio of bond price to annuity.

The derivatives $G'$ and $G''$ involve the **duration** and **convexity** of the underlying swap:

$$
G'(S_0) \approx -\frac{1}{S_0}\left(\frac{P(0,T_p)}{A(0)} \cdot D_{\text{swap}} + \frac{P(0,T_p)}{A(0)} - \frac{P(0,T_p)}{A(0)}\right)
$$

where $D_{\text{swap}}$ is the modified duration of the annuity stream.

---

## Hagan's Replication Approach

### The Replication Argument

Hagan (2003) proposed an alternative derivation based on static replication. The key insight is that the CMS coupon can be replicated using a portfolio of swaptions across all strikes:

$$
S(T_f) = S(T_f)^+ - (-S(T_f))^+ = \text{call}(S, 0) - \text{put}(S, 0)
$$

More precisely, using the general replication identity:

$$
f(S(T_f)) = f(S_0) + f'(S_0)(S(T_f) - S_0) + \int_0^{S_0} f''(K) (K - S(T_f))^+ dK + \int_{S_0}^{\infty} f''(K)(S(T_f) - K)^+ dK
$$

For $f(S) = S$ (linear), $f'' = 0$, so the CMS coupon under the annuity measure would equal $S_0$. The convexity adjustment arises when this is priced under the forward measure instead.

### Hagan's Formula

For a CMS coupon paying $S(T_f)$ at $T_p$, Hagan derives

$$
\text{CMS Adj} \approx \sigma_S^2 T_f \cdot S_0 \cdot h(S_0)
$$

where $h(S_0)$ involves the duration and convexity of the underlying swap:

$$
h(S_0) = \frac{\delta S_0}{1 - (1+\delta S_0)^{-n}} \cdot \left[\frac{1}{S_0} - \frac{n\delta}{(1+\delta S_0)((1+\delta S_0)^n - 1)}\right]
$$

This is a model-free result in the sense that it depends only on the swaption implied volatility $\sigma_S$ and the swap structure, not on the specific dynamics assumed for forward rates.

---

## Worked Example

??? example "CMS Convexity Adjustment Calculation"

    **Setup:** CMS 10Y coupon, fixed in 2 years, paid at $T_p = 2.25$ (3 months after fixing).

    **Parameters:**

    - Forward 10Y swap rate: $S(0) = 4.0\% = 0.04$
    - Swaption implied vol: $\sigma_S = 25\%$
    - Fixing time: $T_f = 2.0$
    - Annual payments, $\delta = 1$, $n = 10$

    **Step 1: Compute the annuity mapping derivative**

    Duration of a 10Y par swap at 4%: $D_{\text{swap}} \approx 8.1$ years.

    $h(S_0) = \frac{1 \times 0.04}{1 - 1.04^{-10}} \times [1/0.04 - 10/(1.04 \times (1.04^{10} - 1))]$

    $= \frac{0.04}{0.3244} \times [25 - 10/(1.04 \times 0.4802)]$

    $= 0.1233 \times [25 - 20.02]$

    $= 0.1233 \times 4.98 = 0.614$

    **Step 2: Convexity adjustment**

    $\text{CMS Adj} = 0.0625 \times 2.0 \times 0.04 \times 0.614 = 0.00307 = 3.07$ bp

    **Step 3: Adjusted CMS rate**

    $\mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] \approx 4.0\% + 3.07 \text{ bp} = 4.031\%$

    The CMS convexity adjustment of about 3 bp is significantly larger than the timing adjustment for a LIBOR rate, reflecting the longer duration of the underlying swap.

---

## Properties of the CMS Adjustment

### Sign

The CMS convexity adjustment is **positive** for coupon payments: $\mathbb{E}^{T_p}[S] > S_0$. Intuitively, when rates are high the annuity is worth less (discounting effect), so high-rate outcomes are "over-weighted" relative to the annuity measure.

### Magnitude

The adjustment:

- Scales as $\sigma_S^2 T_f$ (increases with volatility and time to fixing)
- Increases with the **tenor** of the underlying swap (longer swaps have higher duration/convexity)
- Is typically 1--10 bp for standard CMS products
- Can reach 20+ bp for long-dated CMS on long-tenor swaps in high-volatility environments

### CMS Caps and Floors

For CMS caps, the convexity adjustment is embedded in the pricing and affects the effective strike. CMS cap pricing requires integrating the swaption smile across strikes, making it sensitive to the volatility surface (not just ATM vol).

---

## Key Takeaways

- The **CMS convexity adjustment** arises from pricing a swap rate (martingale under the annuity measure) under a forward measure for the payment date
- The adjustment is always **positive** for CMS coupons, meaning the CMS rate exceeds the forward swap rate
- The correction depends on the **duration and convexity** of the underlying swap and scales as $\sigma_S^2 T_f$
- **Hagan's replication approach** provides a model-free formula using swaption prices
- For long-tenor CMS rates (e.g., CMS 30Y), the adjustment can be substantial (10+ bp)
- Accurate CMS pricing requires the full swaption smile, not just ATM volatility

---

## Further Reading

- Hagan (2003), "Convexity Conundrums: Pricing CMS Swaps, Caps, and Floors"
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 13
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volume III, Chapter 16
- Pelsser (2003), "Mathematical Foundation of Convexity Correction"
