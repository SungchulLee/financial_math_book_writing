# Martingale Theory & Measure Change (Festschrift)

!!! info "Source"
    **From Stochastic Calculus to Mathematical Finance: The Shiryaev Festschrift** edited by Yu. Kabanov, R. Liptser, and J. Stoyanov, Springer, 2006.
    These notes are used for educational purposes.

## Martingale Theory and Applications

Some Particular Problems of Martingale Theory
115
and *
XτnY0 are (Ft)-martingales. By the reasoning above, XτnY σn is an (Ft)-
local martingale. Being bounded, it is an (Ft)-martingale. Consequently, for
any n ∈N, (XY )τn∧σn is an (Ft)-martingale. As τn ∧σn −−−−→
n→∞∞, we get
the desired statement.
⊓⊔
The next theorem shows that the answer to the problem in formulation 6
is positive.
Theorem 2.3. Let X and Y be independent continuous local martingales
(each with respect to its natural filtration). Then XY is a local martingale
(with respect to its natural filtration).
Proof. For n ∈N, set τn = inf{t : |Xt| ≥n}. Then the stopped process
Xτn is an (FX
t )-local martingale. As |Xτn| ≤|X0| ∨n and the latter random
variable is integrable, the process Xτn is an (FX
t )-martingale. For any s ≤t,
A ∈FX
s , and B ∈FY
s , we have
E(Xτn
t IAIB) = E(Xτn
t IA)P(B) = E(Xτn
s IA)P(B) = E(Xτn
s IAIB).
Applying the monotone class lemma, we deduce that Xτn is a martingale with
respect to the filtration Ft = FX
t ∨FY
t . As τn is an (Ft)-stopping time, X is
an (Ft)-local martingale. Similarly, Y is in the same class. By Theorem 2.2,
XY is an (Ft)-local martingale.
For n ∈N, set ρn = inf{t : |XtYt| ≥n}. Then (XY )ρn is an (Ft)-
local martingale. As |(XY )ρn| ≤|X0Y0| ∨n, the process (XY )ρn is an (Ft)-
martingale. Note that ρn is an (FXY
t
)-stopping time. Hence, XY is an (FXY
t
)-
local martingale.
⊓⊔
The next theorem shows that the answer to the problem in formulation 7
is positive.
Theorem 2.4. Let X and Y be independent continuous (Ft)-martingales.
Then XY is an (Ft)-martingale.
Proof. Set *
Xt = Xt −X0, *Yt = Yt −Y0. Then
XtYt = X0Y0 + X0 *Yt + *
XtY0 + *
Xt *Yt,
and it is sufficient to prove that *
X *Y is an (Ft)-martingale. Fix s ≤t. For
n ∈N, set τn = inf{t : | *
Xt| = n} and σn = inf{t : |*Yt| = n}. Then the
stopped processes *
Xτn and *Y σn are independent continuous (Ft)-martingales
and, by Theorem 2.2, *
Xτn *Y σn is an (Ft)-local martingale. Being bounded, it
is an (Ft)-martingale. Hence,
E
 *
Xτn
t
*Y σn
t
 Fs

= *
Xτn
s *Y σn
s
.
(2.1)
Furthermore, *
Xτn
t
a.s.
−−−−→
n→∞
*
Xt and the family
 *
Xτn
t

n∈N is uniformly integrable
due to the martingale property of *
X. Consequently, *
Xτn
t
L1
−−−−→
n→∞
*
Xt. Similarly,
*Y σn
t
L1
−−−−→
n→∞
*Yt. By the independence of *
X and *Y ,

116
A. Cherny
E
 *
Xτn
t
*Y σn
t
−*
Xt *Yt

≤E
 *
Xτn
t
*Y σn
t
−*Yt
 + E
 *
Xτn
t
−*
Xt
*Yt

= E
 *
Xτn
t
 · E
*Y σn
t
−*Yt
 + E
 *
Xτn
t
−*
Xt
 · E
*Yt

≤E
 *
Xt
 · E
*Y τn
t
−*Yt
 + E
 *
Xτn
t
−*
Xt
 · E
*Yt
 −−−−→
n→∞0.
(The last inequality is the Jensen inequality applied to the martingale *
X.)
Thus, *
Xτn
t
*Y σn
t
L1
−−−−→
n→∞
*
Xt *Yt. Now, (2.1) implies that E( *
Xt *Yt | Fs) = *
Xs *Ys,
which is the desired property.
⊓⊔
Formulation
Answer
1. X ∈M, Y ∈M, X ⊥⊥Y
?
=⇒XY ∈M
Yes,
Th.
2.1
2. X ∈Mloc, Y ∈Mloc, X ⊥⊥Y
?
=⇒XY ∈Mloc
No, Ex. 1
3. X ∈M(Ft), Y ∈M(Ft), X ⊥⊥Y
?
=⇒XY ∈M(Ft)
No, Ex. 2
4. X ∈Mloc(Ft), Y ∈Mloc(Ft), X ⊥⊥Y
?
=⇒XY ∈Mloc(Ft)
No, Ex. 2
5. X ∈Mc, Y ∈Mc, X ⊥⊥Y
?
=⇒XY ∈Mc
Yes,
Th. 2.1
6. X ∈Mc
loc, Y ∈Mc
loc, X ⊥⊥Y
?
=⇒XY ∈Mc
loc
Yes,
Th. 2.3
7. X ∈Mc(Ft), Y ∈Mc(Ft), X ⊥⊥Y
?
=⇒XY ∈Mc(Ft)
Yes,
Th. 2.4
8. X ∈Mc
loc(Ft), Y ∈Mc
loc(Ft), X ⊥⊥Y
?
=⇒XY ∈Mc
loc(Ft)
Yes,
Th. 2.2
Table 1. Summary of the answers to the problem “Is a product of
independent martingales also a martingale?”. Here we use the following
notation: “X ⊥⊥Y ” means that X and Y are independent; “X ∈M”
means that X is a martingale with respect to its natural filtration;
“X ∈Mloc” means that X is a local martingale with respect to its
natural filtration; “X ∈Mc” means that X is a continuous martingale
with respect to its natural filtration; “X ∈M(Ft)” means that X is
an (Ft)-martingale, and so on.

Some Particular Problems of Martingale Theory
117
3 Limits of Martingales
The answer to the problem “Is a limit of a converging sequence of martin-
gales also a martingale?” in formulations 1.A–8.A is negative as shown by the
following example.
Example 3. Let ξ be a non-integrable symmetric (i.e. ξ
Law
= −ξ) random vari-
able. Set
Xn
t =

0,
t < 1,
−n ∨ξ ∧n,
t ≥1,
Xt =

0,
t < 1,
ξ,
t ≥1,
Ft = FX
t .
Then each Xn is a martingale with respect to its natural filtration as well as
with respect to the filtration (Ft). Furthermore, (Xn) converges to X in prob-
ability uniformly on compact intervals (hence, the convergence in distribution
also holds). However, X is not an (Ft)-local martingale.
Proof. The first two statements are obvious. The last one follows from the
property that for any (FX
t )-stopping time τ, we have {τ < 1} ∈.
t<1 FX
t
=
{∅, Ω}.
⊓⊔
The next example shows that the answer to the problem in formula-
tions 1.B, 1.C, 2.B, 2.C, 5.B, 5.C, 6.B, and 6.C is negative.
Example 4. Let B be a 3-dimensional Brownian motion started at a point
B0 ̸= 0. Set
Xt =
1

(B1
t )2 + (B2
t )2 + (B3
t )2 ,
t ≥0,
τn = inf{t ≥0 : Xt ≥n},
Xn
t = Xt∧τn,
t ≥0.
Then each Xn is a continuous martingale with respect to its natural filtration
as well as with respect to the filtration Ft = FX
t . Furthermore, (Xn) converges
to X in probability uniformly on compact intervals (hence, the convergence
in distribution also holds). However, X is not a martingale with respect to
any filtration.
Proof. By Itˆo’s formula,
Xt = X0 −
3

i=1
 t
0
Bi
s
((B1s)2 + (B2s)2 + (B3s)2)3/2 dBi
s.
Therefore, X and each Xn are (FB
t )-local martingales. Being bounded, each
Xn is an (FB
t )-martingale and hence, it also an (Ft)-martingale and a mar-
tingale with respect to its natural filtration.

118
A. Cherny
Without loss of generality, we can assume that B2
0 = B3
0 = 0. Then
EXt ≤E
1

(B2
t )2 + (B3
t )2 = const
√
t
−−−→
t→∞0.
This shows that X is not a martingale with respect to any filtration.
⊓⊔
The next example shows that the answer to the problem in formula-
tions 3.B, 3.C, 7.B, and 7.C is negative.
Example 5. Let B be a Brownian motion started at zero. For n ∈N, consider
the function
f n(t) = k2−n for t ∈[(k −1)2−n, k2−n),
k ∈N,
define
τ n
1 = inf{t ≥0 : an
1Bt = f n(t)},
Y n
t = an
1Bt∧τ n
1 ,
t ∈[0, 2−n),
and, for k = 1, 2, . . . , set
τ n
k+1 = inf{t ≥k2−n : Y n
k2−n + an
k+1(Bt −Bk2−n) = f n(t)},
Y n
t = Y n
k2−n + an
k+1

Bt∧τ n
k+1 −Bk2−n
,
t ∈[k2−n, (k + 1)2−n),
where (an
k)k∈N are positive real numbers growing to +∞so rapidly that
µL

t ≥0 : P(Y n
t = f n(t)) ≤1 −2−n
≤2−n
(3.1)
(here µL denotes the Lebesgue measure). Let ξ be a random variable that is
independent of B and has the exponential distribution with parameter 1. Set
Xn
t = Y n
ξt, Xt = ξt, Γt = σ(ξ) ∨FB
t , Ft = Γξt (note that, for any α ≥0,
ξα is a (Γt)-stopping time). Then each Xn is a continuous local martingale
with respect to its natural filtration as well as with respect to (Ft). Moreover,
Xn
t
P
−−−−→
n→∞Xt for any t ≥0 (hence, (Xn) also converges to X in the sense of
the weak convergence of finite-dimensional distributions). However, X is not
a local martingale with respect to any filtration.
Proof. Each process Y n is a stochastic integral of a locally bounded
(FB
t )-predictable process with respect to B. Hence, each Y n is a continu-
ous (FB
t )-local martingale. Consequently, each Y n is a continuous (Γt)-local
martingale. This implies that each Xn is a continuous (Ft)-local martingale
(see [5, Ch. V, Prop. 1.5]). Due the continuity of Xn, each Xn is a local
martingale with respect to its natural filtration.
It follows from (3.1) that Y n
t
a.s.
−−−−→
n→∞
t for µL-a.e. t ≥0. Hence,
Xn
ξt
a.s.
−−−−→
n→∞ξt for any t ≥0.

Some Particular Problems of Martingale Theory
119
The process X is not a local martingale with respect to any filtration since
it has continuous paths of finite variation.
⊓⊔
The proposition below shows that the answer to the problem in formula-
tions 4.B and 4.C is positive.
Proposition 1. Let (Xn) be a sequence of local martingales (each with respect
to its natural filtration) such that Xn
0 = 0 and |∆Xn| ≤a for some constant
a > 0. Suppose that (Xn) converges in distribution to a process X. Then X
is a local martingale (with respect to its natural filtration).
For the proof, see [2, Ch. IX, Cor. 1.19].
The theorem below shows that the answer to the problem in formulations
8.B and 8.C is positive.
Theorem 3.1. Let (Xn) be a sequence of (Ft)-local martingales such that
Xn
0 = 0 and |∆Xn| ≤a for some constant a > 0. Suppose that (Xn) converges
in probability uniformly on compact intervals to a process X. Then X is an
(Ft)-local martingale.
Proof. For m, n ∈N, set τm = inf{t : |Xt| ≥m}, σmn = inf{t : |Xn
t | ≥
2m}. Then, for any m ∈N and t, we have
τm ∧σmn ∧t
P
−−−−→
n→∞τm ∧t,
and hence, the sequence of stopped processes (Xn)τm∧σmn converges in prob-
ability uniformly on compact intervals as n →∞to the stopped process Xτm.
Note that
(Xn)τm∧σmn ≤2m + a.
(3.2)
Hence, (Xn)τm∧σmn is an (Ft)-martingale, i.e. for any s < t, we have
E

(Xn)τm∧σmn
t
 Fs

= (Xn)τm∧σmn
s
.
(3.3)
Combining the property
(Xn)τm∧σmn
t
P
−−−−→
n→∞Xτm
t
with (3.2), we conclude that
(Xn)τm∧σmn
t
L1
−−−−→
n→∞Xτm
t
.
This, together with (3.3), shows that Xτm
is an (Ft)-martingale. As
τm −−−−→
n→∞∞, X is an (Ft)-local martingale.
⊓⊔
The next theorem shows that the answer to the problem in formula-
tions 1.D, 2.D, 3.D, and 4.D is positive.

120
A. Cherny
Theorem 3.2. Let (Xn) be a sequence of martingales (each with respect to
its natural filtration) such that |Xn| ≤a for some constant a > 0. Suppose
that (Xn) converges to a process X in the sense of the weak convergence of
finite-dimensional distributions. Then X is a martingale (with respect to its
natural filtration).
Proof. Fix s ≤t. For any m ∈N, any s1 ≤· · · ≤sm ≤s, any bounded
continuous function f : Rm →R, and any n ∈N, we have
E(Xn
t f(Xn
s1, . . . , Xn
sm)) = E(Xn
s f(Xn
s1, . . . , Xn
sm)).
Letting n →∞, we get
E(Xtf(Xs1, . . . , Xsm)) = E(Xsf(Xs1, . . . , Xsm)).
By the Lebesgue dominated convergence theorem,
E(XtI(Xs1 ∈A1, . . . , Xsm ∈Am)) = E(XsI(Xs1 ∈A1, . . . , Xsm ∈Am))
for any intervals A1, . . . , Am. Due to the monotone class lemma,
{C ∈FX
s : E(XtIC) = E(XsIC)} = FX
s .
This is the desired statement.
⊓⊔
The next theorem shows that the answer to the problem in formula-
tions 5.D, 6.D, 7.D, and 8.D is positive.
Theorem 3.3. Let (Xn) be a sequence of (Ft)-martingales such that |Xn| ≤a
for some constant a > 0. Suppose that Xn
t
P
−−−−→
n→∞Xt for any t. Then X is an
(Ft)-martingale.
Proof. For any s ≤t and any n ∈N, we have E(Xn
t | Fs) = Xs. Further-
more, Xn
t
L1
−−−−→
n→∞Xt. Hence, E(Xt | Fs) = Xs.
⊓⊔
4 Stochastic Integrals with Respect to a Martingale
It follows from [4, Cor. 21] that the answer to the problem “Is a stochastic
integral of a bounded process with respect to a martingale also a martingale?”
is negative. Here we give an explicit counter-example (it follows from [4] that
such an example exists, but it is not constructed explicitly).
We construct a uniformly integrable (Ft)-martingale X = (Xt)t≥0 and
a bounded (Ft)-predictable process H = (Ht)t≥0 such that the stochastic
integral of H with respect to X is not a uniformly integrable martingale. This
yields the negative answer to the problem under consideration. Indeed, the
process

Some Particular Problems of Martingale Theory
121
A. No additional
B. Xn
0 = 0 and
C. Xn
0 = 0 and Xn
D. |Xn| ≤a
assumptions
|∆Xn| ≤a
are continuous
1. Xn ∈M, Xn
FD
−−−−→
n→∞X
?
=⇒X ∈M
No, Ex. 3
No, Ex. 4
No, Ex. 4
Yes, Th. 3.2
2. Xn ∈M, Xn
Law
−−−−→
n→∞X
?
=⇒X ∈M
No, Ex. 3
No, Ex. 4
No, Ex. 4
Yes, Th. 3.2
3. Xn ∈Mloc, Xn
FD
−−−−→
n→∞X
?
=⇒X ∈Mloc
No, Ex. 3
No, Ex. 5
No, Ex. 5
Yes, Th. 3.2
4. Xn ∈Mloc, Xn
Law
−−−−→
n→∞X
?
=⇒X ∈Mloc
No, Ex. 3
Yes, Prop. 1
Yes, Prop. 1
Yes, Th. 3.2
5. Xn ∈M(Ft), ∀t Xn
t
P
−−−−→
n→∞Xt
?
=⇒X ∈M(Ft)
No, Ex. 3
No, Ex. 4
No, Ex. 4
Yes, Th. 3.3
6. Xn ∈M(Ft), Xn
u.p.
−−−−→
n→∞X
?
=⇒X ∈M(Ft)
No, Ex. 3
No, Ex. 4
No, Ex. 4
Yes, Th. 3.3
7. Xn ∈Mloc(Ft), ∀t Xn
t
P
−−−−→
n→∞Xt
?
=⇒X ∈Mloc(Ft)
No, Ex. 3
No, Ex. 5
No, Ex. 5
Yes, Th. 3.3
8. Xn ∈Mloc(Ft), Xn
u.p.
−−−−→
n→∞X
?
=⇒X ∈Mloc(Ft)
No, Ex. 3
Yes, Th. 3.1
Yes, Th. 3.1
Yes, Th. 3.3
Table 2. Summary of the answers to the problem “Is a limit of a converging sequence of mar-
tingales also a martingale?”. Here we use the notation from Table 1 and the additional nota-
tion: “Xn
FD
−−−−→
n→∞X” means that (Xn) converges to X in the sense of the weak convergence of
finite-dimensional distributions; “Xn
Law
−−−−→
n→∞X” means that (Xn) converges to X in distribution;
“Xn
u.p.
−−−−→
n→∞X” means that (Xn) converges to X in probability uniformly on compact intervals.
Formulation
Additional assumptions
❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤

122
A. Cherny
*
Xt =

X
t
1−t ,
t < 1,
X∞,
t ≥1
is a martingale with respect to the filtration
*Ft =

F
t
1−t ,
t < 1,
F,
t ≥1.
Furthermore, the stochastic integral of the process *Ht = H
t
1−t I(t < 1) with
respect to *
X is not a martingale in view of the equality
 t
0
*Hsd *
Xs =

t
1−t
0
HsdXs,
t < 1.
Example 6. Let
an = 2n,
bn =
2n
2n2 −n + 1,
pn = n −1
2n2 ,
n ∈N.
Construct the sequence (Xn)n∈N and the sequence of sets (An)n∈N by
X0 = 1,
X1 = 1,
A1 = Ω, . . .
P(Xn+1 = a2 . . . an+1 | An) = pn+1,
P(Xn+1 = a2 . . . anbn+1 | An) = 1 −pn+1,
P(Xn+1 = Xn | Ac
n) = 1,
An+1 = {Xn+1 = a1 . . . an+1}, . . .
Define the continuous-time process (Xt)t≥0 by Xt = Xn for t ∈[n, n + 1). Set
Ft = FX
t
and consider
Ht =
∞

n=1
I(2n −1 < t ≤2n).
Then X is a uniformly integrable (Ft)-martingale, while the stochastic integral
of H with respect to X is not a uniformly integrable (Ft)-martingale.
Proof. Clearly, X is an (Ft)-martingale. For any n < m ∈N, we have
E|(Xm −Xn)| = E|(Xm −Xn)IAn|
= E|(Xm −Xn)IAn+1| + E|(Xm −Xn)IAnIAc
n+1|
= E|(Xm −Xn)IAn+1| + E|(Xn+1 −Xn)IAnIAc
n+1|.
One can check by the induction in m that (Xm −Xn)IAn+1 > 0 for m > n.
Thus,

Some Particular Problems of Martingale Theory
123
E|(Xm −Xn)IAn+1| = E(Xm −Xn)IAn+1
= E(Xn+1 −Xn)IAn+1 = E|(Xn+1 −Xn)IAn+1|,
and consequently,
E|(Xm −Xn)| = E|(Xn+1 −Xn)IAn|
= a2 . . . an(an+1 −1)p2 . . . pnpn+1 + a2 . . . an(1 −bn+1)p2 . . . pn(1 −pn+1)
≤a2 . . . anp2 . . . pn(an+1pn+1 + 1) = 1
n

n
n + 1 + 1

≤2
n.
As a result, the sequence (Xn)n∈N converges in L1, which means that X is a
uniformly integrable (Ft)-martingale.
Furthermore, for any n ≤m ∈N, we have
E
IA2nIAc
2n+1
 2m
0
HsdXs
 = E

IA2nIAc
2n+1
n

k=1
(X2k −X2k−1)

≥E

IA2nIAc
2n+1(X2n −X2n−1)

= p2 . . . p2n(1 −p2n+1)a2 . . . a2n−1(a2n −1)
≥1
4p2 . . . p2na2 . . . a2n = 1
8n.
Therefore,
E

 2m
0
HsdXs
 ≥
m

n=1
E
IA2nIAc
2n+1
 2m
0
HsdXs
 ≥
m

n=1
1
8n −−−−→
m→∞∞.
As a result, the stochastic integral of H with respect to X is not uniformly
integrable.
⊓⊔
5 Uniform Integrability of Martingales
The answer to the problem “If X = (Xt)t≥0 is a positive process such that
EXτ = EX0 < ∞for any finite stopping time τ, then is it true that X is
a uniformly integrable martingale?” is positive as shown by the following
theorem.
Theorem 5.1. Let (Ft) be a filtration satisfying the usual assumptions of
right-continuity and completeness. Let X = (Xt)t≥0 be an (Ft)-adapted posi-
tive c`adl`ag process such that EXτ = EX0 < ∞for any (Ft)-stopping time τ
that is finite a.s. Then X is a uniformly integrable (Ft)-martingale.

124
A. Cherny
Proof. Fix s ≤t and A ∈Fs. Consider stopping times τ1 = s and τ2 =
sIAc + tIA. Then the equality EXτ1 = EXτ2 implies that EXtIA = EXsIA. As
a result, X is an (Ft)-martingale.
Since X is positive, there exists a limit X∞= (a.s.) limt→∞Xt. By the
Fatou lemma for conditional expectations,
E(X∞| Ft) ≤Xt,
t ≥0.
(5.1)
In particular, EX∞≤EX0.
Suppose that EX∞< EX0. The process *
Xt = E(X∞| Ft), t ≥0 has
a c`adl`ag modification. Moreover, *
Xt
a.s.
−−−→
t→∞X∞. Consequently, the stopping
time
τ = inf

t ≥0 : |Xt −*
Xt| ≤EX0 −EX∞
2

is finite a.s. By the conditions of the theorem, EXτ = EX0, which implies that
E *
Xτ > EX0 −EX0 −EX∞
2
> EX∞.
This contradicts the equality E *
Xτ = EX∞, which is a consequence of the
optional stopping theorem for uniformly integrable martingales. As a result,
EX∞= EX0. This, combined with (5.1), shows that E(X∞| Ft) = Xt for any
t ≥0. The proof is completed.
⊓⊔
We conclude the paper by the following
Question. Let X = (Xt)t≥0 be an (Ft)-adapted c`adl`ag process such
that, for any (Ft)-stopping time τ that is finite a.s., the random variable
Xτ is integrable and EXτ = EX0. Is it true that X is a uniformly integrable
(Ft)-martingale?
References
1. Cherny, A.S.: General arbitrage pricing model: probability approache. Manu-
script, availbale at: http://mech.math.msu.su/~cherny
2. Jacod, J., Shiryaev, A.N.: Limit Theorems for Stochastic Processes. 2nd Ed.
Springer 2003
3. Liptser, R.S., Shiryaev, A.N.: Theory of Martingales. Kluwer Acad. Publ.,
Dortrecht 1989
4. Meyer, P.-A.: Un cours sur les int´egrales stochastiques. Lecture Notes in Mathe-
matics 511, 245–400 (1976)
5. Revuz, D., Yor, M.: Continuous Martingales and Brownian Motion. 3rd Ed.
Springer 2003
6. Yor, M.: Quelques int´eractions entre mesures vectorielles et int´egrales stochas-
tiques. Lecture Notes in Mathematics 713, 264–281 (1979)

On the Absolute Continuity and Singularity
of Measures on Filtered Spaces:
Separating Times
Alexander CHERNY and Mikhail URUSOV
1 Moscow State University,
Faculty of Mechanics and Mathematics,
Department of Probability Theory,
119992 Moscow, Russia.
cherny@mech.math.msu.su
2 Moscow State University,
Faculty of Mechanics and Mathematics,
Department of Probability Theory,
119992 Moscow, Russia.
urusov@mech.math.msu.su
Summary. We introduce the notion of a separating time for a pair of measures
P and *P on a filtered space. This notion is convenient for describing the mutual
arrangement of P and *P from the viewpoint of their absolute continuity and singu-
larity.
Furthermore, we find the explicit form of the separating time for the cases, where
P and *P are distributions of L´evy processes, distributions of Bessel processes, and so-
lutions of stochastic differential equations. The obtained results yield, in particular,
criteria for the (local) absolute continuity and singularity of P and *P.
Key words: Absolute continuity, Bessel processes, L´evy processes, local absolute
continuity, separating times, singularity, stochastic differential equations.
Mathematics Subject Classification (2000): 60G30, 60H10, 60J60
Contents
1. Introduction
126
2. Separating Times
129
2.1. Mutual Arrangement of a Pair of Measures on a
Measurable Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
2.2. Mutual Arrangement of a Pair of Measures
on a Filtered Space. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .129
3. Separating Times for L´evy Processes
133
4. Separating Times for Bessel Processes
134

126
A. Cherny and M. Urusov
5. Separating Times for Solutions of SDEs
135
5.1. Basic Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
5.2. Exploding Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
5.3. Explicit Form of the Separating Time . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
5.4. Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
5.5. Proof of Theorem 5.1. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .144
Appendix
165
References
166
1 Introduction
The problems of absolute continuity and singularity of probability measures
defined on a filtered space play a significant role both in the pure stochastic
analysis and in its applications (for example, financial mathematics). The con-
tribution of A.N. Shiryaev to this subject is large and well known. This is rep-
resented, in particular, by his papers [13], [14], [22], [23], [24], [25], [28] as well
as his monographs [12], [26], [27], and [37]. The plenary talk of A.N. Shiryaev
at the International Congress of Mathematics (Helsinki, 1978) was entitled
“Absolute continuity and singularity of probability measures in functional
spaces”. We therefore hold it an honor to be able to put our paper in the
Festschrift.
The problems that are typically studied in relation to the subject men-
tioned concern such questions as: whether two measures are (locally) ab-
solutely continuous, whether they are singular, etc. However, a situation may
naturally occur, where the two measures are neither (locally) absolutely con-
tinuous nor singular.
Consider the following example: Ω= C([0, ∞)), (Ft) is the canonical
filtration, and P (resp., *P) is the distribution of a γ-dimensional (resp., *γ-
dimensional) Bessel process started at a point x0 > 0. If γ ∧*γ < 2, then, for
any t > 0, the measures
Pt = P | Ft
and
*Pt = *P | Ft
are neither equivalent nor singular. To be more precise, the situation is as
follows: for any stopping time τ such that τ < T0 := inf{t ≥0 : Xt = 0} (here
X is the coordinate process), the measures
Pτ = P | Fτ
and
*Pτ = *P | Fτ
are equivalent; for any stopping time τ ≥T0, Pτ and *Pτ are singular. Thus,
the time T0 plays the following important role in this example: informally,
this is the time, at which P and *P are separated one from another.
The situation described above admits a clear interpretation in terms of
statistical sequential analysis, which is another big topic of the research activ-
ity of A.N. Shiryaev (this is reflected, in particular, by his monographs [27],

Separating Times
127
[36], and [38]). Suppose that we are observing a process X that is governed
either by the measure P or by the measure *P (these are the measures described
above) and are trying to distinguish between these two hypotheses. Then, un-
til the time X hits zero, we cannot say for sure what the true measure is; but
immediately after this time we can say for sure what the true measure is. This
situation is in contrast with the typical setup of statistical sequential analysis,
where the two hypotheses are typically assumed to be locally equivalent.
Let us now consider the general situation: let (Ω, F, (Ft)t∈[0,∞)) be a space
with a right-continuous filtration (here F = .
t Ft) and P, *P be two probabil-
ity measures on this space. In Section 2, we formalize the concept of the time,
at which the two measures are separated. Namely, we prove that there exists
a P, *P-a.s. unique stopping time S with the property: for any stopping time τ,
the measures Pτ and *Pτ are equivalent on the set {τ < S} and are singular on
the set {τ ≥S} (actually, S is given by inf{t ≥0 : Zt = 0 or Zt = 2}, where
Z denotes the density process of P with respect to (P + *P)/2). Informally, P
and *P are equivalent before the time S and are singular after this time. We
call S the separating time for P and *P. In order to be able to distinguish the
situation, where P and *P are locally equivalent and are globally singular (i.e.
singular on F), from the situation, where they are globally equivalent, we add
a point δ > ∞to [0, ∞] and allow S to take values in [0, ∞] ∪{δ} (informally,
the equality S(ω) = δ means that P and *P are “globally equivalent on the ele-
mentary outcome ω”). The properties such as (local) absolute continuity and
singularity are easily expressed in terms of a separating time (see Lemma 2.1).
For example, *P ≪P iffS = δ *P-a.s., *P
loc
≪P iffS ≥∞*P-a.s. (i.e.
*P(S ∈{∞, δ}) = 1); *P0 ⊥P0 iffS = 0 P, *P-a.s., etc.
In order to illustrate the notion of a separating time, we give in Section 3
the explicit form of this time for the case, where P and *P are distributions of
L´evy processes. This is just a translation of known results into the language
of separating times.
In Section 4, we consider the case, where P and *P are distributions of Bessel
processes of different dimensions started at the same point and prove that in
this case the separating time has the form S = inf{t ≥0 : Xt = 0}, where
X denotes the coordinate process. This puts the above discussion related to
Bessel processes on a solid mathematical basis.
The introduction of separating times enables us to give a complete answer
to the problem of (local) absolute continuity and singularity of solutions of
one-dimensional homogeneous stochastic differential equations (abbreviated
below as SDEs), i.e. equations of the form
dXt = b(Xt)dt + σ(Xt)dBt,
X0 = x0
(1.1)
(the conditions we impose on the coefficients are the Engelbert–Schmidt condi-
tions, i.e. b and σ are measurable, σ ̸= 0 pointwise, and (1 + |b|)/σ2 ∈L1
loc(R);
this guarantees the existence and the uniqueness of a solution). Namely, in

128
A. Cherny and M. Urusov
Section 5, we find the explicit form of the separating time for the measure P
being the solution of (1.1) and the measure *P being the solution of a SDE
dXt = *b(Xt)dt + *σ(Xt)dBt,
X0 = x0.
As a corollary, we obtain criteria for (local) absolute continuity and singular-
ity of P and *P. The problems of (local) absolute continuity and singularity
for diffusion processes were extensively studied earlier. Let us mention the
papers [8], [10], [13], [14], [15], [16], [17], [23], [31] and the monographs [12,
Ch. IV,§ 4b], [27, Ch. 7]. We consider here a more particular case (only homo-
geneous SDEs), but in this case we obtain more complete results. Namely, in
the majority of the sources mentioned above, conditions for (local) absolute
continuity and singularity are given in random terms (typically, in terms of the
Hellinger process). In contrast, here the explicit form of the separating time
and conditions for (local) absolute continuity and singularity are obtained in
non-random terms, i.e. in terms of the coefficients of SDEs. In this respect,
our results are similar to those in [31]. Furthermore, all the sources mentioned
above (including [31]) deal with (local) absolute continuity or singularity of
measures, while our results are applicable to measures that are in a general
position, i.e. they are neither (locally) equivalent nor singular.
Let us illustrate the structure of the results of Section 5 by a simple ex-
ample. Let P and *P be solutions of SDEs
dXt = σ(Xt)dBt,
X0 = x0,
dXt = *b(Xt)dt + *σ(Xt)dBt,
X0 = x0,
respectively. We assume that both equations satisfy the Engelbert–Schmidt
conditions. Let us also assume for the simplicity of presentation that *P is non-
exploding (P is non-exploding automatically), although we consider exploding
solutions as well. Our results yield that the separating time for P and *P has
the form:
S =

δ
if *b = 0 and *σ2 = σ2 µL-a.e.,
+ inf{t ≥0 : Xt ∈A}
otherwise,
where X denotes the coordinate process, inf ∅:= ∞, µL denotes the Lebesgue
measure, and A denotes the complement to the set
1
x ∈R : *b2/*σ4 ∈L1
loc(x) and *σ2 = σ2 µL-a.e. in a vicinity of x
2
.
As a corollary,
*P ≪P ⇐⇒P ≪*P ⇐⇒*P = P ⇐⇒*b = 0 and *σ2 = σ2 µL-a.e.,
*P
loc
≪P ⇐⇒P
loc
≪*P ⇐⇒*b2/*σ4 ∈L1
loc(R) and *σ2 = σ2 µL-a.e.,
P0 ⊥*P0 ⇐⇒*b2/*σ4 /∈L1
loc(x0)
or ∀ε>0, µL((x0−ε, x0+ε)∩{*σ2 ̸=σ2})>0.

Separating Times
129
Some facts concerning the qualitative behaviour of solutions of SDEs (these
are needed in the proofs of results of Section 5) are given in the Appendix.
A shortened version of this paper appeared as [5].
2 Separating Times
2.1. Mutual arrangement of a pair of measures on a measurable
space. Let P and *P be probability measures on a measurable space (Ω, F).
The following result is well known.
Proposition 1. There exists a decomposition Ω= E ⊔D ⊔*D, E, D, *D ∈F
such that *P ∼P on the set E and P( *D) = *P(D) = 0 (here “ ⊔” denotes the
disjoint union). This decomposition is unique P, *P-a.s.
Remarks. (i) For the above decomposition, we have *P ∼P on E and
*P ⊥P on Ec (here Ec denotes the complement to E). The decomposition
Ω= E ⊔Ec with these properties is also unique P, *P-a.s.
(ii) The sets E, D, *D from Proposition 1 can be obtained as:
*D =

dP
dQ = 0, d*P
dQ > 0

, E =

dP
dQ > 0, d*P
dQ > 0

,
D =

dP
dQ > 0, d*P
dQ = 0

,
where Q = P+*P
2 .
(iii) Proposition 1 admits the following statistical interpretation. Suppose
that we deal with the problem of distinguishing between two statistical hy-
potheses P and *P. Unlike the standard setting in statistics, we do not assume
that P and *P are equivalent. Suppose that an experiment is performed, and
an elementary outcome ω is obtained. If ω ∈D, we can definitely say that the
true hypothesis is P; if ω ∈*D, we can definitely say that the true hypothesis
is *P; if ω ∈E, we cannot say for sure what is the true hypothesis.
The result of Proposition 1 is illustrated by Figure 1.
2.2. Mutual arrangement of a pair of measures on a filtered space.
Let (Ω, F) be a measurable space endowed with a right-continuous filtration
(Ft)t∈[0,∞). Recall that the σ-field Fτ (τ is a stopping time) is defined by
Fτ =
/
A ∈F : A ∩{τ ≤t} ∈Ft for any t ∈[0, ∞)
0
.
(In particular, F∞= F.)

130
A. Cherny and M. Urusov
9
:;
< 9
:;
< 9
:;
<
*
D
E
D
*P
P
Figure 1. Mutual arrangement of a pair of
measures on a measurable space
Let P and *P be probability measures on F. As usually, Pτ (resp., *Pτ)
denotes the restriction of P (resp., *P) to Fτ.
In what follows, it will be convenient for us to consider the extended posi-
tive half-line [0, ∞]∪{δ}, where δ is an additional point. We order [0, ∞]∪{δ}
in the following way: we take the usual order on [0, ∞] and let δ > ∞.
Definition 1. An extended stopping time is a map T : Ω→[0, ∞] ∪{δ} such
that {T ≤t} ∈Ft for any t ∈[0, ∞].
The following theorem is an analog of Proposition 1 for a filtered space. A
similar statement is proved in [20, Lem. 5.2].
Theorem 2.1. (i) There exists an extended stopping time S such that, for
any stopping time τ,
*Pτ ∼Pτ on the set {τ < S},
(2.1)
*Pτ ⊥Pτ on the set {τ ≥S}.
(2.2)
(ii) If S′ is another extended stopping time with these properties, then
S′ = S P, *P-a.s.
Proof. (i) Set Q = P+*P
2 . Let (Zt)t∈[0,∞] and ( *Zt)t∈[0,∞] denote the density
processes of P and *P with respect to Q (we set Z∞= dP
dQ, *Z∞= d*P
dQ). Let (Ft)
denote the Q-completion of the filtration (Ft). Then the (Ft, Q)-martingales
Z and *Z have the modifications whose all trajectories are c`adl`ag. The time
S = inf{t ∈[0, ∞] : Zt = 0 or *Zt = 0}
(“inf” is the same as “inf”, except that inf ∅= δ) is an extended (Ft)-stopping
time. According to [12, Ch. I, Lem. 1.19], there exists an extended (Ft)-
stopping time S such that S = S Q-a.s. It follows from [12, Ch. III, Lem. 3.6]
that Zt *Zt = 0 on the stochastic interval [S, ∞] Q-a.s. Consequently, for any
(Ft)-stopping time τ, we have Zτ *Zτ = 0 Q-a.s. on {τ ≥S}. The equality
dPτ
dQτ
= EQ
 dP
dQ
 Fτ

= EQ(Z∞| Fτ) = Zτ

Separating Times
131
and the analogous equality for d*Pτ
dQτ complete the proof.
(ii) Proposition 1 implies that, for any stopping time τ, the sets {τ ≥S}
and {τ ≥S′} coincide P, *P-a.s. This yields the desired statement (one needs
to consider only the deterministic τ).
⊓⊔
Definition 2. A separating time for P and *P is an extended stopping time
that satisfies (2.1) and (2.2) for all stopping times τ.
Remarks. (i) It is seen from the proof of Theorem 2.1 (ii) that in defining
the separating time one may use only the deterministic τ.
(ii) Theorem 2.1 admits the following statistical interpretation (compare
with Remark (iii) after Proposition 1). Suppose that we deal with the problem
of the sequential distinguishing between two statistical hypotheses P and *P.
Assume for example that (Ft) is the natural filtration of an observed process
(Xt)t≥0. Suppose that an experiment is performed, and we are observing a
path of X. Then, until time S occurs, we cannot say definitely what the
true hypothesis is. But after S occurs, we can say definitely what the true
hypothesis is (on the set { *ZS = 0}, this is P; on the set {ZS = 0}, this is *P).
Corollary 2.1. (i) There exists an extended stopping time S such that, for
any stopping time τ,
*Pτ ≪Pτ on the set {τ < S},
(2.3)
*Pτ ⊥Pτ on the set {τ ≥S}.
(2.4)
(ii) If S′ is another extended stopping time with these properties, then
S′ = S *P-a.s.
Definition 3. A time separating *P from P is an extended stopping time that
satisfies (2.3) and (2.4) for any stopping time τ.
Clearly, a separating time for P and *P is also a time separating *P from P.
The converse is not true since the former time is unique P, *P-a.s., while the
latter time is unique only *P-a.s.
Informally, Theorem 2.1 states that the measures P and *P are equivalent
up to a random time S and become singular at a time S. The equality S = δ
means that P and *P never become singular, i.e. they are equivalent up to
infinity. Thus, the knowledge of the separating time yields the knowledge of
the mutual arrangement of P and *P. This is illustrated by the following result.
Its proof is straightforward.
Lemma 2.1. Let S be a separating time for P and *P. Then

132
A. Cherny and M. Urusov
(i)
*P ∼P
⇐⇒S = δ P, *P-a.s.;
(ii) *P ≪P ⇐⇒S = δ *P-a.s.;
(iii) *P
loc
∼P ⇐⇒S ≥∞P, *P-a.s.;
(iv) *P
loc
≪P ⇐⇒S ≥∞*P-a.s.;
(v) *P ⊥P
⇐⇒S ≤∞P, *P-a.s. ⇐⇒S ≤∞P-a.s.
(vi) *P0 ⊥P0 ⇐⇒S = 0 P, *P-a.s.
⇐⇒S = 0 P-a.s.
Remark. Other types of the mutual arrangement of P and *P are also easily
expressed in terms of the separating time. For example, for any t ∈[0, ∞],
*Pt ⊥Pt
⇐⇒
S ≤t P, *P-a.s.
⇐⇒
S ≤t P-a.s.
✲
q
q
q
q





















































/











1
2
D0
E0
*
D0
Du
Eu
*
Du
D∞
E∞
*
D∞
ω1
ω2
ω3
ω4
0
S(ω2)
u
∞
δ
t
Figure 2. Mutual arrangement of a pair of
measures on a filtered space (here S(ω1) = 0,
S(ω3) = ∞, S(ω4) = δ)
The mutual arrangement of P and *P is illustrated by Figure 2. In this
figure, the measure *P “lies above” the curve 1; the measure P “lies below”
the curve 2. The decomposition Ω= Et ⊔Dt ⊔*Dt of Proposition 1 for the
measurable space (Ω, Ft) is obtained by drawing a vertical line corresponding
to the time t. Figure 2 shows three decompositions of this type: for t = 0, for
t = u ∈(0, ∞), and for t = ∞.
The separating time for P and *P is illustrated as follows. If ω ∈D0 ⊔*D0,
then S(ω) = 0 (see ω = ω1 in Figure 2). If ω ∈E0, then S(ω) is the time,
at which the horizontal line drawn through the point ω crosses curves 1 or 2
(see ω = ω2 in Figure 2). If this line crosses neither curve 1 nor curve 2, then
S = ∞in the case ω ∈D∞⊔*D∞(see ω = ω3 in Figure 2), and S = δ in the
case ω ∈E∞(see ω = ω4 in Figure 2).

Separating Times
133
3 Separating Times for L´evy Processes
Let D([0, ∞), Rd) denote the space of the c`adl`ag functions [0, ∞) →Rd. Let
X denote the canonical process on this space, i.e Xt(ω) = ω(t). Consider the
filtration Ft = =
ε>0 σ(Xs; s ∈[0, t + ε]) and set F = .
t Ft. In what follows,
(· , ·) denotes the scalar product in Rd and ∥· ∥denotes the Euclidean norm.
Let P be the distribution of a L´evy process with characteristics (b, c, ν),
where b ∈Rd, c is a symmetric positively definite d × d matrix, and ν is a
measure on B(Rd) such that ν({0}) = 0 and

Rd(∥x∥2 ∧1) ν(dx) < ∞. This
means that, for any t ∈[0, ∞) and λ ∈Rd,
EPEi(λ,Xt)
= exp
/
t
)
i(λ, b) −1
2(λ, cλ) +

Rd(Ei(λ,x) −1 −i(λ, x)I(∥x∥≤1))ν(dx)
0
.
(For further information on L´evy processes, see [1], [34], [37, Ch. III, § 1b].)
Let *P be the distribution of a L´evy process with characteristics (*b, *c, *ν).
The following theorem yields an explicit form of the separating time for
P and *P. This is actually a reformulation of known results (see, for example,
the survey paper [35]) into the language of separating times.
Theorem 3.1. The separating time S for P and *P has the following form.
(i) If P = *P, then S = δ P, *P-a.s.
(ii) If P ̸= *P and
c = *c,
(3.1)

Rd
	>
dν
d(ν + *ν) −
>
d*ν
d(ν + *ν)

2
d(ν + *ν) < ∞,
(3.2)
b −*b −

{∥x∥≤1}
x d(ν −*ν ) ∈N(c),
(3.3)
where N(c) = {cx: x ∈Rd}, then
S = inf{t ∈[0, ∞): △Xt ̸= 0, △Xt /∈E} P, *P-a.s.
(we set inf ∅= ∞), where E ∈B(Rd) is a set such that *ν ∼ν on E and *ν ⊥ν
on the complement to E.
(iii) If any of conditions (3.1)–(3.3) is violated, then S = 0 P, *P-a.s.
Remarks. (i) The expression in (3.2) is the Hellinger distance between ν
and *ν.
(ii) If (3.2) is true, then

{∥x∥≤1} ∥x∥d∥ν −*ν∥< ∞, where ∥ν −*ν∥denotes
the total variance of the signed measure ν −*ν (see [34, Rem. 33.3] or [35,

134
A. Cherny and M. Urusov
Lem. 2.18]). Thus, the integral in (3.3) is well defined if condition (3.2) is
true.
Theorem 3.1, combined with Lemma 2.1, yields the following corollary.
This result is known (see [11], [12, Ch. IV, § 4c], [13], [21], [28], [29], [30], [39],
[40], [41]).
Corollary 3.1. (i) Either *P = P or *P ⊥P.
(ii) We have *P
loc
≪P if and only if conditions (3.1)–(3.3) and the condition
*ν ≪ν are satisfied.
(iii) We have *P0 ⊥P0 if and only if any of conditions (3.1)–(3.3) is
violated.
4 Separating Times for Bessel Processes
Consider the SDE
dXt = γ dt + 2

|Xt| dBt,
X0 = x0
with γ ≥0, x0 ≥0. It is known that this SDE has a unique solution Q in
the sense of Definition 5. Moreover, the measure Q is concentrated on positive
functions. A process (Zt)t∈[0,∞) with the distribution Q is called a square of
a γ-dimensional Bessel process started at √x0. The process
√
Z is called a
γ-dimensional Bessel process started at √x0. For more information on Bessel
processes, see [2], [3], [6], [32], [33, Ch. XI].
Let X denote the canonical process on C([0, ∞)). Consider the filtration
Ft = =
ε>0 σ(Xs; s ∈[0, t + ε]) and set F = .
t Ft.
Theorem 4.1. Let P (resp., *P) be the distribution of a γ-dimensional (resp.,
*γ-dimensional) Bessel process started at x0. Then the separating time S for
P and *P has the following form.
(i) If P = *P, then S = δ P, *P-a.s.
(ii) If P ̸= *P, then
S = inf{t ∈[0, ∞): Xt = 0} P, *P-a.s.
(we set inf ∅= ∞).
Proof. We should prove only (ii). Set T0 = inf{t ∈[0, ∞): Xt = 0}. It
follows from [2, Th. 4.1] and the strong Markov property of Bessel processes
that S ≤T0 P, *P-a.s.
Let us prove that S ≥T0 P, *P-a.s. For x0 = 0, this is obvious, so we
assume that x0 > 0. Fix ε ∈(0, x0/2) and consider the stopping time
Tε = inf{t ∈[0, ∞) : Xt = ε}. Define the map Fε : C([0, ∞)) →C([0, ∞))

Separating Times
135
by Fε(ω)(t) = ω(t ∧Tε(ω)) and let Pε denote the image of P under this map.
Using Itˆo’s formula, one can check that Pε is a solution of the SDE
dXt = γ −1
2Xt
I(t ≤Tε) dt + I(t ≤Tε) dBt,
X0 = x0.
Let (Ω′, F′, P′) be a probability space with a Brownian motion (Wt)t∈[0,∞).
Consider the space (C([0, ∞)) × Ω′, F × F′, Pε × P′) and let Qε be the distri-
bution of the process
Zt = Xt +
 t
0
I(s > Tε)dWs,
t ∈[0, ∞).
Then Qε is a solution of the SDE
dXt = γ −1
2Xt
I(t ≤Tε) dt + dBt,
X0 = x0.
Similarly, using the measure *P, we define the measure *Qε that is a solution of
the SDE
dXt = *γ −1
2Xt
I(t ≤Tε) dt + dBt,
X0 = x0.
Since the drift coefficients γ−1
2Xt I(t ≤Tε) and *γ−1
2Xt I(t ≤Tε) are bounded, we get
by Girsanov’s theorem that *Qε loc
∼Qε. The obvious equalities Pε = Qε ◦F −1
ε
and *Pε = *Qε ◦F −1
ε
yield that *Pε loc
∼Pε. One can verify that Pε|FT2ε = P|FT2ε
and *Pε|FT2ε = *P|FT2ε. Consequently, *P|Ft∧T2ε ∼P|Ft∧T2ε for any t ∈[0, ∞).
Since t ∈[0, ∞) and ε ∈(0, x0/2) are arbitrary, we get the desired inequality
S ≥T0 P, *P-a.s. The proof is completed.
⊓⊔
It is known that if 0 ≤γ < 2, then a γ-dimensional Bessel process started
at a strictly positive point hits zero with probability one; if γ ≥2, then a γ-
dimensional Bessel process started at a strictly positive point never hits zero
with probability one. Theorem 4.1, combined with Lemma 2.1 and with these
properties, yields
Corollary 4.1. (i) Either *P = P or *P ⊥P.
(ii) If *P ̸= P and x0 = 0, then *P0 ⊥P0.
(iii) Let *P ̸= P and x0 > 0. Then *P
loc
≪P ⇐⇒*γ ≥2.
This corollary generalizes the result of [2, Th. 4.1].
5 Separating Times for Solutions of SDEs
5.1. Basic definitions. We consider one-dimensional SDEs of the form

136
A. Cherny and M. Urusov
dXt = b(Xt) dt + σ(Xt) dBt,
X0 = x0,
(5.1)
where b and σ are Borel functions R →R and x0 ∈R.
The standard definition of a solution, which goes back to I.V. Girsanov [9],
is as follows.
Definition 4. A solution of (5.1) is a pair (Y, B) of continuous adapted
processes on a filtered probability space

Ω, Γ, (Γt)t∈[0,∞), Q

such that
i) B is a (Γt, Q)-Brownian motion;
ii) for any t ∈[0, ∞),
 t
0
(|b(Ys)| + σ2(Ys)) ds < ∞
Q-a.s.;
iii) for any t ∈[0, ∞),
Yt = x0 +
 t
0
b(Ys) ds +
 t
0
σ(Ys) dBs
Q-a.s.
Remark. A solution in the sense of Definition 4 is sometimes called a weak
solution.
In what follows, it will be convenient for us to treat a solution as a solu-
tion of the corresponding martingale problem, i.e. as a measure on the space
C([0, ∞)) of continuous functions. The corresponding definition goes back to
D.W. Stroock and S.R.S. Varadhan [43]. Let X denote the canonical process
on C([0, ∞)). Consider the filtration Ft = =
ε>0 σ(Xs; s ∈[0, t + ε]) and set
F = .
t Ft.
Definition 5. A solution of (5.1) is a probability measure P on F such that
i) P(X0 = x0) = 1;
ii) for any t ∈[0, ∞),
 t
0
(|b(Xs)| + σ2(Xs)) ds < ∞
P-a.s.;
iii) the process
Mt = Xt −
 t
0
b(Xs) ds,
t ∈[0, ∞)
is an (Ft, P)-local martingale with the quadratic variation
⟨M⟩t =
 t
0
σ2(Xs) ds,
t ∈[0, ∞).
The following statement (see, for example, [19, § 5.4.B]) shows the rela-
tionship between Definitions 4 and 5.

Separating Times
137
Proposition 2. (i) Let (Y, B) be a solution of (5.1) in the sense of Defini-
tion 4. Set P = Law(Yt; t ∈[0, ∞)). Then P is a solution of (5.1) in the sense
of Definition 5.
(ii) Let P be a solution of (5.1) in the sense of Definition 5. Then there
exist a filtered probability space

Ω, Γ, (Γt)t∈[0,∞), Q

and a pair of processes
(Y, B) on this space such that (Y, B) is a solution of (5.1) in the sense of
Definition 4 and Law(Yt; t ∈[0, ∞)) = P.
5.2. Exploding solutions. Definitions 4 and 5 do not include exploding
solutions. However, we need to consider them. Let us introduce some nota-
tions.
Let us add a point ∆to the real line and let C∆([0, ∞)) denote the space
of functions f : [0, ∞) →R ∪{∆} with the property: there exists a time
ζ(f) ∈[0, ∞] such that f is continuous on [0, ζ(f)), f = ∆on [ζ(f), ∞)),
and if 0 < ζ(f) < ∞, then limt↑ζ(f) f(t) = ∞or limt↑ζ(f) f(t) = −∞.
The time ζ(f) is called the explosion time of f. Below in this subsec-
tion, X denotes the canonical process on C∆([0, ∞)). Consider the filtration
Ft = =
ε>0 σ(Xs; s ∈[0, t + ε]) and set F = .
t Ft. Let ζ denote the explosion
time of the process X.
The next definition is a generalization of Definition 5 for the case of ex-
ploding solutions.
Definition 6. A solution of (5.1) is a probability measure P on F such that
i) P(X0 = x0) = 1;
ii) for any t ∈[0, ∞) and n ∈N such that n > |x0|,
 t∧τn
0
(|b(Xs)| + σ2(Xs)) ds < ∞
P-a.s.,
where τn = inf{t ∈[0, ∞): |Xt| = n} (we set inf ∅= ∞);
iii) for any n ∈N such that n > |x0|, the process
M n
t = Xt∧τn −
 t∧τn
0
b(Xs) ds,
t ∈[0, ∞)
is an (Ft, P)-local martingale with the quadratic variation
⟨M n⟩t =
 t∧τn
0
σ2(Xs) ds,
t ∈[0, ∞).
Clearly, if P is a solution of (5.1) in the sense of Definition 6 and ζ = ∞
P-a.s., then the restriction of P to C([0, ∞)) is a solution of (5.1) in the sense of
Definition 5. Conversely, if P is a solution of (5.1) in the sense of Definition 5,
then there exists a unique extension of the measure P to C∆([0, ∞)) that is a
solution of (5.1) in the sense of Definition 6.

138
A. Cherny and M. Urusov
Definition 7. A Borel function f : R →[0, ∞) is locally integrable at a point
a ∈[−∞, ∞] if there exists a neighborhood U of a such that

U f(x) dx < ∞.
(A neighborhood of ∞is a ray of the form (x, ∞); a neighborhood of −∞is
a ray of the form (−∞, x).) Notation: f ∈L1
loc(a).
A function f is locally integrable on a set A ⊆[−∞, ∞] if f is locally
integrable at each point of this set. Notation: f ∈L1
loc(A).
Below we shall use the following result (see [7]).
Proposition 3 (Engelbert, Schmidt). Suppose that the coefficients b and
σ of (5.1) satisfy the conditions:
σ(x) ̸= 0 ∀x ∈R,
(5.2)
1 + |b|
σ2
∈L1
loc(R).
(5.3)
Then, for any starting point x0 ∈R, there exists a unique solution of (5.1)
in the sense of Definition 6.
For the information on the qualitative behaviour of the solution of (5.1)
under conditions (5.2) and (5.3), see the Appendix.
5.3. Explicit form of the separating time. Here we use the notations
F, Ft, X, and ζ introduced in Subsection 5.2.
Consider the SDEs
dXt = b(Xt) dt + σ(Xt) dBt,
X0 = x0,
(5.4)
dXt = *b(Xt) dt + *σ(Xt) dBt,
X0 = x0
(5.5)
with the same starting point x0. Let us assume that conditions (5.2), (5.3)
and the similar conditions for *b, *σ are satisfied.
Set
ρ(x) = exp

−
 x
0
2b(y)
σ2(y) dy

,
x ∈R,
(5.6)
s(x) =
 x
0
ρ(y) dy,
x ∈R,
(5.7)
s(∞) = lim
x→∞s(x),
(5.8)
s(−∞) =
lim
x→−∞s(x).
(5.9)
Similarly, we define *ρ, *s, *s(∞), and *s(−∞) through *b and *σ. Let µL denote
the Lebesgue measure on B(R).
We say that a point x ∈R is good if there exists a neighborhood U of x
such that σ2 = *σ2 µL-a.e. on U and (b −*b)2/σ4 ∈L1
loc(x). We say that the
point ∞is good if all the points from [x0, ∞) are good and

Separating Times
139
s(∞) < ∞,
(5.10)
(s(∞) −s)(b −*b)2
ρσ4
∈L1
loc(∞).
(5.11)
We say that the point −∞is good if all the points from (−∞, x0] are good
and
s(−∞) > −∞,
(5.12)
(s −s(−∞))(b −*b)2
ρσ4
∈L1
loc(−∞).
(5.13)
Let A denote the complement to the set of good points in [−∞, ∞]. Clearly,
A is closed in [−∞, ∞]. Let us define
Aε = {x ∈[−∞, ∞]: ρ(x, A) < ε},
where ρ(x, y) = | arctg x −arctg y|, x, y ∈[−∞, ∞] (we set ∅ε = ∅).
The main result of this section is the following theorem. Its proof is given
in Subsection 5.5.
Theorem 5.1. Suppose that b, σ, *b, *σ satisfy conditions (5.2) and (5.3). Let
P and *P denote the solutions of (5.4) and (5.5) in the sense of Definition 6.
Then the separating time S for P and *P has the following form.
(i) If P = *P, then S = δ P, *P-a.s.
(ii) If P ̸= *P, then
S = sup
n inf{t ∈[0, ∞): Xt ∈A1/n} P, *P-a.s.,
where “inf” is the same as “inf”, except that inf ∅= δ.
Remarks. (i) Let us explain the structure of S in case (ii). Denote by α
the “bad point that is closest to x0 from the left side”, i.e.
α =

sup{x : x ∈[−∞, x0] ∩A}
if [−∞, x0] ∩A ̸= ∅,
∆
if [−∞, x0] ∩A = ∅.
(5.14)
Let us consider the “hitting time of α”:
U =















δ
if α = ∆,
δ
if α = −∞and lim
t↑ζ
Xt > −∞,
ζ
if α = −∞and lim
t↑ζ
Xt = −∞,
T α
if α > −∞,

140
A. Cherny and M. Urusov
where T α = inf{t ∈[0, ∞): Xt = α}. Similarly, denote by γ the “bad point
that is closest to x0 from the right side” and denote by V the “hitting time
of γ”. Then S = U ∧V P, *P-a.s. (This follows from Proposition A.1.)
(ii) Suppose that [x0, ∞) ⊆[−∞, ∞] \ A. Combining Theorem 5.1 with
results of Appendix, we get that the pair of conditions (5.10), (5.11) is equiv-
alent to the inequality P({S = δ} ∩(B+ ∪C+)) > 0, where B+ and C+ are
defined in the Appendix. By the definition of a separating time, the latter
condition is equivalent to the inequality *P({S = δ} ∩(B+ ∪C+)) > 0. Apply-
ing once more Theorem 5.1 (to the measures *P and P rather than P and *P)
and results of Appendix, we get that this condition is, in turn, equivalent to
the pair
*s(∞) < ∞,
(5.15)
(*s(∞) −*s)(b −*b)2
*ρ *σ4
∈L1
loc(∞).
(5.16)
Thus, assuming that [x0, ∞) ⊆[−∞, ∞] \ A, we get the equivalence between
(5.10)+(5.11) and (5.15)+(5.16). A similar remark is true for (5.12)+(5.13).
Theorem 5.1, combined with Lemma 2.1 and Propositions A.1–A.3, yields
several corollaries concerning the mutual arrangement of P and *P. In order to
formulate them, let us introduce the conditions:
*s(∞) = ∞,
(5.17)
*s(∞) < ∞and *s(∞) −*s
*ρ *σ2
/∈L1
loc(∞),
(5.18)
*s(∞) < ∞and (*s(∞) −*s)(b −*b)2
*ρ *σ4
∈L1
loc(∞).
(5.19)
Condition (5.17) means that the paths of the canonical process X under the
measure *P do not tend to ∞as t →∞(see Proposition A.2). Condition (5.18)
means that the paths of the canonical process X with a strictly positive *P-
probability tend to ∞as t →∞, but do not explode into ∞, i.e. the ex-
plosion time for them is ∞(see Proposition A.2). Condition (5.19) is the
pair (5.15), (5.16). Similarly, we introduce the conditions at −∞:
*s(−∞) = −∞,
(5.20)
*s(−∞) > −∞and *s −*s(−∞)
*ρ *σ2
/∈L1
loc(−∞),
(5.21)
*s(−∞) > −∞and (*s −*s(−∞))(b −*b)2
*ρ *σ4
∈L1
loc(−∞).
(5.22)
Corollary 5.1. Under the assumptions of Theorem 5.1, we have *P ≪P if
and only if at least one of conditions (a)–(d) below is satisfied:

Separating Times
141
(a) P = *P;
(b) (5.17), (5.22), and (5.23) are satisfied;
(c) (5.19), (5.20), and (5.23) are satisfied;
(d) (5.19), (5.22), and (5.23) are satisfied.
Corollary 5.2. Under the assumptions of Theorem 5.1, we have *P
loc
≪P if
and only if the condition
σ2 = *σ2 µL-a.e. and (b −*b)2
σ4
∈L1
loc(R),
(5.23)
at least one of conditions (5.17)–(5.19), and at least one of conditions (5.20)–
(5.22) are satisfied.
Remark. The result of Corollary 5.2 is closely connected with the result
of Orey [31], where a criterion for the local absolute continuity of regular
continuous strong Markov families is provided.
Corollary 5.3. Under the assumptions of Theorem 5.1, we have *P ⊥P if and
only if *P ̸= P and −∞, ∞∈A.
Corollary 5.4. Under the assumptions of Theorem 5.1, we have *P0 ⊥P0 if
and only if x0 ∈A.
5.4. Examples. In this subsection, we give 9 examples, which show var-
ious types of the mutual arrangement of P and *P from the point of view of
their (local) absolute continuity, and singularity. The proofs are straightfor-
ward applications of Theorem 5.1 (it is convenient to use also Remark (ii)
following Theorem 5.1). One should also take into account the results on the
qualitative behaviour of solutions of SDEs that are described in Appendix.
In particular, these results imply that a solution P of SDE (5.1) satisfying
condition (5.3) with σ ≡1, has the following properties:
•
If b is a constant in the neighborhood of +∞, then P({ζ < ∞, limt↑ζ Xt =
+∞) = 0.
•
If b is a strictly positive constant in the neighborhood of +∞, then
P(limt→∞Xt = +∞) > 0.
•
If moreover b is positive in the neighborhood of −∞, then P(limt→∞Xt =
+∞) = 1.
•
If b(x) = x2 in the neighborhood of +∞, then P(ζ < ∞, limt↑ζ Xt =
+∞) > 0.
•
If moreover b is positive in the neighborhood of −∞, then P(ζ
<
∞, limt→∞Xt = +∞) = 1.
In all the examples below, σ = *σ ≡1, x0 = 0, and we specify only b and *b.
We use the notation *P△P to denote that P and *P are in a general position,
i.e. *P ̸≪P, P ̸≪*P, *P ̸⊥P.

142
A. Cherny and M. Urusov
Example 1. If
b ≡1,
*b(x) = 1 + I(0 < x < 1),
then
*P ̸= P,
*P ∼P.
Example 2. If
b(x) = I(x > 0) −I(x < 0),
*b ≡1,
then
*P ≪P,
P ̸≪*P,
P
loc
≪*P.
Example 3. If
b(x) = I(x > 0) −x2I(x < 0),
*b ≡1,
then
*P ≪P,
P ̸
loc
≪*P.
Example 4. If
b(x) = I(x > 0) −I(x < 0),
*b(x) = I(x > 0) −2I(x < 0),
then
*P△P,
*P
loc
∼P.
Example 5. If
b(x) = I(x > 0) −x2I(x < 0),
*b(x) = I(x > 0) −I(x < 0),
then
*P△P,
*P
loc
≪P,
P ̸
loc
≪*P.
Example 6. If
b ≡1,
*b(x) = 1 + I(−1 < x < 0)
√x + 1
,
then
*P△P,
*P ̸
loc
≪P,
P ̸
loc
≪*P.
Example 7. If
b ≡0,
*b ≡1,
then
*P ⊥P,
*P
loc
∼P.
Example 8. If
b(x) = x2,
*b ≡0,
then
*P ⊥P,
*P
loc
≪P,
P ̸
loc
≪*P.

Separating Times
143
Type of arrangement
Example
*P = P
trivial
*P ̸= P, *P ∼P
Example 1
*P ≪P, P ̸≪*P, P
loc
≪*P
Example 2
*P ≪P, P ̸
loc
≪*P
Example 3
*P△P, *P
loc
∼P
Example 4
*P△P, *P
loc
≪P, P ̸
loc
≪*P
Example 5
*P△P, *P ̸
loc
≪P, P ̸
loc
≪*P
Example 6
P ⊥P, *P
loc
∼P
Example 7
*P ⊥P, *P
loc
≪P, P ̸
loc
≪*P
Example 8
*P ⊥P, *P ̸
loc
≪P, P ̸
loc
≪*P
Example 9
Table 1. Various possible types of the mutual arrange-
ment of P and *P (up to the symmetry between P and *P)
Example 9. If
b ≡0,
*b(x) = I(0 < x < 1)
√x
,
then
*P ⊥P,
*P ̸
loc
≪P,
P ̸
loc
≪*P.
Examples 1–9 show that all the possible types of the mutual arrangement
of P and *P can be realized. However, the lemma below shows that the types of
the mutual arrangement that appear in Examples 3, 5, and 8 can be realized
only if P explodes. (In Examples 1, 2, 4, 6, 7, and 9, the measures P and *P do
not explode.)
Lemma 5.1. Suppose that P does not explode and *P
loc
≪P. Then P
loc
≪*P.
Proof. Let S be the separating time for P and *P. By Lemma 2.1,
*P(S ≥∞) = 1. It follows from Theorem 5.1 and Proposition A.3 (i), that
all the points of (−∞, ∞) are good. As P does not explode, P(S ≥∞) = 1.
One more application of Lemma 2.1 yields P
loc
≪*P.
⊓⊔
Remark. Example 8 reveals an interesting effect. Suppose that we are ob-
serving a path of the process X and are trying to distinguish between the

144
A. Cherny and M. Urusov
hypotheses P and *P (given by Example 8). If P is the true hypothesis, we will
find this out within a finite time of observations. However, if *P is the true
hypothesis, we will find this out only within the infinite time of observations.
5.5. Proof of Theorem 5.1. In the proof of this theorem, we use the
techniques of random time-changes and local times. These can be found in [33,
Ch. V, § 1; Ch. VI, §§ 1,2]. Below we deal with the following two settings.
Setting 1. Let X denote the canonical process on C([0, ∞)). Consider the
filtration Ft = =
ε>0 σ(Xs; s ∈[0, t + ε]) and set F = .
t∈[0,∞) Ft.
Setting 2. Let X denote the canonical process on C∆([0, ∞)) and ζ denote
the explosion time of X. Consider the filtration Ft = =
ε>0 σ(Xs; s ∈[0, t+ε])
and set F = .
t∈[0,∞) Ft.
We begin with a series of auxiliary lemmas.
Lemma 5.2. In Setting 1 or in Setting 2, consider an (Ft)-stopping time τ.
Let ω and ω′ be such that τ(ω) = t0 ∈[0, ∞) and ω′(s) = ω(s) on [0, t0 + ε]
for some ε > 0. Then τ(ω′) = t0 and, for any A ∈Fτ, ω ∈A ⇐⇒ω′ ∈A.
This lemma may be proved by the standard technique. For statements
with similar proofs, see, for example, [12, Ch. III, Lem. 2.43], [33, Ch. I,
Ex. 4.21], [36, Ch. I, § 2, Lem. 13].
Lemma 5.3. Let Y = (Yt)t∈[0,∞) be a continuous process on a probability
space (Ω, G, Q). Introduce the filtration GY
t = =
ε>0 σ(Ys; s ∈[0, t + ε]). Let τ
be a (GY
t )-stopping time. Then there exists an (Ft)-stopping time ρ such that
τ = ρ(Y ), where (Ft) denotes the filtration introduced in Setting 1.
This lemma may be proved similarly to [12, Ch. I, Lem. 1.19].
Lemma 5.4. Assume that the coefficients b and σ of (5.1) satisfy condi-
tions (5.2) and (5.3). Let P be a solution of (5.1) in the sense of Definition 6
(so, we consider Setting 2). Then F0 is P-trivial.
Proof. This is a consequence of the following result (see [43, Th. 6.2] or [18,
Th. 18.11]): if for any starting point x0 ∈R, there exists a unique solution Px0
of (5.1), then the family (Xt, Ft, Px; t ∈[0, ∞), x ∈R) possesses the strong
Markov property. After applying this result one should note that any strong
Markov family satisfies the required zero-one law.
⊓⊔
Lemma 5.5. Assume that the coefficients b and σ of (5.1) satisfy condi-
tions (5.2) and (5.3) and that the solution is non-exploding. Let P be a solution
of (5.1) in the sense of Definition 5 (so, we consider Setting 1). Then, for
any (Ft)-stopping time ξ such that ξ > 0 P-a.s., there exists an (Ft)-stopping
time ξ′ such that 0 < ξ′ < ξ P-a.s.

Separating Times
145
Proof. 1) Define the functions ρ and s by formulas (5.6) and (5.7). Con-
sider the process Y = s(X). Due to the Ito-Tanaka formula (see [33, Ch. VI,
Th. 1.5]), Y is a continuous (Ft, P)-local martingale with the quadratic varia-
tion ⟨Y ⟩t =
 t
0 κ2(Yu) du, where κ(x) = ρ(s−1(x)) σ(s−1(x)), x ∈s(R). Since
σ(x) ̸= 0 for any x ∈R, then P-a.s. the trajectories of ⟨Y ⟩are continuous
and strictly increasing. Denote by F the P-completion of the σ-field F and
by (Ft) the P-completion of the filtration (Ft). Define an (Ft)-time-change
τt = inf{s ∈[0, ∞): ⟨Y ⟩s > t},
t ∈[0, ∞).
(5.24)
Consider an (F′
t, P′)-Brownian motion W ′ on some stochastic basis
(Ω′, F′, (F′
t), P′) and set
Ω= C([0, ∞)) × Ω′,
G = F × F′,
Gt =
?
ε>0
Fτt+ε × F′
t+ε,
Q = P × P′.
Denote by G the Q-completion of the σ-field G and by (Gt) the Q-completion
of the filtration (Gt). Consider the stochastic basis (Ω, G, (Gt), Q). All the
random variables and the processes defined on C([0, ∞)) or on Ω′ can be
viewed as random variables and processes on Ω. In what follows, we do not
explain on which space we consider a random variable or a process if this is
clear from the context.
Set
Wt = Yτt + W ′
t −W ′
t∧⟨Y ⟩∞,
t ∈[0, ∞).
(5.25)
By the Dambis-Dubins-Schwartz theorem (see [33, Ch. V, Th. 1.6]), the
process W = (Wt)t∈[0,∞) is a (Gt, Q)-Brownian motion with the starting
point s(x0).
As P-a.s. the trajectories of ⟨Y ⟩are continuous, we have ⟨Y ⟩τt = t P-a.s.
on {t < ⟨Y ⟩∞}, i.e.
 τt
0
κ2(Yu) du = t
P-a.s. on {t < ⟨Y ⟩∞}.
As P-a.s. the trajectories of ⟨Y ⟩are strictly increasing, then P-a.s. the tra-
jectories of τ are continuous (however, they may explode). By the change of
variables in the Stieltjes integral, we get
 t
0
κ2(Yτu) dτu = t
P-a.s. on {t < ⟨Y ⟩∞},
and therefore,
τt =
 t
0
κ−2(Yτu) du
P-a.s. on {t < ⟨Y ⟩∞}.
Since τt →∞P-a.s. as t ↑⟨Y ⟩∞and Yτt = Wt for t < ⟨Y ⟩∞, we have

146
A. Cherny and M. Urusov
τt =
 t
0
κ−2(Wu) du
Q-a.s.,
t ∈[0, ∞)
(5.26)
(here we set κ(x) = 1 for x /∈s(R)).
Consider the filtration HW
t
= =
ε>0 σ(Ws; s ∈[0, t + ε]) and let (H
W
t )
denote its Q-completion. By (5.26), the process τ viewed as a process on Ωis
(H
W
t )-adapted. Due to (5.24),
⟨Y ⟩t = inf{s ∈[0, ∞): τs > t}
P-a.s.,
t ∈[0, ∞).
Therefore, the process ⟨Y ⟩viewed as a process on Ωis an (H
W
t )-time-change.
Furthermore, (5.25) implies that Yt = W⟨Y ⟩t Q-a.s. Since the right-continuous
and Q-complete filtration generated by Y viewed as a process on Ωcontains
the filtration (Ft × {∅, Ω′}), we have
Ft × {∅, Ω′} ⊆H
W
⟨Y ⟩t.
(5.27)
The process τ is an (Ft × {∅, Ω′})-time-change. It follows from (5.27) (see
also [33, Ch. V, Ex. 1.12]) that
Fτt × {∅, Ω′} ⊆H
W
t∧⟨Y ⟩∞⊆H
W
t .
(5.28)
2) It is easy to verify that ⟨Y ⟩ξ viewed as a random variable on Ωis
an (Fτt × {∅, Ω′})-stopping time. By (5.28), ⟨Y ⟩ξ is an (H
W
t )-stopping time.
Since ξ > 0 P-a.s., then ⟨Y ⟩ξ > 0 Q-a.s. Furthermore, the σ-field H
W
0
is
Q-trivial; it is also well known that every stopping time on a complete Brown-
ian filtration is predictable. Hence, there exists an (H
W
t )-stopping time η such
that
0 < η < ⟨Y ⟩ξ
Q-a.s.
(5.29)
It is known (see [12, Ch. I, Lem. 1.19]) that every stopping time with respect
to a completion of a right-continuous filtration (Kt) a.s. coincides with a (Kt)-
stopping time. Therefore, we can choose η in such a way that it is an (HW
t )-
stopping time. Due to Lemma 5.3, there exists an (Ft)-stopping time ρ such
that
η = ρ(W)
Q-a.s.
(5.30)
Now, define the process Vt = Yτt, t ∈[0, ∞). (Note that {τt = ∞} = {⟨Y ⟩∞≤
t} P-a.s. and on the set {⟨Y ⟩∞< ∞} the process Yt tends P-a.s. to a finite
random variable Y∞. Hence, the process V is well defined.) Equations (5.29)
and (5.30) imply that ρ(W) < ⟨Y ⟩∞Q-a.s. Since V = W ⟨Y ⟩∞Q-a.s., then,
by Lemma 5.2, ρ(W) = ρ(V ) Q-a.s. The random variables ρ(V ) and ⟨Y ⟩ξ are
defined on C([0, ∞)). Hence, we can write
0 < ρ(V ) < ⟨Y ⟩ξ
P-a.s.
(5.31)

Separating Times
147
Consider the filtration FV
t
on C([0, ∞)) defined by the formula
FV
t =
?
ε>0
σ(Vs; s ∈[0, t + ε]).
Since the process V is Fτt-adapted and the filtration Fτt is right-continuous,
we have FV
t
⊆Fτt. Consequently, ρ(V ) is an (Fτt)-stopping time. By [33,
Ch. V, Ex. 1.12], τρ(V ) is an (Ft)-stopping time. Due to [12, Ch. I, Lem. 1.19],
there exists an (Ft)-stopping time ξ′ such that ξ′ = τρ(V ) P-a.s. Finally,
(5.31) implies that 0 < ξ′ < ξ P-a.s.
⊓⊔
Now, let us introduce some notations. Suppose that a, c ∈[−∞, ∞]. In
Setting 1 or in Setting 2, define
Ta = inf{t ∈[0, ∞): Xt = a},
(5.32)
Ta,c = Ta ∧Tc.
(5.33)
Note that if a = −∞or a = ∞, then Ta = ∞. Similarly, for a process Y , we
use the notations
Ta(Y ) = inf{t ∈[0, ∞): Yt = a},
(5.34)
Ta,c(Y ) = Ta(Y ) ∧Tc(Y ).
(5.35)
Below in this section, we use the notations ρ, s, s(∞), s(−∞) introduced
in (5.6)–(5.9). Let us define the function κ by the formula
κ(x) = ρ(s−1(x)) σ(s−1(x)),
x ∈s(R).
(5.36)
We need a more detailed version of the Engelbert-Schmidt theorem than
Proposition 3 (see [7]).
Proposition 4 (Engelbert, Schmidt). Suppose that the coefficients b and
σ of (5.1) satisfy conditions (5.2) and (5.3).
(i) Then, for any starting point x0 ∈R, there exists a unique solution
of (5.1) in the sense of Definition 6.
(ii)
Let
Px0
denote
this
solution.
Consider
a
stochastic
basis
(Ω, G, (Gt)t∈[0,∞), Q) with a right-continuous and complete filtration. Let B
be a (Gt, Q)-Brownian motion with the starting point s(x0). Define the process
(At)t∈[0,∞) and the (Gt)-time-change (τt)t∈[0,∞) by the formulas
At =
 t
0 κ−2(Bs) ds
if t < Ts(−∞),s(∞)(B),
∞
if t ≥Ts(−∞),s(∞)(B),
(5.37)
τt = inf{s ∈[0, ∞): As > t}.
(5.38)
Then
Px0 = Law

s−1(Bτt); t ∈[0, ∞)
Q

,
where we set s−1(s(∞)) = s−1(s(−∞)) = ∆.

148
A. Cherny and M. Urusov
Remark. Propositions A.1 and A.3 may easily be derived from the second
part of Proposition 4.
Lemma 5.6. Assume that the coefficients b and σ of (5.1) satisfy condi-
tions (5.2) and (5.3). Additionally assume that s(∞) < ∞. Denote by P the
solution of (5.1) in the sense of Definition 6 (so, we consider Setting 2). Let
a < x0 and f be a positive Borel function such that f/σ2 ∈L1
loc([a, ∞)).
(i) If (s(∞) −s)f/(ρσ2) ∈L1
loc(∞), then
 ζ
0
f(Xt) dt < ∞
P-a.s. on the set {Ta = ∞}
(recall that ζ denotes the explosion time of X).
(ii) If (s(∞) −s)f/(ρσ2) /∈L1
loc(∞), then
 ζ
0
f(Xt) dt = ∞
P-a.s. on the set {Ta = ∞}.
Remark. Due to Proposition A.1, limt↑ζ Xt = ∞P-a.s. on the set {Ta =
∞}. Therefore, Lemma 5.6 deals, in fact, with the convergence of some inte-
grals on the trajectories that tend to ∞or explode to ∞. Clearly, this lemma
has its analog for the trajectories that tend to −∞or explode to −∞.
Proof of Lemma 5.6. We prove only the first part. The proof of the second
one is analogous.
Consider a stochastic basis (Ω, G, (Gt)t∈[0,∞), Q) with a right-continuous
and complete filtration and let B be a (Gt, Q)-Brownian motion with the
starting point s(x0). Define the process (At)t∈[0,∞) and the (Gt)-time-change
(τt)t∈[0,∞) by formulas (5.37) and (5.38). Set ξ = ATs(−∞),s(∞)(B)−.
Proposition 4 yields that the convergence of the integral
 ζ
0 f(Xt) dt
P-a.s. on the set {Ta = ∞} is equivalent to the convergence of the integral
 ξ
0 f(s−1(Bτt)) dt Q-a.s. on the set {Ts(∞)(B) < Ts(a)(B)}. By the change of
variables in the Stieltjes integral, we get
 ξ
0
f(s−1(Bτt)) dt =
 ξ
0
f(s−1(Bτt)) dAτt =
 τξ
0
f(s−1(Bt)) dAt
=
 Ts(−∞),s(∞)(B)
0
f
ρ2σ2 (s−1(Bt)) dt.
Set
g(x) =
f
ρ2σ2 (s−1(x)),
x ∈s(R).
Since Ts(−∞),s(∞)(B) =
Ts(∞)(B) on the set {Ts(∞)(B)
<
Ts(a)(B)},
then the problem reduces to investigating the convergence of the integral
 Ts(∞)(B)
0
g(Bt) dt Q-a.s. on the set {Ts(∞)(B) < Ts(a)(B)}.

Separating Times
149
Since (s(∞) −s)f/(ρσ2) ∈L1
loc(∞), then
∃ε > 0:
 s(∞)
s(∞)−ε
(s(∞) −x)g(x) dx < ∞.
As f/σ2 ∈L1
loc([a, ∞)), we have g ∈L1
loc([s(a), s(∞))). Now, we need to use
the results of the paper [2], where the convergence of some integrals associated
with Bessel processes is investigated. By [2, Th. 2.2],
 Ts(a)(s(∞)−Y )
0
g(s(∞) −Y ) dt < ∞
R2
+-a.s.,
where Y is a three-dimensional Bessel process started at zero and defined on
a probability space with a measure R2
+. Set Zt = s(∞) −Yt, t ∈[0, ∞). Then
 Us(x0)(Z)
0
g(Zt) dt < ∞
R2
+-a.s. on the set {Us(x0)(Z) < Ts(a)(Z)},
where we use the notation Uc(Z) = sup{t ∈[0, ∞): Zt = c}. Now, the
Williams theorem (see [33, Ch. VII, Cor. 4.6]), combined with the last formula,
yields
 Ts(∞)(B)
0
g(Bt) dt < ∞
Q-a.s. on the set {Ts(∞)(B) < Ts(a)(B)}.
This completes the proof.
⊓⊔
In what follows, µL denotes the Lebesgue measure on B(R).
Lemma 5.7. Assume that the coefficients b and σ of (5.1) satisfy condi-
tions (5.2) and (5.3). Additionally assume that s(−∞) = −∞and s(∞) = ∞.
Denote by P the solution of (5.1) in the sense of Definition 6 (so, we consider
Setting 2). Let f be a positive Borel function such that µL(f > 0) > 0. Then
 ∞
0
f(Xt) dt = ∞
P-a.s.
(Let us recall that, by Propositions A.1 and A.2, ζ = ∞P-a.s. whenever
s(∞) = ∞and s(−∞) = −∞.)
Remark. Lemmas 5.6 and 5.7 complement each other. Indeed, Lemma 5.6
deals with the convergence of some integrals on the trajectories that tend to
∞(or to −∞), while Lemma 5.7 deals with the convergence of some integrals
on the trajectories that are recurrent.
Proof of Lemma 5.7. Using a reasoning similar to that of the previous lemma,
we see that we need to prove the equality
 ∞
0
g(Bt) dt = ∞Q-a.s., where
g(x) =
f
ρ2σ2 (s−1(x)), x ∈R, and B is a Q-Brownian motion defined on some

150
A. Cherny and M. Urusov
probability space. It is known that local times of a Brownian motion satisfy
Lx
∞(B) = ∞for all x ∈R (see [33, Ch. VI, Cor. 2.4]). By the occupation
times formula (see [33, Ch. VI, Cor. 1.6]),
 ∞
0
g(Bt) dt =

R
g(x)Lx
∞(B) dx = ∞
Q-a.s.
The proof is completed.
⊓⊔
Let Y be a continuous semimartingale on some stochastic basis. Below in
this section, we use the notation Lx
t (Y ) (t ∈[0, ∞), x ∈R) for the local time
of a process Y spent at a point a by a time t. We take versions of local times
that are c`adl`ag in x and use the notation Lx−
t
(Y ) := limε↓0 Lx−ε
t
(Y ).
Lemma 5.8. Assume that the coefficients b, σ and *b, *σ of (5.4) and (5.5)
satisfy conditions (5.2) and (5.3) and that the solutions are non-exploding.
Let P and *P be the solutions of (5.4) and (5.5) in the sense of Definition 5
(so, we consider Setting 1). Suppose that the condition
∀ε > 0, µL((x0 −ε, x0 + ε) ∩{σ2 ̸= *σ2}) > 0
(5.39)
or the condition
(*b −b)2
σ4
/∈L1
loc(x0)
(5.40)
is satisfied. Then *P0 ⊥P0 (let us recall that P0 and *P0 denote the restrictions
of P and *P to the σ-field F0).
Proof. 1) Let us first assume that condition (5.39) holds. By the occupation
times formula (see [33, Ch. VI, Cor. 1.6]),
 t
0
I{σ2̸=*σ2}(Xu)σ2(Xu) du =
 t
0
I{σ2̸=*σ2}(Xu) d⟨X⟩u
=

R
I{σ2̸=*σ2}(x)Lx
t (X) dx
P-a.s.
It follows from [4, Th. 2.7] that Lx0
t (X) > 0 and Lx0−
t
(X) > 0 P-a.s. for any
t > 0. Therefore, for any t > 0,
 t
0
I{σ2̸=*σ2}(Xu)σ2(Xu) du > 0
P-a.s.
Hence, for any t > 0,
P

∃0 < s ≤t:
 s
0
σ2(Xu) du ̸=
 s
0
*σ2(Xu) du

= 1,
and consequently,

Separating Times
151
P

∀t > 0 ∃0 < s ≤t:
 s
0
σ2(Xu) du ̸=
 s
0
*σ2(Xu) du

= 1.
(5.41)
Let us recall that P-quadratic variation (resp., *P-quadratic variation) of X
at time s equals
 s
0 σ2(Xu) du P-a.s. (resp.,
 s
0 *σ2(Xu) du *P-a.s.). Therefore,
for any sequence (∆n) of subdivisions of the interval [0, s] whose diameters
tend to 0, we have
 s
0
σ2(Xu) du = P- lim
n→∞

ti∈∆n
(Xti −Xti−1)2
and
 s
0
*σ2(Xu) du = *P- lim
n→∞

ti∈∆n
(Xti −Xti−1)2.
Now, consider all rational times s. By extracting a.s. converging subse-
quences and using Cantor’s diagonal method, we see that (5.41) implies the
desired result *P0 ⊥P0.
2) Assume now that condition (5.40) holds. Denote by S the separating
time for P and *P. Due to Lemma 5.4, the σ-field F0 is trivial with respect to
each of the measures P and *P. Combining this with Lemma 2.1, we obtain
that either S = 0 P, *P-a.s. or S > 0 P, *P-a.s. Let us prove that the second
variant is not possible.
Suppose, on the contrary, that S > 0 P, *P-a.s. (or, equivalently, *P0 ̸⊥P0).
By Lemma 5.5, there exist stopping times τ ′ and τ ′′ such that 0 < τ ′ < S P-a.s.
and 0 < τ ′′ < S *P-a.s. Set τ = τ ′ ∧τ ′′. Then it follows from our assumption
*P0 ̸⊥P0 and from the fact that F0 is both P- and *P-trivial that 0 < τ <
S P, *P-a.s. Hence, *Pτ ∼Pτ.
Consider the c`adl`ag (Ft, P)-martingale
Zt = EP
d*Pτ
dPτ
Ft

,
t ∈[0, ∞).
Notice that Z is a uniformly integrable martingale with a limit Z∞= d*Pτ
dPτ .
Since Z∞> 0 P-a.s., the processes Z and Z−are strictly positive P-a.s.
(see [12, Ch. III, Lem. 3.6]). Set
Lt =
 t
0
1
Zu−
dZu,
t ∈[0, ∞).
The (Ft, P)-local martingale L is well defined. Clearly, we have Z = Z0 E(L)
(i.e. Z is a stochastic exponent of L). Since P is a unique solution of (5.4), any
(Ft, P)-local martingale is a stochastic integral with respect to the local mar-
tingale Y (see [12, Ch. III, Th. 4.29]), where Y is the continuous martingale
part of the (Ft, P)-semimartingale X, i.e.

152
A. Cherny and M. Urusov
Yt = Xt −
 t
0
b(Xu) du,
t ∈[0, ∞).
In particular, there exists a predictable process β such that
 t
0
β2
u d⟨Y ⟩u < ∞
P-a.s.,
t ∈[0, ∞)
and
Lt =
 t
0
βu dYu
P-a.s.,
t ∈[0, ∞).
This yields that the process L is continuous.
Consider the measure Q = Z∞· P. Then Qτ = *Pτ. It follows from Gir-
sanov’s theorem for local martingales (see [12, Ch. III, Th. 3.11]) that the
process Y −⟨Y, L⟩is an (Ft, Q)-local martingale. We have
⟨Y, L⟩t =
 t
0
βu d⟨Y ⟩u =
 t
0
βuσ2(Xu) du
P-a.s.,
t ∈[0, ∞).
For any t ∈[0, ∞), set
Mt =









Xt∧τ −
 t∧τ
0
(b(Xu) + βuσ2(Xu)) du
if
 t∧τ
0
(|b(Xu)|
+|βu|σ2(Xu)) du < ∞,
∞
otherwise.
The process M is finite and continuous with respect to P. Hence, it is finite
and continuous with respect to Q. Since Qτ = *Pτ and Mt is Fτ-measurable
for any t ∈[0, ∞), the process M is finite and continuous also with respect to
the measure *P. Furthermore, as M = (Y −⟨Y, L⟩)τ Q-a.s., M is an (Ft, Q)-
martingale. Consider the stopping times
ηn = inf{t ∈[0, ∞): |Mt| > n},
n ∈N.
Clearly, ηn ↑∞P, *P-a.s. and M ηn is an (Ft, Q)-martingale for any n ∈N.
Since Qτ = *Pτ, then, for any s < t and B ∈Fs, we have
E*P[IB(M ηn
t
−M ηn
s )] = E*P[IB∩{s<τ}(M ηn
t
−M ηn
s )]
= EQ[IB∩{s<τ}(M ηn
t
−M ηn
s )]
= EQ[IB(M ηn
t
−M ηn
s )] = 0.
Hence, M is an (Ft, *P)-local martingale. Consequently, as *P is a solution
of (5.5), the process
Nt =
 t∧τ
0
b(Xu) du +
 t∧τ
0
βuσ2(Xu) du −
 t∧τ
0
*b(Xu) du,
t ∈[0, ∞)

Separating Times
153
is well defined with respect to *P and is a continuous (Ft, *P)-local martingale
of locally bounded variation. This means that N = 0 *P-a.s. Thus, we have
*P

∀t ∈[0, ∞):
 t∧τ
0
(b(Xu) + βuσ2(Xu)) du =
 t∧τ
0
*b(Xu) du

= 1.
As *Pτ ∼Pτ, we get
P

∀t ∈[0, ∞),
 t∧τ
0
(b(Xu) + βuσ2(Xu)) du =
 t∧τ
0
*b(Xu) du

= 1. (5.42)
Now, let us recall that Lx0
t (X) > 0 and Lx0−
t
(X) > 0 P-a.s. for any t > 0
(see [4, Th. 2.7]). Then it follows from the occupation times formula and (5.40)
that, for any t > 0,
 t
0
(*b −b)2
σ2
(Xu) du =
 t
0
(*b −b)2
σ4
(Xu) d⟨X⟩u
=

R
(*b −b)2
σ4
(x)Lx
t (X) dx = ∞
P-a.s.
Thus,
P
	
∀t ∈(0, ∞):
 t
0
(*b −b)2
σ2
(Xu) du = ∞

= 1.
(5.43)
Let us recall that τ > 0 P-a.s. and
 t
0 β2
uσ2(Xu) du < ∞P-a.s., t ∈[0, ∞).
Therefore, conditions (5.42) and (5.43) contradict each other. As a result,
S = 0, which means that *P0 ⊥P0.
⊓⊔
Lemma 5.9. Assume that the coefficients b, σ and *b, *σ satisfy condi-
tions (5.2) and (5.3). Let P and *P be the solutions of (5.4) and (5.5) in
the sense of Definition 6 (so, we consider Setting 2). Let a and c be real num-
bers such that −∞< a < x0 < c < ∞and [a, c] ⊆[−∞, ∞] \ A (recall that A
denotes the complement to the set of good points). Then *PTa,c ∼PTa,c and
d*PTa,c
dPTa,c
= exp
 Ta,c
0
*b −b
σ2 (Xu) dYu −1
2
 Ta,c
0
(*b −b)2
σ2
(Xu) du

,
(5.44)
where the integrals are taken with respect to the measure P and Y is a contin-
uous (Ft, P)-local martingale defined by the formula
Yt = Xt∧Ta,c −
 t∧Ta,c
0
b(Xu) du,
t ∈[0, ∞).
Remark. Since P is a solution of (5.4), then Y is an (Ft, P)-local martingale
with the quadratic variation

154
A. Cherny and M. Urusov
⟨Y ⟩t =
 t∧Ta,c
0
σ2(Xu) du,
t ∈[0, ∞).
Hence,
 Ta,c
0
(*b −b)2
σ2
(Xu) du =
 Ta,c
0
(*b −b)2
σ4
(Xu) d⟨Y ⟩u
P-a.s.
(5.45)
Let us show that this integral is finite P-a.s. By the occupation times formula
(see [33, Ch. VI, Cor. 1.6]),
 Ta,c
0
(*b −b)2
σ4
(Xu) d⟨Y ⟩u =
 Ta,c
0
(*b −b)2
σ4
(XTa,c
u
) d⟨XTa,c⟩u
=

R
(*b −b)2
σ4
(x)Lx
Ta,c(XTa,c) dx
P-a.s.
(We consider the local time of the process XTa,c rather than of X because X
may explode.) Since [a, c] ⊆[−∞, ∞] \ A, then (*b −b)2/σ4 ∈L1
loc([a, c]). As
P-a.s. the process (Lx
Ta,c(XTa,c))x∈R is equal to zero outside [a, c], we have
 Ta,c
0
(*b −b)2
σ4
(Xu) d⟨Y ⟩u < ∞
P-a.s.
(5.46)
Proof of Lemma 5.9. 1) Since A is a closed subset of [−∞, ∞], there exist a′
and c′ such that −∞< a′ < a, c < c′ < ∞, and [a′, c′] ⊆[−∞, ∞] \ A. Let us
define a continuous (Ft, P)-local martingale Y ′ by the formula
Y ′
t = Xt∧Ta′,c′ −
 t∧Ta′,c′
0
b(Xu) du,
t ∈[0, ∞).
Note that
 Ta′,c′
0
(*b −b)2
σ2
(Xu) du < ∞
P, *P-a.s.
(5.47)
(This follows from the analogs of (5.45) and (5.46) for the process Y ′ instead
of Y .) Fix an arbitrary n ∈N, n > 1. Consider the stopping time
τ = inf

t ∈[0, ∞):
 t
0
(*b −b)2
σ2
(Xu) du ≥n

(5.48)
(we set (*b−b)2
σ2
(∆) = 0). Consider a continuous (Ft, P)-local martingale
Lt =
 t∧Ta′,c′∧τ
0
*b −b
σ2 (Xu) dY ′
u,
t ∈[0, ∞)
(5.49)
(L is well defined due to (5.47)). We have

Separating Times
155
EP exp
1
2⟨L⟩∞

= EP exp
1
2
 Ta′,c′∧τ
0
(*b −b)2
σ2
(Xu) du

≤En/2 < ∞.
By Novikov’s criterion, the process Z = E(L) (i.e. Z is the stochastic exponent
of L) is a uniformly integrable (Ft, P)-martingale. Due to Girsanov’s theorem
for local martingales (see [12, Ch. III, Th. 3.11]), the process Y ′ −⟨Y ′, L⟩
is a continuous (Ft, Q)-local martingale, where the probability measure Q is
defined by the formula Q = Z∞· P. Note that for any t ∈[0, ∞),
Y ′
t −⟨Y ′, L⟩t
= Xt∧Ta′,c′ −
 t∧Ta′,c′
0
b(Xu) du −
 t∧Ta′,c′∧τ
0
(*b −b)(Xu) du
Q-a.s.
Consider the process
Mt = Xt∧Ta′,c′∧τ −
 t∧Ta′,c′∧τ
0
*b(Xu) du,
t ∈[0, ∞).
(5.50)
It is well defined with respect to Q and M = (Y ′ −⟨Y ′, L⟩)τ Q-a.s. Therefore,
M is a continuous (Ft, Q)-local martingale with the quadratic variation
⟨M⟩t =
 t∧Ta′,c′∧τ
0
σ2(Xu) du,
t ∈[0, ∞).
Using the occupation times formula and the fact that σ2 = *σ2 µL-a.e. on
[a′, c′], we get
⟨M⟩t =
 t∧Ta′,c′∧τ
0
*σ2(Xu) du,
t ∈[0, ∞).
(5.51)
2) Let us define the functions *ρ, *s, and *κ through *b and *σ similarly to (5.6),
(5.7), and (5.36). Consider the process N = *s(XTa′,c′∧τ). By the Ito-Tanaka
formula (see [33, Ch. VI, Th. 1.5]) applied under the measure Q,
Nt = *s(x0) +
 t
0
*ρ

X
Ta′,c′∧τ
u

dMu,
t ∈[0, ∞).
Hence, N is a continuous (Ft, Q)-local martingale with the quadratic variation
⟨N⟩t =
 t∧Ta′,c′∧τ
0
*κ2(Nu) du,
t ∈[0, ∞).
Since *σ(x) ̸= 0 for any x ∈R, we have that Q-a.s. the trajectories of ⟨N⟩are
continuous and strictly increasing up to the time Ta′,c′ ∧τ and they are con-
stant after Ta′,c′ ∧τ. Let F denote the Q-completion of the σ-field F and (Ft)
denote the Q-completion of the filtration (Ft). Define an (Ft)-time-change by
the formula

156
A. Cherny and M. Urusov
ξt = inf{s ∈[0, ∞): ⟨N⟩s > t},
t ∈[0, ∞).
Consider
an
(F′
t, P′)-Brownian
motion
W ′
on
a
stochastic
basis
(Ω′, F′, (F′
t), P′) and set
Ω= C∆([0, ∞))×Ω′,
G = F ×F′,
Gt =
?
ε>0
Fξt+ε ×F′
t+ε,
R2
+ = Q×P′.
Denote by G the R2
+-completion of the σ-field G and by (Gt) the R2
+-
completion of the filtration (Gt). Consider the stochastic basis (Ω, G, (Gt), R2
+).
All the random variables and the processes defined on C∆([0, ∞)) or on Ω′
can be viewed as random variables and processes on Ω. In what follows, we
do not explain on which space we consider a random variable or a process if
this is clear from the context.
Set
Wt = Nξt + W ′
t −W ′
t∧⟨N⟩∞,
t ∈[0, ∞).
By the Dambis-Dubins-Schwartz theorem (see [33, Ch. V, Th. 1.6]), the
process W = (Wt)t∈[0,∞) is a (Gt, R2
+)-Brownian motion with the starting
point *s(x0).
As Q-a.s. the trajectories of ⟨N⟩are continuous, we have
⟨N⟩ξt = t
Q-a.s. on the set {t < ⟨N⟩∞},
i.e.
 ξt
0
*κ2(Nu) du = t
Q-a.s. on the set {t < ⟨N⟩∞}.
As Q-a.s. the trajectories of ⟨N⟩are strictly increasing up to the time
Ta′,c′ ∧τ, we have that Q-a.s. the trajectories of ξ are continuous up to the
time ⟨N⟩∞. By the change of variables in the Stieltjes integral, we get
 t
0
*κ2(Nξu) dξu = t
Q-a.s. on the set {t < ⟨N⟩∞},
and hence,
ξt =
 t
0
*κ−2(Nξu) du
Q-a.s. on the set {t < ⟨N⟩∞}.
Clearly, ξt = ∞whenever t ≥⟨N⟩∞. Therefore, R2
+-a.s. for any t ∈[0, ∞),
ξt =
 t
0 *κ−2(Wu) du
if t < ⟨N⟩∞,
∞
if t ≥⟨N⟩∞.
Using the occupation times formula, it is easy to verify that P-a.s. we have
∀t < ⟨N⟩∞,
 ξt
0
(*b −b)2
σ2
(Xu) du =
 ξt
0
(*b −b)2
*σ2
(Xu) du.

Separating Times
157
By the change of variables in the Stieltjes integral, R2
+-a.s. we get
∀t < ⟨N⟩∞,
 ξt
0
(*b −b)2
*σ2
(Xu) du =
 ξt
0
(*b −b)2
*σ2
(*s −1(Nu)) du
=
 t
0
(*b −b)2
*σ2
(*s −1(Nξu)) dξu
=
 t
0
(*b −b)2
*ρ 2*σ4 (*s −1(Wu)) du.
(5.52)
Letting t ↑⟨N⟩∞in (5.52), we get
 Ta′,c′∧τ
0
(*b −b)2
σ2
(Xu) du =
 ⟨N⟩∞
0
(*b −b)2
*ρ 2*σ4 (*s −1(Wu)) du
R2
+-a.s. (5.53)
Set
η(W) = inf

t ∈[0, ∞):
 t
0
(*b −b)2
*ρ 2*σ4 (*s −1(Wu)) du ≥n

(we set (*b−b)2
*ρ 2*σ4 (*s −1(x)) = 0 if x /∈*s(R)), where n is the number that appears
in (5.48). Let us now prove the equality
⟨N⟩∞= T*s(a′),*s(c′)(W) ∧η(W)
R2
+-a.s.
(5.54)
For this, note that
 Ta′,c′∧τ
0
(*b −b)2
σ2
(Xu) du = n
P-a.s. on the set {τ < Ta′,c′}.
(5.55)
Indeed, condition (5.55) may be violated only if the integral is less than n
and the process
 t
0
(*b−b)2
σ2
(Xu) du

t∈[0,∞) jumps to infinity at time τ. But
P-a.s. this cannot happen on the set {τ < Ta′,c′} since (5.47) holds. More-
over, as ξ⟨N⟩∞−= Ta′,c′ ∧τ, we have ⟨N⟩∞≥T*s(a′),*s(c′)(W) R2
+-a.s. on the
set {Ta′,c′ ≤τ}. By (5.53) and (5.55), ⟨N⟩∞≥η(W) R2
+-a.s. on the set
{τ < Ta′,c′}. Thus, ⟨N⟩∞≥T*s(a′),*s(c′)(W) ∧η(W) R2
+-a.s. Finally, the re-
verse inequality easily follows from (5.52). So, statement (5.54) is proved.
It follows from the reasoning above that R2
+-a.s. for any t ∈[0, ∞),
ξt =





 t
0
*κ−2(Wu) du
if t < T*s(a′),*s(c′)(W) ∧η(W),
∞
if t ≥T*s(a′),*s(c′)(W) ∧η(W).
Let us recall that
⟨N⟩t = inf{s ∈[0, ∞): ξs > t}
Q-a.s.,
t ∈[0, ∞),
Nt = W⟨N⟩t
R2
+-a.s.,
t ∈[0, ∞),
XTa′,c′∧τ = *s −1(N).

158
A. Cherny and M. Urusov
So, we obtain an explicit construction of the measure Law

XTa′,c′∧τQ

through the Wiener measure. Furthermore, as *P is a solution of (5.5), the
process M introduced in (5.50) is a continuous (Ft, *P)-local martingale with
the same quadratic variation as in formula (5.51). Therefore, repeating the
reasoning of part 2) with the measure *P instead of Q, we obtain that the
measure Law

XTa′,c′∧τ*P

can be constructed from the Wiener measure in
the same way as Law

XTa′,c′∧τQ

. Thus,
Law

XTa′,c′∧τ*P

= Law

XTa′,c′∧τQ

.
(5.56)
3) Consider the stopping time
ρ = inf

t ∈[0, ∞):
 t
0
(*b −b)2
σ2
(Xu) du ≥n −1

,
where n appears in (5.48). Using (5.55) and the analogous condition for the
measure *P, we get Ta,c ∧ρ < Ta′,c′ ∧τ P, *P-a.s. Applying Lemma 5.2, we
obtain that P, *P-a.s. for any event B ∈FTa,c∧ρ,
X ∈B ⇐⇒XTa′,c′∧τ ∈B.
Then, due to (5.56), for any B ∈FTa,c∧ρ, we have
*P(B) = *P(X∈B) = *P(XTa′,c′∧τ ∈B)
= Q(XTa′,c′∧τ ∈B) = Q(X∈B) = Q(B).
Consequently, the measures Q and *P coincide on the σ-field FTa,c∧ρ. Let us
now recall that Q = Z∞·P, where the uniformly integrable (Ft, P)-martingale
Z is defined by the formula Z = E(L) and L is defined in (5.49). Hence,
*PTa,c∧ρ ∼PTa,c∧ρ and
d*PTa,c∧ρ
dPTa,c∧ρ
= EP(Z∞|FTa,c∧ρ) = ZTa,c∧ρ.
(5.57)
4) Now, let us use the notation
τn = inf

t ∈[0, ∞):
 t
0
(*b −b)2
σ2
(Xu) du ≥n

,
n ∈N.
(We fixed some n ∈N above and considered stopping times τn and τn−1,
which were denoted by τ and ρ for the simplicity of notation. Below we need
to use all τn. That is why we now change the notation.) By (5.57),

Separating Times
159
d*PTa,c∧τn
dPTa,c∧τn
= exp
 Ta,c∧τn
0
*b −b
σ2 (Xu)dY ′
u −1
2
 Ta,c∧τn
0
(*b −b)2
σ2
(Xu)du

.
(5.58)
It follows from (5.47) that
lim
n→∞τn ≥Ta′,c′ > Ta,c
P, *P-a.s.
(5.59)
As a consequence, we get
FTa,c =
∞
@
n=1
FTa,c∧τn
(5.60)
up to events of P, *P-zero measure. (Indeed, the inclusion FTa,c ⊆.∞
n=1 FTa,c∧τn
follows from the formula
B =
∞
A
n=1
(B ∩{Ta,c = Ta,c ∧τn})
P, *P-a.s.,
and the reverse inclusion is obvious.) Formulas (5.58), (5.59), and (5.60) imply
that
d*PTa,c
dPTa,c
= exp
 Ta,c
0
*b −b
σ2 (Xu) dY ′
u −1
2
 Ta,c
0
(*b −b)2
σ2
(Xu) du

,
(5.61)
where by
d*PTa,c
dPTa,c we denote the density of the absolutely continuous part of
the measure *PTa,c with respect to the measure PTa,c. Since
d*PTa,c
dPTa,c > 0 P-a.s.,
we get PTa,c ≪*PTa,c. Due to the symmetry between P and *P, *PTa,c ≪PTa,c.
Thus, *PTa,c ∼PTa,c and the density of *PTa,c with respect to PTa,c is given
by formula (5.61). Finally, it is clear that the process Y ′ in (5.61) may be
replaced by Y .
⊓⊔
Before passing on to the proof of Theorem 5.1, we need one more technical
lemma.
Lemma 5.10. In Setting 2, consider a ∈R and a sequence (cn) such that
c1 > a, cn+1 > cn, and cn ↑∞. Then FTa = .∞
n=1 FTa,cn.
Proof. Consider the collection D of sets B ∈F such that
B ∩{Ta = ∞, lim
t↑ζ Xt = ∞} ∈
∞
@
n=1
FTa,cn.

160
A. Cherny and M. Urusov
Notice that
{Ta = ∞, lim
t↑ζ Xt = ∞} =
∞
?
n=1
{XTa,cn I(Ta,cn < ∞) = cn} ∈
∞
@
n=1
FTa,cn.
(5.62)
Now, one can easily check that D is a σ-field. Since for any t ∈[0, ∞) and
d ∈R,
{Xt < d} ∩{Ta = ∞, lim
t↑ζ Xt = ∞}
=
B
∞
A
n=1

{Ta,cn > t} ∩{Xt∧Ta,cn < d}

C
∩{Ta = ∞, lim
t↑ζ Xt = ∞},
then by applying (5.62), we obtain D = σ(Xt; t ∈[0, ∞)) = F.
Now, the inclusion FTa ⊆.∞
n=1 FTa,cn follows from the formula
B =
B
∞
A
n=1

B ∩{Ta = Ta,cn}

C
∪

B ∩{Ta = ∞, lim
t↑ζ Xt = ∞}

,
and the reverse inclusion is obvious.
⊓⊔
Proof of Theorem 5.1. We should prove only (ii). Therefore, below we assume
that P ̸= *P. Set
τ = sup
n inf{t ∈[0, ∞): Xt ∈A1/n}.
Let us prove that the separating time S equals τ. Denote by α the “bad point
that is closest to x0 from the left side” (see (5.14)). Similarly, denote by γ the
“bad point that is closest to x0 from the right side”. It is convenient for us to
set
α′ =

−∞
if α = ∆,
α
if α ̸= ∆
and
γ′ =

∞
if γ = ∆,
γ
if γ ̸= ∆.
If x0 /∈A (or, equivalently, α′ < x0 < γ′), then we consider sequences (an)
and (cn) such that a1 < x0 < c1, an+1 < an, an ↓α′, cn+1 > cn, and cn ↑γ′.
The proof consists of two parts.
I. Let us first prove that S ≥τ P, *P-a.s. If x0 ∈A, then τ = 0 and this
inequality is obvious. Therefore, we consider the case x0 /∈A. By Lemma 5.9,
*PTan,cn ∼PTan,cn for any n ∈N, and hence, S > Tan,cn P, *P-a.s.
Suppose that α ̸= ∆and γ ̸= ∆. Clearly, in this case Tan,cn ↑τ P, *P-a.s..
Thus, we obtain the desired inequality S ≥τ P, *P-a.s.
Suppose now that α = ∆or γ = ∆. In this case Tan,cn ↑τ ∧ζ P, *P-a.s.,
and hence,

Separating Times
161
S ≥τ ∧ζ
P, *P-a.s.
(5.63)
It is easy to establish that
{τ > ζ} = B−∞∪B∞
P, *P-a.s.,
(5.64)
where
B−∞=

{limt↑ζ Xt = −∞} ∩{∀t < ζ : Xt < γ′}
if α = ∆,
∅
if α ̸= ∆,
B∞=

{limt↑ζ Xt = ∞} ∩{∀t < ζ : Xt > α′}
if γ = ∆,
∅
if γ ̸= ∆.
Let us prove that *P ∼P on the set B∞. If γ ̸= ∆, then this is obvious.
Therefore, we consider the case γ = ∆. Fix a ∈(α′, x0) and define continuous
(Ft, P)-local martingales Y n, Ln, and Zn by the formulas
Y n
t = Xt∧Ta,cn −
 t∧Ta,cn
0
b(Xu) du,
t ∈[0, ∞),
Ln
t =
 t∧Ta,cn
0
*b −b
σ2 (Xu) dY n
u ,
t ∈[0, ∞),
Zn
t = exp

Ln
t −1
2⟨Ln⟩t

,
t ∈[0, ∞).
Note that the process Ln is well defined with respect to the measure P (see the
Remark following Lemma 5.9). Clearly, Zn = E(Ln) (i.e. Zn is the stochastic
exponent of Ln). Set T = Ta ∧ζ. Since Ta,cn ↑T P-a.s. and
Ln+1
t
= Ln
t
P-a.s. on the set {t < Ta,cn},
Zn+1
t
= Zn
t
P-a.s. on the set {t < Ta,cn},
we can define continuous (Ft, P)-local martingales L and Z on the stochastic
interval [0, T) (for the definition of a process on a stochastic interval, see [33,
Ch. IV, Ex. 1.48]) such that
Lt = Ln
t
P-a.s. on the set {t < Ta,cn},
Zt = Zn
t
P-a.s. on the set {t < Ta,cn}.
Notice that
Zt = exp

Lt −1
2⟨L⟩t

,
t ∈[0, T)
and
⟨L⟩t =
 t
0
(*b −b)2
σ2
(Xu) du,
t ∈[0, T).

162
A. Cherny and M. Urusov
Since Z is positive, it converges P-a.s. as t ↑T to a finite random variable
ZT (this follows from the Dambis-Dubins-Schwartz theorem for continuous
local martingales on a stochastic interval; see [33, Ch. V, Ex. 1.18]). Hence,
ZTa,cn →ZT P-a.s. Furthermore, due to Lemma 5.9, ZTa,cn =
d*PTa,cn
dPTa,cn , and
due to Lemma 5.10, FTa = .∞
n=1 FTa,cn. By the Jessen theorem (see [42,
Th. 5.2.26]), ZT is the density of the absolutely continuous part of the measure
*PTa with respect to the measure PTa.
Applying Lemma 5.6 to the function f = (*b −b)2/σ2, we get ⟨L⟩T < ∞
P-a.s. on the set {Ta = ∞} (recall that we consider the case γ = ∆, i.e.
∞is a good point). Clearly, ⟨L⟩T < ∞P-a.s. on the set {Ta < ∞}. Hence,
⟨L⟩T < ∞P-a.s. It follows now from the Dambis-Dubins-Schwartz theorem
for continuous local martingales on a stochastic interval that ZT > 0 P-a.s.
Consequently, PTa ≪*PTa.
Since ∞is a good point, s(∞) < ∞. By Proposition A.3, P(Ta = ∞) > 0.
As PTa ≪*PTa, we get *P(Ta = ∞) > 0. Hence, *s(∞) < ∞. Now, let us prove
that the condition
(*s(∞) −*s )(b −*b)2
*ρ *σ4
∈L1
loc(∞).
(5.65)
holds. For this, apply the above reasoning to P instead of *P. Define continuous
(Ft, *P)-local martingales *L and *Z on the stochastic interval [0, T) similarly to
the processes L and Z. Then *ZT is the density of the absolutely continuous
part of the measure PTa with respect to the measure *PTa. If condition (5.65)
does not hold, then, by Lemma 5.6, ⟨*L⟩T = ∞*P-a.s. on the set {Ta = ∞}.
Due to the Dambis-Dubins-Schwartz theorem for continuous local martingales
on a stochastic interval, we have lim t↑T *Lt = −∞*P-a.s. on the set {Ta = ∞}.
Hence, *P-a.s. on the set {Ta = ∞} we get
*ZT = lim
t↑T
*Zt = exp

lim
t↑T
*Lt −1
2⟨*L⟩T

= 0.
As a consequence, *PTa ⊥PTa on the set {Ta = ∞}, which contradicts the
conditions PTa ≪*PTa and P(Ta = ∞) > 0. Hence, condition (5.65) holds.
Since *s(∞) < ∞and condition (5.65) holds, we can repeat the above
reasoning using the processes *L and *Z instead of L and Z. As a result, we get
*ZT > 0 *P-a.s., and therefore, *PTa ≪PTa.
Thus, *PTa ∼PTa. Hence, *P ∼P on the set {Ta = ∞}. Since a ∈(α′, x0) is
arbitrary, and in view of the fact that the sets {Ta = ∞} tend to B∞P, *P-a.s.
as a ↓α′, we get that *P ∼P on the set B∞. Similarly, *P ∼P on the set
B−∞. Consequently, S = δ P, *P-a.s. on the set B−∞∪B∞. Combining this
with (5.63) and (5.64), we obtain the desired inequality S ≥τ P, *P-a.s.
II. Let us now prove that S ≤τ P, *P-a.s. Consider several cases.
1) Suppose that x0 ∈A. Set

Separating Times
163
b′(x) = b(x)I[x0−2,x0+2](x),
x ∈R,
b′′(x) = *b(x)I[x0−2,x0+2](x),
x ∈R,
σ′(x) = σ(x),
x ∈R,
σ′′(x) = *σ(x),
x ∈R
and consider the SDEs
dXt = b′(Xt) dt + σ′(Xt) dBt,
X0 = x0,
(5.66)
dXt = b′′(Xt) dt + σ′′(Xt) dBt,
X0 = x0.
(5.67)
The coefficients b′, σ′ and b′′, σ′′ satisfy conditions (5.2) and (5.3). Let P′
and P′′ denote the solutions of (5.66) and (5.67) in the sense of Definition 6.
By [4, Th. 2.11], PTx0−1,x0+1 = P′
Tx0−1,x0+1 and *PTx0−1,x0+1 = P′′
Tx0−1,x0+1. It
follows from Propositions A.1 and A.2 that P′ and P′′ do not explode. Due to
Lemma 5.8, P′
0 ⊥P′′
0. Therefore, *P0 ⊥P0, and hence S = 0 P, *P-a.s.
2) Suppose that −∞< α < x0 < γ < ∞. Then τ = Tα,γ P, *P-a.s. Since
Tα,γ < ∞P, *P-a.s., then, using the strong Markov property of solutions of
SDEs (see [43, Th. 6.2] or [18, Th. 18.11]) and the result of 1), we obtain that
*PTα,γ ⊥PTα,γ. Hence, S ≤Tα,γ = τ P, *P-a.s.
3) Suppose that −∞< α < x0, γ = ∞. Then τ = Tα ∧ζ P, *P-a.s.
Therefore, we need to prove that
S ≤Tα
P, *P-a.s. on the set {Tα < ∞}
(5.68)
and
S ≤ζ
P, *P-a.s. on the set {Tα = ∞}.
(5.69)
Condition (5.68) holds due to the strong Markov property of solutions
of SDEs. Prior to proving (5.69), let us notice that Fζ
= F. Hence,
FTα∧ζ = FTα ∩Fζ = FTα.
If s(∞) = ∞, then P(Tα = ∞) = 0. Therefore, *PTα∧ζ ⊥PTα∧ζ on the set
{Tα = ∞}. Consequently, S ≤Tα ∧ζ P, *P-a.s. on the set {Tα = ∞} and it
follows that (5.69) holds.
Finally, let us prove (5.69) in the case, where s(∞) < ∞. For this, fix
a ∈(α, x0), set T = Ta ∧ζ, and consider the continuous (Ft, P)-local mar-
tingales L and Z on the stochastic interval [0, T) introduced in part I of the
proof. By Lemma 5.6, ⟨L⟩T = ∞P-a.s. on the set {Ta = ∞} (recall that here
∞is a bad point). Due to the Dambis-Dubins-Schwartz theorem for continu-
ous local martingales on a stochastic interval, we have lim t↑T Lt = −∞P-a.s.
on the set {Ta = ∞}. Hence, P-a.s. on the set {Ta = ∞} we get
ZT = lim
t↑T
Zt = exp

lim
t↑T
Lt −1
2⟨L⟩T

= 0.

164
A. Cherny and M. Urusov
Since ZT is the density of the absolutely continuous part of the measure
*PTa with respect to the measure PTa, we have *PTa ⊥PTa on the set {Ta =
∞}. As FTa∧ζ = FTa, we get *PTa∧ζ ⊥PTa∧ζ on the set {Ta = ∞}. Hence,
S ≤Ta ∧ζ P, *P-a.s. on the set {Ta = ∞}. Since a ∈(α, x0) is arbitrary,
condition (5.69) is satisfied.
In a similar way, we consider the case, where α = −∞, x0 < γ < ∞.
4) Suppose that −∞< α < x0, γ = ∆. Then τ = inf{t ∈[0, ∞): Xt = α}
P, *P-a.s. Therefore, we need to prove only condition (5.68), and this follows
from the strong Markov property of solutions of SDEs.
In a similar way, we consider the case, where α = ∆, x0 < γ < ∞.
5) Suppose that α = −∞, γ = ∞. Then τ = ζ P, *P-a.s. Let us first assume
that s(−∞) > −∞or s(∞) < ∞. It follows from Propositions A.2 and A.3
that in this case
P({limt↑ζ Xt = ∞} ∪{limt↑ζ Xt = −∞}) = 1.
(5.70)
Similarly to the proof of (5.69), we establish that S ≤ζ P, *P-a.s. on the set
{limt↑ζ Xt = ∞} and S ≤ζ P, *P-a.s. on the set {limt↑ζ Xt = −∞}. Hence,
by (5.70), *P ⊥P. Since Fζ = F, we have *Pζ ⊥Pζ. Thus, S ≤ζ = τ P, *P-a.s.
Let us now assume that s(−∞) = −∞and s(∞) = ∞. Then the measure
P does not explode. Consider the continuous (Ft, P)-local martingale
Yt = Xt −
 t
0
b(Xu) du,
t ∈[0, ∞).
By the occupation times formula (see [33, Ch. VI, Cor. 1.6]),
 t
0
(*b −b)2
σ4
(Xu) d⟨Y ⟩u =
 t
0
(*b −b)2
σ4
(Xu) d⟨X⟩u
=

R
(*b −b)2
σ4
(x)Lx
t (X) dx < ∞
P-a.s.,
since P-a.s. the process (Lx
t (X))x∈R is equal to zero outside a finite interval
(let us recall that in the case under consideration, (*b −b)2/σ4 ∈L1
loc(R)).
Hence, the continuous (Ft, P)-local martingales
Lt =
 t
0
*b −b
σ2 (Xu) dYu,
t ∈[0, ∞)
and
Zt = exp

Lt −1
2⟨L⟩t

,
t ∈[0, ∞)
are well defined with respect to the measure P (note that Z = E(L)). Since
Z is a positive (Ft, P)-local martingale, it converges P-a.s. as t →∞to a

Separating Times
165
finite random variable Z∞. Consider sequences (an) and (cn) such that a1 <
x0 < c1, an+1 < an, an ↓−∞, cn+1 > cn, and cn ↑∞. Then ZTan,cn →
Z∞P-a.s. By Lemma 5.9, ZTan,cn =
d*PTan,cn
dPTan,cn . By the Jessen theorem (see [42,
Th. 5.2.26]), Z∞is the density of the absolutely continuous part of the measure
*Q with respect to the measure Q, where Q and *Q are the restrictions of P and
*P to the σ-field .∞
n=1 FTan,cn .
Due to Lemma 5.7,
⟨L⟩∞=
 ∞
0
(*b −b)2
σ2
(Xu) du = ∞
P-a.s.
Consequently,
Z∞= lim
t→∞Zt = exp

lim
t→∞Lt −1
2⟨L⟩∞

= 0
P-a.s.
Hence, *Q ⊥Q, i.e. *P ⊥P. Since Fζ = F, we have *Pζ ⊥Pζ. Thus, S ≤ζ = τ
P, *P-a.s.
6) Suppose that α = ∆, γ = ∞. Consider the sets
D =
1
ζ = ∞, lim
t→∞Xt = ∞, lim
t→∞Xt = −∞
2
,
D+ =
1
lim
t↑ζ Xt = ∞
2
,
D−=
1
lim
t↑ζ Xt = −∞
2
.
By Proposition A.1,
P(D ∪D+ ∪D−) = *P(D ∪D+ ∪D−) = 1.
In the case under consideration, τ = δ on D−τ = ∞on the set D, τ = ζ on
the set D+. Since s(−∞) > −∞(−∞is a good point), we have P(D) = 0.
Consequently, *P ⊥P on the set D, and therefore, S ≤∞P, *P-a.s. on the
set D. Similarly to the proof of (5.69), we establish that S ≤ζ P, *P-a.s on the
set D+. Thus, S ≤τ P, *P-a.s.
In a similar way, we consider the case, where α = −∞, γ = ∆.
7) Finally, suppose that α = γ = ∆. In this case τ = δ and the desired
inequality S ≤τ is obvious. The proof is completed.
⊓⊔
Appendix
Here we describe the behaviour of solutions of SDEs. We use the notations F,
Ft, X, and ζ introduced in Subsection 5.2.
Let us consider SDE (5.1) and assume that conditions (5.2) and (5.3) are
satisfied. According to Proposition 3, this equation has a unique solution P in
the sense of Definition 6. Consider the sets

166
A. Cherny and M. Urusov
D =
1
ζ = ∞, lim
t→∞Xt = ∞, lim
t→∞Xt = −∞
2
,
B+ =
1
ζ = ∞, lim
t→∞Xt = ∞
2
,
C+ =
1
ζ < ∞, lim
t↑ζ Xt = ∞
2
,
B−=
1
ζ = ∞, lim
t→∞Xt = −∞
2
,
C−=
1
ζ < ∞, lim
t↑ζ Xt = −∞
2
.
Define ρ, s, s(∞), s(−∞) by formulas (5.6)–(5.9).
The statements below follow from [4, Ch. 4].
Proposition A.1. Either P(D) = 1 or P(B+ ∪B−∪C+ ∪C−) = 1.
Proposition A.2. (i) If s(∞) = ∞, then P(B+) = P(C+) = 0.
(ii) If s(∞) < ∞and (s(∞) −s)/ρσ2 /∈L1
loc(∞), then P(B+) > 0,
P(C+) = 0.
(iii) If s(∞) < ∞and (s(∞) −s)/ρσ2 ∈L1
loc(∞), then P(B+) = 0,
P(C+) > 0.
Clearly, Proposition A.2 has its analog for the behaviour at −∞.
For any a, c ∈R, set Ta = inf{t ∈[0, ∞): Xt = a} (here inf ∅= ∞) and
set Ta,c = Ta ∧Tc.
Proposition A.3. (i) For any a ∈R, P(Ta < ∞) > 0.
(ii) Let a ∈(−∞, x0). Then Ta < ∞P-a.s. ⇐⇒s(∞) = ∞.
(iii) Let a ∈(x0, ∞). Then Ta < ∞P-a.s. ⇐⇒s(−∞) = −∞.
(iv) Let a ∈(−∞, x0), c ∈(x0, ∞). Then Ta,c < ∞P-a.s. Moreover,
P(Ta < Tc) > 0 and P(Tc < Ta) > 0.
References
1. Bertoin, J.: L´evy Processes. Cambridge University Press 1996
2. Cherny, A.S.: Convergence of some integrals associated with Bessel processes.
Theory of Probability and Its Applications 45(2), 195–209 (2000)
3. Cherny, A.S.: On the strong and weak solutions of stochastic differential equa-
tions governing Bessel processes. Stochastics and Stochastics Reports 70, 213–
219 (2000)
4. Cherny, A.S., Engelbert, H.-J.: Singular stochastic differential equations. Lec-
ture Notes in Mathematics 1858 (2004)
5. Cherny, A.S., Urusov, M.A.: Separating times for measures on filtered spaces.
Theory of Probability and Its Applications 48(2), 416–427 (2003)
6. Dubins, L.E., Shepp, L.A., Shiryaev, A.N.: Optimal stopping rules and maximal
inequalities for Bessel processes. Theory of Probability and Its Applications
38(2), 226–261 (1993)

Separating Times
167
7. Engelbert, H.-J., Schmidt, W.: Strong Markov continuous local martingales and
solutions of one-dimensional stochastic differential equations, I, II, III. Math.
Nachr. 143, 167–184 (1989); 144, 241–281 (1989); 151, 149–197 (1991)
8. Ershov, M.P.: On the absolute continuity of measures corresponding to diffusion
type processes. Theory of Probability and Its Applications 17, 173–178 (1972)
9. Girsanov, I.V.: On transforming a certain class of stochastic processes by ab-
solutely continuous substitution of measures. Theory of Probability and Its Ap-
plications 5, 285–301 (1960)
10. Hitsuda, M.: Representation of Gaussian processes equivalent to Wiener
processes. Osaka Mathematical Journal 5, 299–312 (1968)
11. Jacod, J., M´emin, J.: Caract´eristiques locales et conditions de continuit´e absolue
pour les semi-martingales. Z. Wahrsch. Verw. Geb. 35(1), 1–37 (1976)
12. Jacod, J., Shiryaev, A.N.: Limit Theorems for Stochastic Processes. 2nd Ed.
Springer 2003
13. Kabanov, Yu.M., Liptser, R.S., Shiryaev, A.N.: Absolute continuity and singu-
larity of locally absolutely continuous probability distributions, I, II. Mathemat-
ical USSR Sbornik 35, 631–680 (1979); 36, 31–58 (1980)
14. Kabanov, Yu.M., Liptser, R.S., Shiryaev, A.N.: On the variation distance for
probability measures defined on a filtered space. Probability Theory and Related
Fields 71, 19–35 (1986)
15. Kadota, T.T., Shepp, L.A.: Conditions for the absolute continuity between a
certain pair of probability measures. Z. Wahrsch. Verw. Geb. 16(3), 250–260
(1970)
16. Kailath, T.: The structure of Radon-Nykodym derivatives with respect to
Wiener and related measures. Bulletin of American Mathematical Society 42,
1054–1067 (1971)
17. Kailath, T., Zakai, M.: Absolute continuity and Radon-Nikodym derivatives for
certain measures relative to Wiener measure. Ann. Math. Statist. 42, 130–140
(1971)
18. Kallenberg, O.: Foundations of Modern Probability. 2nd Ed. Springer 2002
19. Karatzas, I., Shreve, S.: Brownian Motion and Stochastic Calculus. 2nd Ed.
Springer 1991
20. Kunita, H.: Absolute continuity of Markov processes. Lecture Notes in Mathe-
matics 511, 44–77 (1976)
21. Kunita, H., Watanabe, S.: On square integrable martingales. Nagoya Mathe-
matical Journal 30, 209–245 (1967)
22. Liptser, R.S., Pukelsheim, F., Shiryaev, A.N.: Necessary and sufficient condi-
tions for contiguity and entire asymptotic separation of probability measures.
Russian Mathematical Surveys 37(6), 107–136 (1982)
23. Liptser, R.S., Shiryaev, A.N.: On the absolute continuity of measures corre-
sponding to processes of diffusion type relative to a Wiener measure. Izv. Akad.
Nauk SSSR, Ser. Mat. 36, 847–889 (1972)
24. Liptser, R.S., Shiryaev, A.N.: On the problem of “predictable” criteria of con-
tiguity. Lecture Notes in Mathematics 1021, 384–418 (1983)
25. Liptser, R.S., Shiryaev, A.N.: On contiguity of probability measures correspond-
ing to semimartingales. Analysis Mathematica 11, 93–124 (1985)
26. Liptser, R.S., Shiryaev, A.N.: Theory of Martingales. Nauka, Moscow 1986
27. Liptser, R.S., Shiryaev, A.N.: Statistics of Stochastic Processes. 2nd Ed.
Springer 2001

168
A. Cherny and M. Urusov
28. M´emin, J., Shiryaev, A.N.: Distance de Hellinger–Kakutani des lois correspon-
dant `a deux processus `a accroissements ind´ependants. Z. Wahrsch. Verw. Geb.
70, 67–90 (1985)
29. Newman, C.M.: The inner product of path space measures corresponding to
random processes with independent increments. Bulletin of American Mathe-
matical Society 78, 268–271 (1972)
30. Newman, C.M.: On the orthogonality of independent increment processes. In:
Topics in Probability Theory. Eds. D.W. Stroock, S.R.S. Varadhan, Courant
Institute of Mathematical Sciences, New York University 93–111 (1973)
31. Orey, S.: Conditions for the absolute continuity of two diffusions. Transactions
of American Mathematical Society 193, 413–426 (1974)
32. Pitman, J.W., Yor, M.: Bessel processes and infinitely divisible laws. Lecture
Notes in Mathematics 851, 285–370 (1981)
33. Revuz, D., Yor, M.: Continuous martingales and Brownian motion. 3rd Ed.
Springer 1999
34. Sato, K.-I.: L´evy processes and infinitely divisible distributions. Cambridge Uni-
versity Press 1999
35. Sato, K.-I.: Density transformation in L´evy processes. Lecture Notes of the
Centre for Mathematical Physics and Stochastics, University of Aarhus 2000
No. 7
36. Shiryaev, A.N.: Optimal Stopping Rules. Springer 1978
37. Shiryaev, A.N.: Essentials of Stochastic Finance. World Scientific 1998
38. Shiryaev, A.N., Spokoiny, V.G.: Statistical Experiments and Decisions. Asymp-
totic theory. World Scientific 2000
39. Skorokhod, A.V.: On the differentiability of measures which correspond to sto-
chastic processes. I. Processes with independent increments. Theory of Proba-
bility and Its Applications 2(4), 407–432 (1957)
40. Skorokhod, A.V.: Random Processes with Independent Increments. Nauka,
Moscow 1964
41. Skorokhod, A.V.: Studies in the Theory of Random Processes. Addison-Wesley
1965
42. Stroock, D.W.: Probability Theory, an Analytic View. Cambridge University
Press 1993
43. Stroock,
D.W.,
Varadhan,
S.R.S.:
Multidimensional
Diffusion
Processes.
Springer 1979

Optimal Hedging with Basis Risk
Mark H.A. DAVIS∗
Department of Mathematics, Imperial College London
London SW7 2AZ, UK.
mark.davis@imperial.ac.uk
Summary. It often happens that options are written on underlying assets that
cannot be traded directly, but where a ‘closely related’ asset can be traded. Rather
than simply using the traded asset as a proxy for the option underlying, one should
calculate some ‘best’ hedging strategy. The market is incomplete, and we address the
problem using a utility maximization approach. With exponential utility the optimal
hedging strategy can be computed in reasonably explicit form using the methods of
convex duality. In particular, a perturbation analysis using ideas of Malliavin calcu-
lus gives the modification to the exact replication strategy that is appropriate when
the option underlying and traded assets are highly, but not perfectly, correlated.
Key words: Mathematical finance, utility-based pricing, duality, hedging strate-
gies, Malliavin calculus
Mathematics Subject Classification (2000): 60H07, 60H30, 93E20
1 Introduction
On the trading floor at Tokyo-Mitsubishi International, I found that the
traders usually had excellent intuition about the sensitivity of option val-
ues to various modelling assumptions and parameter values. Correlation was
however one area where their intuition sometimes seemed mis-calibrated. If
one is hedging a book of equity options, for example, then by far the cheapest
things to hedge with are index futures: the transaction costs for trading the
underlying securities themselves are an order of magnitude higher. Since the
(return) correlation between a representative basket of stocks and the index is
very high – perhaps 80% – most traders were perfectly happy to hedge using
the index as a “proxy” asset, but had very little idea what the residual risk was
∗Work supported by the Austrian Science Foundation (FWF) under the Wittgen-
stein Prize grant Z36-MAT awarded to Professor Walter Schachermayer.

170
Mark H.A. Davis
in doing so. To see the problem, consider the model (3.1), (3.2) below, where
we have asset prices St, Yt driven by correlated Brownian motions w, w0. We
can construct these from independent Brownian motions w, w′ in the usual
way by taking w0
t = ρwt +

1 −ρ2w′
t. If ρ = 1/
√
2 then ρ =

1 −ρ2, so that
with a correlation of 70.7% half the variance of w0 is due to the independent
component w′. (Note that

1 −ρ2 is still a massive 19.9% when ρ = 98%!)
These simple facts suggest that the correlation has to be very high indeed
before asset St can reasonably be regarded as a proxy for Yt. The analysis
below shows that this is the case.
The first version of this paper was written in 2000 while I was at the
Financial and Actuarial Mathematics group at the Technical University of
Vienna. Before publishing it, I wanted to do some simulations in order to
establish whether the optimal strategy I derived was really any improvement
on the ‘naive hedge’ obtained by proceeding on the assumption that ρ =
1. However, I didn’t have time to do this myself, and various students to
whom I suggested it didn’t do a particularly convincing job. Meanwhile other
authors including Akahori [1], Henderson and Hobson [7], [8], [9], and Musiela
and Zariphopoulou [14], had joined the party with alternative approaches
and new results. Finally, Monoyios [13] gave a clean treatment including the
computational results needed to complete the picture.
I am very happy to contribute this paper – which has been quite widely
cited in preprint form – to this Festschrift for my old friend Albert Shiryaev,
particularly since it concerns a problem in stochastic control theory. I first
met Albert in Warsaw in 1973, when we were both participants (and for a
while the only two visiting ‘stochasticians’) at the first ever Semester of the
Banach Institute, devoted to Control Theory and organized by Cze`law Olech
and (on the stochastic side) Jerzy Zabczyk. It is simply amazing how the
techniques of stochastic analysis have developed and moved into the main
stream in many application areas since then, most particularly of course in
mathematical finance. Nobody has helped this process along with more talent,
enthusiasm, dedication and effectiveness than Albert, a role model for us all.
Happy birthday Albert!
2 Hedging with proxy assets
It frequently happens that options are written on underlying assets for which
no liquid market exists, but where there is a liquid market in some ‘closely
related’ asset. The hedging problem mentioned above is a good example. This
raises the question as to what are an appropriate price and the best hedging
strategy using only the tradable assets. Hubalek and Schachermayer [10] show
that no non-trivial conclusions on the price can be drawn from no-arbitrage
arguments. Indeed, since this is an ‘incomplete markets’ problem, there is no
preference-independent answer and it is appropriate to formulate the problem
in the context of utility maximization. In an earlier paper [4] we calculated the

Optimal Hedging with Basis Risk
171
‘fair price’ of an option written on a log-normal underlying asset when only a
second, correlated, log-normal asset can be traded. The ‘fair price’ is the ‘zero
marginal rate of substitution’ price introduced in [3]. In this paper we use a
similar framework but concentrate on the hedging (or investment) strategy,
using the duality approach to incomplete market investment problems in the
style laid out by Kramkov and Schachermayer [12]. The problem is in fact
one of investment with ‘random endowment’ as studied by Cvitani´c et al. [2].
Like these authors we use duality theory, showing directly the existence of
an optimal solution to the dual problem and the absence of a ‘duality gap’,
thus producing a solution to the primal problem and the optimal investment
strategy. This strategy is given in Theorem 7.1 and has a nice interpretation.
When the traded asset is perfectly correlated with the option underlying we
can hedge perfectly using the ‘rescaled’ Black-Scholes delta given by (3.4)
below. When correlation is imperfect the same strategy is optimal, but with
the Black-Scholes option value C replaced by the value function W of a certain
stochastic control problem.
As will be seen, the stochastic control problem emerges from solving the
dual problem. While existence of a solution to the stochastic control problem
follows from well-known theory there is no closed-form solution since the ter-
minal conditions are option-like payoffs, not, say, quadratic penalties. Thus
we are still in general obliged to resort to numerical algorithms in order to
compute the solution. However, it is also possible to do a perturbation analy-
sis. We are mainly interested in the case ρ ≈1, where ρ is the correlation
between the option underlying and the tradable asset. Defining ε =

1 −ρ2
we can, using elementary ideas of Malliavin calculus, get the leading term in
the expansion of the value function of the stochastic control problem in powers
of ε. (The case ε = 0 is Black-Scholes.) This determines the modification in
hedging strategy required when the correlation is just slightly less than one.
In this paper we use an exponential utility function and assume that option
payoffs are bounded from below. This covers puts and long calls, and most
varieties of spread options, but unfortunately not short calls which are in some
ways the most interesting case. Short call options and exponential utility are
simply incompatible under the standard log-normal price model.
3 Problem formulation
Suppose we have two assets whose prices Yt, St are log-normal diffusions, i.e.,
satisfy
dYt = µ0Ytdt + σ0Ytdw0
t
(3.1)
dSt = µStdt + σStdwt
(3.2)
where w, w0 are standard Brownian motions with E(dwtdw0
t ) = ρdt. All
parameters are constant and (3.1), (3.2) are in the physical measure, not a

172
Mark H.A. Davis
risk neutral measure. The riskless rate of interest is r, again assumed constant.
If |ρ| < 1 there is no necessary relationship between the parameters in (3.1),
(3.2). On the other hand if ρ = 1 then µ0, µ must be related by
µ0 = r + σ0
σ (µ −r)
(3.3)
to avoid arbitrage (see [4]).
A European option has been written on asset Yt whose payoffto us
at exercise time T is h(YT ) where h is a bounded continuous function.
For example, if we are short a spread option with strikes K1 < K2, then
h(y) = [y −K2]+ −[y −K1]+. Let C(t, y) be the Black-Scholes value of the
option at time t when Yt = y. If we hedge using Yt then the hedge ratio
(the number of stock units in the replication portfolio) is of course the Black-
Scholes delta ∂C/∂y(t, Yt). Asset Yt, however, cannot be traded; the only
tradable asset is St. If ρ = 1 we can still form a perfectly replicating portfolio;
the hedge ratio – now the number of St stock units – is2
∂C
∂y (t, Yt)σ0Yt
σSt
.
(3.4)
If |ρ| < 1, perfect hedging is generally impossible. When ρ is close to 1 we
might consider using strategy (3.4), but the performance of this strategy is
rather poor, even when ρ is well in excess of 95%; see section 10 below. To
approach the problem systematically, let us assume that our overall objective
is to maximize utility as measured by the exponential utility function3
U(x) = −e−γβx
(3.5)
where γ > 0 is a fixed constant and β = e−rT . Starting with an initial
endowment x, and in the absence of any options, we wish to maximize
ExU(Xπ
T )
(3.6)
where Xπ
T is the portfolio value at time T under trading strategy π with
Xπ
0 = x (precise definitions later). If at time 0 we purchase for price p an
option with payoffh(YT ) then the objective must be modified to maximizing
Ex−pU (Xπ
T + h(YT )) .
(3.7)
In [4] we considered the pricing problem, i.e., determining the value of p such
that the maximized utilities in (3.6), (3.7) are the same. Here we consider
problem (3.7) with an arbitrary initial endowment x′, the aim being to es-
tablish in as much detail as possible what the optimal investment strategy
π is. The fair price will come out as a by-product; see Theorem 8.1 below.
2Note that the price process Yt can be observed even though Yt cannot be traded.
3The factor β is notationally convenient.

Optimal Hedging with Basis Risk
173
Throughout the paper, the utility function U is always the exponential utility
(3.5).
It is easy to see that if |ρ| < 1 and h(Y ) = −[Y −K]+, i.e., we are
short a call option, then ExU(Xπ
t + h(YT )) = −∞for any trading strat-
egy. (Roughly speaking, h(YT ) ≈−eσ0wT and E exp(eX) = ∞for any nor-
mal random variable X.) To get a meaningful problem we would have to
choose a different utility function, one that decreases sufficiently slowly so
that EU(−[YT −K]+) > −∞. But then we lose some of the explicit compu-
tations that are available for exponential utility.
The precise assumptions on the option exercise value are as follows.
Assumption 3.1 h : R + →R bounded below and is a finite linear combina-
tion of European put and call exercise values.
As pointed out in the Introduction this covers long and short puts, long calls
and various spread options, but excludes short calls. Note that Assumption
3.1 implies the existence of constants y0, c1, c2 such that h(y) = c1 + c2y for
y ≥y0. h is bounded if c2 = 0; otherwise c2 > 0.
4 Local martingale measures
Let us write
w0
t = ρwt +

1 −ρ2w′
t
where wt, w′
t are independent Brownian motions. The stochastic basis will be
(Ω, (F)t≤T , P) where Ft is the natural filtration of (wt, w′
t). From now on we
assume |ρ| < 1 unless otherwise mentioned, and denote ε =

1 −ρ2.
If Q is a probability measure equivalent to P on FT then there exist
adapted processes mt, gt such that
 T
0 m2
tdt < ∞,
 T
0 g2
t dt < ∞, a.s., and
dQ
dP = exp
	 T
0
mtdwt −1
2
 T
0
m2
tdt +
 T
0
gtdw′
t −1
2
 T
0
g2
t dt

.
(4.1)
Under measure Q the processes *wt, *w′
t defined by
d *wt = dwt −mtdt
(4.2)
d *w′
t = dw′
t −gtdt
(4.3)
are independent Brownian motions. Q is a local martingale measure if the
process e−rtSt is a Q-local martingale (recall that St is the only traded asset)
and this is true if and only if
mt ≡m := r −µ
σ
.

174
Mark H.A. Davis
The set of equivalent local martingale measures, denoted M, is therefore in
one-to-one correspondence with the set of integrands gt via formula (4.1) with
mt = m. Under measure Q, Yt satisfies
dYt = Yt(µ0 + σ0ρm + σ0εsilongt)dt + Ytσ0d *w0
t
(4.4)
where *w0
t = ρ *wt+εsilon *w′
t is a Brownian motion. Thus Yt can have essentially
arbitrary drift under equivalent martingale measures, while the drift for St is
the riskless rate r.
5 Trading Strategies
A trading strategy is an adapted process πt satisfying
 T
0
π2
t dt < ∞a.s.
(5.1)
πt is the dollar value of stock in our portfolio at time t. Let A0 denote the
set of trading strategies. Since St is the price, the number of stock units is
Ht = πt/St. If the total portfolio value is Xπ
t , then (Xπ
t −πt) is invested at
the riskless rate r, so the increment in portfolio value is
dXπ
t = HtdSt + (Xπ
t −πt)rdt
= rXπ
t dt + σπtd *wt,
where *wt is given by (4.2). Denoting
ˇXπ
t = e−rtXπ
t , ˇπt = e−rtπt
we find that
d ˇXπ
t = ˇπσd *wt
(5.2)
so that ˇXπ
t is a local martingale under any equivalent martingale measure
Q ∈M. Note that if we work in terms of discounted prices ˇSt = e−rtSt then
(5.2) becomes
d ˇXπ
t = Htd ˇSt.
Our objective is to maximize the utility (3.7) over some class of trading strate-
gies π. We can express (3.7) in terms of discounted quantities by writing
exp (−γβ (Xπ
T + h(YT ))) = exp

−γ
 ˇXπ
T + βh(YT )

,
so that
EU (Xπ
T + h(YT )) = EUγ
 ˇXπ
T + βh(YT )

.
(5.3)
As is well known, in order to obtain a meaningful optimization problem
we have to place some restriction on the trading strategies, to eliminate ‘dou-
bling strategies’ [6]. In the spirit of Schachermayer [15] we make the following
definitions

Optimal Hedging with Basis Risk
175
Ab = {π ∈A0 : Xπ
t ≥aπ a.s. for all t ∈[0, T], for some aπ ∈R} . (5.4)
U = {U (Xπ
T + h(YT )) : π ∈Ab}c .
(5.5)
Here {. . .}c denotes the closure in L1(Ω, FT , P).
A = {π ∈A0 : U (Xπ
T + h(YT )) ∈U} .
(5.6)
The point here is that the class Ab is not big enough. When wealth can be
negative as well as positive, it is natural — and, as we shall see, necessary —
to allow certain strategies where the wealth is not bounded below.
6 The Dual Problem
Duality methods are well established in utility maximization, see Karatzas
and Shreve [11] or Kramkov and Schachermayer [12] for example. The dual
function V : R + →R is defined by
V (η) = max
x∈R {Uγ(x) −xη}
(6.1)
= η
γ

log η
γ −1

(6.2)
= Uγ(I(η)) −ηI(η),
(6.3)
where I = (U ′
γ)−1 is given by
I(η) = −1
γ log η
γ .
The dual problem is to minimize M(η, Q) over M for each η ∈R +, where
M(η, Q) = E

V

η dQ
dP

+ βη dQ
dP h(YT )

= V (η) + η
γ EQ log
dQ
dP

+ βηEQh(YT )
(from (6.2) and with EQ denoting the Q-expectation). The argument at the
beginning of section 7 below shows why this is the appropriate form of dual
problem to consider. Under measure Q we have from (4.2), (4.3)
log dQ
dP = m *wT + 1
2m2T +
 T
0
gtd *w′
t +
 T
0
g2
t dt.
If
EQ
 T
0
g2
t dt < ∞
(6.4)
then EQ

gd *w = 0 and

176
Mark H.A. Davis
EQ log dQ
dP = 1
2m2T + 1
2EQ
 T
0
g2
t dt,
whereas if (6.4) is not satisfied then we define EQ log dQ/dP = ∞. Denoting
by M′ the subset of M for which the integrands g satisfy (6.4) we see that
for Q ∈M′,
M(η, Q) = V (η) + 1
2m2T η
γ + ηEQ

1
2γ
 T
0
g2
t dt + βh(YT )

,
(6.5)
and clearly infQ∈M′ M(η, Q) = infQ∈M M(η, Q). The dual problem is thus
equivalent to the stochastic control problem of minimizing
EQ

1
2γ
 T
0
g2
t dt + βh(YT )

(6.6)
over control processes gt. For a given process gt the measure Q is defined by
(4.1) and Yt is then a weak solution of the SDE (4.4). We can equivalently
pose the problem in the context of admissible systems. An admissible system
is a collection S = (Ξ, (Gt), P, (Bt), (gt)), where (Ξ, (Gt), P) is a filtered prob-
ability space and Bt, gt are adapted processes such that Bt is a Gt-Brownian
motion while gt satisfies
E
 T
0
g2
t dt < ∞.
Given S, a starting time s and an initial point y there is a unique strong
solution Yt to the SDE
dYt = Yt(µ0 + σ0ρm + σ0εgt)dt + Ytσ0dBt,
Ys = y,
(6.7)
to which we associate a cost
CS(s, y) = E

1
2γ
 T
s
g2
t dt + βh(YT )

.
(6.8)
Let c∗= infS CS(0, Y0) be the infimal cost over the set of admissible systems.
Clearly c∗is a lower bound for (6.6); we will show that this bound is attained
for some choice of (gt) in the original setup.
Theorem 6.1. There exists ˆQ ∈M′ such that for all η ∈R +
M(η, ˆQ) = min
Q∈M M(η, Q).
The minimum value is
V (η) +
 1
2γ m2T + W(0, Y0)

η

Optimal Hedging with Basis Risk
177
where W is the unique C1,2 solution of (6.15), (6.16) below4. The minimizing
measure ˆQ corresponds to g = ˆg in (4.1), where ˆg is given by (6.17).
Proof. Under Assumption 3.1, h is either constant, or has constant positive
slope, for large y. Let us first assume the former, specifically:
Assumption 6.1 The function h is bounded by ¯h ∈R +.
Take an admissible system S as described above and define
Zt = 1
σ0
log Yt
and
f(z) = βh(eσ0z), z ∈R.
We find that Zt satisfies
dZt = (a + εgt)dt + dBt
(6.9)
where a := µ0/σ0+ρm−σ0/2. The cost (6.8) is expressed in the new variables
as
C′
S(s, z) = E

1
2γ
 T
s
g2
t dt + f(ZT )

.
(6.10)
Minimizing (6.10) is a standard form of stochastic control problem, whose
solution is related to that of the corresponding Bellman equation , a semilinear
parabolic PDE to be satisfied by a C1,2 function L : [0, T] × R →R:
∂L
∂t + 1
2
∂2L
∂z2 + min
g∈R

(a + εg)∂L
∂z + 1
2γ g2

= 0
(6.11)
L(T, z) = f(z)
(6.12)
Lemma 6.1. When h satisfies Assumptions 3.1 and 6.1, there is a unique
function L, bounded and continuous on [0, T] × R and C1,2 on [0, T[×R, sat-
isfying (6.11), (6.12). L is the value function for the control problem, i.e., for
(s, z) ∈[0, T[×R,
L(s, z) = min
g
Es,z

1
2γ
 T
s
g2
t dt + f(ZT )

,
where the controlled process Zt starts at Zs = z. The optimal process gt is
given by
ˆgt = −γε∂L
∂z (t, Zt)
(6.13)
(the minimizing value in (6.11)).
4C1,2 denotes the set of functions W(t, y) that are continuously differentiable up
to order one (two) in t, (y).

178
Mark H.A. Davis
Proof of Lemma. Assumption 6.1 implies that f is globally Lipschitz contin-
uous. Denote by CM(s, z) the infimum infS CS(s, z), taken over the set of
admissible systems satisfying the additional restriction |gt| ≤M, t ∈[s, T]. It
is clear from the simple dependence of ZT on z given in (6.9) that CM(t, z) is
Lipschitz continuous with the same constant κ′ as f. Now consider equations
(6.11), (6.12) where the minimum in (6.11) is taken over g ∈[−M, M]. It fol-
lows from Fleming and Rishel [5] Theorem VI.6.25 that these equations have
a unique C1,2 solution LM in [0, T[×R that is continuous in [0, T] × R, and
that LM = CM. Hence LM is Lipschitz with constant κ′ and from (6.13) we
see that the optimal process ˆgM
s
satisfies |ˆgM
s | ≤γεκ′. Thus the bound M on
gt is irrelevant as long as M > εκ′ and then LM = L satisfying (6.11), (6.12)
as stated. This completes the proof.
⊓⊔
The point of transforming coordinates from Yt and Zt is that (6.11) is
uniformly elliptic (the coefficient of the second-order term is uniformly positive
– in this case, constant.) Now, however, we can express things in the original
coordinates by defining
W(t, y) = L(t, 1
σ0
log y).
(6.14)
We find that W satisfies
∂W
∂t + (µ0 + σ0ρm)y ∂W
∂y + 1
2σ2
0y2 ∂2W
∂y2
+ min
g
 1
2γ g2 + σ0εgy ∂W
∂y

= 0
(6.15)
W(T, y) = βh(y)
(6.16)
and the optimal gt is given by
ˆgt = ˆu(t, Yt)
(6.17)
where ˆu is the minimizing value in (6.15), i.e.,
ˆu(t, y) = −γεσ0y ∂W
∂y (t, y).
Since W satisfies (6.15), (6.16) if and only if L satisfies (6.11),(6.12), we
have shown that (6.15), (6.16) has a unique C1,2 solution W. Using ˆg
given by (6.17) to define the measure ˆQ in (4.1) gives an admissible sys-
tem (Ω, (Ft), ˆQ, ( ˜w0
t ), (ˆgt)) that achieves the minimal cost. This completes
the proof under the supplementary Assumption 6.1.
Recall that when Assumption 3.1 holds but Assumption 6.1 does not,
h(y) = c1 + c2y for large y, with c2 > 0. For N ∈R, define hN(y) = h(y) ∧N.
5This result as stated requires f to be C2, but it covers our case by using uni-
formly Lipschitz C2 approximations to f and using the local PDE estimates men-
tioned in [5] Appendix E.

Optimal Hedging with Basis Risk
179
Then for sufficiently large N, and N ′ > N, hN satisfies Assumption 6.1 and
there exist yN, yN′ ∈R + such that for
hN′(y) = hN(y) + c2([y −yN]+ −[y −yN′]+).
Let S be an optimal admissible system for the control problem with initial
state Ys = y and terminal cost hN, with control process ˆgt and cost
J N(ˆg) = E
	
1
2γ
 T
s
ˆg2
t dt + βhN(YT (ˆg))

.
(6.18)
Recall ˆg is bounded by, say, ¯c. Now let ˜g(t, ω) be an adapted process such that
˜g(t, ω) ≥0 a.s. and E
 T
s ˜g(t, ω)dt > 0, and define
g(t, ω) = ˆg(t, ω) + ˜g(t, ω).
Since ˆg is optimal, J N(g) ≥J N(ˆg) and also
E([YT (g) −yN]+ −[YT (g) −yN′]+) ≥E([YT (ˆg) −yN]+ −[YT (g) −yN′]+)
in view of the monotone dependence of YT (g) on g. Hence J N′(g) ≥J N′(ˆg).
Thus candidate controls for minimizing J N′(g) must be less than or equal to
ˆg, in particular bounded above by ¯c.
Denoting a0 = µ0 + σ0ρm, the solution to equation (6.7) is Yt = yξs,t
where
ξs,t = exp
 t
s
(a0 + σ0εgu −1
2σ2
0)du + σ0(Bt −Bs)

.
Thus for admissible systems starting at time s with two different starting
points y1, y2 we have, in an obvious notation,
|J N′(g)(y2) −J N′(g)(y1)| ≤E|h(y2ξs,T ) −h(y1ξs,T )|
≤κ|y2 −y1|E[ξs,T ]
≤|y2 −y1|κ exp ((a0 + σ0ε¯c)T)
The functions J N′(g)(y) are thus uniformly Lipschitz continuous in y, and
we know that
W N′(s, y) = min
S J N′(g)(y),
where W N′ denotes the value function, i.e. the solution of (6.15),(6.16) with
h = hN′. The functions W N′ are therefore uniformly Lipschitz continuous,
with the same constant, for all N ′ > N. Since in fact W N′ ∈C(1, 2), we have
shown that the derivatives ∂W N′/∂y are uniformly bounded.
The functions W N′ are monotonically increasing in N ′ since the ’terminal
costs’ hN′ are increasing. They are also bounded by βE(h(Y 0
T )) where Y 0
denotes the solution of (6.7) with g ≡0. Thus W N′(s, y) ↑W(s, y) where W
is a Lipschitz continuous function.

180
Mark H.A. Davis
We can now complete the proof following exactly the proof of Theorem
6.6.2 of Fleming and Rishel [5], pages 210-211. They show that, under condi-
tions that are satisfied here, the derivatives ∂W N′/∂y satisfy a uniform H¨older
condition on compact sets. An application of the Ascoli theorem shows that
W N′ and the required first and second derivatives converge uniformly on
compact sets and hence that the limiting function W is C1,2 and satisfies
(6.15),(6.16). A standard ‘verification’ argument now shows that W is the
value function, i.e. W(s, y) = minS CS(s, y) where CS is given by (6.8). This
completes the proof of Theorem 6.1.
⊓⊔
7 An optimal trading strategy
Taking a trading strategy π ∈Ab and initial endowment x, let us write
ˇXπ
T = x + X = x +
 T
0
Htd ˇSt
using the notation of section 5. The stochastic integral is a local martingale
that is bounded below, and hence a supermartingale, for any Q ∈M. By
definition of the dual function V , for η ∈R +
EUγ (x + X + βh(YT ))
≤E

V

η dQ
dP

+ η (x + X + βh(YT )) dQ
dP

(7.1)
≤E

V

η dQ
dP

+ ηβ dQ
dP h(YT )

+ xη.
Hence, minimizing the right hand side over Q ∈M we have
EUγ (x + X + βh(YT )) ≤v(η) + xη
(7.2)
where v(η) = M(η, ˆQ). The expression v(η) + xη is minimized by ˆη satisfying
v′(ˆη) = −x, and using (6.2) we find that ˆη satisfies
−1
γ log ˆη
γ = 1
2γ m2T + W(0, Y0) + x.
(7.3)
Inequality (7.2) implies that EΘ ≤v(ˆη)+xˆη for any Θ ∈U where U is the set
of ‘achievable utilities’ defined by (5.5). If equality holds in (7.2) with η = ˆη
and X corresponds to some π ∈A then π is optimal in A, though π will
generally not be unique. We see from (6.3) that equality holds in (7.2) if and
only if
x + X + βh(YT ) = I
	
ˆη d ˆQ
dP

= −1
γ log ˆη
γ −1
γ log d ˆQ
dP .

Optimal Hedging with Basis Risk
181
Thus, using (7.3), we see that X is optimal only if X = ˆX where ˆX is given
by
ˆX = 1
γ m2T + W(0, Y0) −1
γ
	
mwT +
 T
0
ˆgtdw′
t −1
2
 T
0
ˆg2
t dt

−βh(YT ).
(7.4)
Theorem 7.1. Let
Ht = µ −r
γσ2
ert
St
−ρert ∂W
∂y
σ0Yt
σSt
(7.5)
and π∗
t = HtSt, where W(t, y) is the solution of (6.15), (6.16). Then π∗∈A
and the utility of π∗achieves supΘ∈U EΘ, where U is defined by (5.5).
Proof. Define ˆX by (7.4). Then equality holds in (7.2) with X = ˆX and η = ˆη,
and therefore x + ˆX is the optimal terminal wealth, as long as E ˆ
Q ˆX = 0 and
there is some admissible strategy π∗such that x + ˆX = ˇXπ∗
T . In (7.4), recall
that βh(YT ) = W(T, YT ). Under measure P, Yt satisfies (3.1), so by the Itˆo
formula,
W(T, YT ) −W(0, Y0) =
 T
0
∂W
∂t + µ0Yt
∂W
∂y + σ2
0Y 2 1
2
∂2W
∂y2

dt
+
 T
0
σ0Ytρ∂W
∂y dwt +
 T
0
σ0Ytε∂W
∂y dw′
t. (7.6)
Now use (6.15),(6.16), recalling that equality holds in (6.15) when
gt = ˆgt = −γεσ0Y ∂W
∂y .
(7.7)
We find that
βh(YT ) −W(0, Y0) = −
 T
0

σ0ρmYt
∂W
∂y + 1
2γ ˆg2
t + σ0εˆgtYt
∂W
∂y

dt
+
 T
0
ρσ0Yt
∂W
∂y dwt −1
γ
 T
0
ˆgtdw′
t.
(7.8)
Replacing βh(YT )−W(0, Y0) by the right-hand side of (7.8) in (7.4) and using
(7.7) we obtain
ˆX = −
 T
0
m
γ + ρσ0Yt
∂W
∂y

d *wt
where *wt = wt −mt is a Q-Brownian motion for any Q ∈M, in particular
for Q = ˆQ. Now ρσ0Yt∂W/∂y = −(ρ/γε)ˆgt, and we know that
E ˆ
Q
 T
0
ˆg2
t dt < ∞
(7.9)

182
Mark H.A. Davis
since ˆgt is optimal for the control problem of minimizing (6.10). Hence
ˆXt := −
 t
0
m
γ + ρσ0Ys
∂W
∂y

d *ws
(7.10)
is a ˆQ-martingale. Comparing (7.10) with (5.2) we see that d ˆXt = Htd ˇSt
where Ht is defined by (7.5) in the Theorem statement.
Finally, it is clear that π∗∈A. If we define πn
t = π∗
t 1t<τn, where τn =
inf{t : ˆXt ≤−n} then πn ∈Ab and Xπn
T
→Xπ∗
T
in L2. This completes the
proof.
⊓⊔
Remark 1. The trading strategy Ht of (7.5) and corresponding portfolio value
process ˆXt of (7.10) are very intuitive. When h ≡0, i.e., no option is written,
ˇπ∗
t = −m/σγ is simply the optimal investment strategy for maximizing expo-
nential utility: this strategy keeps a constant dollar value (in discounted units)
in stock. When h ̸= 0 but ρ = 0 the same strategy is optimal. This is the ‘com-
pletely unhedgeable’ case where h(YT ) is independent of the traded asset St
and simply provides a random perturbation of the level of final wealth. Recall
that the exponential utility function has wealth-independent risk aversion:
−U ′(x)
U ′(x) = γ.
This implies that the investor’s behavior does not depend on his initial endow-
ment. If we condition on the value of h(YT ) then the optimization problem is
equivalent to a shift in the initial endowment, having no effect on the optimal
strategy. Thus the strategy is the same whether or not the option payoffis
included.
At the other extreme is the case ρ = 1, ε = 0, when the assets are perfectly
correlated. Then the drifts µ and µ0 are related by the no-arbitrage condition
(3.3), and clearly the optimal control in (6.15) is ˆgt ≡0. Thus (6.15), (6.16)
reduce to
∂W
∂t + ry ∂W
∂y + 1
2σ2
0y2 ∂2W
∂y2 = 0
W(T, y) = βh(y).
(7.11)
By the Feynman-Kac formula, the solution to this is
W(t, y) = EQ
t,y[βh(YT )],
where EQ
t,y denotes expectation with respect to the (now unique) martingale
measure Q, starting at Yt = y. Recalling that β = e−rT , we can rewrite this
as
W(t, y) = e−rtEQ
t,y[e−r(T −t)h(YT )]
= e−rtC(t, y),

Optimal Hedging with Basis Risk
183
where C is the Black-Scholes option value. The second term in (7.5) therefore
coincides with (3.7), the perfect replication strategy implemented by trading
in St. Again, the fact that the optimal portfolio process (7.10) is the sum
of two funds, an ‘investment fund’ and a ‘hedging fund’ is a consequence of
wealth-independent risk aversion.
When |ρ| < 1 the optimal hedging strategy takes the same form as (3.7),
but with C replaced by the value function of the stochastic control problem
introduced in section 6.
8 Pricing
Let us now consider the question of option pricing. As mentioned in Section
3, the zero marginal rate of substitution price is the number p, if it exists,
such that
sup
π∈A
ExU (Xπ
T ) = sup
π∈A
Ex−pU (Xπ
T + h(YT ))
(8.1)
where Ex denotes the expectation when the investor’s initial endowment is x.
(This could be a buying or writing price depending on whether h represents
a long or short position.) When h ≡0 the optimal investment strategy is
Ht = µ −r
γσ2
ert
St
,
and the corresponding portfolio value is
ˇXπ
T = x + m2
γ T −m
γ wT
(m = (r −µ)/σ), so that
EUγ
 ˇXπ
T

= −e−γxem2T/2.
(8.2)
With the option present, we know from the proof of Theorem 7.1 that the
maximum utility is equal to v(ˆη) + xˆη where v(ˆη) = M(ˆη, ˆQ) and ˆη is defined
by (7.3). From these equations we find that the maximum utility is
−e−γxem2T/2e−γW (0,Y0).
(8.3)
We have shown the following. Note that the fair price does indeed reduce to
the Black-Scholes price when ρ = 1 and the no-arbitrage condition (3.3) is
satisfied.
Theorem 8.1. The fair price p of (8.1) is given by
p = W(0, Y0),
where W(t, y) is the solution of (6.15), (6.16).
Proof. This follows immediately by writing (8.3) as −e−γ(x+W )em2T/2 and
comparing with (8.2).

184
Mark H.A. Davis
9 The High-Correlation Case
The ‘value function’ W introduced in Section 6 satisfies
W(t, y) = min
g
Et,y

1
2γ
 T
t
g2
sds + βh(Y ε
T )

(9.1)
where the minimum is taken over control processes gt for the stochastic dif-
ferential equation
dY ε
s = Y ε
s (µ0 + σ0ρm + σ0εgs)ds + Y ε
s σ0dBs
(9.2)
Y ε
t = y
We now write Y ε
s instead of Ys to emphasize the dependence on ε, and we
wish to consider the case where ρ is close to 1, i.e., ε is small. Note that ε
multiplies gs in (9.2) but not the ‘penalty’ g2
s in (9.1). This implies that the
optimal process ˆgs must be ‘small’ and the corresponding process Y ε
s a small
perturbation away from Y 0
s . Using elementary ideas of Malliavin calculus we
can compute explicitly the function W 0,2 in the expansion
W ε(t, y) = W 0(t, y) + ε2W 0,2(t, y) + o(ε2)
where W ε = W, defined by (9.1). This in turn gives us the perturbation in
the trading strategy due to imperfect correlation between the assets.
Consider first the case ε = 0, ρ = 1. The optimal control is gt ≡0, so that
W 0(t, y) = Et,y[βh(Y 0
T )],
where
dY 0
s = Y 0
s (µ0 + σ0m)ds + Y 0
s σ0dBs.
If we write µ0 + σ0m = r −q then we see, as in Remark 1, that
W 0(t, y) = e−rtC(t, y, q),
where C(t, y, q) denotes the Black-Scholes price with dividend yield q. Note
that q = 0 if µ0 satisfies the no-arbitrage drift condition (3.3), but in the
present context there is no reason why this condition should be satisfied.
Moving to the case in which ε is small but strictly positive, we will need
the following simple result.
Lemma 9.1. Let A be a finite-variance random variable with standard devia-
tion σA, and consider the problem of minimizing E[AG] over random variables
G with EG=0, EG2 = κ2. The minimum value is −κσA, achieved by
G = −κA −EA
σA
.

Optimal Hedging with Basis Risk
185
For a fixed control gs it is evident from (9.2) and the Girsanov theorem
that L(Y ε, P, t, y) = L(Y 0, P ε, t, y), where
dP ε
dP = exp
	
ε
 T
t
gsdBs −1
2ε2
 T
t
g2
sds

=: Gε
T (g).
(9.3)
Here L(Y ε, P, t, y) denotes the law of Y ε under measure P, starting at Y ε
t = y.
Hence
1
ε
1
E [h(Y ε
T )] −E

h(Y 0
T )
2
= E

h(Y 0
T )1
ε (Gε
T (g) −1)

.
(9.4)
Lemma 9.2. The function ε →E[h(Y ε
T )] is differentiable at ε = 0 with deriv-
ative
∂
∂εE [h (Y ε
T )]|ε=0 = E
B
h

Y 0
T
  T
t
gsdBs
C
,
(9.5)
Further, if gt = αˆgt where ˆgt is a fixed integrand and α ∈R,
E [h (Y ε
T )] −E

h

Y 0
T

−εE
B
h

Y 0
T
  T
t
gsdBs
C
= O

ε2α2
.
(9.6)
Proof. Define Gε(g) by (9.3). It is shown in Theorem E.2 of Karatzas and
Shreve [11] that
1
ε (Gε
T (g) −1) →
 T
t
gsdBs in L2 as ε →0.
(9.7)
This establishes (9.5), in view of (9.4) and the fact that h is bounded.
When gt = αˆgt we can express the left hand side of (9.6) as
E

h

Y 0
T

	
Gε
T −1 −εα
 T
t
ˆgsdBs


where Gε
T = Gε
T (g). Now Gε
T satisfies
dGε
s = εαGε
sˆgsdBs, Gε
t = 1
so that
Gε
T −1 −εα
 T
t
ˆgsdBs = εα
 T
t
(Gε
sˆgs −ˆgs) dBs
= ε2α2
 T
t
ˆgs
Gε
s −1
εα
dBs.
Now (9.6) follows, using (9.7) again.

186
Mark H.A. Davis
Theorem 9.1. Denote by W ε(t, y) the right-hand side of (9.1). Then
W ε(t, y) = W 0(t, y) + ε2W 0,2(t, y) + O(ε4)
where
W 0,2(t, y) = −1
2γβ2vart,y

h(Y 0
T )

Proof. For fixed g we have from (9.5)
E

1
2γ
 T
t
g2
sds + βh(Y ε
T )

= βE

h(Y 0
T )

+ E

1
2γ
 T
t
g2
sds + εβh(Y 0
T )
 T
t
gsdBs

+ O(ε2)
Consider the second term on the right. In view of Lemma 9.1, for a fixed value
of E
 T
t g2
sds we minimize this term by choosing gs = αˆgs for some constant
α, where
h(Y 0
T ) = E

h(Y 0
T )

+
 T
t
ˆgsdBs.
(Here Y 0
s begins at Y 0
t = y.) Such a choice of ˆgs is possible, thanks to the
martingale representation theorem for Brownian motion and the assumption
that h is bounded. Then
E

1
2γ
 T
t
ˆg2
sds + εβh(Y 0
T )
 T
t
ˆgsdBs

= var

h(Y 0
T )
 α2
2γ + βεα

The best choice of α is α = −βγε, giving a minimum value of
−1
2γε2β2var(h(Y 0
T )).
The error term is O(ε2α2) = O(ε4), from (9.6).
10 How good is the ‘optimal’ strategy?
As mentioned in section 1, the computational side of this problem has been
thoroughly investigated by Monoyios [13]. In particular, he considers writing
a put option and hedging it both with the optimal strategies derived above
and with the ‘naive’ strategy obtained by assuming ρ = 1. In Monoyios’ simu-
lations, ρ was taken to be either 0.65 or 0.85, and the risk aversion coefficient
γ was 0.01 or .001. The results are qualitatively similar in all four cases. The
optimal strategy is superior to the naive hedge in that the hedge profit distri-
bution is more positively skewed, so that the median hedge profit is increased
and with it the hedger’s probability of a positive outcome. However, in all

Optimal Hedging with Basis Risk
187
cases the variance of the hedge profit is very high, with a standard deviation
comparable to the Black-Scholes option value, so the trader is quite likely to
lose an amount on the hedge which is greater than the premium taken in. (By
contrast, the standard deviation of hedge error due to discrete rather than
continuous-time rebalancing would typically be 5-10% of the premium). The
conclusion is the one alluded to in section 1: even with very high correlation,
a large amount of unhedgeable noise is being injected into the non-traded
asset, making accurate hedging both practically and theoretically impossible.
Option trading in these circumstances is in fact a question of balancing risk
and reward, i.e. of optimal investment, making a utility-based approach highly
appropriate.
References
1. Akahori, J.: Asymptotics of hedging errors in a slightly incomplete discrete
market, working paper, Ritsumeikan University, November 2001.
2. Cvitani´c, J., Schachermayer, W. and Wang, H.: Utility maximization in incom-
plete markets with random endowment, Finance and Stochastics 5, 259–272
(2001)
3. Davis, M.H.A.: Option pricing in incomplete markets, in Mathematics of Deriv-
ative Securities, eds. M.A.H. Dempster and S.R. Pliska, Cambridge University
Press 1997, pp. 216–226.
4. Davis, M.H.A.: Option valuation and hedging with basis risk, in System Theory:
Modeling, Analysis and Control, eds. T.E. Djaferis and I.C. Schick, Amsterdam:
Kluwer 1999, pp. 245–254.
5. Fleming, W.H. and Rishel, R.W.: Deterministic and Stochastic Optimal Control,
New York: Springer-Verlag 1975.
6. Harrison, J.M. and Pliska, S.R.: Martingales and stochastic integrals in the
theory of continuous trading, Stoch. Proc. Appl. 11 215–260 (1981)
7. Henderson, V.: Valuation of claims on non-traded assets using utility maximiza-
tion, Math. Finance, 12, 351–373 (2002)
8. Henderson, V. and Hobson, D.G.: Substitute hedging, Risk 15,71–75 (2002)
9. Henderson, V. and Hobson, D.G.: Real options with constant relative risk aver-
sion, J. Economic Dynamics and Control 27, 329–355 (2002)
10. Hubalek, F. and Schachermayer, W.: The limitation of no-arbitrage arguments
for real options, Int. J. Theor. and Appl. Finance 4, 361–373 (2001)
11. Karatzas, I. and Shreve, S.E.: Methods of Mathematical Finance, New York:
Springer-Verlag 1998.
12. Kramkov, D. and Schachermayer, W.: The asymptotic elasticity of utility func-
tions and optimal investment in incomplete markets, Ann. Appl. Prob. 9, 904–
950 (1999)
13. Monoyios, M.: Performace of utility-based strategies for hedging basis risk,
Quantitative Finance, 4, 245–255 (2004)
14. Musiela, M. and Zariphopoulou, T.: An example of indifference prices under
exponential preferences, Finance and Stochastics, 8, 229–239 (2004)
15. Schachermayer, W.: Optimal investment in incomplete markets when wealth
may become negative, Ann. Appl. Prob. 11, 694–734 (2001)


Moderate Deviation Principle for Ergodic
Markov Chain. Lipschitz Summands
Bernard DELYON, Anatoly JUDITSKY, and Robert LIPTSER
1 Universit´e de Rennes 1, IRISA, Campus de Beaulieu, 35042 Rennes Cedex,
France.
bernard.delyon@univ-rennes1.fr
2 University Joseph Fourier of Grenoble, France.
juditsky@inrialpes.fr
3 Electrical Engineering-Systems, Tel Aviv University, 69978 Tel Aviv Israel,
Institute of Information Transmission, Moscow, Russia.
liptser@eng.tau.ac.il
Summary. For 1
2 < α < 1, we propose the MDP analysis for family
Sα
n = 1
nα
n

i=1
H(Xi−1), n ≥1,
where (Xn)n≥0 be a homogeneous ergodic Markov chain, Xn ∈Rd, when the spec-
trum of operator Px is continuous. The vector-valued function H is not assumed to
be bounded but the Lipschitz continuity of H is required. The main helpful tools in
our approach are Poisson’s equation and Stochastic Exponential; the first enables
to replace the original family by
1
nα Mn with a martingale Mn while the second to
avoid the direct Laplace transform analysis.
Key words: Moderate deviations, Poisson equation, Puhalskii theorem.
Mathematics Subject Classification (2000): 60F10, 60J27
1 Introduction and discussion
Let (Xn)n≥0 be a homogeneous ergodic Markov chain, Xn ∈Rd with the
transition probability kernel for n steps: P (n)
x
= P (n)(x, dy) (for brevity
P (1)
x
:= Px) and the unique invariant measure µ.
Let H be a measurable function Rd H
→Rp with

Rd |H(z)|µ(dz) < ∞and

190
B. Delyon, A. Juditsky and R. Liptser

Rd H(z)µ(dz) = 0.
(1.1)
Set
Sα
n = 1
nα
n

i=1
H(Xi−1), n ≥1; (0.5 < α < 1).
In this paper, we examine the moderate deviation principle (in short:
MDP) for the family (Sα
n)n≥1 when the spectrum of operator Px is continuous.
It is well known that for bounded H satisfying (1.1) ((H) - condition), the
most MDP compatible Markov chains are characterized by eigenvalues gap
condition (EG) (see Wu, [17], [18], Gong and Wu, [7], and citations therein):
the unit is an isolated, simple and the only eigenvalue with modulus 1
of the transition probability kernel Px.
In the framework of (H)-(EG) conditions, the MDP is valid with the rate of
speed n−(2α−1) and the rate function I(y), y ∈Rd
I(y) =

1
2∥y∥2
B⊕,
B⊕By = y
∞,
otherwise,
(1.2)
where B⊕is the pseudoinverse matrix (in Moore–Penrose sense, see e.g.[1])
for the matrix
B =

Rd H(x)H∗(x)µ(dx)
+

n≥1

Rd
)
H(x)(P (n)
x
H)∗+ (P (n)
x
H)H∗(x)

µ(dx)
(1.3)
(henceforth, ∗, | · |, and ∥· ∥Q are the transposition symbol, L1 norm and L2
norm with the kernel Q (∥x∥Q =

⟨x, Qx⟩) respectively).
Thanks to the quadratic form rate function, the MDP is an attractive tool
for an asymptotic analysis in many areas, say, with thesis
“MDP instead of CLT”
(see Section 7).
In this paper, we intend to apply the MDP analysis to Markov chain
defined by the recurrent equation
Xn = f(Xn−1, ξn), n ≥1
generated by i.i.d. sequence (ξn)n≥1 of random vectors, where f is some vector-
valued measurable function. Obviously, the function f and the distribution of
ξ1 might be specified in this way Px satisfies (EG). For instance, if d = 1 and
Xn = f(Xn−1) + ξn,

Moderate Deviation Principle
191
then for bounded f and Laplacian random variable ξ1 (EG) holds. However,
(EG) fails for many useful in applications ergodic Markov chains. For d = 1,
a typical example gives Gaussian Markov chain defined by a linear recurrent
equation governed by i.i.d. sequence of (0, 1)-Gaussian random variables(here
|a| < 1)
Xn = aXn−1 + ξn.
In order to clarify this remark, notice that if (EG) holds true, than for any
bounded and measurable function H, satisfying (H)-property, for some con-
stants K > 0, ̺ ∈(0, 1), n ≥1,
|ExH(Xn)| ≤K̺n.
(1.4)
However, the latter fails for H(x) = sign(x) satisfying (1.1). In fact, if (1.4)
were correct, then ∞
n=0 |ExH(Xn)| ≤
K
1−̺. On the other hand, it is readily
to compute that ∞
n=0 |ExH(Xn)| grows in |x| on the set {|x| > 1} faster
than O(log(|x|).
In this paper, we avoid a verification of (EG). Although our approach is
close to a conception of “Multiplicative Ergodicity” (see Balaji and Meyn
[2]) and “Geometrical Ergodicity” (see Kontoyiannis and Meyn, [8] and Meyn
and Tweedie, [11]), Chen and Guillin, [4]) we do not follow explicitly these
methodologies.
Our main tools are the Poisson equation and the Puhalskii theorem from
[15]. The Poisson equation enables to reduce the MDP verification for (Sα
n)n≥1
to ( 1
nα Mn)n≥1, where Mn is a martingale generated by Markov chain, while
the Puhalskii theorem allows to replace an asymptotic analysis for the Laplace
transform of
1
nα Mn by the asymptotic analysis for, so called, Stochastic Ex-
ponential
En(λ) =
n
(
i=1
E

exp
)D
λ, 1
nα (Mi −Mi−1)
EXi−1

, λ ∈Rd,
(1.5)
being the product of the conditional Laplace transforms for martingale incre-
ments.
An effectiveness of the Poisson equation approach (method of corrector)
combined with the stochastic exponential is well known from the proofs of
functional central limit theorem (FCLT) for the family (S0.5
n )n≥1 (see, e.g.
Papanicolaou, Stroock and Varadhan [12], Ethier and Kurtz [6], Bhattacharya
[3], Pardoux and Veretennikov [13]; related topics can be found in Metivier
and Priouret (80’s) for stochastic algorithms analysis. The use of the same
approach for a continuous time setting can be found e.g. in [9], [10]).
2 Formulation of main result
We consider Markov chain (Xn)n≥0, Xn ∈Rd, defined by a nonlinear recurrent
equation

192
B. Delyon, A. Juditsky and R. Liptser
Xn = f(Xn−1, ξn),
(2.1)
where f = f(z, v) is a vector function with entries f1(z, v), . . . , fd(z, v), u ∈
Rd, v ∈Rp and (ξn)n≥1 is i.i.d. sequence of random vectors of the size p.
We fix the following assumptions.
Assumption 2.1 Entries of f are Lipschitz continuous functions in the fol-
lowing sense: for any v
|fi(z1 . . . , zj−1, z′
j, zj+1 . . . , zd, v1, . . . , vp)
−fi(z1 . . . , zj−1, z′′
j , zj+1 . . . , zd, v1, . . . , vp)|
≤̺ij|z′
j −z′′
j |,
|f(z′, v) −f(z′′, v)| ≤̺|v′ −v′′|,
where
max
i,j ̺ij = ̺ < 1.
Assumption 2.2 For sufficiently small positive δ, Cramer’s condition holds:
Eeδ|ξ1| < ∞.
Theorem 2.1. Under Assumptions 2.1 and 2.2, the Markov chain is ergodic
with the invariant measure µ such that

Rd |z|µ(dz) < ∞. For any Lipschitz
continuous function H, satisfying (1.1), the family (Sα
n)n≥1 obeys the MDP
in the metric space (Rd, r) (r is the Euclidean metric) with the rate of speed
n−(2α−1) and the rate function given in (1.2).
Remark 1. Notice that:
- assumptions of Theorem 2.1 do not guarantee (EG),
- Lipschitz continuous H, obeying the linear growth condition, are permis-
sible for the MDP analysis,
- the ξ1-distribution with a continuous component is not required.
Consider now a linear version of (2.1):
Xn = AXn−1 + ξn,
where A is the d × d-matrix with entries Aij. Now, Assumption 2.1 reads as:
maxij |Aij| < 1. This assumption is too restrictive. We replace it by more
natural one
Assumption 2.3 The eigenvalues of A lie within the unit circle.

Moderate Deviation Principle
193
Theorem 2.2. Under Assumption 2.3, the Markov chain is ergodic with the
invariant measure µ such that

Rd ∥z∥2µ(dz) < ∞. For any Lipschitz con-
tinuous function H, satisfying (1.1), the family (Sα
n)n≥1 obeys the MDP in
the metric space (Rd, r) with the rate of speed n−(2α−1) and the rate function
given in (1.2).
3 Preliminaries
3.1 (EG)-(H) conditions
To clarify our approach to the MDP analysis, let us first demonstrate its
applicability under (EG)-(H) setting.
The (EG) condition provides the geometric ergodicity of P (n)
x
to the invari-
ant measure µ uniformly in x in the total variation norm: there exist constants
K > 0 and ̺ ∈(0, 1) such that for any x ∈Rd,
∥P (n)
x
−µ∥tv ≤K̺n, n ≥1.
The latter provides an existence of bounded function
U(x) = H(x) +

n≥1
P (n)
x
H
(3.1)
solving the Poisson equation
U(x) = H(x) + PxU.
(3.2)
In view of the Markov property, a sequence (ζi)i≥1 of bounded random vectors
with ζi := U(Xi) −PXi−1U forms a martingale-differences relative to the
filtration generated by Markov chain. Hence, Mn = n
i=1 ζi is the martingale
with bounded increments. With the help of Poisson’s equation we get the
following decomposition
1
nα
n

i=1
H(Xi−1) = 1
nα [U(x) −U(Xn)]
9
:;
<
corrector
+ 1
nα Mn.
(3.3)
The boundedness of U provides a corrector negligibility in the MDP scale,
that is, the families Sα
n and
1
nα Mn share the same MDP. In view of that,
suffice it to to establish the MDP for ( 1
nα Mn)n≥1.
Assume for a moment that ζi’s are i.i.d. sequence of random vectors. Recall,
Eζ1 = 0 and denote B = Eζ1ζ∗
1. Then, the Laplace transform for
1
nα Mn is:
En(λ) =

Ee⟨λ, ζ1
nα ⟩n
, λ ∈Rd.
(3.4)

194
B. Delyon, A. Juditsky and R. Liptser
Under this setting, it is well known that
1
nα Mn obeys the MDP if B is not
singular matrix and
lim
n→∞n2α−1 log En(λ) = 1
2⟨λ, Bλ⟩, λ ∈Rd.
We adapt this method of MDP verification to our setting. Instead of B, we
introduce matrices B(Xi−1), i ≥1 with
B(x) = PxUU ∗−PxU

PxU)∗.
(3.5)
The homogeneity of Markov chain and the definition of ζi provide a.s. that
E(ζiζ∗
i |Xi−1) = B(Xi−1).
Instead of the Laplace transform (3.4), we apply the stochastic exponential
(1.5), expressed via ζi’s,
En(λ) =
n
(
i=1
E

e⟨λ, ζi
nα ⟩Xi−1

, λ ∈R,
which is not the Laplace transform itself.
The Poisson equation (3.2) and its solution (3.1) permit to transform (3.5)
into
B(x) = H(x)H∗(x) +

n≥1
)
H(x)

P (n)
x
H
∗+

P (n)
x
H

H∗
,
that is,

Rd B(z)µ(dz) coincides with B from (1.3).
Now, we are in the position to formulate
Puhalskii Theorem. [for more details, see [15] and [16].] Assume B from
(1.3) is nonsingular matrix and for any ε > 0, λ ∈Rd
lim
n→∞
1
n2α−1 log P
n2α−1 log En(λ) −1
2⟨λ, Bλ⟩
 > ε

= −∞.
(3.6)
Then, the family
1
nα Mn, n ≥1 possesses the MDP in the metric space
(Rd, r) (r is the Euclidean metric) with the rate of speed n−(2α−1) and rate
function I(y) = 1
2∥y∥2
B−1.
Remark 2. The condition (3.6) is verifiable with the help of
lim
n→∞
1
n2α−1 log P
 1
n

n

i=1
D
λ,

B(Xi−1) −B

λ
E > ε

= −∞
lim
n→∞
1
n2α−1 log P

1
6n1+α
n

i=1
E
)
|ζi|3en−α|ζi|Xi−1

> ε

= −∞.
(3.7)

Moderate Deviation Principle
195
The second condition in (3.7) is implied by the boundedness of |ζi|’s. The first
part in (3.7) is known as Dembo’s conditions, [5], formulated as follows: for
any ε > 0, λ ∈Rd
lim
n→∞
1
n log P
 1
n

n

i=1
D
λ,

B(Xi−1) −B

λ
E > ε

< 0.
In order to verify the first condition in (3.7), we apply again the Poisson
equation technique. Set h(x) =
F
λ,

B(x) −B

λ
G
and notice that

Rd h(z)µ(dz) = 0.
Then, the function u(x) = h(x) + 
n≥1 P (n)
x
h is well defined and solves the
Poisson equation u(x) = h(x) + Pxu. Similarly to (3.3), we have
1
n
n

i=1
h(Xi−1) = u(x) −u(Xn)
n
+ mn
n ,
where mn = n
i=1 zi is the martingale with bounded martingale-differences
(zi)i≥1. Since u is bounded, the first condition in (3.7) is reduced to
lim
n→∞
1
n2α−1 log P

|mn| > nε

= −∞
(3.8)
while (3.8) is provided by Theorem A.1 in Appendix which states that (3.8)
holds for any martingale with bounded increments.
Singular B
The conditions from (3.7) remain to hold whether B is nonsingular or singular.
For singular B the Puhalskii theorem is no longer valid. With singular B, we
use the Puhalskii theorem as a helpful tool.
It is well known that the family Mn
nα , n ≥1 obeys the MDP with the rate
of speed n−(2α−1) and some rate function,say I(y) provided that
lim
C→∞lim
n→∞
1
n2α−1 log P
Mn
nα
 > C

= −∞
lim
ε→0 lim
n→∞
1
n2α−1 log P
Mn
nα −y
 ≤ε

≤−I(y)
lim
ε→0
lim
n→∞
1
n2α−1 log P
Mn
nα −y
 ≤ε

≥−I(y).
(3.9)
The first condition in (3.9) provides the exponential tightness in the metric r
while the next others the local MDP.

196
B. Delyon, A. Juditsky and R. Liptser
In order to verify of (3.9), we introduce “regularized” family M β
n
nα , n ≥1
with
M β
n = Mn +

β
n

i=1
ϑi,
where β is a positive parameter and (ϑi)i≥1 is a sequence of zero mean i.i.d.
Gaussian random vectors with cov(ϑ1, ϑ1) =: I (I is the unite matrix). The
Markov chain and (ϑi)i≥1 are assumed to be independent objects.
It is clear that for this setting the matrix B is transformed into a positive
definite matrix Bβ = B + βI. Now, the Puhalskii theorem is applicable and
guarantees the MDP with the same rate of speed and the rate function
Iβ(y) = 1
2∥y∥2
B−1
β .
We use now the well-known fact (see, e.g. Puhalskii, [14]) that MDP provides
the exponentially tightness and the the local MDP:
lim
C→∞lim
n→∞
1
n2α−1 log P
M β
n
nα
 > C

= −∞
lim
ε→0 lim
n→∞
1
n2α−1 log P
M β
n
nα −y
 ≤ε

≤−Iβ(y)
lim
ε→0
lim
n→∞
1
n2α−1 log P
M β
n
nα −y
 ≤ε

≥−Iβ(y).
(3.10)
Notice now that (3.9) is implied by (3.10) if
lim
β→0 Iβ(y) =

1
2∥y∥2
B⊕,
B⊕By = y
∞,
otherwise
(3.11)
and
lim
β→0 lim
n→∞
1
n2α−1 log P

√β
nα
n

i=1
ϑi
 > η

= −∞,
∀η > 0.
(3.12)
Let T be an orthogonal matrix transforming B to a diagonal form:
diag(B) = T ∗BT. Then, owing to
2Iβ(y) = y∗(βI + B)−1y = y∗T(βI + diag(B))−1T ∗y,
for y = B⊕By we have (recall that B⊕BB⊕= B⊕, see [1])
2Iβ(y) = y∗B⊕BT(βI + diag(B))−1T ∗y
= y∗B⊕TT ∗BT(βI + diag(B))−1T ∗y
= y∗B⊕T diag(B)(βI + diag(B))−1T ∗y
−−−→
β→0 y∗B⊕T diag(B) diag((B))⊕T ∗y
= y∗B⊕T diag(B)T ∗T(diag(B))⊕T ∗y
= y∗B⊕BB⊕u = u∗B⊕y = ∥y∥2
B⊕= 2I(y).

Moderate Deviation Principle
197
If y ̸= B⊕By, limβ→0 2Iβ(y) = ∞.
Thus, (3.11) holds true.
Since (ϑi)i≥1 is i.i.d. sequence of random vectors and entries of ϑ1 are i.i.d.
(0, 1)-Gaussian random variables, the verification of (3.12) is reduced to
lim
β→0 lim
n→∞
1
n2α−1 log P

n

i=1
ξi
 > nαη
√β

= −∞,
(3.13)
where (ξi)i≥1 is a sequence of i.i.d. (0, 1)-Gaussian random variables, and it
suffices to consider the case “+” only. By the Chernoffinequality with λ > 0,
we find that
P

n

i=1
ϑi > nαη
√β

≤exp

−λnαη
√β + nλ2
2

while the choice of λ =
nαη
n√
β provides
1
n2α−1 log P

n

i=1
ηi > nαη
√β

≤−η2
2β −−−→
β→0 −∞.
3.2 Virtual scenario
- (EG)-(H) are not assumed
- the ergodicity of Markov chain is checked
- H is chosen to hold (1.1).
(1) Let (3.1) hold. Hence, the function U solves the Poisson equation and the
decomposition from (3.3) is valid with Mn = n
i=1 ζi, where
ζi = u(Xi) −PXi−1u.
Let
Eζ∗
i ζi ≤const.
E
)
|ζi|3en−α|ζi|Xi−1

≤const.
(2) With B(x) and B are defined in (3.5) and (1.3) respectively, set
h(x) =
D
λ,

B(x) −B

λ
E
, λ ∈Rd.
Let
(i) u(x) = h(x) + 
n≥1 P (n)
x
h is well defined
(ii) for zi = u(Xi) −PXi−1u,
Ez2
i ≤const.
E
)
|zi|3en−α|zi|Xi−1

≤const.

198
B. Delyon, A. Juditsky and R. Liptser
(3) For any ε > 0, let
lim
n→∞
1
n2α−1 log P

|U(Xn)| > nαε

= −∞
lim
n→∞
1
n2α−1 log P

|u(Xn)| > nαε

= −∞.
Notice that (EG)-(H) provide (1)-(3) and even if (EG)-(H) fail, (1)-(3)
may fulfill. Moreover, (1)-(3) guarantee the validity for all steps of the proof
given in Section 3.1.
Thus, an ergodic Markov chain, possessing (1)-(3), obeys the MDP.
The proof of Theorems 2.1 and 2.2 follows this scenario.
4 The proof of Theorem 2.1
4.1 Ergodic property
Lemma 4.1. Under Assumption 2.1, (Xn)n≥0 possesses the unique probabil-
ity invariant measure µ with

Rd |z|µ(dz) < ∞.
Proof. Let ν be a probability measure on Rd with

Rd |x|ν(dx) < ∞and
let a random vector X0, distributed in the accordance to ν, is independent
of (ξn)n≥1. We initialize the recursion, given in (2.1), by X0. Let now Xn is
generated by (2.1). Then, µn(dz) =

Rd P (n)
x
(dz)ν(dx) defines the distribution
of Xn.
We show that the family (µn)n≥1 is tight in the Levy–Prohorov metric:
lim
k→∞lim
n→∞µn(|z| > k) = 0.
By the Chebyshev inequality, µn(|z| > k) ≤E|Xn|
k
. The tightness follows from
supn≥1 E|Xn| < ∞. Further, since by Assumption 2.1,
|Xn| = |f(0, ξn) + (f(Xn−1, ξn) −f(0, ξn))|
≤|f(0, ξn)| + |f(Xn−1, ξn) −f(0, ξn))|
≤|f(0, ξn)| + ̺|Xn−1|
≤|f(0, 0)| + ℓ|ξn| + ̺|Xn−1|,
the sequence (E|Xn|)n≥1 solves a recurrent inequality
E|Xn| ≤|f(0, 0)| + ℓE|ξ1| + ̺E|Xn−1|
subject to E|X0| =

Rd |x|ν(dx)(< ∞). Hence, we find that for any n ≥1,
E|Xn| ≤E|X0| + |f(0, 0)| + ℓE|ξ1|
1 −̺
.

Moderate Deviation Principle
199
Thus, the family {µn} is tight, so that, by the Prohorov theorem, {µn}
contains further subsequence {µn′} converging, as n′ ր ∞, in the Levy–
Prohorov metric to a limit µ being a probability measure on Rd: for any
bounded and continuous function g on Rd
lim
n′→∞

Rd g(z)µn′(dz) =

Rd g(z)µ(dz).
Thence, for g(z) = L ∧|z| and L > 0, it holds

Rd(L ∧|z|)µ(dz) = lim
n′→∞E(L ∧|Xn′|) ≤lim
n→∞E|Xn| < ∞
and, by the monotone convergence theorem,

Rd |z|µ(dz) ≤lim
n→∞E|Xn| < ∞.
The µ is regarded now as a candidate to be the unique invariant measure. So,
we shall verify

Rd g(x)µ(dx) =

Rd Pxgµ(dx).
for any nonnegative, bounded and continuous function g. For notational con-
venience, write Xx
n and Xν
n, if X0 = x and X0 is distributed in the accordance
with ν. By Assumption 2.1,
|Xx
n −Xν
n| ≤̺|Xx
n−1 −Xν
n−1|, n ≥1,
that is, |Xx
n −Xν
n| converges to zero exponentially fast as long as n →∞. For
any x ∈Rd, the latter provides limn′→∞Eg(Xx
n′) =

Rd g(x)µ(dx). Since the
Markov chain is homogeneous, we also find that
lim
n′→∞Eg(Xx
n′+1) =

Rd g(z)µ(dz).
On the other hand, owing to Eg(Xx
n′+1) = EPXx
n′g, the above relation is
nothing but
lim
n′→∞EPXx
n′g =

Rd g(z)µ(dz).
Finally, owing to Pxg = Eg(f(x, ξ1)), the function Pxg of argument x is
bounded and continuous. Consequently,
lim
n′→∞EPXx
n′g =

Rd Pxgµ(dx).
Assume µ′ is another invariant probability measure, µ′ ̸= µ. Then, taking
Xµ
0 and Xµ′
0 , distributed in the accordance to µ and µ′ respectively and in-
dependent of (ξn)n≥1, we get two stationary Markov chains (Xµ
n) and (Xµ′
n )
defined on the same probability space as:

200
B. Delyon, A. Juditsky and R. Liptser
Xµ
n = f(Xµ
n−1, ξn)
Xµ′
n = f(Xµ′
n−1, ξn).
By Assumption 2.1, |Xµ
n −Xµ′
n | ≤̺|Xµ
n−1 −Xµ′
n−1|, i.e. lim
n→∞|Xµ
n −Xµ′
n | = 0.
Recall that both processes Xµ
n and Xµ′
n
are stationary with the marginal
distributions µ and µ′ respectively. Hence, for any bounded and continuous
function g : Rd →R,


Rd g(x)µ(dx) −

Rd g(x)µ′(dx)
 ≤E|g(Xµ
n) −g(Xµ′
n )| −−−−→
n→∞0,
that is, µ = µ′.
4.2 The verification of (1)
Let K be the Lipschitz constant for H. Then |H(x)| ≤|H(0)| + K|x| and

Rd |H(z)|µ(dz) < ∞. By (1.1), EH(Xµ
n) ≡0. Then,
|EH(Xx
n)| = |E(H(Xx
n) −H(Xµ
n)|
≤K̺nE|x −Xµ
n| ≤K(1 + |x|)̺n.
Therefore, 
n≥1 |EH(Xx
n| ≤
K
1−̺(1 + |x|). Consequently, the function U(x),
given in (3.1), is well defined and solves the Poisson equation.
Recall that ζi = U(Xi) −PXi−1U.
Lemma 4.2. The function U(x) possesses the following properties:
1) U(x) is Lipschitz continuous;
2) Px(UU ∗) −PxU(PxU)∗is bounded and Lipschitz continuous;
3) For sufficiently small δ > 0 and any i ≥1
E
U(Xi) −PXi−1U
3e
δ|U(Xi)−PXi−1 U|Xi−1

≤const.
Proof. 1) Since by Assumption 2.1,
|Xx′
n −Xx′′
n | ≤̺|Xx′
n−1 −Xx′′
n−1|,
|Xx′
0 −Xx′′
0 | ≤|x′ −x′′|,
we have
|U(x′) −U(x′′)| ≤|H(x′) −H(x′′)| +

n≥1
E|H(Xx′
n ) −H(Xx′′
n )|
≤
K
1 −̺|x′ −x′′|.
(4.1)
2) Recall (see (3.5))

Moderate Deviation Principle
201
Px(UU ∗) −PxU(PxU)∗= B(x)
and denote Bpq(x), p, q = 1, . . . , d, the entries of matrix B(x). Also, denote
by Up(x), p = 1, . . . , d, the entries of U(x). Since B(x) is nonnegative definite
matrix, it is sufficient to show only that Bpp(x)’s are bounded functions.
Denote F(z) the distribution function of ξ1. Taking into the consideration
(4.1) and Assumption 2.1, we get
Bpp(x) = E

Up

f(x, ξ1)

−

Rd Up

f(x, z)

dF(z)
2
≤
(Kℓ)2
(1 −̺)2 E


Rd |ξ1 −z|dF(z)

2
≤4 (Kℓ)2
(1 −̺)2 E|ξ1|2 < ∞.
The Lipschitz continuity of Bpq(x) is proved similarly. Write
Bpq(x′) −Bpq(x′′) =: ab −cd,
where
a = E

Up

f(x′, ξ1)

−

Rd Uq

f(x′, z)

dF(z)

b = E

Uq

f(x′, ξ1)

−

Rd Uq

f(x′, z)dF(z)

c = E

Up

f(x′′, ξ1)

−

Rd Uq

f(x′′, z)

dF(z)

d = E

Uq

f(x′′, ξ1)

−

Rd Uq

f(x′′, z)

dF(z)

.
Now, applying ab −cd = a(b −d) + d(a −c) and taking into account (4.1) and
Assumption 2.1, we find that |a|, |d| ≤2Kℓ
1−̺E|ξ1| and so
|Bpq(x′) −Bpq(x′′)| ≤4K2ℓ̺
(1 −̺)2 E|ξ1||x′ −x′′|.
3) By (4.1) and Assumption 2.1
|U(Xi) −PXi−1U| ≤
Kℓ
1 −̺

E|ξ1| + |ξi|

.
4.3 The verification of (2)
The properties of B(x) to be bounded and Lipschitz continuous provide the
same properties for
h(x) =
F
λ,

B(x) −B

λ
G
.
Hence (2) is provided by (1).

202
B. Delyon, A. Juditsky and R. Liptser
4.4 The verification of (3)
Since U and u are Lipschitz continuous, they possess the linear growth condi-
tion, e.g., |U(x)| ≤C(1 + |x|), ∃C > 0. So, (3) is reduced to the verification
of
lim
n→∞
1
n2α−1 log P
Xn
 > εnα
= −∞, ε > 0.
(4.2)
Due to Assumption 2.1, we have
|Xn| ≤|f(Xn−1, ξn)| ≤|f(0, ξn)| + ̺|Xn−1|
≤|f(0, 0)| + ̺|Xn−1| + ℓ|ξn|.
Iterating this inequality with X0 = x we obtain
|Xn| ≤̺n|x| + |f(0, 0)|
n

j=1
̺n−j + ℓ
n

j=1
̺n−j|ξj|
≤|x| + |f(0, 0)|
1 −̺
+ ℓ
n−1

j=0
̺j|ξn−j|.
Hence, (4.2) is reduced to
lim
n→∞
1
n2α−1 log P
 n−1

j=0
̺j|ξn−j| ≥nαε

= −∞.
(4.3)
We verify (4.3) with the help of Chernoff’s inequality: with δ, involving in
Assumption 2.2, and γ =
δ
1−̺
P
 n−1

j=0
̺j|ξn−j| ≥nαε

≤e−nαγεEe
n−1
j=0 γ̺j|ξn−j|.
The i.i.d. property for ξj’s provides
Ee
n−1
j=0 γ̺j|ξn−j| = Ee
n−1
j=0 γ̺j|ξ1| ≤Ee
∞
j=0 γ̺j|ξ1| = Eeδ|ξ1| < ∞
and we get
1
n2α−1 log P
 n−1

j=0
̺j|ξn−j| ≥nαε

≤−n1−αδε + log Eeδ|ξ1|
n2α−1
−−−−→
n→∞−∞.
5 The proof of Theorem 2.2
The proof of this theorem differs from the proof of Theorem 2.1 only in some
details concerning to (L.1). So, only these parts of the proof are given below.

Moderate Deviation Principle
203
5.1 Ergodic property and invariant measure
Introduce (*ξn)n≥1 the independent copy of (ξn)n≥1. Owing to
Xn = Anx +
n

i=1
An−iξi = Anx +
n−1

i=0
Aiξn−i,
we introduce
*
Xn = Anx +
n−1

i=0
Ai*ξi
(5.1)
and notice that the i.i.d. property of (ξi)i≥1 provides (Xn)n≥0
law
= ( *
Xn)n≥0.
By Assumption 2.3, An →0, n →∞, exponentially fast. Particularly,
∞

i=0
trace

Ai cov(ξ1, ξ1)(Ai)∗
< ∞,
so that lim
n→∞
*
Xn = ∞
i=0 Ai*ξi a.s. and in L2 norm.
Thus, the invariant measure µ is generated by the distribution function of
*
X∞. In addition, E∥*
X∞∥2 =
∞

i=0
trace

Ai cov(ξ1, ξ1)(Ai)∗
, so that

Rd ∥z∥2µ(dz) < ∞.
5.2 The verification of (1) and (2)
Due to the relation
(Xx′
n −Xx′′
n ) = A(Xx′
n−1 −Xx′′
n−1),
we have (Xx′
n −Xx′′
n ) = An(x′ −x′′). Let us transform the matrix A into a
Jordan form A = TJT −1 and notice that An = TJnT −1. It is well known
that the maximal absolute value of entries of Jn is n|λ|n, where |λ| is the
maximal absolute value among eigenvalues of A. By Assumption 2.3, |λ| < 1.
So, there exist K > 0 and ̺ < 1 such that |λ| < ̺. Then, entries An
pq of An
are evaluated as: |An
pq| ≤K̺n. Hence, |Xx′
n −Xx′′
n | ≤K̺n|x′ −x′′|, n ≥1,
and the verification of (1), (2) is in the framework of Section 3.
5.3 The verification of (3)
As in Section 3, the verification of this property is reduced to
lim
n→∞
1
n2α−1 log P
Xn
 > εnα
= −∞, ε > 0.
(5.2)

204
B. Delyon, A. Juditsky and R. Liptser
In (5.2), we may replace Xn by its copy *
Xn defined in (5.1). Notice also that
| *
Xn| ≤|Anx| +
∞

i=0
max
pq |Ai
pq||*ξ|.
As was mentioned above, |Ai
pq| ≤K̺j for some K > 0 and ̺ ∈(0, 1). Hence,
suffice it to verify
lim
n→∞
1
n2α−1 log P
 ∞

i=0
̺i|ξi| > εnα
= −∞, ε > 0
what be going on similarly to corresponding part of the proof in Section 3.
6 Exotic example
Let (Xn)n≥0, Xn ∈R and X0 = x, be Markov chain defined by the recurrent
equation
Xn = Xn−1 −m Xn−1
|Xn−1| + ξn,
(6.1)
where m is a positive parameter, (ξn) is i.i.d. sequence of zero mean random
variables with
Eeδ|ξ1| < ∞, for some δ > 0,
and let 0
0 = 0.
Although the virtual scenario is not completely verifiable here we show
that for
H(x) = x
|x|
the family (Sα
n)n≥1 possesses the MDP provided that
m > 1
δ log Eeδ|ξ1|.
(6.2)
Indeed, by (6.1) we have
1
nα
n

k=1
Xk−1
|Xk−1| = 1
m
(Xn −x)
nα
+ 1
nα
n

k=1
ξk
m.
The family
 1
nα
n
k=1
ξk
m

n≥1 possesses the MDP with the rate of speed n−(2α−1)
and the rate function I(y) =
m2
2Eξ2
1 y2. Then, the family (Sα
n)n≥1 obeys the
same MDP provided that
 Xn−x
nα

n≥1 is exponentially negligible family with
the rate n−(2α−1). This verification is reduced to

Moderate Deviation Principle
205
lim
n→∞
1
n2α−1 log P

|Xn| > nαε

= −∞, ε > 0.
(6.3)
By the Chernoffinequality P

|Xn| > nαε

≤e−δnαεEeδ|Xn|, that is (6.3)
holds if sup
n≥1
Eeδ|Xn| < ∞for some δ > 0. We show that the latter holds true
for δ involved in (6.2). A helpful tool for this verification is the inequality
z −m z
|z|
 ≤
|z| −m
. Write
Eeδ|Xn| = Eeδ|Xn|I(|Xn−1| ≤m) + Eeδ|Xn|I(|Xn−1| > m)
≤eδmEeδ|ξ1| + e−δmEeδ|ξ1|Eeδ|Xn−1|.
Set ℓ= eδmEeδ|ξ1| and ̺ = e−δmEeδ|ξ1|. By (6.2), ̺ < 1. Hence, V (x) = eδ|x|
is the Lyapunov function: PxV ≤̺V (x) + ℓ. Consequently,
EV (Xn) ≤̺EV (Xn) + ℓ, n ≥1
and so, supn≥1 EV (Xn) ≤V (x) +
ℓ
1−̺.
7 Statistical example
An asymptotic analysis, given in this section, demonstrate the thesis “MDP
instead of CLT”.
Let
Xn = θf(Xn−1) + ξn,
where θ is a number and (ξn)n≥1 is i.i.d. sequence of of (0, 1)-Gaussian random
variables. We assume that |θ| < 1 and f is bounded continuously differentiable
function with |f ′(x)| ≤1. By Theorem 2.1, (Xn) is an ergodic Markov chain
and its invariant measure µθ depends on parameter θ. Since ξ1 is Gaussian
random variables, µθ, being a convolution of some measure with Gaussian
one, possesses a density relative to dz. Then, assuming f 2(x) > 0 relative
to Lebesgue measure, we have Bθ =

R f 2(z)µ(dz) > 0. Under the above
assumptions,
θn =
n
i=1 f(Xi−1)Xi
n
i=1 f 2(Xi−1)
is a strongly consistent estimate of θ by sampling {X1, . . . , Xn}, that is,
limn→∞θn = θ a.s. Moreover, it is known its asymptotic in the CLT scale:
√n(θ −θn)
law
−−−−→
n→∞

0, 1
Bθ

-Gaussian r. v.
Here, we give an asymptotic of θn in the MDP scale: for any α ∈
 1
2, 1

,
n1−α(θ −θn)
MDP
−−−−→
n→∞

1
n2α−1 , y2
2Bθ

.

206
B. Delyon, A. Juditsky and R. Liptser
Theorem 7.1. The family n1−α(θ−θn) obeys the MDP with the rate of speed
1
n2α−1 and the rate function I(y) =
y2
2Bθ .
Proof. The use of
n1−α(θ −θn) =
1
nα
n
i=1 f(Xi−1)ξi
1
n
n
i=1 f 2(Xi−1)
and the law of large numbers, P- limn→∞1
n
n
i=1 f 2(Xi−1) = Bθ, give a hint
that that the theorem statement is valid provided that
(i) for Mn = 
i=1 f(Xi−1)ξi, the family
 1
nα Mn

n→∞obeys the MDP
with the rate of speed
1
n2α−1 and the rate function I(y) =
y2
2B−1
θ ;
(ii) for any ε > 0,
lim
n→∞
1
n2α−1 log P
 1
n
n

i=1
)
f 2(Xi−1) −Bθ
 ≥ε

= −∞.
Following to (1.5) and taking into account the setting, we notice that
En(λ) = exp

n

i=1
λ2
2n2α f 2(Xi−1)

.
is the stochastic exponential related to
 1
nα Mn

n→∞. Consequently, (3.6) is
reduced to (ii), that is, only (ii) is left to be verified.
The verification of (ii) is in the framework of Theorem (2.1). The function
H(x) = f 2(x)−Bθ satisfies the assumptions of Theorem 2.1. Hence, the family
 1
nα
n
i=k H(Xk1)

n→∞obeys the MDP with the rate of speed
1
n2α−1 and the
rate function
J(y) =

y2
2 B⊕
θ
Bθ > 0,
∞
, Bθ = 0, y ̸= 0,
where, in accordance with (1.3),
Bθ =

R
H2(x)µθ(dx) + 2

n≥1

R
H(x)P (n)
x
Hµθ(dx).
In particular,
lim
n→∞
1
n2α−1 log P
 1
nα
n

k=1
H(Xk−1)
 ≥Cε

≤

−
1
2
Bθ C2ε2,
Bθ > 0
−∞,
otherwise.
Hence, for any C > 0, we find that

Moderate Deviation Principle
207
lim
n→∞
1
n2α−1 log P
 1
n
n

k=1
H(Xk−1)
 ≥ε

= lim
n→∞
1
n2α−1 log P
 1
nα
n

k=1
H(Xk−1)
 ≥n1−αε

≤lim
n→∞
1
n2α−1 log P
 1
nα
n

k=1
H(Xk−1)
 ≥Cε

≤

−C2ε2
2
Bθ
Bθ > 0,
−∞
otherwise
−−−−→
C→∞−∞.
A Exponentially integrable martingale-differences
Let ζn = (ζn)n≥1 be a martingale-difference with respect to some filtration
F = (Fn)n≥0 and Mn =
n
i=1
ζi be the corresponding martingale.
Theorem A.1. Assume that for sufficiently small positive δ and any i ≥1
E

eδ|ζi||Fi−1

≤const.
(A.1)
Then for any α ∈(0.5, 1)
lim
n→∞log
1
n2α−1 P

|Mn| > nε

= −∞.
Proof. Suffice it to prove lim
n→∞
1
n2α−1 log P

± M ′
n > nε

= −∞. We verify
here only “+” only (the proof of “-” is similar).
For fixed positive λ and sufficiently large n, let us introduce the stochastic
exponential
En(λ) =
n
(
i=1
E

eλ ζi
n Fi−1

.
A direct verification shows that
E exp
λMn
n
−log En(λ)

= 1.
We apply this equality for further ones
1 ≥EI

Mn > nε

exp
λMn
n
−log En(λ)

≥EI

Mn > nε

exp

λε −log En(λ)

.
(A.2)
Due to E

λ ζi
n |Fi−1

= 0 and (A.1), we find that

208
B. Delyon, A. Juditsky and R. Liptser
log En(λ) =
n

i=1
log

1 + E

eλ ζi
n −1 −λζi
n |Fi−1

≤
n

i=1
/ λ2
2n2 E

(ζi)2|Xi−1

+ λ3
6n3 E

|ζi|3eλ |ζi|
n |Fi−1
0
≤K
) λ2
2n + λ3
6n2

,
where K is some constant. This inequality, being incorporated into (A.2),
provides
1 ≥EI

Mn > nε

exp

λε −K
) λ2
2n + λ3
6n2

.
If ε < 3, taking λ = εnK−1, we find that
1
n2α−1 log P

Mn > nε

≤−ε2n2(1−α)
K
1
2 −ε
6

−−−−→
n→∞−∞.
Thus, the desired statement holds true.
Acknowledgments
The authors gratefully acknowledge the anonymous referee whose comments
and advice allowed us to improve the paper presentation.
References
1. Albert, A.: Regression and the Moore–Penrose Pseudoinverse. Academic Press,
New York and London (1972)
2. Balaji, S., Meyn, S. P.: Multiplicative ergodicity and large deviations for an
irreducible Markov chain. Stochastic Processes and their Applications, 90, 123–
144 (2000)
3. Bhattacharya, R.N.: On the functional central limit theorem and the law of the
iterated logarithm for Markov processes. Z. Wharsch. verw. Geb., 60, 185–201
(1992)
4. Chen, Xia, Guillin, A.: The functional moderate deviations for Harris recur-
rent Markov chains and applications. Annales de l’Institut Henri Poincar`e (B)
Probabilit`es et Statistiques, 40, 89–124 (2004)
5. Dembo, A.: Moderate deviations for martingales with bounded jumps, Elect.
Comm. in Probab., 1, 11–17 (1996)
6. Ethier, S. N., Kurtz, T. G.: Markov Processes. Characterization and Conver-
gence. Wiley Series in Probability and Mathematical Statistics, John Wiley &
Sons, New York et al. (1986)
7. Gong, F., Wu, L.: Spectral gap of positive operators and applications, C. R.
Acad. Sci., S´er. I, Math., 331 (12), 983–988 (2000)

Moderate Deviation Principle
209
8. Kontoyiannis, I., Meyn, S.P.: Spectral theory and timit theorems for geometri-
cally grgodic Markov Processes. Article math.PR/0209200 (2002)
9. Liptser, R.S., Spokoiny, V.: Moderate deviations type evaluation for integral
functionals of diffusion processes, EJP, 4, Paper 17 (1999)
(http://www.math.washington.edu/ ejpecp/)
10. Liptser, R., Spokoiny, V., Veretennikov, A.Yu.: Freidlin–Wentzell type large
deviations for smooth processes. Markov Process and Relat. Fields, 8, 611–636
(2002)
11. Meyn, S.P., Tweedie, R.L.: Markov Chains and Stochastic Stability. Springer-
Verlag (1993)
12. Papanicolaou, C.C., Stroock, D.W., Varahan, S.R.S.: Martingale approach to
some limit theorems. in: Conference on Statistical Mechanics, Dinamical Sys-
tems and Turbulence, M. Reed ed., Duke Univ. Math. Series, 3 (1977)
13. Pardoux, E., Veretennikov, A.Yu.: On Poisson equation and diffusion approxi-
mation, 1. Ann. Prob., 29 (3), 1061–1085 (2001)
14. Puhalskii, A.A.: On functional principle of large deviations. New trends in Prob-
ability and Statistics., Vilnius, Lithuania, VSP/Mokslas, 198–218 (1991)
15. Puhalskii, A.A.: The method of stochastic exponentials for large deviations.
Stochast. Proc. Appl., 54, 45–70 (1994)
16. Puhalskii, A. Large Deviations and Idempotent Probability. Chapman &
Hall/CRC Press, (2001)
17. Wu, L.: Moderate deviations of dependent random variables related to CLT and
LIL. Pr´epublication N. 118, Lab. de Probabilit´e de l’Universit´e Paris VI. (1992)
18. Wu, L.: Moderate deviations of dependent random variables related to CLT.
Annals of Probability, 23 (1), 420–445 (1995)


Remarks on Risk Neutral and Risk Sensitive
Portfolio Optimization
Giovanni B. DI MASI1 and `Lukasz STETTNER2 ∗
1 Universit`a di Padova Dipartimento di Matematica Pura ed Applicata Via
Belzoni 7, 35131 Padova and CNR-ISIB, Italy.
dimasi@math.unipd.it
2 Institute of Mathematics Polish Academy of Sciences Sniadeckich 8, 00-956
Warsaw, Poland.
L.Stettner@impan.gov.pl
Summary. In this note it is shown that risk neutral optimal portfolio strategy is
nearly optimal for risk sensitive portfolio cost functional with negative risk factor
that is close to zero.
Key words: risk sensitive control, discrete-time Markov processes, splitting, Pois-
son equation, Bellman equation
Mathematics Subject Classification (2000): 93E20; 60J05, 93C55
1 Introduction
We consider a market with m risky assets. Denote by Si(t) the price of the
i-th asset at time t. We shall assume that the prices of assets depend on k
economic factors xi(n), i = 1, . . . , k, with values changing at discrete times
n = 0, 1, . . . , so that for t ∈[n, n + 1) the prices satisfy the equation
dSi(t)
Si(t) = ai(x(n))dt +
k+m

j=1
σij(x(n))dwj(t),
(1.1)
where (w(t) = (w1(t), w2(t), . . . , wk+m(t)) is a (k + m)-dimensional Brownian
motion defined on a given probability space (Ω, (Ft), F, P). The economic
factors x(n) = (x1(n), . . . , xk(n)) evolve according to the equation
∗The research was supported by the MNiI grant 1 P03A 013 28

212
G.B. Di Masi and ^L. Stettner
xi(n + 1) = xi(n) + bi(x(n)) +
k+m

j=1
dij(x(n))[wj(n + 1) −wj(n)]
= g(x(n), W(n)),
(1.2)
where W(n) := (w1(n + 1) −w1(n), . . . , wk+m(n + 1) −wk+m(n)).
We assume that a, b are bounded and continuous vector functions, and
σ, d are bounded and continuous matrix functions of suitable dimensions.
Additionally we shall assume that the matrix ddT (T stands for transpose) is
nondegenerate. Notice that equation (1.2) corresponds to the discretization
of a diffusion process. The set of factors may include dividend yields, price-
earning ratios, short term interest rates, the rate of inflation see e.g. [1]. The
dynamics of such factors is usually modelled using diffusions, frequently linear
as in the case when a is a function of a spot interest rate governed by the
Vasicek process (see [1]). Our assumptions concerning boundedness of the
vector functions a and b may be relaxed allowing linear growth. However in
this case we need more complicated assumptions to obtain analogs of Lemmas
3.2, 3.3 and Corollary 3.1 which are important in the proof of Proposition 3.1.
Assume that starting with an initial capital V (0) we invest in the
given assets. Let hi(n) be the part of the wealth process located in the
i-th asset at time n, which is assumed to be nonnegative. The choice of
hi(n) depends on our observation of the asset prices and economic fac-
tors up to time n. Denoting by V (n) the wealth process at time n and by
h(n) = (h1(n), . . . , hm(n)) our investment strategy at time n, we have that
h(n) ∈U = {(h1, . . . , hm), hi ≥0, m
i=1 hi = 1} and
V (n + 1)
V (n)
=
m

i=1
hi(n)ξi(x(n), W(n)),
(1.3)
where
ξi(x(n), W(n)) = exp

ai(x(n)) −1
2
k+m

j=1
σ2
ij(x(n))
+
k+m

j=1
σij(x(n))[wj(n + 1) −wj(n)]

.
We are interested in the following investment problems:
maximize the risk neutral cost functional
J0
x({h(n)}) = lim inf
n→∞
1
nEx [ln V (n)]
(1.4)
and maximize the risk sensitive cost functional
Jγ
x ({h(n)}) = 1
γ lim sup
n→∞
1
n ln Ex [V (n)γ]
(1.5)

Remarks on Risk Neutral and Risk Sensitive Portfolio Optimization
213
with γ < 0. Using (1.3) we can rewrite the cost functional (1.4) as
J0
x({h(n)}) = lim inf
n→∞
1
nEx
Bn−1

t=0
ln
	 m

i=1
hi(t)ξi(x(t), W(t))

C
= lim inf
n→∞
1
nEx
Bn−1

t=0
c(x(t), h(t))
C
,
(1.6)
with c(x, h) = E {ln (m
i=1 hiξi(x, W(0)))}. It is clear that risk neutral cost
functional J0 depends on the uncontrolled Markov process (x(n)) and we prac-
tically maximize the cost function c itself. Consequently an optimal control
is of the form (ˆu(x(n))), where suph c(x, h) = c(x, ˆu(x)) and the Borel mea-
surable function ˆu : Rk →U exists by continuity of c for fixed x ∈Rk. This
control does not depend on asset prices and is a time independent function of
current values of the factors x only. The Bellman equation corresponding to
the risk neutral control problem is of the form
w(x) + λ = sup
h
[c(x, h) + Pw(x)]
(1.7)
where Pf(x) := Ex {f(x(1))} for f ∈bB(Rk) - the space of bounded Borel
measurable functions on Rk, is a transition operator corresponding to (x(n)).
In Section 2 we shall show that there are solutions w and λ to the equation
(1.7) and λ is the optimal value of the cost functional J0.
Letting
ζh,γ
n (ω) :=
n−1
(
t=0
exp
	
γ ln
	 m

i=1
hi(t)ξi(x(t), W(t))


	
E
B
exp
	
γ ln
	 m

i=1
hi(t)ξi(x(t), W(t))


|Ft−1
C
−1
consider a probability measure P h,γ defined by its restrictions P h,γ
|n
to the
first n times, given by the formula
P h,γ
|n (dω) = ζh,γ
n (ω)P|n(dω).
Then the cost functional (1.5) can be rewritten as
Jγ
x ({h(n)}) = 1
γ lim sup
n→∞
1
n ln Ex
B
exp
	
γ
n−1

t=0
ln
	 m

i=1
hi(t)ξi(x(t), W(t))


C
= 1
γ lim sup
n→∞
1
n ln Eh,γ
x
B
exp
	n−1

t=0
cγ(x(t), h(t))

C
,
(1.8)
with

214
G.B. Di Masi and ^L. Stettner
cγ(x, h) := ln
	
E
B	 m

i=1
hiξi(x, W(0))

γC
.
(1.9)
The risk sensitive Bellman equation corresponding to the cost functional Jγ
is of the form
ewγ(x) = inf
h

e(cγ(x,h)−λγ)

E
ewγ(y)P h,γ(x, dy)

.
(1.10)
where for f ∈bB(Rk)
P h,γf(x) = E
B	 m

i=1
hiξi(x, W(0))

γ
exp (−cγ(x, h)) f (g(x, W(0)))
C
,
(1.11)
with g as in (1.2) and where 1
γ λγ is the optimal value of the cost functional
(1.8). Notice that under measure P h,γ the process (x(n)) is still Markov but
with controlled transition operator P h,γ(x, dy). Following [6] we shall show
that
1
γ λγ →λ
(1.12)
whenever γ ↑0.
In what follows we distinguish two special classes of controls (hn): Markov
controls UM = {(h(n)) : h(n) = un(x(n))}, where un : Rk →U is a sequence
of Borel functions, and stationary controls Us = {(hn) : h(n) = u(x(n))},
where u : Rk →U is a Borel function. We shall denote by B(Rk) the set of
Borel subsets of Rk and by P(Rk) the set of probability measures on Rk.
The study of risk sensitive portfolio optimization has been originated in [1]
and then continued in a number of papers, in particular, in [16]. Risk sensitive
cost functional was studied in papers [13], [6], [7], [3], [4], [12], [2], [8] and
references therein. In this paper using techniques based on the splitting of
Markov processes (see [15]) we study the Poisson equation for additive cost
functional, the solution of which is also a solution to the risk neutral Bellman
equation. We then consider the problem of risk sensitive portfolio optimization
with risk factor close to 0. We generalize the result of [16], where uniform
ergodicity of factors was required and using [8] we show the existence of the
solution to the Bellman equation for small risk in a more general ergodic case.
The proof that a nearly optimal continuous risk neutral control function is
also nearly optimal for risk sensitive cost functional with risk factor close to 0
is based on a modification of the arguments in [6] using some results from the
theory of large deviations.
2 Risk neutral Bellman equation
By the nondegeneracy of the matrix ddT there exists a compact set C ⊂Rk,
for which we can find a closed ball in Rk, β > 0 and ν ∈P(Rk) such that

Remarks on Risk Neutral and Risk Sensitive Portfolio Optimization
215
ν(C) = 1 and ∀A∈B(Rk)
inf
x∈C P(x, A) ≥βν(A).
(2.1)
We fix a compact set C, β > 0 and ν ∈P(Rk) satisfying the above minoriza-
tion property. Additionally assume that the set C is ergodic, i.e.
∀x∈Rk Ex {τC} < ∞
and
sup
x∈C
Ex {τC} < ∞,
where τC = inf {i > 0 : xi ∈C}.
Consider a splitting of the Markov process (x(n)) (see [15]).
Let ˆ
Rk =
1
C × {0} ∪C × {1} ∪(Rk \ C) × {0}
2
and ˆx(n) = (x1(n), x2(n))
be a Markov process defined on ˆ
Rk such that
(i) when (x1(n), x2(n))
∈
C × {0}, x1(n) moves to y accordingly to
(1 −β)−1(P(x1(n), dy) −βν(dy)) and whenever y ∈C, x2(n) is changed
into x2(n + 1) = βn+1, where βn is i.i.d.
P {βn = 0} = 1 −β,
P {βn = 1} = β,
(ii) when (x1(n), x2(n)) ∈C × {1}, x1(n) moves to y accordingly to ν and
x2(n + 1) = βn+1,
(iii) when (x1(n), x2(n)) ∈Rk \ C × {0}, x1(n) moves to y accordingly to
P(x1(n), dy) and whenever y ∈C, x2(n) is changed into x2(n+1) = βn+1.
Let C0 = C × {0}, C1 = C × {1}.
Following [8] and [15] we have
Proposition 2.1. For n = 1, 2 . . . we have P-a.e.
P (ˆx(n) ∈C0|ˆx(n) ∈C0 ∪C1, ˆx(n −1), . . . , ˆx(0)) = 1 −β.
(2.2)
The process (ˆx(n) = (x1(n), x2(n))) is Markov with transition operator
ˆP(ˆx(n), dy) defined by (i)-(iii). Its first coordinate (x1(n)) is also a Markov
process with transition operator P(x1(n), dy). Furthermore, for any bounded
Borel measurable function f : (Rk)n+1 →R we have
Ex {f(x(1), x(2), . . . , x(n))} = ˆEδ∗x
1
f(x1(1), x1(2), . . . , x1(n))
2
(2.3)
where δ∗
x = δ(x,0) for x ∈Rk \ C and δ∗
x = (1 −β)δ(x,0) + βδ(x,1) for x ∈C
and ˆEµ stands for conditional law of Markov process (ˆx(n)) with initial law
µ ∈P( ˆ
Rk).
Proof. Since the Markov property of (x1(n)) is fundamental in this paper we
recall this proof from [8] leaving the proof of other statements to the reader.
For A ∈Rk we have

216
G.B. Di Masi and ^L. Stettner
P

x1(n + 1) ∈A|x1(n), x1(n −1), . . . , x1(0)

= P

x1(n + 1) ∈A|x1(n), x2(n) = 0, x1(n −1), . . . , x1(0)

P

x2(n) = 0|x1(n), x1(n −1), . . . , x1(0)

+P

x1(n + 1) ∈A|x1(n), x2(n) = 1, x1(n −1), . . . , x1(0)

P

x2(n) = 1|x1(n), x1(n −1), . . . , x1(0)

.
In the case when x1(n) ∈C, the right-hand side of the last equation is equal
to
P an(x1(n), A) −βν(A)
1 −β
(1 −β) + βν(A) = P an(x1(n), A).
For x1(n) /∈C, it is equal to P an(x1(n), A), which completes the proof of the
Markov property of (x1(n)).
✷
By the assumption on C and the construction of the split Markov process
we immediately have
Corollary 2.1. ˆEx [τC1] < ∞for x ∈ˆ
Rk and supx∈C1 ˆEx [τC1] < ∞.
Lemma 2.1. Given h(n) ∈UM there is a unique λ({h(n)}) such that for
x ∈C1
ˆEx
BτC1

t=1

c(x1(t), h(t)) −λ({h(n)})

C
= 0.
(2.4)
Proof. Notice that for x ∈C1 the mapping
D : λ →ˆEx
BτC1

t=1

c(x1(t), h(t)) −λ

C
is continuous and strictly decreasing. Since the values of this mapping for ∥c∥
and −∥c∥are, respectively, nonpositive and nonnegative, there is a unique λ
for which the mapping attains 0.
✷
For Borel measurable u : Rk →U let
ˆwu(x) = ˆEx
BτC1

t=0

c(x1(t), u(x1(t))) −λ(u)

C
,
(2.5)
where we use the notation λ(u) = λ({u(x(n))}).
Lemma 2.2. Function ˆwu defined in (2.5) is the unique (up to an additive
constant) solution to the additive Poisson equation (APE) for the split Markov
process (ˆx(n)):
ˆwu(x) = c(x1, u(x1)) −λ(u) +

ˆ
Rk ˆwu(y) ˆP(x, dy).
(2.6)

Remarks on Risk Neutral and Risk Sensitive Portfolio Optimization
217
Furthermore, if ˆw and λ satisfy the equation
ˆw(x) = c(x1, u(x1)) −λ +

ˆ
Rk ˆw(y) ˆP(x, dy)
(2.7)
then λ = λ(u) (defined in Lemma 2.1) and ˆw differs from ˆwu by an additive
constant.
Proof. In fact, we have using (2.4)
ˆEx [w(ˆx(1))] = ˆEx
B
χˆx(1)∈C1 ˆEx(1)
BτC1

t=0

c(x1(t), u(x1(t))) −λ(u)

CC
+ ˆEx
B
χˆx(1)/∈C1 ˆEx(1)
BτC1

t=0

c(x1(t), u(x1(t))) −λ(u)

CC
= ˆEx

χˆx(1)∈C1

c(x1(1), u(x1(1))) −λ(u)

+ ˆEx
B
χˆx(1)/∈C1
τC1

t=0

c(x1(t), u(x1(t))) −λ(u)

C
= ˆEx
BτC1

t=0

c(x1(t), u(x1(t))) −λ(u)

C
−

c(x1, u(x1)) −λ(u)

from which (2.6) follows. If ˆwu is a solution to (2.6) then by iteration we
obtain that
ˆwu(x) = ˆEx
BτC1

t=0

c(x1(t), u(x1(t))) −λ(u)

+ ˆEˆxτC1 [ ˆwu(ˆx(1))]
C
,
(2.8)
where by the construction of the split Markov process
ˆExτC1 [ ˆwu(ˆx(1))] = (1 −β)

Rk ˆwu(z, 0)ν(dz) + β

Rk ˆwu(z, 1)ν(dz).
Consequently, ˆwu differs from ˆwu defined in (2.5) only by an additive constant.
Similarly, if ˆw and λ are solutions to (2.7) then ˆw differs from
˜w(x) = ˆEx
BτC1

t=0

c(x1(t), u(x1(t))) −λ

C
by an additive constant ˆEz { ˆw(ˆx(1))} with z ∈C1. Since ˜w itself is a solution
to (2.7) we have that ˆEz { ˜w(ˆx(1))} = 0 for z ∈C1. Therefore, for z ∈C1

218
G.B. Di Masi and ^L. Stettner
0 = ˆEz [ ˜w(ˆx(1))] = ˆEz
B
χ ˆ
Rk\C1(ˆx(1))
τC1

t=1

c(x1(t), u(x1(t))) −λ

+χC1(ˆx(1)) ˆEˆx(1)
BτC1

t=0

c(x1(t), u(x1(t))) −λ

CC
= ˆEz
BτC1

t=1

c(x1(t), u(x1(t))) −λ

C
and by Lemma 2.1 we have λ = λ(u) which completes the proof.
✷
Corollary 2.2. Given a solution ˆwu : ˆ
Rk →R to the APE (2.6) we have that
wu defined by
wu(x) := ˆwu(x, 0) + 1C(x)β [ ˆwu(x, 1) −ˆwu(x, 0)]
(2.9)
is a solution to the APE for the original Markov process (x(n))
wu(x) = c(x, u(x)) −λ(u) +

Rk wu(y)P(x, dy).
(2.10)
Furthermore if wu is a solution to (2.10) then ˆwu defined by
ˆwu(x1, x2) = c(x1, u(x1)) −λ(u) + ˆEx1,x2 
wu(x1(1))

(2.11)
is a solution to (2.6).
Proof. By (2.2) we have
ˆEx [ ˆwu(ˆx(1))] = ˆEx
)
ˆEx

ˆwu(ˆx(1))|x1(1)

= ˆEx

χC(x1(1))

(1 −β) ˆwu(x1(1), 0) + β ˆwu(x1(1), 1)

+ χE\C(x1(1)) ˆwu(x1(1), 0)

= ˆEx

wu(x1(1))

.
(2.12)
Therefore by (2.6) we obtain that wu defined in (2.9) is a solution to (2.10).
Assume now that wu is a solution to (2.10). Then by (2.3)
ˆEδ∗
x

wu(x1(1))

= Ex [wu(x(1))]
and for ˆwu given in (2.11) we obtain (2.9). From (2.9) we obtain (2.12) which
in turn by (2.11) shows that ˆwu is a solution to (2.6).
✷
Remark 2.1. The APE has been a subject of intensive studies in [14] (together
with the so called multiplicative Poisson equation). The results given above
show that the use of splitting techniques provides an explicit form for the
solutions to this equation.

Remarks on Risk Neutral and Risk Sensitive Portfolio Optimization
219
The value of λ(u) has another important characterization. Namely, we have
Proposition 2.2. For Borel measurable u : Rk →U the value λ(u) defined
in Lemma 2.1 is equal to
λ(u) = lim
n→∞
1
nEx
Bn−1

t=0
c(x(t), u(x(t)))
C
(2.13)
Proof. Let λ > λ(u). For z ∈C1 we have
ˆEz
BτC1

t=1

c(x1(t), u(x1(t))) −λ

C
< 0
and consequently for N ≥N0
ˆEz


τC1∧N

t=1

c(x1(t), u(x1(t))) −λ


≤0.
(2.14)
Let
wu
N(x) = ˆEx


σC1∧N−1

t=0

c(x1(t), u(x1(t))) −λ



(2.15)
with σC1 = inf {t ≥0 : ˆx(t) ∈C1}.
For x /∈C1
wu
N+1(x) = ˆEx
B
c(x1(0), u(x1(0))) −λ
+ ˆEˆx(1)
B σC1∧N−1

t=0

c(x1(t), u(x1(t))) −λ

CC
= ˆEx

c(x1(0), u(x1(0))) −λ + wu
N(ˆx(1))

(2.16)
and for x ∈C1 by (2.14) we have
wu
N+1(x) = c(x1(0), u(x1(0))) −λ
≥ˆEx
B
c(x1(0), u(x1(0))) −λ
+ ˆEˆx(1)
B σC1∧N−1

t=0

c(x1(t), u(x1(t))) −λ

CC
= ˆEx

c(x1(0), u(x1(0))) −λ + wu
N(ˆx(1))

.
(2.17)

220
G.B. Di Masi and ^L. Stettner
Consequently,
wu
N+1(x) ≥ˆEx

c(x1(0), u(x1(0))) −λ + wu
N(ˆx(1))

(2.18)
and by iteration for N ≥N0
wu
N+k(x) ≥ˆEx
Bk−1

t=0

c(x1(t), u(x1(t))) −λ

+ wu
N(ˆx(k))
C
≥ˆEx
Bk−1

t=0
c(x1(t), u(x1(t))) −λ −∥c∥N
C
.
Therefore,
1
k
ˆEx
Bk−1

t=0
c(x1(t), u(x1(t)))
C
≤1
k ∥c∥N + 1
k sup
N
ˆEx


σC1∧N−1

t=1

c(x1(t), u(x1(t))) −λ(u)


+ λ
and, consequently,
lim sup
k→∞
1
k
ˆEx
Bk−1

t=0
c(x1(t), u(x1(t)))
C
≤λ.
With λ decreasing to λ(u), we obtain
lim sup
k→∞
1
k
ˆEx
Bk−1

t=0
c(x1(t), u(x1(t)))
C
≤λ(u).
(2.19)
Assume now that λ < λ(u). For z ∈C1 we have
ˆEz
BτC1

t=1

γc(x1(t), u(x1(t))) −λ

C
> 0
and, consequently, for N ≥N0
ˆEz


τC1∧N

t=1

c(x1(t), u(x1(t))) −λ


≥0.
(2.20)
Therefore, for wu
N defined in (2.15), similarly to (2.16)-(2.17), we have
wu
N+1(x) ≤ˆEx

c(x1(0), u(x1(0))) −λ + wu
N(ˆx(1))

(2.21)
and by iteration for N ≥N0

Remarks on Risk Neutral and Risk Sensitive Portfolio Optimization
221
wu
N+k(x) ≤ˆEx
Bk−1

t=0

c(x1(t), u(x1(t))) −λ

+ wu
N(ˆx(k))
C
≤ˆEx
Bk−1

t=0

c(x1(t), u(x1(t))) −λ

+ ∥c∥N
C
.
Therefore,
1
k
ˆEx
Bk−1

t=0
c(x1(t), u(x1(t)))
C
≥−1
k ∥c∥N + 1
k inf
N
ˆEx


σC1∧N−1

t=1

c(x1(t), u(x1(t))) −λ(u)


+ λ
and
lim inf
k→∞
1
k
ˆEx
Bk−1

t=0
c(x1(t), u(x1(t)))
C
≥λ
and, finally,
lim inf
k→∞
1
k
ˆEx
Bk−1

t=0
c(x1(t), u(x1(t)))
C
≥λ(u)
(2.22)
which together with (2.19) completes the proof.
✷
We summarize the results of this section in the following
Theorem 2.1. There exists a unique (up to an additive constant) function
w : Rk →R and a unique constant λ which are solutions to the Bellman
equation (1.7). Furthermore, λ is the optimal value of the cost functional J0.
Proof. Notice that for ˆu optimal we find w and λ as a solution to the APE
w(x) = c(x, ˆu(x)) −λ +

Rk w(y)P(x, dy),
which exist by Lemmas 2.1, 2.2 and Corollary 2.2. By Proposition 1.17, λ
is an optimal value of the cost functional J0. Uniqueness up to an additive
constant of w follows from uniqueness of the solutions to APE for the split
Markov process (Lemma 2.2) and Corollary 2.2.
✷
3 Risk sensitive asymptotics
In what follows we shall assume that γ ∈(−1, 0). The following estimation
will be useful in this section

222
G.B. Di Masi and ^L. Stettner
Lemma 3.1. We have
eγ∥a∥≤E
B	 m

i=1
hiξi(x, W(0))

γC
≤e|γ|∥a∥+ 1
2 γ2∥σ2∥.
(3.1)
Proof. Since r(z) = zγ is convex, by the Jensen inequality we have
E
B	 m

i=1
hiξi(x, W(0))

γC
≤
m

i=1
hiE [(ξi(x, W(0)))γ] .
Using the H¨older inequality twice we have
E
B	 m

i=1
hiξi(x, W(0))

γC
≥
1
E
)
(m
i=1 hiξi(x, W(0)))−γ
≥
1
(m
i=1 hiE [(m
i=1 ξi(x, W(0)))])−γ .
Then using standard estimations for ξi we easily obtain (3.1).
✷
Immediately from Lemma 3.1 we have
Corollary 3.1.
lim sup
γ→0
sup
x∈Rk sup
h∈U
E
B	 m

i=1
hiξi(x, W(0))

γC
−1
 = 0
(3.2)
and
lim
γ→0 sup
x∈Rk sup
h∈U
|cγ(x, h)| = 0.
(3.3)
We furthermore have
Lemma 3.2.
lim
γ→0
1
γ cγ(x, h) = c(x, h)
(3.4)
and the limit is increasing and uniform in x and h from compact subsets.
Proof. By the H¨older inequality 1
γ cγ(x, h) is increasing in γ. Using l’Hˆopital’s
rule for γ →0 we identify the limit as c(x, h). Since the functions c(x, h)
and cγ(x, h) are continuous, by Dini’s theorem the convergence is uniform on
compact sets.
✷
Lemma 3.3. We have that
sup
A∈B(Rk)
sup
x∈Rk sup
h∈U

P h,γ(x, A)
P(x, A)
−1
 →0
(3.5)
as γ →0.

Remarks on Risk Neutral and Risk Sensitive Portfolio Optimization
223
Proof. Notice that by the H¨older inequality we have
P h,γ(x, A) ≤e−cγ(x,h)e
1
2 c2γ(x,h)
P(x, A)
(3.6)
and
P(x, A) ≤e
1
2 cγ(x,h)e−1
2 γ∥a∥
H
P h,γ(x, A)
(3.7)
from which (3.5) easily follows.
✷
In what follows we shall assume that for some γ < 0 we have
Ex
)
e|γ|τC
< ∞
(3.8)
for x ∈Rk and
sup
x∈C
Ex
)
e|γ|τC
< ∞.
(3.9)
where C is the same compact set as in Section 2.
We recall the following fundamental result from [8].
Theorem 3.1. For γ < 0 sufficiently close to 0 there exists λγ and a contin-
uous function wγ : Rk →R such that the Bellman equation (1.10) is satisfied.
Moreover
1
γ λγ is an optimal value of the cost functional Jγ
x and the control
ˆu(xn), where ˆu is a Borel measurable function for which the infimum in the
right hand side of (1.10) is attained, is an optimal control within the class of
all controls from Us.
Furthermore, if for an admissible control (hn) we have that
lim sup
t→∞E(hn)
x
)
Eht
xt
)
ewγ(x1)α
< ∞
for every α > 1, then 1
γ λγ ≤Jγ
x ((hn)).
Notice now that by the H¨older inequality the value of the functional Jγ is
increasing in γ < 0 and, by the Jensen inequality, is dominated by the value of
J0. Consequently, the same holds for the optimal values of the cost functionals,
i.e.
1
γ λγ ≤λ.
(3.10)
Furthermore, there is a sequence un of continuous functions from Rk to
U such that c(x, un(x)) converges uniformly in x from compact subsets to
suph∈U c(x, h). By Lemma 2.1 and Theorem 2.1 we immediately have that
λ((un)) →λ as n →∞. This means that for any ε > 0 there is an ε-optimal
continuous control function uε. We are going to show that for each ε > 0
Jγ(uε(x(n))) →J0(uε(x(n)))
(3.11)
as γ →0. Since the proof will be based, following Section 5 of [6], upon large
deviation estimates, we need the following assumption:

224
G.B. Di Masi and ^L. Stettner
(A)
there is a continuous function f0 : Rk →[1, ∞) such that for each
positive integer n the set Kn :=
/
x ∈Rk :
f0(x)
P f0(x) ≤n
0
is compact.
Remark 3.1. By direct calculation one can show that for a large class of ergodic
processes (x(n)) function f0(x) = ec∥x∥2 satisfies (A) for small c. To be more
precise, assume for simplicity that k = 1 and |x+b(x)| ≤β|x| for a sufficiently
large x with 0 < β < 1. Then for 0 < c < 1−β2
2ddT assumption (A) holds.
Proposition 3.1. Under (A) for continuous control function u : Rk →U we
have
Jγ(u(x(n))) →J0(u(x(n)))
(3.12)
as γ →0.
Proof. Under (A) using Lemma 3.3 we see that the set
Ku,γ
n
:=

x ∈Rk :
f0(x)
P u,γf0(x) ≤n

is compact for each n. Therefore, by Theorem 4.4 of [10] we have an upper
large deviation estimate for empirical distributions of Markov process with
transition operator P u(x),γ(x, ·). Using the theorem in Section 3 of [11] we
also have a lower large deviation estimate. Consequently, we have a large
deviation principle corresponding to the rate function
Iu,γ(ν) := sup
h∈H

Rk ln
h(x)
P u(x),γh(x)ν(dx),
(3.13)
where H is the set of all bounded functions h : Rk →R such that
1
h(x) is also
bounded and ν ∈P(Rk). Therefore, by Varadhan’s theorem (Theorem 2.1.1
of [5]) we have
1
γ lim
n→∞
1
n ln Eh,γ
x
B
exp
	n−1

t=0
cγ(x(t), h(t))

C
=
inf
ν∈P(Rk)

Rk
1
γ cγ(z, u(z))ν(dz) −1
γ Iu,γ(ν)

.
(3.14)
There is a sequence of measures νγi with γi →0 as i →∞such that

Rk
1
γi
cγi(z, u(z))νgi(dz) −1
γi
Iu,γi(νγi)
≤
inf
ν∈P(Rk)

Rk
1
γi
cγi(z, u(z))ν(dz) −1
γi
Iu,γi(ν)

+ 1
i .
(3.15)
Since from (3.1)

Remarks on Risk Neutral and Risk Sensitive Portfolio Optimization
225
1
γ lim
n→∞
1
n ln Eh,γ
x
B
exp
	n−1

t=0
cγ(x(t), h(t))

C
≤∥a∥
(3.16)
we have that Iu,γi(νγi) →0. We shall show that the sequence (νγi) is tight.
Applying Fatou’s lemma to the sequence {f0 ∧N} with N →∞we obtain
that

Rk ln
f0(x)
P u(x),γf0(x)νγi(dx) ≤Iu,γi(νγi).
(3.17)
By (3.5) for ε > 0 there is γ0 such that for γ ≥γ0
(1 −ε)Pf0(x) ≤P u(x),γf0(x) ≤(1 + ε)Pf0(x).
(3.18)
Therefore, by (3.17)

Rk ln f0(x)
Pf0(x)νγi(dx) ≤Iu,γi(νγi) + ln(1 + ε)
(3.19)
for i > i0. Let ρn := infx∈Kn ln
f0(x)
P f0(x). Then
ρnνγi(Kn) + ln nνγi(Kc
n) ≤Iu,γi(νγi) + ln(1 + ε)
(3.20)
where Kc
n := Rk \ Kn. Consequently,
ln nνγi(Kc
n) ≤Iu,γi(νγi) + ln(1 + ε) −ρn
ln n −ρn
(3.21)
and since ln n ≥1 + ρn for sufficiently large n, we have the tightness of
the measures νγi. By the Prohorov theorem there exists a subsequence of
νγi, for simplicity still denoted by νγi, and a probability measure ¯ν such
that νγi →¯ν as i →∞. Since by (3.5) Iu,γ(ν) converges uniformly to
Iu(ν) := suph∈H

Rk ln
h(x)
P u(x)h(x)ν(dx) as γ →0 and Iu is a nonnegative
lower semicontinuous function, we have that Iu(¯ν) = 0. By Lemma 2.5 of
[9] the measure ¯ν is invariant for the transition operator P(x, ·). Therefore,
by Lemma 3.2
lim
i→∞
1
γi
lim
n→∞
1
n ln Eh,γi
x
B
exp
	n−1

t=0
cγi(x(t), h(t))

C
≥lim
i→∞

Rk
1
γi
cγi(z, u(z))νγi =

Rk c(z, u(z))¯ν(dz) = J0(u(x(n))(3.22)
and using the fact that the cost functional Jγ is increasing in γ we obtain
(3.12), which completes the proof.
✷
We are now in position to summarize the results of this section.

226
G.B. Di Masi and ^L. Stettner
Theorem 3.2. Under (A) a continuous ε-optimal control function uε for J0
is also a 2ε-optimal control function for Jγ provided 0 > γ > γ0. Consequently
convergence (1.12) holds.
Remark 3.2. One can expect that at least a subsequence of 1
γ wγ(x) converges
to w(x) uniformly on compact subsets, as γ →0 , where w is a solution to
the risk neutral Bellman equation (1.7). Unfortunately, the authors were not
able to show this.
References
1. Bielecki T.R., Pliska S.: Risk sensitive dynamic asset management. JAMO 39,
337–360 (1999)
2. Borkar V.S., Meyn S.P.: Risk-sensitive optimal control for Markov decision
processes with monotone cost. Math. Oper. Res., 27, 192–209 (2002)
3. Cavazos-Cadena R.: Solution to the risk-sensitive average cost optimality in a
class of Markov decision processes with finite state space. Math. Meth. Oper.
Res. 57, 263–285 (2003)
4. Cavazos-Cadena R., Hernandez-Hernandez D.: Solution to the risk-sensitive av-
erage optimality equation in communicating Markov decision chains with fi-
nite state space: An alternative approach. Math. Meth. Oper. Res. 56, 473–479
(2002)
5. Deuschel J.D., Stroock D.W.: Large Deviations. New York: Academic Press 1989
6. Di Masi G.B., Stettner L.: Risk sensitive control of discrete time Markov
processes with infinite horizon. SIAM J. Control Optimiz. 38, 61–78 (2000)
7. Di Masi G.B., Stettner L.: Infinite horizon risk sensitive control of discrete time
Markov processes with small risk Sys. Control Lett 40, 305–321 (2000)
8. Di Masi G.B., Stettner L.: Infinite horizon risk sensitive control of discrete time
Markov processes under minorization property. Submitted for publication (2004)
9. Donsker M.D., Varadhan S.R.S.: Asymptotic evaluation of certain Markov
process expectations for large time - I. Comm. Pure Appl. Math. 28, 1–47 (1975)
10. Donsker M.D., Varadhan S.R.S.: Asymptotic evaluation of certain Markov
process expectations for large time - III. Comm. Pure Appl. Math. 29, 389–
461 (1976)
11. Duflo M.: Formule de Chernoffpour des chaines de Markov. Grandes deviations
et Applications Statistiques. Asterisque 68, 99–124 (1979)
12. Fleming W.H., Hernandez-Hernandez D.: Risk sensitive control of finite state
machines on an infinite horizon. SIAM J. Control Optimiz. 35, 1790–1810 (1997)
13. Hernandez-Hernandez D., Marcus S.J.: Risk sensitive control of Markov
processes in countable state space. Sys. Control Letters 29, 147–155 (1996)
14. Kontoyiannis I., Meyn S.P.: Spectral theory and limit theorems for geometrically
ergodic Markov processes. Ann. Appl. Prob. 13, 304–362 (2003)
15. Meyn S.P., Tweedie R.L.: Markov Chains and Stochastic Stability Berlin Hei-
delberg New York: Springer 1996
16. Stettner L.: Risk sensitive portfolio optimization. Math. Meth. Oper. Res. 50,
463–474 (1999)

On Existence and Uniqueness of Reflected
Solutions of Stochastic Equations Driven by
Symmetric Stable Processes ∗
Hans-J¨urgen ENGELBERT1, Vladimir P. KURENOK2, and Adrian
ZALINESCU3
1 Institut f¨ur Stochastik, Friedrich-Schiller-Universit¨at, Ernst-Abbe Platz 1–4,
D-07743 Jena, Germany.
engelbert@minet.uni-jena.de
2 Department of Natural and Applied Sciences, University of Wisconsin-Green
Bay, 2420 Nicolet Drive, Green Bay, WI 54311-7001, USA.
kurenokv@uwgb.edu
3 Institut f¨ur Stochastik, Friedrich-Schiller-Universit¨at, Ernst-Abbe Platz 1–4,
D-07743 Jena, Germany.
zalinesc@minet.uni-jena.de
Summary. We study the one-dimensional stochastic differential equation (SDE) of
the form Xt = x0 +  t
0 b(Xs−)dMs + Kt, t ≥0, where the volatility b : [0, ∞) →R
is a Borel measurable function, x0 ∈[0, ∞) is an arbitrary initial value, the process
X is nonnegative, K is a right-continuous increasing process with K0 = 0, and M
is a symmetric stable process of arbitrary stability index α ∈(0, 2] with M0 = 0.
The process K satisfies the condition  ∞
0
1{Xt̸=0}dKt = 0, that means that K is the
reflecting force for the solution X. For every x0 ∈[0, ∞) we state conditions on b for
the existence and uniqueness of a reflected solution X with X0 = x0. In particular,
our results generalize the results of W. M. Schmidt [16] who considered the given
SDE in the case of the Brownian motion (α = 2).
Key words: symmetric stable processes, Skorohod reflection problem, integral
functionals, stochastic stable integrals, stochastic equations, existence and unique-
ness of solutions
MR Subject Classification (2000): 60H10, 60J60, 60J65, 60G44
∗Work supported in part by the European Community’s Human Potential Pro-
gramme under contract HPRN-CT-2002-00281, [Evolution Equations].

228
H.-J. Engelbert, V. Kurenok and A. Zalinescu
1 Introduction
In this paper we consider the one-dimensional stochastic equation
Xt = x0 +
 t
0
b(Xs−)dMs + Kt ,
t ≥0 ,
(1.1)
where the volatility b : [0, ∞) →R is a Borel function, x0 ∈[0, ∞) is an
arbitrary initial value, the process X is nonnegative, K (called the reflecting
force) is a right-continuous increasing process with K0 = 0 and such that
 ∞
0
1{Xt̸=0}dKt = 0, and M is a symmetric stable process with M0 = 0.
It is well-known that every symmetric stable process can uniquely be char-
acterized by its stability index α ∈(0, 2] in the following sense. A process M is
a symmetric stable process of index α iffit is a process with homogeneous and
independent increments and the characteristic function of Mt has the form
E exp(iλMt) = exp(−t |λ|α) , λ ∈R ,
t ≥0 .
(1.2)
For α = 2 the process M is a Brownian motion (with variance function 2t) and
for α = 1 it is a Cauchy process. The Brownian motion is the only symmetric
stable process with continuous sample paths. For all other parameters α ∈
(0, 2) the process M is a purely discontinuous semimartingale with infinite
variance. Therefore, the cases α = 2 and 0 < α < 2 are rather different,
at least from this point of view. The density function for symmetric stable
processes can be written in explicit form only in three cases: for the Brownian
motion, the Cauchy process and the 1
2-stable process. For more details about
symmetric stable processes we refer to the well-known books [1], [15] or [18].
By a stochastic basis we understand a complete probability space (Ω, F, P)
with a filtration F = (Ft)t≥0 satisfying the usual conditions. Now, a symmetric
α-stable process with respect to the filtration F is a symmetric α-stable process
M which is F-adapted and such that Mt −Ms is independent of Fs for all
≤s ≤t. (Alternatively, exp (iλMt + t |λ|α) is a complex-valued F-martingale
for every λ ∈R.) For the sake of simplicity, in that case we say that (M, F) is
a symmetric α-stable process.
Let α ∈(0, 2], x0 ∈[0, ∞), and a Borel function b : [0, ∞) →R be fixed.
Definition 1. A process X defined on a stochastic basis (Ω, F, P; F) is said
to be a reflected solution of SDE (1.1) in [0, ∞) if there exist two processes
M and K such that:
1) X is F-adapted and Xt ≥0 for all t ≥0;
2) (M, F) is a symmetric stable process of index α;
3) K is an F-adapted, right-continuous and increasing process with K0 = 0;
4)
 ∞
0
1{Xt̸=0}dKt = 0;
5) equation (1.1) is satisfied P-a.s.

Stochastic Equations Driven by Symmetric Stable Processes
229
Relation 4) means that K increases only if X becomes zero. The process
K is called the reflecting force for the solution X of SDE (1.1).
Under the integral in (1.1) we may understand the stochastic integral with
respect to the symmetric stable process M in the sense of Itˆo as defined by
J. Rosi´nski and W. Woyczy´nski [13]. There is a great analogy between the
construction of this stochastic integral and the Itˆo integral for the Brownian
motion. However, and this is very important, the result is completely the
same if this integral is constructed as a stochastic integral with respect to
the semimartingale M, as in the book of J. Jacod and A.N. Shiryaev [7].
In both [7] (Chapter III,
6d) and [13] it was proven that the finiteness of
 t
0 |b(Xs−)|α ds, for all t ≥0, is necessary and sufficient for the existence of
the stochastic integral in (1.1).
Multidimensional stochastic differential equations with reflections in gen-
eral form driven by Brownian motion were considered by many authors. We
only refer to the papers of L. S`lomi´nski [19], [20], and A. Rozkosz and L.
S`lomi´nski [14] where they investigated the equation under quite general as-
sumptions on the coefficients and where one can find other references on this
topic. In the one-dimensional case one can obtain more. Equation (1.1) with
driving process M being a Brownian motion was studied in detail by W. M.
Schmidt in [16], where he obtained necessary and sufficient conditions for
the existence of solutions. W. M. Schmidt essentially used the time change
method and the properties of the local time of the Brownian motion. Nonre-
flected SDEs driven by symmetric α-stable processes were considered by P.
A. Zanzotto [23], [24] (time-independent case), by H. Pragarauskas and P. A.
Zanzotto [10] (time-dependent case, 1 < α < 2) and by H.-J. Engelbert and
V. P. Kurenok [5] (time-dependent case, 0 < α ≤2).
The aim of the present paper is to solve SDE (1.1) for an arbitrary stability
index α ∈(0, 2]. Our results about the existence of solutions will generalize,
in particular, the results of W. M. Schmidt for the case α = 2. To construct
a solution of (1.1) we use the time change method analogously to the case of
nonreflected SDEs (see, e.g., [5]).
The paper is organized as follows. In Section 2 we construct a symmetric
stable process with a reflecting boundary at zero for an arbitrary parame-
ter α ∈(0, 2]. The method for the construction of a Brownian motion with
reflecting boundaries used by W. M. Schmidt cannot be applied to the case
0 < α < 2 because for 0 < α ≤1 there doesn’t exist a local time process
and for 1 < α < 2 (when the local time exists) there is no Tanaka formula,
at least in an explicit form as for the case of the Brownian motion. For the
general case we use the approach for the construction of a reflected process in
a bounded region given by A. V. Skorohod [17]. We prove that the reflected
α-stable processes are recurrent for every α ∈(0, 2]. This allows us to con-
struct nonexploding solutions of (1.1); that is a situation different from the
nonreflected case (when 0 < α < 1). We also investigate some properties of
integral functionals of reflected symmetric stable processes which are the key

230
H.-J. Engelbert, V. Kurenok and A. Zalinescu
for the construction of a solution of (1.1). They are collected in Section 3. The
last section is devoted to the existence and uniqueness of solutions of (1.1).
2 Reflected symmetric stable processes
In this section we shall construct (in the sense of trajectories) a symmetric
stable process reflected at the boundary zero to the right. First of all, we
define what we understand by such a process.
Definition 2. A process ¯
M with ¯
M0 ≥0 is called a reflected symmetric stable
process of index α on [0, ∞) if there exist processes M and K such that:
1) M is a symmetric stable process of index α;
2)
¯
Mt ≥0 for all t ≥0;
3) K is an increasing, right-continuous process with K0 = 0 and
 ∞
0
1{ ¯
Mt̸=0}dKt = 0 ;
4) it holds
¯
Mt = ¯
M0 + Mt + Kt , t ≥0 .
(2.1)
As in the previous section, the process K is called the reflecting force
for ¯
M.
In the case α = 2, the reflected process can be described by |M|, where M
is a Brownian motion (with variance function 2t). Using the Tanaka formula,
we recover the reflecting force K as the local time of M (or 1
2 of the local time
of |M|). This well-known fact was exploited by W. M. Schmidt [16].
But there is another possibility to obtain the reflected Brownian motion
which immediately follows from the solution of the deterministic Skorohod
problem. Let D be the space of functions x : [0, ∞) →R which are c`adl`ag
(right-continuous, with finite left-hand limits). Then the deterministic Skoro-
hod problem can be formulated as follows. For a given function x ∈D such
that x(0) ≥0 there are to find functions z and y from the space D such that:
1) z(t) ≥0 for all t ≥0;
2) y is an increasing function with y(0) = 0 and
 ∞
0
1{z(t)̸=0}dy(t) = 0;
3) it holds z(t) = x(t) + y(t) for all t ≥0.
The existence and uniqueness of the solution of this problem for the space
of continuous functions was first proven by A. V. Skorohod [17] in 1961. H.
Tanaka [21] generalized the problem by formulating it in the space of c`adl`ag
functions, in the multi-dimensional case. In this generality he proved only
uniqueness (Lemma 2.3, [21]). However, in the one-dimensional case, existence
also holds and we give a proof, for the convenience of the reader.

Stochastic Equations Driven by Symmetric Stable Processes
231
Lemma 1. For every function x ∈D such that x(0) ≥0, the deterministic
Skorohod problem on [0, ∞) has a unique solution (z, y), given by
y (t) := sup
0≤s≤t
max (−x (s) , 0) ,
z (t) := x (t) + y (t) , t ≥0 .
(2.2)
Proof. We first prove existence. Let x ∈D such that x(0) ≥0 and y, z be
defined by (2.2). It is obvious that y, z are in D, z(t) ≥0 for all t ≥0
and y is an increasing function with y(0) = 0. It remains only to prove that
 ∞
0
1{z(t)>0}dy(t) = 0.
Let ε > 0 be fixed, but arbitrary. Since z ∈D, the set {t ≥0 : z (t) > ε}
can be written as I
n≥1 In, where In, n ≥1, are pairwise disjoint intervals of
the form In = (un, vn) or [un, vn).
We have, for n ≥1,
−x (t) = y (t) −z (t) ≤y (vn−) −ε , ∀t ∈In .
This yields
y (vn−) = max

y (un) ,
sup
un<t<vn
max (−x (t) , 0)

≤max (y (un) , y (vn−) −ε) ,
which means that y (vn−) = y (un), for every n ≥1. It follows that
 ∞
0
1{z(t)>ε}dy(t) = 0 , ∀n ≥1 .
By letting ε →0, we obtain the result.
For the uniqueness part, we consider two solutions, (z, y) and (z′, y′), of
the Skorokhod problem with input function x. Then,
z (t) −z′ (t) = y (t) −y′ (t) , ∀t ≥0 .
Integrating by parts, this yields that for every t > 0,
[(z −z′) (t)]2
= 2

(0,t]
(z −z′) (s) d (y −y′) (s) −

0<s≤t
[(z −z′) (s) −(z −z′) (s−)]2
≤2

(0,t]
(z −z′) (s) d (y −y′) (s) .
On the other hand, the relations
 ∞
0
z (s) dy(s) = 0 and
 ∞
0
z′ (s) dy′(s) = 0
imply that

(0,t]
(z −z′) (s) d (y −y′) (s) ≤0, ∀t ≥0 .
Hence z (t) = z′ (t), ∀t ≥0, which proves the result.

232
H.-J. Engelbert, V. Kurenok and A. Zalinescu
Now suppose that M is a symmetric stable process of arbitrary index α
defined on a probability space (Ω, F, P) and x0 ≥0. For all t ≥0 we put
Kt := sup
0≤s≤t
max (−Ms −x0, 0)
(2.3)
and let
¯
Mt := x0 + Mt + Kt .
(2.4)
For all 0 < α ≤2, the process M is a right-continuous process with
finite left-hand limits. By Lemma 1, the constructed process ¯
M is a reflected
symmetric stable process in the sense of Definition 2. Reflected symmetric
α-stable processes were already introduced and studied by S. Watanabe [22].
We can also regard the symmetric α-stable process M as a (strong) Markov
process defined on a family (Ω, F, F, Px, x ∈R) of filtered probability spaces
such that Px (M0 = x) = 1 for every x ∈R. Then, as it is noticed in [22], the
reflected process is a strong Markov process on [0, ∞) when viewed as
¯
Mt := Mt + sup
0≤s≤t
max (−Ms, 0) ,
t ≥0 .
(The difference from (2.3) and (2.4) is due to the fact that in this framework
M does not necessarily start at 0.)
Let us consider the following measure on [0, ∞):
m(dy) := n(y)dy , y > 0 ,
(2.5)
where n(y) := α
2 y
α
2 −1. Then the process ¯
M has m as its invariant measure
([22]), which means that for every Borel measurable set A ⊆[0, ∞),
 ∞
0
Px
 ¯
Mt ∈A

m (dx) = m (A) , ∀t ≥0 .
(2.6)
For α = 2, m becomes exactly the Lebesgue measure on the interval [0, ∞).
In order to discuss the recurrence properties of the process ¯
M, let us remind
some standard concepts for Markov processes. First, for any, say, standard
Markov process X with state space (E, E), defined on the corresponding family
of probability spaces (Ω, F, F, Px, x ∈E), we introduce the so-called potential-
measures U(x, ·) as
U(x, A) := Ex
 ∞
0
1{Xt∈A}dt

,
A ∈E .
Then X is called recurrent if, for every measurable set A, U(·, A) ≡∞or
U(·, A) ≡0. In [2], the definition of recurrence is given using nearly measurable
sets, but it is immediately seen that these definitions are equivalent.
Proposition 1. For all α ∈(0, 2], the process ¯
M is recurrent.

Stochastic Equations Driven by Symmetric Stable Processes
233
Proof. From the construction of the process ¯
M it follows that it returns into
the origin at arbitrarily large times. Indeed, let us consider the stopping times
τz := inf {t ≥0 : Mt ≤−z} , z ≥0 .
(2.7)
Then, Px-a.s., τn < ∞, ∀n ∈N and τn ր ∞as n →∞, a consequence
of the fact that lim inf
t→∞Mt = −∞(see, for example p. 222, [1]) and of the
boundedness of M on finite intervals. It is obvious that, for every n ≥0,
¯
Mτn = 0, Px-a.s.
Let U be the potential measure associated with ¯
M and suppose that there
exist z ≥0 and a Borel set A such that U(z, A) < ∞. All we have to prove is
that U(x, A) = 0, for all x ≥0. First, we show that µ(A) = 0, where µ is the
Lebesgue measure on the positive half-line.
By the strong Markov property, for every n ∈N we have
Ex
 ∞
τn
1{ ¯
Mt∈A}dt

= E0
 ∞
0
1{ ¯
Mt∈A}dt

, ∀x ≥0 .
For the particular choice x = z, passing to the limit as n →∞, the finiteness
of the left-hand term in this equality implies that U (0, A) = 0 and so
 ∞
τ0
1{ ¯
Mt∈A}dt = 0 , Px-a.s. , ∀x ≥0 .
(2.8)
On the other hand, relation (2.6) yields
t m (A) =
 ∞
0
Ex
 t
0
1{ ¯
Ms∈A}ds

m (dx) .
From (2.8) and the property that Ms = ¯
Ms on {s < τ0}, we get
t m (A) =
 ∞
0
 t
0
Px (Ms ∈A, s < τ0) ds m (dx) , ∀t ≥0 .
(2.9)
The measure Px (Mt ∈dy, t < τ0) is the transition function of the process M
starting at x which is killed as soon as it leaves (0, ∞). D. Ray [11] proved
that it is absolutely continuous with respect to the Lebesgue measure and its
density, ˜p (t, x, y), satisfies the relation
 ∞
0
˜p (t, x, y) dt =
1
Γ (α/2)2
 min(x,y)
0
ξ
α
2 −1 (ξ + |y −x|)
α
2 −1 dξ , x, y ≥0 ,
where Γ is the Gamma function. We also denote by p (s, x, y) the density of
the measure Px (Ms ∈dy). Without loss of generality, we assume that the set
A is bounded. We choose a > 0 such that A ⊆[0, a], and thus α
2 a
α
2 −1µ (A) ≤
m (A). Splitting the integral in (2.9), we obtain, for every t ≥0,

234
H.-J. Engelbert, V. Kurenok and A. Zalinescu
t m (A) ≤
 a
0
 ∞
0

A
˜p (s, x, y) dy ds m (dx) +
 ∞
a
 t
0

A
p (s, x, y) dy ds m (dx)
≤
1
Γ (α/2)2
 a
0
 a
0
 min(x,y)
0
ξ
α
2 −1 (ξ + |y −x|)
α
2 −1 dξ dy m (dx)
+α
2 a
α
2 −1
 t
0

A
 ∞
y
p (s, x, y) dx dy ds
≤
1
Γ (α/2)2
 a
0
 a
0
xα−1 |y −x|
α
2 −1 dy dx + α
4 a
α
2 −1t µ (A) .
The last inequality comes from the property that p is homogeneous and sym-
metric; indeed, we have
 ∞
y
p (s, x, y) dx =
 ∞
y
p (s, 0, y −x) dx =
 ∞
0
p (s, 0, −x) dx = 1
2 ,
since p (s, 0, −x) = p (s, 0, x) for all s, x > 0. Hence
1
2t m (A) ≤
1
Γ (α/2)2
 a
0
 a
0
xα−1 |y −x|
α
2 −1 dy dx ≤
4a
3α
2
α2Γ (α/2)2 .
This proves that m (A) = 0, t being taken arbitrarily. Therefore, µ (A) = 0.
From (2.8), the fact that Px (Mt ∈·, t < τ0) is absolutely continuous with
respect to µ and the relation
U (x, A) =
 ∞
0
Px (Ms ∈A, s < τ0) ds + Ex
 ∞
τ0
1{ ¯
Ms∈A}ds

, ∀x ≥0 ,
we conclude that U (x, A) = 0 for all x ≥0.
3 Integral Functionals of Reflected Symmetric
Stable Processes
Let ¯
M be a reflected symmetric stable process of index α given by (2.3) and
(2.4) on a probability space (Ω, F, P), with arbitrary initial state x0 ≥0. For
an arbitrary measurable function f : [0, ∞) →[0, ∞] we consider the following
integral functional:
Tt :=
 t
0
f( ¯
Ms)ds, t ≥0 .
(3.1)
The first problem we analyse is whether the functional (3.1) is finite for all
t > 0.
For every y ≥0, let us denote by U(y) the family of open neighborhoods
in [0, ∞) of y, and introduce

Stochastic Equations Driven by Symmetric Stable Processes
235
Ef := {y ≥0 :

U
f(z)m(dz) = ∞, ∀U ∈U(y)} ,
where m is the measure introduced by (2.5). We write f ∈Lloc(m) to denote
that f is locally integrable with respect to m, i.e.,

C f(z)m(dz) < ∞for every
compact subset C of [0, ∞) (which is equivalent to Ef = ∅).
We remind that a measurable set A is called polar if P(D(A) = ∞) = 1,
where D(A) := inf{t > 0 : ¯
Mt ∈A} is the first hitting time of the set A by
the process ¯
M.
If 0 < α ≤1, we define the function hα,x0 : [0, ∞) →[0, ∞] by
hα,x0 (y) :=



|y −x0|α−1 , 0 < α < 1 ,
|ln |y −x0|| , α = 1 ,
and we assume the following hypothesis:
(Hα,x0)







Ef is polar
and ∃U ∈U(x0) :

U hα,x0 (z) f (z) dz < ∞, 0 < α ≤1 ,
f ∈Lloc(m),
1 < α < 2 .
Remark. Of course, since the polarity of a set depends only on the law
of the considered process, condition (Hα,x0) will depend only on α, x0 and
f. In the case x0 = 0, 0 < α ≤1, if Ef is polar, then the condition

U hα,x0 (z) f (z) dz < ∞for some U ∈U(x0) is automatically satisfied. In-
deed, if Ef is polar then 0 cannot belong to Ef (cf. beginning of the proof of
Proposition 1). Hence, there exists U ∈U(0) such that

U
f(z)m(dz) < ∞.
This yields

U
hα,0 (z) f (z) dz < ∞.
Theorem 1. Let α ∈(0, 2] and x0 ≥0. Suppose that f satisfies condition
(H α,x0). Then we have
Tt < ∞for all t ≥0, P-a.s.
Proof. First of all we note that the set Ef is closed. Hence we can find an
increasing sequence QN of open sets in [0, ∞) with compact closures ¯QN ⊂Ec
f
such that Ec
f = I∞
N=1 QN. We introduce the following sequence of stopping
times:

236
H.-J. Engelbert, V. Kurenok and A. Zalinescu
ρN := inf{t ≥0 :
¯
Mt ∈Qc
N} .
It is easy to see that f is integrable over QN with respect to m. The quasi-left
continuity of the process M implies the quasi-left continuity of ¯
M. From this,
the fact that Ef is polar and x0 ∈Ec
f, one can conclude that ρN increases to
infinity as N →∞, P-a.s.
We define the stopping time
σ := inf {t ≥0 : Mt ≤−x0} .
Then
 t∧ρN
0
f
 ¯
Ms

ds =
 t∧ρN∧σ
0
f (x0 + Ms) ds +
 t∧ρN
t∧ρN∧σ
f
 ¯
Ms

ds
≤
 t
0
1QN (x0 + Ms) f (x0 + Ms) ds
+et
 ∞
σ
e−s1QN
 ¯
Ms

f
 ¯
Ms

ds .
(3.2)
But the function 1QN (x0 + ·) f (x0 + ·) is integrable on the real line with
respect to the Lebesgue measure. Then, condition (Hα,x0) implies that the
assumptions of Corollary 2.2, Proposition 2.5, and Proposition 2.7 from [5] in
the cases α > 1, α = 1 and α < 1, respectively, are fulfilled. Therefore,
 t
0
1QN (x0 + Ms) f (x0 + Ms) ds < ∞.
(3.3)
We now deal with the other term of the right-hand side of the inequality (3.2).
Let
ηλ(x) :=
2
αΓ (α/2) Γ (1 + (α/2))

n(x) −λ
 ∞
0
¯gλ(x, y)m(dy)

, λ > 0 ,
(3.4)
where ¯gλ denotes the Green function of the resolvent operator corresponding
to ¯
M.
Lemma 2. For any λ > 0 and any positive Borel measurable function g, it
holds
E
 ∞
σ
e−λtg( ¯
Mt)dt

= Γ (1 + (α/2))
√
λ
E

e−λσ  ∞
0
ηλ(y)g(y)dy .
(3.5)
The formula (3.5) was proven in [22] (see the proofs of Theorem 5.2 and
Theorem 5.3) for a reflected symmetric stable process ¯
M defined on (−∞, 0].
According to the symmetry of a symmetric stable process, the behavior of the
process M on [0, ∞) is the same as the behavior of −M on (−∞, 0]. Using
this, the proof of Lemma 2 follows the same steps as the proof in [22], and we
omit the details.

Stochastic Equations Driven by Symmetric Stable Processes
237
Using the nonnegativity of the function ¯gλ(x, y) for all (x, y), relation (3.4),
and choosing λ = 1 and g = 1QN f, we obtain
E
 ∞
σ
e−s1QN
 ¯
Ms

f
 ¯
Ms

ds ≤Γ
α
2 + 1
 
QN
η1(y)f (y) dy
≤
2
αΓ (α/2)

QN
f (y) m(dy) < ∞. (3.6)
Relations (3.3) and (3.6) yield that for all t ≥0 and N ≥1, Tt∧ρN < ∞,
P-a.s., which proves the theorem.
Example 1. The aim of this example is to show that, in the case 1 < α ≤2,
 t
0
 ¯
Ms
−β ds = ∞, ∀t > 0, P-a.s.
(3.7)
if β ≥α/2 and x0 = 0. This indicates that the condition f ∈Lloc(m) seems to
be optimal for the convergence of the integral functionals
 t
0 f( ¯
Ms)ds, t > 0.
For 1 < α ≤2, it is well-known that the symmetric α-stable process M
has a local time LM (t, a), jointly continuous in (t, a) (cf., e.g., [3]). It is then
natural to ask whether that still holds in the case of the reflected process ¯
M.
For any Borel set A, let
S (t, A) :=
 t
0
1A
 ¯
Ms

ds, t ≥0 ,
denote the sojourn time of ¯
M in A. In [9], F. B. Knight proved that for every
α ∈(0, 2] there exists the local time in 0 of ¯
M, which we denote L ¯
M (t, 0). In
the case x0 = 0, the following holds:
0 < L
¯
M (t, 0) = lim
εց0 ε−α/2S (t, [0, ε)) , ∀t > 0 , P-a.s.
(3.8)
Suppose now that 1 < α ≤2. For every ω ∈Ω, the set
1
t ≥0 : ¯
Mt (ω) > 0
2
can be written as the union of pairwise disjoint intervals of the form In (ω) =
(un (ω) , vn (ω)) or [un (ω) , vn (ω)), n ≥1. As shown in the proof of Lemma
1, the reflecting force K· (ω) is constant on In. We denote this constant by
kn (ω). If a > 0 we define
L
¯
M(t, a) :=
∞

n=1

LM (vn ∧t, a −x0 −kn) −LM (un ∧t, a −x0 −kn)

, t ≥0 .
(3.9)
We give a concise proof of the occupation times formula for L ¯
M, i.e.,
 t
0
g
 ¯
Ms

ds =
 ∞
0
g (a) L
¯
M (t, a) da , ∀t ≥0 ,

238
H.-J. Engelbert, V. Kurenok and A. Zalinescu
for every positive measurable function g, P-a.s. By (3.8) and the strong
Markov property of ¯
M (when considered as such),
µ
1
t ≥0 : ¯
Mt (ω) = 0
2
= 0 , P-a.s.
(recall that µ denotes the Lebesgue measure on the positive half-line). There-
fore it is sufficient to show the occupation times formula only for the function
of the type g ≡1A, where A is a Borel set in (0, ∞). Integrating with respect
to a ∈A in (3.9) and using the occupation times formula for LM, we obtain

A
L
¯
M (t, a) da =
∞

n=1

A−x0−kn

LM (vn ∧t, a) −LM (un ∧t, a)

da
=
∞

n=1
 vn∧t
un∧t
1A−x0−kn (Ms) ds =
∞

n=1
 vn∧t
un∧t
1A
 ¯
Ms

ds
=
 ∞
0
1A
 ¯
Ms

ds, t ≥0 .
That means L ¯
M (t, a) is a possible candidate for the local time of the
process ¯
M.
The equality (3.7) is then a consequence of the occupation times formula.
Indeed, from this it follows
 t
0
 ¯
Ms
−β ds =
 ∞
0
a−βL
¯
M (t, a) da , ∀t ≥0 , P-a.s. ,
and
S (t, [0, ε)) =
 ε
0
L
¯
M (t, a) da , ∀t , ε > 0 , P-a.s.
Using integration by parts and (3.8), for sufficiently small ε > 0, we obtain
 t
0
 ¯
Ms
−β ds ≥
 1
ε
a−βL
¯
M (t, a) da ≥
 1
ε
a−α/2L
¯
M (t, a) da
= S (t, [0, 1)) −ε−α/2S (t, [0, ε)) + α
2
 1
ε
a−α
2 −1S (t, [0, a)) da
≥−ε−α/2S (t, [0, ε)) + α
4 L
¯
M (t, 0)
 √ε
ε
a−1da
≥1
8L
¯
M (t, 0) (−α ln ε −16) .
The result then follows by letting ε →0.
Of course, if β < α/2, Theorem 1 ensures us that
 t
0( ¯
Ms)−βds < ∞,
∀t ≥0. This means that α/2 is the critical exponent for the convergence or
the divergence of the integral.
Let us now discuss briefly the conditions ensuring that

Stochastic Equations Driven by Symmetric Stable Processes
239
T∞=
 ∞
0
f( ¯
Ms)ds = ∞.
Because the process
¯
M is a recurrent one, it is logically to expect to have
similar sufficient conditions found for the symmetric stable process of index
α ∈(1, 2], e.g., see [5].
Theorem 2. Suppose that µ ({a : f(a) > 0}) > 0. Then, for all x0 ≥0 and
α ∈(0, 2], T∞= ∞, P-a.s.
Proof. For the convenience of the reader, we give a proof which is slightly
different of that of Proposition 2.6 [5].
It is sufficient to prove the assertion in the case f = 1A, where A is an
arbitrary Borel measurable set with µ(A) > 0.
Let ε > 0. By the strong Markov property of ¯
M, we have that for every
n ∈N
P0
 ∞
0
1A( ¯
Ms)ds > ε

= P ¯
Mτn
 ∞
0
1A( ¯
Ms)ds > ε

= Px0
 ∞
τn
1A( ¯
Ms)ds > ε
 Fτn

, Px0-a.s. ,
with τn defined by (2.7). The fact that lim
n→∞τn = ∞, Px0-a.s., allows us to pass
to the limit as n →∞in this relation; from the theorem of Lebesgue-L´evy on
the convergence of conditional expectations we obtain that
P0
 ∞
0
1A( ¯
Ms)ds > ε

= 1=
n∈N
/ ∞
τn 1A( ¯
Ms)ds>ε
0, Px0-a.s.
In the proof of Proposition 1, we have shown that µ(A) > 0 implies U (0, A) =
∞; thus P0
 ∞
0
1A( ¯
Ms)ds > ε

> 0. Consequently,
Px0
	 ?
n∈N
 ∞
τn
1A( ¯
Ms)ds > ε

= 1 .
Using once again the unboundedness of the sequence (τn)n∈N, this relation
gives
 ∞
0
1A( ¯
Ms)ds = ∞, Px0-a.s. ,
which proves Theorem 2.
4 Existence and Uniqueness of Solutions
Let us consider a Borel measurable function b : [0, ∞) →R, an arbitrary
initial value x0 ≥0 and an arbitrary stability index α ∈(0, 2]. We also define
the set

240
H.-J. Engelbert, V. Kurenok and A. Zalinescu
Nb := {x ≥0 : b(x) = 0} .
Theorem 3. Assume that |b|−α satisfies condition (H α,x0). Then there exists
a (non-exploding) solution X of (1.1) with X0 = x0. For this solution, the
property
 ∞
0
1Nb (Xs) ds = 0 , P-a.s.
is satisfied.
Proof. On a stochastic basis (Ω, F, P; F) we consider a symmetric α-stable
process (M ∗, F) and the corresponding reflected process ¯
M ∗, defined by
K∗
t := sup
0≤s≤t
max (−M ∗
s −x0, 0) ;
¯
M ∗
t := x0 + M ∗
t + K∗
t .
(4.1)
Let
Tt =
 t
0
|b|−α ( ¯
M ∗
s )ds, t ≥0 ,
(4.2)
and
At = inf{s ≥0 : Ts > t} .
It follows from Theorem 1 that T is a P-a.s. finite and continuous F-adapted
process with T0 = 0. Clearly, the condition of Theorem 2 is satisfied because
|b|−α is strictly positive. (Note that |b|−α (x) = ∞if b (x) = 0). Consequently,
T∞= ∞. Due to its definition, the process A is then a right-continuous F-time
change defined for all t ∈[0, ∞). The condition T∞= ∞means that At < ∞
for all t > 0, and we have A∞:= limt→∞At = ∞, since T is finite. Moreover,
the process A is continuous on [0, ∞) because T is strictly increasing, which is
also a consequence of the strict positivity of |b|−α. One can easily check that
A = T −1.
On the other side, the process ¯
M ∗is a right-continuous semimartingale
because M ∗is a right-continuous semimartingale and K∗is a right-continuous
and increasing process. Then due to the well-known time change theorem for
semimartingales (see, e.g., [6], Theorem 10.16), the process (X, G), where
Xt := ¯
M ∗
At, Gt := FAt, t ≥0 ,
(4.3)
is again a right-continuous semimartingale. From (4.1) we then have
Xt = x0 + M ∗
At + K∗
At, t ≥0 .
Obviously, Xt ≥0 for all t ≥0. We put ˜
Mt = M ∗
At and Kt = K∗
At.
Lemma 3. The process K is a reflecting force for X, i.e., K is increasing,
right-continuous, K0 = 0 and
 ∞
0
1{Xs̸=0}dKs = 0 .
(4.4)

Stochastic Equations Driven by Symmetric Stable Processes
241
Proof. It follows directly from the definition of the process K∗and the con-
tinuity of A that K is also a right-continuous and increasing process with
K0 = 0. Moreover, for every t ≥0, it holds
Kt =
sup
0≤s≤At
max(−M ∗
s −x0, 0)
= sup
0≤s≤t
max(−M ∗
As −x0, 0)
= sup
0≤s≤t
max(−˜
Ms −x0, 0) .
Consequently, we have
Xt = x0 + ˜
Mt + sup
0≤s≤t
max(−˜
Ms −x0, 0) ,
and from Lemma 1 it follows that the relation (4.4) is true.
Lemma 4. It holds
E
 t
0
1Nb( ¯
M ∗
s−)ds

= E
 t
0
1Nb( ¯
M ∗
s )ds

= 0 , ∀t ≥0 .
Proof. Using Lemma 2 for the function g = 1Nb\E|b|−α and λ = 1, we estimate
E
 t
0
g( ¯
M ∗
s )ds

≤E
 σ∧t
0
g(x0 + M ∗
s )ds

+ etE
 ∞
σ
e−sg( ¯
M ∗
s )dt

≤
 t
0
P

x0 + M ∗
s ∈Nb\E|b|−α

ds +
2et
αΓ (α/2)
 ∞
0
g(y)m (dy) .
It is obvious that m(Nb\E|b|−α) = 0. The right-hand side is then equal to zero
due to the equivalence between the Lebesgue measure and m, on one hand,
and to the absolute continuity of the distribution of M ∗
s , on the other hand.
The polarity of E|b|−α is used in order to finish the proof.
Lemma 5. There exists a symmetric stable process M of the same index α
such that for all t ≥0 we have
˜
Mt =
 t
0
b(Xs−)dMs .
(4.5)
Proof. Because we have Tt < ∞for every t ≥0 and the integrand |b|−α ( ¯
M ∗
t )
is Ft-measurable, we can conclude that for all t ≥0 there exists the stochastic
integral
 t
0 b−1( ¯
M ∗
s−)dM ∗
s (cf. [13], [7]). On the other side, from the time

242
H.-J. Engelbert, V. Kurenok and A. Zalinescu
change properties for stochastic integrals with respect to stable processes (cf.,
e.g., [5] or [13]) it follows that the process M, defined by
Mt :=
 At
0
b−1( ¯
M ∗
s−)dM ∗
s , t ≥0 ,
(4.6)
is a G-adapted symmetric α-stable process.
A simple use of Lemma 4 shows that
At =
 At
0
1Nc
b
 ¯
M ∗
s

ds =
 At
0
|b|α ( ¯
M ∗
s ) |b|−α ( ¯
M ∗
s )ds , t ≥0 .
Consequently, changing the variables in the Lebesgue-Stieltjes integral, from
relation (4.2) and A = T −1 we obtain
At =
 At
0
|b|α ( ¯
M ∗
s )dTs =
 TAt
0
|b|α  ¯
M ∗
As

ds =
 t
0
|b|α (Xs)ds , t ≥0 .
Therefore, with similar arguments as above, we have that there exists the
stochastic integral
 t
0
b(Xs−)dMs , t ≥0 .
(4.7)
Now, using time change properties for stochastic integrals with respect to
semimartingales (see, e.g. [6], Chap. X) and taking into account (4.6) and
(4.7), we obtain
Mt =
 At
0
b−1( ¯
M ∗
s−)dM ∗
s =
 t
0
b−1(Xs−)dM ∗
As, t ≥0 ,
and, consequently,
 t
0
b(Xs−)dMs =
 t
0
b(Xs−)b−1(Xs−)dM ∗
As , t ≥0 .
(4.8)
From Lemma 4 we can conclude
 t
0
1Nb( ¯
M ∗
s−)dM ∗
s = 0, ∀t ≥0 , P-a.s. ,
which implies that
 t
0
b( ¯
M ∗
s−)b−1( ¯
M ∗
s−)dM ∗
s = M ∗
t , ∀t ≥0 , P-a.s.
Using once again the properties of time change for stochastic integrals, we
have
 t
0
b(Xs−)b−1(Xs−)dM ∗
As = M ∗
At , ∀t ≥0 , P-a.s.
Combined with (4.8), this relation yields (4.5).

Stochastic Equations Driven by Symmetric Stable Processes
243
We have shown that the process X has the form
Xt = x0 +
 t
0
b(Xs−)dMs + Kt , t ≥0 ,
where K is the reflecting force for X. Therefore, X is a solution of (1.1). From
Lemma 4 one can easily conclude that X also satisfies
 ∞
0
1Nb (Xs) ds = 0 , P-a.s.
This completes the proof of Theorem 3.
Remark. For α = 2 the assumption |b|−α ∈Lloc(m) reduces to the condition
that b−2 is locally integrable over the half-line [0, ∞), which coincides with
the condition found by W. M. Schmidt [16] for the case of a Brownian motion.
Finally we investigate the uniqueness in law of the solution of (1.1). At first
we notice that, in general, condition (Hα,x0) does not ensure the uniqueness
in law of the solution. We give the following general, but very simple example.
Example 2. Let the volatility b be such that |b|−α satisfies condition (Hα,x0).
Suppose that b (x0) = 0. Then the solution X of (1.1) with X0 = x0 is not
unique in law. Indeed, according to Theorem 3, there is a solution X of (1.1)
such that
 ∞
0
1Nb (Xs) ds = 0 , P-a.s.
On the other side, we may put Y ≡x0; obviously, Y is a solution of (1.1) with
Y0 = x0. It is clear that X and Y have different laws.
This example can be generalized as follows. Suppose that |b|−α satisfies
condition (Hα,x0). Let X be the solution of (1.1) constructed in the proof of
Theorem 3.
We assume that the first entry time D (Nb) of X into Nb,
D (Nb) := inf {t ≥0 : b (Xt) = 0} ,
is finite with positive probability:
P (D (Nb) < ∞) > 0 .
Then the process Y obtained by stopping X at D (Nb),
Yt := Xt∧D(Nb) , t ≥0 ,
is again a solution of (1.1) with Y0 = x0 and, obviously, the laws of X and Y
are different. This motivates the following
Definition 3. Let condition (H x0,α) for |b|−α be satisfied. A solution X of
(1.1) is called a fundamental solution if it holds

244
H.-J. Engelbert, V. Kurenok and A. Zalinescu
 ∞
0
1Nb (Xs) ds = 0 , P-a.s.
(4.9)
It is natural to expect that the solution X of (1.1) with X0 = x0 is unique
in law in the class of fundamental solutions. For preparing this result, let X
be an arbitrary solution of (1.1) with X0 = x0 given on the stochastic basis
(Ω, F, P; F). Put
At :=
 t
0
|b|α (Xs) ds ,
t ≥0 .
(4.10)
From [7], [13] we know that At < ∞, t ≥0, P-a.s. and hence is a P-a.s. finite
continuous FX-adapted process. We introduce the right inverse T = (Tt)t≥0
of A:
Tt := inf {s ≥0 : As > t} ,
t ≥0 .
By G := FX ◦T we denote the filtration

FX
Tt

t≥0. To begin with, we will
prove the following representation of the solution X.
Proposition 2. On a, possibly, enlarged stochastic basis (Ω′, F′, P ′; F′) there
exists a reflected symmetric stable process ¯
M ∗of index α with ¯
M ∗
0 = x0 such
that
Xt = ¯
M ∗
At , t ≥0 , P-a.s.
(4.11)
Proof. We have
Xt = x0 +
 t
0
b (Xs−) dMs + Kt , t ≥0 ,
where M is a symmetric stable process of index α (with M0 = 0) and K is a
reflecting force for X. According to [5] (Proposition 4.3), changing the roles
of A and T, the process ˜
M ∗= ( ˜
M ∗
t )t≥0 defined by
˜
M ∗
t :=
 Tt
0
b (Xs−) dMs , t ≥0 ,
is a symmetric stable process of index α stopped at AT∞−= A∞(this latter
equality holds because T∞= ∞P-a.s.). Using [5] (Lemma 4.2), we obtain
that there exists a symmetric stable process M ∗of index α (on a certain
extension of (Ω, F, P; G)) such that
˜
M ∗
t = M ∗
t∧A∞, t ≥0 .
We now define the reflected symmetric stable process ¯
M ∗and the reflecting
force K∗by (4.1). In order to verify relation (4.11), we first remark that, for
all t ≥0,
M ∗
At = ˜
M ∗
At =
 TAt
0
b (Xs−) dMs =
 t
0
b (Xs−) dMs ,

Stochastic Equations Driven by Symmetric Stable Processes
245
the latter being true because [t, TAt] are intervals of constancy for A and hence
for
 ·
0 b (Xs−) dMs (cf. [5], Proposition 4.3 (iv)). Furthermore, for all t ≥0,
K∗
At =
sup
0≤s≤At
max (−M ∗
s −x0, 0) = sup
0≤s≤t
max

−M ∗
As −x0, 0

= sup
0≤s≤t
max

−
 s
0
b (Xu−) dMu −x0, 0

= Kt ,
the reflecting force for X, because of Lemma 1. This proves ¯
M ∗
At = Xt, t ≥0,
and hence Proposition 2.
Next we give a representation for the increasing process T = (Tt)t≥0.
Proposition 3. Suppose that the volatility b is such that |b|−α satisfies condi-
tion (H α,x0) and that X is a fundamental solution of (1.1) with X0 = x0. Let
¯
M ∗be a reflected symmetric α-stable process with
¯
M ∗
0 = x0 on a, possibly,
enlarged stochastic basis, satisfying (4.11). Then
Tt =
 t
0
|b|−α ( ¯
M ∗
s )ds , t ≥0 , P-a.s.
(4.12)
Proof. From (4.9) and (4.11), we obtain
Tt =
 Tt
0
|b|−α (Xs) dAs =
 Tt
0
|b|−α ( ¯
M ∗
As)dAs
and, by time change in this Lebesgue-Stieltjes integral, we get
Tt =
 ATt
0
|b|−α ( ¯
M ∗
ATs )ds .
In view of the continuity of A, we conclude ATt = t ∧A∞and hence
Tt =
 t∧A∞
0
|b|−α ( ¯
M ∗
s )ds .
(4.13)
This yields (4.12) for t ≤A∞. In particular,
 A∞
0
|b|−α ( ¯
M ∗
s )ds = TA∞= ∞.
From this, we observe that (4.12) also holds for t > A∞.
The next proposition shows, in particular, that the representation (4.12)
do hold on the same stochastic basis (Ω, F, P; G) if |b|−α satisfies condition
(Hα,x0) and if X is a fundamental solution. In this case, there is no need for
an enlargement.

246
H.-J. Engelbert, V. Kurenok and A. Zalinescu
Proposition 4. Suppose that |b|−α satisfies condition (H α,x0). Let X be a
fundamental solution of (1.1) with X0 = x0. Then
A∞=
 ∞
0
|b|α (Xs) ds = ∞P-a.s.
Proof. The assertion means that
Tt < ∞, t ≥0 , P-a.s.
But the latter property follows from the equality
Tt =
 t
0
|b|−α  ¯
M ∗
s

ds , t ≥0 , P-a.s. ,
cf. Proposition 3 and Theorem 1 for the reflected symmetric α-stable process
¯
M ∗with ¯
M ∗
0 = x0 of Proposition 2.
Now we turn to the uniqueness in law of the fundamental solution.
Theorem 4. Suppose that the volatility b is such that |b|−α satisfies condition
(H α,x0). Then the fundamental solution X of (1.1) with X0 = x0 (which exists
by Theorem 3) is unique in law. Furthermore,
 ∞
0
|b|α (Xs) ds = ∞, P-a.s.
Proof. Let X be a fundamental solution of (1.1) with X0 = x0. According to
Proposition 2, X is a well-defined measurable functional of
 ¯
M ∗, A

, where
¯
M ∗is a reflected symmetric stable process of index α with ¯
M ∗
0 = x0. Further-
more, Proposition 3 yields that T, and hence A, is a well-defined measurable
functional of ¯
M ∗. Thus we may conclude that X is a well-defined measurable
functional of ¯
M ∗. So, the law of X on the Skorokhod space is the image law
of ¯
M ∗by this measurable mapping and hence uniquely determined. The last
statement is exactly the conclusion of Proposition 4.
Corollary. Suppose that |b|−α satisfies condition (H α,x0) and, moreover,
b (x) ̸= 0 , ∀x ≥0 .
Then the solution X of (1.1) with
X0 = x0 exists and is unique in law.
Furthermore, it holds
 ∞
0
|b|α (Xs) ds = ∞P-a.s.
In conclusion, we note that the fundamental solution X of (1) is nothing
else than a reflected symmetric α-stable process ¯
M ∗taken in another, ran-
dom clock A given by (4.10) and satisfying the additional property A∞= ∞.

Stochastic Equations Driven by Symmetric Stable Processes
247
In other words, the process X is running through the same trajectories as a
reflected symmetric α-stable process but in different clocks. So, roughly speak-
ing, the fundamental solution X of (1.1) has the same recurrence behaviour as
a a reflected symmetric α-stable process. In particular, X hits the boundary
0 infinitely often P-a.s. Moreover, if 1 < α < 2, as for α = 2, the process X
has a local time LX in the sense of a occupation time density, given by
LX(t, a) = L
¯
M ∗(At, a) ,
t ≥0 .
Indeed, it can easily be verified that for every nonnegative Borel function g
on [0, ∞)
 t
0
g(Xs) dAs =
 ∞
0
g(a) LX(t, a) da ,
t ≥0 ,
P-a.s.
or, alternatively,
 t
0
g(Xs) ds =
 ∞
0
g(a) LX(t, a) µb(da) ,
t ≥0 ,
P-a.s.
where the measure µb is given by µb(da) = |b|−α(a) µ(da).
In the first formula, the occupation time is measured by dAs, but the
occupation time density is taken with respect to the Lebesgue measure µ on
[0, ∞), whereas in the second formula the occupation time is measured by ds,
however, in this case, the occupation time density is taken with respect to the
new measure µb depending on the volatility b.
Acknowledgement
The authors would like to express their gratitude to Professor Albert Shiryaev
for his interest in the course of the preparation of this paper. His discussions
and comments were very helpful and gave an improvement of an earlier version
of the present paper in several aspects.
References
1. Bertoin, J.: L´evy Processes. Cambridge University Press, 1996
2. Blumenthal, R. M., Getoor, R. K.: Markov Processes and Potential Theory.
Academic Press, New York, 1968
3. Boylan, E. S.: Local times for a class of Markov processes. Illinois J. Math. 8,
pp. 19–39 (1964)
4. Chung, K. L., Williams, R. J.: Introduction to Stochastic Integration. Birkh¨auser
Verlag, 1983

248
H.-J. Engelbert, V. Kurenok and A. Zalinescu
5. Engelbert, H. J., Kurenok, V. P.: On one-dimensional stochastic equations
driven by symmetric stable processes. in: Buckdahn, R., Engelbert, H. J.,
Yor, M. (eds), Stochastic Processes and Related Topics, pp. 81–110, Taylor and
Francis Group, 2002
6. Jacod, J.: Calcul Stochastique et Probl`emes de Martingales. Lecture Notes in
Math., Vol. 714, Springer-Verlag, Berlin, 1979
7. Jacod, J., Shiryaev, A.: Limit theorems for stochastic processes. 2nd ed.,
Grundlehren der Mathematischen Wissenschaften, Vol. 288, Springer-Verlag,
Berlin, 2003
8. Kallenberg, O.: Foundations of Modern Probability. Springer Verlag, 1998
9. Knight, F. B.: The local time at zero of the reflected symmetric stable process.
Z. Wahrscheinlichkeitstheorie verw. Geb. 19, pp. 180–190 (1971)
10. Pragarauskas, H., Zanzotto, P. A.: On one-dimensional stochastic differential
equations driven by stable processes. Liet. Mat. Rink., Vol. 40, N 1, pp. 1–24
(2000)
11. Ray, D.: Stable processes with an absorbing barrier. Trans. Am. Math. Soc. 87,
pp. 187–197 (1958)
12. Revuz, D., Yor, M.: Continuous Martingales and Brownian Motion. Springer
Verlag, 1994
13. Rosi´nski, J., Woyczy´nski, W.: On Itˆo stochastic integration with respect to p-
stable motion: inner clock, integrability of sample paths, double and multiple
integrals. Ann. Probab., Vol. 14, N 1, pp. 271–286 (1986)
14. Rozkosz, A., S^lomi´nski, L.: On stability and existence of solutions of SDEs with
reflection an the boundary. Stoch. Process. Appl. 68, pp. 285–302 (1997)
15. Sato, K.: L´evy Processes and Infinitely Divisible Distributions. Cambridge Uni-
versity Press, 1999
16. Schmidt, W. M.: On stochastic differential equations with reflecting barriers.
Math. Nachr., Vol. 142, pp. 135–148 (1989)
17. Skorohod, A. V.: Stochastic equations for diffusion processes in a bounded re-
gion. Theory Probab. Appl. 6, pp. 264–274 (1961)
18. Skorohod, A. V.: Random Processes with Independent Increments. Kluwer, Dor-
drecht, Netherlands, 1991
19. S^lomi´nski, L.: On existence, uniqueness and stability of solutions of multidimen-
sional SDE’s with reflecting boundary condition. Inst. Henri Poincar´e 29, N 2,
pp. 169–198 (1993)
20. S^lomi´nski, L.: On approximation of solutions of multidimensional SDE’s with
reflecting boundary conditions. Stoch. Process. Appl. 50, pp. 197–219 (1994)
21. Tanaka, H.: Stochastic differential equations with reflecting boundary condition
in convex regions. Hiroshima Math. J. 9, pp. 163–177 (1978)
22. Watanabe, S.: On stable processes with boundary conditions, J. Math. Soc.
Japan, Vol. 14, N 2, pp. 170–198 (1962)
23. Zanzotto, P. A.: On solutions of one-dimensional stochastic differential equations
driven by stable L´evy motion. Stoch. Process. Appl. 68, pp. 209–228 (1997)
24. Zanzotto, P. A.: On stochastic differential equations driven by a Cauchy process
and other stable L´evy motions. Ann. Probab. 30, N 2, pp. 802–825 (2002)

A Note on Pricing, Duality and Symmetry for
Two-Dimensional L´evy Markets
Jos´e FAJARDO1 and Ernesto MORDECKI2
1 IBMEC Business School, Rio de Janeiro - Brazil.
pepe@ibmecrj.br
2 Centro de Matem´atica, Facultad de Ciencias, Universidad de la Rep´ublica,
Montevideo, Uruguay.
ernesto.mordecki@gmail.com
Summary. The aim of this work is to use a duality approach to study the pricing of
derivatives depending on two stocks driven by a two-dimensional L´evy process. The
main idea is to apply Girsanov’s theorem for L´evy processes, in order to reduce the
problem to the pricing of a one L´evy driven stock in an auxiliary market, baptized
as the “dual market”. In this way, we extend the results obtained by Gerber and
Shiu [5] for two-dimensional Brownian motion. Additionally, we obtain a put-call
relationship, that we call duality, and also a condition in order to have a symmetry
property in a L´evy market.
Key words: L´evy processes, optimal stopping, Girsanov’s theorem, dual market
method, derivative pricing, symmetry
Mathematics Subject Classification (2000): 60G51, 91B28
JEL Classification Numbers: G12, G13
1 Introduction
Since Margrabe’s 1978 paper [8], many important extensions have been car-
rying on to study derivatives written on two stocks. Margrabe studied the
pricing of European options for the case of two non-dividend-paying stocks
driven by a pair of Brownian motions, more exactly, the pricing of the right to
change one asset for another at the end of some fixed period of time, and ob-
tained closed-form formulas for this problem, extending in this way the Black
and Scholes pricing model.
The American option pricing problem leads to the solution of an optimal
stopping problem which, in general, does not admit closed form solutions,

250
J. Fajardo and E. Mordecki
even in the one-asset model (see Jacka [6]). In the perpetual case, i.e. when
the option has no expiration date, Gerber and Shiu [5] obtain a closed-form
formula for Margrabe’s and other related options using the optional sampling
theorem, assuming that stock prices are driven by geometric Brownian mo-
tions, possibly constantly correlated, and stocks pay constant rate continuous
dividends.
In the present paper we consider the problem of pricing European and
American type derivatives written on a two-dimensional stock driven by a
two-dimensional L´evy process (it can be said that the stock follows a two-
dimensional geometric L´evy process), with a pay-offfunction homogeneous
of an arbitrary degree. Additionally, the interest rate can also be stochastic,
modelled by a third geometric L´evy process. As a related result, we obtain a
relation between prices of call and put vanilla options in L´evy markets, and a
condition on the jump structure of the process in order to have a symmetric
L´evy market.
The paper is organized as follows: in Section 2 we describe the market
model and introduce the pricing problem. In Section 3 we describe the Dual
Market Method, which allows us to reduce the two-stock problem with sto-
chastic interest rate into a one-stock problem with a deterministic interest
rate. In Section 4 we study duality and symmetry in L´evy markets. A short
conclusion is given in Section 5.
2 Market Model
2.1 Multidimensional L´evy Processes
Let X = (X1, . . . , Xd) be a d-dimensional L´evy process defined on a sto-
chastic basis B = (Ω, F, {Ft}t≥0, P). This means that X is a stochastically
continuous stochastic process with independent increments such that the dis-
tribution of Xt+s −Xs does not depend on s, with X0 = 0 and trajectories
continuous from the left with limits from the right. The filtration {Ft}t≥0 is
supposed to satisfy the usual assumptions, i.e. continuity from the right and
F0 containing the P-null sets. For z = (z1, . . . , zd) in Cd, when the integral
is convergent (this is always the case if z = iλ with λ in Rd), the L´evy–
Khinchine formula states that EezXt = exp(tψ(z)) where the function ψ is
the characteristic exponent of the process, and is given by
ψ(z) = (a, z) + 1
2(z, Σz) +

Rd

e(z,y) −1 −(z, y)1{|y|≤1}

Π(dy),
(2.1)
where a = (a1, . . . , ad) is a vector in Rd, Π is a positive measure defined on
Rd \ {0} such that

Rd(|y|2 ∧1)Π(dy) is finite, and Σ = ((sij)) is a symmetric
nonnegative definite matrix which can always be written as Σ = A′A (where
′ denotes the transpose) for some matrix A.

Pricing in Two-Dimensional L´evy Markets
251
The triplet (a, Σ, Π) completely determines the law of the process X.
Particular interest has the case when α =

Rd Π(dy) is finite, i.e. X is a
diffusion with jumps. Introducing F by Π(dy) = αF(dy), the L´evy–Khinchine
formula is (changing the value of a if necessary)
ψ(z) = (a, z) + 1
2(z, Σz) +

Rd

e(z,y) −1

Π(dy),
(2.2)
and the process X = {Xt}t≥0 can be represented by
Xt = at + AWt +
Nt

k=1
Yk,
where W is a standard d-dimensional Brownian motion, N = {Nt}t≥0 is a
Poisson process with parameter α, and {Yk}k≥1 is a sequence of independent
d-dimensional random vectors with identical distribution F(dy).
Another important case is when the coordinates of X are independent
processes. This happens if and only if Σ is a diagonal matrix (and A can be
chosen to be diagonal also) and the measure Π has support on the union of
the coordinate axes, see E 12.10 in Sato [10]. In this case ψ(z) = d
k=1 ψk(zk),
where ψk is the characteristic exponent of the k-coordinate of X, given by
ψk(zk) = akzk + 1
2skkz2
k +

R

ezky −1 −zky1{|y|≤1}

Πk(dy),
where Πk(A) =

{x∈Rd : xk∈A} Π(dx).
2.2 Market and Problem
Consider a market model with three assets (S1, S2, S3) given by
S1
t = eX1
t ,
S2
t = S2
0eX2
t ,
S3
t = S3
0eX3
t
(2.3)
where (X1, X2, X3) is a three-dimensional L´evy process; for simplicity and
without loss of generality we take S1
0 = 1. The first asset is the bond and
is usually deterministic. Randomness in the bond {S1
t }t≥0 allows us to con-
sider more general situations, for example, the pricing problem of a derivative
written in a foreign currency, referred as Quanto Option.
Consider a function
f : (0, ∞) × (0, ∞) →R
homogeneous of a degree α; i.e. for any λ > 0 and for all positive x, y
f(λx, λy) = λαf(x, y).

252
J. Fajardo and E. Mordecki
In the above market a derivative contract with pay-offgiven by
Φt = f(S2
t , S3
t )
is introduced. Taking various homogeneous functions f we obtain several
examples of options considered in the literature: Options to Default, Mar-
grabe’s Options, Swap Options, Quanto Options, and Equity-Linked Foreign
Exchange Options. See the details in [3].
Assuming that we are under a risk-neutral martingale measure, i.e. Sk
S1 , k =
2, 3, are P-martingales (P is an equivalent martingale measure), we want
to price the derivative contract just introduced. In the European case, the
problem is reduced to the computation of
ET = E(S2
0, S3
0, T) = E
)
e−X1
T f(S2
0eX2
T , S3
0eX3
T )

.
(2.4)
In the American case, if MT denotes the class of stopping times up to time
T, i.e:
MT = {τ : 0 ≤τ ≤T, τis a stopping time}
(with T = ∞for the perpetual case), the problem of pricing the American-
type derivative consists in solving an optimal stopping problem, more pre-
cisely, in finding the value function AT and an optimal stopping time τ ∗in
MT such that
AT = A(S2
0, S3
0, T) = sup
τ∈MT
E
)
e−X1
τ f(S2
0eX2
τ , S3
0eX3
τ3 )

= E
)
e−X1
τ∗f(S2
0eX2
τ∗, S3
0eX3
τ∗)

.
3 Dual Market Method
The main idea to solve the posed problems is the following: make a change
of measure through Girsanov’s theorem for L´evy processes, in order to re-
duce the original problems to a pricing problems for an auxiliary derivative
written on one L´evy driven stock in an auxiliary market with deterministic
interest rate. This method was used in Shepp and Shiryaev [11] and Kramkov
and Mordecki [7] with the purpose of pricing American perpetual options
with path-dependent pay-offs. It was employed by Araujo and Oliveira [1] to
consider the pricing of swaps, and is strongly related with the choice of the
num´eraire (see Geman et al. [4]). This auxiliary market will be called the Dual
Market.
Observe that
e−X1
t f(S2
0eX2
t , S3
0eX3
t ) = e−X1
t +αX3
t f(S2
0eX2
t −X3
t , S3
0).

Pricing in Two-Dimensional L´evy Markets
253
Put ρ = −log Ee−X1
1+αX3
1 , we assume finite. The process
Zt = e−X1
t +αX3
t +ρt
(3.1)
is a density process (i.e. a positive martingale starting at Z0 = 1) that allow
us (under some hypothesis on the filtered space) to introduce a new measure,
the dual martingale measure ˜P, by its restrictions to each Ft by the formula
d ˜Pt
dPt
= Zt.
Denote now ˜Xt = X2
t −X3
t and St = S2
0e ˜
Xt. Finally, let
F(x) = f(x, S3
0).
With the introduced notations, under the change of measure we obtain our
main results:
ET = ˜E

e−ρT F(ST )

,
AT = sup
τ∈MT
˜E

e−ρτF(Sτ)

.
(3.2)
The concluding step to compute the prices in (3.2) is to determine the law
of the process X under the auxiliary probability measure ˜P, what is done in
the following result, whose proof can be found in [3].
Lemma 3.1. Let X be a L´evy process on Rd with characteristic exponent
given in (2.1). Let u and v be vectors in Rd. Assume that Ee(u,X1) is finite,
and denote ρ = −log Ee(u,X1) = −ψ(u). In this conditions, introduce the
probability measure ˜P by its restrictions ˜Pt to each Ft by
d ˜Pt
dPt
= exp[(u, Xt) + ρt].
Then:
(a) The law of one-dimensional L´evy process {(v, Xt)}t≥0 under ˜P is given
by the triplet



˜a = (a, v) + 1
2[(v, Σu) + (u, Σv)] +

Rd e(u,y)(v, y)1{|(v,y)|≤1,|x|>1}Π(dx)
˜σ2 = (v, Σv)
˜π(A) =

Rd 1{(v,y)∈A}e(u,y)Π(dy).
(3.3)
(b) In the particular case when X is a diffusion with jumps which char-
acteristic exponent given in (2.2) the law of one-dimensional L´evy process
{(v, Xt)}t≥0 under ˜P is given by the triplet



˜a = (a, v) + 1
2[(v, Σu) + (u, Σv)]
˜σ2 = (v, Σv)
˜π(A) =

Rd 1{(v,y)∈A}e(u,y)Π(dy).
(3.4)

254
J. Fajardo and E. Mordecki
Furthermore, the intensity of the Poisson process under ˜P is given by
˜α =

Rd e(u,y)Π(dy) = α

Rd e(u,y)F(dy).
(c) Assume (b), and let Π(dy) = αF(dy) where F is the common distrib-
ution of the random variables {Yk}k≥1 with the characteristic function
ϕ(z) =

Rd e(z,y)F(dy).
Then the characteristic function of the same random variables under ˜P is
given by
˜ϕ(θ) = ϕ(θv + u)
ϕ(u)
.
(3.5)
4 Put-Call Duality and Symmetry
In this section, relying on the same type of arguments of previous sections, we
obtain a relationship between call and put vanilla options, that holds both in
the European and in the American case, that we refer to as put-call duality.
Based on this relation, we obtain conditions to have put-call symmetry.
In order to do this, with the previous notations, consider X1
t = rt, X2
t = 0
and X3
t = Xt, with Xt a L´evy process. In other words, we have a market with
two assets, Bt = ert and St = S0eXt, S0 > 0.
We also assume that the stock pays dividends, with constant rate δ ≥0,
and as in section 2, that the probability measure P is the chosen to be an equiv-
alent martingale measure. In other words, prices are computed as expectations
with respect to P, and the discounted and reinvested process {e−(r−δ)tSt} is
a P-martingale.
Let us assume that τ is a stopping time with respect to the given filtration
{Ft}. Introduce the notation
C(S0, K, r, δ, τ, ψ) = Ee−rτ(Sτ −K)+,
(4.1)
P(S0, K, r, δ, τ, ψ) = Ee−rτ(K −Sτ)+.
(4.2)
If τ = T, where T is a fixed constant time, then formulas (4.1) and (4.2) give
the price of the European call and put options respectively.
Proposition 1 (Put-Call duality). Consider a L´evy market with driving
process X with characteristic exponent ψ(z) given by
ψ(q) = iaq −1
2σ2q2 +

R

eiqy −1 −iqy1{|y|<1}

Π(dy),
(4.3)

Pricing in Two-Dimensional L´evy Markets
255
defined on the set
C0 =
/
z = p + iq ∈C:

{|y|>1}
epyΠ(dy) < ∞
0
.
(4.4)
Then for the expectations introduced in (4.1) and (4.2) we have
C(S0, K, r, δ, τ, ψ) = P(K, S0, δ, r, τ, ˜ψ),
(4.5)
where
˜ψ(z) = ˜az + 1
2 ˜σ2z2 +

R

ezy −1 −zy1{|y|≤1}
 ˜Π(dy)
(4.6)
is a characteristic exponent (of a certain L´evy process) that satisfies
˜ψ(z) = ψ(1 −z) −ψ(1),
for 1 −z ∈C0.
In consequence,





˜a
= δ −r −σ2/2 −

R

ey −1 −y1{|y|≤1}
 ˜Π(dy),
˜σ
= σ,
˜Π(dy)
= e−yΠ(−dy).
(4.7)
The proof of this proposition can be found in [3].
Observe that if we take a deterministic time τ = T in (4.5), we obtain
that the price of an European call option in the risk-neutral market (when
X has a law characterized by ψ) coincides with the price of an European put
option (with different parameters) in the dual market (when X has a law
characterized by ˜ψ).
As this relation holds with for an arbitrary stopping time, taking supre-
mum in the class MT we obtain that the same relation holds true for American
options.
4.1 Symmetric Markets
It is interesting to note, that in a market with no jumps the distribution of the
discounted (and reinvested) stocks in both the given and dual L´evy markets
coincide. It is then natural to define a market to be symmetric when this
relation hold, i.e. when
L

e−(r−δ)t+Xt | P

= L

e−(δ−r)t−Xt | ˜P

,
(4.8)
meaning equality in law. In view of (4.7), and due to the fact that the char-
acteristic triplet determines the law of a L´evy processes, we obtain that a
necessary and sufficient condition for (4.8) to hold is
Π(dy) = e−yΠ(−dy).
(4.9)
This ensures ˜Π = Π, and from this follows a −(r −δ) = ˜a −(δ −r), giving
(4.8), as we always have ˜σ = σ. Condition (4.9) answers a question raised by
Carr and Chesney (1996), see [2].

256
J. Fajardo and E. Mordecki
5 Conclusions
In this paper we have extended the results obtained by Gerber and Shiu [5] for
the bidimensional geometric Brownian motion to the case of two-dimensional
geometric L´evy motion. We have shown that using the Dual Market Method
it is possible to price many derivatives, with pay-offs homogeneous of any
degree, written in terms of two assets driven by geometric L´evy motions, in
the European case and for the American perpetual case. Another important
fact in this paper is the possibility of having a stochastic discount, this allow us
to consider derivatives as quanto derivatives. As a related result, we obtained
a relation between prices of call and put vanilla options in L´evy markets, and
obtained a condition on the jump structure of the process in order to have a
symmetric L´evy market.
Acknowledgments
The first author thanks the comments of participants at The 2004 Winter
Meeting of the Econometric Society and III World Congress of The Bachelier
Finance Society. (The usual disclaimer applies.) The second author thanks
Esko Valkeila and Yuri Kabanov for support.
References
1. Araujo, A., Oliveira R.: On the pricing of European and American swaps op-
tions. IMPA Preprint B 122 (1997)
2. Carr, P., Chesney, M.: American put-call symmetry. Preprint (1996)
3. Fajardo, J.; Mordecki, E.: Duality and derivative pricing with L´evy processes.
Pre-Publicaciones de Matem´atica de la Universidad de la Rep´ublica, Montev-
ideo, Pre-Mat 76 (2003)
4. Geman, H., El Karoui, N., and Rochet,J.: Changes of num´eraire, changes of
probability measure and option pricing. Journal of Applied Probability, 32,
443–458 (1995)
5. Gerber, H. U., Shiu, E. S. W.: Martingale Approach to pricing perpetual Amer-
ican options on two stocks. Mathematical Finance, 6, 303–322 (1996).
6. Jacka, S.D.: Optimal stopping and the American put. Mathematical Finance,
1, 1–14 (1991)
7. Kramkov, D. O., Mordecki, E.: An integral option. Theory Probability and Its
Applications, 39, 162–172 (1994)
8. Margrabe, W.: The value of an option to exchange one asset for another. Journal
of Finance, 33, 177–186 (1978)
9. Mordecki, E. Optimal stopping and perpetual options for L´evy processes. Fi-
nance and Stochastics. VI, 473–493 (2002)
10. Sato, K. : L´evy Processes and Infinitely Divisible Distributions. Cambridge
Studies in Advanced Mathematics, 68. Cambridge University Press, Cambridge
(1999)
11. Shepp, L. A., Shiryaev, A. N.: A new look at the Russian option. Theory of
Probability and its Applications, 39, 103–119 (1995)

Enlargement of Filtration and Additional
Information in Pricing Models: Bayesian
Approach
Dario GASBARRA1, Esko VALKEILA2, and Lioudmila VOSTRIKOVA3
1 University of Helsinki, Department of Mathematics and Statistics,
P.O. Box 68, FIN-00014, Finland.
Dario.Gasbarra@rni.helsinki.fi
2 Institute of Mathematics, P.O. Box 1100, FIN-02015 Helsinki
University of Technology, Finland.
Esko.Valkeila@tkk.fi
3 Departement de Math´ematiques, Universit´e d’Angers, France.
vostrik@univ-angers.fr
Summary. We show how the dynamical Bayesian approach can be used in the
initial enlargement of filtrations theory. We use this approach to obtain new proofs
and results for L´evy processes. We apply the Bayesian approach to some problems
concerning asymmetric information in pricing models, including so-called weak in-
formation approach introduced by Baudoin, as well as some other approaches. We
give also Bayesian interpretation of utility gain related to asymmetric information.
Key words: dynamical Bayesian modelling, enlargement of filtration, asymmetric
information, L´evy processes
Mathematics Subject Classification (2000): 60J60, 60H30, 90A09,
90A60
1 Introduction
The initial enlargement of filtrations is an important topic in the theory of
stochastic processes, and it was studied in the fundamental works of Jeulin
[20], Jacod [18], Stricker and Yor [23] and Yor [24, 25] and others.
Recent interest to this question comes from pricing models in stochastic
finance, where the enlargement of filtrations theory is an important tool in
modelling of asymmetric information between different agents and the possible
additional gain due to this information (see Amendinger et al. [1], Imkeller et
al. [16] Baudoin [3, 4], Elliot and Jeanblanc [13] and others). For an approach
based on anticipating calculus, see, e.g., [21].

258
D. Gasbarra, E. Valkeila and L. Vostrikova
The initial enlargement of filtration consists in the following.
Let (Ω, F, P) be a probability space with the filtration F = (Ft)t≥0 satisfy-
ing the usual conditions and let X be a semimartingale with the (P, F)-triplet
T = (B, C, ν) of predictable characteristics of (we refer to [19] and Section
2 for more details on semimartingales). Suppose that we are given a random
variable ϑ on (Ω, F) such that σ(ϑ) ⊊F0. Define now Gt := Ft ∨σ(ϑ); then
Γ = (Gt)t≥0 is the initially enlarged filtration. The main problems studied are:
is the F-semimartingale X still a semimartingale with respect to the filtration
Γ and if this is true, what is the new triplet T ϑ = (Bϑ, Cϑ, νϑ) with respect
to (P, Γ)?
Surprising at the first glance [and very natural, in fact] the Bayesian ap-
proach proposed in the papers by Dzhaparidze et al. [9, 10] is closely related
to the problem of enlargement of filtrations. In the Bayesian approach one of
the basic concepts is the arithmetic mean measure. This means the follow-
ing. Suppose that on a filtered probability space (Ω, F, F, P) we observe a
semimartingale X = (Xt)t≥0, and the law P θ of X depends of a parameter
θ ∈Θ. Assume that θ is a value of some random variable ϑ, taking values
in a measurable Polish space (Θ, A) where A is the Borel σ-algebra. Denote
the law of the random variable ϑ by α. We suppose that for each θ ∈Θ the
measure P θ is absolutely continuous with respect to P and that the density
process zθ is measurable with respect to F ⊗A. Then we can introduce on
the original space (Ω, F, F, P) the arithmetic mean measure ¯P α: for B ∈F
¯P α(B) :=

Θ
P θ(B)α(dθ) =

Θ

B
zθdPα(dθ).
One can interpret the measure ¯P α also as a ’randomised experiment’. In [9, 10]
it is shown how to compute the predictable characteristics of X with respect
to the arithmetic mean measure ¯P α given the characteristics T θ of X with
respect to P θ.
The Bayesian approach to the initial enlargement of filtration goes as
follows. Suppose for simplicity that the initial σ-algebra is trivial. Let X be
a semimartingale with the (P, F)-triplet T = (B, C, ν). We suppose that we
have, in addition, a random variable ϑ : (Ω, F) →(Θ, A) with values in a
Polish space and the prior law α.
We consider next the product space (Ω×Θ, F ⊗A, IG, IP) with the filtration
IG = (IGt)t≥0 defined by IGt = Ft ⊗A and IP is the joint law of (X(ω), ϑ(ω)).
Let t ∈R+ and αt be the regular a posteriori distribution of the random
variable ϑ given the information Ft:
αt(ω, θ) := P(ϑ ∈dθ|Ft)(ω).
Assume now that αt ≪α. Then, according to the results of Jacod [18] the
process zθ = (zθ
t )t≥0 where
zθ
t (ω) := dαt(ω, θ)
dα(θ)
,

Bayesian Approach to Additional Information
259
is a (P, F)-martingale with zθ
0 = 1. Define now a measure P θ by
dP θ
t := zθ
t dPt,
where the subscript means the restriction of the measure to the sub-σ-algebra
Ft. Then the process X is also a (P θ, F)-semimartingale. If we know the struc-
ture of the density martingale zθ, then, using the Itˆo formula, we can write a
semimartingale decomposition of it and the (P θ, F)-triplet T θ = (Bθ, C, νθ).
Finally, if T θ is P(F) ⊗A-measurable, one obtains the (P, Γ)-triplet of the
semimartingale X by replacing in T θ the fixed parameter θ by the random
variable ϑ. This method is relatively simple and gives a unifying approach
to various concrete models like diffusion processes, counting processes and
L´evy processes. It can also be used outside the semimartingale world. Some
applications will be given in the paper [12].
The paper contains two parts. The first one is devoted to the initial enlarge-
ment of filtration. We begin with reminding some basic facts on semimartin-
gale characteristics and the Girsanov theorem. Then we apply the Bayesian
approach to the initial enlargement. For somewhat related studies see [6, 14].
We continue by giving some examples of the initial enlargement with the final
value. The Bayesian approach can be developed for the progressive enlarge-
ment of filtration as well. This will be done in a later work.
The second part is devoted to so-called weak information introduced in
Baudoin [3, 4]. We show that the notion of weak information can be inter-
preted as changing the “true” prior α, the law of the random variable ϑ, to
another prior distribution γ for the random variable ϑ. After this the whole
analysis can be reduced to the computation of the ¯P γ-characteristics of the
semimartingale X.
Some preliminary results of the Bayesian approach were already obtained
in [11]. We extend and generalize the results in various directions: in addition
to several examples and new applications, we give a Bayesian interpretation of
the so-called additional utility of an insider, or of a weak insider and, finally,
the gain on false information.
2 Characteristics of a semimartingale
We shall work with a semimartingale X
defined on a filtered space
(Ω, F, F, P). Recall some facts concerning the triplet T of a semimartingale
X. Since the triplet T depends on the probability measure P and on the fil-
tration, we keep track of the measures and filtrations in what follows. We
assume that F := FX is the right-continuous version of the natural filtration
of X (completed by P-null sets and that F = FX
∞.
Let µ be the jump measure of X, i.e.
 t
0

|x|>ǫ
xµ(ds, dx) :=

s≤t
∆Xs1{|∆Xs|>ǫ}.

260
D. Gasbarra, E. Valkeila and L. Vostrikova
We use the standard notation from [19] and [15]: if µ := µX is the jump
measure of the semimartingale X, then g ∗µ means the integral with respect
to the jump measure, g ∗ν denotes the integral with respect to the (P, F)-
compensator ν of µ; later g · U is the stochastic integral with respect to a
local martingale U or Riemann–Stieltjes integral with respect to a bounded
variation process U.
Suppose that the semimartingale X has characteristics T = (B, C, ν) with
respect to (P, F). Recall that this means the following (see [19] for more
details and unexplained terminology). Let l : R →R be a truncation function:
l(x) = x in the neighborhood of zero and l has a compact support. Then one
can write the semimartingale X as
X = (X −X(l)) + X(l),
where X(l) is a purely jump process, namely, the process with ’big’ jumps
defined as
X(l)t :=

s≤t
(∆Xs −l(∆Xs))
with ∆Xs = Xs −Xs−.
Having bounded jumps, the process ˜X = (X −X(l)) is a special semi-
martingale and allows the representation
˜Xt = X0 + Xc
t +
 t
0

R\{0}
l(x)(µ(ds, dx) −ν(ds, dx)) + Bt(l),
where Xc is the continuous local martingale part of X, ν is the (P, F) com-
pensator of µ, Bt(l) is the unique (P, F)-predictable locally integrable process
such that the process ˜X −B(l) is a (P, F)-local martingale. Let C be the con-
tinuous process such that the process (Xc)2 −C is a (P, F)-local martingale.
Having all this we have defined the triplet of predictable characteristics of a
semimartingale X as T = (B(l), C, ν). Later we write B instead of B(l).
Consider the class G of real bounded Borel functions on R vanishing in a
neighborhood of 0. If η and ˜η are measures on R such that η(|x| > ǫ) < ∞
and ˜η(|x| > ǫ) < ∞, and if for all g ∈G

R
g(x)η(dx) =

R
g(x)˜η(dx)
then η = ˜η.
Recall Theorem II.2.21 from [19, p.80]
Theorem 2.1. A semimartingale X has the (P, F)-triplet T = (B, C, ν) if
and only if
•
The process M(l) := X −X(l) −B −X0 is a local martingale.

Bayesian Approach to Additional Information
261
•
The process
N(l) := M(l)2 −C2 −l2 ∗ν −

s≤·
(∆Bs)2
is a local martingale.
•
The process U(l) := g ∗(µ −ν) is a local martingale whatever is g ∈G.
Assume moreover that we have on (Ω, F, F, P) a family of probability
measures P θ with θ ∈Θ such that P θ
t ≪Pt for all t ∈R+.
Let θ ∈Θ be fixed. Then X is a (P θ, F)-semimartingale with a triplet
T θ = (Bθ, Cθ, νθ) where
Bθ = B + βθ · C + (Y θ −1)l ∗ν,
Cθ = C,
(2.1)
νθ = Y θ · ν,
with certain (P θ, F)-predictable processes βθ = (βθ
t )t≥0 and Y θ = (Y θ
t )t≥0
such that for all t ∈R+
((βθ)2 · C)t + (|(Y θ −1)l| ∗ν)t < ∞.
(2.2)
For more details see [19].
We denote by P θ
t and Pt the restrictions of the corresponding measures
on Ft and we define the density process zθ = (zθ
t )t≥0 with
zθ
t = dP θ
t
dPt
.
We note that the density process is (P, F)-martingale with the property
inft∈[0,T ] zθ
t > 0 P-a.s. for each T > 0, and we define the stochastic logarithm
mθ of zθ by
dmθ := dzθ/zθ
−.
(2.3)
Then mθ is a (P, F)-local martingale and zθ is the stochastic exponential of
mθ:
zθ
t = E(mθ)t.
Assume now that X is a (P, F)-semimartingale with a triplet T = (B, C, ν)
and that the natural filtration F of X has the predictable representation prop-
erty : a local martingale M with respect to this filtration has the representa-
tion:
M = M0 + H · Xc + W ∗(µ −ν).
(2.4)
Here the predictable process H belongs to the space L2
loc of locally square-
integrable processes with respect to C and the function W = Wt(ω; x) belongs
to Gloc(µ). For information on the space Gloc(µ) see [19, II.1.1,pp. 72-74]. On
the predictable representation property one can consult [19, p.185].

262
D. Gasbarra, E. Valkeila and L. Vostrikova
By the predictable representation property we have that the local martin-
gale mθ from (2.3) has the following semimartingale representation
mθ = βθ · Xc +
	
Y θ −1 +
ˆY θ −ˆ1
1 −ˆ1

∗(µ −ν),
(2.5)
where the processes βθ and Y θ are the same as in (2.1) and the ”hat” processes
are related to the jumps of the compensator ν, namely
ˆ1t(ω) := ν(ω; {t} × R0)
and
ˆY θ
t (ω) :=

R0
Y θ
t (ω, x)ν(ω, {t}, dx).
So, to find the triplet T θ we can read βθ and Y θ from (2.5) and use (2.1) .
3 Arithmetic mean measure
We consider a filtered probability space (Ω, F, F, P) with F = F∞. Suppose
that we are given a parametric family of probability measures (P θ)θ∈Θ where
θ belongs to a measurable Polish space (Θ, A).
We make the following assumption.
Assumption 3.1 For each θ ∈Θ the probability P θ is locally absolute con-
tinuous with respect to P .
Then we can define density process: for each θ ∈Θ and t ∈R+
zθ
t = dP θ
t
dPt
where P θ
t and Pt are the restrictions of P θ and P on Ft. We consider measur-
able with respect to θ versions of the density processes. Given a probability
measure α on (Θ, A) and t ∈R+ and B ∈Ft, we define the arithmetic mean
measure:
¯P α
t (B) :=

Θ
P θ
t (B)α(dθ) =

Θ×B
zθ
t P(dω)α(dθ),
¯P α
t .
Remark 1. In the case of the initial enlargement by a random variable ϑ such
that α = L(ϑ|P), considered in Section 4, we have ¯P α = P. This follows from
the fact that in this case P θ is the regular conditional law of X given ϑ = θ.
We see that ¯P α
t is absolutely continuous with respect to Pt but, in general,
P θ
t is not absolutely continuous with respect to ¯P α
t . For this reason we add
another assumption.

Bayesian Approach to Additional Information
263
Assumption 3.2 For each θ ∈Θ the probability P θ is locally absolute con-
tinuous with respect to ¯P α .
Assume again that X is a (P, F)-semimartingale with triplet T = (B, C, ν)
and having the representation property. Then X is a (P θ, F)-semimartingale
with a triplet T θ = (Bθ, Cθ, νθ) where Bθ , Cθ , νθ are given in (2.1).
The next theorem is a generalization of a result by Kolomiets.
Theorem 3.1. Suppose that the assumptions 3.1 and 3.2 hold and X is a
(P, F)-semimartingale with triplet T = (B, C, ν). Then X is also a ( ¯P α, F)-
semimartingale with the triplet ¯T = ( ¯B, ¯C, ¯ν) defined by
¯B = Eα¯zθ
−· Bθ = B + Eα¯zθ
−βθ · C + Eα¯zθ
−(Y θ −1)l ∗ν,
¯C = C,
(3.1)
¯ν = Eα¯zθ
−Y θ · ν,
where ¯zθ is the density of P θ with respect to the arithmetic mean measure ¯P α.
For the proof see [8, Theorem 3.3].
To interchange the order of integration in (3.1) by using the Fubini theorem
we introduce the following notation. For each t ∈R+ we define a posteriori
measure αt. To do it for B ∈A we put
αt(B) :=

B zθ
t α(dθ)

Θ zθ
t α(dθ).
Let us define αt−(dθ) in the following natural way: for B ∈A
αt−(B) :=

B zθ
t−α(dθ)

Θ zθ
t−α(dθ).
Assuming that βθ
t and Y θ
t are integrable with respect to αt−, we put
¯βt = Eαt−βθ
t ,
¯Yt = Eαt−Y θ
t .
(3.2)
Theorem 3.2. Suppose that the assumptions 3.1 and 3.2 hold and for t > 0
Eαt−|βθ
t | · Ct + Eαt−|Y θ −1|l ∗νt < ∞.
(3.3)
Then X is a ( ¯P α, F)-semimartingale with the triplet ¯T = ( ¯B, ¯C, ¯ν) defined by
¯B = B + ¯β · C + ( ¯Y −1)l ∗ν
¯C = C,
(3.4)
¯ν = ¯Y · ν
where ¯β and ¯Y are given in (3.2).

264
D. Gasbarra, E. Valkeila and L. Vostrikova
Proof
To prove our result we use the classical Fubini theorem. In order
to do it, we show that ¯B is the process of locally P-integrable variation. In
fact, for all t > 0
Var( ¯B)t ≤Var(B)t + Eα¯zθ
−|βθ| · Ct + Eα¯zθ
−|Y θ −1|l ∗νt.
Using classical Fubini theorem for positive functions in last two integrals and
integration with respect the measure αt−we have: for all t > 0
Var( ¯B)t ≤Var(B)t + Eα−|βθ| · Ct + Eα−|Y θ −1|l ∗νt.
We define a localizing sequence as follows. Put
τn = inf{t ≥0 : Eαt−|βθ| · Ct + Eαt−|Y θ −1|l ∗νt + Var(B)t > n}.
(3.5)
and notice that τn is F-stopping time. Moreover, since the jumps of considered
processes are bounded by a constant, we can easily verify that
E ¯
P α[Eαt−|βθ| · Cτn + Eαt−|Y θ −1|l ∗ντn + Var(B)τn] < n + 3 max
x∈R l(x),
where l is the truncation function. Now, we notice that the sequence of F-
stopping times τn increases to infinity due to the condition (3.3). Then, we
localize with τn and apply the classical Fubini theorem to (3.1) and we have
(3.4).
□
Remark 2. Theorem 3.2 is a special case of the stochastic Fubini theorem.
Namely, we know that
zθ
t = E(mθ)t,
where
mθ = βθ · Xc +
	
Y θ −1 +
ˆY θ −ˆ1
1 −ˆ1

Then by Theorem 3.2 we have the following variant of stochastic Fubini the-
orem
¯zt =

Θ
zθ
t α(dθ) = E( ¯m)t
with
¯m = ¯β · Xc +
	
¯Y −1 +
ˆ¯Y −ˆ1
1 −ˆ1

.
Sometimes the verification of the condition (3.3) can be difficult and we
can be interested to replace it by another condition expressed in terms of the
density process. For instance, we can use the following assumption.
Assumption 3.3 There exists a localizing sequence of F- stopping times τn
such that for every n ≥1
E

Θ
[zθ, zθ]1/2
τn α(dθ) < ∞
where E is the expectation with respect to the initial measure P.

