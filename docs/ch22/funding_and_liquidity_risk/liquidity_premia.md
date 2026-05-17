# Liquidity Premia

**Liquidity premia** compensate investors for the cost and risk of trading assets that cannot be bought or sold quickly without significant price impact. Understanding liquidity premia is essential for accurate valuation and risk management.

---

## What Is Liquidity?

### Dimensions of Liquidity

**1. Immediacy:** How quickly can a trade be executed?

**2. Depth:** How large a trade can be executed without moving the price?

**3. Resilience:** How quickly do prices recover after a large trade?

**4. Tightness:** How narrow is the bid-ask spread?

### Illiquidity Measures

Recall (see [§ Market Impact](market_impact.md)) for bid-ask spread, the Amihud illiquidity measure $\text{ILLIQ}=\frac{1}{D}\sum_d |r_d|/V_d$, and the connection to Kyle's $\lambda$.

---

## Liquidity Premium in Prices

### Definition

The **liquidity premium** is the additional expected return required to hold illiquid assets:

$$
\mathbb{E}[R_{\text{illiquid}}] = \mathbb{E}[R_{\text{liquid}}] + \text{Liquidity Premium}
$$

Equivalently, illiquid assets trade at a **discount**:

$$
P_{\text{illiquid}} = P_{\text{liquid}} - \text{Liquidity Discount}
$$

### Sources

1. **Transaction costs:** Direct trading costs reduce net returns
2. **Search costs:** Time and effort to find counterparties
3. **Inventory risk:** Market makers require compensation
4. **Asymmetric information:** Adverse selection from informed traders
5. **Funding constraints:** Illiquid assets harder to repo/pledge

---

## Liquidity-Adjusted CAPM

### Acharya-Pedersen Model

Extends CAPM to include liquidity:

$$
\mathbb{E}[R_i] - R_f = \beta_1 \cdot \lambda_{\text{mkt}} + \beta_2 \cdot \lambda_{\text{liq}}
$$

where:

- $\beta_1$ = market beta
- $\beta_2$ = liquidity beta
- $\lambda_{\text{mkt}}$ = market risk premium
- $\lambda_{\text{liq}}$ = liquidity risk premium

### Liquidity Beta Components

**Commonality in liquidity:** Asset illiquidity correlated with market illiquidity.

**Return sensitivity:** Returns fall when market becomes illiquid.

**Liquidity sensitivity:** Asset becomes illiquid when market falls.

---

## Liquidity Risk

### Flight to Liquidity

During stress:

- Investors flee to liquid assets (Treasuries, cash)
- Illiquid assets suffer disproportionate price declines
- Liquidity premia spike

### Liquidity Spirals

Recall (see [§ Funding Constraints](funding_constraints.md) and [§ Systemic Risk and Network Effects](../systemic_risk_and_network_effects/clearing_and_central_counterparties.md)) for the Brunnermeier-Pedersen feedback loop between market liquidity and funding liquidity.

---

## Liquidity Premium Estimates

### Corporate Bonds

**Longstaff, Mithal, Neis (2005):**

- Non-default component (largely liquidity): 50-100 bps for investment grade

**Dick-Nielsen, Feldhütter, Lando (2012):**

- Liquidity component: 20-50% of total spread
- Higher during crisis periods

### Treasury Securities

**On-the-run vs Off-the-run:**

- On-the-run: Most liquid
- Off-the-run: 5-30 bps yield premium

### CDS-Bond Basis

$$
\text{Basis} = \text{CDS Spread} - \text{Bond Spread}
$$

Negative basis often reflects bond illiquidity premium.

---

## Valuation Implications

### Liquidity Discount

$$
V_{\text{adjusted}} = V_{\text{liquid}} \times (1 - \text{Liquidity Discount})
$$

### Stress Liquidity Adjustment

$$
V_{\text{stressed}} = V_{\text{normal}} - \text{Liquidity Adjustment}_{\text{stress}}
$$

### Regulatory Treatment

IFRS 13 and ASC 820 require fair value hierarchy accounting for liquidity.

---

## Key Takeaways

- Liquidity premia compensate for trading frictions
- Premia are time-varying and spike during stress
- Flight to liquidity and liquidity spirals amplify crises
- Valuation should include liquidity adjustments
- Portfolio construction must balance return against liquidity needs

---

## Further Reading

- Amihud, Y. & Mendelson, H. (1986), "Asset Pricing and the Bid-Ask Spread"
- Acharya, V.V. & Pedersen, L.H. (2005), "Asset Pricing with Liquidity Risk"
- Brunnermeier, M.K. & Pedersen, L.H. (2009), "Market Liquidity and Funding Liquidity"

---

## Exercises

**Exercise 1.** Two bonds from the same issuer have identical credit risk but different maturities and liquidity. Bond A (on-the-run) has a yield of 4.5% and Bond B (off-the-run) yields 4.8%. Estimate the liquidity premium. What fraction of Bond B's credit spread (over Treasuries) is attributable to illiquidity?

??? success "Solution to Exercise 1"
    **Estimating the liquidity premium.**

    Bond A (on-the-run) yields 4.5% and Bond B (off-the-run) yields 4.8%. Since both bonds are from the same issuer, they have identical credit risk. The yield difference must therefore reflect the liquidity premium:

    $$
    \text{Liquidity Premium} = Y_B - Y_A = 4.8\% - 4.5\% = 30 \text{ bp}
    $$

    **Fraction of credit spread attributable to illiquidity:**

    Suppose the risk-free Treasury rate is $r_f$. The total spread of Bond B over Treasuries is:

    $$
    \text{Total Spread}_B = Y_B - r_f
    $$

    This total spread decomposes into credit risk and liquidity:

    $$
    \text{Total Spread}_B = \text{Credit Spread} + \text{Liquidity Premium}
    $$

    Since Bond A is liquid and from the same issuer, Bond A's spread over Treasuries approximates the pure credit spread (assuming on-the-run bonds have negligible liquidity premium):

    $$
    \text{Credit Spread} \approx Y_A - r_f = 4.5\% - r_f
    $$

    The fraction of Bond B's spread attributable to illiquidity is:

    $$
    \text{Liquidity Fraction} = \frac{30 \text{ bp}}{Y_B - r_f}
    $$

    For example, if $r_f = 3.5\%$, then Bond B's total spread is 130 bp, and:

    $$
    \text{Liquidity Fraction} = \frac{30}{130} \approx 23\%
    $$

    This is consistent with empirical estimates (Dick-Nielsen, Feldhutter, Lando 2012) that find the liquidity component is 20-50% of total corporate bond spreads. The fraction tends to be higher for lower-rated issuers and increases during stress periods.

---

**Exercise 2.** The Amihud illiquidity measure is $\text{ILLIQ} = \frac{1}{D}\sum_{d=1}^D \frac{|r_d|}{\text{Volume}_d}$, where $r_d$ is the daily return and $\text{Volume}_d$ is the daily trading volume. Explain the intuition behind this measure. Why does a higher value indicate greater illiquidity?

??? success "Solution to Exercise 2"
    **Intuition behind the Amihud illiquidity measure.**

    The Amihud measure is defined as:

    $$
    \text{ILLIQ} = \frac{1}{D}\sum_{d=1}^{D} \frac{|r_d|}{\text{Volume}_d}
    $$

    **Interpretation:** The ratio $|r_d|/\text{Volume}_d$ measures the **absolute price change per unit of trading volume** on day $d$. It captures the price impact of trading: how much does the price move for each dollar of volume transacted?

    **Why a higher value indicates greater illiquidity:**

    1. **Price sensitivity to volume:** A high ratio means that even moderate trading volume causes large price movements. This is the hallmark of an illiquid market -- trades move prices significantly because the order book is thin (few limit orders at nearby prices).

    2. **Large numerator (high $|r_d|$):** If returns are large relative to volume, it suggests that trades carry significant information content or that the market lacks depth to absorb order flow without price impact.

    3. **Small denominator (low Volume$_d$):** Low trading volume directly indicates illiquidity -- few participants are willing to trade, so each trade has outsized impact.

    4. **Kyle's lambda connection:** In the Kyle (1985) model, the price impact parameter $\lambda$ relates the price change to order flow: $\Delta P = \lambda \cdot Q$. The Amihud measure is an empirical analog: $|r_d|/\text{Volume}_d$ estimates the price sensitivity to order flow, which is precisely what $\lambda$ captures.

    **Practical considerations:**

    - The measure is averaged over $D$ days to reduce noise from day-to-day variation.
    - It is easy to compute from publicly available data (daily returns and volume), making it widely used in empirical asset pricing.
    - However, it uses daily data and may miss intraday liquidity dynamics. It also does not distinguish between temporary and permanent price impact.

---

**Exercise 3.** During the 2008 crisis, the liquidity premium on corporate bonds widened from approximately 20 bp to over 200 bp. Explain the economic mechanism: why does liquidity dry up precisely when investors most need it? How does the Brunnermeier-Pedersen "liquidity spiral" model capture this phenomenon?

??? success "Solution to Exercise 3"
    **Why liquidity dries up when investors need it most.**

    **Economic mechanism:**

    The paradox that liquidity disappears during crises, precisely when it is most needed, arises from the interaction of several reinforcing channels:

    1. **Asymmetric information intensifies:** During crises, uncertainty about asset values increases dramatically. Market makers widen bid-ask spreads because they face greater adverse selection risk -- any counterparty willing to sell might possess negative private information. This is the Glosten-Milgrom (1985) mechanism: spreads widen to protect against informed traders.

    2. **Inventory risk increases:** Market makers and dealers hold inventory to provide liquidity. When volatility spikes, the risk of holding inventory rises, causing dealers to reduce their willingness to warehouse positions. Balance sheet constraints tighten simultaneously, limiting dealers' capacity.

    3. **Funding constraints bind:** Institutions that normally provide liquidity (hedge funds, proprietary trading desks) rely on leverage. During stress, their funding becomes more expensive or unavailable, forcing them to reduce positions rather than absorb selling pressure.

    4. **Forced selling creates one-sided markets:** Margin calls, stop-loss triggers, and regulatory constraints force institutions to sell, creating an excess of sellers over buyers. Market-clearing requires large price concessions.

    **The Brunnermeier-Pedersen liquidity spiral model:**

    The model formalizes the feedback loop between **market liquidity** (the ease of trading) and **funding liquidity** (the ease of financing positions):

    1. **Negative shock** causes asset prices to fall.
    2. **Margin calls:** Leveraged investors face increased margin requirements (both because of losses reducing equity and because margins increase with volatility). They must either post more collateral or reduce positions.
    3. **Forced selling:** Investors who cannot meet margin calls are forced to sell, further depressing prices and reducing market liquidity.
    4. **Funding liquidity tightens:** As asset prices fall, the collateral value of remaining positions declines, reducing available funding. Lenders raise haircuts, further reducing leverage capacity.
    5. **Feedback loop:** Steps 2-4 reinforce each other. Market illiquidity (wider spreads, lower depth) increases the cost of forced liquidation. Funding illiquidity (higher haircuts, reduced credit lines) forces more liquidation. The two forms of liquidity feed on each other in a downward spiral.

    The model explains why the liquidity premium widened from 20 bp to over 200 bp during 2008: the spiral was fully engaged, with institutions simultaneously deleveraging across asset classes, and the normal providers of liquidity were themselves capital-constrained.

---

**Exercise 4.** An investor holds a portfolio of illiquid corporate bonds and marks them to model rather than to market. Explain the risks of this approach. How should the investor adjust the model price to account for the liquidity premium?

??? success "Solution to Exercise 4"
    **Risks of marking illiquid bonds to model rather than to market.**

    **Risks of mark-to-model:**

    1. **Stale valuations:** Model prices may not reflect current market conditions. If the model uses historical parameters (credit spreads, recovery rates, default probabilities), the mark may lag reality significantly during fast-moving markets.

    2. **Underestimation of losses:** If the model does not incorporate the liquidity discount, the reported portfolio value overstates what the investor would actually receive upon sale. This creates a gap between paper value and realizable value.

    3. **Risk measure distortion:** Risk metrics (VaR, ES) computed from model prices understate true risk because they ignore the additional loss that would occur from liquidating at distressed prices.

    4. **Incentive problems:** Traders or portfolio managers may have incentives to choose model parameters that produce favorable valuations, leading to systematic overvaluation (the "mark-to-myth" problem).

    5. **Cliff risk:** When model marks eventually converge to reality (e.g., when the investor must sell or when an auditor intervenes), the adjustment can be sudden and large, creating unexpected losses.

    **How to adjust the model price for the liquidity premium:**

    The investor should apply a liquidity valuation adjustment (LVA):

    $$
    V_{\text{adjusted}} = V_{\text{model}} - \text{LVA}
    $$

    The LVA can be estimated through several approaches:

    **Approach 1 -- Bid-ask spread adjustment:**

    $$
    \text{LVA} = \frac{1}{2} \cdot \text{Bid-Ask Spread} \cdot \text{Notional}
    $$

    Use the mid-to-bid adjustment for sell-side valuations.

    **Approach 2 -- Comparable liquid instrument:**

    If a liquid bond from the same issuer exists:

    $$
    \text{LVA} = (Y_{\text{illiquid}} - Y_{\text{liquid}}) \times \text{Duration} \times \text{Notional}
    $$

    **Approach 3 -- Stress-adjusted discount:**

    Apply a stressed liquidity premium that accounts for the time required to liquidate:

    $$
    \text{LVA} = V_{\text{model}} \times \left(1 - e^{-s_L \cdot T_{\text{liq}}}\right)
    $$

    where $s_L$ is the liquidity spread and $T_{\text{liq}}$ is the estimated time to liquidate.

    The investor should also report a range of valuations (e.g., mark-to-model, mark-to-model with normal liquidity discount, and mark-to-model with stressed liquidity discount) to convey the uncertainty inherent in illiquid bond valuations.

---

**Exercise 5.** Compare the liquidity premium in corporate bond markets with the liquidity premium in CDS markets. Which market is typically more liquid, and why? How does the CDS-bond basis reflect differences in liquidity premia?

??? success "Solution to Exercise 5"
    **Liquidity premium comparison: corporate bonds versus CDS.**

    **Which market is more liquid?**

    CDS markets are generally **more liquid** than corporate bond markets for several reasons:

    1. **Standardization:** CDS contracts are highly standardized (fixed coupons of 100 bp or 500 bp, standard maturities, ISDA documentation). Corporate bonds come in many different maturities, coupons, covenants, and embedded options, fragmenting liquidity.

    2. **No inventory constraint:** Selling protection via CDS does not require owning the underlying bond. This means CDS liquidity is not constrained by the finite supply of bonds outstanding.

    3. **Leverage efficiency:** CDS require only margin (no full principal investment), making them more capital-efficient for expressing credit views. This attracts more participants and trading activity.

    4. **Dealer intermediation:** Dealers can warehouse CDS risk more efficiently because netting and compression reduce net exposures. Bond inventory ties up balance sheet.

    5. **Price discovery:** CDS spreads often react faster to credit events and new information, serving as the primary venue for price discovery.

    **However, CDS liquidity has its own limitations:**

    - Concentrated in a smaller number of reference entities (mainly large, investment-grade names and sovereign issuers)
    - Liquidity can evaporate for specific names during idiosyncratic stress
    - Post-crisis regulation (clearing mandates, margin requirements) has increased costs

    **The CDS-bond basis and liquidity premia:**

    The CDS-bond basis is defined as:

    $$
    \text{Basis} = \text{CDS Spread} - \text{Bond Spread (z-spread or ASW spread)}
    $$

    In theory, under no-arbitrage, the basis should be zero (or close to zero after accounting for technical differences). In practice:

    - **Negative basis** (CDS spread < bond spread): The bond yield includes a liquidity premium that is not present in the CDS. This is the most common situation, reflecting the fact that bonds are less liquid than CDS. The bond holder demands extra yield to compensate for the difficulty of selling the bond.

    - **Positive basis** (CDS spread > bond spread): Can occur when there is strong demand for credit protection (e.g., during a credit crisis), when the cheapest-to-deliver option in CDS has value, or when bond prices are supported by structural demand (e.g., from insurance companies).

    During the 2008 crisis, the CDS-bond basis became extremely negative (reaching -200 bp or more for some investment-grade issuers), primarily reflecting the enormous liquidity premium on corporate bonds. Even though the arbitrage was "obvious" (buy the cheap bond, buy CDS protection), it could not be exploited because of funding constraints: the trade required balance sheet capacity and funding that was unavailable during the crisis.

---

**Exercise 6.** Describe how liquidity risk enters a risk management framework. Should the risk manager use a standard VaR/ES measure, or does liquidity risk require a separate treatment (e.g., Liquidity-adjusted VaR)? Explain the adjustments needed to account for the time required to liquidate positions.

??? success "Solution to Exercise 6"
    **Liquidity risk in a risk management framework.**

    **Standard VaR/ES limitations:**

    Standard Value-at-Risk (VaR) and Expected Shortfall (ES) measures typically assume:

    - Positions can be liquidated at mid-market prices
    - Liquidation occurs instantaneously (or within a fixed holding period, typically 1 or 10 days)
    - Market impact of liquidation is negligible

    These assumptions break down for illiquid positions, leading to **underestimation of true risk**.

    **Why liquidity risk requires separate treatment:**

    Liquidity risk has features that standard VaR/ES cannot capture:

    1. **Endogenous risk:** Market impact depends on the institution's own positions and actions, not just on exogenous market movements.
    2. **Asymmetry:** Liquidity typically deteriorates during losses (when liquidation is most needed), creating tail dependence between market risk and liquidity risk.
    3. **Non-linearity:** Liquidation costs scale nonlinearly with position size (square-root law), so doubling a position more than doubles the liquidity risk.

    **Liquidity-Adjusted VaR (LVaR):**

    The standard approach adjusts VaR for liquidation costs:

    $$
    \text{LVaR} = \text{VaR} + \text{Liquidation Cost Adjustment}
    $$

    **Adjustment 1 -- Bid-ask spread (exogenous liquidity cost):**

    $$
    \text{LVaR} = \text{VaR} + \frac{1}{2} \sum_i |w_i| \cdot (\bar{s}_i + k \cdot \sigma_{s_i})
    $$

    where $\bar{s}_i$ is the average spread for asset $i$, $\sigma_{s_i}$ is the spread volatility, and $k$ is a confidence multiplier.

    **Adjustment 2 -- Holding period extension (time-to-liquidate):**

    If liquidating asset $i$ takes $T_i$ days instead of the standard $h$ days:

    $$
    \text{LVaR}_i = \text{VaR}_i \cdot \sqrt{\frac{T_i}{h}}
    $$

    This scales the VaR by the square root of the actual liquidation horizon. For a portfolio:

    $$
    \text{LVaR} = \sqrt{\sum_i \text{LVaR}_i^2 + 2\sum_{i<j} \rho_{ij} \cdot \text{LVaR}_i \cdot \text{LVaR}_j}
    $$

    **Adjustment 3 -- Market impact cost (endogenous liquidity cost):**

    Using the square-root impact model:

    $$
    \text{Impact Cost}_i = \sigma_i \cdot \sqrt{\frac{Q_i}{V_i}} \cdot P_i \cdot Q_i
    $$

    where $Q_i$ is the position size, $V_i$ is average daily volume, and $P_i$ is the price. This is added to VaR.

    **Recommended framework:**

    A comprehensive approach should:

    1. Compute standard VaR/ES for market risk.
    2. Add exogenous liquidity cost (half-spread adjusted for stress).
    3. Extend holding periods for illiquid positions (using realistic liquidation times).
    4. Add endogenous market impact costs for concentrated positions.
    5. Stress test the liquidity adjustments by using crisis-period parameters (wider spreads, lower volumes, higher volatility).
    6. Report both the standard and liquidity-adjusted risk measures to highlight the liquidity gap.
