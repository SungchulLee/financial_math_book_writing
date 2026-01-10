# Compensators and Martingales

The martingale structure of default processes is formalized using **compensators**. This perspective is essential for rigorous pricing in reduced-form credit models.

---

## 1. Default indicator process

Define the default indicator

\[
H_t := \mathbf{1}_{\{\tau \le t\}}.
\]



This is an increasing jump process that jumps from 0 to 1 at default.

---

## 2. Compensator of the default process

Under intensity \(\lambda_t\), the **compensator** of \(H_t\) is

\[
A_t := \int_0^{t \wedge \tau} \lambda_s ds.
\]



The compensated process

\[
M_t := H_t - A_t
\]


is a \((\mathcal{G}_t, \mathbb{Q})\)-martingale.

---

## 3. Role in pricing

Martingale representation allows:
- construction of arbitrage-free pricing formulas,
- derivation of pricing PDEs and expectation formulas,
- consistent treatment of default jumps.

This parallels drift removal in diffusion models.

---

## 4. Link to enlargement of filtration

Compensators arise naturally under progressive enlargement.
Immersion ensures that default does not introduce spurious drifts in market assets.

---

## 5. Key takeaways

- Default indicators admit compensators under intensity models.
- Compensated processes are martingales.
- This structure underpins arbitrage-free credit pricing.

---

## Further reading

- Jeanblanc & Le Cam, compensators in credit risk.
- Elliott et al., hidden intensity models.
