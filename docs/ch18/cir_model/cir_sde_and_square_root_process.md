# CIR SDE and Square-Root Process

The Cox-Ingersoll-Ross (CIR) model, introduced by Cox, Ingersoll, and Ross in 1985, modifies the Vasicek model by replacing the constant diffusion coefficient with a square-root function of the short rate. This seemingly small change has profound consequences: the model prevents negative interest rates (under appropriate parameter conditions), produces level-dependent volatility consistent with empirical observation, and connects to the non-central chi-squared distribution rather than the Gaussian. The CIR process reappears as the variance dynamics in the Heston stochastic volatility model, making it one of the most widely used diffusions in quantitative finance.

---

## The CIR stochastic differential equation

Under the risk-neutral measure $\mathbb{Q}$, the CIR short rate satisfies

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
$$

where:

- $r_t \geq 0$ is the instantaneous short rate
- $\kappa > 0$ is the **mean-reversion speed**
- $\theta > 0$ is the **long-run mean** level
- $\sigma > 0$ is the **volatility parameter** (sometimes called the "vol of vol" by analogy with Heston)
- $W_t$ is a standard Brownian motion under $\mathbb{Q}$

### Parameter interpretation

The drift $\kappa(\theta - r_t)$ is identical to the Vasicek drift: when $r_t > \theta$ the drift is negative (pulling rates down), and when $r_t < \theta$ the drift is positive (pushing rates up). The half-life of mean reversion is $\ln 2 / \kappa$.

The critical difference from Vasicek is the diffusion coefficient $\sigma\sqrt{r_t}$:

- When $r_t$ is large, the volatility is large: $\text{Vol}(dr_t) \approx \sigma\sqrt{r_t}\,\sqrt{dt}$
- When $r_t$ is near zero, the volatility vanishes: $\sigma\sqrt{r_t} \to 0$
- This **level-dependent volatility** matches the empirical observation that interest rate volatility increases with the level of rates

---

## Non-negativity of the short rate

### Intuitive argument

When $r_t$ approaches zero from above, two effects compete:

1. The **drift** $\kappa(\theta - r_t) \to \kappa\theta > 0$ pushes the rate upward
2. The **diffusion** $\sigma\sqrt{r_t} \to 0$ vanishes, eliminating downward random shocks

The vanishing diffusion at zero means that the process cannot be driven below zero by the Brownian noise. Whether the process actually reaches zero depends on the relative strength of the drift versus the diffusion near zero, captured by the Feller condition (discussed in the next section).

### Formal non-negativity

If $r_0 > 0$, the solution remains non-negative: $r_t \geq 0$ for all $t \geq 0$ almost surely. This follows from the comparison theorem for SDEs, since the CIR process dominates the process $dr_t = -\kappa\,r_t\,dt$ (which is non-negative) when $r_t$ is small.

More precisely, the boundary $r = 0$ is classified as:

- **Entrance boundary** (inaccessible) if $2\kappa\theta \geq \sigma^2$ (the Feller condition)
- **Regular boundary** (accessible, instantly reflecting) if $2\kappa\theta < \sigma^2$

In either case, the process remains non-negative. The Feller condition determines only whether zero is reached, not whether the process goes negative (it never does).

---

## Existence and uniqueness of solutions

### The Lipschitz problem

The standard existence-uniqueness theorem for SDEs requires the drift and diffusion to be globally Lipschitz. The CIR diffusion $\sigma\sqrt{r}$ is not Lipschitz at $r = 0$ (since $|\sqrt{x} - \sqrt{y}| \leq |x - y|/(\sqrt{x} + \sqrt{y})$ diverges near zero).

### Yamada-Watanabe conditions

Nevertheless, the CIR SDE has a **unique strong solution** by the Yamada-Watanabe theorem. The key condition is that the diffusion coefficient $h(r) = \sigma\sqrt{r}$ satisfies

$$
|h(x) - h(y)| \leq C\,|x - y|^\alpha \quad \text{for some } \alpha \geq 1/2
$$

Since $|\sqrt{x} - \sqrt{y}| \leq \sqrt{|x - y|}$, the condition holds with $\alpha = 1/2$ and $C = \sigma$. Combined with the linear growth of the drift, this guarantees pathwise uniqueness and strong existence.

---

## Conditional moments

### Conditional mean

Taking the expectation of the SDE:

$$
\frac{d}{dt}\mathbb{E}[r_t] = \kappa(\theta - \mathbb{E}[r_t])
$$

This is the same ODE as for Vasicek, with solution:

$$
\mathbb{E}[r_t \mid r_0] = \theta + (r_0 - \theta)\,e^{-\kappa t}
$$

The conditional mean is identical to the Vasicek mean: both models have the same mean-reversion dynamics.

### Conditional variance

The variance calculation is more involved because the diffusion is state-dependent. Applying Ito's lemma to $r_t^2$:

$$
d(r_t^2) = 2r_t\,dr_t + (dr_t)^2 = 2r_t\,\kappa(\theta - r_t)\,dt + 2\sigma r_t^{3/2}\,dW_t + \sigma^2 r_t\,dt
$$

Taking expectations and using $\text{Var}(r_t) = \mathbb{E}[r_t^2] - (\mathbb{E}[r_t])^2$, one obtains after calculation:

$$
\text{Var}(r_t \mid r_0) = r_0\,\frac{\sigma^2}{\kappa}\!\left(e^{-\kappa t} - e^{-2\kappa t}\right) + \theta\,\frac{\sigma^2}{2\kappa}\!\left(1 - e^{-\kappa t}\right)^2
$$

**Key differences from Vasicek:**

- The variance depends on $r_0$ (not just on time)
- For $r_0 = 0$: $\text{Var}(r_t) = \theta\sigma^2(1 - e^{-\kappa t})^2/(2\kappa)$
- For $r_0 = \theta$: $\text{Var}(r_t) = \theta\sigma^2(1 - e^{-2\kappa t})/(2\kappa)$ (matches Vasicek with $\sigma_{\text{Vas}}^2 = \sigma^2\theta$)

### Stationary distribution moments

As $t \to \infty$:

$$
\mathbb{E}[r_\infty] = \theta, \qquad \text{Var}(r_\infty) = \frac{\theta\sigma^2}{2\kappa}
$$

The stationary mean is $\theta$ (same as Vasicek), but the stationary variance $\theta\sigma^2/(2\kappa)$ depends on the level $\theta$, reflecting the level-dependent volatility.

---

## Comparison with Vasicek

| Property | Vasicek | CIR |
|---|---|---|
| SDE | $dr = \kappa(\theta - r)\,dt + \sigma\,dW$ | $dr = \kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW$ |
| Diffusion | Constant: $\sigma$ | State-dependent: $\sigma\sqrt{r}$ |
| Negative rates | Possible | Impossible ($r_t \geq 0$) |
| Distribution | Gaussian | Non-central $\chi^2$ (scaled) |
| Conditional mean | $\theta + (r_0 - \theta)e^{-\kappa t}$ | Same |
| Conditional variance | $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$ | $r_0\frac{\sigma^2}{\kappa}(e^{-\kappa t} - e^{-2\kappa t}) + \theta\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa t})^2$ |
| Bond price form | $A(\tau)\,e^{-B(\tau)\,r}$ | Same (but different $A$, $B$) |
| Analytical options | Black-Scholes type | Non-central $\chi^2$ |

---

## Connection to the Heston model

The CIR process appears as the **variance dynamics** in the Heston (1993) stochastic volatility model:

$$
dv_t = \kappa_v(\theta_v - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^v
$$

where $v_t$ is the instantaneous variance of an asset. The same Feller condition $2\kappa_v\theta_v \geq \sigma_v^2$ ensures that variance stays positive. The analytical tractability of CIR (affine structure, known characteristic function) is the key reason Heston admits semi-closed-form option pricing via Fourier inversion.

---

## Numerical example

Parameters: $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.1$, $r_0 = 0.03$.

**Feller ratio**: $2\kappa\theta/\sigma^2 = 2 \times 0.5 \times 0.04 / 0.01 = 4.0 > 1$. The Feller condition is satisfied, so zero is inaccessible.

**Moments at various horizons:**

| $t$ | $\mathbb{E}[r_t]$ | $\text{Var}(r_t)^{1/2}$ |
|:-:|:-:|:-:|
| 0.5 | 3.22% | 0.99% |
| 1 | 3.39% | 1.20% |
| 5 | 3.96% | 1.41% |
| 10 | 4.00% | 1.41% |
| $\infty$ | 4.00% | 1.41% |

The stationary standard deviation is $\sqrt{\theta\sigma^2/(2\kappa)} = \sqrt{0.04 \times 0.01 / 1.0} = 2.0\%$. Note: this is $\sqrt{0.0004} = 0.02 = 2.0\%$.

---

## Summary

The CIR model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$ replaces the Vasicek constant diffusion with $\sigma\sqrt{r_t}$, ensuring non-negative rates and producing level-dependent volatility. The conditional mean is the same as Vasicek, but the variance depends on the initial rate $r_0$. Strong existence and uniqueness hold by the Yamada-Watanabe theorem despite the non-Lipschitz diffusion at zero. The Feller condition $2\kappa\theta \geq \sigma^2$ determines whether zero is accessible, and the CIR process reappears as the variance dynamics in the Heston model.

---

## Exercises

**Exercise 1.** For CIR parameters $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.08$, and $r_0 = 0.03$, compute the conditional mean $\mathbb{E}[r_t \mid r_0]$ and conditional standard deviation at horizons $t = 1, 5, 10$ years. How do these compare with the Vasicek model having the same $\kappa$, $\theta$, and $\sigma_{\text{Vas}} = \sigma\sqrt{\theta}$?

??? success "Solution to Exercise 1"

    Given $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.08$, $r_0 = 0.03$.

    **CIR conditional mean:**

    $$
    \mathbb{E}[r_t \mid r_0] = \theta + (r_0 - \theta)e^{-\kappa t} = 0.05 + (0.03 - 0.05)e^{-0.3t} = 0.05 - 0.02\,e^{-0.3t}
    $$

    **CIR conditional variance:**

    $$
    \text{Var}(r_t \mid r_0) = r_0\frac{\sigma^2}{\kappa}(e^{-\kappa t} - e^{-2\kappa t}) + \theta\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa t})^2
    $$

    $$
    = 0.03 \times \frac{0.0064}{0.3}(e^{-0.3t} - e^{-0.6t}) + 0.05 \times \frac{0.0064}{0.6}(1 - e^{-0.3t})^2
    $$

    $$
    = 6.4 \times 10^{-4}(e^{-0.3t} - e^{-0.6t}) + 5.333 \times 10^{-4}(1 - e^{-0.3t})^2
    $$

    **Vasicek comparison:** $\sigma_{\text{Vas}} = \sigma\sqrt{\theta} = 0.08\sqrt{0.05} = 0.01789$. Vasicek variance: $\sigma_{\text{Vas}}^2(1 - e^{-2\kappa t})/(2\kappa)$.

    | $t$ | $\mathbb{E}[r_t]$ | $\text{Std}_{\text{CIR}}$ | $\text{Std}_{\text{Vas}}$ |
    |:---:|:---:|:---:|:---:|
    | 1 | $0.05 - 0.02(0.7408) = 3.52\%$ | $0.636\%$ | $0.592\%$ |
    | 5 | $0.05 - 0.02(0.2231) = 4.55\%$ | $0.935\%$ | $0.926\%$ |
    | 10 | $0.05 - 0.02(0.0498) = 4.90\%$ | $1.006\%$ | $1.011\%$ |

    The means are identical (both models have the same mean-reversion dynamics). At short horizons, the CIR standard deviation is slightly larger because $r_0 = 0.03 < \theta = 0.05$ and the CIR variance depends on $r_0$. At long horizons, both converge to their respective stationary values.

---

**Exercise 2.** Verify the Feller condition for the parameters $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.15$. Compute the Feller ratio $2\kappa\theta/\sigma^2$. Is zero accessible or inaccessible? What happens to the boundary classification if $\sigma$ is increased to $0.25$ while keeping $\kappa$ and $\theta$ fixed?

??? success "Solution to Exercise 2"

    **Feller ratio:** $\nu = 2\kappa\theta/\sigma^2 = 2(0.5)(0.04)/(0.15)^2 = 0.04/0.0225 = 1.778$.

    Since $\nu = 1.778 \geq 1$, the Feller condition is satisfied. Zero is an **entrance boundary** (inaccessible). The process stays strictly positive for all $t > 0$.

    **With $\sigma = 0.25$:** $\nu = 2(0.5)(0.04)/(0.25)^2 = 0.04/0.0625 = 0.64$.

    Since $\nu = 0.64 < 1$, the Feller condition is **violated**. Zero is now a **regular boundary**: the process reaches zero in finite time with positive probability and is instantaneously reflected. The boundary classification changes from entrance to regular when $\sigma$ increases past $\sqrt{2\kappa\theta} = \sqrt{0.04} = 0.2$.

---

**Exercise 3.** Starting from $d(r_t^2) = 2r_t\,dr_t + (dr_t)^2$, derive the ODE for $\mathbb{E}[r_t^2]$ and then obtain the conditional variance formula. Show each step of the calculation, using $\mathbb{E}[r_t\,dW_t] = 0$ and $(dr_t)^2 = \sigma^2 r_t\,dt$.

??? success "Solution to Exercise 3"

    Starting from $d(r_t^2) = 2r_t\,dr_t + (dr_t)^2$:

    **Step 1:** Compute $2r_t\,dr_t$:

    $$
    2r_t\,dr_t = 2r_t[\kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t] = 2\kappa r_t(\theta - r_t)\,dt + 2\sigma r_t^{3/2}\,dW_t
    $$

    **Step 2:** Compute $(dr_t)^2 = \sigma^2 r_t\,dt$ (keeping only the $dt$ term since $(dW_t)^2 = dt$).

    **Step 3:** Combine:

    $$
    d(r_t^2) = [2\kappa\theta r_t - 2\kappa r_t^2 + \sigma^2 r_t]\,dt + 2\sigma r_t^{3/2}\,dW_t
    $$

    **Step 4:** Take expectations (the $dW_t$ term has zero expectation):

    $$
    \frac{d}{dt}\mathbb{E}[r_t^2] = (2\kappa\theta + \sigma^2)\mathbb{E}[r_t] - 2\kappa\mathbb{E}[r_t^2]
    $$

    **Step 5:** Since $\text{Var}(r_t) = \mathbb{E}[r_t^2] - (\mathbb{E}[r_t])^2$ and we know $\mathbb{E}[r_t] = \theta + (r_0 - \theta)e^{-\kappa t}$, define $V(t) = \text{Var}(r_t)$ and $m(t) = \mathbb{E}[r_t]$. Then:

    $$
    \frac{dV}{dt} = \frac{d}{dt}\mathbb{E}[r_t^2] - 2m(t)m'(t)
    $$

    Using $m'(t) = -\kappa(m(t) - \theta) = \kappa(\theta - m(t))$ and $\mathbb{E}[r_t^2] = V(t) + m(t)^2$:

    $$
    \frac{dV}{dt} = (2\kappa\theta + \sigma^2)m(t) - 2\kappa(V(t) + m(t)^2) - 2m(t) \cdot \kappa(\theta - m(t))
    $$

    $$
    = (2\kappa\theta + \sigma^2)m(t) - 2\kappa V(t) - 2\kappa m(t)^2 - 2\kappa\theta m(t) + 2\kappa m(t)^2
    $$

    $$
    = \sigma^2 m(t) - 2\kappa V(t)
    $$

    **Step 6:** Solve $V'(t) + 2\kappa V(t) = \sigma^2 m(t)$ with $V(0) = 0$. Using the integrating factor $e^{2\kappa t}$:

    $$
    V(t) = \sigma^2 e^{-2\kappa t}\int_0^t e^{2\kappa s}[\theta + (r_0 - \theta)e^{-\kappa s}]\,ds
    $$

    Evaluating:

    $$
    = \sigma^2 e^{-2\kappa t}\left[\theta\frac{e^{2\kappa t} - 1}{2\kappa} + (r_0 - \theta)\frac{e^{\kappa t} - 1}{\kappa}\right]
    $$

    $$
    = \frac{\sigma^2\theta}{2\kappa}(1 - e^{-2\kappa t}) + \frac{\sigma^2(r_0 - \theta)}{\kappa}(e^{-\kappa t} - e^{-2\kappa t})
    $$

    Rearranging:

    $$
    = r_0\frac{\sigma^2}{\kappa}(e^{-\kappa t} - e^{-2\kappa t}) + \theta\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa t})^2
    $$

    which matches the stated formula.

---

**Exercise 4.** The Yamada-Watanabe theorem requires $|h(x) - h(y)| \leq C|x-y|^\alpha$ for $\alpha \geq 1/2$. Verify this for $h(r) = \sigma\sqrt{r}$ by showing that $|\sqrt{x} - \sqrt{y}| \leq \sqrt{|x-y|}$ for all $x, y \geq 0$. Where does the standard Lipschitz condition (i.e., $\alpha = 1$) fail?

??? success "Solution to Exercise 4"

    We need to show $|\sqrt{x} - \sqrt{y}| \leq \sqrt{|x - y|}$ for $x, y \geq 0$.

    Without loss of generality, assume $x \geq y \geq 0$. Then:

    $$
    \sqrt{x} - \sqrt{y} = \frac{x - y}{\sqrt{x} + \sqrt{y}}
    $$

    Since $\sqrt{x} + \sqrt{y} \geq \sqrt{x - y + y} + \sqrt{y} \geq \sqrt{x-y}$ (actually, we use a simpler bound), note that $\sqrt{x} \geq \sqrt{x-y}$ (since $x \geq x - y$) and $\sqrt{y} \geq 0$, so $\sqrt{x} + \sqrt{y} \geq \sqrt{x - y}$.

    More directly: square both sides. We need $(\sqrt{x} - \sqrt{y})^2 \leq x - y$, i.e., $x + y - 2\sqrt{xy} \leq x - y$, i.e., $2y \leq 2\sqrt{xy}$, i.e., $y \leq \sqrt{xy}$, i.e., $y^2 \leq xy$, i.e., $y \leq x$. This holds by assumption. Hence $|\sqrt{x} - \sqrt{y}| \leq \sqrt{|x-y|}$, confirming $\alpha = 1/2$ with $C = 1$ (so $C = \sigma$ for $h(r) = \sigma\sqrt{r}$).

    **Where the standard Lipschitz condition fails:** The Lipschitz condition ($\alpha = 1$) requires $|\sqrt{x} - \sqrt{y}| \leq L|x-y|$ for some constant $L$. But $|\sqrt{x} - \sqrt{y}|/|x-y| = 1/(\sqrt{x} + \sqrt{y}) \to \infty$ as $x,y \to 0$. No finite Lipschitz constant $L$ exists near the origin.

---

**Exercise 5.** The stationary variance of the CIR process is $\theta\sigma^2/(2\kappa)$, while the Vasicek stationary variance is $\sigma_{\text{Vas}}^2/(2\kappa)$. If both models have the same stationary variance, what is the relationship between $\sigma$ (CIR) and $\sigma_{\text{Vas}}$ (Vasicek)? Compute the CIR and Vasicek volatilities that give a stationary standard deviation of 1% when $\kappa = 0.5$ and $\theta = 0.04$.

??? success "Solution to Exercise 5"

    Equating stationary variances: $\theta\sigma^2/(2\kappa) = \sigma_{\text{Vas}}^2/(2\kappa)$, so:

    $$
    \sigma_{\text{Vas}}^2 = \theta\sigma^2 \quad \Longrightarrow \quad \sigma_{\text{Vas}} = \sigma\sqrt{\theta}
    $$

    **Computation for stationary standard deviation of 1%:** We need $\sqrt{\theta\sigma^2/(2\kappa)} = 0.01$, so $\theta\sigma^2/(2\kappa) = 10^{-4}$.

    With $\kappa = 0.5$ and $\theta = 0.04$:

    $$
    0.04 \times \sigma^2 / 1.0 = 10^{-4} \implies \sigma^2 = 0.0025 \implies \sigma = 0.05
    $$

    For Vasicek:

    $$
    \sigma_{\text{Vas}}^2 / (2\kappa) = 10^{-4} \implies \sigma_{\text{Vas}}^2 = 10^{-4} \implies \sigma_{\text{Vas}} = 0.01
    $$

    Check: $\sigma_{\text{Vas}} = \sigma\sqrt{\theta} = 0.05\sqrt{0.04} = 0.05 \times 0.2 = 0.01$. $\checkmark$

---

**Exercise 6.** In the Heston model, the variance process $dv_t = \kappa_v(\theta_v - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^v$ is CIR. If $\kappa_v = 2.0$, $\theta_v = 0.04$ (corresponding to 20% implied vol), and $\sigma_v = 0.3$, check the Feller condition. Discuss the practical implications if the Feller condition is violated for the variance process in an equity options model.

??? success "Solution to Exercise 6"

    **Feller condition:** $\nu = 2\kappa_v\theta_v/\sigma_v^2 = 2(2.0)(0.04)/(0.3)^2 = 0.16/0.09 = 1.778$.

    Since $\nu = 1.778 \geq 1$, the Feller condition **is satisfied**. The variance process stays strictly positive.

    However, in practice, calibrated Heston parameters frequently have much larger $\sigma_v$ (vol-of-vol), often in the range $0.5$ to $1.0$. With $\sigma_v = 0.5$: $\nu = 0.16/0.25 = 0.64 < 1$. With $\sigma_v = 1.0$: $\nu = 0.16/1.0 = 0.16 \ll 1$.

    **Practical implications when Feller is violated:**

    1. The variance process touches zero with positive probability, which is problematic because options with zero instantaneous variance have deterministic prices.
    2. Euler-Maruyama simulation produces negative variance values, requiring truncation or reflection. These fixes introduce bias in Monte Carlo Greeks and hedging ratios.
    3. The non-central chi-squared distribution develops a mass point at zero, complicating numerical integration in semi-analytical Fourier pricing methods.
    4. Despite the Feller violation, the Heston model remains mathematically well-defined (the variance is instantaneously reflected at zero), and the characteristic function-based pricing formula remains valid. The practical challenge is primarily in simulation, not in pricing.

---

**Exercise 7.** Compare the CIR and Vasicek conditional variance formulas at short and long horizons. For small $t$, show that both variances are approximately $\sigma^2 r_0 \cdot t$ (CIR) and $\sigma_{\text{Vas}}^2 \cdot t$ (Vasicek). For large $t$, show that the CIR variance converges to $\theta\sigma^2/(2\kappa)$, independent of $r_0$. Give an economic interpretation of why the CIR short-horizon variance depends on $r_0$.

??? success "Solution to Exercise 7"

    **Short horizon ($t$ small):** Using Taylor expansions $e^{-\kappa t} \approx 1 - \kappa t$ and $e^{-2\kappa t} \approx 1 - 2\kappa t$:

    CIR:

    $$
    \text{Var}(r_t) \approx r_0\frac{\sigma^2}{\kappa}[(1 - \kappa t) - (1 - 2\kappa t)] + \theta\frac{\sigma^2}{2\kappa}(\kappa t)^2
    $$

    $$
    \approx r_0\frac{\sigma^2}{\kappa} \cdot \kappa t + O(t^2) = \sigma^2 r_0 \cdot t
    $$

    Vasicek:

    $$
    \text{Var}(r_t) = \frac{\sigma_{\text{Vas}}^2}{2\kappa}(1 - e^{-2\kappa t}) \approx \frac{\sigma_{\text{Vas}}^2}{2\kappa} \cdot 2\kappa t = \sigma_{\text{Vas}}^2 \cdot t
    $$

    **Long horizon ($t \to \infty$):** In the CIR formula, $e^{-\kappa t} \to 0$ and $e^{-2\kappa t} \to 0$:

    $$
    \text{Var}(r_t) \to r_0\frac{\sigma^2}{\kappa}(0 - 0) + \theta\frac{\sigma^2}{2\kappa}(1 - 0)^2 = \frac{\theta\sigma^2}{2\kappa}
    $$

    This is independent of $r_0$, confirming convergence to the stationary variance.

    **Economic interpretation:** The CIR short-horizon variance is $\sigma^2 r_0 \cdot t$, which depends on $r_0$ because the CIR diffusion coefficient $\sigma\sqrt{r_t}$ scales with the rate level. When rates are high ($r_0$ large), the volatility of rate changes is large, producing greater uncertainty. When rates are near zero, volatility vanishes, producing near-deterministic behavior. This level-dependent volatility is one of the key empirical features that CIR captures and Vasicek misses: in reality, interest rate volatility is higher when rates are high.
