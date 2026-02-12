#@title Heston Call and Put COS Method
# Source Code
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


def BS_Call_Option_Price(CP,S_0,K,sigma,tau,r):
    d1 = ( np.log(S_0/K) + (r+0.5*sigma**2*tau) ) / (sigma*np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    if str(CP).lower()=="c" or str(CP).lower()=="1":
        value = S_0 * st.norm.cdf(d1) - K*np.exp(-r*tau) * st.norm.cdf(d2)
    elif str(CP).lower()=="p" or str(CP).lower()=="-1":
        value = K*np.exp(-r*tau) * st.norm.cdf(-d2) - S_0 * st.norm.cdf(-d1)
    return value


def dV_dsigma(S_0,K,sigma,tau,r):
    """
    Vega = \frac{\partial V}{\partial \sigma}
    """
    d2 = ( np.log(S_0/K) + (r-0.5*sigma**2*tau) ) / (sigma*np.sqrt(tau))
    return K*np.exp(-r*tau) * st.norm.pdf(d2) * np.sqrt(tau)


def ImpliedVolatility(CP,S_0,K,sigma,tau,r,V_market):
    # Handy lambda expressions
    optPrice = lambda sigma: BS_Call_Option_Price(CP,S_0,K,sigma,tau,r)
    vega = lambda sigma: dV_dsigma(S_0,K,sigma,tau,r)

    # Newton-Raphson method
    n = 1
    error = 1e10 # initial error
    while error>10e-9:
        g         = optPrice(sigma) - V_market
        g_prim    = vega(sigma)
        sigma_new = sigma - g / g_prim

        #error    = abs(sigma_new-sigma) # alternative error that can be used
        error     = abs(g)
        sigma     = sigma_new;
        print(f'Iteration {n:05} Error {error:10.8f}')

        n         = n+1
    return sigma


def compute_ABC(r,u,tau,kappa,v_bar,gamma,rho):
    i = complex(0., 1.)

    kappa_ = kappa - gamma * rho * i * u
    D = np.sqrt( kappa_**2 + (u**2+i*u)*gamma**2 )
    kappa_p = kappa_ + D
    kappa_n = kappa_ - D
    kappa_bar = kappa * v_bar / gamma**2
    e = np.exp( - D * tau )
    g = kappa_n / kappa_p

    A = r*(i*u-1)*tau + kappa_bar*tau*kappa_n - 2*kappa_bar*np.log( (1-g*e) / (1-g) )
    B = i*u
    C = (1-e) * kappa_n / ( gamma**2*(1-g*e) )
    return A, B, C


def compute_ChF(X,v,r,u,tau,kappa,v_bar,gamma,rho):
    A, B, C = compute_ABC(r,u,tau,kappa,v_bar,gamma,rho)
    return np.exp(r*tau + A + B*X + C*v)


def compute_A_k(chf,a,b,n):
    """
    chf : characteristic function
    a   : lower limit of the pdf support
    b   : upper limit of the pdf support
    n   : number of terms in Fourier cosine expansion
    """
    k = np.arange(n)
    k_ = k * np.pi / (b-a)

    i = complex(0.0,1.0)
    A_k    = 2.0 / (b - a) * np.real( chf(k_) * np.exp(-i*k_*a) );
    A_k[0] = A_k[0] * 0.5; # adjustment for the first term
    return A_k


def compute_chi_k_and_psi_k(a,b,c,d,n):
    """
    a   : lower limit of the pdf support
    b   : upper limit of the pdf support
    c   : lower limit of the option exercise support
    d   : upper limit of the option exercise support
    n   : number of terms in Fourier cosine expansion
    """
    k = np.arange(n)
    k_pi = k * np.pi / ( b - a )

    theta_c = ( c - a ) * k_pi
    theta_d = ( d - a ) * k_pi

    cos_ = np.cos(theta_d)*np.exp(d) - np.cos(theta_c)*np.exp(c)
    sin_ = k_pi*np.sin(theta_d)*np.exp(d) - k_pi*np.sin(theta_c)*np.exp(c)
    chi_k = ( cos_ + sin_ ) / ( 1 + k_pi**2 )

    psi_k = chi_k.copy()
    psi_k[1:] = ( np.sin(theta_d[1:]) - np.sin(theta_c[1:]) ) / k_pi[1:]
    psi_k[0] = d - c
    return chi_k, psi_k


def compute_H_k(a,b,n,K,cp):
    """
    a   : lower limit of the pdf support
    b   : upper limit of the pdf support
    n   : number of terms in Fourier cosine expansion
    K   : strike
    cp  : 'c' or 'p' representing call or put
    """
    if cp == "c":
        chi_k, psi_k = compute_chi_k_and_psi_k(a,b,c=np.log(K),d=b,n=n)
        H_k = ( chi_k - K * psi_k ) * 2 / (b-a)
    if cp == "p":
        chi_k, psi_k = compute_chi_k_and_psi_k(a,b,c=a,d=np.log(K),n=n)
        H_k = ( K * psi_k - chi_k ) * 2 / (b-a)
    return H_k


def compute_OptionPriceCOSMethod(chf,x0,r,tau,K,a,b,n,cp):
    """
    chf : characteristic function
    x0  : log S0
    r   : interest rate
    tau : time to maturity
    K   : strikes as a list
    a   : lower limit of the pdf support
    b   : upper limit of the pdf support
    n   : number of terms in Fourier cosine expansion
    cp  : 'c' or 'p' representing call or put
    """
    value = []
    for K_temp in K:
        A_k = compute_A_k(chf,a,b,n)
        H_k = compute_H_k(a,b,n,K_temp,cp)
        value.append( (A_k * H_k).sum() * np.exp(-r*tau) * (b - a ) / 2 )
    return value


# def BS_Call_Option_Price(CP,S_0,K,sigma,tau,r):
#     #Black-Scholes Call option price
#     cp = str(CP).lower()
#     K = np.array(K).reshape([len(K),1])
#     d1 = (np.log(S_0 / K) + (r + 0.5 * np.power(sigma,2.0)) * tau) / float(sigma * np.sqrt(tau))
#     d2 = d1 - sigma * np.sqrt(tau)
#     if cp == "c" or cp == "1":
#         value = st.norm.cdf(d1) * S_0 - st.norm.cdf(d2) * K * np.exp(-r * tau)
#     elif cp == "p" or cp =="-1":
#         value = st.norm.cdf(-d2) * K * np.exp(-r * tau) - st.norm.cdf(-d1)*S_0
#     return value


def main():
    S = 100
    X = np.log(S)
    v = 0.3**2
    r = 0.03
    u = np.linspace(0,60,2500)
    tau = 1 / 12
    kappa = 2
    v_bar = 0.2**2
    gamma = 0.4
    rho = - 0.9
    K = np.arange(100, 150, 10) #np.arange(90, 120, 10) #np.arange(50, 210, 10) # np.arange(90, 120, 10) #

    u_max = 60.0
    N = 2**10
    x_min = 4.1
    x_max = 5.1

    # characteristic function
    chf = lambda u : compute_ChF(X,v,r,u,tau,kappa,v_bar,gamma,rho)

    c_1 = compute_OptionPriceCOSMethod(chf,x0=X,r=r,tau=tau,K=K,a=x_min,b=x_max,n=N,cp='c')
    c_2 = BS_Call_Option_Price(CP='c',S_0=S,K=K,sigma=np.sqrt(v),tau=tau,r=r)
    vol_c_1 = []
    for c, K_tmp in zip(c_1,K):
        vol_c_1.append(ImpliedVolatility('c',S,K_tmp,0.3,tau,r,V_market=c))

    p_1 = compute_OptionPriceCOSMethod(chf,x0=X,r=r,tau=tau,K=K,a=x_min,b=x_max,n=N,cp='p')
    p_2 = BS_Call_Option_Price(CP='p',S_0=S,K=K,sigma=np.sqrt(v),tau=tau,r=r)
    vol_p_1 = []
    for p, K_tmp in zip(p_1,K):
        vol_p_1.append(ImpliedVolatility('p',S,K_tmp,0.3,tau,r,V_market=p))

    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2,2,figsize=(12,8))

    ax0.plot(K,c_1,'-*r',label='Call Option Price by COS Method')
    ax0.plot(K,c_2,'-b',label='Call Option Price by BS Model')

    ax1.plot(K,p_1,'-*r',label='Put Option Price by COS Method')
    ax1.plot(K,p_2,'-b',label='Put Option Price by BS Model')

    ax2.plot(K,vol_c_1,"-*r", label='Implied Volatility of Call')

    ax3.plot(K,vol_p_1,"-*r", label='Implied Volatility of Put')

    for ax in (ax0, ax1, ax2, ax3):
        ax.set_xlabel('K')
        ax.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()