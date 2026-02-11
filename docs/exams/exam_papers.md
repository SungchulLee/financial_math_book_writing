# Exam Papers

#### 2025 Spring Midterm

---

**1.** Let $W_t$ be standard Brownian motion.
- (a) What is the distribution of $W_{t+s} - W_s$?
- (b) Are $W_{t+s} - W_s$ and $W_{2t+s} - W_s$ independent?

---

**2.** Let $W_t$ be standard Brownian motion. Find the probability density function of $\tau_a$ for $a > 0$ where $\tau_a$ is given by
$$
\tau_a := \inf \{ t \geq 0 \mid W_t = a \}
$$

---

**3.** Let $M_t = \sup_{0 \le s \le t} W_s$. Compute the joint distribution of $(W_t, M_t)$ and derive: For $a > 0, b < a$
$$
\mathbb{P}(M_t \ge a, W_t \le b)
$$

---

**4.** Evaluate the expectation and variance of $X_t$ where $X_t$ is given by
$$
X_t := \int_0^t W_s \, dW_s
$$

---

**5.** Let $W_t$ be standard Brownian motion. Use Itô's lemma to compute $dM_t$ where $M_t$ is given by
$$
M_t = \exp\left( \theta W_t - \frac{1}{2} \theta^2 t \right)
$$

---

**6.** Let $X_t$ satisfy the CIR (Cox–Ingersoll–Ross) process:
$$
dX_t = a(b - X_t)dt + \sigma \sqrt{X_t} dW_t.
$$
Define $Y_t = \sqrt{X_t}$. Derive the SDE satisfied by $Y_t$.

---

**7.**
When, $S_0$, $\mu$, $\sigma$, and $t$ are given, identify the distribution of $S_t$:
$$
S_t = S_0 \exp\left[\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right]
$$

---

**8.** Let:
$$
dX_t = -X_t \, dt + dW_t,\quad X_0\ \text{given}
$$  
What is the distribution of $X_t$ as $t\rightarrow\infty$.

---

**9.** Given:
$$
\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2}, \quad 0 < x < \pi, \ t > 0, \quad u(0,t) = u(\pi,t) = 0
$$
with initial condition:
$$
u(x,0) = \sin(3x) + 2\sin(5x).
$$
Find the solution $u(x,t)$ explicitly.

---


**10.** Discuss on the Von Neumann stability analysis on Forward, Backward, and CN for the heat equation
$$
\frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2}
$$

---

#### 2025 Spring Final

---

**1.** Let $W_t$ be standard Brownian motion.
- (a) What is the distribution of $W_{t+s} - W_s$?
- (b) Are $W_{t+s} - W_s$ and $W_{2t+s} - W_s$ independent?

---

**2.** Evaluate the expectation and variance of $X_t$ where $X_t$ is given by
$$
X_t := \int_0^t W_s \, dW_s
$$

---

**3.** Let $W_t$ be standard Brownian motion. Use Itô's lemma to compute $dM_t$ where $M_t$ is given by
$$
M_t = \exp\left( \theta W_t - \frac{1}{2} \theta^2 t \right)
$$

---

**4.**
When, $S_0$, $\mu$, $\sigma$, and $t$ are given, identify the distribution of $S_t$:
$$
S_t = S_0 \exp\left[\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right]
$$

---

**5.** Given:
$$
\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2}, \quad 0 < x < \pi, \ t > 0, \quad u(0,t) = u(\pi,t) = 0
$$
with initial condition:
$$
u(x,0) = \sin(3x) + 2\sin(5x).
$$
Find the solution $u(x,t)$ explicitly.

---

**6.** Price a one-period European call option with:

* $S = 100$, $K = 100$, $t = 1$, $u = 1.2$, $d = 0.9$, $r = 5\%$.

---

**7** You short one call option described above with the premium computed above and cover it by buying one stock. Describe your P&L at the end of the node.

---

**8.**
Derive the Black-Scholes PDE.

---

**9.**
Derive the Black-Scholes formula in the form of the expectation using Feynman-Kac formula.

---

**10.** A European call option on a non-dividend-paying stock has 3 months to expiration. The current stock price is $\$45$, the exercise price is $\$50$, the risk-free rate is 4% per annum, and the volatility is 30% per annum. Calculate the option price using the Black-Scholes formula. Use the cdf $N$ of the standard normal distribition to represent the option price.

---

**11.** A European put option has the same parameters as the call option in Problem 10. Use put-call parity to find the put option price. Use the cdf $N$ of the standard normal distribition to represent the option price.

---

**12.** A stock currently trades at $\$80$ with volatility of 25%. A 6-month European call option with strike $\$85$ trades for $\$4.50$. If the risk-free rate is 3%, what equation is the implied volatility of this option satisfying? Describe the logic of finding the implied volatility.

---

**13.** Model a chooser option that allows the holder to decide after 3 months whether the option is a call or put. Both options expire in 6 months with strike $\$100$. Current stock price is $\$95$, volatility is 30%, and risk-free rate is 5%. Describe your logic how to price this option.

---

**14.** A dividend of $\$2$ will be paid in 2 months on a stock currently trading at $\$85$. The risk-free rate is 4% per annum. Price a 4-month European call option with strike $\$90$ using the Black-Scholes model with continuous dividend yield approximation. Use the cdf $N$ of the standard normal distribition to represent the option price.

---

**15.** Below is the time decay of ATM call and put. The calendar spread (also known as a time spread or horizontal Spread) strategy is as follows:

- Sell: Short-term option (front month)

- Buy: Long-term option (same strike, longer expiration)

Why does this strategy make sense? Discuss the weak points of this strategy.


<img src="https://github.com/SungchulLee/img/blob/main/European%20Option%20Time%20Decay.png?raw=true">

---

Have a nice summer!!!














