# The Black-Scholes Formula & Hedging

!!! info "Source"
    **The Basics of Financial Mathematics** by Richard F. Bass, University of Connecticut, Spring 2003.
    These notes are used for educational purposes.

## 20. Black-Scholes Formula, I

20. Black-Scholes formula, I.
We can now derive the formula for the price of any option. Let T ≥0 be a fixed
real. If V is FT measurable, we have by Theorem 19.1 that
V = c +
Z T
KsdPs,
(20.1)
and under P, the process Ps is a martingale.
Theorem 20.1. The price of V must be E V .
Proof. This is the “no arbitrage” principle again. Suppose the price of the option V at
time 0 is W. Starting with 0 dollars, we can sell the option V for W dollars, and use the
W dollars to buy and trade shares of the stock. In fact, if we use c of those dollars, and
invest according to the strategy of holding Ks shares at time s, then at time T we will
have
erT (W0 −c) + V
dollars. At time T the buyer of our option exercises it and we use V dollars to meet that
obligation. That leaves us a profit of erT (W0 −c) if W0 > c, without any risk. Therefore
W0 must be less than or equal to c. If W0 < c, we just reverse things: we buy the option
instead of sell it, and hold −Ks shares of stock at time s. By the same argument, since
we can’t get a riskless profit, we must have W0 ≥c, or W0 = c.
Finally, under P the process Pt is a martingale. So taking expectations in (20.1),
we obtain
E V = c.
The formula in the statement of Theorem 20.1. is amenable to calculation. Suppose
we have the standard European option, where
V = e−rt(St −K)+ = (e−rtSt −e−rtK)+ = (Pt −e−rtK)+.
Recall that under P the stock price satisfies
dPt = σPtdf
Wt,
where f
Wt is a Brownian motion under P. So then
Pt = P0eσ e
Wt−σ2t/2.
Hence
E V = E [(PT −e−rT K)+]
(20.2)
= E [(P0eσ e
WT −(σ2/2)T −e−rT K)+].
We know the density of f
WT is just (2πT)−1/2e−y2/(2T ), so we can do some calculations
(see Note 1) and end up with the famous Black-Scholes formula:
W0 = xΦ(g(x, T)) −Ke−rT Φ(h(x, T)),
where Φ(z) =
√
2π
R z
−∞e−y2/2 dy, x = P0 = S0,
g(x, T) = log(x/K) + (r + σ2/2)T
σ
√
T
,
h(x, T) = g(x, T) −σ
√
T.
It is of considerable interest that the final formula depends on σ but is completely
independent of µ. The reason for that can be explained as follows. Under P the process Pt
satisfies dPt = σPtdf
Wt, where f
Wt is a Brownian motion. Therefore, similarly to formulas
we have already done,
Pt = P0eσ e
Wt−σ2t/2,
and there is no µ present here. (We used the Girsanov formula to get rid of the µ.) The
price of the option V is
E [PT −e−rT K]+,
(20.3)
which is independent of µ since Pt is.
Note 1. We want to calculate
E
h
(xeσ e
WT −σ2T/2 −e−rT K)+i
,
(20.4)
where f
Wt is a Brownian motion under P and we write x for P0 = S0. Since f
WT is a normal
random vairable with mean 0 and variance T, we can write it as
√
TZ, where Z is a standard
mean 0 variance 1 normal random variable.
Now
xeσ
√
T Z−σ2T/2 > e−rT K
if and only if
log x + σ
√
TZ −σ2T/2 > −r + log K,
or if
Z > (σ2T/2) −r + log K −log x.
We write z0 for the right hand side of the above inequality. Recall that 1 −Φ(z) = Φ(−z) for
all z by the symmetry of the normal density. So (20.4) is equal to
√
2π
Z ∞
z0
(xeσ
√
T z−σ2T/2 −e−rT K)+e−z2/2dz
= x
√
2π
Z ∞
z0
e−1
2 (z2−2σ
√
T z+σ2T dz −Ke−rT
√
2π
Z ∞
z0
e−z2/2dz
= x
√
2π
Z ∞
z0
e−1
2 (z−σ
√
T )2dz −Ke−rT (1 −Φ(z0))
= x
√
2π
Z ∞
z0−σ
√
T
e−y2/2dy −Ke−rT Φ(−z0)
= x(1 −Φ(z0 −σ
√
T)) −Ke−rT Φ(−z0)
= xΦ(σ
√
T −z0) −Ke−rT Φ(−z0).
This is the Black-Scholes formula if we observe that σ
√
T −z0 = g(x, T) and −z0 = h(x, T).


## 21. Hedging Strategies

21. Hedging strategies.
The previous section allows us to compute the value of any option, but we would also
like to know what the hedging strategy is. This means, if we know V = E V +
R T
0 HsdSs,
what should Hs be? This might be important to know if we wanted to duplicate an option
that was not available in the marketplace, or if we worked for a bank and wanted to provide
an option for sale.
It is not always possible to compute H, but in many cases of interest it is possible.
We illustrate one technique with two examples.
First, suppose we want to hedge the standard European call V = e−rT (ST −K)+ =
(PT −e−rT K)+. We are working here with the risk-neutral probability only. It turns out
it makes no difference: the definition of
R t
0 HsdXs for a semimartingale X does not depend
on the probability P, other than worrying about some integrability conditions.
We can rewrite V as
V = E V + g(f
WT ),
where
g(x) = (eσx−σ2T/2 −e−rT K)+ −E V.
Therefore the expectation of g(f
WT ) is 0. Recall that under P, f
W is a Brownian motion.
If we write g(f
WT ) as
Z T
Hsdf
Ws,
(21.1)
then since dPt = σPtdf
Wt, we have
g(f
WT ) = c +
Z T
1
σPs
HsdPs.
(21.2)
Therefore it suffices to find the representation of the form (21.1).
Recall from the section on the Markov property that
Ptf(x) = E
xf(f
Wt) = E f(x + f
Wt) =
Z
√
2πte−(y)2/2tf(x + y)dy.
Let Mt = E [g(f
WT ) | Ft]. By Proposition 4.3, we know that Mt is a martingale. By the
Markov property Proposition 17.2, we see that
Mt = E e
Wt[g(f
WT −t] = PT −tg(f
Wt).
(21.3)
Now let us apply Ito’s formula with the function f(x1, x2) = Px2g(x1) to the process
Xt = (X1
t , X2
t ) = (f
Wt, T −t). So we need to use the multidimensional version of Ito’s
formula. We have dX1
t = df
Wt and dX2
t = −dt. Since X2
t is a decreasing process and has
no martingale part, then d⟨X2⟩t = 0 and d⟨X1, X2⟩t = 0, while d⟨X1⟩t = dt. Ito’s formula
says that
f(X1
t , X2
t ) = f(X1
0, X2
0) +
Z t
2
X
i=1
∂f
∂xi
(Xt)dXi
t
+ 1
Z t
2
X
i,j=1
∂2f
∂xi∂xj
(Xt)d⟨Xi, Xj⟩t
= c +
Z t
∂f
∂x1
(Xt)df
Wt + some terms with dt.
But we know that f(Xt) = PT −tg(f
Wt) = Mt is a martingale, so the sum of the terms
involving dt must be zero; if not, f(Xt) would have a bounded variation part. We conclude
Mt =
Z t
∂
∂xPT −sg(f
Ws)df
Ws.
If we take t = T, we then have
g(f
WT ) = MT =
Z T
∂
∂xPT −sg(f
Ws)df
Ws,
and we have our representation.
For a second example, let’s look at the sell-high option. Here the payoffis sups≤T Ss,
the largest the stock price ever is up to time T. This is FT measurable, so we can compute
its value. How can one get the equivalent outcome without looking into the future?
For simplicity, let us suppose the interest rate r is 0.
Let Nt = sups≤t Ss, the
maximum up to time t. It is not the case that Nt is a Markov process. Intuitively, the
reasoning goes like this: suppose the maximum up to time 1 is $100, and we want to
predict the maximum up to time 2. If the stock price at time 1 is close to $100, then we
have one prediction, while if the stock price at time 1 is close to $2, we would definitely
have another prediction. So the prediction for N2 does not depend just on N1, but also
the stock price at time 1. This same intuitive reasoning does suggest, however, that the
triple Zt = (St, Nt, t) is a Markov process, and this turns out to be correct. Adding in the
information about the current stock price gives a certain amount of evidence to predict
the future values of Nt; adding in the history of the stock prices up to time t gives no
additional information.
Once we believe this, the rest of the argument is very similar to the first example.
Let Puf(z) = E
zf(Zu), where z = (s, n, t). Let g(Zt) = Nt −E NT . Then
Mt = E [g(ZT ) | Ft] = E
Zt[g(ZT −t)] = PT −tg(Zt).
We then let f(s, n, t) = PT −tg(s, n, t) and apply Ito’s formula. The process Nt is always
increasing, so has no martingale part, and hence ⟨N⟩t = 0. When we apply Ito’s formula,
we get a dSt term, which is the martingale term, we get some terms involving dt, which are
of bounded variation, and we get a term involving dNt, which is also of bounded variation.
But Mt is a martingale, so all the dt and dNt terms must cancel. Therefore we should be
left with the martingale term, which is
Z t
∂
∂sPT −sg(Ss, Ns, s)dSs,
where again g(s, n, t) = n. This gives us our hedging strategy for the sell-high option, and
it can be explicitly calculated.
There is another way to calculate hedging strategies, using what is known as the
Clark-Haussmann-Ocone formula. This is a more complicated procedure, and most cases
can be done as well by an appropriate use of the Markov property.


## 22. Black-Scholes Formula, II

22. Black-Scholes formula, II.
Here is a second approach to the Black-Scholes formula. This approach works for
European calls and several other options, but does not work in the generality that the
first approach does. On the other hand, it allows one to compute more easily what the
equivalent strategy of buying or selling stock should be to duplicate the outcome of the
given option. In this section we work with the actual price of the stock instead of the
present value.
Let Vt be the value of the portfolio and assume Vt = f(St, T −t) for all t, where f
is some function that is sufficiently smooth. We also want VT = (ST −K)+.
Recall Ito’s formula. The multivariate version is
f(Xt) = f(X0) +
Z t
d
X
i=1
fxi(Xs) dXi
s + 1
Z t
d
X
i,j=1
fxixj(Xs) d⟨Xi, Xj⟩s.
Here Xt = (X1
t , . . . , Xd
t ) and fxi denotes the partial derivative of f in the xi direction,
and similarly for the second partial derivatives.
We apply this with d = 2 and Xt = (St, T −t). From the SDE that St solves,
d⟨X1⟩t = σ2S2
t dt, ⟨X2⟩t = 0 (since T −t is of bounded variation and hence has no
martingale part), and ⟨X1, X2⟩t = 0. Also, dX2
t = −dt. Then
Vt −V0 = f(St, T −t) −f(S0, T)
(22.1)
=
Z t
fx(Su, T −u) dSu −
Z t
fs(Su, T −u) du
+ 1
Z t
σ2S2
ufxx(Su, T −u) du.
On the other hand, if au and bu are the number of shares of stock and bonds, respectively,
held at time u,
Vt −V0 =
Z t
au dSu +
Z t
bu dβu.
(22.2)
This formula says that the increase in net worth is given by the profit we obtain by holding
au shares of stock and bu bonds at time u. Since the value of the portfolio at time t is
Vt = atSt + btβt,
we must have
bt = (Vt −atSt)/βt.
(22.3)
Also, recall
βt = β0ert.
(22.4)
To match up (22.2) with (22.1), we must therefore have
at = fx(St, T −t)
(22.5)
and
r[f(St, T −t) −Stfx(St, T −t)] = −fs(St, T −t) + 1
2σ2S2
t fxx(St, T −t)
(22.6)
for all t and all St. (22.6) leads to the parabolic PDE
fs = 1
2σ2x2fxx + rxfx −rf,
(x, s) ∈(0, ∞) × [0, T),
(22.7)
and
f(x, 0) = (x −K)+.
(22.8)
Solving this equation for f, f(x, T) is what V0 should be, i.e., the cost of setting up the
equivalent portfolio. Equation (22.5) shows what the trading strategy should be.


## 23. The Fundamental Theorem of Finance

23. The fundamental theorem of finance.
In Section 19, we showed there was a probability measure under which Pt = e−rtSt
was a martingale. This is true very generally. Let St be the price of a security in today’s
dollars.
We will suppose St is a continuous semimartingale, and can be written St =
Mt + At.
Arbitrage means that there is a trading strategy Hs such that there is no chance that
we lose anything and there is a positive profit with positive probability. Mathematically,
arbitrage exists if there exists Hs that is adapted and satisfies a suitable integrability
condition with
Z T
HsdSs ≥0,
a.s.
and
P
 Z T
HsdSs > b

> ε
for some b, ε > 0. It turns out that to get a necessary and sufficient condition for St to be
a martingale, we need a slightly weaker condition.
The NFLVR condition (“no free lunch with vanishing risk”) is that there do not
exist a fixed time T, ε, b > 0, and Hn (that are adapted and satisfy the appropriate
integrability conditions) such that
Z T
Hn(s) dSs > −1
n,
a.s.
for all t and
P
 Z T
Hn(s) dSs > b

> ε.
Here T, b, ε do not depend on n. The condition says that one can with positive
probability ε make a profit of b and with a loss no larger than 1/n.
Two probabilities P and Q are equivalent if P(A) = 0 if and only Q(A) = 0,
i.e., the two probabilities have the same collection of sets of probability zero. Q is an
equivalent martingale measure if Q is a probability measure, Q is equivalent to P, and St
is a martingale under Q.
Theorem 23.1. If St is a continuous semimartingale and the NFLVR conditions holds,
then there exists an equivalent martingale measure Q.
The proof is rather technical and involves some heavy-duty measure theory, so we
will only point examine a part of it. Suppose that we happened to have St = Wt + f(t),
where f(t) is a deterministic increasing continuous function.
To obtain the equivalent
martingale measure, we would want to let
Mt = e−R t
0 f ′(s)dWs−1
R t
0 (f ′(s))2ds.
In order for Mt to make sense, we need f to be differentiable. A result from measure
theory says that if f is not differentiable, then we can find a subset A of [0, ∞) such
that
R t
0 1A(s)ds = 0 but the amount of increase of f over the set A is positive. This last
statement is phrased mathematically by saying
Z t
1A(s)df(s) > 0,
where the integral is a Riemann-Stieltjes (or better, a Lebesgue-Stieltjes) integral. Then
if we hold Hs = 1A(s) shares at time s, our net profit is
Z t
HsdSs =
Z t
1A(s)dWs +
Z t
1A(s) df(s).
The second term would be positive since this is the amount of increase of f over the set
A. The first term is 0, since E (
R t
0 1A(s)dWs)2 =
R t
0 1A(s)2ds = 0. So our net profit is
nonrandom and positive, or in other words, we have made a net gain without risk. This
contradicts “no arbitrage.” See Note 1 for more on this.
Sometime Theorem 23.1 is called the first fundamental theorem of asset pricing.
The second fundamental theorem is the following.
Theorem 23.2. The equivalent martingale measure is unique if and only if the market is
complete.
We will not prove this.
Note 1.
We will not prove Theorem 23.1, but let us give a few more indications of what is
going on. First of all, recall the Cantor set. This is where E1 = [0, 1], E2 is the set obtained
from E1 by removing the open interval ( 1
3, 2
3), E3 is the set obtained from E2 by removing
the middle third from each of the two intervals making up E2, and so on. The intersection,
E = ∩∞
n=1En, is the Cantor set, and is closed, nonempty, in fact uncountable, yet it contains
no intervals. Also, the Lebesgue measure of A is 0. We set A = E. Let f be the Cantor-
Lebesgue function. This is the function that is equal to 0 on (−∞, 0], 1 on [1, ∞), equal to
2 on the interval [ 1
3, 2
3], equal to 1
4 on [ 1
9, 2
9], equal to 3
4 on [ 7
9, 8
9], and is defined similarly on
each interval making up the complement of A. It turns out we can define f on A so that it is
continuous, and one can show
R 1
0 1A(s)df(s) = 1. So this A and f provide a concrete example
of what we were discussing.


## 24. American Puts

24. American puts.
The proper valuation of American puts is one of the important unsolved problems
in mathematical finance. Recall that a European put pays out (K −ST )+ at time T,
while an American put allows one to exercise early. If one exercises an American put at
time t < T, one receives (K −St)+. Then during the period [t, T] one receives interest,
and the amount one has is (K −St)+er(T −t). In today’s dollars that is the equivalent of
(K −St)+e−rt. One wants to find a rule, known as the exercise policy, for when to exercise
the put, and then one wants to see what the value is for that policy. Since one cannot look
into the future, one is in fact looking for a stopping time τ that maximizes
E e−rτ(K −Sτ)+.
There is no good theoretical solution to finding the stopping time τ, although good
approximations exist. We will, however, discuss just a bit of the theory of optimal stopping,
which reworks the problem into another form.
Let Gt denote the amount you will receive at time t. For American puts, we set
Gt = e−rt(K −St)+.
Our problem is to maximize E Gτ over all stopping times τ.
We first need
Proposition 24.1. If S and T are bounded stopping times with S ≤T and M is a
martingale, then
E [MT | FS] = MS.
Proof. Let A ∈FS. Define U by
U(ω) =

S(ω)
if ω ∈A,
T(ω)
if ω /∈A.
It is easy to see that U is a stopping time, so by Doob’s optional stopping theorem,
E M0 = E MU = E [MS; A] + E [MT ; Ac].
Also,
E M0 = E MT = E [MT ; A] + E [MT ; Ac].
Taking the difference, E [MT ; A] = E [Ms; A], which is what we needed to show.
Given two supermartingales Xt and Yt, it is routine to check that Xt ∧Yt is also a
supermartingale. Also, if Xn
t are supermartingales with Xn
t ↓Xt, one can check that Xt
is again a supermartingale. With these facts, one can show that given a process such as
Gt, there is a least supermartingale larger than Gt.
So we define Wt to be a supermartingale (with respect to P, of course) such that
Wt ≥Gt a.s for each t and if Yt is another supermartingale with Yt ≥Gt for all t, then
Wt ≤Yt for all t. We set τ = inf{t : Wt = Gt}. We will show that τ is the solution to the
problem of finding the optimal stopping time. Of course, computing Wt and τ is another
problem entirely.
Let
Tt = {τ : τ is a stopping time, t ≤τ ≤T}.
Let
Vt = sup
τ∈Tt
E [Gτ | Ft].
Proposition 24.2. Vt is a supermartingale and Vt ≥Gt for all t.
Proof. The fixed time t is a stopping time in Tt, so Vt ≥E [Gt | Ft] = Gt, or Vt ≥Gt. so
we only need to show that Vt is a supermartingale.
Suppose s < t.
Let π be the stopping time in Tt for which Vt = E [Gπ | Ft].
π ∈Tt ⊂Ts. Then
E [Vt | Fs] = E [Gπ | Fs] ≤sup
τ∈Ts
E [Gτ | Fs] = Vs.
Proposition 24.3. If Yt is a supermartingale with Yt ≥Gt for all t, then Yt ≥Vt.
Proof. If τ ∈Tt, then since Yt is a supermartingale, we have
E [Yτ | Ft] ≤Yt.
So
Vt = sup
τ∈Tt
E [Gτ | Ft] ≤sup
τ∈Tt
E [Yτ | Ft] ≤Yt.
What we have shown is that Wt is equal to Vt. It remains to show that τ is optimal.
There may in fact be more than one optimal time, but in any case τ is one of them. Recall
we have F0 is the σ-field generated by S0, and hence consists of only ∅and Ω.
Proposition 24.4. τ is an optimal stopping time.
Proof. Since F0 is trivial, V0 = supτ∈T0 E [Gτ | F0] = supτ E [Gτ]. Let σ be a stopping
time where the supremum is attained. Then
V0 ≥E [Vσ | F0] = E [Vσ] ≥E [Gσ] = V0.
Therefore all the inequalities must be equalities. Since Vσ ≥Gσ, we must have Vσ = Gσ.
Since τ was the first time that Wt equals Gt and Wt = Vt, we see that τ ≤σ. Then
E [Gτ] = E [Vτ] ≥EVσ = E Gσ.
Therefore the expected value of Gτ is as least as large as the expected value of Gσ, and
hence τ is also an optimal stopping time.
The above representation of the optimal stopping problem may seem rather bizarre.
However, this procedure gives good usable results for some optimal stopping problems. An
example is where Gt is a function of just Wt.

