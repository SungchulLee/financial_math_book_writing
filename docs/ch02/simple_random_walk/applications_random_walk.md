# Applications


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The simple random walk is a prototype for a wide class of models across probability, finance, physics, and biology. We describe five applications and explain precisely which property of the random walk each one exploits.

---

## 1. Gambler's Ruin

**Setting.** A gambler starts with $\$a$ and makes repeated fair bets of $\$1$. What is the probability of reaching $\$b > a$ before going broke?

**Model.** Let $S_n$ be the gambler's fortune after $n$ bets, starting from $S_0 = a$. Define stopping times:

$$\tau_0 = \inf\{n \geq 0 : S_n = 0\}, \qquad \tau_b = \inf\{n \geq 0 : S_n = b\}$$

**Result.** $\mathbb{P}(\tau_b < \tau_0) = a/b$.

**Key tool:** The martingale property of $\{S_n\}$ (Proposition 1.1.3) and the Optional Stopping Theorem. See [Exercise 3](exercises_random_walk.md) for the full derivation.

**Consequence.** As $b \to \infty$, $\mathbb{P}(\tau_b < \tau_0) = a/b \to 0$, so the gambler is ruined with certainty in an unbounded game. This is consistent with recurrence (Theorem 1.1.6): the walk returns to every state infinitely often, including 0.

---

## 2. Financial Market Modeling

**Bachelier's model (1900).** Louis Bachelier modeled stock price changes as symmetric random walk steps:

$$S_n = S_0 + \sum_{i=1}^n \xi_i$$

The scaling limit gives **arithmetic Brownian motion** $S(t) = S_0 + \sigma W_t$, which can become negative — a defect for prices.

**Geometric Brownian motion.** The modern remedy (Samuelson, 1965) models log-returns:

$$\frac{dS(t)}{S(t)} = \mu\,dt + \sigma\,dW_t \implies S(t) = S_0\exp\!\left(\mu t + \sigma W_t - \tfrac{\sigma^2 t}{2}\right)$$

The correction $-\sigma^2 t/2$ is the **Itô correction**, arising from the nonzero quadratic variation $[W]_t = t$ established in [Martingale Property](martingale_property.md).

**Cox–Ross–Rubinstein model (1979).** The discrete counterpart uses multiplicative steps:

$$S_n = S_0 \prod_{i=1}^n R_i, \qquad R_i = \begin{cases} u = e^{\sigma/\sqrt{n}} & \text{with prob.\ }p \\ d = e^{-\sigma/\sqrt{n}} & \text{with prob.\ }1-p \end{cases}$$

By Donsker's theorem applied to the log-returns $\log R_i$, $S_n \to S(t)$ (geometric Brownian motion) as $n \to \infty$. The no-arbitrage binomial pricing formula converges to the Black–Scholes formula in this limit. We develop this in detail in Chapter 8.

**Random walk hypothesis (Fama, 1965).** The Efficient Market Hypothesis rests on the assertion that price increments are approximately i.i.d., making asset prices well-modeled by scaled random walks.

---

## 3. Diffusion Processes

**Einstein (1905)** derived the diffusion equation by modeling a particle suspended in a fluid as a random walk. If the particle takes $n$ steps of size $\delta$ in time $t$, with $n = t/\tau$ and $\delta^2/(2\tau) = D$ (diffusion coefficient), then by the CLT the particle's displacement is approximately $\mathcal{N}(0, 2Dt)$.

The probability density $p(x,t)$ satisfies the **heat equation**:

$$\frac{\partial p}{\partial t} = D\,\frac{\partial^2 p}{\partial x^2}$$

The scaling limit in [Scaling Limit](scaling_limit.md) makes this connection precise: Brownian motion $W_t$ is the canonical solution to the heat equation with $D = 1/2$.

---

## 4. Population Genetics

**Wright–Fisher model.** In a population of $N$ diploid individuals, the frequency $X_n$ of an allele after $n$ generations evolves as:

$$X_{n+1} \approx X_n + \text{(random fluctuation of order } 1/\sqrt{N}\text{)}$$

For large $N$, the rescaled process $X^{(N)}(t) = X_{\lfloor Nt \rfloor}$ converges (by Donsker-type arguments) to a diffusion:

$$dX_t = \sqrt{X_t(1-X_t)}\,dW_t$$

**Recurrence/transience and diversity.** The recurrence of the 1D walk (Theorem 1.1.6) underlies the **fixation** phenomenon: with probability 1, one allele eventually takes over the entire population (the frequency process hits 0 or 1). This is the genetic drift analogue of the gambler being ruined with certainty.

---

## 5. Markov Chains and Reinforcement Learning

The random walk is the prototypical **Markov chain** on $\mathbb{Z}$: the transition probability from state $i$ is $p$ to $i+1$ and $1-p$ to $i-1$, depending only on the current position. The Markov property (Proposition 1.1.9) is the key structural ingredient.

In **reinforcement learning**, value functions for Markov decision processes are estimated by temporal-difference methods that exploit the Markov property. The random walk serves as the canonical test case for policy evaluation algorithms (e.g., TD(0), Monte Carlo). The hitting-time formula $\mathbb{E}[\tau] = a(b-a)$ from [Exercise 3](exercises_random_walk.md) is a closed-form benchmark for verifying these algorithms.

---

## References

- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École normale supérieure.
- Cox, J. C., Ross, S. A., & Rubinstein, M. (1979). Option pricing: A simplified approach. *Journal of Financial Economics*, 7(3), 229–263.
- Einstein, A. (1905). Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung. *Annalen der Physik*.
- Fama, E. F. (1965). Random walks in stock market prices. *Financial Analysts Journal*, 21(5), 55–59.
- Ewens, W. J. (2004). *Mathematical Population Genetics*, 2nd ed. Springer.
- Samuelson, P. A. (1965). Proof that properly anticipated prices fluctuate randomly. *Industrial Management Review*, 6(2), 41–49.
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, 2nd ed. MIT Press.
