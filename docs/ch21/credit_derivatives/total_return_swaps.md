# Total Return Swaps

A **Total Return Swap (TRS)** is a bilateral derivative contract in which one party transfers the **total economic performance** of a reference asset (including both income and capital gains or losses) to the other party, in exchange for a periodic funding payment. Unlike a CDS, which isolates default risk, a TRS transfers **all market risks**---credit, interest rate, and liquidity---making it a versatile tool for synthetic asset exposure and off-balance-sheet financing.

---

## Contract Structure

### Parties and Roles

- **Total return payer (TR payer):** Holds (or references) the asset; pays total return to receiver
- **Total return receiver (TR receiver):** Receives total return; pays a funding leg
- **Reference asset:** Typically a bond, loan, or credit index

### Cash Flows

**Total return leg (paid by TR payer to TR receiver):**

1. **Coupon payments:** All interest or coupon income from the reference asset
2. **Capital appreciation:** Any increase in market value of the reference asset at reset dates or maturity

**Funding leg (paid by TR receiver to TR payer):**

1. **Funding rate:** A floating rate (typically SOFR or EURIBOR) plus a spread $s_{\text{TRS}}$
2. **Capital depreciation:** Any decrease in market value passed to the TR receiver

### Net Payment at Reset

At each reset date $t_i$, the net payment is:

$$
\text{Net}_i = \underbrace{C_i + (P_{t_i} - P_{t_{i-1}})}_{\text{Total return}} - \underbrace{(L_{t_{i-1}} + s_{\text{TRS}}) \Delta_i \cdot N}_{\text{Funding payment}}
$$

where:

- $C_i$: coupon payment during period $(t_{i-1}, t_i]$
- $P_{t_i}$: market value of the reference asset at $t_i$
- $L_{t_{i-1}}$: floating rate set at $t_{i-1}$
- $s_{\text{TRS}}$: TRS spread
- $\Delta_i$: accrual fraction
- $N$: notional amount

If net is positive, TR payer pays TR receiver; if negative, TR receiver pays TR payer.

---

## Economic Analysis

### Synthetic Ownership

The TR receiver obtains the **economic equivalent** of owning the reference asset without actually purchasing it:

| Cash Flow | Physical Ownership | TRS Receiver |
|-----------|-------------------|-------------|
| Coupon income | Receives directly | Receives via TRS |
| Price appreciation | Benefits directly | Receives via TRS |
| Price depreciation | Bears directly | Bears via TRS |
| Funding cost | Bond purchase price + financing | Pays $L + s_{\text{TRS}}$ |

### Funding Advantage

The TRS creates value when the TR receiver has a **higher funding cost** than the TR payer:

- If the TR receiver would borrow at $L + s_{\text{funding}}^{\text{receiver}}$ to buy the bond, and $s_{\text{TRS}} < s_{\text{funding}}^{\text{receiver}}$, the TRS provides cheaper synthetic exposure
- The TR payer (often a bank) funds at $L + s_{\text{funding}}^{\text{payer}}$ and earns the spread $s_{\text{TRS}} - s_{\text{funding}}^{\text{payer}} > 0$

### Off-Balance-Sheet Treatment

For the TR receiver, the TRS provides:

- No need to fund the purchase price of the reference asset
- Off-balance-sheet exposure (under certain accounting standards)
- Leverage: only margin/collateral is required, not the full notional

For the TR payer:

- Removes economic exposure while retaining legal ownership
- Regulatory capital relief (if the credit risk transfer is recognized)
- Continues to hold the asset on the balance sheet (useful for relationship banking)

---

## Pricing Framework

### Fair Value Condition

At inception, the TRS spread $s_{\text{TRS}}$ is set so that the contract has zero initial value:

$$
\text{PV(Total Return Leg)} = \text{PV(Funding Leg)}
$$

### Present Value of Total Return Leg

$$
\text{PV}_{\text{TR}} = \sum_{i=1}^n \mathbb{E}^{\mathbb{Q}}\left[D(0,t_i)\left(C_i + P_{t_i} - P_{t_{i-1}}\right)\right]
$$

This telescopes:

$$
\text{PV}_{\text{TR}} = \sum_{i=1}^n \mathbb{E}^{\mathbb{Q}}[D(0,t_i) C_i] + \mathbb{E}^{\mathbb{Q}}[D(0,T) P_T] - P_0
$$

The first term is the PV of coupons, and the remaining terms capture the expected discounted capital gain.

### Present Value of Funding Leg

$$
\text{PV}_{\text{fund}} = s_{\text{TRS}} \sum_{i=1}^n \Delta_i \, \mathbb{E}^{\mathbb{Q}}[D(0,t_i)] \cdot N + \sum_{i=1}^n \mathbb{E}^{\mathbb{Q}}[D(0,t_i) L_{t_{i-1}} \Delta_i] \cdot N
$$

The floating rate component $\sum \mathbb{E}^{\mathbb{Q}}[D(0,t_i) L_{t_{i-1}} \Delta_i]$ equals $1 - P(0,T)$ (the PV of a floating rate note minus par) under standard assumptions.

### The TRS Spread

Equating the two legs and solving:

$$
s_{\text{TRS}} = \frac{\text{PV}_{\text{TR}} - N(1 - P(0,T))}{N \sum_{i=1}^n \Delta_i P(0,t_i)}
$$

### Replication Argument

The TRS can be replicated by:

1. **TR payer:** Buy the reference asset (funded at $L + s_{\text{payer}}$), enter TRS as payer
2. **TR receiver:** Enter TRS as receiver, invest cash at $L$

The fair TRS spread reflects the funding cost of carrying the reference asset:

$$
s_{\text{TRS}} = y_{\text{bond}} - L
$$

where $y_{\text{bond}}$ is the yield on the reference asset. If the bond trades at par, this is the bond's spread over the floating rate.

---

## Default and Termination

### Treatment at Default

If the reference entity defaults during the TRS term:

1. The TRS typically **terminates early**
2. The TR payer delivers the depreciated asset value:

$$
\text{Final settlement} = P_{\tau} - P_{\text{previous reset}}
$$

where $P_{\tau}$ is the post-default market value (typically $R \times \text{Face Value}$)

3. The TR receiver absorbs the capital loss
4. Any accrued funding payment is settled

### Comparison with CDS at Default

| Event | CDS | TRS |
|-------|-----|-----|
| Default payment | $(1-R) \times N$ | $P_{\text{previous}} - P_{\tau}$ |
| Pre-default value changes | Not covered | Fully covered |
| Interest rate risk | Not covered | Fully covered |
| Early termination | Contract continues (premium stops) | Contract terminates |

The TRS transfers **total risk** including market value fluctuations, while the CDS transfers only **default risk**.

---

## Credit Exposure Analysis

### Counterparty Risk

Both parties face counterparty risk:

**TR payer's exposure to TR receiver:**

- If the reference asset depreciates and the TR receiver cannot pay, the TR payer bears the loss
- Exposure is: $\max(P_{t_{i-1}} - P_{t_i}, 0)$ at each reset

**TR receiver's exposure to TR payer:**

- If the reference asset appreciates and the TR payer cannot pay, the TR receiver loses the gain
- Exposure is: $\max(P_{t_i} - P_{t_{i-1}}, 0)$ at each reset

### Wrong-Way Risk

The TRS exhibits **wrong-way risk** for the TR payer:

- If the reference entity's credit deteriorates, the reference asset depreciates
- The TR receiver owes a larger payment to the TR payer
- But credit deterioration also affects the TR receiver's ability to pay

This positive correlation between exposure and counterparty credit quality is a form of wrong-way risk.

### Collateral and Margining

To mitigate counterparty risk:

- Daily or weekly mark-to-market with collateral posting
- Independent amount (initial margin) reflecting potential future exposure
- Threshold-based margining with minimum transfer amounts

---

## Mark-to-Market Valuation

### After Inception

The mark-to-market value of the TRS to the TR receiver at time $t$ is:

$$
\text{MTM}_t = \underbrace{(P_t - P_0)}_{\text{Capital gain/loss}} + \underbrace{\text{PV of remaining TR payments}}_{\text{Future total return}} - \underbrace{\text{PV of remaining funding payments}}_{\text{Future funding cost}}
$$

### Spread Changes

If the TRS spread moves from $s_{\text{old}}$ to $s_{\text{new}}$:

$$
\Delta \text{MTM} \approx -(s_{\text{new}} - s_{\text{old}}) \times N \times \text{Annuity}
$$

A widening of the TRS spread (higher funding cost) benefits the existing TR payer.

---

## Applications

### Synthetic Leverage

Hedge funds and other leveraged investors use TRS to obtain:

- Exposure to credit assets without balance sheet
- Leverage limited only by margin requirements
- Access to markets where direct investment is restricted

### Balance Sheet Management

Banks use TRS to:

- Remove credit exposure without selling assets (preserve client relationships)
- Achieve regulatory capital relief
- Manage loan portfolio concentration

### Relative Value Trading

Combining a TRS with other instruments:

- **TRS + CDS:** Isolate the funding component of a credit asset
- **TRS on bond vs TRS on loan:** Trade the bond-loan basis
- **TRS across maturities:** Express views on the term structure

---

## Numerical Example

**Setup:**

- Reference asset: 5-year corporate bond, face value \$10 million, coupon 5% semi-annual
- Current bond price: $P_0 = 98\%$ of face (\$9.8 million)
- TRS maturity: 1 year, quarterly resets
- Floating rate: SOFR = 4.2%
- TRS spread: $s_{\text{TRS}} = 80$ bp

**Quarterly cash flows (TR receiver's perspective):**

**Quarter 1:** Suppose bond price rises to 99%.

- Total return: Coupon $= 0.05/2 \times 10\text{M} = \$250{,}000$ (semi-annual, pro-rated = \$125,000) + Capital gain $= (0.99 - 0.98) \times 10\text{M} = \$100{,}000$
- Funding: $(0.042 + 0.008) \times 0.25 \times 10\text{M} = \$125{,}000$
- Net to TR receiver: $\$125{,}000 + \$100{,}000 - \$125{,}000 = \$100{,}000$

**Quarter 2:** Suppose bond price falls to 97%.

- Total return: Coupon = \$125,000 + Capital loss $= (0.97 - 0.99) \times 10\text{M} = -\$200{,}000$
- Funding: \$125,000
- Net to TR receiver: $\$125{,}000 - \$200{,}000 - \$125{,}000 = -\$200{,}000$

The TR receiver bears both the upside and downside of the reference asset, net of funding.

---

## TRS vs Other Credit Derivatives

| Feature | TRS | CDS | Credit-Linked Note |
|---------|-----|-----|-------------------|
| Risk transferred | All market risk | Default risk only | Default risk |
| Funding | Off-balance-sheet | Off-balance-sheet | Funded (investor buys note) |
| Interest rate risk | Transferred | Not transferred | Not transferred |
| Liquidity risk | Transferred | Not transferred | Not transferred |
| Typical users | Banks, hedge funds | Banks, asset managers | Retail, insurance |
| Settlement at default | Asset depreciation | $(1-R) \times N$ | Loss of principal |

---

## Key Takeaways

- A TRS transfers the total economic performance of a reference asset (income + capital gains/losses)
- The TR receiver obtains synthetic ownership; the TR payer retains legal ownership
- The TRS spread reflects the funding cost of carrying the reference asset
- At fair value: $s_{\text{TRS}} \approx y_{\text{bond}} - L$ (bond yield minus floating rate)
- Unlike a CDS, a TRS transfers all market risks, not just default risk
- Default triggers early termination with settlement based on depreciated asset value
- Wrong-way risk arises from correlation between reference asset depreciation and counterparty creditworthiness
- Applications include synthetic leverage, balance sheet management, and relative value trading

---

## Further Reading

- O'Kane, D. (2008). *Modelling Single-name and Multi-name Credit Derivatives*. Wiley, Chapter 3.
- Duffie, D., & Singleton, K. J. (2003). *Credit Risk: Pricing, Measurement, and Management*. Princeton University Press.
- Bomfim, A. N. (2005). *Understanding Credit Derivatives and Related Instruments*. Academic Press, Chapter 4.
- Gregory, J. (2010). *Counterparty Credit Risk*. Wiley, Chapter 8.

---

## Exercises

**Exercise 1.** A TRS is written on a corporate bond with face value \$10 million and a semi-annual coupon of 6%. The bond price at the start of the quarter is $P_0 = 101\%$. At the end of the quarter, the price is $P_1 = 99.5\%$. The floating rate is SOFR $= 4.5\%$ and the TRS spread is 60 bp. Compute the net cash flow to the TR receiver for this quarter.

??? success "Solution to Exercise 1"

    **Given:**

    - Face value: $N = \$10$ million
    - Semi-annual coupon: 6% (so annual coupon rate is 6%)
    - $P_0 = 101\%$ of face $= \$10{,}100{,}000$
    - $P_1 = 99.5\%$ of face $= \$9{,}950{,}000$
    - SOFR $= 4.5\%$, TRS spread $= 60$ bp $= 0.60\%$
    - Quarter length: $\Delta = 0.25$ years

    **Total return leg (received by TR receiver):**

    Coupon: The bond pays 6% semi-annually, so the pro-rated quarterly coupon is:

    $$
    C = \frac{0.06}{4} \times 10{,}000{,}000 = \$150{,}000
    $$

    Capital gain/loss:

    $$
    P_1 - P_0 = 9{,}950{,}000 - 10{,}100{,}000 = -\$150{,}000
    $$

    Total return:

    $$
    \text{TR} = 150{,}000 + (-150{,}000) = \$0
    $$

    **Funding leg (paid by TR receiver):**

    $$
    \text{Funding} = (\text{SOFR} + s_{\text{TRS}}) \times \Delta \times N = (0.045 + 0.006) \times 0.25 \times 10{,}000{,}000
    $$

    $$
    = 0.051 \times 0.25 \times 10{,}000{,}000 = \$127{,}500
    $$

    **Net cash flow to TR receiver:**

    $$
    \text{Net} = \text{TR} - \text{Funding} = 0 - 127{,}500 = -\$127{,}500
    $$

    The TR receiver **pays \$127,500** to the TR payer this quarter. The coupon income exactly offsets the capital loss from the bond price decline, leaving the TR receiver with a net payment equal to the full funding cost.

---

**Exercise 2.** At inception of a TRS, the fair spread is determined by

$$
s_{\text{TRS}} = y_{\text{bond}} - L
$$

where $y_{\text{bond}}$ is the bond yield and $L$ is the floating rate. A bond yields 5.8% and the floating rate is 4.5%. Compute the fair TRS spread. If the TR receiver can borrow at $L + 200$ bp, explain the economic advantage of entering the TRS versus purchasing the bond outright.

??? success "Solution to Exercise 2"

    **Fair TRS spread:**

    $$
    s_{\text{TRS}} = y_{\text{bond}} - L = 5.8\% - 4.5\% = 1.3\% = 130 \text{ bp}
    $$

    **Economic advantage of the TRS:**

    If the TR receiver purchases the bond outright, they must borrow at $L + 200$ bp $= 4.5\% + 2.0\% = 6.5\%$. Their net return from holding the bond would be:

    $$
    \text{Net return (outright)} = y_{\text{bond}} - \text{Borrowing cost} = 5.8\% - 6.5\% = -0.7\%
    $$

    The outright purchase is uneconomical because the funding cost exceeds the bond yield.

    Through the TRS, the TR receiver obtains the total return of the bond and pays $L + s_{\text{TRS}} = 4.5\% + 1.3\% = 5.8\%$. Their net return is:

    $$
    \text{Net return (TRS)} = y_{\text{bond}} - (L + s_{\text{TRS}}) = 5.8\% - 5.8\% = 0\%
    $$

    At fair value, the TRS provides zero excess return. However, compared to the outright purchase at a 6.5% funding cost, the TRS saves the receiver $6.5\% - 5.8\% = 0.7\%$ per year. The receiver effectively borrows at the TR payer's funding rate (embedded in the TRS spread) rather than their own higher rate.

    More generally, the TRS is advantageous whenever $s_{\text{TRS}} < s_{\text{funding}}^{\text{receiver}}$, i.e., whenever the TRS spread is less than the receiver's own credit spread. This creates value because the TR payer (typically a bank with a lower funding cost) intermediates the funding, earning the difference between the TRS spread and its own funding cost.

---

**Exercise 3.** Explain why a TRS transfers all market risks (credit, interest rate, and liquidity) while a CDS transfers only default risk. Construct a portfolio combining a TRS and a CDS on the same reference entity that isolates the non-default component of credit spread risk. Describe what residual risks remain.

??? success "Solution to Exercise 3"

    **Why a TRS transfers all market risks while a CDS transfers only default risk:**

    A CDS has a binary-style protection leg: it pays $(1-R) \times N$ if and only if a credit event (default) occurs. Before default, no matter how much the reference bond's price moves due to spread widening, interest rate changes, or liquidity deterioration, the CDS protection leg has no interim payments. The CDS isolates the default event.

    A TRS, by contrast, passes through the **full mark-to-market** changes of the reference asset at each reset. If the bond price falls due to:

    - **Credit deterioration** (spread widening without default): the TR receiver bears the capital loss
    - **Interest rate increases:** the TR receiver bears the capital loss
    - **Liquidity dry-up:** the TR receiver bears the capital loss

    Thus the TRS transfers credit risk, interest rate risk, and liquidity risk simultaneously.

    **Isolating the non-default component of credit spread risk:**

    Construct the following portfolio:

    1. **Enter a TRS as TR receiver** on the reference bond (receive total return, pay $L + s_{\text{TRS}}$)
    2. **Buy CDS protection** on the same reference entity (pay CDS spread $s_{\text{CDS}}$, receive $(1-R) \times N$ at default)

    Upon default, the TRS settles with the TR receiver absorbing the bond depreciation $(P_{\text{prev}} - P_\tau)$, while the CDS pays $(1-R) \times N$, which approximately offsets the default loss. The combined position is approximately hedged against default.

    Before default, the TRS passes through all mark-to-market changes (credit spread, rates, liquidity), while the CDS has no interim payments. Therefore, the combined position isolates:

    $$
    \text{Residual risk} \approx \text{Interest rate risk} + \text{Liquidity risk} + \text{Spread risk not captured by CDS}
    $$

    **Residual risks that remain:**

    - **Interest rate risk:** Bond price changes from rate movements are not hedged
    - **Basis risk:** The CDS spread and bond spread may move differently (CDS-bond basis changes)
    - **Recovery rate uncertainty:** CDS assumes a fixed recovery; actual recovery may differ
    - **Maturity and roll mismatch:** TRS and CDS may have different maturities or reset conventions
    - **Funding/carry costs:** The net funding cost $s_{\text{TRS}} - s_{\text{CDS}}$ may fluctuate

---

**Exercise 4.** The reference bond in a TRS defaults at time $\tau$, with post-default recovery price $P_{\tau} = 38\%$ of face. The bond price at the last reset before default was $P_{\text{prev}} = 95\%$. On a notional of \$10 million, compute the settlement payment at default. Who makes this payment, the TR payer or the TR receiver?

??? success "Solution to Exercise 4"

    **Given:**

    - Notional: $N = \$10$ million
    - Post-default recovery price: $P_\tau = 38\%$ of face $= \$3{,}800{,}000$
    - Last reset price: $P_{\text{prev}} = 95\%$ of face $= \$9{,}500{,}000$

    **Settlement payment at default:**

    The TRS terminates early. The final total return settlement is:

    $$
    \text{Settlement} = P_\tau - P_{\text{prev}} = 3{,}800{,}000 - 9{,}500{,}000 = -\$5{,}700{,}000
    $$

    Since the total return is negative (the bond depreciated massively), the **TR receiver pays \$5,700,000 to the TR payer**.

    The TR receiver bears the capital loss because they are the synthetic holder of the bond's economic performance. The loss of \$5.7 million represents the bond's depreciation from 95% to 38% of face.

    Note: In addition to the capital loss settlement, any accrued funding payment for the partial period up to default would also be settled. The TR payer is made whole because they pass the asset's loss to the TR receiver, which is the economic purpose of the TRS.

---

**Exercise 5.** Describe the wrong-way risk embedded in a TRS from the perspective of the TR payer. Specifically, explain why the counterparty credit exposure and the TR receiver's creditworthiness may be positively correlated during a credit crisis. How does daily margining mitigate (but not eliminate) this risk?

??? success "Solution to Exercise 5"

    **Wrong-way risk for the TR payer:**

    The TR payer's credit exposure to the TR receiver arises when the reference asset depreciates. In that scenario, the TR receiver owes money to the TR payer (to compensate for the capital loss). The TR payer's exposure at any reset is:

    $$
    \text{Exposure}_{\text{payer}} = \max(P_{t_{i-1}} - P_{t_i}, 0)
    $$

    **Why this creates wrong-way risk:**

    During a credit crisis, the following events are correlated:

    1. **The reference asset depreciates** significantly (e.g., credit spreads widen, bonds lose value)
    2. **The TR receiver's creditworthiness deteriorates** simultaneously, especially if:
        - The TR receiver is a leveraged investor (hedge fund) with exposure to the same credit markets
        - The TR receiver's portfolio suffers losses, reducing their ability to post collateral or make payments
        - Broader market stress affects the TR receiver's own credit standing

    This creates positive correlation between the TR payer's exposure (large when the bond falls) and the TR receiver's probability of default (high when markets are in crisis). This is the classic definition of wrong-way risk.

    **Concrete example:** A hedge fund (TR receiver) uses TRS for leveraged exposure to high-yield bonds. During the 2008 crisis:

    - High-yield bonds fell 20--30% in value, creating large obligations from the TR receiver to the TR payer
    - Simultaneously, the hedge fund faced margin calls on other positions, redemption pressure from investors, and declining creditworthiness
    - The TR payer's largest exposures materialized precisely when the TR receiver was least able to pay

    **How daily margining mitigates but does not eliminate the risk:**

    Daily margining (mark-to-market with collateral posting) reduces the exposure to approximately one day's worth of market movement, rather than the full period between resets. However, residual risks remain:

    - **Margin period of risk (MPoR):** If the TR receiver fails to post margin, the TR payer must close out the position. During this close-out period (typically 10--20 business days for OTC derivatives), the reference asset may continue to depreciate.
    - **Gap risk:** Large, sudden price moves (e.g., credit events, flash crashes) can occur between margin calls, leaving the TR payer with unrecovered exposure.
    - **Collateral haircuts:** Collateral posted may itself lose value during a crisis (if it consists of risky assets).
    - **Operational delays:** Legal and operational processes to seize collateral take time, during which exposure accumulates.

---

**Exercise 6.** A hedge fund uses a TRS to gain leveraged exposure to a \$100 million bond portfolio. The initial margin requirement is 10% of notional. If the bond portfolio appreciates by 3% over the first quarter and the net funding cost (SOFR + TRS spread) is 5.2% annualized, compute the hedge fund's return on equity for the quarter. Compare this to the unleveraged return from purchasing the bonds outright.

??? success "Solution to Exercise 6"

    **Given:**

    - Notional: $N = \$100$ million
    - Initial margin: 10% of notional $= \$10$ million (the hedge fund's equity)
    - Bond appreciation: $3\%$ over the quarter
    - Net funding cost: $5.2\%$ annualized

    **TRS return calculation (leveraged via TRS):**

    Capital gain from the TRS:

    $$
    \text{Capital gain} = 3\% \times 100{,}000{,}000 = \$3{,}000{,}000
    $$

    Funding cost for the quarter (annualized rate $\times$ $\frac{1}{4}$):

    $$
    \text{Funding cost} = 5.2\% \times \frac{1}{4} \times 100{,}000{,}000 = 1.3\% \times 100{,}000{,}000 = \$1{,}300{,}000
    $$

    In addition, the hedge fund receives coupon income passed through the TRS. Assuming the bond has a coupon of, say, $c\%$ annually, the quarterly coupon received is $c/4 \times N$. However, since the problem specifies only the net funding cost and appreciation, we compute the net profit as:

    $$
    \text{Net profit} = \text{Capital gain} - \text{Funding cost} = 3{,}000{,}000 - 1{,}300{,}000 = \$1{,}700{,}000
    $$

    (Note: If coupon income is included in the "3% appreciation," the net profit is as computed above.)

    **Return on equity (TRS/leveraged):**

    $$
    \text{ROE}_{\text{TRS}} = \frac{\text{Net profit}}{\text{Equity}} = \frac{1{,}700{,}000}{10{,}000{,}000} = 17.0\% \text{ (for one quarter)}
    $$

    **Unleveraged return (outright purchase):**

    If the hedge fund purchases \$100 million of bonds outright using \$100 million of its own capital:

    $$
    \text{Return}_{\text{unleveraged}} = \frac{\text{Capital gain}}{\text{Investment}} = \frac{3{,}000{,}000}{100{,}000{,}000} = 3.0\% \text{ (for one quarter)}
    $$

    (There is no external funding cost since the fund uses its own capital, though there is an opportunity cost.)

    **Comparison:**

    | Metric | TRS (Leveraged) | Outright (Unleveraged) |
    |--------|----------------|----------------------|
    | Capital deployed | \$10 million | \$100 million |
    | Exposure | \$100 million | \$100 million |
    | Leverage | 10x | 1x |
    | Quarterly return on capital | 17.0% | 3.0% |

    The TRS provides a 10x leverage ratio (notional / margin), amplifying the quarterly return from 3.0% to 17.0%---a factor of approximately $10 \times (3\% - 1.3\%) / 3\% \approx 5.7$ on a risk-adjusted basis.

    However, leverage is symmetric: if the bond portfolio had declined by 3%, the quarterly loss on equity via the TRS would be:

    $$
    \text{Loss} = \frac{-3{,}000{,}000 - 1{,}300{,}000}{10{,}000{,}000} = -43.0\%
    $$

    This illustrates that TRS leverage amplifies both gains and losses, making it a powerful but risky tool.
