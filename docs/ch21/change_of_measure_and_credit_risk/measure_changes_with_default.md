# Measure Changes with Default


Changing probability measures in the presence of default requires special care because default introduces **jumps** and filtration enlargement.

---

## Measure change framework


Let \(\mathbb{Q}\) and \(\mathbb{P}\) be equivalent measures on the enlarged filtration \((\mathcal{G}_t)\).
The Radon–Nikodym derivative must account for:
- diffusion risks,
- jump-to-default risk.

---

## Effect on intensities


Under a change of measure, the default intensity transforms as

\[
\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \theta_t,
\]


where \(\theta_t\) reflects the market price of default risk.

This parallels drift changes in diffusion models.

---

## Martingale preservation


For pricing, discounted asset prices must remain martingales under the chosen measure.
This imposes consistency conditions linking:
- compensators,
- measure changes,
- recovery assumptions.

---

## Practical relevance


Measure changes with default are crucial for:
- linking historical default models to pricing models,
- joint equity–credit modeling,
- stress testing and scenario analysis.

---

## Key takeaways


- Measure changes affect default intensities.
- Jump risk requires special treatment.
- Consistency is essential for arbitrage-free pricing.

---

## Further reading


- Jeanblanc & Rutkowski, measure changes with default.
- Elliott et al., hidden default intensity models.

---

## Exercises

**Exercise 1.** Let $\mathbb{P}$ and $\mathbb{Q}$ be equivalent measures on $(\Omega, \mathcal{G}_T)$ where $\mathcal{G}_t$ is the enlarged filtration containing default information. Write down the general form of the Radon--Nikodym derivative $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{G}_T}$ that accounts for both a diffusion component (driven by $W_t$) and a jump-to-default component. Identify the role of each factor.

---

**Exercise 2.** Suppose the $\mathbb{P}$-intensity of default is $\lambda_t^{\mathbb{P}} = 0.02$ (constant) and the market price of default risk is $\theta_t = 0.03$. Compute the $\mathbb{Q}$-intensity $\lambda_t^{\mathbb{Q}}$. If a firm has a 5-year horizon, compute the survival probabilities under both $\mathbb{P}$ and $\mathbb{Q}$ and comment on the difference.

---

**Exercise 3.** Consider a defaultable asset whose pre-default price satisfies $dS_t = S_t(\mu dt + \sigma dW_t)$ under $\mathbb{P}$, with a jump to $S_{\tau} = (1 - L)S_{\tau^-}$ at default. Derive the conditions on the Girsanov kernel for the diffusion part and the intensity change so that the discounted price process is a $\mathbb{Q}$-martingale.

---

**Exercise 4.** Prove that if the recovery rate $R$ and the default intensity $\lambda_t$ are both deterministic, then any measure change affecting $\lambda_t$ can be absorbed into an adjusted discount rate. Specifically, show that

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s ds} \mathbf{1}_{\{\tau > T\}}\right] = e^{-\int_0^T (r_s + \lambda_s^{\mathbb{Q}}) ds}
$$

---

**Exercise 5.** In a joint equity--credit model, the equity price follows a geometric Brownian motion and the default intensity is $\lambda_t = f(S_t)$ for some decreasing function $f$. Explain why a measure change that modifies the drift of $S_t$ also implicitly changes the default intensity dynamics. Does this create "wrong-way risk" under the new measure?

---

**Exercise 6.** A credit model specifies $\lambda_t^{\mathbb{P}} = \alpha + \beta X_t$ where $X_t$ is an Ornstein--Uhlenbeck process under $\mathbb{P}$. Under a measure change, $X_t$ becomes an OU process with different drift parameters under $\mathbb{Q}$. Derive the relationship between $\lambda_t^{\mathbb{Q}}$ and the modified OU parameters, and verify that the compensator of the default indicator is consistent under $\mathbb{Q}$.
