# Limits of the Affine Framework

The affine framework is one of the most powerful tools in mathematical finance: it delivers closed-form characteristic functions, exponential-affine bond prices, and Fourier-based pricing for a wide class of models. Yet its power comes from stringent structural requirements --- linear drift, affine diffusion, and state-independent jump size distributions --- that exclude many empirically important phenomena. Rough volatility, non-Markovian dynamics, feedback effects, and certain path-dependent features all lie outside the affine class. This section precisely identifies what the affine framework can and cannot accommodate, explains the mathematical reasons for each limitation, and surveys the modeling approaches that go beyond it.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the three structural requirements that define an affine process
    2. Identify specific empirical phenomena that violate each requirement
    3. Explain mathematically why rough volatility, non-Markovian dynamics, and path-dependence break the affine structure
    4. Compare the pricing and calibration trade-offs between affine and non-affine models
    5. Decide when an affine model is adequate and when a non-affine alternative is necessary

---

## What Makes a Model Affine

Recall (see [affine process definition](../definition_and_setup/definition_of_affine_process.md) and [general Riccati system](../characteristic_function/generalized_riccati_odes.md)). An affine model imposes three structural conditions on $X_t \in D \subseteq \mathbb{R}^d$:

1. **Affine drift**: $\mu(x) = b_0 + Bx$
2. **Affine diffusion**: $a(x) = a_0 + \sum_{i=1}^d \alpha_i x^{(i)}$
3. **Affine jump compensator**: intensity $\Lambda(x) = \lambda_0 + \lambda^\top x$ with state-independent jump size distribution

If any condition is violated, the exponential-affine characteristic function breaks down and the Riccati ODE system no longer applies.

---

## Limitation 1: Rough Volatility

### The Empirical Evidence

Empirical studies of realized volatility time series (Gatheral, Jaisson, and Rosenbaum, 2018) reveal that the log-volatility of equity indices behaves like a fractional Brownian motion with Hurst parameter $H \approx 0.1$, far below the Markovian value $H = 0.5$. This produces:

- Volatility autocorrelation decaying as a power law $t^{2H-1}$ rather than exponentially
- The ATM implied volatility skew decaying as $T^{H-1/2} \approx T^{-0.4}$ for short maturities, much steeper than the $T^{-1/2}$ decay of standard stochastic volatility models
- Term structure of the VIX that is better matched by rough dynamics

### Why Affine Fails

The rough Heston model replaces the CIR variance process $dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t$ with a fractional kernel:

$$
V_t = V_0 + \frac{1}{\Gamma(H + \frac{1}{2})}\int_0^t (t-s)^{H-1/2}\kappa(\theta - V_s)\,ds + \frac{1}{\Gamma(H + \frac{1}{2})}\int_0^t (t-s)^{H-1/2}\xi\sqrt{V_s}\,dW_s
$$

This process is **non-Markovian**: the future evolution of $V_t$ depends on the entire past path $\{V_s\}_{s \leq t}$, not just the current value $V_t$. The affine framework fundamentally requires the Markov property to reduce the conditional expectation $\mathbb{E}[e^{uX_T} | \mathcal{F}_t]$ to a function of the current state $X_t$.

!!! info "Theorem (Rough Heston Characteristic Function)"
    The rough Heston model has a characteristic function of the form

    $$
    \mathbb{E}\!\left[e^{iu\ln S_T}\right] = \exp\!\left(\phi(T, u) + \psi(T, u) V_0\right)
    $$

    where $\psi$ satisfies a **fractional Riccati equation**:

    $$
    \psi(t) = \int_0^t \frac{(t-s)^{H-1/2}}{\Gamma(H+1/2)} R(\psi(s))\,ds
    $$

    with $R(\psi) = \frac{1}{2}(iu - u^2) + (\rho\xi iu - \kappa)\psi + \frac{1}{2}\xi^2\psi^2$. This is a Volterra integral equation, not an ODE.

The fractional Riccati equation has no closed-form solution and must be solved numerically (e.g., by Adams schemes). While the exponential-affine structure is partially preserved (in the sense that the CF is still $\exp(\phi + \psi V_0)$), the Riccati ODE is replaced by a Volterra integral equation that is computationally more expensive and theoretically more subtle.

### What Is Lost

| Feature | Affine (Heston) | Rough Heston |
|---|---|---|
| Riccati system | ODE (millisecond solve) | Volterra integral equation (seconds) |
| Markov property | Yes | No (infinite-dimensional state) |
| Simulation | Exact (or Euler on 1D CIR) | Hybrid scheme, $O(N^{2H+1})$ cost |
| Calibration speed | Fast (Fourier in milliseconds) | Slow (fractional Riccati per CF eval) |
| Short-maturity skew | $O(T^{-1/2})$ | $O(T^{H-1/2})$ (fits market) |

---

## Limitation 2: Non-Markovian Path-Dependence

### Beyond Rough Volatility

Rough volatility is the most prominent example of non-Markovian dynamics, but other non-Markovian features arise naturally:

**Realized variance feedback.** Some models specify that the drift or volatility of the asset depends on the realized variance $\langle\ln S\rangle_t = \int_0^t V_s\,ds$. Since $\langle\ln S\rangle_t$ is a running integral of the state, conditioning on it requires augmenting the state space, and if the dependence is nonlinear, the affine structure breaks.

**Regime-switching with duration dependence.** Standard Markov regime-switching (where the regime follows a finite-state Markov chain) preserves a form of affine structure on the augmented state space. However, if the transition probabilities depend on the **duration** in the current regime (semi-Markov dynamics), the Markov property is violated.

**Path-dependent volatility.** Models where the volatility depends on the running maximum, the drawdown, or other path functionals are inherently non-Markovian unless the relevant functional is included as an additional state variable with affine dynamics.

### The Markov Embedding Problem

A common strategy is to **embed** the non-Markovian process into a higher-dimensional Markov process. For example, the fractional Brownian motion can be represented as a Markov process on an infinite-dimensional state space (the Mandelbrot-Van Ness representation). In principle, one could define an affine process on this extended state space, but:

1. The state space is infinite-dimensional, so the Riccati system becomes a PDE or integral equation
2. Numerical solution is substantially more expensive than finite-dimensional Riccati ODEs
3. Calibration requires solving the extended system at every parameter evaluation

---

## Limitation 3: Nonlinear Drift and Diffusion

### The Black-Karasinski Example

The Black-Karasinski model $d(\ln r_t) = [\theta(t) - a\ln r_t]\,dt + \sigma\,dW_t$ is linear in the log-rate $x_t = \ln r_t$, but the short rate $r_t = e^{x_t}$ enters the discounting factor nonlinearly. The bond pricing PDE contains the term $e^x g$, which is not affine in $x$. This single nonlinearity destroys the exponential-affine bond price formula.

### Quadratic Models

Quadratic short-rate models specify $r_t = \alpha_0 + \alpha_1^\top X_t + X_t^\top \alpha_2 X_t$ where $X_t$ is an affine (typically Gaussian) process. The quadratic dependence of $r$ on $X$ means bond prices are exponential-quadratic rather than exponential-affine:

$$
P(t,T) = \exp\!\left(A(\tau) + B(\tau)^\top X_t + X_t^\top C(\tau) X_t\right)
$$

The coefficients $(A, B, C)$ satisfy a system of matrix Riccati equations. While still semi-analytical, the pricing is more complex than the affine case.

### CEV and Local Volatility

The constant elasticity of variance (CEV) model $dS_t = \mu S_t\,dt + \sigma S_t^{\beta}\,dW_t$ with $\beta \neq 1$ has a diffusion coefficient $\sigma^2 S^{2\beta}$ that is **not affine** in $S$ unless $\beta = 1$ (geometric Brownian motion) or $\beta = 1/2$ (CIR-type). General local volatility models $dS_t = \mu S_t\,dt + \sigma(S_t, t) S_t\,dW_t$ with arbitrary $\sigma(S, t)$ lie entirely outside the affine class.

---

## Limitation 4: State-Dependent Jump Distributions

### The Affine Requirement

The affine jump-diffusion framework requires that the jump size distribution $\nu_k(dz)$ be **independent of the state** $X_t$. The jump intensity can depend on the state (through $\Lambda(x) = \lambda_0 + \lambda^\top x$), but once a jump occurs, its size is drawn from a fixed distribution.

### What This Excludes

**State-dependent jump sizes.** If the distribution of the jump size depends on the current volatility level (e.g., larger jumps when volatility is high), the affine structure breaks because the moment generating function $\hat{\nu}(u, x) = \mathbb{E}[e^{uz} | X = x]$ depends on $x$, and the product $\Lambda(x) \cdot \hat{\nu}(u, x)$ is no longer affine in $x$.

**Contagion models.** In credit risk, a default by one firm can trigger an immediate increase in the default intensity of other firms, with the magnitude depending on the current state of the surviving portfolio. While self-exciting (Hawkes) jump intensities are affine, state-dependent contagion magnitudes generally are not.

---

## Limitation 5: Constraints on the Smile

### What Affine Models Can Generate

Affine stochastic volatility models (like Heston) generate implied volatility surfaces with specific properties:

- **Skew**: Controlled by the correlation $\rho$ between the asset and variance processes
- **Curvature**: Controlled by the vol-of-vol $\xi$
- **Term structure of skew**: Decays as $O(T^{-1/2})$ for large $T$, governed by the mean-reversion speed $\kappa$

### What They Cannot Generate

1. **Steep short-maturity skews**: The $O(T^{-1/2})$ skew decay is a fundamental constraint of Markovian diffusive models. Markets often exhibit $O(T^{-0.4})$ or steeper decay, requiring either jumps (Bates) or rough volatility.

2. **Flexible curvature term structure**: Single-factor Heston produces a curvature that is tied to the same parameters controlling the skew. Multi-factor models (double Heston) provide more flexibility but at the cost of more parameters.

3. **Arbitrary smile shapes**: Affine models produce smiles that are approximately quadratic in log-moneyness. Smiles with kinks, flat wings, or other non-standard shapes require non-affine or non-parametric approaches.

---

## When to Go Beyond Affine

The decision to use a non-affine model involves a trade-off between empirical accuracy and computational tractability.

### Use Affine When

- Speed is critical (real-time pricing, CVA, XVA)
- The model must price thousands of vanilla options quickly
- The implied volatility surface has standard shape (monotone skew, moderate curvature)
- Calibration must run in seconds, not minutes

### Go Beyond Affine When

- Short-maturity smile behavior is critical and the $T^{-1/2}$ skew is inadequate
- The product is path-dependent and requires realistic volatility dynamics (e.g., variance swaps with realized vol triggers)
- Empirical analysis demonstrates rough volatility in the underlying
- The pricing problem requires non-Markovian features (regime duration, path-dependent barriers)

### Decision Framework

| Criterion | Affine adequate? | Non-affine needed? |
|---|---|---|
| Vanilla European options | Yes (Fourier pricing) | Only if short-maturity skew matters |
| Variance swaps | Yes (affine replication) | If realized-vol dynamics matter |
| Bermudan swaptions | Often (tree/PDE on 1-2 factors) | If rate positivity requires BK |
| Exotic path-dependent | Depends on payoff | Often yes (realistic vol dynamics) |
| VIX derivatives | Marginal (Heston struggles) | Yes (rough Heston fits VIX term structure) |

---

## Summary of Non-Affine Alternatives

| Model class | Key feature | Pricing approach | Calibration cost |
|---|---|---|---|
| Rough Heston ($H < 0.5$) | Fractional Riccati CF | Fourier (slow CF eval) | Moderate |
| Local volatility (Dupire) | Non-parametric $\sigma(S,t)$ | PDE / Monte Carlo | Fast (Dupire formula) |
| Stochastic local volatility | Combines LV + SV | Monte Carlo / PDE | Expensive |
| SABR | CEV + lognormal vol | Hagan formula (fast) | Fast per expiry |
| Black-Karasinski | Log-normal short rate | Trinomial tree | Moderate |
| Quadratic Gaussian | Quadratic $r(X)$ | Matrix Riccati | Moderate |
| Neural SDE | Learned dynamics | Monte Carlo + AD | Very expensive |

---

## Summary

The affine framework delivers its remarkable tractability --- exponential-affine characteristic functions, Riccati ODE systems, and Fourier-based pricing --- by imposing three structural requirements: affine drift, affine diffusion, and state-independent jump sizes, all within a Markovian setting. These requirements exclude rough volatility ($H < 0.5$, non-Markovian), general local volatility (non-affine diffusion), state-dependent jump distributions, and path-dependent dynamics. The most empirically important gap is the short-maturity implied volatility skew, where affine models predict $O(T^{-1/2})$ decay but markets exhibit steeper behavior consistent with rough dynamics. Going beyond affine typically means accepting slower pricing (Volterra integral equations instead of Riccati ODEs, Monte Carlo instead of Fourier inversion) in exchange for greater empirical realism. The choice between affine and non-affine models is ultimately a trade-off between computational speed and the fidelity required by the specific trading or risk management application.

---

## Further Reading

- Gatheral, J., Jaisson, T., and Rosenbaum, M. (2018). "Volatility is rough." *Quantitative Finance*, 18(6), 933--949.
- El Euch, O. and Rosenbaum, M. (2019). "The characteristic function of rough Heston models." *Mathematical Finance*, 29(1), 3--38.
- Duffie, D., Filipovic, D., and Schachermayer, W. (2003). "Affine processes and applications in finance." *Annals of Applied Probability*, 13(3), 984--1053.
- Filipovic, D. (2009). *Term-Structure Models: A Graduate Course*. Springer.

---

## Exercises

**Exercise 1.** The SABR model has dynamics $dF_t = \sigma_t F_t^\beta\,dW_t^{(1)}$ and $d\sigma_t = \alpha\sigma_t\,dW_t^{(2)}$ with $\operatorname{Corr}(dW^{(1)}, dW^{(2)}) = \rho\,dt$. Identify which affine condition fails for $\beta \neq 0, 1/2, 1$ and explain why the exponential-affine ansatz cannot be applied.

??? success "Solution to Exercise 1"
    The SABR model has dynamics

    $$
    dF_t = \sigma_t F_t^\beta\,dW_t^{(1)}, \qquad d\sigma_t = \alpha\sigma_t\,dW_t^{(2)}
    $$

    with $\operatorname{Corr}(dW^{(1)}, dW^{(2)}) = \rho\,dt$. The state vector is $X_t = (F_t, \sigma_t)^\top$.

    **Checking the affine diffusion condition.** The diffusion matrix is

    $$
    a(F, \sigma) = \begin{pmatrix} \sigma^2 F^{2\beta} & \rho\alpha\sigma^2 F^\beta \\ \rho\alpha\sigma^2 F^\beta & \alpha^2\sigma^2 \end{pmatrix}
    $$

    For the affine condition, we need $a(x) = a_0 + \alpha_1 x^{(1)} + \alpha_2 x^{(2)}$, i.e., each entry of $a$ must be an affine (linear plus constant) function of the state variables $(F, \sigma)$.

    The $(1,1)$ entry is $\sigma^2 F^{2\beta}$. For general $\beta$:

    - If $\beta = 0$: the entry is $\sigma^2$, which is quadratic in $\sigma$, not affine.
    - If $\beta = 1/2$: the entry is $\sigma^2 F$, which is $\sigma^2$ times $F$ --- a product of state variables, not affine.
    - If $\beta = 1$: the entry is $\sigma^2 F^2$, again not affine.

    In fact, for **any** $\beta$, the diffusion matrix $a(F, \sigma)$ involves products like $\sigma^2 F^{2\beta}$ that are nonlinear functions of the state. The affine condition $a(x) = a_0 + \sum_i \alpha_i x^{(i)}$ requires each component of $a$ to depend at most linearly on $x^{(i)}$, with **no products of state variables** and **no nonlinear powers**.

    The exponential-affine ansatz $\mathbb{E}[e^{u^\top X_T} | X_t = x] = \exp(\phi + \psi^\top x)$ requires that the generator applied to $e^{u^\top x}$ produces a function of the form $(F(u) + R(u)^\top x) \cdot e^{u^\top x}$. The term $\frac{1}{2}\sigma^2 F^{2\beta} u_1^2$ from the $(1,1)$ entry of $a$ is not affine in $(F, \sigma)$ for any $\beta \neq 0, 1/2, 1$ in general, and even at these special values the $\sigma^2$ factor makes it nonlinear. Therefore the Riccati ODE system cannot close, and the affine framework does not apply.

---

**Exercise 2.** Rough volatility models use fractional Brownian motion $B_t^H$ with Hurst parameter $H < 1/2$. The process $B_t^H$ is not Markovian. Explain why the Markov property is essential for the affine framework and why its failure prevents the derivation of Riccati ODEs.

??? success "Solution to Exercise 2"
    The affine framework derives the conditional characteristic function $\mathbb{E}[e^{u^\top X_T} | \mathcal{F}_t]$ by exploiting the Markov property in two essential steps:

    **Step 1: Reduction to a function of the current state.** The Markov property states that $\mathbb{E}[f(X_T) | \mathcal{F}_t] = g(t, X_t)$ for some deterministic function $g$. This allows us to write

    $$
    \mathbb{E}[e^{u^\top X_T} | \mathcal{F}_t] = G(t, X_t, u)
    $$

    Without the Markov property, the conditional expectation depends on the entire path $\{X_s\}_{s \leq t}$, so no finite-dimensional function $G(t, x, u)$ can represent it.

    **Step 2: PDE characterization via the generator.** The Markov property implies that $G$ satisfies the Kolmogorov backward PDE $\partial_t G + \mathcal{A}G = 0$. The affine ansatz $G(t, x, u) = \exp(\phi(T-t, u) + \psi(T-t, u)^\top x)$ is substituted into this PDE, and the affine structure of $\mathcal{A}$ ensures that the PDE reduces to the Riccati ODE system for $(\phi, \psi)$.

    **Why fractional Brownian motion breaks this.** For $B_t^H$ with $H < 1/2$, the increments $B_{t+\Delta}^H - B_t^H$ depend on the entire past through the fractional kernel $(t - s)^{H-1/2}$. The process $X_t$ driven by $B^H$ is not Markovian: knowing $X_t$ alone is insufficient to determine the conditional distribution of $X_T$. The conditional expectation $\mathbb{E}[e^{u^\top X_T} | \mathcal{F}_t]$ depends on the full history $\{X_s\}_{s \leq t}$, not just $X_t$.

    As a result, there is no PDE for $G(t, x)$ --- instead, one obtains a Volterra integral equation (the fractional Riccati equation) that incorporates the memory kernel. This equation is infinite-dimensional in nature and cannot be reduced to a finite system of ODEs, which is why the standard affine Riccati machinery does not apply.

---

**Exercise 3.** Consider a local volatility model $dS_t = rS_t\,dt + \sigma(S_t, t)S_t\,dW_t$ where $\sigma(S, t)$ is a general function calibrated to the implied volatility surface. Show that unless $\sigma(S, t)$ has the specific form $\sigma(S, t) = \sqrt{c_0 + c_1\log S}$, the diffusion is not affine in the log-price.

??? success "Solution to Exercise 3"
    In the local volatility model, define $x_t = \log S_t$. By Ito's lemma:

    $$
    dx_t = \left(r - \frac{1}{2}\sigma^2(e^{x_t}, t)\right)dt + \sigma(e^{x_t}, t)\,dW_t
    $$

    The diffusion coefficient (as a function of the log-price $x$) is $\tilde{\sigma}(x, t) = \sigma(e^x, t)$, and the diffusion matrix is

    $$
    a(x, t) = \tilde{\sigma}(x, t)^2 = \sigma(e^x, t)^2
    $$

    For the affine condition, we need $a(x, t) = c_0(t) + c_1(t)\,x$ for some time-dependent coefficients. This requires

    $$
    \sigma(e^x, t)^2 = c_0(t) + c_1(t)\,x
    $$

    Substituting $S = e^x$, i.e., $x = \log S$:

    $$
    \sigma(S, t)^2 = c_0(t) + c_1(t)\log S
    $$

    Therefore

    $$
    \sigma(S, t) = \sqrt{c_0(t) + c_1(t)\log S}
    $$

    This is the only functional form of $\sigma(S, t)$ for which the diffusion is affine in the log-price. For any other dependence on $S$ --- constant ($\sigma(S,t) = \sigma_0$, which gives $c_1 = 0$, a special case), power-law ($\sigma \propto S^\gamma$ for $\gamma \neq 0$), or a general calibrated surface --- the diffusion $\sigma(S,t)^2$ is not a linear function of $\log S$, and the affine structure fails.

    Note that even the special affine case $\sigma(S,t) = \sqrt{c_0 + c_1\log S}$ is unusual in practice: it requires $c_0 + c_1\log S > 0$ for all relevant $S$, which constrains the domain, and it does not match the Dupire local volatility surfaces typically calibrated from market data.

---

**Exercise 4.** The rough Heston model replaces the CIR variance process with a fractional process driven by $B^H$. El Euch and Rosenbaum (2019) showed that the characteristic function satisfies a fractional Riccati equation. Describe qualitatively how a fractional Riccati equation differs from the standard Riccati ODE and why it is harder to solve.

??? success "Solution to Exercise 4"
    The standard Heston Riccati ODE for the variance factor loading $\psi(t)$ is

    $$
    \frac{d\psi}{dt} = R(\psi) = \frac{1}{2}(iu - u^2) + (\rho\xi iu - \kappa)\psi + \frac{1}{2}\xi^2\psi^2
    $$

    This is an ordinary differential equation: $\psi(t)$ depends only on the current value $\psi$ and can be solved forward from $\psi(0) = 0$. It has a closed-form solution in terms of exponentials.

    The **fractional Riccati equation** in the rough Heston model ($H < 1/2$) replaces this ODE with a Volterra integral equation:

    $$
    \psi(t) = \frac{1}{\Gamma(H + 1/2)}\int_0^t (t - s)^{H - 1/2}\,R(\psi(s))\,ds
    $$

    **Key differences:**

    1. **Memory kernel.** The fractional kernel $(t - s)^{H-1/2}$ with $H < 1/2$ gives exponent $H - 1/2 < 0$, so the kernel is singular at $s = t$ and decays as a power law. This means $\psi(t)$ depends on the entire history $\{\psi(s)\}_{0 \leq s \leq t}$, not just the current value. The equation is non-local in time.

    2. **No closed-form solution.** The Volterra structure with a nonlinear right-hand side $R(\psi)$ (quadratic in $\psi$) admits no known closed-form solution. Numerical methods such as Adams schemes must be used, with care taken to handle the singular kernel.

    3. **Computational cost.** Solving the ODE at a single point $t = T$ costs $O(1)$ (closed form) or $O(N)$ for a numerical ODE solver with $N$ steps. Solving the Volterra equation costs $O(N^2)$ because each step requires evaluating the integral over all previous steps. With acceleration techniques (e.g., the multi-level scheme of Bayer, Friz, and Gatheral), the cost can be reduced but remains substantially higher than the ODE case.

    4. **Regularity.** The solution $\psi(t)$ of the fractional Riccati equation has regularity $\psi(t) \sim t^{H+1/2}$ near $t = 0$, which is less smooth than the ODE solution (which is analytic). This affects the accuracy of numerical quadrature for Fourier inversion.

---

**Exercise 5.** List three empirical phenomena that affine models handle well and three that they handle poorly. For each poorly-handled phenomenon, name a non-affine model that addresses it. Discuss the pricing/calibration trade-off: what computational advantage is lost by moving to the non-affine model?

??? success "Solution to Exercise 5"
    **Three phenomena that affine models handle well:**

    1. **Implied volatility skew for vanilla options.** The Heston model produces a realistic skew through the correlation $\rho < 0$ between the asset and variance, and the Fourier pricing formula evaluates in milliseconds.

    2. **Term structure of interest rates.** Affine short-rate models (Vasicek, CIR, multi-factor Gaussian) deliver exponential-affine bond prices $P(t,T) = e^{A(\tau) + B(\tau)r_t}$, enabling fast yield curve fitting and swaption pricing.

    3. **Credit default swap pricing.** Affine intensity models produce closed-form survival probabilities $\mathbb{Q}(\tau > T | \mathcal{F}_t) = e^{A(\tau) + B(\tau)\lambda_t}$, allowing fast CDS pricing and CVA computation.

    **Three phenomena that affine models handle poorly:**

    1. **Short-maturity implied volatility skew.** Affine diffusion models produce a skew that decays as $O(T^{-1/2})$, but equity markets exhibit steeper decay around $O(T^{-0.4})$. **Non-affine alternative:** The rough Heston model ($H \approx 0.1$) matches the empirical skew decay $O(T^{H-1/2})$. **Trade-off:** The characteristic function requires solving a Volterra integral equation ($O(N^2)$ cost per evaluation) instead of a Riccati ODE (closed form), making calibration orders of magnitude slower.

    2. **Realistic local volatility dynamics.** Affine models cannot reproduce the Dupire local volatility surface, which is a nonlinear function of $(S, t)$. **Non-affine alternative:** Stochastic local volatility (SLV) models combine a calibrated local volatility function with stochastic volatility. **Trade-off:** SLV models require Monte Carlo simulation or PDE methods for pricing --- there is no Fourier-based pricing formula, and calibration requires a particle method or Markovian projection, increasing computation from milliseconds to seconds or minutes.

    3. **Volatility clustering and self-similarity.** Realized volatility exhibits long memory and power-law autocorrelation decay, inconsistent with the exponential decay of Markovian affine models. **Non-affine alternative:** Fractional stochastic volatility models or the rough Bergomi model. **Trade-off:** These models are non-Markovian, requiring Monte Carlo simulation with $O(N^{2H+1})$ cost per path and no closed-form characteristic function, making real-time pricing infeasible.

---

**Exercise 6.** The 3/2 stochastic volatility model has dynamics $dV_t = \kappa V_t(\theta - V_t)\,dt + \xi V_t^{3/2}\,dW_t$. Show that $V_t$ is not affine by checking the diffusion condition: $a(V) = \xi^2 V^3$ is cubic in $V$, not affine. However, show that $Y_t = 1/V_t$ is a CIR process and therefore affine. What does this tell you about the importance of choosing the right state variable?

??? success "Solution to Exercise 6"
    **Showing $V_t$ is not affine.** The diffusion coefficient of $V_t$ is $\sigma(V) = \xi V^{3/2}$, so the diffusion matrix is

    $$
    a(V) = \sigma(V)^2 = \xi^2 V^3
    $$

    For the affine condition, $a(V)$ must be of the form $a_0 + a_1 V$ (affine in $V$). Since $V^3$ is cubic, it cannot be written as $a_0 + a_1 V$ for any constants $a_0, a_1$. Therefore $V_t$ is not an affine process.

    **Showing $Y_t = 1/V_t$ is CIR.** Apply Ito's lemma to $Y_t = f(V_t) = V_t^{-1}$:

    $$
    dY_t = f'(V_t)\,dV_t + \frac{1}{2}f''(V_t)\,(dV_t)^2
    $$

    With $f'(V) = -V^{-2}$ and $f''(V) = 2V^{-3}$:

    $$
    dY_t = -V_t^{-2}\!\left[\kappa V_t(\theta - V_t)\,dt + \xi V_t^{3/2}\,dW_t\right] + \frac{1}{2}\cdot 2V_t^{-3}\cdot\xi^2 V_t^3\,dt
    $$

    $$
    = \left[-\kappa\theta V_t^{-1} + \kappa + \xi^2\right]dt - \xi V_t^{-1/2}\,dW_t
    $$

    Substituting $V_t^{-1} = Y_t$ and $V_t^{-1/2} = \sqrt{Y_t}$:

    $$
    dY_t = \left[(\kappa + \xi^2) - \kappa\theta\,Y_t\right]dt - \xi\sqrt{Y_t}\,dW_t
    $$

    This is a CIR process with parameters:

    - Mean-reversion speed: $\tilde{\kappa} = \kappa\theta$
    - Long-run mean: $\tilde{\theta} = (\kappa + \xi^2)/(\kappa\theta)$
    - Volatility parameter: $\tilde{\xi} = \xi$

    The process $Y_t$ has affine drift $\tilde{\kappa}(\tilde{\theta} - Y_t)$ and diffusion $\tilde{\xi}\sqrt{Y_t}$, which satisfies the affine conditions on $\mathbb{R}_+$.

    **Implications for state variable choice.** This example demonstrates that whether a process is affine depends critically on the **choice of state variable**. The same underlying stochastic dynamics can be non-affine in one parameterization ($V_t$) and affine in another ($Y_t = 1/V_t$). Before concluding that a model lies outside the affine class, one should check whether a nonlinear transformation of the state variable produces an affine process. If such a transformation exists, the full machinery of Riccati ODEs, characteristic functions, and Fourier pricing can be applied in the transformed coordinates.
