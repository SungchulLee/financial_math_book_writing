# Characteristic Functions


A major reason stochastic volatility models (especially affine models like Heston) are practical is that many admit **closed-form characteristic functions** of the log-price. These characteristic functions enable efficient pricing, calibration, and risk computation via Fourier techniques.

---

## Definition


For a random variable \(X\) (typically log-price), the **characteristic function** is

\[
\varphi_X(u) = \mathbb{E}\big[e^{iuX}\big], \qquad u\in\mathbb{R}.
\]



In a time-dependent setting, we often use the conditional characteristic function:

\[
\varphi(t,x;T,u) = \mathbb{E}\left[e^{iuX_T}\mid X_t=x\right].
\]



---

## Why characteristic functions are useful


Characteristic functions help because:

- Fourier inversion recovers densities and distribution functions,
- expectations of payoffs can be expressed as integrals of \(\varphi\),
- in affine models, \(\varphi\) has semi-closed form.

Computationally, evaluating \(\varphi\) is often cheaper and more stable than simulating paths.

---

## Affine exponential form


In many stochastic volatility models, \(\varphi\) has an exponential-affine structure:

\[
\mathbb{E}\left[e^{iuX_T}\mid \mathcal{F}_t\right]
= \exp\Big(A(\tau,u) + B(\tau,u)V_t + iuX_t\Big),
\qquad \tau=T-t,
\]


where \(A\) and \(B\) solve ODEs (often Riccati equations).

Heston is the canonical example.

---

## Risk-neutral drift and discounting


Under \(\mathbb{Q}\), discounted prices must be martingales:

\[
\mathbb{E}^{\mathbb{Q}}\left[e^{-r(T-t)}S_T\mid\mathcal{F}_t\right] = S_t e^{-q(T-t)}.
\]



This condition determines the drift of \(X_t\) (log-price) and must be consistent with the characteristic function used for pricing.

---

## Practical notes


- Characteristic functions may have multiple algebraic forms; numerical stability can depend on the chosen representation.
- Care is needed with complex logarithms, branch cuts, and cancellation errors (notably in Heston).
- For calibration, one often needs stable evaluation for many \((K,T)\) points.

---

## Key takeaways


- Characteristic functions are central to practical stochastic volatility pricing.
- Affine structure yields exponential-affine characteristic functions.
- Stable numerical evaluation matters as much as closed-form availability.

---

## Further reading


- Heston (1993) and subsequent numerical stability refinements.
- Carr & Madan (1999), FFT pricing.
- Duffie, Pan & Singleton (2000), affine jump diffusions.
