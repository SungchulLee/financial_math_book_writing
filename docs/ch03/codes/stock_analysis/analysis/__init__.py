"""
  Init  

Educational script demonstrating   init   concepts.
"""

# ============================================================================
# stock_analysis/analysis/__init__.py
# ============================================================================
from .returns import compute_returns, compute_log_returns, compute_both_returns
from .statistics import compute_mu_and_sigma, annualize_statistics, compute_rolling_stats


if __name__ == "__main__":
    __all__ = [
        "compute_returns", 
        "compute_log_returns",
        "compute_both_returns",
        "compute_mu_and_sigma", 
        "annualize_statistics",
        "compute_rolling_stats"
    ]