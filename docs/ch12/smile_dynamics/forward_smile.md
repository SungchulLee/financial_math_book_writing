# Forward Smile


## Introduction


The **forward smile** describes the implied volatility surface of forward-start options or, equivalently, the conditional distribution of future returns implied by today's option prices. It plays a key role in understanding smile dynamics over time and serves as a powerful diagnostic tool for model validation.

While the spot smile $\sigma_{\text{IV}}(K, T)$ reflects the marginal distribution of $S_T$, the forward smile captures the market's expectation of volatility dynamics at future dates. Understanding forward smiles is essential for pricing and hedging path-dependent exotics, assessing model realism, and trading volatility term structure.

## From Spot Smile to Forward Smile


### 1. The Spot Smile


The **spot implied volatility surface** $\sigma_{\text{IV}}(K, T)$ prices options on the current spot:

$$
C(K, T) = C_{\text{BS}}(S_0, K, T, r, q, \sigma_{\text{IV}}(K, T))
$$


This surface reflects the risk-neutral marginal distribution of $S_T$:

$$
\sigma_{\text{IV}}(K, T) \leftrightarrow \text{Law}^{\mathbb{Q}}(S_T)
$$


### 2. The Forward Smile Definition


The **forward smile** $\sigma_{\text{fwd}}(K, T_1, T_2)$ is the implied volatility surface for options starting at future time $T_1$ and expiring at $T_2$:

$$
\sigma_{\text{fwd}}(K, T_1, T_2) = \text{IV of forward-start option with strike } K \text{ over } [T_1, T_2]
$$


More precisely, it characterizes the conditional distribution:

$$
\sigma_{\text{fwd}}(m, T_1, T_2) \leftrightarrow \text{Law}^{\mathbb{Q}}\left(\frac{S_{T_2}}{S_{T_1}} \bigg| \mathcal{F}_{T_1}\right)
$$


where $m = K/S_{T_1}$ is forward moneyness.

### 3. Mathematical Relationship


For a forward-start call option with payoff:

$$
\text{Payoff} = \left(S_{T_2} - m \cdot S_{T_1}\right)^+
$$


the forward implied volatility $\sigma_{\text{fwd}}$ satisfies:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-rT_2}\left(S_{T_2} - m S_{T_1}\right)^+\right] = C_{\text{BS}}^{\text{fwd}}(m, T_2-T_1, \sigma_{\text{fwd}})
$$


### 4. Variance Perspective


Total variance decomposes additively:

$$
w(T_2) = w(T_1) + w_{\text{fwd}}(T_1, T_2)
$$


where $w(T) = \sigma_{\text{IV}}^2(T) \cdot T$ is total variance. The forward implied volatility is:

$$
\sigma_{\text{fwd}}^2(T_1, T_2) = \frac{w(T_2) - w(T_1)}{T_2 - T_1} = \frac{\sigma_{\text{IV}}^2(T_2) T_2 - \sigma_{\text{IV}}^2(T_1) T_1}{T_2 - T_1}
$$


## Forward-Start Options


### 1. Payoff Structure


A **forward-start option** is a European option whose strike is set at a future date $T_1$:

**Forward-start call:**

$$
\text{Payoff}_{T_2} = \left(S_{T_2} - m \cdot S_{T_1}\right)^+
$$


**Forward-start put:**

$$
\text{Payoff}_{T_2} = \left(m \cdot S_{T_1} - S_{T_2}\right)^+
$$


### 2. Pricing Under Black-Scholes


In Black-Scholes, the ratio $S_{T_2}/S_{T_1}$ is independent of $S_{T_1}$:

$$
\frac{S_{T_2}}{S_{T_1}} = \exp\left((r-q-\sigma^2/2)(T_2-T_1) + \sigma(W_{T_2} - W_{T_1})\right)
$$


**Result:** The forward-start call price is:

$$
C_{\text{fwd}} = S_0 e^{-q T_1} \cdot C_{\text{BS}}^{\text{scaled}}(m, T_2-T_1, \sigma)
$$


**Implication:** Under Black-Scholes, the forward smile equals the spot smile (flat).

## Model-Implied Forward Smiles


### 1. Local Volatility Models


In local volatility models:

$$
dS_t = (r-q) S_t dt + \sigma_{\text{loc}}(S_t, t) S_t dW_t
$$


**Critical issue:** Local vol models imply that the forward smile **flattens rapidly**:

$$
\sigma_{\text{fwd}}(m, T_1, T_2) \to \text{flat as } T_1 \to \infty
$$


This contradicts empirical evidence of persistent forward skew.

### 2. Stochastic Volatility Models (Heston)


The Heston model produces:

- **Persistent skew:** Forward skew remains non-zero due to spot-vol correlation
- **Level depends on $\mathbb{E}[v_{T_1}]$:** Expected future variance determines ATM level

**Approximate forward ATM volatility:**

$$
\sigma_{\text{fwd, ATM}}^2(T_1, T_2) \approx \mathbb{E}[v_{T_1}] + \frac{\xi^2}{4\kappa}(1 - e^{-\kappa(T_2-T_1)})
$$


### 3. SABR Model


The forward smile in SABR depends on the backbone parameter $\beta$:

- $\beta = 1$: Forward smile similar to spot smile
- $\beta = 0$: Forward smile flattens faster

### 4. Bergomi's Variance Curve Model


Bergomi models forward variance directly, providing direct control over forward smile dynamics and realistic behavior.

## Practical Relevance


### 1. Cliquet Pricing


**Cliquet option:** A series of forward-start options with periodic reset:

$$
\text{Payoff} = \sum_{i=1}^{n} f\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right)
$$


Cliquet prices are highly sensitive to the forward smile:

| Model | Cliquet Price | Forward Smile |
|-------|--------------|---------------|
| Black-Scholes | Lowest | Flat |
| Local vol | Low | Flattens |
| Heston | Medium | Persists |

### 2. Forward-Start Products


Forward smiles matter for:

- Cliquets and autocallables
- Long-dated exotics
- Forward-starting variance swaps

### 3. Model Validation


The forward smile is a powerful **model discriminator**:

- Compare model-implied forward smile to market-implied (from cliquets)
- Local vol fails this test
- Stochastic vol performs better

## Summary


- Forward smiles encode conditional future volatility distributions
- They are not directly observable but can be inferred from forward-start products
- **Black-Scholes:** Flat forward smile
- **Local volatility:** Forward smile flattens (unrealistic)
- **Stochastic volatility:** Persistent forward skew
- Forward smile behavior reveals model strengths and weaknesses

---

## Further Reading


- Bergomi, L. *Smile Dynamics* series of papers
- Gatheral, J. *The Volatility Surface*
- Piterbarg, V. *Smiling Hybrids*

---

## Exercises

**Exercise 1.** Define the forward smile $\sigma_{\text{fwd}}(K, T_1, T_2)$ and explain how it differs from the spot smile $\sigma_{\text{IV}}(K, T)$. What type of derivative product depends directly on the forward smile?

??? success "Solution to Exercise 1"
    The **spot smile** $\sigma_{\text{IV}}(K, T)$ is the implied volatility surface observed today for options struck at $K$ expiring at $T$. It encodes the risk-neutral marginal distribution of the terminal spot price $S_T$.

    The **forward smile** $\sigma_{\text{fwd}}(K, T_1, T_2)$ is the implied volatility surface for options that begin at a future date $T_1$ and expire at $T_2$. It encodes the risk-neutral conditional distribution of the return $S_{T_2}/S_{T_1}$ over the future period $[T_1, T_2]$.

    Key differences:

    - The spot smile reflects a single marginal distribution from today to expiry.
    - The forward smile reflects the conditional distribution of future returns, which depends on the joint dynamics of the spot and volatility processes.
    - The forward smile is not directly observable from vanilla option prices; it must be inferred from the spot smile under model assumptions, or extracted from forward-start product prices.

    **Derivative products that depend directly on the forward smile:** Cliquet options (ratchet options) are the primary example. Their payoffs are sums of periodic returns, each of which is a forward-start option. Autocallable structured products and forward-starting variance swaps also depend on the forward smile.

---

**Exercise 2.** The forward variance for the period $[T_1, T_2]$ is $\sigma_{\text{fwd}}^2 = \frac{w(T_2) - w(T_1)}{T_2 - T_1}$. Given total variances $w(0.25) = 0.01$, $w(0.50) = 0.022$, and $w(1.0) = 0.05$, compute the forward variance for periods $[0.25, 0.50]$ and $[0.50, 1.0]$. Is the forward variance term structure upward or downward sloping?

??? success "Solution to Exercise 2"
    The forward variance for a period $[T_1, T_2]$ is:

    $$
    \sigma_{\text{fwd}}^2(T_1, T_2) = \frac{w(T_2) - w(T_1)}{T_2 - T_1}
    $$

    **Period $[0.25, 0.50]$:**

    $$
    \sigma_{\text{fwd}}^2(0.25, 0.50) = \frac{w(0.50) - w(0.25)}{0.50 - 0.25} = \frac{0.022 - 0.01}{0.25} = \frac{0.012}{0.25} = 0.048
    $$

    **Period $[0.50, 1.0]$:**

    $$
    \sigma_{\text{fwd}}^2(0.50, 1.0) = \frac{w(1.0) - w(0.50)}{1.0 - 0.50} = \frac{0.05 - 0.022}{0.50} = \frac{0.028}{0.50} = 0.056
    $$

    The forward variance increases from 0.048 for the $[0.25, 0.50]$ period to 0.056 for the $[0.50, 1.0]$ period. The forward variance term structure is **upward sloping**.

    For comparison, the spot implied variances are $w(0.25)/0.25 = 0.04$ and $w(0.50)/0.50 = 0.044$ and $w(1.0)/1.0 = 0.05$. The upward-sloping forward variance curve is consistent with a market that prices increasing uncertainty at longer horizons. This is the typical shape in calm market conditions for equity indices.

---

**Exercise 3.** In local volatility models, the forward smile tends to flatten as $T_1$ increases. Explain this by considering how the local volatility surface determines the forward-implied distribution. Why is this "forward smile flattening" inconsistent with empirical observations?

??? success "Solution to Exercise 3"
    In a local volatility model, the dynamics are $dS_t = (r-q)S_t \, dt + \sigma_{\text{loc}}(S_t, t) S_t \, dW_t$, where $\sigma_{\text{loc}}(S, t)$ is a deterministic function. The forward-implied distribution for $S_{T_2}/S_{T_1}$ is determined by integrating the local volatility surface over the period $[T_1, T_2]$.

    **Why the forward smile flattens:** The key insight is that local vol is a one-factor model with no stochastic volatility. By time $T_1$, the spot $S_{T_1}$ has diffused over a range of values, and for each realization of $S_{T_1}$, the conditional dynamics over $[T_1, T_2]$ are driven by $\sigma_{\text{loc}}(S, t)$ evaluated near $S_{T_1}$. Averaging over all possible $S_{T_1}$ realizations produces a forward-implied distribution that is a mixture of lognormals, each with a slightly different local vol. This mixing effect smooths out the smile: the skew and curvature that were present in the short-dated spot smile get averaged away, producing a flatter forward smile.

    Mathematically, as $T_1$ increases, the distribution of $S_{T_1}$ broadens, and the averaging effect becomes stronger, driving the forward smile toward flat.

    **Why this is inconsistent with empirical observations:** Empirically, forward smiles retain significant skew. The options market prices persistent skew for forward-start products, implying that the conditional return distribution maintains fat tails and asymmetry regardless of the forward start date. This persistence is driven by stochastic volatility: the volatility process has memory, and its future level is uncertain, preserving the forward smile shape. Local vol, being a deterministic volatility model, cannot generate this persistence.

---

**Exercise 4.** Stochastic volatility models (e.g., Heston) preserve a forward smile because the volatility process has memory. If the Heston model has $\rho = -0.7$ and $\xi = 0.4$, describe qualitatively how the forward smile for the period $[1, 2]$ years compares to the spot smile for $T = 1$ year. Is the forward skew steeper or flatter?

??? success "Solution to Exercise 4"
    In the Heston model with $\rho = -0.7$ and $\xi = 0.4$, the forward smile for the period $[1, 2]$ years preserves a non-trivial shape due to the stochastic volatility process.

    **Qualitative comparison to the spot smile for $T = 1$ year:**

    - **ATM level:** The forward ATM vol is determined by $\mathbb{E}[v_1]$, the expected variance at $T_1 = 1$. Under Heston, $\mathbb{E}[v_t] = \theta + (v_0 - \theta)e^{-\kappa t}$, so the forward ATM level depends on mean reversion. If $v_0 > \theta$, the forward ATM vol is lower than the spot ATM vol for $T = 1$.
    - **Skew:** The forward skew is **flatter** than the spot skew for $T = 1$. The spot skew for a 1-year option benefits from the full correlation effect between spot and variance over one year starting from a known $v_0$. The forward smile, however, conditions on $v_1$, which is uncertain. The averaging over uncertain $v_1$ realizations somewhat dampens the skew, though $\rho = -0.7$ still ensures meaningful negative skew persists.
    - **Curvature:** The forward smile retains curvature (smile wings) because the vol-of-vol $\xi = 0.4$ generates variability in the forward variance, producing fat tails in the conditional return distribution.

    Overall, the forward skew is flatter than the corresponding spot skew but remains significantly non-zero, which is a key advantage of stochastic volatility over local volatility.

---

**Exercise 5.** A cliquet option pays the sum of capped and floored periodic returns: $\sum_{i=1}^n \min(\max(R_i, \text{floor}), \text{cap})$ where $R_i = S_{t_i}/S_{t_{i-1}} - 1$. Explain why the pricing of this product depends critically on the forward smile for each period $[t_{i-1}, t_i]$. Would a local vol model overprice or underprice this product relative to a stochastic vol model?

??? success "Solution to Exercise 5"
    The cliquet pays $\sum_{i=1}^n \min(\max(R_i, \text{floor}), \text{cap})$ where $R_i = S_{t_i}/S_{t_{i-1}} - 1$. Each term in the sum is a function of the return over $[t_{i-1}, t_i]$, which is equivalent to a forward-start option. The price of each periodic payoff depends on the forward smile for that period because:

    - The forward smile determines the risk-neutral distribution of $R_i$.
    - The cap is triggered when $R_i$ exceeds the cap level, and the probability of this event depends on the right tail of the forward-implied distribution.
    - The floor is triggered when $R_i$ falls below the floor level, and this probability depends on the left tail.
    - The expected capped/floored return depends on the full shape of the forward smile, not just ATM vol.

    **Local vol vs. stochastic vol:** A local volatility model **underprices** the cliquet relative to a stochastic volatility model. The reasoning:

    1. Local vol's forward smile flattens, implying thinner tails for the forward return distribution.
    2. Thinner tails mean lower probabilities of triggering both the cap and the floor.
    3. For a typical cliquet with an asymmetric payoff profile (the floor provides significant value), the reduced left tail undervalues the floor protection.
    4. Additionally, the flatter forward smile implies lower variance for periodic returns, reducing the optionality value of each period.
    5. In stochastic vol models, the persistent forward skew and fatter tails produce higher cliquet prices because the periodic payoffs retain more optionality.

---

**Exercise 6.** The forward smile can be used as a diagnostic tool for model selection. Describe a procedure to compare the forward smiles of two candidate models (local vol and Heston) against market-implied forward smiles extracted from variance swap curves and cliquet prices. What data sources would you need?

??? success "Solution to Exercise 6"
    **Procedure for comparing forward smiles:**

    **Step 1: Extract market-implied forward smile information.**

    - Obtain variance swap curves from the market: the fair strikes $K_{\text{var}}(T)$ for a range of maturities $T$.
    - Compute forward variances: $K_{\text{var}}^{\text{fwd}}(T_1, T_2) = \frac{K_{\text{var}}(T_2) T_2 - K_{\text{var}}(T_1) T_1}{T_2 - T_1}$.
    - If available, obtain cliquet or forward-start option prices from dealer quotes or structured product markets.

    **Step 2: Calibrate both candidate models to today's spot smile.**

    - Calibrate the local vol model (Dupire) to the full vanilla surface.
    - Calibrate the Heston model to the same surface (possibly with some fitting error).

    **Step 3: Compute model-implied forward smiles.**

    - For each model, simulate paths to $T_1$ and compute the conditional distribution of $S_{T_2}/S_{T_1}$ via Monte Carlo.
    - Convert these conditional distributions into forward implied volatility smiles $\sigma_{\text{fwd}}^{\text{model}}(m, T_1, T_2)$.

    **Step 4: Compare.**

    - Compare model-implied forward ATM vol to the market-implied forward variance from variance swaps.
    - Compare model-implied forward smile shape (skew and curvature) to the shape implied by cliquet prices.
    - Compute RMSE or other distance metrics between model and market forward smiles.

    **Data sources needed:**

    - Vanilla option prices across strikes and maturities (for calibration)
    - Variance swap curves (for forward variance benchmarks)
    - Cliquet or forward-start option quotes (for forward smile shape validation)
    - Historical data on forward smile evolution (for backtesting)

---

**Exercise 7.** Consider a variance swap starting in 6 months with a 6-month tenor. Using the forward variance formula, compute the fair strike given that the 6-month variance swap strike is 0.04 and the 1-year variance swap strike is 0.038. Compare this to the 6-month spot variance swap strike and explain the economic interpretation of the difference.

??? success "Solution to Exercise 7"
    The forward variance swap starting at $T_1 = 0.5$ years with tenor $T_2 - T_1 = 0.5$ years (expiring at $T_2 = 1.0$ years) has fair strike:

    $$
    K_{\text{var}}^{\text{fwd}}(T_1, T_2) = \frac{K_{\text{var}}(T_2) \cdot T_2 - K_{\text{var}}(T_1) \cdot T_1}{T_2 - T_1}
    $$

    Substituting $K_{\text{var}}(0.5) = 0.04$, $K_{\text{var}}(1.0) = 0.038$:

    $$
    K_{\text{var}}^{\text{fwd}} = \frac{0.038 \times 1.0 - 0.04 \times 0.5}{1.0 - 0.5} = \frac{0.038 - 0.020}{0.5} = \frac{0.018}{0.5} = 0.036
    $$

    **Comparison:** The 6-month spot variance swap strike is $K_{\text{var}}(0.5) = 0.04$, while the 6-month forward variance swap strike (starting in 6 months) is $K_{\text{var}}^{\text{fwd}} = 0.036$.

    **Economic interpretation:** The forward variance strike ($0.036$) is lower than the spot variance strike ($0.04$). This indicates that the market expects variance to decrease over the next 6 months. The current 6-month implied variance is elevated (possibly due to near-term uncertainty or a recent vol spike), and the market prices in mean reversion: the second half of the year is expected to be calmer than the first half. In implied vol terms, the forward vol is $\sqrt{0.036} \approx 19.0\%$ versus the spot 6-month vol of $\sqrt{0.04} = 20.0\%$.

    Note that the 1-year variance swap strike ($0.038$) is lower than the 6-month strike ($0.04$), reflecting a downward-sloping variance swap term structure. This is characteristic of a market in an elevated vol regime where mean reversion pulls long-dated vol expectations below current short-dated levels.
