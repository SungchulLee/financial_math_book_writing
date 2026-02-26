# Bonds & Term Structure Models

!!! info "Source"
    **Mathematics of Financial Markets** by Robert J. Elliott and P. Ekkehard Kopp, Springer, 2nd ed., 2005.
    These notes are used for educational purposes.

## Bonds and Term Structure

8.5. RELATION TO FREE BOUNDARY PROBLEMS
241
Theorem 8.5.5. Suppose D ⊂R+ × [0, T) is an open domain with a
continuously differentiable boundary c.
Furthermore, suppose f ∈C3,1, that g(x, t) = f(ex, t) has Tychonov
growth and L (e−rtf(x, t)) = 0 on D, and
f(x, T) = (K −x)+ for x ∈R+,
f(x, t) > (K −x)+ for (x, t) ∈D,
f(x, t) = (K −x)+ for (x, t) ∈R+ × [0, T) ∩Dc,
lim
x↓c(t) fx(x, t) = −1 for t ∈[0, T).
Then f(x, t) = P(x, t), the American put function, D = C, the continuation
region, and c(t) = S∗
t , the optimal stopping boundary.
We require the following extension of the harmonic property of P on C.
Lemma 8.5.6. On R+ ×[0, T], we have L (e−rtP(x, t)) ≤0 in the sense of
Schwartz distributions. (This shows that the American put value function
P is ‘r-excessive’.)
Proof. Choose ε > 0, and consider the set of stopping times
Vε =

τ : t ≤τ ≤T, -E

e−r(τ−t)(K −Sτ)+ |St

≥P(St, t) −ε

.
For all t ∈[0, T), this set is non-empty. Choose τε ∈Vε and write -Ex (·)
for the -Q-expectation given S0 = x. Then
-Ex

e−rτε(K −Sτε)+
= -Ex

e−rt -E

e−r(τε−t) (K −Sτε)+ |St

≥-Ex

e−rtP(St, t)

−εe−rt.
However, by definition,
P(S0, 0) = P(x, 0) ≥-Ex

e−rτε(K −Sτε)+
≥-Ex

e−rtP(St, t)

−εe−rt.
Letting ε ↓0 gives
P(x, 0) ≥-Ex

e−rtP(St, t)

.
This inequality implies the result, as any excessive function is the limit
of an increasing sequence of infinitely differentiable excessive functions (see
Port and Stone [243]).
Lemma 8.5.7. The American put function P(x, t) satisfies

L

e−rtP(x, t)
 
(K −x)+ −P(x, t)

= 0 for (x, t) ∈R+ × [0, T].
Proof. In the continuation region, we know that L (e−rtP(x, t)) = 0. In the
stopping region, P(x, t) = (K −x)+.

242
CHAPTER 8. THE AMERICAN PUT OPTION
Definition 8.5.8. For any m ∈Z+ and λ > 0, write Hm,λ for the space of
measurable, real-valued functions f on R whose derivatives, in the sense of
distributions, up to and including the mth order, belong to L2(R, e−λ|x|dx).
Write
∥f∥=
 m

i=0

R
''∂if(x)
''2 e−λ|x|dx
 1
2
.
The space L2([0, T], Hm,λ) is the set of measurable functions g : [0, T] →
Hm,λ such that

[0,T ]
∥g(t)∥2 dt < ∞.
In [169], Jaillet, Lamberton, and Lapeyre extend the work of Bensous-
san and Lions ([24]) to show that the American put value function is char-
acterized by a variational inequality. Their result is as follows.
Theorem 8.5.9. Consider a continuous function f defined on R+ × [0, T]
that satisfies
f(e·, ·) ∈L2([0, T], H2,λ),
ft(e·, ·) ∈L2([0, T], H0,λ)
and
f(x, t) ≥(K −x)+ for (x, t) ∈R+ × [0, T),
f(x, T) = (K −x)+ for x ∈R+,
L

e−rtf(x, t)

≤0

L

e−rtf(x, t)
 
f(x, t) −(K −x)+
= 0
where (x, t) ∈R+ × [0, T].
Then f is unique and equals the American put value function P.
Remark 8.5.10. The application of variational inequalities gives rise to a
numerical algorithm. In fact, the early numerical work of Brennan and
Schwartz [33] was justified for the American put, using variational inequal-
ities, by Jaillet, Lamberton, and Lapeyre [169].
The most widely used numerical technique for calculating the American
option value is dynamic programming. The risky asset price S is modelled
as evolving on a binomial tree in discrete time. The Bellman equation is
then solved recursively by evaluating
Pi = max

(K −Si)+, e−r∆-E (Pi+1 |Fi )

with final condition PT = (K −ST )+.

8.6. AN APPROXIMATE SOLUTION
243
8.6
An Approximate Solution
We have seen that the American put function P(x, t) can be written
P(x, t) = p(x, t) + e(x, t),
where
p(x, t) = -Ex

e−r(T −t)(K −ST )+
is the European put value, and
e(x, t) = -Ex
 T
t
e−r(u−t)rK1{Su<S∗
u}du

is the ‘early exercise’ premium.
The early exercise premium involves the critical price, or free boundary,
S∗, and is consequently difficult to evaluate.
Allegretto, Barone-Adesi, and Elliott [5] proposed an approximation for
e(x, t) of the form
ε(x, t) = A(t)
 x
S∗
t
q(t)
,
where A and q are functions of t that are to be determined.
Now we know that, in the continuation region C, we have
L[ertP(x, t)] = 0,
L

e−rtP(x, t)

= 0.
(8.22)
Also, at the critical price,
P(S∗
t , t) = (K −S∗
t )+,
∂P
∂x
''''
x=S∗
t
= −1.
(8.23)
Now LP(x, t) = 0 in C and LP(x, t) = 0 in C, so
L[e−rte(x, t)] = 0,
(8.24)
in C. Substituting P = p + A(t)

S
S∗
t
q(t)
in (8.23), we have
p(S∗
t , t) + A(t) = K −S∗
t
and
A(t)q(t)
S∗
t
−e−(µ−r)(T −t)Φ(−d1(S∗
t , t)) = −1,
(8.25)
where Φ is the standard normal distribution and
d1(x, t) =
log

x
S∗
t

+

µ + σ2
2

(T −t)
σ
√
T −t
.

244
CHAPTER 8. THE AMERICAN PUT OPTION
However, we also would like L[e−rtε(x, t)] = 0. This is the case if
1
2σ2q(t)(q(t) −1)A(t)
 x
S∗
t
q(t)
−rA(t)
 x
S∗
t
q(t)
+ A(t)µq(t)
 x
S∗
t
q(t)
+ ∂
∂t
 x
S∗
t
q(t)
= 0.
(8.26)
Now
∂
∂t

A(t)
 x
S∗
t
q(t)
= dA(t)
dt
 x
S∗
t
q(t)
−dS∗
t
dt
A(t)q(t)
x
  x
S∗
t
q(t)+1
+ dq(t)
dt A(t)
 x
S∗
t
q(t)
log
 x
S∗
t

.
Substituting this into (8.26) and dividing by A(t)

x
S∗
t
q(t)
implies that
1
2σ2q(t)(q(t) −1) −r + µq(t) +

1
A(t)
dA(t)
dt
−q(t)
S∗
t
dS∗
t
dt

+ log
 x
S∗
t
 dq(t)
dt
= 0.
(8.27)
However, this equation indicates that q is not independent of x, and so
e(x, t) is not of the form given by ε(x, t). Nonetheless, a useful approxima-
tion is obtained by neglecting the last term of (8.27). That is, we suppose
q(t) is a solution of
1
2σ2q(t)(q(t) −1) −r + µq(t) +

1
A(t)
dA(t)
dt
−q(t)
S∗
t
dS∗
t
dt

= 0.
(8.28)
This approximation is reasonable when log

x
S∗
t

· dq(t)
dt
is small. This is the
case when x is in a neighbourhood of S∗
t or when dq(t)
dt
is small (at long
maturities).
From equation (8.25), we have
dA(t)
dt
=

e(µ−r)(T −t)Φ (−d1(S∗
t , t)) −1
 dS∗
t
dt −∂p(x, t)
∂t
.
From the second equation of (8.25),
1
A(t)
dA(t)
dt
−q(t)
S∗
t
dS∗
t
dt = −
1
A(t) · ∂p(S∗
t , t)
∂t
.
Writing
g(t) =
1
A(t)
∂p(S∗
t , t)
∂t
,
M = 2r
σ2 ,
N = 2b
σ2 ,
G(t) = 2q(t)
σ2 ,

8.6. AN APPROXIMATE SOLUTION
245
equation (8.28) becomes
q(t)2 + (N −1)q(t) −(M −G(t)) = 0.
To satisfy the boundary condition of zero at x = ∞, we consider only the
root
q(t) = 1
2

1 −N −

(1 −N)2 + 4(M + G(t))

.
With this value of q(t), an approximation for the early exercise premium is
ε(x, t) = A(t)
 x
S∗
t
q(t)
.
To summarise, we have the following system of three equations in three
unknowns A(t), q(t), and S∗
t :
S∗
t =
(K −p(S∗
t , t))q(t)
−1 + q(t) + e(µ−r)(T −t)Φ(−d1(S∗
t , t)),
(8.29)
A(t) = −p(S∗
t , t) −S∗
t + K,
(8.30)
0 = q(t)2 + (N −1)q(t) −M + G(t).
(8.31)
For a fixed value of t, these equations can be solved using the following
iterative procedure.
(i) Give a trial value of S∗
t .
(ii) Calculate A(t) from (8.30).
(iii) Calculate q(t) from (8.31).
(iv) Calculate a new value of S∗
t from (8.29).
Using the new value for S∗
t , steps (ii)-(iv) are repeated.
This algorithm was investigated numerically in [5] and shown to give
satisfactory results.

Chapter 9
Bonds and Term
Structure
9.1
Market Dynamics
Suppose (Ω, F, P) is a probability space, (Bt)0≤t≤T is a Brownian motion,
and (Ft) is the (complete, right-continuous) filtration generated by B. We
first review the martingale pricing results of Chapter 7.
Consider again the case of a bond S0 and a single risky asset S1. We
suppose
S0
t = exp
$ t
0
rudu
%
,
S1
t = S1
0 +
 t
0
µ(u)S1
udu +
 t
0
σ(u)S1
udBu.
Here r, µ and σ are adapted (random) processes.
In particular, r is a
stochastic interest rate in general. Consider a self-financing trading strat-
egy (H0, H1). The corresponding wealth process is
Xt = H0
t S0
t + H1
t S1
t ,
and
dXt = rH0
t S0
t dt + H1
t dS1
t = r

Xt −H1
t S1
t

dt + H1
t dS1
t .
With θt = µ(t)−rt
σ(t)
(which requires σ ̸= 0), the process W θ, where
dW θ
t = θtdt + dBt,
is a Brownian motion under the measure P θ. Consequently, under P θ the
discounted wealth process is Xt
S0
t , and
d
Xt
S0
t

= H1
t σ(t)S1
t
S0
t
dW θ
t .
247

248
CHAPTER 9. BONDS AND TERM STRUCTURE
That is, for any self-financing strategy, the discounted wealth process

Xt
S0
t

is a martingale under the martingale measure P θ.
Consider a contingent claim h ∈L2(Ω, FT ). Then
Mt = Eθ
 h
S0
t
|Ft

is a martingale. Using the martingale representation result Theorem 7.3.9,
Mt = M0 +
 t
0
φudW θ
u.
If we take
H1
t = S0
t φt
σ(t)S1
t
,
X0 = M0 = Eθ
 h
S0
t

,
and write
Mt = Xt
S0
t
= X0 +
 t
0
H1
uσ(t)S1
u
S0u
dW θ
u,
then, with
H0
t = Xt
S0
t
−H1
t
S1
t
S0
t
,
the pair (H0, H1) is a self-financing strategy that hedges the claim h. That
is,
XT = H0
T S0
t + H1
T S1
T = h.
The fair price for the claim at time 0 is Eθ 
h
S0
t

; the price at time t ∈[0, T]
is Xh(t) = Xt, and this equals
S0
t Eθ
 h
S0
t
|Ft

= S0
t Eθ
XT
S0
T
|Ft

because

Xt
S0
t

is a martingale under P θ.
Suppose we have a market with several risky assets S0
t , S1
t , . . . , SN(t)
with dynamics
dS0
t = rtS0
t dt,
S0
0 = 1,
dSi
t = Si
t
⎛
⎝µi(t)dt +
m

j=1
σij(t)dWj(t)
⎞
⎠,
Si
0 = si for i = 1, 2, . . . , n.
Here (Wt) = (W1(t), . . . , Wm(t)) is an m-dimensional Brownian motion
on (Ω, F, P). The risk-neutral pricing formula holds as long as there is a
unique risk-neutral measure P θ, as introduced in Chapter 7. In such an
example the price at time t ≤T of a claim h ∈L2(FT ) is
Xt = S0
t Eθ 
h · (S0
T )−1 |Ft

.

9.1. MARKET DYNAMICS
249
Notation 9.1.1. From now on in this chapter, we assume we are working in
a market where there is a unique risk-neutral measure P θ. The superscript
θ will be dropped. For simplicity, we suppose there is a single risky asset
that has dynamics (under P θ = P)
dS1
t = rtS1
t dt + σ(t)S1
t dWt.
Further, we suppose the martingale representation result holds, so that
every (Ft, P)-martingale has a representation as a stochastic integral with
respect to W.
Definition 9.1.2. A zero coupon bond maturing at time T is a claim that
pays 1 at time T.
From the pricing formula, its value at time t ∈[0, T] is
B(t, T) = S0
t E
 1
S0
T
|Ft

.
As S0
t = exp
4 t
0 rudu

, this is
B(t, T) = E

exp

−
 T
t
rudu
&
|Ft

.
Consequently, given B(t, T) dollars at time t, one can construct a self-
financing hedging strategy (H0
t , H1
t ) such that the corresponding wealth
process
Xt = H0
t S0
t + H1
t S1
t
has value 1 at time T.
If the instantaneous rate rt is deterministic, then
B(t, T) = exp

−
 T
t
rudu
&
and
dB(t, T) = rtB(t, T)dt,
so H1
t is identically 0.
Definition 9.1.3. The T-forward price F(t, T) for the risky asset S1 is a
price agreed at time t ≤T (and thus Ft-measurable) that will be paid for
S1 at time T.
Such a price F(t, T) is characterised by requiring that the claim S1
T −
F(t, T) has (discounted) value 0 under the risk-neutral (martingale) mea-
sure P. Therefore,
0 = E
S1
T −F(t, T)
S0
T
|Ft

= E
S1
T
S0
T
|Ft

−F(t, T)
S0
t
E
 S0
t
S0
T
|Ft


250
CHAPTER 9. BONDS AND TERM STRUCTURE
= S1
t
S0
t
−F(t, T)
S0
t
B(t, T)
because the discounted price
S1
S0 is a martingale under the measure P.
Therefore F(t, T) =
S1
t
B(t,T ).
Remark 9.1.4. The forward price can be defined for other claims. Indeed,
suppose h ∈L2(Ω, FT ) is a contingent claim with exercise date T. The
T-forward price for h, denoted by F(h, t, T), is the Ft-measurable random
variable that has the property that
E
h −F(h, t, T)
S0
T
|Ft

= 0.
Consequently,
F(h, t, T) =
S0
t E

S0
T
−1 h |Ft

B(t, T)
= Xh(t)
B(t, T),
where Xh(t) is, from the pricing discussion, the fair price for h at time t.
In particular, h could be the zero coupon bond of maturity T ∗≥T.
Then
F (B(T, T ∗), t, T) = B (t, T ∗)
B(t, T) .
Definition 9.1.5. Define a new probability measure QT , equivalent to P,
on (Ω, FT ) by setting
dQT
dP
''''
FT
=

S0
T
−1
E

(S0
T )−1 =
1
S0
T B(0, T).
The measure QT is called the forward measure for the settlement date
T. It was introduced in [140] and [170]. Define
Γt = E
dQT
dP |Ft

= E

1
S0
T B(0, T) |Ft

=
B(t, T)
S0
t B(0, T).
The process Γ is a (P, Ft)-martingale, so there is an integrand γ(s, T) such
that
Γt = 1 +
 t
0
γ(s, T)dWs.
Now Γs > 0 a.s. for all s; define
β(s, T) = Γ−1
s γ(s, T).
Then
Γt = 1 +
 t
0
Γsβ(s, T)dWs,

9.1. MARKET DYNAMICS
251
and so
Γt = exp
 T
0
β(s, T)dWs −1
2
 T
0
β(s, T)2ds
&
.
The next lemma shows how the forward price can be expressed in terms
of the forward measure.
Lemma 9.1.6. Suppose that h ∈L2(Ω, FT ) is a contingent claim with
exercise time T. Then
F(h, t, T) = EQT (h |Ft ) .
Consequently, the forward price of h is a QT -martingale.
Proof. Using Bayes’ rule, we have
EQT (h |Ft ) = E (ΓT h |Ft )
E (ΓT |Ft ) = E

Γ−1
t ΓT h |Ft

.
Substituting the expressions for Γ, the result follows.
Remark 9.1.7. Consider the T-forward price for the contingent claim h ∈
L2(Ω, FT ) at time 0,
F(h, 0, T) = Xh(0)
B(0, T).
By definition, F(h, 0, T) is the price, agreed at time 0, that one will pay
at time T for the claim h. The related claim V = h −F(h, 0, T) has price
0 at time 0. However, at later times t ∈[0, T], this claim V does not have
value 0. Indeed, using the pricing formula, at time t it has value
Vt = S0
t E
h −F(h, 0, T)
S0
T
|Ft

= Xh(t) −F(h, 0, T)
B(t, T) .
One can hedge this claim as follows. At time 0, one shorts F(h, 0, T)
zero coupon bonds with maturity T. This provides an amount
F(h, 0, T)
B(0, T)
= Xh(0)
B(0, T) · B(0, T) = Xh(0),
where Xh(0) is the price of the claim h at time 0. Consequently, this amount
Xh(0) can be used at time 0 to buy the claim h. This strategy requires no
initial investment. If this position is held until time T, it is then worth
Xh(T) −F(h, 0, T)
B(T, T)
= h −F(h, 0, T).

252
CHAPTER 9. BONDS AND TERM STRUCTURE
9.2
Future Price and Futures Contracts
Suppose a contingent claim h has a price $h at time T. (By abuse of nota-
tion, we write h for the claim and its price at time T.)
Clearly, at time T, one need not pay anything for the right to buy the
claim for $h. Therefore, at time T, the price of the claim is G(h, T, T) = h.
(Note that this assumes there are no transaction costs, and we are not
discussing problems of delivering the claim itself-we are thinking of a cash
settlement.)
Suppose initially there are only a finite number of trading times t0, . . . , tn
with 0 = t0 < t1 < · · · < tn = T. Furthermore, suppose that ru is constant
on each interval [ti, ti+1). Then
S0
tj+1 = exp
 tj+1
0
rudu = exp
 n

i=0
rti(ti+1 −ti)
&
,
and S0
tj+1 is Ftj-measurable.
Consider the time tn−1 and suppose the price agreed at time tn−1 for
the claim, (to be delivered at time tn = T) is
G(h, tn−1, T).
Then the difference in the price agreed at time tn−1 and the price at tn = T
is
G(h, tn, T) −G(h, tn−1, T).
At time tn−1, one estimates G(h, tn−1, T), given the information Ftn−1, so
that this difference, discounted and conditioned on Ftn−1, is zero; that is,
so that the claim G(h, tn, T) −G(h, tn−1, T) has value zero at time tn−1,
namely
S0
tn−1E
G(h, tn, T) −G(h, tn−1, T)
S0
tn
''Ftn−1

= 0.
Similarly, at time tn−2, one estimates G(h, tn−2, T) so that
S0
tn−2E

G(h, tn−1, T) −G(h, tn−2, T)
S0
tn−1
''Ftn−2

= 0.
Here G(h, tn−2, T) is the estimate at time tn−2 of the price of the claim h
at time T.
Consequently, the value at time t = tk of the sum of future adjustments
is
S0
tkE
⎛
⎝
n−1

j=k
G(h, tj+1, T) −G(h, tj, T)
S0
tj+1
|Ftk
⎞
⎠= 0.
The continuous-time version of this condition gives
S0
t E
 T
t

S0
u
−1 dG(h, u, T) |Ft

= 0 for t ∈[0, T].
(9.1)

9.2. FUTURE PRICE AND FUTURES CONTRACTS
253
Write
Mt =
 t
0

S0
u
−1 dG(h, u, T).
Then (9.1) implies that
E (Mt |Fs ) = Ms for 0 ≤s ≤t ≤T.
That is, M is an (Ft, P)-martingale. Consequently,
 t
0
S0
udMu = G(h, t, T) −G(h, 0, T)
is an (Ft, P)-martingale. Therefore, as G(h, T, T) = h,
G(h, t, T) = E (h |Ft )
is the ‘future price’ at time t for the claim h. This motivates the following
definition.
Definition 9.2.1. The T-future price G at time t of the FT -measurable
contingent claim h is
G(h, t, T) = E (h |Ft ) .
By definition, G(h, t, T) is a martingale under P.
Lemma 9.2.2.
a)

S0
T
−1 and h are (conditionally) uncorrelated if and
only if F(h, t, T) = G(h, t, T).
b) If

S0
T
−1 and h are positively correlated conditional on Ft, then
G(h, t, T) ≤F(h, t, T).
Proof. The T-future price is
G(h, t, T) = E (h |Ft ) .
The T-forward price is
F(h, t, T) = Xh(t)
B(t, T) = EQ (h |Ft ) =
E

h
S0
T |Ft

E

(S0
T )−1 |Ft
.
Part (a) follows immediately. Part (b) states that
E
) 
(S0
t )−1 −E(S0
t
−1 |Ft )

(h −E (h |Ft )) |Ft
*
≥0,
and the result follows.
Remark 9.2.3. The hypothesis of the second part of the lemma arises when
the stock price tends to rise with a fall in the interest rate and conversely.
Holding a futures contract is not advantageous if there is a positive corre-
lation between

S0
t
−1 and h. Therefore, a buyer of a futures contract is
compensated by the lower future price compared with the forward price.

254
CHAPTER 9. BONDS AND TERM STRUCTURE
Futures Contracts
We have noticed that forward contracts possibly have non-zero value. In
contrast, a futures contract is constructed so that the risk of default inher-
ent in a forward contract is eliminated.
The value at time 0 of a forward contract, entered into at time 0, is 0.
However, at later times t ∈[0, T] it has value
Vt = Xh(t) −F(h, 0, T)
B(t, T) .
In contrast to a forward contract, the value of a futures contract is
maintained at zero at all times. Consequently, either party to the contract
can close his or her position at any time.
This is done by marking to
market.
To describe this process, suppose again that trading takes place only at
the finite number of times t0, . . . , tn with 0 = t0 < t1 < · · · < tn = T and
that ru is constant on each interval [ti, ti+1).
At time tk, the future price of the claim h is G(h, tk, T) = E (h |Ftk ) .
Suppose we buy a futures contract at this price. At the time tk+1, the
future price of h is G(h, tk+1, T).
If G(h, tk+1, T) > G(h, tk, T), the buyer of the futures contract receives
a payment of
G(h, tk+1, T) −G(h, tk, T).
If G(h, tk+1, T) < G(h, tk, T), then the buyer of the futures contract makes
a payment of
G(h, tk, T) −G(h, tk+1, T).
To make or receive these payments, a margin account is held by the broker.
At the final time T = tn, the buyer of the futures contract will have
received payments
G(h, tk+1, T) −G(h, tk, T), G(h, tk+2, T) −G(h, tk+1, T),
. . . , G(h, tn, T) −G(h, tn−1, T)
at times tk+1, . . . , tn = T. The value at time t = tk of this sequence of
payments is
S0
t E
n−1

i=k
G(h, ti+1, T) −G(h, ti, T)
S0
ti+1
|Ft

.
The future price G(h, t, T) is such that the cost of entering a futures con-
tract at any time is zero.
Consequently, the value of this sequence of
payments at time t must be 0.
With a continuum of trading times, the sum above becomes a stochastic
integral and the condition is
S0
t E
 T
t

S0
u
−1 dG(h, u, T) |Ft

= 0.

9.3. CHANGING NUM´ERAIRE
255
Now by definition G(h, t, T) = E (h |Ft ) is a martingale. This integral is
therefore a stochastic integral with respect to a martingale and so, under
standard conditions, has conditional expectation zero.
With a T-forward contract, the only payment is at time T: the buyer
agrees at time 0 to pay F(h, 0, T) for the claim h at time T.
With a T-futures contract, the buyer receives a (positive or negative)
cash flow from time 0 to time T. If he still holds the contract at time T,
he pays an amount h at time T for the claim, which has value h. Between
time 0 and time T, the buyer has received an amount
 T
0
dG(h, u, T) = G(h, T, T) −G(h, 0, T) = h −G(h, 0, T).
Therefore, at time T he has paid an amount −(h −G(h, 0, T)) + h =
G(h, 0, T) for the claim that has value h at time T.
9.3
Changing Num´eraire
Consider again the situation described in Notation 9.1.1, where, under a
risk-neutral measure P, there is a risky asset S1 with dynamics
dS1
t = rtS1
t dt + σ(t)S1
t dWt.
Here W is a Brownian motion on a probability space (Ω, F, P) with a
filtration (Ft)0≤t≤T ∗. In general, (Ft) may be larger than the filtration
generated by W. The short-term rate r and volatility σ are adapted (ran-
dom) processes. The value of a dollar in the money market is, as before,
S0
t = exp
4 t
0 rudu

. We note that
d
S1
t
S0
t

= S1
t
S0
t
σ(t)dWt,
so the discounted asset price is a martingale.
When we consider the discounted price S1
t
S0
t , we are saying that, at time t,
one unit of stock is worth S1
t
S0
t units of the money market account. Similarly,
from the expression after Definition 9.1.2 at time t, with T ≤T ∗, the T-
maturity bond is worth B(t,T )
S0
t
units of the money market account; again
this discounted price is E

S0
t
−1 |Ft

and so is a martingale.
Now any strictly positive price process could play the role of S0, and
other assets can be expressed in terms of this process. As in the discrete-
time setting, we have the following
Definition 9.3.1. A strictly positive process Z is the num´eraire of the
model if all asset prices are expressed in terms of Z.

256
CHAPTER 9. BONDS AND TERM STRUCTURE
For example, the T-maturity bond price B(t, T) could be taken as the
num´eraire for t ≤T. In terms of B(t, T), at time t, the risky asset is worth
S1
t
B(t,T ) = F(t, T) units of B(t, T), where B(t, T) is the forward price of
Definition 9.1.3. Of course, the price of the bond itself in terms of the
num´eraire B(t, T) is just B(t,T )
B(t,T ) = 1 unit.
We could also, for example, take S1 to be the num´eraire. Then the
price at time t of a T-maturity bond in units of S1
t is B(t,T )
S1
t
=
1
F (t,T ).
Definition 9.3.2. Suppose Z is a strictly positive process so Z can be
taken as a num´eraire. A probability measure PZ on (Ω, F, P) is said to be
risk-neutral for Z if the price of any asset divided by Z (i.e., expressed in
units of Z) is a martingale under PZ.
We assumed in Notation 9.1 that the original measure P was risk-
neutral for the num´eraire S0.
Theorem 9.3.3. Suppose Z is a num´eraire, so it is the strictly posi-
tive price process of some asset. Define a new probability measure PZ on
(Ω, F, P) by putting for any A ∈FT ∗
PZ(A) = 1
Z0

A
ZT
S0
T
dP.
Then PZ is equivalent to P and is a risk-neutral measure for the num´eraire
Z.
Proof. Note that, for A ∈FT ∗,
P(A) = Z0

A
S0
T Z−1
T dPZ,
so P and PZ have the same null sets.
From the definition of P, Z
S0 is a martingale under P. Consequently,
PZ(Ω) = 1
Z0

Ω
ZT
S0
T
dP = 1
Z0
E
ZT
S0
T

=
Z0
Z0S0
0
= 1
because
Z
S0 is a P-martingale. Consequently, PZ is a probability measure.
Now suppose X is an asset price process, so
X
S0 is a P-martingale. We
shall show that X
Z is then a PZ-martingale. We have
Mt =
Zt
Z0S0
t
= 1
Z0
E
 ZT ∗
S0(T ∗) |Ft

because
Z
S0 is a P-martingale. From Lemma 7.2.2, X
Z is a PZ-martingale if
and only if X
Z M =
1
Z0
X
Z
Z
S0 is a P-martingale. The result follows.

9.3. CHANGING NUM´ERAIRE
257
Remark 9.3.4. Note that, if we take the num´eraire Z to be the bond price
B(t, T) for 0 < T ≤T ∗, then the risk-neutral measure PB(t,T ) for this bond
has a density
B(T, T)
B(0, T)S0
T
=
1
B(0, T)S0
T
.
Consequently, the risk-neutral measure for the bond B is just the forward
measure given in Definition 9.1.5. Note that, as the bond is not defined
after time T, the measure change is defined only on FT , that is, only up to
time T.
With the T-maturity bond as num´eraire, we have seen that the price of
the risky asset S1 is given by its forward price
F(t, T) =
S1
t
B(t, T) for 0 ≤t ≤T.
Now F(t, T) must be a martingale under the risk-neutral measure PB(t,T )
for B and consequently the differential dF(t, T) must be of the form
dF(t, T) = σF (t, T)F(t, T)dWB(t) for 0 ≤t ≤T.
(9.2)
We note that this is a differential without any bounded variation dt
terms and WB(t), 0 ≤t ≤T, is a process that is a standard Brownian
motion under the measure PB(t, T). As usual, σF (t, T) can be taken to be
non- negative.
Suppose now the price S1 of the risky asset is taken as the num´eraire.
Of course, in terms of S1, the price of the risky asset S1 is always 1 unit.
The risk-neutral measure for the num´eraire S1 is defined by
PS(A) = 1
S1
0

A
S1(T ∗)
S0(T ∗)dP for A ∈FT ∗.
In terms of units of S1, the value of a T-maturity bond is just
B(t, T)
S1
t
=
1
F(t, T) for 0 ≤t ≤T ≤T ∗.
However, this is to be a martingale under PS, so it has a differential
d

1
F(t, T)

= σF −1(t, T)

1
F(t, T)

dWS(t) for 0 ≤t ≤T ≤T ∗.
(9.3)
Again there will be no dt terms in the differential, and (WS(t))0≤t≤T is
a standard Brownian motion under PS. Again, σF −1(t, T) can be taken as
non-negative.
Theorem 9.3.5. σF (t, T) = σF −1(t, T).

258
CHAPTER 9. BONDS AND TERM STRUCTURE
Proof. Applying the Itˆo rule to (9.3), we have
d

1
F(t, T)

= −
1
F(t, T)2 σF (t, T)F(t, T)dWB(t)
+
1
F(t, T)3 σF (t, T)2F(t, T)2dt
= σF (t, T)

1
F(t, T)

(−dWB(t) + σB(t, T)dt) .
(9.4)
We know that (WB(t)) is a standard Brownian motion under PB(t,T ), as
is (−WB(t)). Therefore, under PB(t,T ) the process
1
F (t,T ) has volatility
σF (t, T) and mean rate of return σF (t, T)2. Changing the measure from
PB(t,T ) to PS transforms
1
F (t,T ) into a PS-martingale. Consequently, un-
der PS the mean rate of return of
1
F (t,T ) is zero, but the volatility is not
changed. In fact, from (9.4)
d

1
F(t, T)

= σF −1(t, T)
1
F(t, T)dWS(t) for 0 ≤t ≤T ≤T ∗.
(9.5)
Comparing (9.4) and (9.5), we see that
σF (t, T) = σF −1(t, T),
WS(t) = −WB(t) +
 t
0
σF (s, T)ds.
9.4
A General Option Pricing Formula
Following El Karoui, Geman, and Rochet [102] the risk-neutral measures
for the num´eraires S1 and B can be used to express the price of a European
call option:
V0 = E

S0
T
−1 
S1
T −K
+
= E

S0
T
−1 S1
T 1{S1
T >K}

−KE

S0
T
−1 1{S1
T >K}

= S1
0

{S1
T >K}
S1
T
S1
0S0
T
dP −KB(0, T)

{S1
T >K}
1
B(0, T)S0
T
dP
= S1
0PS

S1
T > K

−KB(0, T)PB

S1
T > K

= S1
0PS (F(T, T) > K) −KB(0, T)PB (F(T, T) > K)
= S1
0PS

1
F(T, T) < 1
K

−KB(0, T)PB (F(T, T) > K) .
Let us suppose that σF (t, T) is a constant σF . Then, from (9.3), recalling
that σF = σF −1, we have
1
F(T, T) = B(0, T)
S1
0
exp
$
σF WS(T) −1
2σ2
F T
%

9.4. A GENERAL OPTION PRICING FORMULA
259
where WS is a standard Brownian motion under PS. Consequently,
PS

1
F(T, T) < 1
K

= PS

σF WS(T) −1
2σ2
F T < log

S1
0
KB(0, T)

= PS
WS(T)
√
T
<
1
σF
√
T
log

S1
0
KB(0, T)

+ 1
2σF
√
T

.
Now WS(T )
√
T
is a standard normal random variable. Writing, as usual,
Φ for the standard normal distribution, we have
PS

1
F(T, T) < 1
K

= Φ(h1),
where
h1 =
1
σF
√
T

log

S1
0
KB(0, T)

+ 1
2σ2
F T

.
From (9.2), we have that, with PB = PB(t, T),
F(T, T) =
S1
0
B(0, T) exp
$
σF WB(T) −1
2σ2
F T
%
,
where WB is a standard Brownian motion under PB. Therefore
PB (F(T, T) > K) = PB

σF WB(T) −1
2σ2
F T > log
KB(0, T)
S1
0

= PB
WB(T)
√
T
<
1
σF
√
T

log
KB(0, T)
S1
0

+ 1
2σ2
F T

= PB

−WB(T)
√
T
<
1
σF
√
T

log

S1
0
KB(0, T)

−1
2σ2
F T

.
Again, WB(T )
√
T
is a standard normal random variable, so that
PB (F(T, T) > K) = Φ(h2),
where
h2 =
1
σF
√
T

log

S1
0
KB(0, T)

−1
2σ2
F T

.
Consequently, the price of the European call is
V0 = S1
0Φ(h1) −KB(0, T)Φ(h2).
If r is constant, then B(0, T) = e−rT and this formula reduces to the
Black-Scholes formula of Theorem 7.6.2.
A modification of this argument shows that for any intermediate time
0 ≤t ≤T, the value of the European call, with strike price K and expiration
time T, is
Vt = S1
t Φ(h1(t)) −KB(0, T)Φ(h2(t)),
(9.6)

260
CHAPTER 9. BONDS AND TERM STRUCTURE
where now, recalling that F(t, T) =
S1
t
B(t,T ),
h1(t) =
1
σF
√
T −t

log
F(t, T)
K

+ 1
2σ2
F (T −t)

,
h2(t) =
1
σF
√
T −t

log
F(t, T)
K

−1
2σ2
F (T −t)

.
Formula (9.6) suggests the European call can be hedged, at each time t, by
holding Φ(h1(t)) units of S1 and shorting KΦ(h2(t)) bonds.
We shall establish that this is a self-financing strategy. However, first
we show that a change of num´eraire does not change a trading strategy.
Lemma 9.4.1. Suppose S1, S2, . . . , Sd are the price processes of k assets.
Consider a self-financing strategy (θ1, θ2, . . . , θd), where θi
t represents the
number of units of asset i held at time t. Suppose Z is a num´eraire and
,Si = Si
Z , 1 ≤i ≤d, is the price of asset i in units of Z. Then θi represents
the number of units of ,Si in the portfolio, evaluated in terms of the new
num´eraire (there are no other riskless assets).
Proof. The wealth process is
Xt =
d

i=1
θi
tSi
t.
As the strategy is self-financing, we have
dXt =
d

i=1
θi
tdSi
t.
Write ,
Xt = Xt
Zt for the wealth process expressed in terms of the num´eraire
Z. Then
d ,
X = Z−1dX + Xd
 1
Z

+ d
9
X, 1
Z
:
= 1
Z
d

i=1
θidSi +
 d

i=1
θiSi

d
 1
Z

+
d

i=1
θid
9
Si, 1
Z
:
=
d

i=1
θid,Si.
Corollary 9.4.2. In Lemma 9.4.1, the strategy

θ1, θ2, . . . , θd
determined
the wealth process X. Suppose now that components θ1, θ2, . . . , θd−1 are
given, together with the wealth process X. Then
θd
t = 1
Sd
t

Xt −
d−1

i=1
θi
tSi
t


9.4. A GENERAL OPTION PRICING FORMULA
261
and
dXt =
d

i=1
θi
tdSi
t =
d−1

i=1
θi
tdSi
t + 1
Sd
t

Xt −
d−1

i=1
θi
tSi
t

dSd
t .
In terms of the num´eraire Z, we still have
θd
t = 1
Sd
t

Xt −
d−1

i=1
θi
tSi
t

= 1
,Sd
t

,
Xt −
d−1

i=1
θi
t ,Si
t

and
d ,
Xt =
d−1

i=1
θi
td,Si
t + 1
,Sd
t

,
Xt −
d−1

i=1
θi
t ,Si
t

d,Sd
t .
Let us return to the price (9.6) at time t for a European call option.
Theorem 9.4.3. Holding Φ(h1(t)) units of S1 and shorting KΦ(h2(t))
bonds at each time t ∈[0, T] is a self-financing strategy for the European
call option with strike price K and expiration time T.
Proof. This result could be established using Theorem 9.4.1. Alternatively,
suppose we start with an initial investment of $V0 and hold Φ(h1(t)) units
of S1 at each time t. To maintain this position, we short as many bonds as
necessary.
If we can show that the number of bonds we must short at time t is
KΦ(h2(t)), then the value of our portfolio is indeed
Φ(h1(t))S1
t −KB(t, T)Φ(h2(t)),
which equals Vt, the price of the call option at time t ∈[0, T], and we have
a hedge.
Let us write θ1
t = Φ(h1(t)) so that at time t we hold θ1
t units of S1.
Suppose Xt is the value of our portfolio at time t.
Then we invest
Xt −θ1
t S1
t in the bond and the number of bonds in the portfolio is
θ2
t = Xt −θ1
t S1
t
B(t, T) .
Then
dXt = θ1
t dS1
t + θ2
t dB(t, T) = θ1
t dS1
t + Xt −θ1
t S1
t
B(t, T) dB(t, T).
We must show that, if X0 = V0, then
Xt = Vt for 0 ≤t ≤T.
To establish this, it is easier to work with B(t, T) as num´eraire. In terms
of this zero coupon bond, the asset values S1, B, and X become
,S1
t =
S1
t
B(t, T) = F(t, T),

262
CHAPTER 9. BONDS AND TERM STRUCTURE
,B(t, T) = 1,
,
Xt = Φ(h1(t))F(t, T) + ,
Xt −θ1
t S1
t ,
and d ,
Xt = Φ(h1(t))dF(t, T).
The option value is
Vt = Φ(h1(t))S1
t −KB(t, T)Φ(h2(t)),
and in terms of the num´eraire B(t, T) this becomes
,Vt = Φ(h1(t))F(t, T) −KΦ(h2(t)).
Consequently,
d,Vt = Φ(h1(t))dF(t, T) + F(t, T)dΦ(h1(t)) −KdΦ(h2(t))
+ d ⟨Φ(h1(t)), F(t, T)⟩.
Recall the dynamics (9.2) given by
dF(t, T) = σF F(t, T)dWB(t).
Now consider (Φ(h1(t))), where
h1(t) =
1
σF
√
T −t

log
F(t, T)
K

+ 1
2σ2
F (T −t)

.
The Itˆo rule gives, after some cancellation, with φ as the standard normal
density,
dΦ(h1(t)) = φ(h1) ·
1
σF
√
T −t · 1
F dF −φ(h1)
σF
2
√
T −tdt,
where φ is the standard normal density function.
Also, Fφ(h1) = Kφ(h2), and some elementary but tedious calculations
confirm that
FdΦ(h1) −KdΦ(h2) + d ⟨Φ(h1), F⟩= 0.
The result follows.
9.5
Term Structure Models
Again let W be a standard Brownian motion on (Ω, F, P) and (Ft)0≤t≤T
the (completed) filtration generated by W.
The instantaneous interest rate rt is an adapted, measurable process
and the num´eraire asset S0
t has value
S0
t = exp
$ t
0
rudu
%
for 0 ≤t ≤T.

9.5. TERM STRUCTURE MODELS
263
We have seen that the price at time t ∈[0, T] of a zero coupon bond
maturing at time T is
B(t, T) = S0
t E

S0
t
−1 |Ft

.
If r is non-random, then
B(t, T) = exp

−
 T
t
rudu
&
.
Zero coupon bonds are traded in the market, and their prices can be
used to calibrate the model. They are known as ‘zeros’.
Definition 9.5.1. A term structure model is a mathematical model for the
prices B(t, T) for all t and T with 0 ≤t ≤T ≤T2.
The yield R(t, T) = log B(t,T )
T −t
provides a yield curve for each fixed time
t as the graph of R(t, T) against T, which displays the average return
of bonds after elimination of the distorting effects of maturity. We expect
different yields at different maturities, reflecting market beliefs about future
changes in interest rates. While greater uncertainty about interest rates
in the distant future will tend to lead to increases in yield with maturity,
high current rates (which may be expected to fall) can produce ‘inverted’
yield curves, in which long bonds will have a lower yield than short ones. A
satisfactory term structure model should be able to handle both situations.
Remark 9.5.2. Recall that we are working under a martingale, or risk-
neutral, measure P and that
B(t, T) = S0
t E

S0
t
−1 |Ft

.
That is,
B(t, T)
S0
t
= E

S0
t
−1 |Ft

,
and so

B(t,T )
S0
t

is a martingale under P.
If the market measure P does not have the property that all processes

B(t,T )
S0
t

are martingales, then the term structure model is free of arbitrage
only if there is an equivalent measure -P such that, under -P, all processes

B(t,T )
S0
t

are martingales for all maturity times T.
B(t, T) is a positive process for all T, so that, using the martingale
representation theorem, dynamics for B(t, T) can be expressed in a log-
normal form
dB(t, T) = µ(t, T)B(t, T)dt + σ(t, T)B(t, T)dWt for t ∈[0, T].

264
CHAPTER 9. BONDS AND TERM STRUCTURE
Consequently,
d
B(t, T)
S0
t

= (µ(t, T) −rt) B(t, T)
S0
t
dt + σ(t, T)B(t, T)
S0
t
dWt
and

B(t,T )
S0
t

is a martingale under P if and only if µ(t, T) = rt.
The statement that
B(t, T) = E

exp

−
 T
t
rudu
&
|Ft

is sometimes called the Local Expectations Hypothesis.
The assumption that holding a discount bond to maturity gives the
same return as rolling over a series of single-period bonds is called the
Return to Maturity Expectations Hypothesis. In continuous time, it would
state that, under some probability P ′,
1
B(t, T) = EP ′

exp
 T
t
rudu
&
|Ft

.
The Yield to Maturity Expectations Hypothesis states that the yield
from holding a bond equals the yield from rolling over a series of single-
period bonds. In continuous time, this would imply
B(t, T) = exp

−EP ′
 T
t
rudu |Ft
&
for some probability P ′. A fuller discussion of these concepts can be found
in the papers of Frachot and Lesne [137], [138].
9.6
Short-rate Diffusion Models
Vasicek’s Model
Vasicek [296] proposed a mean-reverting version of the Ornstein-Uhlenbeck
process for the short term rate r. Specifically, under the risk-neutral mea-
sure P, r is given by
drt = a(b −rt)dt + σdWt
for r0 > 0, a > 0, b > 0, and σ > 0. Then
rt = e−at

r0 + b

eat −1

+ σ
 t
0
eaudWu

.
Consequently, rt is a normal random variable with mean
E (rt) = e−at 
r0 + b

eat −1


9.6. SHORT-RATE DIFFUSION MODELS
265
and variance
Var(rt) = σ2
1 −e−2at
2a

.
However, a normal random variable can be negative with positive proba-
bility so this model for r is not too realistic (unless the probability of being
negative is small). Nonetheless, its simplicity validates its discussion.
As t →∞, we see that rt converges in law to a Gaussian random
variable with mean b and variance σ2
2a.
The price of a zero coupon bond in the Vasicek model is therefore
B(t, T) = E

exp

−
 T
t
rudu
&
|Ft

= e−b(T −t)E

exp

−
 T
t
Xudu
&
|Ft

,
(9.7)
where Xu = ru −b. Now X is the solution of the classical Ornstein-
Uhlenbeck equation
dXt = −aXtdt + σdWt,
(9.8)
with X0 = r0 −b. Write
Z(t, x) = E

exp
$
−
 t
0
X(u, x)du
%
,
(9.9)
where X(u, x) is the solution of (9.2) with X(0, x) = x. Now
X(u, x) = e−au

x +
 u
0
σeasdWs

,
so X(u, x) is a Gaussian process with continuous sample paths. Conse-
quently,
4 t
0 X(u, x)du

is a Gaussian process; this can be established by
considering moment-generating functions exp {u1X(t1) + · · · + unX(tn)}.
If Y is a Gaussian random variable with E (Y ) = m and Var(Y ) = γ2,
we know that
E

eY 
= e−m+ 1
2 γ2.
Now
E (X(u, x)) = xe−au,
E
 t
0
X(u, x)du

= x
a

1 −e−at
,
and
Cov[X(t, x), X(u, x)] = σ2e−a(u+t)E
 t
0
easdWs
 u
0
easdWs

= σ2e−a(u+t)
 u∧t
0
e2asds

266
CHAPTER 9. BONDS AND TERM STRUCTURE
= σ2
2ae−a(u+t) 
e2a(u∧t) −1

.
(9.10)
Therefore,
Var
 t
0
X(u, x)du

= Cov
 t
0
X(u, x)du,
 t
0
X(s, x)ds

=
 t
0
 t
0
Cov[X(u, x), X(s, x)]duds
=
 t
0
 t
0
σ2
2ae−a(u+s) 
e2a(u∧s) −1

duds
= σ2
2a3

2at −3 + 4e−at −e−2at
.
Consequently,
Z(t, x) = E

exp
$
−
 t
0
X(u, x)du
%
= exp
$
−x
a

1 −e−at
+ 1
4
σ2
a3

2at −3 + 4e−at −e−2at%
.
Using the time homogeneity of the X process,
B(t, T) = e−b(T −t)Z(T −t, rt −b).
This can be written as
B(t, T) = exp {−(T −t)R(T −t, rt)} ,
where R(T −t, rt) can be thought of as the interest rate between times t
and T. With R∞= b −σ2
2a2 , we can write
R(t, r) = R∞−1
at

(R∞−r)

1 −e−at
−σ2
4a2

1 −e−at2

.
Note that R∞= limt→∞R(t, r), so R∞can be thought of as the long-
term interest rate. However, R∞does not depend on the instantaneous
rate rt. Practitioners consider this to be a weakness of the Vasicek model.
Exercise 9.6.1. Let 0 ≤t ≤T ≤T ∗and consider a call option with expiry
T and strike K on the zero coupon bond B(t, T ∗). Show that this option
will be exercised if and only if r(T) < r∗, where, with R∞as above,
r∗= R∞

1 −
α(T ∗−T)
1 −e−α(T ∗−T )

−σ2[1 −e−α(T ∗−T )]
4α2
−log(K)

α
1 −e−α(T ∗−T )

.
(9.11)

9.6. SHORT-RATE DIFFUSION MODELS
267
The Hull-White Model
In its simplest form this model is a generalisation of the Vasicek model using
deterministic, time-varying coefficients. It is popular with practitioners.
Its more general form includes a term rβ
t in the volatility, in which case it
generalises the Cox-Ingersoll-Ross model discussed in the next section.
In this model, the short rate process is supposed given by the stochastic
differential equation
drt = (α(t) −β(t)rt) dt + σ(t)dWt
(9.12)
for r0 > 0. Here, α, β, and σ are deterministic functions of t.
Write b(t) =
4 t
0 β(u)du, so b is also non-random. We solve (9.12) by
variation of constants to obtain
rt = e−b(t)

r0 +
 t
0
eb(u)α(u)du +
 t
0
eb(u)σ(u)dWu

.
Again, rt is a deterministic quantity plus the stochastic integral of a deter-
ministic function.
Consequently, rt is a Gaussian Markov process with mean
E (rt) = m(t) = e−b(t)

r0 +
 t
0
eb(u)α(u)du

and covariance
Cov(rt, rs) = e−b(s)−b(t)
 s∧t
0
e2b(u)σ2(u)du.
Again we can argue that
4 T
0 rtdt is normal. Its mean is
E
 T
0
rtdt

=
 T
0
e−b(t)

r0 +
 t
0
eb(u)α(u)du

dt
and its variance is
Var
 T
0
rtdt

=
 T
0
e2b(u)σ2(u)
 T
u
e−b(s)ds
2
du.
The price of a zero coupon bond for this model is
B(0, T) = E

exp

−
 T
0
rtdt
&
.
The quantity in the exponential is Gaussian, so we have
B(0, T) = exp

−E
 T
0
rtdt

+ 1
2Var
 T
0
rtdt
&

268
CHAPTER 9. BONDS AND TERM STRUCTURE
= exp

−r0
 T
0
e−b(t)dt −
 T
0
 t
0
e−b(t)+b(u)α(u)dudt
+ 1
2
 T
0
e2b(u)σ2(u)
 T
u
e−b(s)ds
2
du
⎫
⎬
⎭
= exp[−r0C(0, T) −A(0, T)],
where
C(0, T) =
 T
0
e−b(t)dt
and
A(0, T) =
 T
0
 t
0
e−b(t)+b(u)α(u)dudt
−1
2
 T
0
e2b(u)σ2(u)
 T
u
e−b(s)ds
2
du.
Note that the first term in A can be written, using Fubini’s theorem, as
 T
0
 T
u
e−b(t)+b(u)α(u)dudt =
 T
0
eb(u)α(u)
 T
u
e−b(s)ds

du.
Therefore
A(0, T) =
 T
0

eb(u)α(u)γ(u) −1
2e2b(u)σ2(u)γ2(u)

du,
where
γ(u) =
 T
u
e−b(s)ds.
The price at time t of a zero coupon bond is
B(t, T) = E

exp

−
 T
t
rudu
&
|Ft

= E

exp

−
 T
t
rudu
&
|rt

,
where the final step follows because r is Markov. Write
C(t, T) = eb(t)
 T
t
e−b(u)du = eb(t)γ(t)
and
A(t, T) =
 T
t

eb(u)α(u)γ(u) −1
2e2b(u)σ2(u)γ2(u)

du.
Then it can be shown that
B(t, T) = exp {−rtC(t, T) −A(t, T)} .
(9.13)

9.6. SHORT-RATE DIFFUSION MODELS
269
Now α, β, and γ are deterministic functions of time, t; consequently
C(t, T) and A(t, T) are also functions only of t. Write Ct(t, T) and At(t, T)
for their derivatives in t. From (9.13), we have
dB(t, T) = B(t, T)
)
−C(t, T) (α(t) −β(t)rt) dt
−C(t, T)σ(t)dWt −1
2C2(t, T)σ2(t)dt −rtCt(t, T)dt −At(t, T)dt
*
.
(9.14)
We are working under the risk-neutral measure, so
dB(t, T) = rtB(t, T)dt + ∆(t)dWt,
(9.15)
where ∆is some coefficient function. Comparing (9.14) and (9.15), we see
that we must have
rt = −C(t, t) (α(t) −β(t)rt)−1
2C2(t, T)σ2(t)−rtct(t, T)−A(t, T). (9.16)
Consequently,
dB(t, T) = rtB(t, T)dt −B(t, T)σ(t)C(t, T)dWt.
The volatility of the zero coupon bond is σ(t)C(t, T).
Some Normal Densities
Consider times 0 ≤t ≤T1 < T2. In the Hull-White framework, we have
seen that r(T1) is Gaussian with
E (r(T1)) = m1 = e−b(T1)

r0 +
 T1
0
eb(u)α(u)du

,
Var[r(T1)] = σ2
1 = e−2b(T1)
 T1
0
e2b(u)σ2(u)du

.
Also,
4 T1
0
rudu is Gaussian with
E
 T1
0
rudu

= m2 =
 T1
0
e−b(v)

r0 +
 v
0
eb(u)α(u)du

dv,
Var
 T1
0
rudu = σ2
2 =
 T1
0
e2b(u)σ2(u)
 T1
u
e−b(s)ds
2
du.
The covariance of r(T1) and
4 T1
0
rudu is
E
 T1
0
(ru −E (ru)) du

(r(T1) −E (r(T1)))


270
CHAPTER 9. BONDS AND TERM STRUCTURE
=
 T1
0
E ((ru −E (ru)) (r(T1) −E (r(T1)))) du
=
 T1
0
Cov (ru, r(T1)) du
=
 T
0

e−b(u)−b(T1)
 T
0
e2b(s)σ2(s)ds

du
= ρσ1σ2,
say.
Bond Options
Consider a European call option on the zero coupon bond that has strike
price K and expiration time T1. The bond matures at time T2 > T1.
The calculations above imply that (r(T1),
4 T1
0
rudu) is Gaussian with
density
f(x, y) =
1
2πσ1σ2

1 −ρ2
× exp
$
−
1
2(1 −ρ2)
(x −m1)2
σ2
1
−2ρ(x −m1)(y −m2)
σ1σ2
+ (y −m2)2
σ2
2
%
.
The price of the European option on B with expiration time T1 and
strike K at time 0 is
V0 = E

e−
 T1
0
rudu (B(T1, T2) −K)+
= E

e−
 T1
0
rudu (exp {−r(T1)C(T1, T2) −A(T1, T2)} −K)+
=
 ∞
−∞
 ∞
−∞
e−y (exp {−xC(T1, T2) −A(T1, T2)} −K)+ f(x, y)dxdy.
To determine the price of the bond option at time t ≤T1 < T2, we note
that the random variable

r(T1),
4 T1
t
rudu

is Gaussian with a density
similar to f(x, y), except that m1, m2, σ2, σ2, and ρ are replaced by
m1(t) = E (r(t1) |rt ) = e−b(T1)

eb(t)rt +
 T1
t
eb(u)α(u)du

,
σ2
1(t) = E

(r(T1) −m1(t))2 |rt

= e−2b(T1)
 T1
t
e2b(u)σ2(u)du,
m2(t) = E
 T1
t
rudu |rt

=
 T1
t

rte−b(v)+b(t) + e−b(v)
 v
t
eb(u)α(u)du

dv,

9.6. SHORT-RATE DIFFUSION MODELS
271
σ2
2(t) = E
⎛
⎝
 T1
t
rudu −m2(r)
2
|rt
⎞
⎠
=
 T1
t
e2b(v)σ2(v)
 T1
v
e−b(s)ds
2
dv,
and
ρ(t)σ1(t)σ2(t) = E
 T1
t
rudu −m2(t)

(r(T1) −m1(t)) |rt

=
 T1
t
e−b(u)−b(T1)
 u
t
e2b(s)σ2(s)dsdu.
These quantities now depend on rt and so are stochastic as is, therefore,
the corresponding option price
E

e−
 T1
t
rudu (B(T1, T2) −K)+ |Ft

= E

e−
 T1
t
rudu (exp {−r(T1)C(T1, T2) −A(T1, T2)} −K)+ |rt

.
This price can be expressed in terms of an integration with respect to
a density analogous to ft(x, y) in which m1, σ1, m2, σ2, ρ are replaced by
m1(t), σ1(t), m2(t), σ2(t), ρ(t), respectively.
The Hull-White model leads to a closed form expression for the option
on the bond. Also, the parameters of the model can be estimated so the
initial yield curve is matched exactly. However, it is a ‘one-factor’ model
and
B(t, T) = exp {−rtC(t, T) −A(t, T)} ,
so all bond prices for all T are perfectly correlated. Further, the short rate
rt is normally distributed. This means it can take negative values with
positive probability, and the bond price can exceed 1.
The Cox-Ingersoll-Ross Model
We have noted in the Vasicek and Hull-White models for rt that, because
rt is Gaussian, there is a positive probability that rt < 0.
The Cox-Ingersoll-Ross model for rt provides a stochastic differential
equation for rt, the solution of which is always non-negative. To describe
this process, recall the Ornstein-Uhlenbeck equation (9.8)
dXt = −aXtdt + σdWt
(9.17)
with solution
X(t, x) = e−at

x +
 t
0
σeasdWs

.

272
CHAPTER 9. BONDS AND TERM STRUCTURE
Here W is a standard Brownian motion on a probability space (Ω, F, P).
In fact, suppose we have n independent Brownian motions W1, . . . , Wn
on (Ω, F, P) and n Ornstein-Uhlenbeck processes X1, . . . , Xn given by equa-
tions
dXi(t) = −1
2αXi(t)dt + 1
2σdWi(t),
so that
Xi(t) = e−1
2 αt

Xi(0) + 1
2σ
 t
0
e
1
2 βsdWi(s)

.
Consider the process
rt = X2
1(t) + X2
2(t) + · · · + X2
n(t).
From Itˆo’s differential rule,
drt =
n

i=1
2Xi(t)

−1
2αXi(t)dt + 1
2σdWi(t)

+
n

i=1
1
4σ2dt
= −αrtdt + σ
 n

i=1
Xi(t)dWi(t)

+ nσ2
4 dt
=
nσ2
4
−αrt

dt + σ√rt
n

i=1
Xi(t)
√rt
dWi(t).
Consider the process
Wt =
n

i=1
 t
0
Xi(u)
√ru
dWi(u).
Then W is a continuous martingale and
W 2
t = 2
 t
0
WudWu +
n

i=1
 t
0
X2
i (u)
ru
du = 2
 t
0
WudWu + t,
so W 2
t −t is a martingale. From L´evy’s characterisation, therefore, W is a
standard Brownian motion and we can write
drt =
nσ2
4
−αrt

dt + σ√rtdWt.
It is known (see [240], for example) that if n = 1, then P(rt > 0) = 1
but
P (there are infinitely many times t > 0 for which rt = 0) = 1.
However, if n ≥2, then
P (there is at least one time t > 0 for which rt = 0) = 0.

9.6. SHORT-RATE DIFFUSION MODELS
273
Definition 9.6.2. A Cox-Ingersoll-Ross (CIR) process is the process de-
fined by an equation of the form
drt = (a −brt)dt + σ√rtdWt,
(9.18)
where a > 0, b > 0, and σ > 0 are constant. With n = 4a
σ2 , we can interpret
rt as n
i=1 X2
i (t) for Ornstein-Uhlenbeck processes Xi as above. However,
equation (9.18) makes sense whether or not n is an integer.
Remark 9.6.3. Geman and Yor [142] explore the relationship between the
Vasicek and CIR models and show in particular that the CIR process is a
Bessel process.
Similarly to the results for integer n, we quote the following ([240]). If
a < σ2
2 , so n < 2, then
P (there are infinitely many times t > 0 for which rt = 0) = 1.
Consequently, this range for a is not too useful. If a ≥σ2
2 , so n ≥2, then
P (there is at least one time t > 0 for which rt = 0) = 0.
Write r0,t(x) for the solution of (9.18) for which r0 = x. The next result
describes the law of the pair of random variables

r0,t(x),
4 t
0 r0,u(x)du

.
Note that φ and ψ are functions of t only, reminiscent of the A and C
functions in the Hull-White model.
Theorem 9.6.4. For any λ > 0 and µ > 0, we have
E

e−λr0,t(x)e−µ
 t
0 r0,u(x)du
= e−aφλ,µ(t)e−xψλ,µ(t),
where
φλ,u(t) = −2
σ2 log

2γet(b+γ)/2
σ2λ(eγt −1) + γ −b + eγt(γ + b)

,
ψλ,u(t) = λ(γ + b) + eγt(γ −b) + 2µ(eγt −1)
σ2λ(eγt −1) + γ −b + eγt(γ + b)
and γ =

b2 + 2σ2µ.
Proof. Suppose 0 ≤t ≤T. From the uniqueness of solutions of (9.18), we
have the following ‘flow’ property:
r0,T (x) = rt,T (r0,t(x)).
Consider the expectation
E

e−λrt,T (r0,t(x))e−µ
 T
t r0,u(x)dµ |Ft

.

274
CHAPTER 9. BONDS AND TERM STRUCTURE
From the Markov property, this is the same as conditioning on r0,t(x), so
write
V (t, r0,t(x)) = E

e−λr0,T (x)e−µ
 T
t r0,u(x)du |r0,t(x)

.
Now
e−µ
 t
0 r0,u(x)duV (t, r0,t(x)) = E

e−λr0,T (x)e−µ
 T
0 r0,u(x)du |Ft

and so is a martingale. However, applying the Itˆo differentiation rule, we
obtain
e−µ
 t
0 r0,uduV (t, r0,t(x))
= V (0, x) +
 t
0
∂V
∂u (u, r0,u(x)) −µr0,u(x)V (u, r0,u(x))
+ ∂V
∂ξ (u, r0,u(x)) (a −br0,u(x))
+ 1
2
∂2V
∂ξ2 (u, r0,u(x)) σ2r0,u(x)

e−µ
 u
0 r0,s(x)dsdu
+
 t
0
e−µ
 u
0 r0,s(x)ds ∂V
∂ξ (u, r0,u(x)) σ
(
r0,u(x)dWu.
As the left-hand side is a martingale and the right-hand side is an Itˆo
process, the du integral must be the zero process. Consequently,
∂V
∂t (t, y) −µyV (t, y) + ∂V
∂y (t, y)(a −by) + 1
2
∂2V
∂y2 (t, y)σ2y = 0
with
V (t, y) = E

e−λrt,T (y)e−µ
 T
t rt,u(y)du
.
Because the coefficients of (9.18) are independent of t, the solution
of (9.18) is stationary and we can write
V (t, y) = E

e−λr0,T −t(y)e−µ
 T −t
0
r0,u(y)du
.
Define
F(t, y) = E

e−λr0,t(y)e−µ
 t
0 r0,u(y)du
,
so that V (t, y) = F(T −t, y) and F satisfies
∂F
∂t = ∂F
∂y (a −by) −µyF + 1
2σ2y ∂2F
∂y2
(9.19)
with F(0, y) = e−λy.

9.6. SHORT-RATE DIFFUSION MODELS
275
Motivated by the formula of the Hull-White model, we look for a solu-
tion of (9.19) in the form
F(t, y) = e−aφ(t)−xψ(t).
This is the case if φ(0) = 0 and ψ(0) = λ with
φ′(t) = ψ(t),
−ψ′(t) = σ2
2 ψ2(t) + bψ(t) −µ.
Solving these equations gives the expressions for φ and ψ.
Remark 9.6.5. Taking µ = 0, we obtain the Laplace transform of rt(x):
E

eλrt(x)
= (2λK + 1)−2a/σ2 exp
$ −λKz
2λK + 1
%
,
where
K = σ2
4b

1 −e−bt
,
z =
4bx
σ2(ebt −1).
Consequently, the Laplace transform of rt(x)
K
is given by g 4a
σ2 ,z, where
gδ,z =
1
(2λ + 1)δ/2 exp
$
−
λz
2λ + 1
%
.
However, consider the chi-square density fδ,z, having δ degrees of freedom
and decentral parameter z, given by
fδ,z(x) = e−z/2
2z
δ
4 −1
2 e−x/2x
δ
4 −1
2 I δ
2 −1(√xz) for x > 0.
Here Iν is the modified Bessel function of order ν, given by
Iν(x) =
x
2
ν
∞

n=0
 x
2
2n
n!Γ(ν + n + 1).
Then it can be shown that gδ,z is the Laplace transform of the law of a
random variable having density fδ,z(x). Consequently,
rt(x)
K
is a random
variable having a chi-square density with δ degrees of freedom.
Recall that we are working under the risk-neutral probability P. The
price of a zero coupon bond at time 0 is
B(0, T) = E

exp

−
 T
0
ru(x)du
&
= e−aφ0,1(0,T )−r0(x)ψ0,1(0,T ).
Here
φ0,1(T) = −2
σ2 log

2γeT (γ+b)/2
γ −b + eγT (γ + b)

,
ψ0,1(T) =
2(eγT −1)
γ −b + eγT (γ + b)

276
CHAPTER 9. BONDS AND TERM STRUCTURE
with γ =
√
b2 + 2σ2. The price of a zero coupon bond at time t is similarly,
because of stationarity,
B(t, T) = e−aφ0,1(T −t)−rt(x)ψ0,1(T −t).
Suppose 0 ≤T ≤T ∗. Consider a European call option with expiration
time T and strike price K on the zero coupon bond B (t, T ∗) . At time 0,
this has a price
V0 = E

e−
 T
0 ru(x)du (B(T, T ∗) −K)+
= E

E

e−
 T
0 ru(x)du (B(T, T ∗) −K)+ |Ft

= E

e−
 T
0 ru(x)du 
e−aφ0,1(T ∗−T )−rT (x)ψ0,1(T ∗−T ) −K
+
.
Write
r∗= −aφ0,1(T ∗−T) + log K
ψ0,1(T ∗−T)
.
Then
V0 = E

e−
 T
0 ru(x)duB(T, T ∗)1{rT (x)<r∗}

−KE

e−
 T
0 ru(x)du1{rT (x)<r∗}

.
Now
E

e−
 T
0 ru(x)duB(T, T ∗)

= B(0, T ∗),
E

e−
 T
0 ru(x)du
= B(0, T).
Define two new probability measures P1 and P2 by setting
dP1
dP
''''
FT
= e−
 T
0 ru(x)duB(T, T ∗)
B(0, T ∗)
,
dP2
dP
''''
FT
= e−
 T
0 ru(x)du
B(0, T)
.
Then
V0 = B(0, T ∗)P1 (rT (x) < r∗) −KB(0, T)P2 (rT (x) < r∗) .
Write
K1 = δ2
2 ·
eγT −1
γ (eγT + 1) + (σ2ψ0,1(T ∗−T) + b) (eγT −1),
K2 = σ2
2 ·
eγT −1
γ (eγT + 1) + b (eγT −1).
Then it can be shown that the law of rT (x)
K1
under P1 (resp. the law of
rT (x)
K2
under P2) is a decentral chi-square with 4a
σ2 degrees of freedom and
decentral parameter ξ1 (resp. ξ2), where
ξ1 =
8r0(x)γ2eγT
σ2 (eγT −1) (γ (eγT + 1)) + (σ2ψ0,1(T ∗−T) + b) (eγT −1),

9.7. THE HEATH-JARROW-MORTON MODEL
277
ξ2 =
8r0(x)γ2eγT
σ2 (eγT −1) (γ (eγT + 1) + b (eγT −1)).
Consequently, if Fδ,z is the probability distribution function for a chi-square
random variable with δ degrees of freedom and decentral parameter z, then
V0 = B(0, T ∗)F 4a
σ2 ,ξ1
 r∗
K1

−KB(0, T)F 4a
σ2 ,ξ2
 r∗
K2

.
9.7
The Heath-Jarrow-Morton Model
Forward Rate Agreement
Suppose 0 ≤t ≤T < T + ε ≤T ∗. ‘Today’ is time t. We wish to enter a
contract to borrow $1 at the future time T and repay it (with interest) at
the time T + ε. The rate of interest to be paid between T and T + ε is to
be agreed today and so must be Ft-measurable.
We could approximate this transaction by buying today a T-maturity
zero for B(t, T) and shorting an amount
B(t,T )
B(t,T +ε) of (T +ε)-maturity zeros.
The cost of this portfolio at time t is
B(t, T) −
B(t, T)
B(t, T + ε) · B(t, T + ε) = 0.
Now at the future time T we receive $1 for the T-maturity zero. Then, at
the time (T + ε), we must pay
B(t,T )
B(t,T +ε) for the (T + ε)-maturity zeros.
In effect, we are looking at borrowing $1 at the future time T and paying
$
B(t,T )
B(t,T +ε) at time T + ε. Consequently, the interest rate we are paying on
the dollar received at time T is R(t, T, T + ε), where
B(t, T)
B(t, T + ε) = exp {εR(t, T, T + ε)}
so
R(t, T, T + ε) = −1
ε[log B(t, T + ε) −log B(t, T)].
Definition 9.7.1. The instantaneous interest rate for money borrowed at
time T, agreed upon at time t ≤T, is the forward rate f(t, T).
In fact,
f(t, T) = lim
ε↓0 R(t, T, T + ε) = −∂
∂T log B(t, T).
Then, as B(t, t) = 1,
log B(t, T) =
 T
t
∂
∂T log B(t, u)du = −
 T
t
f(t, u)du.

278
CHAPTER 9. BONDS AND TERM STRUCTURE
Therefore, B(t, T) = exp(−
4 T
t f(t, u)du).
We note that this is an alternative representation for B(t, T), in contrast
to its expression in terms of the short-rate process r:
B(t, T) = E

exp

−
 T
t
rudu
&
|Ft

.
Agreeing at time t on the forward rate f(t, u) means one agrees, at time t,
that the instantaneous interest rate at time u ∈[t, T] will be f(t, u).
Thus one agrees that investing $1 at time t will give $ exp
4 T
t f(t, u)du
at time T; investing $B(t, T) at time t will give
$B(t, T) · exp
 T
t
f(t, u)du
&
= $1
at time T.
Lemma 9.7.2. We have rt = f(t, t).
Proof. We have two representations:
B(t, T) = E

exp

−
 T
t
rudu
&
|Ft

,
(9.20)
B(t, T) = exp

−
 T
t
f(r, u)du
&
.
(9.21)
From (9.20),
∂B(t, T)
∂T
= E

−r(T) exp(−
 T
t
rudu) |Ft

.
Evaluating at T = t, we have
∂B(t, T)
∂T
''''
T =t
= −rt.
From (9.21),
∂B(t, T)
∂T
= −f(t, T) exp

−
 T
t
f(t, u)du

and
∂B(t, T)
∂T
''''
T =t
= −f(t, t).

9.7. THE HEATH-JARROW-MORTON MODEL
279
The Heath-Jarrow-Morton model
The Heath-Jarrow-Morton (HJM) model for term structure describes a
system of stochastic differential equations for the evolution of the forward
rate f(t, T). For each T ∈(0, T ∗], suppose the dynamics of f are given by
df(t, T) = α(t, T)dt + σ(t, T)dWt.
(9.22)
Here the coefficients α(u, T) and σ(u, T), for 0 ≤u ≤T, are measurable
(in (u, ω)) and adapted. The integral form of (9.22) is
f(t, T) = f(0, T) +
 t
0
α(u, T)du +
 t
0
σ(u, T)dWu.
(9.23)
Note that we have two time parameters and recall
B(t, T) = exp

−
 T
t
f(t, u)du
&
.
With d denoting a differential in the t variable,
d

−
 T
t
f(t, u)du

= f(t, t)dt −
 T
t
(df(t, u)) du
= rtdt −
 T
t
[α(t, u)dt + σ(t, u)dWt]du
= rtdt −α∗(t, T)dt −σ∗(t, T)dWt,
(9.24)
where
α∗(t, T) =
 T
t
α(t, u)du,
σ∗(t, T) =
 T
t
σ(t, u)du.
Recall, that by definition, f(t, u) is an (Ft)-adapted process. Therefore,
Xt = −
 T
t
f(t, u)du
is an Ft-adapted process. In fact, it is an Itˆo process with, as in (9.24),
dXt = (rt −α∗(t, T)) dt −σ∗(t, T)dWt.
Also, B(t, T) = eXt, so
dB(t, T) = eXt

rt −α∗(t, T) + 1
2σ∗(t, T)2

dt −eXtσ∗(t, T)dWt
= B(t, T)

rt −α∗(t, T) + 1
2σ∗(t, T)2

dt −σ∗(t, T)dWt

.

280
CHAPTER 9. BONDS AND TERM STRUCTURE
Now, the discounted B(t, T) will be a martingale under P (so P is a
risk-neutral measure) if
α∗(t, T) = 1
2 (σ∗(t, T))2 for 0 ≤t ≤T ≤T ∗.
From the definitions of α∗and σ∗, this means that
 T
t
α(t, u)du = 1
2
 T
t
σ(t, u)du
2
.
This is equivalent to
α(t, T) = σ(t, T)
 T
0
σ(t, u)du.
If P itself is not a risk-neutral measure, there may be a probability P θ
under which

B(t,T )
S0
t

is a martingale. This is the content of the following
result due to Heath, Jarrow, and Morton [153].
Theorem 9.7.3. For each T ∈(0, T], suppose α(u, T) and σ(u, T) are
adapted processes.
We assume σ(u, T) > 0 for all u, T, and f(0, T) is
a deterministic function of T. The instantaneous forward rate f(t, T) is
defined by
f(t, T) = f(0, T) +
 t
0
α(u, T)du +
 t
0
σ(u, t)dWu.
Then the term structure model determined by the processes f(t, T) does not
allow arbitrage if and only if there is an adapted process (θt) such that
α(t, T) = σ(t, T)
 T
t
σ(t, u)du + σ(t, T)θt for all 0 ≤t ≤T ≤T ∗,
and the process
Λθ
t = exp
$
−
 t
0
θudWu −1
2
 t
0
θ2
udu
%
is an (Ft, P)-martingale.
Proof. Suppose θ is an adapted process such that Λθ(t) is an (Ft, P)-
martingale, and define a new probability measure P θ by setting
dP θ
dP
''''
FT ∗
= Λθ(T ∗).
By Girsanov’s theorem, W θ is a Brownian motion under P θ, where
W θ
t =
 t
0
θudu + Wt,

9.7. THE HEATH-JARROW-MORTON MODEL
281
and
dB(t, T) = B(t, T)

rt −α∗(t, T) + 1
2σ∗(t, T)2 + σ∗(t, T)θt

dt
−σ∗(t, T)dW θ
t

.
where, as before, α∗(t, T) =
4 T
t α(t, u)du and σ∗(t, T) =
4 T
t σ(t, u)du.
For B(t, T) to have a rate of return rt under P θ, θ must satisfy
α∗(t, T) = 1
2σ∗(t, T)2 + σ∗(t, T)θt.
This must hold for all maturities T. Differentiating with respect to T, that
is
α(t, T) = σ(t, T)σ∗(t, T) + σ(t, T)θt for 0 ≤t ≤T ≤T ∗.
Remark 9.7.4. The point to note is that, if there is such a process θt, it is
independent of the time T maturity of the bond B(t, T), and
θt = −
−α∗(t, T) + 1
2σ∗(t, T)2
σ∗(t, T)

.
Now, under the ‘market’ probability P, the rate of return of the bond
is
rt −α∗(t, T) + 1
2σ∗(t, T)2.
The rate of return above the interest rate rt is therefore
−α∗(t, T) + 1
2σ∗(t, T)2,
and the market price of risk is just
−α∗(t, T) + 1
2σ∗(t, T)2
σ∗(t, T)
= −θt.
The requirement of the theorem therefore is that the market price of
the risk be independent of the maturity times T. Substituting for θ, we
have that, under P θ,
dB(t, T) = B(t, T)

rtdt −σ∗(t, T)dW θ
t

,
df(t, T) = σ(t, T)σ∗(t, T)dt + σ(t, T)dW θ
t .

282
CHAPTER 9. BONDS AND TERM STRUCTURE
9.8
A Markov Chain Model
Elliott, Hunter, and Jamieson ([117]) introduced a self-calibrating model
for the short-term rate.
It is supposed that the short-term rate rt is a
finite state space Markov chain defined on a probability space (Ω, F, P)
taking (positive) values r1, r2, . . . , rN. Each of these values can be identified
with one of the canonical unit vectors ei in RN, ei = (0, . . . , 0, 1, 0, . . . , 0).
(In effect, we are considering an indicator function 1{ri}(r) on the set
{r1, r2, . . . , rN}). Without loss of generality, we can take the state space
of our Markov chain (Xt)t≥0 to be the set S = {e1, e2, . . . , eN} . Writing
r = (r1, r2, . . . , rN) ∈RN, we then have
rt = r · Xt = r(Xt),
where the central dot denotes the scalar product in RN. Considering the
Markov chain to have state space S simplifies the notation.
The unconditional distribution of Xt is E (Xt) = pt = (p1
t, . . . , pN(t)),
where
pi
t = P(Xt = ei) = E (ei · Xt) = P (rt = ri) .
Suppose this distribution evolves according to the Kolmogorov equation
dpt
dt = Apt.
Here A is a ‘Q-matrix’; that is, A = (aji)1≤i,j≤N with N
j=1 aij = 0 and
aji ≥0 if i ̸= j. The components aji could be taken to be time-varying,
though this would complicate their estimation.
The price of a zero coupon bond at time t, with maturity T, in this
model is
B(t, T) = E

exp

−
 T
t
r(Xs)ds
&
|Ft

,
where (Ft) is the filtration generated by X (or, equivalently, by r).
Because of the Markov property, this is
E

exp

−
 T
t
r(Xs)ds
&
|Xt

= B(t, T, Xt),
say, and so is a function of Xt ∈S. Any (real) function of Xt ∈S is given
as the scalar product of some function φt = (φ1
t, φ2
t, . . . , φN(t))′ ∈RN with
Xt. That is, we can write
B(t, T, Xt) = φt · Xt,
where φi
t = B(t, T, ei).
Now
e−
 t
0 r(Xs)dsB(t, T, Xt) = e−
 t
0 r(Xs)dsφt · Xt

9.8. A MARKOV CHAIN MODEL
283
= E

e−
 t
0 r(Xs)ds |Ft

and so is a martingale.
Lemma 9.8.1. Define the RN-valued process M by
Mt = Xt −X0 −
 t
0
AXsds.
Then M is an (Ft, P)-martingale.
Proof. Consider the matrix exponential eA(t−s). By the Markov property,
E (Xt |Xs ) = eA(t−s)Xs
for t ≥s. (In effect, one solves the Kolmogorov equation with initial con-
dition Xs.) Now, for t ≥s, if I is the N × N identity matrix,
E (Mt −Ms |Fs ) = E (Xt −Xs |Fs ) −E
 t
s
AXudu |Fs

= eA(t−s)Xs −Xs −
 t
s
AeA(u−s)Xsdu
=

eA(t−s) −I −
 t
s
AeA(u−s)du

Xs
=

eA(t−s) −I −[eA(u−s)]t
s

Xs = 0.
Corollary 9.8.2. The semimartingale representation of Xt is therefore
Xt = X0 +
 t
0
AXsds + Mt.
Theorem 9.8.3. The process φt ∈RN has dynamics
dφt
dt = (diag r −A∗)φt
with terminal condition φT = 1 = (1, 1, . . . , 1)′ ∈RN.
Proof. We have seen that
e−
 t
0 r(Xs)dsB(t, T, Xt) = e−
 t
0 r(Xs)dsφt · Xt
is an (Ft, P)-martingale. Consequently, the dt term in its Itˆo process (or
semimartingale) representation must be identically zero. Now

284
CHAPTER 9. BONDS AND TERM STRUCTURE
e−
 t
0 r(Xs)dsφt · Xt = B(0, T, X0) −
 t
0
r(Xs)e−
 s
0 r(Xu)duφs · Xsds
+
 t
0
e−
 s
0 r(Xu)du
dφs
ds · Xs + φs · (AXs)

ds+
 t
0
e−
 s
0 r(Xu)duφs·dMs.
Consequently,
e−
 s
0 r(Xu)du

−r(Xs)φs · Xs + dφs
ds · Xs + φs · (AXs)

= 0.
Now r(Xs) = r · Xs, where r = (r1, rs, . . . , rs)′, and r(Xs)φs · Xs =
(diag r)φs·Xs, where diag r is the matrix with r on its diagonal. Therefore
dφs
ds · Xs + A∗φs · Xs −((diag r)φs) · Xs = 0 for all Xs.
Consequently, φ is given by the vector equation
dφt
dt = (diag r −A∗)φt
with terminal condition φT = (1, . . . , 1)′ = 1.
Corollary 9.8.4. Write B = diag r −A∗. Then φt = e−B(T −t)1, and the
price at time t of a zero coupon bond is
B(t, T, Xt) = φt · Xt = (e−B(T −t) · Xt)1.
The yield for such a bond is
yt,T = −
1
T −t log B(t, T, Xt).
Yield values are quoted in the market.
In [117] it is supposed that yield values give noisy information about
such a Markov chain term structure model. The techniques of filtering from
Hidden Markov models (see [110]), are then applied to estimate the state
of X and the model parameters.

Chapter 10
Consumption-Investment
Strategies
10.1
Utility Functions
The results of this chapter are a presentation of the comprehensive, fun-
damental, and elegant contributions of Karatzas, Lehoczky, Sethi, Shreve
and Xu. See, for example, the papers [186] through [190].
We first review in the multi-asset situation concepts relating to trading
strategies, consumption processes, and utility functions.
On a probability space (Ω, F, P), consider a market that includes a
bond S0 and n risky assets S1, . . . , SN. Their dynamics are given by the
equations
dS0
t = S0
t rtdt,
S0
0 = 1,
(10.1)
dSi
t = Si
t
⎛
⎝µi(t)dt +
n

j=1
σij(t)dWj(t)
⎞
⎠,
Si
0 = si for i = 1, 2, . . . , n.
(10.2)
Here W(t) = (W1(t), . . . , Wd(t)) is an n-dimensional Brownian motion
defined on (Ω, F, P) and (Ft) will denote the completion of the filtration
σ {W(u) : 0 ≤u ≤t} = σ {Su : 0 ≤u ≤t} .
The interest rate rt, mean rate of return µ(t) = (µ1(t), . . . , µn(t))′, and
the volatility σ(t) = (σij(t))1≤i,j≤d are taken to be measurable, adapted,
and bounded processes. Note that we have taken the dimension, n, of the
Brownian motion equal to the number of risky assets.
Write a(t) = σ(t)σ∗(t). We assume there is an ε > 0 such that, with |.|
denoting the Euclidean norm in Rn,
ξ∗a(t)ξ ≥ε |ξ|2 for all ξ ∈Rn and (t, ω) ∈[0, ∞) × Ω.
285

286
CHAPTER 10. CONSUMPTION-INVESTMENT STRATEGIES
Consequently, the inverses of σ and σ∗exist and are bounded:
''σ(t, ω)−1ξ
'' ≤ε−1
2 |ξ| ,
''σ∗(t, ω)−1ξ
'' ≤ε−1
2 |ξ| for all ξ ∈Rn.
(10.3)
The filtration is then equivalently given as the completion of the filtration
generated by the process S.
Therefore in this situation the market price of risk defined by equa-
tion (7.34) has the unique solution
θt = σ(t)−1 (b(t) −rt1) ;
furthermore, θ is bounded and progressively measurable.
As in Chapter 8, introduce
Λt = exp
$
−
 t
0
θ′
sdW(s) −1
2
 t
0
|θ′
s|2 ds
%
and define a new probability measure P θ by setting
dP θ
dP
''''
Ft
= Λt.
We know from Girsanov’s theorem that W θ is a Brownian motion under
P θ, where
W θ
t = W(t) +
 t
0
θsds.
Furthermore, under P θ,
dSi
t = Si
t
⎛
⎝rtdt +
n

j=1
σij(t)dW θ
j (t)
⎞
⎠for i = 1, 2, . . . , n.
That is, in this situation, P θ is the unique risk-neutral, or martingale,
measure.
Definition 10.1.1. A utility function U : [0, ∞) × (0, ∞) →R is a C0,1
function such that:
a) U(t, ·) is strictly increasing and strictly concave.
b) The derivative U ′(t, c) =
∂
∂cU(t, c) is such that, for every t > 0,
lim
c→∞U ′(t, c) = 0,
lim
c↓0 U ′(t, c) = U ′(t, 0+) = ∞.
These conditions have natural economic interpretations. The increasing
property of U represents the fact that the investor prefers higher levels of
consumption or wealth. The strict concavity of U(t, c) in c implies U ′(t, c)
is decreasing in c; this models the concept that the investor is risk averse.

10.2. ADMISSIBLE STRATEGIES
287
The condition that U ′(t, 0+) = ∞is not strictly necessary, but it simplifies
some of the proofs.
U ′(t, c) is strictly decreasing in c; therefore, there is an inverse map
I(t, c) so that
I (t, U ′(t, c)) = c = U ′(t, I(t, c))
for c ∈(0, ∞). The concavity of U implies that
U(t, I(t, y)) ≥U(t, c) + y(I(t, y) −c) for all c, y.
(10.4)
For some later results, we require that U(t, c) is C2 in c ∈(0, ∞) for all
t ∈[0, T] and U ′′(t, c) = ∂2U
∂c2 is non-decreasing in c for all t ∈[0, T]. These
two conditions imply that I(t, c) is convex and of class C1 in c ∈(0, ∞),
and
∂
∂y U(t, I(t, y)) = y ∂
∂y I(t, y).
10.2
Admissible Strategies
The definitions in this section are the natural counterparts of the discrete-
time notions introduced and discussed briefly in Section 5.6.
We recall that in the continuous-time setting a portfolio process or
trading strategy H =

H1, . . . , Hn′ is a measurable Rn-valued process
that is adapted (Ft) and is such that
 T
0
|Hs|2 ds < ∞a.s.
A consumption process (ct)0≤t≤T is a non-negative, measurable, adapted
process (with respect to (Ft)) such that
 T
0
ctdt < ∞a.s.
The adapted condition means the investor cannot anticipate the future, so
‘insider trading’ is not allowed.
The wealth of the investor at time t is then
Xt =
n

i=0
Hi
tSi
t −
 t
0
csds.
Here Hi
tSi
t represents the amount invested in asset i = 0, 1, . . . , n, and
4 t
0 csds represents the total amount consumed up to time t.
If the strategy H is self-financing, changes in the wealth derive only from
changes in the asset prices, interest on the bond, and from consumption,
and then
dXt =
d

i=1
Hi
tdSi
t +

1 −
n

i=1
Hi
t

dS0
t −ctdt.

288
CHAPTER 10. CONSUMPTION-INVESTMENT STRATEGIES
From (10.1) and (10.2), this is
(rtXt −ct) dt + H′
t (µ(t) −rt1) dt + H′
tσ(t)dW(t)
= (rtXt −ct) dt + H′
tσ(t)dW θ
t .
Writing βt =

S0
t
−1 = exp

−
4 t
0 rsds

, we see that
βtXt = x −
 t
0
βscsds +
 t
0
βsH′
sσ(s)dW θ(s),
(10.5)
where x = X0 is the initial wealth of the investor.
Consequently,
Dt = βtXt +
 t
0
βscsds = x +
 t
0
βsH′
sσ(s)dW θ(s),
which is the present discounted wealth plus the total discounted consump-
tion so far, is a continuous local martingale under P θ.
Definition 10.2.1. The deflator for the market is the process ξ defined by
ξt = βtΛt.
This equals the discount factor β modified by the Girsanov density Λ to
take account of the financial market.
Now
ΛtDt = Λt

βtXt +
 t
0
βscsds

= Λt

x +
 t
0
βsH′
sσ(s)dW θ(s)

= ξtXt +
 t
0
ξscsds −
 t
0
CsΛsθ′
sdW(s),
where Cs =
4 s
0 βucudu. For any F-measurable, P θ-integrable random vari-
able Ψ, Bayes’ rule states that
Eθ (Ψ |Fs ) = E (ΛtΨ |Fs )
Λs
.
Therefore, ΛD is a continuous local martingale under P. Moreover, so is
4 t
0 CsΛsθ′
sdW(s)

. Consequently,
Nt = ξtXt +
 t
0
ξscsds
(10.6)
is a continuous local martingale under P. Furthermore, from Bayes’ rule, we
see that N is a P-supermartingale if and only if D is a P θ-supermartingale.

10.2. ADMISSIBLE STRATEGIES
289
Definition 10.2.2. Similarly to the set of trading strategies SF(ξ) of
Chapter 8, we introduce the set SF(K, x).
A portfolio process H =

H1
t , . . . , Hn
t
′ and a consumption process c
belong to SF(K, x) if, for initial capital x ≥0 and some non-negative,
P-integrable random variable K = K(H, c), the corresponding wealth pro-
cess satisfies
XT ≥0 a.s.,
ξtXt ≥−K(ω) for all 0 ≤t ≤T.
Here ξt is the deflator process of Definition 10.2.1.
Consequently, for every (H, c) ∈SF(K, x), the P-local martingale N
of (10.6) is bounded from below. Using Fatou’s lemma as in Chapter 8, we
deduce that N is a P-supermartingale; therefore, D is a P θ supermartin-
gale.
Write Tu,v for the set of stopping times with values in [u, v]. Using the
Optional Stopping Theorem on N (or D), for any τ ∈T0,T , for (H, c) ∈
SF(K, x),
E

ξτXτ +
 τ
0
ξscsds

≤x
or, equivalently,
Eθ

βτXτ +
 τ
0
βscsds

≤x.
(10.7)
These inequalities state that the expected value of current wealth at any
time τ, and consumption up to time τ, deflated to time 0, should not exceed
the initial capital x.
We now introduce consumption rate processes and final claims whose
(deflated) expected value is bounded by the initial investment x ≥0.
Definition 10.2.3.
a) Write C(x) for the consumption rate processes c
that satisfy
Eθ
 T
0
cse−
 s
0 rududs

≤x.
b) Write L(x) for the non-negative FT -measurable random variables B
that satisfy
Eθ 
Be−
 T
0 rudu
≤x.
From the inequality (10.6), we see that (H, c) ∈SF(0, x) implies c ∈
C(x) and XT ∈L(x).
We now investigate to what extent we can deduce the opposite impli-
cations.
Theorem 10.2.4. For every c ∈C(x) there is a portfolio H such that
(H, c) ∈SF(0, x). Furthermore, if c belongs to the class
D(x) =

c ∈C(x) : Eθ
 T
0
βscsds

= x
&
,

290
CHAPTER 10. CONSUMPTION-INVESTMENT STRATEGIES
then the corresponding wealth process X satisfies XT = 0 and the process
M is a martingale.
Proof. For c ∈C(x), write
C = CT =
 T
0
βscsds
and define the martingale
mt = Eθ (C |Ft ) −Eθ (C) .
Then, from the martingale representation result, m can be expressed as
mt =
 t
0
φ′
sdW θ(s), 0 ≤t ≤T,
for some (Ft)-adapted, measurable Rd-valued process φ, with
 T
0
|φs|2 ds < ∞a.s.
Now the process
Xt =

Eθ
 T
0
e−
 s
0 ruducsds |Ft

+ (x −Eθ (C))

β−1
t
(10.8)
is non-negative because c ∈C(x). As βt = (S0
t )−1 = exp

−
4 t
0 rudu

,
Xtβt = x + mt −
 t
0
βscsds = x +
 t
0
φ′
sdW θ(s) −
 t
0
βscsds.
Write Ht = (H1
t , . . . , Hn
t ) = e
 t
0 rudu (σ′(t))−1 φt. From (10.3), this is a
portfolio process, so
Xtβt = x +
 t
0
βsH′
sσ(s)dW θ(s) −
 t
0
βscsds,
and we see from (10.4) that X is a wealth process corresponding to (H, c) ∈
SF(0, x).
Now if, furthermore, c ∈D(x), then XT = 0 from (10.8), so DT =
4 T
0 βscsds. We have seen that the process D is a P θ-supermartingale and,
in this situation, it has a constant expectation
x = E (DT ) = E
 T
0
ξscsds

= E (D0) .
Therefore, D is a P-martingale.

10.3. MAXIMISING UTILITY OF CONSUMPTION
291
The next result describes the levels of terminal wealth attainable from
an initial endowment x.
Theorem 10.2.5.
a) If B ∈L(x), there is a pair (H, c) ∈SF(0, x)
such that the corresponding wealth process X satisfies XT = B a.s.
b) Write M(x) =

B ∈L(x) : Eθ (βT B) = x

. Then, if B ∈M(x), we
can take c ≡0 and the process (Xtβt)0≤t≤T is a P θ-martingale.
Proof. For B ∈L(x), we define the non-negative process Yt by
Ytβt = Eθ 
B |Ft

+

x −Eθ 
B
 
1 −t
T

= x + vt −ρt,
where
B = βT B,
ρ = T −1 
x −Eθ 
B

,
vt = Eθ 
B |Ft

−Eθ 
B

.
Take the consumption rate process to be
ct = ρβ−1
t
,
and represent vt as
 t
0
ψ′
sdW θ(s) =
 t
0
βs ,H′
sσ(s)dW θ(s),
where ,H′
s = e
 s
0 rudu (σ′(s))−1 ψs. The result follows as in Theorem 10.2.4.
Remark 10.2.6. Minor modifications show that Theorem 10.2.5 still holds
when T is replaced by a stopping time τ ∈T0,T .
10.3
Maximising Utility of Consumption
We consider an investor with initial wealth x > 0. The problem discussed
in this section is how the investor should choose his trading strategy H1(t)
and consumption rate c1(t) in order to remain solvent and also to maximise
his utility over [0, T], with (H1, c1) ∈SF(0, x).
As above, prices will be discounted by βt = (S0
t )−1 = exp

−
4 t
0 rudu

.
Consider a utility function U1.
The problem then is to maximise the expected discounted utility from
consumption,
J1(x, H1, c1) = E
 T
0
U1(c1(s))ds

,
over all strategies (H1, c1) ∈SF(0, x) satisfying
E
 T
0
U −
1 (c1(s))ds

< ∞.

