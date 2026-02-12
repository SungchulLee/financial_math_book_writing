# Forward Smile


## Introduction


The **forward smile** describes the implied volatility surface of forward-start options or, equivalently, the conditional distribution of future returns implied by today's option prices. It plays a key role in understanding smile dynamics over time and serves as a powerful diagnostic tool for model validation.

While the spot smile $\sigma_{\text{IV}}(K, T)$ reflects the marginal distribution of $S_T$, the forward smile captures the market's expectation of volatility dynamics at future dates. Understanding forward smiles is essential for pricing and hedging path-dependent exotics, assessing model realism, and trading volatility term structure.

## From Spot Smile to Forward Smile


### 1. The Spot Smile


The **spot implied volatility surface** $\sigma_{\text{IV}}(K, T)$ prices options on the current spot:

$$
C(K, T) = C_{\text{BS}}(S_0, K, T, r, q, \sigma_{\text{IV}}(K, T))
$$


This surface reflects the risk-neutral marginal distribution of $S_T$:

$$
\sigma_{\text{IV}}(K, T) \leftrightarrow \text{Law}^{\mathbb{Q}}(S_T)
$$


### 2. The Forward Smile Definition


The **forward smile** $\sigma_{\text{fwd}}(K, T_1, T_2)$ is the implied volatility surface for options starting at future time $T_1$ and expiring at $T_2$:

$$
\sigma_{\text{fwd}}(K, T_1, T_2) = \text{IV of forward-start option with strike } K \text{ over } [T_1, T_2]
$$


More precisely, it characterizes the conditional distribution:

$$
\sigma_{\text{fwd}}(m, T_1, T_2) \leftrightarrow \text{Law}^{\mathbb{Q}}\left(\frac{S_{T_2}}{S_{T_1}} \bigg| \mathcal{F}_{T_1}\right)
$$


where $m = K/S_{T_1}$ is forward moneyness.

### 3. Mathematical Relationship


For a forward-start call option with payoff:

$$
\text{Payoff} = \left(S_{T_2} - m \cdot S_{T_1}\right)^+
$$


the forward implied volatility $\sigma_{\text{fwd}}$ satisfies:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-rT_2}\left(S_{T_2} - m S_{T_1}\right)^+\right] = C_{\text{BS}}^{\text{fwd}}(m, T_2-T_1, \sigma_{\text{fwd}})
$$


### 4. Variance Perspective


Total variance decomposes additively:

$$
w(T_2) = w(T_1) + w_{\text{fwd}}(T_1, T_2)
$$


where $w(T) = \sigma_{\text{IV}}^2(T) \cdot T$ is total variance. The forward implied volatility is:

$$
\sigma_{\text{fwd}}^2(T_1, T_2) = \frac{w(T_2) - w(T_1)}{T_2 - T_1} = \frac{\sigma_{\text{IV}}^2(T_2) T_2 - \sigma_{\text{IV}}^2(T_1) T_1}{T_2 - T_1}
$$


## Forward-Start Options


### 1. Payoff Structure


A **forward-start option** is a European option whose strike is set at a future date $T_1$:

**Forward-start call:**

$$
\text{Payoff}_{T_2} = \left(S_{T_2} - m \cdot S_{T_1}\right)^+
$$


**Forward-start put:**

$$
\text{Payoff}_{T_2} = \left(m \cdot S_{T_1} - S_{T_2}\right)^+
$$


### 2. Pricing Under Black-Scholes


In Black-Scholes, the ratio $S_{T_2}/S_{T_1}$ is independent of $S_{T_1}$:

$$
\frac{S_{T_2}}{S_{T_1}} = \exp\left((r-q-\sigma^2/2)(T_2-T_1) + \sigma(W_{T_2} - W_{T_1})\right)
$$


**Result:** The forward-start call price is:

$$
C_{\text{fwd}} = S_0 e^{-q T_1} \cdot C_{\text{BS}}^{\text{scaled}}(m, T_2-T_1, \sigma)
$$


**Implication:** Under Black-Scholes, the forward smile equals the spot smile (flat).

## Model-Implied Forward Smiles


### 1. Local Volatility Models


In local volatility models:

$$
dS_t = (r-q) S_t dt + \sigma_{\text{loc}}(S_t, t) S_t dW_t
$$


**Critical issue:** Local vol models imply that the forward smile **flattens rapidly**:

$$
\sigma_{\text{fwd}}(m, T_1, T_2) \to \text{flat as } T_1 \to \infty
$$


This contradicts empirical evidence of persistent forward skew.

### 2. Stochastic Volatility Models (Heston)


The Heston model produces:
- **Persistent skew:** Forward skew remains non-zero due to spot-vol correlation
- **Level depends on $\mathbb{E}[v_{T_1}]$:** Expected future variance determines ATM level

**Approximate forward ATM volatility:**

$$
\sigma_{\text{fwd, ATM}}^2(T_1, T_2) \approx \mathbb{E}[v_{T_1}] + \frac{\xi^2}{4\kappa}(1 - e^{-\kappa(T_2-T_1)})
$$


### 3. SABR Model


The forward smile in SABR depends on the backbone parameter $\beta$:
- $\beta = 1$: Forward smile similar to spot smile
- $\beta = 0$: Forward smile flattens faster

### 4. Bergomi's Variance Curve Model


Bergomi models forward variance directly, providing direct control over forward smile dynamics and realistic behavior.

## Practical Relevance


### 1. Cliquet Pricing


**Cliquet option:** A series of forward-start options with periodic reset:

$$
\text{Payoff} = \sum_{i=1}^{n} f\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right)
$$


Cliquet prices are highly sensitive to the forward smile:

| Model | Cliquet Price | Forward Smile |
|-------|--------------|---------------|
| Black-Scholes | Lowest | Flat |
| Local vol | Low | Flattens |
| Heston | Medium | Persists |

### 2. Forward-Start Products


Forward smiles matter for:
- Cliquets and autocallables
- Long-dated exotics
- Forward-starting variance swaps

### 3. Model Validation


The forward smile is a powerful **model discriminator**:
- Compare model-implied forward smile to market-implied (from cliquets)
- Local vol fails this test
- Stochastic vol performs better

## Summary


- Forward smiles encode conditional future volatility distributions
- They are not directly observable but can be inferred from forward-start products
- **Black-Scholes:** Flat forward smile
- **Local volatility:** Forward smile flattens (unrealistic)
- **Stochastic volatility:** Persistent forward skew
- Forward smile behavior reveals model strengths and weaknesses

---

## Further Reading


- Bergomi, L. *Smile Dynamics* series of papers
- Gatheral, J. *The Volatility Surface*
- Piterbarg, V. *Smiling Hybrids*
