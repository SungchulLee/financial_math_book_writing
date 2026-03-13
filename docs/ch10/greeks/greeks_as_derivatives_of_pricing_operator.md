# Greeks as Derivatives of the Pricing Operator


A mathematically clean viewpoint is: pricing is an **operator** that maps a payoff to a function of \((t,S)\), and Greeks are derivatives of that operator with respect to inputs.

---

## Pricing as an operator


For a European payoff \(\Phi(S_T)\) under a risk-neutral model, define the pricing operator


\[
(\mathcal{P}\Phi)(t,S)
:=
\mathbb{E}^{t,S}\!\left[e^{-r(T-t)}\Phi(S_T)\right]
\]



Then the option price is


\[
V(t,S) = (\mathcal{P}\Phi)(t,S)
\]



---

## State derivatives vs parameter derivatives


- **State derivatives**: \(\partial_S(\mathcal{P}\Phi)\), \(\partial_S^2(\mathcal{P}\Phi)\) correspond to \(\Delta,\Gamma\).
- **Parameter derivatives**: \(\partial_\sigma(\mathcal{P}\Phi)\), \(\partial_r(\mathcal{P}\Phi)\) correspond to vega and rho.

This separation matters because:

- state derivatives reflect geometry of \(V\) as a function of \(S\),
- parameter derivatives reflect sensitivity of the law of \(S_T\) to parameter changes.

---

## Differentiation under the expectation


Formally, for a parameter \(\theta\),


\[
\frac{\partial}{\partial \theta}(\mathcal{P}_\theta\Phi)
=
\frac{\partial}{\partial \theta}
\mathbb{E}^{t,S}_\theta\!\left[e^{-r(T-t)}\Phi(S_T)\right]
\]



The derivative can be handled by:

- differentiating the PDE satisfied by \(V\),
- differentiating the stochastic flow \(S_T^{\theta}\) (pathwise differentiation),
- changing measure or using likelihood ratio (score) identities.

Each method leads to a distinct “representation formula” for Greeks.

---

## Functional-analytic analogy


Think of \(\mathcal{P}\) as a linear map (for fixed model) acting on payoffs:


\[
\Phi \mapsto V(\cdot,\cdot)
\]



Greeks are then derivatives of \(\mathcal{P}\Phi\) with respect to:

- the spatial variable \(S\),
- parameters of the operator \(\mathcal{P}\).

---

## What to remember


- The pricing map is an operator \(\mathcal{P}\).
- Greeks are derivatives of \(\mathcal{P}\Phi\) with respect to state variables and model parameters.
- PDE, probabilistic, and measure-theoretic approaches give complementary Greek formulas.
