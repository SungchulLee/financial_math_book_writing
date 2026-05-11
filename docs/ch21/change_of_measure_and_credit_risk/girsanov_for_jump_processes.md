# Girsanov for Jump Processes


Girsanov’s theorem extends beyond diffusions to **jump processes**, providing the mathematical foundation for changing measures in credit risk models.

---

## Jumps and compensators


Default is modeled as a jump process with compensator

$$
A_t = \int_0^{t \wedge \tau} \lambda_s ds
$$



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

This formalism justifies using different intensities under $\mathbb{P}$ and $\mathbb{Q}$.

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

??? success "Solution to Exercise 1"
    **Part 1: $M_t = N_t - \lambda t$ is a $\mathbb{P}$-martingale.**

    We need to verify: (i) $\mathbb{E}^{\mathbb{P}}[|M_t|] < \infty$, and (ii) $\mathbb{E}^{\mathbb{P}}[M_t \mid \mathcal{F}_s] = M_s$ for $s \le t$.

    Since $N_t$ is a Poisson process with intensity $\lambda$, we have $\mathbb{E}^{\mathbb{P}}[N_t] = \lambda t$ and $\mathbb{E}^{\mathbb{P}}[|M_t|] \le \mathbb{E}^{\mathbb{P}}[N_t] + \lambda t = 2\lambda t < \infty$.

    For the martingale property, using the independent and stationary increments of the Poisson process:

    $$
    \mathbb{E}^{\mathbb{P}}[M_t \mid \mathcal{F}_s] = \mathbb{E}^{\mathbb{P}}[N_t - \lambda t \mid \mathcal{F}_s]
    $$

    $$
    = \mathbb{E}^{\mathbb{P}}[N_t - N_s \mid \mathcal{F}_s] + N_s - \lambda t
    $$

    Since $N_t - N_s$ is independent of $\mathcal{F}_s$ with $\mathbb{E}^{\mathbb{P}}[N_t - N_s] = \lambda(t - s)$:

    $$
    = \lambda(t - s) + N_s - \lambda t = N_s - \lambda s = M_s
    $$

    Hence $M_t$ is a $\mathbb{P}$-martingale. $\square$

    **Part 2: Intensity under $\mathbb{Q}$.**

    Define the measure change via the stochastic exponential with parameter $\eta > -1$:

    $$
    L_t = \mathcal{E}\left(\int_0^t \eta \, dM_s\right) = \exp\left(-\eta \lambda t + \int_0^t \ln(1 + \eta) \, dN_s\right)
    $$

    $$
    = \exp\left(-\eta \lambda t\right)(1 + \eta)^{N_t}
    $$

    The new measure $\mathbb{Q}$ is defined by $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_t} = L_t$.

    Under $\mathbb{Q}$, the compensator of $N_t$ changes. The $\mathbb{Q}$-compensator is $(1+\eta)\lambda t$, so the $\mathbb{Q}$-intensity of $N_t$ is:

    $$
    \lambda^{\mathbb{Q}} = (1 + \eta)\lambda
    $$

    To verify, the process $\tilde{M}_t = N_t - (1+\eta)\lambda t$ must be a $\mathbb{Q}$-martingale. By Girsanov's theorem for point processes, the compensated process under the new measure adjusts the intensity by the multiplicative factor $(1 + \eta)$.

---

**Exercise 2.** Suppose default arrives at time $\tau$ with $\mathbb{P}$-intensity $\lambda_t^{\mathbb{P}}$. Under a change of measure given by

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{G}_t} = \mathcal{E}\left(\int_0^t (\eta_s - 1)(dN_s - \lambda_s^{\mathbb{P}} ds)\right)
$$

where $\eta_s > 0$, show that the $\mathbb{Q}$-intensity is $\lambda_t^{\mathbb{Q}} = \eta_t \lambda_t^{\mathbb{P}}$. Explain why $\eta_t$ must be strictly positive.

??? success "Solution to Exercise 2"
    The Radon--Nikodym density is given by the stochastic exponential:

    $$
    L_t = \mathcal{E}\left(\int_0^t (\eta_s - 1)(dN_s - \lambda_s^{\mathbb{P}} ds)\right)
    $$

    Expanding the stochastic exponential for a jump process, we have:

    $$
    L_t = \exp\left(-\int_0^t (\eta_s - 1)\lambda_s^{\mathbb{P}} ds\right) \prod_{0 < s \le t} (1 + (\eta_s - 1))^{\Delta N_s}
    $$

    $$
    = \exp\left(-\int_0^t (\eta_s - 1)\lambda_s^{\mathbb{P}} ds\right) \prod_{0 < s \le t} \eta_s^{\Delta N_s}
    $$

    By Girsanov's theorem for point processes, the $\mathbb{Q}$-compensator of $N_t$ is:

    $$
    A_t^{\mathbb{Q}} = \int_0^{t \wedge \tau} (1 + (\eta_s - 1)) \lambda_s^{\mathbb{P}} ds = \int_0^{t \wedge \tau} \eta_s \lambda_s^{\mathbb{P}} ds
    $$

    Therefore the $\mathbb{Q}$-intensity is:

    $$
    \lambda_t^{\mathbb{Q}} = \eta_t \lambda_t^{\mathbb{P}}
    $$

    **Why $\eta_t$ must be strictly positive:**

    1. **Intensity must be non-negative:** An intensity represents an instantaneous rate of occurrence, so $\lambda_t^{\mathbb{Q}} = \eta_t \lambda_t^{\mathbb{P}} \ge 0$. Since $\lambda_t^{\mathbb{P}} > 0$, we need $\eta_t > 0$.

    2. **Equivalence of measures:** For $\mathbb{Q} \sim \mathbb{P}$ (equivalence), the Radon--Nikodym derivative $L_t$ must be strictly positive. Looking at the product $\prod \eta_s^{\Delta N_s}$, if $\eta_s = 0$ at some time $s$, then at a jump time $L$ would become zero, breaking equivalence. If $\eta_s < 0$, then $L_t$ could become negative, which is impossible for a density.

    3. **Absolute continuity:** If $\eta_t = 0$, then default at time $t$ has zero probability under $\mathbb{Q}$ but positive probability under $\mathbb{P}$, so the measures are not equivalent.

---

**Exercise 3.** Consider a model where the short rate follows $dr_t = \mu_r dt + \sigma_r dW_t^{\mathbb{P}}$ and default occurs at the first jump of a Poisson process with constant intensity $\lambda$. Apply the Girsanov theorem simultaneously to the diffusion and jump parts to derive the dynamics of $r_t$ and the default intensity under a risk-neutral measure $\mathbb{Q}$.

??? success "Solution to Exercise 3"
    We apply Girsanov's theorem simultaneously to the diffusion part (Brownian motion) and the jump part (Poisson process).

    **Under $\mathbb{P}$:** The short rate follows $dr_t = \mu_r dt + \sigma_r dW_t^{\mathbb{P}}$ and default arrives at the first jump of a Poisson process $N_t$ with constant intensity $\lambda$.

    **Girsanov for the diffusion part:** Introduce a market price of risk $\gamma_t$ for the diffusion. Define $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \gamma_s ds$. Then under $\mathbb{Q}$:

    $$
    dr_t = \mu_r dt + \sigma_r (dW_t^{\mathbb{Q}} - \gamma_t dt) = (\mu_r - \sigma_r \gamma_t) dt + \sigma_r dW_t^{\mathbb{Q}}
    $$

    **Girsanov for the jump part:** Introduce a parameter $\eta > -1$ for the jump risk premium. The $\mathbb{Q}$-intensity becomes:

    $$
    \lambda^{\mathbb{Q}} = (1 + \eta)\lambda
    $$

    **Combined Radon--Nikodym derivative:** The full measure change density is the product of the diffusion and jump parts:

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{G}_t} = \underbrace{\exp\left(-\int_0^t \gamma_s dW_s^{\mathbb{P}} - \frac{1}{2}\int_0^t \gamma_s^2 ds\right)}_{\text{diffusion Girsanov}} \cdot \underbrace{\exp\left(-\eta\lambda t\right)(1+\eta)^{N_t}}_{\text{jump Girsanov}}
    $$

    **Under $\mathbb{Q}$, the dynamics are:**

    - Short rate: $dr_t = (\mu_r - \sigma_r \gamma_t) dt + \sigma_r dW_t^{\mathbb{Q}}$
    - Default intensity: $\lambda^{\mathbb{Q}} = (1 + \eta)\lambda$
    - $W_t^{\mathbb{Q}}$ is a $\mathbb{Q}$-Brownian motion
    - The compensated default process $N_t - \lambda^{\mathbb{Q}} t$ is a $\mathbb{Q}$-martingale

    The no-arbitrage condition requires choosing $\gamma_t$ and $\eta$ so that discounted tradeable asset prices are $\mathbb{Q}$-martingales. If a defaultable bond is traded, this imposes constraints linking $\gamma_t$, $\eta$, and the bond's recovery rate.

---

**Exercise 4.** In a jump-diffusion credit model, the compensator of default under $\mathbb{P}$ is $A_t = \int_0^{t \wedge \tau} \lambda_s^{\mathbb{P}} ds$. Verify that the process

$$
M_t = \mathbf{1}_{\{\tau \le t\}} - \int_0^{t \wedge \tau} \lambda_s^{\mathbb{P}} ds
$$

is a $\mathbb{P}$-martingale. What conditions on $\lambda_s^{\mathbb{P}}$ are needed?

??? success "Solution to Exercise 4"
    We verify that $M_t = \mathbf{1}_{\{\tau \le t\}} - \int_0^{t \wedge \tau} \lambda_s^{\mathbb{P}} ds$ is a $\mathbb{P}$-martingale.

    **Step 1: Integrability.** We have $|M_t| \le 1 + \int_0^t \lambda_s^{\mathbb{P}} ds$. Provided $\mathbb{E}^{\mathbb{P}}[\int_0^t \lambda_s^{\mathbb{P}} ds] < \infty$, we get $\mathbb{E}^{\mathbb{P}}[|M_t|] < \infty$.

    **Step 2: Martingale property.** Let $s < t$. We compute $\mathbb{E}^{\mathbb{P}}[M_t - M_s \mid \mathcal{G}_s]$.

    $$
    M_t - M_s = \left(\mathbf{1}_{\{\tau \le t\}} - \mathbf{1}_{\{\tau \le s\}}\right) - \int_{s \wedge \tau}^{t \wedge \tau} \lambda_u^{\mathbb{P}} du
    $$

    **Case 1: $\tau \le s$.** On the event $\{\tau \le s\}$, both $\mathbf{1}_{\{\tau \le t\}} = 1$ and $\mathbf{1}_{\{\tau \le s\}} = 1$, and $\int_{s \wedge \tau}^{t \wedge \tau} \lambda_u du = 0$ since $s \wedge \tau = t \wedge \tau = \tau$. So $M_t - M_s = 0$.

    **Case 2: $\tau > s$.** On $\{\tau > s\}$, by the definition of the intensity (hazard rate):

    $$
    \mathbb{P}(\tau > t \mid \tau > s, \mathcal{F}_t) = \exp\left(-\int_s^t \lambda_u^{\mathbb{P}} du\right)
    $$

    Using the key property of the intensity-based framework, for $\tau > s$:

    $$
    \mathbb{E}^{\mathbb{P}}\left[\mathbf{1}_{\{s < \tau \le t\}} \mid \mathcal{G}_s\right] = \mathbb{E}^{\mathbb{P}}\left[\int_s^{t \wedge \tau} \lambda_u^{\mathbb{P}} du \mid \mathcal{G}_s\right]
    $$

    This identity is precisely the statement that the compensator of $\mathbf{1}_{\{\tau \le t\}}$ (restricted to the interval $(s, t]$ and stopped at $\tau$) is $\int_{s \wedge \tau}^{t \wedge \tau} \lambda_u^{\mathbb{P}} du$.

    Therefore $\mathbb{E}^{\mathbb{P}}[M_t - M_s \mid \mathcal{G}_s] = 0$ in both cases.

    **Required conditions on $\lambda_s^{\mathbb{P}}$:**

    1. **Non-negativity:** $\lambda_s^{\mathbb{P}} \ge 0$ a.s. for all $s$ (intensities are non-negative).
    2. **Integrability:** $\mathbb{E}^{\mathbb{P}}\left[\int_0^T \lambda_s^{\mathbb{P}} ds\right] < \infty$ for each $T > 0$.
    3. **Progressively measurable:** $\lambda_s^{\mathbb{P}}$ must be progressively measurable with respect to the reference filtration $(\mathcal{F}_t)$ (predictability in the enlarged filtration $(\mathcal{G}_t)$).
    4. **The explosion condition** $\int_0^\infty \lambda_s^{\mathbb{P}} ds = \infty$ a.s. is needed for $\tau < \infty$ a.s., though for the martingale property over finite horizons, local integrability suffices.

---

**Exercise 5.** Let $\lambda_t^{\mathbb{P}} = a + b e^{-ct}$ for constants $a, b, c > 0$. Suppose the market price of default risk is $\eta_t = 1 + \alpha \lambda_t^{\mathbb{P}}$ for some $\alpha > 0$. Compute $\lambda_t^{\mathbb{Q}} = \eta_t \lambda_t^{\mathbb{P}}$ explicitly and discuss how the risk-neutral intensity differs qualitatively from the physical intensity as $t \to \infty$.

??? success "Solution to Exercise 5"
    **Computing $\lambda_t^{\mathbb{Q}}$:**

    Given $\lambda_t^{\mathbb{P}} = a + b e^{-ct}$ and $\eta_t = 1 + \alpha \lambda_t^{\mathbb{P}} = 1 + \alpha(a + b e^{-ct})$, we compute:

    $$
    \lambda_t^{\mathbb{Q}} = \eta_t \lambda_t^{\mathbb{P}} = \left(1 + \alpha(a + b e^{-ct})\right)(a + b e^{-ct})
    $$

    Expanding:

    $$
    \lambda_t^{\mathbb{Q}} = (a + b e^{-ct}) + \alpha(a + b e^{-ct})^2
    $$

    $$
    = (a + b e^{-ct}) + \alpha\left(a^2 + 2ab e^{-ct} + b^2 e^{-2ct}\right)
    $$

    $$
    = a + \alpha a^2 + (b + 2\alpha ab) e^{-ct} + \alpha b^2 e^{-2ct}
    $$

    **Behavior as $t \to \infty$:**

    As $t \to \infty$, $e^{-ct} \to 0$, so:

    - $\lambda_t^{\mathbb{P}} \to a$
    - $\eta_t \to 1 + \alpha a$
    - $\lambda_t^{\mathbb{Q}} \to a(1 + \alpha a) = a + \alpha a^2$

    **Qualitative comparison:**

    1. **At $t = 0$:** $\lambda_0^{\mathbb{Q}} = (a + b)(1 + \alpha(a + b)) = (a+b) + \alpha(a+b)^2$, which is substantially larger than $\lambda_0^{\mathbb{P}} = a + b$ since the quadratic term $\alpha(a+b)^2$ amplifies the risk premium for high initial intensity.

    2. **Long-run ($t \to \infty$):** The ratio $\lambda_\infty^{\mathbb{Q}} / \lambda_\infty^{\mathbb{P}} = 1 + \alpha a$, which is a constant markup over the physical intensity.

    3. **Decay structure:** The risk-neutral intensity has three exponential terms (constant, $e^{-ct}$, and $e^{-2ct}$) versus two for the physical intensity. The $e^{-2ct}$ term means the risk-neutral intensity decays faster initially but from a higher level. The risk premium $\lambda_t^{\mathbb{Q}} - \lambda_t^{\mathbb{P}} = \alpha(\lambda_t^{\mathbb{P}})^2$ is **proportional to the square** of the physical intensity, so the risk premium is largest when default risk is highest---a feature consistent with empirical observations during credit crises.

---

**Exercise 6.** Explain why the Girsanov theorem for jump processes requires the condition $\eta_t > -1$ (or $\eta_t > 0$ for strict positivity of the density) rather than merely square-integrability as in the purely diffusive case. What goes wrong if $\eta_t = -1$ at some stopping time?

??? success "Solution to Exercise 6"
    **Why $\eta_t > -1$ is required:**

    In the Girsanov theorem for jump processes, the stochastic exponential that defines the measure change is:

    $$
    L_t = \mathcal{E}\left(\int_0^t \eta_s (dN_s - \lambda_s ds)\right) = \exp\left(-\int_0^t \eta_s \lambda_s ds\right) \prod_{0 < s \le t}(1 + \eta_s)^{\Delta N_s}
    $$

    **The requirement $\eta_t > -1$ ensures:**

    1. **Positivity of the density:** At each jump time $T_k$ of $N$, the density is multiplied by the factor $(1 + \eta_{T_k})$. For $L_t > 0$ (necessary for a valid probability density), we need $(1 + \eta_s) > 0$, i.e., $\eta_s > -1$, at all possible jump times.

    2. **Well-defined intensity:** The new intensity is $\lambda_t^{\mathbb{Q}} = (1 + \eta_t)\lambda_t$. For $\eta_t > -1$, we get $\lambda_t^{\mathbb{Q}} > 0$, which is necessary for a valid intensity.

    **What goes wrong if $\eta_t = -1$:**

    - The factor $(1 + \eta_t) = 0$, so at a jump occurring at time $t$, the density $L_t = 0$.
    - This means $\mathbb{Q}(\text{jump at time } t) = 0$ while $\mathbb{P}(\text{jump at time } t) > 0$, so $\mathbb{Q}$ is no longer equivalent to $\mathbb{P}$ (only absolutely continuous).
    - The new intensity $\lambda_t^{\mathbb{Q}} = 0$, meaning jumps are completely suppressed under $\mathbb{Q}$. This fundamentally changes the nature of the process---the jump component is "killed."
    - If $\eta_t = -1$ at a stopping time $T$, the density process $L$ hits zero and stays at zero thereafter (since one factor in the product is zero), making $\mathbb{Q}$ singular with respect to $\mathbb{P}$ on $\mathcal{F}_s$ for $s > T$.

    **Contrast with the diffusive case:**

    In the purely diffusive Girsanov theorem, the density is $L_t = \exp(-\int_0^t \gamma_s dW_s - \frac{1}{2}\int_0^t \gamma_s^2 ds)$, which is always strictly positive (being the exponential of a continuous process). The Novikov condition $\mathbb{E}[\exp(\frac{1}{2}\int_0^T \gamma_s^2 ds)] < \infty$ ensures $L$ is a true martingale (not just a local martingale), but positivity is automatic. For jump processes, positivity is not automatic---it requires the structural condition $\eta_t > -1$.
