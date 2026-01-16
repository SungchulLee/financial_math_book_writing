# Doob–Meyer Decomposition

## Separating Signal from Noise

One of the deepest insights in martingale theory is that every "reasonable" stochastic process can be decomposed into two parts: a **martingale** (pure noise, unpredictable fluctuations) and a **predictable finite variation process** (systematic drift, accumulated trend).

This is the Doob–Meyer decomposition. It reveals the internal structure of stochastic processes and explains why semimartingales—the natural class for stochastic integration—have the form they do.

---

## Motivation: The Itô Process Perspective

Consider an Itô process:

$$
X_t = X_0 + \int_0^t b_s \, ds + \int_0^t \sigma_s \, dW_s
$$

This already exhibits a decomposition:

- **Drift term**: $A_t = \int_0^t b_s \, ds$ — predictable, finite variation
- **Martingale term**: $M_t = \int_0^t \sigma_s \, dW_s$ — local martingale

The Doob–Meyer theorem says this structure is **universal**: it holds for all submartingales, not just those arising from SDEs.

---

## Discrete-Time Doob Decomposition

We start with discrete time, where the decomposition is elementary.

**Theorem (Discrete Doob Decomposition)**: Let $(X_n, \mathcal{F}_n)_{n \ge 0}$ be an adapted integrable process. Then there exist unique processes:

- $(M_n)$ — a martingale with $M_0 = 0$
- $(A_n)$ — a predictable process with $A_0 = 0$

such that:

$$
\boxed{X_n = X_0 + M_n + A_n}
$$

**Proof**: Define $A_n$ recursively by:

$$
A_0 = 0, \quad A_n - A_{n-1} = \mathbb{E}[X_n - X_{n-1} \mid \mathcal{F}_{n-1}]
$$

Then $A_n$ is predictable (since $A_n - A_{n-1}$ is $\mathcal{F}_{n-1}$-measurable).

Define $M_n = X_n - X_0 - A_n$. Then:

$$
\mathbb{E}[M_n - M_{n-1} \mid \mathcal{F}_{n-1}] = \mathbb{E}[X_n - X_{n-1} \mid \mathcal{F}_{n-1}] - (A_n - A_{n-1}) = 0
$$

So $M_n$ is a martingale.

**Uniqueness**: If $X_n = X_0 + M_n + A_n = X_0 + \widetilde{M}_n + \widetilde{A}_n$, then $M_n - \widetilde{M}_n = \widetilde{A}_n - A_n$ is both a martingale and predictable. A predictable martingale starting at 0 must be 0 (exercise). $\square$

**Submartingale case**: $X_n$ is a submartingale iff $A_n$ is increasing (i.e., $A_n - A_{n-1} \ge 0$).

---

## Continuous-Time: Technical Challenges

In continuous time, the decomposition requires more care:

1. **Path regularity**: We need càdlàg (right-continuous with left limits) paths.
2. **Integrability**: Simple boundedness isn't enough; we need uniform integrability conditions.
3. **Predictability**: The increasing process must be predictable, not just adapted.

The key concept is **class (D)**.

---

## Class (D) Processes

**Definition**: A càdlàg adapted process $(X_t)_{t \ge 0}$ is of **class (D)** if the family:

$$
\{X_\tau : \tau \text{ is a bounded stopping time}\}
$$

is uniformly integrable.

**Interpretation**: Class (D) processes don't blow up too badly, even when stopped at arbitrary (bounded) random times.

**Examples**:

- Any uniformly integrable martingale is class (D).
- $W_t^2$ is not class (D) (it's unbounded in expectation).
- $W_{t \wedge T}^2$ is class (D) for fixed $T$ (it's bounded).

---

## The Doob–Meyer Theorem

**Theorem (Doob–Meyer Decomposition)**: Let $(X_t)_{t \ge 0}$ be a càdlàg submartingale of class (D). Then there exist unique processes:

- $(M_t)$ — a càdlàg martingale
- $(A_t)$ — a predictable càdlàg increasing process with $A_0 = 0$

such that:

$$
\boxed{X_t = X_0 + M_t + A_t, \quad t \ge 0}
$$

Equivalently:

$$
\boxed{M_t = X_t - X_0 - A_t \text{ is a martingale}}
$$

**Remarks**:

1. "Increasing" means $A_s \le A_t$ for $s \le t$ almost surely.
2. "Predictable" is essential—without it, the decomposition wouldn't be unique.
3. The theorem extends to local submartingales via localization.

---

## Proof Sketch

The proof proceeds through several steps:

**Step 1**: For discrete approximations, apply the discrete Doob decomposition.

**Step 2**: Show the discrete increasing processes converge (in an appropriate sense) to a continuous-time limit.

**Step 3**: Verify predictability of the limit using properties of the predictable $\sigma$-algebra.

**Step 4**: Establish uniqueness via the fact that a predictable finite variation martingale starting at 0 must be identically 0.

The details involve delicate arguments from the general theory of processes and are typically found in advanced texts (e.g., Dellacherie-Meyer, Revuz-Yor).

---

## Uniqueness

**Theorem**: The decomposition is unique: if

$$
X_t = X_0 + M_t + A_t = X_0 + \widetilde{M}_t + \widetilde{A}_t
$$

with both $(A_t)$ and $(\widetilde{A}_t)$ predictable increasing, then:

$$
A_t = \widetilde{A}_t \quad \text{for all } t, \text{ a.s.}
$$

Hence $M_t = \widetilde{M}_t$ as well.

**Proof**: The difference $A_t - \widetilde{A}_t = \widetilde{M}_t - M_t$ is both:

- Predictable finite variation (difference of predictable finite variation)
- A martingale (difference of martingales)

A continuous finite variation martingale must be constant (its quadratic variation is 0). With $A_0 = \widetilde{A}_0 = 0$, we get $A_t = \widetilde{A}_t$. $\square$

---

## The Compensator

The predictable increasing process $A_t$ in the Doob–Meyer decomposition is called the **compensator** (or **dual predictable projection**) of the submartingale $X_t$.

**Interpretation**: $A_t$ captures the "expected accumulated increase" of $X_t$ given past information. It's the systematic drift stripped away from the random fluctuations.

**Notation**: Sometimes written $A_t = \langle X \rangle_t^p$ or $A_t = X_t^p$ (predictable compensator).

---

## Key Examples

### Example 1: Squared Brownian Motion

For $X_t = W_t^2$, Itô's formula gives:

$$
W_t^2 = 2\int_0^t W_s \, dW_s + t
$$

Thus:

- $M_t = 2\int_0^t W_s \, dW_s$ (martingale)
- $A_t = t$ (predictable increasing)

The compensator is deterministic: $A_t = t = [W]_t$ (the quadratic variation).

$$
\boxed{W_t^2 = M_t + t}
$$

### Example 2: Submartingale from Convex Transform

If $M_t$ is a martingale and $\varphi$ is convex with $\varphi(M_t) \in L^1$, then $X_t = \varphi(M_t)$ is a submartingale.

For $\varphi(x) = x^2$ and $M_t = W_t$:

$$
W_t^2 - t = M_t \quad \text{(the martingale part)}
$$

### Example 3: Absolute Value

$|W_t|$ is a submartingale. Its Doob–Meyer decomposition involves the **local time** $L_t^0$:

$$
|W_t| = \int_0^t \text{sgn}(W_s) \, dW_s + L_t^0
$$

where $L_t^0$ is the local time at 0 (a continuous increasing process measuring time spent near 0).

### Example 4: Maximum Process

$M_t^* = \sup_{s \le t} W_s$ is a submartingale. Its compensator involves reflected Brownian motion and is related to the running maximum's rate of increase.

---

## Connection to Quadratic Variation

For a continuous local martingale $M_t$, the **quadratic variation** $[M]_t$ is the unique continuous increasing process such that:

$$
M_t^2 - [M]_t \text{ is a local martingale}
$$

Comparing with Doob–Meyer: $M_t^2$ is a submartingale (when $M_t$ is a true martingale), and $[M]_t$ is its compensator.

**For Brownian motion**: $[W]_t = t$, recovering $W_t^2 - t$ is a martingale.

**Key relationship**:

$$
\text{Quadratic variation} = \text{Compensator of the square}
$$

---

## Semimartingales

The Doob–Meyer decomposition naturally leads to the class of **semimartingales**.

**Definition**: A process $X_t$ is a **semimartingale** if it can be written as:

$$
X_t = X_0 + M_t + A_t
$$

where $M_t$ is a local martingale and $A_t$ is an adapted càdlàg finite variation process (not necessarily increasing or predictable).

**Key facts**:

1. Semimartingales are the most general class of integrators for stochastic integrals.
2. Every submartingale of class (D) is a semimartingale (by Doob–Meyer).
3. Itô processes are semimartingales.
4. The semimartingale property is preserved under $C^2$ transformations (Itô's formula).

---

## Applications

### 1. Characterizing Martingales

A process is a martingale iff its Doob–Meyer compensator is 0. This gives a criterion: check whether the expected drift vanishes.

### 2. Change of Measure

Under Girsanov's theorem, changing measure changes the compensator. If $X_t$ has compensator $A_t$ under $\mathbb{P}$, it has a different compensator under $\mathbb{Q}$.

### 3. Stochastic Calculus

The Doob–Meyer decomposition justifies writing Itô processes as drift + martingale. The general theory extends this to all semimartingales.

### 4. Mathematical Finance

In pricing theory, the compensator of a price process determines the "risk premium." Under the risk-neutral measure, the compensator adjusts so that discounted prices become martingales.

---

## Historical Perspective

The theorem is named after:

- **Joseph Doob** (1910–2004): American mathematician who founded modern martingale theory
- **Paul-André Meyer** (1934–2003): French mathematician who generalized the decomposition to continuous time

Meyer's work in the 1960s, as part of the Strasbourg school, established the general theory of processes that underpins modern stochastic analysis.

---

## Summary

The Doob–Meyer Decomposition:

$$
\boxed{X_t = X_0 + M_t + A_t}
$$

| Component | Type | Interpretation |
|-----------|------|----------------|
| $M_t$ | Martingale | Pure noise, unpredictable fluctuations |
| $A_t$ | Predictable increasing | Systematic drift, accumulated trend |

**When it applies**: Class (D) submartingales (or local submartingales via localization).

**Why it matters**:

- Reveals the internal structure of stochastic processes
- Explains why semimartingales are the natural class for integration
- Connects martingale theory to quadratic variation
- Provides the foundation for Itô calculus and beyond

The decomposition tells us that every submartingale is secretly a martingale plus predictable drift—separating what can be anticipated from what cannot.
