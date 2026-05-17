# Wrong-Way Risk


**Wrong-way risk (WWR)** arises when exposure to a counterparty increases precisely when the counterparty’s credit quality deteriorates. It is a major source of model risk in credit markets.

---

## Definition


Wrong-way risk occurs when:

- exposure and default risk are positively correlated,
- losses are amplified during adverse market conditions.

The opposite case is **right-way risk**, where exposure decreases as credit risk increases.

---

## Examples


Typical examples include:

- interest-rate swaps with leveraged counterparties,
- FX derivatives where currency depreciation weakens the counterparty,
- CDS written on correlated reference entities.

WWR is most severe during market stress.

---

## Modeling challenges


Recall (see [§ Reduced-Form Intensity-Based Models](../reduced_form_intensity_based_models/affine_intensity_models.md)): standard intensity models often assume independence between exposure and default, and constant or exogenous intensities. These assumptions underestimate tail losses when WWR is present.

---

## Practical mitigation


Mitigation techniques include:

- conservative exposure modeling,
- stressed CVA calculations — Recall (see [§ Pricing with Default Risk](../pricing_with_default_risk/defaultable_bonds.md)),
- explicit dependence between market factors and intensity.

Regulatory frameworks require explicit WWR consideration.

---

## Key takeaways


- Wrong-way risk amplifies credit losses.
- Independence assumptions are dangerous.
- Stress-based modeling is essential.

---

## Further reading


- Gregory, *Counterparty Credit Risk*.
- Basel III CVA guidance.

---

## Exercises

**Exercise 1.** Define wrong-way risk (WWR) and right-way risk (RWR). For each of the following transactions, determine whether the exposure exhibits WWR or RWR from the perspective of the bank: (a) an interest rate swap where the counterparty benefits from falling rates and is a leveraged firm that suffers in recessions, (b) a put option sold to a gold mining company with the underlying being gold, (c) a CDS where the bank buys protection on a reference entity that is highly correlated with the protection seller.

??? success "Solution to Exercise 1"

    **Definitions:**

    **Wrong-way risk (WWR)** occurs when a bank's exposure to a counterparty is positively correlated with the counterparty's probability of default. In other words, the amount the bank stands to lose increases precisely when the counterparty is most likely to fail.

    **Right-way risk (RWR)** is the opposite: the bank's exposure decreases as the counterparty's credit quality deteriorates. This is a favorable dependence structure that reduces credit risk.

    **Analysis of each transaction:**

    **(a) Interest rate swap — counterparty benefits from falling rates, is a leveraged firm hurt by recessions:**

    The bank pays floating and receives fixed (so the counterparty pays fixed and receives floating). When rates fall:

    - The swap becomes more valuable *to the bank* (receiving above-market fixed rate), so the bank's **exposure increases**.
    - Falling rates typically accompany recessions. The leveraged counterparty suffers in recessions, so its **default probability increases**.

    Since exposure and default probability both increase in the same economic scenario, this is **wrong-way risk**.

    **(b) Put option sold to a gold mining company, underlying is gold:**

    The bank sold a put option on gold to a gold mining company. When the gold price falls:

    - The put option becomes more valuable to the mining company (it can sell gold above market), so the bank's **exposure increases** (the bank owes more on the put).
    - A gold mining company's revenues and creditworthiness *decline* when gold prices fall, so its **default probability increases**.

    However, here the bank owes money to the counterparty (the bank sold the put), so the relevant question is about the counterparty's exposure to the bank, not the bank's exposure to the counterparty. From the bank's perspective as the option seller, if the counterparty defaults, the bank is *relieved* of its obligation. The bank's counterparty credit risk comes from other positions.

    But if we consider the *counterparty's* credit risk to the bank: when gold falls, the counterparty owes less to the bank (the put is in-the-money for the counterparty, meaning the bank pays), so the bank's credit exposure to the counterparty actually *decreases*. Meanwhile, the counterparty's credit quality worsens. Exposure decreases while default probability increases — this is **right-way risk** from the bank's perspective.

    More precisely: the bank has sold the put, so the bank has no positive exposure to the counterparty from this trade (it is the counterparty that has exposure to the bank). If we reframe: the bank has *negative* mark-to-market when gold falls, meaning the counterparty is owed money. The bank's credit risk (that the counterparty defaults owing the bank money) only materializes when gold rises (put is out-of-the-money, and the bank paid a premium). When gold rises, the mining company is doing well (lower default probability). So this is **right-way risk**.

    **(c) CDS where the bank buys protection on a reference entity highly correlated with the protection seller:**

    The bank buys CDS protection. When the reference entity's credit deteriorates:

    - The CDS becomes more valuable to the bank (protection is worth more), so the bank's **exposure to the protection seller increases**.
    - Because the reference entity is highly correlated with the protection seller, the protection seller's **default probability also increases**.

    The bank's exposure increases precisely when the protection seller is most likely to default — this is textbook **wrong-way risk**. This is exactly the situation that occurred with AIG selling CDS protection on mortgage-related CDOs during the 2008 crisis.

---

**Exercise 2.** In a standard CVA calculation, exposure and default probability are assumed independent:

$$
\text{CVA} = (1 - R)\int_0^T \text{EE}(t)\,dP(\tau \le t)
$$

Explain why this formula underestimates CVA when wrong-way risk is present. Propose a modified formula that accounts for positive dependence between exposure and default probability.

??? success "Solution to Exercise 2"

    **The standard CVA formula:**

    $$
    \text{CVA} = (1 - R)\int_0^T \text{EE}(t)\,dP(\tau \le t)
    $$

    Here $\text{EE}(t) = E[\max(V(t), 0)]$ is the expected positive exposure at time $t$, $P(\tau \le t)$ is the counterparty's default probability, and $R$ is the recovery rate. Crucially, this formula computes exposure and default probability *separately* and multiplies them — implicitly assuming **independence**.

    **Why this underestimates CVA under wrong-way risk:**

    The true CVA should be:

    $$
    \text{CVA}_{\text{true}} = (1 - R)\int_0^T E\left[\max(V(t), 0) \mid \tau = t\right]\,dP(\tau \le t)
    $$

    The key difference is the *conditional* expectation $E[V(t)^+ \mid \tau = t]$ — the expected exposure *given that the counterparty defaults at time $t$*. Under wrong-way risk, this conditional expectation exceeds the unconditional one:

    $$
    E[\max(V(t), 0) \mid \tau = t] > E[\max(V(t), 0)] = \text{EE}(t)
    $$

    because default occurs in adverse market states where exposure is high. The standard formula substitutes $\text{EE}(t)$ for $E[V(t)^+ \mid \tau = t]$, systematically understating the loss.

    **Modified formula accounting for WWR:**

    A general WWR-adjusted CVA replaces the independent product with a joint expectation:

    $$
    \text{CVA}_{\text{WWR}} = (1 - R)\int_0^T E\!\left[\max(V(t), 0) \mid \tau = t\right] dP(\tau \le t)
    $$

    In practice, this can be implemented by:

    1. **Joint simulation approach**: Simulate market factors and default times from a joint model (e.g., correlated diffusions for exposure and default intensity):

        $$
        \text{CVA}_{\text{WWR}} = (1 - R)\,E\!\left[\mathbf{1}_{\{\tau \le T\}}\,D(\tau)\,\max(V(\tau), 0)\right]
        $$

        where $D(\tau)$ is the discount factor.

    2. **Multiplier approach** (simpler): Apply a WWR adjustment factor $\alpha(t) > 1$:

        $$
        \text{CVA}_{\text{WWR}} \approx (1 - R)\int_0^T \alpha(t)\,\text{EE}(t)\,dP(\tau \le t)
        $$

        where $\alpha(t)$ is calibrated to stressed scenarios or estimated from the correlation between exposure and credit spreads.

    3. **Copula approach**: Model the joint distribution of exposure $V(t)$ and default time $\tau$ using a copula, and compute the conditional expectation analytically or numerically.

---

**Exercise 3.** A bank has an FX forward with a counterparty in an emerging market. The counterparty receives USD and pays local currency. Explain why this trade exhibits wrong-way risk: if the local currency depreciates significantly, both the bank's exposure and the counterparty's default probability increase simultaneously.

??? success "Solution to Exercise 3"

    **Setting:** A bank enters an FX forward where it will receive local currency and pay USD to an emerging market counterparty. Equivalently, the counterparty receives USD and pays local currency.

    **Why this exhibits wrong-way risk:**

    Consider the scenario where the emerging market local currency depreciates significantly against the USD.

    **Effect on exposure:** The FX forward requires the counterparty to deliver local currency and receive USD. From the bank's perspective, the bank will deliver USD and receive local currency. If the local currency depreciates:

    - The bank's position (receiving local currency) loses value — the local currency the bank will receive is worth less in USD terms.
    - The counterparty's position (receiving USD) gains value — the USD the counterparty will receive is worth more in local currency terms.
    - The mark-to-market of the forward becomes *positive for the counterparty and negative for the bank*.

    Actually, let us re-examine the direction. The counterparty receives USD and pays local currency. From the bank's perspective, the bank receives local currency and pays USD.

    When the local currency depreciates:

    - The forward to receive USD (counterparty's side) is in-the-money for the counterparty.
    - The forward to receive local currency (bank's side) is out-of-the-money for the bank.

    So the bank has *negative* mark-to-market — the bank owes the counterparty. In this case, the bank does not have credit exposure to the counterparty (the counterparty has exposure to the bank).

    **Corrected analysis:** The question states the counterparty receives USD and pays local currency. For the bank to have wrong-way risk, the bank should be on the side that benefits when the local currency depreciates — i.e., the bank receives USD. But the setup says the counterparty receives USD.

    Let us reconsider: if the *bank* is receiving USD and paying local currency (so the counterparty pays USD and receives local currency), and the local currency depreciates:

    - The bank's forward (pay local currency, receive USD) is in-the-money for the bank — **bank's exposure to the counterparty increases**.
    - The emerging market counterparty is weakened by local currency depreciation: their revenues are in local currency, their USD-denominated debts become more burdensome, and capital flight worsens funding — **counterparty's default probability increases**.

    This is **wrong-way risk**: the bank's exposure and the counterparty's default probability move together.

    **The economic mechanism in detail:**

    Emerging market currency depreciation typically reflects or causes:

    1. **Capital outflows** that drain the counterparty's funding sources.
    2. **Rising USD-denominated debt burden** — many EM firms borrow in USD, and depreciation increases the local-currency cost of servicing this debt.
    3. **Central bank rate hikes** to defend the currency, which tighten financial conditions and increase corporate stress.
    4. **Imported inflation** that squeezes margins.

    All of these channels simultaneously increase the bank's mark-to-market exposure (the USD the bank is owed becomes more valuable in local currency terms) and increase the counterparty's probability of default. The correlation between these two effects is strongly positive, making this a classic example of wrong-way risk in FX derivatives with EM counterparties.

---

**Exercise 4.** Describe two approaches for modeling wrong-way risk: (a) explicitly correlating exposure and default intensity using a joint stochastic model, and (b) using stressed exposure profiles in the CVA calculation. Discuss the trade-offs between accuracy and tractability.

??? success "Solution to Exercise 4"

    **Approach (a): Explicit joint stochastic model**

    *Description*: Model exposure $V(t)$ and default intensity $\lambda(t)$ as correlated stochastic processes. For example:

    $$
    dV(t) = \mu_V\,dt + \sigma_V\,dW_1(t)
    $$

    $$
    d\lambda(t) = \kappa(\theta - \lambda(t))\,dt + \sigma_\lambda\sqrt{\lambda(t)}\,dW_2(t)
    $$

    with $\text{Corr}(dW_1, dW_2) = \rho_{VD}$. A positive $\rho_{VD}$ captures wrong-way risk: when exposure rises, default intensity also tends to rise.

    CVA is computed via joint Monte Carlo simulation:

    $$
    \text{CVA} = (1-R)\,E\!\left[\int_0^T D(t)\,\max(V(t), 0)\,\lambda(t)\,e^{-\int_0^t \lambda(s)\,ds}\,dt\right]
    $$

    *Advantages*:

    - Captures the full dependence structure between exposure and default.
    - Flexible: the correlation parameter $\rho_{VD}$ can be calibrated or stress-tested.
    - Produces a complete distribution of CVA, not just a point estimate.
    - Can model nonlinear dependence through more sophisticated factor structures.

    *Limitations*:

    - Computationally expensive: requires joint simulation of market factors and credit dynamics.
    - Calibration is difficult: the correlation $\rho_{VD}$ between exposure and default intensity is not directly observable.
    - Model risk: the choice of joint dynamics (Gaussian, jump-diffusion, etc.) is consequential but hard to validate.
    - Requires careful treatment of the measure (risk-neutral vs. physical) for both components.

    **Approach (b): Stressed exposure profiles**

    *Description*: Instead of modeling dependence explicitly, replace the expected exposure $\text{EE}(t)$ in the standard CVA formula with a stressed exposure profile $\text{EE}_{\text{stress}}(t)$, computed under adverse market scenarios that are consistent with the counterparty defaulting:

    $$
    \text{CVA}_{\text{stressed}} = (1-R)\int_0^T \text{EE}_{\text{stress}}(t)\,dP(\tau \le t)
    $$

    The stressed exposure is typically computed by:

    - Shifting market factors (interest rates, FX rates, spreads) to adverse levels.
    - Using the $97.5\%$ percentile of exposure instead of the mean.
    - Applying regulatory multipliers ($\alpha > 1$).

    *Advantages*:

    - Simple to implement within existing CVA infrastructure.
    - Does not require specifying a joint model — avoids model risk from misspecified dependence.
    - Transparent and easy to explain to management and regulators.
    - Computationally cheap: uses existing exposure simulations with stressed inputs.

    *Limitations*:

    - Ad hoc: the choice of stress level is subjective and may not correspond to actual WWR dependence.
    - May be too conservative or too lenient depending on the stress scenario.
    - Does not capture the dynamic interaction between exposure and credit quality.
    - Cannot distinguish between different WWR intensities across trades or counterparties.
    - Produces a point estimate, not a distribution.

    **Trade-off summary:** Approach (a) is more accurate and theoretically sound but operationally demanding. Approach (b) is pragmatic and robust to model misspecification but lacks precision. In practice, many banks use (b) as a baseline with (a) for material wrong-way risk exposures, combining pragmatism with rigor where it matters most.

---

**Exercise 5.** Regulatory frameworks (e.g., Basel III) require banks to account for wrong-way risk in their CVA calculations. Describe the "alpha multiplier" approach used in regulatory CVA and explain why regulators set $\alpha > 1$ to penalize banks for potential wrong-way risk.

??? success "Solution to Exercise 5"

    **The alpha multiplier approach in regulatory CVA:**

    Under Basel III (and the subsequent SA-CVA and BA-CVA frameworks), banks must compute a regulatory CVA capital charge. The framework recognizes that standard CVA calculations, which assume independence between exposure and default, may underestimate true credit risk.

    **How the alpha multiplier works:**

    The regulatory effective EPE (Expected Positive Exposure) is computed as:

    $$
    \text{Effective EPE}_{\text{reg}} = \alpha \times \text{Effective EPE}
    $$

    where $\alpha \ge 1$ is a multiplier that inflates the exposure measure to account for model limitations, including wrong-way risk. Under Basel III:

    - The **regulatory floor** is $\alpha = 1.4$ for banks using the Internal Model Method (IMM).
    - Banks may compute their own $\alpha$ using internal models, subject to supervisory approval, but it cannot fall below 1.2.
    - For banks that do not model WWR explicitly, $\alpha = 1.4$ serves as a blanket conservatism factor.

    **Why regulators set $\alpha > 1$:**

    1. **Wrong-way risk compensation**: The standard EPE calculation assumes independence between exposure and counterparty credit quality. Since wrong-way risk is present in many common trade types (FX derivatives with EM counterparties, interest rate swaps with leveraged firms, etc.), $\alpha > 1$ provides a systematic upward adjustment.

    2. **Model risk buffer**: Even models that attempt to capture WWR may underestimate it due to misspecified dependence structures, calibration errors, or insufficient tail modeling. The multiplier provides a regulatory cushion.

    3. **Granularity and concentration**: The standard EPE may underestimate risk in concentrated portfolios where a few large counterparties dominate. The alpha multiplier partially compensates for this.

    4. **Procyclicality mitigation**: Standard CVA models may produce low estimates during benign periods (when correlations are low), precisely when capital buffers should be building. The multiplier ensures a minimum conservatism level.

    5. **Simplicity and consistency**: Rather than requiring every bank to model WWR explicitly (which introduces additional model risk), the alpha multiplier provides a simple, universal adjustment that ensures a baseline level of conservatism across the banking system.

    The alpha multiplier is a pragmatic regulatory tool — it is admittedly crude, but it serves the important function of ensuring that banks hold capital against a risk (WWR) that is difficult to model precisely and that manifests most severely during exactly the periods when models are least reliable.

---

**Exercise 6.** A portfolio of credit default swaps has wrong-way risk because the protection sellers are themselves financial institutions whose creditworthiness deteriorates during credit crises. Explain how this feedback mechanism amplified losses during the 2008 financial crisis. What risk management practices could mitigate this systemic wrong-way risk?

??? success "Solution to Exercise 6"

    **The feedback mechanism during the 2008 crisis:**

    The CDS market exhibited a particularly dangerous form of systemic wrong-way risk because protection sellers were themselves financial institutions — banks, insurance companies (notably AIG), and monoline insurers — whose creditworthiness was correlated with the risks they were insuring against.

    **The amplification cycle operated as follows:**

    **Phase 1 — Initial credit deterioration:** As mortgage defaults rose in 2007--2008, the value of mortgage-backed securities and CDO tranches declined. Banks that held these securities suffered losses.

    **Phase 2 — CDS exposure increases:** Banks that had purchased CDS protection on mortgage-related reference entities saw their CDS positions become more valuable (in-the-money). Their exposure to the CDS protection sellers increased.

    **Phase 3 — Protection seller stress:** The protection sellers (AIG, monolines, other banks) faced massive potential payouts on the CDS they had written. Their creditworthiness deteriorated as the market recognized these growing liabilities.

    **Phase 4 — Collateral calls and liquidity drain:** As protection sellers' credit quality declined, their counterparties demanded additional collateral (per CSA agreements). This drained liquidity from already-stressed institutions, further weakening them.

    **Phase 5 — Feedback and contagion:** The weakening of protection sellers raised questions about whether CDS protection was actually reliable. Banks that had hedged their credit risk through CDS realized their hedges might not pay off — the hedging instrument was correlated with the risk being hedged. This "gap risk" in CDS hedging triggered further selling and deleveraging.

    **The AIG example:** AIG Financial Products had sold approximately \$440 billion in CDS protection, much of it on CDOs containing subprime mortgages. As CDO values fell:

    - AIG's exposure to potential payouts grew enormously.
    - AIG's credit rating was downgraded, triggering collateral calls.
    - AIG could not meet collateral demands, threatening a cascade of defaults across all its counterparties.
    - The US government intervened with an \$85 billion bailout (eventually \$182 billion) specifically because AIG's failure would have imposed massive wrong-way risk losses on the entire banking system.

    **Risk management practices to mitigate systemic wrong-way risk:**

    1. **Counterparty diversification for hedges:** Do not concentrate CDS protection purchases with a small number of sellers. Diversify across counterparties with different risk profiles and business models. Avoid buying protection from entities that are themselves exposed to the same risks.

    2. **Central clearing and margin requirements:** Require CDS to be cleared through central counterparties (CCPs) that impose initial and variation margins. This was a key post-crisis reform (Dodd-Frank, EMIR) that reduces bilateral counterparty risk and forces more transparent collateralization.

    3. **Wrong-way risk limits:** Establish explicit limits on wrong-way risk exposure — the maximum notional of CDS protection that can be purchased from counterparties with high correlation to the reference entity. Flag trades where the protection seller's credit is fundamentally linked to the insured risk.

    4. **Stress testing with joint defaults:** Run stress scenarios where protection sellers default simultaneously with the reference entities. Compute the unhedged loss in these scenarios and ensure capital reserves cover it. This "jump-to-default" analysis reveals the true residual risk after accounting for hedge failure.

    5. **Structural reforms:** Require CDS protection sellers to hold adequate capital against their contingent liabilities (which was not the case for AIG). Mandate skin-in-the-game: if an institution sells CDS protection, it must demonstrate the capacity to pay under stressed conditions, not just expected conditions.
