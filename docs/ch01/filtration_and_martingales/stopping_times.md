# Stopping Times

## Definition

A random time \(\tau:\Omega\to[0,\infty]\) is a **stopping time** with respect to \((\mathcal{F}_t)\) if


$$
\boxed{
\{\tau\le t\}\in \mathcal{F}_t \quad \text{for all } t\ge 0.
}
$$




Interpretation: by time \(t\), one can decide whether \(\tau\) has occurred.

Equivalent characterizations:

- \(\{\tau < t\}\in\mathcal{F}_t\) for all \(t>0\),
- \(\{\tau \le t\}\in\mathcal{F}_t\) for all \(t\ge 0\).

---

## Examples

### Deterministic times
For fixed \(t_0\ge 0\), \(\tau(\omega)=t_0\) is a stopping time.

### Hitting times
For an adapted continuous process \(X_t\) and a Borel set \(A\subset\mathbb{R}^d\), define


$$
\tau_A := \inf\{t\ge 0: X_t\in A\}.
$$




If \(X\) has continuous paths and is adapted, then \(\tau_A\) is a stopping time.

In particular for Brownian motion \(W_t\) and \(a\in\mathbb{R}\),


$$
\tau_a := \inf\{t\ge 0: W_t=a\}
$$




is a stopping time.

---

## Stopped processes

Given a process \(X_t\) and a stopping time \(\tau\), define the **stopped process**


$$
X_t^{\tau} := X_{t\wedge \tau}.
$$




If \(X\) is adapted, then \(X^{\tau}\) is adapted. If \(X\) is a (local) martingale, then \(X^{\tau}\) is again a (local) martingale under suitable integrability/boundedness.

---

## \(\sigma\)-algebra at a stopping time

Define


$$
\mathcal{F}_{\tau} := \{A\in\mathcal{F}: A\cap\{\tau\le t\}\in\mathcal{F}_t \text{ for all } t\ge 0\}.
$$




This is the information available “up to time \(\tau\)”.

A key fact: if \(X\) is adapted and right-continuous, then \(X_{\tau}\) is \(\mathcal{F}_{\tau}\)-measurable (when \(\tau<\infty\)).

---

## Strong Markov property (for Brownian motion)

If \(\tau\) is a stopping time, then Brownian motion satisfies:


$$
\boxed{
\{W_{\tau+t}-W_{\tau}\}_{t\ge 0}
\text{ is independent of }\mathcal{F}_{\tau}
\text{ and is a Brownian motion.}
}
$$




This property is central for exit/hitting problems and PDE boundary value problems.
