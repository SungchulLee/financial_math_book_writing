# Bond Pricing via PDEs


In short-rate models, zero-coupon bond prices can be characterized as solutions of **partial differential equations (PDEs)**. The PDE approach provides intuition about boundary conditions and links interest-rate pricing to diffusion theory.

---

## Setup


Let \(r_t\) follow a risk-neutral short-rate diffusion

\[
dr_t = \mu^{\mathbb{Q}}(t,r_t)\,dt + \sigma(t,r_t)\,dW_t^{\mathbb{Q}}.
\]



Define the zero-coupon bond price

\[
P(t,T,r) = \text{price at }t\text{ of }1\text{ paid at }T,
\]


given \(r_t=r\).

---

## Pricing PDE


By standard arbitrage arguments, \(P(t,T,r)\) satisfies

\[
\partial_t P
+ \mu^{\mathbb{Q}}(t,r)\,\partial_r P
+ \tfrac12 \sigma(t,r)^2\,\partial_{rr}P
- rP = 0,
\]


with terminal condition

\[
P(T,T,r)=1.
\]



This PDE is backward in time.

---

## Boundary conditions


Appropriate boundary conditions depend on the model:

- as \(r\to \infty\): bond price decays to zero,
- as \(r\to -\infty\) (if allowed): growth must remain controlled,
- at boundaries like \(r=0\) (CIR): degeneracy requires careful handling.

Correct boundary treatment is crucial for numerical stability.

---

## Analytical solutions


For affine models (Vasicek, CIR):
- the PDE admits closed-form solutions,
- solutions take exponential-affine form,
- coefficients satisfy ODEs.

For more general models, numerical PDE methods are required.

---

## Numerical PDE methods


Common schemes include:
- finite differences (implicit, Crank–Nicolson),
- alternating-direction implicit (ADI) methods,
- grid truncation and stabilization techniques.

Bond PDEs are one-dimensional and relatively tractable.

---

## Key takeaways


- Bond prices satisfy linear parabolic PDEs.
- PDEs clarify boundary behavior and numerical issues.
- Closed forms arise in affine short-rate models.

---

## Further reading


- Wilmott, *Derivatives*.
- Brigo & Mercurio, bond pricing PDEs.
