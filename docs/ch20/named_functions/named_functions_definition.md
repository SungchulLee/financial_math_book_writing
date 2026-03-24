# Hull-White Named Functions

This page collects all the named functions used in the Hull-White model for quick reference.

## τ

$$\tau=T-t$$

## θ

$$\begin{array}{lllllll}
\displaystyle
\theta(t)
&=&\displaystyle
f(0,t)+\frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t}
+
\frac{\sigma^2}{2\lambda^2}\left(1-e^{-2\lambda t}\right)\\
\displaystyle
\theta^\mathbb{T}(t)
&=&\displaystyle\theta(t)+\frac{\sigma^2}{\lambda}B(T-t)\\
\end{array}$$

## ψ

$$\begin{array}{lllllll}
\psi(t)
&=&\displaystyle
r(0)e^{-\lambda t}+\lambda\int_0^t\theta(t')e^{-\lambda(t-t')}dt'
&=&\displaystyle
f(0,t)+\frac{\lambda\sigma^2}{2}B^2(t)\\
\psi(t_0,t)
&=&\displaystyle
r(t_0)e^{-\lambda (t-t_0)}+\lambda\int_{t_0}^t\theta(t')e^{-\lambda(t-t')}dt'
\\
\psi^\mathbb{T}(t_0,t)
&=&\displaystyle
r(t_0)e^{-\lambda (t-t_0)}+\lambda\int_{t_0}^t\theta^\mathbb{T}(t')e^{-\lambda(t-t')}dt'
\\
\end{array}$$

## σ_r², μ_r

$$\begin{array}{lllll}
\displaystyle
\sigma_r^2(t)
&=&\displaystyle
-\frac{1}{2}\sigma^2 B(2t)\\
\displaystyle
\sigma_r^2(t_0,t)
&=&\displaystyle
-\frac{1}{2}\sigma^2 B(2(t-t_0))
\end{array}$$

$$\begin{array}{lllll}
\displaystyle
\mu_r(t)
&=&\displaystyle
\psi(t)\\
\displaystyle
\mu_r(t_0,t)
&=&\displaystyle
\psi(t_0,t)\\
\displaystyle
\mu^\mathbb{T}_r(t_0,t)
&=&\displaystyle
\psi^\mathbb{T}(t_0,t)\\
\end{array}$$

## A, B

$$\begin{array}{lllllll}
A(\tau)&=&A(0,\tau)
&=&\displaystyle
-\frac{\sigma^2}{4\lambda^3}
\left(3-2\lambda\tau-4e^{-\lambda\tau}+e^{-2\lambda\tau}\right)
+
\lambda\int_0^\tau\theta(T-\tau')B(\tau')d\tau'
\\
B(\tau)&=&B(0,\tau)
&=&\displaystyle
-\frac{1-e^{-\lambda\tau}}{\lambda}
\\
\end{array}$$

### Characteristic Function Version

$$\begin{array}{lllll}
\displaystyle
A(u,\tau)
&=&\displaystyle
-\frac{\sigma^2}{4\lambda^3}\left[(1+iu\lambda)\left[
    3-4e^{-\lambda \tau}+e^{-2\lambda \tau}
    - iu\lambda\left(1-e^{-2\lambda \tau}\right)
    \right]-2\lambda\tau\right]
+\lambda\int_0^\tau\theta(T-\tau')B(u,\tau')d\tau'\\
\displaystyle
B(u,\tau)
&=&\displaystyle
-\frac{1-(1+iu\lambda) e^{-\lambda \tau}}{\lambda}
=iue^{-\lambda\tau}+B(\tau)\\
\end{array}$$

### Decomposition Version

$$\begin{array}{lllll}
\displaystyle
\tilde{A}(u,\tau)
&=&\displaystyle
-\frac{\sigma^2}{4\lambda^3}\left(3-2\lambda\tau-4e^{-\lambda\tau}+e^{-2\lambda\tau}+2iu\lambda\left(1-e^{-\lambda\tau}\right)^2+u^2\lambda^2\left(1-e^{-2\lambda\tau}\right)\right)
\\
\displaystyle
\tilde{B}(u,\tau)
&=&\displaystyle
B(u,\tau)\\
\end{array}$$

---

## Exercises

**Exercise 1.** Verify that $B(\tau) \to \tau$ as $\lambda \to 0$ by expanding $e^{-\lambda\tau}$ in a Taylor series. Identify the first correction term and estimate the relative error when $\lambda = 0.05$ and $\tau = 2$.

---

**Exercise 2.** Show that the two expressions for $\psi(t)$ are equivalent: starting from $\psi(t) = r(0)e^{-\lambda t} + \lambda\int_0^t \theta(t')e^{-\lambda(t-t')}dt'$, substitute the formula for $\theta(t)$ and simplify to obtain $\psi(t) = f(0,t) + \frac{\lambda\sigma^2}{2}B^2(t)$.

---

**Exercise 3.** The variance formula uses $\sigma_r^2(t) = -\frac{1}{2}\sigma^2 B(2t)$. Verify that this equals $\frac{\sigma^2}{2\lambda}(1-e^{-2\lambda t})$ by substituting the definition of $B$. Explain why the negative sign appears in the compact form.

---

**Exercise 4.** For $\lambda = 0.05$ and $\sigma = 0.01$, compute numerically $B(\tau)$, $\sigma_r^2(t)$, and $A(\tau)$ at $\tau = 1, 5, 10, 30$ years. Describe the qualitative behavior of each function as $\tau$ increases.

---

**Exercise 5.** The characteristic function version introduces a complex parameter $u$. Show that setting $u = 0$ in $B(u,\tau)$ recovers $B(\tau)$, and setting $u = 0$ in $A(u,\tau)$ recovers $A(\tau)$.

---

**Exercise 6.** Derive the relationship $B(2\tau) = B(\tau)(2 - \lambda B(\tau))$ directly from the definition $B(\tau) = -\frac{1 - e^{-\lambda\tau}}{\lambda}$. Under what circumstances is this identity useful for numerical computation?

---

**Exercise 7.** The decomposition version defines $\tilde{A}(u,\tau)$ and $\tilde{B}(u,\tau)$. Explain the role of the decomposition $r(t) = \tilde{r}(t) + \psi(t)$ in simplifying the characteristic function, and verify that $\tilde{B}(u,\tau) = B(u,\tau)$.
