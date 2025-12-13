# Explicit, Implicit, and Crank–Nicolson Schemes

After spatial discretization, write the semidiscrete system
\[
\boxed{
\frac{\mathrm{d}}{\mathrm{d}\tau}u(\tau)\approx Au(\tau),
}
\]
where \(A\) approximates the Black–Scholes spatial operator and \(u^n\approx u(\tau_n)\).

---

## 1. Explicit (Forward Euler)

\[
\boxed{
u^{n+1}=u^{n}+\Delta\tau\,A u^{n}.
}
\]
Simple, but typically requires a CFL restriction such as \(\Delta\tau\le C(\Delta S)^2\).

---

## 2. Implicit (Backward Euler)

\[
\boxed{
(I-\Delta\tau\,A)u^{n+1}=u^{n}.
}
\]
Robust and often unconditionally stable (parabolic problems), but requires a linear solve per time step.

---

## 3. Crank–Nicolson (Trapezoidal Rule)

\[
\boxed{
\left(I-\frac{\Delta\tau}{2}A\right)u^{n+1}
=
\left(I+\frac{\Delta\tau}{2}A\right)u^{n}.
}
\]
Second-order in time (formally) and widely used, but can oscillate near \(\tau=0\) for kinked payoffs.

---

## 4. Rannacher Smoothing (Practical)

Take a few initial backward Euler steps before switching to Crank–Nicolson to damp high-frequency error created by nonsmooth payoffs.

---

## 5. Theta-Scheme

\[
\boxed{
(I-\theta\Delta\tau A)u^{n+1}=(I+(1-\theta)\Delta\tau A)u^{n}.
}
\]
\(\theta=0\) explicit, \(\theta=1\) implicit, \(\theta=\tfrac12\) Crank–Nicolson.

---

## 6. What to Remember

- Explicit: cheap but time-step restricted.
- Implicit: stable but needs solves.
- Crank–Nicolson: accuracy/stability balance; smooth near maturity.
