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

---

## Exercises

**Exercise 1.** Consider the Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$. Write down the bond pricing PDE for $P(t,T,r)$ explicitly in terms of $\kappa$, $\theta$, and $\sigma$. Verify that the terminal condition $P(T,T,r) = 1$ is satisfied by the known Vasicek closed-form solution.

---

**Exercise 2.** Explain why the bond pricing PDE is **backward** in time. Describe the change of variable $\tau = T - t$ and rewrite the PDE as a forward equation in $\tau$. What is the initial condition in terms of $\tau$?

---

**Exercise 3.** For the CIR model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}$, the diffusion coefficient vanishes at $r = 0$. Discuss the type of boundary condition required at $r = 0$ and explain how the Feller condition $2\kappa\theta \geq \sigma^2$ affects boundary behavior. What happens to the PDE solution when the Feller condition is violated?

---

**Exercise 4.** Show that if $P(t,T,r) = e^{A(t,T) + B(t,T)\,r}$ (exponential-affine form), substitution into the general bond pricing PDE yields a system of ODEs for $A$ and $B$ when the drift and diffusion are affine in $r$:

$$
\mu^{\mathbb{Q}}(t,r) = a(t) + b(t)\,r, \qquad \sigma(t,r)^2 = c(t) + d(t)\,r
$$

Derive the ODEs and their terminal conditions.

---

**Exercise 5.** Consider the Crank--Nicolson finite difference scheme applied to the bond pricing PDE on a uniform grid in $(t, r)$ with spacing $\Delta t$ and $\Delta r$. Write out the scheme explicitly. Under what conditions on the ratio $\sigma^2 \Delta t / (\Delta r)^2$ does the scheme remain stable? Compare the order of accuracy with a fully implicit scheme.

---

**Exercise 6.** A zero-coupon bond in the Vasicek model has price $P(t,T,r) = e^{A(\tau) + B(\tau)\,r}$ where $\tau = T - t$,

$$
B(\tau) = \frac{1 - e^{-\kappa \tau}}{\kappa}
$$

and $A(\tau)$ is known. Verify that as $r \to \infty$, $P \to 0$ (provided $B(\tau) < 0$) and interpret this boundary condition economically.

---

**Exercise 7.** Suppose you need to price a 30-year zero-coupon bond under a short-rate model that does not admit a closed-form solution. Design a finite difference grid by specifying: (a) the range of $r$ values to use, (b) the grid spacing in both $r$ and $t$, and (c) the boundary conditions at the edges of the $r$-grid. Discuss how you would verify the accuracy of your numerical solution.
