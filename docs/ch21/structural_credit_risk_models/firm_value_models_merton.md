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
\text{Assets} = \text{Debt} + \text{Equity}.
$$

### Default Mechanism

Default occurs at maturity $T$ if the firm cannot repay its debt:

$$
\text{Default} \iff V_T < D.
$$

At maturity:
- If $V_T \ge D$: Debt holders receive $D$, equity holders receive $V_T - D$
- If $V_T < D$: Debt holders receive $V_T$, equity holders receive $0$

---

## Asset Value Dynamics

### Risk-Neutral Dynamics

Under the risk-neutral measure $\mathbb{Q}$, the firm's asset value follows geometric Brownian motion:

$$
dV_t = (r - q)V_t \, dt + \sigma_V V_t \, dW_t^{\mathbb{Q}},
$$

where:
- $r$: risk-free interest rate
- $q$: continuous dividend (payout) rate to equity holders
- $\sigma_V$: asset volatility
- $W_t^{\mathbb{Q}}$: standard Brownian motion under $\mathbb{Q}$

### Solution

The asset value at maturity is:

$$
V_T = V_0 \exp\left[\left(r - q - \frac{\sigma_V^2}{2}\right)T + \sigma_V W_T^{\mathbb{Q}}\right].
$$

Under $\mathbb{Q}$, $\ln(V_T/V_0)$ is normally distributed:

$$
\ln\left(\frac{V_T}{V_0}\right) \sim \mathcal{N}\left(\left(r - q - \frac{\sigma_V^2}{2}\right)T, \sigma_V^2 T\right).
$$

---

## Payoff Structure

### Equity as a Call Option

Equity holders have a residual claim:

$$
E_T = (V_T - D)^+ = \max(V_T - D, 0).
$$

This is precisely the payoff of a **European call option** on firm value $V$ with strike $D$.

### Debt as a Portfolio

Debt holders receive:

$$
B_T = \min(V_T, D) = D - (D - V_T)^+.
$$

This can be written as:

$$
B_T = D - \text{Put}(V_T, D),
$$

where the put option represents the loss given default. Equivalently:

$$
B_T = V_T - (V_T - D)^+ = V_T - E_T.
$$

Debt is **risk-free debt minus a put option** on firm value.

---

## Pricing Formulas

### Equity Value (Black-Scholes Call)

Applying the Black-Scholes formula for a call option on $V$:

$$
E_0 = V_0 e^{-qT} N(d_1) - D e^{-rT} N(d_2),
$$

where:

$$
d_1 = \frac{\ln(V_0/D) + (r - q + \sigma_V^2/2)T}{\sigma_V \sqrt{T}}, \quad d_2 = d_1 - \sigma_V \sqrt{T}.
$$

### Debt Value

The value of risky debt is:

$$
B_0 = V_0 - E_0 = V_0\left[1 - e^{-qT} N(d_1)\right] + D e^{-rT} N(d_2).
$$

Alternatively, using the put-call parity interpretation:

$$
B_0 = D e^{-rT} - P_0 = D e^{-rT} - \left[D e^{-rT} N(-d_2) - V_0 e^{-qT} N(-d_1)\right].
$$

Simplifying:

$$
B_0 = V_0 e^{-qT} N(-d_1) + D e^{-rT} N(d_2).
$$

### Risk-Neutral Default Probability

The probability of default under $\mathbb{Q}$ is:

$$
\mathbb{Q}(\tau \le T) = \mathbb{Q}(V_T < D) = N(-d_2).
$$

This is the probability that the asset value ends below the debt threshold.

---

## Credit Spreads

### Yield on Risky Debt

The yield on the risky zero-coupon bond is:

$$
y = -\frac{1}{T} \ln\left(\frac{B_0}{D}\right).
$$

### Credit Spread

The **credit spread** is the excess yield over the risk-free rate:

$$
s = y - r = -\frac{1}{T} \ln\left(\frac{B_0}{D e^{-rT}}\right) = -\frac{1}{T} \ln\left(\frac{B_0}{P(0,T) \cdot D}\right).
$$

### Spread as Function of Leverage and Volatility

Defining **leverage** $L = D e^{-rT}/V_0$ (present value of debt relative to assets), the spread can be expressed as:

$$
s(L, \sigma_V, T) = -\frac{1}{T} \ln\left[N(d_2) + \frac{1}{L} N(-d_1)\right].
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
DD = \frac{\ln(V_0/D) + (\mu - \sigma_V^2/2)T}{\sigma_V \sqrt{T}},
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
s \sim \frac{\sigma_V^2}{2} \cdot \mathbf{1}_{\{V_0 < D\}} + O(T^{1/2}).
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
