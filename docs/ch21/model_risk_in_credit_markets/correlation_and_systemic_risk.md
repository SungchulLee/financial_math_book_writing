# Correlation and Systemic Risk


Credit risk is inherently correlated across firms and sectors. Ignoring **correlation and systemic risk** is a major source of model error, especially for portfolio credit products.

---

## Sources of correlation


Credit correlations arise from:
- macroeconomic shocks,
- sectoral dependencies,
- financial contagion and feedback loops.

These effects intensify during crises.

---

## Modeling correlation


Approaches include:
- copula-based default correlation,
- factor models for intensities,
- structural multi-firm asset models.

Each approach balances tractability and realism.

---

## Systemic risk


Systemic risk refers to:
- joint default events,
- cascading failures,
- breakdown of diversification.

Single-name models cannot capture these effects.

---

## Implications for pricing


Ignoring correlation leads to:
- underpricing of portfolio credit risk,
- severe losses in stress scenarios,
- misleading diversification benefits.

This was evident during the global financial crisis.

---

## Key takeaways


- Credit risk is strongly correlated.
- Systemic risk dominates in crises.
- Correlation modeling is unavoidable for portfolios.

---

## Further reading


- Li, Gaussian copula model.
- Duffie et al., correlated defaults.

---

## Exercises

**Exercise 1.** In a one-factor Gaussian copula model, each firm's latent variable is $X_i = \sqrt{\rho}\,Z + \sqrt{1-\rho}\,\epsilon_i$ where $Z$ and $\epsilon_i$ are independent standard normals. Compute the pairwise correlation $\text{Corr}(X_i, X_j) = \rho$ for $i \neq j$. Explain why this single-parameter structure may be insufficient for capturing heterogeneous correlation patterns across sectors.

---

**Exercise 2.** Consider a portfolio of 100 identical firms, each with 5-year default probability $p = 3\%$. Under zero correlation ($\rho = 0$), compute the expected number of defaults and approximate the standard deviation using the binomial model. Repeat for perfect correlation ($\rho = 1$). Compare the shapes of the two loss distributions.

---

**Exercise 3.** Explain why credit correlation increases during financial crises. Identify at least three channels through which correlated defaults propagate: (a) macroeconomic, (b) direct financial linkages, and (c) information contagion.

---

**Exercise 4.** A risk manager assumes a portfolio default correlation of $\rho = 15\%$ based on pre-crisis data. During a crisis, realized correlations rise to $\rho = 50\%$. Describe qualitatively how the portfolio loss distribution changes and why diversification benefits are reduced. What implications does this have for the pricing of senior CDO tranches?

---

**Exercise 5.** Compare three approaches to modeling default correlation: (a) copula-based models, (b) multi-name intensity factor models, and (c) structural multi-firm asset models. For each, describe the main advantages and limitations.

---

**Exercise 6.** Define systemic risk and distinguish it from idiosyncratic credit risk. Explain why a portfolio with zero expected loss at the individual name level can still suffer large losses due to systemic risk. Give a numerical example using a simple two-state model (normal vs crisis) with correlation $\rho_{\text{normal}} = 10\%$ and $\rho_{\text{crisis}} = 60\%$.
