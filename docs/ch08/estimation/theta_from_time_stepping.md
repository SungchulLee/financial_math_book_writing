# Theta from Time Stepping

Theta ($\Theta$) measures the rate at which an option's value decays with the passage of time. Unlike delta and gamma, which are spatial derivatives readily available from the FDM grid, theta involves the time direction and can be extracted either directly from the time-stepping process or indirectly through the Black-Scholes PDE.

---

## Definition and Sign Convention

Theta is defined as the partial derivative of the option price with respect to calendar time:

$$
\Theta = \frac{\partial V}{\partial t}
$$

Since the time-to-maturity formulation uses $\tau = T - t$, the relationship between the two conventions is:

$$
\frac{\partial V}{\partial t} = -\frac{\partial u}{\partial \tau}
$$

where $u(\tau, S) = V(T - \tau, S)$.

!!! info "Sign Convention"
    For a long position in a standard European option (call or put), theta is typically **negative**: the option loses value as time passes (all else equal). This is called **time decay**. The negative sign arises because $\partial u / \partial \tau > 0$ (the solution grows when marching forward in $\tau$), so $\Theta = -\partial u / \partial \tau < 0$.

---

## Direct Extraction from Time Stepping

### Backward Difference (First-Order)

The simplest approach uses two consecutive time levels from the FDM solution. At the final time step (corresponding to $t = 0$), the solution at time levels $n = N$ and $n = N-1$ gives:

$$
\frac{\partial u}{\partial \tau}\bigg|_{\tau = T} \approx \frac{u_j^N - u_j^{N-1}}{\Delta\tau}
$$

Converting to theta:

$$
\boxed{\Theta_j \approx -\frac{u_j^N - u_j^{N-1}}{\Delta\tau}}
$$

This is a **backward difference** in $\tau$ (equivalently, a forward difference in calendar time $t$), with truncation error $O(\Delta\tau)$.

### Central Difference (Second-Order)

Using three time levels:

$$
\Theta_j \approx -\frac{u_j^N - u_j^{N-2}}{2\Delta\tau}
$$

with truncation error $O((\Delta\tau)^2)$. This requires storing an additional time level.

### Practical Considerations

The quality of the time-step theta estimate depends on:

1. **Time step size $\Delta\tau$**: Smaller $\Delta\tau$ reduces truncation error but amplifies rounding error
2. **Scheme used**: For the explicit scheme, the time derivative is computed explicitly from the spatial operator. For implicit and Crank-Nicolson, the time derivative is embedded in the linear system
3. **Proximity to expiry**: Near $\tau = 0$ (close to expiry), theta can be very large for at-the-money options, requiring fine time resolution

---

## PDE-Based Theta Estimation

### Using the Black-Scholes PDE

Since the Black-Scholes PDE relates all the Greeks:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

Theta can be computed from the spatial Greeks without using the time direction at all:

$$
\boxed{\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma}
$$

This uses the delta and gamma values extracted directly from the spatial grid at the final time level $n = N$.

### Advantages of the PDE Approach

1. **No time differencing**: Avoids the $O(\Delta\tau)$ or $O((\Delta\tau)^2)$ error from time differences
2. **Uses only spatial data**: Delta and gamma at the final time level suffice
3. **Higher effective accuracy**: If delta and gamma are $O((\Delta S)^2)$ accurate, the PDE-derived theta inherits this accuracy
4. **No extra storage**: Does not require saving previous time levels

!!! tip "Recommended Approach"
    In practice, the PDE-based theta estimate is preferred over direct time-step differencing because it leverages the more accurate spatial derivatives and avoids the coarser time resolution.

---

## Comparison of the Two Approaches

### Accuracy Analysis

**Direct time-step theta**: The error has two components:

$$
\text{Error} = O(\Delta\tau) + O((\Delta S)^2)
$$

The $O(\Delta\tau)$ term comes from the backward difference in time. For first-order schemes (explicit, implicit), the time step is already $O(\Delta\tau)$, so the theta estimate inherits this. For Crank-Nicolson, the scheme itself is $O((\Delta\tau)^2)$, but a one-sided time difference reduces the theta estimate to $O(\Delta\tau)$.

**PDE-based theta**: The error is:

$$
\text{Error} = O((\Delta S)^2)
$$

provided delta and gamma are computed with central differences. There is no $\Delta\tau$ component at all.

### When Direct Time-Step Theta is Preferred

Despite its lower accuracy, direct time-step theta has uses:

1. **Verification**: Comparing the two estimates provides a consistency check
2. **Non-constant parameters**: When $\sigma$ or $r$ are time-dependent, the PDE relationship changes, but the direct estimate remains straightforward
3. **Multi-step schemes**: For multi-step time integrators, the time-step history gives the most natural theta estimate

---

## Theta Near Expiry

### At-the-Money Behavior

For an at-the-money European call ($S \approx K$) near expiry ($\tau \to 0$), the Black-Scholes formula gives:

$$
\Theta_{\text{ATM}} \approx -\frac{\sigma S}{2\sqrt{2\pi\tau}}
$$

This diverges as $\tau \to 0^+$: at-the-money options lose value at an accelerating rate near expiry.

### Implications for Numerical Methods

Near expiry, theta is large and changes rapidly. This creates challenges:

1. **Time resolution**: The backward time difference $\Theta \approx -(u^N - u^{N-1})/\Delta\tau$ averages theta over the interval $[\tau_{N-1}, \tau_N]$, missing the rapid variation near $\tau = 0$
2. **Non-uniform time grids**: Using smaller time steps near $\tau = 0$ improves the theta estimate. A geometric or exponential time grid concentrates steps where theta changes most rapidly
3. **PDE-based theta**: The formula $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2\Gamma$ correctly captures the pointwise theta, even near expiry, as long as the spatial Greeks are accurate

---

## Theta for Different Option Types

### European Call

At $t = 0$ (long before expiry), from the Black-Scholes formula:

$$
\Theta_{\text{call}} = -\frac{\sigma S \phi(d_1)}{2\sqrt{T}} - rKe^{-rT}\Phi(d_2)
$$

where $\phi$ is the standard normal density and $\Phi$ is the cumulative normal distribution. Both terms are negative, so $\Theta_{\text{call}} < 0$.

### European Put

$$
\Theta_{\text{put}} = -\frac{\sigma S \phi(d_1)}{2\sqrt{T}} + rKe^{-rT}\Phi(-d_2)
$$

For deep in-the-money puts, the second term can dominate, making $\Theta_{\text{put}} > 0$: a deep ITM put can actually gain value with time passage because the present value of the exercise proceeds increases.

### On the FDM Grid

The FDM naturally handles all these cases. The theta estimate at each grid node $S_j$ reflects the local behavior of the option, including the sign change for deep ITM puts.

---

## Theta and the Theta-Scheme Parameter

The name "theta" is overloaded in finite difference methods:

- **Greek theta** ($\Theta = \partial V / \partial t$): a property of the option price
- **Scheme parameter theta** ($\theta \in [0, 1]$): the weighting between explicit and implicit time stepping

These are unrelated concepts that unfortunately share the same name. In this section, $\Theta$ always denotes the Greek, and $\theta$ the scheme parameter.

The theta-scheme:

$$
(I - \theta\Delta\tau A)\mathbf{u}^{n+1} = (I + (1-\theta)\Delta\tau A)\mathbf{u}^n
$$

does not directly correspond to the Greek theta, though both involve the time direction.

---

## Worked Example

Consider a European call with $K = 100$, $S = 100$, $T = 0.25$, $\sigma = 0.2$, $r = 0.05$.

**Exact Black-Scholes values**:

- $V = 3.934$
- $\Delta = 0.5594$
- $\Gamma = 0.0393$
- $\Theta = -11.35$ (annualized)

**FDM with Crank-Nicolson** ($M = 200$, $N = 100$):

- $V_j = 3.933$ (error $\sim 10^{-3}$)
- $\Delta_j = 0.5593$ (central difference)
- $\Gamma_j = 0.0392$ (central difference)

**PDE-based theta**:

$$
\Theta = 0.05 \times 3.933 - 0.05 \times 100 \times 0.5593 - \frac{1}{2}(0.04)(10000)(0.0392) = -11.34
$$

**Direct time-step theta** (backward difference):

$$
\Theta \approx -(u_j^{100} - u_j^{99}) / \Delta\tau
$$

This gives approximately $-11.3$, consistent but slightly less accurate than the PDE-based estimate.

---

## Summary

| Method | Formula | Accuracy | Cost |
|--------|---------|----------|------|
| Backward difference | $-(u_j^N - u_j^{N-1})/\Delta\tau$ | $O(\Delta\tau)$ | 0 (stored) |
| Central difference | $-(u_j^N - u_j^{N-2})/(2\Delta\tau)$ | $O((\Delta\tau)^2)$ | 0 (stored) |
| PDE-based | $rV - rS\Delta - \frac{1}{2}\sigma^2 S^2\Gamma$ | $O((\Delta S)^2)$ | Needs $\Delta$, $\Gamma$ |

$$
\boxed{
\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
}
$$

The PDE-based approach is generally superior because it avoids time-differencing error and uses the more accurate spatial Greeks. Direct time-step theta serves as a useful consistency check. Near expiry, where theta diverges for at-the-money options, fine time resolution or the PDE-based formula is essential for reliable estimates.

---

## Exercises

**Exercise 1.** Given two consecutive time levels from a Crank-Nicolson solver: $u_j^{N} = 3.934$ and $u_j^{N-1} = 3.962$ with $\Delta\tau = 0.0025$, compute the backward difference estimate of theta. Express the result in annualized terms (multiply by the number of trading periods per year if needed, or simply report per year).

---

**Exercise 2.** Using the PDE-based formula $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2\Gamma$ with $V = 3.934$, $\Delta = 0.5594$, $\Gamma = 0.0393$, $S = 100$, $r = 0.05$, $\sigma = 0.2$, compute theta. Compare this to the exact Black-Scholes value $\Theta = -11.35$ (annualized).

---

**Exercise 3.** The central difference estimate of theta uses three time levels: $\Theta_j \approx -(u_j^N - u_j^{N-2})/(2\Delta\tau)$. Explain why this is second-order accurate in $\Delta\tau$, while the backward difference is only first-order. What is the practical cost of the central difference (in terms of storage)?

---

**Exercise 4.** For an at-the-money European call near expiry, theta diverges as $\Theta_{\text{ATM}} \approx -\sigma S/(2\sqrt{2\pi\tau})$. With $\sigma = 0.3$, $S = 100$, compute $|\Theta|$ at $\tau = 1$ day ($1/252$), $\tau = 1$ week ($5/252$), and $\tau = 1$ month ($21/252$). How does this rapid growth affect the numerical estimation of theta near expiry?

---

**Exercise 5.** A deep in-the-money European put can have positive theta ($\Theta > 0$). Using the put theta formula $\Theta_{\text{put}} = -\frac{\sigma S\phi(d_1)}{2\sqrt{T}} + rKe^{-rT}\Phi(-d_2)$, explain the economic intuition: why does a deep ITM put gain value as time passes?

---

**Exercise 6.** The Greek theta ($\Theta = \partial V/\partial t$) and the scheme parameter theta ($\theta$ in the theta-scheme) are unrelated. A colleague asks: "If I use the theta-scheme with $\theta = 0.5$ (Crank-Nicolson), does that give me the Greek theta?" Explain the difference clearly.
