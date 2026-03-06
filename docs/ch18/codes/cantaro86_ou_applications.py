"""
Ornstein-Uhlenbeck process and applications.

Based on cantaro86's notebook:
    "6.1 Ornstein-Uhlenbeck process and applications.ipynb"
    from the Financial-Models-Numerical-Methods repository.

Covers:
    1. OU process exact simulation and moment verification
    2. OLS parameter estimation from a single path
    3. MLE parameter estimation (closed-form, van den Berg)
    4. First hitting time to theta (density + Monte Carlo)
    5. Vasicek bond pricing (closed formula, Monte Carlo, PDE)
    6. Mean-reversion trading strategy with Sharpe ratio

References:
    [1] van den Berg, "Calibrating the Ornstein-Uhlenbeck (Vasicek) model"
    [2] Brigo & Mercurio, "Interest Rate Models - Theory and Practice"
    [4] Finch, "Ornstein-Uhlenbeck process" (2004)
    [8] Cartea, Jaimungal & Penalva, "Algorithmic and High Frequency Trading" (2015)
"""

import numpy as np
import scipy.stats as ss
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.integrate import quad
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# 1. OU process -- exact simulation
# ---------------------------------------------------------------------------

# ======================================================================

def simulate_ou(kappa, theta, sigma, X0, T, N, paths, seed=42):
    """Simulate OU paths using the exact recursive formula.

    The exact solution of
        dX_t = kappa (theta - X_t) dt + sigma dW_t
    yields the recursion:
        X_{n+1} = theta + (X_n - theta) exp(-kappa dt)
                  + sigma sqrt((1 - exp(-2 kappa dt)) / (2 kappa)) Z_n

    Parameters
    ----------
    kappa : float   -- mean-reversion speed
    theta : float   -- long-term mean
    sigma : float   -- volatility
    X0    : float   -- initial value
    T     : float   -- terminal time
    N     : int     -- number of time steps
    paths : int     -- number of Monte Carlo paths
    seed  : int     -- random seed

    Returns
    -------
    X     : ndarray, shape (N, paths)
    T_vec : ndarray, shape (N,)
    dt    : float
    """
    np.random.seed(seed)
    T_vec, dt = np.linspace(0, T, N, retstep=True)
    X = np.zeros((N, paths))
    X[0, :] = X0
    W = ss.norm.rvs(loc=0, scale=1, size=(N - 1, paths))

    std_dt = np.sqrt(sigma ** 2 / (2 * kappa) * (1 - np.exp(-2 * kappa * dt)))
    exp_factor = np.exp(-kappa * dt)
    for t in range(N - 1):
        X[t + 1, :] = theta + exp_factor * (X[t, :] - theta) + std_dt * W[t, :]

    return X, T_vec, dt


def demo_simulation():
    """Simulate 5000 OU paths, compare sample moments to theory."""
    kappa, theta, sigma, X0 = 3.0, 0.5, 0.6, 1.0
    T, N, paths = 5, 20000, 5000
    X, T_vec, dt = simulate_ou(kappa, theta, sigma, X0, T, N, paths)

    std_asy = np.sqrt(sigma ** 2 / (2 * kappa))
    X_T = X[-1, :]

    # -- theoretical moments at time T --
    mean_T = theta + np.exp(-kappa * T) * (X0 - theta)
    std_T = np.sqrt(sigma ** 2 / (2 * kappa) * (1 - np.exp(-2 * kappa * T)))

    # -- fit from data --
    fit_mean, fit_std = ss.norm.fit(X_T)

    print("=== OU Simulation: Moment Verification ===")
    print(f"  Theoretical  mean = {mean_T:.6f},  std = {std_T:.6f}")
    print(f"  Sample       mean = {fit_mean:.6f},  std = {fit_std:.6f}")

    # -- covariance check --
    n1, n2 = 5950, 6000
    t1, t2 = n1 * dt, n2 * dt
    cov_th = (sigma ** 2 / (2 * kappa)
              * (np.exp(-kappa * abs(t1 - t2)) - np.exp(-kappa * (t1 + t2))))
    cov_data = np.cov(X[n1, :], X[n2, :])[0, 1]
    print(f"  Cov[X(t1),X(t2)] theory = {cov_th:.4f},  data = {cov_data:.4f}")

    # -- plot --
    N_show = 10
    x = np.linspace(X_T.min(), X_T.max(), 100)
    pdf_fitted = ss.norm.pdf(x, fit_mean, fit_std)

    fig = plt.figure(figsize=(14, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.plot(T_vec, X[:, :N_show], linewidth=0.5)
    ax1.axhline(theta + std_asy, color="black", label="1 asymptotic std dev")
    ax1.axhline(theta - std_asy, color="black")
    ax1.axhline(theta, color="tab:orange", label="Long-term mean")
    ax1.legend(loc="upper right")
    ax1.set_title(f"{N_show} OU sample paths")
    ax1.set_xlabel("t")

    ax2.plot(x, pdf_fitted, color="r", label="Normal density")
    ax2.hist(X_T, density=True, bins=50, facecolor="LightBlue",
             label="Frequency of X(T)")
    ax2.legend()
    ax2.set_title("Histogram vs Normal distribution")
    ax2.set_xlabel("X(T)")
    plt.tight_layout()
    plt.show()

    return X, T_vec, dt, kappa, theta, sigma, X0, T, N, paths


# ---------------------------------------------------------------------------
# 2. OLS parameter estimation from a single path
# ---------------------------------------------------------------------------

def ols_estimation(X_path, dt):
    """Estimate OU parameters from a single discrete path via OLS.

    The exact OU discretisation reads
        X_{n+1} = alpha + beta X_n + epsilon_n
    with
        beta  = exp(-kappa dt)
        alpha = theta (1 - beta)
    so that
        kappa = -log(beta) / dt
        theta = alpha / (1 - beta)
        sigma = std(residuals) * sqrt(2 kappa / (1 - beta^2))
    """
    XX = X_path[:-1]
    YY = X_path[1:]
    beta, alpha, _, _, _ = ss.linregress(XX, YY)
    kappa_ols = -np.log(beta) / dt
    theta_ols = alpha / (1 - beta)
    residuals = YY - beta * XX - alpha
    std_resid = np.std(residuals, ddof=2)
    sigma_ols = std_resid * np.sqrt(2 * kappa_ols / (1 - beta ** 2))

    return kappa_ols, theta_ols, sigma_ols


# ---------------------------------------------------------------------------
# 3. MLE parameter estimation (closed-form, van den Berg)
# ---------------------------------------------------------------------------

def mle_estimation(X_path, dt):
    """Closed-form MLE for OU parameters (van den Berg).

    Uses the sufficient statistics S_x, S_y, S_xx, S_xy, S_yy
    computed from consecutive observations.
    """
    XX = X_path[:-1]
    YY = X_path[1:]
    n = len(XX)

    Sx = np.sum(XX)
    Sy = np.sum(YY)
    Sxx = XX @ XX
    Sxy = XX @ YY
    Syy = YY @ YY

    theta_mle = (Sy * Sxx - Sx * Sxy) / (n * (Sxx - Sxy) - (Sx ** 2 - Sx * Sy))

    kappa_mle = -(1.0 / dt) * np.log(
        (Sxy - theta_mle * Sx - theta_mle * Sy + n * theta_mle ** 2)
        / (Sxx - 2 * theta_mle * Sx + n * theta_mle ** 2)
    )

    exp_k = np.exp(-kappa_mle * dt)
    sigma2_hat = (
        Syy
        - 2 * exp_k * Sxy
        + exp_k ** 2 * Sxx
        - 2 * theta_mle * (1 - exp_k) * (Sy - exp_k * Sx)
        + n * theta_mle ** 2 * (1 - exp_k) ** 2
    ) / n
    sigma_mle = np.sqrt(sigma2_hat * 2 * kappa_mle / (1 - np.exp(-2 * kappa_mle * dt)))

    return kappa_mle, theta_mle, sigma_mle


def demo_estimation(X, dt, kappa, theta, sigma):
    """Run both OLS and MLE estimation on a single path and compare."""
    X_1 = X[:, 1]  # pick one path

    k_ols, th_ols, s_ols = ols_estimation(X_1, dt)
    k_mle, th_mle, s_mle = mle_estimation(X_1, dt)

    print("\n=== Parameter Estimation (single path) ===")
    print(f"  {'':18s} {'kappa':>10s} {'theta':>10s} {'sigma':>10s}")
    print(f"  {'True':18s} {kappa:10.4f} {theta:10.4f} {sigma:10.4f}")
    print(f"  {'OLS':18s} {k_ols:10.4f} {th_ols:10.4f} {s_ols:10.4f}")
    print(f"  {'MLE (closed-form)':18s} {k_mle:10.4f} {th_mle:10.4f} {s_mle:10.4f}")

    return X_1


# ---------------------------------------------------------------------------
# 4. First hitting time to theta
# ---------------------------------------------------------------------------

def density_fht_standardised(t, C):
    """Density of the first hitting time to 0 for the standardised OU process.

    The standardised process satisfies dX = -X dt + sqrt(2) dW
    with X(0) = C. The density of T_{0,C} is:

        f(t) = sqrt(2/pi) |C| exp(-t) / (1 - exp(-2t))^(3/2)
               * exp(-C^2 exp(-2t) / (2 (1 - exp(-2t))))
    """
    e2t = np.exp(-2 * t)
    denom = 1.0 - e2t
    return (np.sqrt(2.0 / np.pi) * np.abs(C) * np.exp(-t)
            / denom ** 1.5
            * np.exp(-C ** 2 * e2t / (2.0 * denom)))


def demo_first_hitting_time(X, T_vec, dt, kappa, theta, sigma, X0):
    """Compare Monte Carlo first-passage times with the theoretical density."""
    # Monte Carlo estimation
    if X0 > theta:
        T_to_theta = np.argmax(X <= theta, axis=0) * dt
    else:
        T_to_theta = np.argmax(X >= theta, axis=0) * dt

    mc_mean = T_to_theta.mean()
    mc_sem = ss.sem(T_to_theta)

    # Change of variables to the standardised problem
    C = (X0 - theta) * np.sqrt(2 * kappa) / sigma

    # Theoretical mean and std via numerical integration
    # The density in original time is kappa * f(kappa * t, C)
    def scaled_density(t):
        return kappa * density_fht_standardised(kappa * t, C)

    theoretical_mean = quad(lambda t: t * scaled_density(t), 0, 1000)[0]
    theoretical_std = np.sqrt(
        quad(lambda t: (t - theoretical_mean) ** 2 * scaled_density(t), 0, 1000)[0]
    )

    print("\n=== First Hitting Time to theta ===")
    print(f"  MC mean = {mc_mean:.4f}  (std error = {mc_sem:.4f})")
    print(f"  Theoretical mean = {theoretical_mean:.4f}")
    print(f"  MC std = {T_to_theta.std():.4f},  Theoretical std = {theoretical_std:.4f}")

    # -- plot --
    x_plot = np.linspace(T_to_theta.min(), T_to_theta.max(), 200)
    fig = plt.figure(figsize=(10, 4))
    plt.plot(x_plot, scaled_density(x_plot), color="red",
             label="OU hitting-time density")
    plt.hist(T_to_theta, density=True, bins=100, facecolor="LightBlue",
             label="MC frequencies")
    plt.title("First passage time distribution from X0 to theta")
    plt.xlabel("Time")
    plt.legend()
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 5. Vasicek bond pricing
# ---------------------------------------------------------------------------

def vasicek_closed(kappa, theta, sigma, r0, T):
    """Closed-form zero-coupon bond price under the Vasicek model.

    P(0, T) = A(0,T) exp(-B(0,T) r0)
    with
        B = (1 - exp(-kappa T)) / kappa
        A = exp((theta - sigma^2/(2 kappa^2))(B - T) - sigma^2/(4 kappa) B^2)
    """
    B = (1.0 - np.exp(-kappa * T)) / kappa
    A = np.exp((theta - sigma ** 2 / (2 * kappa ** 2)) * (B - T)
               - sigma ** 2 / (4 * kappa) * B ** 2)
    return A * np.exp(-B * r0)


def vasicek_mc(X, T):
    """Monte Carlo bond price: E[exp(-mean(r)*T)].

    X : ndarray, shape (N, paths) -- simulated short-rate paths
    """
    disc_factor = np.exp(-X.mean(axis=0) * T)
    return disc_factor.mean(), ss.sem(disc_factor)


def vasicek_pde(kappa, theta, sigma, r0, T,
                Nspace=6000, Ntime=6000, r_min=-0.8, r_max=3.0):
    """Vasicek bond price via implicit upwind finite differences.

    Solves the PDE:
        dP/dt + kappa(theta-r) dP/dr + 0.5 sigma^2 d^2P/dr^2 - r P = 0
    backwards from terminal condition P(T,r)=1.
    """
    r_grid, dr = np.linspace(r_min, r_max, Nspace, retstep=True)
    T_array, Dt = np.linspace(0, T, Ntime, retstep=True)

    V = np.zeros((Nspace, Ntime))
    offset = np.zeros(Nspace - 2)
    V[:, -1] = 1.0                                       # terminal condition
    V[-1, :] = np.exp(-r_grid[-1] * (T - T_array))       # boundary r_max
    V[0, :] = np.exp(-r_grid[0] * (T - T_array))         # boundary r_min

    sig2 = sigma * sigma
    drr = dr * dr
    r_int = r_grid[1:-1]
    max_part = np.maximum(kappa * (theta - r_int), 0)
    min_part = np.minimum(kappa * (theta - r_int), 0)

    a = min_part * (Dt / dr) - 0.5 * (Dt / drr) * sig2
    b = 1.0 + Dt * r_int + (Dt / drr) * sig2 + (Dt / dr) * (max_part - min_part)
    c = -max_part * (Dt / dr) - 0.5 * (Dt / drr) * sig2

    D = sparse.diags([a[1:], b, c[:-1]], [-1, 0, 1],
                      shape=(Nspace - 2, Nspace - 2)).tocsc()

    for n in range(Ntime - 2, -1, -1):
        offset[0] = a[0] * V[0, n]
        offset[-1] = c[-1] * V[-1, n]
        V[1:-1, n] = spsolve(D, V[1:-1, n + 1] - offset)

    price = np.interp(r0, r_grid, V[:, 0])
    return price, r_grid, V, T_array


def demo_vasicek(kappa, theta, sigma, X0, T, X):
    """Compare three Vasicek bond-pricing methods."""
    P_closed = vasicek_closed(kappa, theta, sigma, X0, T)
    P_mc, mc_se = vasicek_mc(X, T)
    P_pde, r_grid, V, T_array = vasicek_pde(kappa, theta, sigma, X0, T)

    print("\n=== Vasicek Bond Pricing ===")
    print(f"  Closed formula : {P_closed:.6f}")
    print(f"  Monte Carlo    : {P_mc:.6f}  (std error = {mc_se:.6f})")
    print(f"  PDE (upwind FD): {P_pde:.6f}")

    # -- plot --
    fig = plt.figure(figsize=(14, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122, projection="3d")

    ax1.plot(r_grid, V[:, 0], color="red", label="Bond price at t=0")
    ax1.plot([X0, X0], [0, P_closed], "k--")
    ax1.plot([r_grid[0], X0], [P_closed, P_closed], "k--")
    ax1.text(X0, P_closed + 0.005, "Bond Price")
    ax1.set_xlim(-0.4, 2.5)
    ax1.set_ylim(0.025, 0.12)
    ax1.set_xlabel("r")
    ax1.set_ylabel("P")
    ax1.legend(loc="upper right")
    ax1.set_title("Vasicek bond price at t=0")

    Nsp = len(r_grid)
    lo = 700
    hi = Nsp - 200
    X_plt, Y_plt = np.meshgrid(T_array, r_grid[lo:hi])
    ax2.plot_surface(Y_plt, X_plt, V[lo:hi], cmap="viridis")
    ax2.set_title("Vasicek bond price surface")
    ax2.set_xlabel("r")
    ax2.set_ylabel("time")
    ax2.set_zlabel("P")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 6. Mean-reversion trading strategy
# ---------------------------------------------------------------------------

def strategy(X_path, mean=0.0, std_open=0.5, std_close=0.05, X0=0.0):
    """Execute a mean-reversion strategy on one OU path.

    Rules:
        - Open SHORT when price crosses mean + std_open from below.
        - Open LONG  when price crosses mean - std_open from above.
        - Close position when price returns to within +/- std_close of mean.
        - Force-close any open position at terminal time.

    Parameters
    ----------
    X_path    : 1-D array -- price path
    mean      : float     -- long-term mean (theta)
    std_open  : float     -- band width for opening
    std_close : float     -- band width for closing

    Returns
    -------
    status : 1-D array -- +1 long, -1 short, 0 flat
    cash   : 1-D array -- cumulative cash from trades
    """
    n = len(X_path)
    status = np.zeros(n)
    cash = np.zeros(n)
    cash[0] = X0

    for i in range(1, n):
        x = X_path[i]
        if status[i - 1] == 1 and x >= mean - std_close:
            # close long
            status[i] = 0
            cash[i] += x
        elif status[i - 1] == -1 and x <= mean + std_close:
            # close short
            status[i] = 0
            cash[i] -= x
        elif status[i - 1] == 0 and x >= mean + std_open:
            # open short
            status[i] = -1
            cash[i] += x
        elif status[i - 1] == 0 and x <= mean - std_open:
            # open long
            status[i] = 1
            cash[i] -= x
        else:
            status[i] = status[i - 1]

    # force-close at terminal time
    x_final = X_path[-1]
    if status[-1] == 1:
        cash[-1] += x_final
    elif status[-1] == -1:
        cash[-1] -= x_final

    return status, cash.cumsum()


def demo_trading_strategy():
    """Simulate the mean-reversion strategy across 5000 paths."""
    kappa, theta, sigma, X0 = 10.0, 0.0, 2.0, 0.0
    T, N, paths = 1, 1000, 5000

    X, T_vec, dt = simulate_ou(kappa, theta, sigma, X0, T, N, paths, seed=41)

    std_asy = np.sqrt(sigma ** 2 / (2 * kappa))   # open-position band
    std_10 = std_asy / 10.0                         # close-position band

    # -- compute PnL for every path --
    PnL = np.zeros(paths)
    for i in range(paths):
        _, cash = strategy(X[:, i], mean=theta,
                           std_open=std_asy, std_close=std_10, X0=X0)
        PnL[i] = cash[-1]

    sharpe = PnL.mean() / PnL.std()

    print("\n=== Mean-Reversion Trading Strategy ===")
    print(f"  Paths = {paths},  T = {T},  N = {N}")
    print(f"  kappa = {kappa},  theta = {theta},  sigma = {sigma}")
    print(f"  Open band  = +/- {std_asy:.4f}  (1 asymptotic std dev)")
    print(f"  Close band = +/- {std_10:.4f}   (1/10 asymptotic std dev)")
    print(f"  Mean PnL  = {PnL.mean():.4f}")
    print(f"  Std  PnL  = {PnL.std():.4f}")
    print(f"  Sharpe ratio = {sharpe:.2f}")

    # -- detailed plot for one path --
    process = 0
    status, cash = strategy(X[:, process], mean=theta,
                            std_open=std_asy, std_close=std_10, X0=X0)

    fig = plt.figure(figsize=(16, 10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(223)
    ax3 = fig.add_subplot(222)
    ax4 = fig.add_subplot(224)

    ax1.plot(T_vec, X[:, process], linewidth=0.5)
    ax1.axhline(theta + std_asy, color="sandybrown", label="open short")
    ax1.axhline(theta - std_asy, color="chocolate", label="open long")
    ax1.axhline(theta + std_10, color="gray", label="close short")
    ax1.axhline(theta - std_10, color="rosybrown", label="close long")
    ax1.axhline(theta, color="black", label="Long-term mean")
    ax1.legend()
    ax1.set_title(f"OU process: path {process}")
    ax1.set_xlabel("t")

    ax2.plot(T_vec, status, linestyle="dashed", color="grey")
    ax2.set_title("Position: 1=LONG, -1=SHORT, 0=Flat")
    ax2.set_xlabel("t")

    x_hist = np.linspace(PnL.min(), PnL.max(), 100)
    ax3.hist(PnL, density=True, bins=100, facecolor="LightBlue",
             label="frequencies")
    ax3.plot(x_hist, ss.norm.pdf(x_hist, loc=PnL.mean(), scale=PnL.std()),
             color="r", label="Normal density")
    ax3.legend()
    ax3.set_title(f"PnL distribution.  Sharpe = {sharpe:.2f}")

    ax4.plot(T_vec, cash)
    ax4.set_title("Cumulative cash in portfolio")
    ax4.set_xlabel("t")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # 1. Simulation
    X, T_vec, dt, kappa, theta, sigma, X0, T, N, paths = demo_simulation()

    # 2 & 3. Parameter estimation (OLS + MLE)
    X_1 = demo_estimation(X, dt, kappa, theta, sigma)

    # 4. First hitting time
    demo_first_hitting_time(X, T_vec, dt, kappa, theta, sigma, X0)

    # 5. Vasicek bond pricing
    demo_vasicek(kappa, theta, sigma, X0, T, X)

    # 6. Trading strategy
    demo_trading_strategy()
