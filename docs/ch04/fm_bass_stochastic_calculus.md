# Stochastic Integrals & Ito's Formula

!!! info "Source"
    **The Basics of Financial Mathematics** by Richard F. Bass, University of Connecticut, Spring 2003.
    These notes are used for educational purposes.

## 12. Stochastic Integrals

12. Stochastic integrals.
If one wants to consider the (deterministic) integral
R t
0 f(s) dg(s), where f and g
are continuous and g is continuously differentiable, we can define it analogously to the
usual Riemann integral as the limit of Riemann sums Pn
i=1 f(si)[g(si) −g(si−1)], where
s1 < s2 < · · · < sn is a partition of [0, t]. This is known as the Riemann-Stieltjes integral.
One can show (using the mean value theorem, for example) that
Z t
f(s) dg(s) =
Z t
f(s)g′(s) ds.
If we were to take f(s) = 1[0,a](s) (which is not continuous, but that is a minor matter
here), one would expect the following:
Z t
1[0,a](s) dg(s) =
Z t
1[0,a](s)g′(s) ds =
Z a
g′(s) ds = g(a) −g(0).
Note that although we use the fact that g is differentiable in the intermediate stages, the
first and last terms make sense for any g.
We now want to replace g by a Brownian path and f by a random integrand. The
expression
R
f(s) dW(s) does not make sense as a Riemann-Stieltjes integral because it is
a fact that W(s) is not differentiable as a function of t. We need to define the expression
by some other means. We will show that it can be defined as the limit in L2 of Riemann
sums. The resulting integral is called a stochastic integral.
Let us consider a very special case first. Suppose f is continuous and deterministic
(i.e., does not depend on ω). Suppose we take a Riemann sum approximation
In =
2n−1
X
i=0
f( i
2n )[W( i+1
2n ) −W( i
2n )].
Since Wt has zero expectation for each t, E In = 0. Let us calculate the second moment:
E I2
n = E
h X
i
f( i
2n )[W( i+1
2n ) −W( i
2n )]
2i
(12.1)
= E
2n−1
X
i=0
f( i
2n )2[W( i+1
2n ) −W( i
2n )]2
+ E
X
i̸=j
f( i
2n )f( j
2n )[W( i+1
2n ) −W( i
2n )] [W( j+1
2n ) −W( j
2n )].
The first sum is bounded by
X
i
f( i
2n )2 1
2n ≈
Z 1
f(t)2dt,
since the second moment of W( i+1
2n ) −W( i
2n ) is 1/2n. Using the independence and the
fact that Wt has mean zero,
E

[W( i+1
2n −W( i
2n )] [W( j+1
2n −W( j
2n )]

= E [W( i+1
2n −W( i
2n )]E [W( j+1
2n −W( j
2n )] = 0,
and so the second sum on the right hand side of (12.1) is zero. This calculation is the key
to the stochastic integral.
We now turn to the construction. Let Wt be a Brownian motion. We will only
consider integrands Hs such that Hs is Fs measurable for each s (see Note 1). We will
construct
R t
0 Hs dWs for all H with
E
Z t
H2
s ds < ∞.
(12.2)
Before we proceed we will need to define the quadratic variation of a continuous
martingale. We will use the following theorem without proof because in our applications we
can construct the desired increasing process directly. We often say a process is a continuous
process if its paths are continuous, and similarly a continuous martingale is a martingale
with continuous paths.
Theorem 12.1. Suppose Mt is a continuous martingale such that E M 2
t < ∞for all t.
There exists one and only one increasing process At that is adapted to Ft, has continuous
paths, and A0 = 0 such that M 2
t −At is a martingale.
The simplest example of such a martingale is Brownian motion. If Wt is a Brownian
motion, we saw in Proposition 11.2 that W 2
t −t is a martingale. So in this case At = t
almost surely, for all t. Hence ⟨W⟩t = t.
We use the notation ⟨M⟩t for the increasing process given in Theorem 12.1 and call
it the quadratic variation process of M. We will see later that in the case of stochastic
integrals, where
Nt =
Z t
HsdWs,
it turns out that ⟨N⟩t =
R t
0 H2
s ds.
We will use the following frequently, and in fact, these are the only two properties
of Brownian motion that play a significant role in the construction.
Lemma 12.1. (a) E [Wb −Wa | Fa] = 0.
(b) E [W 2
b −W 2
a | Fa] = E [(Wb −Wa)2 | Fa] = b −a.
Proof. (a) This is E [Wb −Wa] = 0 by the independence of Wb −Wa from Fa and the
fact that Wb and Wa have mean zero.
(b) (Wb −Wa)2 is independent of Fa, so the conditional expectation is the same as
E [(Wb −Wa)2]. Since Wb −Wa is a N(0, b −a), the second equality in (b) follows.
To prove the first equality in (b), we write
E [W 2
b −W 2
a | Fa] = E [((Wb −Wa) + Wa)2 | Fa] −E [W 2
a | Fa]
= E [(Wb −Wa)2 | Fa] + 2E [Wa(Wb −Wa) | Fa] + E [W 2
a | Fa]
−E [W 2
a | Fa]
= E [(Wb −Wa)2 | Fa] + 2WaE [Wb −Wa | Fa],
and the first equality follows by applying (a).
We construct the stochastic integral in three steps. We say an integrand Hs = Hs(ω)
is elementary if
Hs(ω) = G(ω)1(a,b](s)
where 0 ≤a < b and G is bounded and Fa measurable. We say H is simple if it is a finite
linear combination of elementary processes, that is,
Hs(ω) =
n
X
i=1
Gi(ω)1(ai,bi](s).
(12.3)
We first construct the stochastic integral for H elementary; the work here is showing the
stochastic integral is a martingale. We next construct the integral for H simple and here
the difficulty is calculating the second moment. Finally we consider the case of general H.
First step. If G is bounded and Fa measurable, let Hs(ω) = G(ω)1(a,b](s), and define the
stochastic integral to be the process Nt, where Nt = G(Wt∧b −Wt∧a). Compare this to
the first paragraph of this section, where we considered Riemann-Stieltjes integrals.
Proposition 12.2. Nt is a continuous martingale, E N 2
∞= E [G2(b −a)] and
⟨N⟩t =
Z t
G21[a,b](s) ds.
Proof. The continuity is clear. Let us look at E [Nt | Fs]. In the case a < s < t < b, this
is equal to
E [G(Wt −Wa) | Fs] = GE [(Wt −Wa) | Fs] = G(Ws −Wa) = Ns.
In the case s < a < t < b, E [Nt | Fs] is equal to
E [G(Wt −Wa) | Fs] = E [GE [Wt −Wa | Fa] | Fs] = 0 = Ns.
The other possibilities are s < t < a < b, a < b < s < t, as < a < b < t, and a < s < b < t;
these are done similarly.
For E N 2
∞, we have using Lemma 12.1(b)
E N 2
∞= E [G2E [(Wb −Wa)2 | Fa]] = E [G2E [W 2
b −W 2
a | Fa]] = E [G2(b −a)].
For ⟨N⟩t, we need to show
E [G2(Wt∧b −Wt∧a)2 −G2(t ∧b −t ∧a) | Fs]
= G2(Ws∧b −Ws∧a)2 −G2(s ∧b −s ∧a).
We do this by checking all six cases for the relative locations of a, b, s, and t; we do one of
the cases in Note 2.
Second step. Next suppose Hs is simple as in (12.3). In this case define the stochastic
integral
Nt =
Z t
Hs dWs =
n
X
i=1
Gi(Wbi∧t −Wai∧t).
Proposition 12.3. Nt is a continuous martingale, E N 2
∞= E
R ∞
H2
s ds, and ⟨N⟩t =
R t
0 H2
s ds.
Proof. We may rewrite H so that the intervals (ai, bi] satisfy a1 ≤b1 ≤a2 ≤b2 ≤· · · ≤bn.
For example, if we had a1 < a2 < b1 < b2, we could write
Hs = G11(a1,a2] + (G1 + G2)1(a2,b1] + G21(b1,b2],
and then if we set G′
1 = G1, G′
2 = G1 + G2, G′
3 = G2 and a′
1 = a1, b′
1 = a2, a′
2 = a2, b′
2 =
b1, a′
3 = b1, b′
3 = b2, we have written H as
X
i=1
G′
i1(a′
i,b′
i].
So now we have H simple but with the intervals (a′
i, b′
i] non-overlapping.
Since the sum of martingales is clearly a martingale, Nt is a martingale. The sum
of continuous processes will be continuous, so Nt has continuous paths.
We have
E N 2
∞= E
h X
G2
i (Wbi −Wai)2i
+ 2E
h X
i<j
GiGj(Wbi −Wai)(Wbj −Waj)
i
.
The terms in the second sum vanish, because when we condition on Faj, we have
E [GiGj(Wbi −Wai)E [(Wbj −Waj) | Faj] = 0.
Taking expectations,
E [GiGj(Wbi −Wai)(Wbj −Waj)] = 0.
For the terms in the first sum, by Lemma 12.1
E [G2
i (Wbi −Wai)2] = E [G2
i E [(Wbi −Wai)2 | Fai]] = E [G2
i ([bi −ai)].
So
E N 2
∞=
n
X
i=1
E[G2
i ([bi −ai)],
and this is the same as E
R ∞
H2
s ds.
Third step. Now suppose Hs is adapted and E
R ∞
H2
s ds < ∞. Using some results from
measure theory (Note 3), we can choose Hn
s simple such that E
R ∞
0 (Hn
s −Hs)2 ds →0.
The triangle inequality then implies (see Note 3 again)
E
Z ∞
(Hn
s −Hm
s )2 ds →0.
Define N n
t =
R t
0 Hn
s dWs using Step 2. By Doob’s inequality (Theorem 10.3) we have
E [sup
t (N n
t −N m
t )2] = E
h
sup
t
 Z t
(Hn
s −Hm
s ) dWs
2i
≤4E
 Z ∞
(Hn
s −Hm
s ) dWs
2
= 4E
Z ∞
(Hn
s −Hm
s )2 ds →0.
This should look reminiscent of the definition of Cauchy sequences, and in fact that is what
is going on here; Note 3 has details. In the present context Cauchy sequences converge,
and one can show (Note 3) that there exists a process Nt such that
E
h
sup
t

Z t
Hn
s dWs −Nt

2i
→0.
If Hn
s and Hn
s
′ are two sequences converging to H, then E (
R t
0(Hn
s −Hn
s
′) dWs)2 =
E
R t
0(Hn
s −Hn
s
′)2 ds →0, or the limit is independent of which sequence Hn we choose. See
Note 4 for the proof that Nt is a martingale, E N 2
t = E
R t
0 H2
s ds, and ⟨N⟩t =
R t
0 H2
s ds.
Because supt[
R t
0 Hn
s dWs −Nt] →0, one can show there exists a subsequence such that the
convergence takes place almost surely, and with probability one, Nt has continuous paths
(Note 5).
We write Nt =
R t
0 Hs dWs and call Nt the stochastic integral of H with respect to
W.
We discuss some extensions of the definition. First of all, if we replace Wt by a
continuous martingale Mt and Hs is adapted with E
R t
0 H2
s d⟨M⟩s < ∞, we can duplicate
everything we just did (see Note 6) with ds replaced by d⟨M⟩s and get a stochastic integral.
In particular, if d⟨M⟩s = K2
sds, we replace ds by K2
sds.
There are some other extensions of the definition that are not hard. If the random
variable
R ∞
H2
s d⟨M⟩s is finite but without its expectation being finite, we can define the
stochastic integral by defining it for t ≤TN for suitable stopping times TN and then letting
TN →∞; look at Note 7.
A process At is of bounded variation if the paths of At have bounded variation. This
means that one can write At = A+
t −A−
t , where A+
t and A−
t have paths that are increasing.
|A|t is then defined to be A+
t + A−
t . A semimartingale is the sum of a martingale and a
process of bounded variation. If
R ∞
H2
s d⟨M⟩s +
R ∞
|Hs| |dAs| < ∞and Xt = Mt + At,
we define
Z t
Hs dXs =
Z t
Hs dMs +
Z t
Hs dAs,
where the first integral on the right is a stochastic integral and the second is a Riemann-
Stieltjes or Lebesgue-Stieltjes integral. For a semimartingale, we define ⟨X⟩t = ⟨Mt⟩. Note
7 has more on this.
Given two semimartingales X and Y we define ⟨X, Y ⟩t by what is known as polar-
ization:
⟨X, Y ⟩t = 1
2[⟨X + Y ⟩t −⟨X⟩t −⟨Y ⟩t].
As an example, if Xt =
R t
0 HsdWs and Yt =
R t
0 KsdWs, then (X +Y )t =
R t
0(Hs +Ks)dWs,
so
⟨X + Y ⟩t =
Z t
(Hs + Ks)2ds =
Z t
H2
s ds +
Z t
2HsKsds +
Z t
K2
sds.
Since ⟨X⟩t =
R t
0 H2
s ds with a similar formula for ⟨Y ⟩t, we conclude
⟨X, Y ⟩t =
Z t
HsKsds.
The following holds, which is what one would expect.
Proposition 12.4. Suppose Ks is adapted to Fs and E
R ∞
K2
sds < ∞.
Let Nt =
R t
0 KsdWs. Suppose Hs is adapted and E
R ∞
H2
s d⟨N⟩s < ∞. Then E
R ∞
H2
s K2
sds < ∞
and
Z t
HsdNs =
Z t
HsKsdWs.
The argument for the proof is given in Note 8.
What does a stochastic integral mean? If one thinks of the derivative of Zt as being
a white noise, then
R t
0 HsdZs is like a filter that increases or decreases the volume by a
factor Hs.
For us, an interpretation is that Zt represents a stock price. Then
R t
0 HsdZs repre-
sents our profit (or loss) if we hold Hs shares at time s. This can be seen most easily if
Hs = G1[a,b]. So we buy G(ω) shares at time a and sell them at time b. The stochastic
integral represents our profit or loss.
Since we are in continuous time, we are allowed to buy and sell continuously and
instantaneously.
What we are not allowed to do is look into the future to make our
decisions, which is where the Hs adapted condition comes in.
Note 1.
Let us be more precise concerning the measurability of H that is needed. H is a
stochastic process, so can be viewed as a map from [0, ∞) × Ωto R by H : (s, ω) →Hs(ω).
We define a σ-field P on [0, ∞)×Ωas follows. Consider the collection of processes of the form
G(ω)1(a,b])(s) where G is bounded and Fa measurable for some a < b. Define P to be the
smallest σ-field with respect to which every process of this form is measurable. P is called the
predictable or previsible σ-field, and if a process H is measurable with respect to P, then the
process is called predictable. What we require for our integrands H is that they be predictable
processes.
If Hs has continuous paths, then approximating continuous functions by step functions
shows that such an H can be approximated by linear combinations of processes of the form
G(ω)1(a,b])(s). So continuous processes are predictable. The majority of the integrands we
will consider will be continuous.
If one is slightly more careful, one sees that processes whose paths are functions which
are continuous from the left at each time point are also predictable. This gives an indication
of where the name comes from.
If Hs has paths which are left continuous, then Ht =
limn→∞Ht−1
n , and we can “predict” the value of Ht from the values at times that come
before t. If Ht is only right continuous and a path has a jump at time t, this is not possible.
Note 2.
Let us consider the case a < s < t < b; again similar arguments take care of the
other five cases. We need to show
E [G2(Wt −Wa)2 −G2(t −a) | Fs] = G2(Ws −Wa)2 −G2(s −a).
(12.4)
The left hand side is equal to G2E [(Wt −Wa)2 −(t −a) | Fs]. We write this as
G2E [((Wt −Ws) + (Ws −Wa))2 −(t −a) | Fs]
= G2n
E [(Wt −Ws)2 | Fs] + 2E [(Wt −Ws)(Ws −Wa) | Fs]
+ E [(Ws −Wa)2 | Fs] −(t −a)
o
= G2n
E [(Wt −Ws)2] + 2(Ws −Wa)E [Wt −Ws | Fs] + (Ws −Wa)2 −(t −a)
o
= G2n
(t −s) + 0 + (Ws −Wa)2 −(t −a)
o
.
The last expression is equal to the right hand side of (12.4).
Note 3. A definition from measure theory says that if µ is a measure, ∥f∥2, the L2 norm of
f with respect to the measure µ, is defined as
 R
f(x)2µ(dx)
1/2
. The space L2 is defined
to be the set of functions f for which ∥f∥2 < ∞. (A technical proviso: one has to identify as
equal functions which differ only on a set of measure 0.) If one defines a distance between two
functions f and g by d(f, g) = ∥f −g∥2, this is a metric on the space L2, and a theorem from
measure theory says that L2 is complete with respect to this metric. Another theorem from
measure theory says that the collection of simple functions (functions of the form Pn
i=1 ci1Ai)
is dense in L2 with respect to the metric.
Let us define a norm on stochastic processes; this is essentially an L2 norm. Define
∥N∥=

E
sup
0≤t<∞
N 2
t
1/2
.
One can show that this is a norm, and hence that the triangle inequality holds. Moreover, the
space of processes N such that ∥N∥< ∞is complete with respect to this norm. This means
that if N n is a Cauchy sequence, i.e., if given ε there exists n0 such that ∥N n −N m∥< ε
whenever n, m ≥n0, then the Cauchy sequence converges, that is, there exists N with ∥N∥<
∞such that ∥N n −N∥→0.
We can define another norm on stochastic processes. Define
∥H∥2 =

E
Z ∞
H2
s ds
1/2
.
This can be viewed as a standard L2 norm, namely, the L2 norm with respect to the measure
µ defined on P by
µ(A) = E
Z ∞
1A(s, ω)ds.
Since the set of simple functions with respect to µ is dense in L2, this says that if H is
measurable with respect to P, then there exist simple processes Hn
s that are also measurable
with respect to P such that ∥Hn −H∥2 →0.
Note 4. We have ∥N n −N∥→0, where the norm here is the one described in Note 3. Each
N n is a stochastic integral of the type described in Step 2 of the construction, hence each N n
t
is a martingale. Let s < t and A ∈Fs. Since E [N n
t | Fs] = N n
s , then
E [N n
t ; A] = E [N n
s ; A].
(12.5)
By Cauchy-Schwarz,
|E [N n
t ; A] −E [Nt; A]| ≤E [ |N n
t −Nt|; A] ≤

E [(N n
t −Nt)2]
1/2
E [12
A]
1/2
≤∥N n −N∥→0.
(12.6)
We have a similar limit when t is replaced by s, so taking the limit in (12.5) yields
E [Nt; A] = E [Ns; A].
Since Ns is Fs measurable and has the same expectation over sets A ∈Fs as Nt does, then
by Proposition 4.3 E [Nt | Fs] = Ns, or Nt is a martingale.
Suppose ∥N n −N∥→0. Given ε > 0 there exists n0 such that ∥N n −N∥< ε if
n ≥n0. Take ε = 1 and choose n0. By the triangle inequality,
∥N∥≤∥N n∥+ ∥N n −N∥≤∥N n∥+ 1 < ∞
since ∥N n∥is finite for each n.
That N 2
t −⟨N⟩t is a martingale is similar to the proof that Nt is a martingale, but
slightly more delicate. We leave the proof to the reader, but note that in place of (SEC.402)
one writes
|E [(N n
t )2; A] −E [(Nt)2; A]| ≤E [ |(N n
t )2 −(Nt)2|] ≤E [ |N n
t −Nt| |N n
t + Nt|].
(12.7)
By Cauchy-Schwarz this is less than
∥N n
t −Nt∥∥N n
t + Nt∥.
since ∥N n
t + Nt∥≤∥N n
t ∥+ ∥Nt∥is bounded independently of n, we see that the left hand
side of (12.7) tends to 0.
Note 5. We have ∥N n −N∥→0, where the norm is described in Note 3. This means that
E [sup
t |N n
t −Nt|2] →0.
A result from measure theory implies that there exists a subsequence nk such that
sup
t |N nk
t
−Nt|2 →0,
a.s.
So except for a set of ω’s of probability 0, N nk
t (ω) converges to Nt(ω) uniformly. Each N nk
t (ω)
is continuous by Step 2, and the uniform limit of continuous functions is continuous, therefore
Nt(ω) is a continuous function of t. Incidentally, this is the primary reason we considered
Doob’s inequalities.
Note 6.
If Mt is a continuous martingale, E [Mb −Ma | Fa] = E [Mb | Fa] −Ma =
Ma −Ma = 0. This is the analogue of Lemma 12.1(a). To show the analogue of Lemma
12.1(b),
E [(Mb −Ma)2 | Fa] = E [M 2
b | Fa] −2E [MbMa | Fa] + E [M 2
a | Fa]
= E [M 2
b | Fa] −2MaE [Mb | Fa] + M 2
a
= E [M 2
b −⟨M⟩b | Fa] + E [⟨M⟩b −⟨M⟩a | Fa] + M 2
a −⟨M⟩a
= E [⟨M⟩b −⟨M⟩a | Fa],
since M 2
t −⟨M⟩t is a martingale. That
E [M 2
b −M 2
a | Fa] = E [⟨M⟩b −⟨M⟩a | Fa]
is just a rewriting of
E [M 2
b −⟨M⟩b | Fa] = M 2
a −⟨M⟩a = E [M 2
a −⟨M⟩a | Fa].
With these two properties in place of Lemma 12.1, replacing Ws by Ms and ds by
d⟨M⟩s, the construction of the stochastic integral
R t
0 HsdMs goes through exactly as above.
Note 7.
If we let TK = inf{t > 0 :
R t
0 H2
s d⟨M⟩s ≥K}, the first time the integral is larger
than or equal to K, and we let HK
s = Hs1(s≤TK), then
R ∞
HK
s d⟨M⟩s ≤K and there is no
difficulty defining N K
t
=
R t
0 HK
s dMs for every t. One can show that if t ≤TK1 and TK2, then
N K1
t
= N K2
t
a.s. If
R t
0 Hsd⟨M⟩s is finite for every t, then TK →∞as K →∞. If we call the
common value Nt, this allows one to define the stochastic integral Nt for each t in the case
where the integral
R t
0 H2
s d⟨M⟩s is finite for every t, even if the expectation of the integral is
not.
We can do something similar is Mt is a martingale but where we do not have E ⟨M⟩∞<
∞. Let SK = inf{t : |Mt| ≥K}, the first time |Mt| is larger than or equal to K. If we let
M K
t
= Mt∧SK, where t ∧Sk = min(t, SK), then one can show M K is a martingale bounded
in absolute value by K. So we can define JK
t
=
R t
0 HsdM K
t
for every t, using the paragraph
above to handle the wider class of H’s, if necessary. Again, one can show that if t ≤SK1 and
t ≤SK2, then the value of the stochastic integral will be the same no matter whether we use
M K1 or M K2 as our martingale. We use the common value as a definition of the stochastic
integral Jt. We have SK →∞as K →∞, so we have a definition of Jt for each t.
Note 8. We only outline how the proof goes. To show
Z t
HsdNs =
Z t
HsKsdWs,
(12.8)
one shows that (SEC.801) holds for Hs simple and then takes limits. To show this, it suffices
to look at Hs elementary and use linearity. To show (12.8) for Hs elementary, first prove this
in the case when Ks is elementary, use linearity to extend it to the case when K is simple, and
then take limits to obtain it for arbitrary K. Thus one reduces the proof to showing (12.8)
when both H and K are elementary. In this situation, one can explicitly write out both sides
of the equation and see that they are equal.


## 13. Ito's Formula

13. Ito’s formula.
Suppose Wt is a Brownian motion and f : R →R is a C2 function, that is, f and its
first two derivatives are continuous. Ito’s formula, which is sometime known as the change
of variables formula, says that
f(Wt) −f(W0) =
Z t
f ′(Ws)dWs + 1
Z t
f ′′(Ws)ds.
Compare this with the fundamental theorem of calculus:
f(t) −f(0) =
Z t
f ′(s)ds.
In Ito’s formula we have a second order term to carry along.
The idea behind the proof is quite simple. By Taylor’s theorem.
f(Wt) −f(W0) =
n−1
X
i=0
[f(W(i+1)t/n) −f(Wit/n)]
≈
n−1
X
i=1
f ′(Wit/n)(W(i+1)t/n −Wit/n)
+ 1
n−1
X
i=0
f ′′(Wit/n)(W(i+1)t/n −Wit/n)2.
The first sum on the right is approximately the stochastic integral and the second is
approximately the quadratic variation.
For a more general semimartingale Xt = Mt + At, Ito’s formula reads
Theorem 13.1. If f ∈C2, then
f(Xt) −f(X0) =
Z t
f ′(Xs)dXs + 1
Z t
f ′′(Xs)d⟨M⟩s.
Let us look at an example. Let Wt be Brownian motion, Xt = σWt −σ2t/2, and
f(x) = ex. Then ⟨X⟩t = ⟨σW⟩t = σ2t, f ′(x) = f”(x) = ex, and
eσWt−σ2t/2 = 1 +
Z t
eXsσdWs −1
Z t
eXs 1
2σ2ds
(13.1)
+ 1
Z t
eXsσ2ds
= 1 +
Z t
eXsσdWs.
This example will be revisited many times later on.
Let us give another example of the use of Ito’s formula.
Let Xt = Wt and let
f(x) = xk. Then f ′(x) = kxk−1 and f ′′(x) = k(k −1)xk−2. We then have
W k
t = W k
0 +
Z t
kW k−1
s
dWs + 1
Z t
k(k −1)W k−2
s
d⟨W⟩s
=
Z t
kW k−1
s
dWs + k(k −1)
Z t
W k−2
s
ds.
When k = 3, this says W 3
t −3
R t
0 Ws ds is a stochastic integral with respect to a Brownian
motion, and hence a martingale.
For a semimartingale Xt = Mt+At we set ⟨X⟩t = ⟨M⟩t. Given two semimartingales
X, Y , we define
⟨X, Y ⟩t = 1
2[⟨X + Y ⟩t −⟨X⟩t −⟨Y ⟩t].
The following is known as Ito’s product formula.
It may also be viewed as an
integration by parts formula.
Proposition 13.2. If Xt and Yt are semimartingales,
XtYt = X0Y0 +
Z t
XsdYs +
Z t
YsdXs + ⟨X, Y ⟩t.
Proof. Applying Ito’s formula with f(x) = x2 to Xt + Yt, we obtain
(Xt + Yt)2 = (X0 + Y0)2 + 2
Z t
(Xs + Ys)(dXs + dYs) + ⟨X + Y ⟩t.
Applying Ito’s formula with f(x) = x2 to X and to Y , then
X2
t = X2
0 + 2
Z t
XsdXs + ⟨X⟩t
and
Y 2
t = Y 2
0 + 2
Z t
YsdYs + ⟨Y ⟩t.
Then some algebra and the fact that
XtYt = 1
2[(Xt + Yt)2 −X2
t −Y 2
t ]
yields the formula.
There is a multidimensional version of Ito’s formula: if Xt = (X1
t , . . . , Xd
t ) is a
vector, each component of which is a semimartingale, and f ∈C2, then
f(Xt) −f(X0) =
d
X
i=1
Z t
∂f
∂xi
(Xs)dXi
s + 1
d
X
i,j=1
Z t
∂2f
∂x2
i
(Xs)d⟨Xi, Xj⟩s.
The following application of Ito’s formula, known as L´evy’s theorem, is important.
Theorem 13.3. Suppose Mt is a continuous martingale with ⟨M⟩t = t. Then Mt is a
Brownian motion.
Before proving this, recall from undergraduate probability that the moment generating
function of a r.v. X is defined by mX(a) = E eaX and that if two random variables have
the same moment generating function, they have the same law. This is also true if we
replace a by iu. In this case we have ϕX(u) = E eiuX and ϕX is called the characteristic
function of X. The reason for looking at the characteristic function is that ϕX always
exists, whereas mX(a) might be infinite. The one special case we will need is that if X is
a normal r.v. with mean 0 and variance t, then ϕX(u) = e−u2t/2. This follows from the
formula for mX(a) with a replaced by iu (this can be justified rigorously).
Proof. We will prove that Mt is a N(0, t); for the remainder of the proof see Note 1.
We apply Ito’s formula with f(x) = eiux. Then
eiuMt = 1 +
Z t
iueiuMsdMs + 1
Z t
(−u2)eiuMsd⟨M⟩s.
Taking expectations and using ⟨M⟩s = s and the fact that a stochastic integral is a
martingale, hence has 0 expectation, we have
E eiuMt = 1 −u2
Z t
eiuMsds.
Let J(t) = E eiuMt. The equation can be rewritten
J(t) = 1 −u2
Z t
J(s)ds.
So J′(t) = −1
2u2J(t) with J(0) = 1. The solution to this elementary ODE is J(t) =
e−u2t/2. Since
E eiuMt = e−u2t/2,
then by our remarks above the law of Mt must be that of a N(0, t), which shows that Mt
is a mean 0 variance t normal r.v.
Note 1. If A ∈Fs and we do the same argument with Mt replaced by Ms+t −Ms, we have
eiu(Ms+t−Ms) = 1 +
Z t
iueiu(Ms+r−Ms)dMr + 1
Z t
(−u2)eiu(Ms+r−Ms)d⟨M⟩r.
Multiply this by 1A and take expectations. Since a stochastic integral is a martingale, the
stochastic integral term again has expectation 0. If we let K(t) = E [eiu(Mt+s−Mt); A], we
now arrive at K′(t) = −1
2u2K(t) with K(0) = P(A), so
K(t) = P(A)e−u2t/2.
Therefore
E
h
eiu(Mt+s−Ms); A
i
= E eiu(Mt+s−Ms)P(A).
(13.2)
If f is a nice function and bf is its Fourier transform, replace u in the above by −u, multiply
by bf(u), and integrate over u. (To do the integral, we approximate the integral by a Riemann
sum and then take limits.) We then have
E [f(Ms+t −Ms); A] = E [f((Ms+t −Ms)]P(A).
By taking limits we have this for f = 1B, so
P(Ms+t −Ms ∈B, A) = P(Ms+t −Ms ∈B)P(A).
This implies that Ms+t −Ms is independent of Fs.
Note Var (Mt −Ms) = t −s; take A = Ωin (13.2).


## 14. The Girsanov Theorem

14. The Girsanov theorem.
Suppose P is a probability and
dXt = dWt + µ(Xt)dt,
where Wt is a Brownian motion. This is short hand for
Xt = X0 + Wt +
Z t
µ(Xs)ds.
(14.1)
Let
Mt = exp

−
Z t
µ(Xs)dWs −
Z t
µ(Xs)2ds/2

.
(14.2)
Then as we have seen before, by Ito’s formula, Mt is a martingale. This calculation is
reviewed in Note 1. We also observe that M0 = 1.
Now let us define a new probability by setting
Q(A) = E [Mt; A]
(14.3)
if A ∈Ft. We had better be sure this Q is well defined. If A ∈Fs ⊂Ft, then E [Mt; A] =
E [Ms; A] because Mt is a martingale. We also check that Q(Ω) = E [Mt; Ω] = E Mt. This
is equal to E M0 = 1, since Mt is a martingale.
What the Girsanov theorem says is
Theorem 14.1. Under Q, Xt is a Brownian motion.
Under P, Wt is a Brownian motion and Xt is not. Under Q, the process Wt is no
longer a Brownian motion.
In order for a process Xt to be a Brownian motion, we need at a minimum that Xt
is mean zero and variance t. To define mean and variance, we need a probability. Therefore
a process might be a Brownian motion with respect to one probability and not another.
Most of the other parts of the definition of being a Brownian motion also depend on the
probability.
Similarly, to be a martingale, we need conditional expectations, and the conditional
expectation of a random variable depends on what probability is being used.
There is a more general version of the Girsanov theorem.
Theorem 14.2. If Xt is a martingale under P, then under Q the process Xt −Dt is a
martingale where
Dt =
Z t
1
Ms
d⟨X, M⟩s.
⟨X⟩t is the same under both P and Q.
Let us see how Theorem 14.1 can be used. Let St be the stock price, and suppose
dSt = σStdWt + mStdt.
(So in the above formulation, µ(x) = m for all x.) Define
Mt = e(−m/σ)(Wt)−(m2/2σ2)t.
Then from (13.1) Mt is a martingale and
Mt = 1 +
Z t

−m
σ

MsdWs.
Let Xt = Wt. Then
⟨X, M⟩t =
Z t

−m
σ

Msds = −
Z t
Ms
m
σ ds.
Therefore
Z t
1
Ms
d⟨X, M⟩s = −
Z t
m
σ ds = −(m/σ)t.
Define Q by (14.3).
By Theorem 14.2, under Q the process f
Wt = Wt + (m/σ)t is a
martingale. Hence
dSt = σSt(dWt + (m/σ)dt) = σStdf
Wt,
or
St = S0 +
Z t
σSsdf
Ws
is a martingale. So we have found a probability under which the asset price is a martingale.
This means that Q is the risk-neutral probability, which we have been calling P.
Let us give another example of the use of the Girsanov theorem. Suppose Xt =
Wt + µt, where µ is a constant. We want to compute the probability that Xt exceeds the
level a by time t0.
We first need the probability that a Brownian motion crosses a level a by time t0.
If At = sups≤t Wt, (note we are not looking at |Wt|), we have
P(At > a, c ≤Wt ≤d) =
Z d
c
ϕ(t, a, x),
(14.4)
where
ϕ(t, a, x) =
(
√
2πte−x2/2t
x ≥a
√
2πte−(2a−x)2/2t
x < a.
This is called the reflection principle, and the name is due to the derivation, given in Note
2. Sometimes one says
P(Wt = x, At > a) = P(Wt = 2a −x),
x < a,
but this is not precise because Wt is a continuous random variable and both sides of the
above equation are zero; (14.4) is the rigorous version of the reflection principle.
Now let Wt be a Brownian motion under P. Let dQ/dP = Mt = eµWt−µ2t/2. Let
Yt = Wt −µt. Theorem 14.1 says that under Q, Yt is a Brownian motion.
We have
Wt = Yt + µt.
Let A = (sups≤t0 Ws ≥a). We want to calculate
P(sup
s≤t0
(Ws + µs) ≥a).
Wt is a Brownian motion under P while Yt is a Brownian motion under Q. So this proba-
bility is equal to
Q(sup
s≤t0
(Ys + µs) ≥a).
This in turn is equal to
Q(sup
s≤t0
Ws ≥a) = Q(A).
Now we use the expression for Mt:
Q(A) = E P[eµWt0−µ2t0/2; A]
=
Z ∞
−∞
eµx−µ2t0/2P(sup
s≤t0
Ws ≥a, Wt0 = x)dx
= e−µ2t0/2h Z a
−∞
√2πt0
eµxe−(2a−x)2/2t0 dx +
Z ∞
a
√2πt0
eµxe−x2/2t0 dx.
i
Proof of Theorem 14.1. Using Ito’s formula with f(x) = ex,
Mt = 1 −
Z t
µ(Xr)MrdWr.
So
⟨W, M⟩t = −
Z t
µ(Xr)Mr dr.
Since Q(A) = E P[Mt; A], it is not hard to see that
E Q[Wt; A] = E P[MtWt; A].
By Ito’s product formula this is
E P
h Z t
MrdWr; A
i
+ E P
h Z t
WrdMr; A
i
+ E P
h
⟨W, M⟩t; A
i
.
Since
R t
0 MrdWr and
R t
0 WrdMr are stochastic integrals with respect to martingales, they
are themselves martingales. Thus the above is equal to
E P
h Z s
MrdWr; A
i
+ E P
h Z s
WrdMr; A
i
+ E P
h
⟨W, M⟩t; A
i
.
Using the product formula again, this is
E P[MsWs; A] + E P[⟨W, M⟩t −⟨W, M⟩s; A] = E Q[Ws; A] + E P[⟨W, M⟩t −⟨W, M⟩s; A].
The last term on the right is equal to
E P
h Z t
s
d⟨W, M⟩r; A
i
= E P
h
−
Z t
s
Mrµ(Xr)dr; A
i
= E P
h
−
Z t
s
E P[Mt | Fr]µ(Xr)dr; A
i
= E P
h
−
Z t
s
Mtµ(Xr)dr; A
i
= E Q
h
−
Z t
s
µ(Xr)dr; A
i
= −E Q
h Z t
µ(Xr) dr; A
i
+ E Q
h Z s
µ(Xr) dr; A
i
.
Therefore
E Q
h
Wt +
Z t
µ(Xr)dr; A
i
= E Q
h
Ws +
Z s
µ(Xr)dr; A
i
,
which shows Xt is a martingale with respect to Q.
Similarly, X2
t −t is a martingale with respect to Q. By L´evy’s theorem, Xt is a
Brownian motion.
In Note 3 we give a proof of Theorem 14.2 and in Note 4 we show how Theorem
14.1 is really a special case of Theorem 14.2.
Note 1. Let
Yt = −
Z t
µ(Xs)dWs −1
Z t
[µ(Xs)]2ds.
We apply Ito’s formula with the function f(x) = ex. Note the martingale part of Yt is the
stochastic integral term and the quadratic variation of Y is the quadratic variation of the
martingale part, so
⟨Y ⟩t =
Z t
[−µ(Xs)]2ds.
Then f ′(x) = ex, f ′′(x) = ex, and hence
Mt = eYt = eY0 +
Z t
eYsdYs + 1
Z t
eYsd⟨Y ⟩s
= 1 +
Z t
Ms(−µ(Xs)dWs −1
Z t
[µ(Xs)]2ds
+ 1
Z t
Ms[−µ(Xs)]2ds
= 1 −
Z t
Msµ(Xs)dWs.
Since stochastic integrals with respect to a Brownian motion are martingales, this completes
the argument that Mt is a martingale.
Note 2.
Let Sn be a simple random walk. This means that X1, X2, . . . , are independent
and identically distributed random variables with P(Xi = 1) = P(Xi = −1) = 1
2; let Sn =
Pn
i=1 Xi. If you are playing a game where you toss a fair coin and win $1 if it comes up heads
and lose $1 if it comes up tails, then Sn will be your fortune at time n. Let An = max0≤k≤n Sk.
We will show the analogue of (14.4) for Sn, which is
P(Sn = x, An ≥a) =

P(Sn = x)
x ≥a
P(Sn = 2a −x)
x < a.
(14.5)
(14.4) can be derived from this using a weak convergence argument.
To establish (14.5), note that if x ≥a and Sn = x, then automatically An ≥a, so
the only case to consider is when x < a. Any path that crosses a but is at level x at time n
has a corresponding path determined by reflecting across level a at the first time the Brownian
motion hits a; the reflected path will end up at a + (a −x) = 2a −x. The probability on the
left hand side of (14.5) is the number of paths that hit a and end up at x divided by the total
number of paths. Since the number of paths that hit a and end up at x is equal to the number
of paths that end up at 2a−x, then the probability on the left is equal to the number of paths
that end up at 2a −x divided by the total number of paths; this is P(Sn = 2a −x), which is
the right hand side.
Note 3.
To prove Theorem 14.2, we proceed as follows. Assume without loss of generality
that X0 = 0. Then if A ∈Fs,
E Q[Xt; A] = E P[MtXt; A]
= E P
h Z t
Mr dXr; A
i
+ E P
h Z t
Xr dMr; A
i
+ E P[⟨X, M⟩t; A]
= E P
h Z s
Mr dXr; A
i
+ E P
h Z s
Xr dMr; A
i
+ E P[⟨X, M⟩t; A]
= E Q[Xs; A] + E Q[⟨X, M⟩t −⟨X, M⟩s; A].
Here we used the fact that stochastic integrals with respect to the martingales X and M are
again martingales.
On the other hand,
E P[⟨X, M⟩t −⟨X, M⟩s; A] = E P
h Z t
s
d⟨X, M⟩r; A
i
= E P
h Z t
s
Mr dDr; A
i
= E P
h Z t
s
E P[Mt | Fr] dDr; A
i
= E P
h Z t
s
Mt dDr; A
i
= E P[(Dt −Ds)Mt; A]
= E Q[Dt −Ds; A].
The proof of the quadratic variation assertion is similar.
Note 4. Here is an argument showing how Theorem 14.1 can also be derived from Theorem
14.2.
From our formula for M we have dMt = −Mtµ(Xt)dWt, and therefore d⟨X, M⟩t =
−Mtµ(Xt)dt. Hence by Theorem 14.2 we see that under Q, Xt is a continuous martingale
with ⟨X⟩t = t. By L´evy’s theorem, this means that X is a Brownian motion under Q.


## 15. Stochastic Differential Equations

15. Stochastic differential equations.
Let Wt be a Brownian motion. We are interested in the existence and uniqueness
for stochastic differential equations (SDEs) of the form
dXt = σ(Xt) dWt + b(Xt) dt,
X0 = x0.
(15.1)
This means Xt satisfies
Xt = x0 +
Z t
σ(Xs) dWs +
Z t
b(Xs) ds.
(15.2)
Here Wt is a Brownian motion, and (15.2) holds for almost every ω.
We have to make some assumptions on σ and b. We assume they are Lipschitz,
which means:
|σ(x) −σ(y)| ≤c|x −y|,
|b(x) −b(y)| ≤c|x −y|
for some constant c. We also suppose that σ and b grow at most linearly, which means:
|σ(x)| ≤c(1 + |x|),
|b(x)| ≤c(1 + |x|).
Theorem 15.1. There exists one and only one solution to (15.2).
The idea of the proof is Picard iteration, which is how existence and uniqueness for
ordinary differential equations is proved; see Note 1.
The intuition behind (15.1) is that Xt behaves locally like a multiple of Brownian
motion plus a constant drift: locally Xt+h −Xt ≈σ(Wt+h −Wt) + b((t + h) −t). However
the constants σ and b depend on the current value of Xt. When Xt is at different points,
the coefficients vary, which is why they are written σ(Xt) and b(Xt). σ is sometimes called
the diffusion coefficient and µ is sometimes called the drift coefficient.
The above theorem also works in higher dimensions. We want to solve
dXi
t =
d
X
j=1
σij(Xs)dW j
s + bi(Xs)ds,
i = 1, . . . , d.
This is an abbreviation for the equation
Xi
t = xi
0 +
Z t
d
X
j=1
σij(Xs)dW j
s +
Z t
bi(Xs)ds.
Here the initial value is x0 = (x1
0, . . . , xd
0), the solution process is Xt = (X1
t , . . . , Xd
t ), and
W 1
t , . . . , W d
t are d independent Brownian motions. If all of the σij and bi are Lipschitz
and grow at most linearly, we have existence and uniqueness for the solution.
Suppose one wants to solve
dZt = aZt dWt + bZt dt.
Note that this equation is linear in Zt, and it turns out that linear equations are almost
the only ones that have an explicit solution. In this case we can write down the explicit
solution and then verify that it satisfies the SDE. The uniqueness result above (Theorem
15.1) shows that we have in fact found the solution.
Let
Zt = Z0eaWt−a2t/2+bt.
We will verify that this is correct by using Ito’s formula. Let Xt = aWt −a2t/2+bt. Then
Xt is a semimartingale with martingale part aWt and ⟨X⟩t = a2t. Zt = eXt. By Ito’s
formula with f(x) = ex,
Zt = Z0 +
Z t
eXsdXs + 1
Z t
eXsa2ds
= Z0 +
Z t
aZsdWs −
Z t
a2
2 Zsds +
Z t
bZs ds
+ 1
Z t
a2Zsds
=
Z t
aZsdWs +
Z t
bZsds.
This is the integrated form of the equation we wanted to solve.
There is a connection between SDEs and partial differential equations. Let f be a
C2 function. If we apply Ito’s formula,
f(Xt) = f(X0) +
Z t
f ′(Xs)dXs + 1
Z t
f ′′(Xs)d⟨X⟩s.
From (15.2) we know ⟨X⟩t =
R t
0 σ(Xs)2ds. If we substitute for dXs and d⟨X⟩s, we obtain
f(Xt) = f(X0) +
Z t
f ′(Xs)dWs +
Z t
µ(Xs)ds
+ 1
Z t
f ′′(Xs)σ(Xs)2ds
= f(X0) +
Z t
f ′(Xs)dWs +
Z t
Lf(Xs)ds,
where we write
Lf(x) = 1
2σ(x)2f ′′(x) + µ(x)f ′(x).
L is an example of a differential operator. Since the stochastic integral with respect to a
Brownian motion is a martingale, we see from the above that
f(Xt) −f(X0) −
Z t
Lf(Xs)ds
is a martingale. This fact can be exploited to derive results about PDEs from SDEs and
vice versa.
Note 1. Let us illustrate the uniqueness part, and for simplicity, assume b is identically 0 and
σ is bounded.
Proof of uniqueness. If X and Y are two solutions,
Xt −Yt =
Z t
[σ(Xs) −σ(Ys)]dWs.
So
E |Xt −Yt|2 = E
Z t
|σ(Xs) −σ(Ys)|2ds ≤c
Z t
E |Xs −Ys|2ds,
using the Lipschitz hypothesis on σ. If we let g(t) = E |Xt −Yt|2, we have
g(t) ≤c
Z t
g(s) ds.
Since we are assuming σ is bounded, E X2
t = E
R t
0(σ(Xs))2ds ≤ct and similarly for E Y 2
t , so
g(t) ≤ct. Then
g(t) ≤c
Z t
h
c
Z s
g(r) dr
i
ds.
Iteration implies
g(t) ≤Atn/n!
for each n, which implies g must be 0.

