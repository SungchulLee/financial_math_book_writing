# ---
# title: "DX Framework — Option Statistics Plotter"
# description: >
#   Utility function that produces a three-panel figure showing
#   option present value, Delta, and Vega as functions of the
#   initial underlying price.  Useful for visualising the Greeks
#   computed by the DX valuation classes.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import matplotlib.pyplot as plt


def plot_option_stats(s_list, p_list, d_list, v_list, title=''):
    """Plot option value, Delta, and Vega across underlying prices.

    Parameters
    ----------
    s_list : array-like
        Initial underlying values (x-axis for all three panels).
    p_list : array-like
        Present values (top panel).
    d_list : array-like
        Delta values (middle panel).
    v_list : array-like
        Vega values (bottom panel).
    title : str, optional
        Super-title for the figure.
    """
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    if title:
        fig.suptitle(title, fontsize=13)

    # ── Present value ───────────────────────────────────────────
    ax1.plot(s_list, p_list, 'ro-', markersize=4, label='Present Value')
    ax1.set_ylabel('Option Value')
    ax1.legend(loc='best')
    ax1.grid(alpha=0.3)

    # ── Delta ───────────────────────────────────────────────────
    ax2.plot(s_list, d_list, 'gs-', markersize=4, label='Delta')
    ax2.set_ylabel('Delta')
    ax2.set_ylim(min(d_list) - 0.1, max(d_list) + 0.1)
    ax2.legend(loc='best')
    ax2.grid(alpha=0.3)

    # ── Vega ────────────────────────────────────────────────────
    ax3.plot(s_list, v_list, 'b^-', markersize=4, label='Vega')
    ax3.set_xlabel('Initial Value of Underlying')
    ax3.set_ylabel('Vega')
    ax3.legend(loc='best')
    ax3.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
