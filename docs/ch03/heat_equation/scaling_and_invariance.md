# Scaling and Invariance Properties

The heat equation possesses a characteristic scaling that reflects the nature of diffusion.

---

## Parabolic Scaling

If \(u(t,x)\) solves the heat equation, then for any \(\lambda > 0\),
\[
u_\lambda(t,x) := u(\lambda^2 t, \lambda x)
\]
also solves the heat equation.

This scaling shows that:
- Time scales like space squared
- Large spatial moves require long times

---

## Connection to Brownian Scaling

Brownian motion satisfies the scaling property
\[
(B_t)_{t \ge 0}
\;\overset{d}{=}\;
(\lambda^{-1} B_{\lambda^2 t})_{t \ge 0}.
\]

The identical scaling structure explains why the heat equation governs the evolution
of Brownian distributions.

---

## Dimensional Interpretation

Diffusion is fundamentally different from transport:
- Transport: \(x \sim t\)
- Diffusion: \(x \sim \sqrt{t}\)

This distinction underlies many qualitative features of parabolic PDEs
and stochastic processes.
