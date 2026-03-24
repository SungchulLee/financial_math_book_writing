# Characteristic Function of Affine Processes

The characteristic function is the primary analytical tool for pricing derivatives in affine models. Because affine processes have log-characteristic functions that are linear in the state, the characteristic function inherits a particularly tractable exponential-affine form. This section develops the characteristic function of affine processes, connects it to the Riccati ODE system, and establishes the properties that make Fourier-based pricing possible.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write the characteristic function of an affine process in exponential-affine form
    2. Connect the functions $\phi$ and $\psi$ to the generalized Riccati ODEs
    3. State the key analytic properties of the affine characteristic function
    4. Compute the characteristic function for specific one-dimensional models

---

## Intuition

The characteristic function $\Phi_X(v) = \mathbb{E}[e^{iv^\top X}]$ encodes the entire distribution of a random variable. For option pricing via Fourier inversion, we need the *conditional* characteristic function $\mathbb{E}[e^{iv^\top X_T} \mid X_t = x]$, which describes the distribution of the future state given the present. For a general stochastic process, computing this function requires solving a PDE. For an affine process, the exponential-affine structure of the log-moment generating function carries over directly: setting $u = iv$ in the log-affine property yields a characteristic function that is exponential-affine in $x$, with the same functions $\phi$ and $\psi$ evaluated at purely imaginary arguments.

---

## Definition and Basic Properties

### The Affine Characteristic Function

**Definition.** Let $(X_t)_{t \geq 0}$ be an affine process on $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$. The *conditional characteristic function* of $X_T$ given $X_t = x$ is

$$
\Phi(\tau, v, x) := \mathbb{E}\!\left[e^{i\langle v, X_T \rangle} \mid X_t = x\right] = \exp\!\left(\phi(\tau, iv) + \langle \psi(\tau, iv), x \rangle\right)
$$

where $\tau = T - t$, $v \in \mathbb{R}^d$, and $\phi$, $\psi$ are the functions from the log-affine expectation property evaluated at $u = iv$.

The initial conditions become:

$$
\phi(0, iv) = 0, \qquad \psi(0, iv) = iv
$$

At $\tau = 0$, the characteristic function reduces to $e^{i\langle v, x \rangle}$, which is the characteristic function of a point mass at $x$---as expected, since $X_t = x$ with certainty given $X_t = x$.

### Key Analytic Properties

The affine characteristic function inherits several important properties from general characteristic function theory, enhanced by the affine structure:

**Property 1 (Boundedness).** For all $\tau \geq 0$, $v \in \mathbb{R}^d$, and $x \in D$:

$$
|\Phi(\tau, v, x)| \leq 1
$$

This follows from $|\mathbb{E}[e^{i\langle v, X_T \rangle}]| \leq \mathbb{E}[|e^{i\langle v, X_T \rangle}|] = 1$.

**Property 2 (Hermitian symmetry).** $\Phi(\tau, -v, x) = \overline{\Phi(\tau, v, x)}$, so the characteristic function at $-v$ is the complex conjugate of the characteristic function at $v$.

**Property 3 (Continuity).** The map $v \mapsto \Phi(\tau, v, x)$ is uniformly continuous on $\mathbb{R}^d$ for each fixed $\tau$ and $x$.

**Property 4 (Determines the distribution).** By the Levy inversion theorem, the characteristic function uniquely determines the distribution of $X_T \mid X_t = x$. If the density $f(\tau, \cdot, x)$ exists:

$$
f(\tau, y, x) = \frac{1}{(2\pi)^d} \int_{\mathbb{R}^d} e^{-i\langle v, y \rangle} \Phi(\tau, v, x)\,dv
$$

---

## Connection to the Riccati System

### From Log-Affine Property to ODEs

The functions $\phi(\tau, iv)$ and $\psi(\tau, iv)$ satisfy the generalized Riccati ODEs derived in the previous section. For an affine diffusion with drift $b(x) = b_0 + \sum_i b_i x_i$ and diffusion $a(x) = a_0 + \sum_i a_i x_i$:

$$
\frac{\partial \phi}{\partial \tau}(\tau, iv) = F(\psi(\tau, iv))
$$

$$
\frac{\partial \psi}{\partial \tau}(\tau, iv) = R(\psi(\tau, iv))
$$

where

$$
F(w) = \langle b_0, w \rangle + \frac{1}{2}\langle w, a_0 w \rangle + \int_{D \setminus \{0\}} (e^{\langle w, z \rangle} - 1)\,m_0(dz)
$$

$$
R_j(w) = \langle b_j, w \rangle + \frac{1}{2}\langle w, a_j w \rangle + \int_{D \setminus \{0\}} (e^{\langle w, z \rangle} - 1)\,m_j(dz)
$$

evaluated at $w = \psi(\tau, iv)$.

### Scalar Affine Diffusion

For a one-dimensional affine diffusion $dX_t = (\kappa_0 + \kappa_1 X_t)\,dt + \sqrt{\sigma_0 + \sigma_1 X_t}\,dW_t$, the Riccati system for the characteristic function (setting $u = iv$) becomes:

$$
\psi'(\tau) = \kappa_1 \psi(\tau) + \frac{1}{2}\sigma_1 \psi(\tau)^2, \qquad \psi(0) = iv
$$

$$
\phi'(\tau) = \kappa_0 \psi(\tau) + \frac{1}{2}\sigma_0 \psi(\tau)^2, \qquad \phi(0) = 0
$$

Since $\psi(0) = iv$ is purely imaginary, the solution $\psi(\tau)$ is generally complex-valued even though the ODE coefficients are real. This is the typical situation in Fourier pricing: the Riccati equations must be solved in the complex plane.

---

## Characteristic Function of Specific Models

### Gaussian Case (Vasicek / Ornstein-Uhlenbeck)

For $\sigma_1 = 0$ (constant diffusion), the $\psi$-equation is linear:

$$
\psi'(\tau) = \kappa_1 \psi(\tau), \qquad \psi(0) = iv
$$

$$
\psi(\tau) = iv\,e^{\kappa_1 \tau}
$$

The $\phi$-equation integrates to:

$$
\phi(\tau) = \kappa_0 \int_0^\tau \psi(s)\,ds + \frac{\sigma_0}{2}\int_0^\tau \psi(s)^2\,ds
$$

For the Ornstein-Uhlenbeck process ($\kappa_0 = 0$, $\kappa_1 = -\kappa$, $\sigma_0 = \sigma^2$):

$$
\psi(\tau) = iv\,e^{-\kappa\tau}
$$

$$
\phi(\tau) = -\frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau})
$$

The characteristic function is:

$$
\Phi(\tau, v, x) = \exp\!\left(-\frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau}) + iv\,e^{-\kappa\tau} x\right)
$$

This is the characteristic function of a Gaussian random variable with mean $x e^{-\kappa\tau}$ and variance $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})$, confirming that the OU process has a Gaussian transition density.

### Square-Root Case (CIR)

For the CIR process $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ with $\kappa_0 = \kappa\theta$, $\kappa_1 = -\kappa$, $\sigma_0 = 0$, $\sigma_1 = \xi^2$, the $\psi$-equation becomes a genuine Riccati equation:

$$
\psi'(\tau) = -\kappa\psi(\tau) + \frac{\xi^2}{2}\psi(\tau)^2, \qquad \psi(0) = iv
$$

This nonlinear ODE has the closed-form solution:

$$
\psi(\tau) = \frac{iv\,\gamma\,e^{-\frac{1}{2}(\gamma + \kappa)\tau}}{\gamma - \frac{1}{2}iv\xi^2(1 - e^{-\gamma\tau})}
$$

where $\gamma = \sqrt{\kappa^2 - 2\xi^2 iv}$ (the branch of the square root is chosen so that $\operatorname{Re}(\gamma) > 0$).

The $\phi$-equation integrates to:

$$
\phi(\tau) = \frac{\kappa\theta}{\xi^2}\left[(\gamma + \kappa)\tau - 2\log\!\left(\frac{\gamma - \frac{1}{2}iv\xi^2(1-e^{-\gamma\tau})}{\gamma}\right)\right]
$$

!!! warning "Branch Cuts in Complex Riccati Solutions"
    The square root $\gamma = \sqrt{\kappa^2 - 2\xi^2 iv}$ and the logarithm in $\phi(\tau)$ require careful treatment of branch cuts. The standard choice ensures $\operatorname{Re}(\gamma) > 0$ for all $v \in \mathbb{R}$, and the logarithm uses the principal branch with a cut along $(-\infty, 0]$. Incorrect branch choices produce discontinuities in the characteristic function that corrupt Fourier inversion.

---

## The Discounted Characteristic Function

For derivative pricing, we often need the *discounted* characteristic function, which incorporates the discount factor $e^{-\int_t^T r_s\,ds}$ into the expectation. If the short rate is affine, $r(x) = \rho_0 + \langle \rho_1, x \rangle$, the discounted characteristic function also has exponential-affine form:

$$
\mathbb{E}\!\left[e^{-\int_t^T r(X_s)\,ds + i\langle v, X_T \rangle} \mid X_t = x\right] = \exp\!\left(\tilde{\phi}(\tau, iv) + \langle \tilde{\psi}(\tau, iv), x \rangle\right)
$$

where $\tilde{\phi}$ and $\tilde{\psi}$ satisfy a modified Riccati system that incorporates the discounting terms $\rho_0$ and $\rho_1$. This extension is developed in detail in the section on the discounted transform.

---

## From Characteristic Function to Pricing

The characteristic function connects to option pricing through Fourier inversion. For a European call with strike $K$ and maturity $T$ on the log-price $X_T = \log S_T$:

$$
C(t, x) = S_t - \frac{K e^{-r\tau}}{\pi} \int_0^\infty \operatorname{Re}\!\left[\frac{e^{-iv\log K}\,\Phi(\tau, v - i, x)}{iv\,\Phi(\tau, -i, x)}\right] dv
$$

The key point is that $\Phi(\tau, v, x)$ is known in closed form (or semi-closed form) for affine processes, so the only numerical step is evaluating a one-dimensional integral. This is the foundation of the Carr-Madan FFT method and the COS method.

??? example "Characteristic Function of Arithmetic Brownian Motion"
    For $dX_t = \mu\,dt + \sigma\,dW_t$ (constant coefficients, $\kappa_0 = \mu$, $\kappa_1 = 0$, $\sigma_0 = \sigma^2$, $\sigma_1 = 0$):

    $$
    \psi(\tau) = iv, \qquad \phi(\tau) = iv\mu\tau - \frac{1}{2}\sigma^2 v^2 \tau
    $$

    $$
    \Phi(\tau, v, x) = \exp\!\left(ivx + iv\mu\tau - \frac{1}{2}\sigma^2 v^2 \tau\right)
    $$

    This is the characteristic function of $N(x + \mu\tau, \sigma^2\tau)$, as expected. $\square$

---

## Summary

The characteristic function of an affine process has the exponential-affine form $\Phi(\tau, v, x) = \exp(\phi(\tau, iv) + \langle \psi(\tau, iv), x \rangle)$, where $\phi$ and $\psi$ satisfy the generalized Riccati ODE system. For constant-diffusion (Gaussian) models, the Riccati equation is linear and yields Gaussian transition densities. For square-root (CIR-type) models, the Riccati equation is genuinely quadratic and produces non-Gaussian distributions with closed-form but complex-valued solutions requiring careful branch cut management. The characteristic function is the bridge between the affine process theory and practical derivative pricing via Fourier inversion methods.

---

## Further Reading

- Duffie, D., Pan, J., & Singleton, K. (2000). "Transform Analysis and Asset Pricing for Affine Jump-Diffusions." *Econometrica*, 68(6), 1343-1376.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009, Chapter 10.
- Fang, F. & Oosterlee, C. W. (2008). "A Novel Pricing Method for European Options Based on Fourier-Cosine Series Expansions." *SIAM Journal on Scientific Computing*, 31(2), 826-848.

---

## Exercises

**Exercise 1.** For the Vasicek model with $\kappa_0 = \kappa\theta$, $\kappa_1 = -\kappa$, $\sigma_0 = \sigma^2$, $\sigma_1 = 0$, verify the Hermitian symmetry property $\Phi(\tau, -v, x) = \overline{\Phi(\tau, v, x)}$ by showing that $\phi(\tau, -iv) = \overline{\phi(\tau, iv)}$ and $\psi(\tau, -iv) = \overline{\psi(\tau, iv)}$.

---

**Exercise 2.** Starting from the characteristic function of the OU process

$$
\Phi(\tau, v, x) = \exp\!\left(-\frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau}) + iv\,e^{-\kappa\tau} x\right)
$$

use the Fourier inversion formula to recover the conditional density $f(\tau, y, x)$ and verify that it is Gaussian with mean $xe^{-\kappa\tau}$ and variance $\frac{\sigma^2}{2\kappa}(1-e^{-2\kappa\tau})$.

---

**Exercise 3.** For the CIR process, the discriminant is $\gamma = \sqrt{\kappa^2 - 2\xi^2 iv}$. Compute $|\gamma|^2$ as a function of $v$ and verify that $\operatorname{Re}(\gamma) > 0$ for all real $v$ when the principal square root is used. Why is this positivity condition necessary for the stability of the closed-form solution?

---

**Exercise 4.** Consider the discounted characteristic function $\mathbb{E}[e^{-\int_t^T r_s\,ds + ivX_T} \mid X_t = x]$ for the CIR short-rate model. How does the Riccati ODE for $\psi$ change compared to the undiscounted case? Write down the modified ODE and identify the new discriminant.

---

**Exercise 5.** For arithmetic Brownian motion $dX_t = \mu\,dt + \sigma\,dW_t$, the characteristic function is $\Phi(\tau, v, x) = \exp(ivx + iv\mu\tau - \frac{1}{2}\sigma^2 v^2\tau)$. Use this to compute the price of a European call option on $e^{X_T}$ with strike $K$ via the Fourier inversion formula

$$
C = e^{-r\tau}\int_{-\infty}^{\infty} (e^y - K)^+ f(\tau, y, x)\,dy
$$

and verify that you recover the Black-Scholes formula.

---

**Exercise 6.** Explain why the characteristic function of any affine process is continuous in the frequency variable $v$ but the moment generating function may not be continuous in $u$ across the boundary of the admissible set. Illustrate with the CIR process, identifying the critical value $u^*$ at which continuity breaks down.

---

**Exercise 7.** For a two-dimensional affine process with independent Gaussian and CIR components, write the joint conditional characteristic function $\mathbb{E}[e^{iv_1 X_T^{(1)} + iv_2 X_T^{(2)}} \mid X_t = x]$ as a product of two one-dimensional characteristic functions. Under what conditions on the diffusion matrix does this factorization hold?
