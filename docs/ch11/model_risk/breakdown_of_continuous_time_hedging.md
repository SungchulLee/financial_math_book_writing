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

---

## Exercises

**Exercise 1.** In a jump-diffusion model, a jump of size $J = -0.10$ (10% downward) occurs. For a short ATM call with $S = 100$, $K = 100$, $\Gamma = 0.04$, compute the hedging error $\epsilon_{\text{jump}} \approx \frac{1}{2}\Gamma S^2 J^2$. Compare this to the daily diffusive hedging error standard deviation (with $\sigma = 0.20$, $\Delta t = 1/252$). How many standard deviations of diffusive error does a single 10% jump represent?

---

**Exercise 2.** The expected hedging error from jumps is $\frac{1}{2}\lambda_J\int_0^T \Gamma S^2 \sigma_J^2\,dt$. For $\lambda_J = 2$ (two expected jumps per year), $\sigma_J^2 = 0.01$ (jump variance), $\Gamma = 0.03$, $S = 100$, and $T = 0.5$, compute the expected jump hedging error. Is this error systematic or mean-zero? How does this compare to the volatility misspecification error from using $\hat{\sigma} = 0.20$ when true $\sigma = 0.22$?

---

**Exercise 3.** Consider a delta-hedged short call in the Merton jump-diffusion model with $\sigma = 0.15$, $\lambda_J = 1$, and $J \sim \mathcal{N}(-0.05, 0.03^2)$. Compute the minimum hedging error variance $\text{Var}_{\min}(\text{HE}) = \lambda_J\mathbb{E}[(\frac{1}{2}\Gamma S^2 J^2)^2]$ for $\Gamma = 0.04$ and $S = 100$. This is the floor on risk that cannot be eliminated by trading the underlying alone.

---

**Exercise 4.** A trader monitors the hedge P&L daily to detect volatility misspecification. The cumulative misspecification error is $\text{HE} = \frac{1}{2}\int_0^t \Gamma S^2(\sigma^2 - \hat{\sigma}^2)\,ds$. If $\hat{\sigma} = 0.20$, $\sigma = 0.25$, $\Gamma = 0.03$, and $S = 100$, compute the expected daily P&L drift from misspecification. After how many days would the cumulative drift exceed one standard deviation of the diffusive hedging error (assuming daily rebalancing)?

---

**Exercise 5.** The comparison table shows different error structures: discrete trading ($\sqrt{\Delta t}$), jump risk ($\lambda_J\sigma_J^2$), and vol misspecification ($\sim T$). For a 6-month option with daily rebalancing, $\sigma = 0.20$, $\Gamma = 0.03$, $S = 100$, $\lambda_J = 1$, $\sigma_J = 0.08$, and vol misspecification $\delta\sigma = 0.02$, compute the contribution of each error source to the total hedging error. Which dominates?

---

**Exercise 6.** Delta-gamma hedging uses a second option to neutralize gamma, providing protection against large moves and jumps. If the underlying has $\Gamma_1$ and the hedging option has $\Gamma_2 = 0.06$, explain how to set up a delta-gamma neutral position. For a jump of size $J = -0.15$, compute the residual hedging error from the speed term $\frac{1}{6}\text{Speed} \cdot S^3 J^3$ with $\text{Speed} = 0.002$ and $S = 100$. Is gamma hedging sufficient protection against large jumps?
