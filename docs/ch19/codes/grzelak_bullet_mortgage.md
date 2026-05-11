# Bullet Mortgage

## Background

Bullet mortgage payment profile computation.

Based on "Financial Engineering" course by L.A. Grzelak and Emanuele Casamassima.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak and Emanuele Casamassima

---

## Code

```python
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


# ======================================================================
# Functions / Classes
# ======================================================================


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


# ======================================================================
# Main
# ======================================================================

if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
For a bullet mortgage with notional \$1,000,000, annual rate $5\%$, term 30 years, and CPR $= 1\%$, compute the interest payment and installment in year 1.

??? success "Solution to Exercise 1"
    In a bullet mortgage, the notional repayment is zero until the final period. In year 1:

    - Interest payment: $I_1 = r \times N_0 = 0.05 \times 1{,}000{,}000 = \$50{,}000$
    - Notional quote: $Q_1 = 0$ (bullet structure)
    - Prepayment: $P_1 = \text{CPR} \times (N_0 - Q_1) = 0.01 \times 1{,}000{,}000 = \$10{,}000$
    - Installment: $C_1 = I_1 + Q_1 + P_1 = 50{,}000 + 0 + 10{,}000 = \$60{,}000$

---

**Exercise 2.**
Compare the total interest paid over the life of a bullet mortgage versus an annuity mortgage (both with \$1,000,000 notional, $5\%$ rate, 30 years, and zero prepayment).

??? success "Solution to Exercise 2"
    For the bullet mortgage with no prepayment, the full notional is outstanding for all 30 years:

    $$
    \text{Total interest (bullet)} = r \times N_0 \times n = 0.05 \times 1{,}000{,}000 \times 30 = \$1{,}500{,}000.
    $$

    For the annuity mortgage, the annual installment is $C \approx \$65{,}051$ (from the annuity formula). Total payments: $65{,}051 \times 30 = \$1{,}951{,}530$. Total interest: $1{,}951{,}530 - 1{,}000{,}000 = \$951{,}530$.

    The bullet mortgage costs $\$1{,}500{,}000$ in interest versus $\$951{,}530$ for the annuity, because the annuity amortizes the principal over time, reducing the interest base.

---

**Exercise 3.**
In a bullet mortgage with CPR $= 1\%$, what is the remaining notional after 10 years (assuming no scheduled amortization)?

??? success "Solution to Exercise 3"
    With only prepayment reducing the notional each year, the remaining notional after $k$ years is approximately

    $$
    N_k \approx N_0 \times (1 - \text{CPR})^k = 1{,}000{,}000 \times (0.99)^{10}.
    $$

    Computing: $(0.99)^{10} = 0.9044$, so $N_{10} \approx \$904{,}382$.

    After 10 years, about $9.6\%$ of the original notional has been prepaid.

---

**Exercise 4.**
Explain why the final period of a bullet mortgage is treated differently in the code, and what happens to the installment at maturity.

??? success "Solution to Exercise 4"
    In the final period (year 30), the entire remaining notional must be repaid. The code sets $Q_n = N_{n-1}$ (the full outstanding balance), while in all prior periods $Q_t = 0$. The final installment is therefore

    $$
    C_n = I_n + Q_n = r \times N_{n-1} + N_{n-1} = N_{n-1}(1 + r).
    $$

    This creates a large final payment ("balloon payment"), which is the defining feature of a bullet mortgage. Without prepayments, $N_{29} = \$1{,}000{,}000$, so the final installment is $1{,}000{,}000 \times 1.05 = \$1{,}050{,}000$. This concentration of principal repayment at maturity creates significant refinancing risk.
