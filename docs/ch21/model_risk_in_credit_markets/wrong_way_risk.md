# Wrong-Way Risk


**Wrong-way risk (WWR)** arises when exposure to a counterparty increases precisely when the counterparty’s credit quality deteriorates. It is a major source of model risk in credit markets.

---

## Definition


Wrong-way risk occurs when:
- exposure and default risk are positively correlated,
- losses are amplified during adverse market conditions.

The opposite case is **right-way risk**, where exposure decreases as credit risk increases.

---

## Examples


Typical examples include:
- interest-rate swaps with leveraged counterparties,
- FX derivatives where currency depreciation weakens the counterparty,
- CDS written on correlated reference entities.

WWR is most severe during market stress.

---

## Modeling challenges


Standard intensity models often assume:
- independence between exposure and default,
- constant or exogenous intensities.

These assumptions underestimate tail losses when WWR is present.

---

## Practical mitigation


Mitigation techniques include:
- conservative exposure modeling,
- stressed CVA calculations,
- explicit dependence between market factors and intensity.

Regulatory frameworks require explicit WWR consideration.

---

## Key takeaways


- Wrong-way risk amplifies credit losses.
- Independence assumptions are dangerous.
- Stress-based modeling is essential.

---

## Further reading


- Gregory, *Counterparty Credit Risk*.
- Basel III CVA guidance.

---

## Exercises

**Exercise 1.** Define wrong-way risk (WWR) and right-way risk (RWR). For each of the following transactions, determine whether the exposure exhibits WWR or RWR from the perspective of the bank: (a) an interest rate swap where the counterparty benefits from falling rates and is a leveraged firm that suffers in recessions, (b) a put option sold to a gold mining company with the underlying being gold, (c) a CDS where the bank buys protection on a reference entity that is highly correlated with the protection seller.

---

**Exercise 2.** In a standard CVA calculation, exposure and default probability are assumed independent:

$$
\text{CVA} = (1 - R)\int_0^T \text{EE}(t)\,dP(\tau \le t)
$$

Explain why this formula underestimates CVA when wrong-way risk is present. Propose a modified formula that accounts for positive dependence between exposure and default probability.

---

**Exercise 3.** A bank has an FX forward with a counterparty in an emerging market. The counterparty receives USD and pays local currency. Explain why this trade exhibits wrong-way risk: if the local currency depreciates significantly, both the bank's exposure and the counterparty's default probability increase simultaneously.

---

**Exercise 4.** Describe two approaches for modeling wrong-way risk: (a) explicitly correlating exposure and default intensity using a joint stochastic model, and (b) using stressed exposure profiles in the CVA calculation. Discuss the trade-offs between accuracy and tractability.

---

**Exercise 5.** Regulatory frameworks (e.g., Basel III) require banks to account for wrong-way risk in their CVA calculations. Describe the "alpha multiplier" approach used in regulatory CVA and explain why regulators set $\alpha > 1$ to penalize banks for potential wrong-way risk.

---

**Exercise 6.** A portfolio of credit default swaps has wrong-way risk because the protection sellers are themselves financial institutions whose creditworthiness deteriorates during credit crises. Explain how this feedback mechanism amplified losses during the 2008 financial crisis. What risk management practices could mitigate this systemic wrong-way risk?
