import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Requires: BlackScholes class
# from black_scholes_CLASS import BlackScholes

class DeltaHedgingSimulator(BlackScholes):
    """
    Simulates delta hedging for a European call or put option using the Black-Scholes model.
    Inherits from the BlackScholes class for analytic pricing and GBM path generation.

    This class allows:
    - Tracking of discrete-time delta-hedged portfolio.
    - Comparison of replicating portfolio value vs. theoretical option price.
    - Evaluation of hedging error over a single or many paths.

    Parameters:
    -----------
    S0 : float
        Initial stock price.
    K : float
        Strike price.
    T : float
        Time to maturity (in years).
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility of the underlying asset.
    n : int
        Number of discrete hedging intervals.
    option_type : str
        'call' or 'put'.
    """

    def __init__(self, S0, K, T, r, sigma, n, option_type='call'):
        super().__init__(S0=S0, K=K, maturity_time=T, r=r, sigma=sigma)
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.n = n
        self.dt = T / n
        self.option_type = option_type.lower()

        assert self.option_type in ['call', 'put'], "option_type must be 'call' or 'put'"

        # Allocate arrays to store hedging dynamics for a single path
        self.S_path = []  # Stock path
        self.d1 = np.zeros(n + 1)
        self.d2 = np.zeros(n + 1)
        self.N_stock = np.zeros(n + 1)  # Delta (stock units)
        self.N_bond = np.zeros(n + 1)   # Bond or money market account (MMA)

        # Portfolio components and value tracking
        self.stock_value = np.zeros(n + 1)
        self.bond_value = np.zeros(n + 1)
        self.portfolio_value = np.zeros(n + 1)
        self.option_value = np.zeros(n + 1)  # Theoretical value from BSM
        self.hedging_error = np.zeros(n + 1)

        # End-of-period values after each interval
        self.stock_value_end = np.zeros(n + 1)
        self.bond_value_end = np.zeros(n + 1)
        self.portfolio_value_end = np.zeros(n + 1)

    def _black_scholes_price_and_delta(self, S, tau):
        """
        Compute the Black-Scholes price and delta at time-to-maturity tau.

        Handles both scalar and array inputs.

        Parameters:
        -----------
        S : float or np.ndarray
            Current stock price(s).
        tau : float or np.ndarray
            Time to maturity.

        Returns:
        --------
        price : float or np.ndarray
            Option price.
        delta : float or np.ndarray
            Option delta.
        """
        tau = np.maximum(tau, 1e-10)  # Avoid division by zero
        is_scalar = np.isscalar(S)
        S = np.atleast_1d(S)

        if np.any(tau < 1e-8):  # Near expiration: use intrinsic payoff
            if self.option_type == 'call':
                price = np.maximum(S - self.K, 0)
                delta = np.where(S > self.K, 1.0, np.where(S < self.K, 0.0, 0.5))
            else:
                price = np.maximum(self.K - S, 0)
                delta = np.where(S < self.K, -1.0, np.where(S > self.K, 0.0, -0.5))
        else:
            d1 = (np.log(S / self.K) + (self.r + 0.5 * self.sigma ** 2) * tau) / (self.sigma * np.sqrt(tau))
            d2 = d1 - self.sigma * np.sqrt(tau)
            if self.option_type == 'call':
                price = S * stats.norm.cdf(d1) - self.K * np.exp(-self.r * tau) * stats.norm.cdf(d2)
                delta = stats.norm.cdf(d1)
            else:
                price = self.K * np.exp(-self.r * tau) * stats.norm.cdf(-d2) - S * stats.norm.cdf(-d1)
                delta = stats.norm.cdf(d1) - 1

        return (price.item(), delta.item()) if is_scalar else (price, delta)

    def simulate_single_path(self, seed=None):
        """
        Simulate a single delta-hedged path and record full portfolio evolution.
        """
        if seed is not None:
            np.random.seed(seed)

        S = self.S0
        self.S_path.append(S)
        tau = self.T

        # Initialize replicating portfolio
        price, delta = self._black_scholes_price_and_delta(S, tau)
        self.N_stock[0] = delta
        self.N_bond[0] = price - delta * S
        self.stock_value[0] = self.N_stock[0] * S
        self.bond_value[0] = self.N_bond[0]
        self.portfolio_value[0] = self.stock_value[0] + self.bond_value[0]
        self.option_value[0] = price
        self.hedging_error[0] = price - self.portfolio_value[0]

        # Time-stepping for delta rebalancing
        for i in range(self.n):
            tau = self.T - i * self.dt

            # Simulate stock movement (lognormal process)
            Z = np.random.normal()
            S *= np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + self.sigma * np.sqrt(self.dt) * Z)
            self.S_path.append(S)

            # Mark-to-market portfolio from previous delta hedge
            self.stock_value_end[i] = self.N_stock[i] * S
            self.bond_value_end[i] = self.N_bond[i] * np.exp(self.r * self.dt)
            self.portfolio_value_end[i] = self.stock_value_end[i] + self.bond_value_end[i]
            self.portfolio_value[i + 1] = self.portfolio_value_end[i]

            # Recompute hedge
            price, delta = self._black_scholes_price_and_delta(S, tau)
            self.N_stock[i + 1] = delta
            self.stock_value[i + 1] = delta * S
            self.N_bond[i + 1] = self.portfolio_value[i + 1] - self.stock_value[i + 1]
            self.bond_value[i + 1] = self.N_bond[i + 1]
            self.option_value[i + 1] = price
            self.hedging_error[i + 1] = price - self.portfolio_value[i + 1]

        # Final stock movement
        Z = np.random.normal()
        S *= np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + self.sigma * np.sqrt(self.dt) * Z)
        self.S_path.append(S)
        self.stock_value_end[self.n] = self.N_stock[self.n] * S
        self.bond_value_end[self.n] = self.N_bond[self.n] * np.exp(self.r * self.dt)
        self.portfolio_value_end[self.n] = self.stock_value_end[self.n] + self.bond_value_end[self.n]

    def plot_delta(self):
        """
        Plot the delta hedge over time for a single path.
        """
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(np.arange(self.n + 1), self.N_stock, 'o-b', label=f"Delta ({self.option_type.title()})")
        ax.set_xlabel('Time Step')
        ax.set_ylabel('Delta')
        ax.set_title(f'Delta Hedging – {self.option_type.title()} Option')
        ax.grid(True)
        ax.legend()
        plt.tight_layout()
        plt.show()

    def print_results(self):
        """
        Print full delta hedging report for a single path.
        """
        header = 'WEEK  OPTION_VAL  REPL_PORTF  HEDGE_ERR   DELTA   STOCK     MMA   T_at_END S_at_END B_at_END'
        print(header)
        row_fmt = '{:4d} {:11.2f} {:11.2f} {:10.2f} {:7.2f} {:7.2f} {:7.2f} {:10.2f} {:8.2f} {:8.2f}'
        for i in range(self.n + 1):
            print(row_fmt.format(
                i, self.option_value[i], self.portfolio_value[i], self.hedging_error[i],
                self.N_stock[i], self.stock_value[i], self.bond_value[i],
                self.portfolio_value_end[i], self.stock_value_end[i], self.bond_value_end[i]
            ))

    def simulate_many_paths(self, num_paths=1000):
        """
        Simulate multiple independent delta-hedged paths and analyze hedging error.

        Parameters:
        -----------
        num_paths : int
            Number of Monte Carlo simulations.

        Returns:
        --------
        hedging_error : np.ndarray
            Array of terminal hedging errors.
        """
        dt, n, T = self.dt, self.n, self.T
        S = np.full((num_paths,), self.S0, dtype=float)
        N_stock = np.zeros(num_paths)
        N_bond = np.zeros(num_paths)
        portfolio_value = np.zeros(num_paths)

        tau = T
        price, delta = self._black_scholes_price_and_delta(S, tau)
        N_stock[:] = delta
        N_bond[:] = price - delta * S
        portfolio_value[:] = price

        for i in range(n):
            Z = np.random.randn(num_paths)
            S *= np.exp((self.r - 0.5 * self.sigma ** 2) * dt + self.sigma * np.sqrt(dt) * Z)
            tau = T - (i + 1) * dt
            price, delta = self._black_scholes_price_and_delta(S, tau)

            stock_value = N_stock * S
            bond_value = N_bond * np.exp(self.r * dt)
            portfolio_value = stock_value + bond_value

            N_stock = delta
            N_bond = portfolio_value - N_stock * S

        Z = np.random.randn(num_paths)
        S *= np.exp((self.r - 0.5 * self.sigma ** 2) * dt + self.sigma * np.sqrt(dt) * Z)

        if self.option_type == 'call':
            option_payoff = np.maximum(S - self.K, 0)
        else:
            option_payoff = np.maximum(self.K - S, 0)

        final_hedge = N_stock * S + N_bond * np.exp(self.r * dt)
        hedging_error = final_hedge - option_payoff

        mean_error = np.mean(hedging_error)
        std_error = np.std(hedging_error)

        print(f"Simulated {num_paths} paths")
        print(f"Mean Hedging Error: {mean_error:.4f}")
        print(f"Std Dev of Hedging Error: {std_error:.4f}")

        # Plot histogram of errors
        plt.figure(figsize=(8, 4))
        plt.hist(hedging_error, bins=40, density=True, alpha=0.7, color='skyblue')
        plt.axvline(mean_error, color='red', linestyle='--', label=f"Mean = {mean_error:.4f}")
        plt.title("Distribution of Hedging Errors")
        plt.xlabel("Hedging Error")
        plt.ylabel("Density")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

        return hedging_error