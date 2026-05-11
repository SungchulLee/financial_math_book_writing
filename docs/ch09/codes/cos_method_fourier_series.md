# Fourier Series

## Background

Cos Method Fourier Series

Educational script demonstrating cos method fourier series concepts.

---

## Code

```python
"""
Cos Method Fourier Series

Educational script demonstrating cos method fourier series concepts.
"""

#@title Fourier Series Of Non-Periodic Function on $[-\pi,\pi]$
f = lambda x : np.sin( ( x - 1.8 ) ** 2 )

# ======================================================================

def main():
    n = 10_000
    theta = np.linspace(-np.pi,np.pi,n)
    d_theta = theta[1] - theta[0]
    f_theta = f(theta)

    deg = 100
    f_recovered = np.zeros_like(f_theta)
    for k in range(deg):
        A_k = np.sum( f_theta[:-1] * np.cos(k*theta[:-1]) ) * d_theta / np.pi
        B_k = np.sum( f_theta[:-1] * np.sin(k*theta[:-1]) ) * d_theta / np.pi
        if k == 0:
            A_k /= 2
            B_k /= 2
        f_recovered += A_k * np.cos(k*theta) + B_k * np.sin(k*theta)

    fig, ax = plt.subplots(1,1,figsize=(12,4))
    ax.plot(theta,f_theta,label='Original',lw=10,alpha=0.3)
    ax.plot(theta,f_recovered,"--r",label=f'Recovered with {n} Terms')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
For $f(x) = \sin((x - 1.8)^2)$ on $[-\pi, \pi]$, explain why the Fourier series includes both cosine and sine terms.

??? success "Solution to Exercise 1"
    The function $f(x) = \sin((x-1.8)^2)$ is neither even nor odd about $x = 0$ (it has no symmetry). Therefore both Fourier coefficients $A_k$ and $B_k$ are nonzero. The cosine terms capture the even part $\frac{f(x) + f(-x)}{2}$ and the sine terms capture the odd part $\frac{f(x) - f(-x)}{2}$.

---

**Exercise 2.**
The Fourier coefficients are computed as $A_k = \frac{1}{\pi}\int_{-\pi}^{\pi} f(\theta)\cos(k\theta)d\theta$. In the code, this integral is approximated by a Riemann sum. What is the order of this approximation?

??? success "Solution to Exercise 2"
    With $n = 10{,}000$ points and spacing $d\theta = 2\pi/n$, the left-endpoint Riemann sum has error $O(d\theta) = O(1/n)$. For $n = 10{,}000$, the integration error per coefficient is $\sim 10^{-4}$. Using the trapezoidal rule (averaging left and right endpoints) would give $O(1/n^2) \sim 10^{-8}$ accuracy.

---

**Exercise 3.**
If $f$ has a discontinuity on $[-\pi, \pi]$, the Fourier series exhibits the Gibbs phenomenon. Describe what happens near the discontinuity as $N \to \infty$.

??? success "Solution to Exercise 3"
    Near the discontinuity, the partial Fourier sum overshoots by approximately 9% of the jump size, regardless of $N$. As $N$ increases, the overshoot becomes narrower (width $\sim \pi/N$) but its height remains $\sim 0.089 \times \text{jump}$. The Fourier series converges pointwise everywhere except at the discontinuity, but not uniformly. This affects the COS method for digital options, where the payoff has a jump.

---

**Exercise 4.**
For the smooth function $f(x) = \sin((x-1.8)^2)$ with $\deg = 100$ terms, the recovery is visually perfect. Estimate the convergence rate for smooth periodic functions.

??? success "Solution to Exercise 4"
    For infinitely differentiable periodic functions, the Fourier coefficients decay faster than any polynomial: $|A_k|, |B_k| = O(k^{-m})$ for all $m > 0$. The truncation error with $N$ terms is $O(N^{-m})$ for all $m$, giving superalgebraic convergence. In practice, for analytic functions the convergence is exponential: $O(e^{-\alpha N})$. With 100 terms, the error is below machine precision for this smooth function.