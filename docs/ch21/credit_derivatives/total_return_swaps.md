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
