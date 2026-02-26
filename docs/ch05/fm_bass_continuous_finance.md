# Continuous-Time Financial Models

!!! info "Source"
    **The Basics of Financial Mathematics** by Richard F. Bass, University of Connecticut, Spring 2003.
    These notes are used for educational purposes.

## 16. Continuous-Time Financial Models

16. Continuous time financial models.
The most common model by far in finance is one where the security price is based
on a Brownian motion. One does not want to say the price is some multiple of Brownian
motion for two reasons.
First, of all, a Brownian motion can become negative, which
doesn’t make sense for stock prices. Second, if one invests $1,000 in a stock selling for $1
and it goes up to $2, one has the same profit, namely, $1,000, as if one invests $1,000 in a
stock selling for $100 and it goes up to $200. It is the proportional increase one wants.
Therefore one sets ∆St/St to be the quantity related to a Brownian motion. Differ-
ent stocks have different volatilities σ (consider a high-tech stock versus a pharmaceutical).
In addition, one expects a mean rate of return µ on one’s investment that is positive (oth-
erwise, why not just put the money in the bank?). In fact, one expects the mean rate
of return to be higher than the risk-free interest rate r because one expects something in
return for undertaking risk.
So the model that is used is to let the stock price be modeled by the SDE
dSt/St = σdWt + µdt,
or what looks better,
dSt = σStdWt + µStdt.
(16.1)
Fortunately this SDE is one of those that can be solved explicitly, and in fact we
gave the solution in Section 15.
Proposition 16.1. The solution to (16.1) is given by
St = S0eσWt+(µ−(σ2/2)t).
(16.2)
Proof. Using Theorem 15.1 there will only be one solution, so we need to verify that St
as given in (16.2) satisfies (16.1). We already did this, but it is important enough that we
will do it again. Let us first assume S0 = 1. Let Xt = σWt + (µ −(σ2/2)t, let f(x) = ex,
and apply Ito’s formula. We obtain
St = eXt = eX0 +
Z t
eXsdXs + 1
Z t
eXsd⟨X⟩s
= 1 +
Z t
SsσdWs +
Z t
Ss(µ −1
2σ2)ds
+ 1
Z t
Ssσ2ds
= 1 +
Z t
SsσdWs +
Z t
Ssµds,
which is (16.1). If S0 ̸= 0, just multiply both sides by S0.
Suppose for the moment that the interest rate r is 0. If one purchases ∆0 shares
(possibly a negative number) at time t0, then changes the investment to ∆1 shares at time
t1, then changes the investment to ∆2 at time t2, etc., then one’s wealth at time t will be
Xt0 + ∆0(St1 −St0) + ∆1(St2 −St1) + · · · + ∆i(Sti+1 −Sti).
(16.3)
To see this, at time t0 one has the original wealth Xt0. One buys ∆0 shares and the cost
is ∆0St0. At time t1 one sells the ∆0 shares for the price of St1 per share, and so one’s
wealth is now Xt0 + ∆0(St1 −St0). One now pays ∆1St1 for ∆1 shares at time t1 and
continues. The right hand side of (16.3) is the same as
Xt0 +
Z t
t0
∆(s)dSs,
where we have t ≥ti+1 and ∆(s) = ∆i for ti ≤s < ti+1. In other words, our wealth is
given by a stochastic integral with respect to the stock price. The requirement that the
integrand of a stochastic integral be adapted is very natural: we cannot base the number
of shares we own at time s on information that will not be available until the future.
How should we modify this when the interest rate r is not zero? Let Pt be the
present value of the stock price. So
Pt = e−rtSt.
Note that P0 = S0. When we hold ∆i shares of stock from ti to ti+1, our profit in present
days dollars will be
∆i(Pti+1 −Pti).
The formula for our wealth then becomes
Xt0 +
Z t
t0
∆(s)dPs.
By Ito’s product formula,
dPt = e−rtdSt −re−rtStdt
= e−rtσStdWt + e−rtµStdt −re−rtStdt
= σPtdWt + (µ −r)Ptdt.
Similarly to (16.2), the solution to this SDE is
Pt = P0eσWt+(µ−r−σ2/2)t.
(16.4)
The continuous time model of finance is that the security price is given by (16.1)
(often called geometric Brownian motion), that there are no transaction costs, but one can
trade as many shares as one wants and vary the amount held in a continuous fashion. This
clearly is not the way the market actually works, for example, stock prices are discrete,
but this model has proved to be a very good one.


## 17. Markov Properties of Brownian Motion

17. Markov properties of Brownian motion.
Let Wt be a Brownian motion. Because Wt+r −Wt is independent of σ(Ws : s ≤t),
then knowing the path of W up to time s gives no help in predicting Wt+r −Wt. In
particular, if we want to predict Wt+r and we know Wt, then knowing the path up to time
t gives no additional advantage in predicting Wt+r. Phrased another way, this says that
to predict the future, we only need to know where we are and not how we got there.
Let’s try to give a more precise description of this property, which is known as the
Markov property.
Fix r and let Zt = Wt+r −Wr. Clearly the map t →Zt is continuous since the
same is true for W. Since Zt −Zs = Wt+r −Ws+r, then the distribution of Zt −Zs is
normal with mean zero and variance (t + r) −(s + r). One can also check the other parts
of the definition to show that Zt is also a Brownian motion.
Recall that a stopping time in the continuous framework is a r.v. T taking values
in [0, ∞) such that (T ≤t) ∈Ft for all t. To make a satisfactory theory, we need that the
Ft be right continuous (see Section 10), but this is fairly technical and we will ignore it.
If T is a stopping time, FT is the collection of events A such that A ∩(T > t) ∈Ft
for all t.
Let us try to provide some motivation for this definition of FT . It will be simpler to
consider the discrete time case. The analogue of FT in the discrete case is the following:
if N is a stopping time, let
FN = {A : A ∩(N ≤k) ∈Fk for all k}.
If Xk is a sequence that is adapted to the σ-fields Fk, that is, Xk is Fk measurable when
k = 0, 1, 2, . . ., then knowing which events in Fk have occurred allows us to calculate Xk
for each k. So a reasonable definition of FN should allow us to calculate XN whenever
we know which events in FN have occurred or not. Or phrased another way, we want XN
to be FN measurable. Where did the sequence Xk come from? It could be any adapted
sequence. Therefore one definition of the σ-field of events occurring before time N might
be:
Consider the collection of random variables XN where Xk is a sequence adapted
to Fk. Let GN be the smallest σ-field with respect to which each of these random
variables XN is measurable.
In other words, we want GN to be the σ-field generated by the collection of random
variables XN for all sequences Xk that are adapted to Fk.
We show in Note 1 that FN = GN. The σ-field FN is just a bit easier to work with.
Now we proceed to the strong Markov property for Brownian motion, the proof of
which is given in Note 2.
Proposition 17.1. If Xt is a Brownian motion and T is a bounded stopping time, then
XT +t −XT is a mean 0 variance t random variable and is independent of FT .
This proposition says: if you want to predict XT +t, you could do it knowing all of
FT or just knowing XT . Since XT +t −XT is independent of FT , the extra information
given in FT does you no good at all.
We need a way of expressing the Markov and strong Markov properties that will
generalize to other processes.
Let Wt be a Brownian motion. Consider the process W x
t = x + Wt, which is known
as Brownian motion started at x. Define Ω′ to be set of continuous functions on [0, ∞), let
Xt(ω) = ω(t), and let the σ-field be the one generated by the Xt. Define Px on (Ω′, F′) by
Px(Xt1 ∈A1, . . . , Xtn ∈An) = P(W x
t1 ∈A1, . . . , W x
tn ∈An).
What we have done is gone from one probability space Ωwith many processes W x
t to one
process Xt with many probability measures Px.
An example in the Markov chain setting might help. No knowledge of Markov chains
is necessary to understand this. Suppose we have a Markov chain with 3 states, A, B, and
C. Suppose we have a probability P and three different Markov chains. The first, called
XA
n , represents the position at time n for the chain started at A. So XA
0 = A, and XA
1 can
be one of A, B, C, XA
2 can be one of A, B, C, and so on. Similarly we have XB
n , the chain
started at B, and XC
n .
Define Ω′ = {(AAA), (AAB), (ABA), . . . , (BAA), (BAB), . . .}.
So Ω′ denotes the possible sequence of states for time n = 0, 1, 2.
If ω = ABA, set
Y0(ω) = A, Y1(ω) = B, Y2(ω) = A, and similarly for all the other 26 values of ω. Define
PA(AAA) = P(XA
= A, XA
= A, XA
= A).
Similarly define PA(AAB), . . ..
Define
PB(AAA) = P(XB
0 = A, XB
1 = A, XB
2 = A) (this will be 0 because we know XB
0 = B),
and similarly for the other values of ω. We also define PC. So we now have one process,
Yn, and three probabilities PA, PB, PC. As you can see, there really isn’t all that much
going on here.
Here is another formulation of the Markov property.
Proposition 17.2. If s < t and f is bounded or nonnegative, then
E x[f(Xt) | Fs] = E Xs[f(Xt−s)],
a.s.
The right hand side is to be interpreted as follows. Define ϕ(x) = E xf(Xt−s). Then
E Xsf(Xt−s) means ϕ(Xs(ω)). One often writes Ptf(x) for E xf(Xt). We prove this in
Note 3.
This formula generalizes: If s < t < u, then
E x[f(Xt)g(Xu) | Fs] = E Xs[f(Xt−s)g(Xu−s)],
and so on for functions of X at more times.
Using Proposition 17.1, the statement and proof of Proposition 17.2 can be extended
to stopping times.
Proposition 17.3. If T is a bounded stopping time, then
E x[f(XT +t) | FT ] = E XT [f(Xt)].
We can also establish the Markov property and strong Markov property in the
context of solutions of stochastic differential equations. If we let Xx
t denote the solution
to
Xx
t = x +
Z t
σ(Xx
s )dWs +
Z t
b(Xx
s )ds,
so that Xx
t is the solution of the SDE started at x, we can define new probabilities by
Px(Xt1 ∈A1, . . . , Xtn ∈An) = P(Xx
t1 ∈A1, . . . , Xx
tn ∈An).
This is similar to what we did in defining Px for Brownian motion, but here we do not
have translation invariance. One can show that when there is uniqueness for the solution
to the SDE, the family (Px, Xt) satisfies the Markov and strong Markov property. The
statement is precisely the same as the statement of Proposition 17.3.
Note 1. We want to show GN = FN. Since GN is the smallest σ-field with respect to which
XN is measurable for all adapted sequences Xk and it is easy to see that FN is a σ-field, to
show GN ⊂FN, it suffices to show that XN is measurable with respect to FN whenever Xk
is adapted. Therefore we need to show that for such a sequence Xk and any real number a,
the event (XN > a) ∈FN.
Now (XN > a) ∩(N = j) = (Xj > a) ∩(N = j). The event (Xj > a) ∈Fj
since X is an adapted sequence.
Since N is a stopping time, then (N ≤j) ∈Fj and
(N ≤j −1)c ∈Fj−1 ⊂Fj, and so the event (N = j) = (N ≤j) ∩(N ≤j −1)c is in Fj. If
j ≤k, then (N = j) ∈Fj ⊂Fk. Therefore
(XN > a) ∩(N ≤k) = ∪k
j=0((XN > a) ∩(N = j)) ∈Fk,
which proves that (XN > a) ∈FN.
To show FN ⊂GN, we suppose that A ∈FN. Let Xk = 1A∩(N≤k). Since A ∈FN,
then A∩(N ≤k) ∈Fk, so Xk is Fk measurable. But XN = 1A∩(N≤N) = 1A, so A = (XN >
0) ∈GN. We have thus shown that FN ⊂GN, and combining with the previous paragraph,
we conclude FN = GN.
Note 2.
Let Tn be defined by Tn(ω) = (k + 1)/2n if T(ω) ∈[k/2n, (k + 1)/2n). It is easy
to check that Tn is a stopping time. Let f be continuous and A ∈FT . Then A ∈FTn as
well. We have
E [f(XTn+t −XTn); A] =
X
E [f(X k
2n +t −X k
2n ); A ∩Tn = k/2n]
=
X
E [f(X k
2n +t −X k
2n )]P(A ∩Tn = k/2n)
= E f(Xt)P(A).
Let n →∞, so
E [f(XT +t −XT ); A] = E f(Xt)P(A).
Taking limits this equation holds for all bounded f.
If we take A = Ωand f = 1B, we see that XT +t −XT has the same distribution as Xt,
which is that of a mean 0 variance t normal random variable. If we let A ∈FT be arbitrary
and f = 1B, we see that
P(XT +t −XT ∈B, A) = P(Xt ∈B)P(A) = P(XT +t −XT ∈B)P(A),
which implies that XT +t −XT is independent of FT .
Note 3.
Before proving Proposition 17.2, recall from undergraduate analysis that every
bounded function is the limit of linear combinations of functions eiux, u ∈R. This follows
from using the inversion formula for Fourier transforms. There are various slightly different
formulas for the Fourier transform. We use bf(u) =
R
eiuxf(x) dx. If f is smooth enough and
has compact support, then one can recover f by the formula
f(x) = 1
2π
Z
e−iux bf(u) du.
We can first approximate this improper integral by
2π
Z N
−N
e−iux bf(u) du
by taking N larger and larger. For each N we can approximate
2π
R N
−N e−iux bf(u) du by using
Riemann sums. Thus we can approximate f(x) by a linear combination of terms of the form
eiujx. Finally, bounded functions can be approximated by smooth functions with compact
support.
Proof. Let f(x) = eiux. Then
E x[eiuXt | Fs] = eiuXsE x[eiu(Xt−Xs) | Fs]
= eiuXse−u2(t−s)/2.
On the other hand,
ϕ(y) = E y[f(Xt−s)] = E [eiu(Wt−s+y)] = eiuye−u2(t−s)/2.
So ϕ(Xs) = E x[eiuXt | Fs]. Using linearity and taking limits, we have the lemma for all f.


## 18. Martingale Representation Theorem

18. Martingale representation theorem.
In this section we want to show that every random variable that is Ft measurable
can be written as a stochastic integral of Brownian motion. In the next section we use
this to show that under the model of geometric Brownian motion the market is complete.
This means that no matter what option one comes up with, one can exactly replicate the
result (no matter what the market does) by buying and selling shares of stock.
In mathematical terms, we let Ft be the σ-field generated by Ws, s ≤t. From (16.2)
we see that Ft is also the same as the σ-field generated by Ss, s ≤t, so it doesn’t matter
which one we work with. We want to show that if V is Ft measurable, then there exists
Hs adapted such that
V = V0 +
Z
HsdWs,
(18.1)
where V0 is a constant.
Our goal is to prove
Theorem 18.1. If V is Ft measurable and E V 2 < ∞, then there exists a constant c and
an adapted integrand Hs with E
R t
0 H2
s ds < ∞such that
V = c +
Z t
HsdWs.
Before we prove this, let us explain why this is called a martingale representation
theorem. Suppose Ms is a martingale adapted to Fs, where the Fs are the σ-field generated
by a Brownian motion. Suppose also that E M 2
t < ∞. Set V = Mt. By Theorem 18.1, we
can write
Mt = V = c +
Z t
HsdWs.
The stochastic integral is a martingale, so for r ≤t,
Mr = E [Mt | Fr] = c + E
h Z t
HsdWs | Fr
i
= c +
Z r
HsdWs.
We already knew that stochastic integrals were martingales; what this says is the converse:
every martingale can be represented as a stochastic integral. Don’t forget that we need
E M 2
t < ∞and Ms adapted to the σ-fields of a Brownian motion.
In Note 1 we show that if every martingale can be represented as a stochastic
integral, then every random variable V that is Ft measurable can, too, provided E V 2 < ∞.
There are several proofs of Theorem 18.1. Unfortunately, they are all technical. We
outline one proof here, giving details in the notes. We start with the following, proved in
Note 2.
Proposition 18.2. Suppose
V n = cn +
Z t
Hn
s dWs,
cn →c,
E |V n −V |2 →0,
and for each n the process Hn is adapted with E
R t
0(Hn
s )2ds < ∞. Then there exist a
constant c and an adapted Hs with E
R t
0 H2
s ds < ∞so that
Vt = c +
Z t
HsdWs.
What this proposition says is that if we can represent a sequence of random variables Vn
and Vn →V , then we can represent V .
Let R be the collection of random variables that can be represented as stochastic
integrals. By this we mean
R = {V : E V 2 < ∞,V is Ft measurable,V = c +
Z t
HsdWs
for some adapted H with E
Z t
H2
s ds < ∞}.
Next we show R contains a particular collection of random variables. (The proof is
in Note 3.)
Proposition 18.3. If g is bounded, the random variable g(Wt) is in R.
An almost identical proof shows that if f is bounded, then
f(Wt −Ws) = c +
Z t
s
HrdWr
for some c and Hr.
Proposition 18.4. If t0 ≤t1 ≤· · · ≤tn ≤t and f1, . . . , fn are bounded functions, then
f1(Wt1 −Wt0)f2(Wt2 −Wt1) · · · fn(Wtn −Wtn−1) is in R.
See Note 4 for the proof.
We now finish the proof of Theorem 18.1. We have shown that a large class of
random variables is contained in R.
Proof of Theorem 18.1. We have shown that random variables of the form
f1(Wt1 −Wt0)f2(Wt2 −Wt1) · · · fn(Wtn −Wtn−1)
(18.2)
are in R. Clearly if Vi ∈R for i = 1, . . . , m, and ai are constants, then a1V1 + · · · amVm is
also in R. Finally, from measure theory we know that if E V 2 < ∞and V is Ft measurable,
we can find a sequence Vk such that E |Vk −V |2 →0 and each Vk is a linear combination
of random variables of the form given in (18.2). Now apply Proposition 18.2.
Note 1.
Suppose we know that every martingale Ms adapted to Fs with E M 2
t can be
represented as Mr = c+
R r
0 HsdWs for some suitable H. If V is Ft measurable with E V 2 < ∞,
let Mr = E [V | Fr]. We know this is a martingale, so
Mr = c +
Z r
HsdWs
for suitable H. Applying this with r = t,
V = E [V | Ft] = Mt = c +
Z t
HsdWs.
Note 2. We prove Proposition 18.2. By our assumptions,
E |(V n −cn) −(V m −cm)|2 →0
as n, m →∞. So
E

Z t
(Hn
s −Hm
s )dWs
→0.
From our formulas for stochastic integrals, this means
E
Z t
|Hn
s −Hm
s |2ds →0.
This says that Hn
s is a Cauchy sequence in the space L2 (with respect to the norm ∥· ∥2 given
by ∥Y ∥2 =

E
R t
0 Y 2
s ds
1/2
). Measure theory tells us that L2 is a complete metric space, so
there exists Hs such that
E
Z t
|Hn
s −Hs|2ds →0.
In particular Hn
s →Hs, and this implies Hs is adapted. Another consequence, due to Fatou’s
lemma, is that E
R t
0 H2
s ds.
Let Ut =
R t
0 HsdWs. Then as above,
E |(V n −cn) −Ut|2 = E
Z t
(Hn
s −Hs)2ds →0.
Therefore Ut = V −c, and U has the desired form.
Note 3. Here is the proof of Proposition 18.3. By Ito’s formula with Xs = −iuWs + u2s/2
and f(x) = ex,
eXt = 1 +
Z t
eXs(−iu)dWs +
Z t
eXs(u2/2)ds
+ 1
Z t
eXs(−iu)2ds
= 1 −iu
Z t
eXsdWs.
If we multiply both sides by e−u2t/2, which is a constant and hence adapted, we obtain
e−iuWt = cu +
Z t
Hu
s dWs
(18.3)
for an appropriate constant cu and integrand Hu.
If f is a smooth function (e.g., C∞with compact support), then its Fourier transform
bf will also be very nice. So if we multiply (18.3) by bf(u) and integrate over u from −∞to
∞, we obtain
f(Wt) = c +
Z t
HsdWs
for some constant c and some adapted integrand H. (We implicitly used Proposition 18.2,
because we approximate our integral by Riemann sums, and then take a limit.) Now using
Proposition 18.2 we take limits and obtain the proposition.
Note 4. The argument is by induction; let us do the case n = 2 for clarity. So we suppose
V = f(Wt)g(Wu −Wt).
From Proposition 18.3 we now have that
f(Wt) = c +
Z t
HsdWs,
g(Wu −Wt) = d +
Z u
t
KsdWs.
Set Hr = Hr if 0 ≤s < t and 0 otherwise. Set Kr = Kr if s ≤r < t and 0 otherwise. Let
Xs = c +
R s
0 HrdWr and Ys = d +
R s
0 KrdWr. Then
⟨X, Y ⟩s =
Z s
HrKrdr = 0.
Then by the Ito product formula,
XsYs = X0Y0 +
Z s
XrdYr +
Z s
YrdXr
+ ⟨X, Y ⟩s
= cd +
Z s
[XrKr + YrHr]dWr.
If we now take s = u, that is exactly what we wanted. Note that XrKr + YrHr is 0 if r > u;
this is needed to do the general induction step.


## 19. Completeness

19. Completeness.
Now let Pt be a geometric Brownian motion. As we mentioned in Section 16, if
Pt = P0 exp(σWt + (µ −r −σ2/2)t), then given Pt we can determine Wt and vice versa,
so the σ fields generated by Pt and Wt are the same. Recall Pt satisfies
dPt = σPtdWt + (µ −r)Ptdt.
Define a new probability P by
dP
dP = Mt = exp(aWt −a2t/2).
By the Girsanov theorem,
f
Wt = Wt −at
is a Brownian motion under P. So
dPt = σPtdf
Wt + σPtadt + (µ −r)Ptdt.
If we choose a = −(µ −r)/σ, we then have
dPt = σPtdf
Wt.
(19.1)
Since f
Wt is a Brownian motion under P, then Pt must be a martingale, since it is a
stochastic integral of a Brownian motion. We can rewrite (19.1) as
df
Wt = σ−1P −1
t
dPt.
(19.2)
Given a Ft measurable variable V , we know by Theorem 18.1 that there exist a
constant and an adapted process Hs such that E
R t
0 H2
s ds < ∞and
V = c +
Z t
Hsdf
Ws.
But then using (19.2) we have
V = c +
Z t
Hsσ−1P −1
s
dPs.
We have therefore proved
Theorem 19.1. If Pt is a geometric Brownian motion and V is Ft measurable and square
integrable, then there exist a constant c and an adapted process Ks such that
V = c +
Z t
KsdPs.
Moreover, there is a probability P under which Pt is a martingale.
The probability P is called the risk-neutral measure. Under P the present day value
of the stock price is a martingale.

