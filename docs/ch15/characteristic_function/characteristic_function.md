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

Recall (see [generalized Riccati ODEs](generalized_riccati_odes.md)) that $\phi$ and $\psi$ satisfy $\partial_\tau\phi = F(\psi)$, $\partial_\tau\psi = R(\psi)$, with $F$, $R$ assembled from the drift, diffusion, and jump parameters of the affine process. The characteristic function corresponds to evaluating this system at $u = iv$.

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

For $\sigma_1 = 0$, the $\psi$-equation is linear; for the OU process ($\kappa_0 = 0$, $\kappa_1 = -\kappa$, $\sigma_0 = \sigma^2$),

$$
\psi(\tau) = iv\,e^{-\kappa\tau}, \qquad \phi(\tau) = -\frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau})
$$

giving $\Phi(\tau, v, x) = \exp(-\frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau}) + iv\,e^{-\kappa\tau} x)$, the CF of a Gaussian with mean $xe^{-\kappa\tau}$ and variance $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})$. Full derivation: Recall (see [explicit Riccati solutions § Vasicek](explicit_riccati_solutions.md#vasicek-model-linear-riccati)).

### Square-Root Case (CIR)

For the CIR process the $\psi$-equation $\psi' = -\kappa\psi + \frac{\xi^2}{2}\psi^2$, $\psi(0) = iv$ admits the closed-form

$$
\psi(\tau) = \frac{iv\,\gamma\,e^{-\frac{1}{2}(\gamma + \kappa)\tau}}{\gamma - \frac{1}{2}iv\xi^2(1 - e^{-\gamma\tau})}, \qquad \gamma = \sqrt{\kappa^2 - 2\xi^2 iv}
$$

with the principal branch $\operatorname{Re}(\gamma) > 0$, and $\phi(\tau) = \frac{\kappa\theta}{\xi^2}\!\left[(\gamma+\kappa)\tau - 2\log\!\frac{\gamma - \tfrac12 iv\xi^2(1-e^{-\gamma\tau})}{\gamma}\right]$. Branch-cut treatment, alternative ("Little Heston Trap") parameterisation, and derivation: Recall (see [explicit Riccati solutions § CIR](explicit_riccati_solutions.md#cir-model-scalar-riccati-equation)).

---

## The Discounted Characteristic Function

For pricing under an affine short rate $r(x) = \rho_0 + \langle \rho_1, x \rangle$, the discounted CF $\mathbb{E}[e^{-\int_t^T r(X_s)\,ds + i\langle v, X_T\rangle} \mid X_t = x] = \exp(\tilde\phi(\tau,iv) + \langle\tilde\psi(\tau,iv), x\rangle)$ retains the exponential-affine form, with $\tilde\phi$, $\tilde\psi$ solving a Riccati system shifted by $\rho_0$, $\rho_1$. Recall (see [discounted transform](../discounted_transform/discounted_characteristic_function.md)).

---

## From Characteristic Function to Pricing

Fourier inversion turns the affine CF into option prices via a single one-dimensional integral. Recall (see [Fourier inversion § ch09](../../ch09/fourier_series/fourier_series_finite_intervals.md) and the Carr-Madan / COS / Lewis methods in [ch09](../../ch09/index.md)).

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

??? success "Solution to Exercise 1"
    For the Vasicek model we have $\psi(\tau) = iv\,e^{-\kappa\tau}$ and

    $$
    \phi(\tau, iv) = i\theta v(1 - e^{-\kappa\tau}) - \frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau})
    $$

    **Checking $\psi$:** Replace $v$ by $-v$:

    $$
    \psi(\tau, -iv) = -iv\,e^{-\kappa\tau}
    $$

    The complex conjugate of $\psi(\tau, iv) = iv\,e^{-\kappa\tau}$ is $\overline{iv\,e^{-\kappa\tau}} = -iv\,e^{-\kappa\tau}$ since $e^{-\kappa\tau}$ is real. Hence $\psi(\tau, -iv) = \overline{\psi(\tau, iv)}$.

    **Checking $\phi$:** Replace $v$ by $-v$:

    $$
    \phi(\tau, -iv) = -i\theta v(1 - e^{-\kappa\tau}) - \frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau})
    $$

    The complex conjugate of $\phi(\tau, iv)$ is

    $$
    \overline{\phi(\tau, iv)} = -i\theta v(1 - e^{-\kappa\tau}) - \frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau})
    $$

    since all terms multiplying $i$ are real. Hence $\phi(\tau, -iv) = \overline{\phi(\tau, iv)}$.

    **Conclusion:** Since $\Phi(\tau, v, x) = \exp(\phi(\tau, iv) + \psi(\tau, iv)\,x)$, we have

    $$
    \Phi(\tau, -v, x) = \exp(\phi(\tau, -iv) + \psi(\tau, -iv)\,x) = \exp(\overline{\phi(\tau, iv)} + \overline{\psi(\tau, iv)}\,x) = \overline{\Phi(\tau, v, x)}
    $$

    confirming Hermitian symmetry.

---

**Exercise 2.** Starting from the characteristic function of the OU process

$$
\Phi(\tau, v, x) = \exp\!\left(-\frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau}) + iv\,e^{-\kappa\tau} x\right)
$$

use the Fourier inversion formula to recover the conditional density $f(\tau, y, x)$ and verify that it is Gaussian with mean $xe^{-\kappa\tau}$ and variance $\frac{\sigma^2}{2\kappa}(1-e^{-2\kappa\tau})$.

??? success "Solution to Exercise 2"
    The Fourier inversion formula gives

    $$
    f(\tau, y, x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-ivy}\,\Phi(\tau, v, x)\,dv
    $$

    Substituting the OU characteristic function:

    $$
    f(\tau, y, x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \exp\!\left(-ivy + ive^{-\kappa\tau}x - \frac{\sigma^2 v^2}{4\kappa}(1-e^{-2\kappa\tau})\right)dv
    $$

    Define $\mu_\tau = xe^{-\kappa\tau}$ and $\sigma_\tau^2 = \frac{\sigma^2}{2\kappa}(1-e^{-2\kappa\tau})$. The exponent becomes

    $$
    iv(\mu_\tau - y) - \frac{\sigma_\tau^2}{2}v^2
    $$

    Complete the square in $v$:

    $$
    -\frac{\sigma_\tau^2}{2}\!\left(v - \frac{i(\mu_\tau - y)}{\sigma_\tau^2}\right)^2 - \frac{(\mu_\tau - y)^2}{2\sigma_\tau^2}
    $$

    The integral over $v$ of $\exp\!\left(-\frac{\sigma_\tau^2}{2}(v - c)^2\right)$ for any constant $c$ equals $\sqrt{2\pi/\sigma_\tau^2}$ by contour deformation (Gaussian integral). Therefore

    $$
    f(\tau, y, x) = \frac{1}{2\pi}\sqrt{\frac{2\pi}{\sigma_\tau^2}}\exp\!\left(-\frac{(y - \mu_\tau)^2}{2\sigma_\tau^2}\right) = \frac{1}{\sqrt{2\pi\sigma_\tau^2}}\exp\!\left(-\frac{(y - \mu_\tau)^2}{2\sigma_\tau^2}\right)
    $$

    This is the density of $N(\mu_\tau, \sigma_\tau^2)$ with mean $xe^{-\kappa\tau}$ and variance $\frac{\sigma^2}{2\kappa}(1-e^{-2\kappa\tau})$, confirming the Gaussian transition density.

---

**Exercise 3.** For the CIR process, the discriminant is $\gamma = \sqrt{\kappa^2 - 2\xi^2 iv}$. Compute $|\gamma|^2$ as a function of $v$ and verify that $\operatorname{Re}(\gamma) > 0$ for all real $v$ when the principal square root is used. Why is this positivity condition necessary for the stability of the closed-form solution?

??? success "Solution to Exercise 3"
    Write $\gamma = \sqrt{\kappa^2 - 2\xi^2 iv}$. Setting $w = \kappa^2 - 2\xi^2 iv$, we have $w = \kappa^2 - 2\xi^2 iv$, so $\operatorname{Re}(w) = \kappa^2 > 0$ and $\operatorname{Im}(w) = -2\xi^2 v$.

    The modulus is

    $$
    |w| = \sqrt{\kappa^4 + 4\xi^4 v^2}
    $$

    For the principal square root $\gamma = \sqrt{w}$, we have $|\gamma|^2 = |w| = \sqrt{\kappa^4 + 4\xi^4 v^2}$.

    To verify $\operatorname{Re}(\gamma) > 0$: write $w = |w|e^{i\theta}$ where $\theta = \arg(w) = \arctan(-2\xi^2 v / \kappa^2)$. Since $\operatorname{Re}(w) = \kappa^2 > 0$, we have $\theta \in (-\pi/2, \pi/2)$. The principal square root gives $\gamma = \sqrt{|w|}\,e^{i\theta/2}$ with $\theta/2 \in (-\pi/4, \pi/4)$, so $\operatorname{Re}(\gamma) = \sqrt{|w|}\cos(\theta/2) > 0$ for all real $v$.

    **Why positivity is necessary:** The closed-form solution involves denominators of the form $\gamma - c(1 - e^{-\gamma\tau})$ and exponentials $e^{-\gamma\tau}$. If $\operatorname{Re}(\gamma) < 0$, the term $e^{-\gamma\tau}$ would grow exponentially with $\tau$, causing numerical instability and potential division by zero. The condition $\operatorname{Re}(\gamma) > 0$ ensures that $e^{-\gamma\tau} \to 0$ as $\tau \to \infty$, keeping the closed-form solution stable and well-behaved for all maturities.

---

**Exercise 4.** Consider the discounted characteristic function $\mathbb{E}[e^{-\int_t^T r_s\,ds + ivX_T} \mid X_t = x]$ for the CIR short-rate model. How does the Riccati ODE for $\psi$ change compared to the undiscounted case? Write down the modified ODE and identify the new discriminant.

??? success "Solution to Exercise 4"
    In the CIR short-rate model, $r_t = X_t$ with $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$. For the undiscounted characteristic function, the $\psi$-ODE is

    $$
    \psi' = -\kappa\psi + \frac{\xi^2}{2}\psi^2, \qquad \psi(0) = iv
    $$

    For the discounted characteristic function $\mathbb{E}[e^{-\int_t^T r_s\,ds + ivX_T} \mid X_t = x]$, the short rate $r(x) = x$ means $\rho_0 = 0$ and $\rho_1 = 1$. The discounting adds $-\rho_1 = -1$ to the $\psi$-equation (from the $-r_1$ term in the DPS formulation). The modified ODE becomes

    $$
    \tilde{\psi}' = -1 - \kappa\tilde{\psi} + \frac{\xi^2}{2}\tilde{\psi}^2, \qquad \tilde{\psi}(0) = iv
    $$

    This is a full Riccati equation $\tilde{\psi}' = \alpha + \beta\tilde{\psi} + \frac{1}{2}\gamma\tilde{\psi}^2$ with $\alpha = -1$, $\beta = -\kappa$, and $\gamma = \xi^2$.

    The new discriminant is

    $$
    \tilde{\gamma} = \sqrt{\beta^2 - 2\alpha\gamma} = \sqrt{\kappa^2 + 2\xi^2}
    $$

    Compared to the undiscounted case (where the discriminant for the characteristic function is $\gamma = \sqrt{\kappa^2 - 2\xi^2 iv}$ depending on $v$), the discounted bond-pricing discriminant $\sqrt{\kappa^2 + 2\xi^2}$ is a real positive constant independent of $v$. The discounting term introduces a constant $\alpha = -1$ that shifts the Riccati equation from a homogeneous to an inhomogeneous form.

---

**Exercise 5.** For arithmetic Brownian motion $dX_t = \mu\,dt + \sigma\,dW_t$, the characteristic function is $\Phi(\tau, v, x) = \exp(ivx + iv\mu\tau - \frac{1}{2}\sigma^2 v^2\tau)$. Use this to compute the price of a European call option on $e^{X_T}$ with strike $K$ via the Fourier inversion formula

$$
C = e^{-r\tau}\int_{-\infty}^{\infty} (e^y - K)^+ f(\tau, y, x)\,dy
$$

and verify that you recover the Black-Scholes formula.

??? success "Solution to Exercise 5"
    Under arithmetic Brownian motion $dX_t = \mu\,dt + \sigma\,dW_t$, the transition density is $X_T \mid X_t = x \sim N(x + \mu\tau, \sigma^2\tau)$. The call price on $e^{X_T}$ with strike $K$ is

    $$
    C = e^{-r\tau}\int_{-\infty}^{\infty}(e^y - K)^+ f(y)\,dy
    $$

    where $f(y)$ is the density of $N(x + \mu\tau, \sigma^2\tau)$. The integral is nonzero only for $y > \log K$:

    $$
    C = e^{-r\tau}\!\left[\int_{\log K}^{\infty} e^y f(y)\,dy - K\int_{\log K}^{\infty} f(y)\,dy\right]
    $$

    Let $m = x + \mu\tau$ and $s^2 = \sigma^2\tau$.

    **Second integral:** $\int_{\log K}^{\infty} f(y)\,dy = \Phi_N\!\left(\frac{m - \log K}{s}\right)$ where $\Phi_N$ is the standard normal CDF.

    **First integral:** Using the identity $e^y f(y) = e^{m + s^2/2}\,\tilde{f}(y)$ where $\tilde{f}$ is the density of $N(m + s^2, s^2)$:

    $$
    \int_{\log K}^{\infty} e^y f(y)\,dy = e^{m + s^2/2}\,\Phi_N\!\left(\frac{m + s^2 - \log K}{s}\right)
    $$

    Identifying $S_t = e^x$, $e^{m + s^2/2} = e^{x + \mu\tau + \sigma^2\tau/2}$, and setting $\mu = r - \sigma^2/2$ (risk-neutral drift of the log-price), we get $e^{m+s^2/2} = S_t e^{r\tau}$. Define

    $$
    d_1 = \frac{x + r\tau + \sigma^2\tau/2 - \log K}{\sigma\sqrt{\tau}}, \qquad d_2 = d_1 - \sigma\sqrt{\tau}
    $$

    Then

    $$
    C = S_t\,\Phi_N(d_1) - Ke^{-r\tau}\,\Phi_N(d_2)
    $$

    which is the Black-Scholes formula.

---

**Exercise 6.** Explain why the characteristic function of any affine process is continuous in the frequency variable $v$ but the moment generating function may not be continuous in $u$ across the boundary of the admissible set. Illustrate with the CIR process, identifying the critical value $u^*$ at which continuity breaks down.

??? success "Solution to Exercise 6"
    The characteristic function is defined for $u = iv$ with any $v \in \mathbb{R}^d$, and we have $|\mathbb{E}[e^{i\langle v, X_T\rangle}]| \leq \mathbb{E}[|e^{i\langle v, X_T\rangle}|] = 1$. This bound holds regardless of the model and for all $\tau \geq 0$. Therefore, the Riccati solution with initial data $\psi(0) = iv$ can never blow up, and the map $v \mapsto \Phi(\tau, v, x)$ is defined for all $v \in \mathbb{R}^d$. Moreover, since $|e^{i\langle v, X_T\rangle}|$ is bounded and the integrand is dominated, the dominated convergence theorem ensures that $v \mapsto \Phi(\tau, v, x)$ is continuous.

    The moment generating function, on the other hand, requires $\mathbb{E}[e^{\langle u, X_T\rangle}] < \infty$ for real $u$, which may fail. For the CIR process, $\mathbb{E}[e^{uX_T}]$ exists only when $u$ is below a critical threshold $u^* = 2\kappa/\xi^2$. At $u = u^*$, the equilibrium of the Riccati ODE $\psi' = -\kappa\psi + \frac{\xi^2}{2}\psi^2$ is $\psi^* = 2\kappa/\xi^2$, and for $u > u^*$, the quadratic term dominates, driving $\psi(\tau) \to \infty$ in finite time $T^*(u)$. This finite-time explosion of the Riccati solution is reflected in the divergence of the moment generating function.

    Continuity fails at the boundary $u = u^*$ because $\lim_{\tau\to\infty}\psi(\tau, u^*) = u^*$ (finite), but $\lim_{u \downarrow u^*} T^*(u) < \infty$. The transition from global to finite-time existence is discontinuous in the sense that the MGF goes from finite (for $u < u^*$) to infinite (for $u > u^*$) at the critical value.

---

**Exercise 7.** For a two-dimensional affine process with independent Gaussian and CIR components, write the joint conditional characteristic function $\mathbb{E}[e^{iv_1 X_T^{(1)} + iv_2 X_T^{(2)}} \mid X_t = x]$ as a product of two one-dimensional characteristic functions. Under what conditions on the diffusion matrix does this factorization hold?

??? success "Solution to Exercise 7"
    Let $X_t = (X_t^{(1)}, X_t^{(2)})$ where $X^{(1)}$ is Gaussian and $X^{(2)}$ is CIR. The joint characteristic function is

    $$
    \mathbb{E}\!\left[e^{iv_1 X_T^{(1)} + iv_2 X_T^{(2)}} \mid X_t = x\right] = \exp\!\left(\phi(\tau, iv) + \psi_1(\tau, iv_1)\,x_1 + \psi_2(\tau, iv_2)\,x_2\right)
    $$

    When the components are independent, the Riccati system decouples. Each $\psi_j$ depends only on the corresponding $u_j$:

    $$
    \psi_1'(\tau) = R_1(\psi_1(\tau)), \qquad \psi_2'(\tau) = R_2(\psi_2(\tau))
    $$

    and $\phi$ splits as $\phi = \phi_1 + \phi_2$ where $\phi_j' = F_j(\psi_j)$. The joint characteristic function factors as

    $$
    \Phi(\tau, v, x) = \Phi_1(\tau, v_1, x_1)\cdot\Phi_2(\tau, v_2, x_2)
    $$

    where $\Phi_1$ is the Gaussian characteristic function and $\Phi_2$ is the CIR characteristic function.

    **Condition for factorization:** The factorization holds if and only if the diffusion matrix $a(x)$ has no cross terms coupling the two components. Specifically, if

    $$
    a(x) = \begin{pmatrix} a_{11}(x_1) & 0 \\ 0 & a_{22}(x_2) \end{pmatrix}
    $$

    so that the covariance between $dX^{(1)}$ and $dX^{(2)}$ is zero, i.e., the Brownian motions driving the two components are uncorrelated. In affine terms, this means the matrices $a_0, a_1, a_2$ are all diagonal, and the drift vectors $b_1, b_2$ have no cross-component entries (the drift of $X^{(1)}$ does not depend on $X^{(2)}$ and vice versa). If correlation $\rho \neq 0$ is introduced between the driving Brownian motions, the off-diagonal terms in $a(x)$ couple the $\psi$-equations, and the factorization breaks down.
