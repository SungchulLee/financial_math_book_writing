# Greeks via the Infinitesimal Generator


In Markov models, the infinitesimal generator provides a structural link between pricing, PDEs, and sensitivity analysis.

---

## Setup: risk-neutral diffusion


Under $\mathbb{Q}$, consider


$$
\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t\,\mathrm{d}W_t
$$



so the generator acting on smooth test functions $f$ is


$$
\boxed{
(\mathcal{L}f)(S) = rS f'(S) + \frac{1}{2}\sigma^2 S^2 f''(S)
}
$$



---

## Pricing PDE


For a European payoff $\Phi$, the price


$$
V(t,S)=\mathbb{E}^{t,S}\!\left[e^{-r(T-t)}\Phi(S_T)\right]
$$



solves the backward equation


$$
\boxed{
\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0,
\qquad V(T,S)=\Phi(S)
}
$$



---

## Parameter sensitivity as generator sensitivity


Treat the generator as parameterized by $\sigma$:


$$
\mathcal{L}_\sigma f = rS f' + \frac{1}{2}\sigma^2 S^2 f''
$$



Then vega $\nu=V_\sigma$ is linked to the derivative of $\mathcal{L}_\sigma$ with respect to $\sigma$:


$$
\frac{\partial}{\partial \sigma}\mathcal{L}_\sigma f
=
\sigma S^2 f''
$$



This suggests a PDE for $\nu$ of the form


$$
\boxed{
\frac{\partial \nu}{\partial t} + \mathcal{L}\nu - r\nu
= - \left(\frac{\partial \mathcal{L}}{\partial \sigma}V\right)
= -\sigma S^2 V_{SS}
}
$$



---

## What to remember


- The generator $\mathcal{L}$ determines the pricing PDE.
- Parameter Greeks can be viewed as sensitivities of $\mathcal{L}$ itself.
- This framework generalizes to multi-factor models.

---

## Exercises

**Exercise 1.** Verify that the generator $(\mathcal{L}f)(S) = rSf'(S) + \frac{1}{2}\sigma^2 S^2 f''(S)$ applied to $f(S) = S^n$ produces a polynomial in $S^n$. Compute $\mathcal{L}(S^2)$ and interpret the result in terms of the expected quadratic variation of $S$.

??? success "Solution to Exercise 1"
    Apply the generator to $f(S) = S^n$. We have $f'(S) = nS^{n-1}$ and $f''(S) = n(n-1)S^{n-2}$. Then:

    $$
    (\mathcal{L}f)(S) = rS \cdot nS^{n-1} + \frac{1}{2}\sigma^2 S^2 \cdot n(n-1)S^{n-2}
    $$

    $$
    = rnS^n + \frac{1}{2}\sigma^2 n(n-1)S^n = \left[rn + \frac{1}{2}\sigma^2 n(n-1)\right]S^n
    $$

    This is indeed a polynomial (monomial) in $S^n$, confirming that $S^n$ is an eigenfunction of $\mathcal{L}$ with eigenvalue $rn + \frac{1}{2}\sigma^2 n(n-1)$.

    **For $n = 2$:**

    $$
    \mathcal{L}(S^2) = \left[2r + \frac{1}{2}\sigma^2 \cdot 2 \cdot 1\right]S^2 = (2r + \sigma^2)S^2
    $$

    **Interpretation.** The quantity $\mathcal{L}(S^2)$ captures the instantaneous growth rate of $\mathbb{E}[S_t^2]$. Indeed, by the connection between the generator and expected values, $\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[f(S_t)] = \mathbb{E}[\mathcal{L}f(S_t)]$. For $f = S^2$, this gives $\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[S_t^2] = (2r + \sigma^2)\mathbb{E}[S_t^2]$. The term $\sigma^2 S^2$ reflects the quadratic variation contribution: $\mathrm{d}\langle S \rangle_t = \sigma^2 S_t^2\,\mathrm{d}t$.

---

**Exercise 2.** Starting from $\mathcal{A}V = 0$ where $\mathcal{A} = \partial_t + \mathcal{L} - r$, differentiate with respect to $\sigma$ to derive the PDE for vega: $\partial_t \nu + \mathcal{L}\nu - r\nu = -\sigma S^2 V_{SS}$. Explain why the terminal condition is $\nu(T,S) = 0$.

??? success "Solution to Exercise 2"
    Define the full pricing operator $\mathcal{A} = \partial_t + \mathcal{L}_\sigma - r$ so that the pricing PDE is $\mathcal{A}V = 0$.

    Differentiate with respect to $\sigma$. Since $\partial_t$ and $r$ do not depend on $\sigma$:

    $$
    \frac{\partial}{\partial\sigma}(\mathcal{A}V) = \mathcal{A}\left(\frac{\partial V}{\partial\sigma}\right) + \frac{\partial\mathcal{L}_\sigma}{\partial\sigma}V = 0
    $$

    Let $\nu = \frac{\partial V}{\partial\sigma}$. Then:

    $$
    \mathcal{A}\nu = -\frac{\partial\mathcal{L}_\sigma}{\partial\sigma}V
    $$

    Computing $\frac{\partial}{\partial\sigma}\mathcal{L}_\sigma f = \frac{\partial}{\partial\sigma}\!\left(\frac{1}{2}\sigma^2 S^2 f''\right) = \sigma S^2 f''$:

    $$
    \partial_t \nu + \mathcal{L}\nu - r\nu = -\sigma S^2 V_{SS}
    $$

    **Terminal condition.** At $t = T$, $V(T,S) = \Phi(S)$, which does not depend on $\sigma$. Therefore:

    $$
    \nu(T,S) = \frac{\partial}{\partial\sigma}\Phi(S) = 0
    $$

    This makes sense: at expiration, the payoff is determined entirely by $S_T$ and the strike, with no sensitivity to volatility. All vega sensitivity comes from the time value of the option, which vanishes at maturity.

---

**Exercise 3.** Consider a general diffusion with generator $\mathcal{L}_\theta f = \mu(\theta)Sf' + \frac{1}{2}\sigma(\theta)^2 S^2 f''$, where $\theta$ is a model parameter. Compute $\frac{\partial}{\partial \theta}\mathcal{L}_\theta f$ and use it to write down the PDE satisfied by the sensitivity $\partial V / \partial \theta$.

??? success "Solution to Exercise 3"
    The general generator is:

    $$
    \mathcal{L}_\theta f = \mu(\theta)Sf' + \frac{1}{2}\sigma(\theta)^2 S^2 f''
    $$

    Differentiate with respect to $\theta$:

    $$
    \frac{\partial}{\partial\theta}\mathcal{L}_\theta f = \mu'(\theta)Sf' + \sigma(\theta)\sigma'(\theta)S^2 f''
    $$

    The sensitivity $w := \frac{\partial V}{\partial\theta}$ satisfies the PDE obtained by differentiating $\mathcal{A}V = 0$ with respect to $\theta$:

    $$
    \partial_t w + \mathcal{L}_\theta w - rw = -\frac{\partial\mathcal{L}_\theta}{\partial\theta}V = -\mu'(\theta)SV_S - \sigma(\theta)\sigma'(\theta)S^2 V_{SS}
    $$

    with terminal condition $w(T,S) = 0$ (assuming the payoff does not depend on $\theta$).

    The source term on the right involves $V_S$ (delta) and $V_{SS}$ (gamma) of the original pricing problem, weighted by the parameter sensitivities $\mu'(\theta)$ and $\sigma'(\theta)$. In the standard Black-Scholes case where $\theta = \sigma$, we have $\mu(\sigma) = r$ (so $\mu' = 0$) and $\sigma(\theta) = \sigma$ (so $\sigma' = 1$), recovering the vega PDE from Exercise 2.

---

**Exercise 4.** Using the generator approach, show that theta satisfies $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma$ directly from the pricing PDE. Explain why theta does not require a separate PDE but can always be computed from other Greeks.

??? success "Solution to Exercise 4"
    The pricing PDE is:

    $$
    \frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0
    $$

    Expanding $\mathcal{L}V = rSV_S + \frac{1}{2}\sigma^2 S^2 V_{SS}$:

    $$
    \frac{\partial V}{\partial t} + rSV_S + \frac{1}{2}\sigma^2 S^2 V_{SS} - rV = 0
    $$

    Solving for $\Theta = \frac{\partial V}{\partial t}$:

    $$
    \Theta = rV - rSV_S - \frac{1}{2}\sigma^2 S^2 V_{SS} = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
    $$

    **Why theta does not need a separate PDE.** The pricing PDE is a constraint relating $V_t$, $V_S$, $V_{SS}$, and $V$. Since theta is simply $V_t$, it can always be expressed algebraically in terms of the other Greeks ($\Delta$, $\Gamma$) and the option price $V$ itself. There is no need to solve an auxiliary PDE because the Black-Scholes PDE already provides the relationship directly.

    This is in contrast to vega, which requires differentiating the PDE with respect to a parameter $\sigma$, producing a new PDE with a source term. Theta is a state derivative (with respect to $t$) that is already one of the terms in the original PDE.

---

**Exercise 5.** For the CEV (constant elasticity of variance) model with $\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t^\beta\,\mathrm{d}W_t$, write down the infinitesimal generator $\mathcal{L}^{\text{CEV}}$. How does $\frac{\partial}{\partial \sigma}\mathcal{L}^{\text{CEV}}$ differ from the Black--Scholes case?

??? success "Solution to Exercise 5"
    In the CEV model, $\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t^\beta\,\mathrm{d}W_t$. The infinitesimal generator acts on smooth functions $f$ as:

    $$
    (\mathcal{L}^{\text{CEV}}f)(S) = rSf'(S) + \frac{1}{2}\sigma^2 S^{2\beta}f''(S)
    $$

    The key difference from Black-Scholes (where $\beta = 1$) is that the diffusion coefficient is $\frac{1}{2}\sigma^2 S^{2\beta}$ instead of $\frac{1}{2}\sigma^2 S^2$.

    Differentiating with respect to $\sigma$:

    $$
    \frac{\partial}{\partial\sigma}\mathcal{L}^{\text{CEV}}_\sigma f = \sigma S^{2\beta}f''
    $$

    **Comparison with Black-Scholes.** In Black-Scholes, $\frac{\partial}{\partial\sigma}\mathcal{L}_\sigma f = \sigma S^2 f''$. In the CEV model, $S^2$ is replaced by $S^{2\beta}$. Consequently, the vega PDE for the CEV model has the source term $-\sigma S^{2\beta}V_{SS}$ instead of $-\sigma S^2 V_{SS}$.

    For $\beta < 1$ (which produces a leverage effect), the diffusion coefficient grows more slowly with $S$, so the vega source term is relatively smaller for large $S$ and relatively larger for small $S$, compared to Black-Scholes. For $\beta > 1$, the opposite holds.

---

**Exercise 6.** In a two-factor model with state variables $(S, v)$ and generator $\mathcal{L}f = rSf_S + \kappa(\bar{v}-v)f_v + \frac{1}{2}vS^2 f_{SS} + \rho\xi vS f_{Sv} + \frac{1}{2}\xi^2 v f_{vv}$, write down the pricing PDE. How many second-order Greeks appear, and which ones are captured by cross-derivatives $f_{Sv}$?

??? success "Solution to Exercise 6"
    The pricing PDE is obtained from $\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0$:

    $$
    \frac{\partial V}{\partial t} + rSV_S + \kappa(\bar{v} - v)V_v + \frac{1}{2}vS^2 V_{SS} + \rho\xi vS\,V_{Sv} + \frac{1}{2}\xi^2 v\,V_{vv} - rV = 0
    $$

    **Counting second-order Greeks.** The state variables are $(S, v)$, giving three distinct second-order partial derivatives:

    1. $V_{SS}$ -- gamma (sensitivity to spot squared)
    2. $V_{vv}$ -- volga or variance-of-variance sensitivity
    3. $V_{Sv}$ -- cross-derivative (sensitivity to joint spot-variance moves)

    So there are **three** second-order Greeks.

    **The cross-derivative $V_{Sv}$.** This Greek captures the sensitivity of the option price to simultaneous changes in spot $S$ and variance $v$. It is the analogue of vanna ($\partial^2 V / \partial S \partial \sigma$) in the Black-Scholes setting, adapted to a stochastic variance framework. The coefficient $\rho\xi vS$ multiplying $V_{Sv}$ in the PDE shows that this cross-term is driven by the correlation $\rho$ between the spot and variance Brownian motions. When $\rho = 0$ (uncorrelated spot and variance), the cross-derivative term drops out of the PDE, and the model loses its ability to generate skew in implied volatility.
