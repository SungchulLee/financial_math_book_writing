# Infinitesimal Generator and Martingales

Dynkin’s formula implies a fundamental martingale characterization.

## Martingale Associated with a Generator

For any \(f\in \mathrm{Dom}(L)\),

\[
M_t := f(X_t) - f(X_0) - \int_0^t Lf(X_s)\,ds
\]


is a martingale.

## Harmonic Functions

If

\[
Lf(x)=0 \quad \forall x,
\]


then

\[
f(X_t) \text{ is a martingale}.
\]



## Converse (Careful!)

If \(f(X_t)\) is a martingale, then

\[
Lf(X_t)=0 \quad \text{a.s. along sample paths}.
\]



This does **not** automatically imply \(Lf(x)=0\) for all \(x\)
unless additional regularity and irreducibility assumptions hold.

## Correct Characterization

Under suitable conditions:

\[
Lf(x)=0
\quad\Longleftrightarrow\quad
f(X_t)\text{ is a local martingale}.
\]



This characterization is central to:
- Martingale problems
- Probabilistic construction of diffusions
