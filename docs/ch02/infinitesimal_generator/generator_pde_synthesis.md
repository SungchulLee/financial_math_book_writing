# Generator and PDEs: A Synthesis

This page provides a **conceptual map** connecting the infinitesimal generator to the PDEs of diffusion theory. All documents in Sections 2.7–2.8 describe the **same Markov diffusion** from different perspectives.

---

## The Hierarchy of Descriptions

```
Generator
  |  (Markov property extends infinitesimal to finite time)
  v
Backward equation (expectations)
  |  (time integration + martingale averaging)
  v
Dynkin (integrated form)
  |  (assume density exists + integration by parts)
  v
Forward equation (densities)
  |  (fixed points: densities in ker L*)
  v
Stationarity / long-time behavior
```

Each downward arrow represents a **loss of pathwise information** but a **gain in robustness and applicability**.

---

## Level-by-Level Summary

| Level | Object | Equation | Question Answered |
|-------|--------|----------|-------------------|
| **Generator** | $\mathcal{L}$ | $(\mathcal{L}f)(x) = \lim_{t\downarrow 0}\frac{\mathbb{E}_x[f(X_t)] - f(x)}{t}$ | What happens infinitesimally? |
| **Backward** | $u(t,x) = \mathbb{E}_x[g(X_t)]$ | $\partial_t u = \mathcal{L}u$ | Expected payoff starting from $x$? |
| **Dynkin** | Same $u$, integrated | $\mathbb{E}_x[g(X_t)] = g(x) + \mathbb{E}_x\left[\int_0^t \mathcal{L}g\,ds\right]$ | Accumulated expected drift? |
| **Forward** | $p(x,t)$ density | $\partial_t p = \mathcal{L}^* p$ | Where does probability mass go? |
| **Stationary** | $p_\infty$ | $\mathcal{L}^* p_\infty = 0$ | Long-run distribution? |

---

## The Generator: Foundation of Everything

For the diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$:

$$\boxed{\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{\sigma^2(x)}{2}\frac{\partial^2}{\partial x^2}}$$

The generator encodes:

- **Local drift** (first-order term)
- **Local dispersion** (second-order term)

It **uniquely characterizes** the process in law (via the martingale problem).

See [Infinitesimal Generator](infinitesimal_generator.md)

---

## Generator to Backward Equation

**(Markov property extends infinitesimal to finite time)**

The generator gives only an infinitesimal derivative at $t=0$:

$$(\mathcal{L}f)(x) = \lim_{h\downarrow 0}\frac{\mathbb{E}_x[f(X_h)] - f(x)}{h}$$

The **Markov property** extends this to all times. Define $u(t,x) = \mathbb{E}_x[f(X_t)]$. Then:

$$\frac{u(t+h,x) - u(t,x)}{h} = \mathbb{E}_x\left[\frac{\mathbb{E}_{X_t}[f(X_h)] - f(X_t)}{h}\right] \xrightarrow{h \to 0} \mathbb{E}_x[(\mathcal{L}f)(X_t)] = (\mathcal{L}u)(t,x)$$

**PDE**:
$$\frac{\partial u}{\partial t} = \mathcal{L}u, \quad u(0,x) = g(x)$$

**What's gained**: Finite-time evolution of expectations.

**What's lost**: Pathwise detail (we only see averages).

See [Kolmogorov Backward Equation](kolmogorov_backward.md)

---

## Backward to Dynkin (Integration)

**(time integration / martingale averaging)**

Dynkin's formula is the time-integrated (weak) form of the backward equation, obtained by averaging out the martingale term:

$$\mathbb{E}_x[g(X_t)] = g(x) + \mathbb{E}_x\left[\int_0^t (\mathcal{L}g)(X_s)\,ds\right]$$

**What's gained**: 

- Works for stopping times
- No PDE regularity required
- Robust under weak assumptions

**What's lost**: Pointwise-in-time information.

!!! info "Dynkin = E[Ito]"
    Dynkin's formula is Ito's formula with the martingale part averaged out.

See [Dynkin's Formula](dynkin_formula.md)

---

## Dynkin to Forward Equation (Duality)

**(assume density exists + integration by parts)**

Dynkin gives an expectation identity. To get the forward equation:

1. **Assume density exists**: $\mathbb{P}(X_t \in dx) = p(x,t)\,dx$
2. **Rewrite Dynkin**: $\frac{d}{dt}\int f(x)p(x,t)\,dx = \int (\mathcal{L}f)(x)p(x,t)\,dx$
3. **Integration by parts**: Transfer $\mathcal{L}$ from $f$ to $p$

$$\int (\mathcal{L}f) \cdot p\,dx = \int f \cdot (\mathcal{L}^* p)\,dx$$

Since this holds for all test functions $f$: $\partial_t p = \mathcal{L}^* p$.

The backward equation acts on **test functions** $f$:
$$\frac{d}{dt}\mathbb{E}[f(X_t)] = \mathbb{E}[(\mathcal{L}f)(X_t)]$$

The forward equation acts on **densities** $p$:
$$\frac{\partial p}{\partial t} = \mathcal{L}^* p$$

They are connected by duality:
$$\int f \cdot \partial_t p\,dx = \int (\mathcal{L}f) \cdot p\,dx = \int f \cdot (\mathcal{L}^* p)\,dx$$

**What's gained**: Full distributional information.

**What's lost**: Conditioning on specific payoffs.

See [Fokker–Planck Equation](fokker_planck.md)

---

## Forward to Stationarity (Long-Time Limit)

**(fixed points: densities in ker $\mathcal{L}^*$)**

A stationary density $p_\infty$ satisfies $\partial_t p_\infty = 0$. Substituting into the forward equation:

$$0 = \mathcal{L}^* p_\infty$$

So stationarity = kernel of $\mathcal{L}^*$ restricted to **probability densities**.

!!! warning "Existence is Not Automatic"
    - Many processes have **no** stationary distribution (transience, null recurrence)
    - Some have **multiple** stationary distributions
    - Convergence to stationarity requires **ergodicity**
    
    The arrow represents a fixed-point condition, not a guaranteed limit.

**What's gained**: Global qualitative behavior (ergodicity, recurrence).

**What's lost**: Time-dependent dynamics.

See [Invariant Measures](../diffusion_process/invariant_measures_and_stationarity.md)

---

## Reversibility of Arrows

| Transition | Reversible? | Reason |
|------------|-------------|--------|
| Generator - Backward | Yes | $\mathcal{L} = \lim_{t\downarrow 0} \frac{e^{t\mathcal{L}} - I}{t}$ |
| Backward - Dynkin | Yes | Integration / differentiation |
| Dynkin - Backward | No | Loses local-in-time info |
| Forward - Backward | No | Requires density + regularity |
| Stationary - Forward | No | Asymptotics lose dynamics |

---

## The Complete Picture

```
+-----------------------------------+
|           GENERATOR L             |
|    (infinitesimal, t=0 only)      |
+----------------+------------------+
                 | Markov property extends to finite time
                 v
+-----------------------------------+
|       BACKWARD EQUATION           |
|   dt(u) = Lu  (expectations)      |
+----------------+------------------+
                 | time integration + martingale averaging
                 v
+-----------------------------------+
|       DYNKIN'S FORMULA            |
|  E[g(Xt)] = g(x) + E[int Lg ds]   |
+----------------+------------------+
                 | assume density exists + integration by parts
                 v
+-----------------------------------+
|    FORWARD EQUATION (F-P)         |
|    dt(p) = L*p  (densities)       |
+----------------+------------------+
                 | fixed points: densities in ker L*
                 v
+-----------------------------------+
|         STATIONARITY              |
|   L*p_inf = 0  (equilibrium)      |
+-----------------------------------+
```

### Arrow-by-Arrow Explanation

| Arrow | Label | Meaning |
|-------|-------|---------|
| Generator → Backward | Markov property | Extend infinitesimal generator to finite time via $\mathbb{E}_x[\mathbb{E}_{X_t}[\cdot]]$ |
| Backward → Dynkin | time integration | Integrate in time, average out martingale |
| Dynkin → Forward | density + duality | Assume density exists, transfer $\mathcal{L}$ to $p$ via integration by parts |
| Forward → Stationarity | fixed points | Time-independent solutions: probability densities in $\ker \mathcal{L}^*$ |

---

## Extensions

| Topic | Where It Fits | Document |
|-------|---------------|----------|
| **Feynman–Kac** | Backward + potential/killing | [Feynman–Kac Formula](feynman_kac.md) |
| **Martingale Problem** | Generator characterization | [Stroock–Varadhan](../diffusion_process/martingale_problem_stroock_varadhan.md) |
| **Score Functions** | Forward + ML | [Fokker–Planck](fokker_planck.md#connection-to-score-functions-advanced) |
| **Time Reversal** | Forward + backward combined | [Time Reversal](../diffusion_process/time_reversal_of_diffusions.md) |

---

## One-Sentence Summary

!!! quote "The Conceptual Chain"
    **The generator defines the local law; the backward equation evolves expectations; Dynkin weakens this to an integral identity; the forward equation evolves distributions; stationarity studies their long-time fixed points.**

---

## Document Map

### Section 2.7: Generator (Probabilistic)

| Document | Focus |
|----------|-------|
| [Infinitesimal Generator](infinitesimal_generator.md) | Definition, properties, examples |
| [Dynkin's Formula](dynkin_formula.md) | Integral form, applications |
| [Generator and Martingales](generator_and_martingales.md) | Dynkin martingale, harmonic functions |
| [Applications of Dynkin](applications_of_dynkin.md) | Exit times, boundary problems |

### Section 2.8: Generator (PDE)

| Document | Focus |
|----------|-------|
| [Kolmogorov Backward](kolmogorov_backward.md) | $\partial_t u = \mathcal{L}u$ |
| [Fokker–Planck](fokker_planck.md) | $\partial_t p = \mathcal{L}^* p$ |
| [Feynman–Kac](feynman_kac.md) | Discounting, killing, potential |
