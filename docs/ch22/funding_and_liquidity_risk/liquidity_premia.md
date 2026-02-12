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

**Bid-ask spread:**
$$
\text{Spread} = P^{\text{ask}} - P^{\text{bid}}
$$

**Relative spread:**
$$
\text{Relative Spread} = \frac{P^{\text{ask}} - P^{\text{bid}}}{P^{\text{mid}}}
$$

**Amihud illiquidity measure:**
$$
\text{ILLIQ} = \frac{1}{D} \sum_{d=1}^D \frac{|r_d|}{V_d}
$$

where $r_d$ is the return and $V_d$ is dollar volume on day $d$.

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

**Brunnermeier-Pedersen (2009):**

1. Negative shock → Asset prices fall
2. → Margin calls → Forced selling
3. → Further price decline → Reduced market liquidity
4. → Wider funding spreads → Reduced funding liquidity
5. → Back to step 2...

**Feedback loop between market liquidity and funding liquidity.**

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
