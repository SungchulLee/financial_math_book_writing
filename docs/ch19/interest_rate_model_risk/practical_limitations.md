# Practical Limitations


Even well-designed interest-rate models face **practical limitations** when deployed in real trading and risk environments. Recognizing these limitations is a core aspect of model risk management.

---

## Calibration vs usage gap


Models calibrated to:
- liquid vanilla instruments

are often used to price:
- illiquid or exotic products.

Extrapolation beyond calibration data introduces uncertainty.

---

## Sensitivity to implementation choices


Results depend on:
- interpolation and smoothing methods,
- numerical solvers and discretization,
- day-count and market conventions.

These choices can dominate theoretical differences between models.

---

## Hedging limitations


Even with perfect calibration:
- hedging instruments may be illiquid,
- dynamic re-hedging assumptions fail,
- transaction costs and slippage matter.

Model-implied hedges are idealizations.

---

## Governance and controls


Effective model risk management requires:
- validation across scenarios,
- stress testing and benchmarking,
- conservative usage and reserves.

No model should be treated as “truth”.

---

## Key takeaways


- All IR models are approximations.
- Practical constraints limit theoretical optimality.
- Awareness of limitations is essential for safe use.

---

## Further reading


- Basel model risk guidance.
- Cont, *Model Uncertainty and Its Impact on Pricing*.

---

## Exercises

**Exercise 1.** A bank calibrates a SABR model to the ATM swaption surface and uses it to price a 30-year Bermudan swaption. The calibration instruments (European swaptions) have maturities up to 10 years. Discuss the sources of model risk that arise from using the model outside its calibration domain. What specific aspects of the Bermudan swaption are most sensitive to this extrapolation?

---

**Exercise 2.** Two quant teams implement the same Hull--White model for a callable bond. Team A uses cubic spline interpolation for the yield curve, while Team B uses monotone piecewise-linear interpolation. The resulting prices differ by 3 bps. Explain why implementation choices can have this magnitude of impact and propose a protocol for quantifying implementation risk.

---

**Exercise 3.** A trader hedges a 10-year CMS spread option using delta and vega from a two-factor LMM. Over a 1-month period, the realized P&L deviates significantly from the model-predicted P&L. List at least four potential sources of this hedging error, distinguishing between model risk, market risk, and operational risk.

---

**Exercise 4.** A model validation team proposes the following benchmark test: price the same exotic derivative under three different models (Hull--White, LMM, and SABR-LMM) and report the range of prices. If the range is less than 2 bps, the model risk is deemed acceptable. Critique this approach and suggest improvements.

---

**Exercise 5.** Dynamic delta hedging of an interest rate option assumes continuous rebalancing with zero transaction costs. In practice, hedging occurs daily with bid-ask spreads of 0.25 bps on the underlying swap. For a 5-year swaption with notional \$500 million and daily delta rebalancing, estimate the cumulative transaction costs over the life of the option. How does this compare to the model-implied option price?

---

**Exercise 6.** The Basel Committee's SR 11-7 guidance on model risk management requires that models be validated independently of the development team. Describe the key elements of a model validation report for an interest rate derivatives pricing model, including (a) conceptual soundness, (b) data quality, (c) backtesting, and (d) stress testing. For each element, give a concrete example relevant to a LIBOR Market Model.
