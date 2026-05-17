# No-Arbitrage Relations

No-arbitrage principles link discount factors, zero rates, and forward rates. These relations are the foundation of curve construction and fixed-income pricing, ensuring internal consistency of the term structure.

---

## The Fundamental No-Arbitrage Principle

An **arbitrage opportunity** is a trading strategy that:

1. Requires no initial investment
2. Has no possibility of loss
3. Has positive probability of profit

In well-functioning markets, arbitrage opportunities cannot persist. This principle imposes strong constraints on the relationships between financial instruments.

---

## Replication Argument for Forward Rates

Recall (see [§ Simple Forward Rates from Discount Factors](forward_rates_and_term_structures.md#simple-forward-rates-from-discount-factors)): comparing the direct $T_2$-bond strategy with a $T_1$-bond rolled into a forward locks in

$$
\frac{P(0, T_1)}{P(0, T_2)} = 1 + F(0; T_1, T_2)(T_2 - T_1),
$$

so the forward rate arises directly from no-arbitrage.

---

## Discount Factor Constraints

### Monotonicity

Under absence of arbitrage with non-negative rates:

$$
T_1 < T_2 \implies P(0, T_1) \geq P(0, T_2)
$$

**Proof:** If $P(0, T_1) < P(0, T_2)$:

- Buy the $T_1$ bond (cost $P(0, T_1)$)
- Sell the $T_2$ bond (receive $P(0, T_2)$)
- Net cash: $P(0, T_2) - P(0, T_1) > 0$
- At $T_1$: Receive 1, invest risk-free to $T_2$
- At $T_2$: Have $\geq 1$, pay 1 on short position
- This is arbitrage

### Positivity

Discount factors must be strictly positive:

$$
P(0, T) > 0 \quad \text{for all } T
$$

A non-positive discount factor would imply:

- Receiving money today for a future obligation (if $P < 0$)
- Getting a free bond (if $P = 0$)

Both are arbitrage.

### Convexity (Jensen's Inequality Effect)

For stochastic rates, discount factors exhibit convexity:

$$
P(0, T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s ds}\right] \geq e^{-\mathbb{E}^{\mathbb{Q}}\left[\int_0^T r_s ds\right]}
$$

by Jensen's inequality (since $e^{-x}$ is convex).

---

## No-Arbitrage in Continuous Time

### Instantaneous Forward Rates

Recall (see [§ Instantaneous Forward Rate](forward_rates_and_term_structures.md#instantaneous-forward-rate)): the continuous-time analog yields $P(0,T) = P(0,t)\,e^{-\int_t^T f(0,u)\,du}$ and $f(0,T) = -\partial_T \log P(0,T)$.

### Chain Rule for Discount Factors

For any partition $0 = T_0 < T_1 < \cdots < T_n = T$:

$$
P(0, T) = \prod_{i=1}^{n} \frac{P(0, T_i)}{P(0, T_{i-1})} \cdot P(0, T_0)
= \prod_{i=1}^{n} \frac{P(0, T_i)}{P(0, T_{i-1})}
$$

This **multiplicative decomposition** underlies bootstrapping algorithms.

---

## Coupon Bond Pricing

### Linearity of Pricing

A coupon bond with cashflows $c_i$ at times $T_i$ (for $i = 1, \ldots, n$) has price:

$$
B_0 = \sum_{i=1}^n c_i \cdot P(0, T_i)
$$

This is a direct consequence of:

1. **Value additivity:** Portfolio value = sum of component values
2. **No arbitrage:** Each cashflow is discounted at its appropriate rate

### Par Yield

The **par yield** $y_n$ for maturity $T_n$ is the coupon rate that makes a bond trade at par:

$$
1 = \sum_{i=1}^n y_n \cdot \delta_i \cdot P(0, T_i) + P(0, T_n)
$$

where $\delta_i = T_i - T_{i-1}$ is the accrual fraction.

Solving:

$$
y_n = \frac{1 - P(0, T_n)}{\sum_{i=1}^n \delta_i \cdot P(0, T_i)}
$$

Par yields are observable in swap markets.

---

## Static Arbitrage Conditions

### Calendar Spread Arbitrage

A curve violates no-arbitrage if:

$$
\frac{P(0, T_1)}{P(0, T_2)} < 1 \quad \text{for some } T_1 < T_2
$$

This would imply a negative forward rate:

$$
F(0; T_1, T_2) = \frac{1}{T_2 - T_1}\left(\frac{P(0, T_1)}{P(0, T_2)} - 1\right) < 0
$$

While negative forwards can occur (with negative rates), **implied negative rates must be consistent with market reality**.

### Butterfly Arbitrage

For three maturities $T_1 < T_2 < T_3$, convexity requires:

$$
P(0, T_2) \leq \lambda P(0, T_1) + (1-\lambda) P(0, T_3)
$$

where $\lambda = (T_3 - T_2)/(T_3 - T_1)$.

Violation implies arbitrage via a butterfly trade:

- Long $\lambda$ units of $T_1$ bond
- Long $(1-\lambda)$ units of $T_3$ bond  
- Short 1 unit of $T_2$ bond

---

## Forward-Starting Instruments

### Forward Bond

A **forward contract** to buy a $T_2$-bond at time $T_1$ has forward price:

$$
F_B(0; T_1, T_2) = \frac{P(0, T_2)}{P(0, T_1)}
$$

This is the ratio of discount factors, reflecting no-arbitrage.

### Forward Swap

A **forward-starting swap** beginning at $T_0$ with payments at $T_1, \ldots, T_n$ has forward swap rate:

$$
S(0; T_0, T_n) = \frac{P(0, T_0) - P(0, T_n)}{\sum_{i=1}^n \delta_i P(0, T_i)}
$$

This rate makes the swap have zero initial value.

---

## Arbitrage Checks for Curve Construction

When constructing a yield curve, verify:

| Check | Condition | Failure Interpretation |
|-------|-----------|------------------------|
| Positivity | $P(0,T) > 0$ | Impossible prices |
| Monotonicity | $P(0,T_1) \geq P(0,T_2)$ for $T_1 < T_2$ | Calendar arbitrage |
| Smoothness | No extreme oscillations in $f(0,T)$ | Numerical instability |
| Instrument fit | Reprices input instruments | Calibration error |

---

## Practical Implications

### For Traders
- Arbitrage conditions define **fair value bounds**
- Violations signal **relative value opportunities** or **data errors**
- Forward rates should be **economically sensible**

### For Quants
- Curve construction must **respect no-arbitrage**
- Interpolation schemes should **preserve monotonicity**
- Model calibration should **exactly match liquid instruments**

### For Risk Managers
- Arbitrage-free curves ensure **consistent risk measures**
- Violations in stress scenarios may indicate **model breakdown**
- Forward rates provide **sensitivity benchmarks**

---

## Key Takeaways

- No-arbitrage links forwards and discount factors via replication
- Discount factors must be positive and (typically) decreasing
- Coupon bond pricing follows from linearity and no-arbitrage
- Calendar and butterfly arbitrage conditions constrain curve shapes
- Curve construction must respect these constraints for consistency

---

## Further Reading

- Björk, *Arbitrage Theory in Continuous Time*, Chapter 22
- Brigo & Mercurio, *Interest Rate Models—Theory and Practice*, Chapters 1-2
- Rebonato, *Modern Pricing of Interest-Rate Derivatives*, Chapter 2

---

## Exercises

**Exercise 1.** Prove that $P(t, T_1) \ge P(t, T_2)$ for $T_1 \le T_2$ must hold to prevent arbitrage. Construct the arbitrage strategy if this condition is violated: specify which bonds to buy, which to sell, and show the resulting profit.

??? success "Solution to Exercise 1"
    **Claim:** If $P(t, T_1) < P(t, T_2)$ for some $T_1 < T_2$, then an arbitrage exists.

    **Arbitrage strategy construction:**

    1. At time $t$: **Buy** one $T_1$-maturity zero-coupon bond (cost $P(t, T_1)$) and **sell** one $T_2$-maturity zero-coupon bond (receive $P(t, T_2)$).
    2. Net cash at time $t$: $P(t, T_2) - P(t, T_1) > 0$ (positive by assumption).
    3. At time $T_1$: Receive \$1 from the $T_1$-bond. Invest this \$1 at the prevailing risk-free rate over $[T_1, T_2]$.
    4. At time $T_2$: The invested amount grows to $1/P(T_1, T_2) \geq 1$ (since $P(T_1, T_2) \leq 1$ under non-negative rates). Use \$1 of this to settle the short $T_2$-bond obligation.

    **Result:** The trader pockets $P(t, T_2) - P(t, T_1) > 0$ at inception, has no further obligations (the $T_2$-bond liability is covered), and may have additional surplus from the reinvestment. This is a riskless profit from zero net investment — an arbitrage.

    Therefore, no-arbitrage requires $P(t, T_1) \geq P(t, T_2)$ whenever $T_1 \leq T_2$. $\square$

---

**Exercise 2.** Show that the multiplicative property $P(t, T_2) = P(t, T_1) \cdot P(t; T_1, T_2)$ where $P(t; T_1, T_2)$ is the forward discount factor, follows from no-arbitrage. Derive the forward discount factor from the two zero-coupon bond prices.

??? success "Solution to Exercise 2"
    Define the **forward discount factor** as the price at time $t$ of a forward contract to buy a zero-coupon bond maturing at $T_2$, with delivery at $T_1$:

    $$
    P(t; T_1, T_2) := \frac{P(t, T_2)}{P(t, T_1)}
    $$

    **No-arbitrage derivation:** Consider two strategies to receive \$1 at $T_2$, initiated at time $t$:

    **Strategy A:** Buy one $T_2$-bond at cost $P(t, T_2)$.

    **Strategy B:** Buy $P(t; T_1, T_2)$ units of a $T_1$-bond at cost $P(t; T_1, T_2) \cdot P(t, T_1)$, combined with a forward agreement to invest the $T_1$ proceeds at the forward rate over $[T_1, T_2]$.

    At $T_1$, Strategy B delivers $P(t; T_1, T_2)$ units of currency. Investing this at the forward rate over $[T_1, T_2]$ yields exactly \$1 at $T_2$ (by definition of the forward discount factor).

    By no-arbitrage, both strategies have the same cost:

    $$
    P(t, T_2) = P(t; T_1, T_2) \cdot P(t, T_1) = \frac{P(t, T_2)}{P(t, T_1)} \cdot P(t, T_1)
    $$

    which is the multiplicative decomposition:

    $$
    P(t, T_2) = P(t, T_1) \cdot P(t; T_1, T_2)
    $$

    This shows that the discount factor for any maturity can be decomposed into the product of the discount factor to an intermediate date and the forward discount factor from that intermediate date onward — a direct consequence of the absence of arbitrage.

---

**Exercise 3.** A yield curve has $P(0,1) = 0.97$, $P(0,2) = 0.93$, $P(0,3) = 0.90$. Verify that the forward rates $f(0;0,1)$, $f(0;1,2)$, $f(0;2,3)$ are all positive and that the no-arbitrage condition $P(0,3) = P(0,1) \cdot P(0;1,2) \cdot P(0;2,3)$ holds.

??? success "Solution to Exercise 3"
    **Step 1 — Compute forward rates.** Using the simply compounded forward rate formula $F(0; T_1, T_2) = \frac{1}{T_2 - T_1}\left(\frac{P(0, T_1)}{P(0, T_2)} - 1\right)$:

    $$
    F(0; 0, 1) = \frac{1}{1}\left(\frac{1}{0.97} - 1\right) = \frac{0.03}{0.97} \approx 3.093\%
    $$

    $$
    F(0; 1, 2) = \frac{1}{1}\left(\frac{0.97}{0.93} - 1\right) = \frac{0.04}{0.93} \approx 4.301\%
    $$

    $$
    F(0; 2, 3) = \frac{1}{1}\left(\frac{0.93}{0.90} - 1\right) = \frac{0.03}{0.90} \approx 3.333\%
    $$

    All three forward rates are strictly positive.

    **Step 2 — Verify the multiplicative decomposition.** The forward discount factors are:

    $$
    P(0; 0, 1) = P(0, 1) = 0.97
    $$

    $$
    P(0; 1, 2) = \frac{P(0, 2)}{P(0, 1)} = \frac{0.93}{0.97} \approx 0.95876
    $$

    $$
    P(0; 2, 3) = \frac{P(0, 3)}{P(0, 2)} = \frac{0.90}{0.93} \approx 0.96774
    $$

    The product:

    $$
    P(0; 0, 1) \times P(0; 1, 2) \times P(0; 2, 3) = 0.97 \times 0.95876 \times 0.96774
    $$

    $$
    = 0.97 \times 0.92784 = 0.90
    $$

    This equals $P(0, 3) = 0.90$, confirming the no-arbitrage chain rule:

    $$
    P(0, 3) = P(0, 1) \cdot \frac{P(0, 2)}{P(0, 1)} \cdot \frac{P(0, 3)}{P(0, 2)} = P(0, 3)
    $$

    The identity holds by construction of the forward discount factors as ratios of consecutive discount factors.

---

**Exercise 4.** The calendar spread condition for European call options on zero-coupon bonds requires $C(t, T_1, K) \le C(t, T_2, K)$ for $T_1 \le T_2$ (same strike, longer maturity is worth more). Relate this to the no-arbitrage condition on discount factors.

??? success "Solution to Exercise 4"
    A European call on a zero-coupon bond with maturity $T_2$ gives the holder the right to buy the bond at strike $K$ at exercise time $T_e \leq T_2$. Its value at time $t$ is:

    $$
    C(t, T_2, K) = P(t, T_2) \cdot \mathbb{E}^{T_2}\left[\left(\frac{1}{K} - \frac{1}{P(T_e, T_2)}\right)^+ \cdot K\right]
    $$

    More directly, consider two calls with the same strike $K$ and exercise date, but on bonds with different maturities $T_1 < T_2$.

    The payoff of a call on a $T_2$-bond at exercise time $T_e$ is $(P(T_e, T_2) - K)^+$, while the call on a $T_1$-bond pays $(P(T_e, T_1) - K)^+$.

    The no-arbitrage condition on discount factors requires $P(T_e, T_2) \leq P(T_e, T_1)$ for $T_1 \leq T_2$ (longer-maturity bonds are worth less). This means the $T_1$-bond call pays off in **more** states and with **higher** payoffs than the $T_2$-bond call.

    Wait — the exercise statement says $C(t, T_1, K) \leq C(t, T_2, K)$, meaning the longer-maturity bond option is worth more. This seems counterintuitive since $P(\cdot, T_2) \leq P(\cdot, T_1)$. However, interpreting the call as having maturity $T_i$ as both the bond maturity and the option expiry (as in a caplet structure), the longer option has more time value.

    The connection to discount factor no-arbitrage is: the calendar spread condition on options ensures that no arbitrage can be constructed by trading options of adjacent maturities. If $C(t, T_1, K) > C(t, T_2, K)$ for a call where longer maturity should be worth more, one could sell the overpriced short-maturity option and buy the cheap long-maturity option, locking in a riskless profit. This mirrors the discount factor monotonicity condition $P(t, T_1) \geq P(t, T_2)$ — both are manifestations of the same underlying principle that longer-dated claims must be priced consistently with shorter-dated ones.

---

**Exercise 5.** In continuous time, the no-arbitrage relation $R(t, T) = \frac{1}{T-t}\int_t^T f(t, u)\,du$ links zero rates to forward rates. If the forward rate curve $f(0, T)$ is constant at $f_0 = 4\%$, what shape does the zero rate curve have? What about the discount factor curve?

??? success "Solution to Exercise 5"
    If $f(0, T) = f_0 = 4\%$ for all $T \geq 0$, then the zero rate is:

    $$
    R(0, T) = \frac{1}{T}\int_0^T f(0, u)\,du = \frac{1}{T}\int_0^T f_0\,du = \frac{f_0 \cdot T}{T} = f_0 = 4\%
    $$

    The zero rate curve is **flat** at 4% for all maturities. A constant forward rate curve implies a constant zero rate curve — the two coincide.

    The discount factor curve is:

    $$
    P(0, T) = e^{-\int_0^T f_0\,du} = e^{-f_0 T} = e^{-0.04T}
    $$

    This is a **strictly decreasing exponential** function of $T$, starting at $P(0, 0) = 1$ and decaying toward zero as $T \to \infty$. For example:

    - $P(0, 1) = e^{-0.04} \approx 0.9608$
    - $P(0, 10) = e^{-0.40} \approx 0.6703$
    - $P(0, 25) = e^{-1.00} \approx 0.3679$

    This is the simplest possible term structure: flat rates at all horizons, with the discount curve being a pure exponential decay.

---

**Exercise 6.** A trader observes the following quotes: 1-year deposit at 3%, 1x2 FRA at 3.5%, 2-year par swap at 3.2%. Check whether these quotes are internally consistent by computing the implied 2-year discount factor from: (a) the deposit + FRA, and (b) the swap rate. If they disagree, which instrument is likely mispriced?

??? success "Solution to Exercise 6"
    **Part (a) — Discount factor from deposit + FRA:**

    The 1-year deposit rate of 3% (simply compounded) gives:

    $$
    P(0, 1) = \frac{1}{1 + 0.03 \times 1} = \frac{1}{1.03} \approx 0.97087
    $$

    The 1x2 FRA at 3.5% implies a forward rate $F(0; 1, 2) = 3.5\%$ over $[1, 2]$. Using the forward rate relation:

    $$
    P(0, 2) = \frac{P(0, 1)}{1 + F(0; 1, 2) \times 1} = \frac{0.97087}{1.035} \approx 0.93804
    $$

    **Part (b) — Discount factor from the swap rate:**

    The 2-year par swap rate of 3.2% (with annual payments) satisfies:

    $$
    S_2 = \frac{1 - P(0, 2)}{P(0, 1) + P(0, 2)}
    $$

    Using $P(0, 1) = 0.97087$ from the deposit rate and solving for $P(0, 2)$:

    $$
    0.032 = \frac{1 - P(0, 2)}{0.97087 + P(0, 2)}
    $$

    $$
    0.032 \times (0.97087 + P(0, 2)) = 1 - P(0, 2)
    $$

    $$
    0.031068 + 0.032 \, P(0, 2) = 1 - P(0, 2)
    $$

    $$
    1.032 \, P(0, 2) = 0.968932
    $$

    $$
    P(0, 2) = \frac{0.968932}{1.032} \approx 0.93889
    $$

    **Comparison:** The two methods give:

    - Deposit + FRA: $P(0, 2) \approx 0.93804$
    - Swap rate: $P(0, 2) \approx 0.93889$

    These disagree by approximately 0.085%, indicating the quotes are **not internally consistent**.

    **Which instrument is likely mispriced?** The deposit rate and swap rate are typically the most liquid and reliable quotes. The FRA is the most likely candidate for mispricing because:

    1. FRAs are generally less liquid than deposits and swaps, so their quotes may be stale or wider.
    2. The deposit + FRA path implies a higher 2-year rate (lower $P(0,2)$) than the swap, meaning the FRA rate of 3.5% is too high relative to the other instruments.
    3. The implied forward rate from the deposit and swap is $F = 1/1 \times (P(0,1)/P(0,2) - 1) = (0.97087/0.93889 - 1) = 3.406\%$, suggesting the FRA should be approximately 3.41% rather than 3.5%.

    A trader could exploit this by paying fixed on the FRA (locking in borrowing at 3.5%) and constructing the synthetic forward at 3.41% using the deposit and swap, earning approximately 9 basis points.
