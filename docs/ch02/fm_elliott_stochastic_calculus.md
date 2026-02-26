# Continuous-Time Stochastic Calculus

!!! info "Source"
    **Mathematics of Financial Markets** by Robert J. Elliott and P. Ekkehard Kopp, Springer, 2nd ed., 2005.
    These notes are used for educational purposes.

## Review of Continuous-Time Stochastic Calculus

124
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
5.5
Pricing and Hedging American Options
Existence of a Minimal Hedge
Return to the setup at the beginning of Section 5.4 and assume henceforth
that the market model (Ω, F, P, T, F, S) is viable and complete, with Q as
the unique EMM.
Given an American option (ft) in this model (e.g. , an American call
with strike K, where ft = (S1
t −K)+), we saw that a hedging strategy θ
would need to generate a value process V (θ) that satisfies (5.19); that is,
VT (θ) = fT ,
Vt−1(θ) = max

ft−1, (1 + r)−1EQ (Vt |Ft−1 )

for t = 1, 2, . . . , T,
since S0
t = (1+r)−t for all t ∈T. Moving to discounted values, Z =

V t(θ)

is then the Snell envelope of the discounted option price f t = (1 + r)−tft,
so that
ZT = f T ,
Zt−1 = max

f t−1, EQ

V t |Ft−1

for t = 1, 2, . . . , T.
In particular, the results of the previous section yield
Zt = sup
τ∈Tt
EQ

f τ |Ft

for t ∈T,
(5.26)
and the stopping time τ ∗
t = min

s ≥t : Zs = f s

is optimal, so that the
supremum in (5.26) is attained by τ ∗
t .
(We developed these results for
t = 0, but with the extended definition of the Snell envelope, they hold for
general t.)
For τ ∗= τ ∗
0 and T = T0, we have, therefore,
Z0 = sup
τ∈T
EQ

f τ

= EQ

f τ ∗

.
(5.27)
This defines the rational price of the option at time 0 and thus also the
initial investment needed for the existence of a hedging strategy.
Now write the Doob decomposition of the supermartingale Z as Z =
M −A, where M is a martingale and A a predictable increasing process.
Also write Mt = S0
t M t and At = S0
t At.
Since the market is complete, we can attain the contingent claim MT by
a self-financing strategy θ (e.g. , we could use the strategy constructed by
means of the martingale representation in the proof of Proposition 4.1.1)
and we may assume that θ is admissible. Thus V t(θ) = M t, and as V (θ)
is a martingale under the EMM Q,
V t(θ) = M t = Zt + At for all t ∈T.
Hence also
ZtS0
t = Vt(θ) −At for t ∈T.
(5.28)

5.5. PRICING AND HEDGING AMERICAN OPTIONS
125
From the results of the previous section, we know that on the set
C = {(t, ω) : 0 ≤t < τ ∗(ω)} ,
the Snell envelope Z is a martingale and At(ω) = 0 on this set. Hence
Vt(θ)(ω) =
sup
t≤τ≤T
EQ

(1 + r)−(τ−t)fτ |Ft

for all (t, ω) ∈C.
(5.29)
We saw that τ ∗is the smallest optimal exercise time and that Aτ ∗(ω)(ω) =
0. Hence (5.28) and (5.29) imply that
Vτ ∗(ω)(θ)(ω) = Zτ ∗(ω)(ω)S0
τ ∗(ω)(ω) = fτ ∗(ω)(ω).
(5.30)
Thus the hedge θ with initial capital investment
V0(θ) = x = sup
τ∈T
EQ

(1 + r)−τfτ

(5.31)
is minimal. Thus we have verified that this condition is sufficient for the
existence of a minimal hedge for the option.
The Rational Price and Optimal Exercise
Hedging requires an initial investment x of at least supτ∈T EQ ((1 + r)−τfτ),
and the supremum is attained at the optimal time τ ∗. It follows that x is
the minimum initial investment for which a hedging strategy can be con-
structed. Thus (5.31) provides a natural choice for the ‘fair’ or rational
price of the American option.
The optimal exercise time need not be uniquely defined, however; any
optimal stopping time (under Q) for the payofffunction ft will be an op-
timal exercise time. In fact, the holder of the option (the buyer) has no
incentive to exercise the option while ZtS0
t > ft since using the option price
as initial investment he could create a portfolio yielding greater payoffthan
the option at time τ by using the hedging strategy θ. Thus the buyer would
wait for a stopping time σ for which Zσ = f σ; that is, until the optimality
criterion in Proposition 5.4.5 is satisfied. However, he would also choose
σ ≤ν, where ν is the largest optimal stopping time defined in (5.24), since
otherwise the strategy θ would, at times greater than t > ν, yield value
Vt(θ) > ZtS0
t by (5.28). Thus, for any optimal exercise time σ, we need to
have Zt∧σ = V t∧σ, so that Zσ is a martingale. This means that the second
condition in Proposition 5.4.5 holds, so that σ is optimal for the stopping
problem solved by the Snell envelope. (Note that the same considerations
apply to the option writer: if the buyer exercises at a non-optimal time τ,
the strategy θ provides an arbitrage opportunity for the option writer since
either Aτ > 0 or Zτ > f τ, so that Vτ(θ) −fτ = ZτS0
τ + Aτ −fτ > 0.)
We have proved the following theorem.

126
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
Theorem 5.5.1. A stopping time ˆτ ∈T is an optimal exercise time for
the American option (ft)t∈T if and only if
EQ

(1 + r)−ˆτfˆτ

= sup
τ∈T
EQ

(1 + r)−τfτ

.
(5.32)
Remark 5.5.2. We showed by an arbitrage argument in Chapter 1 that
American options are more valuable than their European counterparts in
general but that for a simple call option there is no advantage in early
exercise, so that the American and European call options have the same
value. Using the theory of optimal stopping, we can recover these results
from the martingale properties of the Snell envelope. Indeed, if ft = (S1
t −
K)+ is an American call option with strike K on T, then its discounted
value process is given by the Q-supermartingale (Zt) as in (5.26). Now if
Ct is the discounted time t value of the European option CT = (S1
T −K)+,
then CT = fT , so that
Zt ≥EQ (ZT |Ft ) = EQ

f T |Ft

= EQ

CT |Ft

= Ct.
(5.33)
This shows that the value process of the American call option dominates
that of the European call option.
On the other hand, for these call options, we have Ct ≥ft = (S1
t −K)+,
as we saw in (1.23), and hence the Q-martingale (Ct) dominates (f t). It is
therefore a supermartingale dominating (f t) and, by the definition of the
Snell envelope, (Zt) is the smallest supermartingale with this property. We
conclude that Ct ≥Zt for all t ∈T. Hence Ct = Zt, and so the value
processes of the two options coincide.
5.6
Consumption-Investment Strategies
Extended ‘Self-Financing’ Strategies
In the study of American options in Chapter 8, and especially in studying
continuous-time consumption-investment problems in Chapter 10, we shall
extend the concept of ‘self-financing’ strategies by allowing for potential
consumption. In the present discrete-time setting, the basic concepts ap-
pear more transparent, and we outline them briefly here in preparation for
the technically more demanding discussion in Chapter 10.
Assume that we are given a price process

Si
t : i = 0, 1, . . . , d

t=0,1,...,T
on a stochastic basis (Ω, F, P, T, F). For any process X, the discounted
version is denoted by X, where Xt = βtXt as usual.
If c = (ct)t∈T denotes a ‘consumption process’ (which, if ct is nega-
tive, equates to additional investment at time t), then the self-financing
constraint for strategies (i.e., (∆θt) · St−1 = 0) should be amended to read
(∆θt) · St−1 + ct = 0.
(5.34)

5.6. CONSUMPTION-INVESTMENT STRATEGIES
127
An investment-consumption strategy is a pair (θ, c) of predictable processes
that satisfies (5.34), and their associated value or wealth process V is given
by Vt = θt · St as before. Also define the cumulative consumption process
C by Ct = t
u=1 cu. The constraint (5.34) is trivially equivalent to each
of the following (for all t > 0):
∆Vt = θt · ∆St −ct,
(5.35)
Vt = V0 +
t

u=1
θu · ∆Su −Ct,
(5.36)
V t = V0 +
t

u=1
θu · ∆Su −Ct.
(5.37)
Assume from now on that the market model (Ω, F, P, T, F, S) is viable
and complete and that Q is the unique EMM for S. Assume further that
C is a pure consumption process; that is, ∆Ct = ct ≥0 for all t ∈T. Then
for a strategy (θ, c) as previously, the discounted value process V satisfies,
for t ∈T,
EQ

∆V t |Ft−1

= EQ

(θt · ∆St −ct) |Ft−1

= −ct ≤0
since S is a Q-martingale and ct ≥0. In summary, we have the following.
Proposition 5.6.1. For every consumption strategy (θ, c) satisfying (5.34),
the discounted value process V is a Q-supermartingale.
Construction of Hedging Strategies
Suppose that U = (Ut) is an adapted process whose discounted version
U is a Q-supermartingale. Then we can use the increasing process in its
Doob decomposition to define a consumption process c and a self-financing
strategy θ such that the pair (θ, c) satisfies (5.34) and has value process U.
To do this, write U = M −A for the Doob decomposition of U, so
that A0 = 0 and M is a Q-martingale. As the market is complete, the
contingent claim MT = S0
T M T can be generated by a unique self-financing
strategy θ, so that θT · ST = MT ; that is, θT · StT = M T . As M is a
martingale, we have M t = EQ

θT · ST |Ft

for all t ∈T. Thus
U t = EQ

θT · ST |Ft

−At for t ∈T,
so that
Ut = S0
t EQ

θT · ST |Ft

−At for t ∈T,
where the process At = S0
t At is increasing and has A0 = 0. Since θ is
self-financing, the final portfolio value has the form
θT · ST = θ0 · S0 +
T

u=1
θu · ∆Su for t ∈T,

128
CHAPTER 5. DISCRETE-TIME AMERICAN OPTIONS
so that
EQ

θT · ST |Ft

= θ0 · S0 +
t

u=1
θu · ∆Su for t ∈T.
(5.38)
Choosing C so that At = t
u=1 cu and C0 = 0 = A0, we see that cu =
S0
u−1(∆Au) meets the requirement and that C is predictable and non-
negative (as A is increasing). Inductively, At = t
u=1 Cu yields
At+1 = At + ∆At+1 =
t+1

u=1
cu,
and by (5.37) we obtain V t = U t; that is, Vt = Ut for the value process
associated with (θ, c).
Guided by our discussion of American options, we now call a consump-
tion strategy (θ, c) a hedge for a given claim (i.e., an adapted process)
X = (Xt) if Vt(θ) ≥Xt for all t ∈T. Writing Z for the Snell envelope of
X, the supermartingale Z dominates Xand can be used as the process U
in the previous discussion. Thus we can find a hedging strategy (θ, c) for
X and obtain
Vt(θ) = Ut = S0
t Zt ≥Xt for t ∈T,
VT (θ) = S0
T ZT = XT .
As Z is the smallest supermartingale dominating X, it follows that any
hedge (θ′, c′) for X must have a value process dominating S0Z.
Financing Consumption
Suppose an investor is given an initial endowment x > 0 and follows a con-
sumption strategy c = (ct)t∈T (a non-negative predictable process). How
can this consumption be financed by a self-financing investment strategy
utilising the endowment x?
It seems natural to say that c can be financed (or is budget-feasible)
from the endowment x provided that there is a predictable process θ =
(θ0, θ1, θ2, . . . , θd) for which (θ, c) is a consumption strategy with V0(θ) = x
and Vt(θ) ≥0 for all t ∈T. By (5.37), we require that
V t(θ) = x +
t

u=1
θu · ∆Su −
t

u=1
cu ≥0
(5.39)
if such a strategy θ exists. But S is a Q-martingale, so, taking expectations,
(5.39) becomes, with C = t
u=1 cu as cumulative consumption,
EQ

Ct

= EQ

t

u=1
cu

≤x.
(5.40)

5.6. CONSUMPTION-INVESTMENT STRATEGIES
129
The budget constraint (5.40) is therefore necessary if the consumption C
is to be financed by the endowment x. It is also sufficient as shown in the
following.
Given a consumption process C with ct = ∆Ct, define the process
U t = x −Ct. Since C is predictable and ct+1 ≥0,
U t+1 = EQ

U t+1 |Ft

≤U t,
so that U is a supermartingale. By (5.40), EQ

U t

≥0 for all t ∈T. But
then we can find a hedging strategy θ for the claim X = 0 with V0(θ) = x
and Vt(θ) ≥0 for all t. We have proved the following.
Theorem 5.6.2. The consumption process C can be financed by an initial
endowment x if and only if the constraint (5.40) is satisfied.

Chapter 6
Continuous-Time
Stochastic Calculus
6.1
Continuous-Time Processes
In this and the succeeding chapters, the time parameter takes values in
either a finite interval [0, T] or the infinite intervals [0, ∞), [0, ∞].
We
denote the time parameter set by T in each case.
Filtrations and Stopping Times
Suppose (Ω, F, P) is a probability space. As before, we use the concept
of a filtration on (Ω, F, P) to model the acquisition of information as time
evolves. The definition of a filtration is as in Chapter 2 and now takes
account of the change in the time set T.
Definition 6.1.1. A filtration F = (Ft)t∈T is an increasing family of sub-
σ-fields of F(i.e., Ft ⊂F and if s ≤t, then Fs ⊂Ft).
We assume that F satisfies the ‘usual conditions’. This means the fil-
tration F is:
(a) complete; that is, every null set in F belongs to F0 and thus to each
Ft, and
(b) right continuous; that is, Ft = 5
s>t Fs for t ∈T.
Remark 6.1.2. Just as in the discrete case, Ft represents the history of some
process or processes up to time t. However, all possible histories must be
allowed. If an event A ∈F is Ft-measurable, then it only depends on what
has happened to time t. Unlike the situation we discussed in Chapter 2,
new information can arrive at any time t ∈[0, T] (or even t ∈[0, ∞)), and
the filtration consists of an uncountable collection of σ-fields. The right
continuity assumption is specific to this situation.
131

132
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
Definition 6.1.3. Suppose the time parameter T is [0, ∞] (or [0, ∞), or
[0, T]). A random variable τ taking values in T is a stopping time if, for
every t ≥0,
{τ ≤t} ∈Ft.
Remark 6.1.4. Consequently, the event {τ ≤t} depends only on the history
up to time t. The first time a stock price reaches a certain level is a stopping
time, as is, say, the first time the price reaches a certain higher level after
dropping by a specified amount. However, the last time, before some given
date, at which the stock price reaches a certain level is not a stopping time
because to say it is the ‘last time’ requires information about the future.
Note that in the continuous-time setting it does not make sense to replace
the condition {τ ≤t} ∈Ft by {τ = t} ∈Ft. Many of the properties of
stopping times carry over to this setting, however.
Just as in Chapter 5, a constant random variable, T(ω) = t for all
ω ∈Ω, is a stopping time. If T is any stopping time, then T + s is also a
stopping time for s ≥0.
We continue with some basic properties of stopping times.
Proposition 6.1.5. If S and T are stopping times, then S ∧T and S ∨T
are also stopping times. Consequently, if (Tn)n∈N is a sequence of stopping
times, then ∧nTn = infn Tn and ∨nTn = supn Tn are stopping times.
Proof. The proof is identical to that given in Example 5.2.3 for the discrete
case.
Definition 6.1.6. Suppose T is a stopping time with respect to the fil-
tration (Ft). Then the σ-field FT of events occurring up to time T is the
collection of events A ∈F satisfying
A ∩{T ≤t} ∈Ft for all t ∈T.
Exercise 6.1.7. Prove that FT is a σ-field.
One then can establish the following (compare with Exercise 5.2.6 for
the discrete case).
Theorem 6.1.8. Suppose S, T are stopping times.
a) If S ≤T, then FS ⊂FT .
b) If A ∈FS, then A ∩{S ≤T} ∈FT .
Proof. (a) Suppose that B ∈FS. Then, for t ∈T,
B ∩{T ≤t} = B ∩{S ≤t} ∩{T ≤t} ∈Ft.
(b) Suppose that A ∈FS. For t ∈T, we have
A ∩{S ≤T} ∩{T ≤t} = (A ∩{S ≤t}) ∩{T ≤t} ∩{S ∧t ≤T ∧t} .
Each of the three sets on the right-hand side is in Ft: the first because
A ∈FS, the second because T is a stopping time, and the third because
S ∧t and T ∧t are Ft-measurable random variables.

6.1. CONTINUOUS-TIME PROCESSES
133
Definition 6.1.9. A continuous-time stochastic process X taking values
in a measurable space (E, E) is a family of random variables {Xt} defined
on (Ω, F, P), indexed by t, that take values in (E, E).
That is, for each t, we have a random variable Xt(·) with values in E.
Alternatively, for each ω (i.e., fixing ω and letting t vary), we have a sample
path X·(ω) of the process.
Remark 6.1.10. X could represent the evolution of the price of oil or the
price of a stock over time.
For some (future) time t, Xt(ω) is a random quantity, a random variable.
Each ω represents a ‘state of the world’ corresponding to which there is a
price Xt(ω). Conversely, fixing ω means one realization of the world, as
time evolves, is considered. This gives a realization, or path, of the price
X·(ω) as a function of time t.
Equivalence of Processes
A natural question is to ask when two stochastic processes model the same
phenomenon.
We discuss several possible definitions for stochastic pro-
cesses defined on a probability space (Ω, F, P) and taking values in the
measurable space (E, E).
The weakest notion of equivalence of processes reflects the fact that
in practice one can only observe a stochastic process at finitely many in-
stants. Assume for simplicity that E = R and E is the Borel σ-field B
on R. Then we can form the family of finite-dimensional distributions of
the process X = (Xt)t≥0 by considering the probability that for n ∈N,
times t1, t2, . . . , tn ∈T and a Borel set A ⊂Rn, the random vector
(Xt1, Xt2, . . . , Xtn) takes values in A. Indeed, set
φX
t1,t2,...,tn(A) = P ({ω ∈Ω: (Xt1(ω), Xt2(ω), . . . , Xtn(ω)) ∈A}) .
For each family {t1, t2, . . . , tn}, this defines φX
t1,t2,...,tn as a measure on Rn.
We say that two processes X and Y are equivalent (or have the same law)
if their families of finite-dimensional distributions coincide, and then we
write X ∼Y .
Note that the preceding does not require Y to be defined on the same
probability space as X. This means that we can avoid complicated ques-
tions about the ‘proper’ probability space for a particular problem since
only the finite-dimensional distributions and not the full realisations of the
process (i.e., the various random ‘paths’ it traces out) are relevant for our
description of the probabilities concerned. It turns out that if we consider
the process as a map X : Ω→RT (i.e., ω →X(·, ω)) and we stick to
Borel sets A in RT, then the finite-dimensional distributions give us suf-
ficient information to identify a canonical version of the process, up to
equivalence. (This is the famous Kolmogorov extension theorem; see [194,
Theorem 2.2]).

134
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
However, at least when T is uncountable, most of the interesting sets
in RT are not Borel sets, so that we need a somewhat stronger concept of
‘equivalence’ that ‘fixes’ the paths of our process X tightly enough. Two
such definitions are now given; each of them requires the two processes
concerned to be defined on the same probability space.
Definition 6.1.11. Suppose (Xt)t≥0 and (Yt)t≥0 are two processes defined
on the same probability space (Ω, F, P) and taking values in (E, E). The
process {Yt} is said to be a modification of (Xt) if
Xt = Yt a.s. for all t ∈T;
i.e.,
P(Xt = Yt) = 1 for all t ∈T.
Definition 6.1.12. The processes (Xt) and (Yt) defined as in Defini-
tion 6.1.11 are said to be indistinguishable if, for almost every ω ∈Ω,
Xt(ω) = Yt(ω) for all t ∈T.
(6.1)
The difference between Definition 6.1.11 and Definition 6.1.12 is that
in Definition 6.1.11 the set of zero measure on which Xt and Yt may differ
may depend on t, whereas in Definition 6.1.12 there is a single set of zero
measure outside of which (6.1) holds. When the time index set is countable,
the two definitions coincide.
Exercise 6.1.13. A process X is right-continuous if for almost every ω the
map t →Xt(ω) is right-continuous. Show that if the processes X and Y
are right-continuous and one is a modification of the other, then they are
indistinguishable.
Definition 6.1.14. Suppose A ⊂[0, ∞] × Ωand that 1A(t, ω) = 1A is the
indicator function of A; that is,
1A(t, ω) =

1
if (t, ω) ∈A,
0
if (t, ω) /∈A.
Then A is called evanescent if 1A is indistinguishable from the zero process.
Exercise 6.1.15. Show that A is evanescent if the projection
{ω ∈Ω: there exists t with (t, ω) ∈A}
of A onto Ωis a set of measure zero.
Finally, we recall the following.
Definition 6.1.16. A process (t, ω) →Xt(ω) from ([0, T]×Ω, B([0, T]×F))
to a measurable space (E, E) is said to be progressively measurable, or
progressive, if for every t ∈[0, T] the map (s, ω) →Xs(ω) of [0, T] × Ωto
E is measurable with respect to the σ-field B([0,T]) × Ft.

6.2. MARTINGALES
135
6.2
Martingales
Definition 6.2.1. Suppose (Ft)t≥0 is a filtration of the measurable space
(Ω, F) and (Xt) is a stochastic process defined on (Ω, F) with values in
(E, E). Then X is said to be adapted to (Ft) if Xt is Ft-measurable for
each t.
The random process that models the concept of randomness in the most
fundamental way is a martingale; we now give the continuous-time defini-
tion for t ∈[0, ∞] ; the discrete-time analogue was discussed in Chapters 2
through 5.
Definition 6.2.2. Suppose (Ω, F, P) is a probability space with a filtration
(Ft)t≥0.
A real-valued adapted stochastic process (Mt) is said to be a
martingale with respect to the filtration (Ft) if E |Mt| ≤∞for all t and
for all s ≤t
E (Mt |Fs ) = Ms.
If the equality is replaced by ≤(resp.
≥), then (Mt) is said to be a
supermartingale (resp. submartingale).
Remark 6.2.3. A martingale is a purely random process in the sense that,
given the history of the process so far, the expected value of the process at
some later time is just its present value. Note that in particular
E (Mt) = E (M0) for all t ≥0.
Brownian Motion
The most important example of a continuous-time martingale is a Brownian
motion. This process is named for Robert Brown, a Scottish botanist who
studied pollen grains in suspension in the early nineteenth century. He
observed that the pollen was performing a very random movement and
thought this was because the pollen grains were alive. We now know this
rapid movement is due to collisions at the molecular level.
Definition 6.2.4. A standard Brownian motion (Bt)t≥0 is a real-valued
stochastic process that has continuous sample paths and stationary inde-
pendent Gaussian increments. In other words,
a) B0 = 0 a.s.
b) t →Bt(ω) is continuous a.s.
c) For s ≤t, the increment Bt −Bs is a Gaussian random variable that
has mean 0, variance t−s, and is independent of Fs = σ {Bu : u ≤s}.
We can immediately establish the following.
Theorem 6.2.5. Suppose (Bt) is a standard Brownian motion with respect
to the filtration (Ft)t≥0. Then

136
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
a) (Bt)t≥0 is an Ft-martingale.
b)

B2
t −t

t≥0 is an Ft-martingale.
c)

eσBt−σ2
2 t
t≥0 is an Ft-martingale.
Proof.
a) Since Bt −Bs is independent of Fs for all s ≤t, we have
E (Bt −Bs |Fs ) = E (Bt −Bs) = 0.
Consequently, E (Bt |Fs ) = Bs a.s.
b) For

B2
t −t

, we have
E

B2
t −B2
s |Fs

= E

(Bt −Bs)2 + 2Bs(Bt −Bs) |Fs

= E

(Bt −Bs)2 |Fs

+ 2BsE ((Bt −Bs) |Fs ) .
(6.2)
The second term in (6.2) is zero by the first part.
Independence
implies that
E

(Bt −Bs)2 |Fs

= E

(Bt −Bs)2
= t −s.
Therefore E

B2
t −t |Fs

= B2
s −s.
c) If Z is a standard normal random variable, with density
1
√
2πe−x2
2 ,
then
E

eλZ
=
1
√
2π
 ∞
−∞
eλxe−x2
2 dx = e
λ2
2 for λ ∈R.
For s < t, by independence and stationarity, we have
E

eσBt−σ2
2 t |Fs

= eσBs−σ2
2 tE

eσ(Bt−Bs) |Fs

= eσBs−σ2
2 tE

eσ(Bt−Bs)
= eσBs−σ2
2 tE

eσBt−s
.
Now σBt−s is N

0, σ2(t −s)

; that is, if Z is N(0, 1) as previously,
the random variable σBt−s has the same law as σ√t −sZ and
E

eσBt−s
= E

eσ√t−sZ
= e
σ2
2 (t−s).
Therefore
E

eσBt−σ2
2 t |Fs

= eσBs−σ2
2 s a.s. for s < t.
Conversely, we prove in Theorem 6.4.16 that a continuous process that
satisfies the first two statements in Theorem 6.2.5 is, in fact, a Brownian
motion. (Indeed, the third statement characterises a Brownian motion.)

6.2. MARTINGALES
137
Uniform Integrability and Limit Theorems
We discussed the role of uniform integrability in some detail in the discrete-
time setting of Chapter 5. Here we review briefly how these ideas carry
over to continuous-time martingales. Definition 5.3.1 immediately prompts
the following.
Definition 6.2.6. A martingale {Mt} with t ∈[0, ∞) (or t ∈[0, T]) is said
to be uniformly integrable if the set of random variables {Mt} is uniformly
integrable.
Remark 6.2.7. If {Mt} is a uniformly integrable martingale on [0, ∞), then
lim Mt = M∞exists a.s. as we proved for the discrete case in Chapter 5.
Again, a consequence of {Mt} being a uniformly integrable martingale
on [0, ∞) is that M∞= lim Mt in the L1 norm; i.e., limt ∥Mt −M∞∥1 = 0.
In this case, {Mt} is a martingale on [0, ∞] and
Mt = E (M∞|Ft ) a.s. for all t.
We again say that M is closed by the random variable M∞.
Recall from the examples following Definition 5.3.1 that if a class K of
random variables is in L1(Ω, F, P) and is Lp-bounded for some p > 1, then
K is uniformly integrable.
Notation 6.2.8. Write M for the set of uniformly integrable martingales.
An important concept is that of ‘localization’. If C is a class of processes,
then Cℓoc is the set of processes defined as follows. We say that X ∈Cℓoc if
there is an increasing sequence {Tn} of stopping times such that lim Tn =
∞a.s. and Xt∧Tn ∈C. For example, C might be the bounded processes, or
the processes of bounded variation.
Notation 6.2.9. Mℓoc denotes the set of local martingales.
The defining relation for martingales, E (Mt |Fs ) = Ms, can again be
extended to stopping times. This result, which is the analogue of The-
orem 5.3.9, is again known as Doob’s optional stopping theorem since it
says the martingale equality is preserved even if (non-anticipative) random
stopping rules are allowed. A complete proof of this result in continuous
time can be found in [109, Theorem 4.12, Corollary 4.13]. Note that our
discussion of the discrete case in Chapter 5 showed how the extension from
bounded to more general stopping times required the martingale conver-
gence theorem and conditions under which a supermartingale is closed by
an L1-function. This condition is also required in the following.
Theorem 6.2.10. Suppose (Mt)t≥0 is a right-continuous supermartingale
(resp. submartingale) with respect to the filtration (Ft). If S and T are
two (Ft)-stopping times such that S ≤T a.s., then
E (MT |FS ) ≤MS a.s.
(resp., E (MT |FS ) ≥MS a.s.).

138
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
Corollary 6.2.11. In particular, if (Mt)t≥0 is a right-continuous martin-
gale and S, T are (Ft)-stopping times with S ≤T, then
E (MT |FS ) = MS a.s.
Remark 6.2.12. Note that, if T is any (Ft)-stopping time, then E (MT ) =
E (M0).
The following is a consequence of the optional stopping theorem. Note
that we write x+ = max {x, 0} and x−= max {−x, 0}.
Lemma 6.2.13. Suppose Xt, t ∈[0, ∞] is a supermartingale. Then
αP

(inf
t Xt) ≤−α

≤sup
t E

X−
t

for all α ≥0.
Proof. Write
S(ω) = inf {t : Xt(ω) ≤−α}
and St = S ∧t. Using the optional stopping theorem (Theorem 6.2.10), we
have
E (XSt) ≥E (Xt) .
Therefore
E (Xt) ≤−αP
$
inf
s≤t Xs ≤−α
%
+

{infs≤t Xs>−α}
XtdP;
that is,
αP
$
inf
s≤t Xs ≤−α
%
≤E (−Xt) +

{infs≤t Xs>−α}
XtdP
=

{infs≤t Xs≤−α}
−XtdP
≤E

X−
t

.
(6.3)
Letting t →∞in (6.3), the result follows.
As a consequence, we can deduce Doob’s maximal theorem.
Theorem 6.2.14. Suppose (Xt)t∈[0,∞] is a martingale. Then
αP
$
sup
t |Xt| ≥α
%
≤sup
t ∥Xt∥1 for all α ≥0.
Proof. From Jensen’s inequality (see Proposition 5.3.4), if X is a mar-
tingale, then Yt = −|Xt| is a (negative) supermartingale with ∥Yt∥1 =
∥Xt∥1 = E

Y −
t

. In addition,

inf
t Yt ≤−α

=
$
sup
t |Xt| ≥α
%
,
so the result follows from Lemma 6.2.13.

6.2. MARTINGALES
139
Before proving Doob’s Lp inequality, we first establish the following
result.
Theorem 6.2.15. Suppose X and Y are two positive random variables
defined on the probability space (Ω, F, P) such that X ∈Lp for some p, 1 <
p < ∞, and
αP({Y ≥α}) ≤

{Y ≥α}
XdP for all α > 0.
Then
∥Y ∥p ≤q ∥X∥p ,
where 1
p + 1
q = 1.
Proof. Let F(λ) = P(Y > λ) be the complementary distribution function
of Y . Using integration by parts,
E (Y p) = −
 ∞
0
λpdF(λ)
=
 ∞
0
F(λ)d(λp) −lim
h→∞(λpF(λ))h
0
≤
 ∞
0
F(λ)d(λp)
≤
 ∞
0
λ−1

{Y ≥λ}
XdP

d(λp)
by hypothesis
= E

X
 Y
0
λ−1d(λp)

by Fubini’s theorem
=

p
p −1

E

XY p−1
≤q ∥X∥p
66Y p−166
q
by H¨older’s inequality.
That is,
E (Y p) ≤q ∥X∥p

E

Y pq−q 1
q .
If ∥Y ∥p is finite, the result follows immediately because pq −q = p.
Otherwise, consider the random variable
Yk = Y ∧k, k ∈N.
Then Yk ∈Lp and Yk also satisfies the hypotheses. Therefore
∥Yk∥p ≤q ∥X∥p .
Letting k →∞, the result follows.

140
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
Theorem 6.2.16. Suppose (Xt)t≥0 is a right-continuous positive sub-
martingale. Write X∗(ω) = supt Xt(ω). Then, for 1 < p ≤∞, X∗∈Lp if
and only if
sup
t ∥Xt∥p < ∞.
Also, for 1 < p < ∞and q−1 = 1 −p−1,
∥X∗∥p ≤q sup
t ∥Xt∥p .
Proof. When p = ∞, the first part of the theorem is immediate because
sup
t ∥Xt∥∞= B < ∞
implies that Xt ≤B a.s. for all t ∈[0, ∞]. The right-continuity is required
to ensure there is a single set of measure zero outside which this inequality
is satisfied for all t. Also, for 1 < p < ∞, if X∗∈Lp, then
sup
t ∥Xt∥p ≤∥X∗∥p < ∞.
As in Section 5.3, the random variables (Xt) are uniformly integrable,
so from [109, Corollaries 3.18 and 3.19] we have that
X∞(ω) = lim
t→∞Xt(ω)
exists a.s. Using Fatou’s lemma, we obtain
E

lim
t Xp
t

≤lim inf
t
E (Xp
t ) ≤sup
t E (Xp
t ) < ∞.
Therefore X∞∈Lp and ∥X∞∥p ≤supt ∥Xt∥p.
Write X∗
t (ω) = sups≤t Xs(ω). Then {−Xt} is a supermartingale, so
from inequality (6.3) in Lemma 6.2.13, for any α > 0,
αP

inf
s≤t(−Xs) ≤−α

= αP (X∗
t ≥α) ≤

{X∗
t ≥α}
XtdP ≤

{X∗≥α}
XtdP.
Letting t →∞, we have for any α > 0,
αP (X∗≥α) ≤

{X∗≥α}
X∞dP.
Therefore, Theorem 6.2.15 can be applied with Y = X∗and X = X∞to
obtain
∥X∗∥p ≤q ∥X∞∥p
and the result follows.
The following important special case arises when p = q = 2 and the
time interval is taken as [0, T].
Corollary 6.2.17 (Doob’s Inequality). Suppose (Mt)t≥0 is a continu-
ous martingale. Then
E

sup
0≤t≤T
|Mt|2

≤4E

|MT |2
.

6.3. STOCHASTIC INTEGRALS
141
6.3
Stochastic Integrals
In discrete time the discounted value of a portfolio process having initial
value V0 and generated by a self-financing strategy (Ht)t≥0 is given by
V0 +
n

j=1
Hj(Sj −Sj−1).
Recall that under an equivalent measure the discounted price process S is
a martingale. Consequently, the preceding value process is a martingale
transform. The natural extension to continuous time of such a martingale
transform is the stochastic integral
4 t
0 HsdSs.
However, dS = SσdWt,
where (Wt) is a Brownian motion.
Almost all sample paths W·(ω) of
Brownian motion are known to be of unbounded variation. They are there-
fore certainly not differentiable. The integral
4
HdS cannot be defined as
4
H dS
dt ·dt or even as a Stieltjes integral. It can, however, be defined as the
limit of suitable approximating sums in L2(Ω).
We work initially on the time interval [0, T]. Suppose (Wt) is an (Ft)-
Brownian motion defined on (Ω, F, P) for t ∈[0, T]; that is, W is adapted
to the filtration (Ft).
Simple Processes
Definition 6.3.1. A real-valued simple process on [0, T] is a function H
for which
a) there is a partition 0 = t0 < t1 < . . . tn = T; and
b) Ht0 = H0(ω) and Ht = Hi(ω) for t ∈(ti, ti+1], where Hi(·) is Fti-
measurable and square integrable. That is,
Ht = H0(ω) +
n−1

i=0
Hi(ω)1(ti,ti+1] for t ∈[0, T].
Definition 6.3.2. If H is a simple process, the stochastic integral of H with
respect to the Brownian motion (Wt) is the process defined for t ∈(tk, tk+1],
by
 t
0
HsdWs =
k−1

i=0
Hi(Wti+1 −Wti) + Hk(Wt −Wtk).
This can be written as a martingale transform:
 t
0
HsdWs =
n

i=0
Hi(Wti+1∧t −Wti∧t).

142
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
We write
4 t
0 HdW =
4 t
0 HsdWs.
Note that, because W0 = 0, there is no contribution to the integral at
t = 0.
Theorem 6.3.3. Suppose H is a simple process. Then:
a)
4 t
0 HsdWs

is a continuous Ft-martingale.
b) E
)4 t
0 HsdWs
*2
= E
4 t
0 H2
s ds

.
c) E

sup0≤t≤T
'''
4 t
0 HsdWs
'''
2
≤4E
4 T
0 H2
s ds

.
Proof.
a) For t ∈(tk, tk+1], we have
 t
0
HsdWs =
k−1

i=0
Hi(Wti+1 −Wti) + Hk(Wt −Wtk).
Now Wt(·) is continuous a.s. in t; hence so
4 t
0 HsdWs. Suppose that
0 ≤s ≤t ≤T. Recall that
 t
0
HsdWs =
n

i=0
Hi(Wti+1∧t −Wti∧t),
where Hi is Fti-measurable. Now if s ≤ti, then
E

Hi

Wti+1∧t −Wti∧t

|Fs

= E

E

Hi

Wti+1∧t −Wti∧t

|Fti

|Fs

= E

HiE

Wti+1∧t −Wti∧t |Fti

|Fs

= 0 = Hi

Wti+1∧s −Wti∧s

because ti+1 ∧s = ti ∧s = s. If s ≥ti, then
E

Hi

Wti+1∧t −Wti∧t

|Fs

= HiE

Wti+1∧t −Wti |Fs

= Hi

Wti+1∧s −Wti∧s

.
Consequently, for s ≤t,
E
 t
0
HsdWs |Fs

=
 s
0
HudWu
and
4 t
0 HdW

is a continuous martingale.
b) Now suppose i < j so that i + 1 ≤j. Then
E

HiHj

Wti+1∧t −Wti∧t
 
Wtj+1∧t −Wtj∧t


6.3. STOCHASTIC INTEGRALS
143
= E

E

HiHj

Wti+1∧t −Wti∧t
 
Wtj+1∧t −Wtj∧t
 ''Ftj

= E

HiHj

Wti+1∧t −Wti∧t

E

Wtj+1∧t −Wtj∧t
''Ftj

= 0.
Also,
E

H2
i

Wti+1∧t −Wti∧t
2
= E

H2
i E

Wti+1∧t −Wti∧t
2 |Fti

= E

H2
i (ti+1 ∧t −ti ∧t)

.
Consequently,
E
 t
0
HdW
2
=
n

i=0
E

H2
i (ti+1 ∧t −ti ∧t)

= E
 t
0
H2
s ds

=
 t
0
E

H2
s

ds.
c) For the final part, apply Doob’s maximal inequality, Corollary 6.2.17,
to the martingale
4 t
0 HsdWs

.
Notation 6.3.4. We write H for the space of processes adapted to (Ft) that
satisfy E
4 T
0 H2
s ds

< ∞.
Lemma 6.3.5. Suppose {Hs} ∈H. Then there is a sequence {Hn
s } of
simple processes such that
lim
n→∞E
 T
0
|Hs −Hn
s |2 ds

= 0.
Outline of the Proof. Fix f ∈H, and define a sequence of simple functions
converging to f by setting
fn(t, ω) = n

k
n
k−1
n
f(s, ω)ds for t ∈
.k
n, k + 1
n
/
.
If the integral diverges, replace it by 0. By Fubini’s theorem, this only
happens on a null set in Ωsince f is integrable on T × Ω.
Note that, using progressive measurability (recall Definition 6.1.16), as
a random variable, the preceding integral is F k
n -measurable, so that fn is
a simple process as defined in Definition 6.3.1. We show in the following
that
4 T
0 |fn(t, ω) −f(t, ω)|2 dt converges to 0 whenever f(·, ω) ∈L2[0, T],
and also that, for all such ω ∈Ω,
 T
0
|fn(t, ω)|2 dt ≤
 T
0
|f(t, ω)|2 dt.

144
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
Thus the dominated convergence theorem allows us to conclude that
E
 T
0
|fn −f| dt

→0 as n →∞.
We write fh = fn when h =
1
n.
The proof now reduces to a prob-
lem in L2[0, T], namely to show that if f ∈L2[0, T] is fixed, then as
h ↓0, the ‘time averages’ fh defined for t ∈

(k −1)h, kh ∧h−1
by
fh(t) = 1
h
4 kh
(k−1)h f(s)ds and 0 outside

h, h−1
remain L2-dominated by f
and converge to f in L2-norm. To prove this, first consider the estimate
 T
0
f 2
h(t)dt ≤
[ T
h ]

k=1
'''''
 kh
(k−1)h
f(s)ds
'''''
2
,
which is exact if T
h ∈N or T = ∞. Now the Schwarz inequality, applied
to 1 · f, shows that each term in the latter sum is bounded above by
h ·
4 kh
(k−1)h f 2(s)ds; hence the sum is bounded by h ·
4 [ T
h ]·h
0
f 2(s)ds ≤h ·
4 T
0 f 2(s)ds, which proves domination. To prove the convergence, consider
ε > 0 and note that if f is a step function, then fh will converge to f as
h ↓0. Since the step functions are dense in L2[0, T], choose a step function
f ε such that ∥f ε −f∥< ε (with ∥·∥denoting the norm in L2[0, T]). Note
that since fh is also a step function, fh −f ε
h = (f −f ε)h. Moreover, by the
definition of fh, it is easy to verify that ∥fh −f ε
h∥≤∥f −f ε∥. Therefore
we can write
∥fh −f∥= ∥f ε
h −f ε + (f −f ε)h −(f −f ε)∥≤∥f ε
h −f ε∥+ 2 ∥f −f ε∥.
But the first term goes to 0 as h ↓0 since fh is a step function, while the
second is less than 2ε. This proves the result.
The Integral as a Stochastic Process
Theorem 6.3.6. Suppose (Wt)t≥0 is a Brownian motion on the filtration
(Ft). Then there is a unique linear map I from H into the space of con-
tinuous Ft-martingales on [0, T] such that:
a) If H is a simple process in H, then
I(H)t =
 t
0
HsdWs.
b) If t ≤T,
E

(I(H)t)2
= E
 t
0
H2
s ds

.
The second identity is called the isometry property of the integral.

6.3. STOCHASTIC INTEGRALS
145
Proof. For H a simple process, one defines I(H)t =
4 t
0 HsdWs. Suppose
H ∈H and (Hn) is a sequence of simple processes converging to H. Then
I(Hn+p −Hn)t =
 t
0
(Hn+p
s
−Hn
s )dWs
=
 t
0
Hn+p
s
dWs −
 t
0
Hn
s dWs.
From Doob’s inequality (Corollary 6.2.17),
E

sup
0≤t≤T
''I(Hn+p −Hn)t
''2

≤4E
 T
0
''Hn+p
s
−Hn
s
''2 ds

.
(6.4)
Consequently, there is a subsequence

Hkn
such that
E

sup
t≤T
''I

Hkn+1
t −I

Hkn
t
''2
≤2−n.
Almost surely, the sequence of continuous functions I(Hkn)t, 0 ≤t ≤T is
uniformly convergent on [0, T] to a function I(H)t. Letting p →∞in (6.4),
we see that
E

sup
t≤T
|I(H)t −I(Hn)t|2

≤4E
 T
0
|Hs −Hn
s |2 ds

.
This argument also implies that I(H) is independent of the approximating
sequence (Hn).
Now E (I(Hn)t |Fs ) = I(Hn)s a.s. The integrals {I(Hn), I(H)} belong
to L2(Ω, F, P), so
∥E (I(H)t |Fs ) −I(H)s∥2 ≤∥E (I(H)t |Fs ) −E (I(Hn)t |Fs )∥2
+ ∥E (I(Hn)t |Fs ) −I(Hn)s∥2 + ∥I(Hn)s −I(H)s∥2 .
The right-hand side can be made arbitrarily small, so I(H)t is an Ft-
martingale.
The remaining results follow by continuity and from the density in H
of simple processes.
Notation 6.3.7. We write I(H)t =
4 t
0 HsdWs for H ∈H.
Lemma 6.3.8. For H ∈H,
a) E

sup0≤t≤T
'''
4 t
0 HsdWs
'''
2
≤4E
4 T
0 |H|2
s ds

.
b) If τ is an (Ft)-stopping time such that τ ≤T, then
 τ
0
HsdWs =
 T
0
1{s≤τ}HsdWs.

146
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
Proof.
a) Let (Hn) be a sequence of simple processes approximating H.
We know that
E

I(Hn)2
T

= E
 T
0
|Hn
s |2 ds

so, taking limits, we have
E

I(H)2
T

= E
 T
0
|Hs|2 ds

.
Also,
E

sup
t≤T
I(Hn)2
t

≤4E
 T
0
|Hn
s |2 ds

.
Taking limits, the result follows.
b) Suppose τ is a stopping time of the form
τ =

1≤i≤n
ti1Ai,
(6.5)
where Ai ∩Aj = ∅for i ̸= j and Ai ∈Fti. Then
 T
0
1{s>τ}HsdWs =
 T
0
⎛
⎝
1≤i≤n
1Ai1{s>ti}
⎞
⎠HsdWs.
Now for each i the process 1{s>ti}1AiHs is adapted and in H; it is
zero if s ≤ti and equals 1AiHs otherwise. Therefore
 T
0
⎛
⎝
1≤i≤n
1Ai1{s>ti}
⎞
⎠HsdWs
=

1≤i≤n
1Ai
 T
ti
HsdWs =
 T
τ
HsdWs.
Consequently, for τ of the form (6.5),
 T
0
1{s≤τ}HsdWs =
 τ
0
HsdWs.
Now an arbitrary stopping time τ can be approximated by a decreas-
ing sequence of stopping times τn where
τn =
2n

i=0
(k + 1)T
2n
1A,

6.3. STOCHASTIC INTEGRALS
147
where A =

kT
2n ≤τ < (k+1)T
2n

, so that lim τn = τ a.s. Consequently,
because I(H) is almost surely continuous in t,
lim
n→∞
 τn
0
HsdWs =
 τ
0
HsdWs a.s.
Also,
E
⎛
⎝
'''''
 T
0
1{s≤τ}HsdWs −
 T
0
1{s≤τn}HsdWs
'''''
2⎞
⎠
= E
 T
0
1{τ<s≤τn}H2
s ds

,
and this converges to zero by the dominated convergence theorem.
Therefore
lim
n→∞
 T
0
1{s≤τn}HsdWs =
 T
0
1{s≤τ}HsdWs
both a.s. and in L2(Ω); the result follows.
Notation 6.3.9. Write
,
H =

{Hs} : H is Ft-adapted and
 T
0
H2
s ds < ∞a.s.
&
.
The preceding definition and results for the stochastic integral can be
extended from H to ,
H.
Theorem 6.3.10. There is a unique linear map ,I of ,
H into the space of
continuous processes defined on [0, T] such that:
a) If {Ht}0≤t≤T is in H, then for all t ∈[0, T] the processes ,I(H)t and
I(H)t are indistinguishable.
b) If {Hn}n≥0 is a sequence in ,
H such that
4 T
0 (Hn
s )2ds converges to
zero in probability, then
sup
0≤t≤T
''',I(Hn)t
'''
converges to zero in probability.
Remark 6.3.11. In fact, ,I(H)t is a local martingale, meaning that there
is a non-decreasing sequence Tn of stopping times with limit T such that
Tn ≤Tn+1 ≤T and for each n, ,I(H)Tn∧t is a martingale.

148
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
Notation 6.3.12. One writes ,I(H)t =
4 t
0 HsdWs.
Proof. From Theorem 6.3.6, we know that for H ∈H, I(H) is defined.
Suppose H ∈,
H. Define
Tn = inf
$
0 ≤u ≤T :
 u
0
H2
s ds ≥n
%
∧T.
(Here and elsewhere we adopt the convention that inf(∅) = ∞.) Because
Hs is adapted,
4 t
0 H2
s ds is adapted and Tn is an (Ft)-stopping time.
Then write Hn
s = 1{s<Tn}Hs. The processes Hn are therefore in H and
 t
0
Hn
s dWs =
 t
0
1{s≤Tn}Hn+1
s
dWs =
 Tn∧t
0
Hn+1
s
dWs.
Therefore, on the set
4 T
0 H2
udu < n

, for all t ≤T,
I(Hn)t = I(Hn+1)t.
Now
3
n≥0
 T
0
H2
udu < n
&
=
 T
0
H2
udu < ∞
&
.
Thus we define ,I(H)t by putting ,I(H)t = I(Hn)t on
4 T
0 H2
s ds < n

.
Clearly ,I(H)t = I(H)t and is continuous a.s.
For the second assertion, write
B =
 T
0
H2
udu ≥1
N
&
,
A =
$
ω : sup
0≤t≤T
''',I(H)t
''' ≥ε
%
.
Then
P(A) = P(A ∩B) + P(A ∩Bc) ≤P(B) + P(A ∩Bc).
Therefore, for any ε > 0,
P

sup
0≤t≤T
''',I(H)t
''' ≥ε

≤P
 T
0
H2
udu ≥1
N

+ P
 T
0
H2
udu < 1
N
&
∩
$
sup
0≤t≤T
''',I(H)t
''' ≥ε
%
.
(6.6)
Write
τN = inf
$
s ≤T :
 s
0
H2
udu ≥1
N
%
∧T.
On the set Bc, we have
 t
0
HsdWs =
 t
0
1{s≤τN}HsdWs.

6.4. THE IT ˆO CALCULUS
149
Therefore, with Gs = Hs1{s≤τN}, Gs = Hs on Bc, and from Doob’s in-
equality, it follows that
E

sup
0≤t≤T
''''
 t
0
GsdWs
''''
2
≤4E
 t
0
(Gs)2ds

≤4
N .
(6.7)
Using Chebychev’s inequality, we also have, by (6.7),
P(A ∩Bc) = P

Bc ∩
$
sup
0≤t≤T
''',I(H)t
''' ≥ε
%
≤P

sup
0≤t≤T
''',I(G)t
''' ≥ε

≤1
ε2 E

sup
0≤t≤T
''''
 t
0
GsdWs
''''
2
≤
4
Nε2 .
Consequently, from (6.6),
P

sup
0≤t≤T
''',I(H)t
''' ≥ε

≤P
 T
0
H2
udu ≥1
N

+
4
Nε2 .
Hence we see that if (Hn) is a sequence in ,
H such that
4 T
0 (Hn
u )2du

converges to zero in probability, then

sup0≤t≤T
''',I(Hn)t
'''

converges to
zero in probability. The continuity of the operator ,I is therefore established.
If H ∈,
H, then, with Hn
s = 1{s<Tn}Hs, we see that
4 T
0 (Hs −Hn
s )2ds

converges to zero in probability. Using the continuity property, we see that
the map ,I is uniquely defined.
Similarly, for H, K ∈,
H, suppose there are the approximating sequences
Hn, Kn ∈H. Now
4 T
0 (Hs −Hn
s )2ds

and
4 T
0 (Ks −Kn
s )2ds

converge
to zero in probability as n →∞. Furthermore,
I(αHn + βKn)t = αI(Hn)t + βI(Kn)t.
Letting n →∞, we see that ,I is a linear map.
6.4
The Itˆo Calculus
If f(t) is a real-valued, differentiable function for t ≥0 and f(0) = 0, then
f(t)2 = 2
 t
0
f(s) ˙f(s)ds = 2
 t
0
f(s)df(s).
However, if W is a Brownian motion we know that E

W 2
t

= t. Con-
sequently, W 2
t cannot be equal to 2
4 t
0 WsdWs because this integral is a
(local) martingale and E

2
4 t
0 WsdWs

= 0.

150
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
The Itˆo calculus is described for a class of processes known as Itˆo pro-
cesses, which we will now define.
Itˆo Processes and the Differentiation Rule
Definition 6.4.1. Suppose (Ω, F, P) is a probability space with a filtration
(Ft)t≥0, and (Wt) is a standard (Ft)-Brownian motion. A real-valued Itˆo
process (Xt)t≥0 is a process of the form
Xt = X0 +
 t
0
Ksds +
 t
0
HsdWs,
where
(a) X0 is F0-measurable,
(b) K and H are adapted to Ft, and
(c)
4 T
0 |Ks| ds < ∞a.s. and
4 T
0
''H2
s
'' ds < ∞a.s.
We can then obtain a uniqueness property that is a consequence of the
following result.
Lemma 6.4.2. Suppose the process
4 t
0 Ks ds = Mt is a continuous mar-
tingale, where
4 T
0 |Ks| ds < ∞a.s. Then Mt = 0 a.s. for all t ≤T, and
there is a set N ⊂Ωof measure zero such that, for ω /∈N, Ks(ω) = 0 for
almost all s.
Proof. Suppose initially that
4 T
0 |Ks| ds ≤C < ∞a.s. Then, with tn
i = iT
N
for 0 ≤i ≤n, we have
n

i=1
(Mtn
i −Mtn
i−1)2 ≤sup
i
'''Mtn
i −Mtn
i−1
'''
n

i=1
'''Mtn
i −Mtn
i−1
'''
= sup
i
'''Mtn
i −Mtn
i−1
'''
n

i=1
'''''
 tn
i
tn
i−1
Ksds
'''''
≤sup
i
'''Mtn
i −Mtn
i−1
'''
n

i=1
 tn
i
tn
i−1
|Ks| ds
≤C sup
i
'''Mtn
i −Mtn
i−1
''' .
Consequently, limn→∞
n
i=1(Mtn
i −Mtn
i−1)2 = 0 a.s., so by the bounded
convergence theorem, we have
lim
n→∞E
 n

i=1

Mtn
i −Mtn
i−1
2

= 0 = E

M 2
t −M 2
0

,

6.4. THE IT ˆO CALCULUS
151
as M is a martingale. By definition, M0 = 0 a.s. Consequently, Mt = 0 a.s.,
and so Mt = 0 a.s. for t ≤T.
Now relax the assumption that
4 T
0 |Ks| ds is bounded. Write
Tn = inf
$
0 ≤s ≤T :
 s
0
|Ku| du ≥n
%
∧T.
Then Tn is a stopping time because K is adapted, and limn→∞Tn = T.
The preceding result shows that Mt∧Tn = 0 a.s., and so limn→∞Mt∧Tn =
0 = Mt a.s.
Corollary 6.4.3. Suppose M is a martingale of the form
4 t
0 HsdWs +
4 t
0 Ksds with
4 t
0 H2
s ds < ∞a.s. and
4 t
0 |Ks| ds < ∞a.s. Then
4 t
0 Ksds is
a martingale that is zero a.s. and there is a P-null set N ⊂Ωsuch that,
for ω /∈N, Ks(ω) = 0 for almost all s.
Corollary 6.4.4. Suppose the Itˆo process X has representations
Xt = X0 +
 t
0
Ksds +
 t
0
HsdWs,
Xt = X′
0 +
 t
0
K′
sds +
 t
0
H′
sdWs.
Then X0 = X′
0 a.s., Hs = H′
s a.s. (ds × dP), and Ks = K′
s a.s. (ds × dP).
In particular, if X is a martingale, then K = 0.
Proof. Clearly X0 = X′
0. Therefore
 t
0
(Ks −K′
s)ds =
 t
0
(H′
s −Hs)dWs,
and
4 t
0(Ks −K′
s)ds is a martingale. The result follows from Lemma 6.4.2.
Remark 6.4.5. Suppose (Wt)t≥0 is a Brownian motion and
π = {0 = t0 ≤t1 ≤· · · ≤tN = t}
is a partition of [0, t]. Write
|π| = max
i (ti+1 −ti).
Then
E
N−1

i=0

Wti+1 −Wti
2

= E
N−1

i=0

W 2
ti+1 −W 2
ti

= t.
(6.8)
In fact, we can show that N−1
i=0 (Wti+1 −Wti)2 converges to t almost surely
as |π| →0.

152
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
Choose a sequence (πn) of partitions with |πn| →0 as n →∞. Write
Qn =

πn
(Wti+1 −Wti)2;
then we have shown that Qn →t in L2 as n →∞.
By Chebychev’s
inequality, we have, for any ε > 0, that
P(|Qn −t| > ε) ≤E

(Qn −t)2
ε2
.
Set E

(Qn −t)2
= qn, so that qn →0 as n →∞.
Choosing a sub-
sequence, we can assume that qn <
1
22n .
Letting εn =
1
2n and writing
An =

|Qn −t| >
1
2n

, we obtain P(An) ≤
1
2n , so that ∞
n=1 P(An) < ∞.
By the first Borel-Cantelli lemma, it follows that P(∩n≥1An) = 0, and
hence that Qn →t a.s. as n →∞.
For a general, continuous (local) martingale (Mt)t≥0,
lim
|π|→0
N

i=0

Mti+1 −Mti
2
exists and is a predictable, continuous increasing process denoted by ⟨M⟩t.
From Jensen’s inequality, M 2 is a submartingale and it turns out that
⟨M⟩is the unique (continuous) increasing process in the Doob-Meyer de-
composition of M 2. This decomposition is entirely analogous to the Doob
decomposition described in Section 5.3, but the technical complexities in-
volved are substantially greater in continuous time. For details, see the
development in [109, Chapter 10] or [199, Chapter 3]. ⟨M⟩is called the
(predictable) quadratic variation of M. Consequently, (6.8) states that for
a Brownian motion W,
⟨W⟩t = t.
For H ∈,
H we have seen that Mt =
4 t
0 HsdWs is a local martingale. It
is shown in [109] that in this case
⟨M⟩t =
 t
0
H2
s ds a.s.
In some sense, (6.8) indicates that, very formally, (dW)2 ≃dt, or (dW) ≃
√
dt.
Suppose X is an Itˆo process on 0 ≤t ≤T,
Xt = X0 +
 t
0
Ksds +
 t
0
HsdWs,
(6.9)
where
4 T
0 |Ks| ds < ∞a.s. and
4 T
0 |Hs|2 ds < ∞a.s. Considering partitions
π = {0 = t0 ≤t1 ≤· · · ≤tN = t} of [0, t], it can be shown that
lim
|π|→0
N

i=0

Xti+1 −Xti
2

6.4. THE IT ˆO CALCULUS
153
converges a.s. to
 t
0
|Hs|2 ds.
That is, ⟨X⟩t = ⟨M⟩t, where Mt =
4 t
0 HsdWs is the martingale term in the
representation (6.9) of X.
Again, if X is a differentiable process (that is, if Hs = 0 in (6.9)), then
the usual chain rule states that, for a differentiable function f,
f(Xt) = f(X0) +
 t
0
f ′(Xs)dXs.
However, if X is an Itˆo process, the differentiation rule (commonly known
as the Itˆo formula) has the following form.
Theorem 6.4.6. Suppose {Xt}t≥0 is an Itˆo process of the form
Xt = X0 +
 t
0
Ksds +
 t
0
HsdWs.
Suppose f is twice differentiable. Then
f(Xt) = f(X0) +
 t
0
f ′(Xs)dXs + 1
2
 t
0
f ′′(Xs)d ⟨X⟩s .
Here, by definition, ⟨X⟩t =
4 t
0 H2
s ds; that is, the (predictable) quadratic
variation of X is the quadratic variation of its martingale component
 t
0
HsdWs.
Also,
 t
0
f ′(Xs)dXs =
 t
0
f ′(Xs)Ksds +
 t
0
f ′(Xs)HsdWs.
For a proof see [109]. More generally, the differentiation rule can be
proved in the following form.
Theorem 6.4.7. If F : [0, ∞)×R →R is continuously differentiable in the
first component and twice continuously differentiable in the second, then
F(t, Xt) = F(0, X0) +
 t
0
∂F
∂s (s, Xs)ds
+
 t
0
∂F
∂x (s, Xs)dXs + 1
2
 t
0
∂2F
∂x2 (s, Xs)d ⟨X⟩s .
Example 6.4.8.
(i) Let us consider the case when Ks = 0, Hs = 1. Then
Xt = X0 + Wt,

154
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
where Wt is standard Brownian motion. Taking f(x) = x2, we have
⟨X⟩t = ⟨W⟩t = t so
X2
t = X2
0 + 2
 t
0
WsdWs + 1
2
 t
0
2ds.
That is,
X2
t −X2
0 −t = 2
 t
0
WsdWs.
For any T < ∞, we have E
4 T
0 W 2
s ds

< ∞, so from Theorem 6.3.6,
4 t
0 WsdWs is a martingale. If X0 = 0, then Xt = Wt and we see that
W 2
t −t is a martingale.
(ii) An often-used model for a price process is the so-called ‘log-normal’
model. In this case, it is supposed the price process St evolves ac-
cording to the stochastic dynamics
dSt
St
= µdt + σdWt,
(6.10)
where µ and σ are real constants and S0 = X0. This means that
St = X0 +
 t
0
Ssµds +
 t
0
SsσdWs.
Assuming such a process S exists, it is therefore an Itˆo process with
Ks = µSs,
Hs = σSs.
Then ⟨X⟩t =
4 t
0 σ2S2
sds. Assuming St > 0 and applying Itˆo’s formula
with f(x) = log x (formally, because the logarithmic function is not
twice continuously differentiable everywhere),
log St = log X0 +
 t
0
µdSs
Ss
+ 1
2
 t
0

−1
S2s

σ2S2
sds
= log X0 +
 t
0

µ −σ2
2

ds +
 t
0
σdWs
= log X0 +

µ −σ2
2

t + σWt.
Consequently,
St = X0 exp
$
µ −σ2
2

t + σWt
%
.

6.4. THE IT ˆO CALCULUS
155
Exercise 6.4.9. Consider the function
F(t, x) = X0 exp
$
µ −σ2
2

t + σx
%
.
Apply the Itˆo formula of Theorem 6.4.7 to St = F(t, Wt) to show that
St does satisfy the log-normal equation (6.10). This ‘justifies’ our formal
application of the Itˆo formula.
Exercise 6.4.10. Let B be a Brownian motion, and suppose that the pro-
cesses X, Y have dynamics given by
dXt
=
Xt(µXdt + σXdBt),
dYt
=
Yt(µY dt + σY dBt).
Define Z by Zt = Yt
Xt . Show that Z is also log-normal, with dynamics
dZt = Zt(µZdt + σZdBt),
and determine the coefficients µZ and σZ in terms of the coefficients of X
and Y.
Multidimensional Itˆo Processes
Definition 6.4.11. Suppose we have a probability space (Ω, F, P) with
a filtration (Ft)t≥0. An m-dimensional (Ft)-Brownian motion is a process
Wt =

W 1
t , W 2
t , . . . , W m
t

whose components W i
t are standard, indepen-
dent (Ft)-Brownian motions.
We can extend our definition of an Itˆo process to the situation where the
(scalar) stochastic integral involves an m-dimensional Brownian motion.
Definition 6.4.12. (Xt)0≤t≤T is an Itˆo process if
Xt = X0 +
 t
0
Ksds +
m

i=1
 t
0
Hi
sdW i
s,
where the K and Hi are adapted to (Ft),
4 T
0 |Ks| ds < ∞a.s., and
 T
0
''Hi
s
''2 ds < ∞a.s. for all i = 1, 2, . . . , m.
An n-dimensional Itˆo process is then a process Xt = (X1
t , . . . , XN
t ),
each component of which is an Itˆo process in the sense of Definition 6.4.12.
The differentiation rule takes the following form.
Theorem 6.4.13. Suppose Xt = (X1
t , . . . , XN
t ) is an n-dimensional Itˆo
process with
Xi
t = Xi
0 +
 t
0
Ki
sds +
m

j=1
 t
0
Hij
s dW j
s ,

156
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
and suppose f :[0,T]×Rn →R is in C1,2 (the space of functions once
continuously differentiable in t and twice continuously differentiable in x ∈
Rn). Then
f(t, X1
t , . . . , Xn
t ) = f(0, X1
0, . . . , Xn
0 ) +
 t
0
∂f
∂s (s, X1
s, . . . , Xn
s )ds
+
n

i=1
 t
0
∂f
∂xi
(s, X1
s, . . . , Xn
s )dXi
s
+ 1
2
n

i,j=1
 t
0
∂2f
∂xi∂xj
(s, X1
s, . . . , Xn
s )d
7
Xi, Xj8
s .
Here
dXi
s = Ki
sds +
m

j=1
Hi,j
s dW j
s ,
d
7
Xi, Xj8
s =
m

r=1
Hi,r
s Hj,r
s ds.
Remark 6.4.14. For components
Xp
t = Xp
0 +
 t
0
Kp
s ds +
m

j=1
 t
0
Hpj
s dW j
s ,
Xq
t = Xq
0 +
 t
0
Kq
sds +
m

j=1
 t
0
Hqj
s dW j
s ,
it is shown in [227] that for partitions π = {0 = t0 ≤t1 ≤· · · ≤tN = t},
lim
|π|→0

i

Xp
ti+1 −Xp
ti
 
Xq
ti+1 −Xq
ti

converges in probability to
 t
0
m

r=1
Hpr
s Hqr
s ds.
This process is the predictable covariation of Xp and Xq and is denoted by
⟨XpXq⟩t =
m

r=1
 t
0
Hpr
s Hqr
s ds.
(6.11)
We note that ⟨XpXq⟩is symmetric and bilinear as a function on Itˆo pro-
cesses.
Taking
Yt = Y0 +
 t
0
K′
sds,
Xt = X0 +
 t
0
Ksds +
m

j=1
Hj
sdW j
s ,

6.4. THE IT ˆO CALCULUS
157
we see that ⟨X, Y ⟩t = 0. Furthermore, formula (6.11) gives
9 t
0
Hpi
s dW i
s,
 t
0
Hqj
s dW j
s
:
=
4 t
0 Hpi
s Hqi
s ds
if i = j,
0
if i ̸= j.
Remark 6.4.15. We noted in 6.4.5 that if (Mt)t≥0 is a continuous local
martingale, then ⟨M⟩t is the unique continuous increasing process in the
Doob-Meyer decomposition of the submartingale M 2
t . If
Xt = X0 +
 t
0
Ksds +
 t
0
HsdMs,
where H and K are adapted,
4 T
0 |Ks| ds < ∞a.s., and
4 T
0 H2
s ds < ∞a.s.,
the differentiation formula has the form
f(Xt) = f(X0) +
 t
0
∂f
∂x(Xs)Ksds
+
 t
0
∂f
∂x(Xs)HsdMs + 1
2
 t
0
∂2f
∂x2 (Xs)H2
s d ⟨M⟩s .
Using without proof the analogue of the Itˆo rule (Theorem 6.4.6) for
general square integrable martingales M (see [109, p. 138]), we can prove
the converse of Theorem 6.2.5.
Theorem 6.4.16. Suppose (Wt)t≥0 is a continuous (scalar) local martin-
gale on the filtered probability space (Ω, F, P, Ft), such that

W 2
t −t

t≥0 is
a local martingale. Then (Wt) is a Brownian motion.
Proof. We must show that, for 0 ≤s ≤t, the random variable Wt −Ws is
independent of Fs and is normally distributed with mean 0 and covariance
t −s.
In terms of characteristic functions, this means we must show that
E

eiu(Wt−Ws) |Fs

= E

eiu(Wt−Ws)
= exp
$
−u2(t −s)
2
%
for all u ∈R.
To this end, consider the (complex-valued) function
f(x) = eiux.
Applying the differentiation rule to the real and imaginary parts of f(x),
we have
f(Wt) = eiuWt = f(Ws) +
 t
s
iueiuWrdWr −1
2
 t
s
u2eiuWrdr
(6.12)
because d ⟨W⟩r = dr by hypothesis. Furthermore, the real and imaginary
parts of iu
4 t
s eiuWrdWr are in fact square integrable martingales because

158
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
the integrands are bounded by 1. Consequently, E

iu
4 t
s eiuWrdWr |Fs

=
0 a.s. For any A ∈Fs, we may multiply (6.12) by 1Ae−iuWs and take
expectations to deduce that
E

eiu(Wt−Ws)1A

= P(A) −1
2u2
 t
0
E

eiu(Wr−Ws)1A

dr.
Solving this equation, we have
E

eiu(Wt−Ws)1A

= P(A) exp
$
−u2(t −s)
2
%
.
6.5
Stochastic Differential Equations
We first establish a useful result known as Gronwall’s lemma.
Lemma 6.5.1. Suppose α and β are integrable functions on [a, b]. If there
is a constant H such that
α(t) ≤β(t) + H
 t
a
α(s)ds for t ∈[a, b],
(6.13)
then
α(t) ≤β(t) + H
 t
a
eH(t−s)β(s)ds.
Note that if β(t) = B, a constant, then
α(t) ≤BeH(t−a).
(6.14)
Proof. Write
A(t) =
 t
a
α(s)ds,
g(t) = A(t)e−Ht.
Then
g′(t) = α(t)e−Ht −HA(t)e−Ht ≤β(t)e−Ht
from (6.13). Integrating, we obtain
g(t) −g(a) ≤
 t
a
β(s)e−Hsds.
That is,
A(t) ≤eHt
 t
a
β(s)e−Hsds.

6.5. STOCHASTIC DIFFERENTIAL EQUATIONS
159
Using (6.13) again, we have
α(t) ≤β(t) + HA(t) = β(t) + H
 t
a
β(s)eH(t−s)ds.
Definition 6.5.2. Suppose (Ω, F, P) is a probability space with a filtra-
tion (Ft)0≤t≤T . Let (Wt) = ((W 1
t , . . . , W m
t )) be an m-dimensional (Ft)-
Brownian motion and f(x, t) and σ(x, t) be measurable functions of x ∈Rn
and t ∈[0, T] with values in Rn and L(Rm, Rn), the space of m × n ma-
trices, respectively. We take ξ to be an Rn-valued, F0-measurable random
variable.
A process Xt, 0 ≤t ≤T is a solution of the stochastic differential
equation
dXt = f(Xt, t)dt + σ(Xt, t)dWt
with initial condition X0 = ξ if for all t the integrals
 t
0
f(Xs, s)ds and
 t
0
σ(Xs, s)dWs
are well-defined and
Xt = ξ +
 t
0
f(Xs, s)ds +
 t
0
σ(Xs, s)dWs a.s.
(6.15)
Theorem 6.5.3. Suppose the assumptions of Definition 6.5.2 apply. In
addition, assume that ξ, f, and σ satisfy
|f(x, t) −f(x′, t)| + |σ(x, t) −σ(x′, t)| ≤K |x −x′| ,
(6.16)
|f(x, t)|2 + |σ(x, t)|2 ≤K2
0

1 + |x|2
,
(6.17)
E

|ξ|2
< ∞.
Then there is a solution X of (6.15) such that
E

sup
0≤t≤T
|Xt|2

< C

1 + E

|ξ|2
.
Note, for the matrix σ, that |σ|2 = Tr(σσ∗). This solution is unique in the
sense that, if X′
t is also a solution, then they are indistinguishable in the
sense of Definition 6.1.12.
Proof. Uniqueness: Suppose that X and X′ are solutions of (6.15). Then,
for all t ∈[0, T],
Xt −X′
t =
 t
0
(f(Xs, s) −f(X′
s, s)) ds +
 t
0
(σ(Xs, s) −σ(X′
s, s)) dWs.

160
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
Therefore
|Xt −X′
t|2 ≤2
 t
0
(f(Xs, s) −f(X′
s, s)) ds
2
+ 2
 t
0
(σ(Xs, s) −σ(X′
s, s)) dWs
2
.
Taking expectations, we obtain
E

|Xt −X′
t|2
≤2
 t
0
E

(f(Xs, s) −f(X′
s, s))2
ds
+ 2
 t
0
E

|σ(Xs, s) −σ(X′
s, s)|2
ds.
Write φ(t) = E

|Xt −X′
t|2
and use the Lipschitz conditions (6.16) to
deduce that
φ(t) ≤2(T + 1)K2
 t
0
φ(s)ds.
Gronwall’s inequality (Lemma 6.5.1) therefore implies that φ(t) = 0 for all
t ∈[0, T]. Consequently,
|Xt −X′
t| = 0 a.s.
The process |Xt −X′
t| is continuous, so there is a set N ∈F0 of measure
zero such that if ω /∈N, Xt(ω) = X′
t(ω) for all t ∈[0, T]. That is, X′ is a
modification of X.
Existence: Write X0
t = ξ for 0 ≤t ≤T. Define a sequence of processes

XN
t

by
XN
t
= ξ +
 t
0
f(Xn−1
s
, s)ds +
 t
0
σ(Xn−1
s
, s)dWs.
(6.18)
It can be shown that σ(Xn−1
s
, s) ∈H, so the stochastic integrals are de-
fined.
Using arguments similar to those in the uniqueness proof, we can show
that
E
''Xn+1
t
−XN
t
''2
≤L
 t
0
E
''Xn
s −Xn−1
s
''2
ds,
(6.19)
where L = 2(1 + T)K2. Iterating (6.19), we see that
E
''Xn+1
t
−XN
t
''2
≤Ln
 t
0
(t −s)n−1
(n −1)! E
''X1
s −ξ
''2
ds

6.5. STOCHASTIC DIFFERENTIAL EQUATIONS
161
and
E
''X1
s −ξ
''2
≤LTK2 
1 + E

|ξ|2
.
Therefore
E
''Xn+1
t
−XN
t
''2
≤C T n
n! .
(6.20)
Also,
sup
0≤t≤T
''Xn+1
t
−XN
t
'' ≤
 T
0
''f (Xn
s , s) −f

Xn−1
s
, s
'' ds
+ sup
0≤t≤T
''''
 t
0

σ(Xn
s , s) −σ(Xn−1
s
, s)

dWs
'''' ;
so, using the vector form of Doob’s inequality (Corollary 6.2.17), we have
E

sup
0≤t≤T
''Xn+1
t
−Xn
t
''2
≤2TK2
 T
0
E
''Xn
s −Xn−1
s
''2
ds
+ CE
 T
0
''Xn
s −Xn−1
s
''2 ds

≤C1
T n−1
(n −1)!
using (6.20). Consequently,
∞

n=1
P

sup
0≤t≤T
''Xn+1
t
−Xn
t
'' > 1
n2

≤
∞

n=1
n4C1
T n−1
(n −1)!.
The series on the right converges.
Therefore, almost surely, the series
ξ + ∞
n=0(Xn+1
t
−Xn
t ) converges uniformly in t, and so Xn
t converges to
some Xt uniformly in t.
Each Xn is a continuous process, so X is a continuous process. Now
E

|Xn
t |2
≤3
.
E

|ξ|2
+ K2
0T
 t
0

1 + E
''Xn−1
s
''2
ds
+K2
0
 t
0

1 + E
''Xn−1
s
''2
ds
/
,
so
E

|Xn
t |2
≤C

1 + E

|ξ|2
+ C
 t
0
E
''Xn−1
s
''2
ds.

162
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
By recurrence, taking C > 1,
E

|Xn
t |2
≤

1 + E

|ξ|2 
C + C2t + · · · + Cn−1 tn
n!

≤C

1 + E

|ξ|2
eCt.
Using the bounded convergence theorem, we can take the limit in (6.18) to
deduce that
Xt = ξ +
 t
0
f(Xs, s)ds +
 t
0
σ(Xs, s)dWs a.s.
Therefore, X is the unique solution of the equation (6.15).
6.6
Markov Property of Solutions of SDEs
Definition 6.6.1. Let (Ω, F, P) be a probability space with filtration
(Ft)t≥0.
An adapted process (Xt) is said to be a Markov process with
respect to the filtration (Ft) if
E (f(Xt) |Fs ) = E (f(Xt) |Xs ) a.s. for all t ≥s ≥0
for every bounded real-valued Borel function f defined on Rd.
Consider a stochastic differential equation as in (6.15) with coefficients
satisfying the conditions of Theorem 6.5.3 so the solution exists. Consider
a point x ∈Rn and for s ≤t write Xs(x, t) for the solution process of the
equation
Xs(x, t) = x +
 t
s
f (Xs(x, u), u) du +
 t
s
σ (Xs(x, u), u) dWu.
(6.21)
We quote the following results.
Theorem 6.6.2. Xs(x, t) is a continuous function of its arguments, and
if the coefficients f and σ are C1 functions of their first argument, the
solution Xs(x, t) is C1 in x.
Proof. See Kunita [204].
Write Xs(x, t, ω) for the solution of (6.21), so Xs(x, t, ω) : Rd × [s, T] ×
Ω→Rd, and FW (s, t) for the completion of the σ-field generated by
Ws+u −Ws, 0 ≤u ≤t −s.
Theorem 6.6.3. For t ∈[s, T], the restriction of Xs(x, u, ω) to Rd×[s, t]×
Ωis B(Rd) × B([s, t]) × FW (s, t)-measurable.
Proof. [109, Lemma 14.23].

6.6. MARKOV PROPERTY OF SOLUTIONS OF SDES
163
We next prove the ‘flow’ property of solutions of equation (6.21).
Lemma 6.6.4. If Xs(x, t) is the solution of (6.21) and Xr(x, t) is the
solution of (6.21) starting at time r with r ≤s ≤t, then Xr(x, t) =
Xs (Xr(x, s), t) in the sense that one is a modification of the other.
Proof. By definition,
Xr(x, t) = x +
 t
r
f (Xr(x, u), u) du +
 t
r
σ (Xr(x, u), u) dWu
= Xr(x, s) +
 t
s
f (Xr(x, u), u) du +
 t
s
σ (Xr(x, u), u) dWu.
(6.22)
However, for any y ∈Rn,
Xs(y, t) = y +
 t
s
f (Xs(y, u), u) du +
 t
s
σ (Xs(y, u), u) dWu.
Therefore, using the continuity of the solution,
Xs (Xr(x, s), t) = Xr(x, s) +
 t
s
f (Xs(Xr(x, s), u), u) du
+
 t
s
σ (Xs(Xr(x, s), u), u) dWu.
(6.23)
Using the uniqueness of the solution, we see from (6.22) and (6.23) that
Xr(x, s) is a modification of Xs (Xr(x, s), t).
Before establishing the Markov property of solutions of (6.21), we prove
a general result on conditional expectations.
Lemma 6.6.5. Given a probability space (Ω, G, P) and measurable spaces
(E, E), (F, F), suppose that A ⊂G and X : Ω→E and Y : Ω→F are
random variables such that X is A-measurable and Y is independent of A.
For any bounded real-valued Borel function Φ defined on (E ×F, E ×F),
consider the function φ defined for all x ∈E by
φ(x) = E (Φ(x, Y )) .
Then φ is a Borel function on (E, E) and
E (Φ(X, Y ) |A ) = φ(X) a.s.
Proof. Write PY for the probability law of Y . Then
φ(x) =

F
Φ(x, y)dPY (y).

164
CHAPTER 6. CONTINUOUS-TIME STOCHASTIC CALCULUS
The measurability of Φ follows from Fubini’s theorem.
Suppose Z is any A-measurable random variable. Write PX,Z for the
probability law of (X, Z). Then, because Y is independent of (X, Z),
E (Φ(X, Y )Z) =

Φ(x, y)zdPX,Z(x, z)dPY (y)
=
 
Φ(x, y)dPY (y)

zdPX,Z(x, z)
=

φ(x)zdPX,Z(x, y)
= E (φ(X)Z) .
This identity is true for all such Z; the result follows.
Lemma 6.6.6. Suppose Xs(x, t, ω) is the solution of (6.21) and g : Rd →
R is a bounded Borel-measurable function. Then
f(x, ω) = g (Xs(x, t, ω))
is B(Rd) × FW (s, t)-measurable.
Proof. Write A for the collection of sets A ∈B(Rd) for which the lemma
is true with g = 1A. If f(x, ω) = 1A (Xs(x, t, ω)), then
{(x, ω) : f(x, ω) = 1} = {(x, ω) : Xs(x, t, ω) ∈A} ∈B(Rd) × FW (s, t).
The lemma is therefore true for all A ∈B(Rd), and the result follows for
general g by approximation with simple functions.
We now show that solutions of stochastic differential equations of the
form (6.21) are Markov processes with respect to the right-continuous (and
completed) filtration (Ft) generated by the Brownian motion (Wt)t≥0 and
the initial value x ∈Rd.
Theorem 6.6.7. Suppose X0(x, t) is the solution of (6.21) such that
X0(x, 0) = x ∈Rd. For any bounded real-valued Borel function g defined
on Rd, we have
E (g(Xt) |Fs ) = E (g(Xt) |Xs ) for all 0 ≤s ≤t.
More precisely, if
φ(z) = E (g (Xs(z, t))) ,
then
E (g(Xt) |Fs ) = φ (X0(x, s)) a.s.
Proof. Suppose g : Rd →R is any bounded Borel-measurable function. As
in Lemma 6.6.6, write f(x, ω) = g (Xs(x, t, ω)). Then, for each x ∈Rd,
f(x, ·) is FW (s, t)-measurable and thus independent of Fs.

6.6. MARKOV PROPERTY OF SOLUTIONS OF SDES
165
Write, as in Lemma 6.6.5,
φ(x) = E (g (Xs(x, t, ω))) .
If Z is any Fs-measurable random variable,
E (g (Xs(Z, t, ω)) |Fs ) = φ(Z).
(6.24)
From the flow property of the solutions, Lemma 6.6.4, it follows that
Xt = X0(x, t) = Xs (X0(x, s), t)
and X0(x, s) is Fs-measurable. Substituting Z = X0(x, s) in (6.24), there-
fore,
E (g (X0(x, t)) |Fs ) = E (g(Xt) |Fs ) = φ (X0(x, s)) = φ(Xs).
Consequently, E (g(Xt) |Fs ) = E (g(Xt) |Xs ) and the result follows.
Theorem 6.6.8. Suppose X0(x, s) = Xs ∈Rd is the solution of (6.21),
and consider the process
βs(1, t) = βt = e−
 t
s r(u,Xu)du,
where r(s, x) is a positive measurable function. Then
dβt = −r(t, Xt)βtdt,
βs = 1,
and the augmented process (βt, Xt) ∈Rd+1 is given by an equation similar
to (6.21). Consequently, the augmented process is Markov and, for any
bounded Borel function f : Rd →R,
E

e−
 t
s r(u,Xu)duf(Xt) |Fs

= φ(Xs),
where
φ(x) = E

e−
 t
s r(u,Xs(x,u))duf (Xs(x, t))

.

Chapter 7
Continuous-Time
European Options
In this chapter, we shall develop a continuous-time theory that is the ana-
logue of that in Chapters 1 to 3. The simple model will consist of a riskless
bond and a risky asset, which can be thought of as a stock. The dynamics of
our model are described in Section 7.1. The following two sections present
the fundamental results of Girsanov and martingale representation. These
are then applied to discuss the hedging and pricing of European options.
In particular, we establish the famous results of Black and Scholes, results
that are applied widely in the finance industry in spite of the simplified
nature of the model. Recall that the Black-Scholes pricing formula for a
European call was derived in Section 2.7 as the limit of a sequence of prices
in binomial models.
7.1
Dynamics
We describe the dynamics of the Black-Scholes option pricing model. Our
processes will be defined on a complete probability space (Ω, F, P). The
time parameter t will take values in the intervals [0, ∞) or [0, T]. We suppose
the market contains a riskless asset, or bond, whose price at time t is S0
t ,
and a risky asset, or stock, whose price at time t is S1
t .
Let r be a non-negative constant that represents the instantaneous in-
terest rate on the bond. (This instantaneous interest rate should not be
confused with the interest rate over a period of time in discrete models.)
We then suppose that the evolution in the price of the bond S0
t is described
by the ordinary differential equation
dS0
t = rS0
t dt.
(7.1)
If the initial value at time 0 of the bond is S0
0 = 1, then (7.1) can be solved
167

168
CHAPTER 7. CONTINUOUS-TIME EUROPEAN OPTIONS
to give
S0
t = ert for t ≥0.
(7.2)
Let µ and σ > 0 be constants and (Bt)t≥0 be a standard Brownian
motion on (Ω, F, P). We suppose that the evolution in the price of the
risky asset S1
t is described by the stochastic differential equation
dS1
t = S1
t (µdt + σdBt).
(7.3)
If the initial price at time 0 of the risky asset is S1
0, then (7.3) can be
solved to give
S1
t = S1
0 exp
$
µt −σ2
2 t + σBt
%
.
(7.4)
Taking logarithms, we have
log S1
t = log S1
0 +

µ −σ2
2

t + σBt,
(7.5)
and we see that log S1
t evolves like a Brownian motion with drift (µ −σ2
2 )t
and volatility σ. In particular, log S1
t is a normal random variable, which
is often expressed by saying S1
t is ‘log-normal’. It is immediate from (7.4)
and (7.5) that

S1
t

has continuous trajectories, and log S1
t has independent
stationary increments (so S1
t −S1
v
S1
v
is independent of the σ-field σ(S1
u : u ≤v)
and S1
t −S1
v
S1
v
is identically distributed to
S1
t−v−S1
0
S1
0
).
7.2
Girsanov’s Theorem
Girsanov’s theorem shows how martingales, in particular Brownian motion,
transform under a different probability measure. We first define certain
spaces of martingales.
The set of martingales for which convergence results hold is the set of
uniformly integrable martingales. As we noted in Chapters 5 and 6, this
is not a significant restriction if the time horizon is finite (i.e., T < ∞).
Recall Definition 5.3.1 applied to a martingale: if (Mt) is a martingale, for
0 ≤t < ∞or 0 ≤t ≤T, (Mt) is uniformly integrable if

{|Mt(ω)|≥K}
|Mt(ω)|dP(ω)
converges to 0 uniformly in t as K →∞.
If (Xt)t≥0 is any real, measurable process, we shall write
X∗
t = sup
s≤t
|Xs| .
We shall write M for the space of right-continuous, uniformly integrable
martingales. Consistent with Notation 6.2.9, Mℓoc will denote the set of

7.2. GIRSANOV’S THEOREM
169
processes that are locally in M (i.e., we say that M ∈Mℓoc if there exists
an increasing sequence of stopping times (Tn) such that MTn
t
= Mt∧Tn ∈
M). We call Mℓoc the space of local martingales. Let L be the subset of
Mℓoc consisting of those local martingales for which M0 = 0 a.s.
For M ∈M and p ∈[1, ∞], write
∥M∥Hp = ∥M ∗
∞∥p .
Here ∥·∥p denotes the norm on Lp(Ω, F, P). Then Hp is the space of mar-
tingales in M such that
∥M∥Hp < ∞.
In particular, H2 is the space of square integrable martingales.
Suppose (Ω, F, P) is a probability space with a filtration (Ft)t≥0. Let
Q be a second probability measure on (Ω, F) that is absolutely continuous
with respect to P. Write
Mt =

dQ
dP
if t = ∞,
E (M∞|Ft )
if t < ∞.
Remark 7.2.1. In continuous time, versions of martingales are considered
that are right-continuous and have left limits. There is a right-continuous
version of M with left limits if the filtration (Ft) satisfies the usual condi-
tions (see [109, Theorem 4.11]).
Lemma 7.2.2. (XtMt) is a local martingale under P if and only if (Xt)
is a local martingale under Q.
Proof. We prove the result for martingales. The extension to local martin-
gales can be found in [168, Proposition 3.3.8]. Suppose s ≤t and A ∈Fs.
Then

A
XtdQ =

A
XtMtdP =

A
XsMsdP =

A
XsdQ,
and the result follows.
Suppose (Ω, F, P) is a probability space. Recall from Theorem 6.4.16
that a real process (Bt)t≥0 is a standard Brownian motion if:
a) t →Bt(ω) is continuous a.s.,
b) Bt is a (local) martingale, and
c) B2
t −t is a (local) martingale.
This characterisation of Brownian motion using properties a)-c) is due
to L´evy, and it is shown in Theorem 6.4.16 that these properties imply the
other well-known properties of Brownian motion, including, for example,
that B is a Gaussian process with independent increments.
Write F0
t = σ (Bs : s ≤t) for the σ-field on Ωgenerated by the history
of the Brownian motion up to time t. Then (Ft)t≥0 will denote the right-
continuous complete filtration generated by the F0
t .
We show how (Bt) behaves under a change of measure.

170
CHAPTER 7. CONTINUOUS-TIME EUROPEAN OPTIONS
Theorem 7.2.3 (Girsanov). Suppose (θt)0≤t≤T is an adapted, measur-
able process such that
4 T
0 θ2
sds < ∞a.s. and also so that the process
Λt = exp
$
−
 t
0
θsdBs −1
2
 t
0
θ2
sds
%
is an (Ft, P) martingale. Define a new measure Qθ on FT by putting
dQθ
dP
''''
FT
= ΛT .
Then the process
Wt = Bt +
 t
0
θsds
is a standard Brownian motion on (Ft, Qθ).
Remark 7.2.4. A sufficient condition, widely known as Novikov’s condition,
for Λ to be a martingale is that
E

exp

1
2
 T
0
θ2
sds
&
< ∞
(see [109]).
Proof. Using the Itˆo rule and definition of Λ, we see, as in Exercise 6.4.9,
that
Λt = 1 −
 t
0
ΛsθsdBs.
(7.6)
Clearly Λt > 0 a.s. and as Λ is a martingale
E (Λt) = 1.
Now for A ∈FT , Qθ(A) =
4
A ΛT dP ≥0 and Qθ(Ω) =
4
ΩΛT dP =
E (Λt) = 1, so Qθ is a probability measure.
To show that (Wt) is a standard Brownian motion, we verify that it
satisfies the conditions a)-c) above, which are required for the application
of Theorem 6.4.16.
By definition, (Wt) is a continuous process almost
surely, as (Bt) is continuous a.s. and an indefinite integral is a continuous
process.
For the second condition, we must show that (Wt) is a local
(Ft)-martingale under the measure Qθ. Equivalently, from Lemma 7.2.2
we must show that (ΛtWt) is a local martingale under P. Applying the Itˆo
rule to (7.6) and (Wt), we have
ΛtWt = W0 +
 t
0
ΛsdWs +
 t
0
WsdΛs +
 t
0
d ⟨Λ, W⟩s
= W0 +
 t
0
ΛsdBs +
 t
0
Λsθsds −
 t
0
WsΛsθsdBs −
 t
0
Λsθsds

7.2. GIRSANOV’S THEOREM
171
= W0 +
 t
0
Λs(1 −Wsθs)dBs
and, as a stochastic integral with respect to B, (ΛtWt) is a (local) martin-
gale under P.
The third condition is established similarly since
W 2
t = 2
 t
0
WsdWs + ⟨W⟩t = 2
 t
0
WsdWs + t.
We must prove that W 2
t −t is a local (Ft, Qθ)-martingale. However,
W 2
t −t = 2
 t
0
WsdWs,
and we have established that Ws is a (local) martingale under Qθ. Con-
sequently, the stochastic integral is a (local) martingale under Qθ and the
result follows.
Hitting Times of Brownian Motion
We shall need the following results on hitting times of Brownian motion.
Their proofs involve an exponential martingale M of a form similar to Λ.
Suppose (Bt)t≥0 is a standard Brownian motion with B0 = 0 adapted to
the filtration (Ft). Write
Ta = inf {s ≥0 : Bs = a} for a ∈R.
(7.7)
As usual, we take inf {∅} = ∞.
Theorem 7.2.5. Ta in (7.7) is a stopping time that is almost surely finite
and
E

e−λTa
= e−
√
2λ|a| for λ ≥0.
Proof. Suppose a ≥0. Because B is continuous, we have, with Q+ denoting
the positive rationals,
{Ta ≤t} =
0
ε∈Q+
$
sup
r≤t
Br > a −ε
%
=
0
ε∈Q+
0
r∈Q+
r≤t
{Br > a −ε} ∈Ft.
Consequently, Ta is a stopping time.
For any σ ≥0, the process
Mt = exp
$
σBt −σ2
2 t
%

172
CHAPTER 7. CONTINUOUS-TIME EUROPEAN OPTIONS
is an (Ft)-martingale by Theorem 6.2.5. For n ∈Z+, consider the stopping
time Ta ∧n. Then, from the optional stopping theorem (Theorem 6.2.10),
we have
E (MTa∧n) = E (M0) = 1.
However,
MTa∧n = exp
$
σBTa∧n −σ2
2 (Ta ∧n)
%
≤exp {σa} .
Now if Ta < ∞, then limn→∞MTa∧n = MTa. If Ta = ∞, then Bt ≤a for
all t ≥0, so that limn→∞MTa∧n = 0.
Using Lebesgue’s dominated convergence theorem, we have
E

1{Ta<∞}MTa

= 1.
(7.8)
Now BTa = a if Ta < ∞. Therefore,
E

1{Ta<∞}eσae−σ2
2 Ta
= 1;
consequently,
E

1{Ta<∞}e
σ2
2 Ta
= e−σa.
(7.9)
Letting σ →0 in (7.9), we see that
E

1{Ta<∞}

= P(Ta < ∞) = 1.
Hence almost every sample path of the Brownian motion reaches the value
a, and
E

e
−σ2
2
Ta
= e−σa.
Now (−Bt) is also an (Ft)-Brownian motion, so the case a < 0 can be
deduced by noting that
Ta = inf
s≥0 {s ≥0 : −Bs = −a} .
An application of Girsanov’s theorem enables us to deduce the following
extension.
Corollary 7.2.6. Suppose µ, a are real numbers. Write
Ta(µ) = inf {t ≥0 : µt + Bt = a} .
Then
E

e−αTa(µ)
= exp

µa −|a|

µ2 + 2α

for all α > 0.

7.2. GIRSANOV’S THEOREM
173
Proof. Introduce the probability measure Q by setting
dQ
dP
''''
Ft
= exp
$
µBt −µ2
2 t
%
.
From Girsanov’s theorem, the process -B is a standard Brownian motion
under Q, where
-Bt = Bt −µt.
Clearly, the hitting time Ta(µ) of -Bt + µt is the same as the hitting time
Ta(0) of Bt. Therefore, for all α > 0 and t > 0, we have
E (exp {−α(Ta(µ) ∧t)})
= E

exp {−α(Ta(0) ∧t)} exp
$
µBTa(0)∧t −µ2
2 (Ta(0) ∧t)
%
.
Now exp {−α(Ta(0) ∧t)} ≤e−αt. Noting that Ta(0) = Ta, we have for
t < Ta that t < ∞. Therefore
exp
$
µBTa∧t −µ2
2 (Ta ∧t)
%
1{t<Ta} ≤exp
$
µBt −µ2
2 t
%
,
which has expected value 1, and
E

exp {−α(Ta ∧t)} exp
$
µBTa∧t −µ2
2 (Ta ∧t)
%
1{t<Ta}

≤e−αt.
Suppose initially that a ≥0, and write
;
Mt = exp {−α(Ta ∧t)} exp
$
µBTa∧t −µ2
2 (Ta ∧t)
%
.
Then ;
Mt ≤exp {µa} and, again by the dominated convergence theorem,
E

lim
t→∞
;
Mt

= E

1{t<Ta}e−αTaeµBTa−µ2
2 Ta

= eµaE

1{Ta<∞}e−(α+ µ2
2 )Ta

= eµae−√
2α+µ2|a|.
Again the case when a < 0 can be discussed by considering −B.
We have therefore established that
E

1{Ta<∞}e−αTaeµBTa−µ2
2 Ta

= E

1{Ta(µ)<∞}e−αTa(µ)
= eµa−√
2α+µ2|a|.

