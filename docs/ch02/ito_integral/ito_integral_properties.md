# Properties of the Itô Integral

Having constructed the Itô integral \(\int_0^t H_s \, dB_s\) for adapted square-integrable processes, we now establish its fundamental properties. These properties—linearity, martingale structure, path continuity, and quadratic variation—form the foundation for stochastic calculus and reveal the deep connection between integration and martingale theory.

---

## Linearity

The Itô integral is linear in the integrand.

**Theorem (Linearity)**: Let \(H, K \in \mathcal{L}^2([0,T])\) and \(\alpha, \beta \in \mathbb{R}\). Then:


$$
\boxed{
\int_0^t (\alpha H_s + \beta K_s) \, dB_s
= \alpha \int_0^t H_s \, dB_s + \beta \int_0^t K_s \, dB_s
}
$$



**Proof**: Linearity holds by definition for simple processes. Since simple processes are dense in \(\mathcal{L}^2([0,T])\) and the integral extends by continuity, linearity passes to the limit. \(\square\)

**Remark**: Unlike Riemann integration, the Itô integral is **not** linear in the integrator \(B_t\). The quadratic variation structure means that stochastic integrals with respect to different Brownian motions cannot be simply combined.

---

## Martingale property

The Itô integral defines a martingale with respect to the natural filtration.

**Theorem (Martingale Property)**: Let \(H \in \mathcal{L}^2([0,T])\). Then the process:


$$
I_t := \int_0^t H_s \, dB_s, \quad 0 \le t \le T
$$



is a **continuous martingale** with respect to \(\{\mathcal{F}_t\}\).

**Proof**: We verify the three conditions for a martingale.

**1. Adaptedness**: For each \(t\), \(I_t\) is defined as an \(L^2\)-limit of integrals of simple processes, each of which is \(\mathcal{F}_t\)-measurable. Therefore, \(I_t\) is \(\mathcal{F}_t\)-measurable.

**2. Integrability**: By the Itô isometry:


$$
\mathbb{E}[I_t^2]
= \mathbb{E}\left[\int_0^t H_s^2 \, ds\right]
\le \mathbb{E}\left[\int_0^T H_s^2 \, ds\right]
< \infty
$$



Thus, \(\mathbb{E}[|I_t|] \le \sqrt{\mathbb{E}[I_t^2]} < \infty\).

**3. Martingale property**: For \(0 \le s < t \le T\), we must show:


$$
\mathbb{E}[I_t \mid \mathcal{F}_s] = I_s
$$



**Step 1**: For simple processes, this was verified in the construction (it follows from the independent increments property of Brownian motion and adaptedness of the integrand).

**Step 2**: For general \(H \in \mathcal{L}^2([0,T])\), approximate by simple processes \(H^{(n)} \to H\) in \(\mathcal{L}^2\). Then:


$$
I_t^{(n)} := \int_0^t H_s^{(n)} \, dB_s
\to I_t \quad \text{in } L^2(\Omega)
$$



Since \(I_t^{(n)}\) are martingales:


$$
\mathbb{E}[I_t^{(n)} \mid \mathcal{F}_s] = I_s^{(n)}
$$



Taking \(L^2\)-limits (conditional expectation is continuous in \(L^2\)):


$$
\mathbb{E}[I_t \mid \mathcal{F}_s]
= \lim_{n \to \infty} \mathbb{E}[I_t^{(n)} \mid \mathcal{F}_s]
= \lim_{n \to \infty} I_s^{(n)}
= I_s
$$



This completes the proof. \(\square\)

**Corollary (Zero Mean)**: For all \(t \ge 0\):


$$
\mathbb{E}\left[\int_0^t H_s \, dB_s\right] = 0
$$



**Proof**: Taking expectations in the martingale property at \(s = 0\):


$$
\mathbb{E}[I_t] = \mathbb{E}[\mathbb{E}[I_t \mid \mathcal{F}_0]] = \mathbb{E}[I_0] = 0
$$



since \(I_0 = \int_0^0 H_s dB_s = 0\). \(\square\)

---

## Path continuity

Unlike general semimartingales, the Itô integral with respect to Brownian motion has **continuous sample paths**.

**Theorem (Continuity)**: Let \(H \in \mathcal{L}^2([0,T])\). Then the process:


$$
I_t = \int_0^t H_s \, dB_s
$$



has a **continuous modification**. That is, there exists a continuous process \(\tilde{I}_t\) such that:


$$
\mathbb{P}(I_t = \tilde{I}_t \text{ for all } t \in [0,T]) = 1
$$



**Proof (Sketch)**: The proof uses the **Kolmogorov continuity criterion**.

**Step 1**: Establish a moment bound. For \(s < t\):


$$
\mathbb{E}[|I_t - I_s|^4]
= \mathbb{E}\left[\left(\int_s^t H_u \, dB_u\right)^4\right]
$$



Using **Burkholder-Davis-Gundy inequality** (BDG inequality) for martingales:


$$
\mathbb{E}\left[\sup_{u \le t} |I_u|^4\right]
\le C \mathbb{E}\left[\left(\int_0^t H_s^2 \, ds\right)^2\right]
$$



This gives, for \(s < t\):


$$
\mathbb{E}[|I_t - I_s|^4]
\le C (t - s)^2 \mathbb{E}\left[\sup_{u \le T} H_u^4\right]
$$



under appropriate regularity conditions on \(H\).

**Step 2**: Apply Kolmogorov's criterion. Since:


$$
\mathbb{E}[|I_t - I_s|^4] \le K |t - s|^{1 + \varepsilon}
$$



for some \(\varepsilon > 0\), Kolmogorov's theorem guarantees the existence of a continuous modification.

**Alternative approach**: For simple processes, the integral is manifestly continuous (finite sums of continuous functions). The general case follows by \(L^2\)-approximation and a diagonal argument. \(\square\)

**Remark**: Continuity is a special feature of integration with respect to Brownian motion. For Poisson processes or jump diffusions, stochastic integrals have jumps.

---

## Quadratic variation

The quadratic variation of the Itô integral reveals its fundamental stochastic nature.

**Theorem (Quadratic Variation)**: Let \(H \in \mathcal{L}^2([0,T])\). Then the quadratic variation of \(I_t = \int_0^t H_s dB_s\) is:


$$
\boxed{
[I, I]_t = \int_0^t H_s^2 \, ds
}
$$



**Proof (Heuristic)**: Consider a partition \(\pi: 0 = t_0 < t_1 < \cdots < t_n = t\). The quadratic variation is:


$$
[I, I]_t
= \lim_{|\pi| \to 0} \sum_{i=0}^{n-1} (I_{t_{i+1}} - I_{t_i})^2
$$



Each increment is:


$$
I_{t_{i+1}} - I_{t_i}
= \int_{t_i}^{t_{i+1}} H_s \, dB_s
$$



For small intervals, \(H_s \approx H_{t_i}\) (assuming continuity), so:


$$
I_{t_{i+1}} - I_{t_i}
\approx H_{t_i} (B_{t_{i+1}} - B_{t_i})
$$



Therefore:


$$
(I_{t_{i+1}} - I_{t_i})^2
\approx H_{t_i}^2 (B_{t_{i+1}} - B_{t_i})^2
$$



Summing and using \([B, B]_t = t\):


$$
\sum_{i=0}^{n-1} (I_{t_{i+1}} - I_{t_i})^2
\approx \sum_{i=0}^{n-1} H_{t_i}^2 (B_{t_{i+1}} - B_{t_i})^2
\to \sum_{i=0}^{n-1} H_{t_i}^2 (t_{i+1} - t_i)
= \int_0^t H_s^2 \, ds
$$



**Rigorous proof**: Uses the convergence in probability:


$$
\sum_{i=0}^{n-1} (I_{t_{i+1}} - I_{t_i})^2
\xrightarrow{\mathbb{P}} \int_0^t H_s^2 \, ds
$$



which can be established via the Itô isometry and martingale moment bounds. \(\square\)

**Corollary**: The process:


$$
M_t := I_t^2 - \int_0^t H_s^2 \, ds
$$



is a martingale. This is a direct consequence of the Doob-Meyer decomposition: \(I_t^2\) is a submartingale, and its decomposition into a martingale plus an increasing process is:


$$
I_t^2 = M_t + \int_0^t H_s^2 \, ds
$$



---

## Itô isometry (revisited)

We established the Itô isometry during construction, but it's worth restating in full generality.

**Theorem (Itô Isometry)**: For \(H \in \mathcal{L}^2([0,T])\):


$$
\boxed{
\mathbb{E}\left[\left(\int_0^t H_s \, dB_s\right)^2\right]
= \mathbb{E}\left[\int_0^t H_s^2 \, ds\right]
}
$$



**Interpretation**: The Itô isometry provides a bridge between the stochastic integral (a random variable) and a deterministic integral of the squared integrand. It is the key to:

1. **Existence**: Ensuring the \(L^2\)-approximation procedure converges
2. **Uniqueness**: Guaranteeing the integral is well-defined
3. **Computation**: Calculating second moments and variances

**Generalization**: For two processes \(H, K \in \mathcal{L}^2([0,T])\):


$$
\mathbb{E}\left[\int_0^t H_s \, dB_s \cdot \int_0^t K_s \, dB_s\right]
= \mathbb{E}\left[\int_0^t H_s K_s \, ds\right]
$$



This follows from polarization of the Itô isometry.

---

## Connection to martingale theory

The Itô integral provides a **representation theorem** for certain martingales.

**Theorem (Martingale Representation - Preview)**: Every square-integrable martingale \(M_t\) adapted to the Brownian filtration \(\mathcal{F}_t = \sigma(B_s: s \le t)\) can be represented as:


$$
M_t = M_0 + \int_0^t H_s \, dB_s
$$



for some adapted process \(H \in \mathcal{L}^2([0,T])\).

**Intuition**: In a Brownian filtration, **all randomness comes from Brownian motion**. Any martingale is just a "reweighting" of Brownian increments via stochastic integration.

This result is fundamental in:

- **Option pricing**: Every hedging strategy can be represented as a stochastic integral
- **Filtering theory**: Optimal estimates are expressed as stochastic integrals
- **Stochastic control**: Value functions satisfy integral representations

We will not prove this theorem here, but it highlights the central role of the Itô integral in martingale theory.

---

## Local martingales and localization

For processes that are not globally square-integrable, we can define the Itô integral as a **local martingale**.

**Definition**: A process \(H\) is **locally in \(\mathcal{L}^2\)** if there exist stopping times \(\tau_n \uparrow \infty\) such that:


$$
\mathbb{E}\left[\int_0^{\tau_n \wedge T} H_s^2 \, ds\right] < \infty
\quad \text{for all } n
$$



For such \(H\), define:


$$
\int_0^t H_s \, dB_s
:= \lim_{n \to \infty} \int_0^{t \wedge \tau_n} H_s \, dB_s
$$



The resulting process is a **local martingale**: there exist stopping times \(\tau_n \uparrow \infty\) such that:


$$
I_{t \wedge \tau_n} = \int_0^{t \wedge \tau_n} H_s \, dB_s
$$



is a true martingale for each \(n\).

**Key difference**: Local martingales need not have constant expectation. For example:


$$
\mathbb{E}\left[\int_0^t e^{B_s} \, dB_s\right] = 0
$$



only holds locally, not globally, since \(e^{B_s}\) is not globally square-integrable.

---

## Summary of key properties

The Itô integral \(\int_0^t H_s dB_s\) satisfies:

1. **Linearity**: \(\int (\alpha H + \beta K) dB = \alpha \int H dB + \beta \int K dB\)

2. **Martingale property**: \(\mathbb{E}[\int_0^t H_s dB_s \mid \mathcal{F}_s] = \int_0^s H_u dB_u\)

3. **Zero mean**: \(\mathbb{E}[\int_0^t H_s dB_s] = 0\)

4. **Continuity**: Sample paths are continuous

5. **Quadratic variation**: \([\int H dB, \int H dB]_t = \int_0^t H_s^2 ds\)

6. **Itô isometry**: \(\mathbb{E}[(\int_0^t H_s dB_s)^2] = \mathbb{E}[\int_0^t H_s^2 ds]\)

7. **Martingale representation**: Every \(\mathcal{F}_t^B\)-martingale has the form \(M_0 + \int H dB\)

These properties distinguish the Itô integral from classical integration and reveal its deep connection to martingale theory. They form the foundation for:

- **Itô's formula** (the stochastic chain rule)
- **Stochastic differential equations**
- **Change of measure** (Girsanov's theorem)
- **Mathematical finance** (option pricing, hedging)

In the next section, we introduce **Itô processes**—stochastic processes defined by both deterministic drift and stochastic diffusion—which combine ordinary and stochastic integration into a unified framework.
