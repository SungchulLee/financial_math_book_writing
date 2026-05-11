# Annuity Mortgage

## Background

Annuity mortgage payment profile computation.

Based on "Financial Engineering" course by L.A. Grzelak and Emanuele Casamassima.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak and Emanuele Casamassima

---

## Code

```python
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


# ======================================================================
# Functions / Classes
# ======================================================================


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


# ======================================================================
# Main
# ======================================================================

if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
For an annuity mortgage with notional \$1,000,000, annual rate $5\%$, and 30-year term with no prepayment, compute the constant annual installment $C$.

??? success "Solution to Exercise 1"
    The annuity installment formula is

    $$
    C = \frac{r \cdot N_0}{1 - (1 + r)^{-n}} = \frac{0.05 \times 1{,}000{,}000}{1 - (1.05)^{-30}}.
    $$

    Computing $(1.05)^{-30} = 1/4.3219 = 0.2314$:

    $$
    C = \frac{50{,}000}{1 - 0.2314} = \frac{50{,}000}{0.7686} \approx \$65{,}051.
    $$

---

**Exercise 2.**
In the first year of the mortgage from Exercise 1, compute the interest payment, notional repayment, and remaining notional.

??? success "Solution to Exercise 2"

    - Interest payment: $I_1 = r \times N_0 = 0.05 \times 1{,}000{,}000 = \$50{,}000$
    - Notional repayment: $Q_1 = C - I_1 = 65{,}051 - 50{,}000 = \$15{,}051$
    - Remaining notional: $N_1 = N_0 - Q_1 = 1{,}000{,}000 - 15{,}051 = \$984{,}949$

    In an annuity mortgage, the interest portion decreases over time while the notional repayment increases, keeping the total installment constant.

---

**Exercise 3.**
If a conditional prepayment rate (CPR) of $10\%$ is applied, the prepayment at time $t$ is $P_t = \text{CPR} \times (N_{t-1} - Q_t)$. Compute the prepayment and new notional after year 1 using the values from Exercise 2.

??? success "Solution to Exercise 3"
    The prepayment is

    $$
    P_1 = 0.10 \times (N_0 - Q_1) = 0.10 \times (1{,}000{,}000 - 15{,}051) = 0.10 \times 984{,}949 = \$98{,}495.
    $$

    The new remaining notional is

    $$
    N_1 = N_0 - Q_1 - P_1 = 1{,}000{,}000 - 15{,}051 - 98{,}495 = \$886{,}454.
    $$

    The prepayment significantly accelerates the reduction of the outstanding balance.

---

**Exercise 4.**
Explain how prepayments affect the cash flow profile of an annuity mortgage and why mortgage-backed securities (MBS) investors face prepayment risk.

??? success "Solution to Exercise 4"
    With prepayments, the outstanding notional decreases faster than scheduled. This has several effects:

    1. The interest portion of future payments shrinks because the remaining balance is smaller.
    2. The recalculated installment for subsequent periods is lower (computed from a smaller notional over fewer remaining periods).
    3. The total interest paid over the life of the mortgage is reduced.

    For MBS investors, prepayment risk manifests as reinvestment risk: when rates fall, borrowers prepay (refinance at lower rates), returning principal to investors who must reinvest at lower yields. Conversely, when rates rise, prepayments slow, extending the effective duration of the MBS beyond expectations. This asymmetric behavior creates negative convexity in MBS pricing.
