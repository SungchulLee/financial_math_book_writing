# Numerical Stability and Branch Cuts

Computing the Heston characteristic function requires evaluating complex square roots and complex logarithms, both of which are multi-valued functions. A careless implementation using the principal branch of these functions introduces discontinuities in the characteristic function that corrupt Fourier pricing. This section analyzes the source of these discontinuities, derives the stable formulation that avoids them, and presents the rotation count method as a general-purpose safeguard.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Identify the branch cut problem in the Heston characteristic function
    2. Derive the Albrecher stable formulation and verify the condition $|g| < 1$
    3. Implement the rotation count method for continuous complex logarithms
    4. Diagnose and fix numerical instabilities in characteristic function evaluation

---

## Intuition

Every complex-valued function involving $\sqrt{\cdot}$ or $\log(\cdot)$ faces a fundamental ambiguity: these functions are multi-valued, and any single-valued definition must introduce a discontinuity somewhere in the complex plane --- the **branch cut**. When the characteristic function argument $u$ sweeps along the real line during Fourier inversion, the intermediate quantities $\gamma(u)$ and $\log(1 - g e^{-\gamma\tau})$ may cross a branch cut, causing an artificial jump in the CF. This jump has nothing to do with the underlying probability distribution; it is purely a computational artifact that produces wild oscillations or sign errors in option prices.

The solution is to choose branches carefully so that the CF remains a continuous function of $u$ along the integration path.

---

## The Branch Cut Problem

Recall the Heston characteristic function involves the discriminant

$$
\gamma(u) = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}
$$

and the ratio

$$
g(u) = \frac{\kappa - i\rho\xi u - \gamma(u)}{\kappa - i\rho\xi u + \gamma(u)}
$$

The function $C(\tau, u)$ contains a complex logarithm

$$
C(\tau, u) = \frac{\kappa\theta}{\xi^2}\left[(\kappa - i\rho\xi u - \gamma)\tau - 2\log\!\left(\frac{1 - g e^{-\gamma\tau}}{1 - g}\right)\right]
$$

!!! warning "Source of Discontinuity"
    The principal branch of the complex square root $\sqrt{z}$ has a branch cut along the negative real axis: $\sqrt{z}$ jumps by a sign when $z$ crosses $(-\infty, 0)$. If $(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)$ becomes a negative real number for some $u \in \mathbb{R}$, then $\gamma(u)$ flips sign, causing $g(u)$ and all downstream quantities to jump discontinuously.

    Similarly, the principal branch of $\log(z)$ has a branch cut along $(-\infty, 0]$. If the argument $\frac{1 - ge^{-\gamma\tau}}{1-g}$ crosses the negative real axis, the imaginary part of the logarithm jumps by $2\pi$.

---

## Heston 1993 Original Formulation

In Heston's original 1993 paper, the characteristic function was written with

$$
D_{\text{orig}}(\tau, u) = \frac{\kappa - i\rho\xi u + \gamma}{\xi^2} \cdot \frac{1 - e^{\gamma\tau}}{1 - h \, e^{\gamma\tau}}
$$

where

$$
h = \frac{\kappa - i\rho\xi u + \gamma}{\kappa - i\rho\xi u - \gamma}
$$

and the corresponding $C$ function involves $\log(1 - h \, e^{\gamma\tau})$.

!!! danger "The Instability"
    In this formulation, $|h| \geq 1$ generically. As $\tau$ increases, $|h \, e^{\gamma\tau}|$ grows exponentially, and the argument of the logarithm $1 - h e^{\gamma\tau}$ sweeps through large circles in the complex plane, inevitably crossing the branch cut of $\log$. This makes the original formulation **numerically unstable for moderate to large $\tau$**.

    The exponential $e^{\gamma\tau}$ with $\text{Re}(\gamma) > 0$ amplifies any branch-cut crossing, making the problem worse at longer maturities --- precisely where accurate pricing is most needed.

---

## Albrecher Stable Formulation

The key insight is to rewrite the CF so that all exponentials are **decaying** rather than growing.

!!! info "Theorem (Albrecher-Mayer-Schoutens-Tistaert Formulation)"
    Define $\gamma$ with the branch chosen so that $\text{Re}(\gamma) \geq 0$, and set

    $$
    g = \frac{\kappa - i\rho\xi u - \gamma}{\kappa - i\rho\xi u + \gamma}
    $$

    Then $|g| \leq 1$, and the stable Heston CF components are

    $$
    D(\tau, u) = \frac{\kappa - i\rho\xi u - \gamma}{\xi^2} \cdot \frac{1 - e^{-\gamma\tau}}{1 - g \, e^{-\gamma\tau}}
    $$

    $$
    C(\tau, u) = (r-q)iu\tau + \frac{\kappa\theta}{\xi^2}\left[(\kappa - i\rho\xi u - \gamma)\tau - 2\log\!\left(\frac{1 - g \, e^{-\gamma\tau}}{1 - g}\right)\right]
    $$

**Proof that $|g| \leq 1$.** Write $\alpha = \kappa - i\rho\xi u$ and $\gamma = \sqrt{\alpha^2 + \xi^2(iu + u^2)}$. Then

$$
g = \frac{\alpha - \gamma}{\alpha + \gamma}
$$

The condition $|g| \leq 1$ is equivalent to $|\alpha - \gamma| \leq |\alpha + \gamma|$. By the triangle inequality, this holds whenever $\text{Re}(\alpha \bar{\gamma}) \geq 0$. Since $\text{Re}(\gamma) \geq 0$ and $\text{Re}(\alpha) = \kappa > 0$, this condition is satisfied. $\square$

**Why stability follows.** Since $|g| < 1$ and $\text{Re}(\gamma) \geq 0$, the product $g \, e^{-\gamma\tau}$ satisfies $|g \, e^{-\gamma\tau}| < 1$. Therefore:

1. The denominator $1 - g \, e^{-\gamma\tau}$ never vanishes
2. The argument of the logarithm $\frac{1 - g e^{-\gamma\tau}}{1 - g}$ stays in the right half-plane, away from the branch cut of $\log$
3. As $\tau \to \infty$, $g \, e^{-\gamma\tau} \to 0$, so the logarithm converges smoothly

---

## The Rotation Count Method

Even with the Albrecher formulation, subtle branch-cut crossings can occur for extreme parameter combinations or very large $u$. The **rotation count method** of Kahl and Jackel provides an additional safeguard.

!!! info "Definition (Continuous Complex Logarithm)"
    Let $f: [u_{\min}, u_{\max}] \to \mathbb{C} \setminus \{0\}$ be a continuous function. The **continuous complex logarithm** $\text{Log}_c(f(u))$ is defined by starting from $\text{Log}_c(f(u_{\min})) = \text{Log}(f(u_{\min}))$ (principal value) and adjusting the imaginary part at each subsequent point to maintain continuity:

    $$
    \text{Log}_c(f(u_{j+1})) = \log|f(u_{j+1})| + i\left[\arg(f(u_{j+1})) + 2\pi n_j\right]
    $$

    where $n_j$ is an integer chosen so that $|\text{Im}(\text{Log}_c(f(u_{j+1}))) - \text{Im}(\text{Log}_c(f(u_j)))| < \pi$.

**Algorithm (Rotation Count).** When evaluating the Heston CF at a sequence of points $u_0 < u_1 < \cdots < u_N$:

1. Initialize: evaluate $\text{Log}(1 - g(u_0) e^{-\gamma(u_0)\tau})$ using the principal branch
2. For each $j = 1, \ldots, N$:
    - Compute $\gamma(u_j)$ and $g(u_j)$
    - Evaluate $w_j = 1 - g(u_j) e^{-\gamma(u_j)\tau}$
    - Compute the principal value $\text{Log}(w_j)$
    - If $|\text{Im}(\text{Log}(w_j)) - \text{Im}(\text{Log}_c(w_{j-1}))| > \pi$, adjust by $\pm 2\pi$
    - Store the adjusted value as $\text{Log}_c(w_j)$

!!! tip "When Is the Rotation Count Necessary?"
    For typical equity option pricing parameters ($\kappa \in [0.5, 5]$, $\xi \in [0.1, 1]$, $|\rho| \leq 0.95$, $\tau \leq 5$), the Albrecher formulation alone is sufficient. The rotation count becomes important when:

    - The Fourier inversion integrates over very large $u$ (e.g., $u > 50$)
    - Parameters are extreme ($\xi > 1$ or $\kappa$ very small)
    - Long maturities ($\tau > 10$) are considered

---

## Choosing the Square Root Branch

The choice of branch for $\gamma = \sqrt{z}$ where $z = (\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)$ deserves explicit attention.

**Standard convention.** Most programming languages define $\sqrt{z}$ as the principal square root with $\text{Re}(\sqrt{z}) \geq 0$. This is the correct choice for the Albrecher formulation.

**Alternative convention.** Some implementations choose the branch by requiring $\text{Re}(\gamma) > 0$ explicitly, which can be enforced by:

$$
\gamma \leftarrow \gamma \cdot \text{sign}(\text{Re}(\gamma))
$$

where $\text{sign}(x) = +1$ if $x > 0$ and $-1$ if $x < 0$.

!!! warning "Pitfall with Sign Flips"
    If one naively uses $\text{sign}(\text{Re}(\gamma))$ as a correction, the sign function itself introduces a discontinuity when $\text{Re}(\gamma) = 0$. In practice, this occurs at isolated points and rarely affects integration accuracy, but a robust implementation should handle this edge case by slight perturbation or by using the rotation count as a fallback.

---

## Diagnostic Example

Consider the Heston parameters $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $v_0 = 0.04$, $\tau = 1$.

**Evaluate $\gamma(u)$ for $u \in [0, 50]$:**

At $u = 0$: $\gamma = \sqrt{\kappa^2} = \kappa = 1.5$ (real, positive).

At $u = 10$: $\gamma = \sqrt{(1.5 + 2.1i)^2 + 0.09(10i + 100)} = \sqrt{-2.16 + 6.3i + 0.9i + 9}$. The argument under the square root is complex with positive real part, so $\text{Re}(\gamma) > 0$ and no branch issue arises.

At $u = 30$: the argument under the square root has a large negative real part: $(1.5 + 6.3i)^2 + 0.09(30i + 900) = -37.44 + 18.9i + 2.7i + 81 = 43.56 + 21.6i$. Still safe.

**The original formulation failure.** With $h = 1/g$ and $e^{\gamma\tau}$ growing, the quantity $h e^{\gamma\tau}$ at $u = 30$ has magnitude $|h| \cdot e^{\text{Re}(\gamma)} \approx e^{6} \approx 400$. The logarithm of $1 - 400 \cdot e^{i\theta}$ is dominated by the large-magnitude term and its phase rotates rapidly with $u$, causing the imaginary part of $\log$ to jump by $2\pi$ at each branch-cut crossing.

**The Albrecher formulation.** With $|g| < 1$ and $e^{-\gamma\tau}$ decaying, the quantity $g e^{-\gamma\tau}$ at $u = 30$ has magnitude approximately $|g| \cdot e^{-6} \approx 0.002$. The argument of the logarithm is $1 - 0.002 \cdot e^{i\phi} \approx 1$, which is solidly in the right half-plane. No branch-cut crossing occurs.

??? example "Impact on Option Prices"
    Using the original Heston formulation with Simpson's rule integration over $u \in [0, 100]$:

    - At $\tau = 0.1$: both formulations agree to 8 decimal places
    - At $\tau = 1.0$: the original formulation produces a call price of \$7.94 (correct: \$7.96), an error of 25 basis points
    - At $\tau = 5.0$: the original formulation returns a negative call price, which is impossible

    The Albrecher formulation returns correct prices at all maturities without special handling.

---

## Summary

The Heston characteristic function involves multi-valued complex functions (square root and logarithm) that introduce artificial discontinuities if branch cuts are not handled carefully. The original Heston (1993) formulation uses exponentially growing terms $e^{\gamma\tau}$ that amplify branch-cut crossings, producing numerical instabilities at moderate to long maturities. The Albrecher stable formulation replaces these with decaying exponentials $e^{-\gamma\tau}$ by choosing $g$ such that $|g| < 1$, eliminating nearly all branch-cut issues. The rotation count method of Kahl and Jackel provides an additional safeguard by tracking the winding number of the logarithm's argument along the integration path. Any production implementation of the Heston characteristic function should use the Albrecher formulation as the default, with the rotation count available as a fallback for extreme parameters.

---

## Exercises

**Exercise 1.** The principal square root $\gamma = \sqrt{z}$ for complex $z$ has a branch cut along $(-\infty, 0]$. For $z = (\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)$ with $\kappa = 2$, $\sigma_v = 0.3$, $\rho = -0.7$, compute $z$ at $u = 5$ and verify that $z$ does not lie on the branch cut.

---

**Exercise 2.** Explain the "little Heston trap": the original 1993 formulation uses terms $e^{+\gamma\tau}$ that grow exponentially for large $\tau$, causing catastrophic cancellation when combined with the denominator $1 - g^{-1}e^{+\gamma\tau}$. How does the Albrecher formulation avoid this?

---

**Exercise 3.** The Albrecher formulation ensures $|g| < 1$ by choosing $g = (\beta - \gamma)/(\beta + \gamma)$ with $\operatorname{Re}(\gamma) > 0$. Prove that $|g| < 1$ when $\operatorname{Re}(\gamma) > 0$ and $\operatorname{Re}(\beta) < 0$.

---

**Exercise 4.** The rotation count method of Kahl and Jackel tracks the winding number of the complex logarithm's argument. Explain why discontinuities of $2\pi i$ in the complex logarithm can corrupt the characteristic function and how the rotation count corrects for them.

---

**Exercise 5.** Implement both the Heston 1993 and Albrecher formulations and compare them numerically for $\tau = 5$, $\kappa = 0.5$, $\sigma_v = 1$, $\rho = -0.9$ at $u = 1, 5, 10, 20$. At which $u$ values does the 1993 formulation break down?

---

**Exercise 6.** For a production implementation, describe a testing strategy to verify numerical stability: what parameter ranges should be tested, what reference values can be used, and how should one detect branch-cut crossing errors?
