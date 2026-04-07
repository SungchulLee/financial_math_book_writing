# Margin and Short Positions

When an investor buys an option, the maximum loss is the premium paid — a known, finite amount settled at the time of purchase. The writer of that same option, however, accepts an obligation whose eventual cost depends on the future path of the underlying. This fundamental asymmetry between bounded and potentially unbounded loss is the reason margin requirements exist: they ensure that option writers can meet their obligations when called upon.

---

## Risk Asymmetry Between Buyer and Writer

The holder of a call option pays the premium $C_0$ and receives the payoff $(S_T - K)^+$ at maturity. The worst outcome is that the option expires worthless and the holder loses $C_0$. The same bounded-loss argument applies to put holders, whose maximum loss is the premium $P_0$.

Writers face the opposite situation. The writer of a **naked call** (a call written without holding the underlying asset) receives $C_0$ but must deliver the payoff $(S_T - K)^+$. Since $S_T$ is unbounded above, the writer's loss

$$
L_{\text{call}} = (S_T - K)^+ - C_0
$$

has no finite upper bound. As $S_T \to \infty$, the loss grows without limit.

The writer of a **naked put** receives $P_0$ and must pay $(K - S_T)^+$. Because $S_T \geq 0$, the maximum loss is bounded:

$$
L_{\text{put}} = (K - S_T)^+ - P_0 \leq K - P_0
$$

This worst case occurs when $S_T = 0$. Although the loss is finite, it can still be very large relative to the premium received when $K$ is large.

| Position | Maximum gain | Maximum loss |
|---|---|---|
| Long call | Unlimited | $C_0$ |
| Short (naked) call | $C_0$ | Unlimited |
| Long put | $K - P_0$ | $P_0$ |
| Short (naked) put | $P_0$ | $K - P_0$ |

---

## Margin as a Performance Guarantee

Because the exchange stands between buyer and writer as the central counterparty, it must ensure that every writer can fulfill the contract. **Margin** is the collateral — typically cash or eligible securities — that the writer deposits with the broker to guarantee performance.

The initial margin is set at the time the position is opened. For a naked call, the required margin is larger than for a naked put, reflecting the unbounded loss profile. Covered positions (e.g., a call written while holding the underlying stock) require substantially less margin because the writer's obligation is offset by the asset already held.

---

## Margin Calls and Maintenance

As the underlying price moves against the writer's position, the margin account may fall below a prescribed **maintenance margin** level. When this happens, the broker issues a **margin call**, requiring the writer to deposit additional funds promptly — often within one trading day. Failure to meet the margin call allows the broker to close the position, crystallizing the loss.

This mechanism prevents the accumulation of unrealized losses that the writer cannot cover, protecting both the counterparty and the integrity of the exchange.

---

## Exercises

**Exercise 1.** An investor writes a naked call with strike $K = 80$ for a premium of \$5. Compute the writer's profit or loss at maturity when (a) $S_T = 70$, (b) $S_T = 90$, and (c) $S_T = 120$.

??? success "Solution to Exercise 1"
    The writer's profit at maturity is $C_0 - (S_T - K)^+$.

    (a) $S_T = 70 < K = 80$: the call expires worthless. Profit $= 5 - 0 = \$5$.

    (b) $S_T = 90 > K = 80$: the writer pays the payoff. Profit $= 5 - (90 - 80) = 5 - 10 = -\$5$.

    (c) $S_T = 120 > K = 80$: Profit $= 5 - (120 - 80) = 5 - 40 = -\$35$.

    As $S_T$ increases, the writer's loss grows without bound.

---

**Exercise 2.** An investor writes a naked put with strike $K = 60$ for a premium of \$4. Determine the maximum possible loss and the value of $S_T$ at which it occurs.

??? success "Solution to Exercise 2"
    The writer's loss at maturity is $(K - S_T)^+ - P_0$. The worst case occurs when $S_T = 0$:

    $$
    L_{\max} = (60 - 0) - 4 = \$56
    $$

    Unlike the naked call writer, the naked put writer's loss is bounded. The maximum loss is $K - P_0 = 60 - 4 = \$56$, occurring when the underlying asset becomes worthless.

---

**Exercise 3.** Explain why a covered call (writing a call while holding the underlying stock) requires less margin than a naked call. Describe what happens to the writer's overall position when $S_T > K$.

??? success "Solution to Exercise 3"
    A naked call writer must deliver a stock worth $S_T$ in exchange for $K$ when $S_T > K$. Since $S_T$ is unbounded, the potential outlay is unlimited, and the margin must reflect this open-ended risk.

    A covered call writer already holds the stock. If $S_T > K$, the writer delivers the stock (already owned) and receives $K$. The writer forgoes the upside above $K$ but does not need to purchase the stock at the market price. The worst outcome is opportunity cost, not an out-of-pocket loss.

    Because the obligation is fully offset by the asset held, the covered call has a bounded risk profile, and exchanges accordingly require far less margin collateral.

---

**Exercise 4.** A trader writes a naked call at strike $K = 100$ and posts an initial margin of \$15 per share. Suppose the maintenance margin is \$10 per share and the premium received is \$6. If the stock price rises from \$95 to \$108 after one day, determine whether a margin call is triggered by comparing the margin account balance to the maintenance requirement.

??? success "Solution to Exercise 4"
    At inception the margin account holds the initial margin plus the premium received: $15 + 6 = \$21$ per share.

    After the stock rises to \$108, the call is in the money with intrinsic value $(108 - 100)^+ = 8$. The unrealized loss to the writer is \$8 per share, reducing the margin account balance to $21 - 8 = \$13$ per share.

    Since \$13 exceeds the maintenance margin of \$10, no margin call is triggered. However, if the stock were to rise further to, say, \$112 (unrealized loss of \$12, balance $= 21 - 12 = \$9 < \$10$), a margin call would be issued.
