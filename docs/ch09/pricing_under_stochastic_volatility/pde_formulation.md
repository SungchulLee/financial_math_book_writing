# PDE Formulation


Stochastic volatility models also admit a **partial differential equation (PDE)** formulation for option pricing. The PDE perspective is useful for theoretical analysis, boundary conditions, and for pricing products not well-suited to Fourier methods.

---

## Risk-neutral pricing PDE


Let \(V(t,s,v)\) be the price at time \(t\) when \(S_t=s\) and \(V_t=v\).
Under standard regularity conditions and risk-neutral dynamics, \(V\) satisfies

\[
\partial_t V + \mathcal{L}V - rV = 0,
\]


with terminal condition \(V(T,s,v)=\Phi(s)\), where \(\Phi\) is the payoff.

---

## Generator for a two-factor diffusion


For a generic two-factor model

\[
\begin{aligned}
dS_t &= (r-q)s\,dt + \sqrt{v}\,s\,dW_t^S,\\
dV_t &= a(v,t)\,dt + b(v,t)\,dW_t^V,\\
d\langle W^S,W^V\rangle_t &= \rho\,dt,
\end{aligned}
\]


the generator \(\mathcal{L}\) typically takes the form

\[
\mathcal{L}V =
(r-q)s\,\partial_s V + a(v,t)\,\partial_v V
+ \tfrac12 v s^2\,\partial_{ss}V
+ \tfrac12 b(v,t)^2\,\partial_{vv}V
+ \rho b(v,t) s\sqrt{v}\,\partial_{sv}V.
\]



(For Heston, \(a(v,t)=\kappa(\theta-v)\) and \(b(v,t)=\xi\sqrt{v}\).)

---

## Boundary conditions


PDE pricing requires boundary conditions in:
- asset price \(s\),
- variance \(v\),
- time \(t\).

Typical choices:
- as \(s\to 0\), call value tends to 0,
- as \(s\to \infty\), call behaves like \(s e^{-q\tau} - K e^{-r\tau}\),
- at \(v=0\), degeneracy requires careful treatment (linked to Feller behavior).

---

## When PDE methods are preferred


PDE methods are useful for:
- American-style features (early exercise),
- barriers (path-dependent in \(S\)),
- models without tractable characteristic functions,
- local-stochastic volatility hybrids (often PDE-based).

---

## Key takeaways


- Stochastic volatility pricing can be expressed as a two-dimensional PDE.
- PDE methods complement Fourier methods, especially for complex payoffs.
- Boundary handling (especially near \(v=0\)) is central to stability.

---

## Further reading


- Wilmott, *Derivatives* (PDE methods).
- Itkin, *Pricing Derivatives Under Stochastic Volatility*.
- Heston PDE treatments and numerical schemes (ADI, finite differences).
