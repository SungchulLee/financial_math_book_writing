# PDEs Satisfied by Greeks


A clean way to obtain PDEs for Greeks is to treat Greeks as solutions of **sensitivity PDEs**.

---

## Operator form


Define the Black–Scholes operator

\[
\mathcal{A}V
:=
\frac{\partial V}{\partial t}
+\frac{1}{2}\sigma^2 S^2 V_{SS}
+rS V_S
-rV.
\]


Then \(V\) solves \(\mathcal{A}V=0\).

---

## Vega


Let \(\nu=V_\sigma\). Differentiate \(\mathcal{A}V=0\) in \(\sigma\):

\[
\mathcal{A}\nu = -\sigma S^2 V_{SS}.
\]


With payoff independent of \(\sigma\),

\[
\boxed{\nu(T,S)=0.}
\]



---

## Rho


Let \(\rho=V_r\). Differentiating in \(r\) yields

\[
\boxed{
\frac{\partial \rho}{\partial t}
+\frac{1}{2}\sigma^2 S^2 \rho_{SS}
+rS\rho_S
-r\rho
=
V - S V_S,
\qquad \rho(T,S)=0.
}
\]



---

## Theta identity


From the PDE,

\[
\boxed{
\Theta
=
\frac{\partial V}{\partial t}
=
-\frac{1}{2}\sigma^2 S^2 V_{SS} - rS V_S + rV.
}
\]



---

## What to remember


- Vega and rho satisfy inhomogeneous parabolic PDEs with zero terminal data.
- Theta can be computed directly from $V,\Delta,\Gamma$ using the PDE.

---

## Exercises

**Exercise 1.** Starting from $\mathcal{A}V = 0$, differentiate with respect to $\sigma$ to obtain the vega PDE $\mathcal{A}\nu = -\sigma S^2 V_{SS}$. Explain why the right-hand side is always non-positive for a long call (where $V_{SS} = \Gamma > 0$) and what this implies about the behavior of vega.

---

**Exercise 2.** The rho PDE has source term $V - SV_S$. For an ATM call, estimate the sign and magnitude of $V - S\Delta$ and use this to explain whether rho is positive or negative.

---

**Exercise 3.** Show that theta is not an independent Greek: it can be computed algebraically from $V$, $\Delta$, and $\Gamma$ using the Black--Scholes PDE. Why does this make theta fundamentally different from delta, gamma, vega, and rho?

---

**Exercise 4.** The vega PDE $\mathcal{A}\nu = -\sigma S^2 \Gamma$ with $\nu(T,S) = 0$ can be interpreted as a backward heat equation with a source term. Using the Duhamel principle, express $\nu(t,S)$ as an integral over the remaining time involving $\Gamma$. How does this connect to the closed-form formula $\nu = S\sqrt{\tau}N'(d_1)$?

---

**Exercise 5.** Derive the PDE satisfied by the second-order Greek $\frac{\partial^2 V}{\partial \sigma^2}$ (volga) by differentiating the vega PDE with respect to $\sigma$. What is the source term, and what is the terminal condition?

---

**Exercise 6.** In a model where the interest rate $r$ is stochastic, the operator $\mathcal{A}$ itself depends on $r$. Explain qualitatively how the PDE for rho would change, and why the simple identity $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma$ may no longer hold.
