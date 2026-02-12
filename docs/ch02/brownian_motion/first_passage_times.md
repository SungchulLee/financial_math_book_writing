# First Passage Times

First passage times represent the random time at which a Brownian motion first hits a particular level or set. They are fundamental to understanding the dynamics of stochastic processes and have widespread applications in financial modeling, particularly in option pricing and credit risk.

## Key Concepts

**Hitting Times Definition**
The first passage time (or hitting time) $\tau_a$ to a level $a$ is defined as:
$$\tau_a = \inf\{t \geq 0 : B_t = a\}$$
where $B_t$ is a standard Brownian motion and $a$ is a target level.

**Reflection Principle**
The reflection principle states that for a Brownian motion starting at 0, the probability of hitting level $a > 0$ before time $T$ and ending at level $b < a$ equals the probability of reaching level $2a - b$. This principle is crucial for computing distributions of first passage times.

**Distributions of First Passage Times**
For a standard Brownian motion starting at 0:
- The density of hitting time $\tau_a$ is: $f_{\tau_a}(t) = \frac{|a|}{\sqrt{2\pi t^3}} \exp\left(-\frac{a^2}{2t}\right)$
- This follows an inverse Gaussian distribution
- The survival probability is: $P(\tau_a > t) = 2\Phi\left(-\frac{|a|}{\sqrt{t}}\right)$

**Barrier Option Applications**
First passage times directly price knock-out and knock-in barrier options through the relationship between hitting times and barrier crossing probabilities.

!!! note "Key Applications"
    First passage times are used extensively in:
    - Barrier option pricing (knock-out, knock-in barriers)
    - Credit default swap valuation (first time a credit spread crosses a threshold)
    - Optimal stopping and exercise decisions
    - Drawdown and Merton portfolio choice problems
