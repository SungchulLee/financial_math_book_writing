# Integrability Conditions for Martingales

In the [unifying framework](unifying_principle.md) of this section, integrability conditions are the **concrete tests that determine whether a local martingale can be upgraded to a true martingale**. While the [Novikov and Kazamaki conditions](novikov_kazamaki_conditions.md) address the special case of stochastic exponentials, the criteria on this page apply to general local martingales.

A local martingale is a process that "looks like" a martingale when stopped at appropriate times, but may lose mass globally. The upgrade from local martingale to true martingale always comes down to a single question: is the family of random variables $\{M_\tau : \tau \text{ stopping time}\}$ sufficiently well-behaved? This page catalogs the standard conditions that answer this question and shows how they relate to one another.

!!! info "Prerequisites"
    This section assumes familiarity with:

    - [Local Martingales](local_martingale.md)
    - [Quadratic Variation](../../ch03/ito_integral/quadratic_variation.md)

---

## The Core Problem

Recall from the [local martingale](local_martingale.md) page that every martingale is a local martingale, but the converse fails. A non-negative local martingale $M_t$ is always a supermartingale (by Fatou's lemma), so

$$
\mathbb{E}[M_t] \leq \mathbb{E}[M_0]
$$

When strict inequality holds — when $\mathbb{E}[M_t] < \mathbb{E}[M_0]$ — probability mass has "leaked to infinity." The local martingale is then a **strict local martingale**, and it cannot serve as a Radon–Nikodym derivative for a valid measure change. The integrability conditions below are precisely the tools that rule out this mass leakage.

---

## Uniform Integrability

The most fundamental upgrade criterion is **uniform integrability** (UI). Uniform integrability of the family $\{M_\tau : \tau \leq T\}$ is the **necessary and sufficient condition** for upgrading a local martingale to a true martingale on $[0,T]$.

**Definition.** A family of random variables $\{X_\alpha\}_{\alpha \in A}$ is **uniformly integrable** if

$$
\lim_{c \to \infty} \sup_{\alpha \in A} \mathbb{E}\!\left[|X_\alpha|\,\mathbf{1}_{\{|X_\alpha| > c\}}\right] = 0
$$

Intuitively, no member of the family can carry significant mass in its tails — the tails are "uniformly thin."

**Upgrade Theorem.** Let $M$ be a continuous local martingale on $[0,T]$. If the family $\{M_\tau : \tau \text{ stopping time}, \tau \leq T\}$ is uniformly integrable, then $M$ is a **true martingale**:

$$
\boxed{
\text{Local martingale} + \text{UI of } \{M_\tau : \tau \leq T\} \;\Longrightarrow\; \text{True martingale}
}
$$

The converse also holds: $M$ is a UI martingale if and only if $\{M_\tau : \tau \leq T\}$ is UI. But the key message is the upgrade direction — UI is what lets you remove the localization.

**Proof sketch.** Let $\{\tau_n\}$ be a localizing sequence. Since $M$ is a local martingale, $\mathbb{E}[M_{t \wedge \tau_n} \mid \mathcal{F}_s] = M_{s \wedge \tau_n}$ for each $n$. As $n \to \infty$, $M_{t \wedge \tau_n} \to M_t$ a.s. Uniform integrability of $\{M_\tau\}$ allows passing the limit inside the conditional expectation (by the UI convergence theorem), yielding $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$. $\square$

!!! warning "UI of $\{M_\tau\}$ is stronger than UI of $\{M_t\}$"
    The family $\{M_\tau : \tau \leq T\}$ indexed over **all stopping times** is strictly larger than $\{M_t : t \leq T\}$ indexed over **fixed times** only. A local martingale can look well-behaved at deterministic times while hiding mass explosions at random stopping times. The upgrade theorem requires the stronger condition — controlling all stopped versions, not just the fixed-time snapshots. In practice this distinction rarely matters, because the sufficient criteria below automatically imply UI of the full family $\{M_\tau\}$.

!!! note "Connection to convergence"
    Uniform integrability is equivalent to $L^1$ convergence: a martingale $(M_t)_{t \geq 0}$ is UI if and only if $M_t \to M_\infty$ in $L^1$ (not just almost surely). See [Martingale Convergence](../../ch02/filtration_and_martingales/martingale_convergence.md).

---

## Practical Criteria

Verifying uniform integrability of $\{M_\tau : \tau \leq T\}$ directly from its definition — which involves a supremum over all stopping times — is almost never feasible. In practice, one establishes a stronger condition that automatically implies UI of the full family $\{M_\tau\}$. The following criteria cover most cases encountered in financial mathematics.

### Criterion 1: Boundedness

If $|M_t| \leq C$ almost surely for all $t \in [0,T]$ and some constant $C < \infty$, then $M$ is a uniformly integrable martingale on $[0,T]$.

This is the simplest criterion. Bounded random variables are automatically UI because the tails are empty.

### Criterion 2: Domination

If there exists an integrable random variable $Y$ with $\mathbb{E}[Y] < \infty$ such that $|M_t| \leq Y$ almost surely for all $t \in [0,T]$, then $M$ is a uniformly integrable martingale on $[0,T]$.

This generalizes boundedness: the bound need not be deterministic, but must itself be integrable.

### Criterion 3: Lp Boundedness (p > 1)

If $\sup_{t \in [0,T]} \mathbb{E}[|M_t|^p] < \infty$ for some $p > 1$, then $M$ is a uniformly integrable martingale on $[0,T]$.

The key point is that $p > 1$ is required — $p = 1$ (the definition of a martingale) is not sufficient for UI. The extra integrability provided by $p > 1$ prevents mass from concentrating in the tails. This follows from the de la Vallée-Poussin criterion.

### Criterion 4: Finite Quadratic Variation (BDG Inequality)

For a continuous local martingale $M$ with $M_0 = 0$, if

$$
\mathbb{E}\!\left[\langle M \rangle_T^{p/2}\right] < \infty
$$

for some $p \geq 1$, then $M$ is a true martingale on $[0,T]$. For $p > 1$, the **Burkholder–Davis–Gundy (BDG) inequality** gives the quantitative bound:

$$
c_p\,\mathbb{E}\!\left[\langle M \rangle_T^{p/2}\right] \leq \mathbb{E}\!\left[\sup_{t \leq T} |M_t|^p\right] \leq C_p\,\mathbb{E}\!\left[\langle M \rangle_T^{p/2}\right]
$$

where $c_p, C_p > 0$ are universal constants depending only on $p$.

The BDG inequality converts a question about the martingale itself (the left/right sides) into a question about its quadratic variation (the middle), which is often easier to compute.

**The most common special case** ($p = 2$): An Itô integral $M_t = \int_0^t \sigma_s\,dW_s$ is a true martingale on $[0,T]$ whenever

$$
\mathbb{E}\!\left[\int_0^T \sigma_s^2\,ds\right] < \infty
$$

This is the **Itô isometry condition** — it is by far the most frequently used upgrade criterion in practice.

---

## Conceptual Unification

The criteria above form a hierarchy of sufficient conditions, all implying uniform integrability:

$$
\boxed{
\text{Bounded} \;\Rightarrow\; \text{Dominated} \;\Rightarrow\; L^p \text{ bounded } (p > 1) \;\Rightarrow\; \text{UI} \;\Rightarrow\; \text{True martingale}
}
$$

The BDG criterion provides a parallel path through quadratic variation:

$$
\mathbb{E}[\langle M \rangle_T^{p/2}] < \infty \;\Rightarrow\; L^p \text{ bounded} \;\Rightarrow\; \text{UI} \;\Rightarrow\; \text{True martingale}
$$

Each condition is strictly stronger than the next — there exist true martingales that are UI but not $L^p$ bounded, and UI martingales that are not dominated. In practice, one uses the weakest criterion that applies to the problem at hand.

---

## Relation to Novikov and Kazamaki

The [Novikov and Kazamaki conditions](novikov_kazamaki_conditions.md) are integrability conditions specialized to **stochastic exponentials** $\mathcal{E}(M)_t = \exp(M_t - \frac{1}{2}\langle M \rangle_t)$:

| Condition | Applies to | Requires |
|-----------|-----------|----------|
| Boundedness / Domination / $L^p$ | Any local martingale | Bounds on $M_t$ itself |
| BDG / Itô isometry | Any local martingale | Bounds on $\langle M \rangle_t$ |
| **Novikov** | Stochastic exponential $\mathcal{E}(M)$ | $\mathbb{E}[\exp(\frac{1}{2}\langle M \rangle_T)] < \infty$ |
| **Kazamaki** | Stochastic exponential $\mathcal{E}(M)$ | $\sup_{t \leq T}\mathbb{E}[\exp(\frac{1}{2}M_t)] < \infty$ |

Novikov and Kazamaki are **not** special cases of the general criteria above — they exploit the specific exponential structure of $\mathcal{E}(M)$. In particular, Novikov's condition involves exponential moments of $\langle M \rangle$, which is much stronger than the polynomial moments required by BDG but is tailored to guarantee that the stochastic exponential (rather than $M$ itself) is a true martingale.

---

## Summary

$$
\boxed{
\text{Local martingale} + \text{Uniform integrability} = \text{True martingale}
}
$$

| Criterion | Condition | Strength |
|-----------|-----------|----------|
| Boundedness | $|M_t| \leq C$ a.s. | Strongest |
| Domination | $|M_t| \leq Y,\ \mathbb{E}[Y] < \infty$ | |
| $L^p$ bound ($p > 1$) | $\sup_t \mathbb{E}[|M_t|^p] < \infty$ | |
| BDG / Itô isometry | $\mathbb{E}[\langle M \rangle_T^{p/2}] < \infty$ | |
| Uniform integrability | Tails uniformly thin | Weakest sufficient |

!!! abstract "Key takeaway"
    Every sufficient condition for the true martingale property works by establishing uniform integrability, either directly or through moment bounds. In financial applications, the Itô isometry condition $\mathbb{E}[\int_0^T \sigma_s^2\,ds] < \infty$ and the Novikov condition $\mathbb{E}[\exp(\frac{1}{2}\int_0^T \theta_s^2\,ds)] < \infty$ are the two most commonly used tests.

---

## Exercises

**Exercise 1.**
Let $M_t = \int_0^t s\,dW_s$ for $t \in [0,T]$. Verify the Itô isometry condition and conclude that $M$ is a true martingale. Compute $\mathbb{E}[M_T^2]$.

??? success "Solution to Exercise 1"
    The integrand is $\sigma_s = s$, which is deterministic. The Itô isometry condition requires:

    $$
    \mathbb{E}\!\left[\int_0^T s^2\,ds\right] = \int_0^T s^2\,ds = \frac{T^3}{3} < \infty
    $$

    Since the integrand is deterministic, the expectation is just the integral itself. The condition holds for any finite $T$, so $M_t$ is a true martingale on $[0,T]$.

    By the Itô isometry:

    $$
    \mathbb{E}[M_T^2] = \mathbb{E}\!\left[\left(\int_0^T s\,dW_s\right)^2\right] = \int_0^T s^2\,ds = \frac{T^3}{3}
    $$

---

**Exercise 2.**
Show that a bounded local martingale is a true martingale. Specifically, if $M_t$ is a continuous local martingale with $|M_t| \leq C$ a.s. for all $t \in [0,T]$, prove that $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for all $0 \leq s \leq t \leq T$.

??? success "Solution to Exercise 2"
    Let $\{\tau_n\}$ be a localizing sequence for $M$. Since $M$ is a local martingale, the stopped process $M^{\tau_n}_t = M_{t \wedge \tau_n}$ is a martingale for each $n$:

    $$
    \mathbb{E}[M_{t \wedge \tau_n} \mid \mathcal{F}_s] = M_{s \wedge \tau_n}
    $$

    As $n \to \infty$, $\tau_n \to \infty$ a.s., so $M_{t \wedge \tau_n} \to M_t$ a.s. and $M_{s \wedge \tau_n} \to M_s$ a.s.

    Since $|M_{t \wedge \tau_n}| \leq C$ for all $n$, the bounded convergence theorem (or dominated convergence with the constant dominator $C$) allows passing the limit inside the conditional expectation:

    $$
    \mathbb{E}[M_t \mid \mathcal{F}_s] = \lim_{n \to \infty} \mathbb{E}[M_{t \wedge \tau_n} \mid \mathcal{F}_s] = \lim_{n \to \infty} M_{s \wedge \tau_n} = M_s
    $$

    Therefore $M$ is a true martingale. $\square$

---

**Exercise 3.**
Give an example showing that $L^1$ boundedness ($\sup_t \mathbb{E}[|M_t|] < \infty$) is **not** sufficient for uniform integrability. (Hint: consider a martingale that concentrates mass on increasingly rare but large events.)

??? success "Solution to Exercise 3"
    Consider the following discrete-time martingale. Let $M_0 = 1$ and at each step, independently:

    $$
    M_{n+1} = \begin{cases} 2M_n & \text{with probability } 1/2 \\ 0 & \text{with probability } 1/2 \end{cases}
    $$

    Then $\mathbb{E}[M_{n+1} \mid M_n] = \frac{1}{2}(2M_n) + \frac{1}{2}(0) = M_n$, so $M_n$ is a martingale. We have $\mathbb{E}[M_n] = 1$ for all $n$, so $M$ is $L^1$ bounded.

    However, $M_n$ is not UI. At time $n$, $M_n = 2^n$ with probability $2^{-n}$ and $M_n = 0$ otherwise. For any $c > 0$, once $2^n > c$:

    $$
    \mathbb{E}[|M_n|\,\mathbf{1}_{\{|M_n| > c\}}] = 2^n \cdot 2^{-n} = 1
    $$

    This does not vanish as $c \to \infty$ (since we can always choose $n$ large enough). The tail mass stays at 1 no matter how high we set the threshold, violating UI. Indeed, $M_n \to 0$ a.s. but $\mathbb{E}[M_n] = 1 \neq 0 = \mathbb{E}[M_\infty]$, confirming that $L^1$ convergence fails.

---

**Exercise 4.**
For the Itô integral $M_t = \int_0^t \sigma_s\,dW_s$, use the BDG inequality with $p = 2$ to show that $\mathbb{E}[\sup_{t \leq T} M_t^2] \leq 4\,\mathbb{E}[\int_0^T \sigma_s^2\,ds]$. Why is the constant 4 (Doob's $L^2$ inequality), and how does BDG generalize this?

??? success "Solution to Exercise 4"
    The quadratic variation of $M_t = \int_0^t \sigma_s\,dW_s$ is $\langle M \rangle_t = \int_0^t \sigma_s^2\,ds$. The BDG inequality with $p = 2$ states:

    $$
    c_2\,\mathbb{E}[\langle M \rangle_T] \leq \mathbb{E}\!\left[\sup_{t \leq T} M_t^2\right] \leq C_2\,\mathbb{E}[\langle M \rangle_T]
    $$

    The sharp upper constant is $C_2 = 4$, which recovers **Doob's maximal inequality** for $L^2$ martingales:

    $$
    \mathbb{E}\!\left[\sup_{t \leq T} M_t^2\right] \leq 4\,\mathbb{E}[M_T^2] = 4\,\mathbb{E}\!\left[\int_0^T \sigma_s^2\,ds\right]
    $$

    where the last equality uses the Itô isometry.

    The BDG inequality generalizes Doob's inequality in two ways: (1) it extends to all $p > 0$ (not just $p \geq 1$), and (2) it provides a **two-sided** bound — the lower bound $c_p > 0$ shows that $\sup|M_t|^p$ and $\langle M \rangle_T^{p/2}$ are equivalent in $L^1$, not just one-sided. This equivalence is central to the theory of stochastic integration.

---

**Exercise 5.**
A non-negative continuous local martingale $M$ with $M_0 = 1$ satisfies $\mathbb{E}[M_T] = 1$. Prove that $M$ is a true martingale on $[0,T]$. (Hint: a non-negative local martingale is a supermartingale.)

??? success "Solution to Exercise 5"
    A non-negative local martingale is a supermartingale by Fatou's lemma: for any $0 \leq s \leq t$,

    $$
    \mathbb{E}[M_t \mid \mathcal{F}_s] \leq M_s
    $$

    Taking unconditional expectations: $\mathbb{E}[M_t] \leq \mathbb{E}[M_s] \leq \mathbb{E}[M_0] = 1$.

    Now we use the hypothesis $\mathbb{E}[M_T] = 1$. For $t \leq T$:

    $$
    1 = \mathbb{E}[M_T] \leq \mathbb{E}[M_t] \leq 1
    $$

    so $\mathbb{E}[M_t] = 1$ for all $t \in [0,T]$. Combined with the supermartingale inequality:

    $$
    \mathbb{E}[M_t \mid \mathcal{F}_s] \leq M_s
    $$

    Taking expectations of both sides: $\mathbb{E}[M_t] \leq \mathbb{E}[M_s]$. But we showed both equal 1, so $\mathbb{E}[M_t - \mathbb{E}[M_t \mid \mathcal{F}_s]] = 0$ with $M_t - \mathbb{E}[M_t \mid \mathcal{F}_s] \geq 0$ (since $\mathbb{E}[M_t \mid \mathcal{F}_s] \leq M_s$ and we need to be more careful). Instead, note that $M_s - \mathbb{E}[M_t \mid \mathcal{F}_s] \geq 0$ and $\mathbb{E}[M_s - \mathbb{E}[M_t \mid \mathcal{F}_s]] = \mathbb{E}[M_s] - \mathbb{E}[M_t] = 0$. A non-negative random variable with zero expectation is zero a.s., so $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ a.s. $\square$

---

**Exercise 6.**
A candidate argues: "Since $M_{t \wedge \tau_n}$ is a martingale for each $n$, take $n \to \infty$ and conclude $M_t$ is a martingale." What assumption did they forget, and why can't the limit be taken for free?

??? success "Solution to Exercise 6"
    The candidate forgot the assumption needed to pass the limit inside the conditional expectation. The martingale property $\mathbb{E}[M_{t \wedge \tau_n} \mid \mathcal{F}_s] = M_{s \wedge \tau_n}$ holds for each $n$, and $M_{t \wedge \tau_n} \to M_t$ a.s. as $n \to \infty$.

    However, almost sure convergence alone does not guarantee $\mathbb{E}[M_t \mid \mathcal{F}_s] = \lim \mathbb{E}[M_{t \wedge \tau_n} \mid \mathcal{F}_s]$. To interchange the limit and the conditional expectation, one needs a convergence theorem — typically:

    - **Bounded convergence** (if the process is bounded),
    - **Dominated convergence** (if dominated by an integrable random variable), or
    - **Uniform integrability** of the family $\{M_{t \wedge \tau_n}\}_n$.

    Without such control, the limit may lose mass. This is precisely where the upgrade from local martingale to true martingale requires real work — localization does not disappear for free.
