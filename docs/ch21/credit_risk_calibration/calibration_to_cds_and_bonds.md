# Calibration to CDS and Bonds


In practice, credit models are calibrated jointly to **CDS spreads** and **bond prices**, requiring consistency across instruments.

---

## CDS-based calibration


CDS are preferred calibration instruments because:

- they isolate default risk,
- they are relatively liquid,
- they are less affected by funding and coupon effects.

Thus, CDS-implied hazard rates are often taken as primary inputs.

---

## Bond pricing consistency


Bond prices reflect:

- default risk,
- interest rates,
- liquidity and funding premia.

After calibrating to CDS, bond prices are used as a validation check or secondary calibration target.

---

## Joint calibration challenges


Joint calibration faces:

- conflicting signals between CDS and bonds,
- liquidity differences,
- model limitations (constant recovery, flat intensities).

Perfect consistency is rarely achievable.

---

## Practical compromises


Practitioners often:

- calibrate primarily to CDS,
- allow bond pricing errors within tolerances,
- introduce bond-specific spreads or adjustments.

This reflects real-market frictions.

---

## Key takeaways


- CDS are the main calibration instruments.
- Bonds provide consistency checks.
- Market frictions prevent perfect joint fit.

---

## Further reading


- Duffie & Singleton, CDS vs bond spreads.
- O'Kane, practical credit calibration.

---

## Exercises

**Exercise 1.** A corporate issuer has a 5-year CDS spread of 120 bp and a 5-year bond trading at a spread of 150 bp over the risk-free rate. Assuming $R = 40\%$, compute the hazard rate implied by each instrument. Explain why the two estimates differ and which source of default risk information is considered more reliable for calibration purposes.

??? success "Solution to Exercise 1"
    **Given:** 5-year CDS spread $s_{\text{CDS}} = 120$ bp, 5-year bond spread $s_{\text{bond}} = 150$ bp, $R = 40\%$.

    **Hazard rate from CDS:**

    Using the standard approximation $s \approx (1-R)\lambda$:

    $$
    \lambda_{\text{CDS}} = \frac{s_{\text{CDS}}}{1-R} = \frac{0.0120}{0.60} = 2.00\%
    $$

    **Hazard rate from bond:**

    Applying the same formula to the bond spread:

    $$
    \lambda_{\text{bond}} = \frac{s_{\text{bond}}}{1-R} = \frac{0.0150}{0.60} = 2.50\%
    $$

    **Why the two estimates differ:**

    The bond-implied hazard rate (2.50%) exceeds the CDS-implied hazard rate (2.00%) by 50 bp in spread terms (or 0.50% in intensity). This difference arises because bond spreads contain components beyond pure credit risk:

    1. **Liquidity premium:** Corporate bonds are less liquid than CDS. Investors demand compensation for the difficulty of selling the bond quickly, widening the bond spread relative to the CDS spread.

    2. **Funding costs:** Buying a bond requires financing. If the investor's funding cost exceeds the risk-free rate, the effective spread is higher. CDS, being unfunded, do not carry this cost.

    3. **Tax effects:** Government bonds (the benchmark) may receive favorable tax treatment, artificially widening the corporate-Treasury spread.

    The residual $s_{\text{bond}} - s_{\text{CDS}} = 30$ bp is often called the **CDS-bond basis** and reflects these non-default frictions.

    **Which is more reliable:** The CDS-implied hazard rate is considered more reliable for calibrating credit models because CDS contracts isolate default risk more cleanly. The CDS market is typically more liquid, standardized, and less contaminated by funding and tax effects. Therefore, $\lambda_{\text{CDS}} = 2.00\%$ is the preferred calibration input.

---

**Exercise 2.** Describe three specific frictions that prevent perfect consistency between CDS-implied and bond-implied hazard rates. For each friction, state whether it causes the bond spread to overstate or understate the pure credit component relative to the CDS spread.

??? success "Solution to Exercise 2"
    **Three specific frictions preventing CDS-bond consistency:**

    **1. Liquidity premium in bonds**

    Corporate bonds are traded over-the-counter with significant bid-ask spreads and irregular trading. Investors demand a liquidity premium for holding less liquid instruments. This causes the bond spread to **overstate** the pure credit component relative to the CDS spread. The liquidity premium is typically 20--50 bp for investment-grade bonds and can exceed 100 bp during stress periods.

    **2. Funding cost asymmetry**

    Buying a bond requires cash outlay (or repo financing), while a CDS protection buyer posts only margin. An investor who funds at LIBOR + $x$ bp effectively sees a higher spread on the bond. This causes the bond spread to **overstate** the credit component. Conversely, if an investor has cheap funding (below risk-free), the bond spread may understate credit risk, but this is less common.

    **3. Cheapest-to-deliver (CTD) option in CDS**

    Upon a credit event, the CDS protection buyer can deliver the cheapest eligible bond to settle the contract. This delivery option has value to the protection buyer, which is reflected in a slightly higher CDS spread. This causes the CDS spread to **overstate** the pure credit component relative to the bond spread. However, this effect is typically small (a few basis points) compared to the liquidity and funding effects.

    **Summary:**

    | Friction | Bond spread effect |
    |----------|-------------------|
    | Liquidity premium | Overstates credit |
    | Funding cost | Overstates credit |
    | CTD option (in CDS) | CDS overstates credit |

    On net, the liquidity and funding effects dominate, so bond spreads typically exceed CDS spreads, making the CDS-bond basis negative (i.e., $s_{\text{CDS}} < s_{\text{bond}}$) under normal conditions.

---

**Exercise 3.** A practitioner calibrates a hazard rate curve to CDS spreads and then computes model bond prices. The model underprices a 7-year bond by 80 cents on the dollar relative to the market. Propose two adjustments the practitioner might introduce to reconcile the bond price without disturbing the CDS calibration.

??? success "Solution to Exercise 3"
    The model, calibrated to CDS spreads, underprices a 7-year bond by 80 cents (i.e., the model price is \$99.20 when the market price is \$100.00, or equivalently the model overstates the bond spread). Two adjustments to reconcile without disturbing CDS calibration:

    **Adjustment 1: Bond-specific liquidity spread (Z-spread adjustment)**

    Introduce a **bond-specific spread adjustment** $s_{\text{liq}}$ that accounts for the difference between bond and CDS implied credit quality. Define the model bond price as:

    $$
    P^{\text{adj}} = \sum_{i} c_i \cdot D(0,t_i) \cdot e^{-s_{\text{liq}} \cdot t_i} \cdot S^{\text{CDS}}(0,t_i) + \text{recovery terms}
    $$

    where $S^{\text{CDS}}(0,t_i)$ is the CDS-calibrated survival curve. The parameter $s_{\text{liq}}$ is solved so that $P^{\text{adj}}$ matches the market bond price. Since this adjustment is applied only to the bond pricing formula and does not alter the CDS-calibrated hazard rates, the CDS fit is preserved. Economically, $s_{\text{liq}}$ represents the liquidity, funding, and other non-default components in the bond spread.

    **Adjustment 2: Recovery rate differentiation**

    Use **different recovery rates** for CDS and bonds. CDS contracts settle at par minus recovery, while bond holders receive recovery on the face value. If the bond is trading below par (e.g., at 95 cents), the actual recovery on the bond investment differs from the CDS recovery assumption. Set:

    - $R_{\text{CDS}} = 40\%$ (for CDS calibration, unchanged)
    - $R_{\text{bond}}$: calibrated to match the market bond price

    By adjusting $R_{\text{bond}}$ (which only enters the bond pricing formula), the model bond price can be reconciled. A lower $R_{\text{bond}}$ increases the bond's expected loss, lowering its model price toward the market level. Since the CDS uses a separate recovery assumption, its calibration is undisturbed.

---

**Exercise 4.** Explain why CDS contracts are preferred over bonds as the primary calibration instrument for reduced-form credit models. In your answer, discuss the roles of funding risk, coupon effects, and liquidity.

??? success "Solution to Exercise 4"
    **Why CDS contracts are preferred over bonds as primary calibration instruments:**

    **1. Isolation of default risk**

    CDS contracts are pure credit derivatives: the protection buyer receives a payment if and only if a credit event occurs. The CDS spread therefore reflects primarily the market's assessment of default risk and loss given default. Bonds, by contrast, bundle credit risk with interest rate risk, liquidity risk, and other factors, making it harder to extract the pure credit component.

    **2. Absence of funding risk**

    CDS are unfunded instruments---neither party pays the notional upfront (aside from small margin). Bond investments require full cash outlay or financing. The funding cost depends on the investor's credit quality and market conditions, introducing investor-specific effects into bond spreads that are unrelated to the issuer's credit risk. CDS spreads are largely free of this contamination.

    **3. Minimal coupon effects**

    Bonds with different coupons on the same issuer can trade at different yield spreads due to duration, convexity, and tax effects. A high-coupon bond and a low-coupon bond on the same issuer may imply different hazard rates, even though the underlying credit risk is identical. CDS contracts are standardized (fixed coupon with upfront payment adjustment since 2009), eliminating this source of inconsistency.

    **4. Superior liquidity and standardization**

    For many investment-grade and high-yield issuers, the CDS market is more liquid than the underlying bond market. Standardized ISDA documentation, quarterly roll dates, and fixed coupons make CDS quotes more comparable across issuers and over time. Bond markets are fragmented across many issues with different maturities, coupons, covenants, and embedded options.

    **5. Direct observability of credit events**

    CDS settlements are triggered by well-defined credit events (bankruptcy, failure to pay, restructuring), providing a direct link between the instrument and the default model. Bond price declines may reflect many factors besides credit deterioration.

    For all these reasons, reduced-form credit models are calibrated primarily to CDS spreads, with bond prices serving as secondary validation targets.

---

**Exercise 5.** In a joint calibration, a modeler minimizes

$$
w_{\text{CDS}} \sum_{i} \left(s_i^{\text{model}} - s_i^{\text{market}}\right)^2 + w_{\text{bond}} \sum_{j} \left(P_j^{\text{model}} - P_j^{\text{market}}\right)^2
$$

Discuss how the choice of weights $w_{\text{CDS}}$ and $w_{\text{bond}}$ affects the calibrated hazard rates. What economic rationale would justify setting $w_{\text{CDS}} \gg w_{\text{bond}}$?

??? success "Solution to Exercise 5"
    **Joint calibration objective:**

    $$
    \min_{\boldsymbol{\lambda}} \; w_{\text{CDS}} \sum_{i} \left(s_i^{\text{model}} - s_i^{\text{market}}\right)^2 + w_{\text{bond}} \sum_{j} \left(P_j^{\text{model}} - P_j^{\text{market}}\right)^2
    $$

    **Effect of weights on calibrated hazard rates:**

    The weights $w_{\text{CDS}}$ and $w_{\text{bond}}$ determine the relative importance of matching CDS spreads versus bond prices. Since CDS and bonds generally imply different hazard rates (due to the CDS-bond basis), the calibrated $\boldsymbol{\lambda}$ is a compromise:

    - **High $w_{\text{CDS}}$:** The hazard rates are driven primarily by CDS spreads. Bond pricing errors are tolerated. The resulting $\boldsymbol{\lambda}$ closely approximates the pure CDS-bootstrapped curve.

    - **High $w_{\text{bond}}$:** The hazard rates shift to match bond prices, which include liquidity and funding premia. The CDS fit deteriorates, and the hazard rates may overstate true default risk.

    - **Equal weights:** The calibration compromises between both markets, fitting neither perfectly. The hazard rates reflect an average of CDS-implied and bond-implied credit quality.

    **Rationale for $w_{\text{CDS}} \gg w_{\text{bond}}$:**

    Several economic arguments justify heavily weighting CDS:

    1. **Purity of signal:** CDS spreads isolate default risk more cleanly than bond spreads, which conflate credit risk with liquidity, funding, and tax effects. Calibrating to bonds would embed non-credit components into the hazard rate.

    2. **Liquidity and reliability:** CDS quotes are typically firmer and more liquid, especially for standard maturities. Bond quotes may be stale or reflect dealer inventory effects.

    3. **Model consistency:** Reduced-form models assume that the hazard rate captures default risk. Forcing the model to fit bond prices (which include non-default components) violates this assumption and produces economically inconsistent parameters.

    4. **Hedging practice:** Practitioners hedge credit exposure using CDS. A model calibrated to CDS produces hedge ratios that are consistent with the instruments actually used for hedging.

    A common practical choice is $w_{\text{CDS}} = 1$ and $w_{\text{bond}} = 0$ (calibrate to CDS only, use bonds for validation), or $w_{\text{CDS}}/w_{\text{bond}} \sim 10$--$100$ to allow minor bond influence without distorting the credit signal.

---

**Exercise 6.** During a credit crisis, CDS spreads widen sharply but bond prices remain relatively stable due to illiquidity in the bond market. Describe the challenge this presents for joint calibration. How might a practitioner handle conflicting signals from the two markets?

??? success "Solution to Exercise 6"
    **The challenge during a credit crisis:**

    During a credit crisis, CDS spreads widen rapidly because the CDS market remains relatively liquid and responsive to new credit information. Protection buyers rush to hedge, pushing spreads up. Meanwhile, bond prices may remain artificially stable because:

    - Bond holders are reluctant to sell at distressed prices (loss aversion)
    - Dealer balance sheet constraints reduce market-making capacity
    - Some institutional holders (insurance companies, pension funds) are locked in by mandate or accounting rules
    - Bid-ask spreads in bonds widen dramatically, making mid-market quotes unreliable

    This creates a **divergence in implied hazard rates**: CDS-implied $\lambda^{\text{CDS}}$ spikes while bond-implied $\lambda^{\text{bond}}$ remains muted. The CDS-bond basis (normally negative, meaning $s_{\text{CDS}} < s_{\text{bond}}$) can flip to strongly positive ($s_{\text{CDS}} \gg s_{\text{bond}}$) during crises.

    For joint calibration, this divergence is catastrophic. The optimizer cannot simultaneously fit CDS spreads (which demand high hazard rates) and bond prices (which imply lower hazard rates). Any compromise produces a hazard rate curve that misprices both markets.

    **How a practitioner might handle this:**

    1. **Prioritize CDS:** Treat CDS as the authoritative source of credit risk information during the crisis, since the CDS market is more liquid and price-responsive. Accept bond pricing errors and attribute the residual to a time-varying liquidity factor:

        $$
        s_{\text{bond}} = (1-R)\lambda + s_{\text{liq}}(t)
        $$

        where $s_{\text{liq}}(t)$ is estimated as the residual after CDS calibration.

    2. **Time-varying weights:** Dynamically reduce $w_{\text{bond}}$ as bond market illiquidity increases. Use observable illiquidity proxies (bid-ask spread, trading volume, dealer inventory) to adjust weights. During normal times, $w_{\text{bond}}/w_{\text{CDS}} \approx 0.1$; during crisis, set $w_{\text{bond}} \approx 0$.

    3. **Separate credit and liquidity models:** Decompose the bond spread into a credit component (calibrated to CDS) and a stochastic liquidity component. This requires a two-factor model but produces consistent pricing across both markets.

    4. **Use staleness filters:** Flag bond quotes that have not updated for several days and exclude them from calibration. Only bonds with recent transactions at reasonable bid-ask spreads contribute to the objective function.
