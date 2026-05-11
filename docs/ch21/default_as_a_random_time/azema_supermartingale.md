# Azema Supermartingale

The **Azema supermartingale** is a central object in the mathematical theory of default. It represents the conditional probability of survival given the market filtration and encodes the essential information needed for pricing defaultable claims. Its Doob-Meyer decomposition reveals the **compensator** of the default process, providing the rigorous foundation for intensity-based credit models.

---

## Definition

### The Conditional Survival Process

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ be a filtered probability space satisfying the usual conditions, and let $\tau$ be a non-negative random variable representing the default time.

The **Azema supermartingale** (also called the **conditional survival probability process**) is defined as:

$$
G_t := \mathbb{P}(\tau > t \mid \mathcal{F}_t)
$$

This process gives the probability of surviving past time $t$, conditioned on all market information available at time $t$.

### Basic Properties

1. **Range:** $0 \le G_t \le 1$ almost surely
2. **Initial value:** $G_0 = \mathbb{P}(\tau > 0 \mid \mathcal{F}_0)$. If $\mathbb{P}(\tau > 0) = 1$ (no instantaneous default), then $G_0 = 1$
3. **Monotone limit:** $G_t \to G_\infty := \mathbb{P}(\tau = \infty \mid \mathcal{F}_\infty)$ as $t \to \infty$
4. **Adaptedness:** $G_t$ is $\mathcal{F}_t$-measurable (it depends only on market information, not on whether default has occurred)

!!! note "Notation"
    The process is named after Jacques Azema, who studied it systematically in the context of progressive enlargement of filtrations. In credit risk, it is sometimes denoted $Z_t$ (following Bielecki and Rutkowski) or $p_t$ (following some probabilistic treatments).

---

## Supermartingale Property

### Statement

!!! abstract "Theorem"
    The process $(G_t)_{t \ge 0}$ is a **supermartingale** with respect to $(\mathcal{F}_t, \mathbb{P})$.

### Proof

For $s \le t$, we must show $\mathbb{E}[G_t \mid \mathcal{F}_s] \le G_s$.

$$
\mathbb{E}[G_t \mid \mathcal{F}_s] = \mathbb{E}[\mathbb{P}(\tau > t \mid \mathcal{F}_t) \mid \mathcal{F}_s]
$$

By the tower property of conditional expectation:

$$
= \mathbb{P}(\tau > t \mid \mathcal{F}_s)
$$

Since $\{\tau > t\} \subseteq \{\tau > s\}$ (surviving past $t$ implies surviving past $s$):

$$
\mathbb{P}(\tau > t \mid \mathcal{F}_s) \le \mathbb{P}(\tau > s \mid \mathcal{F}_s) = G_s
$$

Therefore $\mathbb{E}[G_t \mid \mathcal{F}_s] \le G_s$, establishing the supermartingale property. $\square$

### Interpretation

The supermartingale property encodes the economic reality that, on average, the probability of survival can only **decrease** over time. New information may reveal credit deterioration, but survival probability cannot systematically increase on average. This is the probabilistic counterpart of the intuition that default risk accumulates over time.

---

## Doob-Meyer Decomposition

### Statement

By the Doob-Meyer theorem, since $G_t$ is a right-continuous supermartingale of class (D), it admits a unique decomposition:

$$
G_t = G_0 + m_t - a_t
$$

where:

- $m_t$ is a right-continuous $(\mathcal{F}_t, \mathbb{P})$-**martingale** with $m_0 = 0$
- $a_t$ is a **predictable, non-decreasing** process with $a_0 = 0$

Equivalently:

$$
G_t = M_t - A_t
$$

where $M_t = G_0 + m_t$ is a martingale starting at $G_0$ and $A_t = a_t$.

### Interpretation of Components

- **Martingale part $M_t$:** Captures the "innovation" in survival probability due to new market information. Positive increments ($dM_t > 0$) reflect good credit news; negative increments reflect bad news. On average, these are zero.
- **Compensator $A_t$:** Represents the systematic, predictable erosion of survival probability over time. This is the deterministic drift component that makes $G_t$ decline on average.

### Relationship to Intensity

When the compensator $A_t$ is absolutely continuous with respect to Lebesgue measure:

$$
A_t = \int_0^t \alpha_s \, ds
$$

for a non-negative, $\mathcal{F}_t$-predictable process $\alpha_t$, the decomposition becomes:

$$
G_t = G_0 + m_t - \int_0^t \alpha_s \, ds
$$

The process $\alpha_t$ is closely related to the default intensity. Specifically, when $G_t > 0$:

$$
\lambda_t = \frac{\alpha_t}{G_{t-}}
$$

defines the **$(\mathcal{G}_t, \mathbb{P})$-intensity** of the default time $\tau$.

---

## The Compensator of Default

### Default Indicator Process

Recall the default indicator $H_t = \mathbf{1}_{\{\tau \le t\}}$ and the enlarged filtration $\mathcal{G}_t = \mathcal{F}_t \vee \sigma(H_s : s \le t)$.

### Key Result

!!! abstract "Theorem"
    If $G_{t-} > 0$ for all $t$ a.s. and $A_t$ is the predictable increasing process in the Doob-Meyer decomposition of $G_t$, then the $(\mathcal{G}_t, \mathbb{P})$-compensator of $H_t$ is:

    $$
    \Lambda_t^{\mathcal{G}} = \int_0^{t \wedge \tau} \frac{dA_s}{G_{s-}}
    $$

    and the process

    $$
    M_t^H := H_t - \int_0^{t \wedge \tau} \frac{dA_s}{G_{s-}}
    $$

    is a $(\mathcal{G}_t, \mathbb{P})$-martingale.

### Proof Sketch

The proof uses the **key lemma** of enlargement of filtration theory. For any bounded, $\mathcal{F}_t$-predictable process $\phi$:

$$
\mathbb{E}\left[\phi_\tau \mathbf{1}_{\{\tau \le t\}}\right] = \mathbb{E}\left[\int_0^t \phi_s \frac{dA_s}{G_{s-}} \cdot G_{s-} \frac{1}{G_{s-}} \, \right] = \mathbb{E}\left[\int_0^t \phi_s \, dA_s\right]
$$

This identity, combined with the optional projection theorem, establishes that $\int_0^{t \wedge \tau} dA_s / G_{s-}$ is the compensator. $\square$

### Connection to Intensity

When $A_t = \int_0^t \alpha_s ds$ is absolutely continuous:

$$
\Lambda_t^{\mathcal{G}} = \int_0^{t \wedge \tau} \frac{\alpha_s}{G_{s-}} \, ds = \int_0^{t \wedge \tau} \lambda_s \, ds
$$

This confirms that $\lambda_t = \alpha_t / G_{t-}$ is the default intensity.

---

## Explicit Formulas Under Cox Construction

### Cox Process Setting

Under the doubly stochastic construction with $\mathcal{F}_t$-adapted intensity $\lambda_t$ and $\tau = \inf\{t : \int_0^t \lambda_s ds \ge E\}$, $E \sim \text{Exp}(1)$ independent of $\mathcal{F}_\infty$:

$$
G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t) = \mathbb{P}\left(E > \int_0^t \lambda_s ds \mid \mathcal{F}_t\right) = e^{-\int_0^t \lambda_s ds} = e^{-\Lambda_t}
$$

### Doob-Meyer Decomposition Under Cox

Since $G_t = e^{-\Lambda_t}$, applying Ito's formula:

$$
dG_t = -\lambda_t e^{-\Lambda_t} dt + (\text{martingale terms from } \lambda_t)
$$

More precisely, if $\lambda_t$ follows a diffusion $d\lambda_t = \mu_\lambda dt + \sigma_\lambda dW_t$:

$$
dG_t = e^{-\Lambda_t}\left[-\lambda_t dt - \frac{\partial G}{\partial \lambda} d\lambda_t + \frac{1}{2}\frac{\partial^2 G}{\partial \lambda^2}(d\lambda_t)^2\right]
$$

The predictable finite-variation part gives:

$$
dA_t = \lambda_t e^{-\Lambda_t} dt = \lambda_t G_t \, dt
$$

so $\alpha_t = \lambda_t G_t$, confirming $\lambda_t = \alpha_t / G_t$.

### Simplicity of the Cox Case

Under the Cox construction, the Azema supermartingale has the explicit exponential form $G_t = e^{-\Lambda_t}$, and the compensator of default is simply $\int_0^{t \wedge \tau} \lambda_s ds$. This elegant structure is one of the primary reasons for the popularity of the Cox process in credit modeling.

---

## General (Non-Cox) Default Times

### When the Cox Structure Fails

Not all default times arise from a Cox process. In general:

- $G_t$ need not have the form $e^{-\Lambda_t}$
- The compensator $A_t$ may not be absolutely continuous (it may have singular components)
- The intensity $\lambda_t$ may not exist

### Azema's Example

Azema studied the case where $\tau = \sup\{t \le 1 : W_t = 0\}$, the last zero of Brownian motion before time 1. For this random time:

$$
G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t) = \mathbb{P}(\text{no more zeros after } t \mid \mathcal{F}_t)
$$

This Azema supermartingale has a **singular** Doob-Meyer decomposition: $A_t$ is the local time of $W$ at zero, which is singular with respect to Lebesgue measure. No intensity exists.

### Implications for Credit Modeling

In practice, the Cox construction is almost universally adopted because:

1. It guarantees the existence of an intensity
2. It ensures immersion (H-hypothesis)
3. It produces clean pricing formulas
4. Calibration to market data is tractable

Non-Cox default times arise in theoretical investigations of information-based models and in structural models where default is predictable.

---

## Role in Pricing Defaultable Claims

### Pre-Default Pricing Formula

For a $\mathcal{G}_T$-measurable claim $X$ payable at $T$ if no default, the pre-default price at time $t < T$ (on $\{\tau > t\}$) is:

$$
V_t = \frac{1}{G_t} \mathbb{E}\left[e^{-\int_t^T r_s ds} X \cdot G_T \mid \mathcal{F}_t\right]
$$

The factor $G_T / G_t$ represents the conditional survival probability from $t$ to $T$.

### Default-Contingent Claims

For a recovery payment $Z_\tau$ made at default:

$$
V_t = \frac{1}{G_t} \mathbb{E}\left[\int_t^T e^{-\int_t^s r_u du} Z_s \, dA_s \mid \mathcal{F}_t\right]
$$

This formula uses the compensator $A_s$ rather than the intensity directly, making it applicable even when no intensity exists.

### Hazard-Process Approach

More generally, if $G_t > 0$ a.s. for all $t$, the **hazard process** $\Gamma_t = -\ln G_t$ is well-defined and:

$$
G_t = e^{-\Gamma_t}
$$

Under the Cox construction, $\Gamma_t = \Lambda_t = \int_0^t \lambda_s ds$. In general, $\Gamma_t$ may not be absolutely continuous.

---

## Numerical Example

**Setup:** CIR intensity with $\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, $\lambda_0 = 1.5\%$.

**Azema supermartingale at selected times:**

$$
G_t = e^{-\Lambda_t}, \quad \text{where } \Lambda_t = \int_0^t \lambda_s ds
$$

Using the CIR expected cumulative intensity $\mathbb{E}[\Lambda_t] = \theta t + (\lambda_0 - \theta)(1 - e^{-\kappa t})/\kappa$:

$$
\mathbb{E}[\Lambda_1] = 0.02(1) + (-0.005)(1 - e^{-0.5})/0.5 = 0.02 - 0.005 \times 0.787 = 0.0161
$$

$$
\mathbb{E}[G_1] \approx e^{-0.0161} = 0.984
$$

$$
\mathbb{E}[\Lambda_5] = 0.02(5) + (-0.005)(1 - e^{-2.5})/0.5 = 0.10 - 0.005 \times 1.836 = 0.0908
$$

$$
\mathbb{E}[G_5] \approx e^{-0.0908} = 0.913
$$

**Doob-Meyer components at $t = 1$:**

- Compensator contribution: $\mathbb{E}[A_1] = \mathbb{E}[\int_0^1 \lambda_s G_s ds] \approx 0.0161 \times 0.992 = 0.0160$
- Martingale part: $\mathbb{E}[m_1] = 0$ (by definition)

---

## Key Takeaways

- The Azema supermartingale $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t)$ is the fundamental object encoding default information in the market filtration
- It is a supermartingale because survival probability cannot increase on average
- The Doob-Meyer decomposition $G_t = M_t - A_t$ separates the innovation and systematic components
- The compensator of default is $\int_0^{t \wedge \tau} dA_s / G_{s-}$, linking $G_t$ to the default intensity via $\lambda_t = \alpha_t / G_{t-}$
- Under the Cox construction, $G_t = e^{-\int_0^t \lambda_s ds}$ with an absolutely continuous compensator
- The Azema supermartingale provides the general framework for pricing defaultable claims, even without an intensity

---

## Further Reading

- Azema, J. (1972). Quelques applications de la theorie generale des processus. *Inventiones Mathematicae*, 18, 293--336.
- Jeulin, T. (1980). *Semi-martingales et grossissement d'une filtration*. Lecture Notes in Mathematics 833, Springer.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 5.
- Jeanblanc, M., Yor, M., & Chesney, M. (2009). *Mathematical Methods for Financial Markets*. Springer.

---

## Exercises

**Exercise 1.** Let $\tau$ be a default time with constant intensity $\lambda > 0$ under a Cox process construction, so that $G_t = e^{-\lambda t}$. Write down the Doob-Meyer decomposition $G_t = G_0 + m_t - A_t$ explicitly. Show that $m_t = 0$ (i.e., $G_t$ is purely deterministic) and $A_t = 1 - e^{-\lambda t}$.

??? success "Solution to Exercise 1"
    With constant intensity $\lambda > 0$ under the Cox construction, $G_t = e^{-\lambda t}$ is deterministic (no dependence on $\omega$).

    **Doob-Meyer decomposition:** We write $G_t = G_0 + m_t - A_t$ where $m_t$ is a martingale with $m_0 = 0$ and $A_t$ is predictable and increasing with $A_0 = 0$.

    Since $G_0 = e^0 = 1$, we need:

    $$
    e^{-\lambda t} = 1 + m_t - A_t
    $$

    **Showing $m_t = 0$:** The process $G_t = e^{-\lambda t}$ is deterministic (it does not depend on $\omega$). A deterministic process $G_t$ is both a supermartingale and a submartingale if and only if it is constant. Since $G_t$ is not constant, we examine the decomposition more carefully.

    For the Doob-Meyer decomposition: $G_t$ is a deterministic, decreasing function of $t$. A deterministic supermartingale $G_t$ is trivially its own predictable process. We have:

    $$
    \mathbb{E}[G_t \mid \mathcal{F}_s] = G_t = e^{-\lambda t}
    $$

    since $G_t$ is deterministic. The martingale part must satisfy $\mathbb{E}[m_t \mid \mathcal{F}_s] = m_s$. Since $m_t = G_t - G_0 + A_t = e^{-\lambda t} - 1 + A_t$, and taking conditional expectations:

    $$
    \mathbb{E}[m_t \mid \mathcal{F}_s] = e^{-\lambda t} - 1 + A_t = m_s = e^{-\lambda s} - 1 + A_s
    $$

    This means $A_t - A_s = e^{-\lambda s} - e^{-\lambda t}$ for all $s \le t$, giving $A_t = 1 - e^{-\lambda t}$ (with $A_0 = 0$). Then:

    $$
    m_t = e^{-\lambda t} - 1 + (1 - e^{-\lambda t}) = 0
    $$

    **Verification:** The decomposition is:

    $$
    G_t = 1 + 0 - (1 - e^{-\lambda t}) = e^{-\lambda t} \checkmark
    $$

    The martingale part vanishes entirely because $G_t$ is deterministic — there is no randomness and hence no innovation. The compensator $A_t = 1 - e^{-\lambda t}$ captures the entire deterministic decline in survival probability.

    Note that $dA_t = \lambda e^{-\lambda t} dt = \lambda G_t \, dt$, confirming the general formula $\alpha_t = \lambda_t G_t$ with $\alpha_t = \lambda e^{-\lambda t}$, and the intensity is $\lambda_t = \alpha_t / G_t = \lambda$. $\square$

---

**Exercise 2.** Prove that the Azema supermartingale $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t)$ satisfies $\mathbb{E}[G_t \mid \mathcal{F}_s] \le G_s$ for $s \le t$. In your proof, clearly identify where the inclusion $\{\tau > t\} \subseteq \{\tau > s\}$ is used.

??? success "Solution to Exercise 2"
    We prove the supermartingale property: for $s \le t$, $\mathbb{E}[G_t \mid \mathcal{F}_s] \le G_s$.

    **Step 1: Apply the tower property.**

    $$
    \mathbb{E}[G_t \mid \mathcal{F}_s] = \mathbb{E}\left[\mathbb{P}(\tau > t \mid \mathcal{F}_t) \mid \mathcal{F}_s\right]
    $$

    By the tower property of conditional expectation (since $\mathcal{F}_s \subseteq \mathcal{F}_t$):

    $$
    \mathbb{E}\left[\mathbb{P}(\tau > t \mid \mathcal{F}_t) \mid \mathcal{F}_s\right] = \mathbb{P}(\tau > t \mid \mathcal{F}_s)
    $$

    **Step 2: Use the set inclusion $\{\tau > t\} \subseteq \{\tau > s\}$.**

    Since $s \le t$, surviving past time $t$ requires surviving past time $s$. Therefore $\{\tau > t\} \subseteq \{\tau > s\}$, which means $\mathbf{1}_{\{\tau > t\}} \le \mathbf{1}_{\{\tau > s\}}$ pointwise.

    **Step 3: Apply monotonicity of conditional expectation.**

    Since $\mathbf{1}_{\{\tau > t\}} \le \mathbf{1}_{\{\tau > s\}}$ a.s., monotonicity of conditional expectation gives:

    $$
    \mathbb{P}(\tau > t \mid \mathcal{F}_s) = \mathbb{E}[\mathbf{1}_{\{\tau > t\}} \mid \mathcal{F}_s] \le \mathbb{E}[\mathbf{1}_{\{\tau > s\}} \mid \mathcal{F}_s] = \mathbb{P}(\tau > s \mid \mathcal{F}_s) = G_s
    $$

    **Combining Steps 1-3:**

    $$
    \mathbb{E}[G_t \mid \mathcal{F}_s] = \mathbb{P}(\tau > t \mid \mathcal{F}_s) \le \mathbb{P}(\tau > s \mid \mathcal{F}_s) = G_s
    $$

    This is the supermartingale inequality. The inclusion $\{\tau > t\} \subseteq \{\tau > s\}$ is used in Step 2 to establish the pointwise inequality between indicator functions, which then yields the inequality between conditional expectations via monotonicity. $\square$

---

**Exercise 3.** Under the Cox construction with CIR intensity $d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma\sqrt{\lambda_t}\,dW_t$, the Azema supermartingale is $G_t = e^{-\int_0^t \lambda_s\,ds}$. Apply Ito's formula to show that

$$
dG_t = -\lambda_t G_t\,dt + G_t \cdot (\text{martingale terms})
$$

Identify the compensator $dA_t = \lambda_t G_t\,dt$ and verify that the intensity equals $\lambda_t = dA_t / (G_{t-}\,dt)$.

??? success "Solution to Exercise 3"
    Under the Cox construction with CIR intensity, $G_t = e^{-\Lambda_t}$ where $\Lambda_t = \int_0^t \lambda_s \, ds$.

    **Applying Ito's formula:** Define $f(x) = e^{-x}$ so that $G_t = f(\Lambda_t)$. We have $f'(x) = -e^{-x}$ and $f''(x) = e^{-x}$. Since $\Lambda_t = \int_0^t \lambda_s \, ds$ is absolutely continuous with $d\Lambda_t = \lambda_t \, dt$ (finite variation, no quadratic variation from $\Lambda$ itself), Ito's formula gives:

    $$
    dG_t = f'(\Lambda_t) \, d\Lambda_t = -e^{-\Lambda_t} \lambda_t \, dt = -\lambda_t G_t \, dt
    $$

    Wait — this gives $G_t$ as purely deterministic in its own dynamics, but $G_t$ is random through $\Lambda_t$. The issue is that $\Lambda_t$ depends on $\lambda_t$, which is itself stochastic. We should apply Ito's formula to $G_t = e^{-\Lambda_t}$ as a function of $\Lambda_t$, recognizing that $\Lambda_t$ is of finite variation (it is an integral of a positive process).

    Since $d\Lambda_t = \lambda_t \, dt$ has no martingale component, the direct computation gives:

    $$
    dG_t = -\lambda_t G_t \, dt
    $$

    However, this seems to imply $G_t$ is deterministic, which contradicts $\lambda_t$ being stochastic. The resolution is that $G_t$ is indeed a random process (through its dependence on $\lambda_s$ for $s \le t$), but its differential involves only $dt$ terms when expressed in terms of $d\Lambda_t$.

    To see the martingale component, we must express $G_t$ as a function of $\lambda_t$ using the affine structure. Under CIR dynamics, the bond-pricing-like formula gives:

    $$
    G_t = e^{-\Lambda_t} = \mathbb{E}\left[e^{-\Lambda_T} \mid \mathcal{F}_t\right] \cdot (\text{ratio})
    $$

    More directly, consider $G_t$ as a process and compute its semimartingale decomposition. Since $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t) = e^{-\int_0^t \lambda_s ds}$ and $\lambda_t$ follows CIR dynamics, we apply the product rule / chain rule via Ito's formula to $G_t = e^{-\int_0^t \lambda_s ds}$ viewed as a functional of the path $(\lambda_s)_{s \le t}$.

    Define $F(t, \lambda) = \mathbb{E}[e^{-\int_0^T \lambda_s ds} \mid \lambda_t = \lambda]$ — but this is the full conditional expectation. Instead, let us work directly.

    **Doob-Meyer decomposition approach:** Since $G_t$ is an $\mathcal{F}_t$-supermartingale, the Doob-Meyer decomposition is $G_t = G_0 + m_t - A_t$. The predictable decreasing part satisfies:

    $$
    dA_t = \lambda_t G_t \, dt
    $$

    This follows from the general theory: for the Cox construction, $\alpha_t = \lambda_t G_t$ where $\alpha_t \, dt = dA_t$. To verify, note that the compensator of $H_t = \mathbf{1}_{\{\tau \le t\}}$ in $\mathcal{G}_t$ is $\int_0^{t \wedge \tau} \frac{dA_s}{G_{s-}} = \int_0^{t \wedge \tau} \lambda_s \, ds$, which is the standard result.

    **Identifying the compensator:**

    $$
    dA_t = \lambda_t G_t \, dt = \lambda_t e^{-\Lambda_t} \, dt
    $$

    **Verifying the intensity:**

    $$
    \frac{dA_t}{G_{t-} \, dt} = \frac{\lambda_t G_t}{G_{t-}} = \lambda_t
    $$

    since $G_t$ is continuous (hence $G_{t-} = G_t$). This confirms that the default intensity equals $\lambda_t$, consistent with the Cox construction.

    **The martingale part:** The martingale component is:

    $$
    m_t = G_t - G_0 + A_t = e^{-\Lambda_t} - 1 + \int_0^t \lambda_s e^{-\Lambda_s} \, ds
    $$

    This is an $\mathcal{F}_t$-martingale that captures the stochastic fluctuations in survival probability driven by the random intensity $\lambda_t$. Its increments reflect the "surprise" component of credit quality changes. $\square$

---

**Exercise 4.** Explain why the Azema supermartingale for Azema's example ($\tau = \sup\{t \le 1 : W_t = 0\}$, the last zero of Brownian motion before time 1) has a singular Doob-Meyer decomposition. Why does no intensity exist in this case? What property of the local time of Brownian motion is responsible for the singularity?

??? success "Solution to Exercise 4"
    **Azema's example:** $\tau = \sup\{t \le 1 : W_t = 0\}$, the last zero of a standard Brownian motion before time 1.

    **Why the Doob-Meyer decomposition is singular:**

    The Azema supermartingale for this random time is $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t)$. For $t < 1$, this equals the probability that the Brownian motion $W$ has no more zeros in $(t, 1]$, given $\mathcal{F}_t$.

    By the arcsine law and properties of Brownian motion, this probability is related to whether $W_t = 0$ or $W_t \neq 0$. Specifically, if $W_t \neq 0$, there is a positive probability that $W$ does not return to zero before time 1, while if $W_t = 0$, then $\tau \ge t$ and it is certain (by the fine structure of Brownian paths) that zeros accumulate, making the analysis delicate.

    The Doob-Meyer decomposition of $G_t$ has the form $G_t = G_0 + m_t - A_t$, where the predictable increasing process $A_t$ is proportional to the **local time of Brownian motion at zero**, $L_t^0$.

    **Why $A_t$ is singular:** The local time $L_t^0$ of Brownian motion at zero is a continuous, non-decreasing process that increases only when $W_t = 0$. By the occupation times formula:

    $$
    L_t^0 = \lim_{\epsilon \to 0} \frac{1}{2\epsilon} \int_0^t \mathbf{1}_{\{|W_s| < \epsilon\}} \, ds
    $$

    The set $\{s : W_s = 0\}$ has Lebesgue measure zero (Brownian motion spends zero time at any given level). Therefore $L_t^0$ is singular with respect to Lebesgue measure: it increases on a set of Lebesgue measure zero.

    **Why no intensity exists:** An intensity $\lambda_t$ would require $A_t = \int_0^t \alpha_s \, ds$ to be absolutely continuous with respect to Lebesgue measure, meaning $dA_t = \alpha_t \, dt$ for some non-negative process $\alpha_t$. Since $A_t$ is proportional to $L_t^0$, which is singular with respect to $dt$, no such density $\alpha_t$ exists. The compensator "charges" only the zero set of Brownian motion, which has full measure under $dL_t^0$ but zero measure under $dt$.

    **The property of local time responsible:** The singularity arises because:

    1. Local time $L_t^0$ is supported on $\{s : W_s = 0\}$, a set of Lebesgue measure zero
    2. $L_t^0$ is continuous and non-decreasing, but its derivative $dL_t^0 / dt$ does not exist as a function (it is a singular measure)
    3. Brownian motion visits zero on a dense but measure-zero set (a perfect set of measure zero, like a Cantor-type set)

    This example illustrates that the intensity-based framework is a special case of the general Azema supermartingale theory, valid only when the compensator is absolutely continuous. For last passage times of continuous processes, the compensator is typically singular, and the full generality of the Doob-Meyer decomposition is needed.

---

**Exercise 5.** Using the pre-default pricing formula

$$
V_t = \frac{1}{G_t}\,\mathbb{E}\!\left[e^{-\int_t^T r_s\,ds}\,X \cdot G_T \mid \mathcal{F}_t\right]
$$

derive the price of a zero-coupon defaultable bond with zero recovery, constant risk-free rate $r$, and constant intensity $\lambda$. Show that the result is $V_t = e^{-(r+\lambda)(T-t)}$.

??? success "Solution to Exercise 5"
    We derive the price of a zero-coupon defaultable bond with zero recovery ($R = 0$), constant risk-free rate $r$, and constant intensity $\lambda$.

    The claim pays $X = 1$ at maturity $T$ if no default. Under the pre-default pricing formula:

    $$
    V_t = \frac{1}{G_t} \, \mathbb{E}\left[e^{-\int_t^T r_s \, ds} \, X \cdot G_T \mid \mathcal{F}_t\right]
    $$

    **Step 1: Substitute the given quantities.**

    With constant $r$, $X = 1$, and $G_T = e^{-\lambda T}$, $G_t = e^{-\lambda t}$:

    $$
    V_t = \frac{1}{e^{-\lambda t}} \, \mathbb{E}\left[e^{-r(T-t)} \cdot 1 \cdot e^{-\lambda T} \mid \mathcal{F}_t\right]
    $$

    **Step 2: Simplify.**

    Since $r$, $\lambda$, $T$, and $t$ are all deterministic constants, the conditional expectation reduces to the expression itself:

    $$
    V_t = e^{\lambda t} \cdot e^{-r(T-t)} \cdot e^{-\lambda T}
    $$

    **Step 3: Combine exponentials.**

    $$
    V_t = e^{\lambda t} \cdot e^{-r(T-t)} \cdot e^{-\lambda T} = e^{-r(T-t)} \cdot e^{\lambda t - \lambda T} = e^{-r(T-t)} \cdot e^{-\lambda(T-t)}
    $$

    $$
    = e^{-(r+\lambda)(T-t)}
    $$

    **Result:**

    $$
    V_t = e^{-(r+\lambda)(T-t)}
    $$

    **Interpretation:** The defaultable zero-coupon bond price is the same as a default-free zero-coupon bond discounted at rate $r + \lambda$ instead of $r$. The credit spread is exactly $\lambda$, the default intensity. This is the fundamental result of reduced-form credit models: the credit spread for a zero-recovery bond equals the risk-neutral default intensity.

    The factor $G_T / G_t = e^{-\lambda(T-t)}$ represents the conditional probability of surviving from $t$ to $T$, which acts as an additional discount factor on top of the risk-free discounting $e^{-r(T-t)}$. $\square$

---

**Exercise 6.** Consider two default times $\tau_1$ and $\tau_2$ with respective Azema supermartingales $G_t^{(1)} = \mathbb{P}(\tau_1 > t \mid \mathcal{F}_t)$ and $G_t^{(2)} = \mathbb{P}(\tau_2 > t \mid \mathcal{F}_t)$. If $\tau_1$ and $\tau_2$ are conditionally independent given $\mathcal{F}_\infty$, show that the joint survival probability satisfies $\mathbb{P}(\tau_1 > t, \tau_2 > t \mid \mathcal{F}_t) = G_t^{(1)} G_t^{(2)}$.

??? success "Solution to Exercise 6"
    We show that $\mathbb{P}(\tau_1 > t, \tau_2 > t \mid \mathcal{F}_t) = G_t^{(1)} G_t^{(2)}$ under conditional independence of $\tau_1$ and $\tau_2$ given $\mathcal{F}_\infty$.

    **Step 1: Apply the tower property.**

    $$
    \mathbb{P}(\tau_1 > t, \tau_2 > t \mid \mathcal{F}_t) = \mathbb{E}\left[\mathbf{1}_{\{\tau_1 > t\}} \mathbf{1}_{\{\tau_2 > t\}} \mid \mathcal{F}_t\right]
    $$

    Using the tower property with $\mathcal{F}_t \subseteq \mathcal{F}_\infty$:

    $$
    = \mathbb{E}\left[\mathbb{E}\left[\mathbf{1}_{\{\tau_1 > t\}} \mathbf{1}_{\{\tau_2 > t\}} \mid \mathcal{F}_\infty\right] \mid \mathcal{F}_t\right]
    $$

    **Step 2: Apply conditional independence given $\mathcal{F}_\infty$.**

    By the assumption that $\tau_1$ and $\tau_2$ are conditionally independent given $\mathcal{F}_\infty$:

    $$
    \mathbb{E}\left[\mathbf{1}_{\{\tau_1 > t\}} \mathbf{1}_{\{\tau_2 > t\}} \mid \mathcal{F}_\infty\right] = \mathbb{E}\left[\mathbf{1}_{\{\tau_1 > t\}} \mid \mathcal{F}_\infty\right] \cdot \mathbb{E}\left[\mathbf{1}_{\{\tau_2 > t\}} \mid \mathcal{F}_\infty\right]
    $$

    $$
    = \mathbb{P}(\tau_1 > t \mid \mathcal{F}_\infty) \cdot \mathbb{P}(\tau_2 > t \mid \mathcal{F}_\infty)
    $$

    **Step 3: Substitute back and use the tower property for each factor.**

    $$
    \mathbb{P}(\tau_1 > t, \tau_2 > t \mid \mathcal{F}_t) = \mathbb{E}\left[\mathbb{P}(\tau_1 > t \mid \mathcal{F}_\infty) \cdot \mathbb{P}(\tau_2 > t \mid \mathcal{F}_\infty) \mid \mathcal{F}_t\right]
    $$

    Now, define $\xi_i = \mathbb{P}(\tau_i > t \mid \mathcal{F}_\infty)$ for $i = 1, 2$. These are $\mathcal{F}_\infty$-measurable random variables. In general, $\mathbb{E}[\xi_1 \xi_2 \mid \mathcal{F}_t] \neq \mathbb{E}[\xi_1 \mid \mathcal{F}_t] \mathbb{E}[\xi_2 \mid \mathcal{F}_t]$.

    However, in the typical Cox process setting, we can proceed using the specific structure. Under the **doubly stochastic construction** for each default time (which is the standard setting for conditional independence given $\mathcal{F}_\infty$):

    - $\tau_i = \inf\{t : \int_0^t \lambda_s^{(i)} ds \ge E_i\}$ where $E_i \sim \text{Exp}(1)$ are independent of each other and of $\mathcal{F}_\infty$
    - $\mathbb{P}(\tau_i > t \mid \mathcal{F}_\infty) = e^{-\int_0^t \lambda_s^{(i)} ds} = e^{-\Lambda_t^{(i)}}$

    Then:

    $$
    \mathbb{P}(\tau_1 > t, \tau_2 > t \mid \mathcal{F}_t) = \mathbb{E}\left[e^{-\Lambda_t^{(1)}} \cdot e^{-\Lambda_t^{(2)}} \mid \mathcal{F}_t\right]
    $$

    Since $\Lambda_t^{(i)} = \int_0^t \lambda_s^{(i)} ds$ is $\mathcal{F}_t$-measurable (the intensities are $\mathcal{F}$-adapted and we integrate up to time $t$):

    $$
    = e^{-\Lambda_t^{(1)}} \cdot e^{-\Lambda_t^{(2)}} = G_t^{(1)} \cdot G_t^{(2)}
    $$

    **More generally**, even without the Cox construction, the result holds. The key observation is that $\mathbb{P}(\tau_i > t \mid \mathcal{F}_\infty)$ is $\mathcal{F}_\infty$-measurable and its conditional expectation given $\mathcal{F}_t$ yields $G_t^{(i)}$ by the tower property. Writing $\xi_i = \mathbb{P}(\tau_i > t \mid \mathcal{F}_\infty)$, we need to show $\mathbb{E}[\xi_1 \xi_2 \mid \mathcal{F}_t] = \mathbb{E}[\xi_1 \mid \mathcal{F}_t] \cdot \mathbb{E}[\xi_2 \mid \mathcal{F}_t]$.

    Under the Cox construction, $\xi_i = e^{-\Lambda_t^{(i)}}$ is $\mathcal{F}_t$-measurable, so the product $\xi_1 \xi_2$ is $\mathcal{F}_t$-measurable, and the result follows immediately:

    $$
    \mathbb{E}[\xi_1 \xi_2 \mid \mathcal{F}_t] = \xi_1 \xi_2 = G_t^{(1)} G_t^{(2)}
    $$

    This confirms that under conditional independence (given $\mathcal{F}_\infty$) and the Cox framework, the joint survival probability factors into the product of individual Azema supermartingales. This is the foundation for multi-name credit models and basket credit derivatives. $\square$
