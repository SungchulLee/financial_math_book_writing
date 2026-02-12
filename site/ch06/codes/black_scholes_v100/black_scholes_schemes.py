# ============================================================================
# black_scholes/black_scholes_schemes.py
# ============================================================================
import numpy as np
import scipy.sparse as sparse

def setup_log_grid(Smin, Smax, NX, NT, T):
    """Set up log-space grid and parameters."""
    xmin, xmax = np.log(Smin), np.log(Smax)
    dx = (xmax - xmin) / (NX - 1)
    dt = T / (NT - 1)
    x_grid = np.linspace(xmin, xmax, NX)
    S_grid = np.exp(x_grid)
    return dx, dt, x_grid, S_grid, xmin, xmax

def explicit_scheme(model, option_type='put', Smin=0, Smax=200, NS=100, NT=None, early_exercise=False):
    """Explicit finite difference scheme in stock price space."""
    dS = (Smax - Smin) / (NS - 1)
    if NT is None:
        dt_stable = (dS ** 2) / (model.sigma ** 2 * Smax ** 2)
        NT = int(np.ceil(model.T / (0.5 * dt_stable)))
    dt = model.T / (NT - 1)

    S_grid = np.linspace(Smin, Smax, NS)
    V = np.zeros((NS, NT))
    V[:, -1] = model._payoff(S_grid, option_type)

    # Finite difference coefficients (using consistent indexing)
    i = np.arange(1, NS - 1)
    sigma2 = model.sigma ** 2
    r = model.r
    q = model.q

    a = 0.5 * dt * (sigma2 * i**2 - (r - q) * i)
    b = 1 - dt * (sigma2 * i**2 + r)
    c = 0.5 * dt * (sigma2 * i**2 + (r - q) * i)

    # Time stepping (backward in time)
    for n in reversed(range(NT - 1)):
        # Apply finite difference update
        V[1:-1, n] = a * V[0:-2, n+1] + b * V[1:-1, n+1] + c * V[2:, n+1]
        
        # Apply boundary conditions at current time step
        tau = (NT - 1 - n) * dt  # Time to expiry
        disc = np.exp(-r * tau)
        if option_type == 'put':
            V[0, n] = model.K * disc      # At S=0: put worth K*exp(-r*tau)
            V[-1, n] = 0                  # At S=Smax: put worth 0
        else:  # call
            V[0, n] = 0                   # At S=0: call worth 0
            V[-1, n] = S_grid[-1] - model.K * disc  # At S=Smax: call worth S-K*exp(-r*tau)

        # Early exercise for American options
        if early_exercise:
            V[:, n] = np.maximum(V[:, n], model._payoff(S_grid, option_type))

    return S_grid, V[:, 0]

def implicit_scheme(model, option_type='put', Smin=1e-3, Smax=500, NS=100, NT=100, early_exercise=False):
    """Implicit finite difference scheme in stock price space."""
    S_grid = np.linspace(Smin, Smax, NS)
    dS = S_grid[1] - S_grid[0]
    dt = model.T / (NT - 1)

    V = np.zeros((NS, NT))
    V[:, -1] = model._payoff(S_grid, option_type)

    # Finite difference coefficients
    i = np.arange(1, NS - 1)
    sigma2 = model.sigma ** 2
    r = model.r
    q = model.q

    a = -0.5 * dt * (sigma2 * i**2 - (r - q) * i)
    b = 1 + dt * (sigma2 * i**2 + r)
    c = -0.5 * dt * (sigma2 * i**2 + (r - q) * i)

    # Build tridiagonal matrix
    A = sparse.diags([a[1:], b, c[:-1]], offsets=[-1, 0, 1], format='csr')

    # Time stepping (backward in time)
    for n in reversed(range(NT - 1)):
        rhs = V[1:-1, n + 1].copy()
        
        # Apply boundary conditions at current time step
        tau = (NT - 1 - n) * dt
        disc = np.exp(-r * tau)
        if option_type == 'put':
            V[0, n] = model.K * disc
            V[-1, n] = 0
        else:  # call
            V[0, n] = 0
            V[-1, n] = S_grid[-1] - model.K * disc

        # Incorporate boundary conditions into RHS
        rhs[0]  -= a[0] * V[0, n]
        rhs[-1] -= c[-1] * V[-1, n]
        
        # Solve linear system
        V[1:-1, n] = sparse.linalg.spsolve(A, rhs)

        # Early exercise for American options
        if early_exercise:
            V[:, n] = np.maximum(V[:, n], model._payoff(S_grid, option_type))

    return S_grid, V[:, 0]

def cn_scheme(model, option_type='put', Smin=0, Smax=200, NS=100, NT=100, early_exercise=False):
    """Crank-Nicolson finite difference scheme in stock price space."""
    dS = (Smax - Smin) / (NS - 1)
    dt = model.T / (NT - 1)
    S_grid = np.linspace(Smin, Smax, NS)

    V = np.zeros((NS, NT))
    V[:, -1] = model._payoff(S_grid, option_type)

    # Finite difference coefficients
    i = np.arange(1, NS - 1)
    sigma2 = model.sigma ** 2
    r = model.r
    q = model.q

    alpha = 0.25 * dt * (sigma2 * i**2 - (r - q) * i)
    beta  = -0.5 * dt * (sigma2 * i**2 + r)
    gamma = 0.25 * dt * (sigma2 * i**2 + (r - q) * i)

    # Build matrices for Crank-Nicolson
    A = sparse.diags([-alpha[1:], 1 - beta, -gamma[:-1]], [-1, 0, 1], format='csr')
    B = sparse.diags([alpha[1:], 1 + beta, gamma[:-1]], [-1, 0, 1], format='csr')

    # Time stepping (backward in time)
    for n in reversed(range(NT - 1)):
        # Apply boundary conditions at current and next time steps
        tau_current = (NT - 1 - n) * dt
        tau_next = (NT - n) * dt
        disc_current = np.exp(-r * tau_current)
        disc_next = np.exp(-r * tau_next)
        
        if option_type == 'put':
            V[0, n] = model.K * disc_current
            V[-1, n] = 0
            # Boundary values at next time step
            bc_0_next = model.K * disc_next
            bc_end_next = 0
        else:  # call
            V[0, n] = 0
            V[-1, n] = S_grid[-1] - model.K * disc_current
            # Boundary values at next time step
            bc_0_next = 0
            bc_end_next = S_grid[-1] - model.K * disc_next

        # Right-hand side for Crank-Nicolson
        rhs = B @ V[1:-1, n + 1]
        rhs[0]  += alpha[0] * (bc_0_next + V[0, n])
        rhs[-1] += gamma[-1] * (bc_end_next + V[-1, n])
        
        # Solve linear system
        V[1:-1, n] = sparse.linalg.spsolve(A, rhs)
        
        # Early exercise for American options
        if early_exercise:
            V[:, n] = np.maximum(V[:, n], model._payoff(S_grid, option_type))

    return S_grid, V[:, 0]

def explicit_log_scheme(model, option_type='put', Smin=1e-3, Smax=500, NX=100, NT=None, early_exercise=False):
    """Explicit finite difference scheme in log-price space."""
    dx, dt, x_grid, S_grid, _, _ = setup_log_grid(Smin, Smax, NX, NT, model.T)

    if NT is None:
        dt_stable = dx**2 / model.sigma**2
        NT = int(np.ceil(model.T / (0.5 * dt_stable)))
    dt = model.T / (NT - 1)

    V = np.zeros((NX, NT))
    V[:, -1] = model._payoff(S_grid, option_type)

    # Log-space finite difference coefficients
    nu = model.r - model.q - 0.5 * model.sigma**2
    sigma2 = model.sigma ** 2

    a = 0.5 * dt * ((sigma2 / dx**2) - (nu / dx))
    b = 1 - dt * ((sigma2 / dx**2) + model.r)
    c = 0.5 * dt * ((sigma2 / dx**2) + (nu / dx))

    # Time stepping (backward in time)
    for n in reversed(range(NT - 1)):
        # Apply finite difference update
        for i in range(1, NX - 1):
            V[i, n] = a * V[i - 1, n + 1] + b * V[i, n + 1] + c * V[i + 1, n + 1]

        # Apply boundary conditions at current time step
        tau = (NT - 1 - n) * dt
        disc = np.exp(-model.r * tau)
        if option_type == 'put':
            V[0, n] = model.K * disc
            V[-1, n] = 0
        else:  # call
            V[0, n] = 0
            V[-1, n] = S_grid[-1] - model.K * disc

        # Early exercise for American options
        if early_exercise:
            V[:, n] = np.maximum(V[:, n], model._payoff(S_grid, option_type))

    return S_grid, V[:, 0]

def implicit_log_scheme(model, option_type='put', Smin=1e-3, Smax=500, NX=100, NT=100, early_exercise=False):
    """Implicit finite difference scheme in log-price space."""
    dx, dt, x_grid, S_grid, _, _ = setup_log_grid(Smin, Smax, NX, NT, model.T)
    V = np.zeros((NX, NT))
    V[:, -1] = model._payoff(S_grid, option_type)

    # Log-space finite difference coefficients
    nu = model.r - model.q - 0.5 * model.sigma**2
    sigma2 = model.sigma ** 2

    alpha = 0.5 * dt * ((sigma2 / dx**2) - (nu / dx))
    beta  = 1 + dt * ((sigma2 / dx**2) + model.r)
    gamma = 0.5 * dt * ((sigma2 / dx**2) + (nu / dx))

    # Build tridiagonal matrix
    lower_diag = -alpha * np.ones(NX-2)
    main_diag  =  beta  * np.ones(NX-2)
    upper_diag = -gamma * np.ones(NX-2)

    A = sparse.diags(
        diagonals=[lower_diag[1:], main_diag, upper_diag[:-1]],
        offsets=[-1, 0, 1],
        format='csr'
    )

    # Time stepping (backward in time)
    for n in reversed(range(NT - 1)):
        rhs = V[1:-1, n+1].copy()
        
        # Apply boundary conditions at current time step
        tau = (NT - 1 - n) * dt
        disc = np.exp(-model.r * tau)

        if option_type == 'put':
            V[0, n] = model.K * disc
            V[-1, n] = 0
        else:  # call
            V[0, n] = 0
            V[-1, n] = S_grid[-1] - model.K * disc

        # Incorporate boundary conditions into RHS
        rhs[0]  += alpha * V[0, n]
        rhs[-1] += gamma * V[-1, n]

        # Solve linear system
        V[1:-1, n] = sparse.linalg.spsolve(A, rhs)

        # Early exercise for American options
        if early_exercise:
            V[1:-1, n] = np.maximum(V[1:-1, n], model._payoff(S_grid[1:-1], option_type))

    return S_grid, V[:, 0]

def cn_log_scheme(model, option_type='put', Smin=1e-3, Smax=500, NX=100, NT=100, early_exercise=False):
    """Crank-Nicolson finite difference scheme in log-price space."""
    dx, dt, x_grid, S_grid, _, _ = setup_log_grid(Smin, Smax, NX, NT, model.T)

    V = np.zeros((NX, NT))
    V[:, -1] = model._payoff(S_grid, option_type)

    # Log-space finite difference coefficients
    nu = model.r - model.q - 0.5 * model.sigma**2
    sigma2 = model.sigma ** 2

    alpha = 0.25 * dt * ((sigma2/dx**2) - (nu/dx))
    beta  = 0.5 * dt * ((sigma2/dx**2) + model.r)
    gamma = 0.25 * dt * ((sigma2/dx**2) + (nu/dx))

    # Build matrices for Crank-Nicolson
    lower_diag = -alpha * np.ones(NX-2)
    main_diag  = (1 + beta) * np.ones(NX-2)
    upper_diag = -gamma * np.ones(NX-2)

    B_lower_diag = alpha * np.ones(NX-2)
    B_main_diag  = (1 - beta) * np.ones(NX-2)
    B_upper_diag = gamma * np.ones(NX-2)

    A = sparse.diags([lower_diag[1:], main_diag, upper_diag[:-1]],
                    offsets=[-1, 0, 1], format='csr')

    B = sparse.diags([B_lower_diag[1:], B_main_diag, B_upper_diag[:-1]],
                    offsets=[-1, 0, 1], format='csr')

    # Time stepping (backward in time)
    for n in reversed(range(NT - 1)):
        # Apply boundary conditions at current and next time steps
        tau_current = (NT - 1 - n) * dt
        tau_next = (NT - n) * dt
        disc_current = np.exp(-model.r * tau_current)
        disc_next = np.exp(-model.r * tau_next)

        if option_type == 'put':
            V[0, n] = model.K * disc_current
            V[-1, n] = 0
            # Boundary values at next time step
            bc_0_next = model.K * disc_next
            bc_end_next = 0
        else:  # call
            V[0, n] = 0
            V[-1, n] = S_grid[-1] - model.K * disc_current
            # Boundary values at next time step
            bc_0_next = 0
            bc_end_next = S_grid[-1] - model.K * disc_next

        # Right-hand side for Crank-Nicolson
        rhs = B @ V[1:-1, n+1]
        rhs[0]  += alpha * (bc_0_next + V[0, n])
        rhs[-1] += gamma * (bc_end_next + V[-1, n])

        # Solve linear system
        V[1:-1, n] = sparse.linalg.spsolve(A, rhs)

        # Early exercise for American options
        if early_exercise:
            V[1:-1, n] = np.maximum(V[1:-1, n], model._payoff(S_grid[1:-1], option_type))

    return S_grid, V[:, 0]