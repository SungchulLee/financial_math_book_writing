# Log-Normal PDF Recovery

## Background

Cos Method Lognormal Pdf

Educational script demonstrating cos method lognormal pdf concepts.

---

## Code

```python
"""
Cos Method Lognormal Pdf

Educational script demonstrating cos method lognormal pdf concepts.
"""

#@title Log-Normal PDF Recovery
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# ======================================================================

def COSDensity(cf,x_point_of_interest,n,a,b):
    """
    cf                  : characteristic function
    x_point_of_interest : x values where we would like to compute pdf
    n                   : number of terms in Fourier cosine expansion
    a                   : lower limit of the pdf support
    b                   : upper limit of the pdf support
    """
    i = complex(0.0,1.0)
    k = np.arange(n)
    k_ = k * np.pi / (b-a)

    # A_k coefficients
    A_k    = 2.0 / (b - a) * np.real( cf(k_) * np.exp(-i*k_*a) );
    A_k[0] = A_k[0] * 0.5; # adjustment for the first term

    return A_k @ np.cos( np.outer( k_, x_point_of_interest - a ) )


def main(mu=0.0,sigma=1.0,original_scale_used=True):
    """
    mu    : mean of normal distribution
    sigma : std of normal distribution
    """
    mu = 0.5
    sigma = 0.2

    # characteristic function for the normal distribution
    i = complex(0.0, 1.0)
    cF = lambda u : np.exp(i*mu*u - 0.5*sigma**2*u**2)

    # define domain for density
    if original_scale_used:
        y_point_of_interest = np.linspace(0.05,5,1000)
        x_point_of_interest = np.log(y_point_of_interest)
    else:
        x_point_of_interest = np.linspace(-3,3,1000)
        y_point_of_interest = np.exp(x_point_of_interest)
    f = stats.lognorm(s=sigma, loc=0, scale=np.exp(mu)).pdf(y_point_of_interest)
    a = -4.0 # lower limit of the normal, not log-normal pdf support
    b = 4.0 # upper limit of the normal, not log-normal support

    fig, ax = plt.subplots(1,1,figsize=(15,10))
    ax.plot(y_point_of_interest,f,label=f'Exact PDF',lw=10,alpha=0.3)
    ax.grid()
    ax.set_xlabel("x")
    ax.set_ylabel("$f_X(x)$")
    for n in [2**k for k in range(5,7)]:
        f_X = COSDensity(cF,x_point_of_interest,n,a,b)
        f_Y = (1/y_point_of_interest) * f_X
        error = np.max(np.abs(f_Y-f))
        print(f"For {n:6} expanansion terms the error is {error:.2e}")
        ax.plot(y_point_of_interest,f_Y,"--",label=f'PDF recovered using {n:6} COS terms')
    plt.legend(loc='upper right')
    plt.show()


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
The COS density recovery for the log-normal distribution uses $f_Y(y) = \frac{1}{y}f_X(\ln y)$. Derive this change-of-variables formula.

??? success "Solution to Exercise 1"
    If $X \sim N(\mu, \sigma^2)$ and $Y = e^X$, then $x = \ln y$ and $dx/dy = 1/y$. The density transforms as $f_Y(y) = f_X(\ln y) \cdot |dx/dy| = f_X(\ln y)/y$ for $y > 0$. The COS method recovers $f_X$ (the normal density) and then applies the Jacobian factor $1/y$ to obtain the log-normal density.

---

**Exercise 2.**
Why are the COS truncation limits $a = -4$ and $b = 4$ appropriate for the underlying normal distribution with $\mu = 0.5$, $\sigma = 0.2$?

??? success "Solution to Exercise 2"
    The limits are for the normal variable $X$, not the log-normal $Y$. With $\mu = 0.5$, $\sigma = 0.2$: $[a, b] = [-4, 4]$ covers $[\mu - 22.5\sigma, \mu + 17.5\sigma]$, well beyond $\pm 5\sigma$. The normal density is negligible outside $\pm 4\sigma$, so these limits capture essentially all probability mass.

---

**Exercise 3.**
With $N = 32$ expansion terms, the error is reported around $10^{-2}$; with $N = 64$, it drops to $\sim 10^{-5}$. What convergence rate does this suggest?

??? success "Solution to Exercise 3"
    Doubling $N$ from 32 to 64 reduces the error by a factor of $10^{-2}/10^{-5} = 1000 \approx 2^{10}$. This suggests approximately $O(2^{-\alpha N})$ with $\alpha \approx 10/32 \approx 0.31$, i.e., exponential convergence. For smooth densities like the normal, the Fourier cosine coefficients decay exponentially, confirming this rate.

---

**Exercise 4.**
Explain why the COS method recovers the log-normal density on the original scale $y > 0$ rather than working directly with the log-normal CF.

??? success "Solution to Exercise 4"
    The log-normal distribution does not have a simple closed-form characteristic function in terms of $y$. Instead, $\ln Y \sim N(\mu, \sigma^2)$ has the simple normal CF $\varphi(u) = e^{iu\mu - u^2\sigma^2/2}$. The COS method recovers the normal density $f_X$ efficiently using this CF, then transforms to $f_Y(y) = f_X(\ln y)/y$. This two-step approach avoids the complexity of the log-normal CF.