# Hölder Continuity and Non-Differentiability

In **Brownian Motion Foundations** we saw that Brownian increments satisfy
$\mathbb{E}[(W_{t+h}-W_t)^2] = h$, so a typical increment has size $\sqrt{h}$ rather
than $h$. This $\sqrt{h}$ scaling is the fingerprint of an unusual regularity class:
the paths are continuous — in fact Hölder continuous of every order $\alpha < \tfrac{1}{2}$
— yet they are nowhere differentiable and have infinite total variation on every interval.

Understanding this dichotomy is essential before building stochastic calculus. Hölder
continuity explains *why* paths exist and are well-behaved enough to study. Nowhere
differentiability and infinite total variation explain *why* the Riemann–Stieltjes
integral $\int f(t)\,dW_t$ cannot be defined in the classical sense and why a new
calculus (Itô's calculus) is required.

---

## Hölder Continuity

### Definition

!!! definition "Hölder Continuity"
    A function $f:[0,T]\to\mathbb{R}$ is **Hölder continuous of order $\alpha \in (0,1]$**
    if there exists a finite constant $C > 0$ such that

    $$|f(t) - f(s)| \leq C\,|t - s|^\alpha \quad \text{for all } s, t \in [0,T].$$

    The largest such $\alpha$ is called the **Hölder exponent** of $f$.

**Examples:**

- $f(t) = t^{1/2}$ is Hölder-$\tfrac{1}{2}$ but not Hölder-$\alpha$ for any $\alpha > \tfrac{1}{2}$.
- Every $C^1$ function is Hölder-$1$ (Lipschitz).
- The Cantor function is Hölder-$(\log 2/\log 3)$ but nowhere differentiable.

Hölder continuity with $\alpha > 0$ implies uniform continuity, but for $\alpha < 1$ it
allows the function to oscillate in ways that preclude differentiability.

### Kolmogorov's Continuity Criterion

The tool used to establish path regularity for stochastic processes is the following
general theorem.

!!! theorem "Kolmogorov's Continuity Criterion"
    Let $\{X_t\}_{t \in [0,T]}$ be a stochastic process satisfying

    $$\mathbb{E}[|X_t - X_s|^p] \leq C\,|t-s|^{1+\beta}$$

    for some constants $p > 0$, $\beta > 0$, and $C < \infty$.
    Then $X$ has a **continuous modification** $\{\tilde{X}_t\}$ that is almost surely
    Hölder continuous of every order $\alpha < \beta/p$.

**Proof sketch.** One bounds the oscillation of $X$ over dyadic intervals and applies
the Borel–Cantelli lemma to show that the modulus of continuity decays at the required
rate. The details use the Markov inequality and a chaining argument; see Karatzas &
Shreve (1991), Theorem 2.2.8 for the full proof. $\square$

### Brownian Motion is Hölder-$\alpha$ for Every $\alpha < \tfrac{1}{2}$

**Theorem** (Hölder Regularity of Brownian Motion)

Brownian motion $\{W_t\}_{t \in [0,T]}$ has a continuous modification that is almost
surely Hölder continuous of order $\alpha$ for every $\alpha < \tfrac{1}{2}$.

**Proof.**

Since $W_t - W_s \sim \mathcal{N}(0, t-s)$, the $p$-th moment of a Gaussian increment is:

$$\mathbb{E}[|W_t - W_s|^p] = \mathbb{E}[|Z|^p]\,|t-s|^{p/2}, \quad Z \sim \mathcal{N}(0,1).$$

For the $p$-th absolute moment of a standard normal, $\mathbb{E}[|Z|^p] = \frac{2^{p/2}\,\Gamma((p+1)/2)}{\sqrt{\pi}} < \infty$, so set $C_p = \mathbb{E}[|Z|^p]$:

$$\mathbb{E}[|W_t - W_s|^p] = C_p\,|t-s|^{p/2}.$$

We want to apply Kolmogorov's criterion with exponent $1+\beta$. Matching:

$$p/2 = 1 + \beta \implies \beta = p/2 - 1.$$

For $\beta > 0$ we need $p > 2$. With $p > 2$, the criterion gives Hölder continuity of
every order $\alpha < \beta/p = (p/2 - 1)/p = \tfrac{1}{2} - \tfrac{1}{p}$.

Taking $p \to \infty$, the Hölder exponent approaches $\tfrac{1}{2}$ from below. Since
this works for every $p > 2$, the paths are almost surely Hölder-$\alpha$ for every
$\alpha < \tfrac{1}{2}$. $\square$

!!! note "The Bound $\alpha < \tfrac{1}{2}$ is Sharp"
    Brownian motion is *not* Hölder-$\tfrac{1}{2}$ globally. A more delicate argument
    (law of the iterated logarithm) shows that near any fixed time $t$:

    $$\limsup_{h\to 0}\,\frac{|W_{t+h}-W_t|}{\sqrt{2h\log\log(1/h)}} = 1 \quad \text{a.s.}$$

    The $\sqrt{h\log\log(1/h)}$ factor grows slightly faster than $\sqrt{h}$, confirming
    that $\alpha = \tfrac{1}{2}$ is not attained.

---

## Nowhere Differentiability

### Statement

!!! theorem "Brownian Motion is Nowhere Differentiable"
    Almost surely, the function $t \mapsto W_t(\omega)$ is differentiable at no point
    $t \in [0, \infty)$.

This is a striking contrast with the Hölder continuity result: the paths are continuous
everywhere but differentiable nowhere — much like the Weierstrass function, but arising
naturally from probabilistic axioms.

### Proof

We give a clean argument using the quadratic variation.

**Suppose** for contradiction that $W_t(\omega)$ is differentiable at some $t_0$, with
derivative $W'_{t_0} = L(\omega)$. Then for any $\varepsilon > 0$ there exists $\delta > 0$ such that

$$|W_{t_0+h} - W_{t_0}| \leq (|L| + \varepsilon)|h| \quad \text{for all } |h| < \delta.$$

Fix a partition $\Pi_n$ of a small interval $[t_0, t_0+\eta]$ with $\eta < \delta$ and mesh $\|\Pi_n\| \to 0$. Then

$$\sum_i (W_{t_{i+1}} - W_{t_i})^2 \leq \max_i |W_{t_{i+1}} - W_{t_i}| \cdot \sum_i |W_{t_{i+1}} - W_{t_i}|.$$

The first factor is bounded by $(|L|+\varepsilon)\|\Pi_n\| \to 0$. The second factor is the
total variation of $W$ over $[t_0, t_0+\eta]$, which is finite (since the increments are
bounded by $(|L|+\varepsilon)\eta$). Therefore the left side converges to 0.

But by the quadratic variation theorem (Section: Quadratic Variation of Brownian Motion), for any interval $[t_0, t_0+\eta]$:

$$\sum_i (W_{t_{i+1}}-W_{t_i})^2 \xrightarrow{L^2} \eta > 0.$$

$L^2$ convergence implies convergence along a subsequence of partitions for a.e. $\omega$, so for a.e. $\omega$ there exists a subsequence along which $\sum_i (W_{t_{i+1}} - W_{t_i})^2(\omega) \to \eta > 0$ — contradicting the deterministic bound above which forces the same sum to $0$ for any $\omega$ where $W$ is differentiable at $t_0$.

This contradiction shows that $W_t$ cannot be differentiable at $t_0$. Since $t_0$ was
arbitrary and the exceptional null set can be chosen uniformly over all rational $t_0$
(using a countable union argument), the paths are almost surely differentiable nowhere. $\square$

### Heuristic Explanation

The $\sqrt{\Delta t}$ scaling of increments is the immediate intuition:

$$\frac{W_{t+h} - W_t}{h} \approx \frac{\sqrt{h}}{h} = \frac{1}{\sqrt{h}} \to \infty \quad \text{as } h \to 0.$$

The difference quotient diverges in magnitude (though not in a fixed direction, since
increments are symmetric about zero). This is why no limit exists.

```mermaid
flowchart LR
    A["Increment: W_{t+h} - W_t ~ N(0,h)"] --> B["Size ≈ sqrt(h)"]
    B --> C["Difference quotient ≈ 1/sqrt(h)"]
    C --> D["→ ∞ as h → 0"]
    D --> E["No derivative exists"]
```

---

## Infinite Total Variation

### Definition and Smooth Comparison

!!! definition "Total Variation"
    The **total variation** of $f:[0,T]\to\mathbb{R}$ along a partition
    $\Pi = \{0 = t_0 < t_1 < \cdots < t_n = T\}$ is

    $$V_1(f,\Pi) = \sum_{i=0}^{n-1}|f(t_{i+1})-f(t_i)|.$$

    The **total variation** of $f$ on $[0,T]$ is $V_1(f) = \sup_\Pi V_1(f,\Pi)$.

For a $C^1$ function, $V_1(f) = \int_0^T |f'(t)|\,dt < \infty$.

**Why finite total variation matters.** The Riemann–Stieltjes integral $\int_0^T g(t)\,df(t)$
is well-defined for continuous $g$ whenever $f$ has finite total variation (the Jordan
decomposition applies). Classical integration theory relies entirely on this fact.

### Brownian Motion Has Infinite Total Variation

!!! theorem "Infinite Total Variation"
    Almost surely, the total variation of $W$ on $[0,T]$ is infinite:

    $$V_1(W) = \sup_\Pi \sum_{i}|W_{t_{i+1}} - W_{t_i}| = +\infty \quad \text{a.s.}$$

**Proof.**

For any partition $\Pi$ of $[0,T]$, bound each squared increment by the maximum:

$$\sum_i (\Delta W_i)^2
= \sum_i |\Delta W_i| \cdot |\Delta W_i|
\leq \left(\max_i |\Delta W_i|\right) \cdot \sum_i |\Delta W_i|
= \left(\max_i |\Delta W_i|\right) \cdot V_1(W, \Pi).$$

Rearranging:

$$V_1(W, \Pi) \geq \frac{\sum_i (\Delta W_i)^2}{\max_i |\Delta W_i|}.$$

As $\|\Pi\| \to 0$: the numerator converges in $L^2$ to $T > 0$ (the quadratic variation
result), while the denominator converges to 0 in probability (since
$\max_i |\Delta W_i| \leq \|\Pi\|^{1/2-\varepsilon}$ eventually, by Hölder continuity).
Therefore $V_1(W, \Pi) \to \infty$ in probability, and hence almost surely along a
suitable subsequence. Since the total variation is a supremum over partitions, it
equals $+\infty$ a.s. $\square$

### Consequence for Integration Theory

The failure of finite total variation means:

$$\int_0^T f(t)\,dW_t \text{ cannot be defined as a Riemann–Stieltjes integral.}$$

Specifically: the Riemann–Stieltjes construction requires approximating
$\sum_i f(t_i^*)(W_{t_{i+1}} - W_{t_i})$, and the limit fails to exist for general
adapted integrands $f$ because the accumulated oscillations of $W$ are too large.

This motivates the construction of the **Itô integral**, which handles this by working
in $L^2$ and exploiting the martingale structure of Brownian motion rather than
pathwise control. The key idea is that the *variance* of increments sums to $T$ even
though the total variation is infinite.

---

## Summary Table

| Property | Smooth $C^1$ function | Brownian motion |
|---|---|---|
| Continuity | ✓ | ✓ (a.s.) |
| Hölder-1 (Lipschitz) | ✓ | ✗ (a.s.) |
| Hölder-$\alpha$, all $\alpha < \tfrac{1}{2}$ | ✓ (trivially, since Hölder-1) | ✓ (a.s., best possible) |
| Differentiability | ✓ | ✗ (nowhere, a.s.) |
| Finite total variation | ✓ | ✗ (a.s.) |
| Quadratic variation | $0$ | $T$ (finite, nonzero) |

The last row is the decisive one for stochastic calculus: Brownian motion has *finite,
nonzero* quadratic variation, whereas smooth functions have zero quadratic variation.
This is why $dW_t^2 = dt$ survives in Itô's formula while $(dt)^2 = 0$.

---

## Python: Observing Path Roughness

The following simulation illustrates the Hölder regularity and infinite total variation
by computing the $p$-th variation $\sum_i |\Delta W_i|^p$ for several values of $p$.

For a Hölder-$\alpha$ function and a uniform partition with $n$ steps:

- $p > 1/\alpha$: $p$-variation $\to \infty$ as $n \to \infty$
- $p < 1/\alpha$: $p$-variation $\to 0$
- $p = 1/\alpha$: $p$-variation converges to a finite limit

For Brownian motion ($\alpha \approx 1/2$), the critical $p$ is $1/\alpha = 2$, so
total variation ($p=1$) diverges and quadratic variation ($p=2$) converges to $T$.

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

T = 1.0
p_values = [1.0, 1.5, 2.0, 2.5, 3.0]   # p = 1 is total variation, p = 2 is quadratic
n_values = [10, 50, 100, 500, 1000, 5000]
n_paths = 200

results = {p: [] for p in p_values}

for n in n_values:
    dt = T / n
    dW = np.random.normal(0, np.sqrt(dt), size=(n_paths, n))
    for p in p_values:
        pvar = np.mean(np.sum(np.abs(dW)**p, axis=1))
        results[p].append(pvar)

fig, ax = plt.subplots(figsize=(10, 5))
for p in p_values:
    label = f'$p = {p}$' + (' (total var)' if p == 1.0 else ' (quad var)' if p == 2.0 else '')
    ax.semilogx(n_values, results[p], 'o-', label=label)

ax.axhline(T, color='black', linestyle='--', linewidth=1.5, label=f'$T = {T}$ (quad var limit)')
ax.set_xlabel('Number of partition steps $n$', fontsize=12)
ax.set_ylabel('$p$-variation', fontsize=12)
ax.set_title('$p$-Variation of Brownian Motion vs. Partition Size', fontsize=13)
ax.legend(fontsize=10)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('figures/fig_holder_pvar.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Interpretation:**

- $p = 1$ (total variation): grows without bound as $n \to \infty$ — confirming infinite total variation.
- $p = 2$ (quadratic variation): converges to $T = 1$ — the quadratic variation theorem.
- $p < 2$: diverges; $p > 2$: converges to 0. The critical exponent is exactly $p = 2$.

---

## Summary

!!! abstract "Key Results"
    1. **Hölder regularity**: Brownian motion is almost surely Hölder-$\alpha$ for
       every $\alpha < \tfrac{1}{2}$, established via Kolmogorov's criterion with
       $\mathbb{E}[|W_t - W_s|^p] = C_p\,|t-s|^{p/2}$.
    2. **Nowhere differentiable**: Difference quotients diverge a.s. at every point,
       because increments scale as $\sqrt{h}$ while the denominator is $h$.
    3. **Infinite total variation**: $V_1(W) = +\infty$ a.s. on every interval, which
       rules out Riemann–Stieltjes integration for adapted integrands.
    4. **Finite quadratic variation**: $[W]_T = T$ — the *only* variation that remains
       finite and nonzero, and the foundation for Itô calculus.

**Looking ahead:**

- **Quadratic Variation** (next section): Proves $[W]_T = T$ rigorously in $L^2$.
- **Itô's Formula** (Chapter 3): The correction term $\tfrac{1}{2}f''(W_t)\,dt$ is a
  direct consequence of the nowhere differentiability forcing $dW_t^2 = dt$.

---

## Exercises

1. Show that if $f:[0,T]\to\mathbb{R}$ is Hölder-$\alpha$ with $\alpha > 1$, then $f$ must be constant. (Hint: For any $t, s$, write $|f(t)-f(s)| \leq C|t-s|^\alpha$ and let $s \to t$.)

2. Let $W_t$ be Brownian motion. Use Kolmogorov's criterion with $p = 4$ to show that
   $W$ is almost surely Hölder-$\alpha$ for $\alpha < 1/4$. (This is a weaker bound;
   the optimal $1/2$ requires $p \to \infty$.)

3. Show that the process $X_t = t$ has zero quadratic variation on $[0,T]$ but finite
   (in fact linear) total variation. Contrast with Brownian motion.

4. Let $f$ be Hölder-$\alpha$ with $\alpha > 1/2$. Show that $\sum_i (f(t_{i+1}) - f(t_i))^2 \to 0$ as the mesh $\|\Pi\| \to 0$, confirming zero quadratic variation for regular functions.

5. Verify the infinite total variation of Brownian motion numerically: for $T = 1$
   and increasing $n$, plot $\sum_{i=0}^{n-1}|W_{(i+1)/n} - W_{i/n}|$ as a function
   of $n$ and confirm divergence.

6. Suppose $f:[0,T]\to\mathbb{R}$ is differentiable at $t_0$ with $f'(t_0) = L$.
   Show directly that for any partition $\Pi$ of $[t_0, t_0+\eta]$ with small $\eta$,
   $\sum_i (f(t_{i+1}) - f(t_i))^2 \to 0$ as $\|\Pi\| \to 0$.

---

## Solutions

??? success "Solution to Exercise 1"
    Suppose $f:[0,T]\to\mathbb{R}$ is Hölder-$\alpha$ with $\alpha > 1$. Then there exists $C > 0$ such that for all $s, t \in [0,T]$:

    $$
    |f(t) - f(s)| \leq C\,|t - s|^\alpha
    $$

    For any fixed $s$ and $t$, divide the interval $[s, t]$ into $n$ equal parts with mesh $h = (t-s)/n$. By the triangle inequality and then the Hölder condition:

    $$
    |f(t) - f(s)| \leq \sum_{k=0}^{n-1}|f(s + (k+1)h) - f(s + kh)| \leq n \cdot C \cdot h^\alpha = C \cdot n \cdot \left(\frac{t-s}{n}\right)^\alpha = C(t-s)^\alpha \cdot n^{1-\alpha}
    $$

    Since $\alpha > 1$, we have $1 - \alpha < 0$, so $n^{1-\alpha} \to 0$ as $n \to \infty$. Therefore $|f(t) - f(s)| = 0$ for all $s, t$, which means $f$ is constant.

??? success "Solution to Exercise 2"
    We apply Kolmogorov's criterion with $p = 4$. For Brownian motion:

    $$
    \mathbb{E}[|W_t - W_s|^4] = 3(t-s)^2 = 3\,|t-s|^{1+1}
    $$

    This is of the form $\mathbb{E}[|X_t - X_s|^p] \leq C|t-s|^{1+\beta}$ with $p = 4$, $\beta = 1$, and $C = 3$.

    By Kolmogorov's criterion, $W$ has a modification that is Hölder-$\alpha$ for every:

    $$
    \alpha < \frac{\beta}{p} = \frac{1}{4}
    $$

    This gives the weaker bound $\alpha < 1/4$. To recover the optimal bound $\alpha < 1/2$, one uses arbitrarily large $p$: with $p > 2$, $\mathbb{E}[|W_t - W_s|^p] = C_p |t-s|^{p/2}$, giving $\beta = p/2 - 1$ and $\alpha < (p/2-1)/p = 1/2 - 1/p$. Letting $p \to \infty$ yields $\alpha < 1/2$.

??? success "Solution to Exercise 3"
    For $X_t = t$, the quadratic variation along a uniform partition $\Pi_n = \{0 = t_0 < t_1 < \cdots < t_n = T\}$ with $\Delta t_i = T/n$ is:

    $$
    V_2(X, \Pi_n) = \sum_{i=0}^{n-1}(X_{t_{i+1}} - X_{t_i})^2 = \sum_{i=0}^{n-1}\left(\frac{T}{n}\right)^2 = n \cdot \frac{T^2}{n^2} = \frac{T^2}{n} \to 0
    $$

    The total variation is:

    $$
    V_1(X, \Pi_n) = \sum_{i=0}^{n-1}|X_{t_{i+1}} - X_{t_i}| = \sum_{i=0}^{n-1}\frac{T}{n} = T < \infty
    $$

    **Contrast with Brownian motion:** For $X_t = t$, the quadratic variation is zero and the total variation is $T$ (finite). For Brownian motion, the quadratic variation is $T$ (finite, nonzero) and the total variation is $+\infty$. Brownian paths oscillate so much that they accumulate infinite path length, yet the squared increments sum to a finite quantity.

??? success "Solution to Exercise 4"
    Let $f$ be Hölder-$\alpha$ with $\alpha > 1/2$. Then $|f(t_{i+1}) - f(t_i)| \leq C|t_{i+1} - t_i|^\alpha = C(\Delta t_i)^\alpha$ for some constant $C$. Therefore:

    $$
    \sum_i (f(t_{i+1}) - f(t_i))^2 \leq C^2 \sum_i (\Delta t_i)^{2\alpha}
    $$

    Since $2\alpha > 1$, each term satisfies $(\Delta t_i)^{2\alpha} \leq \|\Pi\|^{2\alpha - 1} \cdot \Delta t_i$:

    $$
    \sum_i (\Delta t_i)^{2\alpha} \leq \|\Pi\|^{2\alpha - 1} \sum_i \Delta t_i = T \cdot \|\Pi\|^{2\alpha - 1} \to 0
    $$

    as $\|\Pi\| \to 0$ (since $2\alpha - 1 > 0$). Therefore the quadratic variation of any Hölder-$\alpha$ function with $\alpha > 1/2$ is zero.

??? success "Solution to Exercise 5"
    For a single Brownian path on $[0, T]$ with uniform partition $t_i = iT/n$, the total variation is:

    $$
    V_1(W, \Pi_n) = \sum_{i=0}^{n-1} |W_{t_{i+1}} - W_{t_i}|
    $$

    Each $|W_{t_{i+1}} - W_{t_i}| = \sqrt{T/n}\,|Z_i|$ where $Z_i \sim \mathcal{N}(0,1)$ are independent. The expected total variation is:

    $$
    \mathbb{E}[V_1(W, \Pi_n)] = n \cdot \sqrt{\frac{T}{n}} \cdot \mathbb{E}[|Z|] = n \cdot \sqrt{\frac{T}{n}} \cdot \sqrt{\frac{2}{\pi}} = \sqrt{\frac{2nT}{\pi}}
    $$

    This grows as $\sqrt{n} \to \infty$. To verify numerically, simulate a Brownian path for increasing $n$ and plot $V_1(W, \Pi_n)$ vs $n$. The plot should show a curve growing like $\sqrt{n}$, confirming that the total variation diverges.

??? success "Solution to Exercise 6"
    Suppose $f$ is differentiable at $t_0$ with $f'(t_0) = L$. Then for any $\varepsilon > 0$, there exists $\delta > 0$ such that for all $|h| < \delta$:

    $$
    |f(t_0 + h) - f(t_0) - Lh| \leq \varepsilon |h|
    $$

    In particular, $|f(t_0 + h) - f(t_0)| \leq (|L| + \varepsilon)|h|$.

    For any partition $\Pi$ of $[t_0, t_0 + \eta]$ with $\eta < \delta$ and mesh $\|\Pi\| < \delta$:

    $$
    \sum_i (f(t_{i+1}) - f(t_i))^2 \leq (|L| + \varepsilon)^2 \sum_i (\Delta t_i)^2 \leq (|L| + \varepsilon)^2 \|\Pi\| \sum_i \Delta t_i = (|L| + \varepsilon)^2 \|\Pi\| \cdot \eta
    $$

    As $\|\Pi\| \to 0$, the right side tends to 0. Therefore $\sum_i (f(t_{i+1}) - f(t_i))^2 \to 0$, confirming zero quadratic variation at a point of differentiability.

---

## References

- Karatzas, I., & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer. (Theorem 2.2.8 for Kolmogorov criterion; Chapter 1 for path properties)
- Mörters, P., & Peres, Y. (2010). *Brownian Motion*. Cambridge University Press. (Chapter 1 for Hölder regularity and non-differentiability)
- Revuz, D., & Yor, M. (1999). *Continuous Martingales and Brownian Motion*, 3rd ed. Springer. (Chapter I for Kolmogorov criterion)
- Billingsley, P. (1995). *Probability and Measure*, 3rd ed. Wiley. (Weak convergence and tightness)
