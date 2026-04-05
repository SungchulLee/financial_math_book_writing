# Stopping Times and Enlargement of Filtration

Credit risk models represent default as a **random time** $\tau$. To incorporate default into a stochastic framework rigorously, one must understand stopping times and the enlargement of filtrations. This foundational machinery enables consistent pricing and hedging in the presence of default events.

---

## Filtrations and Information Flow

A filtration $(\mathcal{F}_t)_{t \ge 0}$ represents the information available up to time $t$. In default-free models, $\mathcal{F}_t$ typically contains information about market factors such as asset prices, interest rates, and other observable quantities. Formally, we require:

1. **Right-continuity:** $\mathcal{F}_t = \mathcal{F}_{t+} := \bigcap_{s > t} \mathcal{F}_s$
2. **Completeness:** $\mathcal{F}_0$ contains all $\mathbb{P}$-null sets

These are the **usual conditions** ensuring technical regularity.

Introducing default requires expanding this information set to include knowledge of whether default has occurred.

---

## Default Time as a Stopping Time

A random time $\tau: \Omega \to [0, \infty]$ is a **stopping time** with respect to a filtration $(\mathcal{G}_t)$ if

$$
\{\tau \le t\} \in \mathcal{G}_t \quad \text{for all } t \ge 0
$$

Equivalently, under right-continuous filtrations, $\{\tau < t\} \in \mathcal{G}_t$ for all $t$.

**Interpretation:** At any time $t$, we can determine whether default has already occurred. This is the minimal requirement for default to be observable.

A stronger condition is **predictability**: $\tau$ is predictable if there exists an increasing sequence of stopping times $(\tau_n)$ with $\tau_n < \tau$ on $\{\tau > 0\}$ and $\tau_n \uparrow \tau$. In structural models, default is often predictable (hitting times of continuous processes). In reduced-form models, default is typically **totally inaccessible**—it cannot be anticipated by any announcing sequence.

---

## The Default Indicator Process

The **default indicator** is the process

$$
H_t := \mathbf{1}_{\{\tau \le t\}}
$$

This is a right-continuous, non-decreasing process that jumps from 0 to 1 at the moment of default. Key properties:

- $H_t$ is $\mathcal{G}_t$-adapted when $\tau$ is a $(\mathcal{G}_t)$-stopping time
- $H_t$ is a **submartingale** (non-decreasing processes are always submartingales)
- The jump $\Delta H_\tau = 1$ occurs at a single random time

---

## Enlargement of Filtration

To model default within the existing market framework, we **enlarge** the default-free filtration $(\mathcal{F}_t)$ to a larger filtration $(\mathcal{G}_t)$ such that:

1. $\tau$ is a stopping time in $(\mathcal{G}_t)$
2. $\mathcal{F}_t \subseteq \mathcal{G}_t$ for all $t$

This process is known as **enlargement of filtration**. The enlarged filtration contains both market information and default information.

### Minimal Enlargement

The **minimal enlargement** making $\tau$ a stopping time is

$$
\mathcal{G}_t = \mathcal{F}_t \vee \mathcal{H}_t
$$

where $\mathcal{H}_t = \sigma(H_s : s \le t) = \sigma(\mathbf{1}_{\{\tau \le s\}} : s \le t)$.

This can be written more explicitly as

$$
\mathcal{G}_t = \bigcap_{s > t} \left( \mathcal{F}_s \vee \sigma(\tau \wedge s) \right)
$$

Every $\mathcal{G}_t$-measurable random variable $X$ admits the representation

$$
X = X_0 \mathbf{1}_{\{\tau > t\}} + X_1(\tau) \mathbf{1}_{\{\tau \le t\}}
$$

where $X_0$ is $\mathcal{F}_t$-measurable and $X_1(s)$ is $\mathcal{F}_t \otimes \mathcal{B}([0,t])$-measurable.

---

## The Azéma Supermartingale

A fundamental object in the theory is the **Azéma supermartingale**:

$$
G_t := \mathbb{P}(\tau > t \mid \mathcal{F}_t)
$$

This process represents the conditional probability of survival given market information. Key properties:

1. $G_t$ is a **supermartingale** (survival probability cannot increase on average)
2. $G_0 = \mathbb{P}(\tau > 0)$ (typically 1 if default cannot occur instantly)
3. $G_t \to G_\infty = \mathbb{P}(\tau = \infty \mid \mathcal{F}_\infty)$ as $t \to \infty$

The Azéma supermartingale admits the **Doob-Meyer decomposition**:

$$
G_t = M_t - A_t
$$

where $M_t$ is a martingale and $A_t$ is a predictable increasing process.

---

## Pre-Default and Post-Default Dynamics

The enlarged filtration naturally separates into pre-default and post-default regimes. For any $\mathcal{G}$-adapted process $X_t$:

$$
X_t = X_t^{\text{pre}} \mathbf{1}_{\{\tau > t\}} + X_t^{\text{post}} \mathbf{1}_{\{\tau \le t\}}
$$

**Pre-default:** On $\{\tau > t\}$, the relevant information is $\mathcal{F}_t$ (market factors only).

**Post-default:** On $\{\tau \le t\}$, we additionally know the exact default time $\tau$.

This decomposition is crucial for pricing defaultable claims, where cashflows differ fundamentally before and after default.

---

## Financial Interpretation

Enlargement of filtration formalizes several key aspects of credit modeling:

1. **Information arrival:** Default news arrives at a random time, enriching the information set
2. **Observability:** Market participants observe default when it occurs (stopping time property)
3. **Pricing consistency:** Arbitrage-free pricing must account for the expanded information
4. **Hedging constraints:** Hedging strategies must be adapted to $(\mathcal{G}_t)$, not just $(\mathcal{F}_t)$

The mathematical framework ensures that pricing and hedging are internally consistent with the observed default events.

---

## Connection to Cox Process Construction

In reduced-form models, default is often constructed via a **doubly-stochastic** (Cox) process. Given an $\mathcal{F}$-adapted intensity process $\lambda_t \ge 0$, define

$$
\Lambda_t := \int_0^t \lambda_s \, ds
$$

and let $E \sim \text{Exp}(1)$ be independent of $\mathcal{F}_\infty$. The default time is

$$
\tau := \inf\{t \ge 0 : \Lambda_t \ge E\} = \Lambda^{-1}(E)
$$

Under this construction:
- $\tau$ is a totally inaccessible stopping time in $(\mathcal{G}_t)$
- The conditional survival probability is $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t) = e^{-\Lambda_t}$
- The Azéma supermartingale has an explicit form

This construction is the workhorse of intensity-based credit models.

---

## Key Takeaways

- Default is modeled as a random time $\tau$, which must be a stopping time for observability
- Filtration enlargement formally incorporates default information into the probability space
- The Azéma supermartingale $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t)$ is central to the theory
- Pre-default and post-default dynamics are naturally separated
- The Cox process construction provides a canonical way to generate default times

---

## Further Reading

- Jeanblanc, M., Yor, M., & Chesney, M. (2009). *Mathematical Methods for Financial Markets*. Springer.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer.
- Protter, P. (2005). *Stochastic Integration and Differential Equations*. Springer.
- Jeulin, T. (1980). *Semi-martingales et grossissement d'une filtration*. Lecture Notes in Mathematics 833.

---

## Exercises

**Exercise 1.** Let $\tau$ be a stopping time with respect to $(\mathcal{G}_t)$ and let $H_t = \mathbf{1}_{\{\tau \le t\}}$. Prove that $H_t$ is a submartingale. Compute $\mathbb{E}[H_t]$ when $\tau \sim \text{Exp}(\lambda)$.

??? success "Solution to Exercise 1"
    **Part 1: $H_t$ is a submartingale.**

    We must show that for $s \le t$, $\mathbb{E}[H_t \mid \mathcal{G}_s] \ge H_s$.

    Since $H_t = \mathbf{1}_{\{\tau \le t\}}$ and $H_s = \mathbf{1}_{\{\tau \le s\}}$, and $s \le t$ implies $\{\tau \le s\} \subseteq \{\tau \le t\}$, we have $H_t \ge H_s$ pointwise (both are 0 or 1, and $H_t = 1$ whenever $H_s = 1$).

    Therefore:

    $$
    \mathbb{E}[H_t \mid \mathcal{G}_s] \ge \mathbb{E}[H_s \mid \mathcal{G}_s] = H_s
    $$

    where the inequality follows from $H_t \ge H_s$ a.s. and the monotonicity of conditional expectation, and the equality follows from $H_s$ being $\mathcal{G}_s$-measurable.

    Additionally, $\mathbb{E}[H_t] = \mathbb{P}(\tau \le t) < \infty$, so $H_t$ is integrable for all $t$. Thus $H_t$ is a submartingale. $\blacksquare$

    **Part 2: Compute $\mathbb{E}[H_t]$ when $\tau \sim \text{Exp}(\lambda)$.**

    When $\tau \sim \text{Exp}(\lambda)$, the cumulative distribution function is $\mathbb{P}(\tau \le t) = 1 - e^{-\lambda t}$ for $t \ge 0$. Therefore:

    $$
    \mathbb{E}[H_t] = \mathbb{E}[\mathbf{1}_{\{\tau \le t\}}] = \mathbb{P}(\tau \le t) = 1 - e^{-\lambda t}
    $$

    For example, with $\lambda = 0.02$ (2% annual intensity):

    - $\mathbb{E}[H_1] = 1 - e^{-0.02} \approx 0.0198$ (about 2% default probability by year 1)
    - $\mathbb{E}[H_5] = 1 - e^{-0.10} \approx 0.0952$ (about 9.5% by year 5)
    - $\mathbb{E}[H_{10}] = 1 - e^{-0.20} \approx 0.1813$ (about 18.1% by year 10)

---

**Exercise 2.** Consider the Cox process construction with constant intensity $\lambda = 2\%$ and $E \sim \text{Exp}(1)$ independent of $\mathcal{F}_\infty$. Compute the Azema supermartingale $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t)$ and verify that it equals $e^{-\lambda t}$. What is $G_5$ and what is its interpretation?

??? success "Solution to Exercise 2"
    Under the Cox process construction with constant intensity $\lambda = 2\% = 0.02$, the cumulative intensity is:

    $$
    \Lambda_t = \int_0^t \lambda \, ds = \lambda t = 0.02t
    $$

    The default time is $\tau = \inf\{t \ge 0 : \Lambda_t \ge E\} = \inf\{t \ge 0 : \lambda t \ge E\} = E / \lambda$, where $E \sim \text{Exp}(1)$ is independent of $\mathcal{F}_\infty$.

    **Computing the Azema supermartingale:**

    Since $E$ is independent of $\mathcal{F}_\infty$ (and hence of $\mathcal{F}_t$), and $\Lambda_t = \lambda t$ is deterministic (hence $\mathcal{F}_t$-measurable):

    $$
    G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t) = \mathbb{P}(\Lambda_t < E \mid \mathcal{F}_t) = \mathbb{P}(E > \lambda t \mid \mathcal{F}_t)
    $$

    Since $E \sim \text{Exp}(1)$ with survival function $\mathbb{P}(E > x) = e^{-x}$ for $x \ge 0$, and $E$ is independent of $\mathcal{F}_t$:

    $$
    G_t = \mathbb{P}(E > \lambda t) = e^{-\lambda t} = e^{-0.02t}
    $$

    This confirms $G_t = e^{-\lambda t}$.

    **Computing $G_5$:**

    $$
    G_5 = e^{-0.02 \times 5} = e^{-0.10} \approx 0.9048
    $$

    **Interpretation:** $G_5 \approx 0.9048$ means that, given all market information available at time $t = 5$, the conditional probability that the entity has survived beyond year 5 is approximately 90.48%. Equivalently, the cumulative default probability over 5 years is approximately $1 - 0.9048 = 9.52\%$. In this constant-intensity case, $G_t$ is deterministic, so market information plays no role — the survival probability is the same regardless of the market state.

---

**Exercise 3.** Explain the difference between a predictable stopping time and a totally inaccessible stopping time. Give an example of each in the context of credit risk models: (a) a predictable default time arising from a structural model, and (b) a totally inaccessible default time arising from a reduced-form model.

??? success "Solution to Exercise 3"
    **Predictable stopping time:** A stopping time $\tau$ is **predictable** if there exists an increasing sequence of stopping times $(\tau_n)_{n \ge 1}$ (called an announcing sequence) such that $\tau_n < \tau$ on $\{\tau > 0\}$ and $\tau_n \uparrow \tau$ a.s. Intuitively, predictable stopping times can be "foreseen" — information accumulates gradually, signaling that the event is approaching.

    **Totally inaccessible stopping time:** A stopping time $\tau$ is **totally inaccessible** if $\mathbb{P}(\tau = S < \infty) = 0$ for every predictable stopping time $S$. Intuitively, totally inaccessible stopping times come as a complete surprise — they cannot be anticipated by any sequence of events.

    Every stopping time can be uniquely decomposed into a predictable part and a totally inaccessible part.

    **(a) Predictable default time from a structural model:**

    Consider the Merton structural model where the firm value $V_t$ follows a geometric Brownian motion:

    $$
    dV_t = \mu V_t \, dt + \sigma V_t \, dW_t
    $$

    and default occurs when $V_t$ hits a lower barrier $B$ for the first time: $\tau = \inf\{t \ge 0 : V_t \le B\}$.

    Since $V_t$ is a continuous process, when $V_t$ approaches $B$ from above, the process must pass through every intermediate value before hitting $B$. Define $\tau_n = \inf\{t \ge 0 : V_t \le B + 1/n\}$. Then $\tau_n < \tau$ on $\{\tau > 0\}$ (since $V$ must enter each neighborhood $B + 1/n$ before hitting $B$), and $\tau_n \uparrow \tau$. This provides the announcing sequence, making $\tau$ predictable. Economically, as the firm value declines toward the default barrier, credit spreads widen progressively, signaling imminent default.

    **(b) Totally inaccessible default time from a reduced-form model:**

    Consider the Cox process construction where $\tau = \inf\{t : \int_0^t \lambda_s \, ds \ge E\}$ with $E \sim \text{Exp}(1)$ independent of $\mathcal{F}_\infty$. The default time $\tau$ is totally inaccessible as a $\mathcal{G}_t$-stopping time.

    The key reason is the independence of $E$ from all market information. Even though the cumulative intensity $\Lambda_t$ is continuous and predictable, the threshold $E$ is unknown and independent. Default occurs at the random instant when $\Lambda_t$ crosses $E$, which cannot be anticipated. For any predictable stopping time $S$, we have $\mathbb{P}(\tau = S) = \mathbb{P}(\Lambda_S = E) = 0$ because $E$ has a continuous distribution and $\Lambda_S$ is $\mathcal{F}_S$-measurable (hence independent of $E$). Economically, this models sudden, unexpected defaults — default arrives as a surprise even though the credit quality may be deteriorating.

---

**Exercise 4.** The minimal enlargement of filtration is $\mathcal{G}_t = \mathcal{F}_t \vee \mathcal{H}_t$, where $\mathcal{H}_t = \sigma(H_s : s \le t)$. Show that every $\mathcal{G}_t$-measurable random variable can be written as $X = X_0\,\mathbf{1}_{\{\tau > t\}} + X_1(\tau)\,\mathbf{1}_{\{\tau \le t\}}$. Explain why $X_0$ must be $\mathcal{F}_t$-measurable and why $X_1$ may depend on the realized value of $\tau$.

??? success "Solution to Exercise 4"
    **Showing the representation:** Let $X$ be $\mathcal{G}_t$-measurable where $\mathcal{G}_t = \mathcal{F}_t \vee \mathcal{H}_t$.

    The sigma-algebra $\mathcal{H}_t = \sigma(H_s : s \le t)$ encodes two types of information: (i) whether $\tau \le t$ or $\tau > t$, and (ii) if $\tau \le t$, the exact value of $\tau$ (since knowing $H_s = \mathbf{1}_{\{\tau \le s\}}$ for all $s \le t$ determines $\tau = \inf\{s : H_s = 1\}$).

    The sample space $\Omega$ decomposes into the disjoint events $\{\tau > t\}$ and $\{\tau \le t\}$. On each piece, we analyze what $\mathcal{G}_t$-measurability implies.

    **On $\{\tau > t\}$:** Here $H_s = 0$ for all $s \le t$, so $\mathcal{H}_t$ provides no additional information beyond $\{\tau > t\}$ itself. Any $\mathcal{G}_t$-measurable random variable restricted to this event depends only on $\mathcal{F}_t$. Therefore $X \cdot \mathbf{1}_{\{\tau > t\}} = X_0 \cdot \mathbf{1}_{\{\tau > t\}}$ where $X_0$ is $\mathcal{F}_t$-measurable.

    **Why $X_0$ must be $\mathcal{F}_t$-measurable:** On $\{\tau > t\}$, no default has occurred, so the only information available comes from the market filtration $\mathcal{F}_t$. The default indicator $H_s = 0$ for all $s \le t$ provides no additional information beyond confirming survival, which is already an $\mathcal{F}_t$-augmented event. Hence the pre-default value $X_0$ can depend only on market information, making it $\mathcal{F}_t$-measurable.

    **On $\{\tau \le t\}$:** Default has occurred at some time $\tau \in [0, t]$. The sigma-algebra $\mathcal{H}_t$ reveals the exact value of $\tau$ (from the jump time of $H$). Therefore $X$ restricted to this event can depend on both $\mathcal{F}_t$ and the realized value of $\tau$. We write $X \cdot \mathbf{1}_{\{\tau \le t\}} = X_1(\tau) \cdot \mathbf{1}_{\{\tau \le t\}}$.

    **Why $X_1$ may depend on $\tau$:** Once default has occurred, the exact default time $\tau$ is observed (it is $\mathcal{H}_t$-measurable). This additional piece of information — precisely when default happened — is not contained in $\mathcal{F}_t$ alone. For instance, the recovery value of a defaultable bond may depend on the time of default (through the prevailing market conditions at $\tau$), so $X_1$ naturally depends on $\tau$. Formally, $X_1(s)$ must be jointly measurable in $(s, \omega)$ with respect to $\mathcal{B}([0,t]) \otimes \mathcal{F}_t$, meaning it can depend on the default time $s = \tau$ and on market information $\omega$ through $\mathcal{F}_t$.

    Combining both pieces:

    $$
    X = X_0 \, \mathbf{1}_{\{\tau > t\}} + X_1(\tau) \, \mathbf{1}_{\{\tau \le t\}}
    $$

    which is the claimed representation. $\blacksquare$

---

**Exercise 5.** For a defaultable zero-coupon bond with face value 1, recovery $R$ at default, constant risk-free rate $r$, and constant intensity $\lambda$, write the price $V_t$ as a $\mathcal{G}_t$-adapted process using the pre-default/post-default decomposition:

$$
V_t = V_t^{\text{pre}}\,\mathbf{1}_{\{\tau > t\}} + V_t^{\text{post}}\,\mathbf{1}_{\{\tau \le t\}}
$$

Derive explicit expressions for $V_t^{\text{pre}}$ and $V_t^{\text{post}}$.

??? success "Solution to Exercise 5"
    We price a defaultable zero-coupon bond with face value 1, recovery $R$ paid at default, constant risk-free rate $r$, and constant intensity $\lambda$, using the pre-default/post-default decomposition.

    **Pre-default value $V_t^{\text{pre}}$ (on $\{\tau > t\}$):**

    If no default has occurred by time $t$, the bond still promises to pay 1 at maturity $T$ (if no default before $T$) or recovery $R$ at the time of default (if default occurs between $t$ and $T$). The pre-default price is:

    $$
    V_t^{\text{pre}} = \mathbb{E}\left[e^{-r(T-t)} \mathbf{1}_{\{\tau > T\}} + R \, e^{-r(\tau - t)} \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t, \tau > t \right]
    $$

    Under constant intensity $\lambda$, the conditional survival and default densities (given $\tau > t$) are:

    - $\mathbb{P}(\tau > T \mid \tau > t) = e^{-\lambda(T-t)}$
    - $\mathbb{P}(\tau \in ds \mid \tau > t) = \lambda e^{-\lambda(s-t)} ds$ for $s > t$

    **Survival component:**

    $$
    e^{-r(T-t)} \cdot e^{-\lambda(T-t)} = e^{-(r+\lambda)(T-t)}
    $$

    **Recovery component:**

    $$
    \int_t^T R \, e^{-r(s-t)} \lambda e^{-\lambda(s-t)} \, ds = R\lambda \int_t^T e^{-(r+\lambda)(s-t)} \, ds
    $$

    $$
    = R\lambda \left[\frac{-1}{r+\lambda} e^{-(r+\lambda)(s-t)}\right]_t^T = \frac{R\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)(T-t)}\right)
    $$

    Combining:

    $$
    V_t^{\text{pre}} = e^{-(r+\lambda)(T-t)} + \frac{R\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)(T-t)}\right)
    $$

    This can be rewritten as:

    $$
    V_t^{\text{pre}} = \frac{R\lambda}{r+\lambda} + \left(1 - \frac{R\lambda}{r+\lambda}\right)e^{-(r+\lambda)(T-t)}
    $$

    **Post-default value $V_t^{\text{post}}$ (on $\{\tau \le t\}$):**

    If default has already occurred by time $t$, the recovery $R$ has already been paid at time $\tau \le t$. The bond has no remaining cashflows (the recovery was a one-time payment at default). Therefore:

    $$
    V_t^{\text{post}} = 0
    $$

    (The recovery $R$ was received at time $\tau$ and is no longer reflected in the bond's value at time $t > \tau$.)

    **Full decomposition:**

    $$
    V_t = V_t^{\text{pre}} \, \mathbf{1}_{\{\tau > t\}} + V_t^{\text{post}} \, \mathbf{1}_{\{\tau \le t\}}
    $$

    $$
    = \left[e^{-(r+\lambda)(T-t)} + \frac{R\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)(T-t)}\right)\right] \mathbf{1}_{\{\tau > t\}}
    $$

    **Special cases:**

    - If $R = 0$ (zero recovery): $V_t = e^{-(r+\lambda)(T-t)} \, \mathbf{1}_{\{\tau > t\}}$
    - If $R = 1$ (full recovery): $V_t = e^{-r(T-t)} \, \mathbf{1}_{\{\tau > t\}}$ (reduces to default-free bond on survival)

---

**Exercise 6.** Under the Cox process construction, explain why $\tau$ is totally inaccessible as a $\mathcal{G}_t$-stopping time, even though the cumulative intensity $\Lambda_t = \int_0^t \lambda_s\,ds$ is $\mathcal{F}_t$-predictable. Why does knowing $\Lambda_t$ not allow prediction of $\tau$?

??? success "Solution to Exercise 6"
    Under the Cox process construction, $\tau = \inf\{t \ge 0 : \Lambda_t \ge E\}$ where $\Lambda_t = \int_0^t \lambda_s \, ds$ is $\mathcal{F}_t$-adapted and $E \sim \text{Exp}(1)$ is independent of $\mathcal{F}_\infty$.

    **Why $\tau$ is totally inaccessible despite $\Lambda_t$ being predictable:**

    A stopping time $\tau$ is totally inaccessible if $\mathbb{P}(\tau = S < \infty) = 0$ for every $\mathcal{G}_t$-predictable stopping time $S$. We verify this:

    **Step 1: The threshold $E$ is unobservable.** Although $\Lambda_t$ is continuous and $\mathcal{F}_t$-predictable, the level $E$ at which $\Lambda_t$ triggers default is a random variable independent of all market information $\mathcal{F}_\infty$. Before default, the value of $E$ is completely unknown — observing market factors tells us nothing about $E$.

    **Step 2: Default occurs at a random crossing.** Default occurs when $\Lambda_t$ first crosses the random level $E$. Since $\Lambda_t$ is continuous and increasing (assuming $\lambda_t > 0$), the default time satisfies $\Lambda_\tau = E$. The time $\tau$ is determined by the equation $\Lambda_t = E$, where the left side is $\mathcal{F}$-adapted and the right side is independent of $\mathcal{F}_\infty$.

    **Step 3: No announcing sequence exists.** Suppose, for contradiction, that $(\tau_n)$ is an announcing sequence with $\tau_n < \tau$ and $\tau_n \uparrow \tau$. Each $\tau_n$ is a $\mathcal{G}$-predictable stopping time. The values $\Lambda_{\tau_n}$ are $\mathcal{G}_{\tau_n}$-measurable. Since $\tau_n < \tau$, we have $\Lambda_{\tau_n} < E$. As $\tau_n \uparrow \tau$ and $\Lambda$ is continuous, $\Lambda_{\tau_n} \uparrow \Lambda_\tau = E$. This would mean $E$ is $\mathcal{G}_{\tau-}$-measurable and hence anticipatable. But on $\{\tau > t\}$ for $t < \tau$, the $\mathcal{G}_t$-information only tells us that $E > \Lambda_t$, not the exact value of $E$. The information that $E \in (\Lambda_t, \infty)$ does not converge to a point because knowing the exact crossing time would require resolving the independent randomness of $E$.

    **Step 4: Formal verification.** For any $\mathcal{G}$-predictable stopping time $S$:

    $$
    \mathbb{P}(\tau = S < \infty) = \mathbb{P}(\Lambda_S = E, S < \infty)
    $$

    Since $\Lambda_S$ is $\mathcal{F}_S$-measurable (hence determined by market information) and $E$ is independent of $\mathcal{F}_\infty$ with a continuous (exponential) distribution:

    $$
    \mathbb{P}(\Lambda_S = E \mid \mathcal{F}_\infty) = \mathbb{P}(E = \Lambda_S \mid \mathcal{F}_\infty) = 0
    $$

    because $E$ has no atoms (continuous distribution). Therefore $\mathbb{P}(\tau = S < \infty) = 0$.

    **Why knowing $\Lambda_t$ does not allow prediction of $\tau$:**

    Knowing $\Lambda_t$ at time $t$ tells us the cumulative hazard up to time $t$. On $\{\tau > t\}$, we know that $E > \Lambda_t$. But the conditional distribution of $E$ given $E > \Lambda_t$ is $\text{Exp}(1)$ shifted by $\Lambda_t$ (by the memoryless property: $E - \Lambda_t \mid E > \Lambda_t \sim \text{Exp}(1)$). The remaining "distance to default" $E - \Lambda_t$ is still exponentially distributed with no memory of the past, making it impossible to predict exactly when $\Lambda_t$ will reach $E$. The predictability of the path $\Lambda_t$ is irrelevant because the target level $E$ remains random and independent. This is the fundamental mechanism by which reduced-form models produce surprise defaults.
