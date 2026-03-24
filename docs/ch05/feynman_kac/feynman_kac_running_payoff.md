# Feynman Kac Running


Let \(X_t\) be a diffusion with generator \(L\). Let

- \(f(x)\): terminal payoff
- \(r(x,t)\): discount/killing rate
- \(g(x,t)\): running payoff (source term)

---

## Statement General


Define

\[
u(x,t)=\mathbb E\!\left[
\exp\!\Big(-\int_t^T r(X_s,s)\,ds\Big)f(X_T)
+
\int_t^T \exp\!\Big(-\int_t^s r(X_\tau,\tau)\,d\tau\Big)g(X_s,s)\,ds
\,\middle|\,X_t=x
\right].
\]



Then \(u\) solves

\[
u_t + Lu - r\,u + g = 0,
\qquad
u(x,T)=f(x).
\]



---

## Proof augmented


Let

\[
Z_s=\exp\!\Big(-\int_t^s r(X_u,u)\,du\Big),\qquad dZ_s=-r(X_s,s)Z_s\,ds.
\]



Assume \(u\in C^{1,2}\) solves the PDE. Define

\[
Y_s := Z_s u(X_s,s) + \int_t^s Z_\tau\,g(X_\tau,\tau)\,d\tau.
\]



Compute \(dY_s\). Using Itô + product rule:

\[
d(Z_su(X_s,s))
=
Z_s(u_t+Lu-r\,u)(X_s,s)\,ds
+
Z_s\sigma u_x\,dW_s.
\]


Adding \(d\left(\int_t^s Z_\tau g(X_\tau,\tau)\,d\tau\right)=Z_sg(X_s,s)\,ds\), we get

\[
dY_s
=
Z_s\big(u_t+Lu-r\,u+g\big)(X_s,s)\,ds
+
Z_s\sigma u_x\,dW_s.
\]


By the PDE the drift is zero, hence \(Y_s\) is a local martingale.

Taking expectations from \(t\) to \(T\) yields

\[
u(x,t)=\mathbb E^{x,t}\!\left[
Z_T f(X_T) + \int_t^T Z_s g(X_s,s)\,ds
\right],
\]


which is exactly the stated representation.

---

## Interpretation


- \(g\) acts as a **source term** (like heat generation).
- \(r\) acts as **discounting** (finance) or **killing** (probability/physics).

---

## Exercises

**Exercise 1.**
Consider the PDE $u_t + \frac{1}{2}\sigma^2 u_{xx} - ru + g(x) = 0$ with $u(T, x) = 0$ and constant $r$, $g(x) = 1$. Use the Feynman-Kac representation with running payoff to write $u(t, x)$ as an expectation. Evaluate explicitly for the process $dX_s = \sigma\,dW_s$.

---

**Exercise 2.**
A bond with continuous coupon payments at rate $c$ has value $V(t, r) = \mathbb{E}[\int_t^T e^{-\int_t^s r_u\,du}\,c\,ds + e^{-\int_t^T r_u\,du} | r_t = r]$. Write the PDE that $V$ satisfies. Identify the running payoff $g = c$, the terminal payoff $f = 1$, and the discounting rate.

---

**Exercise 3.**
In the proof sketch, the process $Y_s = Z_s u(X_s, s) + \int_t^s Z_\tau g(X_\tau, \tau)\,d\tau$ is claimed to be a local martingale. Show that when the PDE $u_t + \mathcal{L}u - ru + g = 0$ holds, the drift of $Y_s$ vanishes. Identify where the running payoff $g$ cancels.

---

**Exercise 4.**
A derivative pays a continuous dividend at rate $q S_t$ (proportional to the stock price) plus a terminal payoff $g(S_T)$. Write the Feynman-Kac representation with both running and terminal payoffs, and derive the corresponding PDE.

---

**Exercise 5.**
Show that the running payoff formula reduces to the discounted Feynman-Kac formula when $g = 0$ (no running payoff). Show that it reduces to a pure annuity-like formula when $f = 0$ (no terminal payoff) and $g$ is constant.

---

**Exercise 6.**
Consider $u_t + \mu u_x + \frac{1}{2}\sigma^2 u_{xx} + g(x, t) = 0$ (no discounting, $r = 0$) with $u(T, x) = 0$. Write the Feynman-Kac representation and verify that $u(t, x) = \mathbb{E}[\int_t^T g(X_s, s)\,ds | X_t = x]$. Compute explicitly for $g(x, t) = x$ and $dX_s = \mu\,ds + \sigma\,dW_s$.

---

**Exercise 7.**
In mathematical physics, the source term $g(x,t)$ represents heat generation at rate $g$ in a medium with thermal diffusivity $\sigma^2/2$. The killing term $-ru$ represents heat loss proportional to temperature. Give the financial analogues of each term and explain why the general Feynman-Kac formula with all terms ($\mathcal{L}u$, $-ru$, $f$, $g$) is needed for realistic derivative pricing.
