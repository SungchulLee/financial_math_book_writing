# Recovery Schemes


Recovery assumptions specify what is paid to investors upon default. They are crucial modeling choices that significantly affect prices and credit spreads.

---

## Common recovery conventions


Three standard recovery schemes are widely used:

- **Recovery of face value (RFV):**
  A fixed fraction of par is paid at default.
- **Recovery of market value (RMV):**
  A fraction of the bond’s pre-default market value is recovered.
- **Recovery of treasury (RT):**
  A fraction of the risk-free bond value is recovered.

---

## Modeling implications


Different recovery schemes imply different pricing formulas:
- RFV introduces jump losses independent of rates,
- RMV leads to multiplicative losses and analytical simplifications,
- RT ties recovery to interest-rate dynamics.

Choice affects calibration and spread term structure.

---

## Empirical considerations


Empirically:
- recovery rates vary across sectors and seniority,
- they are stochastic and correlated with default risk,
- constant recovery is a simplification.

Nonetheless, constant recovery is standard in practice.

---

## Interaction with intensity


Under intensity models:
- recovery assumptions interact with default intensity,
- spreads depend on both hazard rate and recovery level,
- identifiability issues may arise.

Often, recovery is fixed to stabilize calibration.

---

## Key takeaways


- Recovery assumptions materially affect prices.
- RFV, RMV, and RT are standard conventions.
- Simplicity often outweighs realism in practice.

---

## Further reading


- Duffie & Singleton, recovery modeling.
- O'Kane, recovery assumptions in CDS.
