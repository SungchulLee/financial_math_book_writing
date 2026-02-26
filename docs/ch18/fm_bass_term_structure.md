# Term Structure & Interest Rate Models

!!! info "Source"
    **The Basics of Financial Mathematics** by Richard F. Bass, University of Connecticut, Spring 2003.
    These notes are used for educational purposes.

## 25. Term Structure

25. Term structure.
We now want to consider the case where the interest rate is nondeterministic, that
is, it has a random component. To do so, we take another look at option pricing.
Accumulation factor. Let r(t) be the (random) interest rate at time t. Let
β(t) = e
R t
0 r(u)du
be the accumulation factor. One dollar at time T will be worth 1/β(T) in today’s dollars.
Let V = (ST −K)+ be the payoffon the standard European call option at time T
with strike price K, where St is the stock price. In today’s dollars it is worth, as we have
seen, V/β(T). Therefore the price of the option should be
E
h V
β(T)
i
.
We can also get an expression for the value of the option at time t. The payoff, in terms
of dollars at time t, should be the payoffat time T discounted by the interest or inflation
rate, and so should be
e−R T
t
r(u)du(ST −K)+.
Therefore the value at time t is
E
h
e−R T
t
r(u)du(ST −K)+ | Ft
i
= E
h β(t)
β(T)V | Ft
i
= β(t)E
h V
β(T) | Ft
i
.
From now on we assume we have already changed to the risk-neutral measure and
we write P instead of P.
Zero coupon. A zero coupon bond with maturity date T pays $1 at time T and nothing
before. This is equivalent to an option with payoffvalue V = 1. So its price at time t, as
above, should be
B(t, T) = β(t)E
h
β(T) | Ft
i
= E
h
e−R T
t
r(u)du | Ft
i
.
Let’s derive the SDE satisfied by B(t, T). Let Nt = E [1/β(T) | Ft]. This is a
martingale. By the martingale representation theorem,
Nt = E [1/β(T)] +
Z t
HsdWs
for some adapted integrand Hs. So B(t, T) = β(t)Nt. Here T is fixed. By Ito’s product
formula,
dB(t, T) = β(t)dNt + Ntdβ(t)
= β(t)HtdWt + Ntr(t)β(t)dt
= β(t)HtdWt + B(t, T)r(t)dt,
and we thus have
dB(t, T) = β(t)HtdWt + B(t, T)r(t)dt.
(25.1)
Forward rates. We now discuss forward rates. If one holds T fixed and graphs B(t, T) as
a function of t, the graph will not clearly show the behavior of r. One sometimes specifies
interest rates by what are known as forward rates.
Suppose we want to borrow $1 at time T and repay it with interest at time T + ε.
At the present time we are at time t ≤T. Let us try to accomplish this by buying a zero
coupon bond with maturity date T and shorting (i.e., selling) N zero coupon bonds with
maturity date T + ε. Our outlay of money at time t is
B(t, T) −NB(t, T + ε) = 0.
If we set
N = B(t, T)/B(t, T + ε),
our outlay at time t is 0. At time T we receive $1. At time T +ε we pay B(t, T)/B(t, T +ε).
The effective rate of interest R over the time period T to T + ε is
eεR =
B(t, T)
B(t, T + ε).
Solving for R, we have
R = log B(t, T) −log B(t, T + ε)
ε
.
We now let ε →0. We define the forward rate by
f(t, T) = −∂
∂T log B(t, T).
(25.2)
Sometimes interest rates are specified by giving f(t, T) instead of B(t, T) or r(t).
Recovering B from f. Let us see how to recover B(t, T) from f(t, T). Integrating, we have
Z T
t
f(t, u)du = −
Z T
t
∂
∂u log B(t, u)du = −log B(t, u) |u=T
u=t
= −log B(t, T) + log B(t, t).
Since B(t, t) is the value of a zero coupon bond at time t which expires at time t, it is
equal to 1, and its log is 0. Solving for B(t, T), we have
B(t, T) = e−R T
t
f(t,u)du.
(25.3)
Recovering r from f. Next, let us show how to recover r(t) from the forward rates. We
have
B(t, T) = E
h
e−R T
t
r(u)du | Ft
i
.
Differentiating,
∂
∂T B(t, T) = E
h
−r(T)e−R T
t
r(u)du | Ft
i
.
Evaluating this when T = t, we obtain
E [−r(t) | Ft] = −r(t).
(25.4)
On the other hand, from (25.3) we have
∂
∂T B(t, T) = −f(t, T)e−R T
t
f(t,u)du.
Setting T = t we obtain −f(t, t). Comparing with (25.4) yields
r(t) = f(t, t).
(25.5)


## 26. Some Interest Rate Models

26. Some interest rate models.
Heath-Jarrow-Morton model
Instead of specifying r, the Heath-Jarrow-Morton model (HJM) specifies the forward
rates:
df(t, T) = σ(t, T)dWt + α(t, T)dt.
(26.1)
Let us derive the SDE that B(t, T) satisfies. Let
α∗(t, T) =
Z T
t
α(t, u)du,
σ∗(t, T) =
Z T
t
σ(t, u)du.
Since B(t, T) = exp(−
R T
t f(t, u)du), we derive the SDE for B by using Ito’s formula with
the function ex and Xt = −
R T
t f(t, u)du. We have
dXt = f(t, t)dt −
Z T
t
df(t, u)du
= r(t)dt −
Z T
t
[α(t, u)dt + σ(t, u)dWt] du
= r(t)dt −
h Z T
t
α(t, u)du
i
dt −
h Z T
t
σ(t, u)du
i
dWt
= r(t)dt −α∗(t, T)dt −σ∗(t, T)dWt.
Therefore, using Ito’s formula,
dB(t, T) = B(t, T)dXt + 1
2B(t, T)(σ∗(t, T))2dt
= B(t, T)
h
r(t) −α∗+ 1
2(σ∗)2i
dt −σ∗B(t, T)dWt.
From (25.1) we know the dt term must be B(t, T)r(t)dt, hence
dB(t, T) = B(t, T)r(t)dt −σ∗B(t, T)dWt.
Comparing with (26.1), we see that if P is the risk-neutral measure, we have α∗= 1
2(σ∗)2.
See Note 1 for more on this.
Hull and White model
In this model, the interest rate r is specified as the solution to the SDE
dr(t) = σ(t)dWt + (a(t) −b(t)r(t))dt.
(26.2)
Here σ, a, b are deterministic functions. The stochastic integral term introduces random-
ness, while the a −br term causes a drift toward a(t)/b(t). (Note that if σ(t) = σ, a(t) =
a, b(t) = b are constants and σ = 0, then the solution to (26.2) becomes r(t) = a/b.)
(26.2) is one of those SDE’s that can be solved explicitly. Let K(t) =
R t
0 b(u)du.
Then
d
h
eK(t)r(t)
i
= eK(t)r(t)b(t)dt + eK(t)h
a(t) −b(t)r(t)
i
dt + eK(t)[σ(t)dWt]
= eK(t)a(t)dt + eK(t)[σ(t)dWt].
Integrating both sides,
eK(t)r(t) = r(0) +
Z t
eK(u)a(u)du +
Z t
eK(u)σ(u)dWu.
Multiplying both sides by e−K(t), we have the explicit solution
r(t) = e−K(t)h
r(0) +
Z t
eK(u)a(u)du +
Z t
eK(u)σ(u)dWu
i
.
If F(u) is deterministic, then
Z t
F(u)dWu = lim
X
F(ui)(Wui+1 −Wui).
From undergraduate probability, linear combinations of Gaussian r.v.’s (Gaussian = nor-
mal) are Gaussian, and also limits of Gaussian r.v.’s are Gaussian, so we conclude that the
r.v.
R t
0 F(u)dWu is Gaussian. We see that the mean at time t is
E r(t) = e−K(t)h
r(0) +
Z t
eK(u)a(u)du
i
.
We know how to calculate the second moment of a stochastic integral, so
Var r(t) = e−2K(t)
Z t
e2K(u)σ(u)2du.
(One can similarly calculate the covariance of r(s) and r(t).) Limits of linear combinations
of Gaussians are Gaussian, so we can calculate the mean and variance of
R T
0 r(t)dt and get
an explicit expression for
B(0, T) = E e−R T
0 r(u)du.
Cox-Ingersoll-Ross model
One drawback of the Hull and White model is that since r(t) is Gaussian, it can take
negative values with positive probability, which doesn’t make sense. The Cox-Ingersoll-
Ross model avoids this by modeling r by the SDE
dr(t) = (a −br(t))dt + σ
p
r(t)dWt.
The difference from the Hull and White model is the square root of r in the stochastic
integral term. This square root term implies that when r(t) is small, the fluctuations in
r(t) are larger than they are in the Hull and White model. Provided a ≥1
2σ2, it can be
shown that r(t) will never hit 0 and will always be positive. Although one cannot solve
for r explicitly, one can calculate the distribution of r. It turns out to be related to the
square of what are known in probability theory as Bessel processes. (The density of r(t),
for example, will be given in terms of Bessel functions.)
Note 1. If P is not the risk-neutral measure, it is still possible that one exists. Let θ(t) be a
function of t, let Mt = exp(−
R t
0 θ(u)dWu −1
R t
0 θ(u)2du) and define P(A) = E [MT ; A] for
A ∈FT . By the Girsanov theorem,
dB(t, T) = B(t, T)
h
r(t) −α∗+ 1
2(σ∗)2 + σ∗θ]dt −σ∗B(t, T)df
Wt,
where f
Wt is a Brownian motion under P. Again, comparing this with (25.1) we must have
α∗= 1
2(σ∗)2 + σ∗θ.
Differentiating with respect to T, we obtain
α(t, T) = σ(t, T)σ∗(t, T) + σ(t, T)θ(t).
If we try to solve this equation for θ, there is no reason off-hand that θ depends only on t and
not T. However, if θ does not depend on T, P will be the risk-neutral measure.

