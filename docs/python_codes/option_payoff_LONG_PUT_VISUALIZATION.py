import numpy as np
import matplotlib.pyplot as plt

# ---------------- Inputs ----------------
ticker = "TSLA"
K = 200
prem = 10.00
S0 = 200  # current price (for vertical line)

breakeven = K - prem
max_loss  = -prem
max_profit = (K - prem)  # if stock -> 0

# Price grid (match your plot range)
S = np.linspace(100, 260, 600)
pnl = np.maximum(K - S, 0) - prem

# ---------------- Plot ----------------
fig, ax = plt.subplots(figsize=(14, 6), dpi=150)

# Main P&L
ax.plot(S, pnl, linewidth=2.8, label="Long Put P&L")

# Regions
ax.fill_between(S, pnl, 0, where=(pnl >= 0), alpha=0.25, label="Profit Region")
ax.fill_between(S, pnl, 0, where=(pnl < 0),  alpha=0.25, label="Loss Region")

# Reference lines
ax.axhline(0, linewidth=1.2, label="Breakeven (P&L=0)")
ax.axvline(K, linestyle="--", linewidth=1.2, label=f"Strike: ${K:.0f}")
ax.axvline(S0, linestyle="--", linewidth=1.2, label=f"Current Price: ${S0:.0f}")
ax.axvline(breakeven, linestyle=":", linewidth=1.6, label=f"Breakeven: ${breakeven:.2f}")

# Labels
ax.set_xlabel("Stock Price at Expiration ($)")
ax.set_ylabel("Profit / Loss ($)")
ax.grid(True, alpha=0.25)

# ---------------- FIXED TITLE: ALL BOLD + SPACING + MISSING SPACES ----------------
# NOTE: add spaces explicitly so you never get "200Putfor10"
title = (
    f"Real-World Example: {ticker} {K:.0f} Put for {prem:.0f}\n"
    f"Strike: {K:.0f} | Premium: {prem:.2f}\n"
    f"Max Profit: ${max_profit:.2f} | Max Loss: ${max_loss:.2f} | Breakeven: ${breakeven:.2f}"
)
fig.suptitle(title, fontweight="bold", y=1.02)

# ---------------- Layout fix (avoid clipping) ----------------
fig.tight_layout()
fig.subplots_adjust(top=0.82)  # increase if you want more headroom

ax.legend(loc="upper right", fontsize=8)

plt.savefig("tsla_long_put_bold_title_fixed_spacing.png", bbox_inches="tight")
plt.show()
