# Pricing under Intensity Models


Intensity-based models provide tractable pricing formulas for defaultable claims by modeling default via a hazard rate process.

---

## Pricing framework


Assume:
- default intensity $\lambda_t$,
- recovery scheme specified,
- immersion and progressive enlargement hold.

Pricing reduces to computing discounted expectations involving survival probabilities.

---

## Defaultable zero-coupon bond


Under recovery of treasury (RT), the price simplifies to

$$
P^d(t,T)
= \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T (r_s + \lambda_s) ds\right)
\middle| \mathcal{F}_t
\right]
$$



Default risk acts like an additional discount rate.

---

## General recovery case


With recovery of face value or market value, pricing involves:
- integrals over default times,
- survival probabilities,
- expected recovery payments.

Closed forms exist for simple intensity models.

---

## Relation to CDS pricing


The same framework prices:
- credit default swaps (premium vs protection legs),
- risky bonds and loans,
- credit-linked notes.

Consistency across products is essential.

---

## Key takeaways


- Intensity models yield tractable pricing formulas.
- Default risk enters through survival probabilities.
- Recovery assumptions must be consistent across instruments.

---

## Further reading


- Duffie & Singleton, intensity-based pricing.
- Brigo et al., credit derivatives pricing.

---

## Exercises

**Exercise 1.** Under the recovery of treasury convention, the defaultable zero-coupon bond price is

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + \lambda_s)\,ds} \mid \mathcal{F}_t\right]
$$

For constant $r = 3\%$ and constant $\lambda = 2\%$, compute $P^d(0,5)$. Interpret the result as discounting at a "credit-adjusted" rate.

??? success "Solution to Exercise 1"

    **Given:** Constant $r = 0.03$, constant $\lambda = 0.02$, recovery of treasury (RT), $T = 5$, face value $F = 1$ (unit notional).

    Under RT, the defaultable zero-coupon bond price is:

    $$
    P^d(0,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T (r_s + \lambda_s)\,ds} \mid \mathcal{F}_0\right]
    $$

    With constant $r$ and $\lambda$, this simplifies to:

    $$
    P^d(0,5) = e^{-(r + \lambda)T} = e^{-(0.03 + 0.02) \times 5} = e^{-0.25}
    $$

    Computing:

    $$
    P^d(0,5) = e^{-0.25} = 0.77880
    $$

    **Interpretation as credit-adjusted discounting:** The price can be viewed as discounting at a "credit-adjusted" rate of $r + \lambda = 5\%$ instead of the risk-free rate $r = 3\%$. The additional $\lambda = 2\%$ in the discount rate reflects the default intensity. This means default risk acts exactly like an additional interest rate: it increases the effective discount rate, thereby reducing the present value of the bond.

    Equivalently, we can factor the price as:

    $$
    P^d(0,5) = \underbrace{e^{-rT}}_{P(0,5)} \times \underbrace{e^{-\lambda T}}_{S(0,5)} = 0.86071 \times 0.90484 = 0.77880
    $$

    The defaultable bond price equals the risk-free bond price multiplied by the survival probability. Under the RT convention with independence of rates and intensity, the credit and interest rate components separate cleanly into a product.

---

**Exercise 2.** Using the intensity-based framework, derive the price of a CDS protection leg:

$$
\text{PV}_{\text{prot}} = (1 - R)\int_0^T D(0,u)\,\lambda_u\,S(0,u)\,du
$$

For $R = 40\%$, $r = 3\%$, $\lambda = 1.5\%$, and $T = 5$, compute the numerical value per unit notional.

??? success "Solution to Exercise 2"

    **Goal:** Derive the CDS protection leg formula and compute its numerical value.

    **Derivation:**

    The protection leg of a CDS pays $(1-R)$ at default time $\tau$ (per unit notional), provided $\tau \le T$. Under the intensity-based framework, its present value is:

    $$
    \text{PV}_{\text{prot}} = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{\tau} r_s\,ds}(1-R)\,\mathbf{1}_{\{\tau \le T\}}\right]
    $$

    Using the key identity for intensity-based models (the intensity representation of conditional expectations involving $\tau$):

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{\tau} r_s\,ds}\,g(\tau)\,\mathbf{1}_{\{\tau \le T\}}\right] = \mathbb{E}^{\mathbb{Q}}\!\left[\int_0^T e^{-\int_0^u r_s\,ds}\,g(u)\,\lambda_u\,e^{-\int_0^u \lambda_s\,ds}\,du\right]
    $$

    with $g(u) = (1-R)$:

    $$
    \text{PV}_{\text{prot}} = (1-R)\int_0^T \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^u (r_s + \lambda_s)\,ds}\,\lambda_u\right]du
    $$

    Under independence of $r$ and $\lambda$ (and deterministic or constant values), this becomes:

    $$
    \text{PV}_{\text{prot}} = (1-R)\int_0^T D(0,u)\,S(0,u)\,\lambda_u\,du
    $$

    where $D(0,u) = e^{-\int_0^u r_s\,ds}$ is the risk-free discount factor and $S(0,u) = e^{-\int_0^u \lambda_s\,ds}$ is the survival probability.

    **Numerical computation:** With $R = 0.40$, $r = 0.03$, $\lambda = 0.015$, $T = 5$:

    $$
    \text{PV}_{\text{prot}} = (1-0.40)\int_0^5 e^{-0.03u}\,e^{-0.015u}\,0.015\,du = 0.6 \times 0.015 \int_0^5 e^{-0.045u}\,du
    $$

    $$
    = 0.009 \int_0^5 e^{-0.045u}\,du = 0.009 \times \left[\frac{-1}{0.045}e^{-0.045u}\right]_0^5
    $$

    $$
    = 0.009 \times \frac{1}{0.045}\left(1 - e^{-0.225}\right) = 0.009 \times 22.222 \times (1 - 0.79852)
    $$

    $$
    = 0.009 \times 22.222 \times 0.20148 = 0.009 \times 4.4773 = 0.04030
    $$

    The present value of the protection leg is **0.04030** (or 4.030%) per unit notional.

    This means that for a $\$1{,}000{,}000$ notional CDS, the protection buyer receives expected payments worth $\$40{,}300$ in present value terms.

---

**Exercise 3.** Explain why the immersion (H-hypothesis) and progressive enlargement assumptions are essential for the intensity-based pricing framework. What would go wrong if default revealed information about future market factor values?

??? success "Solution to Exercise 3"

    **The immersion (H-hypothesis) and progressive enlargement assumptions:**

    **Progressive enlargement of filtration:** The full market filtration $\mathcal{G}_t$ is constructed as $\mathcal{G}_t = \mathcal{F}_t \vee \mathcal{H}_t$, where $\mathcal{F}_t$ contains information about market factors (interest rates, stock prices, etc.) and $\mathcal{H}_t = \sigma(\mathbf{1}_{\{\tau \le s\}} : s \le t)$ is the default indicator filtration. This means the only additional information beyond $\mathcal{F}_t$ is whether default has occurred.

    **Immersion (H-hypothesis):** Every $(\mathcal{F}_t)$-martingale remains a $(\mathcal{G}_t)$-martingale. Equivalently, observing whether default has occurred does not change the conditional distribution of future market factors. Formally:

    $$
    \mathbb{E}[\xi \mid \mathcal{G}_t] = \mathbb{E}[\xi \mid \mathcal{F}_t] \quad \text{for all } \mathcal{F}_\infty\text{-measurable } \xi
    $$

    **Why these assumptions are essential:**

    1. **Pricing decomposition:** The key identity used in intensity-based pricing is:

        $$
        \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}} \mid \mathcal{G}_t\right] = \mathbf{1}_{\{\tau > t\}}\,\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + \lambda_s)\,ds} \mid \mathcal{F}_t\right]
        $$

        This identity requires immersion. It allows replacing the expectation over default events with an integral involving the intensity, greatly simplifying calculations.

    2. **Intensity interpretation:** Under immersion, the $\mathcal{F}_t$-intensity $\lambda_t$ is also the $\mathcal{G}_t$-intensity of default. Without immersion, the hazard rate could change once default information is incorporated.

    3. **Hedging and replication:** Immersion ensures that $\mathcal{F}_t$-adapted hedging strategies remain valid in the enlarged filtration.

    **What would go wrong without immersion:**

    If default revealed information about future market factors (violating immersion), then:

    - Observing that a firm has not defaulted by time $t$ would update the conditional distribution of interest rates, stock prices, and other factors.
    - The intensity $\lambda_t$ computed from $\mathcal{F}_t$ would differ from the true hazard rate in $\mathcal{G}_t$.
    - The key pricing identity above would fail, and the tractable decomposition into survival and recovery components would break down.
    - Simple formulas like "discount at $r + \lambda$" would no longer hold.
    - Example: If a bank's default signals a forthcoming interest rate cut, then $\mathbb{E}[r_T \mid \tau = 2] \neq \mathbb{E}[r_T \mid \mathcal{F}_2]$, violating immersion and invalidating standard intensity-based pricing.

---

**Exercise 4.** A CDS with maturity 5 years has a par spread of 100 bp, and a defaultable bond with the same maturity and issuer trades at a yield spread of 130 bp. Using the intensity model framework, explain why these two spread measures should be approximately equal in theory, and identify three practical reasons they might differ.

??? success "Solution to Exercise 4"

    **Given:** CDS par spread = 100 bp, bond yield spread = 130 bp, maturity = 5 years, same issuer.

    **Why the two spreads should be approximately equal in theory:**

    In the intensity-based framework, both the CDS spread and the bond yield spread are determined by the same default intensity $\lambda$ and recovery rate $R$. Under the approximation with constant parameters:

    - CDS par spread: $s_{\text{CDS}} \approx (1-R)\lambda$
    - Bond yield spread (under RMV): $s_{\text{bond}} \approx (1-R)\lambda$

    Both spreads reflect the same loss-adjusted intensity $(1-R)\lambda$. This is because:

    1. The CDS protection leg pays $(1-R)$ at default, priced at $(1-R)\int_0^T D(0,u)S(0,u)\lambda_u\,du$.
    2. The CDS premium leg pays $s_{\text{CDS}}$ continuously until default, priced at $s_{\text{CDS}}\int_0^T D(0,u)S(0,u)\,du$.
    3. Setting these equal: $s_{\text{CDS}} \approx (1-R)\bar{\lambda}$.
    4. The bond yield spread under RMV is $s_{\text{bond}} = (1-R)\bar{\lambda}$.

    Therefore, in a frictionless market with consistent recovery assumptions, $s_{\text{CDS}} \approx s_{\text{bond}}$.

    **Three practical reasons they differ (CDS-bond basis of $130 - 100 = 30$ bp):**

    1. **Funding costs and the repo rate:** Bond investors must fund the purchase of the bond. If the funding rate exceeds the risk-free rate (as is typical), the effective bond spread includes a funding cost component that the CDS does not. This pushes bond spreads above CDS spreads, contributing to a positive basis (bond spread > CDS spread).

    2. **Liquidity differences:** Corporate bonds are generally less liquid than CDS contracts. The bond yield spread includes a liquidity premium to compensate investors for illiquidity, bid-ask spreads, and difficulty of execution. CDS markets are typically more liquid for actively traded names. This liquidity premium widens the bond spread relative to the CDS spread.

    3. **Cheapest-to-deliver option in CDS:** Upon a CDS credit event, the protection buyer can deliver the cheapest eligible bond. This delivery option has value to the protection buyer, which is reflected in a lower CDS spread than would otherwise prevail. Additionally, recovery conventions differ: CDS settlement uses actual recovery (often via auction), while bond pricing models assume a fixed $R$.

    Other factors include: counterparty risk in CDS, accrued interest conventions, coupon effects in bonds, and the fact that bonds embed interest rate risk that is netted out differently than in the CDS.

---

**Exercise 5.** Under the Duffie-Singleton (RMV) recovery convention, derive the defaultable bond price

$$
P^d(t,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + (1-R)\lambda_s)\,ds} \mid \mathcal{F}_t\right]
$$

starting from the recursive relationship $P^d(\tau-,T) = R \cdot P^d(\tau-,T)$ at default. Show that the loss-adjusted intensity $(1-R)\lambda$ replaces $\lambda$ in the discount rate.

??? success "Solution to Exercise 5"

    **Goal:** Derive the Duffie-Singleton formula under RMV recovery.

    **Step 1: Setup.**

    Consider a defaultable zero-coupon bond with face value $F$ and maturity $T$. Under RMV, at default the recovery is:

    $$
    \text{Recovery} = R \cdot P^d(\tau-, T)
    $$

    where $P^d(\tau-, T)$ is the pre-default market value.

    **Step 2: Pre-default pricing equation.**

    On the event $\{\tau > t\}$, the pre-default price $P^d(t,T)$ satisfies the risk-neutral valuation:

    $$
    P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,F\,\mathbf{1}_{\{\tau > T\}} + e^{-\int_t^{\tau} r_s\,ds}\,R\,P^d(\tau-,T)\,\mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right]
    $$

    **Step 3: Apply the intensity representation.**

    Using the key identity for intensity models, the first term becomes:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + \lambda_s)\,ds}\,F \mid \mathcal{F}_t\right]
    $$

    For the second term, using the intensity representation:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\int_t^T e^{-\int_t^u (r_s + \lambda_s)\,ds}\,\lambda_u\,R\,P^d(u,T)\,du \mid \mathcal{F}_t\right]
    $$

    Note that we replace $P^d(\tau-, T)$ with $P^d(u, T)$ since the pre-default price is $\mathcal{F}_t$-adapted.

    **Step 4: Integral equation.**

    Combining:

    $$
    P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + \lambda_s)\,ds}\,F + \int_t^T e^{-\int_t^u (r_s + \lambda_s)\,ds}\,R\lambda_u\,P^d(u,T)\,du \mid \mathcal{F}_t\right]
    $$

    **Step 5: Guess and verify the solution.**

    Conjecture:

    $$
    P^d(t,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + (1-R)\lambda_s)\,ds} \mid \mathcal{F}_t\right]
    $$

    To verify, define $\tilde{r}_s = r_s + (1-R)\lambda_s$ and write $r_s + \lambda_s = \tilde{r}_s + R\lambda_s$. Then:

    $$
    e^{-\int_t^u (r_s + \lambda_s)\,ds} = e^{-\int_t^u \tilde{r}_s\,ds} \cdot e^{-\int_t^u R\lambda_s\,ds}
    $$

    Substituting the conjectured form $P^d(u,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_u^T \tilde{r}_s\,ds} \mid \mathcal{F}_u\right]$ into the integral equation and using the tower property, the second term becomes:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\int_t^T e^{-\int_t^u \tilde{r}_s\,ds}\,R\lambda_u\,e^{-R\int_t^u \lambda_s\,ds}\,F\,e^{-\int_u^T \tilde{r}_s\,ds}\,du \mid \mathcal{F}_t\right]
    $$

    This simplifies (using $\tilde{r}_s + R\lambda_s = r_s + \lambda_s$) to match the original equation. More directly, the Duffie-Singleton argument proceeds via the infinitesimal generator.

    **Step 6: Infinitesimal argument.**

    Consider the bond price over an infinitesimal interval $[t, t+dt]$. With probability $\lambda_t\,dt$, default occurs and the holder receives $R \cdot P^d(t,T)$. With probability $1 - \lambda_t\,dt$, survival occurs and the holder retains $P^d(t+dt, T)$. The no-arbitrage condition gives:

    $$
    r_t\,P^d(t,T)\,dt = -dP^d(t,T) + \lambda_t\,dt\left(R\,P^d(t,T) - P^d(t,T)\right)
    $$

    $$
    r_t\,P^d\,dt = -dP^d - (1-R)\lambda_t\,P^d\,dt
    $$

    $$
    dP^d = -(r_t + (1-R)\lambda_t)\,P^d\,dt
    $$

    This is the ODE for exponential discounting at rate $\tilde{r}_t = r_t + (1-R)\lambda_t$, yielding:

    $$
    P^d(t,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + (1-R)\lambda_s)\,ds} \mid \mathcal{F}_t\right]
    $$

    The loss-adjusted intensity $(1-R)\lambda$ replaces $\lambda$ in the discount rate because the RMV recovery "cancels" a fraction $R$ of the default loss. Instead of losing the entire value at default (which would require discounting at $r + \lambda$), the holder loses only $(1-R)$ of the value, so the effective default-related discount is $(1-R)\lambda$.

---

**Exercise 6.** Consider an affine intensity model where $\lambda_t$ follows a CIR process: $d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma\sqrt{\lambda_t}\,dW_t$ with $\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, and $\lambda_0 = 1\%$. Using the affine bond pricing formula, describe qualitatively how the defaultable bond price depends on the current intensity $\lambda_0$. What happens to the price as $\lambda_0$ increases from $1\%$ to $5\%$?

??? success "Solution to Exercise 6"

    **Given:** CIR intensity process $d\lambda_t = \kappa(\theta - \lambda_t)\,dt + \sigma\sqrt{\lambda_t}\,dW_t$ with $\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, $\lambda_0 = 1\%$.

    **Affine bond pricing structure:**

    Since $\lambda_t$ follows a CIR process, the defaultable bond price (under RT or zero recovery) has the affine form:

    $$
    P^d(0,T) = e^{-rT} \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T \lambda_s\,ds}\right] = e^{-rT} \cdot e^{-A(T) - B(T)\lambda_0}
    $$

    where $A(T)$ and $B(T)$ satisfy Riccati ODEs:

    $$
    B'(T) = 1 - \kappa B(T) - \frac{1}{2}\sigma^2 B(T)^2, \quad B(0) = 0
    $$

    $$
    A'(T) = -\kappa\theta\,B(T), \quad A(0) = 0
    $$

    The explicit solution for $B(T)$ is:

    $$
    B(T) = \frac{2(e^{\gamma T} - 1)}{(\gamma + \kappa)(e^{\gamma T} - 1) + 2\gamma}
    $$

    where $\gamma = \sqrt{\kappa^2 + 2\sigma^2} = \sqrt{0.25 + 2 \times 0.0064} = \sqrt{0.2628} = 0.5126$.

    **Qualitative dependence on $\lambda_0$:**

    The bond price is $P^d(0,T) = e^{-rT - A(T) - B(T)\lambda_0}$. Since $B(T) > 0$ for all $T > 0$, the price is a **decreasing exponential function** of $\lambda_0$:

    $$
    \frac{\partial P^d}{\partial \lambda_0} = -B(T) \cdot P^d(0,T) < 0
    $$

    Higher current intensity means higher default risk, which reduces the bond price. The sensitivity is:

    - **Linear in $B(T)$:** For short maturities, $B(T) \approx T$ (the intensity acts like a parallel shift in rates). For longer maturities, $B(T)$ saturates at $B(\infty) = \frac{2}{\kappa + \gamma} = \frac{2}{0.5 + 0.5126} = 1.975$.
    - **Proportional to the price level:** The percentage impact is $-B(T)\,d\lambda_0$.

    **Effect as $\lambda_0$ increases from 1% to 5%:**

    For a 5-year bond ($T = 5$), the change in the exponent is approximately:

    $$
    \Delta(\text{exponent}) = -B(5) \times (\lambda_0^{\text{new}} - \lambda_0^{\text{old}})
    $$

    Computing $B(5)$ with $\gamma = 0.5126$:

    $$
    e^{\gamma \times 5} = e^{2.563} = 12.97
    $$

    $$
    B(5) = \frac{2(12.97 - 1)}{(0.5126 + 0.5)(12.97 - 1) + 2 \times 0.5126} = \frac{23.94}{1.0126 \times 11.97 + 1.0252} = \frac{23.94}{12.12 + 1.03} = \frac{23.94}{13.15} = 1.821
    $$

    The price ratio is:

    $$
    \frac{P^d(\lambda_0 = 5\%)}{P^d(\lambda_0 = 1\%)} = e^{-B(5)(0.05 - 0.01)} = e^{-1.821 \times 0.04} = e^{-0.0728} = 0.9298
    $$

    The bond price decreases by approximately 7% when $\lambda_0$ quadruples from 1% to 5%.

    **Mean reversion effects:** Since $\lambda_0 = 1\% < \theta = 2\%$, the intensity is expected to increase toward $\theta$ over time, which means the short-end of the spread curve will be below the long-end (upward-sloping spread curve). When $\lambda_0$ rises to $5\% > \theta$, the intensity is expected to revert downward, producing a downward-sloping spread curve. The long-run spread in both cases converges to approximately $(1-R)\theta_{\infty}$, which depends on the risk-neutral long-run mean.
