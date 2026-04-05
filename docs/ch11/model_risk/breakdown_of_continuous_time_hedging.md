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

??? success "Solution to Exercise 1"
    The hedging error from a jump of size $J = -0.10$ is

    $$
    \epsilon_{\text{jump}} \approx \frac{1}{2}\Gamma S^2 J^2 = \frac{1}{2} \times 0.04 \times 100^2 \times (-0.10)^2 = \frac{1}{2} \times 0.04 \times 10{,}000 \times 0.01 = \$2.00
    $$

    Now compute the daily diffusive hedging error standard deviation. For a delta-hedged position with discrete daily rebalancing, the hedging error per step is

    $$
    \epsilon_k = \frac{1}{2}\Gamma\left[(\Delta S)^2 - \sigma^2 S^2 \Delta t\right]
    $$

    The variance of $(\Delta S)^2$ is $\text{Var}((\sigma S \sqrt{\Delta t} Z)^2) = 2\sigma^4 S^4 (\Delta t)^2$ (since $\text{Var}(Z^2) = 2$ for $Z \sim \mathcal{N}(0,1)$). Thus

    $$
    \text{Std}(\epsilon_k) = \frac{1}{2}\Gamma \cdot \sigma^2 S^2 \Delta t \cdot \sqrt{2} = \frac{1}{2} \times 0.04 \times 0.04 \times 10{,}000 \times \frac{1}{252} \times \sqrt{2}
    $$

    $$
    = \frac{1}{2} \times 0.04 \times 0.04 \times 10{,}000 \times 0.003968 \times 1.414 = \frac{1}{2} \times 0.04 \times 0.5610 = \$0.01122
    $$

    The jump error of $\$2.00$ compared to the daily diffusive standard deviation of $\$0.01122$:

    $$
    \frac{\$2.00}{\$0.01122} \approx 178 \text{ standard deviations}
    $$

    A single 10% jump produces a hedging error equivalent to roughly 178 standard deviations of daily diffusive hedging error. This illustrates why jump risk is qualitatively different from diffusion risk: jumps create rare but enormous hedging losses that cannot be captured by normal-distribution-based risk measures.

---

**Exercise 2.** The expected hedging error from jumps is $\frac{1}{2}\lambda_J\int_0^T \Gamma S^2 \sigma_J^2\,dt$. For $\lambda_J = 2$ (two expected jumps per year), $\sigma_J^2 = 0.01$ (jump variance), $\Gamma = 0.03$, $S = 100$, and $T = 0.5$, compute the expected jump hedging error. Is this error systematic or mean-zero? How does this compare to the volatility misspecification error from using $\hat{\sigma} = 0.20$ when true $\sigma = 0.22$?

??? success "Solution to Exercise 2"
    The expected jump hedging error is

    $$
    \mathbb{E}[\text{Jump HE}] = \frac{1}{2}\lambda_J \int_0^T \Gamma S^2 \sigma_J^2\,dt
    $$

    With constant $\Gamma = 0.03$, $S = 100$, $\sigma_J^2 = 0.01$, $\lambda_J = 2$, $T = 0.5$:

    $$
    \mathbb{E}[\text{Jump HE}] = \frac{1}{2} \times 2 \times 0.03 \times 100^2 \times 0.01 \times 0.5 = 1.0 \times 0.03 \times 10{,}000 \times 0.01 \times 0.5
    $$

    $$
    = 1.0 \times 0.03 \times 100 \times 0.5 = \$1.50
    $$

    This error is **systematic** (not mean-zero) because gamma has a definite sign. For a short call ($\Gamma > 0$ from the hedger's perspective), jumps always produce a loss on average because $J^2 > 0$ regardless of jump direction.

    For the volatility misspecification comparison, the error is

    $$
    \text{HE}_{\text{vol}} = \frac{1}{2}\int_0^T \Gamma S^2(\sigma^2 - \hat{\sigma}^2)\,dt = \frac{1}{2} \times 0.03 \times 10{,}000 \times (0.0484 - 0.0400) \times 0.5
    $$

    $$
    = \frac{1}{2} \times 0.03 \times 10{,}000 \times 0.0084 \times 0.5 = 0.015 \times 10{,}000 \times 0.0042 = \$0.63
    $$

    The jump error ($\$1.50$) exceeds the vol misspecification error ($\$0.63$) for these parameters. Both are systematic (non-zero mean), but the jump error arises from market incompleteness while the vol error arises from parameter misestimation. The jump error cannot be eliminated by better calibration, whereas the vol error can be reduced by using realized volatility.

---

**Exercise 3.** Consider a delta-hedged short call in the Merton jump-diffusion model with $\sigma = 0.15$, $\lambda_J = 1$, and $J \sim \mathcal{N}(-0.05, 0.03^2)$. Compute the minimum hedging error variance $\text{Var}_{\min}(\text{HE}) = \lambda_J\mathbb{E}[(\frac{1}{2}\Gamma S^2 J^2)^2]$ for $\Gamma = 0.04$ and $S = 100$. This is the floor on risk that cannot be eliminated by trading the underlying alone.

??? success "Solution to Exercise 3"
    In the Merton model, $J \sim \mathcal{N}(\mu_J, \sigma_J^2)$ with $\mu_J = -0.05$ and $\sigma_J = 0.03$. We need $\mathbb{E}[J^4]$ for the variance calculation.

    For $J \sim \mathcal{N}(\mu_J, \sigma_J^2)$:

    $$
    \mathbb{E}[J^2] = \mu_J^2 + \sigma_J^2 = 0.0025 + 0.0009 = 0.0034
    $$

    $$
    \mathbb{E}[J^4] = \mu_J^4 + 6\mu_J^2\sigma_J^2 + 3\sigma_J^4 = (0.05)^4 + 6(0.05)^2(0.03)^2 + 3(0.03)^4
    $$

    $$
    = 6.25 \times 10^{-6} + 6 \times 0.0025 \times 0.0009 + 3 \times 8.1 \times 10^{-7}
    $$

    $$
    = 6.25 \times 10^{-6} + 1.35 \times 10^{-5} + 2.43 \times 10^{-6} = 2.218 \times 10^{-5}
    $$

    The minimum hedging error variance (per unit time, per jump) is

    $$
    \text{Var}_{\min}(\text{HE}) = \lambda_J \mathbb{E}\left[\left(\frac{1}{2}\Gamma S^2 J^2\right)^2\right] = \lambda_J \cdot \frac{1}{4}\Gamma^2 S^4 \cdot \mathbb{E}[J^4]
    $$

    $$
    = 1 \times \frac{1}{4} \times (0.04)^2 \times (100)^4 \times 2.218 \times 10^{-5}
    $$

    $$
    = 0.25 \times 0.0016 \times 10^8 \times 2.218 \times 10^{-5}
    $$

    $$
    = 0.25 \times 0.0016 \times 2218 = 0.25 \times 3.549 = \$^2 0.8872
    $$

    The standard deviation of the hedging error per year from jumps is $\sqrt{0.8872} \approx \$0.942$. This represents the irreducible floor on hedging risk from jump exposure. Even with perfect continuous delta hedging of the diffusive component, the hedger faces roughly $\$0.94$ of standard deviation per year from unhedgeable jump risk.

---

**Exercise 4.** A trader monitors the hedge P&L daily to detect volatility misspecification. The cumulative misspecification error is $\text{HE} = \frac{1}{2}\int_0^t \Gamma S^2(\sigma^2 - \hat{\sigma}^2)\,ds$. If $\hat{\sigma} = 0.20$, $\sigma = 0.25$, $\Gamma = 0.03$, and $S = 100$, compute the expected daily P&L drift from misspecification. After how many days would the cumulative drift exceed one standard deviation of the diffusive hedging error (assuming daily rebalancing)?

??? success "Solution to Exercise 4"
    The daily P&L drift from volatility misspecification is

    $$
    \frac{d(\text{HE})}{dt} = \frac{1}{2}\Gamma S^2(\sigma^2 - \hat{\sigma}^2)
    $$

    With $\hat{\sigma} = 0.20$, $\sigma = 0.25$:

    $$
    \sigma^2 - \hat{\sigma}^2 = 0.0625 - 0.0400 = 0.0225
    $$

    $$
    \frac{d(\text{HE})}{dt} = \frac{1}{2} \times 0.03 \times 10{,}000 \times 0.0225 = \frac{1}{2} \times 0.03 \times 225 = \$3.375 \text{ per year}
    $$

    Converting to daily: $3.375 / 252 = \$0.01339$ per day.

    The standard deviation of the daily diffusive hedging error (from Exercise 1's approach) is

    $$
    \text{Std}(\epsilon_{\text{daily}}) = \frac{1}{2}\Gamma \sigma^2 S^2 \Delta t \sqrt{2}
    $$

    Using the true $\sigma = 0.25$:

    $$
    = \frac{1}{2} \times 0.03 \times 0.0625 \times 10{,}000 \times \frac{1}{252} \times \sqrt{2} = 0.015 \times 0.0625 \times 10{,}000 \times 0.005607
    $$

    $$
    = 0.015 \times 625 \times 0.005607 = 0.015 \times 3.504 = \$0.05256
    $$

    After $n$ days, the cumulative drift is $n \times 0.01339$ and the cumulative standard deviation is $\sqrt{n} \times 0.05256$ (since daily errors are approximately independent).

    Setting the drift equal to one standard deviation:

    $$
    n \times 0.01339 = \sqrt{n} \times 0.05256
    $$

    $$
    \sqrt{n} = \frac{0.05256}{0.01339} = 3.925
    $$

    $$
    n \approx 15.4 \text{ days}
    $$

    After approximately 15 trading days (about 3 weeks), the cumulative misspecification drift exceeds one standard deviation of the cumulative random hedging error. This is the timescale on which systematic vol misspecification becomes statistically detectable.

---

**Exercise 5.** The comparison table shows different error structures: discrete trading ($\sqrt{\Delta t}$), jump risk ($\lambda_J\sigma_J^2$), and vol misspecification ($\sim T$). For a 6-month option with daily rebalancing, $\sigma = 0.20$, $\Gamma = 0.03$, $S = 100$, $\lambda_J = 1$, $\sigma_J = 0.08$, and vol misspecification $\delta\sigma = 0.02$, compute the contribution of each error source to the total hedging error. Which dominates?

??? success "Solution to Exercise 5"
    We compute each error source for a 6-month option ($T = 0.5$) with daily rebalancing ($\Delta t = 1/252$), $\sigma = 0.20$, $\Gamma = 0.03$, $S = 100$.

    **Discrete trading error:** The variance per step is

    $$
    \text{Var}(\epsilon_k) = \frac{1}{4}\Gamma^2 \sigma^4 S^4 (\Delta t)^2 \times 2
    $$

    Over $N = 126$ steps (half year of daily trading):

    $$
    \text{Total Var} = 126 \times \frac{1}{2} \times (0.03)^2 \times (0.20)^4 \times (100)^4 \times (1/252)^2
    $$

    $$
    = 126 \times 0.5 \times 9 \times 10^{-4} \times 1.6 \times 10^{-3} \times 10^{8} \times 1.575 \times 10^{-5}
    $$

    $$
    = 63 \times 9 \times 10^{-4} \times 1.6 \times 10^{-3} \times 10^8 \times 1.575 \times 10^{-5}
    $$

    $$
    = 63 \times 9 \times 1.6 \times 1.575 \times 10^{-4} = 63 \times 22.68 \times 10^{-4} = 63 \times 0.002268 = 0.1429
    $$

    Standard deviation: $\sqrt{0.1429} \approx \$0.378$.

    **Jump risk:** The expected error is

    $$
    \frac{1}{2}\lambda_J \Gamma S^2 \sigma_J^2 T = \frac{1}{2} \times 1 \times 0.03 \times 10{,}000 \times 0.0064 \times 0.5 = 0.48
    $$

    The standard deviation (from the variance formula) is

    $$
    \sqrt{\lambda_J T} \times \frac{1}{2}\Gamma S^2 \sigma_J^2 = \sqrt{0.5} \times 0.96 \approx \$0.679
    $$

    **Vol misspecification:** With $\delta\sigma = 0.02$:

    $$
    \text{HE}_{\text{vol}} = \frac{1}{2}\Gamma S^2(\sigma_{\text{true}}^2 - \hat{\sigma}^2)T
    $$

    $$
    \sigma_{\text{true}}^2 - \hat{\sigma}^2 = (0.22)^2 - (0.20)^2 = 0.0484 - 0.0400 = 0.0084
    $$

    $$
    \text{HE}_{\text{vol}} = \frac{1}{2} \times 0.03 \times 10{,}000 \times 0.0084 \times 0.5 = \$0.63
    $$

    This is a deterministic (systematic) error.

    **Summary of contributions:**

    | Source | Error type | Magnitude |
    |:-------|:-----------|:----------|
    | Discrete trading | Random (std dev) | $\$0.38$ |
    | Jump risk | Biased + random | $\$0.48$ (mean), $\$0.68$ (std) |
    | Vol misspecification | Systematic | $\$0.63$ |

    For these parameters, vol misspecification and jump risk dominate. Discrete trading error is the smallest contributor. The vol misspecification is the most concerning because it is purely systematic and accumulates predictably over time, while the jump risk contributes both a bias and significant randomness.

---

**Exercise 6.** Delta-gamma hedging uses a second option to neutralize gamma, providing protection against large moves and jumps. If the underlying has $\Gamma_1$ and the hedging option has $\Gamma_2 = 0.06$, explain how to set up a delta-gamma neutral position. For a jump of size $J = -0.15$, compute the residual hedging error from the speed term $\frac{1}{6}\text{Speed} \cdot S^3 J^3$ with $\text{Speed} = 0.002$ and $S = 100$. Is gamma hedging sufficient protection against large jumps?

??? success "Solution to Exercise 6"
    **Setting up a delta-gamma neutral position:** Suppose we hold a portfolio with gamma $\Gamma_1$ (from the position to be hedged). We buy $n$ units of the hedging option with gamma $\Gamma_2 = 0.06$. For gamma neutrality:

    $$
    \Gamma_1 + n\Gamma_2 = 0 \implies n = -\frac{\Gamma_1}{\Gamma_2} = -\frac{\Gamma_1}{0.06}
    $$

    For example, if $\Gamma_1 = -0.03$ (short gamma from selling calls), then $n = 0.03/0.06 = 0.5$ units of the hedging option. After gamma neutralization, we adjust the delta by trading the underlying to make the total delta zero.

    **Residual hedging error from speed:** With gamma neutralized ($\Gamma_{\text{net}} = 0$), the dominant hedging error from a jump comes from the third-order (speed) term:

    $$
    \epsilon_{\text{residual}} = \frac{1}{6}\text{Speed} \cdot S^3 J^3
    $$

    With $\text{Speed} = 0.002$, $S = 100$, $J = -0.15$:

    $$
    S^3 J^3 = (100)^3 \times (-0.15)^3 = 10^6 \times (-0.003375) = -3{,}375
    $$

    $$
    \epsilon_{\text{residual}} = \frac{1}{6} \times 0.002 \times (-3{,}375) = \frac{-6.75}{6} = -\$1.125
    $$

    **Is gamma hedging sufficient?** Compare to the gamma error that would have occurred without gamma hedging. If $\Gamma_1 = -0.03$ (before hedging):

    $$
    \epsilon_{\text{gamma}} = \frac{1}{2}|\Gamma_1| S^2 J^2 = \frac{1}{2} \times 0.03 \times 10{,}000 \times 0.0225 = \$3.375
    $$

    Gamma hedging reduced the error from $\$3.375$ to $\$1.125$ (a factor of 3 reduction), but the residual speed error is still substantial for a 15% jump. For large jumps, the Taylor expansion converges slowly, and even higher-order terms (involving the fourth derivative, etc.) may contribute. Gamma hedging provides meaningful but not complete protection against large jumps. Full protection against jumps of this magnitude requires either buying protective options (puts/calls) with payoffs that match the tail exposure or accepting the residual risk as a cost of market incompleteness.
