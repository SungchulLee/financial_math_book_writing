# The Stratonovich Integral

### 1. Concept Definition

The **Stratonovich integral** is a stochastic integral defined using **midpoint sampling**:

$$
\int_0^T f(t,\omega) \circ dB_t
:= \lim_{|\Pi|\to 0} \sum_{j=0}^{n-1}
f\!\left(\frac{t_j + t_{j+1}}{2},\, \omega\right)
(B_{t_{j+1}} - B_{t_j})
$$

The circle notation $\circ\,dB_t$ distinguishes it from the Itô integral, which uses left-endpoint sampling. Both integrals are mathematically valid, but they assign different values to the same formal expression.

The core example that illustrates the difference is

$$
\int_0^t B_s \, dB_s = \frac{1}{2}(B_t^2 - t)
\qquad\text{(Itô)}
$$

$$
\int_0^t B_s \circ dB_s = \frac{1}{2}B_t^2
\qquad\text{(Stratonovich)}
$$

The two integrals differ by $\frac{1}{2}t$, which is exactly half the quadratic variation of Brownian motion on $[0,t]$. The midpoint rule picks up this additional contribution because it evaluates the integrand symmetrically—partially in the future—rather than strictly in the past.

In Stratonovich form, stochastic differentials obey the **classical chain rule**:

$$
df(X_t) = f'(X_t) \circ dX_t \qquad \text{(no second-order correction)}
$$

This makes Stratonovich calculus the natural choice in physics and geometric modeling, where coordinate invariance and classical differential rules are essential.

---

### 2. Why Midpoint Sampling Changes the Limit

The choice of evaluation point in the Riemann sum determines which stochastic integral we obtain. We illustrate with the integrand $f(t) = B_t$.

```mermaid
flowchart TD
    A["Partition 0 = t_0 < t_1 < ... < t_n = T"] --> B["Choose evaluation point on each interval"]
    B --> C["Left endpoint t_j"]
    B --> D["Midpoint ½(t_j + t_(j+1))"]

    C --> E["Use B_{t_j}"]
    E --> F["Σ B_{t_j}(B_{t_(j+1)} - B_{t_j})"]
    F --> G["Itô integral ½(B_T² - T)"]

    D --> H["Use ½(B_{t_j} + B_{t_(j+1)})"]
    H --> I["Σ ½(B_{t_j} + B_{t_(j+1)})(B_{t_(j+1)} - B_{t_j})"]
    I --> J["Stratonovich integral ½B_T²"]

    G --> K["Excludes quadratic variation"]
    J --> L["Captures half of quadratic variation"]
```

#### Left-endpoint (Itô)

Evaluating at the left endpoint $t_j^* = t_j$:

$$
\sum_j B_{t_j}(B_{t_{j+1}} - B_{t_j})
$$

Since Brownian increments are independent of the past and have mean zero, each term has $\mathbb{E}[B_{t_j}(B_{t_{j+1}} - B_{t_j})] = 0$. This reflects the **martingale property**: the integral has zero mean.

#### Right-endpoint (for contrast only)

Evaluating at the right endpoint $t_j^* = t_{j+1}$:

$$
\sum_j B_{t_{j+1}}(B_{t_{j+1}} - B_{t_j})
$$

Writing $B_{t_{j+1}} = B_{t_j} + (B_{t_{j+1}} - B_{t_j})$ and expanding:

$$
\mathbb{E}[B_{t_{j+1}}(B_{t_{j+1}} - B_{t_j})]
= \underbrace{\mathbb{E}[B_{t_j}(B_{t_{j+1}} - B_{t_j})]}_{=\,0} + \mathbb{E}[(B_{t_{j+1}} - B_{t_j})^2]
= t_{j+1} - t_j
$$

Summing over all intervals: the right-endpoint sum picks up the **full** quadratic variation $T$.

!!! note
    The right-endpoint rule is shown as a contrast only. It is not a standard stochastic integration convention.

#### Midpoint (Stratonovich)

The midpoint rule evaluates at the average of left and right endpoints:

$$
\frac{1}{2}(B_{t_j} + B_{t_{j+1}})
$$

This is the average of the left-endpoint and right-endpoint evaluations, so it picks up exactly **half** of the quadratic variation. For $\int_0^T B_t \circ dB_t$, the expected correction is $T/2$:

$$
\int_0^t B_s \circ dB_s
= \int_0^t B_s \, dB_s + \frac{1}{2}t
= \frac{1}{2}(B_t^2 - t) + \frac{1}{2}t
= \frac{1}{2}B_t^2
$$

This is exactly the result that the classical chain rule applied to $\frac{d}{dt}\frac{1}{2}B_t^2 = B_t\,\frac{dB_t}{dt}$ would give—if we pretended $B_t$ were differentiable.

---

### 3. The Stratonovich Chain Rule

The principal advantage of Stratonovich calculus is that stochastic differentials obey the same formal chain rule as ordinary calculus. For $f \in C^2$ and an Itô process $X_t$:

**Stratonovich chain rule**: $df(X_t) = f'(X_t) \circ dX_t$

**Itô's formula**: $df(X_t) = f'(X_t)\,dX_t + \frac{1}{2}f''(X_t)\,(dX_t)^2$

The Stratonovich form has no second-order correction. This is why Stratonovich integrals appear naturally when passing from smooth-noise models to white-noise limits (Wong-Zakai theorem), and in geometric problems where the chain rule must behave classically under coordinate changes.

| Property | Itô | Stratonovich |
|---|---|---|
| Chain rule | $df = f'\,dX + \frac{1}{2}f''(dX)^2$ | $df = f' \circ dX$ |
| Martingale | Preserved under adapted $L^2$ assumptions | Not preserved (correction term shifts mean) |
| Riemann sum | Left endpoint | Midpoint |
| Finance | Standard choice | Rarely used |
| Physics / geometry | Requires explicit noise correction | Natural formulation |

---

### 4. Conversion Formula

The two integrals are related by a **correction term** equal to half the quadratic covariation between the integrand and the Brownian motion.

Suppose $X_t$ satisfies $dX_t = b(t,X_t)\,dt + \sigma(t,X_t)\,dW_t$. Then:

$$
\boxed{
\int_0^t f(s, X_s) \circ dW_s
= \int_0^t f(s, X_s) \, dW_s
+ \frac{1}{2}\int_0^t \frac{\partial f}{\partial x}(s, X_s)\,\sigma(s, X_s) \, ds
}
$$

where $\sigma(s,X_s)$ is the diffusion coefficient of $X_t$. Equivalently, using quadratic covariation notation:

$$
\int_0^t f \circ dW = \int_0^t f \, dW + \frac{1}{2}[f({\cdot},X_{\cdot}), W]_t
$$

**Note**: the correction term depends on $\sigma(s,X_s)$—how strongly the Brownian noise affects the process $X_t$. If $f$ does not depend on $X_t$ (deterministic integrand), then $\partial f/\partial x = 0$ and the two integrals coincide.

---

### 5. Numerical Illustration

The following script simulates one Brownian path and compares the left-point and midpoint approximations to $\int_0^T B_t\, dB_t$.

```python
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
from typing import Optional


@dataclass
class BrownianMotionResult:
    time_steps: np.ndarray
    time_step_size: float
    brownian_paths: np.ndarray
    increments: np.ndarray


class BrownianMotion:
    DEFAULT_STEPS_PER_YEAR = 252

    def __init__(self, maturity_time: float = 1.0, seed: Optional[int] = None):
        if maturity_time <= 0:
            raise ValueError("maturity_time must be positive")
        self.maturity_time = maturity_time
        self.rng = np.random.RandomState(seed)

    def simulate(self, num_paths: int = 1,
                 num_steps: Optional[int] = None) -> BrownianMotionResult:
        if num_steps is None:
            num_steps = int(self.maturity_time * self.DEFAULT_STEPS_PER_YEAR)
        time_steps = np.linspace(0, self.maturity_time, num_steps + 1)
        dt = time_steps[1] - time_steps[0]
        increments = self.rng.standard_normal((num_paths, num_steps)) * np.sqrt(dt)
        brownian_paths = np.concatenate(
            [np.zeros((num_paths, 1)), increments.cumsum(axis=1)], axis=1
        )
        return BrownianMotionResult(time_steps=time_steps, time_step_size=dt,
                                    brownian_paths=brownian_paths, increments=increments)


if __name__ == "__main__":
    N = 1000
    bm = BrownianMotion(maturity_time=1.0, seed=42)
    result = bm.simulate(num_paths=1, num_steps=N)

    W = result.brownian_paths[0]
    dW = result.increments[0]
    t = result.time_steps

    # Itô integral (left-point): Σ W_{t_j} ΔW_j
    ito = np.concatenate(([0.0], np.cumsum(W[:-1] * dW)))

    # Stratonovich integral (midpoint): Σ ½(W_{t_j} + W_{t_{j+1}}) ΔW_j
    strat = np.concatenate(([0.0], np.cumsum(0.5 * (W[:-1] + W[1:]) * dW)))

    # Theoretical closed forms
    ito_theory = 0.5 * (W**2 - t)
    strat_theory = 0.5 * W**2

    difference = strat - ito

    plt.figure(figsize=(12, 6))
    plt.plot(t, ito,        "b-",  label="Itô (left-point approximation)")
    plt.plot(t, ito_theory, "b--", label=r"Exact Itô: $\frac{1}{2}(W_t^2 - t)$")
    plt.plot(t, strat,        "r-",  label="Stratonovich (midpoint approximation)")
    plt.plot(t, strat_theory, "r--", label=r"Exact Stratonovich: $\frac{1}{2}W_t^2$")
    plt.plot(t, difference, "k-",  label=r"Stratonovich $-$ Itô")
    plt.plot(t, 0.5 * t,    "k--", label=r"Exact difference: $\frac{1}{2}t$")
    plt.legend(loc="upper left", fontsize=9)
    plt.xlabel("$t$")
    plt.title(r"Itô vs. Stratonovich for $\int_0^t B_s\,dB_s$")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("./image/ito_and_stratonovich_integration.png", dpi=150)
    plt.show()
```

![Itô vs Stratonovich](./image/ito_and_stratonovich_integration.png)

The numerical approximations closely track their theoretical values. The black curve shows the difference between the Stratonovich and Itô approximations; it follows the $t/2$ line (dashed black), confirming that the gap equals exactly half the quadratic variation.

---

### 6. Summary

$$
\boxed{
\int_0^t f(s,X_s) \circ dW_s = \int_0^t f(s,X_s) \, dW_s + \frac{1}{2}\int_0^t \frac{\partial f}{\partial x}(s,X_s)\,\sigma(s,X_s) \, ds
}
\quad \text{where } dX_t = b\,dt + \sigma\,dW_t
$$

The Stratonovich integral and the Itô integral differ by a correction term equal to half the quadratic covariation between the integrand and the driving Brownian motion. The correction is zero when the integrand does not depend on the stochastic process.

| Aspect | Itô | Stratonovich |
|---|---|---|
| Definition | Left endpoint | Midpoint |
| Chain rule | Itô's formula (with correction) | Classical (no correction) |
| Martingale | Preserved under adapted $L^2$ | Not generally preserved |
| Wong-Zakai limit | No | Yes |
| Finance | Standard choice | Rarely used |
| Physics / geometry | Requires noise correction | Natural formulation |

??? note "Advanced: Wong-Zakai theorem"
    The **Wong-Zakai theorem** explains why Stratonovich integrals appear naturally in physics. Replace Brownian motion $W_t$ by a smooth approximation $W_t^{(n)}$ (e.g., piecewise linear interpolation) and solve the ordinary differential equation:

    $$
    \frac{dX_t^{(n)}}{dt} = b(X_t^{(n)}) + \sigma(X_t^{(n)})\frac{dW_t^{(n)}}{dt}
    $$

    As $n \to \infty$, the solutions $X_t^{(n)}$ converge to the solution of the **Stratonovich SDE** $dX_t = b(X_t)\,dt + \sigma(X_t) \circ dW_t$, not the Itô SDE. The equivalent Itô form requires an extra **noise-induced drift** $\frac{1}{2}\sigma(X_t)\sigma'(X_t)\,dt$.

    This means: in physical models derived from smooth-noise limits, Stratonovich is the natural formulation, and the Itô form requires an explicit correction to account for truly delta-correlated (white) noise.

??? note "Advanced: when to use each convention"
    **Itô** is naturally aligned with mathematical finance (risk-neutral pricing, Black-Scholes, Girsanov theorem), filtering theory, and numerical simulation (Euler-Maruyama is Itô by construction).

    **Stratonovich** is naturally aligned with physics (Langevin equations, thermodynamics), stochastic flows on manifolds, smooth-noise limits (Wong-Zakai), and contexts where coordinate-invariant differential rules are essential.

    The choice is not about correctness—both are mathematically valid. It depends on which properties are most important for the application at hand.

??? note "Advanced: overdamped Langevin equation"
    The overdamped Langevin equation is often written in physics as:

    $$
    \gamma \frac{dx}{dt} = -V'(x) + \sqrt{2\gamma k_B T}\,\xi(t)
    $$

    where $\xi(t)$ is white noise. The Wong-Zakai interpretation yields the Stratonovich SDE:

    $$
    dx = -\frac{V'(x)}{\gamma}\, dt + \sqrt{\frac{2k_B T}{\gamma}} \circ dW_t
    $$

    For state-independent diffusion (as here), the Itô and Stratonovich forms coincide. When the diffusion coefficient depends on $x$, the two forms differ by a state-dependent noise-induced drift, which has important physical consequences (e.g., in thermophoresis and stochastic resonance).

---

## Exercises

**Exercise 1.** Compute the Stratonovich integral $\int_0^t s \circ dB_s$. Does it differ from the Ito integral $\int_0^t s\, dB_s$? Explain why or why not, using the conversion formula.

??? success "Solution to Exercise 1"
    The integrand $f(s) = s$ is deterministic — it does not depend on $B_s$. Using the conversion formula:

    $$
    \int_0^t f(s) \circ dB_s = \int_0^t f(s)\, dB_s + \frac{1}{2}\int_0^t \frac{\partial f}{\partial x}(s)\, \sigma(s)\, ds
    $$

    Since $f(s) = s$ does not depend on the stochastic process (i.e., $\partial f / \partial x = 0$), the correction term vanishes:

    $$
    \int_0^t s \circ dB_s = \int_0^t s\, dB_s
    $$

    The two integrals are identical. This illustrates the general principle: **when the integrand does not depend on the driving Brownian motion, the Ito and Stratonovich integrals coincide**.

---

**Exercise 2.** Using the conversion formula

$$
\int_0^t f(B_s) \circ dB_s = \int_0^t f(B_s)\, dB_s + \frac{1}{2}\int_0^t f'(B_s)\, ds
$$

compute $\int_0^t B_s^2 \circ dB_s$ and verify that the result is consistent with the classical chain rule applied to $g(x) = x^3/3$.

??? success "Solution to Exercise 2"
    Apply the conversion formula with $f(x) = x^2$ (so $f'(x) = 2x$) and $X_t = B_t$ (so $\sigma = 1$):

    $$
    \int_0^t B_s^2 \circ dB_s = \int_0^t B_s^2\, dB_s + \frac{1}{2}\int_0^t 2B_s \cdot 1\, ds = \int_0^t B_s^2\, dB_s + \int_0^t B_s\, ds
    $$

    From Ito's formula applied to $x^3/3$ (Exercise 5 of the Ito integration intuitive section): $\int_0^t B_s^2\, dB_s = \frac{1}{3}B_t^3 - \int_0^t B_s\, ds$. Substituting:

    $$
    \int_0^t B_s^2 \circ dB_s = \frac{1}{3}B_t^3 - \int_0^t B_s\, ds + \int_0^t B_s\, ds = \frac{1}{3}B_t^3
    $$

    **Verification via the classical chain rule:** For $g(x) = x^3/3$, the classical chain rule gives $dg(B_t) = g'(B_t) \circ dB_t = B_t^2 \circ dB_t$. Integrating: $g(B_t) - g(0) = \int_0^t B_s^2 \circ dB_s$, so $\int_0^t B_s^2 \circ dB_s = B_t^3/3$. ✓

---

**Exercise 3.** The Stratonovich chain rule gives $d(\sin B_t) = \cos(B_t) \circ dB_t$. Convert this to Ito form by finding $d(\sin B_t)$ using Ito's formula. Identify the drift correction term and verify it matches the conversion formula.

??? success "Solution to Exercise 3"
    **Stratonovich chain rule:** $d(\sin B_t) = \cos(B_t) \circ dB_t$.

    **Ito's formula** applied to $f(x) = \sin x$ with $f'(x) = \cos x$, $f''(x) = -\sin x$:

    $$
    d(\sin B_t) = \cos(B_t)\, dB_t + \frac{1}{2}(-\sin(B_t))\, dt = \cos(B_t)\, dB_t - \frac{1}{2}\sin(B_t)\, dt
    $$

    **Identifying the drift correction:** The Ito form has a drift term $-\frac{1}{2}\sin(B_t)\, dt$ that is absent from the Stratonovich form.

    **Verification via the conversion formula:** With $f(x) = \cos x$ (the integrand in the Stratonovich integral), $f'(x) = -\sin x$, and $\sigma = 1$:

    $$
    \cos(B_t) \circ dB_t = \cos(B_t)\, dB_t + \frac{1}{2}(-\sin(B_t)) \cdot 1\, dt
    $$

    This matches the Ito form: $d(\sin B_t) = \cos(B_t)\, dB_t - \frac{1}{2}\sin(B_t)\, dt$. ✓

---

**Exercise 4.** Consider the Stratonovich SDE $dX_t = \sigma X_t \circ dB_t$ (no drift in Stratonovich form). Convert this to its equivalent Ito SDE. What drift term appears in the Ito form? Solve the resulting Ito SDE.

??? success "Solution to Exercise 4"
    The Stratonovich SDE is $dX_t = \sigma X_t \circ dB_t$. Apply the conversion formula with $f(x) = \sigma x$, so $f'(x) = \sigma$, and the diffusion coefficient of $X_t$ is $\sigma X_t$:

    $$
    \sigma X_t \circ dB_t = \sigma X_t\, dB_t + \frac{1}{2}\sigma \cdot \sigma X_t\, dt = \sigma X_t\, dB_t + \frac{\sigma^2}{2}X_t\, dt
    $$

    The equivalent Ito SDE is:

    $$
    dX_t = \frac{\sigma^2}{2}X_t\, dt + \sigma X_t\, dB_t
    $$

    A drift term $\frac{\sigma^2}{2}X_t\, dt$ appears in the Ito form. This is geometric Brownian motion with $\mu = \sigma^2/2$. The solution is:

    $$
    X_t = X_0 \exp\!\left(\left(\frac{\sigma^2}{2} - \frac{\sigma^2}{2}\right)t + \sigma B_t\right) = X_0 e^{\sigma B_t}
    $$

    In the Stratonovich framework, the zero-drift SDE $dX_t = \sigma X_t \circ dB_t$ has the "naive" exponential solution $X_t = X_0 e^{\sigma B_t}$, consistent with the classical chain rule.

---

**Exercise 5.** Let $f(x) = e^x$. Using the Stratonovich chain rule, write $d(e^{B_t})$ in Stratonovich form. Then convert to Ito form and verify that you recover the standard result from Ito's formula.

??? success "Solution to Exercise 5"
    **Stratonovich chain rule** applied to $f(x) = e^x$ with $X_t = B_t$:

    $$
    d(e^{B_t}) = e^{B_t} \circ dB_t
    $$

    **Converting to Ito form** using $f(x) = e^x$, $f'(x) = e^x$, $\sigma = 1$:

    $$
    e^{B_t} \circ dB_t = e^{B_t}\, dB_t + \frac{1}{2}e^{B_t}\, dt
    $$

    So in Ito form:

    $$
    d(e^{B_t}) = e^{B_t}\, dB_t + \frac{1}{2}e^{B_t}\, dt
    $$

    **Verification via Ito's formula:** With $f(x) = e^x$, $f'(x) = e^x$, $f''(x) = e^x$:

    $$
    d(e^{B_t}) = e^{B_t}\, dB_t + \frac{1}{2}e^{B_t}\, dt
    $$

    This matches. ✓

---

**Exercise 6.** Using the coin-flip approximation with $n = 10$ and the sequence $H, T, H, H, T, H, T, T, H, H$, compute both the left-endpoint (Ito) and midpoint (Stratonovich) sums for $\int_0^1 B_s\, dB_s$. Verify that their difference is approximately $\frac{1}{2} \cdot 1 = 0.5$ times the quadratic variation sum $\sum (\Delta B_k)^2$.

??? success "Solution to Exercise 6"
    With $n = 10$, $\Delta t = 1/10$, $\Delta B_k = \pm 1/\sqrt{10}$. The sequence $H, T, H, H, T, H, T, T, H, H$ gives increments $+,-,+,+,-,+,-,-,+,+$ in units of $1/\sqrt{10}$.

    Build the path:

    | $k$ | $\Delta B_k$ | $B_{t_k}$ |
    |-----|-------------|-----------|
    | 0 | | $0$ |
    | 1 | $+1/\sqrt{10}$ | $1/\sqrt{10}$ |
    | 2 | $-1/\sqrt{10}$ | $0$ |
    | 3 | $+1/\sqrt{10}$ | $1/\sqrt{10}$ |
    | 4 | $+1/\sqrt{10}$ | $2/\sqrt{10}$ |
    | 5 | $-1/\sqrt{10}$ | $1/\sqrt{10}$ |
    | 6 | $+1/\sqrt{10}$ | $2/\sqrt{10}$ |
    | 7 | $-1/\sqrt{10}$ | $1/\sqrt{10}$ |
    | 8 | $-1/\sqrt{10}$ | $0$ |
    | 9 | $+1/\sqrt{10}$ | $1/\sqrt{10}$ |
    | 10 | $+1/\sqrt{10}$ | $2/\sqrt{10}$ |

    **Ito (left-endpoint) sum:** $\sum_{k=0}^{9} B_{t_k} \Delta B_k$

    $$
    = \frac{1}{10}\left(0 \cdot (+1) + 1 \cdot (-1) + 0 \cdot (+1) + 1 \cdot (+1) + 2 \cdot (-1) + 1 \cdot (+1) + 2 \cdot (-1) + 1 \cdot (-1) + 0 \cdot (+1) + 1 \cdot (+1)\right)
    $$

    $$
    = \frac{1}{10}(0 - 1 + 0 + 1 - 2 + 1 - 2 - 1 + 0 + 1) = \frac{-3}{10}
    $$

    **Verification:** $\frac{1}{2}(B_1^2 - 1) = \frac{1}{2}(4/10 - 1) = \frac{1}{2}(-6/10) = -3/10$. ✓

    **Stratonovich (midpoint) sum:** $\sum_{k=0}^{9} \frac{1}{2}(B_{t_k} + B_{t_{k+1}}) \Delta B_k$

    $$
    = \frac{1}{2} \cdot \frac{1}{10}\left((0+1)(+1) + (1+0)(-1) + (0+1)(+1) + (1+2)(+1) + (2+1)(-1)\right
    $$

    $$
    \left.+ (1+2)(+1) + (2+1)(-1) + (1+0)(-1) + (0+1)(+1) + (1+2)(+1)\right)
    $$

    $$
    = \frac{1}{20}(1 - 1 + 1 + 3 - 3 + 3 - 3 - 1 + 1 + 3) = \frac{4}{20} = \frac{1}{5}
    $$

    **Verification:** $\frac{1}{2}B_1^2 = \frac{1}{2} \cdot 4/10 = 2/10 = 1/5$. ✓

    **Difference:** Stratonovich $-$ Ito $= 1/5 - (-3/10) = 1/5 + 3/10 = 5/10 = 1/2$.

    **Quadratic variation sum:** $\sum_{k=0}^{9} (\Delta B_k)^2 = 10 \cdot (1/10) = 1$.

    So the difference is $\frac{1}{2} \cdot 1 = 1/2$, exactly half the quadratic variation sum. ✓

---

**Exercise 7.** Explain why the Stratonovich integral $\int_0^t B_s \circ dB_s = \frac{1}{2}B_t^2$ is not a martingale, while the Ito integral $\int_0^t B_s\, dB_s = \frac{1}{2}(B_t^2 - t)$ is a martingale. What property of the midpoint evaluation causes the martingale property to fail?

??? success "Solution to Exercise 7"
    **Ito integral $\frac{1}{2}(B_t^2 - t)$ is a martingale.** For $s < t$:

    $$
    \mathbb{E}\!\left[\frac{B_t^2 - t}{2} \,\Big|\, \mathcal{F}_s\right] = \frac{1}{2}\left(\mathbb{E}[B_t^2 \mid \mathcal{F}_s] - t\right) = \frac{1}{2}(B_s^2 + (t-s) - t) = \frac{B_s^2 - s}{2}
    $$

    This equals $I_s$, confirming the martingale property. ✓

    **Stratonovich integral $\frac{1}{2}B_t^2$ is not a martingale.** For $s < t$:

    $$
    \mathbb{E}\!\left[\frac{B_t^2}{2} \,\Big|\, \mathcal{F}_s\right] = \frac{1}{2}(B_s^2 + (t - s)) = \frac{B_s^2}{2} + \frac{t-s}{2} \neq \frac{B_s^2}{2}
    $$

    The conditional expectation exceeds the current value by $(t-s)/2$, so $\frac{1}{2}B_t^2$ is a **submartingale**, not a martingale.

    **Why midpoint evaluation breaks the martingale property.** The martingale property of the Ito integral relies on the independence of the integrand from the future Brownian increment: $\mathbb{E}[H_{t_k} \Delta B_k \mid \mathcal{F}_{t_k}] = H_{t_k} \cdot \mathbb{E}[\Delta B_k \mid \mathcal{F}_{t_k}] = 0$. With left-endpoint evaluation, $H_{t_k}$ is $\mathcal{F}_{t_k}$-measurable and thus independent of $\Delta B_k$.

    With midpoint evaluation, the integrand involves $\frac{1}{2}(B_{t_k} + B_{t_{k+1}})$, which partially depends on $B_{t_{k+1}}$ and hence on the increment $\Delta B_k$. This creates a positive correlation between the integrand and the increment: $\mathbb{E}[\frac{1}{2}(B_{t_k} + B_{t_{k+1}})\Delta B_k] = \frac{1}{2}\mathbb{E}[(\Delta B_k)^2] = \frac{\Delta t}{2} > 0$. Summing these positive contributions produces the systematic upward drift of $t/2$, destroying the martingale property.
