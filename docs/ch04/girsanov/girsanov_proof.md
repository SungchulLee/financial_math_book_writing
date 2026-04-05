# Proof Sketch and Key Ideas

This section develops the main ideas behind the proof of Girsanov's theorem systematically.

---

## Step 1: Verify the Exponential Martingale Property

**Goal:** Show that $Z_t = \exp\left(-\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)$ is a $\mathbb{P}$-martingale.

**Method:** Apply Itô's lemma to $Z_t = e^{X_t}$ where $X_t = -\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds$.

**Computing the differential:**

$$
dX_t = -\theta_t\,dW_t - \frac{1}{2}\theta_t^2\,dt
$$

Apply Itô to $f(X) = e^X$:

$$
dZ_t = e^{X_t}\,dX_t + \frac{1}{2}e^{X_t}(dX_t)^2
$$

Compute $(dX_t)^2$:

$$
(dX_t)^2 = \left(-\theta_t\,dW_t - \frac{1}{2}\theta_t^2\,dt\right)^2 = \theta_t^2\,(dW_t)^2 = \theta_t^2\,dt
$$

Therefore:

$$
dZ_t = Z_t\left(-\theta_t\,dW_t - \frac{1}{2}\theta_t^2\,dt\right) + \frac{1}{2}Z_t\,\theta_t^2\,dt
$$

$$
= -Z_t\theta_t\,dW_t - \frac{1}{2}Z_t\theta_t^2\,dt + \frac{1}{2}Z_t\theta_t^2\,dt
$$

$$
\boxed{dZ_t = -Z_t\theta_t\,dW_t}
$$

**Key observation:** There is **no $dt$ term**, only the $dW_t$ term. This shows $Z_t$ is a local martingale; the **Novikov condition** then ensures it is a true martingale.

Since $Z_t$ is a true martingale (by Novikov):

$$
\mathbb{E}^{\mathbb{P}}[Z_t] = \mathbb{E}^{\mathbb{P}}[Z_0] = 1
$$

---

## Step 2: Unit Expectation (Justification)

When $\theta_t$ is deterministic (or constant), $X_t = -\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds$ is Gaussian (since the Ito integral of a deterministic integrand is Gaussian):

$$
X_t \sim \mathcal{N}\left(-\frac{1}{2}\int_0^t \theta_s^2\,ds, \int_0^t \theta_s^2\,ds\right)
$$

For any Gaussian random variable $Y \sim \mathcal{N}(\mu, \sigma^2)$:

$$
\mathbb{E}[e^Y] = \exp\left(\mu + \frac{\sigma^2}{2}\right)
$$

Applying this with $\mu = -\frac{1}{2}\int_0^t \theta_s^2\,ds$ and $\sigma^2 = \int_0^t \theta_s^2\,ds$:

$$
\mathbb{E}^{\mathbb{P}}[Z_t] = \exp\left(-\frac{1}{2}\int_0^t \theta_s^2\,ds + \frac{1}{2}\int_0^t \theta_s^2\,ds\right) = 1 \quad \checkmark
$$

---

## Step 3: The Shifted Process is a Q-Martingale

**Goal:** Show that $\widetilde{W}_t = W_t + \int_0^t \theta_s\,ds$ is a martingale under $\mathbb{Q}$.

**Method:** Use the change-of-measure formula. For any $\mathcal{F}_t$-adapted process $X_t$:

$$
\mathbb{E}^{\mathbb{Q}}[X_t | \mathcal{F}_s] = \frac{\mathbb{E}^{\mathbb{P}}[X_t Z_T | \mathcal{F}_s]}{\mathbb{E}^{\mathbb{P}}[Z_T | \mathcal{F}_s]}
$$

For $s \leq t$, by the martingale property of $Z$:

$$
\mathbb{E}^{\mathbb{P}}[Z_T | \mathcal{F}_s] = Z_s
$$

Therefore, for the shifted Brownian motion:

$$
\mathbb{E}^{\mathbb{Q}}\left[\widetilde{W}_t | \mathcal{F}_s\right] = \frac{\mathbb{E}^{\mathbb{P}}\left[\left(W_t + \int_0^t \theta_u\,du\right) Z_T | \mathcal{F}_s\right]}{Z_s}
$$

By the martingale property and adapted property of $\theta$:

$$
= \frac{\mathbb{E}^{\mathbb{P}}\left[\left(W_t + \int_0^t \theta_u\,du\right) Z_T | \mathcal{F}_s\right]}{Z_s}
$$

The key step is to compute $d(\widetilde{W}_t Z_t)$ via the Ito product rule and verify that no $dt$ term survives. The explicit calculation (carried out in the [cancellation mechanism](#key-insight-the-cancellation-mechanism) section below) proceeds as:

1. Compute $d(\widetilde{W}_t Z_t) = Z_t\,d\widetilde{W}_t + \widetilde{W}_t\,dZ_t + d\langle \widetilde{W}, Z\rangle_t$
2. The $dt$ contributions $+Z_t\theta_t\,dt$ (from the drift in $\widetilde{W}_t$) and $-Z_t\theta_t\,dt$ (from the cross-variation) cancel exactly
3. Therefore $\widetilde{W}_t Z_t$ is a $\mathbb{P}$-martingale. Dividing by $Z_s$ in the conditional expectation (using Bayes' rule for conditional expectations under measure change) yields that $\widetilde{W}_t$ is a $\mathbb{Q}$-martingale

**Result:** $\widetilde{W}_t$ is a **$\mathbb{Q}$-martingale**.

---

## Step 4: Quadratic Variation is Measure-Invariant

**Key principle:** Quadratic variation is a **pathwise property**—it depends only on the paths of the process, not on the probability measure used.

Since:

$$
\widetilde{W}_t = W_t + \int_0^t \theta_s\,ds
$$

and the integral term has **finite variation** (in particular, absolutely continuous):

$$
d\langle\widetilde{W}\rangle_t = d\langle W\rangle_t = dt
$$

**Conclusion:** The quadratic variation of $\widetilde{W}_t$ equals $t$, the same as for standard Brownian motion.

---

## Step 5: Lévy Characterization Theorem

**Theorem (Lévy):** A continuous local martingale $M_t$ with quadratic variation $\langle M\rangle_t = t$ is a standard Brownian motion.

**Application:** We have shown:

1. $\widetilde{W}_t$ is continuous (sum of continuous processes)
2. $\widetilde{W}_t$ is a $\mathbb{Q}$-martingale (Step 3)
3. $\langle\widetilde{W}\rangle_t = t$ (Step 4)

By Lévy's theorem:

$$
\boxed{\widetilde{W}_t \text{ is a standard Brownian motion under } \mathbb{Q}}
$$

---

## Step 6: Alternative Derivation Using Change of Variables

Another approach uses direct computation. This derivation is most transparent when $\theta$ is constant; for general adapted $\theta_t$, the characteristic-function argument requires additional care. Under $\mathbb{Q}$, we want to show $\widetilde{W}_t$ is Brownian.

**Key formula:** For a $\mathbb{Q}$-martingale $M_t$ with $\langle M\rangle_t = t$, the process must be Brownian.

We can verify this by computing the characteristic function (shown here for constant $\theta$):

$$
\mathbb{E}^{\mathbb{Q}}[e^{i\lambda\widetilde{W}_t}] = e^{-\lambda^2 t/2}
$$

This matches the characteristic function of $\mathcal{N}(0, t)$, confirming that $\widetilde{W}_t$ is a standard Brownian motion. For general adapted $\theta_t$, Levy's characterization (Steps 3-5) is the standard route.

---

## Summary of the Proof Strategy

| Step | What we prove | Why it's needed |
|------|---------------|-----------------|
| 1 | $Z_t$ is a $\mathbb{P}$-martingale | To define the measure $\mathbb{Q}$ properly |
| 2 | $\mathbb{E}^{\mathbb{P}}[Z_t] = 1$ | Ensures $\mathbb{Q}$ is a probability measure |
| 3 | $\widetilde{W}_t$ is a $\mathbb{Q}$-martingale | Necessary property of Brownian motion |
| 4 | $d\langle\widetilde{W}\rangle_t = dt$ | Identifies the volatility as unit constant |
| 5 | Apply Lévy's theorem | Concludes $\widetilde{W}_t$ is Brownian motion |

---

## Key Insight: The Cancellation Mechanism

The proof's elegance lies in a concrete $dt$-cancellation that occurs inside the Itô product rule for $\widetilde{W}_t Z_t$.

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

No $dt$ term survives, so $\widetilde{W}_t Z_t$ is a $\mathbb{P}$-martingale, and $\widetilde{W}_t$ is a $\mathbb{Q}$-martingale. This cancellation is not coincidental — $Z_t$ is defined by $dZ_t = -Z_t\theta_t\,dW_t$ precisely so that its cross-variation with $\widetilde{W}_t$ kills the drift $\theta_t\,dt$ term.

---

## Technical Note: Novikov's Condition

The Novikov condition $\mathbb{E}^{\mathbb{P}}[\exp(\frac{1}{2}\int_0^T \theta_s^2\,ds)] < \infty$ is sufficient to guarantee:

1. $Z_t$ is a **true martingale** (not just a local martingale)
2. $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$
3. The measure change is valid

Without this condition, $Z_t$ may only be a local martingale, and the measure change may not define a valid probability measure.

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
For constant $\theta$, the exponent $X_t = -\theta W_t - \frac{1}{2}\theta^2 t$ is Gaussian with mean $-\frac{1}{2}\theta^2 t$ and variance $\theta^2 t$. Using the moment generating function of a Gaussian random variable, verify that $\mathbb{E}^{\mathbb{P}}[Z_t] = 1$ for all $t \geq 0$.

??? success "Solution to Exercise 2"
    For constant $\theta$, the exponent is $X_t = -\theta W_t - \frac{1}{2}\theta^2 t$. Since $W_t \sim \mathcal{N}(0, t)$ under $\mathbb{P}$:

    $$
    -\theta W_t \sim \mathcal{N}(0, \theta^2 t)
    $$

    Therefore:

    $$
    X_t = -\theta W_t - \frac{1}{2}\theta^2 t \sim \mathcal{N}\!\left(-\frac{1}{2}\theta^2 t,\; \theta^2 t\right)
    $$

    with mean $\mu_X = -\frac{1}{2}\theta^2 t$ and variance $\sigma_X^2 = \theta^2 t$.

    For a Gaussian random variable $Y \sim \mathcal{N}(\mu, \sigma^2)$, the moment generating function gives:

    $$
    \mathbb{E}[e^Y] = \exp\!\left(\mu + \frac{\sigma^2}{2}\right)
    $$

    Applying this to $Z_t = e^{X_t}$:

    $$
    \mathbb{E}^{\mathbb{P}}[Z_t] = \exp\!\left(-\frac{1}{2}\theta^2 t + \frac{\theta^2 t}{2}\right) = \exp(0) = 1
    $$

    This holds for all $t \geq 0$, confirming the unit expectation property of the exponential martingale.

---

**Exercise 3.**
In Step 3 of the proof, the change-of-measure formula states

$$
\mathbb{E}^{\mathbb{Q}}[X_t | \mathcal{F}_s] = \frac{\mathbb{E}^{\mathbb{P}}[X_t Z_T | \mathcal{F}_s]}{Z_s}
$$

Explain why the denominator is $Z_s$ rather than $Z_T$. What property of $Z_t$ makes this valid?

??? success "Solution to Exercise 3"
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

**Exercise 4.**
Levy's characterization theorem states that a continuous local martingale with quadratic variation $\langle M \rangle_t = t$ is a standard Brownian motion. Explain why both conditions (continuity and unit quadratic variation) are necessary. Give an example of a continuous martingale whose quadratic variation is not $t$ and is therefore not a Brownian motion.

??? success "Solution to Exercise 4"
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

**Exercise 5.**
Consider the process $\widetilde{W}_t = W_t + \int_0^t \theta_s\,ds$. Show that the integral $\int_0^t \theta_s\,ds$ has zero quadratic variation, and conclude that $\langle \widetilde{W} \rangle_t = \langle W \rangle_t = t$. Why does this step rely on the fact that the integral is a finite-variation process?

??? success "Solution to Exercise 5"
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

**Exercise 6.**
Suppose the Novikov condition fails, meaning $\mathbb{E}^{\mathbb{P}}[\exp(\frac{1}{2}\int_0^T \theta_s^2\,ds)] = \infty$. Explain why $Z_t$ may still be a local martingale but could fail to be a true martingale. What goes wrong with the measure change in this case? State the consequence for $\mathbb{E}^{\mathbb{P}}[Z_T]$.

??? success "Solution to Exercise 6"
    When the Novikov condition fails, the exponential process $Z_t = \exp(-\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds)$ is still a **non-negative local martingale** under $\mathbb{P}$ (this follows from the Itô computation $dZ_t = -Z_t\theta_t\,dW_t$, which has no drift term, regardless of whether the Novikov condition holds).

    However, a non-negative local martingale is always a **supermartingale** (by Fatou's lemma), meaning:

    $$
    \mathbb{E}^{\mathbb{P}}[Z_T | \mathcal{F}_s] \leq Z_s
    $$

    In particular, $\mathbb{E}^{\mathbb{P}}[Z_T] \leq Z_0 = 1$. Without the Novikov condition, strict inequality can occur:

    $$
    \mathbb{E}^{\mathbb{P}}[Z_T] < 1
    $$

    This means the "measure" $\mathbb{Q}$ defined by $d\mathbb{Q}/d\mathbb{P} = Z_T$ satisfies $\mathbb{Q}(\Omega) = \mathbb{E}^{\mathbb{P}}[Z_T] < 1$, so $\mathbb{Q}$ is not a valid probability measure (it does not assign total mass 1 to the sample space). Some probability "leaks" to infinity.

    Intuitively, when $\theta_s$ can become very large, the exponential martingale $Z_t$ can spend extended periods near zero, causing its expectation to drop below 1. The "lost mass" corresponds to paths along which $Z_t$ collapses toward zero. The Novikov condition prevents this by ensuring $\theta_s$ does not grow too fast, keeping $Z_t$ well-behaved enough to be a true martingale with unit expectation.

---

**Exercise 7.**
Verify the characteristic function computation in Step 6: show that $\mathbb{E}^{\mathbb{Q}}[e^{i\lambda \widetilde{W}_t}] = e^{-\lambda^2 t / 2}$ for constant $\theta$. Start from the definition $\mathbb{E}^{\mathbb{Q}}[e^{i\lambda \widetilde{W}_t}] = \mathbb{E}^{\mathbb{P}}[e^{i\lambda \widetilde{W}_t} Z_T]$ and use the fact that $\widetilde{W}_t = W_t + \theta t$ and $Z_T = \exp(-\theta W_T - \frac{1}{2}\theta^2 T)$.

??? success "Solution to Exercise 7"
    We want to compute $\mathbb{E}^{\mathbb{Q}}[e^{i\lambda \widetilde{W}_t}]$ for constant $\theta$. By definition of the $\mathbb{Q}$-expectation:

    $$
    \mathbb{E}^{\mathbb{Q}}[e^{i\lambda \widetilde{W}_t}] = \mathbb{E}^{\mathbb{P}}[e^{i\lambda \widetilde{W}_t} Z_T]
    $$

    Substituting $\widetilde{W}_t = W_t + \theta t$ and $Z_T = \exp(-\theta W_T - \frac{1}{2}\theta^2 T)$:

    $$
    = \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(i\lambda(W_t + \theta t) - \theta W_T - \frac{1}{2}\theta^2 T\right)\right]
    $$

    $$
    = e^{i\lambda\theta t - \frac{1}{2}\theta^2 T} \cdot \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(i\lambda W_t - \theta W_T\right)\right]
    $$

    Since $W_T = W_t + (W_T - W_t)$ and $W_t$ is independent of $W_T - W_t$ under $\mathbb{P}$:

    $$
    = e^{i\lambda\theta t - \frac{1}{2}\theta^2 T} \cdot \mathbb{E}^{\mathbb{P}}\!\left[e^{(i\lambda - \theta)W_t}\right] \cdot \mathbb{E}^{\mathbb{P}}\!\left[e^{-\theta(W_T - W_t)}\right]
    $$

    Using the moment generating function of Gaussian variables, $W_t \sim \mathcal{N}(0, t)$ and $W_T - W_t \sim \mathcal{N}(0, T-t)$:

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[e^{(i\lambda - \theta)W_t}\right] = \exp\!\left(\frac{(i\lambda - \theta)^2 t}{2}\right) = \exp\!\left(\frac{(-\lambda^2 - 2i\lambda\theta + \theta^2)t}{2}\right)
    $$

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[e^{-\theta(W_T - W_t)}\right] = \exp\!\left(\frac{\theta^2(T-t)}{2}\right)
    $$

    Combining all factors:

    $$
    \mathbb{E}^{\mathbb{Q}}[e^{i\lambda\widetilde{W}_t}] = \exp\!\left(i\lambda\theta t - \frac{\theta^2 T}{2} + \frac{(-\lambda^2 - 2i\lambda\theta + \theta^2)t}{2} + \frac{\theta^2(T-t)}{2}\right)
    $$

    Collecting terms in the exponent:

    $$
    = i\lambda\theta t - \frac{\theta^2 T}{2} - \frac{\lambda^2 t}{2} - i\lambda\theta t + \frac{\theta^2 t}{2} + \frac{\theta^2 T}{2} - \frac{\theta^2 t}{2}
    $$

    The terms $i\lambda\theta t$ cancel, $-\frac{\theta^2 T}{2} + \frac{\theta^2 T}{2}$ cancel, and $\frac{\theta^2 t}{2} - \frac{\theta^2 t}{2}$ cancel, leaving:

    $$
    \mathbb{E}^{\mathbb{Q}}[e^{i\lambda\widetilde{W}_t}] = e^{-\lambda^2 t/2}
    $$

    This is the characteristic function of $\mathcal{N}(0, t)$, confirming that $\widetilde{W}_t$ is a standard Brownian motion under $\mathbb{Q}$.
