"""
Jamshidian's trick for handling E[max(sum, K)] as sum of E[max].

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def psi_sum(psi, n, x):
    """Compute sum of psi_i."""
    temp = 0
    for i in range(0, n):
        temp = temp + psi(i, x)
    return temp


def jamshidian_trick(psi, n, k):
    """Compute optimal strike using Jamshidian's trick."""
    a = lambda x: psi_sum(psi, n, x) - k
    result = optimize.newton(a, 0.1)
    return result


def main():
    """Main computation."""
    num_samples = 1000
    x = np.random.normal(0.0, 1.0, (num_samples, 1))
    psi_i = lambda i, x: np.exp(-i * np.abs(x))

    # Number of terms
    n = 15

    a = 0
    for i in range(0, n):
        a = a + psi_i(i, x)

    k = np.linspace(2, 10, 10)
    result_mc = np.zeros(len(k))
    for (i, ki) in enumerate(k):
        result_mc[i] = np.mean(np.maximum(a - ki, 0))

    # Jamshidian's trick
    result_jams = np.zeros(len(k))
    for i, ki in enumerate(k):
        # Compute optimal K*
        opt_x = jamshidian_trick(psi_i, n, ki)
        a = 0
        for j in range(0, n):
            a = a + np.mean(np.maximum(psi_i(j, x) - psi_i(j, opt_x), 0))
        result_jams[i] = a

    plt.figure()
    plt.plot(k, result_mc)
    plt.plot(k, result_jams, '--r')
    plt.grid()
    plt.xlabel('K')
    plt.ylabel('expectation')
    plt.legend(['Monte Carlo', "Jamshidian's trick"])


if __name__ == "__main__":
    main()
