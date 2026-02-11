#@title Fourier Series Of Non-Periodic Function on $[-\pi,\pi]$
f = lambda x : np.sin( ( x - 1.8 ) ** 2 )

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