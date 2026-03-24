# Greeks via the Infinitesimal Generator


In Markov models, the infinitesimal generator provides a structural link between pricing, PDEs, and sensitivity analysis.

---

## Setup: risk-neutral diffusion


Under \(\mathbb{Q}\), consider


\[
\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t\,\mathrm{d}W_t
\]



so the generator acting on smooth test functions \(f\) is


\[
\boxed{
(\mathcal{L}f)(S) = rS f'(S) + \frac{1}{2}\sigma^2 S^2 f''(S)
}
\]



---

## Pricing PDE


For a European payoff \(\Phi\), the price


\[
V(t,S)=\mathbb{E}^{t,S}\!\left[e^{-r(T-t)}\Phi(S_T)\right]
\]



solves the backward equation


\[
\boxed{
\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0,
\qquad V(T,S)=\Phi(S)
}
\]



---

## Parameter sensitivity as generator sensitivity


Treat the generator as parameterized by \(\sigma\):


\[
\mathcal{L}_\sigma f = rS f' + \frac{1}{2}\sigma^2 S^2 f''
\]



Then vega \(\nu=V_\sigma\) is linked to the derivative of \(\mathcal{L}_\sigma\) with respect to \(\sigma\):


\[
\frac{\partial}{\partial \sigma}\mathcal{L}_\sigma f
=
\sigma S^2 f''
\]



This suggests a PDE for \(\nu\) of the form


\[
\boxed{
\frac{\partial \nu}{\partial t} + \mathcal{L}\nu - r\nu
= - \left(\frac{\partial \mathcal{L}}{\partial \sigma}V\right)
= -\sigma S^2 V_{SS}
}
\]



---

## What to remember


- The generator \(\mathcal{L}\) determines the pricing PDE.
- Parameter Greeks can be viewed as sensitivities of \(\mathcal{L}\) itself.
- This framework generalizes to multi-factor models.

---

## Exercises

**Exercise 1.** Verify that the generator $(\mathcal{L}f)(S) = rSf'(S) + \frac{1}{2}\sigma^2 S^2 f''(S)$ applied to $f(S) = S^n$ produces a polynomial in $S^n$. Compute $\mathcal{L}(S^2)$ and interpret the result in terms of the expected quadratic variation of $S$.

---

**Exercise 2.** Starting from $\mathcal{A}V = 0$ where $\mathcal{A} = \partial_t + \mathcal{L} - r$, differentiate with respect to $\sigma$ to derive the PDE for vega: $\partial_t \nu + \mathcal{L}\nu - r\nu = -\sigma S^2 V_{SS}$. Explain why the terminal condition is $\nu(T,S) = 0$.

---

**Exercise 3.** Consider a general diffusion with generator $\mathcal{L}_\theta f = \mu(\theta)Sf' + \frac{1}{2}\sigma(\theta)^2 S^2 f''$, where $\theta$ is a model parameter. Compute $\frac{\partial}{\partial \theta}\mathcal{L}_\theta f$ and use it to write down the PDE satisfied by the sensitivity $\partial V / \partial \theta$.

---

**Exercise 4.** Using the generator approach, show that theta satisfies $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma$ directly from the pricing PDE. Explain why theta does not require a separate PDE but can always be computed from other Greeks.

---

**Exercise 5.** For the CEV (constant elasticity of variance) model with $\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t^\beta\,\mathrm{d}W_t$, write down the infinitesimal generator $\mathcal{L}^{\text{CEV}}$. How does $\frac{\partial}{\partial \sigma}\mathcal{L}^{\text{CEV}}$ differ from the Black--Scholes case?

---

**Exercise 6.** In a two-factor model with state variables $(S, v)$ and generator $\mathcal{L}f = rSf_S + \kappa(\bar{v}-v)f_v + \frac{1}{2}vS^2 f_{SS} + \rho\xi vS f_{Sv} + \frac{1}{2}\xi^2 v f_{vv}$, write down the pricing PDE. How many second-order Greeks appear, and which ones are captured by cross-derivatives $f_{Sv}$?
