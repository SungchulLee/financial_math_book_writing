# Mortgage Prepayment Incentives

## Background

Created on July 05  2021
Incentive function as a function of a swap rate or the differential w.r.t. "old" mortgage rate

This code is purely educational and comes from "Financial Engineering" course by L.A. Grzelak
The course is based on the book “Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes”,
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak and Emanuele Cassamassima

---

## Code

```python
#%%
"""
Created on July 05  2021
Incentive function as a function of a swap rate or the differential w.r.t. "old" mortgage rate

This code is purely educational and comes from "Financial Engineering" course by L.A. Grzelak
The course is based on the book “Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes”,
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak and Emanuele Cassamassima
"""
import numpy as np
import matplotlib.pyplot as plt

# ======================================================================

def Annuity(rate,notional,periods,CPR):
    # it returns a matrix M such that
    # M = [t  notional(t)  prepayment(t)  notional_quote(t)  interest_quote(t)  installment(t)]
    # WARNING! here "rate" and "periods" are quite general, the choice of getting year/month/day.. steps, depends on the rate
    # that the function receives. So, it is necessary to pass the correct rate to the function
    M = np.zeros((periods + 1,6))
    M[:,0] = np.arange(periods + 1) # we define the times
    M[0,1] = notional
    for t in range(1,periods + 1):
        # we are computing the installment at time t knowing the oustanding at time (t-1)
        remaining_periods = periods - (t - 1)  
        
        # Installment, C(t_i) 
        M[t,5] = rate * M[t-1,1]/(1 - 1/(1 + rate)**remaining_periods) 
        
        # Interest rate payment, I(t_i) = r * N(t_{i})
        M[t,4] = rate * M[t-1,1] 
        
        # Notional payment, Q(t_i) = C(t_i) - I(t_i)
        M[t,3] = M[t,5] - M[t,4] 
        
        # Prepayment, P(t_i)= Lambda * (N(t_i) -Q(t_i))
        M[t,2] = CPR * (M[t-1,1] - M[t,3]) 
        
        # notional, N(t_{i+1}) = N(t_{i}) - lambda * (Q(t_{i} + P(t_i)))
        M[t,1] = M[t-1,1] - M[t,3] - M[t,2] 
    return M

def mainCode():


    IncentiveFunction = lambda x : 0.04 + 0.1/(1 + np.exp(115 * (0.02-x))) 
    
    oldRate = 0.05
    newRate = np.linspace(-0.05,0.15,25)
    
    epsilon = oldRate-newRate
    incentive = IncentiveFunction(epsilon)
    
    plt.figure(1)
    plt.plot(newRate,incentive)
    plt.xlabel('S(t)')
    plt.ylabel('Incentive')
    plt.grid()
    
    plt.figure(2)
    plt.plot(epsilon,incentive)
    plt.xlabel('epsilon= K - S(t)')
    plt.ylabel('Incentive')
    plt.grid()

    return 0.0


if __name__ == "__main__":
    mainCode()
```

## Exercises

**Exercise 1.**
The incentive function is defined as $\Lambda(\varepsilon) = 0.04 + 0.1/(1 + e^{115(0.02 - \varepsilon)})$ where $\varepsilon = K - S(t)$ is the difference between the old mortgage rate and the current swap rate. Compute $\Lambda(0.05)$ and $\Lambda(-0.05)$.

??? success "Solution to Exercise 1"
    For $\varepsilon = 0.05$: $\Lambda(0.05) = 0.04 + 0.1/(1 + e^{115(0.02 - 0.05)}) = 0.04 + 0.1/(1 + e^{-3.45})$. Since $e^{-3.45} \approx 0.0317$: $\Lambda(0.05) = 0.04 + 0.1/1.0317 \approx 0.04 + 0.0969 = 0.137$.

    For $\varepsilon = -0.05$: $\Lambda(-0.05) = 0.04 + 0.1/(1 + e^{115(0.02 + 0.05)}) = 0.04 + 0.1/(1 + e^{8.05})$. Since $e^{8.05} \approx 3133$: $\Lambda(-0.05) \approx 0.04 + 0.1/3134 \approx 0.04$.

    When rates fall ($\varepsilon > 0$), the incentive is high ($13.7\%$ CPR). When rates rise ($\varepsilon < 0$), the incentive drops to the baseline $4\%$ CPR.

---

**Exercise 2.**
Explain the economic interpretation of the sigmoid shape of the incentive function. Why does prepayment not jump to $100\%$ immediately when refinancing is beneficial?

??? success "Solution to Exercise 2"
    The sigmoid shape captures several real-world frictions:

    1. **Transaction costs**: Refinancing involves fees (origination, appraisal, legal), so small rate differentials do not justify prepayment.
    2. **Information asymmetry**: Not all borrowers are aware of market rate changes or actively monitor rates.
    3. **Heterogeneous borrowers**: Some are rate-sensitive (prepay quickly), others are less responsive.
    4. **Lock-in effects**: Some borrowers cannot refinance due to credit deterioration, negative equity, or contractual constraints.

    The sigmoid smoothly transitions from the baseline CPR (around $4\%$) to the maximum (about $14\%$) as the rate differential increases, reflecting this gradual behavioral response.

---

**Exercise 3.**
If the old mortgage rate is $K = 5\%$ and the current swap rate drops to $S = 2\%$, compute $\varepsilon$ and the prepayment incentive.

??? success "Solution to Exercise 3"
    $$
    \varepsilon = K - S = 0.05 - 0.02 = 0.03.
    $$

    $$
    \Lambda(0.03) = 0.04 + \frac{0.1}{1 + e^{115(0.02 - 0.03)}} = 0.04 + \frac{0.1}{1 + e^{-1.15}}.
    $$

    Since $e^{-1.15} \approx 0.3166$: $\Lambda(0.03) = 0.04 + 0.1/1.3166 \approx 0.04 + 0.0760 = 0.116$.

    The CPR is approximately $11.6\%$, indicating strong prepayment activity. A 300 basis point rate differential triggers significant refinancing.

---

**Exercise 4.**
How would you modify the incentive function to model a "burnout" effect, where the prepayment rate decreases over time even if the rate differential remains favorable?

??? success "Solution to Exercise 4"
    Burnout occurs because the most rate-sensitive borrowers prepay first, leaving a pool of less responsive borrowers. To model this, multiply the incentive function by a time-dependent decay factor:

    $$
    \Lambda_{\text{burnout}}(\varepsilon, t) = \Lambda(\varepsilon) \times \bigl[\alpha + (1 - \alpha)e^{-\beta t}\bigr],
    $$

    where $\alpha \in (0,1)$ is the long-run prepayment fraction (the "floor") and $\beta > 0$ controls the burnout speed. Initially ($t = 0$) the full incentive applies; as $t$ increases, only the fraction $\alpha$ of borrowers remains responsive. Alternatively, one can condition on the path history of $\varepsilon$, reducing the incentive if $\varepsilon$ has been positive for many consecutive periods.
