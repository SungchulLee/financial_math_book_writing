# Fitting Initial Yield Curves


A fundamental requirement of any interest-rate model is the **exact fit of the initial yield curve**. Since discount factors are directly observable from the market, a model must reproduce them to avoid static arbitrage.

---

## Market input and bootstrapping


The market provides quotes for liquid instruments such as:

- deposits and short-term rates,
- futures and FRAs,
- OIS and IRS swaps.

From these, a discount curve $P(0,T)$ is constructed via **bootstrapping**, ensuring that each instrument is priced exactly.

---

## Curve fitting vs model fitting


Two conceptually distinct steps are involved:

1. **Curve construction:** build a smooth, arbitrage-free discount curve from market quotes.
2. **Model initialization:** ensure the model reproduces this curve at time 0.

Modern practice treats curve construction as a pre-model step.

---

## Exact fit techniques


Common approaches to enforce exact fit include:

- **Deterministic shifts:** add a time-dependent drift. Recall (see [§ Short-rate models](../../ch18/short_rate_models/affine_term_structure.md)) for the Hull–White extension $\theta(t)$.
- **Initial term-structure fitting:** calibrate model functions to match $P(0,T)$.
- **HJM framework:** exact fit is automatic by construction. Recall (see [§ HJM](../hjm/forward_rate_dynamics.md)).

Exact fit is essential for pricing curve-sensitive products.

---

## Consequences of poor curve fit


Failure to match the initial curve leads to:

- immediate arbitrage,
- systematic mispricing of swaps and FRAs,
- unstable hedging behavior.

Thus, curve fitting is non-negotiable in practice.

---

## Key takeaways


- The initial yield curve must be fitted exactly.
- Curve construction and model calibration are separate tasks.
- Shifts and HJM ensure consistency with market curves.

---

## Further reading


- Brigo & Mercurio, curve construction.
- Andersen & Piterbarg, interest-rate modeling practice.

---

## Exercises

**Exercise 1.** Suppose you observe the following zero-coupon bond prices: $P(0,0.5) = 0.9950$, $P(0,1) = 0.9870$, $P(0,1.5) = 0.9760$, and $P(0,2) = 0.9620$. Compute the continuously compounded zero rates $R(0,T)$ for each maturity using the relation

$$
P(0,T) = e^{-R(0,T)\,T}
$$

Verify that the zero rates are increasing with maturity and interpret this shape economically.

??? success "Solution to Exercise 1"
    The continuously compounded zero rate is obtained by inverting $P(0,T) = e^{-R(0,T)\,T}$:

    $$
    R(0,T) = -\frac{\ln P(0,T)}{T}
    $$

    **For $T = 0.5$:**

    $$
    R(0, 0.5) = -\frac{\ln 0.9950}{0.5} = -\frac{-0.005013}{0.5} = 1.0025\%
    $$

    **For $T = 1.0$:**

    $$
    R(0, 1.0) = -\frac{\ln 0.9870}{1.0} = -(-0.013091) = 1.3091\%
    $$

    **For $T = 1.5$:**

    $$
    R(0, 1.5) = -\frac{\ln 0.9760}{1.5} = -\frac{-0.024291}{1.5} = 1.6194\%
    $$

    **For $T = 2.0$:**

    $$
    R(0, 2.0) = -\frac{\ln 0.9620}{2.0} = -\frac{-0.038733}{2.0} = 1.9367\%
    $$

    **Summary:**

    | $T$ | $P(0,T)$ | $R(0,T)$ |
    |---|---|---|
    | 0.5 | 0.9950 | 1.003% |
    | 1.0 | 0.9870 | 1.309% |
    | 1.5 | 0.9760 | 1.619% |
    | 2.0 | 0.9620 | 1.937% |

    The zero rates are increasing: $1.003\% < 1.309\% < 1.619\% < 1.937\%$. This is an **upward-sloping (normal) yield curve**, which is the most commonly observed shape. Economically, it reflects:

    - **Term premium:** investors demand higher compensation for locking up capital over longer horizons due to greater uncertainty.
    - **Expectations hypothesis:** the market may expect future short-term rates to rise, pushing longer rates higher.
    - **Liquidity preference:** longer maturities carry more interest-rate risk, warranting a premium.

---

**Exercise 2.** A two-year par swap with semiannual payments has a quoted rate of $s = 3.80\%$. Using the discount factors from Exercise 1, verify whether the par swap rate is consistent with these discount factors via the formula

$$
s = \frac{1 - P(0,T_n)}{\sum_{i=1}^{n} \delta_i\, P(0,T_i)}
$$

where $\delta_i = 0.5$ for semiannual periods. If it is not consistent, explain what adjustment to the curve would be needed.

??? success "Solution to Exercise 2"
    The par swap rate formula for semiannual payments ($\delta_i = 0.5$) is:

    $$
    s = \frac{1 - P(0, T_n)}{\sum_{i=1}^{n} \delta_i \, P(0, T_i)}
    $$

    For a two-year swap with semiannual payments, $n = 4$ and the payment dates are $T_1 = 0.5$, $T_2 = 1.0$, $T_3 = 1.5$, $T_4 = 2.0$.

    **Numerator:**

    $$
    1 - P(0, 2.0) = 1 - 0.9620 = 0.0380
    $$

    **Denominator (annuity):**

    $$
    \sum_{i=1}^{4} 0.5 \times P(0, T_i) = 0.5 \times (0.9950 + 0.9870 + 0.9760 + 0.9620)
    $$

    $$
    = 0.5 \times 3.9200 = 1.9600
    $$

    **Implied par swap rate:**

    $$
    s = \frac{0.0380}{1.9600} = 0.019388 = 1.9388\%
    $$

    The implied par swap rate is approximately $1.94\%$, which is significantly lower than the quoted rate of $3.80\%$. The two are **not consistent**.

    To reconcile the quoted swap rate of $3.80\%$ with the discount factors, the discount curve would need to be adjusted. Specifically, the discount factors at longer maturities would need to be lower (corresponding to higher zero rates). From the formula $s = (1 - P(0,2)) / A$, achieving $s = 3.80\%$ requires:

    $$
    1 - P(0, 2) = 0.0380 \times \frac{A}{0.0380/s} \quad \Longrightarrow \quad P(0,2) \approx 1 - 0.038 \times \frac{1.96}{0.038/0.038}
    $$

    More directly, we need $1 - P(0,2) = 0.038 \times A / 0.0194... \times A = s \times A$, so:

    $$
    P(0,2) = 1 - 0.038 \times A
    $$

    Solving iteratively, the discount factors would need to correspond to zero rates roughly double the current values. This indicates either the swap quote is from a different market date or the discount factors are inconsistent with the swap market. In practice, the bootstrapping algorithm would adjust $P(0,2)$ (and potentially intermediate points) so that the swap is repriced exactly.

---

**Exercise 3.** Consider the Hull--White model with short-rate dynamics

$$
dr(t) = \bigl[\theta(t) - a\,r(t)\bigr]\,dt + \sigma\,dW(t)
$$

Show that exact fit to the initial term structure is achieved by choosing

$$
\theta(t) = \frac{\partial f(0,t)}{\partial t} + a\,f(0,t) + \frac{\sigma^2}{2a}\bigl(1 - e^{-2at}\bigr)
$$

where $f(0,t) = -\frac{\partial}{\partial t}\ln P(0,t)$ is the initial instantaneous forward rate. Explain why this deterministic shift approach is called "fitting the initial curve."

??? success "Solution to Exercise 3"
    In the Hull--White model, the short rate satisfies:

    $$
    dr(t) = [\theta(t) - a\,r(t)]\,dt + \sigma\,dW(t)
    $$

    The zero-coupon bond price in this affine model takes the form:

    $$
    P(t,T) = A(t,T)\,e^{-B(t,T)\,r(t)}
    $$

    where $B(t,T) = \frac{1}{a}(1 - e^{-a(T-t)})$ and $A(t,T)$ depends on $\theta(\cdot)$.

    **Step 1: Relate $\theta(t)$ to the initial forward rate.**

    The instantaneous forward rate is defined as:

    $$
    f(0,T) = -\frac{\partial}{\partial T}\ln P(0,T)
    $$

    In the Hull--White model, $f(0,T)$ is determined by $\theta(\cdot)$. Since the model must reproduce $P(0,T)$ for all $T$, we need the model-implied forward rate $f^{\text{model}}(0,T)$ to equal the market forward rate $f^{\text{mkt}}(0,T)$.

    **Step 2: Derive $\theta(t)$.**

    The solution of the Hull--White SDE is:

    $$
    r(t) = r(0)\,e^{-at} + \int_0^t e^{-a(t-s)}\theta(s)\,ds + \sigma\int_0^t e^{-a(t-s)}\,dW(s)
    $$

    The model-implied forward rate at time 0 for maturity $T$ can be shown to satisfy:

    $$
    f^{\text{model}}(0,T) = \mathbb{E}^{\mathbb{Q}}[r(T)] - \frac{\sigma^2}{2}B(0,T)^2 \cdot (\text{adjustment})
    $$

    Through the explicit bond pricing formula, one obtains:

    $$
    f^{\text{model}}(0,T) = -\frac{\partial}{\partial T}\ln A(0,T) + \frac{\partial B(0,T)}{\partial T}\,r(0)
    $$

    Requiring $f^{\text{model}}(0,T) = f(0,T)$ for all $T$ and differentiating the consistency condition yields:

    $$
    \theta(t) = \frac{\partial f(0,t)}{\partial t} + a\,f(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
    $$

    **Step 3: Interpretation.**

    This formula shows that $\theta(t)$ is completely determined by:

    - $\frac{\partial f(0,t)}{\partial t}$: the slope of the initial forward curve,
    - $a\,f(0,t)$: a mean-reversion pull toward the forward rate level,
    - $\frac{\sigma^2}{2a}(1-e^{-2at})$: a convexity correction that accounts for the variance of the short rate.

    The approach is called "fitting the initial curve" because $\theta(t)$ is a **deterministic function of time** chosen so that the model exactly reproduces every market discount factor $P(0,T)$. The function $\theta(t)$ acts as a time-dependent drift adjustment (a "shift") that absorbs the entire initial term structure into the model, leaving $a$ and $\sigma$ as the free parameters governing dynamics.

---

**Exercise 4.** Explain why the HJM framework provides an automatic exact fit to the initial yield curve, whereas equilibrium short-rate models (such as Vasicek or CIR without extensions) do not. In your answer, reference the role of the initial forward-rate curve $f(0,T)$ as an input to the HJM dynamics.

??? success "Solution to Exercise 4"
    **HJM framework: automatic exact fit.**

    In the Heath--Jarrow--Morton (HJM) framework, the fundamental state variable is the entire forward rate curve $f(t,T)$, and its dynamics under the risk-neutral measure are:

    $$
    df(t,T) = \alpha(t,T)\,dt + \sigma(t,T)\,dW(t)
    $$

    The crucial feature is that the **initial condition** of these dynamics is the observed market forward curve $f(0,T)$. The HJM no-arbitrage drift condition determines $\alpha(t,T)$ in terms of $\sigma(t,T)$:

    $$
    \alpha(t,T) = \sigma(t,T)\int_t^T \sigma(t,u)\,du
    $$

    Since the model starts from the observed $f(0,T)$ and evolves forward in time, every discount factor $P(0,T) = \exp\bigl(-\int_0^T f(0,u)\,du\bigr)$ is reproduced **by construction**. No parameter needs to be adjusted to match the initial curve --- it is an input, not an output.

    **Equilibrium short-rate models: no automatic fit.**

    In contrast, equilibrium models like Vasicek ($dr = a(b - r)\,dt + \sigma\,dW$) or CIR ($dr = a(b-r)\,dt + \sigma\sqrt{r}\,dW$) have a **finite** set of constant parameters $(a, b, \sigma)$. The implied yield curve $R^{\text{model}}(0,T)$ is a specific function of these parameters. For the Vasicek model:

    $$
    P^{\text{Vasicek}}(0,T) = A(T)\,e^{-B(T)\,r(0)}
    $$

    with $A(T)$ and $B(T)$ determined by $(a, b, \sigma)$. This functional form is rigid: it can produce only a limited family of yield curve shapes (monotone increasing, monotone decreasing, or mildly humped). There is no guarantee that the market's yield curve lies in this family.

    In particular, with 3 free parameters, the model cannot match an arbitrary set of $n \gg 3$ discount factors. Extensions like Hull--White add $\theta(t)$ precisely to recover this flexibility. Without such extensions, equilibrium models fail to reproduce the market curve, leading to static arbitrage.

    **Summary:** The HJM framework takes $f(0,T)$ as a given input and builds dynamics on top of it, ensuring automatic fit. Equilibrium short-rate models parameterize the curve shape with finitely many constants, which generically cannot match an arbitrary market curve.

---

**Exercise 5.** A trader builds a discount curve by bootstrapping deposits (up to 6 months), futures (6 months to 2 years), and swaps (2 years to 30 years). After bootstrapping, the instantaneous forward-rate curve $f(0,T)$ exhibits a sudden jump at the 2-year point where futures end and swaps begin. Discuss why this discontinuity arises and propose at least two methods to produce a smoother forward-rate curve while still fitting all market instruments exactly.

??? success "Solution to Exercise 5"
    **Why the discontinuity arises.**

    The three instrument classes --- deposits, futures, and swaps --- have different tenors, day-count conventions, and convexity properties. At the 2-year boundary:

    - **Futures** (Eurodollar or SOFR futures) are convexity-adjusted forward rates for short (3-month) periods, providing dense information up to 2 years.
    - **Swaps** are par instruments involving multiple cash flows over longer periods. The first swap point at 2 years anchors the curve differently from the last futures contract.

    If the bootstrapping algorithm uses **piecewise-constant forward rates** (a common simple approach), each instrument defines the forward rate in its specific interval. At the boundary where the instrument type changes, the level and slope of the implied forward rate can jump because:

    1. There may be a gap or overlap in maturity coverage.
    2. The convexity adjustment applied to futures introduces a systematic shift relative to the raw FRA rates implied by swaps.
    3. The interpolation method within each segment does not enforce continuity at the junction.

    **Two methods to produce a smoother forward curve:**

    **Method 1: Global spline interpolation.** Instead of bootstrapping segment by segment, fit a **cubic spline** (or similar smooth function) to the **zero rates** or **discount factors** globally, subject to the constraint that all market instruments are repriced exactly. This produces $f(0,T) = -\partial_T \ln P(0,T)$ that is at least continuous (and often $C^1$). Tension splines or monotone-preserving splines can further control oscillations.

    **Method 2: Smoothness penalty (regularized bootstrap).** Add a penalty term to the bootstrapping objective:

    $$
    \min \int_0^{T_{\max}} \bigl(f''(0,T)\bigr)^2\,dT \quad \text{subject to all instruments being repriced exactly}
    $$

    This is equivalent to a **natural cubic spline** on the forward curve. The penalty discourages rapid changes in the slope of $f(0,T)$, eliminating the jump at the 2-year point. The resulting forward curve is smooth and still consistent with market prices.

    Other approaches include using **Nelson--Siegel** or **Svensson** parameterizations, which impose a smooth functional form by construction, or using **monotone convex interpolation** on the discount factors.

---

**Exercise 6.** Consider two candidate discount curves that both reprice all market instruments exactly:

- Curve A uses piecewise-constant forward rates.
- Curve B uses cubic-spline interpolation on zero rates.

For a 10-year Bermudan swaption priced under a short-rate model calibrated to each curve, explain how the choice of interpolation method could affect (a) the shape of $\theta(t)$, (b) the model-implied volatility of forward rates, and (c) the resulting Bermudan swaption price.

??? success "Solution to Exercise 6"
    **(a) Shape of $\theta(t)$:**

    In a short-rate model such as Hull--White, the deterministic shift $\theta(t)$ is determined by the initial forward curve:

    $$
    \theta(t) = \frac{\partial f(0,t)}{\partial t} + a\,f(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
    $$

    - **Curve A (piecewise-constant forwards):** The forward rate $f(0,t)$ is a step function, so $\frac{\partial f}{\partial t}$ is zero almost everywhere except at jump points where it is a sum of Dirac deltas. Consequently, $\theta(t)$ is also piecewise-constant with jumps at each knot point. These discontinuities introduce non-smooth behavior in the model's drift.

    - **Curve B (cubic-spline zero rates):** The forward rate $f(0,t)$ is a smooth function (at least $C^1$), so $\frac{\partial f}{\partial t}$ is continuous. This gives a smooth $\theta(t)$, which produces more natural model dynamics.

    **(b) Model-implied volatility of forward rates:**

    The forward rate volatility in a one-factor model is related to $\sigma$ and $a$ through $\sigma_f(t,T) = \sigma e^{-a(T-t)}$, which does not directly depend on the discount curve. However, the **effective volatility of par swap rates and forward LIBOR rates** depends on the shape of the yield curve through the bond price sensitivities. A jagged $\theta(t)$ (Curve A) can create artificial local volatility features that do not correspond to genuine market dynamics.

    **(c) Bermudan swaption price:**

    A Bermudan swaption involves exercise decisions at multiple dates, which depend on the entire forward curve evolution. The discontinuities in $\theta(t)$ from Curve A can cause:

    - Artificial early exercise incentives near the jump points of $\theta(t)$.
    - Incorrect continuation values due to locally distorted forward rate dynamics.
    - Sensitivity of the option price to the precise placement of knot points.

    Curve B, with its smooth $\theta(t)$, produces more stable and economically sensible Bermudan prices. The difference can be material (several basis points) for long-dated Bermudans, illustrating that the choice of interpolation method is not merely cosmetic --- it directly affects exotic product pricing.

---

**Exercise 7.** Suppose the initial discount curve is perturbed by a parallel shift of $+10$ basis points in all zero rates. For a portfolio consisting of a 5-year receiver swap (notional \$100 million, fixed rate 3.50%, semiannual) priced using the original curve, estimate the change in portfolio value using the first-order approximation

$$
\Delta V \approx -\text{DV01} \times \Delta r
$$

where DV01 is the dollar value of one basis point. Explain why exact curve fitting is critical for obtaining an accurate DV01 estimate.

??? success "Solution to Exercise 7"
    **Setting up the calculation.**

    A 5-year receiver swap pays fixed at $3.50\%$ semiannually on a notional of \$100 million. The DV01 (dollar value of one basis point) measures the sensitivity of the swap's mark-to-market value to a 1 bp parallel shift in the yield curve.

    For a receiver swap (receiving fixed, paying floating), the value is:

    $$
    V = N \cdot s_{\text{fixed}} \cdot A - N \cdot (1 - P(0, T_n))
    $$

    where $A = \sum_{i=1}^{n}\delta_i P(0, T_i)$ is the annuity factor, $s_{\text{fixed}} = 3.50\%$, $N = \$100\text{M}$, and $n = 10$ (semiannual payments over 5 years).

    **DV01 estimation.**

    The DV01 of the swap is approximately equal to the DV01 of the annuity stream, which for a 5-year semiannual swap is roughly the modified duration times the notional divided by 10,000:

    $$
    \text{DV01} \approx N \times \text{Duration}_{\text{mod}} \times 10^{-4}
    $$

    For a 5-year swap, the modified duration is approximately 4.5--4.8 years (depending on the exact yield level). Using a representative value of 4.7:

    $$
    \text{DV01} \approx \$100{,}000{,}000 \times 4.7 \times 10^{-4} = \$47{,}000
    $$

    **Change in value for a +10 bp shift:**

    Since the swap is a receiver (long duration), a rise in rates decreases its value:

    $$
    \Delta V \approx -\text{DV01} \times \Delta r = -\$47{,}000 \times 10 = -\$470{,}000
    $$

    The portfolio loses approximately \$470,000.

    **Why exact curve fitting matters for DV01:**

    The DV01 depends on the accurate computation of all discount factors $P(0, T_i)$. If the initial curve is not fitted exactly:

    1. **Biased annuity factor:** Incorrect discount factors lead to a wrong annuity $A$, and therefore wrong DV01.
    2. **Incorrect hedge ratios:** Since DV01 determines the hedge ratio (e.g., how many bonds or futures to trade), an inaccurate DV01 leads to over- or under-hedging.
    3. **P&L leakage:** Even if the directional bet is correct, the wrong hedge ratio causes unexplained P&L, which accumulates over time.
    4. **Portfolio aggregation errors:** For a large portfolio, DV01 errors compound across positions, potentially leading to materially wrong risk measures.

    Exact curve fitting ensures that the model's sensitivities are consistent with the actual market prices, which is the foundation of accurate risk management.
