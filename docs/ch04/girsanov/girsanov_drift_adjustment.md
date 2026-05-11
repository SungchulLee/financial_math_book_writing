# Drift Adjustment and Financial Meaning


Applying [Girsanov’s theorem](girsanov_theorem.md) to geometric Brownian motion removes risk premia from asset prices, making arbitrage-free pricing possible.

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

The Girsanov kernel for GBM is the [market price of risk](../risk_neutral/market_price_of_risk.md) $\theta = (\mu - r)/\sigma$, representing excess return per unit of volatility. To remove the residual drift $(\mu - r)$ from the discounted stock price, we shift the Brownian motion by $\theta$.

---

## Measure Change

Using the [exponential martingale](girsanov_theorem.md#the-exponential-martingale) $Z_T$ with kernel $\theta = (\mu - r)/\sigma$, define $\mathbb{Q}$ via $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T} = Z_T$. By [Girsanov's theorem](girsanov_theorem.md#statement-of-girsanovs-theorem), the shifted process $W_t^{\mathbb{Q}} := W_t^{\mathbb{P}} + \theta t$ is a standard $\mathbb{Q}$-Brownian motion, so $W_t^{\mathbb{P}} = W_t^{\mathbb{Q}} - \theta t$.

---

## Risk-Neutral Dynamics

We now substitute $W_t^{\mathbb{P}} = W_t^{\mathbb{Q}} - \theta t$ into the original SDE:

$$\begin{array}{lll}
dS_t 
&=&\displaystyle \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}\\
&=&\displaystyle \mu S_t\,dt + \sigma S_t\left(dW_t^{\mathbb{Q}} - \theta\,dt\right)\\
&=&\displaystyle \mu S_t\,dt - \sigma\theta S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}\\
&=&\displaystyle (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
\end{array}$$

Substituting $\theta = (\mu - r)/\sigma$, so $\sigma\theta = \mu - r$:

$$
\boxed{dS_t = r S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}}
$$

The drift has shifted from $\mu$ to $r$. To confirm that $\widetilde{S}_t = e^{-rt}S_t$ is now a $\mathbb{Q}$-martingale, apply Itô's lemma:

$$
d\widetilde{S}_t = e^{-rt}S_t\bigl[(r - r)\,dt + \sigma\,dW_t^{\mathbb{Q}}\bigr] = \sigma\widetilde{S}_t\,dW_t^{\mathbb{Q}}
$$

There is no $dt$ term, confirming that $\widetilde{S}_t$ is a $\mathbb{Q}$-local martingale. In the constant-coefficient GBM setting the integrability check is straightforward, so $\widetilde{S}_t$ is a true $\mathbb{Q}$-martingale. For the pricing formula that follows from this martingale property, see [Risk-Neutral Valuation](../risk_neutral/risk_neutral_valuation_principle.md).

---

## Interpretation

**Expected returns are redefined to equal the risk-free rate.** Under $\mathbb{Q}$, every asset grows at $r$ — a reweighting of the probability space (see [Intuitive Introduction](girsanov_intuition.md)), not a belief about actual returns. The real-world drift $\mu$ drops out of option prices entirely.

**Volatility is unchanged** — quadratic variation is a pathwise property (see [Intuitive Introduction](girsanov_intuition.md)).

**Girsanov transforms a model with drift $\mu$ into a pricing model with drift $r$, enabling arbitrage-free valuation.** This drift adjustment converts the no-arbitrage condition (the discounted price is a martingale) into a concrete computational tool.

---

## Exercises

**Exercise 1.**
A stock follows $dS_t = 0.08\,S_t\,dt + 0.30\,S_t\,dW_t^{\mathbb{P}}$ with risk-free rate $r = 0.02$. Compute the market price of risk $\theta$, write the density process $Z_t$, and derive the risk-neutral dynamics of $S_t$.

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

---

**Exercise 2.**
Starting from the physical dynamics $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$ and the definition $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$, show step by step that the discounted price process $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale. In particular, verify that the $dt$ term vanishes after substitution.

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

---

**Exercise 3.**
Assume a complete market driven by a single Brownian motion. An asset has physical drift $\mu = 0.05$ and volatility $\sigma = 0.40$ with $r = 0.03$. A second asset has $\mu' = 0.10$ and $\sigma' = 0.40$, driven by the same Brownian motion. Compute $\theta$ for each asset. Are the two values consistent? What does this tell you about arbitrage in this market?

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

    This means **there is no single equivalent martingale measure** under which both discounted prices are martingales. By the fundamental theorem of asset pricing, this implies the market admits **arbitrage**. Intuitively, one could exploit the inconsistency by trading the two assets against each other, since they share the same risk factor but offer different compensation per unit of risk. (The precise construction of the arbitrage strategy requires care and is not immediate from the $\theta$-mismatch alone.)

---

**Exercise 4.**
Under $\mathbb{P}$, a zero-coupon bond price satisfies $dP(t,T) = \mu_P P(t,T)\,dt + \sigma_P P(t,T)\,dW_t^{\mathbb{P}}$. Apply the Girsanov drift adjustment to derive the dynamics under $\mathbb{Q}$ and show that the discounted bond price $e^{-\int_0^t r_s\,ds}P(t,T)$ is a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 4"
    Under $\mathbb{P}$, the zero-coupon bond dynamics are:

    $$
    dP(t,T) = \mu_P P(t,T)\,dt + \sigma_P P(t,T)\,dW_t^{\mathbb{P}}
    $$

    The market price of risk is $\lambda_t = (\mu_P - r_t)/\sigma_P$, where $r_t$ is the short rate. Note that in interest rate models the market price of risk $\lambda_t$ may depend on state variables such as $r_t$, making $\lambda_t$ adapted rather than constant. Define $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \lambda_s\,ds$. Substituting $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \lambda_t\,dt$:

    $$
    dP(t,T) = \mu_P P\,dt + \sigma_P P\bigl(dW_t^{\mathbb{Q}} - \lambda_t\,dt\bigr)
    $$

    $$
    = (\mu_P - \sigma_P\lambda_t)P\,dt + \sigma_P P\,dW_t^{\mathbb{Q}}
    $$

    Since $\sigma_P\lambda_t = \sigma_P \cdot \frac{\mu_P - r_t}{\sigma_P} = \mu_P - r_t$:

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

---

**Exercise 5.**
Suppose $\theta$ is not constant but depends on the current stock price: $\theta_t = (\mu(S_t) - r) / \sigma(S_t)$. Write the Radon–Nikodym derivative $Z_T$ in integral form and state the Novikov condition that must hold. Explain why this condition may fail for certain choices of $\mu(\cdot)$ and $\sigma(\cdot)$.

??? success "Solution to Exercise 5"
    When $\theta_t = (\mu(S_t) - r)/\sigma(S_t)$ depends on the stock price, the Radon–Nikodym derivative in integral form is:

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

---

**Exercise 6.**
After applying Girsanov to remove the drift from $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$, you obtain $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. The discounted price $\tilde{S}_t$ satisfies $d\tilde{S}_t = \sigma\tilde{S}_t\,dW_t^{\mathbb{Q}}$ — a driftless SDE. A candidate concludes: "Therefore $\tilde{S}_t$ is a martingale." Is this conclusion justified?

??? success "Solution to Exercise 6"
    **Not automatically.** A driftless SDE only guarantees that $\tilde{S}_t$ is a **local martingale**. Upgrading to a true martingale requires an integrability condition such as $\mathbb{E}[\int_0^T \sigma^2\tilde{S}_s^2\,ds] < \infty$.

    In the constant-coefficient Black–Scholes model this is easily verified (and Novikov handles the density). But for models with state-dependent or unbounded volatility (e.g., CEV with $\beta > 1$), the driftless discounted price can be a strict local martingale — driftless yet not a martingale. "No drift" certifies a candidate; integrability certifies the real thing.

