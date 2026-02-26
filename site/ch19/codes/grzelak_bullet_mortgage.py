"""
Bullet mortgage payment profile computation.

Based on "Financial Engineering" course by L.A. Grzelak and Emanuele Casamassima.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak and Emanuele Casamassima
"""
import numpy as np
import matplotlib.pyplot as plt


def bullet(rate, notional, periods, cpr):
    """
    Compute bullet mortgage payment profile.

    Returns a matrix M where each row contains:
    [t, notional(t), prepayment(t), notional_quote(t), interest_(t), installment(t)]

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

    for t in range(1, periods):
        m[t, 4] = rate * m[t - 1, 1]      # Interest quote
        m[t, 3] = 0                       # Notional quote (zero for bullet)
        scheduled_outstanding = m[t - 1, 1] - m[t, 3]
        m[t, 2] = scheduled_outstanding * cpr     # Prepayment
        # Notional at next time
        m[t, 1] = scheduled_outstanding - m[t, 2]
        m[t, 5] = m[t, 4] + m[t, 2] + m[t, 3]    # Installment

    # Final period: principal and all interest due
    m[periods, 4] = rate * m[periods - 1, 1]     # Interest quote
    m[periods, 3] = m[periods - 1, 1]            # Notional quote (full principal)
    m[periods, 5] = m[periods, 4] + m[periods, 2] + m[periods, 3]

    return m


def plot_notional(m, periods):
    """
    Plot notional balance over time.

    Parameters
    ----------
    m : ndarray
        Payment profile matrix from bullet() function
    periods : int
        Number of periods
    """
    plt.figure(1)
    plt.plot(m[:, 0], m[:, 1], '-r')
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('notional')


def main():
    """Run bullet mortgage analysis."""
    # ============= Parameters =============
    n0 = 1000000  # Initial notional
    r = 0.05      # Interest rate
    cpr = 0.01    # Conditional prepayment rate (1%)
    t_end = 30    # Number of periods (yearly payments)

    # ============= Computation =============
    m = bullet(r, n0, t_end, cpr)

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
