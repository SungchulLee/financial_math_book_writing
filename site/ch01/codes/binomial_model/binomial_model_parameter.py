# ============================================================================
# binomial_model/binomial_model_parameter.py
# ============================================================================
import numpy as np


class BinomialParameter:
    """
    Handles parameter calculations for binomial option pricing models.
    
    Attributes:
    -----------
    r : float
        Risk-free interest rate
    sigma : float
        Volatility of the underlying asset
    T : float
        Time to maturity (in years)
    M : int
        Number of time steps in the binomial tree
    model : str
        Binomial model to use: 'CRR', 'JR', or 'Wilmott'
    dt : float
        Time step size
    U : float
        Up movement factor
    D : float
        Down movement factor
    q_u : float
        Risk-neutral probability of up movement
    q_d : float
        Risk-neutral probability of down movement
    """
    
    def __init__(self, r, sigma, T, M, model='JR'):
        # Validate inputs
        if T <= 0:
            raise ValueError("Time to maturity must be positive")
        if M <= 0:
            raise ValueError("Number of steps must be positive")
        if sigma < 0:
            raise ValueError("Volatility must be non-negative")
        
        self.r = r
        self.sigma = sigma
        self.T = T
        self.M = M
        self.model = model
        
        self.dt = T / M
        self.U, self.D, self.q_u, self.q_d = self._compute_binomial_parameters()
    
    def _compute_binomial_parameters(self):
        """Compute binomial parameters based on the selected model."""
        dt = self.dt
        sqrt_dt = np.sqrt(dt)
        r, sigma = self.r, self.sigma
        
        if self.model == 'Wilmott':
            u, d = 1 + sigma * sqrt_dt, 1 - sigma * sqrt_dt
        elif self.model == 'CRR':
            u, d = np.exp(sigma * sqrt_dt), np.exp(-sigma * sqrt_dt)
        elif self.model == 'JR':
            drift = (r - 0.5 * sigma ** 2) * dt
            u = np.exp(drift + sigma * sqrt_dt)
            d = np.exp(drift - sigma * sqrt_dt)
        else:
            raise ValueError("Invalid model. Choose 'JR', 'CRR', or 'Wilmott'.")
        
        q_u = (np.exp(r * dt) - d) / (u - d)
        return u, d, q_u, 1 - q_u