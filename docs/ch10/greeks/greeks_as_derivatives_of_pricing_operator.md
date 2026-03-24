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

---

## Exercises

**Exercise 1.** Let $\mathcal{P}_\sigma$ denote the pricing operator parameterized by volatility $\sigma$. For a European call payoff $\Phi(S_T) = (S_T - K)^+$, show that vega can be written as $\nu = \frac{\partial}{\partial \sigma}(\mathcal{P}_\sigma \Phi)(t,S)$. Explain why this is a parameter derivative rather than a state derivative.

---

**Exercise 2.** Consider the pricing operator $\mathcal{P}$ acting on the payoff $\Phi_1(x) = (x - K)^+$ and $\Phi_2(x) = x$. Compute $(\mathcal{P}\Phi_2)(t,S)$ explicitly in the Black--Scholes model and verify that $\Delta = \partial_S(\mathcal{P}\Phi_2) = 1$, as expected for a forward contract.

---

**Exercise 3.** The pricing operator $\mathcal{P}$ is linear in the payoff $\Phi$ for a fixed model. Using this linearity, express the price and delta of a straddle (long call + long put at the same strike) in terms of the pricing operator applied to the call and put payoffs individually.

---

**Exercise 4.** State derivatives (delta, gamma) and parameter derivatives (vega, rho) respond to different types of perturbations. Describe a market scenario in which parameter derivatives dominate the P&L, and another in which state derivatives dominate. What determines which class is more important for risk management?

---

**Exercise 5.** Explain how the three methods for computing $\frac{\partial}{\partial \theta}(\mathcal{P}_\theta \Phi)$ --- PDE differentiation, pathwise differentiation, and likelihood ratio --- each handle the derivative. For each method, identify one setting where it is preferred and one where it fails or is impractical.

---

**Exercise 6.** Consider a pricing operator $\mathcal{P}$ in a local volatility model where $\sigma = \sigma(S,t)$. Is vega still well-defined as $\partial_\sigma(\mathcal{P}\Phi)$? Discuss what "volatility sensitivity" means when $\sigma$ is a function rather than a parameter, and describe how bucket vega addresses this issue.
