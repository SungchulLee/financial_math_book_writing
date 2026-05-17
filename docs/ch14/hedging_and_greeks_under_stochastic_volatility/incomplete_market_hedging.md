# Incomplete Market Hedging


Stochastic volatility models operate in **incomplete markets**: not all sources of risk can be hedged using traded assets. This fundamentally changes hedging theory and practice.

---

## Why markets are incomplete


Recall (see [§ General SV framework](../general_stochastic_volatility_framework/correlation_and_leverage_effect.md)): volatility is not directly tradable and variance shocks introduce a second Brownian factor, so delta hedging alone cannot eliminate uncertainty and perfect replication is impossible.

---

## Consequences for hedging


In an incomplete market:

- hedging strategies are not unique,
- residual risk remains even after optimal hedging,
- hedging performance depends on chosen objective.

This contrasts sharply with Black–Scholes replication.

---

## Common hedging instruments


Practitioners attempt to reduce incompleteness using:

- options of different strikes/maturities (vega hedging),
- variance swaps or volatility indices (when available),
- dynamic rebalancing across the surface.

Still, some risks remain irreducible.

---

## Hedging error as a random variable


Recall (see [§ Hedging errors](../../ch11/hedging_errors/asymptotic_hedging_error_expansions.md)): hedging error is a random variable; risk management focuses on its distribution, tail risk, and robustness across scenarios. Under SV, the decomposition becomes

$$
\text{P&L}_{\text{hedge}} = \text{model error} + \text{unhedgeable variance risk}.
$$

---

## Key takeaways


- Stochastic volatility implies incomplete markets.
- Hedging aims to reduce, not eliminate, risk.
- Residual risk must be measured and managed explicitly.

---

## Further reading


- Schweizer, mean–variance hedging.
- Cont, *Model Uncertainty and Its Impact on Pricing*.

---

## Exercises

**Exercise 1.** In the Heston model, the stock and bond provide two instruments, but there are two sources of risk ($W^S$ and $W^V$). Explain the dimension mismatch and why a single traded option (in addition to the stock and bond) would restore market completeness. What properties must this option have to be useful as a hedging instrument?

??? success "Solution to Exercise 1"
    In the Heston model the stock price and variance satisfy

    $$
    dS_t = \mu S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S
    $$

    $$
    dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V
    $$

    where $W^S$ and $W^V$ are (correlated) Brownian motions. There are **two sources of randomness** ($W^S$ and $W^V$) but only **two traded instruments** (stock and bond). Since the bond is riskless, only the stock provides a risky payoff, leaving one source of risk unhedged. This is the dimension mismatch: two risk factors versus one risky instrument.

    Adding a single traded option $O(S, V, t)$ whose price depends on both $S$ and $V$ introduces a second risky instrument. By Ito's lemma, $dO$ loads on both $dW^S$ and $dW^V$. A portfolio of the stock, the option, and the bond can then be constructed to neutralize both sources of risk simultaneously, restoring completeness.

    For the option to be useful as a hedging instrument, it must have **non-degenerate sensitivity to the variance factor** — that is, its vega (sensitivity to $V$) must be materially non-zero. A deep-in-the-money option with negligible vega would be nearly redundant with the stock. In practice, ATM or slightly OTM options with sufficient maturity are preferred because they carry significant volatility exposure.

---

**Exercise 2.** A trader is short a 3-month ATM call on the S&P 500 and delta-hedges using the underlying. Under the Heston model with $\rho = -0.7$ and $\xi = 0.5$, explain qualitatively why the hedging P&L will have non-zero variance even with continuous rebalancing. Decompose the residual risk into (a) volatility risk and (b) correlation risk.

??? success "Solution to Exercise 2"
    Under the Heston model, the stock price is driven by $W^S$ and the variance process by $W^V$, with $\text{Corr}(dW^S, dW^V) = \rho = -0.7$. Delta hedging with the underlying neutralizes exposure to $dW^S$ only at the level of first-order spot moves, but it leaves the portfolio exposed to:

    **(a) Volatility risk:** The variance $V_t$ evolves randomly through $dW^V$. With $\xi = 0.5$, variance shocks are substantial. Even with continuous delta rebalancing, the portfolio's value depends on the path of $V_t$, which is unhedged. This is the primary source of residual risk.

    **(b) Correlation risk:** Because $\rho = -0.7$, spot drops are strongly associated with volatility spikes. The Black-Scholes delta (computed at a fixed implied vol) does not account for the simultaneous move in volatility when the spot moves. When the spot falls, volatility rises, making the option more expensive than the delta hedge anticipated. This correlation-induced mismatch contributes additional P&L variance.

    With $|\rho| < 1$, the variance process has an independent component orthogonal to the stock. Even the part correlated with the stock creates hedging error because delta is computed at a fixed volatility rather than the stochastic one. Continuous delta rebalancing eliminates diffusion risk from $dW^S$ only under the assumption of constant volatility. In the Heston model that assumption fails, so the hedging P&L retains non-zero variance.

---

**Exercise 3.** Consider the hedging error decomposition

$$
\text{P\&L}_{\text{hedge}} = \text{Gamma P\&L} + \text{Vega P\&L} + \text{higher-order terms}
$$

If the trader uses Black-Scholes delta to hedge, the gamma P&L depends on $(\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)$. In a stochastic volatility world, $\sigma_{\text{realized}}$ is itself random. Explain why this makes the gamma P&L a random variable with non-zero variance, and contrast with the Black-Scholes case where gamma P&L has zero variance under continuous hedging.

??? success "Solution to Exercise 3"
    In the Black-Scholes model, volatility is constant ($\sigma_{\text{realized}} = \sigma_{\text{implied}} = \sigma$), so under continuous hedging the gamma P&L over an infinitesimal interval is

    $$
    \frac{1}{2}\Gamma S^2(\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)\,dt = 0
    $$

    The cumulative gamma P&L is zero with probability one — there is no randomness.

    In a stochastic volatility world, $\sigma_{\text{realized}}$ over any finite interval is a random variable because the instantaneous variance $V_t$ follows its own diffusion. The gamma P&L becomes

    $$
    \frac{1}{2}\Gamma S^2(V_t - \sigma_{\text{implied}}^2)\,dt
    $$

    at each instant. Since $V_t$ is random, this quantity is random even when delta is rebalanced continuously. Over the life of the option, the integrated gamma P&L depends on the entire path of $V_t$, which has non-zero variance.

    Furthermore, the trader uses Black-Scholes delta, which is computed at the fixed implied volatility $\sigma_{\text{implied}}$, not at the true instantaneous volatility $\sqrt{V_t}$. This means the hedge ratio itself is systematically incorrect whenever $V_t \neq \sigma_{\text{implied}}^2$, compounding the randomness of the gamma P&L. The variance of the gamma P&L is directly related to $\text{Var}[V_t]$ and hence to the vol-of-vol parameter $\xi$.

---

**Exercise 4.** A portfolio manager uses variance swaps to partially hedge volatility risk. The variance swap payoff is $\text{RV}^2 - K_{\text{var}}$, where $\text{RV}$ is realized volatility and $K_{\text{var}}$ is the strike. Explain how adding a variance swap to a delta-hedged option position reduces the incompleteness of the market. Does a single variance swap fully complete the market under the Heston model? Why or why not?

??? success "Solution to Exercise 4"
    A variance swap pays $\text{RV}^2 - K_{\text{var}}$ at maturity, where $\text{RV}^2$ is the realized variance. Under the Heston model, realized variance is

    $$
    \text{RV}^2 = \frac{1}{T}\int_0^T V_t\,dt
    $$

    which is an integral functional of the variance process. Adding a variance swap to a delta-hedged option position provides direct exposure to the integrated variance, allowing the trader to offset the portfolio's sensitivity to the level of realized variance.

    After delta hedging (which handles $dW^S$ risk) and adding the variance swap (which hedges the average level of $V_t$), the portfolio is less sensitive to both risk factors. This reduces incompleteness because the variance swap spans a direction in payoff space that is not reachable through the stock alone.

    However, a single variance swap does **not** fully complete the market under Heston. The reasons are:

    - The variance swap hedges the *integrated* (average) variance, not the *instantaneous* variance path. The option price depends on the entire joint distribution of $(S_t, V_t)$, not just on $\int V_t\,dt$.
    - Path-dependent features such as the correlation between spot and variance moves, the timing of variance shocks, and higher moments of the variance distribution are not captured by a single variance swap.
    - To fully complete the market, one would need a continuum of variance-sensitive instruments or at least one additional option that provides sufficient exposure to the independent component of $dW^V$ at each instant.

    In practice, the variance swap significantly reduces volatility risk but leaves residual exposure to vol-of-vol, correlation, and term-structure effects.

---

**Exercise 5.** In an incomplete market, the hedging strategy that minimizes $\mathbb{E}[(H - V_T^\pi)^2]$ is called the mean-variance optimal hedge. Explain why this hedge depends on the risk-neutral measure $\mathbb{Q}$ chosen. If two practitioners use different models (and hence different $\mathbb{Q}$s) but the same instruments, will they arrive at the same hedge? What practical issue does this raise?

??? success "Solution to Exercise 5"
    The mean-variance optimal hedge minimizes $\mathbb{E}[(H - V_T^\pi)^2]$, which can be expanded as

    $$
    \mathbb{E}[(H - V_T^\pi)^2] = \bigl(\mathbb{E}[H - V_T^\pi]\bigr)^2 + \text{Var}[H - V_T^\pi]
    $$

    The expectation and variance are computed under the physical measure $\mathbb{P}$, but the initial cost of the hedging portfolio (and hence $V_0^\pi$) is determined by the risk-neutral pricing measure $\mathbb{Q}$. In an incomplete market, $\mathbb{Q}$ is not unique — there is a family of equivalent martingale measures, each corresponding to a different price for volatility risk.

    Different choices of $\mathbb{Q}$ lead to different initial option prices $V_0^\pi$, different drift adjustments in the hedging dynamics, and therefore different optimal hedge ratios $\pi^*$. The optimal hedge is the projection of the payoff $H$ onto the space of replicable payoffs, and this projection depends on the inner product structure induced by $\mathbb{Q}$.

    If two practitioners use different models (and hence different $\mathbb{Q}$s) but the same instruments, they will generally arrive at **different hedges**. Even if both models fit the current option prices exactly, they imply different dynamics for the volatility surface and different market prices of volatility risk. This leads to different delta and vega hedge ratios.

    The practical issue this raises is **model risk**: the hedging strategy is sensitive to modeling choices that cannot be uniquely determined from market prices alone. Risk managers must account for the range of plausible hedges across reasonable models, not just the hedge from a single calibration.

---

**Exercise 6.** Explain why the concept of "model error" is especially important in incomplete markets. In a complete market, any model that is arbitrage-free and fits market prices produces the same hedging strategy. In an incomplete market, different models produce different hedges even when they fit the same prices. Describe a scenario where two Heston calibrations with identical fit quality lead to materially different hedging strategies.

??? success "Solution to Exercise 6"
    In a complete market, the replicating portfolio is uniquely determined by the requirement that the hedged portfolio is self-financing and matches the payoff. Any arbitrage-free model that reproduces observed prices will yield the same hedge ratios because there is only one equivalent martingale measure.

    In an incomplete market, multiple equivalent martingale measures exist, each consistent with observed prices. Different models correspond to different choices of measure, and each choice implies different dynamics for unobservable quantities (e.g., the market price of volatility risk). Since hedging strategies depend on these dynamics, different models produce different hedges — even when they fit the same market data equally well.

    **Scenario with two Heston calibrations:** Consider calibrating the Heston model to the same set of European option prices on the S&P 500. Two calibrations may achieve the same root-mean-square pricing error but with different parameter sets:

    - Calibration A: $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.65$, $V_0 = 0.04$
    - Calibration B: $\kappa = 4.0$, $\theta = 0.05$, $\xi = 0.6$, $\rho = -0.80$, $V_0 = 0.035$

    Both fit today's vanilla surface well, but they imply very different forward dynamics. Calibration B has faster mean reversion, higher vol-of-vol, and stronger leverage effect. When hedging a long-dated barrier option:

    - Calibration A implies moderate vega and lower vanna, leading to a smaller volatility hedge ratio.
    - Calibration B implies that volatility is more reactive and more correlated with spot, leading to a significantly larger vanna and vega hedge.

    The two hedging strategies can differ materially in the notional of options used for vega hedging, the frequency of rebalancing, and the expected residual P&L distribution. This demonstrates that model error — the uncertainty in choosing the right model — directly translates into hedging uncertainty, making it a first-order concern in incomplete markets.
