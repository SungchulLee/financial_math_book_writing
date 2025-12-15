# Credit Default Swaps (CDS)

A **Credit Default Swap (CDS)** is the fundamental traded instrument for transferring and pricing credit risk. It provides insurance against the default of a reference entity.

---

## 1. Contract structure

A CDS involves two legs:

- **Protection leg:** pays compensation if default occurs.
- **Premium leg:** periodic payments made until default or maturity.

The contract references:
- a notional amount,
- a maturity \(T\),
- a reference entity,
- a recovery convention.

---

## 2. Protection leg

If default occurs at time \(\tau \le T\), the protection seller pays
\[
(1 - R) \times \text{Notional},
\]
where \(R\) is the recovery rate.

Settlement can be:
- physical (delivery of bonds),
- cash (par minus recovery value).

---

## 3. Premium leg

The protection buyer pays a fixed **CDS spread** \(s\) on scheduled dates until default or maturity:
\[
\sum_i s \, \Delta_i \, \mathbf{1}_{\{\tau > t_i\}},
\]
where \(\Delta_i\) are accrual fractions.

Accrued premium is paid if default occurs between payment dates.

---

## 4. Pricing principle

At inception, the CDS spread is set so that:
\[
\text{PV(premium leg)} = \text{PV(protection leg)}.
\]

This no-arbitrage condition determines the fair CDS spread.

---

## 5. Key takeaways

- CDS transfer default risk without funding the bond.
- Pricing balances premium and protection legs.
- CDS are central to credit market pricing.

---

## Further reading

- O'Kane, *Modelling Single-name Credit Derivatives*.
- Duffie & Singleton, CDS pricing.
