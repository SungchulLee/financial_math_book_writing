# Proof Sketch and Key Ideas

This section justifies the [theorem statement](girsanov_theorem.md#statement-of-girsanovs-theorem) through a sequence of steps.

!!! tip "Toy mechanism: one cancellation does all the work"
    The whole proof has a single load-bearing identity. The shifted process $\widetilde W_t = W_t + \int_0^t\theta\,ds$ carries an unwanted drift $+\theta_t\,dt$; the density $Z_t$ is *defined* with the term $-\theta_t\,dW_t$ precisely so that the Itô product $d(\widetilde W_t Z_t)$ generates a cross-variation $-Z_t\theta_t\,dt$ that *cancels* the drift exactly. After that one cancellation, $\widetilde W_t Z_t$ is a $\mathbb{P}$-martingale, $\widetilde W_t$ is a continuous $\mathbb{Q}$-local martingale with $\langle\widetilde W\rangle_t = t$, and Lévy's theorem closes the argument. The four steps below verify this in turn; the [cancellation table](#key-insight-the-cancellation-mechanism) at the bottom makes the bookkeeping explicit.

---

## Step 1: Verify the Exponential Martingale Property

**Goal:** Show that $Z_t = \exp\left(-\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)$ is a $\mathbb{P}$-martingale.

Recall (see [§ The Stochastic Exponential](../martingale/stochastic_exponential.md)): for a continuous local martingale $M_t = -\int_0^t \theta_s\,dW_s$, the Doléans-Dade exponential $\mathcal{E}(M)_t = \exp(M_t - \tfrac{1}{2}\langle M\rangle_t)$ satisfies the driftless SDE

$$
\boxed{dZ_t = -Z_t\theta_t\,dW_t}
$$

so $Z_t$ is automatically a $\mathbb{P}$-local martingale. Recall (see [§ Novikov and Kazamaki Conditions](../martingale/novikov_kazamaki_conditions.md)): the Novikov condition $\mathbb{E}^{\mathbb{P}}[\exp(\tfrac{1}{2}\int_0^T \theta_s^2\,ds)] < \infty$ promotes this local martingale to a true martingale with $\mathbb{E}^{\mathbb{P}}[Z_t] = 1$ for all $t$.

---

## Step 2: The Shifted Process is a Q-Martingale

**Goal:** Show that $\widetilde{W}_t = W_t + \int_0^t \theta_s\,ds$ is a continuous local martingale under $\mathbb{Q}$.

**Method:** The abstract Bayes rule relates $\mathbb{Q}$-conditional expectations to $\mathbb{P}$-conditional expectations weighted by the density:

$$
\mathbb{E}^{\mathbb{Q}}[X_t | \mathcal{F}_s] = \frac{\mathbb{E}^{\mathbb{P}}[X_t Z_T | \mathcal{F}_s]}{Z_s}
$$

where the denominator simplifies to $Z_s$ by the martingale property of $Z_t$. The key step is to show that $\widetilde{W}_t Z_t$ is a $\mathbb{P}$-martingale (which implies $\widetilde{W}_t$ is a $\mathbb{Q}$-martingale). This is verified by the Itô product rule in the [cancellation mechanism](#key-insight-the-cancellation-mechanism) below: the $dt$ contributions from the drift in $\widetilde{W}_t$ and from the cross-variation $d\langle \widetilde{W}, Z\rangle_t$ cancel exactly.

**Result:** $\widetilde{W}_t$ is a **continuous $\mathbb{Q}$-local martingale**.

---

## Step 3: Quadratic Variation is Measure-Invariant

Since:

$$
\widetilde{W}_t = W_t + \int_0^t \theta_s\,ds
$$

and the integral term has **finite variation** (in particular, absolutely continuous):

$$
d\langle\widetilde{W}\rangle_t = d\langle W\rangle_t = dt
$$

Therefore $\langle\widetilde{W}\rangle_t = t$.

---

## Step 4: Lévy Characterization Theorem

**Theorem (Lévy):** A continuous local martingale $M_t$ with quadratic variation $\langle M\rangle_t = t$ is a standard Brownian motion.

**Application:** We have shown:

1. $\widetilde{W}_t$ is continuous (sum of continuous processes)
2. $\widetilde{W}_t$ is a continuous $\mathbb{Q}$-local martingale (Step 2)
3. $\langle\widetilde{W}\rangle_t = t$ (Step 3)

By Lévy's theorem:

$$
\boxed{\widetilde{W}_t \text{ is a standard Brownian motion under } \mathbb{Q}}
$$

---

## Step 5: Alternative Derivation Using Change of Variables (Optional)

Another approach uses direct computation. This is most transparent when $\theta$ is constant; for general adapted $\theta_t$, the characteristic-function argument does not generalize (use Steps 2–4 instead).

**Key formula:** For a continuous $\mathbb{Q}$-local martingale $M_t$ with $\langle M\rangle_t = t$, the process must be Brownian (Lévy's characterization).

We can verify this by computing the characteristic function (shown here for constant $\theta$):

$$
\mathbb{E}^{\mathbb{Q}}[e^{i\lambda\widetilde{W}_t}] = e^{-\lambda^2 t/2}
$$

This matches the characteristic function of $\mathcal{N}(0, t)$, confirming that $\widetilde{W}_t$ is a standard Brownian motion. For general adapted $\theta_t$, Levy's characterization (Steps 3-5) is the standard route.

!!! warning "Constant θ only"
    The characteristic function argument above applies when $\theta$ is constant. For general adapted $\theta_t$, the proof requires the full machinery of stochastic exponentials and Lévy's characterization theorem — the direct computation does not generalize.

---

## Summary of the Proof Strategy

| Step | What we prove | Why it's needed |
|------|---------------|-----------------|
| 1 | $Z_t$ is a $\mathbb{P}$-martingale with $\mathbb{E}[Z_t]=1$ | Defines a valid probability measure $\mathbb{Q}$ |
| 2 | $\widetilde{W}_t$ is a continuous $\mathbb{Q}$-local martingale | Necessary property of Brownian motion |
| 3 | $\langle\widetilde{W}\rangle_t = t$ | Identifies the volatility as unit constant |
| 4 | Apply Lévy's theorem | Concludes $\widetilde{W}_t$ is Brownian motion |

---

## Key Insight: The Cancellation Mechanism

Recall the two SDEs in play:

$$
d\widetilde{W}_t = dW_t + \theta_t\,dt, \qquad dZ_t = -Z_t\theta_t\,dW_t
$$

Itô's product rule gives:

$$
d(\widetilde{W}_t Z_t)
= Z_t\,d\widetilde{W}_t + \widetilde{W}_t\,dZ_t + d\langle \widetilde{W}, Z \rangle_t
$$

Expanding each term:

| Term | Expands to | $dt$ part | $dW_t$ part |
|------|-----------|-----------|-------------|
| $Z_t\,d\widetilde{W}_t$ | $Z_t\,dW_t + Z_t\theta_t\,dt$ | $+Z_t\theta_t\,dt$ | $Z_t\,dW_t$ |
| $\widetilde{W}_t\,dZ_t$ | $-\widetilde{W}_t Z_t\theta_t\,dW_t$ | $0$ | $-\widetilde{W}_t Z_t\theta_t\,dW_t$ |
| $d\langle \widetilde{W}, Z \rangle_t$ | $(dW_t)(-Z_t\theta_t\,dW_t) = -Z_t\theta_t\,dt$ | $-Z_t\theta_t\,dt$ | $0$ |

Summing the $dt$ column: $+Z_t\theta_t\,dt - Z_t\theta_t\,dt = 0$.

The two $dt$ contributions are:

- **$+Z_t\theta_t\,dt$** comes from the drift $\theta_t\,dt$ baked into $\widetilde{W}_t = W_t + \int\theta\,ds$
- **$-Z_t\theta_t\,dt$** comes from the cross-variation $d\langle \widetilde{W}, Z\rangle_t$, which is non-zero precisely because $Z_t$ was constructed with the $-\theta_t\,dW_t$ term

These two cancel to give:

$$
d(\widetilde{W}_t Z_t) = \bigl(Z_t - \widetilde{W}_t Z_t \theta_t\bigr)\,dW_t
$$

No $dt$ term survives, so $\widetilde{W}_t Z_t$ is a $\mathbb{P}$-martingale, and $\widetilde{W}_t$ is a $\mathbb{Q}$-martingale.

---

Recall (see [§ Novikov and Kazamaki Conditions](../martingale/novikov_kazamaki_conditions.md)): without Novikov, $Z_t$ is only a supermartingale with $\mathbb{E}^{\mathbb{P}}[Z_T] \le 1$, and the measure change may fail.

---

!!! note "Filtration is preserved"
    The measure change from $\mathbb{P}$ to $\mathbb{Q}$ does not alter the filtration $\{\mathcal{F}_t\}$. Adaptedness is a pathwise property: a process $X_t$ is $\mathcal{F}_t$-measurable if and only if it depends only on the history up to time $t$. Since equivalent measure changes do not alter the sample space or the sigma-algebras, every adapted process under $\mathbb{P}$ remains adapted under $\mathbb{Q}$.

---

## Exercises

**Exercise 1.**
Let $\theta$ be a constant. Apply Ito's lemma to $Z_t = \exp(-\theta W_t - \frac{1}{2}\theta^2 t)$ and verify that $dZ_t = -\theta Z_t\,dW_t$. Explain why the absence of a $dt$ term guarantees that $Z_t$ is a local martingale.

??? success "Solution to Exercise 1"
    Let $\theta$ be constant and $Z_t = \exp(-\theta W_t - \frac{1}{2}\theta^2 t)$. Write $Z_t = e^{f(W_t, t)}$ where $f(x, t) = -\theta x - \frac{1}{2}\theta^2 t$.

    By Itô's lemma applied to $Z_t = e^{f(W_t, t)}$:

    $$
    dZ_t = \frac{\partial Z_t}{\partial t}\,dt + \frac{\partial Z_t}{\partial W_t}\,dW_t + \frac{1}{2}\frac{\partial^2 Z_t}{\partial W_t^2}\,(dW_t)^2
    $$

    Computing the partial derivatives:

    $$
    \frac{\partial Z_t}{\partial t} = -\frac{1}{2}\theta^2 Z_t, \qquad \frac{\partial Z_t}{\partial W_t} = -\theta Z_t, \qquad \frac{\partial^2 Z_t}{\partial W_t^2} = \theta^2 Z_t
    $$

    Substituting and using $(dW_t)^2 = dt$:

    $$
    dZ_t = -\frac{1}{2}\theta^2 Z_t\,dt + (-\theta Z_t)\,dW_t + \frac{1}{2}\theta^2 Z_t\,dt
    $$

    $$
    = -\theta Z_t\,dW_t + \left(-\frac{1}{2}\theta^2 + \frac{1}{2}\theta^2\right)Z_t\,dt
    $$

    $$
    = -\theta Z_t\,dW_t
    $$

    The $dt$ terms cancel exactly, leaving $dZ_t = -\theta Z_t\,dW_t$.

    The absence of a $dt$ term means $Z_t$ has no drift, which is precisely the defining property of a local martingale. A process whose stochastic differential contains only $dW_t$ terms and no $dt$ terms is a local martingale because its conditional expectation satisfies $\mathbb{E}[Z_{t+h} - Z_t | \mathcal{F}_t] \approx 0$ (the Itô integral has zero expectation). The Novikov condition then promotes this local martingale to a true martingale.

---

**Exercise 2.**
In Step 2 of the proof, the change-of-measure formula states

$$
\mathbb{E}^{\mathbb{Q}}[X_t | \mathcal{F}_s] = \frac{\mathbb{E}^{\mathbb{P}}[X_t Z_T | \mathcal{F}_s]}{Z_s}
$$

Explain why the denominator is $Z_s$ rather than $Z_T$. What property of $Z_t$ makes this valid?

??? success "Solution to Exercise 2"
    The change-of-measure formula states:

    $$
    \mathbb{E}^{\mathbb{Q}}[X_t | \mathcal{F}_s] = \frac{\mathbb{E}^{\mathbb{P}}[X_t Z_T | \mathcal{F}_s]}{Z_s}
    $$

    The denominator is $Z_s$ rather than $Z_T$ because of the **tower property** combined with the **martingale property** of $Z_t$.

    Since $Z_t$ is a $\mathbb{P}$-martingale, we have $\mathbb{E}^{\mathbb{P}}[Z_T | \mathcal{F}_s] = Z_s$. This is the key property that allows us to replace $Z_T$ by $Z_s$ in the denominator. Formally, the derivation proceeds as follows. For any $A \in \mathcal{F}_s$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\mathbf{1}_A X_t] = \mathbb{E}^{\mathbb{P}}[\mathbf{1}_A X_t Z_T]
    $$

    We want to express $\mathbb{E}^{\mathbb{Q}}[X_t | \mathcal{F}_s]$ in terms of a $\mathbb{P}$-conditional expectation. The abstract Bayes formula for conditional expectations under a change of measure gives:

    $$
    \mathbb{E}^{\mathbb{Q}}[X_t | \mathcal{F}_s] = \frac{\mathbb{E}^{\mathbb{P}}[X_t Z_T | \mathcal{F}_s]}{\mathbb{E}^{\mathbb{P}}[Z_T | \mathcal{F}_s]} = \frac{\mathbb{E}^{\mathbb{P}}[X_t Z_T | \mathcal{F}_s]}{Z_s}
    $$

    The final equality uses precisely the martingale property $\mathbb{E}^{\mathbb{P}}[Z_T | \mathcal{F}_s] = Z_s$. Without this property, the formula would not simplify, and the denominator would remain as the conditional expectation of $Z_T$, which would depend on the specific event and not factor out cleanly.

---

**Exercise 3.**
Levy's characterization theorem states that a continuous local martingale with quadratic variation $\langle M \rangle_t = t$ is a standard Brownian motion. Explain why both conditions (continuity and unit quadratic variation) are necessary. Give an example of a continuous martingale whose quadratic variation is not $t$ and is therefore not a Brownian motion.

??? success "Solution to Exercise 3"
    Lévy's characterization requires **both** conditions:

    1. **Continuity:** The process must have continuous sample paths.
    2. **Unit quadratic variation:** $\langle M \rangle_t = t$.

    Both are necessary because:

    - A continuous martingale can have quadratic variation different from $t$. In that case, it is a time-changed Brownian motion but not a standard Brownian motion.
    - A process with $\langle M \rangle_t = t$ that is not continuous could be a jump process.

    **Example of a continuous martingale that is not Brownian:** Let $B_t$ be a standard Brownian motion and define $M_t = \sigma B_t$ for some constant $\sigma \neq 1$. Then $M_t$ is a continuous martingale (since $B_t$ is), but its quadratic variation is:

    $$
    \langle M \rangle_t = \sigma^2 \langle B \rangle_t = \sigma^2 t \neq t
    $$

    So $M_t$ is not a Brownian motion. It is a scaled Brownian motion with the wrong volatility.

    Another example: let $M_t = B_{t^2}$ (Brownian motion evaluated at $t^2$). This is a continuous martingale (in a suitably defined filtration), but $\langle M \rangle_t = t^2 \neq t$, so it is not a standard Brownian motion. It can, however, be represented as a time-changed Brownian motion.

---

**Exercise 4.**
Consider the process $\widetilde{W}_t = W_t + \int_0^t \theta_s\,ds$. Show that the integral $\int_0^t \theta_s\,ds$ has zero quadratic variation, and conclude that $\langle \widetilde{W} \rangle_t = \langle W \rangle_t = t$. Why does this step rely on the fact that the integral is a finite-variation process?

??? success "Solution to Exercise 4"
    The process $\widetilde{W}_t = W_t + \int_0^t \theta_s\,ds$ is the sum of a Brownian motion and a finite-variation process.

    **Quadratic variation of the integral term:** Let $A_t = \int_0^t \theta_s\,ds$. This is a process of **bounded (finite) variation** on $[0, T]$ because, for any partition $0 = t_0 < t_1 < \cdots < t_n = T$:

    $$
    \sum_{k=0}^{n-1} |A_{t_{k+1}} - A_{t_k}| = \sum_{k=0}^{n-1} \left|\int_{t_k}^{t_{k+1}} \theta_s\,ds\right| \leq \int_0^T |\theta_s|\,ds < \infty
    $$

    A fundamental property of quadratic variation is that **any finite-variation process has zero quadratic variation**. This is because:

    $$
    \sum_{k=0}^{n-1} (A_{t_{k+1}} - A_{t_k})^2 \leq \max_k |A_{t_{k+1}} - A_{t_k}| \cdot \sum_{k=0}^{n-1} |A_{t_{k+1}} - A_{t_k}|
    $$

    As the partition mesh goes to zero, the maximum increment $\max_k |A_{t_{k+1}} - A_{t_k}| \to 0$ (by continuity of $A$), while the total variation sum remains bounded. Therefore the quadratic variation sum converges to zero: $\langle A \rangle_t = 0$.

    For the quadratic variation of $\widetilde{W}_t$:

    $$
    \langle \widetilde{W} \rangle_t = \langle W + A \rangle_t = \langle W \rangle_t + 2\langle W, A \rangle_t + \langle A \rangle_t
    $$

    The cross-variation $\langle W, A \rangle_t = 0$ because $A$ has finite variation (the cross-variation of a continuous semimartingale with a finite-variation process is always zero). Since $\langle A \rangle_t = 0$ as well:

    $$
    \langle \widetilde{W} \rangle_t = \langle W \rangle_t = t
    $$

---

**Exercise 5.**
Suppose the Novikov condition fails, meaning $\mathbb{E}^{\mathbb{P}}[\exp(\frac{1}{2}\int_0^T \theta_s^2\,ds)] = \infty$. Explain why $Z_t$ may still be a local martingale but could fail to be a true martingale. What goes wrong with the measure change in this case? State the consequence for $\mathbb{E}^{\mathbb{P}}[Z_T]$.

??? success "Solution to Exercise 5"
    When the Novikov condition fails, the exponential process $Z_t = \exp(-\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds)$ is still a **non-negative local martingale** under $\mathbb{P}$ (this follows from the Itô computation $dZ_t = -Z_t\theta_t\,dW_t$, which has no drift term, regardless of whether the Novikov condition holds).

    However, a non-negative local martingale is always a **supermartingale** (by Fatou's lemma), meaning:

    $$
    \mathbb{E}^{\mathbb{P}}[Z_T | \mathcal{F}_s] \leq Z_s
    $$

    In particular, $\mathbb{E}^{\mathbb{P}}[Z_T] \leq Z_0 = 1$. Without the Novikov condition, strict inequality can occur:

    $$
    \mathbb{E}^{\mathbb{P}}[Z_T] < 1
    $$

    This means the "measure" $\mathbb{Q}$ defined by $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T} = Z_T$ satisfies $\mathbb{Q}(\Omega) = \mathbb{E}^{\mathbb{P}}[Z_T] < 1$, so $\mathbb{Q}$ is not a valid probability measure (it does not assign total mass 1 to the sample space). Some probability "leaks" to infinity.

    Intuitively, when $\theta_s$ can become very large, the exponential martingale $Z_t$ can spend extended periods near zero, causing its expectation to drop below 1. The "lost mass" corresponds to paths along which $Z_t$ collapses toward zero. The Novikov condition prevents this by ensuring $\theta_s$ does not grow too fast, keeping $Z_t$ well-behaved enough to be a true martingale with unit expectation.

---

**Exercise 6.**
The Radon–Nikodym derivative is $Z_t = \exp(-\theta W_t - \frac{1}{2}\theta^2 t)$. Explain why the correction term $-\frac{1}{2}\theta^2 t$ is absolutely necessary. What goes wrong if you define $\hat{Z}_t = \exp(-\theta W_t)$ instead?

??? success "Solution to Exercise 6"
    Apply Itô's lemma to $\hat{Z}_t = \exp(-\theta W_t)$. Writing $\hat{Z}_t = e^{f(W_t)}$ with $f(x) = -\theta x$:

    $$
    d\hat{Z}_t = -\theta\hat{Z}_t\,dW_t + \frac{1}{2}\theta^2\hat{Z}_t\,dt
    $$

    The $dt$ term $\frac{1}{2}\theta^2\hat{Z}_t\,dt$ does not vanish. This means $\hat{Z}_t$ is **not** a local martingale — it has a positive drift. Consequently:

    - $\mathbb{E}^{\mathbb{P}}[\hat{Z}_T] = e^{\frac{1}{2}\theta^2 T} \neq 1$, so $\hat{Z}_T$ cannot define a valid probability measure.
    - The measure defined by normalizing $\hat{Z}_T$ would not produce the correct Brownian shift — the resulting shifted process would not be a standard Brownian motion under the new measure.

    The correction $-\frac{1}{2}\theta^2 t$ is precisely the Itô correction that cancels this unwanted drift. With $Z_t = \exp(-\theta W_t - \frac{1}{2}\theta^2 t)$:

    $$
    dZ_t = -\theta Z_t\,dW_t
    $$

    No $dt$ term survives, making $Z_t$ a local martingale with $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$. This is the defining property of the **stochastic exponential**: the $-\frac{1}{2}\theta^2 t$ term is the price of working with exponentials in Itô calculus, where the chain rule picks up an extra second-derivative (quadratic variation) term that must be compensated.
