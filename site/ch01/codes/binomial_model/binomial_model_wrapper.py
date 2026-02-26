# ============================================================================
# binomial_model/binomial_model_wrapper.py
# ============================================================================
from .binomial_model_parameter import BinomialParameter
from .binomial_model_plotter import BinomialPlotter
from .binomial_model_pricer import BinomialPricer


class BinomialModel:
    """
    A class for pricing options using risk-neutral binomial tree methods.
    
    This is the main interface that combines all binomial model functionality
    and provides backward compatibility with the original monolithic class.
    
    Attributes:
    -----------
    S0 : float
        Initial stock price
    K : float
        Strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate
    sigma : float
        Volatility of the underlying asset
    M : int
        Number of time steps in the binomial tree
    model : str
        Binomial model to use: 'CRR', 'JR', or 'Wilmott'
    params : BinomialParameter
        Parameter object containing computed binomial parameters
    pricer : BinomialPricer
        Pricer object for option valuation
    plotter : BinomialPlotter
        Plotter object for tree visualization
    
    Methods:
    --------
    risk_neutral_valuation(option_type='call', american=False, barrier=None)
        Prices call/put options with risk-neutral backward induction
    state_price_valuation(option_type='call')
        Prices European call and put options using Arrow-Debreu state prices
    plot_tree()
        Visualizes the binomial tree of stock price evolution
    """
    
    def __init__(self, S0, K, T, r, sigma, M, model='JR'):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.M = M
        self.model = model
        
        # Create parameter object
        self.params = BinomialParameter(r, sigma, T, M, model)
        
        # Create pricer and plotter
        self.pricer = BinomialPricer(S0, K, self.params)
        self.plotter = BinomialPlotter(S0, self.params)
    
    def risk_neutral_valuation(self, option_type='call', american=False, barrier=None):
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
        return self.pricer.price_risk_neutral(option_type, american, barrier)
    
    def state_price_valuation(self, option_type='call'):
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
        return self.pricer.price_state_space(option_type)

    def plot_tree(self, figsize=(12, 8), title=None, show=True, save_path=None):
        """
        Visualize the binomial tree for stock price evolution.
        
        Parameters:
        -----------
        figsize : tuple
            Figure size (width, height)
        title : str, optional
            Custom title for the plot
        show : bool
            Whether to display the plot (default True)
        save_path : str, optional
            Path to save the figure
        
        Returns:
        --------
        tuple or None
            Figure and axis objects if show=False, None otherwise
        """
        # Call the plotter with all parameters
        result = self.plotter.plot_tree(
            figsize=figsize, 
            title=title, 
            show=show, 
            save_path=save_path
        )
        
        # Return the result (fig, ax) if show=False, otherwise None
        return result if not show else None
    
    # Properties for easy access to parameters (backward compatibility)
    @property
    def U(self):
        """Up movement factor"""
        return self.params.U
    
    @property
    def D(self):
        """Down movement factor"""
        return self.params.D
    
    @property
    def q_u(self):
        """Risk-neutral probability of up movement"""
        return self.params.q_u
    
    @property
    def q_d(self):
        """Risk-neutral probability of down movement"""
        return self.params.q_d
    
    @property
    def dt(self):
        """Time step size"""
        return self.params.dt