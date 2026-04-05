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

??? success "Solution to Exercise 1"
    The general Radon--Nikodym derivative on the enlarged filtration $\mathcal{G}_T$ takes the form:

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{G}_T} = L_T^{\text{diff}} \cdot L_T^{\text{jump}}
    $$

    **Diffusion component:** This accounts for the change in the drift of the Brownian motion $W_t$:

    $$
    L_T^{\text{diff}} = \exp\left(-\int_0^T \gamma_s \, dW_s^{\mathbb{P}} - \frac{1}{2}\int_0^T \gamma_s^2 \, ds\right)
    $$

    where $\gamma_t$ is the market price of diffusion risk. This is the classical Girsanov density that transforms $W_t^{\mathbb{P}}$ into a $\mathbb{Q}$-Brownian motion $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \gamma_s ds$.

    **Jump-to-default component:** This accounts for the change in the default intensity:

    $$
    L_T^{\text{jump}} = \exp\left(-\int_0^{T \wedge \tau}(\eta_s - 1)\lambda_s^{\mathbb{P}} ds\right) \cdot \eta_\tau^{\mathbf{1}_{\{\tau \le T\}}}
    $$

    where $\eta_t > 0$ is the multiplicative intensity adjustment factor. This transforms the $\mathbb{P}$-intensity $\lambda_t^{\mathbb{P}}$ into the $\mathbb{Q}$-intensity $\lambda_t^{\mathbb{Q}} = \eta_t \lambda_t^{\mathbb{P}}$.

    **Role of each factor:**

    - $L_T^{\text{diff}}$ handles the reweighting of diffusive paths (continuous market risk factors like interest rates, spreads)
    - $L_T^{\text{jump}}$ handles the reweighting of default/survival outcomes---it adjusts both the probability of default occurring and its timing
    - The product structure arises because the diffusion and jump parts of the semimartingale decomposition contribute independently to the likelihood ratio

    The combined density must satisfy $\mathbb{E}^{\mathbb{P}}[L_T] = 1$ and $L_T > 0$ a.s. for the measures to be equivalent.

---

**Exercise 2.** Suppose the $\mathbb{P}$-intensity of default is $\lambda_t^{\mathbb{P}} = 0.02$ (constant) and the market price of default risk is $\theta_t = 0.03$. Compute the $\mathbb{Q}$-intensity $\lambda_t^{\mathbb{Q}}$. If a firm has a 5-year horizon, compute the survival probabilities under both $\mathbb{P}$ and $\mathbb{Q}$ and comment on the difference.

??? success "Solution to Exercise 2"
    **Computing $\lambda_t^{\mathbb{Q}}$:**

    With $\lambda_t^{\mathbb{P}} = 0.02$ and $\theta_t = 0.03$ (additive risk premium):

    $$
    \lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \theta_t = 0.02 + 0.03 = 0.05
    $$

    **Survival probabilities over $T = 5$ years:**

    Under $\mathbb{P}$ (constant intensity):

    $$
    S^{\mathbb{P}}(5) = \exp(-\lambda^{\mathbb{P}} \cdot 5) = e^{-0.02 \times 5} = e^{-0.10} \approx 0.9048
    $$

    Under $\mathbb{Q}$:

    $$
    S^{\mathbb{Q}}(5) = \exp(-\lambda^{\mathbb{Q}} \cdot 5) = e^{-0.05 \times 5} = e^{-0.25} \approx 0.7788
    $$

    **Comparison and interpretation:**

    - Under $\mathbb{P}$: approximately 90.5% survival probability (about 9.5% default probability)
    - Under $\mathbb{Q}$: approximately 77.9% survival probability (about 22.1% default probability)

    The risk-neutral default probability (22.1%) is more than twice the physical default probability (9.5%). The difference reflects the **credit risk premium**: investors demand compensation for bearing default risk, which inflates the risk-neutral intensity. Market-implied spreads (CDS, bonds) embed this premium, so using them directly as physical default probabilities would significantly overestimate actual default rates.

    The ratio $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}} = 0.05/0.02 = 2.5$ indicates that the market prices default risk at 2.5 times the actuarial rate.

---

**Exercise 3.** Consider a defaultable asset whose pre-default price satisfies $dS_t = S_t(\mu dt + \sigma dW_t)$ under $\mathbb{P}$, with a jump to $S_{\tau} = (1 - L)S_{\tau^-}$ at default. Derive the conditions on the Girsanov kernel for the diffusion part and the intensity change so that the discounted price process is a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 3"
    **Setup:** The pre-default asset price follows $dS_t = S_t(\mu \, dt + \sigma \, dW_t)$ under $\mathbb{P}$, with a jump at default: $S_\tau = (1 - L)S_{\tau^-}$, where $L$ is the fractional loss given default.

    **Discounted price process:** Let $\tilde{S}_t = e^{-rt}S_t$ (using constant $r$ for simplicity). For $\tilde{S}_t$ to be a $\mathbb{Q}$-martingale, we need to account for both continuous dynamics and the jump at default.

    **Girsanov for the diffusion part:** Let $\gamma$ be the Girsanov kernel so that $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \gamma t$ is a $\mathbb{Q}$-Brownian motion. Under $\mathbb{Q}$:

    $$
    dS_t = S_{t^-}\left[(\mu - \sigma\gamma) dt + \sigma \, dW_t^{\mathbb{Q}}\right] - L \cdot S_{t^-} \, dN_t
    $$

    **Martingale condition:** The compensated dynamics of the discounted price must have zero drift. The pre-default drift is $(\mu - \sigma\gamma - r)$ and each jump reduces the price by $L \cdot S_{t^-}$. Including the default intensity $\lambda^{\mathbb{Q}}$, the drift condition is:

    $$
    (\mu - \sigma\gamma - r) - L \cdot \lambda^{\mathbb{Q}} = 0
    $$

    This is because the expected loss rate from jumps is $L \cdot \lambda^{\mathbb{Q}}$ (jump size $\times$ intensity), which must be offset by the continuous drift excess.

    **Solving for the Girsanov kernel:**

    $$
    \gamma = \frac{\mu - r - L \cdot \lambda^{\mathbb{Q}}}{\sigma}
    $$

    **Intensity change:** If the $\mathbb{P}$-intensity is $\lambda^{\mathbb{P}}$ and we apply a multiplicative change $\lambda^{\mathbb{Q}} = \eta \lambda^{\mathbb{P}}$, then $\eta > 0$ is a free parameter (market price of jump risk). Substituting:

    $$
    \gamma = \frac{\mu - r - L \cdot \eta \lambda^{\mathbb{P}}}{\sigma}
    $$

    The two free parameters ($\gamma$ for diffusion risk and $\eta$ for jump risk) satisfy one equation, reflecting the **incompleteness** of the market with jump risk---there is a family of risk-neutral measures parameterized by $\eta$ (or equivalently $\gamma$).

---

**Exercise 4.** Prove that if the recovery rate $R$ and the default intensity $\lambda_t$ are both deterministic, then any measure change affecting $\lambda_t$ can be absorbed into an adjusted discount rate. Specifically, show that

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s ds} \mathbf{1}_{\{\tau > T\}}\right] = e^{-\int_0^T (r_s + \lambda_s^{\mathbb{Q}}) ds}
$$

??? success "Solution to Exercise 4"
    **Claim:** When $R$ and $\lambda_t$ are deterministic:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s \, ds} \mathbf{1}_{\{\tau > T\}}\right] = e^{-\int_0^T (r_s + \lambda_s^{\mathbb{Q}}) ds}
    $$

    **Proof:**

    Using the tower property and the key property of the intensity-based framework, we condition on the market filtration $\mathcal{F}_T$:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s \, ds} \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_T\right] = e^{-\int_0^T r_s \, ds} \cdot \mathbb{Q}(\tau > T \mid \mathcal{F}_T)
    $$

    Since default has $\mathbb{Q}$-intensity $\lambda_t^{\mathbb{Q}}$ (which is deterministic by assumption), the survival probability is:

    $$
    \mathbb{Q}(\tau > T \mid \mathcal{F}_T) = \exp\left(-\int_0^T \lambda_s^{\mathbb{Q}} ds\right)
    $$

    When $\lambda_t^{\mathbb{Q}}$ is deterministic, this is non-random, so taking the outer expectation:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s \, ds} \mathbf{1}_{\{\tau > T\}}\right] = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s \, ds}\right] \cdot e^{-\int_0^T \lambda_s^{\mathbb{Q}} ds}
    $$

    If $r_s$ is also deterministic (or independent of default):

    $$
    = e^{-\int_0^T r_s \, ds} \cdot e^{-\int_0^T \lambda_s^{\mathbb{Q}} ds} = e^{-\int_0^T (r_s + \lambda_s^{\mathbb{Q}}) ds}
    $$

    **Interpretation as adjusted discount rate:** This shows that the survival-contingent pricing problem reduces to discounting at the **credit-adjusted rate** $r_s + \lambda_s^{\mathbb{Q}}$. The default intensity acts as an additional spread on top of the risk-free rate. Any measure change that modifies $\lambda_s^{\mathbb{P}} \to \lambda_s^{\mathbb{Q}}$ simply changes the spread, which can be absorbed into the discount rate. This is the foundation of the "hazard rate as spread" interpretation commonly used in credit markets. $\square$

---

**Exercise 5.** In a joint equity--credit model, the equity price follows a geometric Brownian motion and the default intensity is $\lambda_t = f(S_t)$ for some decreasing function $f$. Explain why a measure change that modifies the drift of $S_t$ also implicitly changes the default intensity dynamics. Does this create "wrong-way risk" under the new measure?

??? success "Solution to Exercise 5"
    **Setup:** Equity follows $dS_t = S_t(\mu \, dt + \sigma \, dW_t)$ and default intensity is $\lambda_t = f(S_t)$ with $f$ decreasing (low stock price $\Rightarrow$ high default intensity).

    **How a drift change modifies intensity dynamics:**

    Under a measure change with Girsanov kernel $\gamma$, the equity dynamics become:

    $$
    dS_t = S_t\left[(\mu - \sigma\gamma) dt + \sigma \, dW_t^{\mathbb{Q}}\right]
    $$

    Since $\lambda_t = f(S_t)$, by Ito's formula:

    $$
    d\lambda_t = \left[f'(S_t) S_t (\mu - \sigma\gamma) + \frac{1}{2}f''(S_t) S_t^2 \sigma^2\right] dt + f'(S_t) S_t \sigma \, dW_t^{\mathbb{Q}}
    $$

    The drift of $\lambda_t$ changes from its $\mathbb{P}$-value because the drift of $S_t$ has changed. Specifically, the drift shift in $\lambda$ is:

    $$
    \Delta\mu_\lambda = -f'(S_t) S_t \sigma \gamma
    $$

    Since $f' < 0$ (decreasing function) and typically $\gamma > 0$ (equity risk premium is positive, so $\mu > r$), we get $\Delta\mu_\lambda > 0$. The intensity drift increases under $\mathbb{Q}$.

    **Wrong-way risk:**

    Yes, this creates wrong-way risk under the new measure. Wrong-way risk refers to the phenomenon where credit exposure increases precisely when the counterparty's credit quality deteriorates.

    Under $\mathbb{Q}$, the stock price typically has lower drift (drift $r$ instead of $\mu > r$). With $f$ decreasing:

    - Lower stock price drift $\Rightarrow$ stock price tends to be lower under $\mathbb{Q}$
    - Lower stock price $\Rightarrow$ higher $\lambda_t = f(S_t)$ (since $f$ is decreasing)
    - Higher $\lambda_t$ $\Rightarrow$ higher default probability

    The measure change simultaneously makes the stock price drift downward (lower growth rate) and amplifies the default intensity. This correlation between market and credit risk is the essence of wrong-way risk. It means that risk-neutral default probabilities are inflated not only by the credit risk premium but also by the equity risk premium through the coupling $\lambda_t = f(S_t)$.

---

**Exercise 6.** A credit model specifies $\lambda_t^{\mathbb{P}} = \alpha + \beta X_t$ where $X_t$ is an Ornstein--Uhlenbeck process under $\mathbb{P}$. Under a measure change, $X_t$ becomes an OU process with different drift parameters under $\mathbb{Q}$. Derive the relationship between $\lambda_t^{\mathbb{Q}}$ and the modified OU parameters, and verify that the compensator of the default indicator is consistent under $\mathbb{Q}$.

??? success "Solution to Exercise 6"
    **Under $\mathbb{P}$:** Let $X_t$ follow the Ornstein--Uhlenbeck process:

    $$
    dX_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - X_t) dt + \sigma_X dW_t^{\mathbb{P}}
    $$

    The $\mathbb{P}$-intensity is $\lambda_t^{\mathbb{P}} = \alpha + \beta X_t$.

    **Under $\mathbb{Q}$:** Apply a Girsanov kernel $\gamma_t$ so that $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \gamma_s ds$. With a common parameterization $\gamma_t = \gamma_0 + \gamma_1 X_t$ (affine market price of risk), the $\mathbb{Q}$-dynamics of $X_t$ are:

    $$
    dX_t = \left[\kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - X_t) - \sigma_X(\gamma_0 + \gamma_1 X_t)\right] dt + \sigma_X dW_t^{\mathbb{Q}}
    $$

    $$
    = \left[(\kappa^{\mathbb{P}} \theta^{\mathbb{P}} - \sigma_X \gamma_0) - (\kappa^{\mathbb{P}} + \sigma_X \gamma_1) X_t\right] dt + \sigma_X dW_t^{\mathbb{Q}}
    $$

    This is again an OU process with modified parameters:

    $$
    \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \sigma_X \gamma_1, \quad \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}} \theta^{\mathbb{P}} - \sigma_X \gamma_0}{\kappa^{\mathbb{Q}}}
    $$

    **Relationship between $\lambda_t^{\mathbb{Q}}$ and $\lambda_t^{\mathbb{P}}$:**

    The intensity itself does not change as a function of the state variable---it is still $\lambda_t = \alpha + \beta X_t$. What changes is the **dynamics** of $X_t$, and hence the distribution of $\lambda_t$. Specifically:

    $$
    \lambda_t = \alpha + \beta X_t \quad \text{under both } \mathbb{P} \text{ and } \mathbb{Q}
    $$

    but the dynamics of $\lambda_t$ become:

    $$
    d\lambda_t = \beta \, dX_t = \beta\left[\kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - X_t) dt + \sigma_X dW_t^{\mathbb{Q}}\right]
    $$

    $$
    = \kappa^{\mathbb{Q}}\left[(\alpha + \beta\theta^{\mathbb{Q}}) - \lambda_t\right] dt + \beta\sigma_X dW_t^{\mathbb{Q}}
    $$

    The long-run mean of $\lambda$ under $\mathbb{Q}$ is $\alpha + \beta\theta^{\mathbb{Q}}$, which differs from the $\mathbb{P}$-mean $\alpha + \beta\theta^{\mathbb{P}}$.

    **Verifying compensator consistency under $\mathbb{Q}$:**

    Under $\mathbb{Q}$, the compensator of the default indicator $\mathbf{1}_{\{\tau \le t\}}$ must be $\int_0^{t \wedge \tau} \lambda_s \, ds = \int_0^{t \wedge \tau} (\alpha + \beta X_s) ds$. This means:

    $$
    M_t^{\mathbb{Q}} = \mathbf{1}_{\{\tau \le t\}} - \int_0^{t \wedge \tau} (\alpha + \beta X_s) ds
    $$

    must be a $\mathbb{Q}$-martingale. Since the intensity function $\lambda_t = \alpha + \beta X_t$ is unchanged (only the distribution of $X_t$ changes via the drift modification), the compensator structure is preserved. The martingale property of $M_t^{\mathbb{Q}}$ under $\mathbb{Q}$ follows from the general theory: the Girsanov theorem for the diffusion part changes the drift of $X_t$ but preserves the compensator formula for the jump part as $\int_0^{t \wedge \tau} \lambda_s ds$ (with $\lambda_s$ still given by the same function of $X_s$).

    If one additionally applies a jump-Girsanov change with parameter $\eta_t$, then the $\mathbb{Q}$-intensity would become $\eta_t(\alpha + \beta X_t)$, and the compensator would adjust accordingly.
