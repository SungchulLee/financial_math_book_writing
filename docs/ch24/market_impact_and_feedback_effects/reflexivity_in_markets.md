# Reflexivity in Markets


**Reflexivity**, a concept popularized by George Soros, describes the circular relationship between market participants’ beliefs and market outcomes.

---

## Concept of reflexivity


Reflexivity posits that:
- beliefs influence actions,
- actions influence prices,
- prices reinforce beliefs.

Markets are thus self-referential systems.

---

## Reflexivity vs equilibrium


In reflexive markets:
- equilibrium may not exist or be stable,
- expectations can be self-fulfilling,
- feedback dominates fundamentals.

This contrasts with rational expectations models.

---

## Formal modeling approaches


Reflexivity can be modeled via:
- feedback control systems,
- agent-based models,
- learning and belief-updating frameworks.

These models emphasize dynamics over equilibrium.

---

## Implications for finance


Reflexivity explains:
- bubbles and crashes,
- persistent mispricings,
- sudden market reversals.

It highlights limits of purely rational models.

---

## Key takeaways


- Markets are reflexive systems.
- Beliefs and prices co-evolve.
- Feedback challenges equilibrium-based modeling.

---

## Further reading


- Soros, *The Alchemy of Finance*.
- Shiller, narrative economics.

---

## Exercises

**Exercise 1.** Formalize Soros's reflexivity concept. Let $p_t$ be the market price, $v_t$ the fundamental value, and $b_t$ the market participants' aggregate belief about value. The reflexive system is: (a) beliefs influence prices: $p_t = b_t + \epsilon_t$, (b) prices influence beliefs: $b_{t+1} = (1-\alpha)b_t + \alpha p_t$. Substitute (a) into (b) to obtain $b_{t+1} = b_t + \alpha \epsilon_t$. Show that beliefs follow a random walk even if fundamentals are constant. (c) Now add a mean-reverting fundamental anchor: $b_{t+1} = (1-\alpha)b_t + \alpha p_t + \beta(v - b_t)$. Under what conditions on $\alpha$ and $\beta$ do beliefs converge to the fundamental value?

??? success "Solution to Exercise 1"
    **(a)** We have two equations:

    - Beliefs influence prices: $p_t = b_t + \epsilon_t$
    - Prices influence beliefs: $b_{t+1} = (1-\alpha)b_t + \alpha p_t$

    Substituting the first equation into the second:

    $$
    b_{t+1} = (1-\alpha)b_t + \alpha(b_t + \epsilon_t) = (1-\alpha)b_t + \alpha b_t + \alpha \epsilon_t = b_t + \alpha \epsilon_t
    $$

    Therefore:

    $$
    b_{t+1} - b_t = \alpha \epsilon_t
    $$

    This shows that beliefs follow a **random walk** (with increment $\alpha \epsilon_t$), even if the fundamental value is constant. The reflexive feedback between beliefs and prices transforms transient noise $\epsilon_t$ into permanent belief shifts. Each random price fluctuation is partially incorporated into beliefs, which in turn influence future prices---a ratchet effect where noise accumulates rather than washing out.

    **(b)** The beliefs follow $b_{t+1} = b_t + \alpha \epsilon_t$, which means:

    $$
    b_t = b_0 + \alpha \sum_{s=0}^{t-1} \epsilon_s
    $$

    Since $\epsilon_t$ are (presumably) i.i.d. with mean zero and variance $\sigma_\epsilon^2$, we have $\text{Var}(b_t) = \alpha^2 t \sigma_\epsilon^2$, which grows without bound. Beliefs drift arbitrarily far from any fixed fundamental value, even though no persistent information arrives.

    **(c)** With the fundamental anchor, the belief update becomes:

    $$
    b_{t+1} = (1-\alpha)b_t + \alpha p_t + \beta(v - b_t) = (1-\alpha)b_t + \alpha(b_t + \epsilon_t) + \beta(v - b_t)
    $$

    $$
    = b_t + \alpha \epsilon_t + \beta(v - b_t) = (1-\beta)b_t + \beta v + \alpha \epsilon_t
    $$

    This is an AR(1) process for $b_t$ with mean-reversion toward $v$:

    $$
    b_{t+1} - v = (1-\beta)(b_t - v) + \alpha \epsilon_t
    $$

    Beliefs converge to the fundamental value (in the sense that $b_t$ is stationary around $v$) if and only if:

    $$
    |1-\beta| < 1 \quad \Longleftrightarrow \quad 0 < \beta < 2
    $$

    For any $\beta \in (0, 2)$ and any $\alpha > 0$, the process is stationary with:

    $$
    \mathbb{E}[b_t] \to v, \quad \text{Var}(b_t) \to \frac{\alpha^2 \sigma_\epsilon^2}{1 - (1-\beta)^2} = \frac{\alpha^2 \sigma_\epsilon^2}{\beta(2-\beta)}
    $$

    The speed of convergence increases with $\beta$ (stronger fundamental anchor) and the variance around $v$ increases with $\alpha$ (stronger reflexive feedback). The fundamental anchor $\beta$ must be strong enough relative to the reflexive parameter $\alpha$ to keep beliefs stable---specifically, the variance $\alpha^2 \sigma_\epsilon^2 / [\beta(2-\beta)]$ must be finite, which holds for any $\beta > 0$.

---

**Exercise 2.** Self-fulfilling prophecies are a manifestation of reflexivity. In a currency crisis model, if enough investors believe the currency will devalue and sell, capital outflows force the central bank to devalue. (a) Set up a coordination game: $N$ investors each choose to attack (sell) or hold. The currency devalues if and only if at least $M$ investors attack. Each attacker pays a cost $c$ and earns a payoff $R$ if the devaluation occurs. (b) Find the conditions under which "all attack" and "no one attacks" are both Nash equilibria. (c) Explain how this multiple-equilibrium structure embodies reflexivity: the outcome depends on beliefs about others' actions, not just fundamentals.

??? success "Solution to Exercise 2"
    **(a)** The coordination game is defined as follows:

    - There are $N$ investors, each choosing to **attack** (sell the currency) or **hold**.
    - Attacking costs $c$ (e.g., the cost of short-selling the currency).
    - The currency devalues if and only if at least $M$ investors attack.
    - If the currency devalues, each attacker earns payoff $R$.

    The payoff matrix for investor $i$ is:

    | | Devaluation ($\geq M$ attackers) | No devaluation ($< M$ attackers) |
    |---|---|---|
    | Attack | $R - c$ | $-c$ |
    | Hold | $0$ | $0$ |

    **(b)** We look for conditions under which both "all attack" and "no one attacks" are Nash equilibria.

    **"All attack" equilibrium**: All $N$ investors attack, so there are $N \geq M$ attackers (assuming $N \geq M$). Devaluation occurs. Each attacker earns $R - c$. For this to be a Nash equilibrium, no individual wants to deviate to "hold." If investor $i$ deviates to hold, there are $N-1$ attackers. If $N-1 \geq M$, devaluation still occurs and the deviator earns $0$ instead of $R-c$. For the deviator to prefer not deviating, we need $R - c > 0$, i.e.:

    $$
    R > c
    $$

    Also, we need $N - 1 \geq M$ so that one defection does not prevent devaluation (otherwise the deviator would prevent the devaluation and save $c$, making deviation profitable since $0 > R - c$ is impossible when $R > c$). Actually, if $N - 1 < M$, i.e., $N = M$, then each attacker is pivotal. The deviator's payoff from holding is $0$ (devaluation does not occur), and from attacking is $R - c$. So the condition is still $R > c$.

    **"No one attacks" equilibrium**: No investor attacks. No devaluation occurs. Each investor earns $0$. If investor $i$ deviates to attack alone, there is $1 < M$ attacker, so no devaluation. The deviator earns $-c < 0$. Since $-c < 0$, the deviator is worse off. This is always a Nash equilibrium (for $M > 1$).

    Therefore, both equilibria coexist when:

    $$
    R > c \quad \text{and} \quad M > 1
    $$

    **(c)** The multiple-equilibrium structure embodies reflexivity because:

    - In the "all attack" equilibrium, investors believe others will attack, so they attack, causing the devaluation. The belief is **self-fulfilling**: the devaluation occurs because investors expect it to occur.
    - In the "no one attacks" equilibrium, investors believe others will hold, so they hold, and no devaluation occurs. This belief is also self-fulfilling.
    - The fundamental value of the currency (which determines $R$, $c$, and $M$) does not uniquely determine the outcome. Instead, **beliefs about others' actions** determine which equilibrium is selected. This is the essence of reflexivity: the outcome depends on collective beliefs, not just fundamentals.
    - This explains why currency crises can appear to come "out of nowhere": a shift in beliefs (e.g., triggered by a rumor or a minor policy change) can flip the system from the stable equilibrium to the crisis equilibrium, even when fundamentals have not changed.

---

**Exercise 3.** Asset bubbles exhibit reflexive dynamics: rising prices attract buyers, whose demand further raises prices. Model a bubble using the feedback equation $p_{t+1} = p_t + \gamma(p_t - p_{t-1}) + \epsilon_{t+1}$ where $\gamma > 0$ is the momentum feedback parameter. (a) Show that the characteristic equation is $z^2 - (1+\gamma)z + \gamma = 0$ and find the roots. (b) For $\gamma < 1$, show that the price process is stationary (bubble eventually deflates). For $\gamma \ge 1$, show that the process is explosive. (c) In the explosive case, the bubble eventually crashes. Introduce a crash probability $\pi_t$ that increases with the bubble size $p_t - v_t$ and describe the resulting dynamics qualitatively.

??? success "Solution to Exercise 3"
    **(a)** The bubble model is:

    $$
    p_{t+1} = p_t + \gamma(p_t - p_{t-1}) + \epsilon_{t+1}
    $$

    For stability analysis, consider the homogeneous equation (set $\epsilon = 0$):

    $$
    p_{t+1} - (1+\gamma)p_t + \gamma p_{t-1} = 0
    $$

    The characteristic equation is obtained by substituting $p_t = z^t$:

    $$
    z^2 - (1+\gamma)z + \gamma = 0
    $$

    Using the quadratic formula:

    $$
    z = \frac{(1+\gamma) \pm \sqrt{(1+\gamma)^2 - 4\gamma}}{2} = \frac{(1+\gamma) \pm \sqrt{1 + 2\gamma + \gamma^2 - 4\gamma}}{2} = \frac{(1+\gamma) \pm \sqrt{(1-\gamma)^2}}{2}
    $$

    $$
    = \frac{(1+\gamma) \pm (1-\gamma)}{2}
    $$

    So the roots are:

    $$
    z_1 = \frac{(1+\gamma) + (1-\gamma)}{2} = 1, \quad z_2 = \frac{(1+\gamma) - (1-\gamma)}{2} = \gamma
    $$

    **(b)** The general solution of the homogeneous equation is $p_t = C_1 \cdot 1^t + C_2 \cdot \gamma^t = C_1 + C_2 \gamma^t$.

    **For $\gamma < 1$**: Both roots satisfy $|z| \leq 1$, with $z_1 = 1$ (unit root) and $|z_2| = \gamma < 1$ (stable). The $\gamma^t$ component decays to zero over time. The price converges to a constant $C_1$ (plus the random-walk component from the $\epsilon$ terms). The bubble $p_t - v_t$ eventually deflates because the momentum feedback ($\gamma < 1$) is too weak to sustain exponential growth.

    **For $\gamma = 1$**: Both roots equal 1 (repeated root). The general solution is $p_t = C_1 + C_2 t$, which is a linear trend---the price drifts at a constant rate, representing a marginally explosive process.

    **For $\gamma > 1$**: The root $z_2 = \gamma > 1$ is explosive. The component $C_2 \gamma^t$ grows exponentially, so the price diverges from fundamentals at an exponential rate. This represents a bubble with exponential growth: the momentum feedback is self-reinforcing and causes the deviation from fundamental value to grow without bound.

    **(c)** In the explosive case ($\gamma \geq 1$), the bubble size $B_t = p_t - v_t$ grows over time. We introduce a crash probability that increases with bubble size:

    $$
    \pi_t = h(B_t), \quad h'(B_t) > 0, \quad h(0) = 0
    $$

    For example, $\pi_t = 1 - \exp(-\lambda B_t^2)$. The dynamics become:

    - With probability $1 - \pi_t$: the bubble continues, $p_{t+1} = p_t + \gamma(p_t - p_{t-1}) + \epsilon_{t+1}$.
    - With probability $\pi_t$: a crash occurs, $p_{t+1} = v_{t+1} + \eta_{t+1}$ (price reverts to near fundamental value).

    The resulting dynamics exhibit the characteristic **boom-bust pattern**:

    1. **Boom phase**: As long as no crash occurs, the feedback term $\gamma > 1$ drives exponential growth of $B_t$. During this phase, realized returns are high, attracting more momentum buyers.
    2. **Increasing fragility**: As $B_t$ grows, $\pi_t$ increases. The expected return conditional on no crash is high, but the crash probability grows.
    3. **Crash**: Eventually the crash occurs (it is almost certain in finite time since $\sum \pi_t = \infty$ for the expanding bubble). The price snaps back to fundamentals.
    4. **Restart**: After the crash, $B_t$ is near zero, $\pi_t$ is small, and the process can begin again.

    This model produces the asymmetric pattern observed empirically: slow buildup of bubbles followed by rapid crashes, with crash magnitude proportional to the preceding bubble size.

---

**Exercise 4.** Rational expectations theory assumes that beliefs are consistent with outcomes in equilibrium. Reflexivity challenges this by emphasizing that beliefs shape outcomes. (a) In a rational expectations equilibrium (REE), market price $p = \mathbb{E}[v \mid p]$ (the price is the conditional expectation of value given the price itself). Explain the circularity: $p$ appears on both sides. (b) Describe conditions under which the REE exists and is unique (e.g., normally distributed fundamentals and noise). (c) Discuss cases where multiple REE exist, and explain how reflexivity selects among equilibria: initial beliefs determine which equilibrium is reached.

??? success "Solution to Exercise 4"
    **(a)** In a rational expectations equilibrium (REE), the market price satisfies:

    $$
    p = \mathbb{E}[v \mid p]
    $$

    The circularity is fundamental: $p$ is defined as a function of the conditional expectation given $p$ itself. To compute $\mathbb{E}[v \mid p]$, one needs to know how $p$ relates to $v$ (the signal structure), but this relationship is precisely what the equilibrium determines. Specifically:

    - To form the expectation $\mathbb{E}[v \mid p]$, agents need to know the joint distribution of $(v, p)$.
    - The distribution of $p$ depends on how agents trade, which depends on their expectations.
    - Their expectations depend on the distribution of $p$.

    This is a fixed-point problem: the equilibrium price function $p(\cdot)$ must be a fixed point of the mapping that takes a conjectured price function, computes the resulting conditional expectation, and produces the equilibrium price.

    **(b)** A standard setting where the REE exists and is unique involves normally distributed fundamentals and noise:

    - Fundamental value: $v \sim N(\bar{v}, \sigma_v^2)$.
    - Informed trader observes $v$ and submits order $x = \beta(v - p)$ for some $\beta > 0$.
    - Noise traders submit $u \sim N(0, \sigma_u^2)$.
    - Total order flow: $y = x + u = \beta(v - p) + u$.
    - Market maker sets $p = \mathbb{E}[v \mid y]$.

    Under normality, the conditional expectation is linear: $\mathbb{E}[v \mid y] = \bar{v} + \frac{\text{Cov}(v, y)}{\text{Var}(y)} y$. Substituting and solving the fixed-point condition yields a unique linear equilibrium price:

    $$
    p = \bar{v} + \lambda y
    $$

    where $\lambda = \beta \sigma_v^2 / (\beta^2 \sigma_v^2 + \sigma_u^2)$. Uniqueness holds because the linear-normal structure produces a unique linear fixed point (the projection theorem in Gaussian spaces guarantees uniqueness of the conditional expectation).

    **(c)** Multiple REE can arise when:

    - Distributions are non-Gaussian (allowing for non-linear equilibria).
    - There are complementarities in information acquisition (as in Grossman-Stiglitz type models with endogenous information).
    - The state space admits multiple self-consistent price functions.

    When multiple REE exist, reflexivity selects among them: the equilibrium actually reached depends on initial beliefs. If agents initially believe that "high prices signal high value," they coordinate on a high-price REE. If they initially believe "prices are uninformative," they may coordinate on a no-trade or low-information REE.

    This is reflexive because the realized equilibrium is shaped by beliefs, not uniquely pinned down by fundamentals. Two markets with identical fundamentals can reach different equilibria depending on the prevailing narrative or convention. Historical path-dependence, herding, and anchoring effects all influence which equilibrium is selected, making the outcome a product of the market's self-referential dynamics rather than a unique function of external information.

---

**Exercise 5.** In credit markets, reflexivity operates through the debt-deflation channel. When asset prices fall, collateral values decline, triggering margin calls and forced selling, which further depresses prices. (a) Write a two-period model: in period 1, an adverse shock reduces asset prices by $\Delta$. Borrowers with leverage $L$ face margin calls of $L \cdot \Delta$. (b) To meet margin calls, they sell $L \cdot \Delta / p_1$ units of the asset, causing a further price decline of $\eta L \Delta / p_1$ (where $\eta$ is the price impact per unit sold). (c) Show that the total price decline exceeds the initial shock $\Delta$ when the feedback parameter $\eta L / p_1 > 0$ is sufficiently large. This amplification mechanism was central to the 2008 financial crisis.

??? success "Solution to Exercise 5"
    **(a)** The two-period debt-deflation model:

    - **Period 0**: Asset price is $p_0$. Borrowers have leverage $L$, meaning they hold assets worth $L \cdot E_0$ where $E_0$ is equity, with debt $D = (L-1) \cdot E_0$.
    - **Period 1**: An adverse shock reduces asset prices by $\Delta$. New price: $p_1 = p_0 - \Delta$.

    Borrowers' equity after the shock:

    $$
    E_1 = L \cdot E_0 \cdot \frac{p_1}{p_0} - D = L \cdot E_0 \cdot \frac{p_0 - \Delta}{p_0} - (L-1)E_0 = E_0 - L \cdot E_0 \cdot \frac{\Delta}{p_0}
    $$

    The margin call is triggered when $E_1$ falls below the required margin. The shortfall is:

    $$
    \text{Margin call} = L \cdot E_0 \cdot \frac{\Delta}{p_0} = L \cdot \Delta \cdot \frac{E_0}{p_0}
    $$

    For simplicity, normalizing so that total asset position is worth $p_0$ per unit, the margin call per unit of leverage is $L \cdot \Delta$.

    **(b)** To meet the margin call, borrowers must sell assets. The number of units sold:

    $$
    \text{Units sold} = \frac{L \cdot \Delta}{p_1} = \frac{L \cdot \Delta}{p_0 - \Delta}
    $$

    The further price decline due to this forced selling (with price impact $\eta$ per unit sold):

    $$
    \Delta_2 = \eta \cdot \frac{L \cdot \Delta}{p_1} = \frac{\eta L \Delta}{p_0 - \Delta}
    $$

    **(c)** The total price decline after two rounds is:

    $$
    \Delta_{\text{total}} = \Delta + \Delta_2 = \Delta + \frac{\eta L \Delta}{p_0 - \Delta} = \Delta\left(1 + \frac{\eta L}{p_0 - \Delta}\right)
    $$

    The amplification factor is:

    $$
    \text{Amplification} = 1 + \frac{\eta L}{p_0 - \Delta} > 1
    $$

    For the total decline to significantly exceed the initial shock, we need $\eta L / (p_0 - \Delta)$ to be large, which occurs when:

    - **$\eta$ is large**: illiquid market (high price impact per unit sold).
    - **$L$ is large**: high leverage (more forced selling per unit of price decline).
    - **$p_0 - \Delta$ is small**: already-depressed prices (denominator shrinks as the crisis deepens).

    If we iterate the cascade (each round of selling triggers further price decline, further margin calls, further selling), the total decline converges to:

    $$
    \Delta_{\text{total}} = \frac{\Delta}{1 - \eta L / p_0}
    $$

    (in the geometric series approximation), which diverges when $\eta L / p_0 \geq 1$. This was precisely the mechanism of the 2008 crisis: mortgage-backed securities experienced initial losses $\Delta$, triggering margin calls on leveraged holders (banks, hedge funds), whose forced selling caused further price declines, creating a self-reinforcing spiral that was absent from models treating asset prices as exogenous.

---

**Exercise 6.** Agent-based models (ABMs) can capture reflexive dynamics. Consider a market with three types of agents: fundamentalists (buy when $p < v$, sell when $p > v$), chartists (follow trends), and noise traders. (a) Write trading rules for each type and a price impact function $p_{t+1} = p_t + f(D_t)$ where $D_t$ is excess demand. (b) Show that when chartists dominate, the market exhibits bubbles and crashes. When fundamentalists dominate, prices revert to fundamentals. (c) If agents switch between strategies based on recent performance (e.g., chartists have higher returns during bubbles), describe the endogenous regime-switching dynamics. How does this relate to Soros's concept of boom-bust sequences?

??? success "Solution to Exercise 6"
    **(a)** Trading rules for each agent type:

    **Fundamentalists** ($D_t^F$): Buy when price is below fundamental value, sell when above:

    $$
    D_t^F = n_F \cdot \phi_F (v_t - p_t)
    $$

    where $n_F$ is the fraction of fundamentalists and $\phi_F > 0$ is their aggressiveness.

    **Chartists** ($D_t^C$): Follow trends (buy when price is rising, sell when falling):

    $$
    D_t^C = n_C \cdot \phi_C (p_t - p_{t-1})
    $$

    where $n_C$ is the fraction of chartists and $\phi_C > 0$.

    **Noise traders** ($D_t^N$): Random demand:

    $$
    D_t^N = n_N \cdot \epsilon_t, \quad \epsilon_t \sim N(0, \sigma_\epsilon^2)
    $$

    where $n_F + n_C + n_N = 1$. Total excess demand:

    $$
    D_t = D_t^F + D_t^C + D_t^N = n_F \phi_F(v_t - p_t) + n_C \phi_C(p_t - p_{t-1}) + n_N \epsilon_t
    $$

    Price impact function:

    $$
    p_{t+1} = p_t + f(D_t) = p_t + \mu D_t
    $$

    for a linear impact function with parameter $\mu > 0$.

    **(b)** When chartists dominate ($n_C$ large, $n_F$ small):

    Substituting the demand functions into the price equation:

    $$
    p_{t+1} = p_t + \mu[n_F \phi_F(v_t - p_t) + n_C \phi_C(p_t - p_{t-1}) + n_N \epsilon_t]
    $$

    $$
    = (1 - \mu n_F \phi_F + \mu n_C \phi_C)p_t - \mu n_C \phi_C p_{t-1} + \mu n_F \phi_F v_t + \mu n_N \epsilon_t
    $$

    When $n_C \phi_C \gg n_F \phi_F$, the coefficient on $p_t$ exceeds 1 (positive feedback dominates mean-reversion), and the system can become unstable---producing bubbles (sustained positive deviations from $v_t$) and crashes (rapid corrections when the deviation becomes extreme or when a large negative $\epsilon_t$ shock arrives).

    When fundamentalists dominate ($n_F$ large, $n_C$ small), the coefficient on $p_t$ is less than 1 (mean-reversion dominates momentum), and prices revert to fundamental value with small, stationary fluctuations.

    **(c)** Strategy switching based on recent performance creates **endogenous regime switching**:

    Let $U_t^F$ and $U_t^C$ be the recent (e.g., exponentially weighted) profits of fundamentalists and chartists. The fractions evolve according to a discrete-choice model:

    $$
    n_{C,t} = \frac{\exp(\delta U_t^C)}{\exp(\delta U_t^F) + \exp(\delta U_t^C) + \text{const}}
    $$

    where $\delta > 0$ is the sensitivity of switching to performance.

    The dynamics produce boom-bust sequences:

    1. **Boom**: A positive shock starts a trend. Chartists earn high returns (they follow the trend). Agents switch to chartist strategies ($n_C$ increases). More chartists amplify the trend (positive feedback). The bubble grows.
    2. **Turning point**: As the price deviates far from fundamentals, fundamentalists earn negative returns but the potential for mean-reversion increases. Eventually, a shock or the growing tension triggers a reversal.
    3. **Bust**: The trend reverses. Chartists now follow the downtrend, amplifying the decline. Fundamentalists begin earning positive returns as prices overshoot below fundamentals.
    4. **Recovery**: Agents switch to fundamentalist strategies ($n_F$ increases). Mean-reversion dominates, pulling prices back to fundamentals.

    This is precisely Soros's boom-bust sequence: the cycle is driven by the reflexive interaction between strategies, prices, and strategy adoption. The regime (boom vs. bust vs. quiet) is endogenous---determined by the internal dynamics of the system rather than external shocks.

---

**Exercise 7.** Discuss the implications of reflexivity for quantitative modeling. (a) If a widely adopted pricing model (e.g., Black-Scholes) influences market behavior (e.g., delta hedging creates predictable order flows), is the model describing reality or creating it? This is the "performativity" thesis of MacKenzie. (b) Explain how the 1987 portfolio insurance crash illustrates performativity: the widespread use of synthetic puts via dynamic hedging created the very crash the insurance was designed to protect against. (c) Argue that any sufficiently influential model becomes reflexive, and discuss what this means for the validation and deployment of machine learning models in finance.

??? success "Solution to Exercise 7"
    **(a)** The performativity thesis (MacKenzie, 2006) argues that financial models do not merely describe markets---they actively shape them. The Black-Scholes model is the canonical example:

    - The model assumes continuous delta hedging is possible and that volatility is constant.
    - When traders adopt the model and delta-hedge their options positions, they create **predictable order flows**: as the stock price changes, delta hedgers buy or sell stock in a pattern determined by the Black-Scholes delta.
    - These hedging flows affect the actual stock price dynamics, potentially making the price process more consistent with the model's assumptions (e.g., the "pinning" effect near option strikes at expiry).
    - The model is thus both descriptive (it prices options) and constitutive (it creates the market conditions it assumes).

    The answer to "is the model describing reality or creating it?" is: **both, simultaneously**. This is reflexivity at the level of modeling itself. The model's validity is partly a consequence of its adoption, not purely of its theoretical correctness.

    **(b)** The 1987 portfolio insurance crash illustrates performativity vividly:

    1. **Portfolio insurance**: In the 1980s, many institutional investors adopted "portfolio insurance" strategies that replicated a protective put using dynamic hedging: sell stocks as prices fall, buy as prices rise (the delta of a put becomes more negative as the stock falls).
    2. **Model assumption**: The Black-Scholes framework assumes that the hedger's trades do not affect the stock price---the hedger is a price taker in a perfectly liquid market.
    3. **Reality**: By October 1987, an estimated \$60--90 billion in assets were managed with portfolio insurance strategies. When the market began to fall, all these strategies simultaneously dictated selling stocks.
    4. **Feedback loop**: The aggregate selling from portfolio insurance programs pushed prices lower, which triggered more selling (the delta of the synthetic put became more negative at lower prices), which pushed prices lower still.
    5. **Crash**: On October 19, 1987 (Black Monday), the S&P 500 fell 20.5% in a single day. The very strategy designed to protect against crashes **caused** the crash through the reflexive feedback between hedging models and market prices.

    The model's assumption of no market impact was violated precisely because the model was so widely adopted that the aggregate hedging flows overwhelmed market liquidity.

    **(c)** The general principle is: **any sufficiently influential model becomes reflexive**. This follows because:

    1. A model that influences a significant fraction of market participants creates predictable aggregate behavior (everyone responds to the same signals in the same way).
    2. Predictable aggregate behavior creates exploitable patterns for other participants and systematic feedback effects.
    3. These feedback effects are not captured by the original model (which assumes the modeler is a price taker), so the model's predictions become biased by its own adoption.

    For **machine learning models in finance**, this implies:

    - **Validation challenge**: Traditional backtesting assumes that the model's deployment does not change the data-generating process. But if a successful ML model is widely adopted, the market dynamics shift, and the backtest performance is no longer representative of live performance. This is a form of **concept drift** induced by the model itself.
    - **Alpha decay as reflexivity**: Profitable ML signals attract imitators. As more funds trade on the same signal, the signal's profitability is arbitraged away---not because the signal was spurious, but because collective exploitation of the signal changes the market.
    - **Amplification risk**: If many ML models learn similar patterns from similar data (e.g., all trained on price/volume features), they may produce correlated strategies that amplify market moves, analogous to the portfolio insurance crash.
    - **Deployment implications**: Model deployment should account for market impact and competitive effects. Stress tests should include scenarios where the model's predictions are self-defeating (because too many participants act on them) or self-fulfilling (because collective action creates the predicted pattern). Diversity of model architectures, training data, and signals is a defense against reflexive instability.
