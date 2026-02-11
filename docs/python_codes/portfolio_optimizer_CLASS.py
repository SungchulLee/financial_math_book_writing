import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize, stats
import cvxpy as cp

# Requires: Stock class from stock_analysis module
# import yfinance as yf

class PortfolioOptimizer:
    def __init__(self, tickers, start_date, end_date=None, risk_free_rate=0.03):
        """Initialize the PortfolioOptimizer.

        Parameters:
            tickers (list of str): List of asset tickers.
            start_date (str): Start date for historical data (YYYY-MM-DD).
            end_date (str, optional): End date for historical data. Defaults to None (latest available).
            risk_free_rate (float): Annualized risk-free rate (in decimal). Defaults to 0.03.
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.risk_free_rate = risk_free_rate

        self.returns_df = self.fetch_daily_returns()
        self.mu = self.returns_df.mean() * 252
        self.sigma = self.returns_df.cov() * 252

    def fetch_daily_returns(self):
        """Fetch daily return series for each ticker using the Stock class.

        Returns:
            pd.DataFrame: DataFrame of daily returns, one column per asset.
        """
        returns = {}
        for ticker in self.tickers:
            stock = Stock(ticker)
            stock.get_historical_prices(self.start_date, self.end_date)
            stock.compute_returns()
            returns[ticker] = stock.df['Return']
        return pd.DataFrame(returns).dropna(axis=1)

    def plot_individual_assets(self, ax):
        """Plot individual assets as points in the risk-return space.

        Parameters:
            ax (matplotlib.axes.Axes): Axes object to plot on.
        """
        volatilities = pd.Series(np.sqrt(np.diag(self.sigma)), index=self.sigma.columns)
        for ticker in self.mu.index:
            ax.plot(volatilities[ticker], self.mu[ticker], 'o', color='red', alpha=0.7)
            ax.annotate(ticker, (volatilities[ticker], self.mu[ticker]))

    def plot_equal_portfolio(self, ax):
        """Plot the equal-weight portfolio in the risk-return space.

        Parameters:
            ax (matplotlib.axes.Axes): Axes object to plot on.
        """
        w_equal = self.equal_portfolio()
        mu_equal, vol_equal, _ = self.portfolio_performance(w_equal)
        ax.plot([vol_equal], [mu_equal], 'o')
        ax.annotate('Equal', (vol_equal, mu_equal))

    def plot_random_portfolios(self, ax, num_portfolios=100_000, short=True):
        """Simulate and plot a set of random portfolios.

        Parameters:
            ax (matplotlib.axes.Axes): Axes object to plot on.
            num_portfolios (int): Number of random portfolios to simulate.
            short (bool): If True, allows short-selling in random weights; otherwise enforces long-only weights.
        """
        n_assets = len(self.mu)
        weights = np.random.normal(size=(num_portfolios, n_assets))
        if not short:
            weights = np.exp(weights)
        weights /= weights.sum(axis=1, keepdims=True)

        mu_vec = self.mu.values
        sigma_mat = self.sigma.values

        returns = weights @ mu_vec
        risks = np.sqrt(np.einsum('ij,jk,ik->i', weights, sigma_mat, weights))
        ax.plot(risks, returns, ',', color='blue', alpha=0.05, label='Random Portfolios')

    def plot_capital_market_line(self, ax, short=True):
        """Plot the Capital Market Line (CML) using the tangency portfolio.

        Parameters:
            ax (matplotlib.axes.Axes): Axes object to plot on.
            short (bool): If True, uses unconstrained tangency portfolio; otherwise uses long-only version.
        """
        w_tan = self.tangency_portfolio(short)
        mu_tan, vol_tan, _ = self.portfolio_performance(w_tan)
        ax.plot([vol_tan], [mu_tan], 'o')
        ax.annotate('Tangeny Portfolio' if short else 'Constrained Tangeny Portfolio', (vol_tan, mu_tan))

        slope = (mu_tan - self.risk_free_rate) / vol_tan
        x_vals = np.linspace(0, vol_tan * 1.5, 100)
        y_vals = self.risk_free_rate + slope * x_vals
        ax.plot(x_vals, y_vals, linestyle='--', color='green', label='Capital Market Line')

        ax.plot(x_vals[0:1], y_vals[0:1], 'o')
        ax.annotate('Risk Free Rate', (0, y_vals[0]))

    def plot_efficient_frontier(self, ax, short=True):
        """Plot the efficient frontier.

        Parameters:
            ax (matplotlib.axes.Axes): Axes object to plot on.
            short (bool): If True, uses two-fund mix of GMVP and tangency; otherwise solves constrained optimization.
        """
        df_efficient_frontier = self.efficient_frontier(short=short)
        if short:
            ax.plot(df_efficient_frontier.Volatility, df_efficient_frontier.Return, label="Efficient Frontier")
        else:
            ax.plot(df_efficient_frontier.Volatility, df_efficient_frontier.Return, label="Constrained Efficient Frontier")

    def plot_gmvp(self, ax, short=True):
        """Plot the Global Minimum Variance Portfolio (GMVP).

        Parameters:
            ax (matplotlib.axes.Axes): Axes object to plot on.
            short (bool): If True, uses unconstrained GMVP; otherwise uses constrained (long-only) GMVP.
        """
        w_gmvp = self.gmvp(short)
        mu_gmvp, vol_gmvp, _ = self.portfolio_performance(w_gmvp)
        ax.plot([vol_gmvp], [mu_gmvp], 'o')
        ax.annotate('GMVP' if short else 'Constrained GMVP', (vol_gmvp, mu_gmvp))

    def plot(self):
        """Generate side-by-side plots of portfolio optimization results:
        - Short selling allowed
        - No short selling (long-only)

        Includes: Efficient frontier, Capital Market Line (CML), GMVP,
        equal-weight portfolio, and individual assets.

        Notes:
            - Two subplots are generated: one for short-selling allowed, and one for long-only.
            - The subplot titles ("Short Allowed", "No Short") are set using:
                ax.set_title(f"Efficient Frontier and Capital Market Line ({constraint})")
            so each plot dynamically reflects its constraint in the title.
        """
        fig, (ax_short_allowed, ax_no_short) = plt.subplots(1,2, figsize=(12, 5))

        for ax, short, constraint in zip( (ax_short_allowed, ax_no_short), (True, False), ("Short Allowed", "No Short") ) :
            self.plot_individual_assets(ax)
            self.plot_equal_portfolio(ax)
            self.plot_random_portfolios(ax, short=short)
            self.plot_capital_market_line(ax, short=short)
            self.plot_efficient_frontier(ax, short=short)
            self.plot_gmvp(ax, short=short)

            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_position("zero")
            ax.spines['left'].set_position("zero")

            # ax.set_xlabel("Volatility (σ)")
            # ax.set_ylabel("Expected Return (μ)")
            # ax.set_title(f"Efficient Frontier and Capital Market Line ({constraint})")
            ax.set(xlabel="Volatility (σ)",ylabel="Expected Return (μ)",title=f"Efficient Frontier and Capital Market Line ({constraint})")

            ax.grid(True)
            ax.legend()
            ax.set_xlim([0, np.sqrt(self.sigma.max().max()) * 1.1])
            ax.set_ylim([0, self.mu.max() * 1.1])

        plt.tight_layout()
        plt.show()

    def plot_correlation_matrix(self):
        """Visualize the correlation matrix of asset returns.

        Generates a heatmap to show pairwise correlations between asset returns,
        helping to assess diversification potential and co-movement.
        """
        corr = self.returns_df.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
        plt.title("Asset Return Correlation Matrix")
        plt.show()

    def plot_return_distributions(self):
        """Plot kernel density estimates (KDE) of daily return distributions.

        Visualizes the shape, spread, and skewness of return distributions
        for each asset using overlapping KDE curves.

        Notes:
            - Useful for diagnosing non-normality or heavy tails in asset returns.
        """
        fig, ax = plt.subplots(figsize=(10, 5))
        self.returns_df.plot(kind='kde', ax=ax, alpha=0.7)

        ax.set_title("Return Distributions")
        ax.set_xlabel("Daily Return")
        ax.grid(True)
        ax.legend(title="Assets")

        plt.tight_layout()
        plt.show()

    def equal_portfolio(self):
        """Compute the equal-weight portfolio.

        Returns:
            pd.Series: Equal weights for each asset.
        """
        weights = np.ones(len(self.mu)) / len(self.mu)
        return pd.Series(weights, index=self.mu.index)

    def tangency_portfolio(self, short=True):
        """Compute the tangency portfolio that maximizes the Sharpe ratio.

        Parameters:
            short (bool): If True, uses closed-form solution (unconstrained); otherwise solves numerically with long-only constraint.

        Returns:
            pd.Series: Weights of the tangency portfolio.
        """
        if short:
            excess_returns = self.mu.values - self.risk_free_rate
            inv_sigma = np.linalg.inv(self.sigma.values)
            ones = np.ones(len(self.mu))

            w_unnormalized = inv_sigma @ excess_returns
            denom = ones @ w_unnormalized
            weights = w_unnormalized / denom

            return pd.Series(weights, index=self.mu.index)

        # Fall back to numerical optimization if short-selling is not allowed
        n = len(self.mu)

        def neg_sharpe(w):
            ret = w @ self.mu.values
            vol = np.sqrt(w @ self.sigma.values @ w.T)
            return -((ret - self.risk_free_rate) / vol)

        constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
        bounds = [(0, 1)] * n
        x0 = np.ones(n) / n

        result = optimize.minimize(neg_sharpe, x0, bounds=bounds, constraints=constraints)
        return pd.Series(result.x, index=self.mu.index)

    def gmvp(self, short=True):
        """Compute the Global Minimum Variance Portfolio (GMVP).

        Parameters:
            short (bool): If True, uses closed-form solution; otherwise solves constrained optimization.

        Returns:
            pd.Series: Weights of the GMVP.
        """
        if short:
            inv_sigma = np.linalg.inv(self.sigma.values)
            ones = np.ones(len(self.mu))
            weights = inv_sigma @ ones / (ones @ inv_sigma @ ones)
            return pd.Series(weights, index=self.mu.index)

        n = len(self.mu)
        w = cp.Variable(n)
        objective = cp.Minimize(cp.quad_form(w, self.sigma.values))
        constraints = [cp.sum(w) == 1, w >= 0]
        problem = cp.Problem(objective, constraints)
        problem.solve()

        if w.value is not None:
            return pd.Series(w.value, index=self.mu.index)
        else:
            raise ValueError("Constrained GMVP optimization failed.")

    def minimum_risk_portfolio_given_return(self, target_return, short=True):
        """Compute the minimum-risk portfolio for a given target return.

        Parameters:
            target_return (float): Desired portfolio return.
            short (bool): If True, allows short-selling; otherwise enforces long-only constraint.

        Returns:
            pd.Series: Weights of the optimized portfolio.

        Raises:
            ValueError: If optimization fails.
        """
        n = len(self.mu)
        w = cp.Variable(n)
        objective = cp.Minimize(cp.quad_form(w, self.sigma.values))

        constraints = [
            cp.sum(w) == 1,
            self.mu.values @ w == target_return
        ]

        if not short:
            constraints.append(w >= 0)

        prob = cp.Problem(objective, constraints)
        prob.solve()

        if w.value is not None:
            return pd.Series(w.value, index=self.mu.index)
        else:
            raise ValueError("Optimization failed.")

    def max_return_portfolio_given_risk(self, target_vol, short=True):
        """Compute the maximum-return portfolio for a given level of volatility.

        Parameters:
            target_vol (float): Target portfolio volatility.
            short (bool): If True, allows short-selling; otherwise enforces long-only constraint.

        Returns:
            pd.Series: Weights of the optimized portfolio.

        Raises:
            ValueError: If optimization fails.
        """
        n = len(self.mu)
        w = cp.Variable(n)
        ret = self.mu.values @ w
        objective = cp.Maximize(ret)

        constraints = [
            cp.sum(w) == 1,
            cp.quad_form(w, self.sigma.values) <= target_vol ** 2
        ]

        if not short:
            constraints.append(w >= 0)

        prob = cp.Problem(objective, constraints)
        prob.solve()

        if w.value is not None:
            return pd.Series(w.value, index=self.mu.index)
        else:
            raise ValueError("Optimization failed.")

    def two_fund_mix(self, w1, w2, t):
        """Compute a convex combination of two portfolios.

        Parameters:
            w1 (pd.Series): First portfolio weights.
            w2 (pd.Series): Second portfolio weights.
            t (float): Mixing coefficient in [0, 1].

        Returns:
            np.ndarray: Combined portfolio weights.
        """
        return t * w1 + (1 - t) * w2

    def efficient_frontier(self, n_points=100, short=True):
        """Construct the efficient frontier using either two-fund mix or constrained optimization.

        Parameters:
            n_points (int): Number of points to evaluate along the frontier.
            short (bool): If True, uses two-fund mix; otherwise uses constrained optimization.

        Returns:
            pd.DataFrame: DataFrame with columns ['Volatility', 'Return', 'Sharpe'].
        """
        if short:
            # Tangency Portfolio
            w_tangency = self.tangency_portfolio(short)
            mu_tangency, vol_tangency, _ = self.portfolio_performance(w_tangency)

            # GMVP
            w_gmvp = self.gmvp(short)
            mu_gmvp, vol_gmvp, _ = self.portfolio_performance(w_gmvp)

            frontier = []
            for t in np.linspace(0,3,n_points):
                w = self.two_fund_mix(w_tangency, w_gmvp, t)
                port_return, port_vol, sharpe = self.portfolio_performance(w)
                frontier.append((port_vol, port_return, sharpe))

            return pd.DataFrame(frontier, columns=['Volatility', 'Return', 'Sharpe'])

        min_return = self.mu.min()
        max_return = self.mu.max()
        target_returns = np.linspace(min_return, max_return, n_points)

        frontier = []
        for r in target_returns:
            try:
                w = self.minimum_risk_portfolio_given_return(r, short)
                port_return, port_vol, sharpe = self.portfolio_performance(w)
                frontier.append((port_vol, port_return, sharpe))
            except:
                continue

        return pd.DataFrame(frontier, columns=['Volatility', 'Return', 'Sharpe'])

    def portfolio_performance(self, weights):
        """Calculate the expected return, volatility, and Sharpe ratio for a portfolio.

        Parameters:
            weights (array-like): Portfolio weights.

        Returns:
            tuple: (expected return, volatility, Sharpe ratio)
        """
        weights = np.array(weights)
        port_return = weights @ self.mu.values
        port_volatility = np.sqrt(weights @ self.sigma.values @ weights)
        sharpe_ratio = (port_return - self.risk_free_rate) / port_volatility
        return port_return, port_volatility, sharpe_ratio

    def compare_strategies(self):
        """Compare performance of various portfolio strategies:
        - Equal-weight portfolio
        - Unconstrained GMVP and tangency portfolio
        - Constrained (long-only) GMVP and tangency portfolio
        - Individual assets

        Prints a summary of weights and performance metrics.
        """
        w_equal = np.ones(len(self.mu)) / len(self.mu)
        w_gmvp = self.gmvp()
        w_cgmvp = self.gmvp(short=False)
        w_tan = self.tangency_portfolio()
        w_ctan = self.tangency_portfolio(short=False)

        r_equal, v_equal, s_equal = self.portfolio_performance(w_equal)
        r_gmvp, v_gmvp, s_gmvp = self.portfolio_performance(w_gmvp)
        r_cgmvp, v_cgmvp, s_cgmvp = self.portfolio_performance(w_cgmvp)
        r_tan, v_tan, s_tan = self.portfolio_performance(w_tan)
        r_ctan, v_ctan, s_ctan = self.portfolio_performance(w_ctan)

        print("Equal Weight Portfolio:")
        print(pd.Series(w_equal, index=self.mu.index).apply(lambda x: f"{x:.2%}"))
        print(f"Return: {r_equal:.2%}, Volatility: {v_equal:.2%}, Sharpe: {s_equal:.2f}\n")

        print("GMVP:")
        print(w_gmvp.apply(lambda x: f"{x:.2%}"))
        print(f"Return: {r_gmvp:.2%}, Volatility: {v_gmvp:.2%}, Sharpe: {s_gmvp:.2f}\n")

        print("Constrained GMVP (Long-only):")
        print(w_cgmvp.apply(lambda x: f"{x:.2%}"))
        print(f"Return: {r_cgmvp:.2%}, Volatility: {v_cgmvp:.2%}, Sharpe: {s_cgmvp:.2f}\n")

        print("Tangency Portfolio:")
        print(w_tan.apply(lambda x: f"{x:.2%}"))
        print(f"Return: {r_tan:.2%}, Volatility: {v_tan:.2%}, Sharpe: {s_tan:.2f}\n")

        print("Constrained Tangency Portfolio (Long-only):")
        print(w_ctan.apply(lambda x: f"{x:.2%}"))
        print(f"Return: {r_ctan:.2%}, Volatility: {v_ctan:.2%}, Sharpe: {s_ctan:.2f}\n")

        print("Individual Asset Performance:")
        for ticker in self.mu.index:
            unit_vector = np.zeros(len(self.mu))
            unit_vector[self.mu.index.get_loc(ticker)] = 1.0
            r, v, s = self.portfolio_performance(unit_vector)
            print(f"{ticker}: Return: {r:.2%}, Volatility: {v:.2%}, Sharpe: {s:.2f}")

    def rolling_sharpe_ratio(self, window=63):
        """Compute the rolling Sharpe ratio of the equal-weight portfolio.

        Parameters:
            window (int): Rolling window size in days. Default is 63 (1 quarter).

        Returns:
            pd.Series: Rolling Sharpe ratio indexed by date.
        """
        weights = np.ones(len(self.mu)) / len(self.mu)
        portfolio_returns = self.returns_df @ weights
        rolling_mean = portfolio_returns.rolling(window).mean()
        rolling_std = portfolio_returns.rolling(window).std()
        sharpe = (rolling_mean - self.risk_free_rate / 252) / rolling_std
        return sharpe

    def value_at_risk(self, weights, alpha=0.05):
        """Compute the parametric Value at Risk (VaR) for a portfolio.

        Parameters:
            weights (array-like): Portfolio weights.
            alpha (float): Significance level (e.g., 0.05 for 95% VaR).

        Returns:
            float: Estimated daily Value at Risk.
        """
        weights = np.array(weights)
        mean = weights @ self.mu.values / 252
        std = np.sqrt(weights @ self.sigma.values @ weights.T) / np.sqrt(252)
        z = stats.norm().ppf(alpha)
        return -(mean + z * std)

    def optimize_custom_objective(self, objective_fn, bounds=None, constraints=None):
        """Optimize a custom user-defined portfolio objective function.

        Parameters:
            objective_fn (callable): Function to minimize; accepts portfolio weights.
            bounds (list of tuple, optional): Bounds on weights.
            constraints (list or dict, optional): Constraints for optimization.

        Returns:
            pd.Series: Optimized portfolio weights.

        Raises:
            ValueError: If optimization fails.
        """
        n = len(self.mu)
        x0 = np.ones(n) / n
        result = optimize.minimize(objective_fn, x0, bounds=bounds, constraints=constraints)
        if result.success:
            return pd.Series(result.x, index=self.mu.index)
        else:
            raise ValueError("Custom optimization failed.")

    def zero_beta_portfolio(self, short=True):
        """Compute a portfolio with zero covariance with the tangency portfolio.

        Parameters:
            short (bool): If True, allows short-selling; else, long-only.

        Returns:
            pd.Series: Weights of the zero-beta portfolio.
        """
        w_tan = self.tangency_portfolio(short)
        r_c = self.returns_df @ w_tan

        def objective(w):
            r_p = self.returns_df @ w
            return np.abs(np.cov(r_p, r_c)[0, 1])  # minimize absolute covariance

        constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1}]
        bounds = None if short else [(0, 1)] * len(self.mu)
        x0 = np.ones(len(self.mu)) / len(self.mu)

        result = optimize.minimize(objective, x0, bounds=bounds, constraints=constraints)
        return pd.Series(result.x, index=self.mu.index)

    def plot_zero_beta_portfolio(self, ax, short=True):
        """Plot the zero-beta portfolio on the return-volatility diagram.

        Parameters:
            ax (matplotlib.axes.Axes): Plotting axis.
            short (bool): Whether to allow short selling.
        """
        w_zb = self.zero_beta_portfolio(short)
        mu_zb, vol_zb, _ = self.portfolio_performance(w_zb)
        ax.plot([vol_zb], [mu_zb], 'o', color='black', label='Zero-Beta')
        ax.annotate('Zero-Beta', (vol_zb, mu_zb))

    def plot_zero_beta_line(self, ax, short=True):
        """Plot Black's CAPM line from the zero-beta portfolio.

        Parameters:
            ax (matplotlib.axes.Axes): Plotting axis.
            short (bool): Whether to allow short selling.
        """
        w_tan = self.tangency_portfolio(short)
        w_zb = self.zero_beta_portfolio(short)
        mu_tan, vol_tan, _ = self.portfolio_performance(w_tan)
        mu_zb, vol_zb, _ = self.portfolio_performance(w_zb)

        slope = (mu_tan - mu_zb) / (vol_tan - 0)
        x_vals = np.linspace(0, vol_tan * 1.5, 100)
        y_vals = mu_zb + slope * x_vals
        ax.plot(x_vals, y_vals, linestyle='-.', color='purple', label="Zero-Beta Line")

    def plot_theoretical_vs_empirical_frontier(self, ax):
        """Compare theoretical and empirical efficient frontiers."""
        df_theory = self.efficient_frontier(short=True)
        df_empirical = self.efficient_frontier(short=False)

        ax.plot(df_theory.Volatility, df_theory.Return, label='Markowitz Bullet (Short Selling Allowed)', color='blue')
        ax.plot(df_empirical.Volatility, df_empirical.Return, label='Markowitz Bullet (Long-Only)', color='orange')
        ax.set_xlabel("Volatility (σ)")
        ax.set_ylabel("Expected Return (μ)")
        ax.grid(True)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    def plot_return_beta_lines(self, ax):
        """Plot return vs beta under CAPM and Black's CAPM assumptions.

        Parameters:
            ax (matplotlib.axes.Axes): Plotting axis.
        """
        # Standard CAPM beta approximation: regression vs equal-weight market proxy
        market_weights = np.ones(len(self.mu)) / len(self.mu)
        market_return = self.returns_df @ market_weights
        asset_returns = self.returns_df

        # Compute CAPM betas for each asset
        betas_capm = []
        for ticker in self.mu.index:
            cov = np.cov(asset_returns[ticker], market_return)[0, 1]
            var = np.var(market_return)
            beta = cov / var if var > 0 else np.nan
            betas_capm.append(beta)
        betas_capm = np.array(betas_capm)
        returns = self.mu.values

        # Regression for CAPM line
        capm_fit = np.polyfit(betas_capm, returns, 1)
        beta_vals = np.linspace(betas_capm.min() - 0.1, betas_capm.max() + 0.1, 100)
        capm_line = np.polyval(capm_fit, beta_vals)

        # Black CAPM (relative to tangency portfolio)
        w_tan = self.tangency_portfolio()
        r_c = self.returns_df @ w_tan
        tangency_var = r_c.var()

        betas_black = self.returns_df.cov().dot(w_tan) / tangency_var
        betas_black = betas_black.values

        black_fit = np.polyfit(betas_black, returns, 1)
        black_line = np.polyval(black_fit, beta_vals)

        # Plot data
        ax.scatter(betas_capm, returns, label='Assets (CAPM)', color='blue', alpha=0.6)

        # Annotate with asset names
        for i, ticker in enumerate(self.mu.index):
            ax.annotate(ticker, (betas_capm[i] + 0.02, returns[i]), fontsize=9)

        # Plot CAPM and Black's CAPM lines
        ax.plot(beta_vals, capm_line, label='CAPM Line', color='blue', linestyle='--')
        ax.plot(beta_vals, black_line, label="Black's CAPM Line", color='purple', linestyle='-.')

        # Formatting
        ax.set_title("Return vs Beta: Standard CAPM vs Black's CAPM")
        ax.set_xlabel("Beta")
        ax.set_ylabel("Expected Return")
        ax.grid(True)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    def compute_alpha_table(self):
        """Compute alpha values for each asset under both CAPM and Black's CAPM.

        Returns:
            pd.DataFrame: Table with columns ['Expected Return', 'Beta (CAPM)', 'Alpha (CAPM)',
                                            'Beta (Black)', 'Alpha (Black)']
        """
        rf = self.risk_free_rate
        mu_i = self.mu.copy()

        # ----- CAPM Part -----
        # Market proxy: equal-weight portfolio
        w_mkt = np.ones(len(mu_i)) / len(mu_i)
        r_mkt = self.returns_df @ w_mkt
        E_rm = r_mkt.mean() * 252
        var_rm = r_mkt.var()

        betas_capm = []
        alphas_capm = []
        for ticker in mu_i.index:
            cov = np.cov(self.returns_df[ticker], r_mkt)[0, 1]
            beta = cov / var_rm if var_rm > 0 else np.nan
            expected = rf + beta * (E_rm - rf)
            alpha = mu_i[ticker] - expected
            betas_capm.append(beta)
            alphas_capm.append(alpha)

        # ----- Black's CAPM Part -----
        w_tan = self.tangency_portfolio()
        r_c = self.returns_df @ w_tan
        E_rc = r_c.mean() * 252
        var_rc = r_c.var()
        w_zb = self.zero_beta_portfolio()
        c = (self.returns_df @ w_zb).mean() * 252

        cov_matrix = self.returns_df.cov()
        betas_black = cov_matrix @ w_tan / var_rc
        alphas_black = mu_i - (c + betas_black * (E_rc - c))

        # Assemble the result
        df = pd.DataFrame({
            'Expected Return': mu_i,
            'Beta (CAPM)': betas_capm,
            'Alpha (CAPM)': alphas_capm,
            'Beta (Black)': betas_black,
            'Alpha (Black)': alphas_black
        })

        return df.round(4)