# Displaced Diffusion Implied Volatility

## Background

Created on August 25 2021
Displaced Diffusion and implied volatilities

This code is purely educational and comes from "Financial Engineering" course by L.A. Grzelak
The course is based on the book “Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes”,
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak

---

## Code

```python
#%%
"""
Created on August 25 2021
Displaced Diffusion and implied volatilities

This code is purely educational and comes from "Financial Engineering" course by L.A. Grzelak
The course is based on the book “Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes”,
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import scipy.optimize as optimize
import enum 


# ======================================================================
# Functions / Classes
# ======================================================================

# set i= imaginary number


# ======================================================================
# Main
# ======================================================================

if __name__ == "__main__":
    i   = np.complex(0.0,1.0)

    # time-step needed for differentiation
    dt = 0.0001
 
    # ======================================================================
    # This class defines puts and calls
    class OptionType(enum.Enum):
        CALL = 1.0
        PUT = -1.0
    
    # Black-Scholes Call option price
    def BS_Call_Option_Price(CP,S_0,K,sigma,tau,r):
        if K is list:
            K = np.array(K).reshape([len(K),1])
        d1    = (np.log(S_0 / K) + (r + 0.5 * np.power(sigma,2.0)) * tau) / (sigma * np.sqrt(tau))
        d2    = d1 - sigma * np.sqrt(tau)
        if CP == OptionType.CALL:
            value = st.norm.cdf(d1) * S_0 - st.norm.cdf(d2) * K * np.exp(-r * tau)
        elif CP == OptionType.PUT:
            value = st.norm.cdf(-d2) * K * np.exp(-r * tau) - st.norm.cdf(-d1)*S_0
        return value

    # Implied volatility method
    def ImpliedVolatilityBlack76_xxx(CP,marketPrice,K,T,S_0):
        func = lambda sigma: np.power(BS_Call_Option_Price(CP,S_0,K,sigma,T,0.0) - marketPrice, 1.0)
        impliedVol = optimize.newton(func, 0.2, tol=1e-9)
        #impliedVol = optimize.brent(func, brack= (0.05, 2))
        return impliedVol

    # Implied volatility method
    def ImpliedVolatilityBlack76(CP,marketPrice,K,T,S_0):
        # To determine initial volatility we interpolate define a grid for sigma
        # and interpolate on the inverse
        sigmaGrid = np.linspace(0.0,2.0,5000)
        optPriceGrid = BS_Call_Option_Price(CP,S_0,K,sigmaGrid,T,0.0)
        sigmaInitial = np.interp(marketPrice,optPriceGrid,sigmaGrid)
        print("Initial volatility = {0}".format(sigmaInitial))
    
        # Use determined input for the local-search (final tuning)
        func = lambda sigma: np.power(BS_Call_Option_Price(CP,S_0,K,sigma,T,0.0) - marketPrice, 1.0)
        impliedVol = optimize.newton(func, sigmaInitial, tol=1e-5)
        print("Final volatility = {0}".format(impliedVol))
        return impliedVol

    def DisplacedDiffusionModel_CallPrice(K,P0T,beta,sigma,frwd,T):
         d1    = (np.log(frwd / (beta*K+(1.0-beta)*frwd)) + 0.5 * np.power(sigma*beta,2.0) * T) / (sigma * beta* np.sqrt(T))
         d2    = d1 - sigma * beta * np.sqrt(T)
         return P0T(T) * (frwd/beta * st.norm.cdf(d1) - (K + (1.0-beta)/beta*frwd) * st.norm.cdf(d2))

    def mainCalculation():
        CP  = OptionType.CALL
        
        K = np.linspace(0.3,2.8,22)
        K = np.array(K).reshape([len(K),1])
    
        # We define a ZCB curve (obtained from the market)
        P0T = lambda T: np.exp(-0.05*T) 
    
        # DD model parameters
        beta  = 0.5
        sigma = 0.15
    
        # Forward rate
        frwd = 1.0
    
        # Maturity
        T = 2.0
           
        # Effect of sigma
        plt.figure(1)
        plt.grid()
        plt.xlabel('strike, K')
        plt.ylabel('implied volatility')
        sigmaV = [0.1,0.2,0.3,0.4]
        legend = []
        for sigmaTemp in sigmaV:    
           callPrice = DisplacedDiffusionModel_CallPrice(K,P0T,beta,sigmaTemp,frwd,T)
           # Implied volatilities
           IV =np.zeros([len(K),1])
           for idx in range(0,len(K)):
               valCOSFrwd = callPrice[idx]/P0T(T)
               IV[idx] = ImpliedVolatilityBlack76(CP,valCOSFrwd,K[idx],T,frwd)
           plt.plot(K,IV*100.0)       
           legend.append('sigma={0}'.format(sigmaTemp))
           plt.ylim([0.0,60])
        plt.legend(legend)    
    
        # Effect of beta
        plt.figure(2)
        plt.grid()
        plt.xlabel('strike, K')
        plt.ylabel('implied volatility')
        betaV = [-0.5, 0.0001, 0.5, 1.0]
        legend = []
        for betaTemp in betaV:    
           callPrice = DisplacedDiffusionModel_CallPrice(K,P0T,betaTemp,sigma,frwd,T)
           # Implied volatilities
           IV =np.zeros([len(K),1])
           for idx in range(0,len(K)):
               valCOSFrwd = callPrice[idx]/P0T(T)
               IV[idx] = ImpliedVolatilityBlack76(CP,valCOSFrwd,K[idx],T,frwd)
           plt.plot(K,IV*100.0)       
           legend.append('beta={0}'.format(betaTemp))
        plt.legend(legend)    
    
    mainCalculation()
```

## Exercises

**Exercise 1.**
The displaced diffusion model defines the forward process as $dF = \sigma\beta F\,dW$ instead of $dF = \sigma F\,dW$. Explain the role of $\beta$ and what happens when $\beta = 1$ and $\beta \to 0$.

??? success "Solution to Exercise 1"
    The parameter $\beta$ controls the mixture between lognormal ($\beta = 1$) and normal ($\beta = 0$) dynamics. At $\beta = 1$, the model reduces to standard Black-Scholes with lognormal returns. As $\beta \to 0$, the dynamics become $dF = \sigma F_0\,dW$ (approximately), yielding normal (Bachelier) dynamics. Intermediate values of $\beta$ generate implied volatility skews: $\beta < 1$ produces downward-sloping skew (higher implied vol for low strikes), while negative $\beta$ can produce upward-sloping skew.

---

**Exercise 2.**
The displaced diffusion call price is computed using a shifted Black-Scholes formula. Write the modified strike and forward that enter the standard Black-Scholes formula.

??? success "Solution to Exercise 2"
    The displaced diffusion call price uses the substitutions:

    $$
    F_{\text{eff}} = \frac{F}{\beta}, \qquad K_{\text{eff}} = K + \frac{1 - \beta}{\beta}F, \qquad \sigma_{\text{eff}} = \sigma\beta.
    $$

    The call price is then $P(0,T)\bigl[F_{\text{eff}}\,\mathcal{N}(d_1) - K_{\text{eff}}\,\mathcal{N}(d_2)\bigr]$ where $d_1$ and $d_2$ use $\sigma_{\text{eff}}\sqrt{T}$.

---

**Exercise 3.**
For $\beta = 0.5$, $\sigma = 0.15$, $F = 1.0$, $T = 2.0$, and strike $K = 1.0$ (ATM), compute the effective volatility $\sigma_{\text{eff}}$ and explain how it compares to the Black implied volatility.

??? success "Solution to Exercise 3"
    The effective volatility is $\sigma_{\text{eff}} = \sigma\beta = 0.15 \times 0.5 = 0.075 = 7.5\%$. This is the volatility parameter that enters the displaced Black-Scholes formula. The Black implied volatility (from inverting the standard Black formula at the displaced diffusion price) will generally differ from $7.5\%$ because the displaced diffusion model is not lognormal. At the money ($K = F$), the implied vol is approximately $\sigma_{\text{eff}}$ but deviates for away-from-the-money strikes, creating the skew.

---

**Exercise 4.**
The code plots implied volatility as a function of strike for different values of $\beta$. Describe the shape of the implied volatility smile for $\beta = -0.5$, $\beta = 0.5$, and $\beta = 1.0$.

??? success "Solution to Exercise 4"

    - $\beta = 1.0$: The model is pure lognormal, so the implied volatility is flat across all strikes (no skew, no smile).
    - $\beta = 0.5$: The implied volatility curve slopes downward from low strikes to high strikes, producing a negative skew. This is because low-strike options have relatively higher implied vol in the displaced diffusion framework.
    - $\beta = -0.5$: The skew reverses -- implied volatility slopes upward from low to high strikes. This behavior is unusual for equity markets but can be relevant for certain interest rate products. The negative $\beta$ effectively makes the diffusion coefficient increase with the forward rate.
