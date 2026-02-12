# Chapter 7: Extensions, American, and Exotic Options

This chapter extends the Black-Scholes framework beyond European vanilla options, covering American options with early exercise features, exotic options with complex payoff structures, and jump-diffusion models that capture discontinuous market movements.

## Key Concepts

**Black-Scholes Extensions**
The classical Black-Scholes model assumes:
- Constant volatility
- No dividends
- No transaction costs
- Frictionless markets

Real markets violate these assumptions, necessitating extensions including:
- Time-varying and stochastic volatility
- Continuous dividend yields
- Transaction costs and bid-ask spreads
- Jump risk in asset returns

**American Options**
American options permit early exercise at any time up to maturity, making them more valuable than European counterparts. Key features:
- Free boundary problem: optimal exercise boundary must be determined
- No closed-form solution exists for American puts under GBM
- Numerical methods (finite difference, binomial trees, least-squares Monte Carlo) required
- Early exercise is optimal when exercising immediately exceeds continuation value

**Exotic Options**
Exotic options have non-standard payoffs or features:
- **Path-dependent**: Asian, lookback, barrier options
- **Multi-asset**: basket, rainbow, spread options
- **Hybrid**: convertible bonds, structured products
- **Knock-out/In**: activate or deactivate based on barrier crossing

**Merton Jump-Diffusion Model**
Real asset returns exhibit occasional large jumps not captured by continuous diffusions:
$$dS_t = \mu S_t dt + \sigma S_t dB_t + S_t d(J_t - \lambda \mathbb{E}[J_t] t)$$
where $J_t$ is a compound Poisson process of jump sizes. This model enables:
- More realistic capture of tail risk and volatility smiles
- Pricing of options with jump risk premia
- Calibration to market option data exhibiting smile effects

!!! warning "Numerical Considerations"
    American options and exotic options typically require:
    - Numerical approximation (no closed-form solutions)
    - Careful handling of exercise boundaries and path dependencies
    - Validation through comparison with limiting cases and market data
    - Computational efficiency for real-time pricing in production systems
