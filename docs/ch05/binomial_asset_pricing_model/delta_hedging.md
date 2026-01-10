# Delta as a Hedging Strategy (Dynamic Replication)

## Purpose of This Section

This section introduces **delta hedging** as a **dynamic trading strategy** in a multi-period binomial tree.


Here, delta is no longer a single number but a **process**:




$$
\{ \Delta_{n,j} \}_{n,j}



---


## Multi-Period Tree Setup


Let the stock evolve on a recombining binomial tree:



S_{n+1,j+1} = u S_{n,j}, \qquad
S_{n+1,j} = d S_{n,j}



Let the option value at node $(n,j)$ be $V_{n,j}$.


## Node-by-Node Delta


At each node, define



\boxed{
\Delta_{n,j}
= \frac{V_{n+1,j+1} - V_{n+1,j}}{(u-d)S_{n,j}}

}



This is the **local hedge ratio** at that node.



## Self-Financing Rebalancing


At each time step:

1. Hold $\Delta_{n,j}$ shares of stock
2. Invest the remainder in the bank account
3. Rebalance after each move

The portfolio remains **self-financing**.



## Interpretation


- Delta hedging is **path-dependent**



- The hedge must be **updated dynamically**



- Perfect replication holds only in the binomial limit



## Link to Continuous Time

As $d t \to 0$:


- The tree converges to geometric Brownian motion



- Discrete delta hedging converges to continuous hedging



- This leads to the Black–Scholes PDE



## Key Takeaway

> **Delta hedging is a trading strategy, not a pricing identity.**


Pricing comes from replication; hedging is how replication is implemented over time.
