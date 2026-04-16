# Applications

The simple random walk is a prototype for a wide class of models across probability, finance, physics, and biology. We describe five applications and explain precisely which property of the random walk each one exploits.

---

## 1. Gambler's Ruin

**Setting.** A gambler starts with $\$a$ and makes repeated fair bets of $\$1$. What is the probability of reaching $\$b > a$ before going broke?

**Model.** Let $S_n$ be the gambler's fortune after $n$ bets, starting from $S_0 = a$. Define stopping times:

$$\tau_0 = \inf\{n \geq 0 : S_n = 0\}, \qquad \tau_b = \inf\{n \geq 0 : S_n = b\}$$

**Result.** $\mathbb{P}(\tau_b < \tau_0) = a/b$.

**Key tool:** The martingale property of $\{S_n\}$ (Proposition 1.1.3) and the Optional Stopping Theorem. See [Exercise 8](martingale_property.md#exercises) for the full derivation.

**Consequence.** As $b \to \infty$, $\mathbb{P}(\tau_b < \tau_0) = a/b \to 0$, so the gambler is ruined with certainty in an unbounded game. This is consistent with recurrence (Theorem 1.1.7): the unrestricted walk returns to every state infinitely often. There is no contradiction — the walk is recurrent on all of $\mathbb{Z}$, but in the gambler's ruin setup the walk is *absorbed* at 0, preventing any return once ruin occurs.

---

## 2. Financial Market Modeling

**Bachelier's model (1900).** Louis Bachelier modeled stock price changes as symmetric random walk steps:

$$S_n = S_0 + \sum_{i=1}^n \xi_i$$

The scaling limit gives **arithmetic Brownian motion** $S(t) = S_0 + \sigma W_t$, which can become negative — a defect for prices.

**Geometric Brownian motion.** The modern remedy (Samuelson, 1965) models log-returns:

$$\frac{dS(t)}{S(t)} = \mu\,dt + \sigma\,dW_t \implies S(t) = S_0\exp\!\left(\mu t + \sigma W_t - \tfrac{\sigma^2 t}{2}\right)$$

The correction $-\sigma^2 t/2$ is the **Itô correction**, arising from the nonzero quadratic variation $\langle W\rangle_t = t$ established in [Martingale Property](martingale_property.md).

**Cox–Ross–Rubinstein model (1979).** The discrete counterpart uses multiplicative steps:

$$S_n = S_0 \prod_{i=1}^n R_i, \qquad R_i = \begin{cases} u = e^{\sigma/\sqrt{n}} & \text{with prob.\ }p^* \\ d = e^{-\sigma/\sqrt{n}} & \text{with prob.\ }1-p^* \end{cases}$$

where $p^* = (e^{r/\sqrt{n}} - d)/(u - d)$ is the **risk-neutral probability** and $r$ is the risk-free rate. Using $e^x = 1 + x + O(x^2)$: the numerator is $e^{r/\sqrt{n}} - e^{-\sigma/\sqrt{n}} \approx (r+\sigma)/\sqrt{n}$ and the denominator is $e^{\sigma/\sqrt{n}} - e^{-\sigma/\sqrt{n}} \approx 2\sigma/\sqrt{n}$, giving $p^* \approx (r+\sigma)/(2\sigma)$. This is not $1/2$ in general, but the centred log-return $Y_i = \log R_i - \mathbb{E}^*[\log R_i]$ has mean 0 and variance $\sigma^2/n + O(n^{-3/2})$ under $p^*$. Donsker's theorem (Thm 1.1.11) applied to the scaled sum of $Y_i$ gives $\sum_{i=1}^{\lfloor nt \rfloor} Y_i / \sqrt{n} \Rightarrow \sigma W_t$, and hence $S_n \to S(t) = S_0 \exp\!\bigl(r t + \sigma W_t - \tfrac{1}{2}\sigma^2 t\bigr)$ (geometric Brownian motion under the risk-neutral measure $p^*$, with risk-free drift $r$). The no-arbitrage binomial pricing formula converges to the Black–Scholes formula in this limit. We develop this in detail in Chapter 8.

**Random walk hypothesis (Fama, 1965).** The Efficient Market Hypothesis rests on the assertion that price increments are approximately i.i.d., making asset prices well-modeled by scaled random walks.

---

## 3. Diffusion Processes

**Einstein (1905)** derived the diffusion equation by modeling a particle suspended in a fluid as a random walk. If the particle takes $n$ steps of size $\delta$ in time $t$, with $n = t/\tau$ and $\delta^2/(2\tau) = D$ (diffusion coefficient), then by the CLT the particle's displacement is approximately $\mathcal{N}(0, 2Dt)$.

The transition density $p(x,t)$ of the particle's position satisfies the **heat equation**:

$$\frac{\partial p}{\partial t} = D\,\frac{\partial^2 p}{\partial x^2}$$

The scaling limit in [Scaling Limit](scaling_limit.md) makes this connection precise: the transition density of Brownian motion $W_t$ is $p(x,t) = (4\pi D t)^{-1/2} e^{-x^2/(4Dt)}$, which is the fundamental solution of the heat equation with diffusion coefficient $D$. (For standard Brownian motion, $D = 1/2$.)

---

## 4. Population Genetics

**Wright–Fisher model.** In a population of $N$ diploid individuals, the frequency $X_n$ of an allele after $n$ generations evolves as:

$$X_{n+1} \approx X_n + \text{(random fluctuation of order } 1/\sqrt{N}\text{)}$$

For large $N$, the rescaled process $X^{(N)}(t) = X_{\lfloor Nt \rfloor}$ converges (by Donsker-type arguments) to a diffusion:

$$dX_t = \sqrt{X_t(1-X_t)}\,dW_t$$

**Fixation and absorption.** The Wright–Fisher diffusion has absorbing boundaries at 0 and 1: once the frequency reaches either endpoint, it stays there. By a martingale argument (the frequency process is itself a martingale), the process hits one of the two boundaries with probability 1, and the probability of fixation at 1 starting from $X_0 = x$ is exactly $x$. This is the continuous-time analogue of the gambler's ruin result $\mathbb{P}(\tau_b < \tau_0) = a/b$. The analogy with recurrence of the 1D walk is instructive — both results reflect the absence of a restoring force — but fixation follows from the martingale property of $X_t$, not directly from recurrence.

---

## 5. Markov Chains and Reinforcement Learning

The random walk is the prototypical **Markov chain** on $\mathbb{Z}$: the transition probability from state $i$ is $p$ to $i+1$ and $1-p$ to $i-1$, depending only on the current position. The Markov property (Proposition 1.1.6) is the key structural ingredient.

In **reinforcement learning**, value functions for Markov decision processes are estimated by temporal-difference methods that exploit the Markov property. The random walk serves as the canonical test case for policy evaluation algorithms (e.g., TD(0), Monte Carlo). The quantity $\mathbb{E}[\tau_0 \wedge \tau_b] = a(b-a)$ from [Exercise 8(c)](martingale_property.md#exercises) gives the expected absorption time starting from $a$ with absorbing barriers at 0 and $b$; this closed-form result serves as a benchmark for verifying RL algorithms.

---

## References

- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École normale supérieure.
- Cox, J. C., Ross, S. A., & Rubinstein, M. (1979). Option pricing: A simplified approach. *Journal of Financial Economics*, 7(3), 229–263.
- Einstein, A. (1905). Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung. *Annalen der Physik*.
- Fama, E. F. (1965). Random walks in stock market prices. *Financial Analysts Journal*, 21(5), 55–59.
- Ewens, W. J. (2004). *Mathematical Population Genetics*, 2nd ed. Springer.
- Samuelson, P. A. (1965). Proof that properly anticipated prices fluctuate randomly. *Industrial Management Review*, 6(2), 41–49.
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, 2nd ed. MIT Press.

---

## Exercises

**Exercise 1.** In the Gambler's Ruin problem with initial wealth $a = 20$ and target $b = 100$, compute the probability of reaching $b$ before going broke (assuming a fair game). Then compute the expected duration $\mathbb{E}[\tau]$ of the game using $\mathbb{E}[\tau] = a(b-a)$.

??? success "Solution to Exercise 1"
    With $a = 20$ and $b = 100$ in a fair game ($p = 1/2$), the probability of reaching $b$ before going broke is:

    $$
    \mathbb{P}(\tau_b < \tau_0) = \frac{a}{b} = \frac{20}{100} = \frac{1}{5} = 0.2
    $$

    The expected duration of the game is:

    $$
    \mathbb{E}[\tau] = a(b - a) = 20 \cdot (100 - 20) = 20 \cdot 80 = 1600 \text{ rounds}
    $$

---

**Exercise 2.** In the Cox-Ross-Rubinstein model with $S_0 = 100$, $\sigma = 0.3$, $r = 0.05$, and $n = 252$ steps (daily), compute the up and down factors $u = e^{\sigma/\sqrt{n}}$ and $d = e^{-\sigma/\sqrt{n}}$, and the risk-neutral probability $p^*$. Verify that $p^* \neq 1/2$ and compute how far it deviates from $1/2$.

??? success "Solution to Exercise 2"
    With $S_0 = 100$, $\sigma = 0.3$, $r = 0.05$, and $n = 252$:

    $$
    u = e^{\sigma/\sqrt{n}} = e^{0.3/\sqrt{252}} = e^{0.3/15.875} = e^{0.01890} \approx 1.01908
    $$

    $$
    d = e^{-\sigma/\sqrt{n}} = e^{-0.01890} \approx 0.98127
    $$

    The risk-neutral probability is:

    $$
    p^* = \frac{e^{r/n} - d}{u - d} = \frac{e^{0.05/252} - 0.98127}{1.01908 - 0.98127}
    $$

    Computing: $e^{0.05/252} = e^{0.000198} \approx 1.000198$. Therefore:

    $$
    p^* = \frac{1.000198 - 0.98127}{0.03781} = \frac{0.01893}{0.03781} \approx 0.5005
    $$

    The deviation from $1/2$ is $p^* - 0.5 \approx 0.0005$, which is very small. This small deviation reflects the risk-free drift $r = 0.05$ being spread over 252 daily steps.

---

**Exercise 3.** In Bachelier's arithmetic Brownian motion model $S(t) = S_0 + \sigma W_t$, compute the probability that the stock price becomes negative before time $T = 1$ when $S_0 = 10$ and $\sigma = 3$. This illustrates the defect that motivated the switch to geometric Brownian motion.

??? success "Solution to Exercise 3"
    In Bachelier's model, $S(t) = S_0 + \sigma W_t$ with $S_0 = 10$ and $\sigma = 3$. The stock becomes negative when $S(t) < 0$, i.e., $W_t < -S_0/\sigma = -10/3$. The probability that $\min_{0 \leq t \leq 1} S(t) < 0$ equals the probability that $\min_{0 \leq t \leq 1} W_t < -10/3$.

    By the reflection principle, $\mathbb{P}(\min_{0 \leq t \leq 1} W_t < -c) = 2\mathbb{P}(W_1 < -c) = 2\Phi(-c)$ for $c > 0$. With $c = 10/3 \approx 3.333$:

    $$
    \mathbb{P}(\text{negative price before } T=1) = 2\Phi(-10/3) = 2\Phi(-3.333) \approx 2 \times 0.000429 = 0.000858
    $$

    Although this is small (about 0.086%), the probability is strictly positive, illustrating the fundamental defect of arithmetic Brownian motion: for any $S_0$ and $\sigma > 0$, there is always a positive probability of negative prices.

---

**Exercise 4.** The Einstein diffusion relation states that the diffusion coefficient is $D = \delta^2/(2\tau)$ where $\delta$ is the step size and $\tau$ is the time per step. If a pollen particle in water has $D = 10^{-9}$ cm$^2$/s and makes $10^{12}$ collisions per second, what is the effective step size $\delta$ of each collision?

??? success "Solution to Exercise 4"
    Given $D = 10^{-9}$ cm$^2$/s and the collision rate is $10^{12}$/s, so $\tau = 10^{-12}$ s. From $D = \delta^2/(2\tau)$:

    $$
    \delta^2 = 2D\tau = 2 \times 10^{-9} \times 10^{-12} = 2 \times 10^{-21} \text{ cm}^2
    $$

    $$
    \delta = \sqrt{2 \times 10^{-21}} = \sqrt{2} \times 10^{-10.5} \approx 1.41 \times 10^{-10.5} \approx 4.47 \times 10^{-11} \text{ cm}
    $$

    This is $\delta \approx 4.47 \times 10^{-13}$ m $= 0.447$ pm (picometers), which is on the order of atomic bond lengths, consistent with the physical picture of molecular collisions.

---

**Exercise 5.** In the Wright-Fisher model, the fixation probability starting from allele frequency $x$ is $\mathbb{P}(\text{fixation at 1}) = x$. This is the continuous-time analogue of the gambler's ruin result $\mathbb{P}(\tau_b < \tau_0) = a/b$ with $x = a/b$. If a new mutation appears in a population of $N = 1000$ diploid individuals (so $x = 1/(2N) = 0.0005$), what is the fixation probability? How many such mutations must arise for the expected number of fixations to equal 1?

??? success "Solution to Exercise 5"
    In a diploid population of $N = 1000$, a new mutation starts at frequency $x = 1/(2N) = 1/2000 = 0.0005$. The fixation probability is:

    $$
    \mathbb{P}(\text{fixation}) = x = 0.0005
    $$

    For the expected number of fixations to equal 1, we need $m$ mutations where $m \times 0.0005 = 1$:

    $$
    m = \frac{1}{0.0005} = 2000
    $$

    So 2000 independent new mutations must arise for one fixation event to be expected on average.

---

**Exercise 6.** The random walk serves as a test problem for temporal-difference learning. Consider a 7-state random walk with states $\{0, 1, 2, 3, 4, 5, 6\}$ where states 0 and 6 are absorbing (giving rewards 0 and 1 respectively), and the walk starts at state 3. Using the martingale property, compute the true value function $V(i) = \mathbb{P}(\text{reach state 6 before state 0} \mid S_0 = i)$ for each state $i = 0, 1, \ldots, 6$.

??? success "Solution to Exercise 6"
    By the Gambler's Ruin result (martingale property), the probability of reaching state $b$ before state 0 starting from state $i$ is $V(i) = i/b$. Here, the absorbing states are 0 and 6, so $b = 6$:

    $$
    V(i) = \frac{i}{6}
    $$

    The value function for each state is:

    | State $i$ | $V(i) = i/6$ |
    |---|---|
    | 0 | 0 |
    | 1 | 1/6 |
    | 2 | 2/6 = 1/3 |
    | 3 | 3/6 = 1/2 |
    | 4 | 4/6 = 2/3 |
    | 5 | 5/6 |
    | 6 | 1 |

    The linearity of $V(i)$ reflects the martingale property: $V(i)$ satisfies $V(i) = \frac{1}{2}V(i-1) + \frac{1}{2}V(i+1)$ for interior states (the discrete harmonic condition), with boundary conditions $V(0) = 0$ and $V(6) = 1$, whose unique solution is $V(i) = i/6$.
