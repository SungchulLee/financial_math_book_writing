#@title Log-Normal PDF Recovery
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