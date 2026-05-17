# Discrete-Time Hedging Error

Continuous-time delta hedging is an idealization. Discrete rebalancing introduces a random hedging error influenced by gamma.

!!! tip "Toy mechanism: $(\Delta S)^2$ doesn't equal $\sigma^2 S^2\Delta t$ at finite resolution"
    The mechanism is one line. Continuous-time Black–Scholes hedging works because $\langle S\rangle_t = \int_0^t \sigma^2 S_s^2\,ds$ exactly — the gamma term $\tfrac{1}{2}\Gamma(\delta S)^2$ matches the theta term $-\Theta\,\delta t$ on average. Discretise the time grid and the *pathwise* random variable $(\Delta S_k)^2$ replaces the *expected* quantity $\sigma^2 S_k^2\Delta t$. Their difference $(\Delta S_k)^2 - \sigma^2 S_k^2\Delta t$ has mean zero but nonzero variance — and that variance, multiplied by $\tfrac{1}{2}\Gamma$, *is* the per-step hedging error. Everything below — the gamma scaling, the $\sqrt{\Delta t}$ standard deviation, the cost–error tradeoff — comes from accumulating this single discrepancy across $N$ steps.

---

## Setup


Consider hedging an option $V(t,S)$ by holding $\Delta(t_k, S_{t_k})$ shares at discrete times $t_0 < t_1 < \cdots < t_N = T$ with $\Delta t = t_{k+1} - t_k$.

The hedging portfolio value at $t_{k+1}$ is:

$$
\Pi_{k+1} = \Pi_k e^{r\Delta t} + \Delta_k (S_{k+1} - S_k e^{r\Delta t})
$$

where $\Delta_k = \Delta(t_k, S_k)$ is the delta computed at rebalancing time.

---

## Hedging error: rigorous derivation


The hedging error over $[t_k, t_{k+1}]$ is $\epsilon_k = (V_{k+1} - V_k) - (\Pi_{k+1} - \Pi_k)$. Recall (see [§ Gamma Risk and Convexity Effects](gamma_risk_and_convexity_effects.md)): Taylor expanding $V$ and subtracting the hedge P&L $\Delta_k(S_{k+1}-S_k)$ leaves

$$
\boxed{\epsilon_k \approx \Theta_k \Delta t + \frac{1}{2}\Gamma_k(\Delta S_k)^2}
$$

Using the theta-gamma identity:

$$
\epsilon_k \approx \frac{1}{2}\Gamma_k\left[(\Delta S_k)^2 - \sigma^2 S_k^2 \Delta t\right]
$$

---

## Heuristic structure


The hedging error can be related to the replacement of quadratic variation by realized squared increments:

$$
\mathrm{HE} \approx
\frac{1}{2}\sum_k \Gamma(t_k,S_{t_k})(\Delta S_k)^2
-\frac{1}{2}\int_0^T \Gamma(t,S_t)\,\mathrm{d}\langle S\rangle_t
$$

The first term is the realized gamma P&L; the second is the continuous-time limit.

---

## Error variance


Under Black–Scholes dynamics, the hedging error per step has:

**Mean:**

$$
\mathbb{E}[\epsilon_k | \mathcal{F}_{t_k}] \approx 0
$$

**Variance:**

$$
\text{Var}(\epsilon_k | \mathcal{F}_{t_k}) \approx \frac{1}{2}\Gamma_k^2 S_k^4 \sigma^4 (\Delta t)^2
$$

**Cumulative error variance** (summing over $N = T/\Delta t$ steps):

$$
\boxed{\text{Var}(\mathrm{HE}) \approx \frac{1}{2}\bar{\Gamma}^2 S^4 \sigma^4 T \cdot \Delta t}
$$

where $\bar{\Gamma}$ is an average gamma. The variance scales linearly with $\Delta t$.

**Standard deviation of hedging error:**

$$
\text{Std}(\mathrm{HE}) \sim \sqrt{\Delta t}
$$

---

## Central limit theorem for hedging error


For small $\Delta t$, the cumulative hedging error is approximately Gaussian:

$$
\mathrm{HE} \xrightarrow{d} \mathcal{N}\left(0, \frac{1}{2}\int_0^T \Gamma^2 S^4 \sigma^4 dt \cdot \Delta t\right)
$$

This is the basis for asymptotic hedging error expansions:

$$
\mathrm{HE} = c_1 \sqrt{\Delta t} \cdot Z + \mathcal{O}(\Delta t)
$$

where $Z \sim \mathcal{N}(0,1)$ and $c_1 = \sqrt{\frac{1}{2}\int_0^T \Gamma^2 S^4 \sigma^4 dt}$.

---

## Frequency-error tradeoff


| Rebalancing | $\Delta t$ | Error Std | Transaction Cost |
|:------------|:-------------|:----------|:-----------------|
| Daily | 1/252 yr | $\mathcal{O}(0.06)$ | Low |
| Hourly | 1/6048 yr | $\mathcal{O}(0.01)$ | Moderate |
| Continuous | 0 | 0 | Infinite |

More frequent rebalancing reduces hedging error but increases transaction costs.

---

## Numerical example


Consider an ATM call with $S = K = 100$, $\sigma = 20\%$, $\tau = 0.25$ (3 months), $r = 5\%$:

- $\Gamma \approx 0.032$
- $\Gamma S^2 \sigma^2 = 0.032 \times 10000 \times 0.04 = 12.8$

**Daily rebalancing** ($\Delta t = 1/252$):

$$
\text{Std}(\epsilon_{\text{daily}}) \approx \sqrt{\frac{1}{2}} \times 12.8 \times \frac{1}{252} \approx 0.036
$$

Over 63 trading days:

$$
\text{Std}(\mathrm{HE}) \approx 0.036 \times \sqrt{63} \approx 0.28
$$

**Weekly rebalancing** ($\Delta t = 1/52$):

$$
\text{Std}(\mathrm{HE}) \approx 0.28 \times \sqrt{5} \approx 0.63
$$

Weekly hedging has about $\sqrt{5} \approx 2.2\times$ higher error standard deviation.

---

## Path dependence of hedging error


The hedging error is path-dependent through gamma:

1. **Volatile paths**: Higher $(\Delta S)^2$, larger errors
2. **Paths crossing strike**: Gamma spikes, error amplified
3. **Calm paths**: Lower errors

This path dependence is the source of "gamma risk" in practice.

---

## Model risk in hedging error


The analysis assumes correct model. In practice:

- **Volatility misspecification**: Changes the drift of hedging error (see [§ Impact of Volatility Misspecification](impact_of_volatility_misspecification.md))
- **Jump risk**: Causes large discrete errors that dominate diffusive terms
- **Correlation breakdown**: Hedging error in multi-asset positions

---

## What to remember


- Discrete hedging creates variance-like error terms
- Error variance scales as $\Gamma^2 S^4 \sigma^4 T \cdot \Delta t$
- Standard deviation scales as $\sqrt{\Delta t}$
- Near-expiry gamma blow-up magnifies the error
- More frequent rebalancing reduces error but increases costs
- The hedging error is approximately Gaussian for small $\Delta t$ (CLT)

---

## Exercises

**Exercise 1.** For an ATM call with $S = K = 100$, $\sigma = 0.20$, $\tau = 0.5$, $r = 0.03$, compute $\Gamma$ and then the per-step hedging error variance $\text{Var}(\epsilon_k) \approx \frac{1}{2}\Gamma^2 S^4 \sigma^4 (\Delta t)^2$ for daily rebalancing ($\Delta t = 1/252$). What is the standard deviation of a single day's hedging error?

??? success "Solution to Exercise 1"
    For an ATM call under Black--Scholes, the gamma is:

    $$
    \Gamma = \frac{\phi(d_1)}{S\sigma\sqrt{\tau}}
    $$

    With $S = K = 100$, $\sigma = 0.20$, $\tau = 0.5$, $r = 0.03$:

    $$
    d_1 = \frac{\ln(1) + (0.03 + 0.02)(0.5)}{0.20\sqrt{0.5}} = \frac{0.025}{0.1414} \approx 0.1768
    $$

    $$
    \phi(d_1) = \frac{1}{\sqrt{2\pi}}e^{-d_1^2/2} \approx \frac{1}{\sqrt{2\pi}}e^{-0.0156} \approx 0.3939
    $$

    $$
    \Gamma = \frac{0.3939}{100 \times 0.20 \times 0.7071} \approx \frac{0.3939}{14.14} \approx 0.02786
    $$

    Now the per-step hedging error variance with daily rebalancing ($\Delta t = 1/252$):

    $$
    \operatorname{Var}(\epsilon_k) \approx \frac{1}{2}\Gamma^2 S^4 \sigma^4 (\Delta t)^2
    $$

    $$
    = \frac{1}{2}(0.02786)^2 (100)^4 (0.20)^4 (1/252)^2
    $$

    $$
    = \frac{1}{2}(7.76 \times 10^{-4})(10^8)(1.6 \times 10^{-3})(1.575 \times 10^{-5})
    $$

    $$
    = \frac{1}{2}(7.76 \times 10^{-4})(2520) \approx \frac{1}{2}(1.956) \approx 0.978
    $$

    Wait -- let us recompute more carefully:

    $$
    \Gamma^2 S^4 \sigma^4 = (0.02786)^2 \times 10^8 \times (0.20)^4 = 7.76 \times 10^{-4} \times 10^8 \times 1.6 \times 10^{-3} = 124.2
    $$

    $$
    \operatorname{Var}(\epsilon_k) = \frac{1}{2} \times 124.2 \times (1/252)^2 = 62.1 \times 1.575 \times 10^{-5} \approx 9.78 \times 10^{-4}
    $$

    The standard deviation of a single day's hedging error is:

    $$
    \operatorname{Std}(\epsilon_k) \approx \sqrt{9.78 \times 10^{-4}} \approx 0.0313
    $$

    So a single day's hedging error has a standard deviation of approximately $\$0.031$.

---

**Exercise 2.** Using the cumulative error variance formula $\text{Var}(\text{HE}) \approx \frac{1}{2}\bar{\Gamma}^2 S^4 \sigma^4 T \cdot \Delta t$, compute the hedging error standard deviation for daily, weekly, and monthly rebalancing of an ATM call with $T = 0.25$, $\Gamma = 0.032$, $S = 100$, $\sigma = 0.20$. Verify the $\sqrt{\Delta t}$ scaling.

??? success "Solution to Exercise 2"
    Using $\operatorname{Var}(\text{HE}) \approx \frac{1}{2}\bar{\Gamma}^2 S^4 \sigma^4 T \cdot \Delta t$ with $\Gamma = 0.032$, $S = 100$, $\sigma = 0.20$, $T = 0.25$:

    First compute the constant factor:

    $$
    \frac{1}{2}\Gamma^2 S^4 \sigma^4 T = \frac{1}{2}(0.032)^2(10^8)(1.6 \times 10^{-3})(0.25)
    $$

    $$
    = \frac{1}{2}(1.024 \times 10^{-3})(10^8)(4 \times 10^{-4}) = \frac{1}{2}(1.024 \times 10^{-3})(40000) = \frac{1}{2}(40.96) = 20.48
    $$

    **Daily** ($\Delta t = 1/252$):

    $$
    \operatorname{Std}(\text{HE}) = \sqrt{20.48 / 252} = \sqrt{0.08127} \approx 0.285
    $$

    **Weekly** ($\Delta t = 1/52$):

    $$
    \operatorname{Std}(\text{HE}) = \sqrt{20.48 / 52} = \sqrt{0.3938} \approx 0.628
    $$

    **Monthly** ($\Delta t = 1/12$):

    $$
    \operatorname{Std}(\text{HE}) = \sqrt{20.48 / 12} = \sqrt{1.707} \approx 1.307
    $$

    **Verification of scaling.** The ratios should equal $\sqrt{\Delta t_1 / \Delta t_2}$:

    $$
    \frac{\text{Std(weekly)}}{\text{Std(daily)}} = \frac{0.628}{0.285} \approx 2.20 \approx \sqrt{252/52} = \sqrt{4.846} \approx 2.20 \;\checkmark
    $$

    $$
    \frac{\text{Std(monthly)}}{\text{Std(daily)}} = \frac{1.307}{0.285} \approx 4.59 \approx \sqrt{252/12} = \sqrt{21} \approx 4.58 \;\checkmark
    $$

    The $\sqrt{\Delta t}$ scaling is confirmed.

---

**Exercise 3.** The error formula $\epsilon_k \approx \frac{1}{2}\Gamma_k[(\Delta S_k)^2 - \sigma^2 S_k^2 \Delta t]$ shows that the hedging error is zero in expectation. Explain intuitively why: what would it mean if the expected hedging error were nonzero, and how would that contradict the Black--Scholes pricing framework?

??? success "Solution to Exercise 3"
    The hedging error $\epsilon_k \approx \frac{1}{2}\Gamma_k[(\Delta S_k)^2 - \sigma^2 S_k^2 \Delta t]$ compares the realized squared price move $(\Delta S_k)^2$ against the expected squared move $\sigma^2 S_k^2 \Delta t$. Under the true Black--Scholes dynamics, $\mathbb{E}[(\Delta S_k)^2 \mid \mathcal{F}_{t_k}] = \sigma^2 S_k^2 \Delta t + O((\Delta t)^2)$, so $\mathbb{E}[\epsilon_k] \approx 0$.

    **Intuitive explanation:** If the expected hedging error were systematically positive (or negative), it would mean the delta-hedging strategy over-replicates (or under-replicates) the option in expectation. This would create a systematic arbitrage: one could exploit the mispricing by trading the option against the hedge portfolio. In the Black--Scholes framework, the option price is defined as the cost of the replicating portfolio. If the expected replication error were nonzero, the option price would be wrong -- contradicting the no-arbitrage pricing principle.

    Put differently, the Black--Scholes PDE is derived precisely from the condition that the hedging error has zero drift. The theta-gamma identity $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)$ encodes this condition: the time decay and expected gamma P&L exactly offset the financing cost, leaving no expected profit or loss from delta hedging.

---

**Exercise 4.** Consider two options with the same gamma but different paths to expiry: Option A stays ATM throughout, while Option B moves deep ITM early on. Which option has higher cumulative hedging error variance? Explain using the path dependence of $\Gamma(t, S_t)$.

??? success "Solution to Exercise 4"
    **Option A (stays ATM)** has higher cumulative hedging error variance.

    The cumulative hedging error variance is:

    $$
    \operatorname{Var}(\text{HE}) \approx \frac{1}{2}\sum_k \Gamma(t_k, S_{t_k})^2 S_{t_k}^4 \sigma^4 (\Delta t)^2
    $$

    The gamma $\Gamma(t, S)$ of an option is maximized when the option is ATM (i.e., $S \approx K$) and increases as $\tau \to 0$. For Option A, which stays ATM throughout its life, $\Gamma$ remains at or near its maximum value at every rebalancing date. The sum of $\Gamma_k^2$ terms is therefore large.

    For Option B, which moves deep ITM early, the gamma drops sharply once the option is deep ITM (since $\Gamma \to 0$ for deep ITM options). The sum of $\Gamma_k^2$ terms is dominated by the short initial period near ATM, and the remaining time contributes very little.

    In the continuous limit, $\int_0^T \Gamma(t, S_t)^2 S_t^4 \sigma^4 \, dt$ is much larger for paths that stay near the strike (Option A) than for paths that move far from the strike early (Option B). This illustrates the path dependence of hedging error: gamma risk is concentrated near the strike.

---

**Exercise 5.** The CLT predicts that $\text{HE}/\sqrt{\Delta t} \xrightarrow{d} \mathcal{N}(0, \frac{1}{2}\int_0^T \Gamma^2 S^4 \sigma^4 \, dt)$. For a 95% confidence interval on the hedging error with daily rebalancing, compute the interval bounds for the ATM call in Exercise 1. Express the interval in dollars and as a percentage of the option price.

??? success "Solution to Exercise 5"
    From Exercise 1, $\Gamma \approx 0.02786$, $S = 100$, $\sigma = 0.20$, $T = 0.5$, and daily rebalancing ($\Delta t = 1/252$).

    The cumulative hedging error variance is:

    $$
    \operatorname{Var}(\text{HE}) = \frac{1}{2}\Gamma^2 S^4 \sigma^4 T \cdot \Delta t
    $$

    $$
    = \frac{1}{2}(0.02786)^2(10^8)(1.6 \times 10^{-3})(0.5)(1/252)
    $$

    Compute $\frac{1}{2}\Gamma^2 S^4 \sigma^4 = 62.1$ (from Exercise 1), so:

    $$
    \operatorname{Var}(\text{HE}) = 62.1 \times 0.5 \times (1/252) = 62.1 \times 1.984 \times 10^{-3} \approx 0.1232
    $$

    $$
    \operatorname{Std}(\text{HE}) \approx \sqrt{0.1232} \approx 0.351
    $$

    The 95% confidence interval (using CLT) is:

    $$
    |\text{HE}| \leq 1.96 \times 0.351 \approx 0.688
    $$

    So the interval is approximately $[-0.69, +0.69]$.

    The Black--Scholes call price with these parameters is approximately $C \approx 7.10$. As a percentage of the option price:

    $$
    \frac{0.688}{7.10} \approx 9.7\%
    $$

    The 95% confidence interval for the hedging error is about $\pm \$0.69$, or roughly $\pm 9.7\%$ of the option price. This is a nontrivial fraction, illustrating the practical limitation of daily hedging.

---

**Exercise 6.** A trader claims that switching from daily to hourly rebalancing will "eliminate hedging error." Using the $\sqrt{\Delta t}$ scaling, compute the reduction factor in hedging error standard deviation. Is the improvement sufficient to justify the approximately $8\times$ increase in transaction costs? At what cost-per-trade does hourly rebalancing become suboptimal?

??? success "Solution to Exercise 6"
    **Reduction factor.** There are approximately 8 trading hours per day, so hourly rebalancing uses $\Delta t_{\text{hourly}} = \Delta t_{\text{daily}} / 8$. By the $\sqrt{\Delta t}$ scaling:

    $$
    \frac{\operatorname{Std}(\text{HE})_{\text{hourly}}}{\operatorname{Std}(\text{HE})_{\text{daily}}} = \sqrt{\frac{\Delta t_{\text{hourly}}}{\Delta t_{\text{daily}}}} = \sqrt{\frac{1}{8}} = \frac{1}{2\sqrt{2}} \approx 0.354
    $$

    So hourly rebalancing reduces the hedging error standard deviation by a factor of about $2.83$, not "eliminates" it. The error is reduced to roughly $35\%$ of the daily level.

    **Cost-benefit analysis.** The improvement is a factor of $2.83$ in error reduction, but transaction costs increase by a factor of $\sqrt{8} \approx 2.83$ (since expected TC scales as $\sqrt{N}$). Whether this is worthwhile depends on the relative magnitudes.

    Let $c$ denote the cost per trade. The total cost with $N$ rebalancings per day is:

    $$
    \text{Total} = \frac{a}{\sqrt{N}} + c \cdot N
    $$

    where $a$ captures the hedging error. For daily rebalancing ($N = 1$ per day): $\text{Total}_D = a + c$. For hourly ($N = 8$): $\text{Total}_H = a/(2\sqrt{2}) + 8c$.

    Hourly becomes suboptimal when $\text{Total}_H > \text{Total}_D$:

    $$
    \frac{a}{2\sqrt{2}} + 8c > a + c
    $$

    $$
    7c > a\left(1 - \frac{1}{2\sqrt{2}}\right) = a \times 0.646
    $$

    $$
    c > \frac{0.646\,a}{7} \approx 0.092\,a
    $$

    If the cost per trade exceeds roughly $9.2\%$ of the daily hedging error impact $a$, hourly rebalancing is suboptimal. For example, if the daily hedging error standard deviation is $\$0.30$, then hourly rebalancing becomes suboptimal when cost per trade exceeds approximately $\$0.028$.
