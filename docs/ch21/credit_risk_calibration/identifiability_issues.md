# Identifiability Issues


Credit risk calibration suffers from **identifiability problems**, especially when multiple parameters affect prices in similar ways.

---

## Recovery vs hazard rate trade-off


A central identifiability issue is:
- higher hazard rate + higher recovery
- vs lower hazard rate + lower recovery.

Both can fit the same CDS spreads.

---

## Limited market information


Challenges include:
- sparse maturity coverage,
- illiquidity in stressed markets,
- noisy quotes.

This limits the information content of calibration targets.

---

## Consequences in practice


Poor identifiability leads to:
- unstable parameter estimates,
- sensitivity to small quote changes,
- misleading economic interpretation.

These are intrinsic inverse-problem features.

---

## Mitigation strategies


Stability is improved by:
- fixing recovery rates,
- restricting parameter dynamics,
- smoothing hazard rate curves,
- prioritizing robust fits.

---

## Key takeaways


- Identifiability issues are inherent in credit calibration.
- Recovery and intensity are weakly separable.
- Stability often outweighs theoretical precision.

---

## Further reading


- Engl et al., inverse problems.
- Cont, model uncertainty in credit.

---

## Exercises

**Exercise 1.** A 5-year CDS spread is 90 bp. Show that the parameter pairs $(\lambda = 1.5\%, R = 40\%)$ and $(\lambda = 1.29\%, R = 30\%)$ both approximately reproduce this spread using $s \approx (1 - R)\lambda$. What does this imply about the uniqueness of the calibrated parameters?

---

**Exercise 2.** Suppose a calibration procedure recovers hazard rates $\lambda_1 = 120$ bp and $\lambda_2 = 180$ bp from two CDS maturities. A small change in the 3-year CDS spread (from 100 bp to 105 bp) causes $\lambda_2$ to jump from 180 bp to 230 bp. Explain why this instability arises and how it relates to the condition number of the inverse problem.

---

**Exercise 3.** Describe the "recovery-intensity trade-off" in formal terms. Given the approximate CDS pricing equation $s \approx (1 - R)\lambda$, show that the partial derivatives $\partial s / \partial R$ and $\partial s / \partial \lambda$ are proportional, making $R$ and $\lambda$ nearly collinear in calibration. What additional data or constraints could break this collinearity?

---

**Exercise 4.** A practitioner fixes $R = 40\%$ for all issuers in a calibration exercise. Discuss the advantages and disadvantages of this approach from an identifiability perspective. Under what circumstances might fixing recovery lead to economically misleading hazard rates?

---

**Exercise 5.** Explain how smoothness constraints on the hazard rate curve (e.g., penalizing $\sum_i (\lambda_{i+1} - \lambda_i)^2$) help mitigate identifiability issues in sequential bootstrapping. What trade-off does the modeler face between fitting accuracy and parameter stability?

---

**Exercise 6.** In illiquid credit markets, CDS quotes may have wide bid-ask spreads (e.g., 20 bp). Explain how this uncertainty propagates through the bootstrapping algorithm. If the 3-year CDS spread is known only to lie in $[80, 100]$ bp, estimate the range of implied hazard rates for the $(1\text{Y}, 3\text{Y}]$ period, assuming $R = 40\%$ and a previously calibrated $\lambda_1 = 100$ bp.
