import numpy as np
import matplotlib.pyplot as plt

class OptionReplication:
    def __init__(self, K=100, S_min=50, S_max=150, num_points=500):
        self.K = K
        self.S_T = np.linspace(S_min, S_max, num_points)

    def call_payoff(self, K=None):
        K = self.K if K is None else K
        return np.maximum(self.S_T - K, 0)

    def put_payoff(self, K=None):
        K = self.K if K is None else K
        return np.maximum(K - self.S_T, 0)

    def binary_call_payoff(self, K=None):
        K = self.K if K is None else K
        return (self.S_T > K).astype(float)

    def binary_put_payoff(self, K=None):
        K = self.K if K is None else K
        return (self.S_T < K).astype(float)

    def quanto_call_payoff(self, Q=10, K=None):
        return Q * self.binary_call_payoff(K)

    def quanto_put_payoff(self, Q=10, K=None):
        return Q * self.binary_put_payoff(K)

    def plot_call_vs_binary(self, K=None):
        K = self.K if K is None else K
        call = self.call_payoff(K)
        binary = self.binary_call_payoff(K)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self.S_T, call, label=f'Call: max($S_T - {K}$, 0)', lw=2)
        ax.plot(self.S_T, binary, '--', label=f'Binary: $\mathbf{{1}}_{{S_T > {K}}}$', lw=2)
        ax.axvline(K, color='gray', linestyle=':', label=f'Strike $K = {K}$')
        ax.set_title(f"Call vs Binary Call Payoff (K = {K})")
        ax.set_xlabel("Terminal Price $S_T$")
        ax.set_ylabel("Payoff")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_put_vs_binary(self, K=None):
        K = self.K if K is None else K
        put = self.put_payoff(K)
        binary = self.binary_put_payoff(K)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self.S_T, put, label=f'Put: max({K} - $S_T$, 0)', lw=2)
        ax.plot(self.S_T, binary, '--', label=f'Binary: $\mathbf{{1}}_{{S_T < {K}}}$', lw=2)
        ax.axvline(K, color='gray', linestyle=':', label=f'Strike $K = {K}$')
        ax.set_title(f"Put vs Binary Put Payoff (K = {K})")
        ax.set_xlabel("Terminal Price $S_T$")
        ax.set_ylabel("Payoff")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_call_vs_quanto(self, Q=10, K=None):
        K = self.K if K is None else K
        call = self.call_payoff(K)
        quanto = self.quanto_call_payoff(Q, K)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self.S_T, call, label=f'Call: max($S_T - {K}$, 0)', lw=2)
        ax.plot(self.S_T, quanto, '--', label=f'Quanto: {Q} if $S_T > {K}$', lw=2)
        ax.axvline(K, color='gray', linestyle=':', label=f'Strike $K = {K}$')
        ax.set_title(f"Call vs Quanto Call Payoff (K = {K})")
        ax.set_xlabel("Terminal Price $S_T$")
        ax.set_ylabel("Payoff")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_put_vs_quanto(self, Q=10, K=None):
        K = self.K if K is None else K
        put = self.put_payoff(K)
        quanto = self.quanto_put_payoff(Q, K)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self.S_T, put, label=f'Put: max({K} - $S_T$, 0)', lw=2)
        ax.plot(self.S_T, quanto, '--', label=f'Quanto: {Q} if $S_T < {K}$', lw=2)
        ax.axvline(K, color='gray', linestyle=':', label=f'Strike $K = {K}$')
        ax.set_title(f"Put vs Quanto Put Payoff (K = {K})")
        ax.set_xlabel("Terminal Price $S_T$")
        ax.set_ylabel("Payoff")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()

    def fit_payoff_with_basis(self, target_fn, K_grid, basis='binary', Q=1.0, option_type='call'):
        """
        Fit a target payoff using binary or quanto options across a range of strikes.

        Parameters:
        - target_fn: callable, a function of S_T
        - K_grid: array-like, list of strikes to use in the basis
        - basis: 'binary' or 'quanto'
        - Q: payoff amount for quanto options
        - option_type: 'call' or 'put' basis functions

        Returns:
        - weights: optimal weights for each basis component
        """
        target = target_fn(self.S_T)
        A = []
        for K in K_grid:
            if basis == 'binary':
                if option_type == 'call':
                    col = self.binary_call_payoff(K)
                elif option_type == 'put':
                    col = self.binary_put_payoff(K)
            elif basis == 'quanto':
                if option_type == 'call':
                    col = self.quanto_call_payoff(Q=Q, K=K)
                elif option_type == 'put':
                    col = self.quanto_put_payoff(Q=Q, K=K)
            else:
                raise ValueError("basis must be 'binary' or 'quanto'")
            A.append(col)

        A = np.column_stack(A)
        weights, _, _, _ = np.linalg.lstsq(A, target, rcond=None)
        fitted = A @ weights

        self.plot_fitted_vs_target(target, fitted, basis=basis)
        return weights

    def plot_fitted_vs_target(self, target, fitted, basis='binary'):
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self.S_T, target, label='Target Payoff', lw=2)
        ax.plot(self.S_T, fitted, '--', label=f'Fitted using {basis} options', lw=2)
        ax.set_title("Target vs Fitted Payoff")
        ax.set_xlabel("Terminal Price $S_T$")
        ax.set_ylabel("Payoff")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()