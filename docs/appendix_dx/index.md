# Appendix: DX Derivatives Analytics Library

This appendix presents the **DX derivatives analytics library**, an
object-oriented Python framework that unifies many of the concepts
developed throughout this book into a single, reusable pricing engine.

The library is organised into three layers:

| Layer | Classes | Purpose |
|-------|---------|---------|
| **Frame** | `MarketEnvironment`, `ConstantShortRate`, `get_year_deltas` | Market data management and discounting |
| **Simulation** | `SimulationClass` (base), `GeometricBrownianMotion`, `SquareRootDiffusion`, `JumpDiffusion` | Monte Carlo path generation |
| **Valuation** | `ValuationClass` (base), `ValuationMCSEuropean`, `ValuationMCSAmerican`, `DerivativesPosition`, `DerivativesPortfolio` | Pricing, Greeks, and portfolio aggregation |

The design demonstrates how inheritance and composition can turn the
individual algorithms from earlier chapters into a coherent system
capable of valuing multi-asset portfolios with correlated risk factors.

!!! note "Attribution"
    The DX library is adapted from Yves Hilpisch,
    *Python for Finance*, 2nd edition (O'Reilly, 2018).
    The versions presented here have been refactored with improved
    documentation, type hints, and Pythonic naming conventions.
