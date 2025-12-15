# Forward Rates and Term Structures

Forward rates describe **future borrowing/lending rates** implied by today’s yield curve. They are central to term-structure modeling, pricing FRAs/swaps, and understanding no-arbitrage dynamics.

---

## 1. Simple forward rates from discount factors

Given discount factors \(P(0,T_1)\) and \(P(0,T_2)\) with \(0<T_1<T_2\), the **simple forward rate** over \([T_1,T_2]\) is defined by
\[
1 + F(0;T_1,T_2)\,(T_2-T_1)
= \frac{P(0,T_1)}{P(0,T_2)}.
\]

Equivalently,
\[
F(0;T_1,T_2)
= \frac{1}{T_2-T_1}\left(\frac{P(0,T_1)}{P(0,T_2)} - 1\right).
\]

This is the rate that makes a forward-starting loan have zero value at time 0 under no-arbitrage.

---

## 2. Instantaneous forward rate curve

The **instantaneous forward rate** \(f(0,T)\) is defined by
\[
f(0,T) := -\frac{\partial}{\partial T}\log P(0,T).
\]

It satisfies
\[
P(0,T) = \exp\left(-\int_0^T f(0,u)\,du\right).
\]

The relationship to the continuously compounded zero rate \(z(0,T)\) is:
\[
z(0,T) = \frac{1}{T}\int_0^T f(0,u)\,du.
\]

Thus:
- zero rates are averages of forward rates,
- forward rates are local (marginal) rates.

---

## 3. Term structures as curves

A **term structure** can refer to:
- the discount factor curve \(T\mapsto P(0,T)\),
- the zero curve \(T\mapsto z(0,T)\),
- the forward curve \(T\mapsto f(0,T)\).

All contain equivalent information (given differentiability), but are used differently in practice.

---

## 4. Practical notes

- Market data are discrete; forward rates require interpolation/smoothing.
- Different interpolation choices can change forwards significantly (even if discounting is similar).
- For model building (e.g., HJM), smoothness of \(f(0,T)\) is especially important.

---

## 5. Key takeaways

- Forward rates are implied by ratios of discount factors.
- Instantaneous forward rates are derivatives of \(-\log P(0,T)\).
- Term structure representations are equivalent but numerically different.

---

## Further reading

- Brigo & Mercurio, *Interest Rate Models*.
- Filipović, *Term-Structure Models*.
