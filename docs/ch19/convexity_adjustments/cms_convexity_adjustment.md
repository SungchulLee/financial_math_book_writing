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

---

## Exercises

**Exercise 1.** A CMS 10Y coupon fixes in 5 years ($T_f = 5$) and is paid at $T_p = 5.25$. The forward 10-year swap rate is $S(0) = 3.5\%$, the swaption implied volatility is $\sigma_S = 22\%$, and the underlying swap has annual payments ($\delta = 1$, $n = 10$). Using Hagan's formula, compute the CMS convexity adjustment and the adjusted CMS rate. Compare the result to the worked example in this section and explain why the adjustment is larger.

??? success "Solution to Exercise 1"

    **Given:** $S(0) = 0.035$, $\sigma_S = 0.22$, $T_f = 5$, $\delta = 1$, $n = 10$.

    **Step 1: Compute $h(S_0)$ using Hagan's formula.**

    $$
    h(S_0) = \frac{\delta S_0}{1 - (1 + \delta S_0)^{-n}} \cdot \left[\frac{1}{S_0} - \frac{n\delta}{(1 + \delta S_0)((1 + \delta S_0)^n - 1)}\right]
    $$

    Substituting $S_0 = 0.035$, $\delta = 1$, $n = 10$:

    $(1 + \delta S_0)^n = 1.035^{10} = 1.4106$

    $(1 + \delta S_0)^{-n} = 1/1.4106 = 0.7089$

    $$
    \frac{\delta S_0}{1 - (1+\delta S_0)^{-n}} = \frac{0.035}{1 - 0.7089} = \frac{0.035}{0.2911} = 0.1202
    $$

    $$
    \frac{1}{S_0} = \frac{1}{0.035} = 28.571
    $$

    $$
    \frac{n\delta}{(1+\delta S_0)((1+\delta S_0)^n - 1)} = \frac{10}{1.035 \times 0.4106} = \frac{10}{0.4250} = 23.529
    $$

    $$
    h(S_0) = 0.1202 \times (28.571 - 23.529) = 0.1202 \times 5.042 = 0.606
    $$

    **Step 2: Convexity adjustment.**

    $$
    \text{CMS Adj} = \sigma_S^2 T_f \cdot S_0 \cdot h(S_0) = 0.0484 \times 5 \times 0.035 \times 0.606 = 0.00513
    $$

    This is $5.13$ basis points.

    **Step 3: Adjusted CMS rate.**

    $$
    \mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] \approx 3.5\% + 5.13 \text{ bp} = 3.551\%
    $$

    **Comparison with the worked example:** The worked example had $S(0) = 4\%$, $\sigma_S = 25\%$, $T_f = 2$, giving an adjustment of $3.07$ bp. The current exercise gives $5.13$ bp, which is larger for two reasons: (1) the longer fixing horizon ($T_f = 5$ vs $T_f = 2$) contributes a factor of $5/2 = 2.5$ increase, and (2) although the forward rate and volatility are slightly lower, the dominant effect is the $T_f$ dependence. The adjustment scales linearly with $T_f$, so longer-dated CMS products carry substantially larger convexity adjustments.

---

**Exercise 2.** Show that the CMS convexity adjustment is always positive by arguing that $G'(S_0) > 0$ (or equivalently, that $h(S_0) > 0$). Specifically, for a swap with $n$ annual payments, verify that

$$
\frac{1}{S_0} > \frac{n\delta}{(1 + \delta S_0)\bigl((1 + \delta S_0)^n - 1\bigr)}
$$

for all $S_0 > 0$, $n \geq 2$, and $\delta > 0$.

??? success "Solution to Exercise 2"

    We need to show that for all $S_0 > 0$, $n \geq 2$, and $\delta > 0$:

    $$
    \frac{1}{S_0} > \frac{n\delta}{(1+\delta S_0)((1+\delta S_0)^n - 1)}
    $$

    Let $x = \delta S_0 > 0$ and rewrite the inequality as:

    $$
    \frac{1}{x/\delta} > \frac{n\delta}{(1+x)((1+x)^n - 1)} \implies \frac{\delta}{x} > \frac{n\delta}{(1+x)((1+x)^n - 1)}
    $$

    Dividing both sides by $\delta > 0$:

    $$
    \frac{1}{x} > \frac{n}{(1+x)((1+x)^n - 1)}
    $$

    This is equivalent to:

    $$
    (1+x)((1+x)^n - 1) > nx
    $$

    Let $u = 1 + x > 1$. Then $x = u - 1$ and the inequality becomes:

    $$
    u(u^n - 1) > n(u-1)
    $$

    By the binomial/geometric expansion, $u^n - 1 = (u-1)(u^{n-1} + u^{n-2} + \cdots + 1)$, so:

    $$
    u(u-1)\sum_{k=0}^{n-1} u^k > n(u-1)
    $$

    Since $u > 1$, we have $u - 1 > 0$, so dividing both sides:

    $$
    u \sum_{k=0}^{n-1} u^k > n
    $$

    Since $u > 1$, each term $u \cdot u^k = u^{k+1} > 1$ for $k = 0, 1, \ldots, n-1$. Therefore:

    $$
    u \sum_{k=0}^{n-1} u^k = \sum_{k=0}^{n-1} u^{k+1} = u + u^2 + \cdots + u^n > \underbrace{1 + 1 + \cdots + 1}_{n} = n
    $$

    The strict inequality holds since $u > 1$ and $n \geq 2$. Therefore $h(S_0) > 0$, which implies the CMS convexity adjustment $\sigma_S^2 T_f S_0 h(S_0) > 0$. $\blacksquare$

---

**Exercise 3.** Consider two CMS coupons: CMS 5Y and CMS 30Y, both fixing in 3 years with identical swaption implied volatility $\sigma_S = 20\%$. Without performing a full calculation, explain qualitatively why the CMS 30Y convexity adjustment is much larger than the CMS 5Y adjustment. Which properties of the underlying swap drive this difference?

??? success "Solution to Exercise 3"

    The CMS convexity adjustment depends on the **duration and convexity** of the underlying swap through the function $h(S_0)$. The key factors driving the difference between CMS 5Y and CMS 30Y are:

    1. **Modified duration:** A 30Y swap at par has a much higher modified duration (roughly 17--19 years) compared to a 5Y swap (roughly 4.3--4.5 years). Higher duration means the annuity value $A(S)$ is more sensitive to changes in the swap rate, amplifying the measure-change effect.

    2. **Convexity of the annuity:** The annuity of a 30Y swap is a more convex function of the swap rate than that of a 5Y swap. The second derivative $G''(S_0)$ is larger for the 30Y swap, contributing an additional term to the adjustment formula.

    3. **Level of $h(S_0)$:** From Hagan's formula, $h(S_0)$ involves $n\delta/((1+\delta S_0)((1+\delta S_0)^n - 1))$, and the difference $1/S_0 - n\delta/\ldots$ is sensitive to $n$. For larger $n$ (more payments), the annuity mapping function $G(S)$ has a steeper dependence on $S$, so $G'(S_0)$ is larger in magnitude.

    4. **Numerically:** For $S_0 = 4\%$, the value $h(S_0)$ for CMS 30Y is approximately 3--4 times larger than for CMS 5Y. Combined with the $\sigma_S^2 T_f S_0$ factor (which is the same for both since the fixing time and vol are identical), the CMS 30Y adjustment is roughly 3--4 times larger than the CMS 5Y adjustment.

    In summary, the CMS 30Y adjustment is much larger because the 30Y swap has higher duration and convexity, making the annuity-to-forward measure change more pronounced.

---

**Exercise 4.** Starting from the Radon--Nikodym derivative

$$
\frac{d\mathbb{Q}^{T_p}}{d\mathbb{Q}^A}\bigg|_{\mathcal{F}_{T_f}} = \frac{P(T_f, T_p) \cdot A(0)}{A(T_f) \cdot P(0, T_p)}
$$

derive the expression $\mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] = \frac{A(0)}{P(0, T_p)}\,\mathbb{E}^{\mathbb{Q}^A}[S(T_f) \cdot G(S(T_f))]$ where $G(S) = P(T_f, T_p)/A(T_f)$. State clearly which properties of $S(T_f)$ under $\mathbb{Q}^A$ you use.

??? success "Solution to Exercise 4"

    Starting from the definition of the $T_p$-forward measure expectation:

    $$
    P(0, T_p) \, \mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{T_f} r(s)ds} \, P(T_f, T_p) \, S(T_f)\right]
    $$

    Under the annuity measure $\mathbb{Q}^A$ with numéraire $A(t)$:

    $$
    A(0) \, \mathbb{E}^{\mathbb{Q}^A}[S(T_f) \cdot g(T_f)] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{T_f} r(s)ds} \, A(T_f) \, S(T_f) \cdot g(T_f)\right]
    $$

    for any $\mathcal{F}_{T_f}$-measurable $g$. Setting $g(T_f) = P(T_f, T_p)/A(T_f)$:

    $$
    A(0) \, \mathbb{E}^{\mathbb{Q}^A}\!\left[S(T_f) \cdot \frac{P(T_f, T_p)}{A(T_f)}\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{T_f} r(s)ds} \, P(T_f, T_p) \, S(T_f)\right]
    $$

    The right-hand side equals $P(0, T_p) \, \mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)]$, so:

    $$
    A(0) \, \mathbb{E}^{\mathbb{Q}^A}\!\left[S(T_f) \cdot \frac{P(T_f, T_p)}{A(T_f)}\right] = P(0, T_p) \, \mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)]
    $$

    Solving:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_p}}[S(T_f)] = \frac{A(0)}{P(0, T_p)} \, \mathbb{E}^{\mathbb{Q}^A}\!\left[S(T_f) \cdot G(S(T_f))\right]
    $$

    where $G(S) = P(T_f, T_p)/A(T_f)$.

    **Properties used:**

    1. $S(T_f)$ is a **martingale** under $\mathbb{Q}^A$: $\mathbb{E}^{\mathbb{Q}^A}[S(T_f)] = S(0)$. This follows from the definition of the swap rate as the ratio of the fixed-for-floating value to the annuity, making $S(t) = V_{\text{float}}(t)/A(t)$ a martingale under the annuity numéraire.

    2. The **numéraire change** between $\mathbb{Q}^A$ and $\mathbb{Q}^{T_p}$ uses the Radon--Nikodym derivative $dQ^{T_p}/dQ^A = (P(T_f,T_p)/P(0,T_p)) \cdot (A(0)/A(T_f))$.

    3. The function $G(S) = P(T_f, T_p)/A(T_f)$ is assumed to depend on $S(T_f)$ alone (the **annuity mapping** assumption), which holds exactly under a one-factor model or under the parallel-shift approximation. $\blacksquare$

---

**Exercise 5.** A CMS cap with strike $K = 4\%$ pays $\delta\max(S(T_f) - K, 0)$ at $T_p$. Explain why pricing this product requires knowledge of the full swaption smile (i.e., implied volatilities across all strikes), not just the ATM swaption volatility. Describe how the static replication formula

$$
\max(S - K, 0) = (S - K)^+ = \int_K^\infty \delta(S - K')\,dK'
$$

can be used together with swaption prices to value the CMS caplet.

??? success "Solution to Exercise 5"

    **Why the full swaption smile is needed:**

    The CMS caplet pays $\delta\max(S(T_f) - K, 0)$ at $T_p$, priced under the $T_p$-forward measure. However, $S$ is a martingale under the annuity measure $\mathbb{Q}^A$, not $\mathbb{Q}^{T_p}$. The change of measure introduces the factor $G(S) = P(T_f, T_p)/A(T_f)$, which is a nonlinear function of $S$. The pricing formula becomes:

    $$
    \text{CMS Caplet} = \frac{A(0)}{P(0,T_p)} \cdot P(0,T_p) \, \delta \, \mathbb{E}^{\mathbb{Q}^A}\!\left[(S(T_f) - K)^+ \cdot G(S(T_f))\right]
    $$

    The product $(S - K)^+ \cdot G(S)$ is a nonlinear function of $S$. To evaluate its expectation under $\mathbb{Q}^A$, we use the **static replication formula**:

    For any twice-differentiable function $f(S)$:

    $$
    f(S) = f(K) + f'(K)(S-K) + \int_0^K f''(\kappa)(\kappa - S)^+ d\kappa + \int_K^\infty f''(\kappa)(S - \kappa)^+ d\kappa
    $$

    Apply this with $f(S) = (S - K)^+ \cdot G(S)$. Since $f''$ is generally nonzero (due to the nonlinearity of $G$), the expectation of $f(S(T_f))$ under $\mathbb{Q}^A$ involves:

    $$
    \mathbb{E}^{\mathbb{Q}^A}[f(S)] = f(S_0) + \int_0^{S_0} f''(\kappa) \, \text{ReceiverSwaption}(\kappa) \, d\kappa + \int_{S_0}^\infty f''(\kappa) \, \text{PayerSwaption}(\kappa) \, d\kappa
    $$

    Each swaption at strike $\kappa$ is priced using its own implied volatility $\sigma_S(\kappa)$, so the integral requires knowledge of swaption prices (or equivalently, implied volatilities) **across all strikes**. Using only the ATM volatility would correspond to assuming a flat smile, which generally misprices the CMS caplet.

    The Dirac delta representation $\max(S-K,0) = \int_K^\infty \delta(S-K')dK'$ shows that the CMS caplet can be viewed as an integral of digital swaptions across all strikes above $K$, each of which depends on the local implied volatility at that strike.

---

**Exercise 6.** A trader prices a 5-year CMS swap (receiving CMS 10Y annually against paying 3-month LIBOR quarterly). The trader uses an ATM-only CMS convexity adjustment of 4.2 bp per coupon. A risk manager argues that the smile is important and that using the full swaption smile increases the adjustment by 1.5 bp. Over 5 annual CMS coupons on a \$500 million notional, compute the total valuation difference between the ATM-only and smile-adjusted approaches.

??? success "Solution to Exercise 6"

    **ATM-only approach:** Adjustment per coupon $= 4.2$ bp.

    Total CMS leg value adjustment (ATM-only): $5 \times 4.2 = 21.0$ bp cumulative adjustment.

    **Smile-adjusted approach:** Adjustment per coupon $= 4.2 + 1.5 = 5.7$ bp.

    Total CMS leg value adjustment (smile): $5 \times 5.7 = 28.5$ bp cumulative adjustment.

    **Dollar difference per coupon:**

    $$
    \Delta_{\text{per coupon}} = 1.5 \text{ bp} \times \$500{,}000{,}000 = 0.00015 \times 500{,}000{,}000 = \$75{,}000
    $$

    **Total dollar difference over 5 coupons:**

    $$
    \Delta_{\text{total}} = 5 \times \$75{,}000 = \$375{,}000
    $$

    More precisely, discounting each coupon's difference:

    $$
    \Delta_{\text{total, PV}} = \$500{,}000{,}000 \times 0.00015 \times \sum_{j=1}^{5} P(0, T_j)
    $$

    Assuming discount factors $P(0,1) \approx 0.96$, $P(0,2) \approx 0.92$, $P(0,3) \approx 0.89$, $P(0,4) \approx 0.86$, $P(0,5) \approx 0.82$:

    $$
    = \$75{,}000 \times (0.96 + 0.92 + 0.89 + 0.86 + 0.82) = \$75{,}000 \times 4.45 = \$333{,}750
    $$

    The present-valued difference is approximately **\$334,000**. On a \$500 million notional, this is a material valuation difference that underscores the importance of incorporating the swaption smile in CMS pricing.

---

**Exercise 7.** Suppose the swaption implied volatility doubles from $\sigma_S$ to $2\sigma_S$. By what factor does the CMS convexity adjustment approximately change? Verify this using the scaling property of Hagan's formula and discuss the practical implication for CMS product risk management in high-volatility environments.

??? success "Solution to Exercise 7"

    From Hagan's formula:

    $$
    \text{CMS Adj} = \sigma_S^2 \, T_f \cdot S_0 \cdot h(S_0)
    $$

    The function $h(S_0)$ depends only on the swap structure ($S_0$, $\delta$, $n$) and is independent of $\sigma_S$. Therefore, the adjustment depends on volatility **only through the factor $\sigma_S^2$**.

    If $\sigma_S \to 2\sigma_S$:

    $$
    \text{CMS Adj}_{\text{new}} = (2\sigma_S)^2 \, T_f \cdot S_0 \cdot h(S_0) = 4\sigma_S^2 \, T_f \cdot S_0 \cdot h(S_0) = 4 \times \text{CMS Adj}_{\text{old}}
    $$

    The CMS convexity adjustment increases by a **factor of 4** when volatility doubles.

    **Verification:** From the worked example, with $\sigma_S = 25\%$ the adjustment was 3.07 bp. Doubling to $\sigma_S = 50\%$:

    $$
    \text{CMS Adj}_{\text{new}} = 4 \times 3.07 = 12.28 \text{ bp}
    $$

    **Practical implications:**

    1. **Vega risk is amplified:** The CMS convexity adjustment has a convex dependence on volatility ($\propto \sigma^2$), meaning that the sensitivity of the CMS adjustment to volatility changes (i.e., the "CMS vega") itself increases with volatility. In high-volatility environments, the CMS vega is larger, making hedging more expensive and volatile.

    2. **Crisis scenarios:** During market stress (e.g., 2008, 2020), swaption volatilities can spike dramatically. A doubling of vol from 20% to 40% would quadruple the CMS adjustment, potentially swinging the mark-to-market of a large CMS book by tens of millions of dollars.

    3. **Hedging frequency:** The quadratic sensitivity to volatility means that CMS books must be rehedged more frequently in high-volatility regimes, as the adjustment changes rapidly with market moves.

    4. **Model risk:** In high-volatility environments, the first-order approximation underlying Hagan's formula may become less accurate, requiring either higher-order corrections or full numerical replication-based pricing.
