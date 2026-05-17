# Risk-Neutral Measure

Recall (see [§ risk-neutral construction](../../ch04/risk_neutral/construction.md)): with the money-market account $B_t = \exp(\int_0^t r_s\,ds)$ as numéraire, the risk-neutral measure $\mathbb{Q}$ makes $S_t/B_t$ a martingale for every tradable, giving

$$
V_t = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,V_T\,\middle|\,\mathcal{F}_t\right]
$$

This section emphasises features specific to interest-rate modelling.

---

## Interest-rate context


In interest-rate models:

- the short rate $r_t$ determines discounting,
- $\mathbb{Q}$-dynamics are calibrated to prices,
- physical dynamics are relevant for risk management, not pricing.

---

## Key takeaways


- Risk-neutral measure enforces arbitrage-free pricing.
- Discounted prices are martingales under $\mathbb{Q}$.
- Pricing reduces to discounted expectation.

---

## Further reading


- Harrison & Pliska, martingale pricing.
- Björk, *Arbitrage Theory in Continuous Time*.

---

## Exercises

**Exercise 1.** Under the risk-neutral measure $\mathbb{Q}$, the short rate follows the Vasicek model $dr_t = a(b - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$. Using the pricing formula

$$
P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\;\middle|\;\mathcal{F}_t\right]
$$

explain why the bond price depends on $r_t$ but not on the physical drift parameters. What role does the risk-neutral drift $a(b - r_t)$ play in determining bond prices?

??? success "Solution to Exercise 1"

    Under the risk-neutral measure $\mathbb{Q}$, the bond price is given by

    $$
    P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\;\middle|\;\mathcal{F}_t\right]
    $$

    The key observation is that this formula involves only $\mathbb{Q}$-dynamics of $r_t$, which are $dr_t = a(b - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$. The parameters $a$, $b$, $\sigma$ are the **risk-neutral** parameters. Crucially, the **physical** drift parameters (say $\tilde{a}$ and $\tilde{b}$ under $\mathbb{P}$) do not appear anywhere in this computation.

    **Why $P(t, T)$ depends on $r_t$ but not on physical drift parameters:**

    1. The expectation is taken under $\mathbb{Q}$, so only the $\mathbb{Q}$-drift $a(b - r_t)$ and volatility $\sigma$ govern the evolution of $r_s$ for $s \in [t, T]$.
    2. The process $r_t$ is Markov under $\mathbb{Q}$, so conditioned on $\mathcal{F}_t$, the distribution of $\{r_s\}_{s \geq t}$ under $\mathbb{Q}$ depends only on $r_t$ (and the risk-neutral parameters).
    3. The physical-measure drift $\tilde{a}(\tilde{b} - r_t)$ is absorbed into the Girsanov change of measure. Once we pass to $\mathbb{Q}$, only $\mathbb{Q}$-parameters remain.

    **Role of the risk-neutral drift:** The risk-neutral drift $a(b - r_t)$ determines the conditional distribution of future short rates under $\mathbb{Q}$, which in turn determines:

    - The expected path of $r_s$ under $\mathbb{Q}$ (affecting the mean of the discount factor).
    - The mean-reversion speed $a$ controls how fast $r_t$ reverts to $b$, shaping the term structure.
    - The long-run mean $b$ determines the asymptotic level of yields for long maturities.

    In the Vasicek model, the bond price has the closed-form expression $P(t, T) = e^{A(t,T) - B(t,T) r_t}$ where $B(t,T) = \frac{1 - e^{-a(T-t)}}{a}$ and $A(t,T)$ depends on $a$, $b$, and $\sigma$ --- all risk-neutral parameters. The physical drift plays no role.

---

**Exercise 2.** Show that if $S_t$ is a tradable asset (with no dividends) and $B_t = \exp(\int_0^t r_s\,ds)$, then the discounted price $\tilde{S}_t = S_t / B_t$ being a $\mathbb{Q}$-martingale implies that

$$
S_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,S_T\right]
$$

Verify this identity for the special case where $r_t = r$ is constant and $S_t$ follows geometric Brownian motion.

??? success "Solution to Exercise 2"

    **Showing the pricing identity.** Since $\tilde{S}_t = S_t / B_t$ is a $\mathbb{Q}$-martingale, the martingale property gives

    $$
    \tilde{S}_0 = \mathbb{E}^{\mathbb{Q}}[\tilde{S}_T \mid \mathcal{F}_0] = \mathbb{E}^{\mathbb{Q}}[\tilde{S}_T]
    $$

    Substituting $\tilde{S}_0 = S_0 / B_0 = S_0$ (since $B_0 = 1$) and $\tilde{S}_T = S_T / B_T = e^{-\int_0^T r_s\,ds} S_T$:

    $$
    S_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,S_T\right]
    $$

    This is the fundamental pricing formula applied to the asset $S_t$ itself.

    **Verification for constant $r$ and GBM.** Under $\mathbb{Q}$ with constant $r$, the stock satisfies $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. By Itô's formula:

    $$
    S_T = S_0 \exp\!\left((r - \tfrac{1}{2}\sigma^2)T + \sigma W_T^{\mathbb{Q}}\right)
    $$

    Now compute the right-hand side:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT} S_T\right] = e^{-rT} S_0 \, \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left((r - \tfrac{1}{2}\sigma^2)T + \sigma W_T^{\mathbb{Q}}\right)\right]
    $$

    Since $W_T^{\mathbb{Q}} \sim N(0, T)$, we use $\mathbb{E}[e^{cZ}] = e^{c^2/2}$ for $Z \sim N(0,1)$:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(\sigma W_T^{\mathbb{Q}}\right)\right] = e^{\sigma^2 T / 2}
    $$

    Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT} S_T\right] = e^{-rT} S_0 \, e^{(r - \sigma^2/2)T} \, e^{\sigma^2 T/2} = e^{-rT} S_0 \, e^{rT} = S_0
    $$

    This confirms $S_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT} S_T]$.

---

**Exercise 3.** Under the physical (real-world) measure $\mathbb{P}$, a stock follows $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$ with $\mu = 10\%$ and $\sigma = 25\%$. The risk-free rate is $r = 3\%$. Identify the market price of risk $\lambda = (\mu - r)/\sigma$ and write down the stock dynamics under $\mathbb{Q}$. Verify that the discounted stock price is a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 3"

    **Market price of risk.** The market price of risk is

    $$
    \lambda = \frac{\mu - r}{\sigma} = \frac{0.10 - 0.03}{0.25} = \frac{0.07}{0.25} = 0.28
    $$

    **Girsanov transformation.** Define $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \lambda t$. By Girsanov's theorem, $W_t^{\mathbb{Q}}$ is a Brownian motion under $\mathbb{Q}$, where

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = \exp\!\left(-\lambda W_t^{\mathbb{P}} - \frac{\lambda^2}{2}t\right)
    $$

    **Stock dynamics under $\mathbb{Q}$.** Substituting $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \lambda\,dt$ into the physical dynamics:

    $$
    dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}} = \mu S_t\,dt + \sigma S_t(dW_t^{\mathbb{Q}} - \lambda\,dt)
    $$

    $$
    = (\mu - \sigma\lambda)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}} = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    since $\mu - \sigma\lambda = 0.10 - 0.25 \times 0.28 = 0.10 - 0.07 = 0.03 = r$.

    **Verification that the discounted price is a $\mathbb{Q}$-martingale.** The discounted stock price is $\tilde{S}_t = e^{-rt}S_t$. By Itô's formula:

    $$
    d\tilde{S}_t = e^{-rt}(dS_t - rS_t\,dt) = e^{-rt}\sigma S_t\,dW_t^{\mathbb{Q}} = \sigma \tilde{S}_t\,dW_t^{\mathbb{Q}}
    $$

    This is a driftless SDE driven by a $\mathbb{Q}$-Brownian motion. Since the coefficient satisfies standard integrability conditions (the stochastic exponential is a true martingale for GBM), $\tilde{S}_t$ is indeed a $\mathbb{Q}$-martingale.

---

**Exercise 4.** Consider a digital option that pays \$1 at time $T$ if $r_T > K$ and nothing otherwise. Express the price as a risk-neutral expectation:

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{r_T > K\}}\right]
$$

Explain why this expectation cannot be simplified by pulling the discount factor outside the indicator function. Contrast this with the simplification possible under the $T$-forward measure.

??? success "Solution to Exercise 4"

    The digital option price is

    $$
    V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{r_T > K\}}\right]
    $$

    **Why the discount factor cannot be pulled outside the indicator:**

    The discount factor $e^{-\int_0^T r_s\,ds}$ depends on the entire path $\{r_s\}_{0 \leq s \leq T}$, while the indicator $\mathbf{1}_{\{r_T > K\}}$ depends on the terminal value $r_T$. Since $r_T$ and $\int_0^T r_s\,ds$ are **jointly dependent** (not independent), one cannot factor the expectation as

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\right] \cdot \mathbb{E}^{\mathbb{Q}}\!\left[\mathbf{1}_{\{r_T > K\}}\right]
    $$

    In particular, higher values of $r_T$ tend to be associated with higher values of $\int_0^T r_s\,ds$ (larger discount), creating a negative correlation between the two factors. Factoring would ignore this dependency and produce an incorrect price.

    To evaluate $V_0$ under $\mathbb{Q}$, one needs the **joint distribution** of $\left(\int_0^T r_s\,ds,\; r_T\right)$, which is available in Gaussian models (e.g., Vasicek/Hull-White) but is generally complex.

    **Simplification under the $T$-forward measure:** Under $\mathbb{Q}^T$ with numéraire $P(t, T)$:

    $$
    V_0 = P(0, T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[\mathbf{1}_{\{r_T > K\}}\right] = P(0, T)\,\mathbb{Q}^T(r_T > K)
    $$

    The stochastic discounting has been absorbed into the numéraire change. One now only needs the **marginal distribution** of $r_T$ under $\mathbb{Q}^T$ (not the joint distribution). In Gaussian short-rate models, $r_T$ is normally distributed under $\mathbb{Q}^T$, so:

    $$
    V_0 = P(0, T)\,\Phi\!\left(\frac{m^T - K}{s^T}\right)
    $$

    where $m^T = \mathbb{E}^{\mathbb{Q}^T}[r_T]$ and $(s^T)^2 = \mathrm{Var}^{\mathbb{Q}^T}(r_T)$, and $\Phi$ is the standard normal CDF.

---

**Exercise 5.** In a two-period binomial model, the risk-free rate is $r = 2\%$ per period, the up factor is $u = 1.10$, and the down factor is $d = 0.92$. Compute the risk-neutral probability $q = (1+r-d)/(u-d)$ and price a European call option with strike $K = 105$ on a stock with $S_0 = 100$. Verify that the discounted stock price is a martingale under $q$.

??? success "Solution to Exercise 5"

    **Risk-neutral probability.** The risk-neutral probability of an up move is

    $$
    q = \frac{1 + r - d}{u - d} = \frac{1 + 0.02 - 0.92}{1.10 - 0.92} = \frac{0.10}{0.18} = \frac{5}{9} \approx 0.5556
    $$

    **Stock price tree.** Starting from $S_0 = 100$:

    - Period 1: $S_u = 110$, $S_d = 92$
    - Period 2: $S_{uu} = 121$, $S_{ud} = S_{du} = 101.20$, $S_{dd} = 84.64$

    **Option payoff at $T = 2$.** With strike $K = 105$:

    - $C_{uu} = \max(121 - 105, 0) = 16$
    - $C_{ud} = \max(101.20 - 105, 0) = 0$
    - $C_{dd} = \max(84.64 - 105, 0) = 0$

    **Option price by backward induction.** At period 1:

    $$
    C_u = \frac{1}{1 + r}[q \cdot C_{uu} + (1-q) \cdot C_{ud}] = \frac{1}{1.02}\left[\frac{5}{9} \cdot 16 + \frac{4}{9} \cdot 0\right] = \frac{80/9}{1.02} = \frac{80}{9.18} \approx 8.7146
    $$

    $$
    C_d = \frac{1}{1.02}[q \cdot C_{ud} + (1-q) \cdot C_{dd}] = \frac{1}{1.02}[0] = 0
    $$

    At period 0:

    $$
    C_0 = \frac{1}{1.02}[q \cdot C_u + (1-q) \cdot C_d] = \frac{1}{1.02}\left[\frac{5}{9} \cdot 8.7146 + 0\right] = \frac{4.8415}{1.02} \approx 4.7466
    $$

    Alternatively, using the two-period formula directly:

    $$
    C_0 = \frac{1}{(1+r)^2}\left[q^2 \cdot C_{uu} + 2q(1-q) \cdot C_{ud} + (1-q)^2 \cdot C_{dd}\right]
    $$

    $$
    = \frac{1}{1.0404}\left[\left(\frac{5}{9}\right)^2 \cdot 16\right] = \frac{1}{1.0404} \cdot \frac{25}{81} \cdot 16 = \frac{400/81}{1.0404} = \frac{4.9383}{1.0404} \approx 4.7466
    $$

    **The call option price is approximately $\$4.75$.**

    **Verification of the martingale property.** The discounted stock price at each node should satisfy $\tilde{S}_t = \mathbb{E}^q[\tilde{S}_{t+1} \mid \mathcal{F}_t]$.

    At $t = 0$: $\tilde{S}_0 = S_0 = 100$, and

    $$
    \mathbb{E}^q\!\left[\frac{S_1}{1+r}\right] = \frac{q \cdot 110 + (1-q) \cdot 92}{1.02} = \frac{(5/9)(110) + (4/9)(92)}{1.02} = \frac{61.11 + 40.89}{1.02} = \frac{102}{1.02} = 100 = \tilde{S}_0 \;\checkmark
    $$

    At $t = 1$, node $u$: $\tilde{S}_u = 110/1.02 = 107.84$, and

    $$
    \mathbb{E}^q\!\left[\frac{S_2}{(1+r)^2}\;\middle|\;S_1 = 110\right] = \frac{q \cdot 121 + (1-q) \cdot 101.20}{1.0404} = \frac{67.22 + 44.98}{1.0404} = \frac{112.20}{1.0404} = 107.84 \;\checkmark
    $$

    The discounted stock price is indeed a martingale under $q$.

---

**Exercise 6.** Explain why the risk-neutral measure $\mathbb{Q}$ is unique in a complete market but not unique in an incomplete market. In the context of interest-rate modeling, give an example of a situation where market incompleteness arises and discuss how practitioners resolve the non-uniqueness of $\mathbb{Q}$.

??? success "Solution to Exercise 6"

    **Uniqueness in a complete market:**

    A market is **complete** if every contingent claim can be replicated by a self-financing trading strategy in the underlying assets. By the Second Fundamental Theorem of Asset Pricing (Harrison--Pliska), the risk-neutral measure $\mathbb{Q}$ is **unique** if and only if the market is complete.

    Intuitively, in a complete market with $d$ sources of randomness (Brownian motions), there are exactly $d$ risky assets available for trading. The $d$ market prices of risk $\lambda_1, \ldots, \lambda_d$ are uniquely determined by the requirement that all discounted asset prices be martingales under $\mathbb{Q}$. This gives $d$ equations in $d$ unknowns, yielding a unique solution.

    **Non-uniqueness in an incomplete market:**

    In an incomplete market, there are **more sources of randomness than tradable assets**. If there are $d$ Brownian motions but only $k < d$ traded assets, the martingale conditions provide only $k$ equations for $d$ market prices of risk. This leaves $d - k$ free parameters, resulting in a family of risk-neutral measures.

    **Interest-rate example of incompleteness:**

    Stochastic volatility models provide a natural example. Consider a short-rate model where both the level and the volatility are stochastic:

    $$
    dr_t = \mu(r_t, v_t)\,dt + \sqrt{v_t}\,dW_t^{(1)}
    $$

    $$
    dv_t = \alpha(r_t, v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
    $$

    There are two sources of randomness ($W^{(1)}$ and $W^{(2)}$), but only one asset (the bond market, driven through $r_t$) is liquidly traded for hedging. The volatility risk associated with $W^{(2)}$ cannot be perfectly hedged, making the market incomplete. The market price of volatility risk $\lambda_2$ is not determined by no-arbitrage alone.

    **How practitioners resolve non-uniqueness:**

    1. **Calibration to market prices:** Choose $\mathbb{Q}$ (equivalently, $\lambda_2$) so that model prices match observed market prices of liquid instruments (caps, swaptions, etc.).
    2. **Risk premium specification:** Impose an explicit functional form for the market price of risk, e.g., $\lambda_2 = \gamma \sqrt{v_t}$, with $\gamma$ estimated from data.
    3. **Utility-based arguments:** Select $\mathbb{Q}$ by minimizing some criterion (e.g., minimal entropy martingale measure).
    4. **Pricing by superreplication or indifference:** Give a range of prices or a utility-based unique price without selecting a single $\mathbb{Q}$.
