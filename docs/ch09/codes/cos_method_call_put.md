# Call and Put COS Method

## Background

Cos Method Call Put

Educational script demonstrating cos method call put concepts.

---

## Code

```python
"""
Cos Method Call Put

Educational script demonstrating cos method call put concepts.
"""

#@title Call and Put COS Method
# Source Code
# https://github.com/LechGrzelak/Computational-Finance-Course/blob/main/
# Lecture%2008-%20Fourier%20Transformation%20for%20Option%20Pricing/Materials/
# CallPut_COS_Method.py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import time

# ======================================================================

def CallPutOptionPriceCOSMthd(cf,CP,S0,r,tau,K,N,L):
    # cf   - characteristic function as a functon, in the book denoted as \varphi
    # CP   - C for call and P for put
    # S0   - Initial stock price
    # r    - interest rate (constant)
    # tau  - time to maturity
    # K    - list of strikes
    # N    - Number of expansion terms
    # L    - size of truncation domain (typ.:L=8 or L=10)

    # reshape K to a column vector
    K = np.array(K).reshape([len(K),1])

    #assigning i=sqrt(-1)
    i = np.complex(0.0,1.0)

    x0 = np.log(S0 / K)

    # truncation domain
    a = 0.0 - L * np.sqrt(tau)
    b = 0.0 + L * np.sqrt(tau)

    # sumation from k = 0 to k=N-1
    k = np.linspace(0,N-1,N).reshape([N,1])
    u = k * np.pi / (b - a);

    # Determine coefficients for Put Prices
    H_k = CallPutCoefficients(CP,a,b,k)

    mat = np.exp(i * np.outer((x0 - a) , u))

    temp = cf(u) * H_k
    temp[0] = 0.5 * temp[0]

    value = np.exp(-r * tau) * K * np.real(mat.dot(temp))

    return value

"""
Determine coefficients for Put Prices
"""
def CallPutCoefficients(CP,a,b,k):
    if str(CP).lower()=="c" or str(CP).lower()=="1":
        c = 0.0
        d = b
        coef = Chi_Psi(a,b,c,d,k)
        Chi_k = coef["chi"]
        Psi_k = coef["psi"]
        if a < b and b < 0.0:
            H_k = np.zeros([len(k),1])
        else:
            H_k      = 2.0 / (b - a) * (Chi_k - Psi_k)

    elif str(CP).lower()=="p" or str(CP).lower()=="-1":
        c = a
        d = 0.0
        coef = Chi_Psi(a,b,c,d,k)
        Chi_k = coef["chi"]
        Psi_k = coef["psi"]
        H_k      = 2.0 / (b - a) * (- Chi_k + Psi_k)

    return H_k

def Chi_Psi(a,b,c,d,k):
    psi = np.sin(k * np.pi * (d - a) / (b - a)) - np.sin(k * np.pi * (c - a)/(b - a))
    psi[1:] = psi[1:] * (b - a) / (k[1:] * np.pi)
    psi[0] = d - c

    chi = 1.0 / (1.0 + np.power((k * np.pi / (b - a)) , 2.0))
    expr1 = np.cos(k * np.pi * (d - a)/(b - a)) * np.exp(d)  - np.cos(k * np.pi
                  * (c - a) / (b - a)) * np.exp(c)
    expr2 = k * np.pi / (b - a) * np.sin(k * np.pi *
                        (d - a) / (b - a))   - k * np.pi / (b - a) * np.sin(k
                        * np.pi * (c - a) / (b - a)) * np.exp(c)
    chi = chi * (expr1 + expr2)

    value = {"chi":chi,"psi":psi }
    return value


def BS_Call_Option_Price(CP,S_0,K,sigma,tau,r):
    #Black-Scholes Call option price
    cp = str(CP).lower()
    K = np.array(K).reshape([len(K),1])
    d1    = (np.log(S_0 / K) + (r + 0.5 * np.power(sigma,2.0))
    * tau) / float(sigma * np.sqrt(tau))
    d2    = d1 - sigma * np.sqrt(tau)
    if cp == "c" or cp == "1":
        value = st.norm.cdf(d1) * S_0 - st.norm.cdf(d2) * K * np.exp(-r * tau)
    elif cp == "p" or cp =="-1":
        value = st.norm.cdf(-d2) * K * np.exp(-r * tau) - st.norm.cdf(-d1)*S_0
    return value

def main():
    i = np.complex(0.0,1.0)

    CP = "c"
    S0 = 100.0
    r = 0.1
    tau = 0.1
    sigma = 0.25
    K = [80.0, 90.0, 100.0, 110, 120.0]
    N = 4*32
    L = 10

    # Definition of the characteristic function for the GBM, this is an input
    # for the COS method
    # Note that Chf does not include coefficient "+iuX(t_0)" this coefficient
    # is included internally in the evaluation
    # In the book we denote this function as \varphi(u)

    cf = lambda u: np.exp((r - 0.5 * np.power(sigma,2.0)) * i * u * tau - 0.5
                          * np.power(sigma, 2.0) * np.power(u, 2.0) * tau)

    # Timing results
    NoOfIterations = 100
    time_start = time.time()
    for k in range(0,NoOfIterations,1):
        val_COS = CallPutOptionPriceCOSMthd(cf,CP,S0,r,tau,K,N,L)
    time_stop = time.time()
    print("It took {0} seconds to price.".format((time_stop-time_start)/float(NoOfIterations)))

    # evaluate analytical Black Scholes equation
    val_Exact = BS_Call_Option_Price(CP,S0,K,sigma,tau,r)
    plt.plot(K,val_COS)
    plt.plot(K,val_Exact,'--')
    plt.xlabel("strike, K")
    plt.ylabel("Option Price")
    plt.legend(["COS Price","BS model"])
    plt.grid()

    #Error comuputation
    error = []
    for i in range(0,len(K)):
        error.append(np.abs(val_COS[i]-val_Exact[i])[0])
        print("Abs error for strike {0} is equal to {1:.2E}".format(K[i],error[i]))


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
The COS method truncates the integration domain to $[a, b]$ with $a = -L\sqrt{\tau}$ and $b = L\sqrt{\tau}$. For $\tau = 0.1$ and $L = 10$, compute $a$ and $b$. Why does the domain scale with $\sqrt{\tau}$?

??? success "Solution to Exercise 1"
    $a = -10\sqrt{0.1} = -3.162$ and $b = 10\sqrt{0.1} = 3.162$. The domain scales with $\sqrt{\tau}$ because the log-return $\ln(S_T/S_0)$ has standard deviation proportional to $\sigma\sqrt{\tau}$ under GBM. Setting $L = 10$ captures about 10 standard deviations, ensuring the density tail contribution is negligible ($< 10^{-23}$ for normal).

---

**Exercise 2.**
The COS method uses $N$ cosine expansion terms. For GBM with $\sigma = 0.25$, $\tau = 0.1$, if $N = 128$ gives error $2 \times 10^{-8}$, estimate the error for $N = 64$.

??? success "Solution to Exercise 2"
    The COS method has exponential convergence for smooth densities: error $\sim C \cdot e^{-\alpha N}$ for some $\alpha > 0$. Halving $N$ from 128 to 64 roughly squares the error (since $e^{-\alpha \cdot 64} = (e^{-\alpha \cdot 128})^{1/2}$). So the error at $N = 64$ is approximately $\sqrt{2 \times 10^{-8}} \approx 1.4 \times 10^{-4}$.

---

**Exercise 3.**
The Chi and Psi coefficients in the COS method involve integrals of $e^x\cos(k\pi(x-a)/(b-a))$ and $\cos(k\pi(x-a)/(b-a))$ respectively. Explain their roles in pricing calls versus puts.

??? success "Solution to Exercise 3"
    The Chi coefficients capture the exponential part of the payoff ($e^x = S/K$ after log transformation), while Psi coefficients capture the indicator function (whether the option is in the money). For calls, the payoff coefficients are $H_k = \frac{2}{b-a}(\text{Chi}_k - \text{Psi}_k)$ integrated over $[0, b]$ (ITM region). For puts, $H_k = \frac{2}{b-a}(-\text{Chi}_k + \text{Psi}_k)$ over $[a, 0]$. The sign difference reflects call payoff $(e^x - 1)^+$ versus put payoff $(1 - e^x)^+$.

---

**Exercise 4.**
Compare the COS method timing with Black-Scholes closed-form for $N = 128$ expansion terms and 5 strikes. Why is the COS method competitive despite requiring a summation?

??? success "Solution to Exercise 4"
    The COS method computes $N$ CF evaluations (vectorized) and one matrix-vector product, giving $O(N \times |\text{strikes}|)$ operations. For $N = 128$ and 5 strikes, this is 640 operations. Black-Scholes requires computing $d_1, d_2, N(d_1), N(d_2)$ per strike (about 20 operations each, total 100). The COS method is slightly slower for few strikes but extends to any model with a known CF, unlike the BS formula. For exotic payoffs or non-GBM models, COS is the only viable Fourier approach.