#@title Fourier Series On $[-\pi,\pi]$ For Even Function $g$
import matplotlib.pyplot as plt
import numpy as np

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