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

**Key observation:** There is **no $dt$ term**, only the $dW_t$ term. This is the defining property of a martingale!

Since $Z_t$ has no drift and is adapted to the filtration, it is a local martingale. The **Novikov condition** ensures it is a **true martingale** with:

$$
\mathbb{E}^{\mathbb{P}}[Z_t] = \mathbb{E}^{\mathbb{P}}[Z_0] = 1
$$

---

## Step 2: Unit Expectation (Justification)

For $X_t = -\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds$, the random variable $X_t$ is Gaussian:

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

## Step 3: The Shifted Process is a $\mathbb{Q}$-Martingale

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

The key step involves showing that the $dW$ term and the measure change $Z_T$ cancel exactly, leaving only a martingale in $t$. More precisely, under the conditional expectation, the drift from the integral is exactly compensated by the likelihood reweighting from $Z_T$.

**Result:** $\widetilde{W}_t$ is a **$\mathbb{Q}$-martingale**.

---

## Step 4: Quadratic Variation is Measure-Invariant

**Key principle:** Quadratic variation is a **pathwise property**—it depends only on the paths of the process, not on the probability measure used.

Since:

$$
\widetilde{W}_t = W_t + \int_0^t \theta_s\,ds
$$

and the integral term has **finite variation** (it's a deterministic or adapted process with finite $L^2$ norm):

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

Another approach uses direct computation. Under $\mathbb{Q}$, we want to show $\widetilde{W}_t$ is Brownian.

**Key formula:** For a $\mathbb{Q}$-martingale $M_t$ with $\langle M\rangle_t = t$, the process must be Brownian.

We can verify this by computing the characteristic function:

$$
\mathbb{E}^{\mathbb{Q}}[e^{i\lambda\widetilde{W}_t}] = e^{-\lambda^2 t/2}
$$

This matches the characteristic function of $\mathcal{N}(0, t)$, confirming that $\widetilde{W}_t$ is a standard Brownian motion.

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

The proof's elegance lies in a remarkable **cancellation**:

$$
Z_T \cdot \text{(drift from measure change)} = \text{(drift from } \theta \text{ term)}
$$

These two sources of drift, coming from different places, exactly cancel when we change measures. This is not coincidental—it's built into the definition of $Z_t$.

**Intuition:** The exponential martingale $Z_t$ is precisely constructed so that reweighting by $Z_T$ removes the drift $\theta$ from the Brownian motion. This is why Girsanov's theorem works so elegantly in practice.

---

## Technical Note: Novikov's Condition

The Novikov condition $\mathbb{E}^{\mathbb{P}}[\exp(\frac{1}{2}\int_0^T \theta_s^2\,ds)] < \infty$ is sufficient to guarantee:

1. $Z_t$ is a **true martingale** (not just a local martingale)
2. $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$
3. The measure change is valid

Without this condition, $Z_t$ may only be a local martingale, and the measure change may not define a valid probability measure.
