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
