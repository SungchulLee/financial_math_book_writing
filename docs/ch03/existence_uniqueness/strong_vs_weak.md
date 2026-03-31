# Strong and Weak Solutions of SDEs

The theory of SDEs distinguishes two fundamentally different notions of solution:
**strong** and **weak**. The distinction turns on what is prescribed in advance
and what must be constructed. The existence of strong solutions under Lipschitz
conditions is established via [Picard Iteration](picard_iteration.md); the conditions
themselves are in [Lipschitz Conditions and Linear Growth](lipschitz_conditions.md).

---

## The Core Question

Consider the SDE:

$$
dX_t = b(t, X_t)\,dt + \sigma(t, X_t)\,dW_t, \qquad X_0 = x
$$

**What is given, and what must be built?**

| | Strong solution | Weak solution |
|---|---|---|
| **Given** | Probability space $(\Omega,\mathcal{F},\mathbb{P})$ and Brownian motion $W_t$ | Coefficients $b$, $\sigma$, and initial distribution $\mu$ |
| **Construct** | An adapted process $X_t$ satisfying the SDE | A probability space, a Brownian motion $W_t$, and a process $X_t$ |
| **Informal slogan** | $X_t$ is a functional of the given $W_t$ | $(X_t, W_t)$ has the right joint distribution |

---

## Formal Definitions

### Strong Solution

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \geq 0}, \mathbb{P})$ be a filtered
probability space carrying a Brownian motion $W_t$. A **strong solution** is a
continuous adapted process $X_t$ satisfying:

1. $X_t$ is adapted to $\mathcal{F}_t^W := \sigma(W_s : 0 \leq s \leq t)$,
   the natural filtration of $W$ (augmented to satisfy the usual conditions).
2. $\displaystyle\int_0^T \bigl(|b(t,X_t)| + |\sigma(t,X_t)|^2\bigr)\,dt < \infty$ a.s.
3. $\displaystyle X_t = x + \int_0^t b(s,X_s)\,ds + \int_0^t \sigma(s,X_s)\,dW_s$ a.s.

**Key point.** Condition 1 means $X_t$ is completely determined by the Brownian
path — there is no additional randomness.

### Weak Solution

A **weak solution** is a tuple $(\Omega, \mathcal{F}, (\mathcal{F}_t), \mathbb{P}, W_t, X_t)$
where $(\Omega, \mathcal{F}, (\mathcal{F}_t), \mathbb{P})$ satisfies the usual
conditions, $W_t$ is an $(\mathcal{F}_t)$-Brownian motion, $X_t$ is continuous
and $(\mathcal{F}_t)$-adapted, and the SDE integral equation holds a.s.

**Key difference from strong.** $X_t$ is required to be $(\mathcal{F}_t)$-adapted,
not necessarily $(\mathcal{F}_t^W)$-adapted. The process may depend on randomness
beyond the driving Brownian motion.

!!! note "Usual conditions"
    A filtration satisfies the **usual conditions** if it is right-continuous
    ($\mathcal{F}_t = \mathcal{F}_{t+}$) and $\mathcal{F}_0$ contains all
    $\mathbb{P}$-null sets. These are standard regularity hypotheses in
    stochastic analysis.

---

## Two Notions of Uniqueness

### Pathwise Uniqueness

**Pathwise uniqueness** holds if: whenever $(X_t, W_t)$ and $(Y_t, W_t)$ are two
solutions on the **same** probability space with the **same** Brownian motion and
$X_0 = Y_0$ a.s., then

$$
\mathbb{P}\!\left(X_t = Y_t\ \text{for all}\ t \geq 0\right) = 1.
$$

Meaning: the solution trajectory is uniquely determined by the Brownian path.

### Uniqueness in Law

**Uniqueness in law** holds if any two weak solutions with the same initial
distribution have the same law:

$$
\mathrm{Law}(X_t : t \geq 0) = \mathrm{Law}(X_t' : t \geq 0).
$$

Meaning: the probability distribution of the solution is unique, even if individual
paths on different probability spaces differ.

### Logical Relationships

$$
\text{Strong solution} \implies \text{Weak solution}
$$

$$
\text{Pathwise uniqueness} \implies \text{Uniqueness in law}
$$

Neither converse holds in general.

---

## The Yamada–Watanabe Theorem

This theorem is the central bridge between the two levels of the theory.

**Theorem (Yamada–Watanabe, 1971).**

$$
\boxed{\text{Pathwise uniqueness} + \text{Weak existence}
\implies \text{Strong existence} + \text{Uniqueness in law}}
$$

More precisely: if pathwise uniqueness holds and at least one weak solution
exists, then a strong solution exists and it is unique in law.

**Strategic value.** To establish strong existence it suffices to:

1. Verify pathwise uniqueness (often via Gronwall or the Yamada–Watanabe
   $\rho$-condition; see [Lipschitz Conditions](lipschitz_conditions.md)).
2. Construct *any* weak solution — often easier, since one has freedom to choose
   the probability space. Girsanov's theorem (measure change to introduce drift)
   and the Stroock–Varadhan martingale problem (characterising the law of $X_t$
   directly) are the standard tools, both treated in later sections of this chapter.

---

## Examples

### Example 1: Lipschitz Coefficients (Strong Solution)

For $dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t$ with globally Lipschitz coefficients:

- Strong existence: ✓ (Picard iteration)
- Pathwise uniqueness: ✓ (Gronwall)
- Uniqueness in law: ✓ (follows from pathwise uniqueness)

### Example 2: Tanaka's SDE (Weak but Not Strong)

$$
dX_t = \mathrm{sgn}(X_t)\,dW_t, \qquad X_0 = 0,
\qquad \mathrm{sgn}(x) = \begin{cases} 1 & x > 0 \\ -1 & x \leq 0 \end{cases}
$$

**Weak solution exists.** Let $B_t$ be a standard Brownian motion on some
probability space. By the Tanaka–Meyer formula:

$$
|B_t| = \int_0^t \mathrm{sgn}(B_s)\,dB_s + L_t^0(B)
$$

where $L_t^0(B)$ is the local time of $B$ at $0$. Define
$W_t := \int_0^t \mathrm{sgn}(B_s)\,dB_s.$
By Lévy's characterisation theorem, $W_t$ is a Brownian motion (it is a
continuous local martingale with $\langle W \rangle_t = t$). Since $L_t^0(B)$
is non-decreasing and supported on $\{t : |B_t| = 0\}$, the tuple
$((\Omega,\mathcal{F},\mathbb{P}), W_t, X_t = |B_t|)$ satisfies
$dX_t = \mathrm{sgn}(X_t)\,dW_t$ in the integral sense and is a valid weak solution.

**Pathwise uniqueness fails.** The Engelbert–Schmidt theory provides a direct proof.
The coefficient $\sigma(x) = \mathrm{sgn}(x)$ satisfies $1/\sigma^2 \equiv 1 \in
L^1_{\mathrm{loc}}(\mathbb{R})$ but is not locally Lipschitz at $x = 0$. The
Engelbert–Schmidt theorem guarantees that on any filtered probability space
carrying a Brownian motion $W_t$, the equation $dX_t = \mathrm{sgn}(X_t)\,dW_t$
started at $X_0 = 0$ admits multiple solutions — that is, two adapted continuous
processes $X$ and $Y$ with $X_0 = Y_0 = 0$ and $X_t \neq Y_t$ on a set of
positive measure — directly violating pathwise uniqueness. The explicit
construction of these multiple solutions is given in Revuz–Yor, Chapter IX.

**Strong solution does not exist.** Since pathwise uniqueness fails, the
Yamada–Watanabe theorem (contrapositive) implies immediately that no strong
solution can exist: if a strong solution existed, Yamada–Watanabe would force
pathwise uniqueness, a contradiction.

!!! note "Intuition"
    The reason no strong solution exists can be understood informally: $W_t$
    records only the $\mathrm{sgn}$-weighted increments of $B_t$, destroying
    the sign information of $B_t$ itself. A measurable functional
    $F(W_s : s \leq t)$ therefore cannot recover the sign of $X_t$, so the
    map $W \mapsto X$ is not well-defined.

**Uniqueness in law holds.** Any weak solution $X_t$ satisfies $X_0 = 0$,
has continuous paths, and $\langle X \rangle_t = t$ (since $\mathrm{sgn}^2 = 1$
a.e.). For the non-negative solution constructed above, the Skorokhod reflection
characterisation identifies its law as that of reflected Brownian motion $|B_t|$.
For a general weak solution (which need not be non-negative a priori), uniqueness
of the law follows from the martingale characterisation of reflected Brownian
motion: any continuous semimartingale $X_t$ with $\langle X \rangle_t = t$,
$X_0 = 0$, satisfying the SDE, has the same law as $|B_t|$ by uniqueness of the
solution to the corresponding martingale problem. Hence
$\mathrm{Law}(X_t) = \mathrm{Law}(|B_t|)$ for all weak solutions.

### Example 3: No Weak Solution (Tsirelson, 1975)

Tsirelson constructed a time-inhomogeneous SDE $dX_t = b(t, X_t)\,dW_t$ with
bounded measurable coefficients for which no weak solution exists. The
obstruction is measure-theoretic: the filtration generated by any candidate
$(X_t, W_t)$ cannot simultaneously satisfy the adaptedness requirement and the
SDE equation. The construction is beyond the scope of this chapter; see
Revuz–Yor, Chapter IX, or Rogers–Williams, Volume II.

---

## When Does Strong Existence Hold?

| Hypothesis | Conclusion |
|---|---|
| Lipschitz + linear growth | Strong existence and pathwise uniqueness |
| Yamada–Watanabe $\rho$-condition + Lipschitz drift (1D) | Pathwise uniqueness |
| Pathwise uniqueness + weak existence | Strong existence + uniqueness in law |
| Weak existence only, pathwise uniqueness unknown | Uniqueness in law may or may not hold (holds for Tanaka; vacuous for Tsirelson since no weak solution exists) |

---

## Practical Implications

**Simulation.** Strong solutions can be simulated pathwise by discretising $W_t$
(e.g., Euler–Maruyama). For weak solutions, only the distribution is meaningful;
different simulations may live on different probability spaces.

**Mathematical finance.** Option pricing requires only the distribution of $X_t$
under the risk-neutral measure — weak solutions suffice. Delta-hedging, however,
requires a pathwise relationship between the asset price and the hedging portfolio,
making strong solutions more natural.

**Nonlinear filtering.** The filter must compute an estimate of the signal $X_t$
from an observed process on the *same* probability space. Strong adaptedness —
$X_t$ measurable with respect to the observation filtration — is essential; a
weak solution on a different space cannot be used directly.

---

## Summary

$$
\boxed{\begin{aligned}
&\text{Strong} \implies \text{Weak} \\[4pt]
&\text{Pathwise uniqueness} \implies \text{Uniqueness in law} \\[4pt]
&\text{Pathwise uniqueness} + \text{Weak existence}
  \implies \text{Strong existence} + \text{Uniqueness in law}
\end{aligned}}
$$

1. A **strong solution** is a functional of the prescribed Brownian motion;
   a **weak solution** only specifies the joint distribution of $(X_t, W_t)$.
2. **Pathwise uniqueness** is the stronger condition; it implies uniqueness in
   law but not vice versa.
3. The **Yamada–Watanabe theorem** converts pathwise uniqueness + weak existence
   into strong existence — a powerful reduction strategy.
4. **Tanaka's SDE** is the canonical example of a weak solution existing without
   a strong solution: pathwise uniqueness fails by the Engelbert–Schmidt theorem,
   and non-existence of a strong solution follows from Yamada–Watanabe by
   contrapositive.

---

## Exercises

**Exercise 1.** For each of the following SDEs, determine whether the solution is strong, weak (but not strong), or whether existence fails. Justify your answers by identifying which conditions (Lipschitz, Yamada--Watanabe, etc.) hold or fail.

(a) $dX_t = -X_t\,dt + 2\,dW_t$, $\quad X_0 = 1$

(b) $dX_t = \mathrm{sgn}(X_t)\,dW_t$, $\quad X_0 = 0$

(c) $dX_t = X_t\,dt + X_t\,dW_t$, $\quad X_0 = x_0 > 0$

---

**Exercise 2.** State the formal definition of a strong solution. Explain why condition 1 ($X_t$ is $\mathcal{F}_t^W$-adapted) means that a strong solution is a "functional of the Brownian path." Give an explicit example by writing the strong solution of the geometric Brownian motion SDE $dX_t = \mu X_t\,dt + \sigma X_t\,dW_t$ as a measurable map $X_t = F(t, W_s : 0 \leq s \leq t)$.

---

**Exercise 3.** Consider Tanaka's SDE $dX_t = \mathrm{sgn}(X_t)\,dW_t$ with $X_0 = 0$. The text constructs a weak solution using the Tanaka--Meyer formula for $|B_t|$.

(a) Verify that $W_t = \int_0^t \mathrm{sgn}(B_s)\,dB_s$ has quadratic variation $\langle W \rangle_t = t$, confirming it is a Brownian motion by Levy's characterisation.

(b) Explain why $X_t = |B_t|$ satisfies $dX_t = \mathrm{sgn}(X_t)\,dW_t$ despite the presence of the local time term $L_t^0(B)$ in the Tanaka--Meyer formula.

---

**Exercise 4.** Prove that pathwise uniqueness implies uniqueness in law. Proceed as follows: let $(\Omega_1, \mathbb{P}_1, W^1, X^1)$ and $(\Omega_2, \mathbb{P}_2, W^2, X^2)$ be two weak solutions with the same initial distribution. Construct a common probability space on which both solutions can be compared (hint: use the product space $\Omega_1 \times \Omega_2$), and explain how pathwise uniqueness on this space forces $\mathrm{Law}(X^1) = \mathrm{Law}(X^2)$.

---

**Exercise 5.** The Yamada--Watanabe theorem states:

$$
\text{Pathwise uniqueness} + \text{Weak existence} \implies \text{Strong existence}
$$

Explain why the converse fails: give an example (or describe a scenario) where a strong solution exists but pathwise uniqueness does not hold. Then explain why the Yamada--Watanabe theorem is still useful despite this asymmetry.

---

**Exercise 6.** In mathematical finance, the Black--Scholes model $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ admits a strong solution. Explain why strong existence is essential for delta-hedging, where the hedging strategy must be computed pathwise as a function of the observed asset price trajectory. Contrast this with option pricing under the risk-neutral measure, where only the distribution of $S_T$ matters, and a weak solution would suffice.

---

**Exercise 7.** Complete the following classification table by filling in "Yes," "No," or "N/A" for each entry. Justify each answer briefly.

| SDE | Weak existence | Pathwise uniqueness | Uniqueness in law | Strong existence |
|---|---|---|---|---|
| $dX_t = -X_t\,dt + dW_t$ | | | | |
| $dX_t = \mathrm{sgn}(X_t)\,dW_t$, $X_0 = 0$ | | | | |
| $dX_t = \kappa(\theta - X_t)\,dt + \sigma\sqrt{X_t}\,dW_t$ (CIR) | | | | |

---

## Solutions

??? success "Solution to Exercise 1"
    **(a)** $dX_t = -X_t\,dt + 2\,dW_t$, $X_0 = 1$.

    The drift $b(x) = -x$ is globally Lipschitz with constant $K = 1$, and the diffusion $\sigma(x) = 2$ is constant (Lipschitz with constant $0$). Both satisfy linear growth. By the main existence and uniqueness theorem, a **strong solution** exists and is pathwise unique. This is the Ornstein--Uhlenbeck process with explicit solution:

    $$
    X_t = e^{-t} + 2\int_0^t e^{-(t-s)}\,dW_s
    $$

    **(b)** $dX_t = \mathrm{sgn}(X_t)\,dW_t$, $X_0 = 0$.

    This is Tanaka's SDE. The diffusion coefficient $\sigma(x) = \mathrm{sgn}(x)$ is discontinuous at $x = 0$, so the global Lipschitz condition fails. As shown in the text, a **weak solution** exists (via the Tanaka--Meyer formula, $X_t = |B_t|$), but pathwise uniqueness fails (by the Engelbert--Schmidt theorem). By the contrapositive of Yamada--Watanabe, **no strong solution exists**. Uniqueness in law does hold.

    **(c)** $dX_t = X_t\,dt + X_t\,dW_t$, $X_0 = x_0 > 0$.

    Both $b(x) = x$ and $\sigma(x) = x$ are globally Lipschitz with constant $K = 1$, and linear growth holds. A **strong solution** exists and is pathwise unique. The explicit solution is geometric Brownian motion:

    $$
    X_t = x_0 \exp\!\left(\tfrac{1}{2}t + W_t\right)
    $$

??? success "Solution to Exercise 2"
    A strong solution is a continuous adapted process $X_t$ on a given filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}_t), \mathbb{P})$ carrying a Brownian motion $W_t$ such that:

    1. $X_t$ is $\mathcal{F}_t^W$-adapted (measurable with respect to the natural filtration of $W$).
    2. $\int_0^T (|b(t,X_t)| + |\sigma(t,X_t)|^2)\,dt < \infty$ a.s.
    3. $X_t = x + \int_0^t b(s,X_s)\,ds + \int_0^t \sigma(s,X_s)\,dW_s$ a.s.

    **Why condition 1 means "functional of the Brownian path":** Being $\mathcal{F}_t^W$-adapted means that for each $t$, the random variable $X_t(\omega)$ depends on $\omega$ only through the values $(W_s(\omega) : 0 \leq s \leq t)$. By measurability, there exists a measurable function $F_t$ such that $X_t = F_t(W_s : 0 \leq s \leq t)$. The solution is completely determined by the Brownian path — no additional randomness is needed.

    **Explicit example for GBM:** The SDE $dX_t = \mu X_t\,dt + \sigma X_t\,dW_t$ has the strong solution:

    $$
    X_t = x_0 \exp\!\left[\left(\mu - \tfrac{1}{2}\sigma^2\right)t + \sigma W_t\right]
    $$

    This is an explicit measurable map $F(t, W_s : 0 \leq s \leq t) = x_0\exp[(\mu - \sigma^2/2)t + \sigma W_t]$. Note that $X_t$ depends on the Brownian path only through the terminal value $W_t$, which is a special feature of SDEs with linear coefficients.

??? success "Solution to Exercise 3"
    **(a)** Define $W_t = \int_0^t \mathrm{sgn}(B_s)\,dB_s$. The quadratic variation is:

    $$
    \langle W \rangle_t = \int_0^t \mathrm{sgn}(B_s)^2\,ds = \int_0^t 1\,ds = t
    $$

    since $\mathrm{sgn}(x)^2 = 1$ for all $x$ (using $\mathrm{sgn}(0) = -1$ by convention, but the set $\{s : B_s = 0\}$ has Lebesgue measure zero a.s., so the value at zero is irrelevant). Since $W_t$ is a continuous local martingale (as a stochastic integral of a bounded predictable integrand against a Brownian motion) with $\langle W \rangle_t = t$, Levy's characterisation theorem implies $W_t$ is a standard Brownian motion.

    **(b)** The Tanaka--Meyer formula gives:

    $$
    |B_t| = \int_0^t \mathrm{sgn}(B_s)\,dB_s + L_t^0(B) = W_t + L_t^0(B)
    $$

    Setting $X_t = |B_t|$, we want to verify $dX_t = \mathrm{sgn}(X_t)\,dW_t$. Since $X_t = |B_t| \geq 0$, we have $\mathrm{sgn}(X_t) = 1$ for $X_t > 0$ and $\mathrm{sgn}(0) = -1$.

    The key observation is that in the SDE integral equation:

    $$
    X_t = X_0 + \int_0^t \mathrm{sgn}(X_s)\,dW_s
    $$

    we need to check this against $X_t = W_t + L_t^0(B)$. We can write $dB_s = \mathrm{sgn}(B_s)\,dW_s$ (inverting $dW_s = \mathrm{sgn}(B_s)\,dB_s$, since $\mathrm{sgn}^2 = 1$). Then:

    $$
    \int_0^t \mathrm{sgn}(X_s)\,dW_s = \int_0^t \mathrm{sgn}(|B_s|)\,\mathrm{sgn}(B_s)\,dB_s = \int_0^t |\mathrm{sgn}(B_s)|\,dB_s
    $$

    Since $|\mathrm{sgn}(B_s)| = 1$ a.e., this equals $\int_0^t dB_s = B_t = B_t - B_0$. But the Tanaka--Meyer formula gives $|B_t| = W_t + L_t^0$, and the local time $L_t^0(B)$ is a continuous non-decreasing process that increases only when $B_t = 0$ (equivalently, $X_t = 0$). The local time acts as a reflecting boundary term. In the weak formulation, the SDE $dX_t = \mathrm{sgn}(X_t)\,dW_t$ is satisfied because the local time does not contribute to the martingale part — it is a process of zero quadratic variation, and the SDE is understood to hold in the sense of the integral equation with $X_0 = 0$.

??? success "Solution to Exercise 4"
    Let $(\Omega_1, \mathbb{P}_1, W^1, X^1)$ and $(\Omega_2, \mathbb{P}_2, W^2, X^2)$ be two weak solutions with $\mathrm{Law}(X_0^1) = \mathrm{Law}(X_0^2) = \mu$.

    **Construct a common probability space:** Take the product space $(\Omega, \mathbb{P}) = (\Omega_1 \times \Omega_2, \mathbb{P}_1 \otimes \mathbb{P}_2)$. Define:

    - $\tilde{X}^1(\omega_1, \omega_2) = X^1(\omega_1)$, $\tilde{W}^1(\omega_1, \omega_2) = W^1(\omega_1)$
    - $\tilde{X}^2(\omega_1, \omega_2) = X^2(\omega_2)$, $\tilde{W}^2(\omega_1, \omega_2) = W^2(\omega_2)$

    Both $(\tilde{X}^1, \tilde{W}^1)$ and $(\tilde{X}^2, \tilde{W}^2)$ are weak solutions on the product space.

    Now, $\tilde{W}^1$ and $\tilde{W}^2$ are two different Brownian motions on $(\Omega, \mathbb{P})$. Since $\mathrm{Law}(\tilde{W}^1) = \mathrm{Law}(\tilde{W}^2)$ (both are standard Brownian motions) and $\mathrm{Law}(\tilde{X}_0^1) = \mathrm{Law}(\tilde{X}_0^2) = \mu$, the joint distributions $\mathrm{Law}(\tilde{X}_0^1, \tilde{W}^1)$ and $\mathrm{Law}(\tilde{X}_0^2, \tilde{W}^2)$ agree (both equal $\mu \otimes \text{Wiener measure}$ since the initial condition is independent of the Brownian motion).

    By the Skorokhod representation theorem, we can find a probability space $(\hat{\Omega}, \hat{\mathbb{P}})$ carrying a single Brownian motion $\hat{W}$ and two processes $\hat{X}^1$, $\hat{X}^2$ such that $(\hat{X}^i, \hat{W})$ has the same law as $(\tilde{X}^i, \tilde{W}^i)$ for $i = 1,2$, and both solve the SDE driven by $\hat{W}$ with $\hat{X}_0^1 = \hat{X}_0^2$ a.s.

    Now pathwise uniqueness applies on $(\hat{\Omega}, \hat{\mathbb{P}})$: since $\hat{X}^1$ and $\hat{X}^2$ are two solutions driven by the same $\hat{W}$ with the same initial condition, $\hat{X}^1 = \hat{X}^2$ a.s. Therefore $\mathrm{Law}(X^1) = \mathrm{Law}(\hat{X}^1) = \mathrm{Law}(\hat{X}^2) = \mathrm{Law}(X^2)$.

??? success "Solution to Exercise 5"
    **Why the converse fails:** A strong solution can exist without pathwise uniqueness. Consider an SDE where the coefficients are smooth and Lipschitz except on a null set that is never visited by any particular solution. More concretely, consider an SDE of the form $dX_t = \sigma(X_t)\,dW_t$ where $\sigma$ is chosen so that multiple weak solutions exist (pathwise uniqueness fails), yet one can still construct a strong (adapted to $\mathcal{F}^W$) solution for specific initial conditions.

    A more standard example: the SDE $dX_t = \mathrm{sgn}(X_t)\,dW_t$ with $X_0 = 1$ (instead of $X_0 = 0$). For this initial condition, the solution $X_t$ stays away from zero for small $t$ (where the discontinuity lives), and the coefficients are locally Lipschitz away from zero. A local strong solution exists. However, pathwise uniqueness in the global sense (for all initial conditions, including $X_0 = 0$) fails.

    **Why Yamada--Watanabe is still useful:** Despite the asymmetry, the theorem provides a powerful strategy for establishing strong existence: instead of constructing a strong solution directly (which requires exhibiting a measurable functional of the Brownian motion), one can separately (1) prove pathwise uniqueness via analytical estimates and (2) construct any weak solution by choosing a convenient probability space. This decomposition is often much easier than a direct construction.

??? success "Solution to Exercise 6"
    **Delta-hedging requires strong solutions:** In the Black--Scholes framework, the delta-hedging strategy $\Delta_t = \partial_S V(t, S_t)$ must be computed as a function of the observed asset price trajectory $S_t$. This requires that $S_t$ is a functional of the Brownian motion driving the market — precisely the condition for a strong solution. The hedger observes the price path $(S_s : 0 \leq s \leq t)$, which determines $W_t$ (and vice versa), and must construct a portfolio process adapted to this filtration.

    If only a weak solution existed, $S_t$ would not be uniquely determined by the Brownian path. Different probability spaces could yield different price trajectories with the same distribution but different pathwise relationships to the driving noise. The hedging strategy $\Delta_t$ would not be well-defined as a function of the observed path, because the map from the Brownian motion to the asset price would not be unique.

    **Option pricing needs only weak solutions:** The Black--Scholes price of a European option with payoff $h(S_T)$ is:

    $$
    V_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[h(S_T)]
    $$

    This depends only on the distribution of $S_T$ under the risk-neutral measure $\mathbb{Q}$, not on the pathwise relationship between $S_t$ and $W_t$. If two weak solutions $S$ and $S'$ have the same law, then $\mathbb{E}^{\mathbb{Q}}[h(S_T)] = \mathbb{E}^{\mathbb{Q}}[h(S_T')]$, so the price is the same. A weak solution (plus uniqueness in law) therefore suffices for pricing.

??? success "Solution to Exercise 7"
    The completed table:

    | SDE | Weak existence | Pathwise uniqueness | Uniqueness in law | Strong existence |
    |---|---|---|---|---|
    | $dX_t = -X_t\,dt + dW_t$ | Yes | Yes | Yes | Yes |
    | $dX_t = \mathrm{sgn}(X_t)\,dW_t$, $X_0 = 0$ | Yes | No | Yes | No |
    | $dX_t = \kappa(\theta - X_t)\,dt + \sigma\sqrt{X_t}\,dW_t$ (CIR) | Yes | Yes | Yes | Yes |

    **Justifications:**

    **OU process** $dX_t = -X_t\,dt + dW_t$: Both $b(x) = -x$ and $\sigma(x) = 1$ are globally Lipschitz (with $K = 1$) and satisfy linear growth. The main existence and uniqueness theorem gives strong existence and pathwise uniqueness. Uniqueness in law follows since pathwise uniqueness implies it.

    **Tanaka's SDE** $dX_t = \mathrm{sgn}(X_t)\,dW_t$, $X_0 = 0$: Weak existence holds via the Tanaka--Meyer construction ($X_t = |B_t|$). Pathwise uniqueness fails by the Engelbert--Schmidt theorem (the coefficient $\mathrm{sgn}(x)$ is discontinuous at $x = 0$). Strong existence fails by the contrapositive of Yamada--Watanabe. Uniqueness in law holds: every weak solution has the law of reflected Brownian motion $|B_t|$.

    **CIR process:** The drift $b(x) = \kappa(\theta - x)$ is globally Lipschitz with constant $\kappa$. The diffusion $\sigma(x) = \sigma\sqrt{x}$ is not globally Lipschitz, but satisfies the Yamada--Watanabe condition with $\rho(u) = \sigma u^{1/2}$ (since $\int_0^\epsilon u^{-1}\,du = +\infty$). Linear growth holds since $|\sqrt{x}| \leq 1 + |x|$. Weak existence follows from general results (e.g., the Stroock--Varadhan martingale problem, or direct construction). Pathwise uniqueness holds by the Yamada--Watanabe $\rho$-condition. By the Yamada--Watanabe theorem, strong existence and uniqueness in law follow.
