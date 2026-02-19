# Chapter 23: Robust Pricing

This chapter develops the theory of pricing, hedging, and decision-making under model uncertainty—when no single probability model can be trusted. Starting from the distinction between risk (known probabilities) and Knightian uncertainty (unknown or ambiguous probabilities), we build model-free pricing bounds via the Skorokhod embedding problem and martingale optimal transport, develop robust hedging strategies that perform well across a set of models, study ambiguity-averse preferences and their implications for portfolio choice, and construct the nonlinear expectation framework of $g$-expectations and second-order BSDEs that provides the mathematical foundation for pricing under volatility uncertainty.

## Key Concepts

**Model Uncertainty and Ambiguity**
Classical financial mathematics assumes a single probability measure $\mathbb{Q}$; robust pricing acknowledges that $\mathbb{Q}$ is uncertain. **Knightian uncertainty** (Knight, 1921) distinguishes between risk (quantifiable randomness under a known distribution) and uncertainty (ambiguity about which distribution governs the data). The robust framework replaces a single $\mathbb{Q}$ with a **set of probability measures** $\mathcal{Q}$—the ambiguity set—representing all models the decision-maker considers plausible. Common constructions include: $\varepsilon$-contamination neighborhoods $\mathcal{Q} = \{(1-\varepsilon)\mathbb{Q}_0 + \varepsilon\mathbb{Q} : \mathbb{Q} \in \mathcal{M}\}$, **Wasserstein balls** $\mathcal{Q} = \{\mathbb{Q} : W_p(\mathbb{Q}, \mathbb{Q}_0) \leq \varepsilon\}$ providing distributional robustness with metric structure, and moment constraint sets $\mathcal{Q} = \{\mathbb{Q} : \mathbb{E}^{\mathbb{Q}}[g_i] = c_i\}$ calibrated to market observables. The distinction between **misspecification** (the true model lies outside the assumed class) and **estimation error** (the true model lies inside but parameters are uncertain) determines whether robustness is structural or statistical.

**Model-Free Pricing Bounds**
Given only the current prices of traded instruments (the underlying and European options at certain strikes), what are the tightest bounds on the price of an exotic derivative?

- **Superhedging duality**: the model-free upper bound on an exotic payoff $\Phi$ is the cost of the cheapest superhedging portfolio using traded instruments: $\sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[\Phi] = \inf\{c : \exists \text{ hedge } H \text{ with } c + H \geq \Phi\}$
- **Skorokhod embedding problem**: for path-dependent options, the problem reduces to finding a stopping time $\tau$ of Brownian motion such that $B_\tau$ has a specified distribution (the risk-neutral marginal implied by European options). Different embeddings (Root, Rost, Azéma-Yor) correspond to different extremal models and yield sharp bounds for lookback, barrier, and variance options
- **Hobson's robust bounds**: specific sharp bounds for variance options, lookback options, and barrier options derived via the Azéma-Yor embedding, proving that certain model-free relationships hold across all consistent models
- **Martingale optimal transport** (MOT): the multi-marginal extension optimizes $\sup\{\mathbb{E}^{\mathbb{Q}}[\Phi(S_{T_1},\ldots,S_{T_n})] : \mathbb{Q} \in \mathcal{M}(\mu_1,\ldots,\mu_n)\}$ over all martingale measures consistent with given marginals $\mu_i$ (calibrated to European option surfaces at maturities $T_i$). The dual problem identifies the optimal semi-static hedge. Computational methods include linear programming, entropy regularization, and neural network approaches

**Robust Hedging**
Classical hedging minimizes risk under a single model; robust hedging seeks strategies that perform well across the ambiguity set $\mathcal{Q}$:

- **Pathwise hedging**: constructs portfolios whose P&L bounds hold path-by-path without probabilistic assumptions, using only the continuity or bounded variation of price paths
- **Robust delta-gamma hedging**: minimizes the worst-case hedging error $\inf_{\Delta,\Gamma}\sup_{\mathbb{Q} \in \mathcal{Q}}\mathbb{E}^{\mathbb{Q}}[\text{error}^2]$, yielding model-averaged Greeks that are more stable than single-model Greeks
- **Semi-static hedging**: combines dynamic trading in the underlying with static positions in European options (which are liquid and model-independently priced), decomposing the exotic payoff into a replicable component and a residual bounded by the model-free spread
- **Transaction cost robustness**: the super-replication price under proportional transaction costs $k$ is $V^k = V^0 + \mathcal{O}(k^{2/3})$, with the Leland correction providing the leading-order adjustment

**Ambiguity-Averse Preferences**
Standard expected utility $\max_{\pi}\mathbb{E}^{\mathbb{Q}}[U(W)]$ is replaced by preferences that penalize model uncertainty:

- **Max-min expected utility** (Gilboa-Schmeidler): $\max_{\pi}\min_{\mathbb{Q} \in \mathcal{Q}}\mathbb{E}^{\mathbb{Q}}[U(W)]$ optimizes against the worst-case model, yielding conservative portfolios that underweight ambiguous assets—explaining the equity premium puzzle and home bias
- **Multiplier preferences** (Hansen-Sargent): $\max_{\pi}\min_{\mathbb{Q}}\{\mathbb{E}^{\mathbb{Q}}[U(W)] + \theta\,R(\mathbb{Q}\|\mathbb{Q}_0)\}$ penalizes deviation from the reference model $\mathbb{Q}_0$ via relative entropy $R(\mathbb{Q}\|\mathbb{Q}_0)$, with the penalty parameter $\theta$ controlling the degree of robustness
- **Risk-sensitive control**: the exponential criterion $\sup_{\pi}(-\frac{1}{\theta})\ln\mathbb{E}^{\mathbb{Q}_0}[e^{-\theta U(W)}]$ provides an equivalent formulation through the duality between exponential utilities and entropic penalties

**Robust Portfolio Optimization**
The **Black-Litterman** model provides Bayesian robustness: combining market equilibrium (prior) with investor views (likelihood) via Bayes' rule $\mu_{\text{BL}} = [(\tau\Sigma)^{-1} + P'\Omega^{-1}P]^{-1}[(\tau\Sigma)^{-1}\pi + P'\Omega^{-1}q]$, shrinking extreme mean estimates toward equilibrium. **Distributionally robust optimization** minimizes the worst-case expected loss over Wasserstein balls: $\min_{\pi}\sup_{\mathbb{Q}: W(\mathbb{Q},\hat{\mathbb{Q}}_n) \leq \varepsilon}\mathbb{E}^{\mathbb{Q}}[-U(\pi'R)]$, with the radius $\varepsilon$ calibrated to the sample size for finite-sample guarantees. **Dynamic consistency** requires that robust preferences satisfy a recursive structure: today's optimal plan should remain optimal tomorrow given updated information—a stringent requirement that rules out some natural formulations of ambiguity aversion.

**Nonlinear Expectations and Second-Order BSDEs**
The mathematical framework for pricing under volatility uncertainty:

- **Uncertain volatility models** (Avellaneda-Levy-Paras, 1995): the Black-Scholes-Barenblatt equation $\partial_t V + \frac{1}{2}\bar{\sigma}^2(V_{SS})S^2 V_{SS} + rSV_S - rV = 0$ with $\bar{\sigma}^2(\gamma) = \underline{\sigma}^2\mathbf{1}_{\gamma \leq 0} + \overline{\sigma}^2\mathbf{1}_{\gamma > 0}$ selects the worst-case volatility at each point, producing super-replication prices within the volatility band $[\underline{\sigma}, \overline{\sigma}]$
- **$g$-expectations** (Peng): the nonlinear expectation $\mathcal{E}_g[X] = Y_0$ where $(Y_t, Z_t)$ solves the BSDE $dY_t = -g(t, Z_t)\,dt + Z_t\,dW_t$ with $Y_T = X$; the generator $g$ encodes the pricing rule, with $g = 0$ recovering classical linear expectation
- **Sublinear expectations** (Peng): $\hat{\mathbb{E}}[X] = \sup_{\mathbb{Q} \in \mathcal{Q}}\mathbb{E}^{\mathbb{Q}}[X]$ defines a coherent nonlinear expectation under which the canonical process is "$G$-Brownian motion" with uncertain volatility
- **Second-order BSDEs** (2BSDEs) (Soner-Touzi-Zhang): extend BSDEs to pathwise formulations that price and hedge under volatility uncertainty, with the solution representing the super-replication price across all models in $\mathcal{Q}$

**Limits of Quantitative Modeling**
Case studies in model failure—the 1987 crash, LTCM, the 2008 credit crisis, the 2020 COVID-19 vol spike—illustrate recurring themes: tail events occur more frequently than models predict, correlations break down in crises, liquidity vanishes when models assume it persists, and calibration to past data provides false confidence about future dynamics. The chapter concludes with open problems: extending robust methods to high-dimensional settings, developing computationally tractable MOT for realistic derivative books, reconciling statistical and risk-neutral uncertainty, and the fundamental question of how much model structure is needed versus how much can be left unspecified.

!!! note "Role in the Book"
    Robust pricing provides the conceptual counterpoint to the model-specific frameworks developed throughout the book. The superhedging duality connects to the FTAP (Chapter 1), the uncertain volatility model extends the Black-Scholes PDE (Chapter 6), $g$-expectations generalize the Feynman-Kac formula (Chapter 5), and the model risk analysis complements the calibration framework (Chapter 17) and risk management chapter (Chapter 22). The martingale optimal transport framework provides the deepest connection between probability theory and financial mathematics.

---
