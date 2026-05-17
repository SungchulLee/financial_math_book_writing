# Understanding Solutions of Stochastic Differential Equations

The previous section defined what a stochastic differential equation is and introduced the canonical models. We now turn to a deeper question: what does it mean to **solve** an SDE?

Unlike ODEs, solving an SDE means describing a **random process**, not a single deterministic function. This fundamental distinction — that the solution is itself random — shapes everything that follows: the types of solutions one can seek, the analytical techniques available, and the limits of closed-form solvability.

!!! tip "Toy mechanism: one ODE → one function, one SDE → many paths"
    Start with $dx/dt = x$, $x_0 = 1$. The "solution" is a single function: $x(t) = e^t$. Now perturb to $dX_t = X_t\,dt + X_t\,dW_t$. The "solution" is no longer a function — it is a *random family* $X_t(\omega) = \exp(\tfrac{1}{2}t + W_t(\omega))$, one trajectory per outcome $\omega$. So "solve" can mean: (i) write the pathwise formula $X_t(\omega) = F(t, W_\cdot(\omega))$ — the strongest answer; (ii) name the distribution $X_t \sim$ log-normal — enough for pricing; (iii) characterise via a PDE on $u(t,x) = \mathbb{E}[\phi(X_T) \mid X_t = x]$ — useful when the law is implicit; (iv) simulate. The four senses of "solve" below are exactly these four answers to the same question.

!!! abstract "Learning Goals"
    After completing this section you should be able to:

    - explain what it means to solve an SDE
    - distinguish between explicit pathwise solutions and distributional characterizations
    - recognize structural classes of SDEs
    - understand why transformations are central to solvability
    - identify when analytical methods are unlikely to succeed

The discussion proceeds in three stages:

1. **What a solution means**
2. **Transformation-based thinking**
3. **Limits of closed-form solvability**

---

## 1. What Does "Solving" an SDE Mean?

In deterministic calculus we solve for a function $x(t)$.

For stochastic differential equations the solution is itself a **random process**.

### Types of Solution

There are several distinct senses in which an SDE can be "solved":

**Explicit pathwise solution.** This is the strongest case. One writes $X_t$ explicitly in terms of time, the initial condition, and Brownian motion — for example, $X_t = X_0 + \mu t + \sigma W_t$. Such formulas allow direct simulation and transparent moment computation.

**Distributional characterization.** Sometimes no simple pathwise formula exists, but the law of $X_t$ is fully known. Examples include the Gaussian law of the OU process and the log-normal law of GBM. Knowing the distribution suffices for computing option prices, risk measures, and other statistical quantities.

**PDE / generator characterization.** A diffusion may be analyzed indirectly through the partial differential equations satisfied by conditional expectations. This approach connects SDEs to the Kolmogorov equations and the Feynman–Kac formula.

**Numerical solvability.** When closed forms are unavailable, the SDE may still be studied effectively through simulation, moment approximations, or PDE solvers.

Recall (see [§ Strong vs Weak Solutions](../existence_uniqueness/strong_vs_weak.md)): a strong solution is an adapted continuous process satisfying the integral equation a.s., where the stochastic term is an Itô integral. Solutions may depend on the entire Brownian path up to time $t$ — e.g., the OU solution involves a stochastic integral over the path.

Analytical solutions allow us to compute distributions, derive moments, analyze long-term behavior, and benchmark numerical algorithms.

!!! warning "Important"
    Most SDEs **do not admit elementary closed-form pathwise solutions**.
    In many cases one can still characterize the process through its law, transition density, or associated PDE.

---

## 2. Types of SDE Structures

Recall (see [§ Stochastic Differential Equations § Structure Classification](sde.md#3-sde-structure-classification)): additive noise, multiplicative noise, linear/mean-reverting drift, and state-dependent diffusion are the four canonical structures. Recognizing the structure is the most important step in solving an SDE.

---

## 3. The Transformation Viewpoint

Many solvable SDEs become manageable only after a suitable change of variables. The central theme is

$$
\text{complicated SDE}
\;\rightarrow\;
\text{simpler transformed SDE}
\;\rightarrow\;
\text{solution or characterization}
$$

We do not usually solve difficult SDEs by brute force, but by transforming them into forms we already understand. Typical transformations include:

- **log transforms** for multiplicative noise — removes state dependence from the diffusion
- **integrating factors** for linear drift — cancels the deterministic decay term
- **Lamperti transforms** for state-dependent diffusion — normalizes the diffusion coefficient to a constant

Although the details differ from model to model, the strategy is the same: identify the equation's structure, apply the appropriate transformation, solve or simplify, then interpret the result in the original variables.

---

## 4. Diffusion Model Cheat Sheet

The four-structure classification of [§ SDE Structure Classification](sde.md#3-sde-structure-classification) extends to two further families used in finance:

| Model | SDE | Key Property | Typical Use |
|---|---|---|---|
| **CIR** | $dr_t = a(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$ | non-negative, state-dependent diffusion | short-rate models |
| **Heston** | $dv_t = \kappa(\bar{v} - v_t)\,dt + \xi\sqrt{v_t}\,dW_t$ | stochastic volatility | option pricing |

!!! note "Heston Notation"
    The Heston variance SDE uses the conventional parameters $\kappa$ (mean-reversion speed), $\bar{v}$ (long-run variance), and $\xi$ (vol of vol) to distinguish it from the CIR/Vasicek notation $a$, $\theta$, $\sigma$ used elsewhere in this chapter.

For the canonical BM-with-drift, GBM, and Vasicek/OU formulas and methods, see [§ Canonical Examples](sde.md#2-canonical-examples) and [§ Techniques for Solving SDEs](solving_sde.md).

---

## 5. Analytical Tools for Studying SDEs

Some techniques do not directly produce an explicit pathwise solution, but still provide powerful analytical information.

### Martingale Methods

If one can identify a function $g(X_t,t)$ such that $M_t = g(X_t,t)$ is a martingale, then conditional expectations can be analyzed through the generator of the diffusion. This viewpoint leads naturally to the **Kolmogorov backward equation**.

### Feynman–Kac Formula

Recall (see [§ Kolmogorov Backward Equation](../../ch05/kolmogorov_equations/kolmogorov_backward.md)): conditional expectations $u(t,x) = \mathbb{E}[\phi(X_T) \mid X_t = x]$ satisfy the backward PDE $u_t + b\,u_x + \tfrac{1}{2}\sigma^2 u_{xx} = 0$ — the foundation of the Black–Scholes equation.

### Girsanov's Theorem

Girsanov's theorem allows one to change the **drift** of a stochastic process by changing the probability measure. This is a fundamental tool in **risk-neutral pricing**: under the physical measure $\mathbb{P}$ the drift involves the true return $\mu$, while under the risk-neutral measure $\mathbb{Q}$ it involves the risk-free rate $r$.

---

## 6. When Closed-Form Solutions Do Not Exist

Most SDEs cannot be solved analytically in an elementary pathwise sense. Examples include nonlinear stochastic volatility models, SABR-type models, multi-factor interest rate models, jump-diffusions, and coupled nonlinear systems.

Even when a simple explicit pathwise formula is unavailable, one may still have access to transition densities, characteristic functions, moment equations, PDE representations, and simulation methods. In all these cases the structural classification of §2 remains the starting point: knowing the equation's form determines which analytical or numerical tool to reach for.

---

## 7. Bridge to Solution Techniques

This page focused on **conceptual foundations**: what it means to solve an SDE, the four senses of solvability, and the structural patterns that determine which techniques apply.

The next page turns to the main **solution techniques** themselves: direct integration, Itô transformations, integrating factors, Lamperti transforms, and the practical workflow for applying them to classical solvable models.

---

## Exercises

**Exercise 1.** For each of the following, state which type of solution is being described: explicit pathwise solution, distributional characterization, PDE/generator characterization, or numerical solvability.

(a) $S_t = S_0 \exp[(\mu - \sigma^2/2)t + \sigma W_t]$

(b) The transition density of $r_t$ satisfies the Fokker–Planck equation.

(c) $r_t$ follows a noncentral chi-squared distribution with known parameters.

(d) Euler–Maruyama simulation with $10^6$ sample paths gives $\widehat{\mathbb{E}}[X_T] = 3.14 \pm 0.02$.

??? success "Solution to Exercise 1"
    **(a)** $S_t = S_0 \exp[(\mu - \sigma^2/2)t + \sigma W_t]$ — this is an **explicit pathwise solution**. The process is written as a deterministic function of time, the initial condition, and the Brownian motion path.

    **(b)** The transition density of $r_t$ satisfies the Fokker-Planck equation — this is a **PDE/generator characterization**. The process is described indirectly through the partial differential equation governing its probability density.

    **(c)** $r_t$ follows a noncentral chi-squared distribution with known parameters — this is a **distributional characterization**. The full law of $r_t$ is specified, even though no simple pathwise formula may exist.

    **(d)** Euler-Maruyama simulation with $10^6$ sample paths gives $\widehat{\mathbb{E}}[X_T] = 3.14 \pm 0.02$ — this is **numerical solvability**. The SDE is studied through Monte Carlo simulation rather than analytical formulas.

---

**Exercise 2.** For the SDE $dX_t = \alpha X_t(1 - X_t)\,dt + \sigma X_t(1 - X_t)\,dW_t$:

(a) Classify the noise structure (additive, multiplicative, or state-dependent diffusion).

(b) Suggest a transformation that might simplify the diffusion coefficient.

(c) Is a closed-form pathwise solution likely? Justify your reasoning.

??? success "Solution to Exercise 2"
    **(a)** The diffusion coefficient is $\sigma(X_t) = \sigma X_t(1 - X_t)$, which depends on the state $X_t$ in a nonlinear way. This is **state-dependent diffusion** (neither purely additive nor simply multiplicative in the standard sense).

    **(b)** The Lamperti transform $h(x) = \int^x \frac{1}{\sigma s(1-s)}\,ds$ would normalize the diffusion to a constant. Using partial fractions:

    $$
    \frac{1}{s(1-s)} = \frac{1}{s} + \frac{1}{1-s}
    $$

    so $h(x) = \frac{1}{\sigma}\ln\frac{x}{1-x}$, i.e., the **logit transform** $Y_t = \frac{1}{\sigma}\ln\frac{X_t}{1-X_t}$ would make the diffusion coefficient constant.

    **(c)** A closed-form pathwise solution is **unlikely**. The drift $\alpha X_t(1 - X_t)$ is nonlinear (logistic growth), and after the Lamperti transform the resulting drift in $Y_t$ will generally be a complicated nonlinear function of $Y_t$. Standard transformation techniques are unlikely to reduce this to a directly integrable form. One would typically resort to numerical simulation, PDE methods, or moment analysis.

---

**Exercise 3.** Consider the three canonical transformations:

| Transformation | Target structure |
|---|---|
| $Y_t = \log X_t$ | ? |
| $Y_t = e^{at}(X_t - \theta)$ | ? |
| $Y_t = \int^{X_t} \frac{dx}{\sigma(x)}$ | ? |

Fill in the "Target structure" column by describing what type of SDE each transformation is designed to simplify.

??? success "Solution to Exercise 3"
    | Transformation | Target structure |
    |---|---|
    | $Y_t = \log X_t$ | Removes **multiplicative noise**: if $dX_t = \mu X_t\,dt + \sigma X_t\,dW_t$, then $Y_t = \log X_t$ satisfies an SDE with **additive (constant) diffusion** coefficient, namely $dY_t = (\mu - \sigma^2/2)\,dt + \sigma\,dW_t$ |
    | $Y_t = e^{at}(X_t - \theta)$ | Eliminates **linear mean-reverting drift**: if $dX_t = a(\theta - X_t)\,dt + \sigma\,dW_t$, then $Y_t$ satisfies a **driftless SDE** $dY_t = \sigma e^{at}\,dW_t$ that can be integrated directly |
    | $Y_t = \int^{X_t} \frac{dx}{\sigma(x)}$ | Normalizes **state-dependent diffusion** to unit (constant) diffusion coefficient — this is the **Lamperti transform**, converting the SDE to one where only the drift remains state-dependent |

---

**Exercise 4.** The SABR model for forward rates is

$$
dF_t = \sigma_t F_t^\beta\,dW_t^{(1)}, \qquad d\sigma_t = \alpha\,\sigma_t\,dW_t^{(2)}
$$

with $\langle dW_t^{(1)}, dW_t^{(2)} \rangle = \rho\,dt$.

(a) Does this model admit an elementary closed-form pathwise solution? Why or why not?

(b) Which of the four senses of solvability (pathwise, distributional, PDE, numerical) are available for this model?

??? success "Solution to Exercise 4"
    **(a)** The SABR model does **not** admit an elementary closed-form pathwise solution. Several factors prevent this:

    - The forward rate $F_t$ has **state-dependent diffusion** $\sigma_t F_t^\beta$, where the local volatility itself is stochastic.
    - The volatility $\sigma_t$ follows its own GBM-type SDE.
    - The two Brownian motions are **correlated** ($\rho \neq 0$), creating a coupled two-dimensional system.
    - No single transformation can simultaneously simplify both equations into integrable form.

    **(b)** Available senses of solvability:

    - **Pathwise:** Not available in elementary form.
    - **Distributional:** Asymptotic expansions for the implied volatility are available (the Hagan et al. formula), which provide approximate distributional information. The exact transition density is not known in closed form.
    - **PDE:** The Kolmogorov backward equation for the two-dimensional diffusion $(F_t, \sigma_t)$ can be written down and solved numerically or asymptotically.
    - **Numerical:** Monte Carlo simulation is straightforward and is the standard approach for pricing under SABR. Euler-Maruyama or more specialized schemes can be applied to the coupled system.

---

**Exercise 5.** Explain why the Feynman–Kac formula creates a connection between SDEs and PDEs. Specifically, if $u(t,x) = \mathbb{E}[\phi(X_T) \mid X_t = x]$ for an SDE with drift $b(x)$ and diffusion $\sigma(x)$, write down the PDE that $u$ satisfies and explain why this is useful when direct simulation is expensive.

??? success "Solution to Exercise 5"
    For an SDE $dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t$, consider the function $u(t, x) = \mathbb{E}[\phi(X_T) \mid X_t = x]$. By the Feynman-Kac formula, $u$ satisfies the backward PDE

    $$
    \frac{\partial u}{\partial t} + b(x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 u}{\partial x^2} = 0
    $$

    with terminal condition $u(T, x) = \phi(x)$.

    This connection is useful because it provides two complementary approaches to the same problem. When Monte Carlo simulation is expensive (high-dimensional expectations, path-dependent payoffs, need for full solution surface), one can instead solve the PDE numerically using finite difference or finite element methods. Conversely, when PDE methods are expensive (high-dimensional state spaces), Monte Carlo simulation of the SDE provides an efficient alternative. The Feynman-Kac formula guarantees that both approaches compute the same quantity, and it forms the mathematical foundation of the Black-Scholes equation, where the option price satisfies a PDE derived from the underlying GBM dynamics.

---

**Exercise 6.** A colleague proposes modeling a stock price with the SDE $dS_t = \mu\,dt + \sigma\,dW_t$ (Brownian motion with drift) instead of geometric Brownian motion. Identify at least two problems with this choice from a modeling perspective, referring to the structural classification discussed in this chapter.

??? success "Solution to Exercise 6"
    **Problem 1: Non-positivity.** Brownian motion with drift $S_t = S_0 + \mu t + \sigma W_t$ is a Gaussian process. Since a Gaussian random variable takes all real values with positive probability, $S_t < 0$ occurs with positive probability for any $t > 0$. Stock prices cannot be negative, so this model is structurally inconsistent with the fundamental constraint of limited liability.

    **Problem 2: Constant absolute volatility vs proportional volatility.** In Brownian motion with drift, the diffusion coefficient is the constant $\sigma$, meaning that a \$1000 stock and a \$1 stock experience the same absolute random fluctuations. In reality, price fluctuations are roughly proportional to the price level. GBM captures this with multiplicative noise ($\sigma S_t\,dW_t$), producing **percentage returns** that are stationary, which is consistent with empirical observations.

    In terms of the structural classification: the additive-noise model uses a constant diffusion coefficient independent of the state, while GBM uses multiplicative noise where the diffusion is proportional to the state. The multiplicative structure is what ensures positivity (through the log-normal distribution) and produces realistic return dynamics.
