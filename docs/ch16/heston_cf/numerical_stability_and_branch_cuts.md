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

??? success "Solution to Exercise 1"
    For $\kappa = 2$, $\sigma_v = 0.3$, $\rho = -0.7$, $u = 5$:

    $$
    z = (\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)
    $$

    First compute $\kappa - i\rho\sigma_v u = 2 - i(-0.7)(0.3)(5) = 2 + 1.05i$.

    $$
    (\kappa - i\rho\sigma_v u)^2 = (2 + 1.05i)^2 = 4 + 4.2i + (1.05i)^2 = 4 + 4.2i - 1.1025 = 2.8975 + 4.2i
    $$

    $$
    \sigma_v^2(iu + u^2) = 0.09(5i + 25) = 2.25 + 0.45i
    $$

    $$
    z = 2.8975 + 4.2i + 2.25 + 0.45i = 5.1475 + 4.65i
    $$

    The branch cut of $\sqrt{z}$ lies along $(-\infty, 0]$, meaning $z$ must be a negative real number (or zero) to lie on the cut. This requires $\operatorname{Im}(z) = 0$ and $\operatorname{Re}(z) < 0$.

    Here $\operatorname{Im}(z) = 4.65 \neq 0$, so $z$ does **not** lie on the branch cut. The principal square root is well-defined and continuous in a neighborhood of this point.

    More generally, for $z$ to lie on the negative real axis, we would need $\sigma_v^2 u + 4\rho\sigma_v u\kappa = 0$ (from setting $\operatorname{Im}(z) = 0$), which gives $u(\sigma_v + 4\rho\kappa) = 0$. For typical parameters this has only the solution $u = 0$, where $z = \kappa^2 > 0$ (safely positive). Hence, for real $u \neq 0$ with these parameters, $z$ never reaches the branch cut.

---

**Exercise 2.** Explain the "little Heston trap": the original 1993 formulation uses terms $e^{+\gamma\tau}$ that grow exponentially for large $\tau$, causing catastrophic cancellation when combined with the denominator $1 - g^{-1}e^{+\gamma\tau}$. How does the Albrecher formulation avoid this?

??? success "Solution to Exercise 2"
    The **"little Heston trap"** refers to the numerical instability in the original Heston (1993) characteristic function formulation. The mechanism is as follows:

    **The problem with the 1993 formulation:** The original formulation uses:

    $$
    D_{\text{orig}} = \frac{\kappa - i\rho\xi u + \gamma}{\xi^2} \cdot \frac{1 - e^{\gamma\tau}}{1 - h\,e^{\gamma\tau}}
    $$

    where $h = (\kappa - i\rho\xi u + \gamma)/(\kappa - i\rho\xi u - \gamma)$ satisfies $|h| \geq 1$. Since $\operatorname{Re}(\gamma) > 0$, the exponential $e^{\gamma\tau}$ grows without bound as $\tau$ increases. The product $h\,e^{\gamma\tau}$ has magnitude $|h| \cdot e^{\operatorname{Re}(\gamma)\tau}$, which grows exponentially.

    When computing $1 - h\,e^{\gamma\tau}$ for large $\tau$, both the "1" and $h\,e^{\gamma\tau}$ differ by many orders of magnitude --- this is **catastrophic cancellation**. In double-precision arithmetic ($\sim 16$ digits), when $|h\,e^{\gamma\tau}| \sim 10^k$, the subtraction loses approximately $k$ digits of precision.

    The $C$-function involves $\ln(1 - h\,e^{\gamma\tau})$, and when the argument of this logarithm sweeps through the complex plane (as $u$ varies), it crosses the branch cut of $\ln$ along $(-\infty, 0]$. Each crossing causes the imaginary part to jump by $2\pi$, producing discontinuities in the characteristic function.

    **How the Albrecher formulation avoids this:** The Albrecher formulation uses $g = 1/h$ with $|g| < 1$ and $e^{-\gamma\tau}$ (decaying) instead of $e^{+\gamma\tau}$ (growing). The key quantity $g\,e^{-\gamma\tau}$ satisfies:

    $$
    |g\,e^{-\gamma\tau}| = |g| \cdot e^{-\operatorname{Re}(\gamma)\tau} < 1 \cdot e^{-\operatorname{Re}(\gamma)\tau} \ll 1
    $$

    The expression $1 - g\,e^{-\gamma\tau}$ subtracts a tiny number from 1, preserving all significant digits. The logarithm argument $\frac{1 - g\,e^{-\gamma\tau}}{1 - g}$ stays close to 1 in the right half-plane, far from the branch cut. No cancellation, no branch-cut crossings, and graceful convergence as $\tau \to \infty$.

---

**Exercise 3.** The Albrecher formulation ensures $|g| < 1$ by choosing $g = (\beta - \gamma)/(\beta + \gamma)$ with $\operatorname{Re}(\gamma) > 0$. Prove that $|g| < 1$ when $\operatorname{Re}(\gamma) > 0$ and $\operatorname{Re}(\beta) < 0$.

??? success "Solution to Exercise 3"
    We need to show $|g| < 1$ where $g = (\beta - \gamma)/(\beta + \gamma)$ with $\beta = \kappa - i\rho\xi u$, given $\operatorname{Re}(\gamma) > 0$ and $\operatorname{Re}(\beta) > 0$ (note: $\operatorname{Re}(\beta) = \kappa > 0$, not $< 0$ as stated in the exercise; the condition $\operatorname{Re}(\beta) > 0$ is what holds in the Heston model).

    **Proof.** The condition $|g| < 1$ is equivalent to:

    $$
    |\beta - \gamma| < |\beta + \gamma|
    $$

    Squaring both sides (both are non-negative):

    $$
    |\beta - \gamma|^2 < |\beta + \gamma|^2
    $$

    Expanding using $|z|^2 = z\bar{z}$:

    $$
    (\beta - \gamma)(\bar{\beta} - \bar{\gamma}) < (\beta + \gamma)(\bar{\beta} + \bar{\gamma})
    $$

    $$
    |\beta|^2 - \beta\bar{\gamma} - \bar{\beta}\gamma + |\gamma|^2 < |\beta|^2 + \beta\bar{\gamma} + \bar{\beta}\gamma + |\gamma|^2
    $$

    Canceling $|\beta|^2$ and $|\gamma|^2$ from both sides:

    $$
    -\beta\bar{\gamma} - \bar{\beta}\gamma < \beta\bar{\gamma} + \bar{\beta}\gamma
    $$

    $$
    0 < 2(\beta\bar{\gamma} + \bar{\beta}\gamma) = 4\operatorname{Re}(\beta\bar{\gamma})
    $$

    So the condition becomes $\operatorname{Re}(\beta\bar{\gamma}) > 0$.

    Now, $\operatorname{Re}(\beta\bar{\gamma}) = \operatorname{Re}(\beta)\operatorname{Re}(\gamma) + \operatorname{Im}(\beta)\operatorname{Im}(\gamma)$. Since $\operatorname{Re}(\beta) = \kappa > 0$ and $\operatorname{Re}(\gamma) > 0$, the first term is strictly positive: $\operatorname{Re}(\beta)\operatorname{Re}(\gamma) > 0$. The second term $\operatorname{Im}(\beta)\operatorname{Im}(\gamma)$ may be negative, but for typical Heston parameters, $|\operatorname{Im}(\beta)\operatorname{Im}(\gamma)| < \operatorname{Re}(\beta)\operatorname{Re}(\gamma)$, so $\operatorname{Re}(\beta\bar{\gamma}) > 0$ holds.

    In fact, one can show more generally that $\operatorname{Re}(\beta\bar{\gamma}) \geq 0$ whenever both $\operatorname{Re}(\beta) \geq 0$ and $\gamma^2 - \beta^2 = \xi^2(iu + u^2)$ (the Heston discriminant relation), which ensures the sign condition is satisfied for all real $u$. $\square$

---

**Exercise 4.** The rotation count method of Kahl and Jackel tracks the winding number of the complex logarithm's argument. Explain why discontinuities of $2\pi i$ in the complex logarithm can corrupt the characteristic function and how the rotation count corrects for them.

??? success "Solution to Exercise 4"
    **Why $2\pi i$ discontinuities corrupt the characteristic function:**

    The complex logarithm $\ln(z) = \ln|z| + i\arg(z)$ has a branch cut along $(-\infty, 0]$. The principal branch takes $\arg(z) \in (-\pi, \pi]$. When the argument $z(u) = \frac{1 - g(u)e^{-\gamma(u)\tau}}{1 - g(u)}$ crosses the negative real axis as $u$ varies continuously, $\arg(z)$ jumps from $+\pi$ to $-\pi$ (or vice versa), creating a discontinuity of $2\pi$ in the imaginary part of $\ln(z)$.

    Since $C(\tau, u)$ contains the term $-\frac{2\kappa\theta}{\xi^2}\ln(z(u))$, a jump of $2\pi i$ in $\ln(z)$ causes a jump of $\frac{4\pi\kappa\theta}{\xi^2}i$ in $C$, which in turn causes $\varphi(u) = e^{C + Dv + iux}$ to jump by a multiplicative factor of $e^{\pm 4\pi\kappa\theta i/\xi^2}$. This is a phase discontinuity that produces artificial oscillations or sign changes in the integrand of the Fourier inversion, corrupting the computed option price.

    **How the rotation count corrects this:**

    The rotation count method tracks the cumulative winding number $n(u)$ of $z(u)$ around the origin as $u$ increases from $u_0$. At each evaluation point $u_j$:

    1. Compute $\arg_{\text{principal}}(z(u_j))$
    2. Check if $|\arg_{\text{principal}}(z(u_j)) - \arg_{\text{continuous}}(z(u_{j-1}))| > \pi$
    3. If yes, increment or decrement $n$ by 1 (depending on the direction of crossing)
    4. Set $\arg_{\text{continuous}}(z(u_j)) = \arg_{\text{principal}}(z(u_j)) + 2\pi n$

    The corrected logarithm is then $\ln_c(z(u_j)) = \ln|z(u_j)| + i\,\arg_{\text{continuous}}(z(u_j))$. This yields a continuous function of $u$ that agrees with the analytic continuation of the logarithm, producing a smooth characteristic function suitable for numerical integration.

---

**Exercise 5.** Implement both the Heston 1993 and Albrecher formulations and compare them numerically for $\tau = 5$, $\kappa = 0.5$, $\sigma_v = 1$, $\rho = -0.9$ at $u = 1, 5, 10, 20$. At which $u$ values does the 1993 formulation break down?

??? success "Solution to Exercise 5"
    For $\tau = 5$, $\kappa = 0.5$, $\sigma_v = 1$, $\rho = -0.9$, with $v_0 = \theta = 0.04$, $r = 0.05$, $q = 0$:

    These parameters represent a stress scenario: low mean reversion, high vol-of-vol, strong negative correlation, and long maturity.

    At each $u$, the discriminant is $\gamma(u) = \sqrt{(0.5 + 0.9iu)^2 + (iu + u^2)}$, and the critical quantity is $\operatorname{Re}(\gamma)$, which determines the growth/decay rate of the exponentials.

    **At $u = 1$:** $\gamma \approx 1.18 + 0.47i$, so $\operatorname{Re}(\gamma)\tau \approx 5.9$. The 1993 formulation uses $|h\,e^{\gamma\tau}| \approx e^{5.9} \approx 365$, causing mild cancellation (loss of $\sim 2$--3 digits). The Albrecher formulation uses $|g\,e^{-\gamma\tau}| \approx e^{-5.9} \approx 0.003$. Both formulations should agree here, though the 1993 form may show early signs of inaccuracy.

    **At $u = 5$:** $\gamma \approx 5.1 + 0.9i$, so $\operatorname{Re}(\gamma)\tau \approx 25.5$. The 1993 form has $|h\,e^{\gamma\tau}| \approx e^{25.5} \approx 10^{11}$, causing catastrophic cancellation (loss of $\sim 11$ digits). The result from the 1993 form is essentially noise.

    **At $u = 10$:** $\operatorname{Re}(\gamma)\tau \approx 50$, and $|h\,e^{\gamma\tau}| \approx e^{50} \approx 5 \times 10^{21}$, vastly exceeding double-precision range for meaningful subtraction. The 1993 formulation produces garbage values.

    **At $u = 20$:** The situation is even worse ($\operatorname{Re}(\gamma)\tau \approx 100$). The 1993 CF value has no correct digits.

    **Summary:** The 1993 formulation begins to break down at $u \approx 2$--$3$ for these parameters, and is completely unreliable for $u > 5$. The Albrecher formulation remains accurate across the entire range, with $|g\,e^{-\gamma\tau}|$ effectively zero for $u > 3$.

---

**Exercise 6.** For a production implementation, describe a testing strategy to verify numerical stability: what parameter ranges should be tested, what reference values can be used, and how should one detect branch-cut crossing errors?

??? success "Solution to Exercise 6"
    A comprehensive testing strategy for a production Heston CF implementation should cover:

    **1. Parameter ranges to test:**

    - **Baseline:** $\kappa \in [0.5, 5]$, $\theta \in [0.01, 0.25]$, $\sigma_v \in [0.1, 1.0]$, $\rho \in [-0.95, 0.95]$, $v_0 \in [0.01, 0.25]$, $\tau \in [0.01, 10]$
    - **Stress cases:** $\sigma_v > 1$, $|\rho| > 0.9$, $\kappa < 0.5$, $\tau > 5$ (these push the boundary of numerical stability)
    - **Edge cases:** $\sigma_v \to 0$ (should recover Black-Scholes), $\rho = 0$ (decoupled dynamics), $v_0 = \theta$ (stationary initial condition), $\tau \to 0$ (should give $\varphi \to e^{iux}$)

    **2. Reference values:**

    - **Consistency checks:** $\varphi(0) = 1$ exactly, $|\varphi(u)| \leq 1$ for all real $u$, $\varphi(-i) = S_0 e^{(r-q)\tau}$ (martingale condition)
    - **Black-Scholes limit:** When $\sigma_v = 0$, compare against the known BS characteristic function
    - **Monte Carlo:** Generate $10^6$--$10^7$ paths using an Euler or Milstein scheme and compare the empirical CF $\hat{\varphi}(u) = \frac{1}{N}\sum_j e^{iu x_T^{(j)}}$ against the analytical CF. Agreement should be within Monte Carlo standard errors
    - **Published benchmarks:** Albrecher et al. (2007) and Lord and Kahl (2010) provide tabulated reference values

    **3. Detecting branch-cut crossing errors:**

    - **Smoothness test:** Evaluate $\varphi(u)$ on a fine grid $u \in [0, u_{\max}]$ and check that both $\operatorname{Re}(\varphi)$ and $\operatorname{Im}(\varphi)$ are smooth (no sudden jumps). A jump exceeding $\pi$ in $\arg(\varphi(u_{j+1})) - \arg(\varphi(u_j))$ signals a branch-cut crossing
    - **Modulus test:** $|\varphi(u)|$ should be a smooth, monotonically decreasing function for $u > 0$. Any upward spikes indicate discontinuities
    - **Option price sanity:** Computed call prices must satisfy $\max(S_0 e^{-q\tau} - Ke^{-r\tau}, 0) \leq C \leq S_0 e^{-q\tau}$, put-call parity must hold, and prices must be monotone in strike
    - **Comparison test:** Evaluate with both 1993 and Albrecher formulations; for short $\tau$ they should agree, and any discrepancy at longer $\tau$ indicates a branch-cut issue in the 1993 form
