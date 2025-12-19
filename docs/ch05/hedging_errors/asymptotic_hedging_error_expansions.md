# Asymptotic Hedging Error Expansions

One seeks expansions of hedging error in small parameters.

Examples:
- small time step \(\Delta t\):

\[
\mathrm{HE}=c_1\sqrt{\Delta t}+c_2\Delta t+\cdots,
\]


- small transaction costs \(\lambda\ll 1\): no-trade band scaling laws,
- small model error \(\varepsilon\): \(\mathrm{HE}\approx \varepsilon A_1+\varepsilon^2 A_2+\cdots\).

---

## What to remember

- Leading terms are often gamma- and quadratic-variation-driven.
- These expansions connect asymptotics to practical P\&L attribution.
