# Identifiability Issues

Credit risk calibration suffers from **identifiability problems**, especially when multiple parameters affect prices in similar ways.

---

## 1. Recovery vs hazard rate trade-off

A central identifiability issue is:
- higher hazard rate + higher recovery
- vs lower hazard rate + lower recovery.

Both can fit the same CDS spreads.

---

## 2. Limited market information

Challenges include:
- sparse maturity coverage,
- illiquidity in stressed markets,
- noisy quotes.

This limits the information content of calibration targets.

---

## 3. Consequences in practice

Poor identifiability leads to:
- unstable parameter estimates,
- sensitivity to small quote changes,
- misleading economic interpretation.

These are intrinsic inverse-problem features.

---

## 4. Mitigation strategies

Stability is improved by:
- fixing recovery rates,
- restricting parameter dynamics,
- smoothing hazard rate curves,
- prioritizing robust fits.

---

## 5. Key takeaways

- Identifiability issues are inherent in credit calibration.
- Recovery and intensity are weakly separable.
- Stability often outweighs theoretical precision.

---

## Further reading

- Engl et al., inverse problems.
- Cont, model uncertainty in credit.
