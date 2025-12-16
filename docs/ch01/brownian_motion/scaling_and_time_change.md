# Scaling and Time Change

## Brownian scaling

Let \(\{W_t\}_{t\ge 0}\) be a standard Brownian motion in \(\mathbb{R}^d\). For any constant \(c>0\), define

\[
\widetilde{W}_t := \frac{1}{\sqrt{c}}\,W_{ct}, \qquad t\ge 0.
\]

Then \(\{\widetilde{W}_t\}_{t\ge 0}\) is again a standard Brownian motion (in distribution, and in fact as a process).

To verify this, note that
 
\[
\widetilde{W}_t-\widetilde{W}_s = \frac{1}{\sqrt{c}}\left(W_{ct}-W_{cs}\right)\sim \mathcal{N}\!\left(0,(t-s)I_d\right)
\]

since \(W_{ct}-W_{cs}\sim \mathcal{N}(0,c(t-s)I_d)\).
We leave the details to the reader.

Hence we write the **self-similarity (scaling) property**

\[
\boxed{
\{W_{ct}\}_{t\ge 0}\;\overset{d}{=}\;\{\sqrt{c}\,W_t\}_{t\ge 0}.
}
\]

---

## Consequences of scaling

### Typical size of increments
For small \(\Delta t>0\),

\[
W_{t+\Delta t}-W_t \sim \mathcal{N}(0,\Delta t),
\qquad
\mathbb{E}\!\left[|W_{t+\Delta t}-W_t|^2\right]=\Delta t,
\]

so the “typical magnitude” is of order \(\sqrt{\Delta t}\). This scaling is the source of the Itô correction terms.

### No intrinsic time scale
Scaling shows Brownian motion has no preferred time scale: zooming in on time by a factor \(c\) is equivalent (in law) to zooming out in space by \(\sqrt{c}\).

---

## Time change (deterministic)

Let \(\phi:[0,\infty)\to[0,\infty)\) be nondecreasing, continuous, with \(\phi(0)=0\). Define

\[
B_t := W_{\phi(t)}.
\]

Then \(\{B_t\}\) is a continuous Gaussian process with

\[
\mathbb{E}[B_t]=0,
\qquad
\mathrm{Cov}(B_s,B_t)=\min(\phi(s),\phi(t)).
\]

In general, \(\{B_t\}\) is **not** Brownian motion in time \(t\) unless \(\phi(t)=t\), because increments are not stationary with respect to \(t\).

However, if \(\phi\) is linear, \(\phi(t)=ct\), then

\[
W_{\phi(t)} = W_{ct} \;\overset{d}{=}\; \sqrt{c}\,W_t,
\]

which is Brownian up to a spatial scaling.

---

## Time change (random): quadratic variation clock

One of the most important time-change ideas is that a continuous local martingale can be parameterized by its quadratic variation.

Let \(M=\{M_t\}_{t\ge 0}\) be a continuous local martingale with \(M_0=0\), and define its quadratic variation \(\langle M\rangle_t\). When \(\langle M\rangle_t\) is strictly increasing, define the right-continuous inverse

\[
\tau(u) := \inf\{t\ge 0:\langle M\rangle_t>u\}, \qquad u\ge 0.
\]

Then the time-changed process \(\{M_{\tau(u)}\}_{u\ge 0}\) has quadratic variation \(u\).

A fundamental theorem (stated here; proved later in martingale theory) is the **Dambis–Dubins–Schwarz theorem**:

\[
\boxed{
\text{There exists a Brownian motion \(\{B_u\}_{u\ge 0}\) such that }
M_t = B_{\langle M\rangle_t},\quad t\ge 0.
}
\]

This result explains why Brownian motion is universal among continuous martingales: every continuous local martingale is a Brownian motion run on a random clock \(\langle M\rangle_t\).

---

## Link to stochastic integration

For an Itô integral

\[
M_t := \int_0^t H_s\,\mathrm{d}W_s,
\]

we have

\[
\langle M\rangle_t = \int_0^t H_s^2\,\mathrm{d}s,
\]

so \(M_t\) is a Brownian motion under the clock \(\int_0^t H_s^2\,\mathrm{d}s\) (in the sense of Dambis–Dubins–Schwarz).
