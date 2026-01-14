# Smoothness and Regularity Issues


Regularity of \(V\) and Greeks depends on:
- regularity of payoff \(\Phi\),
- ellipticity/smoothness of coefficients,
- time distance to maturity.

---

## Diffusion smoothing


Parabolic equations smooth initial/terminal data for \(t<T\). Even if \(\Phi\) is not \(C^1\), \(V(t,\cdot)\) is often smooth for \(t<T\) (away from degeneracies such as \(S=0\)).

---

## Kinks and gamma concentration


For \(\Phi(S)=(S-K)^+\), the second derivative at maturity is distributional (Dirac mass at \(K\)). For \(t<T\), diffusion replaces this by a narrow bump of width \(\mathcal{O}(\sqrt{T-t})\).

---

## American options


Free boundaries reduce regularity; viscosity solutions provide the right weak framework, and Greeks may fail to be smooth across the exercise boundary.

---

## What to remember


- Smoothness improves for \(t<T\) but deteriorates as \(t\uparrow T\).
- Payoff kinks create large gamma near maturity.
- Early exercise introduces weaker regularity and free boundary effects.
