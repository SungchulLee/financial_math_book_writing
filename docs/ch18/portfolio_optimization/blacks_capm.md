# Black's 1972 Model (Zero-Beta CAPM)



**Also known as Black’s CAPM**, this model was developed by Fischer Black in 1972 as a generalization of the standard Capital Asset Pricing Model (CAPM). It addresses a critical limitation of the classical CAPM—the assumption of a **risk-free asset** that investors can borrow or lend unlimited amounts at a constant rate. Black's framework offers a powerful extension by retaining the core intuition of CAPM while eliminating the need for a risk-free benchmark.

### A. Motivation:




In many real-world markets, truly risk-free assets do not exist, or investors face constraints (e.g., credit restrictions, transaction costs, illiquidity, or regulatory barriers) that make borrowing or lending at the risk-free rate unrealistic or impossible. For example, institutional investors such as pension funds or insurance companies often operate under constraints that prevent them from holding or trading in theoretical risk-free assets. Black's model relaxes this unrealistic assumption, creating a more **robust and general version** of CAPM that functions effectively in environments where only risky assets are accessible.

By considering a market of purely risky assets, Black's model aligns more closely with actual investment conditions faced by many agents. It maintains the critical CAPM insight: that expected returns should compensate investors for systematic risk. But instead of grounding this in the existence of a risk-free asset, Black finds an alternative in the form of a special portfolio—the **zero-beta portfolio**.







### B. Key Features:



- **No risk-free asset**: The model does not rely on the existence of a perfectly safe asset with a guaranteed return.
- **Only risky assets are available for investment**: Investors construct portfolios using only risky securities.
- **Efficient frontier forms a curve**, not a straight line: Without the ability to borrow or lend at a risk-free rate, investors cannot form the Capital Market Line. Instead, the mean-variance efficient frontier is a curved locus of optimal portfolios comprised entirely of risky assets.
- The **market portfolio** is replaced by the **Sharpe portfolio**, which is the tangency portfolio on the efficient frontier, possessing the highest Sharpe ratio among feasible portfolios.
- The role of the risk-free asset is assumed by a **zero-beta portfolio**, which is a portfolio that is **uncorrelated** with the Sharpe portfolio and effectively acts as the baseline return in the linear pricing equation.

The model posits that all investors will hold some combination of the Sharpe portfolio and the zero-beta portfolio, depending on their risk preferences, echoing the logic of the two-fund separation theorem under restricted conditions.


### C. Main Proposition:


Let:
- $r_p$: return of any portfolio $p$
- $r_c$: return of the Sharpe (tancy) portfolio
- $c$: expected return of the zero-beta portfolio

Then, the expected return of any portfolio $p$ satisfies the following linear relationship:

$$
E(r_p) = c + \beta_p \left(E(r_c) - c\right)
$$

Where:
- $\beta_p = \dfrac{\operatorname{Cov}(r_p, r_c)}{\sigma_c^2}$ is the **beta** of portfolio $p$ with respect to the Sharpe portfolio
- $E(r_c)$ is the expected return of the Sharpe portfolio
- $c$ is the expected return of the **zero-beta portfolio**, i.e., the portfolio with zero covariance with $r_c$

This equation shows that expected returns depend linearly on beta even in the absence of a risk-free asset, but the intercept $c$ is now endogenous and market-determined, unlike the fixed $r_f$ in standard CAPM.

#### Derivation of the Standard CAPM



Let:
- $r_p$: return of any portfolio $p$
- $r_m$: return of the **market portfolio**
- $r_f$: return of the **risk-free asset**

Then the **expected return** of portfolio $p$ satisfies the **Capital Asset Pricing Model** (CAPM):

$$
E(r_p) = r_f + \beta_p \left(E(r_m) - r_f\right)
$$

Where:
- $\beta_p = \dfrac{\operatorname{Cov}(r_p, r_m)}{\operatorname{Var}(r_m)}$ is the **beta** of portfolio $p$ with respect to the market portfolio
- $E(r_m)$ is the expected return of the market portfolio
- $r_f$ is the return of the risk-free asset

**Intuition Behind the Formula**

- Investors combine the risk-free asset with the **market portfolio**, forming a straight line in mean–variance space — the **Capital Market Line (CML)**.
- All efficient portfolios lie on this line. Thus, **expected returns depend only on beta** — the exposure to the market.
- $\beta_p$ captures the **systematic risk**: how much portfolio $p$ co-moves with the market.

**Where Does This Come From?**

1. The **market portfolio** is mean–variance optimal under CAPM assumptions.
2. Investors can borrow/lend at the **risk-free rate**, forming linear combinations:
   $$ r_p = w r_m + (1 - w) r_f $$
3. This yields:
   $$ E(r_p) = w E(r_m) + (1 - w) r_f = r_f + w(E(r_m) - r_f) $$
4. Since $\beta_p = w$ in this case (because volatility scales linearly with $w$),
   we get:
   $$
   E(r_p) = r_f + \beta_p (E(r_m) - r_f)
   $$

**Key Assumptions of Standard CAPM**

- All investors can borrow/lend at the risk-free rate $r_f$
- Homogeneous expectations
- Market portfolio is **the** efficient portfolio of risky assets
- No taxes, no transaction costs
- Returns are normally distributed or investors are mean–variance optimizers



#### Understanding the Zero-Beta Portfolio


A key innovation in Black's CAPM is the replacement of the risk-free asset with the **zero-beta portfolio**, denoted $r_z$. This portfolio plays a critical role in anchoring the expected return line, analogous to how the risk-free rate anchors the Capital Market Line in standard CAPM.

But what exactly is this zero-beta portfolio?

Black defines $r_z$ as a portfolio that satisfies two conditions:
1. It is fully invested in risky assets (i.e., a convex combination of risky securities).
2. It is **uncorrelated with the tangency portfolio** $r_c$:
   $$
   \operatorname{Cov}(r_z, r_c) = 0
   $$

This covariance condition makes $r_z$ a "zero-beta" asset in the sense of having no systematic exposure to $r_c$. However, the mere condition of zero covariance does not uniquely determine such a portfolio. To make it unique, Black imposes an **additional optimization condition**:

> The zero-beta portfolio $r_z$ is the portfolio with **minimum variance** among all fully invested portfolios that are uncorrelated with the tangency portfolio $r_c$.


#### Why this implies $r_z$ lies on the boundary of the bullet:





The set of all feasible portfolios made from risky assets forms the so-called **Markowitz bullet** in the mean-standard deviation space. The boundary of this bullet is the **mean-variance frontier**, consisting of all portfolios that minimize variance for a given expected return.

By solving a variance minimization problem subject to full investment and zero covariance with $r_c$, $r_z$ lies on this boundary — but typically on the **inefficient (lower)** part of the frontier, below the tangency portfolio.

In summary:
- $r_z$ is **not** on the efficient frontier (it offers lower return for the same risk compared to efficient portfolios).
- $r_z$ **is** on the boundary of the bullet (mean-variance frontier) because it minimizes variance under linear constraints.
- It is **entirely composed of risky assets**.

Thus, Black's CAPM retains the elegant linear pricing structure of CAPM, but replaces the exogenous risk-free asset with an **endogenously derived** zero-beta portfolio that is feasible within the set of risky portfolios.

#### Derivation of Black's CAPM (Zero-Beta CAPM)





Let:
- $r_p$: return of any portfolio $p$  
- $r_c$: return of the **tangency portfolio** (Sharpe portfolio)  
- $c$: expected return of the **zero-beta portfolio** (uncorrelated with $r_c$)

**Key Setup**

In Black’s model:
- There is **no risk-free asset**, so investors can only invest in **risky portfolios**.
- The mean–variance efficient frontier is **a curve**, not a straight line.
- The optimal risky portfolio is the **tangency portfolio** $r_c$, just like in CAPM.
- Since investors cannot move along a straight line by borrowing/lending at $r_f$, we replace the role of $r_f$ with a **zero-beta portfolio**: a portfolio that satisfies:

$$
\operatorname{Cov}(r_z, r_c) = 0
$$

**Goal: Express $E(r_p)$ in terms of $\beta_p$ with respect to $r_c$ and the return of the zero-beta portfolio.**

**Step 1: Any portfolio lies on a line in $(\sigma, E[r])$ space**

From mean–variance theory, if $r_z$ is a portfolio **uncorrelated with $r_c$**, then any other portfolio $r_p$ can be written as a linear combination of $r_z$ and $r_c$:

$$
r_p = \alpha r_c + (1 - \alpha) r_z
$$

for some scalar $\alpha$.

Taking expectation on both sides:

$$
E(r_p) = \alpha E(r_c) + (1 - \alpha) E(r_z) = c + \alpha (E(r_c) - c)
$$


**Step 2: Relate $\alpha$ to $\beta_p$**

Let’s compute the covariance of $r_p$ with $r_c$:

$$
\operatorname{Cov}(r_p, r_c) = \operatorname{Cov}(\alpha r_c + (1 - \alpha) r_z, r_c)
= \alpha \operatorname{Var}(r_c) + (1 - \alpha) \underbrace{\operatorname{Cov}(r_z, r_c)}_{=0}
= \alpha \sigma_c^2
$$

So we can solve for $\alpha$:

$$
\alpha = \frac{\operatorname{Cov}(r_p, r_c)}{\sigma_c^2} = \beta_p
$$


**Step 3: Plug into Expected Return Equation**

$$
E(r_p) = c + \beta_p (E(r_c) - c)
$$

This is **Black’s CAPM equation**. ✔️

**Intuition Recap**

- In standard CAPM, the **intercept** is $r_f$.
- In Black’s CAPM, there’s **no $r_f$**, so we estimate the **expected return of a portfolio that has zero beta** (uncorrelated with the market/tangency portfolio).
- The pricing relation remains **linear in beta**.



**Assumptions of Black's CAPM**

- Investors can only invest in **risky assets** (no risk-free borrowing/lending)
- All investors are mean–variance optimizers
- Markets are frictionless
- The tangency portfolio is the optimal risky portfolio
- A **zero-beta portfolio** can be formed (uncorrelated with tangency portfolio)



#### Q. Why Can We Write $r_p$ as a convex combination of $r_c$ and $r_z$?

**Why Can We Write $r_p = \alpha r_c + (1 - \alpha) r_z$?**

This comes from a general result in **mean–variance portfolio theory**:

> Any portfolio on the **mean-variance frontier** can be expressed as a linear combination of **any two other efficient portfolios**, **provided those two are not perfectly colinear**.

So in Black’s CAPM:
- We assume two portfolios:
  - $r_c$: the **tangency portfolio** (analogous to the market portfolio)
  - $r_z$: the **zero-beta portfolio**, which lies on the frontier and is **uncorrelated** with $r_c$
- Then any other efficient portfolio $r_p$ can be written as a **convex combination** of $r_c$ and $r_z$.

This is a generalization of the **two-fund separation theorem**:
> Any investor's optimal portfolio is a combination of **two efficient portfolios**, even without a risk-free asset.

**Why Choose $r_z$ Specifically?**

Because it’s:
- On the efficient frontier
- **Uncorrelated** with $r_c$ (so its beta is zero)
- Provides a **new intercept** in the absence of a risk-free asset



**Analogy: Risk-Free vs Zero-Beta**

| With Risk-Free Asset         | Without Risk-Free Asset         |
|-----------------------------|----------------------------------|
| $r_p = \alpha r_m + (1 - \alpha) r_f$ | $r_p = \alpha r_c + (1 - \alpha) r_z$ |
| $r_f$ is known constant      | $r_z$ is unknown but estimated  |
| Leads to CAPM                | Leads to Black's CAPM           |



So Step 1 holds because **efficient portfolios lie in a 2D plane**, and we’re choosing $r_z$ and $r_c$ as the basis for expressing any other efficient portfolio $r_p$.





### D. Intuition and Interpretation:


- Like the classical CAPM, Black's model implies a **linear pricing relationship** between expected returns and systematic risk, measured by beta.
- However, because there is no risk-free rate, the intercept of this line is the expected return of the **zero-beta portfolio** rather than a constant risk-free rate $r_f$.
- The **Sharpe portfolio** plays the role of the benchmark or proxy for the market portfolio, offering the best trade-off between risk and return among all risky portfolios.
- The **zero-beta portfolio** serves as a theoretical baseline portfolio against which the risk of other portfolios is measured. It is constructed such that it has zero covariance with the Sharpe portfolio, and its expected return $c$ becomes the new anchor point for the expected return line.
- Portfolios with higher $\beta_p$ have greater covariance with the Sharpe portfolio and therefore require higher expected returns to compensate for the additional systematic risk.

This pricing relationship preserves the elegance and interpretability of the CAPM framework while broadening its range of applicability.

### E. Applications:




Black's model is particularly useful in the following scenarios:
- **Markets without reliable risk-free assets**: For example, in emerging markets or during financial crises, risk-free borrowing or lending may not be possible.
- **Institutional constraints**: Pension funds, mutual funds, and insurance companies often operate under investment restrictions that exclude borrowing or restrict access to Treasury instruments.
- **Testing asset pricing models empirically**: Researchers often face difficulties identifying a suitable risk-free asset; Black's model offers a viable alternative.
- **Illiquid markets**: When the theoretical risk-free asset is highly illiquid or when bid-ask spreads and transaction costs are substantial, standard CAPM assumptions break down.

In such settings, Black's model offers a consistent and economically intuitive framework for understanding how risk is priced in equilibrium.



### F. Comparison to Standard CAPM:



| Feature                        | **Standard CAPM**           | **Black’s Zero-Beta CAPM**     |
|-------------------------------|------------------------------|---------------------------------|
| Risk-free asset               | Assumed to exist             | Not assumed                     |
| Efficient frontier            | Straight line (with $r_f$)   | Convex curve (risky assets only)|
| Benchmark portfolio           | Market portfolio             | Sharpe (tangency) portfolio     |
| Intercept of return-beta line | Risk-free rate $r_f$         | Zero-beta return $c$            |
| Beta interpretation           | Relative to market portfolio | Relative to Sharpe portfolio    |
| Applicability                 | Idealized markets            | Broader, real-world scenarios   |
| Required instruments          | Risky + risk-free assets      | Risky assets only               |

This comparison highlights the generalization that Black's CAPM offers: the structure of risk-based pricing holds without relying on idealized instruments.

### G. Python Demo

#### Q. What Is Beta?




**Beta ($\beta$)** measures how sensitive an asset’s return is to movements in a benchmark portfolio:
- In **CAPM**, this benchmark is the **market portfolio** (or a proxy for it).
- In **Black’s CAPM**, it’s the **tangency (Sharpe) portfolio**.

**Mathematically:**

$$
\beta_i = \frac{\operatorname{Cov}(r_i, r_{\text{benchmark}})}{\operatorname{Var}(r_{\text{benchmark}})}
$$



#### Q. What Does It Mean If NFLX Is Above the CAPM Line?



**Interpretation:**

- **NFLX’s actual expected return** is **higher than predicted** by the CAPM model for its level of beta risk.
- This means it's delivering more return than the CAPM suggests it should.

##### Implication: Potential Underpricing or Alpha



In traditional CAPM thinking:
- **Above the line = “undervalued” or positive alpha** (rewarding more than expected for its risk)
- **Below the line = “overvalued” or negative alpha** (offering too little for its risk)

So in this case:
> NFLX may be viewed (by this model) as offering excess return **relative to its systematic risk**.

This is why these plots are often used to **test the validity of CAPM** or spot **mispriced assets** under a given model.

#### Q. Is It “Okay” That NFLX Is Above the Line?



Yes — perfectly okay, and **common**. CAPM is a **theoretical model**, and real-world assets:
- Rarely fall exactly on the predicted line.
- May reflect market inefficiencies, behavioral mispricings, or risk factors not captured by CAPM.



#### Q. What Is Alpha?


**Alpha** is a measure of **excess return**:
> It's the part of an asset's return that **cannot be explained by its beta** (systematic risk) in a CAPM-like model.

In other words:
- **CAPM predicts** a certain expected return based on an asset’s beta.
- **Alpha is the difference** between the actual return and this predicted return.



**Formula (Using CAPM):**

For an asset $i$ with beta $\beta_i$ and expected return $E(r_i)$, the CAPM prediction is:

$$
E(r_i)^{\text{CAPM}} = r_f + \beta_i (E(r_m) - r_f)
$$

Then, alpha is:

$$
\\alpha_i = E(r_i) - E(r_i)^{\\text{CAPM}}
$$

**Intuition**

| Alpha Sign     | Interpretation                               |
|----------------|-----------------------------------------------|
| $\alpha > 0$   | Asset is **outperforming** CAPM prediction (undervalued) |
| $\alpha = 0$   | Asset return is **fully explained by CAPM**   |
| $\alpha < 0$   | Asset is **underperforming** for its risk      |

**Example (from plot):**

If NFLX has:
- Beta = 1.0
- Expected Return = 0.70
- CAPM-predicted Return = 0.55

Then:
$$
\\alpha_{\\text{NFLX}} = 0.70 - 0.55 = 0.15
$$

That 0.15 (or 15%) is **alpha** — excess return over what CAPM says it should deliver.

#### Q. So there are two alphas, one from CAPM and another from Black's CAPM

Exactly! 🔥 You're absolutely right — each model (Standard CAPM and Black's CAPM) gives **its own predicted return**, so you can compute **two different alphas** for each asset.

**Summary Table**

| Model             | Predicted Return                     | Alpha Formula                              |
|------------------|---------------------------------------|---------------------------------------------|
| **Standard CAPM** | $r_f + \beta_i (E[r_m] - r_f)$        | $\alpha_i^{\text{CAPM}} = E[r_i] - E[r_i]^{\text{CAPM}}$ |
| **Black's CAPM** | $c + \beta_i (E[r_c] - c)$            | $\alpha_i^{\text{Black}} = E[r_i] - E[r_i]^{\text{Black}}$ |

- $r_f$ = risk-free rate  
- $E[r_m]$ = expected return of market portfolio  
- $c$ = expected return of **zero-beta portfolio**  
- $E[r_c]$ = expected return of **tangency (Sharpe) portfolio**  
- $\beta_i$ = beta relative to either market or tangency

**Interpretation**

| If...                            | Then...                                      |
|----------------------------------|----------------------------------------------|
| $\alpha_i^{\text{CAPM}} > 0$     | Asset is beating the CAPM line               |
| $\alpha_i^{\text{Black}} > 0$    | Asset is beating Black’s CAPM prediction     |
| $\alpha_i^{\text{CAPM}} \ne \alpha_i^{\text{Black}}$ | They disagree on what's “fair” for that beta! |

So comparing both can give insight into how assumptions affect valuation.



#### Q. Which one is more commonly used in the market

Great question — here’s a breakdown of which alpha is more commonly used **in practice**:

**Most Common in the Market: Standard CAPM Alpha**

Why?

- **Simplicity & convention**: CAPM with a risk-free rate is the textbook standard.
- **Benchmarks & reports**: Financial analysts, hedge funds, mutual funds, and Bloomberg terminals often report **alpha based on CAPM**.
- **Sharpe ratios, Jensen's alpha, regression-based factor models** all usually use the **risk-free rate version**.

**When is Black’s CAPM Alpha Used?**

- **Academic papers or advanced quant models**, especially when:
  - **No reliable risk-free rate** exists (emerging markets, crises).
  - **Institutional constraints** make borrowing/lending at $r_f$ unrealistic.
- **More realistic modeling** in settings with only risky assets.

**Real-World Practice vs Theory**

| Context                        | Common Alpha Used               |
|-------------------------------|---------------------------------|
| Asset managers, reports       | **Standard CAPM alpha**         |
| Academic / constrained markets| Black's CAPM alpha              |
| Retail investors & dashboards | Standard CAPM alpha             |
| Custom quant research         | Either / both                   |

**TL;DR**

> If you're building something **for real-world investment or reporting**, use **CAPM alpha**.  
> If you're exploring **alternative pricing models** or **markets without a clean risk-free asset**, Black’s CAPM alpha can reveal deeper insights.











### Conclusion:


Black’s extension of CAPM demonstrates that the concept of **pricing of systematic risk via beta** remains fundamentally valid even when a risk-free asset is not available. His work showed that the key insight of CAPM—that investors are only compensated for bearing systematic (non-diversifiable) risk—can be preserved in more realistic market settings.

By introducing the **zero-beta portfolio** and adjusting the pricing formula accordingly, Black made the CAPM framework significantly more **realistic, robust, and applicable** to the complexities of actual financial markets. This model remains a cornerstone of asset pricing theory, particularly valuable when strict assumptions of classical models cannot be justified.

Ultimately, the Zero-Beta CAPM stands as a testament to the enduring power of economic modeling to adapt to market imperfections while preserving theoretical coherence.

