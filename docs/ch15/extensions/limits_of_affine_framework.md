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

An affine model is defined by three structural conditions on the state vector $X_t \in D \subseteq \mathbb{R}^d$:

!!! info "Definition: Affine Process"
    A Markov process $X_t$ is **affine** if its infinitesimal generator $\mathcal{A}$ has the property that for every $u \in i\mathbb{R}^d$, the function $x \mapsto e^{u^\top x}$ is an eigenvector of $\mathcal{A}$ up to an affine correction. Equivalently, the conditional characteristic function has the exponential-affine form:

    $$
    \mathbb{E}\!\left[e^{u^\top X_T} \mid X_t = x\right] = \exp\!\left(\phi(\tau, u) + \psi(\tau, u)^\top x\right)
    $$

    where $\phi$ and $\psi$ solve Riccati ODEs.

This requires:

1. **Affine drift**: $\mu(x) = b_0 + Bx$ (linear in the state)
2. **Affine diffusion**: $a(x) = a_0 + \sum_{i=1}^d \alpha_i x^{(i)}$ (the diffusion matrix is affine in the state)
3. **Affine jump compensator**: The jump intensity is $\Lambda(x) = \lambda_0 + \lambda^\top x$ and the jump size distribution is state-independent

If any of these three conditions is violated, the exponential-affine form of the characteristic function breaks down, and the Riccati ODE system no longer applies.

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

---

**Exercise 2.** Rough volatility models use fractional Brownian motion $B_t^H$ with Hurst parameter $H < 1/2$. The process $B_t^H$ is not Markovian. Explain why the Markov property is essential for the affine framework and why its failure prevents the derivation of Riccati ODEs.

---

**Exercise 3.** Consider a local volatility model $dS_t = rS_t\,dt + \sigma(S_t, t)S_t\,dW_t$ where $\sigma(S, t)$ is a general function calibrated to the implied volatility surface. Show that unless $\sigma(S, t)$ has the specific form $\sigma(S, t) = \sqrt{c_0 + c_1\log S}$, the diffusion is not affine in the log-price.

---

**Exercise 4.** The rough Heston model replaces the CIR variance process with a fractional process driven by $B^H$. El Euch and Rosenbaum (2019) showed that the characteristic function satisfies a fractional Riccati equation. Describe qualitatively how a fractional Riccati equation differs from the standard Riccati ODE and why it is harder to solve.

---

**Exercise 5.** List three empirical phenomena that affine models handle well and three that they handle poorly. For each poorly-handled phenomenon, name a non-affine model that addresses it. Discuss the pricing/calibration trade-off: what computational advantage is lost by moving to the non-affine model?

---

**Exercise 6.** The 3/2 stochastic volatility model has dynamics $dV_t = \kappa V_t(\theta - V_t)\,dt + \xi V_t^{3/2}\,dW_t$. Show that $V_t$ is not affine by checking the diffusion condition: $a(V) = \xi^2 V^3$ is cubic in $V$, not affine. However, show that $Y_t = 1/V_t$ is a CIR process and therefore affine. What does this tell you about the importance of choosing the right state variable?
