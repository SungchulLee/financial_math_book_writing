# Firm Value Models (Merton)


Structural credit risk models view default as an economic event driven by the firm’s asset value. The **Merton model** is the foundational framework in this class.

---

## Basic idea


A firm defaults at maturity \(T\) if the value of its assets \(V_T\) is insufficient to repay its debt \(D\).
Equity and debt are interpreted as contingent claims on firm value.

---

## Asset dynamics


Under the risk-neutral measure,

\[
dV_t = (r - q)V_t\,dt + \sigma_V V_t\,dW_t,
\]


where:
- \(V_t\): firm asset value,
- \(\sigma_V\): asset volatility,
- \(D\): face value of debt.

---

## Default event and payoffs


At maturity \(T\):
- default occurs if \(V_T < D\),
- equity payoff: \((V_T - D)^+\),
- debt payoff: \(\min(V_T, D)\).

Thus, equity is a call option on firm value, and debt is risk-free debt minus a put.

---

## Credit spreads


The value of risky debt implies a credit spread over the risk-free rate.
Spreads depend on:
- leverage \(D/V_0\),
- asset volatility,
- time to maturity.

The model links credit spreads to equity volatility.

---

## Key takeaways


- Default occurs at maturity only.
- Equity and debt are option-like claims.
- Merton provides a direct equity–credit link.

---

## Further reading


- Merton (1974).
- Leland, structural credit models.
