# Error Analysis and Convergence

Understanding the error structure of the COS method is essential for choosing parameters ($N$, $[a,b]$, $L$) that achieve a target accuracy with minimal computation. The total error decomposes into two independent components: the truncation error from restricting the density to a finite interval, and the series truncation error from using finitely many cosine terms. This section derives rigorous bounds for each component, establishes the exponential convergence rate for smooth densities, and explains why the COS method achieves machine precision with remarkably few terms for standard financial models.

!!! info "Prerequisites"

    - [COS Pricing Formula](cos_pricing_formula.md) (the formula whose error we analyze)
    - [Truncation to Finite Domain](truncation_to_finite_domain.md) (domain truncation)
    - [Convergence of Fourier Series](../fourier_series/convergence_of_fourier_series.md) (coefficient decay rates)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Decompose the total COS error into truncation and series components
    2. Bound each error component in terms of model parameters
    3. Determine the convergence rate for a given model
    4. Choose $N$ and $[a, b]$ to achieve a prescribed accuracy
    5. Explain why exponential convergence holds for affine models with smooth densities

---

## Error Decomposition

**Recall** (see [§ COS Pricing Formula](cos_pricing_formula.md)): the COS approximation is $V_{\text{COS}} = e^{-rT}\sum_{k=0}^{N-1}{}' F_k\, V_k$. The total error $|V - V_{\text{COS}}|$ arises from two sources that we analyze separately.

!!! note "Theorem: Error Decomposition"
    The total COS error satisfies

    $$
    |V - V_{\text{COS}}| \leq \underbrace{|V - V_{[a,b]}|}_{\text{truncation error } \varepsilon_1} + \underbrace{|V_{[a,b]} - V_{\text{COS}}|}_{\text{series truncation error } \varepsilon_2}
    $$

    where $V_{[a,b]} = e^{-rT}\int_a^b \Phi(x)f(x)\,dx$ is the option value with the density restricted to $[a, b]$.

This decomposition follows from the triangle inequality. The two errors are independent: $\varepsilon_1$ depends only on the choice of $[a, b]$, while $\varepsilon_2$ depends on $N$ and the smoothness of $f$.

---

## Truncation Error Analysis

The truncation error arises from the probability mass and payoff contribution outside $[a, b]$.

!!! note "Theorem: Truncation Error Bound"
    For a European call with payoff $\Phi(x) = K(e^x - 1)^+$:

    $$
    \varepsilon_1 = e^{-rT}\left|\int_{\mathbb{R}\setminus[a,b]} \Phi(x)f(x)\,dx\right| \leq e^{-rT}K\left[\mathbb{E}[e^{X}\mathbf{1}_{X \notin [a,b]}] + P(X \notin [a,b])\right]
    $$

    If $X$ has mean $c_1$, variance $c_2$, and the truncation interval is $[c_1 - L\sqrt{c_2}, c_1 + L\sqrt{c_2}]$, then for distributions with sub-Gaussian tails:

    $$
    \varepsilon_1 \leq C\, e^{-\alpha L^2}
    $$

    for constants $C, \alpha > 0$ depending on the model parameters.

For the cumulant-based truncation with $L = 10$:

| Model | $\varepsilon_1$ (approximate) |
|---|---|
| Black--Scholes | $< 10^{-20}$ |
| Heston (typical) | $< 10^{-15}$ |
| Variance Gamma | $< 10^{-10}$ |

The truncation error is negligible for all standard models with $L \geq 10$.

---

## Series Truncation Error Analysis

The series truncation error arises from using $N$ cosine terms instead of infinitely many. This is the dominant error component and the one that determines the convergence rate.

!!! note "Theorem: Series Truncation Error"
    Assume $f$ is supported on $[a, b]$ (truncation error already handled). The series truncation error is

    $$
    \varepsilon_2 = e^{-rT}\left|\sum_{k=N}^{\infty}{}' A_k\, V_k\right|
    $$

    This satisfies the bound

    $$
    \varepsilon_2 \leq e^{-rT}\left(\sum_{k=N}^{\infty} A_k^2\right)^{1/2}\left(\sum_{k=N}^{\infty} V_k^2\right)^{1/2}
    $$

    by the Cauchy--Schwarz inequality.

The bound involves the tail sums of two coefficient sequences:

- $\{A_k\}$: the density coefficients, whose decay rate depends on the smoothness of $f$
- $\{V_k\}$: the payoff coefficients, whose decay depends on the smoothness of $\Phi$

---

## Convergence Rate for Smooth Densities

The convergence rate of the COS method is determined by the slower-decaying of the two coefficient sequences. Since payoff functions (calls, puts) have a kink at the strike, the payoff coefficients decay as $O(1/k^2)$. However, this does not limit the COS method because the density coefficients $A_k$ typically decay much faster.

!!! note "Theorem: Exponential Convergence for Analytic Densities"
    If the density $f$ extends to an analytic function in a strip $|\text{Im}(z)| < \beta$ around the real axis, then the cosine coefficients decay exponentially:

    $$
    |A_k| \leq C\, e^{-\beta k\pi/(b-a)}
    $$

    and the series truncation error satisfies

    $$
    \varepsilon_2 \leq C'\, e^{-\beta N\pi/(b-a)}
    $$

    for constants $C, C'$ depending on $f$ and $\Phi$.

**Proof sketch.** The cosine coefficient $A_k$ can be written as a contour integral in the complex plane. Shifting the contour by $\pm i\beta$ (into the strip of analyticity) introduces a factor of $e^{-\beta k\pi/(b-a)}$ from the exponential term, while the integral along the shifted contour is bounded by the supremum of $|f|$ on the shifted contour. $\square$

The exponential convergence rate $\beta\pi/(b-a)$ depends on the ratio of the analyticity strip width $\beta$ to the interval length $b-a$. This explains why narrower truncation intervals (when justified by negligible truncation error) give faster convergence.

---

## Convergence Rates for Standard Models

Different financial models have different analyticity properties, leading to different convergence rates:

| Model | Density analyticity | Coefficient decay | $N$ for 8-digit accuracy |
|---|---|---|---|
| Black--Scholes (log-normal) | Entire ($\beta = \infty$) | $O(e^{-ck^2})$ (super-exponential) | $\approx 32$ |
| Heston | Strip of finite width | $O(e^{-ck})$ (exponential) | $\approx 64$--$128$ |
| Variance Gamma | Strip of finite width | $O(e^{-ck})$ (exponential) | $\approx 128$ |
| CGMY ($Y < 1$) | Strip of finite width | $O(e^{-ck})$ (exponential) | $\approx 128$--$256$ |
| CGMY ($Y \geq 1$) | No strip / reduced width | $O(1/k^p)$ (algebraic) | $\approx 10^3$ or more |

!!! warning "Algebraic Convergence"
    When the density is not analytic (e.g., models with jumps that produce density kinks), the COS method converges only algebraically: $\varepsilon_2 = O(1/N^p)$ for some power $p$. In such cases, many more terms are needed, and alternative methods (FFT, numerical integration) may be competitive.

---

## Interaction Between Truncation and Series Error

The two error components interact through the interval length $b - a$:

- **Wider $[a, b]$** (larger $L$): reduces truncation error $\varepsilon_1$ but increases $b - a$, which slows the exponential convergence rate $e^{-\beta N\pi/(b-a)}$ and requires larger $N$.

- **Narrower $[a, b]$** (smaller $L$): improves convergence rate but risks significant truncation error.

The optimal balance is achieved when both errors are comparable. For the standard cumulant-based truncation with $L = 10$, the truncation error is $O(10^{-20})$ or smaller, while the series error with $N = 64$ is typically $O(10^{-8})$ to $O(10^{-12})$. Since the truncation error is always negligible, the series error dominates and $N$ is the primary tuning parameter.

---

## Practical Error Estimation

In implementations, the convergence can be monitored empirically:

!!! tip "Convergence Diagnostics"

    1. **Richardson extrapolation.** Compute $V_N$ and $V_{2N}$. If $|V_{2N} - V_N| < \varepsilon$, then $V_{2N}$ is accurate to approximately $\varepsilon$.

    2. **Coefficient magnitude.** If $|F_k V_k| < \varepsilon$ for $k \geq N_0$, then the remaining terms contribute less than $(N - N_0)\varepsilon$ to the sum.

    3. **Double the interval test.** Recompute with $[a', b'] = [2a, 2b]$. If the price changes by less than $\varepsilon$, the truncation is adequate.

---

## Example: Error Convergence Under Black--Scholes

To illustrate the convergence behavior, we examine the error as a function of $N$ for the Black--Scholes model.

!!! example "Convergence Study: Black--Scholes Call"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0.10$, $\sigma = 0.25$, $T = 0.1$, $[a,b] = [-1, 1]$.

    | $N$ | COS price | $|V_{\text{COS}} - V_{\text{BS}}|$ | Convergence rate |
    |---|---|---|---|
    | 8 | 3.6614 | $2.1 \times 10^{-3}$ | --- |
    | 16 | 3.6593 | $3.5 \times 10^{-6}$ | super-exponential |
    | 32 | 3.6593 | $1.2 \times 10^{-11}$ | super-exponential |
    | 64 | 3.6593 | $< 10^{-15}$ | machine precision |

    The error decreases faster than any exponential, consistent with the super-exponential coefficient decay of the Gaussian density. The convergence is so rapid that $N = 32$ already provides 11-digit accuracy.

---

## Example: Error Convergence Under Heston

The Heston model provides the benchmark for exponential (but not super-exponential) convergence.

!!! example "Convergence Study: Heston Call"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0$, $T = 1$, typical Heston parameters.

    | $N$ | $|V_{\text{COS}} - V_{\text{ref}}|$ | Convergence rate |
    |---|---|---|
    | 16 | $\approx 10^{-2}$ | --- |
    | 32 | $\approx 10^{-4}$ | exponential |
    | 64 | $\approx 10^{-7}$ | exponential |
    | 128 | $\approx 10^{-11}$ | exponential |
    | 256 | $\approx 10^{-15}$ | machine precision |

    Each doubling of $N$ adds approximately 3--4 digits of accuracy, consistent with exponential convergence $\varepsilon_2 \sim e^{-cN}$.

---

## Summary

The COS method's error structure is clean and well-understood:

| Error component | Source | Bound | Typical magnitude |
|---|---|---|---|
| Truncation error $\varepsilon_1$ | Restricting density to $[a, b]$ | $O(e^{-\alpha L^2})$ | $< 10^{-15}$ with $L = 10$ |
| Series error $\varepsilon_2$ | Using $N$ cosine terms | $O(e^{-\beta N\pi/(b-a)})$ for analytic $f$ | Dominant; tuned via $N$ |
| Total error | $\varepsilon_1 + \varepsilon_2$ | Dominated by $\varepsilon_2$ | Target via choice of $N$ |

**For models with analytic characteristic functions and smooth densities, the COS method achieves exponential convergence in $N$, with the convergence rate determined by the width of the analyticity strip of the density relative to the truncation interval length.**

---

## Exercises

**Exercise 1.** The total COS error satisfies $|V - V_{\text{COS}}| \leq \varepsilon_1 + \varepsilon_2$, where $\varepsilon_1$ is the truncation error and $\varepsilon_2$ is the series truncation error. For the Heston model with $L = 10$ and $N = 128$, the text states $\varepsilon_1 < 10^{-15}$ and $\varepsilon_2 \approx 10^{-11}$. Verify that the total error is dominated by $\varepsilon_2$ and determine how large $N$ must be to make $\varepsilon_2 < 10^{-15}$.

??? success "Solution to Exercise 1"
    With $\varepsilon_1 < 10^{-15}$ and $\varepsilon_2 \approx 10^{-11}$:

    $$
    |V - V_{\text{COS}}| \leq \varepsilon_1 + \varepsilon_2 < 10^{-15} + 10^{-11} \approx 10^{-11}
    $$

    The total error is dominated by $\varepsilon_2$ since $\varepsilon_1/\varepsilon_2 < 10^{-15}/10^{-11} = 10^{-4}$, making the truncation error contribution negligible.

    To find $N$ such that $\varepsilon_2 < 10^{-15}$: From the convergence data, the Heston model shows exponential convergence $\varepsilon_2 \sim e^{-cN}$. Using two data points from the table:

    - $N = 64$: $\varepsilon_2 \approx 10^{-7}$
    - $N = 128$: $\varepsilon_2 \approx 10^{-11}$

    From $e^{-64c} \cdot K \approx 10^{-7}$ and $e^{-128c}\cdot K \approx 10^{-11}$, dividing: $e^{-64c} = 10^{-4}$, so $c = 4\ln 10/64 \approx 0.1439$.

    For $\varepsilon_2 < 10^{-15}$: Using the relationship $\varepsilon_2(N) = \varepsilon_2(128)\cdot e^{-c(N-128)}$:

    $$
    10^{-11}\cdot e^{-0.1439(N-128)} < 10^{-15}
    $$

    $$
    e^{-0.1439(N-128)} < 10^{-4} \implies 0.1439(N-128) > 4\ln 10 \approx 9.21
    $$

    $$
    N - 128 > 64 \implies N > 192
    $$

    Therefore $N \approx 192$ is needed. Rounding to the next power of 2, $N = 256$ provides a comfortable margin, consistent with the table showing $\varepsilon_2 \approx 10^{-15}$ at $N = 256$.

---

**Exercise 2.** The series truncation error bound uses the Cauchy-Schwarz inequality: $\varepsilon_2 \leq e^{-rT}(\sum_{k=N}^{\infty}A_k^2)^{1/2}(\sum_{k=N}^{\infty}V_k^2)^{1/2}$. For a call payoff, the payoff coefficients decay as $V_k = O(1/k^2)$. If the density coefficients decay as $|A_k| \leq Ce^{-\beta k\pi/(b-a)}$, show that the dominant factor in the error bound is the density coefficient tail sum, and derive an explicit bound on $\varepsilon_2$.

??? success "Solution to Exercise 2"
    For the call payoff, $V_k = O(K/k^2)$ for large $k$ (due to the kink in $(e^x - 1)^+$ at $x = 0$). The payoff coefficient tail sum is:

    $$
    \sum_{k=N}^{\infty}V_k^2 = O\!\left(\sum_{k=N}^{\infty}\frac{K^2}{k^4}\right) = O\!\left(\frac{K^2}{N^3}\right)
    $$

    The density coefficient tail sum with exponential decay $|A_k| \leq Ce^{-\beta k\pi/(b-a)}$ is:

    $$
    \sum_{k=N}^{\infty}A_k^2 \leq C^2\sum_{k=N}^{\infty}e^{-2\beta k\pi/(b-a)} = \frac{C^2 e^{-2\beta N\pi/(b-a)}}{1 - e^{-2\beta\pi/(b-a)}}
    $$

    Let $\gamma = 2\beta\pi/(b-a)$. This simplifies to $O(e^{-\gamma N})$.

    By Cauchy--Schwarz:

    $$
    \varepsilon_2 \leq e^{-rT}\left(\sum_{k=N}^{\infty}A_k^2\right)^{1/2}\left(\sum_{k=N}^{\infty}V_k^2\right)^{1/2} = O\!\left(e^{-rT}\cdot e^{-\gamma N/2}\cdot\frac{K}{N^{3/2}}\right)
    $$

    The dominant factor is $e^{-\gamma N/2} = e^{-\beta N\pi/(b-a)}$, which decays exponentially in $N$. The algebraic factor $N^{-3/2}$ from the payoff coefficients is negligible compared to the exponential decay. Therefore, the density coefficient tail sum is the dominant factor, and:

    $$
    \varepsilon_2 \leq C' e^{-rT}K\,e^{-\beta N\pi/(b-a)}\,N^{-3/2}
    $$

    for a constant $C'$. The exponential term dominates, confirming that the convergence rate is determined by the density's analyticity strip width $\beta$.

---

**Exercise 3.** For the Black-Scholes model, the density is Gaussian (entire function) and the coefficients decay as $|A_k| \sim e^{-ck^2}$ (super-exponential). Using the convergence data in the example ($N = 8$: error $\approx 10^{-3}$; $N = 16$: error $\approx 10^{-6}$; $N = 32$: error $\approx 10^{-11}$), estimate the parameter $c$ in the decay rate and predict the error for $N = 48$.

??? success "Solution to Exercise 3"
    For super-exponential convergence $\varepsilon_2 \sim e^{-cN^2}$, we can estimate $c$ from the data:

    - $N = 8$: $\varepsilon_2 \approx 2.1\times 10^{-3}$, so $-64c \approx \ln(2.1\times 10^{-3}) = -6.17$, giving $c \approx 0.0964$
    - $N = 16$: $\varepsilon_2 \approx 3.5\times 10^{-6}$, so $-256c \approx \ln(3.5\times 10^{-6}) = -12.56$, giving $c \approx 0.0491$
    - $N = 32$: $\varepsilon_2 \approx 1.2\times 10^{-11}$, so $-1024c \approx \ln(1.2\times 10^{-11}) = -25.14$, giving $c \approx 0.0246$

    The estimates of $c$ are decreasing because the actual error model is not a pure $e^{-cN^2}$ form---there are sub-leading corrections and the payoff coefficient decay also contributes. Using the two most reliable data points ($N = 16$ and $N = 32$):

    From $e^{-c\cdot 256}/e^{-c\cdot 1024} = 10^{-6}/10^{-11} = 10^5$, so $e^{768c} = 10^5$, giving $c = 5\ln 10/768 \approx 0.01499$.

    **Prediction for $N = 48$:** Using $\varepsilon_2(N) \approx e^{-cN^2}$ with the relationship $\varepsilon_2(48)/\varepsilon_2(32) = e^{-c(2304-1024)} = e^{-1280c}$:

    $$
    \varepsilon_2(48) \approx 1.2\times 10^{-11}\cdot e^{-1280\times 0.01499} \approx 1.2\times 10^{-11}\cdot e^{-19.19} \approx 1.2\times 10^{-11}\times 4.6\times 10^{-9} \approx 5.5\times 10^{-20}
    $$

    This is well below machine precision ($\approx 10^{-16}$), so $N = 48$ would effectively achieve machine precision for this Black--Scholes case, consistent with the observation that $N = 32$ already provides 11-digit accuracy.

---

**Exercise 4.** Explain why narrower truncation intervals (smaller $b - a$) improve the COS convergence rate. If the analyticity strip width is $\beta$ and the interval length is $b - a$, the exponential convergence rate is $e^{-\beta N\pi/(b-a)}$. For the Heston model with $\beta = 0.5$ and two truncation choices $b - a = 5$ and $b - a = 10$, compare the values of $N$ needed to achieve $\varepsilon_2 < 10^{-8}$.

??? success "Solution to Exercise 4"
    The exponential convergence rate is $\varepsilon_2 \sim e^{-\beta N\pi/(b-a)}$. The ratio $\beta\pi/(b-a)$ appears in the exponent, so a narrower interval (smaller $b-a$) increases this ratio and accelerates convergence.

    **Intuitive explanation:** A narrower interval means the cosine frequencies $\omega_k = k\pi/(b-a)$ are more widely spaced. Since the characteristic function (and hence the density coefficients) decay at a rate determined by $\beta$ in frequency space, wider frequency spacing means that fewer terms are needed before the coefficients become negligible.

    **Quantitative comparison for Heston with $\beta = 0.5$:**

    Case 1: $b - a = 5$. The convergence rate per term is $e^{-0.5\pi/5} = e^{-\pi/10} \approx e^{-0.3142}$. For $\varepsilon_2 < 10^{-8}$:

    $$
    e^{-0.3142 N} < 10^{-8} \implies N > \frac{8\ln 10}{0.3142} \approx 58.6
    $$

    So $N \approx 59$ suffices.

    Case 2: $b - a = 10$. The convergence rate per term is $e^{-0.5\pi/10} = e^{-\pi/20} \approx e^{-0.1571}$. For $\varepsilon_2 < 10^{-8}$:

    $$
    e^{-0.1571 N} < 10^{-8} \implies N > \frac{8\ln 10}{0.1571} \approx 117.2
    $$

    So $N \approx 118$ is needed.

    Doubling the interval width approximately doubles the required $N$ (from 59 to 118). This confirms that the convergence rate scales inversely with $b - a$, and keeping the interval as narrow as possible (while maintaining negligible truncation error) is optimal.

---

**Exercise 5.** The convergence study for the Heston model shows each doubling of $N$ adds approximately 3-4 digits of accuracy. Verify this is consistent with exponential convergence $\varepsilon_2 \sim e^{-cN}$ by computing $c$ from the data ($N = 32$: error $\approx 10^{-4}$; $N = 64$: error $\approx 10^{-7}$). What convergence rate would you expect for algebraic convergence $\varepsilon_2 \sim N^{-p}$ with $p = 4$?

??? success "Solution to Exercise 5"
    From the Heston data: $N = 32$ gives $\varepsilon_2 \approx 10^{-4}$ and $N = 64$ gives $\varepsilon_2 \approx 10^{-7}$.

    **Computing $c$ for exponential convergence $\varepsilon_2 \sim Ke^{-cN}$:**

    $$
    \frac{\varepsilon_2(32)}{\varepsilon_2(64)} = e^{-32c}/e^{-64c} = e^{32c} = \frac{10^{-4}}{10^{-7}} = 10^3
    $$

    $$
    32c = 3\ln 10 \implies c = \frac{3\ln 10}{32} = \frac{6.908}{32} \approx 0.2159
    $$

    **Verification:** Each doubling of $N$ adds $32c/\ln 10 = 32\times 0.2159/2.3026 \approx 3.0$ decimal digits. The data shows approximately 3 digits gained from $N = 32$ to $64$ ($10^{-4} \to 10^{-7}$) and approximately 4 digits from $N = 64$ to $128$ ($10^{-7} \to 10^{-11}$). The 3--4 digit range per doubling is consistent with $c \approx 0.2$.

    **Algebraic convergence comparison:** For $\varepsilon_2 = C N^{-p}$ with $p = 4$:

    $$
    \frac{\varepsilon_2(N)}{\varepsilon_2(2N)} = \frac{(2N)^4}{N^4} = 2^4 = 16
    $$

    Each doubling of $N$ reduces the error by a factor of $2^4 = 16$, which corresponds to $\log_{10}(16) \approx 1.2$ decimal digits. This is much slower than the 3--4 digits per doubling observed for exponential convergence. To go from $10^{-4}$ to $10^{-11}$ (7 digits) with $p = 4$ algebraic convergence would require increasing $N$ by a factor of $10^{7/4} \approx 56$, i.e., from $N = 32$ to $N \approx 1800$---far more than the $N = 128$ needed with exponential convergence.

---

**Exercise 6.** The practical convergence diagnostic suggests computing $V_N$ and $V_{2N}$ and checking if $|V_{2N} - V_N| < \varepsilon$. Explain why this Richardson-type estimate works for exponentially convergent methods. For algebraic convergence $\varepsilon_2 = O(N^{-p})$, derive the relationship between $|V_{2N} - V_N|$ and the true error $|V_{2N} - V_{\text{exact}}|$.

---

??? success "Solution to Exercise 6"
    **Why Richardson extrapolation works for exponential convergence:**

    Suppose $V_N = V_{\text{exact}} + Ke^{-cN}$ (leading error term). Then:

    $$
    V_{2N} - V_N = Ke^{-cN}(e^{-cN} - 1) = -Ke^{-cN}(1 - e^{-cN})
    $$

    The true error at $2N$ is $V_{2N} - V_{\text{exact}} = Ke^{-2cN}$. The ratio:

    $$
    \frac{|V_{2N} - V_{\text{exact}}|}{|V_{2N} - V_N|} = \frac{e^{-2cN}}{e^{-cN}(1 - e^{-cN})} = \frac{e^{-cN}}{1 - e^{-cN}}
    $$

    For large $cN$ (which holds when the method is converging well), $e^{-cN} \ll 1$, so:

    $$
    |V_{2N} - V_{\text{exact}}| \approx e^{-cN}\cdot|V_{2N} - V_N| \ll |V_{2N} - V_N|
    $$

    This means the true error at $2N$ is exponentially smaller than the difference $|V_{2N} - V_N|$. Therefore, if $|V_{2N} - V_N| < \varepsilon$, the true error is much smaller than $\varepsilon$, making $|V_{2N} - V_N|$ a conservative error estimate.

    **Algebraic convergence case:** Suppose $V_N = V_{\text{exact}} + C N^{-p}$. Then:

    $$
    V_{2N} - V_N = C(2N)^{-p} - CN^{-p} = CN^{-p}(2^{-p} - 1)
    $$

    The true error at $2N$ is:

    $$
    V_{2N} - V_{\text{exact}} = C(2N)^{-p} = CN^{-p}\cdot 2^{-p}
    $$

    The ratio:

    $$
    \frac{|V_{2N} - V_{\text{exact}}|}{|V_{2N} - V_N|} = \frac{2^{-p}}{1 - 2^{-p}}
    $$

    This is a constant (independent of $N$). For $p = 4$: $2^{-4}/(1 - 2^{-4}) = (1/16)/(15/16) = 1/15$.

    Therefore, for algebraic convergence with $p = 4$:

    $$
    |V_{2N} - V_{\text{exact}}| = \frac{1}{15}|V_{2N} - V_N|
    $$

    The difference $|V_{2N} - V_N|$ overestimates the true error by a factor of 15, which is still a useful (conservative) estimate but not as dramatically conservative as in the exponential case.
