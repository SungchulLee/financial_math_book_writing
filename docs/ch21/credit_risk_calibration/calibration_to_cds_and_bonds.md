# Calibration to CDS and Bonds


In practice, credit models are calibrated jointly to **CDS spreads** and **bond prices**, requiring consistency across instruments.

---

## CDS-based calibration


CDS are preferred calibration instruments because:
- they isolate default risk,
- they are relatively liquid,
- they are less affected by funding and coupon effects.

Thus, CDS-implied hazard rates are often taken as primary inputs.

---

## Bond pricing consistency


Bond prices reflect:
- default risk,
- interest rates,
- liquidity and funding premia.

After calibrating to CDS, bond prices are used as a validation check or secondary calibration target.

---

## Joint calibration challenges


Joint calibration faces:
- conflicting signals between CDS and bonds,
- liquidity differences,
- model limitations (constant recovery, flat intensities).

Perfect consistency is rarely achievable.

---

## Practical compromises


Practitioners often:
- calibrate primarily to CDS,
- allow bond pricing errors within tolerances,
- introduce bond-specific spreads or adjustments.

This reflects real-market frictions.

---

## Key takeaways


- CDS are the main calibration instruments.
- Bonds provide consistency checks.
- Market frictions prevent perfect joint fit.

---

## Further reading


- Duffie & Singleton, CDS vs bond spreads.
- O'Kane, practical credit calibration.
