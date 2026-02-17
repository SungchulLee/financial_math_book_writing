# ---
# title: "DX Framework — Derivatives Portfolio"
# description: >
#   Orchestrates the valuation of a multi-position derivatives portfolio.
#   Key responsibilities:
#     1. Build a unified time grid across all positions.
#     2. Handle correlations between underlyings (Cholesky decomposition
#        of the correlation matrix).
#     3. Instantiate the correct simulation and valuation objects.
#     4. Aggregate present values, Deltas, and Vegas into a DataFrame.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np
import pandas as pd

from dx_sn_random_numbers import sn_random_numbers
from dx_geometric_brownian_motion import GeometricBrownianMotion
from dx_jump_diffusion import JumpDiffusion
from dx_square_root_diffusion import SquareRootDiffusion
from dx_valuation_mcs_european import ValuationMCSEuropean
from dx_valuation_mcs_american import ValuationMCSAmerican

# ── Registry of available models and exercise types ─────────────
MODELS = {
    'gbm': GeometricBrownianMotion,
    'jd': JumpDiffusion,
    'srd': SquareRootDiffusion,
}
OTYPES = {
    'European': ValuationMCSEuropean,
    'American': ValuationMCSAmerican,
}


class DerivativesPortfolio:
    """Portfolio-level derivatives valuation engine.

    Parameters
    ----------
    name : str
        Portfolio identifier.
    positions : dict
        ``{key: DerivativesPosition}`` mapping.
    val_env : MarketEnvironment
        Shared valuation environment (must contain ``starting_date``,
        ``final_date``, ``frequency``, ``paths``).
    assets : dict
        ``{underlying_name: MarketEnvironment}`` for each risk factor.
    correlations : list of tuples, optional
        ``[(asset_i, asset_j, rho), ...]`` pairwise correlations.
    fixed_seed : bool
        Fix the random seed globally for the portfolio.
    """

    def __init__(self, name, positions, val_env, assets,
                 correlations=None, fixed_seed=False):
        self.name = name
        self.positions = positions
        self.val_env = val_env
        self.assets = assets
        self.underlyings = set()
        self.correlations = correlations
        self.time_grid = None
        self.underlying_objects = {}
        self.valuation_objects = {}
        self.fixed_seed = fixed_seed
        self.special_dates = []

        # Determine date range across all positions
        for pos in self.positions:
            p = positions[pos]
            self.val_env.constants['starting_date'] = min(
                self.val_env.constants['starting_date'],
                p.mar_env.pricing_date)
            self.val_env.constants['final_date'] = max(
                self.val_env.constants['final_date'],
                p.mar_env.constants['maturity'])
            self.underlyings.add(p.underlying)

        # Build unified time grid
        start = self.val_env.constants['starting_date']
        end = self.val_env.constants['final_date']
        time_grid = list(pd.date_range(
            start=start, end=end,
            freq=self.val_env.constants['frequency']).to_pydatetime())

        for pos in self.positions:
            mat = positions[pos].mar_env.constants['maturity']
            if mat not in time_grid:
                time_grid.append(mat)
                self.special_dates.append(mat)
        if start not in time_grid:
            time_grid.insert(0, start)
        if end not in time_grid:
            time_grid.append(end)
        self.time_grid = np.array(sorted(set(time_grid)))
        self.val_env.add_list('time_grid', self.time_grid)

        # Handle correlations via Cholesky decomposition
        if correlations is not None:
            ul_list = sorted(self.underlyings)
            corr_mat = pd.DataFrame(
                np.eye(len(ul_list)), index=ul_list, columns=ul_list)
            for i, j, rho in correlations:
                rho = min(rho, 0.999999999999)
                corr_mat.loc[i, j] = rho
                corr_mat.loc[j, i] = rho
            cholesky = np.linalg.cholesky(np.array(corr_mat))
            rn_set = {asset: ul_list.index(asset) for asset in self.underlyings}
            random_numbers = sn_random_numbers(
                (len(rn_set), len(self.time_grid),
                 self.val_env.constants['paths']),
                fixed_seed=self.fixed_seed)
            self.val_env.add_list('cholesky_matrix', cholesky)
            self.val_env.add_list('random_numbers', random_numbers)
            self.val_env.add_list('rn_set', rn_set)

        # Instantiate simulation objects
        for asset in self.underlyings:
            mar_env = self.assets[asset]
            mar_env.add_environment(val_env)
            model = MODELS[mar_env.constants['model']]
            corr = correlations is not None
            self.underlying_objects[asset] = model(asset, mar_env, corr=corr)

        # Instantiate valuation objects
        for pos in positions:
            val_class = OTYPES[positions[pos].otype]
            mar_env = positions[pos].mar_env
            mar_env.add_environment(self.val_env)
            self.valuation_objects[pos] = val_class(
                name=positions[pos].name,
                mar_env=mar_env,
                underlying=self.underlying_objects[positions[pos].underlying],
                payoff_func=positions[pos].payoff_func)

    def get_positions(self):
        """Print information about all positions."""
        for pos in self.positions:
            print('\n' + '─' * 50)
            self.positions[pos].get_info()

    def get_statistics(self, fixed_seed=False):
        """Return a DataFrame with value, Delta, and Vega for each position."""
        rows = []
        for pos, val_obj in self.valuation_objects.items():
            p = self.positions[pos]
            pv = val_obj.present_value(fixed_seed=fixed_seed)
            rows.append([
                p.name, p.quantity, pv, val_obj.currency,
                pv * p.quantity,
                val_obj.delta() * p.quantity,
                val_obj.vega() * p.quantity,
            ])
        return pd.DataFrame(rows, columns=[
            'name', 'quantity', 'value', 'currency',
            'pos_value', 'pos_delta', 'pos_vega'])
