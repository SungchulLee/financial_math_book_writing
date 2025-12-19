# Greeks via the Infinitesimal Generator

In Markov models, the infinitesimal generator provides a structural link between pricing, PDEs, and sensitivity analysis.

---

## Setup: risk-neutral diffusion

Under \(\mathbb{Q}\), consider


\[
\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t\,\mathrm{d}W_t,
\]



so the generator acting on smooth test functions \(f\) is


\[
\boxed{
(\mathcal{L}f)(S) = rS f'(S) + \frac{1}{2}\sigma^2 S^2 f''(S).
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
\qquad V(T,S)=\Phi(S).
}
\]



---

## Parameter sensitivity as generator sensitivity

Treat the generator as parameterized by \(\sigma\):


\[
\mathcal{L}_\sigma f = rS f' + \frac{1}{2}\sigma^2 S^2 f''.
\]



Then vega \(\nu=V_\sigma\) is linked to the derivative of \(\mathcal{L}_\sigma\) with respect to \(\sigma\):


\[
\frac{\partial}{\partial \sigma}\mathcal{L}_\sigma f
=
\sigma S^2 f''.
\]



This suggests a PDE for \(\nu\) of the form


\[
\boxed{
\frac{\partial \nu}{\partial t} + \mathcal{L}\nu - r\nu
= - \left(\frac{\partial \mathcal{L}}{\partial \sigma}V\right)
= -\sigma S^2 V_{SS}.
}
\]



---

## What to remember

- The generator \(\mathcal{L}\) determines the pricing PDE.
- Parameter Greeks can be viewed as sensitivities of \(\mathcal{L}\) itself.
- This framework generalizes to multi-factor models.
