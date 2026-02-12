# Gamma Risk and Convexity Effects


For a small move \(\delta S\),

\[
\delta V \approx \Delta\,\delta S + \frac{1}{2}\Gamma(\delta S)^2.
\]


Delta-hedging removes the linear term, leaving

\[
\boxed{\delta V_{\text{delta-hedged}}\approx \frac{1}{2}\Gamma(\delta S)^2}
\]


Thus gamma exposure links delta-hedged P&L to realized variance.

---

## Continuous-time P&L decomposition


For a delta-hedged option position over time interval \([t, t+dt]\), the instantaneous P&L is:

\[
dP\&L = dV - \Delta \, dS
\]

Using Itô's lemma on \(V(t,S)\):

\[
dV = \Theta \, dt + \Delta \, dS + \frac{1}{2}\Gamma (dS)^2
\]

After delta-hedging:

\[
\boxed{dP\&L_{\text{hedged}} = \Theta \, dt + \frac{1}{2}\Gamma (dS)^2}
\]

Since \((dS)^2 = \sigma^2 S^2 dt\) (in expectation):

\[
\mathbb{E}[dP\&L_{\text{hedged}}] = \left(\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma\right) dt
\]

By the Black–Scholes PDE, this equals \(r(V - S\Delta)dt\), the cost of financing.

---

## Theta-gamma relationship


The fundamental identity:

\[
\boxed{\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)}
\]

**Interpretation:**
- Long gamma positions earn from realized volatility (\(\frac{1}{2}\Gamma(dS)^2\))
- But pay theta (time decay) to maintain the position
- These exactly offset when realized vol equals implied vol

**For ATM options:**
\[
\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma
\]

since \(V - S\Delta \approx 0\) for ATM.

---

## Gamma P&L over discrete intervals


Over a finite interval \(\Delta t\), with spot move \(\Delta S = S_{t+\Delta t} - S_t\):

\[
P\&L_{\text{hedged}} \approx \Theta \Delta t + \frac{1}{2}\Gamma (\Delta S)^2
\]

In terms of returns \(R = \Delta S/S\):

\[
P\&L_{\text{hedged}} \approx \Theta \Delta t + \frac{1}{2}\Gamma S^2 R^2
\]

**Expected P&L** (assuming correct model):
\[
\mathbb{E}[P\&L_{\text{hedged}}] = \Theta \Delta t + \frac{1}{2}\Gamma S^2 \sigma^2 \Delta t = r(V - S\Delta)\Delta t
\]

**Variance of P&L:**
\[
\text{Var}(P\&L_{\text{hedged}}) \approx \frac{1}{2}\Gamma^2 S^4 \sigma^4 \Delta t^2
\]

(using \(\text{Var}(R^2) \approx 2\sigma^4 \Delta t\) for normal returns)

---

## Long gamma vs short gamma


**Long gamma** (positive \(\Gamma\)):
- Benefits from large moves: \(\frac{1}{2}\Gamma(\Delta S)^2 > 0\)
- Pays theta: \(\Theta < 0\) typically
- Profits when realized volatility exceeds implied volatility
- "Buy low, sell high" rebalancing: as \(S\) rises, sell; as \(S\) falls, buy

**Short gamma** (negative \(\Gamma\)):
- Earns theta: \(\Theta > 0\) (collecting premium)
- Loses on large moves: \(\frac{1}{2}\Gamma(\Delta S)^2 < 0\)
- Profits when realized volatility is below implied volatility
- "Buy high, sell low" rebalancing: adverse rebalancing

---

## Realized vs implied volatility trading


The P&L from delta-hedging over \([0,T]\) is:

\[
P\&L = \frac{1}{2}\int_0^T \Gamma(t,S_t) S_t^2 (\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2) dt
\]

where \(\sigma_{\text{realized}}^2 dt = (dS/S)^2\) is instantaneous realized variance.

**Trading strategy:**
- If you expect \(\sigma_{\text{realized}} > \sigma_{\text{implied}}\): buy options (long gamma)
- If you expect \(\sigma_{\text{realized}} < \sigma_{\text{implied}}\): sell options (short gamma)

---

## Dollar gamma


Practitioners often use **dollar gamma**:

\[
\Gamma_{\$} = \frac{1}{2}\Gamma S^2
\]

This measures the dollar P&L from a 1% move:

\[
P\&L \approx \Gamma_{\$} \cdot (R \times 100)^2 / 10000 = \Gamma_{\$} R^2
\]

---

## Numerical example


Consider an ATM call with \(S = K = 100\), \(\sigma = 20\%\), \(\tau = 30\) days, \(r = 5\%\):

- \(\Gamma = 0.055\)
- \(\Theta = -0.044\) per day
- \(\Gamma_{\$} = \frac{1}{2} \times 0.055 \times 100^2 = 275\)

**Scenario: 2% daily move**
\[
\text{Gamma P&L} = \frac{1}{2} \times 0.055 \times (2)^2 = 0.11
\]
\[
\text{Theta P&L} = -0.044
\]
\[
\text{Net P&L} = 0.11 - 0.044 = 0.066
\]

The position profits because the realized move (2%) exceeds the implied daily vol (\(\sigma\sqrt{1/252} \approx 1.26\%\)).

---

## What to remember


- Long gamma benefits from volatility (large squared moves)
- Short gamma earns carry but is exposed to large moves
- Theta and gamma are linked: \(\Theta + \frac{1}{2}\sigma^2 S^2\Gamma = r(V - S\Delta)\)
- Delta-hedged P&L depends on realized vs implied volatility
- Dollar gamma \(\Gamma_{\$} = \frac{1}{2}\Gamma S^2\) measures dollar exposure to variance
