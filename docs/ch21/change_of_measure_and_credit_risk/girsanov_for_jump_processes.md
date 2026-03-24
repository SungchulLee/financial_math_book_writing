# Girsanov for Jump Processes


Girsanov’s theorem extends beyond diffusions to **jump processes**, providing the mathematical foundation for changing measures in credit risk models.

---

## Jumps and compensators


Default is modeled as a jump process with compensator

\[
A_t = \int_0^{t \wedge \tau} \lambda_s ds.
\]



Under a measure change, both the compensator and intensity may change.

---

## Girsanov theorem for jumps


Girsanov’s theorem states that, under suitable integrability conditions:
- the compensated jump process remains a martingale,
- the intensity transforms multiplicatively or additively.

This generalizes the drift adjustment in diffusion models.

---

## Application to default modeling


In credit models:
- the likelihood of default paths is reweighted,
- jump intensities reflect risk premia,
- pricing formulas remain tractable.

This formalism justifies using different intensities under \(\mathbb{P}\) and \(\mathbb{Q}\).

---

## Combined diffusion–jump models


Many models include:
- diffusive market factors,
- jump-to-default components.

Girsanov’s theorem applies jointly to both parts.

---

## Key takeaways


- Girsanov extends to jump processes.
- Default intensities change under measure change.
- This underpins risk-neutral credit pricing.

---

## Further reading


- Jacod & Shiryaev, jump processes.
- Cont & Tankov, financial modeling with jumps.

---

## Exercises

**Exercise 1.** Let $N_t$ be a Poisson process with intensity $\lambda$ under $\mathbb{P}$. Define the compensated process $M_t = N_t - \lambda t$. Show that $M_t$ is a $\mathbb{P}$-martingale. Then, under a measure change with Radon--Nikodym density involving a parameter $\eta > -1$, find the intensity of $N_t$ under the new measure $\mathbb{Q}$.

---

**Exercise 2.** Suppose default arrives at time $\tau$ with $\mathbb{P}$-intensity $\lambda_t^{\mathbb{P}}$. Under a change of measure given by

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{G}_t} = \mathcal{E}\left(\int_0^t (\eta_s - 1)(dN_s - \lambda_s^{\mathbb{P}} ds)\right)
$$

where $\eta_s > 0$, show that the $\mathbb{Q}$-intensity is $\lambda_t^{\mathbb{Q}} = \eta_t \lambda_t^{\mathbb{P}}$. Explain why $\eta_t$ must be strictly positive.

---

**Exercise 3.** Consider a model where the short rate follows $dr_t = \mu_r dt + \sigma_r dW_t^{\mathbb{P}}$ and default occurs at the first jump of a Poisson process with constant intensity $\lambda$. Apply the Girsanov theorem simultaneously to the diffusion and jump parts to derive the dynamics of $r_t$ and the default intensity under a risk-neutral measure $\mathbb{Q}$.

---

**Exercise 4.** In a jump-diffusion credit model, the compensator of default under $\mathbb{P}$ is $A_t = \int_0^{t \wedge \tau} \lambda_s^{\mathbb{P}} ds$. Verify that the process

$$
M_t = \mathbf{1}_{\{\tau \le t\}} - \int_0^{t \wedge \tau} \lambda_s^{\mathbb{P}} ds
$$

is a $\mathbb{P}$-martingale. What conditions on $\lambda_s^{\mathbb{P}}$ are needed?

---

**Exercise 5.** Let $\lambda_t^{\mathbb{P}} = a + b e^{-ct}$ for constants $a, b, c > 0$. Suppose the market price of default risk is $\eta_t = 1 + \alpha \lambda_t^{\mathbb{P}}$ for some $\alpha > 0$. Compute $\lambda_t^{\mathbb{Q}} = \eta_t \lambda_t^{\mathbb{P}}$ explicitly and discuss how the risk-neutral intensity differs qualitatively from the physical intensity as $t \to \infty$.

---

**Exercise 6.** Explain why the Girsanov theorem for jump processes requires the condition $\eta_t > -1$ (or $\eta_t > 0$ for strict positivity of the density) rather than merely square-integrability as in the purely diffusive case. What goes wrong if $\eta_t = -1$ at some stopping time?
