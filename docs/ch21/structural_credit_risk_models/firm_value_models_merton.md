# Firm Value Models (Merton)

Structural credit risk models view default as an economic event driven by the firm's asset value. The **Merton model** (1974) is the foundational framework in this class, interpreting equity and debt as contingent claims on firm value. This approach provides a unified treatment of equity and credit markets with strong economic intuition.

---

## Basic Economic Framework

### The Firm's Balance Sheet

Consider a firm with:

- **Assets:** Total value $V_t$ at time $t$
- **Liabilities:** A single zero-coupon debt with face value $D$ maturing at time $T$
- **Equity:** Residual claim after debt repayment

The fundamental accounting identity is:

$$
\text{Assets} = \text{Debt} + \text{Equity}
$$

### Default Mechanism

Default occurs at maturity $T$ if the firm cannot repay its debt:

$$
\text{Default} \iff V_T < D
$$

At maturity:

- If $V_T \ge D$: Debt holders receive $D$, equity holders receive $V_T - D$
- If $V_T < D$: Debt holders receive $V_T$, equity holders receive $0$

---

## Asset Value Dynamics

### Risk-Neutral Dynamics

Recall (see [GBM under $\mathbb{Q}$](../../ch06/black_scholes_model/introduction.md) and [risk-neutral measure](../../ch04/risk_neutral/martingale_and_no_arbitrage.md)). Under $\mathbb{Q}$, the firm's asset value follows geometric Brownian motion:

$$
dV_t = (r - q)V_t \, dt + \sigma_V V_t \, dW_t^{\mathbb{Q}}
$$

with $r$ the risk-free rate, $q$ the payout rate, $\sigma_V$ the asset volatility. The terminal log-asset is normal:

$$
\ln(V_T/V_0) \sim \mathcal{N}\!\left((r - q - \sigma_V^2/2)T, \sigma_V^2 T\right).
$$

---

## Payoff Structure

### Equity as a Call Option

Equity holders have a residual claim:

$$
E_T = (V_T - D)^+ = \max(V_T - D, 0)
$$

This is precisely the payoff of a **European call option** on firm value $V$ with strike $D$.

### Debt as a Portfolio

Debt holders receive:

$$
B_T = \min(V_T, D) = D - (D - V_T)^+
$$

This can be written as:

$$
B_T = D - \text{Put}(V_T, D)
$$

where the put option represents the loss given default. Equivalently:

$$
B_T = V_T - (V_T - D)^+ = V_T - E_T
$$

Debt is **risk-free debt minus a put option** on firm value.

---

## Pricing Formulas

### Equity Value (Black-Scholes Call)

Recall (see [Black-Scholes formula](../../ch06/black_scholes_formula/bs_formula_statement.md)). Equity is a call on $V$ with strike $D$:

$$
E_0 = V_0 e^{-qT} N(d_1) - D e^{-rT} N(d_2),
$$

$$
d_1 = \frac{\ln(V_0/D) + (r - q + \sigma_V^2/2)T}{\sigma_V \sqrt{T}}, \quad d_2 = d_1 - \sigma_V \sqrt{T}.
$$

### Debt Value

The value of risky debt is:

$$
B_0 = V_0 - E_0 = V_0\left[1 - e^{-qT} N(d_1)\right] + D e^{-rT} N(d_2)
$$

Alternatively, using the put-call parity interpretation:

$$
B_0 = D e^{-rT} - P_0 = D e^{-rT} - \left[D e^{-rT} N(-d_2) - V_0 e^{-qT} N(-d_1)\right]
$$

Simplifying:

$$
B_0 = V_0 e^{-qT} N(-d_1) + D e^{-rT} N(d_2)
$$

### Risk-Neutral Default Probability

The probability of default under $\mathbb{Q}$ is:

$$
\mathbb{Q}(\tau \le T) = \mathbb{Q}(V_T < D) = N(-d_2)
$$

This is the probability that the asset value ends below the debt threshold.

---

## Credit Spreads

### Yield on Risky Debt

The yield on the risky zero-coupon bond is:

$$
y = -\frac{1}{T} \ln\left(\frac{B_0}{D}\right)
$$

### Credit Spread

The **credit spread** is the excess yield over the risk-free rate:

$$
s = y - r = -\frac{1}{T} \ln\left(\frac{B_0}{D e^{-rT}}\right) = -\frac{1}{T} \ln\left(\frac{B_0}{P(0,T) \cdot D}\right)
$$

### Spread as Function of Leverage and Volatility

Defining **leverage** $L = D e^{-rT}/V_0$ (present value of debt relative to assets), the spread can be expressed as:

$$
s(L, \sigma_V, T) = -\frac{1}{T} \ln\left[N(d_2) + \frac{1}{L} N(-d_1)\right]
$$

Key properties:

- $s \to 0$ as $L \to 0$ (low leverage)
- $s \to \infty$ as $L \to 1$ from below (high leverage approaching default)
- $s$ increases in $\sigma_V$ (higher asset volatility increases default risk)
- Term structure of spreads depends on the interplay of $L$, $\sigma_V$, and $T$

---

## Distance to Default

A key metric from the Merton model is the **distance to default** (DD):

$$
DD = \frac{\ln(V_0/D) + (\mu - \sigma_V^2/2)T}{\sigma_V \sqrt{T}}
$$

where $\mu$ is the physical (real-world) drift of asset value.

**Interpretation:** DD measures how many standard deviations the asset value is from the default threshold, normalized by the diffusion over the time horizon.

- Higher DD $\implies$ lower default probability
- DD is approximately the negative of the $z$-score for default
- Physical default probability: $\mathbb{P}(\tau \le T) \approx N(-DD)$

The distance to default is widely used in practice (e.g., Moody's KMV model) as a credit risk indicator.

---

## Model Limitations

### Underestimation of Short-Term Spreads

The Merton model significantly underestimates credit spreads for short maturities. As $T \to 0$:

$$
s \sim \frac{\sigma_V^2}{2} \cdot \mathbf{1}_{\{V_0 < D\}} + O(T^{1/2})
$$

For $V_0 > D$, spreads vanish too quickly. Empirically, even high-quality bonds have non-trivial short-term spreads.

### Default Only at Maturity

Default can only occur at time $T$, not before. This ignores:

- Covenant violations
- Cash flow crises
- Strategic default
- Regulatory intervention

### Unobservable Asset Value

$V_0$ and $\sigma_V$ are not directly observable. They must be inferred from:

- Equity prices and volatility
- Balance sheet data
- Calibration procedures

### Constant Volatility and Interest Rates

The model assumes constant $\sigma_V$ and $r$, while in reality:

- Asset volatility is stochastic and may jump
- Interest rates vary over time
- Correlation between rates and firm value matters

---

## Calibration: Inferring Asset Parameters

### Two-Equation System

Given observable equity value $E_0$ and equity volatility $\sigma_E$, solve for $(V_0, \sigma_V)$:

**Equation 1 (Price):**

$$
E_0 = V_0 e^{-qT} N(d_1) - D e^{-rT} N(d_2)
$$

**Equation 2 (Volatility via Itô's Lemma):**

$$
\sigma_E = \frac{\partial E}{\partial V} \cdot \frac{V_0}{E_0} \cdot \sigma_V = \frac{V_0 e^{-qT} N(d_1)}{E_0} \cdot \sigma_V
$$

This is a system of two nonlinear equations in two unknowns $(V_0, \sigma_V)$.

### Iterative Solution

1. Initialize: $V_0^{(0)} = E_0 + D e^{-rT}$
2. Compute $\sigma_V^{(k)}$ from the volatility equation given $V_0^{(k)}$
3. Update $V_0^{(k+1)}$ from the price equation given $\sigma_V^{(k)}$
4. Iterate until convergence

---

## Numerical Example

**Parameters:**

- Asset value: $V_0 = 100$
- Face value of debt: $D = 80$
- Risk-free rate: $r = 5\%$
- Asset volatility: $\sigma_V = 20\%$
- Time to maturity: $T = 1$ year
- Dividend rate: $q = 0$

**Calculations:**

$$
d_1 = \frac{\ln(100/80) + (0.05 + 0.04/2) \cdot 1}{0.20 \cdot 1} = \frac{0.2231 + 0.07}{0.20} = 1.466
$$

$$
d_2 = 1.466 - 0.20 = 1.266
$$

$$
N(d_1) = N(1.466) = 0.9286, \quad N(d_2) = N(1.266) = 0.8972
$$

**Equity value:**

$$
E_0 = 100 \times 0.9286 - 80 \times e^{-0.05} \times 0.8972 = 92.86 - 68.28 = 24.58
$$

**Debt value:**

$$
B_0 = V_0 - E_0 = 100 - 24.58 = 75.42
$$

**Risk-neutral default probability:**

$$
\mathbb{Q}(\text{default}) = N(-d_2) = N(-1.266) = 0.1028 \approx 10.3\%
$$

**Credit spread:**

$$
y = -\frac{1}{1} \ln\left(\frac{75.42}{80}\right) = 0.0590 = 5.90\%
$$

$$
s = y - r = 5.90\% - 5.00\% = 0.90\% = 90 \text{ bp}
$$

---

## Key Takeaways

- The Merton model interprets equity as a call option and debt as risk-free debt minus a put
- Default occurs when asset value falls below debt at maturity
- Credit spreads are determined by leverage, asset volatility, and time to maturity
- The distance to default (DD) is a key credit risk metric
- The model provides an explicit equity-credit link but underestimates short-term spreads
- Calibration requires solving for unobservable asset value and volatility

---

## Further Reading

- Merton, R. C. (1974). On the pricing of corporate debt: The risk structure of interest rates. *Journal of Finance*, 29(2), 449–470.
- Black, F., & Scholes, M. (1973). The pricing of options and corporate liabilities. *Journal of Political Economy*, 81(3), 637–654.
- Leland, H. E. (1994). Corporate debt value, bond covenants, and optimal capital structure. *Journal of Finance*, 49(4), 1213–1252.
- Crosbie, P., & Bohn, J. (2003). Modeling default risk. *Moody's KMV Technical Document*.

---

## Exercises

**Exercise 1.** A firm has current asset value $V_0 = 100$, debt face value $D = 70$, asset volatility $\sigma_V = 25\%$, risk-free rate $r = 4\%$, and debt maturity $T = 5$. Compute $d_1$ and $d_2$ and find the risk-neutral default probability $\mathbb{Q}(\tau \le T) = N(-d_2)$. Also compute the equity value $E_0 = V_0\,N(d_1) - De^{-rT}\,N(d_2)$.

??? success "Solution to Exercise 1"
    **Given:** $V_0 = 100$, $D = 70$, $\sigma_V = 0.25$, $r = 0.04$, $T = 5$, $q = 0$.

    **Step 1: Compute $d_1$ and $d_2$.**

    $$
    d_1 = \frac{\ln(V_0/D) + (r + \sigma_V^2/2)T}{\sigma_V \sqrt{T}} = \frac{\ln(100/70) + (0.04 + 0.03125) \times 5}{0.25\sqrt{5}}
    $$

    Numerator: $\ln(100/70) = \ln(1.4286) = 0.3567$. Then $(0.04 + 0.03125) \times 5 = 0.07125 \times 5 = 0.35625$.

    $$
    d_1 = \frac{0.3567 + 0.35625}{0.25 \times 2.2361} = \frac{0.71295}{0.55902} = 1.2753
    $$

    $$
    d_2 = d_1 - \sigma_V \sqrt{T} = 1.2753 - 0.55902 = 0.7163
    $$

    **Step 2: Risk-neutral default probability.**

    $$
    \mathbb{Q}(\tau \le T) = N(-d_2) = N(-0.7163) = 0.2369 \approx 23.7\%
    $$

    **Step 3: Equity value.**

    $$
    N(d_1) = N(1.2753) = 0.8989, \quad N(d_2) = N(0.7163) = 0.7631
    $$

    $$
    E_0 = V_0 N(d_1) - D e^{-rT} N(d_2) = 100 \times 0.8989 - 70 \times e^{-0.20} \times 0.7631
    $$

    $$
    = 89.89 - 70 \times 0.8187 \times 0.7631 = 89.89 - 43.73 = 46.16
    $$

    **Summary:** $d_1 = 1.275$, $d_2 = 0.716$, default probability $\approx 23.7\%$, equity value $\approx \$46.16$.

---

**Exercise 2.** In the Merton model, equity is a call option on firm value with strike $D$. Using put-call parity, show that the value of risky debt can be written as $D_0 = V_0 - E_0 = De^{-rT} - \text{Put}(V_0, D, T)$, where Put is a European put on $V_t$ with strike $D$. Interpret this economically.

??? success "Solution to Exercise 2"
    **Goal:** Show $B_0 = V_0 - E_0 = De^{-rT} - \text{Put}(V_0, D, T)$ using put-call parity.

    **Step 1: Recall the payoffs at maturity.**

    Equity holders receive:

    $$
    E_T = (V_T - D)^+ = \max(V_T - D, 0) \quad \text{(call payoff)}
    $$

    Debt holders receive:

    $$
    B_T = \min(V_T, D) = V_T - (V_T - D)^+ = V_T - E_T
    $$

    **Step 2: Alternative representation of $B_T$.**

    We can write:

    $$
    B_T = D - (D - V_T)^+ = D - \text{Put payoff}
    $$

    This is verified by cases:

    - If $V_T \ge D$: $B_T = D$, and $D - 0 = D$. Correct.
    - If $V_T < D$: $B_T = V_T$, and $D - (D - V_T) = V_T$. Correct.

    **Step 3: Discounting to $t = 0$.**

    Taking risk-neutral expectations:

    $$
    B_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT} B_T] = De^{-rT} - \mathbb{E}^{\mathbb{Q}}[e^{-rT}(D - V_T)^+] = De^{-rT} - P_0
    $$

    where $P_0$ is the Black-Scholes put price on $V$ with strike $D$.

    **Step 4: Verify via put-call parity.**

    Put-call parity states $C_0 - P_0 = V_0 - De^{-rT}$, so $P_0 = C_0 - V_0 + De^{-rT} = E_0 - V_0 + De^{-rT}$.

    Substituting:

    $$
    B_0 = De^{-rT} - (E_0 - V_0 + De^{-rT}) = V_0 - E_0
    $$

    This confirms the balance sheet identity $V_0 = E_0 + B_0$.

    **Economic interpretation:** Risky debt equals risk-free debt minus a put option on firm value. The put represents the **credit risk** component: it is the expected discounted loss that debt holders bear in the event of default. The put premium is the cost of bearing default risk. When leverage is high or asset volatility is large, the put value increases, reducing the risky debt value and widening credit spreads.

---

**Exercise 3.** Compute the physical default probability in the Merton model using $\mathbb{P}(\tau \le T) = N(-DD)$ where the distance to default is

$$
DD = \frac{\ln(V_0/D) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}
$$

Use the parameters from Exercise 1 with asset drift $\mu = 10\%$. Compare with the risk-neutral default probability from Exercise 1 and explain why they differ.

??? success "Solution to Exercise 3"
    **Given:** Same parameters as Exercise 1 ($V_0 = 100$, $D = 70$, $\sigma_V = 0.25$, $T = 5$) plus physical drift $\mu = 0.10$.

    **Step 1: Compute the distance to default.**

    $$
    DD = \frac{\ln(V_0/D) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}} = \frac{\ln(100/70) + (0.10 - 0.03125) \times 5}{0.25\sqrt{5}}
    $$

    Numerator: $0.3567 + 0.06875 \times 5 = 0.3567 + 0.34375 = 0.70045$.

    $$
    DD = \frac{0.70045}{0.55902} = 1.2530
    $$

    **Step 2: Physical default probability.**

    $$
    \mathbb{P}(\tau \le T) = N(-DD) = N(-1.2530) = 0.1051 \approx 10.5\%
    $$

    **Step 3: Comparison with risk-neutral default probability.**

    From Exercise 1, $\mathbb{Q}(\tau \le T) = N(-d_2) = N(-0.7163) \approx 23.7\%$.

    The risk-neutral default probability ($23.7\%$) is significantly higher than the physical default probability ($10.5\%$).

    **Why they differ:** The two probabilities are computed under different measures:

    - The **physical measure** $\mathbb{P}$ uses the actual asset drift $\mu = 10\%$, which reflects the expected return investors require for bearing asset risk.
    - The **risk-neutral measure** $\mathbb{Q}$ replaces $\mu$ with the risk-free rate $r = 4\%$, removing the equity risk premium.

    Under $\mathbb{Q}$, the asset drifts at a lower rate ($r = 4\%$ instead of $\mu = 10\%$), making it more likely to end below $D$. The difference $\mu - r = 6\%$ represents the market price of risk. Risk-neutral probabilities are higher because they incorporate a **risk premium**: investors demand compensation for default risk, which inflates the risk-neutral probability above the actuarial one. This is exactly analogous to the fact that risk-neutral probabilities in option pricing are not forecasts of future outcomes but rather pricing weights.

---

**Exercise 4.** The Merton model credit spread is $s(T) = -\frac{1}{T}\ln[N(d_2) + \frac{1}{L}N(-d_1)]$ where $L = De^{-rT}/V_0$. Compute $s(T)$ for $T = 1, 3, 5, 10$ years using the parameters from Exercise 1. Describe the shape of the resulting spread curve and explain why it vanishes at short maturities.

??? success "Solution to Exercise 4"
    **Given:** $V_0 = 100$, $D = 70$, $\sigma_V = 0.25$, $r = 0.04$, $q = 0$. Compute spreads for $T = 1, 3, 5, 10$.

    The credit spread formula is:

    $$
    s(T) = -\frac{1}{T}\ln\left[N(d_2) + \frac{1}{L}N(-d_1)\right]
    $$

    where $L = De^{-rT}/V_0$.

    **For $T = 1$:**

    $L = 70e^{-0.04}/100 = 0.6726$.

    $$
    d_1 = \frac{\ln(100/70) + (0.04 + 0.03125) \times 1}{0.25} = \frac{0.3567 + 0.07125}{0.25} = 1.7118
    $$

    $$
    d_2 = 1.7118 - 0.25 = 1.4618
    $$

    $N(d_2) = 0.9281$, $N(-d_1) = 0.0434$.

    $$
    s(1) = -\ln\left[0.9281 + \frac{0.0434}{0.6726}\right] = -\ln[0.9281 + 0.0645] = -\ln[0.9926] = 0.0074 = 0.74\%
    $$

    Wait -- let me recompute more carefully. Actually $s(T) = -\frac{1}{T}\ln[\cdot]$ so:

    $$
    s(1) = -\frac{1}{1}\ln[0.9926] \approx 0.0074 = 0.74\% = 74 \text{ bp}
    $$

    **For $T = 3$:**

    $L = 70e^{-0.12}/100 = 0.6208$.

    $$
    d_1 = \frac{0.3567 + 0.07125 \times 3}{0.25\sqrt{3}} = \frac{0.3567 + 0.21375}{0.4330} = \frac{0.57045}{0.4330} = 1.3175
    $$

    $$
    d_2 = 1.3175 - 0.4330 = 0.8845
    $$

    $N(d_2) = 0.8117$, $N(-d_1) = 0.0938$.

    $$
    s(3) = -\frac{1}{3}\ln\left[0.8117 + \frac{0.0938}{0.6208}\right] = -\frac{1}{3}\ln[0.8117 + 0.1511] = -\frac{1}{3}\ln[0.9628]
    $$

    $$
    = -\frac{1}{3}(-0.0379) = 0.0126 = 1.26\% = 126 \text{ bp}
    $$

    **For $T = 5$:**

    From Exercise 1: $L = 70e^{-0.20}/100 = 0.5731$, $d_1 = 1.2753$, $d_2 = 0.7163$.

    $N(d_2) = 0.7631$, $N(-d_1) = 0.1011$.

    $$
    s(5) = -\frac{1}{5}\ln\left[0.7631 + \frac{0.1011}{0.5731}\right] = -\frac{1}{5}\ln[0.7631 + 0.1764] = -\frac{1}{5}\ln[0.9395]
    $$

    $$
    = -\frac{1}{5}(-0.0624) = 0.0125 = 1.25\% = 125 \text{ bp}
    $$

    **For $T = 10$:**

    $L = 70e^{-0.40}/100 = 0.4689$.

    $$
    d_1 = \frac{0.3567 + 0.07125 \times 10}{0.25\sqrt{10}} = \frac{0.3567 + 0.7125}{0.7906} = \frac{1.0692}{0.7906} = 1.3524
    $$

    $$
    d_2 = 1.3524 - 0.7906 = 0.5618
    $$

    $N(d_2) = 0.7129$, $N(-d_1) = 0.0882$.

    $$
    s(10) = -\frac{1}{10}\ln\left[0.7129 + \frac{0.0882}{0.4689}\right] = -\frac{1}{10}\ln[0.7129 + 0.1881] = -\frac{1}{10}\ln[0.9010]
    $$

    $$
    = -\frac{1}{10}(-0.1043) = 0.0104 = 1.04\% = 104 \text{ bp}
    $$

    **Summary:**

    | $T$ | $s(T)$ (bp) |
    |-----|-------------|
    | 1   | 74          |
    | 3   | 126         |
    | 5   | 125         |
    | 10  | 104         |

    **Shape of the spread curve:** The spread curve is **hump-shaped**. It rises steeply from short maturities to a peak around $T = 3$--$5$ years, then gradually declines for longer maturities.

    **Why it vanishes at short maturities:** In the Merton model (default only at maturity), the asset price follows a continuous diffusion. For very short horizons $T \to 0$ with $V_0 > D$, the probability that a continuous Brownian path moves from $\ln(V_0/D) > 0$ to below zero in a vanishingly small time interval is negligible -- it decays faster than any power of $T$. Specifically, $N(-d_2) \sim e^{-d_2^2/2}$ where $d_2 \sim 1/\sqrt{T} \to \infty$, so the default probability and hence the spread approach zero exponentially fast. This is a well-known limitation of the Merton model that is addressed by first-passage models (e.g., Black-Cox).

---

**Exercise 5.** Explain three major limitations of the Merton model: (a) default only at maturity, (b) single debt class, (c) unobservable firm value. For each limitation, describe a model extension that addresses it (e.g., Black-Cox for (a), KMV for (c)).

??? success "Solution to Exercise 5"
    **(a) Default only at maturity.**

    In the Merton model, default is triggered exclusively at debt maturity $T$ when $V_T < D$. This ignores the possibility that a firm may become insolvent at intermediate dates due to cash-flow shortfalls, covenant violations, or creditor actions. In reality, a firm whose asset value drops well below its liabilities at time $t < T$ would almost certainly be forced into bankruptcy -- it would not continue operating until maturity.

    **Extension: The Black-Cox model** introduces a default barrier $B_t$ such that default occurs at the first time $\tau = \inf\{t : V_t \le B_t\}$. This allows for early default via first passage, producing more realistic short-term credit spreads and richer term structure shapes (hump-shaped or downward-sloping curves). The model can also incorporate time-dependent barriers $B_t = Ke^{\gamma t}$ to reflect evolving covenant requirements.

    **(b) Single debt class.**

    The Merton model assumes a single zero-coupon debt instrument with face value $D$ and maturity $T$. Real firms have complex capital structures with senior and subordinated debt, revolving credit facilities, convertible bonds, and various covenants. The single-class assumption ignores priority rules, cross-default clauses, and the interaction between different creditor classes.

    **Extension: Multi-class structural models** (e.g., Geske's compound option model, 1977) treat junior debt as a compound option -- an option on the equity, which is itself an option on firm value. Leland and Toft (1996) model firms with a stationary debt structure of continuously maturing bonds. These approaches capture subordination, seniority, and the effects of complex capital structures on credit risk.

    **(c) Unobservable firm value.**

    The firm's total asset value $V_0$ and asset volatility $\sigma_V$ are not directly tradable or observable quantities. They must be inferred from equity market data, which introduces estimation error. Small errors in $(V_0, \sigma_V)$ can lead to large errors in credit spreads, particularly for short maturities.

    **Extension: The KMV (Moody's Analytics) approach** addresses this by developing a systematic calibration methodology: (i) solve the two-equation system linking equity value and equity volatility to $(V_0, \sigma_V)$, (ii) compute the distance to default (DD) using the calibrated asset parameters, and (iii) map DD to expected default frequencies (EDF) using a proprietary empirical database rather than relying on the theoretical normal distribution. This hybrid structural-empirical approach significantly improves default prediction accuracy.

---

**Exercise 6.** A firm's equity value increases from $E_0 = 30$ to $E_1 = 45$ over one year. If asset volatility $\sigma_V$ and debt $D$ remain constant, explain qualitatively how the firm's default probability, credit spread, and distance to default change. What leverage ratio measure is most relevant?

??? success "Solution to Exercise 6"
    **Setting:** A firm's equity increases from $E_0 = 30$ to $E_1 = 45$ (a 50% increase) over one year, with $\sigma_V$ and $D$ held constant.

    **What happens to firm value:** Since equity is a call option on firm value, an increase in equity implies an increase in the underlying asset value $V$. From $E = V N(d_1) - De^{-rT}N(d_2)$, a rise in $E$ with fixed $D$ and $\sigma_V$ requires $V$ to increase. If $D = 70$ and initially $V_0 \approx 100$, the new asset value $V_1$ must be higher (approximately $V_1 \approx 115$, depending on exact parameters).

    **Default probability decreases.** The risk-neutral default probability is $\mathbb{Q}(\text{default}) = N(-d_2)$. As $V$ increases with $D$ constant:

    $$
    d_2 = \frac{\ln(V/D) + (r - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}
    $$

    The numerator increases (larger $\ln(V/D)$), so $d_2$ increases, $-d_2$ decreases, and $N(-d_2)$ decreases. The firm is further from the default boundary.

    **Credit spread decreases.** Since $s = -\frac{1}{T}\ln[N(d_2) + \frac{1}{L}N(-d_1)]$ and the leverage ratio $L = De^{-rT}/V$ decreases (denominator increases), the argument of the logarithm moves closer to 1, reducing the spread. Intuitively, the firm has more assets backing its debt, so creditors face less risk.

    **Distance to default increases.** The DD under the physical measure is:

    $$
    DD = \frac{\ln(V/D) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}
    $$

    Higher $V$ directly increases $\ln(V/D)$, pushing DD further into positive territory. The firm has moved further from the default boundary measured in standard deviations.

    **Most relevant leverage measure:** The most relevant leverage ratio is the **market-value leverage** $L = De^{-rT}/V_0$, which compares the present value of debt obligations to the current market value of assets. Book leverage (debt/book assets) does not capture the market's real-time assessment of firm health. In the Merton framework, $L$ directly enters the credit spread formula and determines the default probability. As $V$ increases with $D$ fixed, $L$ decreases from $De^{-rT}/100$ to $De^{-rT}/V_1$, reflecting the improved creditworthiness that drives all three changes above.
