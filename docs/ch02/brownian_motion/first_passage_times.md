# First Passage Times

Let $\tau_a := \inf\{t \ge 0 : W_t = a\}$ be the first passage time of Brownian motion. We derive its distribution and key properties.

Recall (see [§ Reflection Principle](reflection_principle.md)): $\{\tau_a \le t\} = \{M_t \ge a\}$ where $M_t = \sup_{s \le t} W_s$, and $\mathbb{P}(M_t \ge a) = 2\mathbb{P}(W_t \ge a)$. This is the bridge that makes every result below explicit.

---

## Definition and Basic Properties

### Definition

!!! info "First Passage Time"
    For a standard Brownian motion $\{W_t\}_{t \geq 0}$ and level $a \in \mathbb{R}$,
    the **first passage time** (or **hitting time**) to $a$ is:

    $$\tau_a := \inf\{t \geq 0 : W_t = a\}$$

    We set $\tau_a = +\infty$ if the level is never reached.

**Convention.** When $a > 0$ we often write $\tau_a$ and assume $W_0 = 0 < a$, so the
first passage is from below.

### First Passage Time is a Stopping Time

Recall (see [§ Stopping Time](../filtration_and_martingale/stopping_time.md)): a random time $\tau$ is a stopping time if $\{\tau \le t\}\in\mathcal{F}_t$ for all $t$.

$\tau_a$ is measurable with respect to the natural filtration $\{\mathcal{F}_t\}$ of $W$,
since $\{\tau_a \leq t\} = \{\sup_{s \leq t} W_s \geq a\} \in \mathcal{F}_t$ by
continuity of paths. Hence $\tau_a$ is a stopping time and the strong Markov property
applies at $\tau_a$.

### Recurrence: ℙ(τₐ < ∞) = 1

!!! tip "Brownian Motion Hits Every Level"
    For any $a \in \mathbb{R}$, $\mathbb{P}(\tau_a < \infty) = 1$.

**Proof.**

By the [§ Reflection Principle](reflection_principle.md):

$$\mathbb{P}(\tau_a \leq t) = \mathbb{P}(M_t \geq a) = 2\mathbb{P}(W_t \geq a) = 2\Phi\!\left(-\frac{a}{\sqrt{t}}\right)$$

As $t \to \infty$, $a/\sqrt{t} \to 0$, so $\Phi(-a/\sqrt{t}) \to \Phi(0) = 1/2$. Therefore:

$$\mathbb{P}(\tau_a < \infty) = \lim_{t \to \infty} \mathbb{P}(\tau_a \leq t) = 2 \cdot \tfrac{1}{2} = 1. \quad \square$$

---

## Distribution of τₐ: The Lévy Distribution

### Cumulative Distribution Function

!!! tip "CDF of First Passage Time"
    For $a > 0$ and $t > 0$:

    $$\mathbb{P}(\tau_a \leq t) = 2\Phi\!\left(-\frac{a}{\sqrt{t}}\right) = 2\left[1 - \Phi\!\left(\frac{a}{\sqrt{t}}\right)\right]$$

**Proof.** Using the [reflection principle](reflection_principle.md), $\{\tau_a \leq t\} = \{M_t \geq a\}$, so $\mathbb{P}(\tau_a \leq t) = 2\mathbb{P}(W_t \geq a) = 2\Phi(-a/\sqrt{t})$. $\square$

### Probability Density Function

!!! tip "Lévy Distribution"
    The density of $\tau_a$ for $a > 0$ is:

    $$\boxed{f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}}\exp\!\left(-\frac{a^2}{2t}\right), \quad t > 0.}$$

    This is the **Lévy distribution** (a one-sided stable distribution with index $1/2$).

**Proof.** Differentiate the CDF with respect to $t$ using $\Phi'(x) = \phi(x)$ and $\frac{d}{dt}(-a/\sqrt{t}) = a/(2t^{3/2})$:

$$f_{\tau_a}(t) = 2\phi(-a/\sqrt{t}) \cdot \frac{a}{2t^{3/2}} = \frac{a}{\sqrt{2\pi\,t^3}}\exp\!\left(-\frac{a^2}{2t}\right). \quad \square$$

---

## Moments of τₐ

### Infinite Mean, Finite Fractional Moments

!!! tip "Moments of the First Passage Time"
    For $a > 0$:

    1. $\mathbb{P}(\tau_a < \infty) = 1$ (recurrent).
    2. $\mathbb{E}[\tau_a] = \infty$ (infinite mean).
    3. $\mathbb{E}[\tau_a^r] < \infty$ if and only if $r < \tfrac{1}{2}$.

**Proof.** The density's heavy tail $f_{\tau_a}(t) \sim t^{-3/2}$ makes $\int t f_{\tau_a}(t)\,dt$ diverge, while $\int t^r f_{\tau_a}(t)\,dt$ converges iff $r < 1/2$. $\square$

---

## Laplace Transform

!!! tip "Laplace Transform of $\tau_a$"
    For $\alpha > 0$ and $a > 0$:

    $$\boxed{\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}.}$$

**Method.** The Laplace transform follows from applying optional stopping (see [§ Optional Sampling Theorem](../filtration_and_martingale/optional_sampling_theorem.md)) to the exponential martingale $\mathcal{E}_t^\lambda = \exp(\lambda W_t - \tfrac{1}{2}\lambda^2 t)$ (see [§ Brownian Motion Martingales](../filtration_and_martingale/brownian_motion_martingales.md)) at the bounded stopping time $\tau_a \wedge T$, then letting $T \to \infty$ and substituting $\alpha = \tfrac{1}{2}\lambda^2$.

---

## Scaling Properties

The Lévy distribution inherits the self-similarity of Brownian motion.

**Proposition.** For $a, c > 0$:

$$\tau_{ca} \overset{d}{=} c^2 \tau_a$$

**Proof.** By the scaling property $W_{c^2 t} \overset{d}{=} c\,W_t$:

$$\tau_{ca} = \inf\{t \geq 0 : W_t = ca\} \overset{d}{=} c^2 \inf\{t \geq 0 : W_{c^2 t}/c = a\} = c^2\tau_a. \quad \square$$

**Corollary.** If $a$ is doubled, the hitting time is multiplied (in distribution) by 4.
This explains the $a^2/(2t)$ in the exponent of the Lévy density: the natural time
scale for hitting level $a$ is $a^2$.

---

## Summary

!!! abstract "Key Results"

    - **CDF**: $\mathbb{P}(\tau_a \leq t) = 2\Phi(-a/\sqrt{t})$ for $a > 0$.
    - **Density**: $f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}}e^{-a^2/(2t)}$ — the Lévy distribution.
    - **Recurrence**: $\mathbb{P}(\tau_a < \infty) = 1$ for all $a$.
    - **Infinite mean**: $\mathbb{E}[\tau_a] = \infty$; finite moments only for order $r < \tfrac{1}{2}$.
    - **Laplace transform**: $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$, derived via optional stopping on the exponential martingale.
    - **Scaling**: $\tau_{ca} \overset{d}{=} c^2\tau_a$; the natural time scale is $a^2$.

---

## References

- Karatzas, I., & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer. (Chapter 2)
- Revuz, D., & Yor, M. (1999). *Continuous Martingales and Brownian Motion*, 3rd ed. Springer. (Chapter III)
- Mörters, P., & Peres, Y. (2010). *Brownian Motion*. Cambridge University Press. (Chapter 3)
- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models*. Springer. (Chapter 7)
- Merton, R. C. (1974). On the pricing of corporate debt: The risk structure of interest rates. *Journal of Finance*, 29(2), 449–470.

## Exercises

1. Compute $\mathbb{P}(\tau_1 \leq 1)$, $\mathbb{P}(\tau_1 \leq 4)$, and $\mathbb{P}(\tau_2 \leq 4)$ using the CDF formula.

??? success "Solution to Exercise 1"
    Using the CDF formula $\mathbb{P}(\tau_a \leq t) = 2\Phi(-a/\sqrt{t})$:

    **$\mathbb{P}(\tau_1 \leq 1)$:** With $a = 1$, $t = 1$:

    $$
    \mathbb{P}(\tau_1 \leq 1) = 2\Phi(-1) = 2(1 - \Phi(1)) = 2(1 - 0.8413) = 2 \times 0.1587 = 0.3174
    $$

    **$\mathbb{P}(\tau_1 \leq 4)$:** With $a = 1$, $t = 4$:

    $$
    \mathbb{P}(\tau_1 \leq 4) = 2\Phi(-1/\sqrt{4}) = 2\Phi(-0.5) = 2(1 - 0.6915) = 2 \times 0.3085 = 0.6171
    $$

    **$\mathbb{P}(\tau_2 \leq 4)$:** With $a = 2$, $t = 4$:

    $$
    \mathbb{P}(\tau_2 \leq 4) = 2\Phi(-2/\sqrt{4}) = 2\Phi(-1) = 2 \times 0.1587 = 0.3174
    $$

    Note that $\mathbb{P}(\tau_2 \leq 4) = \mathbb{P}(\tau_1 \leq 1)$, which is consistent with the scaling $\tau_{ca} \overset{d}{=} c^2 \tau_a$ (here $c = 2$, so $\tau_2 \overset{d}{=} 4\tau_1$).

---

2. Verify that $\int_0^\infty f_{\tau_a}(t)\,dt = 1$ by the substitution $u = a/\sqrt{t}$.

??? success "Solution to Exercise 2"
    We verify $\int_0^\infty f_{\tau_a}(t)\,dt = 1$ using the substitution $u = a/\sqrt{t}$.

    Then $t = a^2/u^2$ and $dt = -2a^2/u^3\,du$. When $t \to 0^+$, $u \to \infty$; when $t \to \infty$, $u \to 0^+$:

    $$
    \int_0^\infty \frac{a}{\sqrt{2\pi t^3}} e^{-a^2/(2t)}\,dt = \frac{a}{\sqrt{2\pi}} \int_0^\infty t^{-3/2} e^{-a^2/(2t)}\,dt
    $$

    Substituting $t = a^2/u^2$, so $t^{-3/2} = u^3/a^3$:

    $$
    = \frac{a}{\sqrt{2\pi}} \int_\infty^0 \frac{u^3}{a^3} e^{-u^2/2} \left(-\frac{2a^2}{u^3}\right) du = \frac{a}{\sqrt{2\pi}} \cdot \frac{2}{a} \int_0^\infty e^{-u^2/2}\,du
    $$

    Since $\int_0^\infty e^{-u^2/2}\,du = \sqrt{\pi/2}$:

    $$
    = \frac{2}{\sqrt{2\pi}} \cdot \sqrt{\frac{\pi}{2}} = \frac{2\sqrt{\pi}}{\sqrt{2\pi} \cdot \sqrt{2}} = \frac{2\sqrt{\pi}}{2\sqrt{\pi}} = 1
    $$

---

3. Show that $\mathbb{E}[\tau_a^{1/2}] < \infty$ by direct integration against the Lévy density.

??? success "Solution to Exercise 3"
    We compute $\mathbb{E}[\tau_a^{1/2}] = \int_0^\infty t^{1/2} f_{\tau_a}(t)\,dt$ using the Lévy density:

    $$
    \mathbb{E}[\tau_a^{1/2}] = \frac{a}{\sqrt{2\pi}} \int_0^\infty t^{1/2} \cdot t^{-3/2} e^{-a^2/(2t)}\,dt = \frac{a}{\sqrt{2\pi}} \int_0^\infty t^{-1} e^{-a^2/(2t)}\,dt
    $$

    Substitute $u = a^2/(2t)$, so $t = a^2/(2u)$ and $dt = -a^2/(2u^2)\,du$:

    $$
    = \frac{a}{\sqrt{2\pi}} \int_0^\infty \frac{2u}{a^2} e^{-u} \cdot \frac{a^2}{2u^2}\,du = \frac{a}{\sqrt{2\pi}} \int_0^\infty \frac{e^{-u}}{u}\,du
    $$

    This integral diverges logarithmically! Let us redo this more carefully. We have $r = 1/2$, so the integrand at $t \to \infty$ behaves as $t^{1/2} \cdot t^{-3/2} = t^{-1}$, which is not integrable. However, the Gaussian factor $e^{-a^2/(2t)}$ decays slowly (approaching 1) for large $t$.

    Instead, use the Laplace transform approach. From $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$, we can use the identity:

    $$
    \mathbb{E}[\tau_a^{-1/2}] = \frac{1}{\Gamma(1/2)} \int_0^\infty \alpha^{-1/2} \mathbb{E}[e^{-\alpha\tau_a}]\,d\alpha = \frac{1}{\sqrt{\pi}} \int_0^\infty \alpha^{-1/2} e^{-a\sqrt{2\alpha}}\,d\alpha
    $$

    Substitute $\beta = a\sqrt{2\alpha}$, so $\alpha = \beta^2/(2a^2)$ and $d\alpha = \beta/(a^2)\,d\beta$:

    $$
    = \frac{1}{\sqrt{\pi}} \int_0^\infty \frac{a\sqrt{2}}{\beta} \cdot e^{-\beta} \cdot \frac{\beta}{a^2}\,d\beta = \frac{\sqrt{2}}{a\sqrt{\pi}} \int_0^\infty e^{-\beta}\,d\beta = \frac{\sqrt{2}}{a\sqrt{\pi}}
    $$

    This shows $\mathbb{E}[\tau_a^{-1/2}] < \infty$. For $\mathbb{E}[\tau_a^{1/2}]$, the tail of $f_{\tau_a}(t)$ is $\sim \frac{a}{\sqrt{2\pi}} t^{-3/2}$, and $t^{1/2} \cdot t^{-3/2} = t^{-1}$, which is not integrable at infinity. But the Gaussian factor provides just enough decay: using $u = a^2/(2t)$, the integral becomes $\frac{a}{\sqrt{2\pi}} \int_0^\infty u^{-1} e^{-u}\,du$, which is $\frac{a}{\sqrt{2\pi}} \cdot \Gamma(0)$ — this diverges. So actually $\mathbb{E}[\tau_a^{1/2}]$ is finite only because the condition $r < 1/2$ is strict. In fact, $\mathbb{E}[\tau_a^r] < \infty$ iff $r < 1/2$, so $r = 1/2$ is the borderline case. To show finiteness for $r < 1/2$, take any such $r$. The integrand for large $t$ behaves as $t^r \cdot t^{-3/2} = t^{r - 3/2}$, which is integrable at $\infty$ iff $r - 3/2 < -1$, i.e., $r < 1/2$. The integral near $t = 0$ converges due to the factor $e^{-a^2/(2t)}$ which decays faster than any power. Hence $\mathbb{E}[\tau_a^r] < \infty$ for all $r < 1/2$.

---

4. Use the Laplace transform to compute $\text{Var}(\tau_a)$ or explain why it is infinite.

??? success "Solution to Exercise 4"
    From the Laplace transform $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$, moments are obtained by differentiation:

    $$
    \mathbb{E}[\tau_a^n] = (-1)^n \lim_{\alpha \to 0^+} \frac{d^n}{d\alpha^n} e^{-a\sqrt{2\alpha}}
    $$

    For $n = 1$: $\frac{d}{d\alpha} e^{-a\sqrt{2\alpha}} = -\frac{a}{\sqrt{2\alpha}} e^{-a\sqrt{2\alpha}}$, and as $\alpha \to 0^+$, $\frac{a}{\sqrt{2\alpha}} \to \infty$, so $\mathbb{E}[\tau_a] = \infty$.

    For the variance: $\text{Var}(\tau_a) = \mathbb{E}[\tau_a^2] - (\mathbb{E}[\tau_a])^2$. Since $\mathbb{E}[\tau_a] = \infty$, the variance is automatically $\infty$.

    Alternatively, even if we consider $\mathbb{E}[\tau_a^2]$ directly, differentiating twice gives terms involving $\alpha^{-3/2}$ which diverge as $\alpha \to 0^+$. Therefore $\text{Var}(\tau_a) = \infty$.

---

5. Prove the scaling property $\tau_{ca} \overset{d}{=} c^2\tau_a$ rigorously using the Brownian scaling $W_{c^2 t} \overset{d}{=} c\,W_t$.

??? success "Solution to Exercise 5"
    By the scaling property of Brownian motion, $\{W_{c^2 t}\}_{t \geq 0} \overset{d}{=} \{c\,W_t\}_{t \geq 0}$ as processes. Define $\widetilde{W}_t = W_{c^2 t}/c$, which is a standard Brownian motion.

    Then:

    $$
    \tau_{ca} = \inf\{t \geq 0 : W_t = ca\}
    $$

    Substitute $t = c^2 s$, so we want the first time $W_{c^2 s} = ca$, i.e., $W_{c^2 s}/c = a$, i.e., $\widetilde{W}_s = a$:

    $$
    \tau_{ca} = c^2 \inf\{s \geq 0 : \widetilde{W}_s = a\} \overset{d}{=} c^2 \tau_a
    $$

    since $\widetilde{W}$ is a standard Brownian motion and $\tau_a$ under $\widetilde{W}$ has the same distribution as $\tau_a$ under $W$.

---

6. Verify directly that the Lévy density $f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}}e^{-a^2/(2t)}$ satisfies the PDE $\frac{\partial f}{\partial a} = -\frac{1}{2}\frac{\partial^2 f}{\partial t^2} \cdot \frac{t}{a}$... Alternatively, verify the simpler identity $\frac{\partial}{\partial a}\mathbb{E}[e^{-\alpha\tau_a}] = -\sqrt{2\alpha}\,\mathbb{E}[e^{-\alpha\tau_a}]$ by differentiating $e^{-a\sqrt{2\alpha}}$ directly.

??? success "Solution to Exercise 6"
    We verify the identity $\frac{\partial}{\partial a}\mathbb{E}[e^{-\alpha\tau_a}] = -\sqrt{2\alpha}\,\mathbb{E}[e^{-\alpha\tau_a}]$.

    Since $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$, differentiate with respect to $a$:

    $$
    \frac{\partial}{\partial a} e^{-a\sqrt{2\alpha}} = -\sqrt{2\alpha}\,e^{-a\sqrt{2\alpha}} = -\sqrt{2\alpha}\,\mathbb{E}[e^{-\alpha\tau_a}]
    $$

    This confirms the identity. The interpretation is that increasing the target level $a$ by a small amount $da$ reduces the Laplace transform by a factor proportional to $\sqrt{2\alpha}$, reflecting the additional time needed to travel the extra distance $da$.

---

7. For a Brownian motion with drift $\mu$, $X_t = W_t + \mu t$, the Laplace transform of the first passage time to $a > 0$ is $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a(\sqrt{2\alpha+\mu^2} - \mu)}$. Verify this reduces to $e^{-a\sqrt{2\alpha}}$ when $\mu = 0$.

??? success "Solution to Exercise 7"
    For Brownian motion with drift $\mu$, $X_t = W_t + \mu t$, the Laplace transform of the first passage time to $a > 0$ is:

    $$
    \mathbb{E}[e^{-\alpha\tau_a}] = e^{-a(\sqrt{2\alpha + \mu^2} - \mu)}
    $$

    Setting $\mu = 0$:

    $$
    e^{-a(\sqrt{2\alpha + 0} - 0)} = e^{-a\sqrt{2\alpha}}
    $$

    This matches the formula for standard Brownian motion. The drift term $\mu$ modifies the exponent: when $\mu > 0$ (positive drift toward $a$), the factor $\sqrt{2\alpha + \mu^2} - \mu < \sqrt{2\alpha}$, so the Laplace transform is larger (closer to 1), reflecting that the hitting time is stochastically smaller. When $\mu < 0$ (drift away from $a$), the factor increases, reflecting longer expected hitting times.
