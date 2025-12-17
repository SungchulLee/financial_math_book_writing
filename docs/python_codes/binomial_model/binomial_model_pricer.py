# ============================================================================
# binomial_model/binomial_model_pricer.py
# ============================================================================
import numpy as np
import scipy.special as special
from binomial_model import BinomialParameter


class BinomialPricer:
    """
    Handles option pricing using binomial tree methods.
    
    Attributes:
    -----------
    S0 : float
        Initial stock price
    K : float
        Strike price
    params : BinomialParameter
        Parameter object containing binomial model parameters
    """
    
    def __init__(self, S0, K, params: BinomialParameter):
        self.S0 = S0
        self.K = K
        self.params = params
    
    def price_risk_neutral(self, option_type='call', american=False, barrier=None):
        """
        Price a call or put option using risk-neutral valuation via backward induction.
        
        Parameters:
        -----------
        option_type : str
            'call' or 'put'
        american : bool
            If True, allows early exercise (American style)
        barrier : float or None
            If set, knocks out the option when price falls below this level
        
        Returns:
        --------
        float
            Option price
        """
        S0, K = self.S0, self.K
        U, D = self.params.U, self.params.D
        q_u = self.params.q_u
        r, dt, M = self.params.r, self.params.dt, self.params.M
        
        # Terminal stock prices
        ST = np.array([S0 * (U**j) * (D**(M - j)) for j in range(M + 1)])
        
        # Payoff at maturity
        if option_type == 'call':
            V = np.maximum(ST - K, 0)
        elif option_type == 'put':
            V = np.maximum(K - ST, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")
        
        # Backward induction
        for i in range(M - 1, -1, -1):
            ST = ST[:i + 1] / D
            V = np.exp(-r * dt) * (q_u * V[1:i + 2] + (1 - q_u) * V[0:i + 1])
            
            # Apply barrier condition
            if barrier is not None:
                V[ST <= barrier] = 0
            
            # Early exercise for American options
            if american:
                if option_type == 'call':
                    V = np.maximum(V, ST - K)
                elif option_type == 'put':
                    V = np.maximum(V, K - ST)
        
        return V[0]
    
    def price_state_space(self, option_type='call'):
        """
        Price European call and put options using stable Arrow–Debreu summation.
        
        Parameters:
        -----------
        option_type : str
            'call' or 'put'
        
        Returns:
        --------
        float
            Option price
        """
        S0, K = self.S0, self.K
        U, D = self.params.U, self.params.D
        q_u, q_d = self.params.q_u, self.params.q_d
        r, T, M = self.params.r, self.params.T, self.params.M
        
        # Binomial paths
        up = np.arange(M + 1)
        down = M - up
        
        # Log-space terminal stock prices
        log_stock = np.log(S0) + down * np.log(D) + up * np.log(U)
        stock = np.exp(log_stock)
        
        # Payoffs
        if option_type == 'call':
            V = np.maximum(stock - K, 0)
        elif option_type == 'put':
            V = np.maximum(K - stock, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")
        
        # Log-space binomial weights
        eps = 1e-14
        log_q_u = np.log(np.clip(q_u, eps, 1 - eps))
        log_q_d = np.log(np.clip(q_d, eps, 1 - eps))
        
        log_weights = (
            log_q_u * up +
            log_q_d * down +
            special.gammaln(M + 1) -
            special.gammaln(up + 1) -
            special.gammaln(down + 1)
        )
        
        # Combine and discount once
        weights = np.exp(log_weights - r * T)
        return np.sum(V * weights)