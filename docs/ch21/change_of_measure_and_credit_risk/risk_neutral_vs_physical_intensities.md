# Risk-Neutral vs Physical Intensities


In credit risk modeling, default intensities differ under the **risk-neutral measure** \(\mathbb{Q}\) and the **physical measure** \(\mathbb{P}\). Understanding this distinction is essential for interpreting calibrated parameters.

---

## Two measures, two roles


- **Physical measure \(\mathbb{P}\):**
  governs real-world default frequencies and risk management.
- **Risk-neutral measure \(\mathbb{Q}\):**
  governs pricing and is inferred from market instruments (e.g. CDS).

The two intensities generally differ due to risk premia.

---

## Intensity decomposition


A common representation is

\[
\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \text{credit risk premium}.
\]



The premium compensates investors for bearing default risk.

---

## Empirical implications


Empirically:
- \(\lambda^{\mathbb{Q}}\) implied from CDS is typically higher,
- historical default frequencies underestimate market-implied risk,
- stress periods amplify the gap.

Thus, CDS-implied intensities should not be interpreted as real default probabilities.

---

## Modeling approaches


Common approaches include:
- specifying \(\lambda^{\mathbb{P}}\) and adding a market price of risk,
- directly modeling \(\lambda^{\mathbb{Q}}\) for pricing,
- joint estimation using market and historical data.

---

## Key takeaways


- Risk-neutral and physical intensities differ.
- The gap reflects default risk premia.
- Measure consistency is crucial for interpretation.

---

## Further reading


- Duffie & Singleton, risk premia in credit.
- Bielecki & Rutkowski, measure changes in credit models.

---

## Exercises

**Exercise 1.** A firm has a physical default intensity of $\lambda^{\mathbb{P}} = 1.5\%$ per year. The 5-year CDS spread implies a risk-neutral intensity of $\lambda^{\mathbb{Q}} = 4.0\%$ (assuming 40% recovery). Compute the credit risk premium $\theta = \lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}}$ and interpret its economic meaning. Calculate the ratio $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ and discuss what it reveals about investor risk aversion.

---

**Exercise 2.** Suppose the physical survival probability over $[0, T]$ is $S^{\mathbb{P}}(T) = e^{-\lambda^{\mathbb{P}} T}$ and the risk-neutral survival probability is $S^{\mathbb{Q}}(T) = e^{-\lambda^{\mathbb{Q}} T}$. For $\lambda^{\mathbb{P}} = 2\%$ and $\lambda^{\mathbb{Q}} = 5\%$, compute both survival probabilities at $T = 1, 3, 5, 10$ years. Plot or tabulate the results and discuss how the gap widens with maturity.

---

**Exercise 3.** Consider a time-varying market price of default risk $\theta_t = a + b e^{-ct}$ with $a = 0.01$, $b = 0.04$, and $c = 0.5$. If $\lambda_t^{\mathbb{P}} = 0.02$ is constant, compute $\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \theta_t$ at $t = 0, 1, 2, 5$. Discuss the term structure of the credit risk premium.

---

**Exercise 4.** A rating agency reports a 5-year cumulative default probability of 3.2% for BBB-rated firms (physical measure). The market-implied 5-year cumulative default probability from CDS spreads is 11.5%. Compute the implied constant intensities under each measure and the multiplicative risk premium ratio. Explain why investors demand this premium.

---

**Exercise 5.** Derive the relationship between the CDS spread $s$ and the risk-neutral intensity $\lambda^{\mathbb{Q}}$ under the simplifying assumptions of constant intensity, constant risk-free rate $r$, continuous premium payments, and recovery of market value with rate $R$. Show that $s \approx (1-R)\lambda^{\mathbb{Q}}$.

---

**Exercise 6.** During a financial crisis, the CDS spread of a firm jumps from 100 bps to 500 bps while rating agencies maintain the same rating. Discuss whether this increase reflects a change in $\lambda^{\mathbb{P}}$, a change in the risk premium $\theta$, or both. What empirical evidence would help distinguish the two effects?

---

**Exercise 7.** Suppose you estimate $\lambda^{\mathbb{P}}$ from historical default data and $\lambda^{\mathbb{Q}}$ from CDS markets. If you mistakenly use $\lambda^{\mathbb{Q}}$ for risk management (e.g., computing expected losses), would you overestimate or underestimate the true expected loss? Quantify the error for a portfolio with \$100 million notional, $\lambda^{\mathbb{P}} = 1\%$, $\lambda^{\mathbb{Q}} = 3\%$, and $R = 40\%$.
