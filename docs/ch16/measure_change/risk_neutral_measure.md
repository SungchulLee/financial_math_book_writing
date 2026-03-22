# Risk-Neutral Measure for the Heston Model

The Heston model operates in an incomplete market: the variance process $v_t$ introduces a source of randomness that cannot be hedged by trading in the stock and bond alone. Passing from the physical measure $\mathbb{P}$ to a risk-neutral measure $\mathbb{Q}$ requires specifying a market price of risk for both the stock Brownian motion and the variance Brownian motion. The choice of the variance risk premium determines the risk-neutral dynamics and therefore all derivative prices. This section derives the Girsanov measure change for the Heston model and establishes how each physical parameter transforms under $\mathbb{Q}$.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Apply Girsanov's theorem to the two-dimensional Heston SDE
    2. Derive the risk-neutral dynamics and identify which parameters change under $\mathbb{Q}$
    3. Explain why the Heston market is incomplete and what freedom remains in choosing $\mathbb{Q}$
    4. Connect the volatility risk premium to the parameter transformation $\kappa \to \kappa^*$

---

## Intuition

Under the physical measure $\mathbb{P}$, the stock has a drift $\mu$ reflecting the expected return demanded by investors, and the variance process has mean-reversion parameters $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}})$ reflecting the physical dynamics of realized volatility. To price derivatives, we need a measure $\mathbb{Q}$ under which the discounted stock price is a martingale. Girsanov's theorem achieves this by adjusting the drift of each Brownian motion, but in the Heston model there are two Brownian motions and only one stock to hedge. This leaves one degree of freedom --- the market price of variance risk $\lambda_v$ --- that must be specified externally (from market data, economic arguments, or calibration to option prices).

---

## Physical Dynamics

Under the physical measure $\mathbb{P}$, the Heston model specifies

$$
dS_t = \mu S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1), \mathbb{P}}
$$

$$
dv_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2), \mathbb{P}}
$$

with $d\langle W^{(1), \mathbb{P}}, W^{(2), \mathbb{P}} \rangle_t = \rho \, dt$.

The five physical parameters are:

| Parameter | Symbol | Interpretation |
|-----------|--------|---------------|
| Expected return | $\mu$ | Drift of the stock under $\mathbb{P}$ |
| Mean-reversion speed | $\kappa^{\mathbb{P}}$ | Rate at which $v_t$ reverts to $\theta^{\mathbb{P}}$ |
| Long-run variance | $\theta^{\mathbb{P}}$ | Stationary level of $v_t$ under $\mathbb{P}$ |
| Vol-of-vol | $\xi$ | Volatility of the variance process |
| Correlation | $\rho$ | Leverage effect |

---

## Girsanov's Theorem for Two-Dimensional Diffusions

To change from $\mathbb{P}$ to $\mathbb{Q}$, define the market prices of risk $\lambda_S(t)$ and $\lambda_v(t)$ and the Radon-Nikodym derivative

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \exp\!\left(-\int_0^T \lambda_S(t) \, dW_t^{(1), \mathbb{P}} - \int_0^T \lambda_v(t) \, dW_t^{(2), \mathbb{P}} - \frac{1}{2}\int_0^T (\lambda_S^2(t) + \lambda_v^2(t)) \, dt\right)
$$

!!! info "Theorem (Girsanov for Heston)"
    Under the change of measure defined above, the $\mathbb{Q}$-Brownian motions are

    $$
    dW_t^{(1), \mathbb{Q}} = dW_t^{(1), \mathbb{P}} + \lambda_S(t) \, dt
    $$

    $$
    dW_t^{(2), \mathbb{Q}} = dW_t^{(2), \mathbb{P}} + \lambda_v(t) \, dt
    $$

    provided the Novikov condition $\mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T(\lambda_S^2 + \lambda_v^2) \, dt\right)\right] < \infty$ holds.

The correlation is preserved: $d\langle W^{(1),\mathbb{Q}}, W^{(2),\mathbb{Q}} \rangle_t = \rho \, dt$.

---

## Determining the Stock Market Price of Risk

The discounted stock price $\tilde{S}_t = e^{-rt} S_t$ must be a $\mathbb{Q}$-martingale. Substituting $dW_t^{(1),\mathbb{P}} = dW_t^{(1),\mathbb{Q}} - \lambda_S dt$ into the stock SDE:

$$
dS_t = \mu S_t \, dt + \sqrt{v_t} \, S_t \left(dW_t^{(1),\mathbb{Q}} - \lambda_S \, dt\right)
$$

$$
= (\mu - \lambda_S \sqrt{v_t}) S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1),\mathbb{Q}}
$$

For $\tilde{S}_t$ to be a $\mathbb{Q}$-martingale, the drift must equal $rS_t$:

$$
\mu - \lambda_S \sqrt{v_t} = r
$$

!!! info "Proposition (Stock Market Price of Risk)"
    The no-arbitrage condition uniquely determines

    $$
    \lambda_S(t) = \frac{\mu - r}{\sqrt{v_t}}
    $$

    This is the equity risk premium per unit of volatility, the analogue of the Sharpe ratio.

---

## Freedom in the Variance Market Price of Risk

The variance process is not a traded asset, so there is no no-arbitrage restriction on $\lambda_v$. This is the source of **market incompleteness** in the Heston model.

!!! warning "Market Incompleteness"
    The Heston model has two sources of randomness ($W^{(1)}$ and $W^{(2)}$) but only two traded assets (stock and bond). Since the stock loads on both Brownian motions (through $\rho$), it provides partial hedging of variance risk, but the component of $W^{(2)}$ orthogonal to $W^{(1)}$ is unhedgeable. The choice of $\lambda_v$ represents the market's pricing of this unhedgeable variance risk.

**Common specifications for $\lambda_v$:**

1. **Proportional to $\sqrt{v_t}$**: $\lambda_v(t) = \lambda \sqrt{v_t}$ for a constant $\lambda$. This preserves the affine structure and is the standard assumption.
2. **Constant**: $\lambda_v(t) = \lambda_0$. This breaks the CIR structure of the variance process under $\mathbb{Q}$.
3. **Zero**: $\lambda_v = 0$. The minimal choice, but inconsistent with observed option prices.

We adopt the standard specification $\lambda_v(t) = \lambda \sqrt{v_t}$, which preserves the Heston model's affine structure under $\mathbb{Q}$.

---

## Risk-Neutral Dynamics

Substituting $dW_t^{(2),\mathbb{P}} = dW_t^{(2),\mathbb{Q}} - \lambda\sqrt{v_t} \, dt$ into the variance SDE:

$$
dv_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - v_t) \, dt + \xi\sqrt{v_t}\left(dW_t^{(2),\mathbb{Q}} - \lambda\sqrt{v_t}\,dt\right)
$$

$$
= \left[\kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - v_t) - \xi\lambda v_t\right] dt + \xi\sqrt{v_t} \, dW_t^{(2),\mathbb{Q}}
$$

$$
= \left[\kappa^{\mathbb{P}}\theta^{\mathbb{P}} - (\kappa^{\mathbb{P}} + \xi\lambda)v_t\right] dt + \xi\sqrt{v_t} \, dW_t^{(2),\mathbb{Q}}
$$

!!! info "Theorem (Risk-Neutral Heston Dynamics)"
    Under the risk-neutral measure $\mathbb{Q}$, the Heston model is

    $$
    dS_t = (r - q) S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1), \mathbb{Q}}
    $$

    $$
    dv_t = \kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2), \mathbb{Q}}
    $$

    where the risk-neutral parameters are

    $$
    \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \xi\lambda, \qquad \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}} \theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \xi\lambda}
    $$

    The vol-of-vol $\xi$ and correlation $\rho$ are **unchanged** by the measure change.

---

## Parameter Transformation Summary

| Parameter | Under $\mathbb{P}$ | Under $\mathbb{Q}$ | Change |
|-----------|-------------------|-------------------|--------|
| Stock drift | $\mu$ | $r - q$ | Fixed by no-arbitrage |
| Mean-reversion speed | $\kappa^{\mathbb{P}}$ | $\kappa^{\mathbb{P}} + \xi\lambda$ | Increased if $\lambda > 0$ |
| Long-run variance | $\theta^{\mathbb{P}}$ | $\kappa^{\mathbb{P}}\theta^{\mathbb{P}} / \kappa^{\mathbb{Q}}$ | Decreased if $\lambda > 0$ |
| Vol-of-vol | $\xi$ | $\xi$ | Unchanged |
| Correlation | $\rho$ | $\rho$ | Unchanged |

!!! note "Preservation of Affine Structure"
    The risk-neutral dynamics retain the CIR form for $v_t$, so the Heston characteristic function is still available in closed form under $\mathbb{Q}$. This is the key advantage of the $\lambda_v = \lambda\sqrt{v_t}$ specification: any other functional form would destroy the affine structure and the analytical tractability.

---

## Feller Condition Under Measure Change

The Feller condition for strict positivity of $v_t$ under $\mathbb{Q}$ is

$$
2\kappa^{\mathbb{Q}} \theta^{\mathbb{Q}} \geq \xi^2
$$

Substituting the risk-neutral parameters:

$$
2\kappa^{\mathbb{P}}\theta^{\mathbb{P}} \geq \xi^2
$$

This is the **same** condition as under $\mathbb{P}$. The measure change does not affect whether the Feller condition is satisfied, because $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$.

---

## Numerical Example

Consider physical parameters $\mu = 0.08$, $\kappa^{\mathbb{P}} = 3.0$, $\theta^{\mathbb{P}} = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $v_0 = 0.04$, $r = 0.05$, $q = 0$.

**Step 1: Stock market price of risk.**

$$
\lambda_S(t) = \frac{0.08 - 0.05}{\sqrt{v_t}} = \frac{0.03}{\sqrt{v_t}}
$$

At $v_0 = 0.04$: $\lambda_S = 0.03/0.2 = 0.15$.

**Step 2: Variance risk premium.** Suppose calibration to option prices reveals $\lambda = 1.0$ (a positive variance risk premium, meaning investors pay a premium to be long variance).

**Step 3: Risk-neutral parameters.**

$$
\kappa^{\mathbb{Q}} = 3.0 + 0.3 \times 1.0 = 3.3
$$

$$
\theta^{\mathbb{Q}} = \frac{3.0 \times 0.04}{3.3} = 0.0364
$$

The risk-neutral mean-reversion is faster ($\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$) and the risk-neutral long-run variance is lower ($\theta^{\mathbb{Q}} < \theta^{\mathbb{P}}$). Both effects are consistent with the empirical observation that variance under $\mathbb{Q}$ mean-reverts faster to a lower level than under $\mathbb{P}$.

**Step 4: Feller condition check.**

$$
2\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = 2(3.3)(0.0364) = 0.240 \geq 0.09 = \xi^2
$$

The condition is satisfied.

??? example "Impact on Option Prices"
    Computing the ATM call ($K = 100$, $\tau = 1$) under both measures:

    - Using risk-neutral parameters $(\kappa^{\mathbb{Q}} = 3.3, \theta^{\mathbb{Q}} = 0.0364)$: Call = \$7.82
    - Using physical parameters $(\kappa^{\mathbb{P}} = 3.0, \theta^{\mathbb{P}} = 0.04)$ with drift $\mu = 0.08$: the "physical" call is not well-defined as a derivative price, but the expected payoff $e^{-\mu\tau}\mathbb{E}^{\mathbb{P}}[(S_T - K)^+]$ would differ due to the higher drift and different variance dynamics.

    The difference illustrates that derivative prices depend on the risk-neutral measure, not the physical dynamics.

---

## Summary

The passage from the physical measure $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$ in the Heston model is achieved via Girsanov's theorem with two market prices of risk: $\lambda_S = (\mu - r)/\sqrt{v_t}$ (uniquely determined by no-arbitrage) and $\lambda_v = \lambda\sqrt{v_t}$ (free parameter reflecting market incompleteness). The standard specification $\lambda_v \propto \sqrt{v_t}$ preserves the affine structure, transforming $\kappa^{\mathbb{P}} \to \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \xi\lambda$ and $\theta^{\mathbb{P}} \to \theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$ while leaving $\xi$, $\rho$, and the Feller condition unchanged. The freedom in choosing $\lambda$ reflects the market's pricing of unhedgeable variance risk and is resolved in practice through calibration to observed option prices.
