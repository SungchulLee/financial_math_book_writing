# Pricing under Intensity Models


Intensity-based models provide tractable pricing formulas for defaultable claims by modeling default via a hazard rate process.

---

## Pricing framework


Assume:
- default intensity \(\lambda_t\),
- recovery scheme specified,
- immersion and progressive enlargement hold.

Pricing reduces to computing discounted expectations involving survival probabilities.

---

## Defaultable zero-coupon bond


Under recovery of treasury (RT), the price simplifies to

\[
P^d(t,T)
= \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T (r_s + \lambda_s) ds\right)
\middle| \mathcal{F}_t
\right].
\]



Default risk acts like an additional discount rate.

---

## General recovery case


With recovery of face value or market value, pricing involves:
- integrals over default times,
- survival probabilities,
- expected recovery payments.

Closed forms exist for simple intensity models.

---

## Relation to CDS pricing


The same framework prices:
- credit default swaps (premium vs protection legs),
- risky bonds and loans,
- credit-linked notes.

Consistency across products is essential.

---

## Key takeaways


- Intensity models yield tractable pricing formulas.
- Default risk enters through survival probabilities.
- Recovery assumptions must be consistent across instruments.

---

## Further reading


- Duffie & Singleton, intensity-based pricing.
- Brigo et al., credit derivatives pricing.

---

## Exercises

**Exercise 1.** Under the recovery of treasury convention, the defaultable zero-coupon bond price is

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + \lambda_s)\,ds} \mid \mathcal{F}_t\right]
$$

For constant $r = 3\%$ and constant $\lambda = 2\%$, compute $P^d(0,5)$. Interpret the result as discounting at a "credit-adjusted" rate.

---

**Exercise 2.** Using the intensity-based framework, derive the price of a CDS protection leg:

$$
\text{PV}_{\text{prot}} = (1 - R)\int_0^T D(0,u)\,\lambda_u\,S(0,u)\,du
$$

For $R = 40\%$, $r = 3\%$, $\lambda = 1.5\%$, and $T = 5$, compute the numerical value per unit notional.

---

**Exercise 3.** Explain why the immersion (H-hypothesis) and progressive enlargement assumptions are essential for the intensity-based pricing framework. What would go wrong if default revealed information about future market factor values?

---

**Exercise 4.** A CDS with maturity 5 years has a par spread of 100 bp, and a defaultable bond with the same maturity and issuer trades at a yield spread of 130 bp. Using the intensity model framework, explain why these two spread measures should be approximately equal in theory, and identify three practical reasons they might differ.

---

**Exercise 5.** Under the Duffie-Singleton (RMV) recovery convention, derive the defaultable bond price

$$
P^d(t,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + (1-R)\lambda_s)\,ds} \mid \mathcal{F}_t\right]
$$

starting from the recursive relationship $P^d(\tau-,T) = R \cdot P^d(\tau-,T)$ at default. Show that the loss-adjusted intensity $(1-R)\lambda$ replaces $\lambda$ in the discount rate.

---

**Exercise 6.** Consider an affine intensity model where $\lambda_t$ follows a CIR process: $d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma\sqrt{\lambda_t}\,dW_t$ with $\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, and $\lambda_0 = 1\%$. Using the affine bond pricing formula, describe qualitatively how the defaultable bond price depends on the current intensity $\lambda_0$. What happens to the price as $\lambda_0$ increases from $1\%$ to $5\%$?
