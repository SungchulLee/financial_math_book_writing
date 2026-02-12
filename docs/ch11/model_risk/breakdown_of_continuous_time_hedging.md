# Breakdown of Continuous-Time Hedging


Replication assumes continuous trading, no costs, continuous paths, and correct model. Jumps, discrete trading, and model error break replication.

---

## The Black–Scholes assumptions


The Black–Scholes hedging argument requires:

1. **Continuous trading**: Rebalance at every instant
2. **No transaction costs**: Frictionless markets
3. **Continuous paths**: No jumps in the underlying
4. **Known volatility**: \(\sigma\) is constant and observable
5. **No arbitrage**: Risk-free borrowing/lending at rate \(r\)

Violation of any assumption breaks perfect replication.

---

## Jump risk: quantitative analysis


Consider a jump-diffusion model:

\[
\frac{dS_t}{S_{t^-}} = \mu \, dt + \sigma \, dW_t + J \, dN_t
\]

where \(N_t\) is a Poisson process with intensity \(\lambda_J\) and \(J\) is the jump size.

**Delta hedging error from a jump.** When a jump of size \(J\) occurs:

\[
\text{Option P&L} = V(t, S(1+J)) - V(t, S)
\]
\[
\text{Hedge P&L} = \Delta \cdot S \cdot J
\]

The hedging error is:

\[
\epsilon_{\text{jump}} = V(t, S(1+J)) - V(t, S) - \Delta \cdot S \cdot J
\]

By Taylor expansion:

\[
\boxed{\epsilon_{\text{jump}} \approx \frac{1}{2}\Gamma S^2 J^2 + \frac{1}{6}\text{Speed} \cdot S^3 J^3 + \cdots}
\]

**Key insight:** Jump hedging error is quadratic in jump size (like gamma P&L from diffusion), but occurs discretely and unpredictably.

---

## Expected hedging error from jumps


For a Poisson process with intensity \(\lambda_J\) and i.i.d. jump sizes with \(\mathbb{E}[J^2] = \sigma_J^2\):

\[
\mathbb{E}[\text{Jump Hedging Error}] \approx \frac{1}{2}\lambda_J \int_0^T \Gamma(t, S_t) S_t^2 \sigma_J^2 \, dt
\]

Compare to diffusive error, which has zero mean. **Jump error has systematic bias** when gamma is signed.

**Variance of jump hedging error:**

\[
\text{Var}(\text{Jump HE}) \approx \lambda_J \int_0^T \left(\frac{1}{2}\Gamma S^2 \sigma_J^2\right)^2 dt
\]

---

## Discrete trading: the fundamental limit


With trading only at times \(t_0, t_1, \ldots, t_N\), the hedging error per interval is:

\[
\epsilon_k = \frac{1}{2}\Gamma_k \left[(\Delta S_k)^2 - \sigma^2 S_k^2 \Delta t\right] + \mathcal{O}(\Delta t)
\]

**Total error variance** scales as \(\Delta t\), never reaching zero:

\[
\text{Var}(\text{HE}) = \mathcal{O}(\Delta t)
\]

**Implication:** Perfect replication is impossible with discrete trading.

---

## Model error: volatility misspecification


If the hedger uses \(\hat{\sigma}\) while true volatility is \(\sigma(t)\):

\[
\text{HE} = \frac{1}{2}\int_0^T \Gamma(t, S_t) S_t^2 \left(\sigma(t)^2 - \hat{\sigma}^2\right) dt
\]

This is a **systematic error** (not mean-zero) that accumulates over time.

**For stochastic volatility:** \(\sigma(t)\) is random, so hedging error is doubly stochastic:
1. Randomness from \(S\) path
2. Randomness from \(\sigma\) path

Delta hedging in a stochastic volatility world leaves **vega exposure** unhedged.

---

## Comparison: continuous vs discrete vs jump


| Assumption violated | Error structure | Scaling |
|:--------------------|:----------------|:--------|
| Discrete trading | Mean-zero, variance \(\sim \Delta t\) | \(\sqrt{\Delta t}\) |
| Jump risk | Biased if \(\Gamma \neq 0\), rare large errors | \(\lambda_J \sigma_J^2\) |
| Vol misspecification | Systematic drift | \(\sim T\) |
| Stochastic vol | Path-dependent, vega exposure | \(\sim \sqrt{T}\) |

---

## Robustness of hedging strategies


**Delta-only hedging** is robust to:
- Small volatility changes (first-order effect is zero)
- Small discrete intervals

**Delta-only hedging** is fragile to:
- Large jumps
- Systematic volatility misspecification
- Near-expiry gamma exposure

**Delta-gamma hedging** adds second-order protection but:
- Requires additional instruments (e.g., another option)
- Introduces new risks (basis risk)

---

## Implications for practice


1. **Size positions for jump risk**: Maximum loss \(\approx \frac{1}{2}\Gamma S^2 J_{\max}^2\)
2. **Hedge more frequently as expiry approaches**: Gamma increases, error amplifies
3. **Use realized vol monitoring**: Detect when \(\sigma \neq \hat{\sigma}\)
4. **Consider delta-gamma-vega hedging**: For complex books
5. **Stress test for jumps**: Compute P&L under tail scenarios

---

## Jump risk in specific models


**Merton jump-diffusion:**
\[
\frac{dS}{S} = (r - \lambda_J \bar{J}) dt + \sigma dW + J dN
\]

where \(J \sim \mathcal{N}(\mu_J, \sigma_J^2)\). Options cannot be perfectly hedged; a risk premium for jump risk appears.

**Variance gamma:**
Pure jump process with infinite activity but finite variation. Delta hedging breaks down fundamentally.

**Poisson-driven jumps:**
Large, rare jumps dominate hedging error. Hedging becomes insurance against tail events.

---

## Quantifying unhedgeable risk


The **minimum hedging error variance** achievable with continuous delta hedging in a jump-diffusion is:

\[
\text{Var}_{\min}(\text{HE}) = \lambda_J \mathbb{E}\left[\left(\frac{1}{2}\Gamma S^2 J^2\right)^2\right]
\]

This sets a **floor** on risk that cannot be eliminated by trading the underlying alone.

> **Forward reference.** Complete treatment of jump risk and incompleteness is in **Chapter 9** (Stochastic Volatility) and **Chapter 11** (Jump Processes).

---

## What to remember


- Delta hedging is local; jumps invalidate small-move approximations
- Jump hedging error: \(\epsilon \approx \frac{1}{2}\Gamma S^2 J^2\) (quadratic in jump size)
- Discrete hedging error becomes large when gamma is large
- Systematic model errors accumulate; random errors scale as \(\sqrt{T}\)
- In jump models, perfect replication is impossible: markets are incomplete
- Size positions for worst-case jump scenarios
