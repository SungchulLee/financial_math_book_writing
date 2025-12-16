# Greeks via Feynman–Kac

Feynman–Kac represents prices as expectations and can yield expectation representations for Greeks.

---

## Price

Under \(\mathbb{Q}\),

\[
\mathrm{d}S_t=rS_t\,\mathrm{d}t+\sigma S_t\,\mathrm{d}W_t,
\qquad
V(t,S)=\mathbb{E}^{t,S}\!\left[e^{-r(T-t)}\Phi(S_T)\right].
\]



---

## Delta via the stochastic flow (formal)

In Black–Scholes,

\[
S_T = S \exp\!\left((r-\tfrac12\sigma^2)\tau+\sigma(W_T-W_t)\right),
\quad \tau=T-t,
\]


so

\[
\boxed{\frac{\partial S_T}{\partial S}=\frac{S_T}{S}.}
\]


For sufficiently smooth \(\Phi\),

\[
\boxed{
\Delta(t,S)=\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{S_T}{S}\right].
}
\]



---

## Gamma is delicate

For kinked \(\Phi\), \(\Phi''\) is distributional. One often prefers PDE-based gamma or likelihood ratio identities.

---

## What to remember

- Delta can often be written as an expectation involving the Jacobian \(\partial S_T/\partial S\).
- Gamma requires more care when payoffs are nonsmooth.
