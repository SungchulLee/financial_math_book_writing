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

To change from $\mathbb{P}$ to $\mathbb{Q}$, define the market prices of risk $\lambda_S(t)$ and $\lambda_v(t)$ and the Radon–Nikodym derivative

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

---

## Exercises

**Exercise 1.**
The stock market price of risk is $\lambda_S(t) = (\mu - r)/\sqrt{v_t}$. Explain why this diverges as $v_t \to 0$. Under the Feller condition ($2\kappa\theta \geq \xi^2$), the variance stays strictly positive, so $\lambda_S$ remains finite. What happens to the Novikov condition when the Feller condition is violated and $v_t$ can reach zero?

??? success "Solution to Exercise 1"
    The stock market price of risk is $\lambda_S(t) = (\mu - r)/\sqrt{v_t}$. As $v_t \to 0^+$, we have $\sqrt{v_t} \to 0$ and thus $\lambda_S(t) \to \pm\infty$ (depending on the sign of $\mu - r$). This divergence creates a problem for the Girsanov measure change because the Novikov condition requires

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \lambda_S^2(t)\,dt\right)\right] = \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{(\mu-r)^2}{2}\int_0^T \frac{1}{v_t}\,dt\right)\right] < \infty
    $$

    When the Feller condition $2\kappa\theta \geq \xi^2$ is satisfied, the CIR process $v_t$ remains strictly positive almost surely. In this case, $1/v_t$ stays finite on $[0,T]$, and the integral $\int_0^T v_t^{-1}\,dt$ is finite almost surely. Under additional integrability conditions (which hold for typical Heston parameters), the Novikov condition is satisfied and the measure change is well-defined.

    When the Feller condition is violated ($2\kappa\theta < \xi^2$), the variance process can reach zero. Near $v_t = 0$, the integrand $1/v_t$ explodes, and the integral $\int_0^T v_t^{-1}\,dt$ may diverge. Specifically, for a CIR process that touches zero, the time spent near zero contributes a divergent integral of $1/v_t$, causing $\int_0^T \lambda_S^2\,dt = \infty$ with positive probability.

    When this integral is infinite, the stochastic exponential defining the Radon–Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$ may fail to be a true martingale (it could be a strict local martingale), and the Novikov condition fails. In this case, the standard Girsanov construction does not produce a valid equivalent martingale measure, and one must either:

    - Relax the specification of $\lambda_S$ near $v_t = 0$ (e.g., cap $\lambda_S$ at some maximum value)
    - Use a weaker sufficient condition than Novikov (such as Kazamaki's criterion)
    - Work with the Heston model only in parameter regimes where the Feller condition holds

    This highlights a fundamental tension: the no-arbitrage condition requires $\lambda_S = (\mu-r)/\sqrt{v_t}$ exactly, but this specification is well-behaved only when the variance stays strictly positive.

---

**Exercise 2.**
The measure change transforms $\kappa^{\mathbb{P}} \to \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \xi\lambda$ and $\theta^{\mathbb{P}} \to \theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$. Verify that $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$ for any value of $\lambda$. Explain why this product is invariant under the measure change and connect it to the Feller condition being preserved.

??? success "Solution to Exercise 2"
    We verify directly:

    $$
    \kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = (\kappa^{\mathbb{P}} + \xi\lambda)\cdot\frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \xi\lambda} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}
    $$

    The $(\kappa^{\mathbb{P}} + \xi\lambda)$ factors cancel exactly for any value of $\lambda$, confirming $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$.

    **Why this product is invariant.** The measure change with $\lambda_v = \lambda\sqrt{v_t}$ modifies only the drift of the variance SDE. Under $\mathbb{P}$:

    $$
    dv_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2),\mathbb{P}}
    $$

    Under $\mathbb{Q}$:

    $$
    dv_t = [\kappa^{\mathbb{P}}\theta^{\mathbb{P}} - (\kappa^{\mathbb{P}} + \xi\lambda)v_t]\,dt + \xi\sqrt{v_t}\,dW_t^{(2),\mathbb{Q}}
    $$

    The constant term in the drift is $\kappa^{\mathbb{P}}\theta^{\mathbb{P}}$, which is unchanged by the measure change. Only the coefficient of $v_t$ changes from $-\kappa^{\mathbb{P}}$ to $-(\kappa^{\mathbb{P}} + \xi\lambda)$. Since the constant term equals $\kappa\theta$ for any CIR representation $\kappa(\theta - v_t) = \kappa\theta - \kappa v_t$, the product $\kappa\theta$ is the constant part of the drift, which the Girsanov shift $-\xi\lambda v_t\,dt$ does not affect.

    **Connection to the Feller condition.** The Feller condition is $2\kappa\theta \geq \xi^2$. Since $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$ and $\xi$ is unchanged, the condition $2\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} \geq \xi^2$ is equivalent to $2\kappa^{\mathbb{P}}\theta^{\mathbb{P}} \geq \xi^2$. Therefore, if the Feller condition holds under $\mathbb{P}$, it automatically holds under $\mathbb{Q}$ for any $\lambda$. The variance process either stays strictly positive under both measures or can reach zero under both measures---the measure change cannot create or remove the boundary behavior.

---

**Exercise 3.**
Consider the alternative specification $\lambda_v(t) = \lambda_0$ (constant, not proportional to $\sqrt{v_t}$). Substitute this into the variance SDE under $\mathbb{Q}$ and show that the resulting drift is $\kappa(\theta - v_t) - \xi\lambda_0\sqrt{v_t}$. Explain why this breaks the CIR (affine) structure: the drift is no longer a linear function of $v_t$. What computational consequence does this have for pricing?

??? success "Solution to Exercise 3"
    With the constant specification $\lambda_v(t) = \lambda_0$, substitute $dW_t^{(2),\mathbb{P}} = dW_t^{(2),\mathbb{Q}} - \lambda_0\,dt$ into the variance SDE:

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}(dW_t^{(2),\mathbb{Q}} - \lambda_0\,dt)
    $$

    $$
    = [\kappa(\theta - v_t) - \xi\lambda_0\sqrt{v_t}]\,dt + \xi\sqrt{v_t}\,dW_t^{(2),\mathbb{Q}}
    $$

    $$
    = [\kappa\theta - \kappa v_t - \xi\lambda_0\sqrt{v_t}]\,dt + \xi\sqrt{v_t}\,dW_t^{(2),\mathbb{Q}}
    $$

    The drift under $\mathbb{Q}$ is $\kappa\theta - \kappa v_t - \xi\lambda_0\sqrt{v_t}$. In the CIR (affine) model, the drift must be a linear (affine) function of $v_t$, i.e., of the form $a + bv_t$ for constants $a, b$. Here, the term $-\xi\lambda_0\sqrt{v_t}$ is proportional to $\sqrt{v_t}$, which is not a linear function of $v_t$. This breaks the affine structure because the drift is now

    $$
    \mu(v) = \kappa\theta - \kappa v - \xi\lambda_0\sqrt{v}
    $$

    which is a nonlinear function of $v$.

    **Computational consequences:**

    1. **No closed-form characteristic function.** The Heston model's tractability relies on the Riccati ODE system for the characteristic function, which requires the drift and squared diffusion to be affine in $v_t$. With the $\sqrt{v}$ term in the drift, the Riccati system no longer closes, and no analytical CF exists.

    2. **No semi-analytical pricing.** Without the CF, methods such as Fourier inversion (Carr-Madan, COS, Gil-Pelaez) cannot be applied directly. One must resort to Monte Carlo simulation or PDE methods, both of which are significantly slower.

    3. **Calibration becomes expensive.** Option pricing under the non-affine model requires numerical solutions at each parameter evaluation, making optimization-based calibration much more computationally demanding.

    This is precisely why the specification $\lambda_v = \lambda\sqrt{v_t}$ is standard: it cancels the $\sqrt{v_t}$ in the Girsanov drift adjustment against the $\sqrt{v_t}$ diffusion coefficient, producing a drift term $-\xi\lambda v_t$ that is linear in $v_t$ and preserves the affine structure.

---

**Exercise 4.**
Using the numerical example ($\kappa^{\mathbb{P}} = 3.0$, $\theta^{\mathbb{P}} = 0.04$, $\xi = 0.3$, $\lambda = 1.0$), compute the risk-neutral parameters and verify the Feller condition under both $\mathbb{P}$ and $\mathbb{Q}$. Now increase $\lambda$ to 5.0. What are the new $\kappa^{\mathbb{Q}}$ and $\theta^{\mathbb{Q}}$? Is the Feller condition still satisfied? At what value of $\lambda$ does $\theta^{\mathbb{Q}}$ become unreasonably small (say, less than $0.01$)?

??? success "Solution to Exercise 4"
    **Risk-neutral parameters with $\lambda = 1.0$:**

    $$
    \kappa^{\mathbb{Q}} = 3.0 + 0.3(1.0) = 3.3
    $$

    $$
    \theta^{\mathbb{Q}} = \frac{3.0 \times 0.04}{3.3} = \frac{0.12}{3.3} = 0.0364
    $$

    **Feller condition under $\mathbb{P}$:** $2\kappa^{\mathbb{P}}\theta^{\mathbb{P}} = 2(3.0)(0.04) = 0.24 \geq 0.09 = \xi^2$. Satisfied.

    **Feller condition under $\mathbb{Q}$:** $2\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = 2(3.3)(0.0364) = 0.240 \geq 0.09 = \xi^2$. Satisfied (as expected, since $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$).

    **Now with $\lambda = 5.0$:**

    $$
    \kappa^{\mathbb{Q}} = 3.0 + 0.3(5.0) = 3.0 + 1.5 = 4.5
    $$

    $$
    \theta^{\mathbb{Q}} = \frac{3.0 \times 0.04}{4.5} = \frac{0.12}{4.5} = 0.0267
    $$

    **Feller condition:** $2(4.5)(0.0267) = 0.240 \geq 0.09$. Still satisfied, as always.

    **Finding when $\theta^{\mathbb{Q}} < 0.01$:**

    $$
    \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \xi\lambda} = \frac{0.12}{3.0 + 0.3\lambda} < 0.01
    $$

    $$
    0.12 < 0.01(3.0 + 0.3\lambda) = 0.03 + 0.003\lambda
    $$

    $$
    0.09 < 0.003\lambda \implies \lambda > 30
    $$

    So $\theta^{\mathbb{Q}} < 0.01$ (corresponding to long-run vol below 10%) requires $\lambda > 30$, which is far outside typical empirical estimates ($\lambda \in [0.5, 3.0]$). At $\lambda = 30$:

    $$
    \kappa^{\mathbb{Q}} = 3.0 + 0.3(30) = 12.0, \qquad \theta^{\mathbb{Q}} = \frac{0.12}{12.0} = 0.01
    $$

    Such extreme values of $\lambda$ would imply an enormous variance risk premium, with the risk-neutral variance dynamics reverting extremely fast ($\kappa^{\mathbb{Q}} = 12$, half-life of about 3 weeks) to a very low level. This is economically implausible for equity markets.

---

**Exercise 5.**
The Heston model has two sources of randomness but only two traded assets (stock and bond). Explain precisely which component of the variance risk is unhedgeable. Decompose $W^{(2)} = \rho W^{(1)} + \sqrt{1 - \rho^2} W^{\perp}$ and argue that the $W^{(1)}$ component of variance risk can be partially hedged via delta hedging, while the $W^{\perp}$ component is entirely unhedgeable.

??? success "Solution to Exercise 5"
    Decompose the second Brownian motion as

    $$
    W_t^{(2)} = \rho W_t^{(1)} + \sqrt{1 - \rho^2}\,W_t^{\perp}
    $$

    where $W^{\perp}$ is a standard Brownian motion independent of $W^{(1)}$. The variance SDE becomes

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\left(\rho\,dW_t^{(1)} + \sqrt{1-\rho^2}\,dW_t^{\perp}\right)
    $$

    The stock SDE only involves $W^{(1)}$:

    $$
    dS_t = \mu S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^{(1)}
    $$

    **Which component is hedgeable.** By delta-hedging the stock, an investor can offset exposure to $W^{(1)}$. Since the variance process loads on $W^{(1)}$ through the term $\xi\sqrt{v_t}\,\rho\,dW_t^{(1)}$, this component of variance risk can be partially hedged. Specifically, a portfolio combining the option, $\Delta$ shares of stock, and the bond can eliminate the $dW_t^{(1)}$ sensitivity.

    **Which component is unhedgeable.** The term $\xi\sqrt{v_t}\sqrt{1-\rho^2}\,dW_t^{\perp}$ involves $W^{\perp}$, which is orthogonal to $W^{(1)}$ and hence orthogonal to the stock return innovation. No amount of trading in the stock can hedge this component. This is the source of market incompleteness.

    **Quantifying the hedgeable fraction.** The total variance of $dv_t$ coming from the diffusion term is $\xi^2 v_t\,dt$. The fraction attributable to $W^{(1)}$ is $\rho^2$, and the fraction attributable to $W^{\perp}$ is $1 - \rho^2$. With $\rho = -0.7$:

    - Hedgeable fraction: $\rho^2 = 0.49$ (49%)
    - Unhedgeable fraction: $1 - \rho^2 = 0.51$ (51%)

    The market price of risk for $W^{(1)}$ is uniquely determined by no-arbitrage ($\lambda_S = (\mu-r)/\sqrt{v_t}$). The market price of risk for $W^{\perp}$ is undetermined, and this is exactly the freedom parameterized by $\lambda$. When $|\rho|$ is close to 1, most variance risk is hedgeable and the choice of $\lambda$ has a smaller effect on prices. When $|\rho|$ is close to 0, nearly all variance risk is unhedgeable, and $\lambda$ has a large effect.

---

**Exercise 6.**
The parameter transformation table shows that $\xi$ and $\rho$ are unchanged by the measure change. Prove this directly from the Girsanov construction: the variance SDE under $\mathbb{Q}$ retains $\xi\sqrt{v_t}\,dW_t^{(2),\mathbb{Q}}$ as the diffusion term, and the correlation $\text{Corr}(dW^{(1),\mathbb{Q}}, dW^{(2),\mathbb{Q}}) = \rho$ is preserved because the Girsanov shifts are deterministic (conditional on $\mathcal{F}_t$).

??? success "Solution to Exercise 6"
    **Preservation of $\xi$.** Under $\mathbb{P}$, the variance diffusion coefficient is $\xi\sqrt{v_t}$. The Girsanov measure change modifies only the drift, not the diffusion coefficient. Under $\mathbb{Q}$:

    $$
    dv_t = [\kappa^{\mathbb{P}}\theta^{\mathbb{P}} - (\kappa^{\mathbb{P}} + \xi\lambda)v_t]\,dt + \xi\sqrt{v_t}\,dW_t^{(2),\mathbb{Q}}
    $$

    The diffusion term $\xi\sqrt{v_t}\,dW_t^{(2),\mathbb{Q}}$ retains $\xi$ unchanged. This is a general property of Girsanov's theorem: the measure change affects drifts but not volatilities (diffusion coefficients). The quadratic variation $d\langle v \rangle_t = \xi^2 v_t\,dt$ is the same under both measures.

    **Preservation of $\rho$.** The correlation between $W^{(1)}$ and $W^{(2)}$ is determined by their quadratic covariation:

    $$
    d\langle W^{(1),\mathbb{Q}}, W^{(2),\mathbb{Q}} \rangle_t
    $$

    Using $dW_t^{(i),\mathbb{Q}} = dW_t^{(i),\mathbb{P}} + \lambda_i(t)\,dt$:

    $$
    d\langle W^{(1),\mathbb{Q}}, W^{(2),\mathbb{Q}} \rangle_t = d\langle W^{(1),\mathbb{P}} + \lambda_S\,dt,\; W^{(2),\mathbb{P}} + \lambda_v\,dt \rangle_t
    $$

    Since the Girsanov shifts $\lambda_S(t)\,dt$ and $\lambda_v(t)\,dt$ are $\mathcal{F}_t$-measurable (they are locally deterministic, i.e., adapted and of finite variation), they do not contribute to the quadratic covariation. Therefore:

    $$
    d\langle W^{(1),\mathbb{Q}}, W^{(2),\mathbb{Q}} \rangle_t = d\langle W^{(1),\mathbb{P}}, W^{(2),\mathbb{P}} \rangle_t = \rho\,dt
    $$

    The correlation is preserved because quadratic covariation depends only on the martingale (diffusion) parts of the processes, and the Girsanov drift shifts are of bounded variation and hence invisible to the quadratic variation operator.

---

**Exercise 7.**
If the Heston model were augmented with a traded variance swap, the market would become complete and $\lambda$ would be uniquely determined. Explain this using the fundamental theorem of asset pricing: with three traded assets (stock, bond, variance swap) and two Brownian motions, the equivalent martingale measure is unique. How would you determine $\lambda$ from the observed variance swap rate?

??? success "Solution to Exercise 7"
    **Completeness from the fundamental theorem.** The second fundamental theorem of asset pricing states: in an arbitrage-free market, the equivalent martingale measure is unique if and only if the market is complete (every contingent claim is replicable). The Heston model has two sources of randomness ($W^{(1)}$, $W^{(2)}$) and two traded assets (stock, bond), leaving one unhedgeable dimension and hence an infinite family of EMMs parameterized by $\lambda$.

    Adding a traded variance swap introduces a third asset whose price process depends on $W^{(2)}$ (through its exposure to $v_t$). With three assets and two Brownian motions, the system of replication equations

    $$
    \alpha\,dS_t + \beta\,dB_t + \gamma\,d(\text{VS}_t) = dV_t
    $$

    has a solution for any contingent claim $V_t$. The market is complete, and the EMM is unique.

    **Determining $\lambda$ from the variance swap rate.** A variance swap with maturity $T$ has a payoff proportional to the realized integrated variance $\int_0^T v_t\,dt$. Its fair strike (variance swap rate) is

    $$
    K_{\text{var}} = \frac{1}{T}\mathbb{E}^{\mathbb{Q}}\!\left[\int_0^T v_t\,dt\right] = \theta^{\mathbb{Q}} + (v_0 - \theta^{\mathbb{Q}})\frac{1 - e^{-\kappa^{\mathbb{Q}} T}}{\kappa^{\mathbb{Q}} T}
    $$

    This is an observable quantity (quoted in the market). Given the physical parameters $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}}, \xi)$ estimated from time-series data and the current variance $v_0$, the observed $K_{\text{var}}$ pins down $\kappa^{\mathbb{Q}}$ (and hence $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$) through the above equation, which can be solved numerically. Then

    $$
    \lambda = \frac{\kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}}}{\xi}
    $$

    In practice, one would observe variance swap rates at multiple maturities $T_1, \ldots, T_n$ and fit $\lambda$ (or equivalently $\kappa^{\mathbb{Q}}$) by minimizing the pricing error across all maturities. With a single constant $\lambda$, one degree of freedom suffices to match the entire term structure in the Heston model, and the market is complete: every contingent claim on $(S, v)$ can be replicated using a portfolio of the stock, bond, and variance swaps.
