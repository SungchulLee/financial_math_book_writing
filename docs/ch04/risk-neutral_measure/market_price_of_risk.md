# Market Price of Risk


Investors holding a risky asset are exposed to uncertainty and require compensation
beyond the risk-free rate. The **market price of risk** captures exactly how much
excess return the market demands per unit of Brownian risk. It is simultaneously an
economic quantity (the instantaneous Sharpe ratio) and the mathematical kernel that
drives the Girsanov measure change from \(\mathbb{P}\) to \(\mathbb{Q}\).

---

## Definition


For a risky asset with dynamics
\[
dS_t = \mu_t S_t\,dt + \sigma_t S_t\,dW_t^{\mathbb{P}},
\]
the **market price of risk** is defined as
\[
\theta_t := \frac{\mu_t - r_t}{\sigma_t}.
\]

In a single-factor setting, \(\theta_t\) coincides with the **instantaneous Sharpe ratio**:
excess expected return per unit of standard deviation.

---

## Interpretation


- Large \(\theta_t\): high compensation required for bearing risk.
- Small \(\theta_t\): low risk premium.

### How probabilities are tilted

The Radon-Nikodym derivative
\(Z_T = \exp(-\int_0^T\!\theta_s\,dW_s^{\mathbb{P}} - \tfrac12\int_0^T\!\theta_s^2\,ds)\)
re-weights paths: when \(\theta > 0\), paths with negative Brownian increments (adverse
for the stock) receive higher weight under \(\mathbb{Q}\), while paths with positive
increments (favorable returns) receive lower weight. In this way, the risk-neutral
measure **overweights bad states and underweights good states**, removing the risk
premium from expected returns.

### Geometric view

Geometrically, the Girsanov change \(W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds\)
shifts the center of the Brownian distribution by \(\theta\) per unit time.
Equivalently, it tilts the drift of the log-price from \(\mu - \tfrac12\sigma^2\) to
\(r - \tfrac12\sigma^2\), shifting the distribution of paths rather than individual realizations.

---

## Role in Measure Change


The drift adjustment in Girsanov’s theorem is precisely \(\theta_t\):
\[
W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds.
\]

Thus:
- \(\theta_t\) removes excess drift,
- volatility remains unchanged.

---

## Multi-Asset Case


In a market with \(n\) risky assets driven by a \(d\)-dimensional Brownian motion
\(\mathbf{W}_t^{\mathbb{P}}\), the scalar \(\theta_t\) generalises to a vector
\(\boldsymbol{\theta}_t \in \mathbb{R}^d\) satisfying
\[
\boldsymbol{\mu}_t - r_t \mathbf{1}
= \Sigma_t \boldsymbol{\theta}_t,
\]
where \(\Sigma_t\) is the volatility matrix.

---

## Connection to the Stochastic Discount Factor


In equilibrium asset pricing, the **stochastic discount factor** (SDF, or pricing
kernel) \(M_t\) satisfies \(\mathbb{E}^{\mathbb{P}}[M_T \Phi_T \mid \mathcal{F}_t] = V_t\).
The Radon-Nikodym derivative \(Z_T = d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T}\) is
proportional to \(M_T / B_T^{-1}\): switching from SDF pricing under \(\mathbb{P}\) to
expectation pricing under \(\mathbb{Q}\) is achieved by absorbing the SDF into the
probability measure. The market price of risk \(\theta\) therefore encodes the same
information as the SDF, expressed as a Girsanov drift adjustment rather than a
multiplicative kernel. In other words, the SDF discounts payoffs directly under
\(\mathbb{P}\), while the change of measure incorporates this discounting into
probabilities under \(\mathbb{Q}\). These are two equivalent ways of encoding the same
pricing rule.

---

## Summary


The market price of risk:

- encodes risk premia,
- determines the Radon–Nikodym derivative,
- equals the instantaneous Sharpe ratio in single-factor models,
- connects to the stochastic discount factor of equilibrium theory.

It is the key quantity connecting observed returns to risk-neutral pricing.

---

## Exercises

**Exercise 1.**
A stock has $\mu = 0.09$, $\sigma = 0.20$, and $r = 0.03$. Compute the market price of risk $\theta$. If $\mu$ increases to $0.12$ while $\sigma$ and $r$ remain unchanged, how does $\theta$ change? Interpret this economically.

??? success "Solution to Exercise 1"
    With $\mu = 0.09$, $\sigma = 0.20$, and $r = 0.03$:

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.09 - 0.03}{0.20} = 0.30
    $$

    If $\mu$ increases to $0.12$:

    $$
    \theta' = \frac{0.12 - 0.03}{0.20} = 0.45
    $$

    The market price of risk increases from $0.30$ to $0.45$. Economically, this means that the asset now offers a higher excess return per unit of volatility, so more probability tilting is needed when moving from $\mathbb{P}$ to $\mathbb{Q}$. A higher $\theta$ reflects a larger risk premium that must be "removed" to construct the risk-neutral measure.

---

**Exercise 2.**
Using the definition $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$, show that under $\mathbb{Q}$ the drift of the stock price process changes from $\mu$ to $r$, while the volatility $\sigma$ is unchanged. Explain why $\theta$ is called the "price" of risk.

??? success "Solution to Exercise 2"
    Under $\mathbb{P}$, the stock satisfies $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$. Using $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$ with constant $\theta = (\mu - r)/\sigma$, we have $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta\,dt$. Substituting:

    $$
    dS_t = \mu S_t\,dt + \sigma S_t(dW_t^{\mathbb{Q}} - \theta\,dt) = (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    Since $\sigma\theta = \mu - r$, the drift becomes $\mu - (\mu - r) = r$:

    $$
    dS_t = r S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    The drift changes from $\mu$ to $r$, while the diffusion coefficient $\sigma$ is unchanged. The quantity $\theta$ is called the "price" of risk because it measures the excess return $\mu - r$ per unit of risk $\sigma$. It quantifies how much compensation (in units of drift per unit of volatility) the market demands for bearing one unit of Brownian risk, analogous to a per-unit price.

---

**Exercise 3.**
In a two-asset market with volatility matrix $\Sigma$ and excess return vector $\boldsymbol{\mu} - r\mathbf{1}$, the market price of risk vector satisfies $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$. Suppose $\Sigma$ is a $2 \times 3$ matrix (two assets, three Brownian motions). How many free parameters does $\boldsymbol{\theta}$ have? What does this imply about market completeness?

??? success "Solution to Exercise 3"
    The system $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$ becomes a $2 \times 3$ system with $\boldsymbol{\theta} \in \mathbb{R}^3$. This is an **underdetermined** system: 2 equations with 3 unknowns.

    Any particular solution $\boldsymbol{\theta}_0$ can be modified by adding any vector in the null space of $\Sigma$: if $\Sigma\mathbf{v} = 0$, then $\boldsymbol{\theta}_0 + c\mathbf{v}$ is also a solution for any scalar $c$. Since $\Sigma$ is $2 \times 3$ with rank at most 2, the null space has dimension at least $3 - 2 = 1$.

    Therefore $\boldsymbol{\theta}$ has (at least) **one free parameter**. This means there are infinitely many risk-neutral measures, implying the market is **incomplete**. With fewer traded assets than sources of risk, not all contingent claims can be replicated, and derivative prices are not uniquely determined by no-arbitrage alone.

---

**Exercise 4.**
Show that the market price of risk $\theta = (\mu - r)/\sigma$ equals the Sharpe ratio of the asset. Explain why this means all assets in a single-factor complete market must have the same Sharpe ratio, and relate this to the absence of arbitrage.

??? success "Solution to Exercise 4"
    The Sharpe ratio of the asset is defined as the excess expected return per unit of standard deviation:

    $$
    \text{Sharpe ratio} = \frac{\mathbb{E}[dS_t/S_t] - r\,dt}{\text{Std}[dS_t/S_t]} = \frac{\mu\,dt}{\sigma\sqrt{dt}} \cdot \frac{1}{\sqrt{dt}} - \frac{r}{\sigma} = \frac{\mu - r}{\sigma} = \theta
    $$

    More precisely, over an infinitesimal interval, $dS_t/S_t$ has mean $\mu\,dt$ and standard deviation $\sigma\sqrt{dt}$, so the instantaneous Sharpe ratio is $(\mu - r)/\sigma = \theta$.

    In a single-factor complete market (one Brownian motion), the market price of risk $\theta$ is uniquely determined and must be the same for all traded assets. If asset $i$ has drift $\mu_i$ and volatility $\sigma_i$, then $(\mu_i - r)/\sigma_i = \theta$ for all $i$. This means every asset has the same Sharpe ratio.

    If two assets had different Sharpe ratios, say $(\mu_1 - r)/\sigma_1 > (\mu_2 - r)/\sigma_2$, one could construct a zero-investment portfolio (long asset 1, short asset 2 in appropriate proportions) with zero volatility but positive drift — an arbitrage. Therefore, equal Sharpe ratios are equivalent to absence of arbitrage in a single-factor model.

---

**Exercise 5.**
Suppose $\theta_t$ is time-varying with $\theta_t = a + b\sin(2\pi t)$ where $a = 0.3$ and $b = 0.2$. Compute $\int_0^1 \theta_t^2\,dt$ and verify that the Novikov condition is satisfied for $T = 1$. Does the market price of risk need to be constant for the risk-neutral measure to exist?

??? success "Solution to Exercise 5"
    With $\theta_t = a + b\sin(2\pi t)$ where $a = 0.3$ and $b = 0.2$:

    $$
    \int_0^1 \theta_t^2\,dt = \int_0^1 [a + b\sin(2\pi t)]^2\,dt
    $$

    Expanding:

    $$
    = \int_0^1 [a^2 + 2ab\sin(2\pi t) + b^2\sin^2(2\pi t)]\,dt
    $$

    Computing each term: $\int_0^1 a^2\,dt = a^2 = 0.09$, $\int_0^1 2ab\sin(2\pi t)\,dt = 0$ (full period of sine), and $\int_0^1 b^2\sin^2(2\pi t)\,dt = b^2/2 = 0.02$. Therefore:

    $$
    \int_0^1 \theta_t^2\,dt = 0.09 + 0 + 0.02 = 0.11
    $$

    The Novikov condition requires $\mathbb{E}^{\mathbb{P}}[\exp(\frac{1}{2}\int_0^T \theta_s^2\,ds)] < \infty$. Since $\theta_t$ is deterministic, this reduces to $\exp(\frac{1}{2} \cdot 0.11) = \exp(0.055) \approx 1.0566 < \infty$. The condition is trivially satisfied.

    No, $\theta_t$ does **not** need to be constant. The risk-neutral measure exists as long as the Novikov condition (or a weaker sufficient condition) holds, which accommodates a wide class of time-varying and even stochastic market prices of risk.

---

**Exercise 6.**
A market has two stocks both driven by the same Brownian motion: $dS_t^i = \mu_i S_t^i\,dt + \sigma_i S_t^i\,dW_t$ for $i = 1, 2$. Show that no-arbitrage requires $(\mu_1 - r)/\sigma_1 = (\mu_2 - r)/\sigma_2$. What happens if this equality is violated?

??? success "Solution to Exercise 6"
    Both stocks are driven by the same Brownian motion, so $dS_t^i = \mu_i S_t^i\,dt + \sigma_i S_t^i\,dW_t$ for $i = 1,2$. For a risk-neutral measure to exist, a single $\theta$ must satisfy

    $$
    \mu_1 - r = \sigma_1\theta, \qquad \mu_2 - r = \sigma_2\theta
    $$

    Dividing: $\theta = (\mu_1 - r)/\sigma_1 = (\mu_2 - r)/\sigma_2$, which gives

    $$
    \frac{\mu_1 - r}{\sigma_1} = \frac{\mu_2 - r}{\sigma_2}
    $$

    If this equality is violated, no risk-neutral measure exists, and by the first fundamental theorem of asset pricing, arbitrage exists. Concretely, suppose $(\mu_1 - r)/\sigma_1 > (\mu_2 - r)/\sigma_2$. Construct a portfolio that is long $1/(\sigma_1 S_t^1)$ shares of asset 1 and short $1/(\sigma_2 S_t^2)$ shares of asset 2. The Brownian motion terms cancel, producing a risk-free portfolio with return exceeding $r$ — an arbitrage.

---

**Exercise 7.**
In an interest rate model, the market price of risk is specified exogenously as $\theta_t = \lambda r_t / \sigma$ (proportional to the short rate). Write the risk-neutral dynamics of the short rate and explain how $\theta_t$ modifies the physical drift. Why can't $\theta_t$ be determined from traded asset prices alone in this setting?

??? success "Solution to Exercise 7"
    Suppose the short rate follows $dr_t = \alpha(r_t)\,dt + \sigma\,dW_t^{\mathbb{P}}$ under $\mathbb{P}$, with market price of risk $\theta_t = \lambda r_t / \sigma$. The Girsanov change gives $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta_t\,dt$, so

    $$
    dr_t = \alpha(r_t)\,dt + \sigma(dW_t^{\mathbb{Q}} - \theta_t\,dt) = [\alpha(r_t) - \lambda r_t]\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    For example, if the physical drift is $\alpha(r_t) = \kappa(\bar{r} - r_t)$, the risk-neutral drift becomes

    $$
    \kappa(\bar{r} - r_t) - \lambda r_t = \kappa\bar{r} - (\kappa + \lambda)r_t
    $$

    which can be written as $\kappa^*(\bar{r}^* - r_t)$ with $\kappa^* = \kappa + \lambda$ and $\bar{r}^* = \kappa\bar{r}/(\kappa + \lambda)$.

    The market price of risk $\theta_t$ cannot be determined from traded asset prices alone because the bond market is **incomplete** in the sense that the short rate itself is not a directly traded asset. There is no traded asset whose return dynamics pin down a unique $\theta_t$. Different choices of $\theta_t$ produce different but equally valid risk-neutral measures, each consistent with no-arbitrage but implying different bond and derivative prices. In practice, $\theta_t$ (or equivalently the risk-neutral drift) is calibrated to observed bond prices.
