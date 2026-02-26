"""
Annuity mortgage payment profile computation.

Based on "Financial Engineering" course by L.A. Grzelak and Emanuele Casamassima.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak and Emanuele Casamassima
"""
import numpy as np
import matplotlib.pyplot as plt


def annuity(rate, notional, periods, cpr):
    """
    Compute annuity mortgage payment profile.

    Returns a matrix M where each row contains:
    [t, notional(t), prepayment(t), notional_quote(t), interest_quote(t), installment(t)]

    Note: 'rate' and 'periods' are general. The choice of year/month/day steps
    depends on the rate provided. Pass the correct rate to match the time step.

    Parameters
    ----------
    rate : float
        Periodic interest rate
    notional : float
        Initial loan amount
    periods : int
        Number of periods
    cpr : float
        Conditional prepayment rate

    Returns
    -------
    ndarray
        Shape (periods+1, 6) containing payment profile over time
    """
    m = np.zeros((periods + 1, 6))
    m[:, 0] = np.arange(periods + 1)
    m[0, 1] = notional

    for t in range(1, periods + 1):
        # Remaining periods for amortization
        remaining_periods = periods - (t - 1)

        # Installment, C(t_i)
        m[t, 5] = rate * m[t - 1, 1] / (1 - 1 / (1 + rate) ** remaining_periods)

        # Interest payment, I(t_i) = rate * N(t_i)
        m[t, 4] = rate * m[t - 1, 1]

        # Notional payment, Q(t_i) = C(t_i) - I(t_i)
        m[t, 3] = m[t, 5] - m[t, 4]

        # Prepayment, P(t_i) = CPR * (N(t_i) - Q(t_i))
        m[t, 2] = cpr * (m[t - 1, 1] - m[t, 3])

        # Notional, N(t_{i+1}) = N(t_i) - Q(t_i) - P(t_i)
        m[t, 1] = m[t - 1, 1] - m[t, 3] - m[t, 2]

    return m


def plot_notional(m, periods):
    """
    Plot notional balance over time.

    Parameters
    ----------
    m : ndarray
        Payment profile matrix from annuity() function
    periods : int
        Number of periods
    """
    plt.figure(1)
    plt.plot(m[:, 0], m[:, 1], '.r')
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('notional')


def main():
    """Run annuity mortgage analysis."""
    # ============= Parameters =============
    n0 = 1000000  # Initial notional
    r = 0.05      # Interest rate
    cpr = 0.1     # Conditional prepayment rate (10%)
    t_end = 30    # Number of periods (yearly payments)

    # ============= Computation =============
    m = annuity(r, n0, t_end, cpr)

    # ============= Output =============
    for i in range(0, t_end + 1):
        print("Ti={0}, Notional={1:.0f}, Prepayment={2:.0f}, "
              "Notional Repayment={3:.0f}, Interest Rate={4:.0f}, "
              "Installment={5:.0f}".format(m[i, 0], m[i, 1], m[i, 2],
                                           m[i, 3], m[i, 4], m[i, 5]))

    # ============= Plotting =============
    plot_notional(m, t_end)


if __name__ == "__main__":
    main()
