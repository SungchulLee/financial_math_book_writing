# Drift Adjustment and Financial Meaning


Girsanov’s theorem is used in finance to remove risk premia from asset prices,
making arbitrage-free pricing possible.

---

## Asset Price Dynamics

Under the physical measure $\mathbb{P}$, assume the stock price follows geometric Brownian motion:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

where $\mu$ is the real-world expected return and $\sigma > 0$ is the volatility.

For derivative pricing we need the **discounted** stock price $\widetilde{S}_t := e^{-rt}S_t$ to be a martingale. By Itô's lemma:

$$
d\widetilde{S}_t = d(e^{-rt}S_t) = -r e^{-rt}S_t\,dt + e^{-rt}dS_t
= e^{-rt}S_t\bigl[(\mu - r)\,dt + \sigma\,dW_t^{\mathbb{P}}\bigr]
$$

The $dt$ coefficient is $(\mu - r)S_te^{-rt}$, which is non-zero whenever $\mu \neq r$. Discounting alone does not eliminate the drift — we need a change of measure to remove it.

---

## Market Price of Risk

To eliminate the residual drift $(\mu - r)$ we need to shift the Brownian motion by exactly the right amount. Define the **market price of risk**:

$$
\theta := \frac{\mu - r}{\sigma}
$$

This has a concrete financial interpretation: it is the **excess return per unit of volatility**, i.e. how many units of risk premium the investor earns for each unit of volatility exposure. It is also called the **Sharpe ratio** of the asset.

The sign of $\theta$ encodes the direction of the adjustment:

- If $\mu > r$: the asset earns a positive risk premium, so $\theta > 0$. The measure change will shift probability mass toward lower paths (removing the upward drift).
- If $\mu < r$: $\theta < 0$, and the adjustment goes the other way.
- If $\mu = r$: $\theta = 0$, no measure change is needed, and $\widetilde{S}_t$ is already a martingale.

The factor of $\sigma$ in the denominator appears because the Brownian motion enters the dynamics with coefficient $\sigma$ — a unit shift in $W_t$ produces a $\sigma$-sized move in $S_t$, so we need to shift $W_t$ by $\theta = (\mu-r)/\sigma$ to cancel a drift of size $(\mu-r)$.

---

## Measure Change

Define the **Radon-Nikodym density process**:

$$
Z_t = \exp\!\left(-\theta W_t^{\mathbb{P}} - \frac{1}{2}\theta^2 t\right), \qquad \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T
$$

By Girsanov's theorem, under $\mathbb{Q}$ the process

$$
W_t^{\mathbb{Q}} := W_t^{\mathbb{P}} + \theta t
$$

is a standard Brownian motion. Equivalently, $W_t^{\mathbb{P}} = W_t^{\mathbb{Q}} - \theta t$.

**Why this specific $Z_t$?** The exponential form arises from Itô's lemma: applying it to $e^{X_t}$ with $X_t = -\theta W_t^{\mathbb{P}} - \frac{1}{2}\theta^2 t$ gives $dZ_t = -\theta Z_t\,dW_t^{\mathbb{P}}$, which has no $dt$ term, guaranteeing $Z_t$ is a $\mathbb{P}$-martingale with $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$ so that $\mathbb{Q}$ is a valid probability measure.

**How the reweighting works:** Paths where $W_T^{\mathbb{P}}$ is large and positive make $Z_T = e^{-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T}$ small (for $\theta > 0$), downweighting the high-return paths. Paths where $W_T^{\mathbb{P}}$ is negative get upweighted. The net effect is that the average drift is shifted from $\mu$ down to $r$.

---

## Risk-Neutral Dynamics

We now substitute $W_t^{\mathbb{P}} = W_t^{\mathbb{Q}} - \theta t$ into the original SDE:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
= \mu S_t\,dt + \sigma S_t\left(dW_t^{\mathbb{Q}} - \theta\,dt\right)
$$

$$
= \mu S_t\,dt - \sigma\theta S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
= (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

Substituting $\theta = (\mu - r)/\sigma$, so $\sigma\theta = \mu - r$:

$$
\boxed{dS_t = r S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}}
$$

The drift has shifted from $\mu$ to $r$. To confirm that $\widetilde{S}_t = e^{-rt}S_t$ is now a $\mathbb{Q}$-martingale, apply Itô's lemma:

$$
d\widetilde{S}_t = e^{-rt}S_t\bigl[(r - r)\,dt + \sigma\,dW_t^{\mathbb{Q}}\bigr] = \sigma\widetilde{S}_t\,dW_t^{\mathbb{Q}}
$$

There is no $dt$ term, confirming that $\widetilde{S}_t$ is a $\mathbb{Q}$-martingale. The option pricing formula follows immediately:

$$
V_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}\bigl[\Phi(S_T)\,\big|\,\mathcal{F}_t\bigr]
$$

where $\Phi$ is the payoff function. This is the **risk-neutral pricing formula**, and it holds for any derivative whose payoff depends on $S_T$.

---

## Interpretation

**Expected returns are adjusted to the risk-free rate.** Under $\mathbb{P}$, a risky asset earns $\mu > r$ to compensate investors for bearing risk. Under $\mathbb{Q}$, every asset grows at $r$ regardless of its risk. This does not mean we believe the stock actually grows at $r$ — it means we have reweighted the probability space so that the pricing formula $V = e^{-rT}\mathbb{E}^{\mathbb{Q}}[\Phi]$ is internally consistent and arbitrage-free. The real-world drift $\mu$ drops out entirely, which is why option prices do not depend on investors' return expectations.

**Volatility is unchanged.** The Girsanov shift only moves the drift; the diffusion coefficient $\sigma$ multiplies $dW_t$ in both the $\mathbb{P}$ and $\mathbb{Q}$ dynamics. This is because quadratic variation — which determines $\sigma$ — is a pathwise property of the sample paths, independent of which measure is used to weight them. The paths themselves are identical under $\mathbb{P}$ and $\mathbb{Q}$; only their probabilities differ.

**Sample paths are identical; probabilities are reweighted.** Both $\mathbb{P}$ and $\mathbb{Q}$ are defined on the same probability space and generate the same set of possible paths. What changes is how much weight each path receives. Specifically, for $\theta > 0$ (i.e. $\mu > r$), paths that drifted strongly upward under $\mathbb{P}$ (large positive $W_T^{\mathbb{P}}$) are downweighted by $Z_T = e^{-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T}$, while paths that drifted downward are upweighted. The net effect is that the average drift seen under $\mathbb{Q}$ equals $r$ rather than $\mu$.

This drift adjustment is the mathematical foundation of risk-neutral pricing: it converts the no-arbitrage condition (the discounted price is a martingale) into a concrete computational tool.

---

## Exercises

**Exercise 1.**
A stock follows $dS_t = 0.08\,S_t\,dt + 0.30\,S_t\,dW_t^{\mathbb{P}}$ with risk-free rate $r = 0.02$. Compute the market price of risk $\theta$, write the density process $Z_t$, and derive the risk-neutral dynamics of $S_t$.

---

**Exercise 2.**
Starting from the physical dynamics $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$ and the definition $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$, show step by step that the discounted price process $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale. In particular, verify that the $dt$ term vanishes after substitution.

---

**Exercise 3.**
Consider an asset with physical drift $\mu = 0.05$ and volatility $\sigma = 0.40$ in a market with $r = 0.03$. A second asset has $\mu' = 0.10$ and $\sigma' = 0.40$. Both assets are driven by the same Brownian motion. Compute $\theta$ for each asset. Are the two values consistent? What does this tell you about arbitrage in this market?

---

**Exercise 4.**
Explain why the volatility $\sigma$ is unchanged under the Girsanov measure change, while the drift changes from $\mu$ to $r$. Relate your answer to the fact that quadratic variation is a pathwise quantity.

---

**Exercise 5.**
Under $\mathbb{P}$, a zero-coupon bond price satisfies $dP(t,T) = \mu_P P(t,T)\,dt + \sigma_P P(t,T)\,dW_t^{\mathbb{P}}$. Apply the Girsanov drift adjustment to derive the dynamics under $\mathbb{Q}$ and show that the discounted bond price $e^{-\int_0^t r_s\,ds}P(t,T)$ is a $\mathbb{Q}$-martingale.

---

**Exercise 6.**
Suppose $\theta$ is not constant but depends on the current stock price: $\theta_t = (\mu(S_t) - r) / \sigma(S_t)$. Write the Radon-Nikodym derivative $Z_T$ in integral form and state the Novikov condition that must hold. Explain why this condition may fail for certain choices of $\mu(\cdot)$ and $\sigma(\cdot)$.

---

**Exercise 7.**
For the density process $Z_t = \exp(-\theta W_t^{\mathbb{P}} - \frac{1}{2}\theta^2 t)$ with constant $\theta = 0.3$ and $T = 2$, compute $\mathbb{E}^{\mathbb{P}}[Z_T]$ and verify it equals 1. Then compute $Z_T$ for a specific path where $W_T^{\mathbb{P}} = 1.5$ and interpret the result: is this path upweighted or downweighted under $\mathbb{Q}$?

---

## Solutions

??? success "Solution to Exercise 1"
    Given $dS_t = 0.08\,S_t\,dt + 0.30\,S_t\,dW_t^{\mathbb{P}}$ with $r = 0.02$, the parameters are $\mu = 0.08$, $\sigma = 0.30$.

    **Market price of risk:**

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.08 - 0.02}{0.30} = \frac{0.06}{0.30} = 0.2
    $$

    **Density process:**

    $$
    Z_t = \exp\!\left(-0.2\,W_t^{\mathbb{P}} - \frac{1}{2}(0.2)^2 t\right) = \exp\!\left(-0.2\,W_t^{\mathbb{P}} - 0.02\,t\right)
    $$

    **Risk-neutral dynamics:** Define $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + 0.2\,t$, so $W_t^{\mathbb{P}} = W_t^{\mathbb{Q}} - 0.2\,t$. Substituting:

    $$
    dS_t = 0.08\,S_t\,dt + 0.30\,S_t\left(dW_t^{\mathbb{Q}} - 0.2\,dt\right)
    $$

    $$
    = 0.08\,S_t\,dt + 0.30\,S_t\,dW_t^{\mathbb{Q}} - 0.06\,S_t\,dt
    $$

    $$
    = 0.02\,S_t\,dt + 0.30\,S_t\,dW_t^{\mathbb{Q}}
    $$

    Under $\mathbb{Q}$: $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}} = 0.02\,S_t\,dt + 0.30\,S_t\,dW_t^{\mathbb{Q}}$. The drift has changed from $\mu = 0.08$ to $r = 0.02$ while volatility remains $\sigma = 0.30$.

??? success "Solution to Exercise 2"
    Start with $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$ and $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$ where $\theta = (\mu - r)/\sigma$.

    **Step 1:** Substitute $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta\,dt$ into the SDE:

    $$
    dS_t = \mu S_t\,dt + \sigma S_t(dW_t^{\mathbb{Q}} - \theta\,dt) = (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    **Step 2:** Since $\sigma\theta = \sigma \cdot \frac{\mu - r}{\sigma} = \mu - r$:

    $$
    dS_t = (\mu - (\mu - r))S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}} = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    **Step 3:** Apply Itô's lemma to $\widetilde{S}_t = e^{-rt}S_t$:

    $$
    d\widetilde{S}_t = -re^{-rt}S_t\,dt + e^{-rt}\,dS_t
    $$

    $$
    = -re^{-rt}S_t\,dt + e^{-rt}\bigl(rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}\bigr)
    $$

    $$
    = e^{-rt}S_t(-r + r)\,dt + \sigma e^{-rt}S_t\,dW_t^{\mathbb{Q}}
    $$

    $$
    = \sigma\widetilde{S}_t\,dW_t^{\mathbb{Q}}
    $$

    **Step 4:** The $dt$ term is zero. Since $d\widetilde{S}_t = \sigma\widetilde{S}_t\,dW_t^{\mathbb{Q}}$ contains only a $dW_t^{\mathbb{Q}}$ term and no drift, $\widetilde{S}_t = e^{-rt}S_t$ is a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 3"
    For the first asset: $\mu = 0.05$, $\sigma = 0.40$, $r = 0.03$:

    $$
    \theta_1 = \frac{\mu - r}{\sigma} = \frac{0.05 - 0.03}{0.40} = \frac{0.02}{0.40} = 0.05
    $$

    For the second asset: $\mu' = 0.10$, $\sigma' = 0.40$, $r = 0.03$:

    $$
    \theta_2 = \frac{\mu' - r}{\sigma'} = \frac{0.10 - 0.03}{0.40} = \frac{0.07}{0.40} = 0.175
    $$

    The two values are **not consistent**: $\theta_1 = 0.05 \neq 0.175 = \theta_2$.

    Since both assets are driven by the **same** Brownian motion $W_t$, a single Girsanov change of measure can only shift $W_t$ by one value of $\theta$. If we use $\theta_1 = 0.05$, then the first asset's discounted price is a martingale under $\mathbb{Q}$, but the second asset's drift under $\mathbb{Q}$ would be $\mu' - \sigma'\theta_1 = 0.10 - 0.40 \times 0.05 = 0.08 \neq r = 0.03$. The second asset's discounted price would not be a martingale.

    This means **there is no single equivalent martingale measure** under which both discounted prices are martingales. By the fundamental theorem of asset pricing, this implies the market admits **arbitrage**. One could construct an arbitrage by going long the high-Sharpe-ratio asset and short the low-Sharpe-ratio asset, since they share the same risk factor but offer different compensation per unit of risk.

??? success "Solution to Exercise 4"
    The drift changes from $\mu$ to $r$ because it depends on how probabilities are assigned to paths. The Girsanov measure change reweights the probability of each path via the Radon-Nikodym derivative $Z_T$, which shifts the expected value of $dW_t$ from $0$ (under $\mathbb{P}$) to $-\theta\,dt$ (effectively, by making $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$ a $\mathbb{Q}$-Brownian motion). This reweighting changes the first moment (mean/drift) of the process.

    The volatility $\sigma$, however, is determined by the **quadratic variation**, which is a **pathwise** quantity. Quadratic variation is computed as:

    $$
    \langle S \rangle_t = \lim_{n \to \infty} \sum_{k} (S_{t_{k+1}} - S_{t_k})^2
    $$

    This limit depends only on the individual sample paths, not on how those paths are weighted by the probability measure. Since $\mathbb{P}$ and $\mathbb{Q}$ are defined on the same sample space with the same set of paths (they are equivalent measures), the quadratic variation is identical under both measures.

    Formally, in the SDE $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$, the Girsanov substitution replaces $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta\,dt$, which only modifies the $dt$ coefficient (the drift). The coefficient of $dW_t^{\mathbb{Q}}$ remains $\sigma S_t$, leaving volatility unchanged.

??? success "Solution to Exercise 5"
    Under $\mathbb{P}$, the zero-coupon bond dynamics are:

    $$
    dP(t,T) = \mu_P P(t,T)\,dt + \sigma_P P(t,T)\,dW_t^{\mathbb{P}}
    $$

    The market price of risk is $\theta = (\mu_P - r_t)/\sigma_P$, where $r_t$ is the short rate. Define $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$. Substituting $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta_t\,dt$:

    $$
    dP(t,T) = \mu_P P\,dt + \sigma_P P\bigl(dW_t^{\mathbb{Q}} - \theta_t\,dt\bigr)
    $$

    $$
    = (\mu_P - \sigma_P\theta_t)P\,dt + \sigma_P P\,dW_t^{\mathbb{Q}}
    $$

    Since $\sigma_P\theta_t = \sigma_P \cdot \frac{\mu_P - r_t}{\sigma_P} = \mu_P - r_t$:

    $$
    dP(t,T) = r_t P(t,T)\,dt + \sigma_P P(t,T)\,dW_t^{\mathbb{Q}}
    $$

    Now consider the discounted bond price $\widetilde{P}(t,T) = e^{-\int_0^t r_s\,ds}P(t,T)$. By the product rule:

    $$
    d\widetilde{P} = -r_t e^{-\int_0^t r_s\,ds}P\,dt + e^{-\int_0^t r_s\,ds}\,dP
    $$

    $$
    = -r_t\widetilde{P}\,dt + e^{-\int_0^t r_s\,ds}\bigl(r_t P\,dt + \sigma_P P\,dW_t^{\mathbb{Q}}\bigr)
    $$

    $$
    = -r_t\widetilde{P}\,dt + r_t\widetilde{P}\,dt + \sigma_P\widetilde{P}\,dW_t^{\mathbb{Q}}
    $$

    $$
    = \sigma_P\widetilde{P}\,dW_t^{\mathbb{Q}}
    $$

    The $dt$ term vanishes, confirming that $e^{-\int_0^t r_s\,ds}P(t,T)$ is a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 6"
    When $\theta_t = (\mu(S_t) - r)/\sigma(S_t)$ depends on the stock price, the Radon-Nikodym derivative in integral form is:

    $$
    Z_T = \exp\!\left(-\int_0^T \theta_t\,dW_t^{\mathbb{P}} - \frac{1}{2}\int_0^T \theta_t^2\,dt\right)
    $$

    $$
    = \exp\!\left(-\int_0^T \frac{\mu(S_t) - r}{\sigma(S_t)}\,dW_t^{\mathbb{P}} - \frac{1}{2}\int_0^T \left(\frac{\mu(S_t) - r}{\sigma(S_t)}\right)^2 dt\right)
    $$

    The **Novikov condition** requires:

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_t^2\,dt\right)\right] = \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \left(\frac{\mu(S_t) - r}{\sigma(S_t)}\right)^2 dt\right)\right] < \infty
    $$

    This condition may fail in several scenarios:

    - If $\sigma(S_t) \to 0$ as $S_t$ approaches some value (e.g., in the CEV model $\sigma(S) = \sigma_0 S^{\beta-1}$ with $\beta < 1$, the volatility vanishes as $S \to 0$), then $\theta_t = (\mu(S_t) - r)/\sigma(S_t) \to \infty$, making the integral $\int_0^T \theta_t^2\,dt$ potentially infinite.
    - If $\mu(S_t)$ grows without bound (e.g., superlinear drift), $\theta_t$ can become unbounded.
    - In stochastic volatility models where $\sigma(S_t)$ can become very small with positive probability, the exponential moment may diverge.

    When Novikov fails, $Z_t$ is only a local martingale, and the measure change may not define a valid probability measure.

??? success "Solution to Exercise 7"
    With $\theta = 0.3$ and $T = 2$:

    $$
    Z_T = \exp\!\left(-0.3\,W_T^{\mathbb{P}} - \frac{1}{2}(0.3)^2 \cdot 2\right) = \exp\!\left(-0.3\,W_T^{\mathbb{P}} - 0.09\right)
    $$

    **Computing $\mathbb{E}^{\mathbb{P}}[Z_T]$:** Since $W_T^{\mathbb{P}} \sim \mathcal{N}(0, T) = \mathcal{N}(0, 2)$ under $\mathbb{P}$, the exponent $-0.3\,W_T^{\mathbb{P}} - 0.09$ is Gaussian with mean $-0.09$ and variance $(0.3)^2 \cdot 2 = 0.18$. Using the lognormal moment formula:

    $$
    \mathbb{E}^{\mathbb{P}}[Z_T] = \exp\!\left(-0.09 + \frac{0.18}{2}\right) = \exp(-0.09 + 0.09) = e^0 = 1 \quad \checkmark
    $$

    **Specific path with $W_T^{\mathbb{P}} = 1.5$:**

    $$
    Z_T = \exp(-0.3 \times 1.5 - 0.09) = \exp(-0.45 - 0.09) = \exp(-0.54) \approx 0.583
    $$

    Since $Z_T \approx 0.583 < 1$, this path is **downweighted** under $\mathbb{Q}$.

    **Interpretation:** The path where $W_T^{\mathbb{P}} = 1.5$ is a path where the Brownian motion drifted upward (1.5 standard deviations above zero at $T = 2$, since $\sqrt{T} = \sqrt{2} \approx 1.41$). Since $\theta > 0$ (meaning $\mu > r$), the Girsanov measure change needs to reduce the apparent upward drift. It does so by assigning lower probability to upward-trending paths and higher probability to downward-trending paths. A path with positive $W_T^{\mathbb{P}}$ gets a weight $Z_T < 1$, meaning it is less likely under $\mathbb{Q}$ than under $\mathbb{P}$. Conversely, a path with $W_T^{\mathbb{P}} = -1.5$ would give $Z_T = \exp(0.45 - 0.09) = e^{0.36} \approx 1.433 > 1$, meaning it would be upweighted.
