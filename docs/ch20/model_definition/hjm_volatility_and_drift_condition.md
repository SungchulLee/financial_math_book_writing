# HJM Volatility Structure and Drift Condition

The Hull-White model is fully characterized within the HJM framework by the choice of forward rate volatility $\sigma_f(t,T) = \sigma e^{-a(T-t)}$. This single specification, combined with the HJM no-arbitrage drift condition, determines the drift of forward rates, the volatility of bond prices, and the covariance structure of the entire yield curve. This section examines the volatility structure in detail, derives its consequences for bond price dynamics, and establishes the variance and covariance formulas that are essential for option pricing.

!!! info "Prerequisites"

    - HJM framework and drift condition (Chapter 19)
    - Derivation of Hull-White from HJM (previous section)
    - Bond price dynamics under the risk-neutral measure
    - Stochastic calculus: Ito's formula, stochastic integration

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the Hull-White forward rate volatility and interpret the exponential decay
    2. Derive the no-arbitrage drift from the HJM condition
    3. Compute the bond price volatility from the forward rate volatility
    4. Calculate the variance and covariance of forward rate changes
    5. Compare the Hull-White volatility with the Ho-Lee and general HJM specifications

---

## The Exponentially Decaying Volatility

The defining feature of the Hull-White model within HJM is its volatility specification.

!!! note "Definition: Hull-White Forward Rate Volatility"
    The instantaneous forward rate volatility in the Hull-White model is

    $$
    \sigma_f(t,T) = \sigma\, e^{-a(T-t)}
    $$

    where $\sigma > 0$ is a constant scaling parameter and $a > 0$ is the mean-reversion speed.

The volatility depends on $t$ and $T$ only through the difference $\tau = T - t$ (time to maturity), making it a function of the "tenor" rather than of calendar time or maturity separately. Key properties:

- **At the short end** ($T = t$): $\sigma_f(t,t) = \sigma$, the short rate volatility
- **Exponential decay**: forward rate volatility decreases as $e^{-a\tau}$ with the time to maturity $\tau$
- **Long maturities** ($T - t \to \infty$): $\sigma_f(t,T) \to 0$, distant forward rates are nearly deterministic
- **Deterministic**: $\sigma_f(t,T)$ does not depend on the current state (forward rates or short rate), which ensures the Gaussian property and analytical tractability

!!! example "Volatility Term Structure"
    With $\sigma = 0.01$ (100 bps annualized) and $a = 0.05$:

    | Time to maturity $\tau$ | $\sigma_f(t,T)$ | Ratio to short rate vol |
    |:---:|:---:|:---:|
    | 0 | 0.0100 | 100% |
    | 5 | 0.0078 | 78% |
    | 10 | 0.0061 | 61% |
    | 20 | 0.0037 | 37% |
    | 30 | 0.0022 | 22% |

    The 30-year forward rate has only 22% of the short rate's volatility, reflecting the strong dampening effect of mean reversion on long-dated rates.

---

## The No-Arbitrage Drift

The HJM drift condition applied to the Hull-White volatility yields the risk-neutral drift of the forward rate.

!!! note "Theorem: HJM Drift Under Hull-White Volatility"
    The no-arbitrage drift of the forward rate is

    $$
    \alpha(t,T) = \sigma_f(t,T) \int_t^T \sigma_f(t,u)\, du = \frac{\sigma^2}{a}\, e^{-a(T-t)}\bigl(1 - e^{-a(T-t)}\bigr)
    $$

???+ note "Proof"
    Compute the integral:

    $$
    \int_t^T \sigma_f(t,u)\, du = \sigma \int_t^T e^{-a(u-t)}\, du = \frac{\sigma}{a}\bigl(1 - e^{-a(T-t)}\bigr)
    $$

    Multiply by $\sigma_f(t,T) = \sigma e^{-a(T-t)}$:

    $$
    \alpha(t,T) = \sigma e^{-a(T-t)} \cdot \frac{\sigma}{a}(1 - e^{-a(T-t)}) = \frac{\sigma^2}{a}\, e^{-a(T-t)}(1 - e^{-a(T-t)})
    $$

    $\square$

The drift $\alpha(t,T)$ has the following properties:

- $\alpha(t,t) = 0$ for all $t$ (the short rate drift does not come from the HJM drift at $T = t$)
- $\alpha(t,T) \geq 0$ for all $T \geq t$ (forward rates drift upward under $\mathbb{Q}$, a manifestation of the convexity correction)
- $\alpha(t,T) \to 0$ as $T - t \to \infty$ (long-dated forward rates have negligible drift)
- Maximum drift occurs at $T - t = \frac{\ln 2}{a}$ (the half-life of mean reversion)

---

## Complete Forward Rate Dynamics

Combining the volatility and drift, the full dynamics are:

$$
df(t,T) = \frac{\sigma^2}{a}\, e^{-a(T-t)}(1 - e^{-a(T-t)})\, dt + \sigma\, e^{-a(T-t)}\, dW_t^{\mathbb{Q}}
$$

Integrating from time $0$ to time $t$:

!!! note "Proposition: Forward Rate at Time $t$"
    The forward rate at time $t$ for maturity $T$ is

    $$
    f(t,T) = f(0,T) + \frac{\sigma^2}{2a^2}\bigl(e^{-a(T-t)} - e^{-aT}\bigr)^2 - \frac{\sigma^2}{2a^2}\bigl(1 - e^{-aT}\bigr)^2 + \frac{\sigma^2}{2a^2}\bigl(1 - e^{-a(T-t)}\bigr)^2 + \sigma \int_0^t e^{-a(T-s)}\, dW_s^{\mathbb{Q}}
    $$

This can be simplified. Writing $B(\tau) = (1 - e^{-a\tau})/a$ for the standard Hull-White function:

$$
f(t,T) = f(0,T) + \frac{\sigma^2}{2}\bigl[B(T-t)^2 - B(T)^2 + (e^{-a(T-t)} - e^{-aT})^2/a^2\bigr] + \sigma \int_0^t e^{-a(T-s)}\, dW_s^{\mathbb{Q}}
$$

---

## Bond Price Volatility

The zero-coupon bond price volatility follows directly from the forward rate volatility through integration.

!!! note "Theorem: Hull-White Bond Price Volatility"
    The zero-coupon bond price $P(t,T)$ satisfies

    $$
    \frac{dP(t,T)}{P(t,T)} = r_t\, dt + \sigma_P(t,T)\, dW_t^{\mathbb{Q}}
    $$

    where the bond price volatility is

    $$
    \sigma_P(t,T) = -\int_t^T \sigma_f(t,u)\, du = -\frac{\sigma}{a}\bigl(1 - e^{-a(T-t)}\bigr) = -\sigma\, B(T-t)
    $$

    with $B(\tau) = (1 - e^{-a\tau})/a$.

???+ note "Proof"
    The relationship between bond prices and forward rates is $P(t,T) = \exp\!\left(-\int_t^T f(t,u)\, du\right)$. Applying Ito's formula:

    $$
    \frac{dP(t,T)}{P(t,T)} = \left[r_t + \frac{1}{2}\left(\int_t^T \sigma_f(t,u)\, du\right)^2\right] dt - \left(\int_t^T \sigma_f(t,u)\, du\right) dW_t^{\mathbb{Q}}
    $$

    Under the risk-neutral measure, the drift must equal $r_t$ (by the fundamental theorem of asset pricing), which is consistent with the HJM drift condition. The diffusion coefficient is

    $$
    \sigma_P(t,T) = -\int_t^T \sigma_f(t,u)\, du = -\sigma \int_t^T e^{-a(u-t)}\, du = -\frac{\sigma}{a}(1 - e^{-a(T-t)})
    $$

    $\square$

The negative sign indicates that bond prices move opposite to interest rates: when $dW > 0$ (rates rise), bond prices fall. The magnitude $|\sigma_P(t,T)| = \sigma B(T-t)$ increases with maturity but saturates at $\sigma/a$ for long maturities, consistent with the bounded duration of mean-reverting rate models.

---

## Variance and Covariance of Forward Rates

The Gaussian structure of the Hull-White model provides explicit formulas for the variance and covariance of forward rate changes.

!!! note "Proposition: Forward Rate Variance"
    The variance of the change in the forward rate over $[0, t]$ is

    $$
    \text{Var}\bigl[f(t,T) - f(0,T)\bigr] = \sigma^2 \int_0^t e^{-2a(T-s)}\, ds = \frac{\sigma^2}{2a}\, e^{-2a(T-t)}\bigl(e^{2at} - 1\bigr)
    $$

    For fixed $t$, this is maximized at $T = t$ (the short rate has the highest variance) and decays as $e^{-2a(T-t)}$ for large $T - t$.

!!! note "Proposition: Forward Rate Covariance"
    For maturities $T_1$ and $T_2$ with $T_1 \leq T_2$, the covariance of forward rate changes over $[0, t]$ is

    $$
    \text{Cov}\bigl[f(t,T_1) - f(0,T_1),\; f(t,T_2) - f(0,T_2)\bigr] = \frac{\sigma^2}{2a}\, e^{-a(T_1 + T_2 - 2t)}\bigl(e^{2at} - 1\bigr)
    $$

???+ note "Proof"
    The forward rate change is $f(t,T) - f(0,T) = \text{(deterministic terms)} + \sigma \int_0^t e^{-a(T-s)}\, dW_s$. The variance of the stochastic part is

    $$
    \text{Var}\bigl[\sigma \int_0^t e^{-a(T-s)}\, dW_s\bigr] = \sigma^2 \int_0^t e^{-2a(T-s)}\, ds = \frac{\sigma^2 e^{-2aT}}{2a}(e^{2at} - 1) = \frac{\sigma^2}{2a} e^{-2a(T-t)}(e^{2at} - 1)
    $$

    For the covariance, by the Ito isometry:

    $$
    \text{Cov} = \sigma^2 \int_0^t e^{-a(T_1 - s)} e^{-a(T_2 - s)}\, ds = \sigma^2 e^{-a(T_1 + T_2)} \int_0^t e^{2as}\, ds = \frac{\sigma^2}{2a} e^{-a(T_1 + T_2 - 2t)}(e^{2at} - 1)
    $$

    $\square$

The **correlation** between forward rate changes at maturities $T_1$ and $T_2$ is

$$
\rho(T_1, T_2) = \frac{\text{Cov}[f(t,T_1) - f(0,T_1),\; f(t,T_2) - f(0,T_2)]}{\sqrt{\text{Var}[f(t,T_1) - f(0,T_1)] \cdot \text{Var}[f(t,T_2) - f(0,T_2)]}} = 1
$$

This perfect correlation is a fundamental limitation of the one-factor Hull-White model: all forward rate movements are driven by a single Brownian motion, so all maturities move in perfect lock-step (up to scaling). The two-factor extension $\sigma_f(t,T) = \sigma_1 e^{-a_1(T-t)} + \sigma_2 e^{-a_2(T-t)}$ resolves this limitation.

---

## Comparison with Other Volatility Structures

| Model | $\sigma_f(t,T)$ | Short Rate Drift | Markov? |
|:---|:---:|:---|:---:|
| Ho-Lee | $\sigma$ (constant) | $\theta(t)\, dt + \sigma\, dW$ | Yes |
| Hull-White | $\sigma e^{-a(T-t)}$ | $[\theta(t) - ar]\, dt + \sigma\, dW$ | Yes |
| General HJM | $\sigma_f(t,T,\omega)$ | Determined by drift condition | Generally no |

The Ho-Lee model is the $a \to 0$ limit of Hull-White, where the volatility is flat across all maturities. In this limit, the bond price volatility $|\sigma_P| = \sigma(T-t)$ grows linearly and is unbounded, leading to the variance of the integrated rate $V(t,T) = \frac{1}{3}\sigma^2(T-t)^3$ (versus the bounded Hull-White formula). The mean-reversion parameter $a$ in the Hull-White volatility thus serves a dual role: it controls the persistence of rate shocks and bounds the effective duration of the model.

---

## The Integrated Volatility

For option pricing, the key quantity is the integrated volatility of the bond price ratio.

!!! note "Proposition: Integrated Bond Price Variance"
    The variance of $\ln(P(T,S)/P(t,S)) - \ln(P(T,T))$ relevant for bond option pricing is

    $$
    \sigma_P^2 = \int_t^T \bigl[\sigma_P(s,S) - \sigma_P(s,T)\bigr]^2\, ds = \frac{\sigma^2}{a^2}(1 - e^{-a(S-T)})^2 \cdot \frac{1 - e^{-2a(T-t)}}{2a}
    $$

???+ note "Proof"
    The difference of bond price volatilities is

    $$
    \sigma_P(s,S) - \sigma_P(s,T) = -\frac{\sigma}{a}(1 - e^{-a(S-s)}) + \frac{\sigma}{a}(1 - e^{-a(T-s)}) = \frac{\sigma}{a}(e^{-a(T-s)} - e^{-a(S-s)})
    $$

    $$
    = \frac{\sigma}{a}\, e^{-a(T-s)}(1 - e^{-a(S-T)})
    $$

    Squaring and integrating:

    $$
    \sigma_P^2 = \frac{\sigma^2}{a^2}(1 - e^{-a(S-T)})^2 \int_t^T e^{-2a(T-s)}\, ds = \frac{\sigma^2}{a^2}(1 - e^{-a(S-T)})^2 \cdot \frac{1 - e^{-2a(T-t)}}{2a}
    $$

    $\square$

This quantity $\sigma_P$ appears directly in the Hull-White zero-coupon bond option formula as the log-normal volatility parameter.

---

## Summary

The Hull-White volatility structure $\sigma_f(t,T) = \sigma e^{-a(T-t)}$ produces an exponentially decaying forward rate volatility that captures the empirical observation that short rates are more volatile than long rates. The HJM drift condition determines $\alpha(t,T) = \frac{\sigma^2}{a} e^{-a(T-t)}(1 - e^{-a(T-t)})$ uniquely, and the bond price volatility is $\sigma_P(t,T) = -\sigma B(T-t)$ with $B(\tau) = (1-e^{-a\tau})/a$. The one-factor structure implies perfect correlation among all forward rates, a limitation addressed by the two-factor extension. The integrated bond price variance $\sigma_P^2$ combines the exponential decay with the variance accumulation formula and enters directly into bond option pricing formulas.

---

## Exercises

**Exercise 1.** For $\sigma = 0.012$ and $a = 0.08$, compute the forward rate volatility $\sigma_f(t,T)$ for time-to-maturity $\tau = 0, 5, 10, 20$ years. At what maturity does the forward rate volatility fall below 50% of the short rate volatility?

??? success "Solution to Exercise 1"
    With $\sigma = 0.012$ and $a = 0.08$, the forward rate volatility is $\sigma_f(t,T) = 0.012\,e^{-0.08\tau}$ where $\tau = T - t$.

    | $\tau$ (years) | $e^{-0.08\tau}$ | $\sigma_f$ | Ratio to $\sigma$ |
    |:---:|:---:|:---:|:---:|
    | 0 | 1.0000 | 0.01200 | 100% |
    | 5 | 0.6703 | 0.00804 | 67.0% |
    | 10 | 0.4493 | 0.00539 | 44.9% |
    | 20 | 0.2019 | 0.00242 | 20.2% |

    To find the maturity where the volatility falls below 50% of the short rate volatility, solve $e^{-0.08\tau} = 0.5$:

    $$
    \tau = \frac{\ln 2}{0.08} = \frac{0.6931}{0.08} \approx 8.66 \text{ years}
    $$

    At approximately 8.66 years to maturity, the forward rate volatility drops below 50% of the short rate volatility. This is the half-life of the volatility decay.

---

**Exercise 2.** Verify that the HJM drift $\alpha(t,T)$ is maximized at $T - t = \frac{\ln 2}{a}$ by differentiating $\alpha(t,T)$ with respect to $T$ and setting it to zero. For $a = 0.05$ and $\sigma = 0.01$, compute the maximum drift in basis points per year.

??? success "Solution to Exercise 2"
    The HJM drift is $\alpha(t,T) = \frac{\sigma^2}{a}e^{-a\tau}(1 - e^{-a\tau})$ where $\tau = T - t$. Differentiate with respect to $T$ (equivalently with respect to $\tau$):

    $$
    \frac{\partial \alpha}{\partial \tau} = \frac{\sigma^2}{a}\left[-a\,e^{-a\tau}(1 - e^{-a\tau}) + e^{-a\tau}\cdot a\,e^{-a\tau}\right]
    $$

    $$
    = \frac{\sigma^2}{a}\cdot a\,e^{-a\tau}\left[-(1 - e^{-a\tau}) + e^{-a\tau}\right] = \sigma^2 e^{-a\tau}(2e^{-a\tau} - 1)
    $$

    Setting $\frac{\partial \alpha}{\partial \tau} = 0$: since $e^{-a\tau} > 0$, we need $2e^{-a\tau} - 1 = 0$, giving $e^{-a\tau} = 1/2$, so

    $$
    \tau^* = \frac{\ln 2}{a}
    $$

    This is the half-life of mean reversion. The second derivative is negative at this point, confirming a maximum.

    For $a = 0.05$ and $\sigma = 0.01$, the maximum occurs at $\tau^* = \ln 2/0.05 \approx 13.86$ years. The maximum drift is

    $$
    \alpha_{\max} = \frac{\sigma^2}{a}\cdot\frac{1}{2}\cdot\left(1 - \frac{1}{2}\right) = \frac{\sigma^2}{4a} = \frac{0.0001}{0.20} = 0.0005
    $$

    In basis points per year: $0.0005 \times 10000 = 5$ bps/year. This is a small drift, consistent with the convexity correction being a second-order effect.

---

**Exercise 3.** Derive the bond price volatility $\sigma_P(t,T) = -\frac{\sigma}{a}(1 - e^{-a(T-t)})$ from the forward rate volatility via $\sigma_P(t,T) = -\int_t^T \sigma_f(t,u)\,du$. Verify the sign and interpret why bond prices move opposite to interest rates.

??? success "Solution to Exercise 3"
    The bond price volatility is

    $$
    \sigma_P(t,T) = -\int_t^T \sigma_f(t,u)\,du = -\int_t^T \sigma\,e^{-a(u-t)}\,du
    $$

    Substituting $v = u - t$:

    $$
    = -\sigma\int_0^{T-t} e^{-av}\,dv = -\sigma\left[-\frac{1}{a}e^{-av}\right]_0^{T-t} = -\frac{\sigma}{a}(1 - e^{-a(T-t)})
    $$

    **Verification of sign:** $\sigma_P(t,T) < 0$ for all $T > t$, since $(1 - e^{-a(T-t)}) > 0$.

    **Interpretation:** The negative sign means that when $dW_t > 0$ (which increases the short rate $r_t$ via $\sigma\,dW_t$ in the Hull-White SDE), the bond price $P(t,T)$ decreases. This is the fundamental inverse relationship between interest rates and bond prices: higher rates imply lower present values, so bond prices fall when rates rise.

    The magnitude $|\sigma_P(t,T)| = \frac{\sigma}{a}(1 - e^{-a(T-t)}) = \sigma\,B(T-t)$ is bounded above by $\sigma/a$. For long maturities, the bond price volatility saturates rather than growing linearly (as it would in the Ho-Lee model where $|\sigma_P| = \sigma(T-t)$). This saturation is a direct consequence of mean reversion: long-dated bond prices are less sensitive to short-rate shocks because the shock mean-reverts away before reaching distant cash flows.

---

**Exercise 4.** Show that the correlation between forward rate changes at maturities $T_1$ and $T_2$ equals 1 in the one-factor Hull-White model. Why is this a limitation for pricing instruments sensitive to yield curve shape, such as CMS spread options?

??? success "Solution to Exercise 4"
    In the one-factor Hull-White model, the forward rate change is

    $$
    f(t,T) - f(0,T) = \text{(deterministic terms)} + \sigma\int_0^t e^{-a(T-s)}\,dW_s
    $$

    The stochastic part for maturity $T_i$ is $I(T_i) = \sigma\int_0^t e^{-a(T_i - s)}\,dW_s$. The covariance is

    $$
    \text{Cov}[I(T_1), I(T_2)] = \sigma^2\int_0^t e^{-a(T_1-s)}e^{-a(T_2-s)}\,ds
    $$

    and the variances are $\text{Var}[I(T_i)] = \sigma^2\int_0^t e^{-2a(T_i-s)}\,ds$. The correlation is

    $$
    \rho = \frac{\sigma^2\int_0^t e^{-a(T_1+T_2-2s)}\,ds}{\sqrt{\sigma^2\int_0^t e^{-2a(T_1-s)}\,ds \cdot \sigma^2\int_0^t e^{-2a(T_2-s)}\,ds}}
    $$

    Notice that $I(T_i) = \sigma e^{-aT_i}\int_0^t e^{as}\,dW_s$. Both $I(T_1)$ and $I(T_2)$ are **scalar multiples** of the same random variable $Z = \int_0^t e^{as}\,dW_s$:

    $$
    I(T_i) = \sigma e^{-aT_i} \cdot Z
    $$

    Since $\sigma e^{-aT_i} > 0$, we have $\rho(T_1, T_2) = 1$ identically for all $T_1, T_2$.

    **Why this is a limitation:** Perfect correlation means all forward rates move in lock-step (up or down together, with magnitudes scaled by $e^{-aT}$). Real yield curves exhibit:

    - Steepening/flattening (short and long rates moving in opposite directions)
    - Butterfly moves (middle maturities moving differently from wings)

    These are impossible in a one-factor model. For instruments like CMS spread options (which pay based on the difference between, say, the 30-year and 2-year swap rates), the one-factor model implies the spread is deterministic up to a scale factor, leading to zero or near-zero option values. In practice, CMS spread options have significant value because the long-short spread is genuinely stochastic, requiring at least a two-factor model.

---

**Exercise 5.** Compute the integrated bond price variance $\sigma_P^2 = \frac{\sigma^2}{a^2}(1 - e^{-a(S-T)})^2 \cdot \frac{1 - e^{-2a(T-t)}}{2a}$ for a bond option with $t = 0$, $T = 5$, $S = 10$, $a = 0.05$, $\sigma = 0.01$. This quantity appears as the volatility parameter in the Black-Scholes-type bond option formula.

??? success "Solution to Exercise 5"
    Using the formula $\sigma_P^2 = \frac{\sigma^2}{a^2}(1 - e^{-a(S-T)})^2 \cdot \frac{1 - e^{-2a(T-t)}}{2a}$ with $t = 0$, $T = 5$, $S = 10$, $a = 0.05$, $\sigma = 0.01$:

    **Step 1:** Compute $(1 - e^{-a(S-T)})$:

    $$
    1 - e^{-0.05 \times 5} = 1 - e^{-0.25} = 1 - 0.7788 = 0.2212
    $$

    **Step 2:** Compute $(1 - e^{-a(S-T)})^2$:

    $$
    (0.2212)^2 = 0.04893
    $$

    **Step 3:** Compute $\frac{1 - e^{-2a(T-t)}}{2a}$:

    $$
    \frac{1 - e^{-2 \times 0.05 \times 5}}{2 \times 0.05} = \frac{1 - e^{-0.5}}{0.1} = \frac{1 - 0.6065}{0.1} = \frac{0.3935}{0.1} = 3.935
    $$

    **Step 4:** Compute $\frac{\sigma^2}{a^2}$:

    $$
    \frac{(0.01)^2}{(0.05)^2} = \frac{0.0001}{0.0025} = 0.04
    $$

    **Step 5:** Combine:

    $$
    \sigma_P^2 = 0.04 \times 0.04893 \times 3.935 = 0.007702
    $$

    $$
    \sigma_P = \sqrt{0.007702} \approx 0.08776
    $$

    This value $\sigma_P \approx 8.78\%$ is the log-normal volatility parameter that enters the Black-Scholes-type formula for pricing a European option on the $P(T,S) = P(5,10)$ zero-coupon bond, with the option expiring at $T = 5$.

---

**Exercise 6.** Compare the Ho-Lee model ($a = 0$) with the Hull-White model in terms of: (i) forward rate volatility term structure, (ii) bond price volatility growth with maturity, and (iii) variance of the integrated short rate $\int_t^T r(s)\,ds$.

??? success "Solution to Exercise 6"
    **(i) Forward rate volatility term structure:**

    - **Ho-Lee** ($a = 0$): $\sigma_f(t,T) = \sigma$ for all $T$. The volatility is flat across all maturities; distant forward rates are just as volatile as the short rate.
    - **Hull-White** ($a > 0$): $\sigma_f(t,T) = \sigma e^{-a(T-t)}$ decays exponentially. Distant forward rates are less volatile, with the ratio $\sigma_f/\sigma = e^{-a\tau}$ controlled by $a$.

    **(ii) Bond price volatility growth with maturity:**

    - **Ho-Lee:** $|\sigma_P(t,T)| = \sigma(T - t)$. The bond price volatility grows linearly without bound. A 100-year bond has 10 times the volatility of a 10-year bond.
    - **Hull-White:** $|\sigma_P(t,T)| = \frac{\sigma}{a}(1 - e^{-a(T-t)})$. The bond price volatility saturates at $\sigma/a$ for long maturities. This is consistent with the observation that very long-dated bond sensitivities do not grow proportionally with maturity when rates are mean-reverting.

    **(iii) Variance of the integrated short rate $\int_t^T r(s)\,ds$:**

    - **Ho-Lee:** $\text{Var}\left[\int_t^T r(s)\,ds\right] = \frac{\sigma^2(T-t)^3}{3}$. The variance grows cubically with the horizon, reflecting the lack of mean reversion. This leads to increasingly unreliable long-horizon bond prices and makes the model unsuitable for long-dated instruments.
    - **Hull-White:** $\text{Var}\left[\int_t^T r(s)\,ds\right] = \frac{\sigma^2}{a^2}\left[(T-t) - \frac{2}{a}(1 - e^{-a(T-t)}) + \frac{1}{2a}(1 - e^{-2a(T-t)})\right]$. For large $T-t$, this grows linearly as $\frac{\sigma^2}{a^2}(T-t)$, which is much slower than the cubic growth of Ho-Lee. Mean reversion bounds the effective duration, keeping the integrated variance manageable for long-dated instruments.

---

**Exercise 7.** Explain how the two-factor volatility specification $\sigma_f(t,T) = \sigma_1 e^{-a_1(T-t)} + \sigma_2 e^{-a_2(T-t)}$ breaks the perfect correlation between forward rates. Compute the correlation between the 1-year and 10-year forward rate changes for $\sigma_1 = 0.008$, $a_1 = 0.02$, $\sigma_2 = 0.005$, $a_2 = 0.30$.

??? success "Solution to Exercise 7"
    **How two factors break perfect correlation:**

    In the two-factor model, forward rate changes are driven by two independent Brownian motions $W_1$ and $W_2$:

    $$
    df(t,T) = \alpha(t,T)\,dt + \sigma_1 e^{-a_1(T-t)}\,dW_{1,t} + \sigma_2 e^{-a_2(T-t)}\,dW_{2,t}
    $$

    The stochastic part of the forward rate change at maturity $T$ is a vector in the span of $dW_1$ and $dW_2$. The "direction" of this vector depends on $T$ through the ratio $\sigma_1 e^{-a_1(T-t)} : \sigma_2 e^{-a_2(T-t)}$, which changes with $T$. Since the two exponentials decay at different rates ($a_1 \neq a_2$), short-maturity forward rates have a different mix of $W_1$ and $W_2$ exposure than long-maturity forward rates, producing imperfect correlation.

    **Correlation computation:** The variance of the forward rate change at maturity $T$ (over $[0,t]$) is

    $$
    V(T) = \sigma_1^2\int_0^t e^{-2a_1(T-s)}\,ds + \sigma_2^2\int_0^t e^{-2a_2(T-s)}\,ds
    $$

    and the covariance between maturities $T_1$ and $T_2$ is

    $$
    C(T_1,T_2) = \sigma_1^2\int_0^t e^{-a_1(T_1-s)}e^{-a_1(T_2-s)}\,ds + \sigma_2^2\int_0^t e^{-a_2(T_1-s)}e^{-a_2(T_2-s)}\,ds
    $$

    For large $t$ (stationary limit), the integrals evaluate to:

    $$
    V(T) \to \frac{\sigma_1^2}{2a_1} + \frac{\sigma_2^2}{2a_2}, \qquad C(T_1,T_2) \to \frac{\sigma_1^2}{2a_1}e^{-a_1|T_1-T_2|} + \frac{\sigma_2^2}{2a_2}e^{-a_2|T_1-T_2|}
    $$

    With $\sigma_1 = 0.008$, $a_1 = 0.02$, $\sigma_2 = 0.005$, $a_2 = 0.30$, $T_1 = 1$, $T_2 = 10$ ($|T_1 - T_2| = 9$):

    $$
    V(T_i) = \frac{0.000064}{0.04} + \frac{0.000025}{0.60} = 0.001600 + 0.0000417 = 0.001642
    $$

    $$
    C(1,10) = \frac{0.000064}{0.04}e^{-0.02 \times 9} + \frac{0.000025}{0.60}e^{-0.30 \times 9}
    $$

    $$
    = 0.001600 \times e^{-0.18} + 0.0000417 \times e^{-2.7}
    $$

    $$
    = 0.001600 \times 0.8353 + 0.0000417 \times 0.06721
    $$

    $$
    = 0.001337 + 0.00000280 = 0.001340
    $$

    $$
    \rho(1,10) = \frac{C(1,10)}{\sqrt{V(1)\cdot V(10)}} = \frac{0.001340}{0.001642} \approx 0.816
    $$

    The correlation is approximately $0.82$, substantially below the perfect correlation of 1.0 in the one-factor model. The fast-decaying factor ($a_2 = 0.30$) creates idiosyncratic short-rate volatility that does not propagate to long maturities, decorrelating short and long forward rates.
