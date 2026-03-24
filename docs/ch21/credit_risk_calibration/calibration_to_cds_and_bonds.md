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

---

## Exercises

**Exercise 1.** A corporate issuer has a 5-year CDS spread of 120 bp and a 5-year bond trading at a spread of 150 bp over the risk-free rate. Assuming $R = 40\%$, compute the hazard rate implied by each instrument. Explain why the two estimates differ and which source of default risk information is considered more reliable for calibration purposes.

---

**Exercise 2.** Describe three specific frictions that prevent perfect consistency between CDS-implied and bond-implied hazard rates. For each friction, state whether it causes the bond spread to overstate or understate the pure credit component relative to the CDS spread.

---

**Exercise 3.** A practitioner calibrates a hazard rate curve to CDS spreads and then computes model bond prices. The model underprices a 7-year bond by 80 cents on the dollar relative to the market. Propose two adjustments the practitioner might introduce to reconcile the bond price without disturbing the CDS calibration.

---

**Exercise 4.** Explain why CDS contracts are preferred over bonds as the primary calibration instrument for reduced-form credit models. In your answer, discuss the roles of funding risk, coupon effects, and liquidity.

---

**Exercise 5.** In a joint calibration, a modeler minimizes

$$
w_{\text{CDS}} \sum_{i} \left(s_i^{\text{model}} - s_i^{\text{market}}\right)^2 + w_{\text{bond}} \sum_{j} \left(P_j^{\text{model}} - P_j^{\text{market}}\right)^2
$$

Discuss how the choice of weights $w_{\text{CDS}}$ and $w_{\text{bond}}$ affects the calibrated hazard rates. What economic rationale would justify setting $w_{\text{CDS}} \gg w_{\text{bond}}$?

---

**Exercise 6.** During a credit crisis, CDS spreads widen sharply but bond prices remain relatively stable due to illiquidity in the bond market. Describe the challenge this presents for joint calibration. How might a practitioner handle conflicting signals from the two markets?
