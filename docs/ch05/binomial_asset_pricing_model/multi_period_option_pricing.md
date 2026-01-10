# Binomial Tree Construction and Multi-Period Option Pricing


This section develops the binomial tree model for asset prices and applies it
to multi-period option pricing. The binomial tree provides a discrete-time,

intuitive framework for understanding no-arbitrage pricing, dynamic hedging,

and the convergence to continuous-time models such as Black–Scholes.


---


## 1. One-Period Binomial Model (Review)


Let the current stock price be \( S_0 \). Over one time step \( \Delta t \),
the stock price evolves according to

\[
S_{dt} =
\begin{cases}
u S_0, & \text{with up move} \\
d S_0, & \text{with down move}
\end{cases}
\]

where \( u > 1 \) and \( 0 < d < 1 \).

Let the risk-free interest rate be \( r \). The value of one unit of cash after

one period is

B_1 = e^{r dt} B_0 

No-arbitrage requires


d < e^{r dt} < u 


## 2. Building the Binomial Tree

### 2.1 Time Discretization

Fix a maturity \( T \) and divide it into \( N \) equal periods:

d t = \frac{T}{N}

At each time step, the stock price moves up by factor \( u \) or down by factor
\( d \).


### 2.2 Stock Price Dynamics

At time step \( n \), after \( k \) up moves and \( n-k \) down moves, the stock

price is

S_{n,k} = S_0 u^k d^{n-k}


The binomial tree is **recombining**, meaning that the order of up and down moves

does not matter.


### 2.3 Choice of Parameters

Typical choices of parameters include:


- **Cox–Ross–Rubinstein (CRR) model**


u = e^{\sigma \sqrt{d t}}, \quad
d = e^{-\sigma \sqrt{d t}}


where \( \sigma \) is the volatility.


- **Risk-free growth**


e^{r dt} 

These choices ensure recombination and convergence to continuous-time limits.



## 3. Risk-Neutral Probability


Define the **risk-neutral probability** \( q \) by


q = \frac{e^{r dt} - d}{u - d}


Under the no-arbitrage condition \( d < e^{r dt} < u \), we have \( 0 < q < 1 \).


Under the risk-neutral measure:


- The expected growth rate of the stock equals the risk-free rate.


- Pricing reduces to discounted expectation of future payoffs.



## 4. Multi-Period Option Pricing


Let \( V_{n,k} \) denote the value of an option at node \( (n,k) \).


### 4.1 Terminal Payoff

At maturity \( T \) (time step \( N \)), the option value is given by its payoff.


- **European call option**


V_{N,k} = \max(S_{N,k} - K, 0)



- **European put option**


V_{N,k} = \max(K - S_{N,k}, 0)



### 4.2 Backward Induction

For \( n = N-1, \dots, 0 \), the option value is computed recursively as


V_{n,k}
=
\frac{1}{e^{r dt}}
\left(
q V_{n+1,k+1} + (1-q) V_{n+1,k}

\right)

This backward induction corresponds to forming a locally risk-free replicating

portfolio at each node.


### 4.3 Interpretation

The pricing formula shows that:


- Option pricing is independent of investors’ risk preferences.


- Only the risk-free rate and volatility matter.


- Dynamic hedging is implicit in the recursion.



## 5. American Options (Optional Extension)

For an **American option**, early exercise is allowed. The pricing rule becomes


\max\left(
\text{intrinsic value},
\;
\left[
\right]

Early exercise may be optimal for American puts but not for non-dividend-paying

American calls.


## 6. Convergence and Link to Black–Scholes

As the number of periods \( N \to \infty \) and \( \Delta t \to 0 \):


- The binomial tree converges to a geometric Brownian motion.


- The binomial option price converges to the Black–Scholes price.


- The discrete-time hedge converges to continuous delta hedging.


Thus, the binomial model provides a transparent and rigorous bridge from
discrete-time no-arbitrage pricing to continuous-time option pricing theory.


