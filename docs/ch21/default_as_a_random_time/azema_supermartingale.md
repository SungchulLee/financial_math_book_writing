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

---

**Exercise 2.** Prove that the Azema supermartingale $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t)$ satisfies $\mathbb{E}[G_t \mid \mathcal{F}_s] \le G_s$ for $s \le t$. In your proof, clearly identify where the inclusion $\{\tau > t\} \subseteq \{\tau > s\}$ is used.

---

**Exercise 3.** Under the Cox construction with CIR intensity $d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma\sqrt{\lambda_t}\,dW_t$, the Azema supermartingale is $G_t = e^{-\int_0^t \lambda_s\,ds}$. Apply Ito's formula to show that

$$
dG_t = -\lambda_t G_t\,dt + G_t \cdot (\text{martingale terms})
$$

Identify the compensator $dA_t = \lambda_t G_t\,dt$ and verify that the intensity equals $\lambda_t = dA_t / (G_{t-}\,dt)$.

---

**Exercise 4.** Explain why the Azema supermartingale for Azema's example ($\tau = \sup\{t \le 1 : W_t = 0\}$, the last zero of Brownian motion before time 1) has a singular Doob-Meyer decomposition. Why does no intensity exist in this case? What property of the local time of Brownian motion is responsible for the singularity?

---

**Exercise 5.** Using the pre-default pricing formula

$$
V_t = \frac{1}{G_t}\,\mathbb{E}\!\left[e^{-\int_t^T r_s\,ds}\,X \cdot G_T \mid \mathcal{F}_t\right]
$$

derive the price of a zero-coupon defaultable bond with zero recovery, constant risk-free rate $r$, and constant intensity $\lambda$. Show that the result is $V_t = e^{-(r+\lambda)(T-t)}$.

---

**Exercise 6.** Consider two default times $\tau_1$ and $\tau_2$ with respective Azema supermartingales $G_t^{(1)} = \mathbb{P}(\tau_1 > t \mid \mathcal{F}_t)$ and $G_t^{(2)} = \mathbb{P}(\tau_2 > t \mid \mathcal{F}_t)$. If $\tau_1$ and $\tau_2$ are conditionally independent given $\mathcal{F}_\infty$, show that the joint survival probability satisfies $\mathbb{P}(\tau_1 > t, \tau_2 > t \mid \mathcal{F}_t) = G_t^{(1)} G_t^{(2)}$.
