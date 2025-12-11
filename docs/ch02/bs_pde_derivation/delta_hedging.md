

**Setup:** Consider a stock price process following geometric Brownian motion:

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

where $\mu$ is the drift, $\sigma$ is the volatility, and $W_t$ is a standard Brownian motion.

**Step 1: Construct a self-financing portfolio**

Consider a portfolio $\Pi_t$ consisting of:

- Long position in one derivative with value $V(S_t, t)$

- Short position in $\Delta$ shares of the underlying stock

$$\Pi_t = V(S_t, t) - \Delta S_t$$

**Step 2: Apply Itô's lemma**

By Itô's lemma, the derivative price satisfies:

$$dV = \left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt + \sigma S \frac{\partial V}{\partial S} dW_t$$

**Step 3: Compute portfolio dynamics**

$$\begin{array}{lll}
\displaystyle d\Pi_t 
&=&\displaystyle dV - \Delta dS_t \\
&=&\displaystyle \left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt + \sigma S \frac{\partial V}{\partial S} dW_t - \Delta(\mu S dt + \sigma S dW_t)
\end{array}$$

**Step 4: Eliminate risk (delta hedging)**

Choose $\Delta = \frac{\partial V}{\partial S}$ to eliminate the stochastic term:

$$d\Pi_t = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt$$

**Step 5: No-arbitrage condition**

Since $\Pi_t$ is now riskless, it must earn the risk-free rate $r$:

$$d\Pi_t = r\Pi_t dt = r\left(V - S\frac{\partial V}{\partial S}\right)dt$$

**Step 6: Black-Scholes PDE**

Equating the two expressions for $d\Pi_t$:

$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

