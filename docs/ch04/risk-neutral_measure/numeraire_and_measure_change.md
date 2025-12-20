# Numéraire and Change of Measure

Changing the numéraire provides an alternative and often simpler way to construct
equivalent pricing measures.

---

## Numéraire Concept

A **numéraire** is any strictly positive traded asset used as the unit of account.

Examples:
- money market account,
- zero-coupon bond,
- foreign currency.

---

## General Pricing Rule

Let \(N_t\) be a numéraire. A probability measure \(\mathbb{Q}^N\) is associated with \(N_t\)
if, for any traded asset \(S_t\),
\[
\frac{S_t}{N_t}
\]
is a martingale under \(\mathbb{Q}^N\).

---

## Relation to Risk-Neutral Measure

- Using the money market account as numéraire gives the standard risk-neutral measure.
- Using a bond as numéraire yields a forward measure.

All such measures are equivalent but correspond to different units of valuation.

---

## Measure Change Between Numéraires

If \(N_t\) and \(M_t\) are two numeraires, the corresponding measures satisfy
\[
\frac{d\mathbb{Q}^N}{d\mathbb{Q}^M}
\propto \frac{M_T / M_0}{N_T / N_0}.
\]

This formula allows direct transitions between pricing measures.

---

## Importance in Finance

Numéraire techniques:
- simplify pricing formulas,
- clarify symmetry between assets,
- underpin forward and terminal measures.

They will be used extensively in interest-rate and multi-currency models.
