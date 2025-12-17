# ============================================================================
# brownian_motion_ITO_INTEGRAL.py
# ============================================================================
import brownian_motion as bmw
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

num_paths = 10_000
T = 1

bm = bmw.BrownianMotion(maturity_time=T, seed=0)
result = bm.simulate(num_paths)
t, dt, sqrt_dt, b, db = result.time_steps, result.time_step_size, result.sqrt_time_step_size, result.brownian_paths, result.increments

integrands = (
    lambda t, b : b[:, :-1], # B_t
    lambda t, b : b[:, :-1]**2, # B_t^2
    lambda t, b : t[:-1] * b[:, :-1], # tB_t
    lambda t, b : t[:-1]**2 * b[:, :-1], # t^2 B_t
    lambda t, b : t[:-1] * b[:, :-1]**2, # tB_t^2
    lambda t, b : t[:-1] * np.exp(b[:, :-1]), # t e^{B_t}
)
integrands_str = (
    "B_t",
    "B_t^2",
    "tB_t",
    "t^2 B_t",
    "tB_t^2",
    "t e^{B_t}",
)

fig, axes = plt.subplots(len(integrands),2,figsize=(12,3*len(integrands)))

for i, stock_position, stock_position_str in zip(range(len(integrands)), integrands, integrands_str):
    ax0, ax1 = axes[i,0], axes[i,1]

    # Ito integral
    # stock_position( t, b ).shape : (num_path, num_steps)
    # db.shape                     : (num_path, num_steps)
    ito = np.cumsum( stock_position( t, b ) * db, axis=1 )
    ito = np.concatenate( ( np.zeros( (num_paths, 1) ), ito ), axis=1)

    ax0.set_title(f'Ito integral with f = {stock_position_str}', fontsize=10)
    ax0.plot(t,b[0,:],'--b',label='Brownian Motion')
    ax0.plot(t,ito[0,:],'r',label='Ito Integral')
    ax0.set_xlabel('time')
    ax0.set_ylabel('$B_t$')
    #ax0.grid(True)
    ax0.legend()

    for spine in ["top","right"]:
        ax0.spines[spine].set_visible(False)
    for spine in ["bottom","left"]:
        ax0.spines[spine].set_position("zero")

    mu = ito[:,-1].mean()
    sigma = ito[:,-1].std()
    x_pdf = np.linspace(-3,3,101) * sigma + mu
    y_pdf = stats.norm(loc=mu,scale=sigma).pdf(x_pdf)

    ax1.plot(x_pdf,y_pdf,"--r",label="Normal PDF",lw=3)

    ax1.legend()

    ax1.set_title('Histogram of $\int_0^Tf(s,B_s)dB_s$', fontsize=10)
    ax1.hist(ito[:,-1], bins=70, density=True)
    #ax1.grid(True)

plt.tight_layout()
plt.show()