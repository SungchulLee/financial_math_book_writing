# Normal PDF Recovery

## Background

Cos Method Normal Pdf

Educational script demonstrating cos method normal pdf concepts.

---

## Code

```python
"""
Cos Method Normal Pdf

Educational script demonstrating cos method normal pdf concepts.
"""

#@title Normal PDF Recovery
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


def main(mu=0.0, sigma=1.0):
    """
    mu    : mean of normal distribution
    sigma : std of normal distribution
    """
    # characteristic function for the normal distribution
    i = complex(0.0, 1.0)
    cF = lambda u : np.exp(i*mu*u - 0.5*sigma**2*u**2)

    # define domain for density
    x = np.linspace(-10.0,10,1000)
    f = stats.norm.pdf(x,mu,sigma)
    a = -10.0 # lower limit of the pdf support
    b = 10.0 # upper limit of the pdf support

    fig, ax = plt.subplots(1,1,figsize=(15,4))
    ax.plot(x,f,label=f'Exact PDF', lw=10,alpha=0.3)
    ax.grid()
    ax.set_xlabel("x")
    ax.set_ylabel("$f_X(x)$")
    #for n in [2**k for k in range(2,7)]:
    for n in [2**k for k in range(2,5)]:
        f_X = COSDensity(cF,x,n,a,b)
        error = np.max(np.abs(f_X-f))
        print(f"For {n:2} expanansion terms the error is {error:.2e}")
        ax.plot(x,f_X,"--",label=f'PDF recovered using {n:2} COS terms')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
The COS density formula uses $A_k = \frac{2}{b-a}\text{Re}[\varphi(k\pi/(b-a))e^{-ika\pi/(b-a)}]$ with $A_0$ halved. Derive this from the Fourier cosine expansion on $[a, b]$.

??? success "Solution to Exercise 1"
    On $[a, b]$, expand $f(x) = \sum_{k=0}^\infty A_k \cos(k\pi(x-a)/(b-a))$ where $A_k = \frac{2}{b-a}\int_a^b f(x)\cos(k\pi(x-a)/(b-a))dx$. Using $f(x) = \frac{1}{2\pi}\int e^{-iux}\varphi(u)du$ and exchanging integrals: $A_k = \frac{2}{b-a}\text{Re}[\varphi(k\pi/(b-a))e^{-ika\pi/(b-a)}]$. The factor of $1/2$ on $A_0$ corrects for the constant term in the cosine expansion.

---

**Exercise 2.**
For $N = 4$ terms, the COS recovery of $N(0,1)$ shows visible deviations. For $N = 16$, it is nearly exact. Estimate the error for $N = 8$.

??? success "Solution to Exercise 2"
    With exponential convergence for the normal density, if $N = 4$ gives error $\sim 10^{-1}$ and $N = 16$ gives $\sim 10^{-6}$, interpolating: error $\approx C \cdot e^{-\alpha N}$ with $\alpha \approx \ln(10^5)/12 \approx 0.96$. At $N = 8$: error $\approx 10^{-1} \cdot e^{-0.96 \cdot 4} \approx 10^{-1} \cdot 0.02 \approx 2 \times 10^{-3}$.

---

**Exercise 3.**
Why must the support $[a, b] = [-10, 10]$ for $N(0,1)$ be wider than needed for the Gamma or Poisson distributions?

??? success "Solution to Exercise 3"
    The standard normal has unbounded support $(-\infty, \infty)$ with significant density throughout $[-4, 4]$. The truncation $[a, b]$ must capture this range. For Gamma (support $[0, \infty)$) or Poisson (support $\{0, 1, 2, \ldots\}$), the effective range is more compact. However, $[-10, 10]$ provides extra margin since the truncation error is $\int_{|x|>10}\varphi(x)dx < 10^{-23}$ for $N(0,1)$.

---

**Exercise 4.**
The COS method evaluates the CF at $u_k = k\pi/(b-a)$. For $[a,b] = [-10, 10]$ and $N = 16$ terms, compute the highest frequency $u_{15}$ and the corresponding normal CF value $|\varphi(u_{15})|$.

??? success "Solution to Exercise 4"
    $u_{15} = 15\pi/20 = 15\pi/20 = 2.356$. For $N(0,1)$: $|\varphi(2.356)| = e^{-2.356^2/2} = e^{-2.776} = 0.0623$. This is small but non-negligible, confirming that 16 terms capture the significant part of the CF. The CF at $u_{16} = 2.513$ gives $|\varphi| = 0.042$, and the rapid decay beyond ensures the series converges.