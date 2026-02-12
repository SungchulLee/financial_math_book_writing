#@title Normal PDF Recovery
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


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