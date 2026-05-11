# Fourier Series (Even Function)

## Background

Cos Method Fourier Series Even

Educational script demonstrating cos method fourier series even concepts.

---

## Code

```python
"""
Cos Method Fourier Series Even

Educational script demonstrating cos method fourier series even concepts.
"""

#@title Fourier Series On $[-\pi,\pi]$ For Even Function $g$
import matplotlib.pyplot as plt
import numpy as np

# ======================================================================

def main():
    f = lambda x : np.sin( (x-1.8)**2 )
    g = lambda x: np.array([f(xi) if xi>0 else f(-xi) for xi in x])

    n = 10000
    theta = np.linspace(-np.pi,np.pi,n)
    d_theta = theta[1] - theta[0]
    g_theta = g(theta)

    deg = 100
    g_recovered = np.zeros_like(g_theta)
    for k in range(deg):
        A_k = np.sum( g_theta[:-1] * np.cos(k*theta[:-1]) ) * d_theta / np.pi
        B_k = np.sum( g_theta[:-1] * np.sin(k*theta[:-1]) ) * d_theta / np.pi
        if k == 0:
            A_k /= 2
            B_k /= 2
        g_recovered += A_k * np.cos(k*theta) + B_k * np.sin(k*theta)

    fig, ax = plt.subplots(1,1,figsize=(12,4))
    ax.plot(theta,g_theta,label='Original',lw=10,alpha=0.3)
    ax.plot(theta,g_recovered,"--r",label=f'Recovered with {n} Terms')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
If $g(x) = f(|x|)$ where $f(x) = \sin((x-1.8)^2)$, verify that $g$ is an even function and explain why $B_k = 0$ for all $k$.

??? success "Solution to Exercise 1"
    $g(-x) = f(|-x|) = f(|x|) = g(x)$, confirming $g$ is even. For even functions, $B_k = \frac{1}{\pi}\int_{-\pi}^{\pi}g(\theta)\sin(k\theta)d\theta = 0$ because $g(\theta)\sin(k\theta)$ is an odd function (even times odd = odd), and the integral of an odd function over a symmetric interval is zero.

---

**Exercise 2.**
For the even function $g$, the Fourier series reduces to a cosine series. Explain the connection to the COS method for option pricing.

??? success "Solution to Exercise 2"
    The COS method expands the density function on $[a, b]$ using only cosine terms: $f(x) \approx \sum_{k=0}^{N-1} A_k \cos(k\pi(x-a)/(b-a))$. This works because any function on $[a, b]$ can be even-extended to $[2a-b, b]$, making the cosine series a natural basis. The CF provides the coefficients directly: $A_k = \frac{2}{b-a}\text{Re}[\varphi(k\pi/(b-a))e^{-ika\pi/(b-a)}]$.

---

**Exercise 3.**
Compare the convergence of the Fourier series for $f$ (general) versus $g$ (even). Does evenness improve convergence?

??? success "Solution to Exercise 3"
    Evenness itself does not improve the convergence rate---it only eliminates the sine terms. However, $g(x) = f(|x|)$ typically has a kink at $x = 0$ (unless $f^\prime(0) = 0$), which can reduce convergence to $O(1/N^2)$. For the original $f$ (smooth), convergence is superalgebraic. So the even extension may actually worsen convergence if it introduces a non-smooth point.

---

**Exercise 4.**
For 100 expansion terms, both $f$ and $g$ show excellent recovery. Estimate the minimum number of terms needed for the error to be below $10^{-3}$.

??? success "Solution to Exercise 4"
    For smooth $f$: with exponential convergence $O(e^{-\alpha N})$, the error reaches $10^{-3}$ at roughly $N \approx 7\alpha^{-1} \ln 10 \approx 20$--30 terms. For $g$ with a kink: convergence is $O(1/N^2)$, so $10^{-3}$ requires $N \approx 1/\sqrt{10^{-3}} \approx 32$ terms. In practice, about 30--50 terms suffice for both at this tolerance.