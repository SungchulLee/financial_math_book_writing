# Multi-Factor Volatility Models


Single-factor stochastic volatility models often fail to capture the full richness of volatility dynamics. **Multi-factor volatility models** introduce additional latent factors to improve realism and stability.

---

## Motivation for multiple factors


Empirical volatility exhibits:

- short-term fluctuations,
- long-term persistence,
- regime-dependent behavior.

A single volatility factor cannot capture all time scales simultaneously.

---

## General structure


A generic multi-factor model may be written as

$$
V_t = \sum_{i=1}^n V_t^{(i)}
$$


where each factor satisfies its own stochastic dynamics, often with different mean-reversion speeds.

---

## Examples


- **Two-factor Heston:** fast and slow variance components,
- **Long/short memory models:** separated time scales,
- **Factor-based rough approximations:** Markovian lifts of rough volatility.

These models improve fit and stability across maturities.

---

## Calibration and identifiability


Adding factors increases flexibility but introduces:

- identifiability challenges,
- higher calibration variance,
- need for stronger regularization.

Calibration typically requires:

- wide maturity coverage,
- strong parameter constraints,
- stability-focused objectives.

---

## Key takeaways


- Multi-factor models capture multiple volatility time scales.
- They improve surface fit and dynamic consistency.
- Complexity must be balanced against stability.

---

## Further reading


- Bergomi, *Stochastic Volatility Modeling*.
- Fouque et al., multiscale volatility models.
- Abi Jaber et al., multi-factor rough volatility.

---

## Exercises

**Exercise 1.** In a two-factor Heston model, the total variance is $V_t = V_t^{(1)} + V_t^{(2)}$ where

$$
dV_t^{(i)} = \kappa_i(\theta_i - V_t^{(i)})\,dt + \xi_i\sqrt{V_t^{(i)}}\,dW_t^{(i)}, \quad i = 1, 2
$$

with $\kappa_1 = 5$ (fast factor) and $\kappa_2 = 0.5$ (slow factor). Compute the half-lives $t_{1/2}^{(i)} = \ln 2/\kappa_i$ for each factor. Explain how the fast factor captures short-term volatility spikes while the slow factor captures long-term regime shifts.

??? success "Solution to Exercise 1"
    **Half-lives.** The half-life is $t_{1/2} = \ln 2 / \kappa$:

    - Fast factor: $t_{1/2}^{(1)} = \ln 2 / 5 \approx 0.693 / 5 \approx 0.139$ years $\approx 35$ trading days
    - Slow factor: $t_{1/2}^{(2)} = \ln 2 / 0.5 \approx 0.693 / 0.5 \approx 1.386$ years

    **Interpretation.** The fast factor ($\kappa_1 = 5$) has a half-life of about 5 weeks, meaning it captures short-term volatility spikes that dissipate quickly. Events like earnings surprises, flash crashes, or sudden market dislocations elevate the fast component, which then decays rapidly back toward its long-run mean $\theta_1$.

    The slow factor ($\kappa_2 = 0.5$) has a half-life of nearly 1.4 years, capturing persistent regime shifts in volatility. Events like the 2008 financial crisis or the COVID-19 pandemic, where elevated volatility persists for months or years, are driven primarily by the slow factor.

    Together, the two factors allow the model to simultaneously exhibit rapid spikes and slow regime changes, which a single CIR factor cannot achieve without compromising on one time scale.

---

**Exercise 2.** For the two-factor model with $\theta_1 = 0.02$, $\theta_2 = 0.03$, the long-run total variance is $\theta_1 + \theta_2 = 0.05$ (corresponding to $\sqrt{0.05} \approx 22.4\%$ vol). If the current fast variance is $V_0^{(1)} = 0.06$ (elevated) and the slow variance is $V_0^{(2)} = 0.025$ (near equilibrium), describe the expected evolution of the ATM implied volatility term structure. Will it be in contango or backwardation at short maturities? At long maturities?

??? success "Solution to Exercise 2"
    The expected variance at time $t$ is:

    $$
    \mathbb{E}[V_t] = \mathbb{E}[V_t^{(1)}] + \mathbb{E}[V_t^{(2)}]
    $$

    For each CIR factor, the conditional expectation is:

    $$
    \mathbb{E}[V_t^{(i)}] = \theta_i + (V_0^{(i)} - \theta_i)e^{-\kappa_i t}
    $$

    **Fast factor:** $\mathbb{E}[V_t^{(1)}] = 0.02 + (0.06 - 0.02)e^{-5t} = 0.02 + 0.04e^{-5t}$. This starts at $0.06$ and decays to $0.02$ with half-life $\approx 0.14$ years.

    **Slow factor:** $\mathbb{E}[V_t^{(2)}] = 0.03 + (0.025 - 0.03)e^{-0.5t} = 0.03 - 0.005e^{-0.5t}$. This starts at $0.025$ and slowly rises to $0.03$ over several years.

    **Total expected variance:**

    $$
    \mathbb{E}[V_t] = 0.05 + 0.04e^{-5t} - 0.005e^{-0.5t}
    $$

    At $t = 0$: $V_0 = 0.06 + 0.025 = 0.085$, corresponding to $\sqrt{0.085} \approx 29.2\%$ vol.

    At $t \to \infty$: $V_\infty = 0.05$, corresponding to $\sqrt{0.05} \approx 22.4\%$ vol.

    **Term structure.** At short maturities, the total variance is dominated by the elevated fast factor ($V_0^{(1)} = 0.06 \gg \theta_1 = 0.02$), so current implied vol is high. As the fast factor mean-reverts quickly, the forward variance drops, producing a **backwardation** (downward-sloping) term structure at short maturities.

    At long maturities, the slow factor dominates and is slightly below equilibrium ($V_0^{(2)} = 0.025 < \theta_2 = 0.03$). After the fast factor has decayed, the slow factor's gradual rise produces a mild **contango** (upward slope) at long maturities.

    The overall term structure therefore has a "hump" shape: steeply downward at the short end, then gently upward at the long end.

---

**Exercise 3.** Adding a second variance factor doubles the number of variance parameters from 3 ($\kappa, \theta, \xi$) to 6. Discuss the identifiability challenges: with a typical options surface of 30 quotes, is a 10-parameter model (6 variance + $\rho_1, \rho_2, V_0^{(1)}, V_0^{(2)}$) well-identified? What constraints could you impose to improve identification?

??? success "Solution to Exercise 3"
    **Parameter count analysis.** A two-factor Heston model has 10 parameters: $\kappa_1, \theta_1, \xi_1, \kappa_2, \theta_2, \xi_2, \rho_1, \rho_2, V_0^{(1)}, V_0^{(2)}$. With 30 option quotes, the ratio of data points to parameters is $30/10 = 3$, which is low for a nonlinear optimization problem.

    **Identifiability challenges:**

    - **Factor permutation:** The two factors are exchangeable; swapping all subscripts 1 and 2 gives an identical model. This creates a discrete symmetry in the parameter space.
    - **Parameter correlations:** $\theta_i$ and $V_0^{(i)}$ can partially offset each other, especially when $\kappa_i$ is small and mean reversion is slow.
    - **$\kappa$-$\xi$ tradeoff:** Within each factor, higher $\xi_i$ with higher $\kappa_i$ can produce similar smile shapes.
    - **Limited maturity data:** If options cover only a narrow maturity range, the two time scales may not be separately identifiable.

    **Constraints to improve identification:**

    - Fix one $\kappa$ value (e.g., force $\kappa_1 > 3$ to ensure it is the "fast" factor)
    - Impose an ordering constraint $\kappa_1 > \kappa_2$ to break the permutation symmetry
    - Fix total long-run variance $\theta_1 + \theta_2$ to a value implied by long-dated options
    - Use Tikhonov regularization penalizing large $\xi_i$ values
    - Constrain Feller conditions $2\kappa_i\theta_i \geq \xi_i^2$ to ensure well-posedness
    - Use options across a wide maturity range (1 week to 5 years) to separately identify the two time scales

---

**Exercise 4.** The Fouque-Papanicolaou-Sircar (2000) approach uses asymptotic analysis for multi-scale volatility, treating the fast factor as a perturbation. If $\kappa_1 \to \infty$ (infinitely fast mean reversion), the fast factor averages out and the model reduces to an effective single-factor model. Explain intuitively why the fast factor still affects option prices through corrections to the effective volatility and skew.

??? success "Solution to Exercise 4"
    **Averaging of the fast factor.** When $\kappa_1 \to \infty$, the fast factor $V_t^{(1)}$ mean-reverts infinitely quickly to $\theta_1$. By ergodic averaging, $V_t^{(1)} \approx \theta_1$ at all times, and the total variance effectively becomes $V_t \approx \theta_1 + V_t^{(2)}$.

    However, the fast factor still affects option prices through **second-order corrections**. The key insight from Fouque-Papanicolaou-Sircar is that the fluctuations of the fast factor around its mean, though rapid, systematically modify the effective parameters of the slow model:

    - **Effective volatility correction:** The time-averaged variance is not simply $\theta_1$ but includes a correction proportional to $\xi_1^2 / \kappa_1$, reflecting the variance of the fast factor's fluctuations.
    - **Effective skew correction:** The correlation $\rho_1$ between the asset and the fast factor creates an additional skew contribution proportional to $\rho_1 \xi_1 / \kappa_1$.

    Intuitively, even though the fast factor averages out, the nonlinearity of option payoffs means that fluctuations around the average do not cancel. A call option's convexity in volatility means that symmetric fluctuations above and below the mean raise the option price (Jensen's inequality). Similarly, the correlation between the fast volatility fluctuations and the asset creates systematic skew that persists in the averaged model.

---

**Exercise 5.** Compare the implied volatility surface generated by: (a) a single-factor Heston model with $\kappa = 2$; (b) a two-factor model with $\kappa_1 = 8$, $\kappa_2 = 0.5$, where $\theta_1 + \theta_2 = \theta$ (same total long-run variance). Which model can better match both a steep short-maturity skew and a flatter long-maturity term structure? Justify your answer using the different time scales.

??? success "Solution to Exercise 5"
    **(a) Single-factor Heston ($\kappa = 2$).** The single mean-reversion speed $\kappa = 2$ (half-life $\approx 0.35$ years) determines the term structure of the smile. At short maturities, the smile is influenced by the current variance level. At long maturities, the smile flattens as variance converges to $\theta$. The single time scale means the model cannot independently control the short-term and long-term smile behavior.

    **(b) Two-factor model ($\kappa_1 = 8$, $\kappa_2 = 0.5$).** The fast factor ($\kappa_1 = 8$, half-life $\approx 0.087$ years $\approx 22$ days) generates steep short-maturity skew: a volatility spike today creates large ATM skew for weekly and monthly options but decays rapidly. The slow factor ($\kappa_2 = 0.5$, half-life $\approx 1.4$ years) controls the long-maturity term structure, allowing a flatter but persistent smile at the 1-year horizon and beyond.

    **The two-factor model is superior** for matching both features simultaneously. In the single-factor model, setting $\kappa = 2$ compromises: it is too slow to capture the very steep skew seen in weekly options, yet too fast to generate the persistent smile structure observed at 2-year maturities. The two-factor model separates these roles, with $\kappa_1 = 8$ handling the explosive short-dated behavior and $\kappa_2 = 0.5$ handling the slow mean reversion visible in the term structure.

    Empirically, the volatility surface exhibits exactly this two-scale behavior: steep, rapidly evolving smiles at the short end and stable, slowly moving smiles at the long end.

---

**Exercise 6.** A Markovian lift of a rough volatility model approximates the non-Markovian fractional process with multiple exponential factors:

$$
V_t \approx \sum_{i=1}^n w_i V_t^{(i)}, \quad dV_t^{(i)} = -\lambda_i V_t^{(i)}\,dt + dW_t
$$

with $\lambda_i$ geometrically spaced. Explain why increasing $n$ provides a better approximation to the fractional kernel $K(t) \sim t^{H-1/2}$. For $H = 0.1$ and $n = 3$, suggest an appropriate spacing for $\lambda_1, \lambda_2, \lambda_3$ to cover time scales from days to years.

??? success "Solution to Exercise 6"
    **Why more factors help.** Each Ornstein-Uhlenbeck component $V_t^{(i)}$ has an exponential kernel $e^{-\lambda_i t}$. The weighted sum approximates the fractional kernel:

    $$
    t^{H-1/2} \approx \sum_{i=1}^n w_i e^{-\lambda_i t}
    $$

    This is essentially a Prony-type approximation of a power law by a sum of exponentials. A single exponential can match the power law at one time scale but diverges at others. Each additional exponential adds a new "node" in the approximation, allowing the sum to track the power law across a wider range of time scales.

    Mathematically, as $n \to \infty$ with appropriately chosen weights and rates, the sum converges to the Laplace representation of the power-law kernel:

    $$
    t^{H-1/2} = \frac{1}{\Gamma(H+1/2)}\int_0^\infty \lambda^{-H-1/2}e^{-\lambda t}\,d\lambda
    $$

    More terms provide a finer discretization of this integral.

    **Suggested spacing for $H = 0.1$, $n = 3$.** To cover time scales from days ($\sim 1/252$ years) to years ($\sim 1$ year), we need mean-reversion rates spanning:

    - Fast: $\lambda_1 \approx 252$ (characteristic time $\sim 1$ day)
    - Medium: $\lambda_2 \approx 12$ (characteristic time $\sim 1$ month)
    - Slow: $\lambda_3 \approx 0.5$ (characteristic time $\sim 2$ years)

    A geometric spacing is natural: with ratio $r = (\lambda_1/\lambda_3)^{1/2} \approx (504)^{1/2} \approx 22.4$, set:

    $$
    \lambda_1 \approx 250, \quad \lambda_2 \approx 11, \quad \lambda_3 \approx 0.5
    $$

    The weights $w_i$ are then chosen to minimize the $L^2$ error between $\sum w_i e^{-\lambda_i t}$ and $t^{H-1/2} = t^{-0.4}$ over the relevant time interval.
