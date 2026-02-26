# Mathematical Finance: Research Frontiers (Festschrift)

!!! info "Source"
    **From Stochastic Calculus to Mathematical Finance: The Shiryaev Festschrift** edited by Yu. Kabanov, R. Liptser, and J. Stoyanov, Springer, 2006.
    These notes are used for educational purposes.

## Financial Mathematics Research

Bayesian Approach to Additional Information
265
Theorem 3.3. Suppose that the assumptions 3.1, 3.2, 3.3 hold. Then X is a
( ¯P α, F)-semimartingale with the triplet ¯T = ( ¯B, ¯C, ¯ν) defined by (3.4).
Proof
In fact, we have only to show that the assumption 3.3 implies
the local integrability of the variation of ¯B. Since B is locally integrable with
respect to the arithmetic mean measure, which follows from the fact that the
jumps of B are bounded by a constant, we have only to show that there exists
a localizing sequence of stopping times sn such that for each n
E ¯
P α

Eα−|βθ| · Cτn + Eα−|Y θ −1|l ∗ντn

< ∞.
(3.6)
Let
¯Zt = d ¯Pt
dPt
.
We remark that
¯Zt =

Θ
zθ
t α(dθ).
Using the fact that ¯Z is a positive (P, F)-martingale and the observation that
we are dealing with the predictable positive processes, we obtain:
E ¯
P α

Eα−|βθ| · Cτn + Eα−|Y θ −1|l ∗ντn

= EP ¯Zτn

Eα−|βθ| · Cτn + Eα−|Y θ −1|l ∗ντn

=

Θ
EP {zθ
−|βθ| · Cτn + zθ
−|Y θ −1|l ∗ντn}α(dθ)
=

Θ
EP {zθ
−|βθ| · Cτn + zϑ
−|Y θ −1|l ∗µX
τn}α(dθ)
=

Θ
EP {Var([zθ, X(l) −B])τn}α(dθ)
Let
τ ′
n = inf{t ≥0 :
sup
0≤s≤t
|Xs(l) −Bs| > n}
and sn = τ ′
n ∧τn. By the Fefferman inequality, (see [15, Theorem 10.17]) and
the fact that X(l) −B is (P, F)-local martingale we deduce that
EP Var([zθ, X(l) −B])sn ≤∥(X(l) −B)sn ∥BMO EP [zθ, zθ]1/2
sn .
We remark that
∥(X(l) −B)sn ∥BMO≤2(n + 2 max
x
l(x))
where l is truncation function. So, after integration with respect to α, we ob-
tain from assumption 3.3 that (3.6) holds, and, hence, ¯B has locally integrable
variation with respect to ¯P α.
□

266
D. Gasbarra, E. Valkeila and L. Vostrikova
4 Initial enlargement
4.1 Triplet and initial enlargement
Let X be a semimartingale on a filtered space (Ω, F, F, P) with the (right-
continuous completed) natural filtration of X. Let T = (B, C, ν) be the (P, F)-
triplet of X.
Suppose that we have also a random variable ϑ with values in measurable
Polish space (Θ, A). Define the initially enlarged filtration Γ = (Gt)t≥0 by
Gt :=
?
s>t
(Fs ∨σ(ϑ)).
Our problem is to find the semimartingale decomposition of X with respect
to the enlarged filtration Γ.
Let α be the distribution of the random variable ϑ, i.e. P(ϑ ∈dθ) = α(dθ).
Let for αt be its regular conditional distribution with respect to the σ-algebra
Ft. Following Bayesian terminology we say that α is the a priori distribution
and αt is the a posteriori distribution of the random variable ϑ with respect
to the information Ft.
We make the following standing assumption.
Assumption 4.1 The posterior distributions αt and the prior distribution α
satisfy: for each t ∈[0, T] we have P-a.s.
αt ≪α.
(4.1)
We make a stop to discuss the right-continuity of the filtration Γ: in
Amendinger [2, Proposition 3.3] it is shown that under the assumption αt ∼α
we have that Gt = Ft ∨σ(ϑ). Inspecting the proof of this result in [2], one
can see that, in fact, it is sufficient to assume only assumption 4.1. So, under
assumption 4.1 we have Gt = Ft ∨σ(ϑ).
We consider next the product space (Ω×Θ, F ⊗A, IG, IP) where the filtra-
tion IG = (IGt)t≥0 is defined by
IGt =
?
s>t
(Fs ⊗A)
(4.2)
and IP is the joint law of (ω, ϑ(ω)). Again, under assumption 4.1 we can take
IGt = Ft ⊗A.
Denote the optional and predictable σ-algebras on (Ω× R+) with respect
to F by O(F) and P(F). With the filtration IG we have that
P(IG) = P(F) ⊗A
and
O(F) ⊗A ⊂O(IG).
The following result is due to Jacod [18, Lemme 1.8., p.18-19].

Bayesian Approach to Additional Information
267
Lemma 4.1. Under assumption 4.1 there exists a strictly positive O(IG)-
measurable function (ω, t, θ) →zθ
t (ω) such that:
1. For each θ ∈Θ, zθ is a (P, F)-martingale.
2. For each t ∈R+, the measure zθ
t α(dθ) is a version of the regular condi-
tional distribution αt(dθ) so that Pt × α-a.s.
dαt
dα (θ) = zθ
t .
(4.3)
For each θ ∈Θ define also a measure P θ:
dP θ
t := zθ
t dPt.
(4.4)
The measure P θ is absolutely continuous with respect to the P, and so X
is a (P θ, F)-semimartingale with the (P θ, F)-triplet T θ = (Bθ, C, νθ).
Next we indicate how one can use the prior and posterior distributions
to obtain the semimartingale decomposition of a (P, F)-semimartingale with
respect to the filtration Γ.
1. We are given a semimartingale X with (P, F)-triplet T = (B, C, ν), where
the natural filtration F has the representation property, random variable
ϑ, prior α(dθ) = P(ϑ ∈dθ) and posterior αt(dθ) = P(ϑ ∈dθ|Ft).
2. Compute dαt
dα (θ) with the Itˆo formula as E(mθ) and read βθ and Y θ from
the representation (2.5), use (2.1) to obtain T θ .
3. If T θ is P(F) ⊗A-measurable, replace θ by ϑ in T θ to obtain the triplet
of X with respect to (P, Γ).
In the following theorem we give the link between the Girsanov theorem
and enlargement of filtrations.
Theorem 4.1. Assume that the process X is a (P, F)-semimartingale with
triplet T = (B, C, ν) and we have the martingale representation property with
respect to natural filtration F. Let ϑ be a random variable such that the as-
sumption (4.1) is satisfied. Suppose also that L1(Ω, F, P) is separable and the
condition (3.3) holds.
Then the following conditions are equivalent:
(a)X is a (P θ, F)-semimartingale with triplet T θ = (Bθ, C, νθ) on the space
(Ω, F, F, P) for α-almost all θ and the application T ′ : (ω, t, θ) →T θ
t (ω)
is P(F) ⊗A-measurable.
(b)X is a (IP, IG)-semimartingale with triplet T
′ : (ω, t, θ) →T θ
t (ω) on the
product space (Ω× Θ, F ⊗A, IG, IP) where IP is the joint law of (ω, ϑ(ω).
(c)X is a (P, Γ)-semimartingale on (Ω, F, P) with triplet T ϑ = (Bϑ, C, νϑ).
Remark 1. It should be noticed that separability condition will be used only
in the direction: c) ⇒b) ⇒a).

268
D. Gasbarra, E. Valkeila and L. Vostrikova
To prove the theorem we need some lemmas concerning the transformation
of triplets, stopping times and martingales.
Lemma 4.2. The function X : (ω, t, θ) →(R, B(R)) is P(F) ⊗A-measurable
if and only if Xϑ : (ω, t, ϑ(ω)) →(R, B(R)) is P(Γ)-measurable.
Proof
It is sufficient to establish the property on semi-algebras generating
the corresponding σ-algebras. Let now a, b, c ∈R, a < b, A ∈Fa, B ∈A and
X(ω, t, θ) = c1(a,b](t)1A(ω)1B(θ).
(4.5)
Then X is an element of semi-algebra generating P(F) ⊗A and
Xϑ(ω, t, ϑ(ω)) = c1(a,b](t)1A(ω)1B(ϑ(ω)) = c1(a,b](t)1A∩ϑ−1(B)(ω).
(4.6)
Since the set A ∩ϑ−1(B) belongs to Fa ∨σ(ϑ), it belongs also to Ga, and the
function Xϑ defined by (4.6) is an element of P(Γ).
Inversely, let a, b, c ∈R, a < b, C ∈Ga−, then
Xϑ(ω, t, ϑ(ω)) = c1(a,b](t)1C(ω)
(4.7)
is an element of semi-algebra generating P(Γ). Since Ga−= .
s<a(Fs ∨σ(ϑ))
it suffices to consider elements of the generating algebra I
s<a(Fs ∨σ(ϑ)). In
turn, if C ∈I
s<a(Fs ∨σ(ϑ)), then there exists s < a such that C ∈Fs ∨σ(ϑ).
Next, the σ-algebra Fs∨σ(ϑ) is generated by the sets A∩ϑ−1(B) with A ∈Fs
and B ∈A. So, we have to consider only the elements Xϑ of the form (4.7)
with C = A ∩ϑ−1(B). But the corresponding application X is (4.5) and it is
P(F) ⊗A-measurable.
□
Lemma 4.3. Let for each θ ∈Θ the process (Xθ
t )t≥0 be an F-adapted c`adl`ag
process. Let L > 0 and
τ θ
L = inf{s ≥0 : Xθ
s (ω) > L}.
(4.8)
If the application X : (ω, t, θ) →Xθ
t is O(IG)-measurable, then
τ ϑ
L = inf{s ≥0 : Xϑ(ω)
s
(ω) > L}
is a Γ-stopping time.
Proof
Let t ∈R+. Then
{(ω, θ) : τ θ
L > t} = {(ω, θ) : sup
s≤t
Xθ
s ≤L} ∈IGt
where IGt is defined by (4.2). It means that for all u > t
{(ω, θ) : τ θ
L > t} ∈Fu ⊗A.

Bayesian Approach to Additional Information
269
Since Fu ⊗A is generated by the semi-algebra of the sets A × B with A ∈Fu
and B ∈A, we can restrict ourselves to this special type of sets. But
{ω : (ω, ϑ(ω)) ∈A × B} ∈Fu ∨σ(ϑ)
and, hence, for u > t
{ω : τ ϑ
L > t} ∈Fu ∨σ(ϑ).
Then, τ ϑ
L is a Γ-stopping time.
□
Lemma 4.4. Let θ ∈Θ and (M θ
t )t≥0 be an F-adapted c`adl`ag process. Let M
be the application (t, ω, θ) →M θ
t (ω). Suppose that L1(Ω, F, P) is separable.
Then the following conditions are equivalent:
a) M θ is (P θ, F)-martingale for α-almost all θ and M is O(IG)-measurable
process,
b) M is a (IP, IG)-martingale,
c) M ϑ is a (P, Γ)-martingale.
Proof
We show that
a) (i)
⇒c) (ii)
⇒b) (iii)
⇒a).
(i): Let E be the expectation with respect to P and E be the expectation
with respect to IP, the joint law of (ω, ϑ(ω)). For each s < t, A ∈Fs, B ∈A
E(1A(ω)1B(ϑ(ω))(M ϑ
t −M ϑ
s )) = E(1A(ω)1B(θ)(M θ
t −M θ
s )).
Let Eα be the expectation with respect to α and Eθ is the expectation with
respect to P θ. Then by the Fubini theorem and conditioning we obtain:
E(1A(ω)1B(θ)(M θ
t −M θ
s )) = Eα[1B(θ)Eθ(1A(ω)Eθ(M θ
t −M θ
s |Fs))] = 0
since M θ is a martingale α-a.s. with respect to (P θ, F). Hence, P-a.s.
E(M ϑ
t −M ϑ
s |Fs ∨σ(ϑ)) = 0.
Since M ϑ is c`adl`ag, using corollary 2.4 of [22], p.59, we have:
E(M ϑ
t −M ϑ
s |Gs) = lim
u↓s E(M ϑ
t −M ϑ
s |Fu ∨σ(ϑ)) = 0
which gives c).
(ii): If M ϑ is (P, Γ)-martingale, then for each t ∈IQ+ the random variable
M ϑ
t is Gt = =
s>t(Fs ∨σ(ϑ))-measurable and it can be written in the form
M ϑ
t (ω) = M(ω, t, ϑ(ω)) (P-a.s.) where M is measurable with respect to the
filtration IGt = =
s>t(Ft ⊗A). Taking a right-continuous version having left-
hand limits we obtain the application M : (ω, t, θ) →(R, B(R)) which is
O(IG)-measurable. For all s < t and A ∈Fs, B ∈A we have:

270
D. Gasbarra, E. Valkeila and L. Vostrikova
E(1A(ω)1B(θ)(M(ω, t, θ) −M(ω, s, θ)) = E(1A(ω)1B(ϑ(ω))(M ϑ
t −M ϑ
s )) = 0
which means that IP-a.s.
E(M(ω, t, θ) −M(ω, s, θ)|Fs ⊗A) = 0
and we have b) in the same way as c) before, since M is c`adl`ag.
(iii): If we have b), then for each (ω, t, θ) we have M θ
t = M(ω, t, θ). For
A ∈Fs and B ∈A we obtain by the Fubini theorem
0 = E(1A(ω)1B(θ)(M(ω, t, θ) −M(ω, s, θ)))
= Eα(1B(θ)Eθ(1A(ω)(M θ
t −M θ
s ))).
Hence, for each s < t and α-a.s.
Eθ(1A(M θ
t −M θ
s )) = 0.
The measurability problem which may occur here is that α-a.s. set can depend
on A and s. Since L1(Ω, F, P) is separable, we obtain that α-a.s. for all s and
all Fs-measurable bounded functions gs
Eθ(gs(M θ
t −M θ
s )) = 0
and, hence,
Eθ(M θ
t −M θ
s |Fs) = 0
which gives a).
□
Proof
We show that a), b), c) are equivalent. With the notation of The-
orem 2.1, the processes M θ(l), N θ(l) and U θ(l) are (P, F)-local martingales.
Since the semimartingale ˜X has bounded jumps, all these local martingales
are also locally bounded, i.e. for each θ there exists a localizing sequence τ θ
L
such that the stopped processes are bounded. By Lemma 4.3 the replacing θ
by ϑ in stopping times gives τ ϑ
L(ω) which is a (P, Γ)-stopping time. Moreover,
the application τL : (ω, t, θ) →τ θ
L is a (IP, IG)-stopping time.
Next, by Lemma 4.2 the replacing of θ by ϑ in T θ which supposed to
be P(F) ⊗A-measurable, gives T ϑ which is P(Γ)-measurable. Moreover, the
application T ′ : (ω, t, θ) →T θ is P(IG)-measurable.
Finally, the claim follows from Lemma 4.4 which guaranties the conserva-
tion of martingale properties in the case of replacing θ by the variable ϑ and
in the case of replacing of the initial space by the product space.
□
In the considered case where P θ is the conditional law of semimartingale
X given ϑ = θ, one can rewrite the assumption 3.3 in terms of the so-called
decoupling measure Q as in [14]. Let us suppose that the density process
z = (zθ)θ∈Θ is O(F) ⊗A-measurable. Then we can replace θ by ϑ to obtain
zϑ. We denote by Pt and Qt the restrictions of the measures P and Q to Gt

Bayesian Approach to Additional Information
271
where Γ = (Gt)t≥0 is the filtration enlarged by the initial value ϑ. If zϑ
t > 0
P-a.s. for all t > 0, we can define Q by
dQt = (zϑ
t )−1dPt.
The decoupling measure has the following property: (Q, Γ)- triplet of X is the
same as the (P, F)- triplet of X and L(ϑ|Q) = L(ϑ|P). We can also use an
another definition of a decoupling measure Q, namely, as the solution of the
following martingale problem, if it exists and unique: the (Q, Γ)-triplet of X
is the same as the (P, F)-triplet of X and L(ϑ|Q) = L(ϑ|P).
Remark 2. If zϑ
t > 0 P-a.s. for all t > 0, the assumption 3.3 is equivalent to
the assumption:
EQ[zϑ, zϑ]1/2
τn < ∞
(4.9)
for some localizing sequence of F-stopping times τn. We note that [zϑ, zϑ]1/2
is (Q, Γ)-locally integrable (see [19, Corollary I.4.55]). Here we require the
existence of a localizing sequence of F-stopping times.
Theorem 4.2. Under the settings of Theorem 4.1, assume that a) and (4.9)
hold. Then X is a (P, Γ)-semimartingale with the triplet T ϑ = (Bϑ, C, νϑ).
Proof Using the proof of Theorem 4.1 we note that it remains to prove that
Bϑ is of locally integrable variation with respect to P. Since Bϑ is obtained
from Bθ by replacing θ by ϑ, we have:
Var(Bϑ)t ≤Var(B)t + |βϑ| · Ct + |Y ϑ −1|l ∗νt.
Since B is locally integrable with respect to P, the question of local integra-
bility of Bϑ is reduced to the existence of a localizing sequence of F-stopping
times τn such that for each n
EP

|βϑ| · Cτ + |Y ϑ −1|l ∗ντn

< ∞.
(4.10)
We have:
EP

|βϑ| · Cτn + |Y ϑ −1|l ∗ντn

= EQ{zϑ
τ

|βϑ| · Cτn + |Y ϑ −1|l ∗ντn

}
= EQ{zϑ
−|βϑ| · Cτn + zϑ
−|Y ϑ −1|l ∗ντn}
= EQ{zϑ
−|βϑ| · Cτn + zϑ
−|Y ϑ −1|l ∗µX
τn}
= EQVar([zϑ, X(l) −B])τn.
By the Fefferman inequality, (see [15, Theorem 10.17]) and the fact that
X(l) −B is both (Q, Γ)- and (P, F)-local martingale we deduce that
EQVar([zϑ, X(l) −B])τn ≤∥(X(l) −B)τn ∥BMO EQ[zϑ, zϑ]1/2
τn .

272
D. Gasbarra, E. Valkeila and L. Vostrikova
From Proposition 2.38 in [17] it follows easily that the (P, F)-local martin-
gale (X(l) −B) is (P, F)-locally in BMO since it has bounded jumps, and by
assumption (4.9) there is a localizing sequence of F-stopping times τn tending
to infinity which makes the last expression finite. Hence, the inequality (4.10)
holds and Bϑ has locally integrable variation with respect to P.
□
Remark 3. Assumption (4.9) can be expressed in term of information. More
precisely,
EQ[zϑ, zϑ]1/2
τ
≤C(1 + EQzϑ
τ log zϑ
τ ).
The boundedness of this information was used in [10] to verify the stochastic
Fubini theorem.
4.2 Initial enlargement and Gaussian martingales
Let us first consider a classical example of the initial enlargement of filtration.
Here X is a continuous Gaussian martingale with respect to the measure P
starting from zero and such that there exists lim
t→∞Xt = X∞.
Let ϑ = X∞. We denote by ⟨X⟩the predictable quadratic variation of X
and we put ⟨X⟩t,∞:= ⟨X⟩∞−⟨X⟩t.
The prior distribution α(dθ) := P(ϑ ∈dθ) is a N(0, ⟨X⟩∞) and the pos-
terior distribution αt of ϑ given Ft is N(Xt, ⟨X⟩t,∞).
Assume ⟨X⟩t,∞> 0 for all t ∈R+, then αt is equivalent to α, so the
assumption (4.1) is valid.
From the Itˆo formula with the function f(x, y) = x2/y applied to the first
term in exponential we have:
dαt
dα (θ) =

⟨X⟩∞

⟨X⟩t,∞
exp

−(θ −Xt)2
2⟨X⟩t,∞
+
θ2
2⟨X⟩∞

= exp
 t
0
βθ
sdXs −1
2
 t
0

βθ
s
2 d⟨X⟩s

,
where
βθ
s := θ −Xs
⟨X⟩s,∞
.
Since βθ is a predictable process for each θ ∈Θ, continuous in θ uniformly
in t ∈[0, T] for each T > 0, the application (ω, t, θ) →βθ
t is P(F) ⊗A-
measurable. By Theorem 4.1 we can now conclude that the process
Xt −
 t
0
X∞−Xs
⟨X⟩s,∞
d⟨X⟩s
is a (P, Γ)-Gaussian martingale with the bracket ⟨X⟩.
We give some special cases of the above results.

Bayesian Approach to Additional Information
273
•
Let Y be a Brownian motion and put Xt =
 t
0 asdYs, where a is deter-
ministic square-integrable function on R+. If as := I(0,T ](s), then we have:
ϑ = YT , ⟨X⟩t,∞= T −t for t ≤T and βθ
s = θ −Ys
T −s ; this implies the
classical representation of the Brownian bridge
Yt =
 t
0
YT −Ys
T −s ds + Y Γ
t ,
where Y Γ is a Brownian motion with respect to Γ.
•
In the previous case take a = I(0,T +η]. We obtain the case of final value
distorted by a small noise example from [1].
•
Assume that Y is a fractional Brownian motion and let Xt := E[YT |F Y
t ]
be the prediction martingale. This example and related will be studied in
detail in [12].
4.3 Initial enlargement in the Poisson filtration
Assume that X is a Poisson process with intensity 1 on (Ω, F, F, P) stopped
in time T and let ϑ = XT . Here the prior distribution α is Poisson(T) and
the posterior distribution
αt(θ) =

eT −t (T −t)θ−Xt
(θ−Xt)!
if θ ≥Xt,
0
if θ < Xt.
(4.11)
Next, for all t ∈[0, T[ we have αt ≪α and
dαt
dα (θ) = e−t (T −t)θ−Xt
T θ
I{θ≥Xt}
θ!
(θ −Xt)!.
We put Y θ
s := θ −Xs−
T −s
and note that Y θ is a predictable process such that
0 ≤Y θ
s < ∞for all s ∈[0, T] – this follows from the fact that ∆XT = 0 IP-a.s.
Since
dαt
dα (θ) = exp
 t
0
(Y θ
s −1)ds
 (
s≤t

Y θ
s
∆Xs ,
we obtain that with respect to the filtration Γ the standard Poisson process
has the semimartingale representation:
Xt = nt +
 t
0
XT −Xs−
T −s
ds,
t < T
where n = (nt)t≥0 is a (P, Γ)-martingale.

274
D. Gasbarra, E. Valkeila and L. Vostrikova
4.4 L´evy processes: initial enlargement with the final value
Let X be a L´evy process. Then for each λ ∈R the characteristic function of
Xt is
EeiλXt = e−tψ(λ)
where ψ is characteristic exponent given by
ψ(λ) = iaλ + 1
2σ2λ2 +

R

1 −eiλx + iλxI{|x|<1}

π(dx)
with π a measure on R verifying

R(1 ∧x2)π(dx) < ∞. The (P, F)-triplet of
X is T = (aI, σ2I, Leb ⊗π), where It = t.
We consider again stopped in T process and we take ϑ := XT . The process
X is a time-homogeneous Markov process with independent increments and
hence
αt(dθ) = P(XT ∈dθ|Xt) = P(XT −t + x ∈dθ)|x=Xt.
To be able to continue we assume that the law of the random variable Xs has
a density f(s, y) with respect to fixed dominating measure η, i.e. for B ∈B(R)
P(Xs ∈B) =

B
f(s, y)η(dy).
Moreover, we assume that f ∈C1,2
b
(R+×U) where U is an open set belonging
to R.
Since αt ≺≺α for t ∈[0, T[, we can write that η-a.s.
dαt
dα (θ) = f(T −t, θ −Xt)
f(T, θ)
.
(4.12)
Use the Itˆo formula to obtain that
f(T −t, θ −Xt) = f(T, θ) −
 t
0
∂f
∂s (T −s, θ −Xs−)ds
−
 t
0
∂f
∂x(T −s, θ −Xs−)dXs
(4.13)
+1
2σ2
 t
0
∂2f
∂x2 (T −s, θ −Xs−)ds
+

s≤t

∆f(T −s, θ −Xs) + ∂f
∂x(T −s, θ −Xs−)∆Xs

.
We know that the expression in (4.12) is a (P, F)-martingale for each θ. So, we
can identify the continuous martingale part on the right-hand side of (4.13)
and then the continuous martingale part of (4.12) as
−
 t
0
∂f
∂x(T −s, θ −Xs−)
f(T, θ)
dXc
s.
(4.14)

Bayesian Approach to Additional Information
275
Recall that zθ
t = dαt
dα (θ). According to the Girsanov theorem the term βθ in
the equation (2.1) is obtained as (for more details on this kind of computations
see [19, Lemma III.3.31])
βθ
t =
d⟨zθ, Xc⟩t
zθ
t−d⟨Xc, Xc⟩t
=
−∂f
∂x(T −t, θ −Xt−)
f(T −t, θ −Xt−)
= −∂
∂x log f(T −t, x)|x=θ−Xt−.
(4.15)
Consider next the pure jump martingale in (4.12): we have that
∆f(T −t, θ −Xt) = f(T −t, θ −Xt) −f(T −t, θ −Xt−)
and so
∆zθ
t
zθ
t−
= f(T −t, θ −Xt)
f(T −t, θ −Xt−) −1,
from this we obtain (for more details, see [19, p. 175]) that the P θ compensator
νθ of µX is
νθ(dt, du) = f(T −t, θ −(Xt−+ u))
f(T −t, θ −Xt−)
π(du)dt.
(4.16)
Moreover, since the expression on the right-hand side of (4.12) is a martin-
gale, the function f(t, u) satisfies the following integro-differential equation,
which might be called Kolmogorov backward integro-differential equation:
∂f
∂t (T −t, θ −x) = 1
2σ2 ∂2f
∂x2 (T −t, θ −x) −a∂f
∂x(T −t, θ −x)
+

R

f (T −t, θ −(x + y))
(4.17)
−f (T −t, θ −x) + ∂f
∂x (T −t, θ −x) y

π(dy)
with the boundary condition f(T, θ −x) = δ{0}(θ −x).
Example: Brownian motion
We look again the Brownian case, as in Subsection 4.2, but now using the
L´evy processes approach. Since the triplet of X is T = (0, σ2I, 0), the equation
(4.17) is reduced to:
∂f
∂t (T −t, θ −x) = 1
2σ2 ∂2f
∂x2 (T −t, θ −x)
with boundary condition f(T, θ −x) = δ{0}(θ −x).
It is well-known that the solution is

276
D. Gasbarra, E. Valkeila and L. Vostrikova
f(T −t, θ −x) =
1

2π(T −t)
exp

−(θ −x)2
2(T −t)

and so βθ = θ −Xs
T −s and a new drift is Bθ
t =
 t
0
θ −Xs
T −s ds.
Example: Gamma process
Let X be a Gamma process. This means that the (P, F)-triplet of X is T =
( a
b t, 0, a
ue−bududt). We know also that the density f(t, x) = P(Xt ∈dx) is
f(t, x) =
bat
Γ (at)xat−1e−bx with some parameters a, b > 0 (see [5, p.73] ). In
particular, we have that Xt −a
b t is a (P, F)-martingale.
Put again ϑ = XT and we have from (4.16) that the (P θ, F) compensator
is
νθ(dx, dt) =

1 −
x
θ −Xt−
a(T −t)−1 a
xdxdt.
Hence, (P θ, F)-drift of the process X is
 t
0
 θ−Xt−
0
x

1 −
x
θ −Xs−
a(T −s)−1 a
xdxdt =
 t
0
θ −Xs−
T −s ds,
and this means that the process Xt−a
b t−
 t
0
θ−Xs−
T −s ds is a (P θ, F)-martingale.
Example: Poisson process
We look again at the Poisson case, as in subsection 4.3. We indicate briefly
how one can use the approach described in 4.4, where we know only the triplet
of the process X. So, let X be a Poisson process with intensity λ.
Put again ϑ = XT . Put p(t, k) := P(Xt = k) and we assume that for k ≥0
the functions p(·, k) ∈C1(R+).
We know (see (4.12)) that
dαt
dα (θ) = p(T −t, θ −Xt)
p(T, θ)
.
We start with the trivial identity, which is the analog of the Itˆo formula here:
p(T −t, θ −Xt) =
(4.18)
p(T, θ) −
 t
0
pt(T −s, θ −Xs−)ds +

s≤t
∆p(T −s, θ −Xs).
Using the fact that ∆Xt ∈{0, 1}, we have the identity

Bayesian Approach to Additional Information
277
∆p(T −s, θ −Xs) = (p(T −s, θ −(Xs−+ 1)) −p(T −s, θ −Xs−))∆Xs;
since the right-hand side of (4.18) is a (P, F)-martingale, we obtain that the
functions p(t, k) satisfy the following system of differential equations:
pt(T −s, k) = λ(p(T −s, k) −p(T −s, k + 1))
(4.19)
and, hence,
p(T −s, k) = e−λ(T −s) (λ(T −s))k
k!
is the solution of (4.19) with the boundary condition p(T, θ−x) = δ{0}(θ−x).
It remains to note that
p(T −s, k) −p(T −s, k + 1) = p(T −s, k)

k + 1
λ(T −s) −1

(4.20)
and we can conclude that with respect to the measure P θ the process X has
intensity θ−Xs−
T −s . This means that the process Xt −
 t
0
θ−Xs−
T −s ds is a (P θ, F)-
martingale.
5 Weak information
In this and in the next sections we discuss briefly some other applications
of the Bayesian viewpoint related with the enlargement and arithmetic mean
measure.
5.1 Weak insider information
The notion of weak information in mathematical finance was introduced by
Baudoin [3, 4]. Before we discuss briefly this notion, recall our basic setup.
We have a semimartingale X on a filtered space (Ω, F, F, P) with the right-
continuous version of natural filtration F = (FX
t )t≥0 completed by the P-null
sets of F, and F = FX
∞. We assume the predictable representation property
for FX and we denote by T = (B, C, ν) the (P, F)-triplet of X.
Let ϑ be a FT -measurable random variable with the values in a measurable
Polish space (Θ, A). Let α := L(ϑ|P), αt(dθ) := P(ϑ ∈dθ|Ft), assume that
we have (4.1), and define zθ
t by (4.3) and finally put dP θ
t = zθ
t dPt. Recall that
in this case the arithmetic mean measure is
¯P α
t (B) :=

Θ
P θ
t (B)α(dθ) = P(B).
In particular, the (P, F)-triplet of the semimartingale X does not change under
the arithmetic mean measure ¯P α (see Remark 1).
Consider three types of agents in the pricing model, where the stock price
is given by the semimartingale X: ordinary agents, strong insiders and weak

278
D. Gasbarra, E. Valkeila and L. Vostrikova
insiders. We do not want to go in too detailed description of the pricing model,
but we define these three types by giving the information and the (historical)
probability of the agent.
•
ordinary agents For the ordinary agent the information is given by F, the
probability is P and he uses the triplet T = (B, C, ν) to build his strategy.
•
strong insiders For the strong insider the information is given in the pair
(X, ϑ), and we can model this by an initial enlargement of the filtration.
By using Theorem 4.1 we see that one possibility to model strong insider
is to change the probability P to P θ, and the strong insider works with
the filtration F and the new triplet T θ.
We describe the notion of weak insider
in more detail. Let γ be the
probability distribution on (Θ, A). Following [3, p. 112] we assume that γ ≪α.
Then it is easy to see that ¯P γ ≪¯P α = P, where
¯P γ
t (B) =

Θ×B
zθ
t γ(dθ)dP,
and the measure ¯P γ is the arithmetic mean measure with respect to the prior
distribution γ; in [3] the corresponding measure on (Ω, F, F) is called the
minimal probability associated with the conditioning (T, ϑ, γ).
Hence, we can model the weak insiders as follows:
•
weak insiders For the weak insider the information is given by the filtration
F, but he changes the probability measure P to the measure ¯P γ and he
works with the triplet ¯T γ = ( ¯Bγ, C, ¯νγ).
Assume that we have
γt ≪γ
and we have assumption 3.3 with respect to the measure P ⊗γ.
We can now use Theorem 3.1 to compute the new triplet with respect to
the measure ¯P γ and we obtain:
¯Bγ = B + ¯βγ · C + ( ¯Y γ −1)l ∗ν,
¯Cγ = C,
(5.1)
¯νγ = ¯Y γ · ν,
where the predictable local characteristics ¯βγ and ¯Y γ are given by
¯βγ
t = Eγt−βθ
t ,
¯Y γ
t = Eγt−Y θ
t
(5.2)
with γt and γt−be the a posteriori distributions under γ. Recall that γt is
defined by :
γt(A) :=

A zθ
t γ(dθ)

Θ zθ
t γ(dθ),
A ∈A,

Bayesian Approach to Additional Information
279
and γt−is given by the same formula with replacing zθ
t by zθ
t−.
Define now ¯mγ as
¯mγ = ¯βγ · Xc +
	
¯Y γ −1 +
ˆ¯Y γ −ˆ1
1 −ˆ1

∗(µ −ν),
then we have that
d ¯P γ
t
dPt
= E( ¯mγ)t.
By definition of ¯P γ
t and γt we have also that
dγt
dγ (θ) = dP θ
t
d ¯P γ
t
= dP θ
t
dPt
dPt
d ¯P γ
t
= zθ
t
1
E( ¯mγ)t
.
In comparison with dαt
dα (θ) which is equal to zθ
t (Pt × α -a.s.), it means that
dγt
dγ (θ) = dαt
dα (θ)
1
E( ¯mγ)t
.
Example: Brownian motion
Let X be a Brownian motion stopped in T and suppose that the Brownian
filtration F is enlarged by ϑ = XT . In this example T = (0, I, 0) and
βθ = θ −Xt
T −t .
Consider the example of final value distorted with a noise. We suppose that
the weak insider knows in advance the value y of random variable Y = XT +ǫ,
where ǫ is independent of XT and has N(0, η2) as law. The prior of the insider
with weak information is γ = P(XT |Y ), which by the normal correlation
theorem is N(m, σ2) with σ2 = (T −1 + η−2)−1 and m = Y σ2/η2.
For t < T the posterior distribution is γt := P(XT |Y, Xt), which by the
normal correlation theorem is N(mt, σ2
t ) with σ2
t = ((T −t)−1 + η−2)−1 and
mt = (Y η−2 + Xt(T −t)−1)σ2
t .
According to previous results on triplets the drift of X under the insider
measure is given by
¯Bγ
t =
t

0
Eγsϑ −Xs
T −s
ds.
(5.3)
Since
Eγsϑ = Y (T −s) + Xsη−2
T −s + η−2
,
we have after simplifications that

280
D. Gasbarra, E. Valkeila and L. Vostrikova
¯Bγ
t =
t

0
Y −Xs
T −s + η2 ds.
Remark 1. One can analyze the increasing information along the same lines.
By this we mean that the insider obtains dynamically more and more precise
information about the random variable ϑ. A model of this type is the following:
in addition to the price process X the insider observes the process Y , where
Yt = ϑ + ǫt,
where ǫ is a semimartingale, independent of the random variable ϑ such that
ǫt →0 P-a.s. as t →T. This kind of models are analyzed in [7].
6 Additional expected logarithmic utility of an insider
6.1 Introduction
We consider the pricing model with two assets, the stock (risky asset) and the
bond (riskless asset). We assume as in [1] that the process X has the dynamics
dXt = µtd⟨M⟩t + dMt
(6.1)
where µ is a predictable process and M is a continuous Gaussian martingale
with deterministic bracket ⟨M⟩. We assume that the interest rate r is equal
to zero, so the bond price Bt = 1 for all t.
We assume that the stock price S has the dynamics
dSt = StdXt.
For the investment strategy π we have the portfolio dynamics
dV π
t = πtV π
t dXt.
Then it can be shown that with respect to the logarithmic utility, the
average optimal strategy πo of an ordinary investor is πo := µ. Note that here
the average optimal strategy is computed with respect to the measure P.
6.2 Additional expected utility of strong insiders
Now consider a strong insider who knows the final value of the stock. We
assume that it is the same as the insider knows the final value of the martingale
MT . Put again ϑ = MT .
Then he can model the dynamics of X as
dXt = (µt + βθ
t )d⟨M⟩t + dM θ
t .
(6.2)

Bayesian Approach to Additional Information
281
Here M θ is a continuous Γ-martingale with
M θ
t = Mt −
 t
0
βθ
sd⟨M⟩s
and
βθ
t = θ −Mt
⟨M⟩t,T
where ⟨M⟩t,T = ⟨M⟩T −⟨M⟩t. Again the optimal expected investment strat-
egy of an insider agent for the logarithmic utility is πi = µ+βθ. Note that the
expectation is computed with respect to the measure IP which is the joint law
of (M, ϑ(ω)). The log-value of the optimal strategy for an ordinary investor is
log V πo
t
= log V0 +
 t
0
µsdMs + 1
2
 t
0
µ2
sd⟨M⟩s.
(6.3)
Similarly, the log-value of the optimal strategy for the insider investor is
log V πi
t
= log V0 +
 t
0
(µs + βθ
s)dM θ
s + 1
2
t

0
(βθ
s + µs)2d⟨M⟩s.
(6.4)
To calculate the expectation E we need the following lemma.
Lemma 6.1. Let uθ = (uθ
t )t≥0 be a positive F-adapted c`adl`ag process for each
θ ∈Θ. Suppose that the application u : (ω, t, θ) →uθ
t(ω) is O(IG)-measurable
with IG defined by (4.2). Then
E
 t
0
uθ
sd⟨M⟩s = E
 t
0
¯uα
s d⟨M⟩s
(6.5)
where and ¯uα
s is the posterior mean of uθ
s, i.e.
¯uα
s = Eαs−uθ
s
Proof
Recall first the following fact. Assume that y = (yt)t≥0 is a posi-
tive uniformly integrable (P, F)-martingale and D is a predictable increasing
process with D0 = 0. Then by [15, Theorem 5.16, p. 144 and Remark 5.3, p.
137]
EytDt = E
 t
0
(pY )sdDs = E
 t
0
Ys−dDs.
(6.6)
Since zθ is the conditional density of the law of X given ϑ = θ with respect
to P, we have using (6.6) and the ordinary Fubini theorem that
E
 t
0
uθ
sd⟨M⟩s = E

Θ
zθ
t
 t
0
uθ
sd⟨M⟩sdα

=

Θ
E

zθ
t
 t
0
uθ
sd⟨M⟩s

dα
=

Θ
E
 t
0
zθ
s−uθ
sd⟨M⟩sdα = E
 t
0

Θ
zθ
s−uθ
sdα

d⟨M⟩s
= E
 t
0
¯uα
s d⟨M⟩s.

282
D. Gasbarra, E. Valkeila and L. Vostrikova
This proves (6.5).
□
Let us now compute the expected utility from the insider point of view.
This means that we take the expectation of (6.4) with respect to the insider
measure IP which is the joint law of (ω, ϑ). In the computation we use the
fact that the martingale M has a drift
 ·
0 βθ
sd⟨M⟩s with respect to the insider
measure. We obtain:
E(log V πi
t
−log V πo
t
) = 1
2E
 t
0
(µs + βθ
s)2d⟨M⟩s
−1
2E
 t
0
µ2
sd⟨M⟩s −E
 t
0
µsdMs
= 1
2E
 t
0
(βθ
s)2d⟨M⟩s
= 1
2E
 t
0
¯vα
s (β)d⟨M⟩s
where ¯vα
s (β) is the posterior variance of the process βθ
s. Next we give the
Bayesian interpretation of this result. Note first that the Kullback–Leibler
information in the prior with respect to posterior is
I(α|ατ) := Eατ log dατ
dα (θ).
In our case we have:
E(log V πi
t
−log V πo
t
) = EI(α|αt).
For more information on this kind of computations we refer to [10].
We compute next the difference of the expected gain from the ordinary
agent point of view. This has the interpretation that an ordinary agent has
excess to the insider information, but he thinks that this is false. We model
this by the measure P ⊗α — this means that the ordinary agent does not
change his triplet. So the expected utility gain has to be calculated using the
measure P ⊗α. With a similar computation to the previous one we obtain
that
EP ⊗α(log V πo
t
−log V πi
t ) = 1
2EP ⊗α
 t
0
(βθ
s)2d⟨M⟩s.
The Kullback–Leibler information in the posterior ατ with respect to the prior
α is define by
I(ατ|α) := Eα log dα
dατ .
For our model we can conclude that
EP ⊗α(log V πo
t
−log V πi
t ) = EI(αt|α).
Note that the differences of the expected gains are in both cases positive
— this reflects the fact the the investors act optimally according to their own
model.

Bayesian Approach to Additional Information
283
6.3 Additional expected logarithmic utility of weak insider
Assume that γ and α are two different equivalent priors for the parameter ϑ;
we can define the arithmetic mean measures ¯P γ and ¯P α; we can compute the
(F, ¯P γ) and (F, ¯P α)-triplets of the semimartingale X by (3.1). Note that here
we do not assume that α is the marginal law of the parameter ϑ.
Denote the optimal strategies based on the weak information for the prior
γ and α by πw,γ and πw,α, respectively.
Then, with a familiar computation
E ¯
P γ (log V w,γ
t
−log V w,α
t
) = 1
2E ¯
P γ

t

0
(β
γ
s −β
α
s )2d⟨M⟩s

(6.7)
where
¯βγ
s = Eγs−βθ
s,
¯βα
s = Eαs−βθ
s.
Note that the right-hand side of (6.7) is nothing else but thye Kullback–Leibler
information of ¯P α in ¯P γ and, hence,
E ¯
P γ (log V w,γ
t
−log V w,α
t
) = I( ¯P α| ¯P γ)t.
Note that
0 ≤I( ¯P α| ¯P γ)t = E ¯
P γ log d ¯P γ
t
d ¯P α
t
=
=

Θ

Ω

log dP θ
t
d ¯P α
t
−log dP θ
t
d ¯P γ
t

P θ
t (dω)γ(dθ)
= Eγ
1
I(P θ
t | ¯P α
t ) −I(P θ
t | ¯P γ
t )
2
= E ¯
P γ
t
1
I(α|αt) −I(γ|γt)
2
In particular, this means that
E ¯
P γ
t I(γ|γt) = inf
α E ¯
P γ
t I(α|αt)
where the infimum is taken over all measures α which are equivalent to γ.
The interpretation is that if one believes in his own prior γ, he expects to get
less information from the data than any other person using the same model
with a “wrong” prior.
Acknowledgements
D.G. and E.V. are grateful to the Universit´e d’Angers for partial support, L.V.
is grateful to the EU-IHP network Dynstoch for partial support. We thank an
anonymous referee for useful remarks and additional references.

284
D. Gasbarra, E. Valkeila and L. Vostrikova
References
1. Amendinger, J., Imkeller, P. and Schweizer, M.: Additional logarithmic utility
of an insider. Stochastic Processes and their Applications, 75, 263–286 (1998).
2. Amendinger, J.: Martingale representation theorems for initially enlarged filtra-
tions. Stochastic Processes and their Applications, 89, 101–116 (2000)
3. Baudoin, F.: Conditioned stochastic differential equations: theory, examples and
application to finance. Stochastic Processes and their Applications, 100, 109–
145, (2003)
4. Baudoin, F.: Modeling anticipations on financial markets. In: Lecture Notes in
Mathematics, 1814, 43–94, Springer-Verlag, Berlin, (2003)
5. Bertoin, J.: L´evy Processes. Cambridge University Press, Cambridge (1996)
6. Chao, T.M. and Chou, C.S.: Girsanov transformation and its application to the
theory of enlargement of filtrations. Stochastic analysis and applications, 19,
439–454, (2001)
7. Corcuera, J.M., Imkeller, P., Kohatsu-Higa, A. and Nualart, D.: Additional util-
ity of insiders with imperfect dynamical information. Finance and Stochastics,
8, 437–450 (2004)
8. Dzhaparidze, K., Spreij, P. and Valkeila, E.: On Hellinger Processes for Para-
metric Families of Experiments. In: Kabanov, Yu. et. al. (Eds.) Statistics and
Control of Stochastic Processes. The Liptser Festschrift, World Scientific, Sin-
gapore, (1997)
9. Dzhaparidze, K. Spreij, P. and Valkeila, E.: Information concepts in filtered ex-
periments. Theory of Probability and Mathematical Statistics, 67, 38–56 (2002)
10. Dzhaparidze, K. Spreij, P. and Valkeila, E.:
Information processes for semi-
martingale experiments. Annals of Probability, 31, 216–243 (2003)
11. Gasbarra, D. and Valkeila, E.: Initial enlargement: a Bayesian approach. Theory
of Stochastic Processes, 9, 26–37 (2004)
12. Gasbarra, D., Sottinen, T. and Valkeila, E.: Gaussian bridges. Helsinki Univer-
sity of Technology, Research Report A481, (2004)
13. Elliott, R.J. and Jeanblanc, M.: Incomplete markets with jumps and informed
agents. Mathematical Methods of Operations Research, 50, 475–492 (1998)
14. F¨ollmer H. and Imkeller P.: Anticipation cancelled by a Girsanov transforma-
tion: a paradox on Wiener space. Annales de l’Institut Henri Poincar´e, 29,
569–586 (1993)
15. He, S.-W., Wang, J.-G. and Yan, J.-A.: Semimartingale Theory and Stochastic
Calculus. Science Press, New York (1992)
16. Imkeller P.: Enlargement of Wiener filtration by an absolutely continuous ran-
dom variable via Malliavin’s calculus. Probability Theory and Related Fields,
106, 105–135 (1996)
17. Jacod, J.: Calcul Stochastique et probl`emes de Martingales. Lecture Notes in
Mathematics, 714, Springer, Berlin (1979)
18. Jacod, J.: Grossissement initial, hypothese (H’) et theoreme de Girsanov. In:
Jeulin, T. and Yor, M. (Eds.) Grossissements de filtrations: exemples et appli-
cations. Lecture Notes in Mathematics, 1118, Springer, Berlin (1980)
19. Jacod, J. and Shiryaev, A.N.: Limit Theorems for Stochastic Processes. Springer,
Berlin (2003)
20. Jeulin, T.: Semimartingales et Grossissement d’une Filtration. Lecture Notes in
Mathematics, 833, Springer, Berlin (1980)

Bayesian Approach to Additional Information
285
21. Leon, J.A., Navarro, R. and Nualart, D.: An anticipating calculus approach
to the utility maximization of an insider. Mathematical Finance, 13, 171–185
(2003)
22. Revuz D. and Yor M.: Continuous Martingales and Brownian Motion. Springer-
Verlag, Berlin (1999)
23. Stricker, C. and Yor, M.: Calcul stochastique d´ependant d’un param`etre.
Zeitschrift f¨ur Wahrscheinlichkeitstheorie und Verwandte Gebiete, 45, 109–133
(1978)
24. Yor M.: Grossisement de filtration et absolue continuit´e de noyaux. In: Jeulin,
T. and Yor, M. (eds.) Grossissements de filtrations: exemples et applications,
Lecture Notes in Mathematics, 1118, Springer, Berlin (1980)
25. Yor M.: Some Aspects of Brownian Motion, Part II: Some Recent Martingale
Problems. Birkh¨auser, Berlin (1997)


A Minimax Result for f-Divergences
Alexander A. GUSHCHIN1 and Denis A. ZHDANOV2
1 Steklov Mathematical Institute, Gubkina Str. 8, 119991 Moscow, Russia.
gushchin@mi.ras.ru
2 Faculty of Physics and Mathematics, Mary State University,
Lenin Square 1, 424001 Yoshkar-Ola, Russia.
hobbit2@mail.ru
Summary. We consider the following game of a statistician against the nature.
First the nature chooses a measure P at random from a measurable set P of Borel
probability measures on a complete separable metric space X. Then, without know-
ing the strategy of the nature, the statistician chooses a Borel probability measure
Q on X. The loss of the statistician is the f-divergence Jf(P|Q). We show that
the minimax and maximin values of this game coincide and there always exists a
minimax strategy. This generalizes a result of Haussler proved for the case where
the loss is the Kullback–Leibler divergence D(P∥Q).
Key words: f-divergence, Bayes strategy, minimax strategy, minimax theorem,
statistical game
Mathematics Subject Classification (2000): 62C20, 62B10, 62C10
1 Introduction and the Main Result
Statistical games are a part of Wald’s theory of statistical decision functions
[10]. For the theory of statistical games the reader may consult Blackwell and
Girshick [1], Ferguson [6], and Borovkov [2].
In this note we consider a generalization of the game studied by Haussler
[7]. Let (X, ̺) be a complete separable metric space and B(X) its Borel σ-
field. We denote by P(X) the set of all probability measures on (X, B(X)). It
is well known that the weak convergence in P(X) is metrizable. In particular,
one can use the bounded Lipschitz metric β defined as
β(P, Q) = sup


f dP −

f dQ


,
where the supremum is taken over all real-valued functions f on X satisfying
|f(x)| ⩽1 and |f(x) −f(y)| ⩽|x −y| for all x, y ∈X. The metric space

288
A. Gushchin and D. Zhdanov
(P(X), β) is complete and separable (and compact if X is compact). Denote
by P(P(X)) the set of all probability measures on

P(X), B(P(X))

.
Let a Borel set P ∈B(P(X)) be given. Elements of P are interpreted as
possible states of the nature. Consider now a game of a statistician against
the nature. First, the nature chooses a prior measure
π ∈P(P) := {π ∈P(P(X)): π(P) = 1}
and picks a measure P ∈P at random according to π. Then, without knowing
the value P and the strategy π, the statistician chooses a measure Q ∈P(X).
Finally, the loss of the statistician is Jf(P|Q), where f is a fixed convex
function f : (0, ∞) →R and Jf(·|·) stands for the corresponding f-divergence
(see Section 2 for the precise definition). In particular, this setting includes
the following loss functions:
the Kullback–Leibler divergence D(P∥Q): f(x) = x log x,
the Kullback–Leibler divergence D(Q∥P): f(x) = −log x,
the squared Hellinger distance ̺2(P|Q): f(x) = (x1/2 −1)2,
the total variation distance ∥P −Q∥: f(x) = |x −1|.
The minimax value of this game is
V =
inf
Q∈P(X)
sup
π∈P(P)

P
Jf(P|Q) π(dP)
and the maximin value is
V =
sup
π∈P(P)
inf
Q∈P(X)

P
Jf(P|Q) π(dP).
(The integral above is well defined since the integrand is lower semicontinuous
and bounded from below, see Section 2.) It is clear that V ⩽V . We shall say
that a measure Qπ ∈P(X) is a Bayes strategy corresponding to a prior
π ∈P(P) if

P Jf(P|Q) π(dP) attains the infimum over Q ∈P(X) at Qπ.
We can now formulate the main result of this note.
Theorem 1.1. V = V , and there exists a minimax strategy, i.e. there is a
measure Q ∈P(X) such that
V =
sup
π∈P(P)

P
Jf(P|Q) π(dP).
If f(x) = x log x, i.e. Jf(P|Q) = D(P∥Q), this result was proved by Haus-
sler [7], see also his paper for further references and for interpretations of this
game in the information theory and other fields. Under stronger assumptions
a similar statement for the same loss function appeared also in Krob and
Scholl [8].

A Minimax Result for f-Divergences
289
To prove the theorem Haussler considers separately two cases. First, he
assumes that the family P is relatively compact in the weak topology. Then
his arguments are close to those used in similar minimax theorems. However,
it is essential in this part of the proof that the family of Bayes strategies
corresponding to all π ∈P(P) is also relatively compact, which follows easily
from the fact that, for f(x) = x log x, the measure Qπ defined by
Qπ(B) =

P
P(B) π(dP),
B ∈B(X),
is a Bayes strategy corresponding to π. For other f the relative compactness of
Bayes strategies does not hold in general. One can construct simple examples
where P is relatively compact, Jf(P|Q) = D(Q∥P) or Jf(P|Q) = ̺2(P, Q),
and the family of Bayes strategies is not relatively compact.
If the family P is not relatively compact, Haussler shows that V = ∞. For
general f this is also true if f(x)/x →∞as x →∞; otherwise this assumption
on P seems to be rather useless.
Thus our proof is different from that of Haussler. The main idea is to com-
pactify the space X reducing the problem to the case of a compact space X.
In the compact case our arguments are quite standard for minimax theorems,
compare e.g. with the first case considered by Haussler.
If P is finite, the minimax result for arbitrary convex f was proved by
Csisz´ar [4]. (Here there is no need to impose topological assumptions on X.)
Csisz´ar indicates also a way of constructing Bayes strategies based on La-
grange multipliers.
2 Preliminaries
We fix a convex function f on (0, ∞) with values in R. Put f(0) := limu↓0 f(u)
and f(∞)
∞
:= limu↑∞
f(u)
u . Both limits exist and may belong to (−∞, ∞]. The
f-divergence Jf(P|Q) of probability measures P and Q (given on the same
measurable space) is defined, see Csisz´ar [3], by
Jf(P|Q) =

qf
p
q

dλ,
(2.1)
where λ is a σ-finite measure dominating P and Q, p = dP/dλ, q = dQ/dλ.
The following conventions are used in this definition and below:
0 · ∞= 0,
0 · f
a
0

= a · f(∞)
∞
.
The integral in (2.1) is well defined and its value does not depend on the
choice of a dominating measure λ.
We refer to Liese and Vajda [9] for properties of the f-divergence. Here
we mention a few ones used in the proof.

290
A. Gushchin and D. Zhdanov
For any pair P, Q
f(1) ⩽Jf(P|Q) ⩽f(0) + f(∞)
∞
.
If P and Q are singular then Jf(P|Q) = f(0) + f(∞)
∞. If f(0) = ∞and
Jf(P|Q) < ∞then Q is absolutely continuous with respect to P.
Let now P, Q ∈P(X), where X is a complete separable metric space.
Then the function P(X) × P(X)(P, Q) ⇝Jf(P|Q) is lower semicontinuous
and convex, see Liese and Vajda [9, Theorem (1.47) and Corollary (1.55)].
Using boundedness of Jf(P|Q) from below and Fatou’s lemma, we imme-
diately obtain that for every prior π ∈P(P(X)), the function
P(X)Q ⇝

P(X)
Jf(P|Q) π(dP)
is lower semicontinuous.
3 Proof of Theorem 1.1
Step 1. First we show that V = V if P is finite, cf. Haussler [7, Lemma 2].
Let P = {P1, . . . , Pk}. Put
S =
1
Jf(P1|Q), . . . , Jf(Pk|Q)

: Q ∈P(X)
2
∩Rk.
If S = ∅then for any prior π ∈P(P) with strictly positive weights we have

P
Jf(P|Q) π(dP) = ∞
for any
Q ∈P(X),
hence V = ∞. So we assume that S ̸= ∅.
Let conv S be the convex hull of S. By Carath´eodory’s theorem, for each
z ∈conv S there exist s1, . . . , sk+1 in S and nonnegative α1, . . . , αk+1 such
that
k+1

i=1
αi = 1
and
k+1

i=1
αisi = z.
Let si =

Jf(P1|Qi), . . . , Jf(Pk|Qi)

, Qi ∈P(X), i = 1, . . . , k + 1. Then
for Q := k+1
i=1 αiQi
k+1

i=1
αiJf(Pj|Qi) ⩾Jf(Pj|Q),
j = 1, . . . , k,
due to convexity of the f-divergence. Thus for each z ∈conv S there is a point
s ∈S such that sj ⩽zj, j = 1, . . . , k.

A Minimax Result for f-Divergences
291
Let La := {(z1, . . . , zk): zj ⩽a, j = 1, . . . , k}, a ∈R. Put V
:=
sup {a: La ∩conv S = ∅}. According to the above, for every n ⩾1 there
is a measure Qn ∈P(X) such that
Jf(Pj|Qn) ⩽V + 1
n,
j = 1, . . . , k.
Thus V ⩽V , and it remains to show that V ⩾V .
Let Int LV be the interior of LV . Then Int LV and conv S are disjoint
convex sets, and there exists a separating hyperplane, i.e. there are a nonzero
vector (p1, . . . , pk) and a real c such that
k

j=1
pjzj ⩽c
if
zj < V,
j = 1, . . . , k,
(3.1)
and
k

j=1
pjJf(Pj|Q) ⩾c
for all
Q ∈P(X).
(3.2)
It follows easily from (3.1) that pj are nonnegative. In particular k
j=1 pj > 0.
Dividing pj and c by k
j=1 pj, we can assume that k
j=1 pj = 1.
Now it follows from (3.1) that c ⩾V . On the other hand, (3.2) implies
V ⩾c. Hence V ⩾V .
Step 2. Now our aim is to prove the statement of the theorem if X is a
compact.
Assume that V < V . Let V be any real such that V < V . Given P ∈P,
put
U(P) := {Q ∈P(X): Jf(P|Q) > V }.
Since Jf(P|Q) is lower semicontinuous in Q, U(P) is an open subset of the
compact P(X). Moreover, the sets U(P), P ∈P, cover P(X). Indeed,
sup
π∈P(P)

P
Jf(P|Q) π(dP) ⩾V
for every Q ∈P(X),
hence there is a prior π ∈P(P) such that

P
Jf(P|Q) π(dP) > V,
and there is a measure P ∈P such that Jf(P|Q) > V .
Therefore, there exists a finite subcover U(P1), . . . , U(Pk) of P(X), i.e. for
every Q ∈P(X) there is a number j, 1 ⩽j ⩽k, such that Jf(Pj|Q) > V .
Applying the first step of the proof to P′ = {P1, . . . , Pk}, we obtain

292
A. Gushchin and D. Zhdanov
V =
sup
π∈P(P)
inf
Q∈P(X)

P
Jf(P|Q) π(dP) ⩾
sup
π∈P(P′)
inf
Q∈P(X)

P′ Jf(P|Q) π(dP)
=
inf
Q∈P(X)
sup
π∈P(P′)

P′ Jf(P|Q) π(dP) =
inf
Q∈P(X) sup
j
Jf(Pj|Q) ⩾V.
Since V is any number smaller than V , we have V = V .
As it was mentioned in the previous section, the function
P(X)Q ⇝

P
Jf(P|Q) π(dP)
is lower semicontinuous for every prior π. Therefore, the function
P(X)Q ⇝
sup
π∈P(P)

P
Jf(P|Q) π(dP)
is also lower semicontinuous and hence attains its infimum over the compact
set P(X). This implies the existence of the minimax strategy.
Step 3. Finally we shall prove the theorem in full generality.
Since X is a separable metric space, there is another metric ̺′ for X
generating on X the same topology as ̺ and such that X is totally bounded
in ̺′, see e.g. Dudley [5, Theorem 2.8.2]. Let Y be the completion of X with
respect to ̺′, then (Y, ̺′) is compact. The Borel σ-field for (Y, ̺′) is denoted
by B(Y ).
Let F be a closed set in (X, ̺). Since the metric space (F, ̺) is complete and
its completion with respect to ̺′ coincides with the closure F of F in (Y, ̺′),
F is a countable intersection of sets that are open in (F, ̺′), see e.g. Dudley
[5, Theorem 2.5.4]. Hence F ∈B(Y ), and it follows that B(X) ⊆B(Y ).
Conversely let F be closed in (Y, ̺′). Since ̺ and ̺′ define the same topology
on X, F ∩X is closed in (X, ̺). This implies that B ∩X ∈B(X) for every
B ∈B(Y ).
Let P(Y ) be the set of all probability measures on (Y, B(Y )). Evidently,
we can identify measures from P(X) as elements of P(Y ) that have zero mass
on Y \ X. Let Pn, n ⩾1, and P be from P(X). If the sequence {Pn} weakly
converges to P in P(P(Y )), then it does the same in P(P(X)), which follows
from the definition. The converse statement follows from the Portmanteau
theorem. Hence the bounded Lipschitz metrics in P(X) and P(Y ) generate
the same topology on P(X). Repeating the above arguments, we conclude
that a set Q in P(X) belongs to B(P(X)) if and only if it belongs to B(P(Y )).
Thus we may consider priors from P(P) as elements of P(P(Y )) as well with
no danger of confusion.
The second step of our proof shows that
sup
π∈P(P)
inf
Q∈P(Y )

P
Jf(P|Q) π(dP) =
inf
Q∈P(Y )
sup
π∈P(P)

P
Jf(P|Q) π(dP),
(3.3)

A Minimax Result for f-Divergences
293
and there is a measure Q ∈P(Y ) such that supπ∈P(P)

P Jf(P|Q) π(dP) is
equal to the right-hand side of (3.3). To complete the proof it is enough to
show that for any Q ∈P(Y ) \ P(X) there is a measure Q′ ∈P(X) such that
Jf(P|Q) ⩾Jf(P|Q′) for all P ∈P(X), in particular, for all P ∈P. We
consider three cases.
First, if Q(Y \ X) = 1 then Q is singular with respect to every P ∈P(X),
hence the f-divergence Jf(P|Q) takes its maximal value f(0)+ f(∞)
∞, and any
Q′ ∈P(X) does the job.
Second, let 0 < Q(X) < 1 and f(0) = ∞. Then Q is not absolutely
continuous with respect to every P ∈P(X), Jf(P|Q) = ∞, and any choice of
Q′ ∈P(X) is appropriate again.
Finally, let 0 < Q(X) < 1 and f(0) < ∞. Define a measure Q′ ∈P(X) by
Q′(B) = Q(B ∩X)
Q(X)
,
B ∈B(X).
Take a measure P ∈P(X) and let λ = (P + Q)/2, p = dP/dλ, q = dQ/dλ.
Using the inequality
(1 −Q(X))f(0) + Q(X)f
u
v

⩾f

Q(X)u
v

,
v > 0, u ⩾0,
which is due to convexity of f, we obtain
Jf(P|Q) =

Y
qf
p
q

dλ
=

X∩{q>0}
qf
p
q

dλ + f(∞)
∞
P(X ∩{q = 0}) + (1 −Q(X))f(0)
⩾

X∩{q>0}
q
Q(X)f

Q(X)p
q

dλ −1 −Q(X)
Q(X)
f(0)

X∩{q>0}
q dλ
+ f(∞)
∞
P(X ∩{q = 0}) + (1 −Q(X))f(0)
=

X∩{q>0}
q
Q(X)f

p
q/Q(X)

dλ + f(∞)
∞
P(X ∩{q = 0})
= Jf(P|Q′).
The claim follows.
References
1. Blackwell, D., Girshick, M.A.: Theory of Games and Statistical Decisions. Wiley,
New York; Chapman and Hall, London (1954)
2. Borovkov, A.A.: Mathematical Statistics. Gordon and Breach, Amsterdam
(1998)

294
A. Gushchin and D. Zhdanov
3. Csisz´ar, I.: Eine Informationstheoretische Ungleichung und ihre Anwendung auf
den Beweis der Ergodizit¨at von Markoffschen Ketten. Magyar Tud. Akad. Mat.
Kutat´o Int. K¨ozl., 8, 85–108 (1963)
4. Csisz´ar, I.: A class of measures of informativity of observation channels. Period.
Math. Hungar., 2, 191–213 (1972)
5. Dudley, R.M.: Real Analysis and Probability. Wadsworth, Pacific Grove, CA
(1989)
6. Ferguson, T.S.: Mathematical Statistics: A Decision Theoretic Approach. Aca-
demic Press, New York–London (1967)
7. Haussler, D.: A general minimax result for relative entropy. IEEE Trans. Inform.
Theory, 43, 1276–1280 (1997)
8. Krob, J., Scholl, H.R.: A minimax result for the Kullback Leibler Bayes risk.
Econ. Qual. Control, 12, 147–157 (1997).
9. Liese, F., Vajda, I.: Convex Statistical Distances. Teubner, Leipzig (1987)
10. Wald, A.: Statistical Decision Functions. Wiley, New York; Chapman & Hall,
London (1950)

Impulse and Absolutely Continuous Ergodic
Control of One-Dimensional Itˆo Diffusions
Andrew JACK and Mihail ZERVOS ∗
Department of Mathematics, King’s College London,
The Strand, London WC2R 2LS, UK.
andrew.j.jack@kcl.ac.uk, mihail.zervos@kcl.ac.uk
Summary. We consider a problem that combines impulse control with absolutely
continuous control of the drift of a general one-dimensional Itˆo diffusion. The objec-
tive of the control problem is to minimize an ergodic or long-term average criterion
that penalizes both deviations of the state process from a given nominal point and
the use of control effort. Our analysis completely characterizes the optimal strategy.
Key words: Itˆo diffusions, impulse control, absolutely continuous control, ergodic
criterion
Mathematics Subject Classification (2000): 93E20, 49J40, 49N25
1 Introduction
We consider a stochastic system, the state of which is modelled by the con-
trolled one-dimensional Itˆo diffusion
dXt = Ut dt + dZt + σ(Xt) dWt,
X0 = x ∈R,
(1.1)
where W is a standard one-dimensional Brownian motion, U is a progressively
measurable process such that
Ut ∈[−b(Xt), b(Xt)]
for all t ≥0,
(1.2)
and Z is a controlled piecewise constant process, the jumps of which occur at
the times when control effort is exercised in an impulsive way to reposition the
system’s state by an amount equal to the associated jump sizes. The objective
of the optimization problem is to minimize the long-term average criterion
∗Research supported by EPSRC grant no. GR/S22998/01

296
A. Jack and M. Zervos
lim sup
T →∞
1
T Ex
 T
0
h(Xt) dt +

t∈[0,T ]

K+∆Zt + c+
1{∆Zt>0}
+

t∈[0,T ]

−K−∆Zt + c−
1{∆Zt<0}

,
which is taken to be equal to ∞if X explodes in finite time with positive prob-
ability, over all admissible choices of the controlled processes U and Z. Here, h
is a given function that is strictly decreasing in ]−∞, 0[ and strictly increasing
in ]0, ∞[, and c+, c−, K+, K−are positive constants. This performance index
penalizes deviations of the state process X from the nominal operating point
0. While the index does not explicitly penalize the expenditure of control ef-
fort associated with an admissible choice of U, which is constrained by (1.2),
it reflects a cost paid each time that control is exercised in an impulsive way.
In particular, the constants c+ and K+ (resp., c−and K−) provide a fixed
and a proportional cost paid each time that the controller incurs a jump of
the system’s state in the positive (resp., negative) direction.
This problem provides one of the few non-trivial examples of optimal sto-
chastic control models that admit a solution of an explicit analytic nature.
The version of the problem that arises when the drift of (1.1) is not control-
lable has been solved by Jack and Zervos [5]. Both of these problems have
been motivated by the research presented in Jeanblanc-Picqu´e [6], Mundaca
and Øksendal [8], Cadenillas and Zapatero [1, 2], and Chiarolla and Hauss-
mann [3] who consider the issue of controlling in an optimal way the stochastic
dynamics of a foreign exchange (FX) or an inflation rate by means of a central
bank intervention policy.
With regard to these references, we can see that the optimization problem
that we consider can be of use to a central bank in its task of controlling an
FX rate as follows. The process X is used to model the stochastic dynamics
of the logarithm of an FX rate relative to a given nominal point. The central
bank wishes to keep the rate as close as possible to its given nominal point,
which translates to 0 in the state space of X. To achieve this aim, the central
bank uses the function h to penalize deviations of the rate from its nominal
value. To control the rate, the central bank has two intervention policies at
its disposal. The first one is through the continuous adjustment of its interest
rate, the effect of which is modelled by the process U. The second policy is to
purchase or sell large amounts of foreign capital at discrete times, the effect
of which is incorporated into the model through the jumps of the process Z.
In contrast to the above mentioned references where discounted criteria are
considered, here, as well as in Jack and Zervos [5], we consider a long-term
average criterion. Since an FX rate is not an asset and the function h does
not represent a tangible cost, the choice of a discounting factor does not have
a clear economic interpretation. This observation suggests that addressing
this type of application using a long-term average criterion rather than a
discounted one conforms better with the standard economic theory.

Control of One-Dimensional Itˆo Diffusions
297
Our analysis is based on the explicit construction of an appropriate solu-
tion to the associated Hamilton–Jacobi–Bellman (HJB) equation. This con-
struction relies upon the use of the so-called “smooth-pasting condition” that
was first observed to characterize a wide class of optimal stopping problems
(e.g., see Shiryaev [9] and Krylov [7]). Also, part of it follows steps that paral-
lel the ones used in the analysis of Harrison, Sellke and Taylor [4] who consider
the impulse control of a Brownian motion with an expected discounted crite-
rion. With regard to the structure of the problem that we solve, it is worth
noting that, even though the dynamics modelled by (1.1) allow for the possi-
bility that the state process X explodes in finite time, our assumptions ensure
that the optimal control strategy is a “stabilizing” one.
2 The control problem
We consider a stochastic system, the state process X of which is driven by a
Brownian motion W, a controlled process U that affects the system’s dynamics
in an absolutely continuous way and a controlled process Z that affects the
system’s dynamics impulsively. In particular, we assume that the system’s
state process satisfies the controlled SDE
dXt = Ut dt + dZt + σ(Xt) dWt,
X0 = x ∈R,
(2.1)
where σ : R →R is a given function and W is a standard one-dimensional
Brownian motion. Here, U is a process such that, for some given function
b : R →[0, ∞[,
Ut ∈[−b(Xt), b(Xt)]
for all t ≥0,
(2.2)
and Z is a piece-wise constant, c`agl`ad process. The time evolution of both
of these processes is determined by the system’s controller. With reference to
the current impulse control literature, it is worth observing that an admissible
choice of a process Z can equivalently be described by the collection
Z = (τ1, τ2, . . . , τn, . . . ; ∆Zτ1, ∆Zτ2, . . . , ∆Zτn, . . .) ,
where (τn, n ≥1) is the sequence of random times at which the jumps of Z
occur and (∆Zτn, n ≥1) are the sizes of the corresponding jumps.
We adopt a weak formulation of the control problem that we study:
Definition 1. Given an initial condition x ∈R, a control of a stochastic
system governed by dynamics as in (2.1) is any nine-tuple
Cx = (Ω, F, Ft, Px, W, U, Z, X, τ),
where

298
A. Jack and M. Zervos
(Ω, F, Ft, Px) is a filtered probability space satisfying the usual
conditions,
W is a standard one-dimensional (Ft)-Brownian motion,
U is an (Ft)-progressively measurable process,
Z is a finite variation piecewise constant c`agl`ad (Ft)-adapted
process with Z0 = 0,
X is a c`agl`ad (Ft)-adapted process such that (2.1) and (2.2) are
well-defined and satisfied up to the explosion time τ.
We define Cx to be the family of all such controls Cx.
With a control Cx ∈Cx we associate the performance criterion defined by
J(Cx) := lim sup
T →∞
1
T Ex
 T
0
h(Xt) dt +

t∈[0,T ]

K+∆Zt + c+
1{∆Zt>0}
+

t∈[0,T ]

−K−∆Zt + c−
1{∆Zt<0}

,
if Px (τ = ∞) = 1,
(2.3)
where ∆Zt := Zt+ −Zt, and by
J(Cx) := ∞,
if Px (τ = ∞) < 1.
(2.4)
Here h : R →R is a given function that models the running cost resulting from
the system’s operation and K+, c+, K−, c−> 0 are given constants penalizing
the use of impulsive control effort.
The objective of the control problem is to minimize the performance crite-
rion defined by (2.3)–(2.4) over all controls Cx ∈Cx. The next assumption on
the problem’s data is sufficient for our optimization problem to be well-posed.
Assumption 2.1 The following conditions hold:
(a) There exists C1 > 0 such that
0 < σ2(x) ≤C1(1 + |x|)
for all x ∈R,
(2.5)
(b) For all x ∈R there exists ε > 0 such that
 x+ε
x−ε
1 + b(s)
σ2(s)
ds < ∞,
(2.6)
(c) The function h is continuous, strictly decreasing on ] −∞, 0[ and strictly
increasing on ]0, ∞[. Also, h(0) = 0, and there is a constant C2 > 0 such that
h(x) ≥C2(|x| −1)
for all x ∈R.
(2.7)
(d) Given any constant γ ∈R,
lim
x→±∞
1
σ2(x) [h(x) + b(x)γ] = ∞.
(2.8)

Control of One-Dimensional Itˆo Diffusions
299
(e) There exist a−≤a+ such that the function
h(·) −b(·)K−





is strictly decreasing on ] −∞, a−[,
is strictly negative inside ]a−, a+[, if a−< a+,
is strictly increasing on ]a+, ∞[.
(2.9)
(f) There exist α−≤α+ such that the function
h(·) −b(·)K+





is strictly decreasing on ] −∞, α−[,
is strictly negative inside ]α−, α+[, if α−< α+,
is strictly increasing on ]α+, ∞[.
(2.10)
(g) K+, c+, K−, c−> 0.
Note that the conditions in this assumption involve no convexity properties
such as the ones often imposed in the stochastic control literature. Also, al-
though they appear to be involved, they are quite general and easy to verify
in practice.
Example 1. If we choose
b(x) = β|x| + γ,
σ(x) = ζ
and
h(x) = θ|x|p,
for some constants β, γ > 0, ζ ̸= 0, θ > 0 and p > 1, then Assumption 2.1
holds.
Remark 1. It is worth noting that we can easily dispense of the assumption
that h is continuous. However, we decided to keep it because to avoid compli-
cations in a part of our analysis.
3 The solution to the control problem
With regard to the general theory of stochastic control, the solution to the
control problem formulated in the previous section can be obtained by finding
a sufficiently smooth, for an application of Itˆo’s formula, function w and a
constant λ satisfying the HJB equation
min
1
2σ2(x)w′′(x) −b(x)|w′(x)| + h(x) −λ,
c+ −w(x) + inf
z≥0

w(x + z) + K+z

,
c−−w(x) + inf
z≤0

w(x + z) −K−z

= 0.
(3.1)
If such a pair (w, λ) exists, then, subject to suitable technical conditions, we
expect the following. Given any initial condition x ∈R,

300
A. Jack and M. Zervos
λ =
inf
Cx∈Cx J(Cx).
Note that this expression also reflects the fact that the optimal value of the
performance criterion is independent of the system’s initial condition. The set
of all x ∈R such that
c−−w(x) + inf
z≤0

w(x + z) −K−z

= 0
(3.2)
is the part of the state space where the controller should act immediately with
an impulse in the negative direction, while the set of all x ∈R such that
c+ −w(x) + inf
z≥0

w(x + z) + K+z

= 0
(3.3)
is the region of the state space where the controller should act with an impulse
in the positive direction. The interior of the set of all x ∈R such that
1
2σ2(x)w′′(x) −b(x)|w′(x)| + h(x) −λ = 0
(3.4)
defines the part of the state space in which the controller should act only
through the exercise of absolutely continuous control of the drift. Inside this
region, it is optimal to choose
Ut = −sgn(w′(Xt))b(Xt).
(3.5)
It turns out that all of these statements, indeed, are true.
Now, we conjecture that an optimal strategy is characterized by five points,
y2 < y1 < a < x1 < x2, and takes the form that can be described as follows.
If the state space process X takes any value x ≥x2, then impulsive control is
exercised to “push” it instantaneously to the level x1. Similarly, whenever the
state process X assumes a value x ≤y2, impulsive control action is used to
reposition it at y1. As long as the state process is inside the interval ]y2, x2[,
the controller expends absolutely continuous control effort at the maximum
rate, given by b(X), to “push” the state process X towards a, which, in view
of (3.5), is associated with (3.9) below. We therefore look for a solution (w, λ)
to the HJB equation (3.1) such that
w(x) = w(x1) + K−(x −x1) + c−,
for x ≥x2,
(3.6)
1
2σ2(x)w′′(x) −b(x)|w′(x)| + h(x) −λ = 0,
for x ∈]y2, x2[,
(3.7)
w(x) = w(y1) + K+(y1 −x) + c+,
for x ≤y2,
(3.8)
w′(x)





< 0,
for x < a,
= 0,
for x = a,
> 0,
for x > a.
(3.9)

Control of One-Dimensional Itˆo Diffusions
301
Assuming that this strategy is indeed optimal, we need a system of appro-
priate equations to determine the free-boundary points y2, y1, a, x1, x2 and
the constant λ. To derive such equations, we argue as follows. With regard
to the boundary points y2 and x2 that separate the three regions defined by
(3.2)–(3.4) and the so-called “smooth-pasting condition”, we impose
w′(y2+) = −K+
and
w′(x2−) = K−.
(3.10)
Now, relative to impulses in the negative direction, we consider the inequality
c−−w(x) + inf
z≤0

w(x + z) −K−z

≥0.
Assuming for the sake of the argument that we have somehow calculated w,
this inequality implies that
c−−w(x2) + w(x) −K−(x −x2) ≥0
for all x ≤x2.
With regard to (3.6) and the fact that x2 is a constant, this observation implies
that the function x →w(x) −K−x has a local minimum at x = x1, which
can be true only if
w′(x1) = K−.
(3.11)
Moreover, for x = x2, (3.6) implies that
 x2
x1
w′(s) ds = K−(x2 −x1) + c−.
(3.12)
Similarly, considering impulses in the positive direction, we conclude that
w′(y1) = −K+
and
 y1
y2
w′(s) ds = −K+ (y1 −y2) −c+.
(3.13)
Summarizing the considerations above, a candidate for an optimal strategy
is characterized by six parameters, namely y2 < y1 < a < x1 < x2 and λ, and
a function w such that (3.6)–(3.13) are all true. Now, (3.7) and (3.9) can both
be true only if w satisfies the equation
1
2σ2(x)w′′(x) −sgn(x −a)b(x)w′(x) + h(x) −λ = 0,
x ∈]y2, x2[,
which is the case if
w′(x) = g(x, λ, a)
for all x ∈]y2, x2[,
(3.14)
where g is defined by
g(x, λ, a) := p′
a(x)
 x
a
[λ −h(s)] ma(ds),
x ∈]y2, x2[.
(3.15)

302
A. Jack and M. Zervos
Here, pa and ma are defined by
pa(x) :=
 x
a exp

2
 s
a b(u)σ−2(u) du

ds,
if x ≥a,
−
 a
x exp

2
 a
s b(u)σ−2(u) du

ds,
if x < a,
(3.16)
ma(dx) :=
2
p′a(x)σ2(x) dx.
(3.17)
It follows that, to determine the six parameters y2 < y1 < a < x1 < x2 and λ,
we have to solve the system of the following six algebraic nonlinear equations:
g(x2, λ, a) = K−,
g(x1, λ, a) = K−,
(3.18)
g(y2, λ, a) = −K+,
g(y1, λ, a) = −K+,
(3.19)
 x2
x1
g(s, λ, a) ds = K−(x2 −x1) + c−,
(3.20)
 y1
y2
g(s, λ, a) ds = −K+ (y1 −y2) −c+,
(3.21)
where g is as in (3.15).
At this point, it is worth observing that pa and ma are, respectively, the
scale function and the speed measure of the uncontrolled Itˆo diffusion
dXt = −sgn(Xt −a)b(Xt) dt + σ(Xt) dWt.
The following result asserts that a solution to the HJB equation (3.1) that
conforms with all of the heuristic considerations above indeed exists. Its proof
is given in the Appendix.
Lemma 3.1. Suppose that Assumption 2.1 holds. The system (3.18)–(3.21)
has a solution (y2, y1, a, x1, x2, λ) such that y2 < y1 < a < x1 < x2, and, if
w is the function defined by (3.6), (3.8) and (3.14), then w ∈W 2,∞
loc (R), w
satisfies (3.9), and the pair (w, λ) is a classical solution to the HJB equation
(3.1).
We can now establish our main result.
Theorem 3.1. Consider the control problem formulated in Section 2, suppose
that Assumption 2.1 holds and let (w, λ) be the solution to the HJB equation
(3.1) provided by Lemma 3.1. Given any initial condition x ∈R,
λ =
inf
Cx∈Cx J(Cx),
(3.22)
and the strategy discussed above, which is constructed rigorously in the proof
below, is optimal.
Proof. Throughout this proof, we fix the solution (w, λ) to the HJB equation
(3.1) constructed in Lemma 3.1. We also fix an initial condition x ∈R.

Control of One-Dimensional Itˆo Diffusions
303
Consider any admissible control Cx ∈Cx such that J(Cx) < ∞. Using
Itˆo’s formula, we calculate that
w(XT +) = w(x) +
 T
0
1
2σ2(Xs)w′′(Xs) + Usw′(Xs)

ds
+
 T
0
σ(Xs)w′(Xs) dWs +

s∈[0,T ]
[w(Xs + ∆Zs) −w(Xs)] ,
implying the representation
IT (Cx) :=
 T
0
h(Xs) ds +

s∈[0,T ]

K+∆Zt + c+
1{∆Zt>0}
+

s∈[0,T ]

−K−∆Zt + c−
1{∆Zt<0}
= λT + w(x) −w(XT +) +
 T
0
σ(Xs)w′(Xs) dWs
+
 T
0
1
2σ2(Xs)w′′(Xs) + Usw′(Xs) + h(Xs) −λ

ds
+

s∈[0,T ]

w(Xs + ∆Zs) −w(Xs) + K+∆Zs + c+
1{∆Zs>0}
+

s∈[0,T ]

w(Xs + ∆Zs) −w(Xs) −K−∆Zs + c−
1{∆Zs<0}.
(3.23)
With reference to (2.2), we note that Utw′(Xt) ≥−b(Xt)|w′(Xt)|. Combining
this observation with the fact that (w, λ) satisfies the HJB equation (3.1), we
get the bound
IT (Cx) ≥λT + w(x) −w(XT +) +
 T
0
σ(Xs)w′(Xs) dWs.
(3.24)
By construction, w is C1, w′(x) = K−for all x ≥x2, and w′(x) = −K+
for all x ≤y2. Therefore, there exists a constant C3 > 0 such that
w(x) ≤C3(1 + |x|)
and
|w′(x)| ≤C3,
for all x ∈R.
(3.25)
For such a choice of C3, (3.24) yields
IT (Cx) ≥λT + w(x) −C3 −C3 |XT +| +
 T
0
σ(Xs)w′(Xs) dWs.
(3.26)
Now, with respect to Assumption 2.1.(c),

304
A. Jack and M. Zervos
∞> J(Cx) ≥−C2 + C2 lim sup
T →∞
1
T Ex
B T
0
|Xs| ds
C
.
(3.27)
These inequalities imply that
Ex
B T
0
|Xs| ds
C
< ∞for all T > 0,
(3.28)
lim inf
T →∞
1
T Ex [|XT +|] = 0.
(3.29)
To see (3.29), suppose that lim infT →∞T −1Ex [|XT +|] > ε > 0. This implies
that there exists T1 ≥0 such that Ex [|Xs+|] > εs/2, for all s ≥T1. Since the
sample paths of X have countable discontinuities, it follows that
lim sup
T →∞
1
T Ex
B T
0
|Xs| ds
C
≥lim sup
T →∞
1
T
 T
T1
εs
2 ds = ∞,
which contradicts (3.27).
Taking into account (2.5) in Assumption 2.1, the second inequality in
(3.25), and (3.28), we obtain that
Ex
B T
0
[σ(Xs)w′(Xs)]2 ds
C
≤C2
3C1
B
T + Ex
B T
0
|Xs| ds
CC
< ∞
(3.30)
for all T > 0, proving that the stochastic integral in (3.26) is a square inte-
grable martingale and, therefore, has zero expectation. In view of this obser-
vation, we can take expectations in (3.26) and divide by T to get the bound
1
T Ex [IT (Cx)] ≥λ + w(x)
T
−C3
T −C3
T Ex [|XT +|] .
In view of (3.29) and the definition of IT (Cx) in (3.23), we can pass to the
limit T →∞to obtain J(Cx) ≥λ.
To prove the reverse inequality, suppose that we can find a control
ˆCx = ( ˆΩ, ˆF, ˆFt, ˆPx, ˆW, ˆU, ˆZ, ˆX, ˆτ) ∈Cx
such that
ˆUt = −sgn( ˆXt −a)b( ˆXt),
(3.31)
ˆXt+ ∈[y2, x2],
(3.32)
∆ˆZt1{∆ˆZt>0} = (y1 −y2)1{ ˆ
Xt=y2},
(3.33)
∆ˆZt1{∆ˆ
Zt<0} = −(x2 −x1)1{ ˆ
Xt=x2},
(3.34)

Control of One-Dimensional Itˆo Diffusions
305
for all t ≥0, ˆPx-a.s.. Plainly, (3.32) implies that ˆX is non-explosive, so that
ˆτ = ∞ˆPx-a.s. Also, since w satisfies (3.9), ˆUtw′( ˆXt) = −b( ˆXt)|w′( ˆXt)|. In
view of this observation and (3.6)–(3.8), we can see that, in this context, (3.23)
implies the equality
IT (ˆCx) = λT + w(x) −w( ˆXT +) +
 T
0
σ( ˆXs)w′( ˆXs) d ˆWs.
(3.35)
Now, (2.5) in Assumption 2.1, (3.25) and (3.32) imply that
Ex
B T
0
)
σ( ˆXs)w′( ˆXs)
2
ds
C
≤C2
3C1 (1 + |y2| ∨|x2|) T < ∞
for all T > 0, which proves that the stochastic integral in (3.35) is a square
integrable martingale, and
lim
T →∞
1
T Ex
)
|w( ˆXT +)|

≤lim
T →∞
C3 (1 + |y2| ∨|x2|)
T
= 0.
It follows that
lim
T →∞
1
T Ex
)
IT (ˆCx)

= λ,
which proves that J(ˆCx) = λ, and establishes (3.22).
It remains to construct a control ˆCx ∈Cx satisfying (3.31)–(3.34), which
amounts to constructing a weak solution ( ˆΩ, ˆF, ˆFt, ˆPx, ˆW, ˆZ, ˆX) to the SDE
d ˆXt = −sgn( ˆXt −a)b( ˆXt) dt + d ˆZt + σ( ˆXt) d ˆWt
(3.36)
that satisfies (3.32)–(3.34). To this end, we fix a filtered probability space
( ˆΩ, ˆF, ¯Ft, ˆPx) satisfying the usual conditions and supporting a standard
(scalar) Brownian motion ¯W. By appealing to a simple induction argument,
we construct a c`agl`ad piecewise constant process ¯Z with ¯Z0 = 0 such that, if
¯Xt := pa(x) + ¯Zt + ¯Wt,
(3.37)
then
¯Xt+ ∈[pa(y2), pa(x2)] ,
(3.38)
∆¯Zt1{∆¯
Zt>0} = (pa(y1) −pa(y2)) 1{ ¯
Xt=pa(y2)},
(3.39)
∆¯Zt1{∆¯
Zt<0} = −(pa(x2) −pa(x1)) 1{ ¯
Xt=pa(x2)}
(3.40)
ˆPx-a.s. for all t ≥0. The function pa appearing here is the solution to the
ODE
1
2σ2(x)p′′
a(x) −sgn(x −a)b(x)p′
a(x) = 0,
(3.41)
that is given by (3.16). In what follows, we denote by qa the inverse function
of pa. For future reference, we note that the derivatives of qa satisfies the
relations

306
A. Jack and M. Zervos
q′
a (pa(x)) =
1
p′a(x)
and
q′′
a (pa(x)) = −p′′
a(x)
[p′a(x)]3 .
(3.42)
Now, we consider the continuous increasing process
At :=
 t
0
˜σ−2( ¯Xs) ds,
where
˜σ(x) := p′
a

qa(x)

σ

qa(x)

,
x ∈R,
(3.43)
and we observe that limt→∞At = ∞due to (2.5) in Assumption 2.1 and
(3.38). Also, we denote by C the inverse of A defined by
Ct := inf {s ≥0 | As > t} ,
and we note that limt→∞Ct = ∞. Since C is continuous, if we define
ˆFt := ¯FCt,
˜Xt := ¯XCt,
˜Zt := ¯ZCt
and
Mt := ¯WCt,
(3.44)
then
˜X, ˜Z are c`agl`ad ( ˆFt)-adapted processes satisfying (3.38)–(3.40),
(3.45)
and M is a continuous ( ˆFt)-local martingale. Furthermore, if we define
ˆWt :=
 t
0
˜σ−1( ˜Xs) dMs,
then, in view of (3.37) and (3.44),
d ˜Xt = d ˜Zt + ˜σ( ˜Xt) d ˆWt,
˜
X0 = pa(x).
To see that ˆW is a standard ( ˆFt)-Brownian motion, we first observe that
⟨M⟩t = Ct =
 Ct
0
˜σ2( ¯Xs) dAs =
 t
0
˜σ2( ˜Xs) ds,
the last equality following due to the time change formula and the fact that
ACs = s. It follows that
⟨ˆW⟩t =
 t
0
˜σ−2( ˜Xs) d⟨M⟩s = t.
By L´evy’s characterisation theorem, this calculation and the fact that ˆW is a
continuous ( ˆFt)-local martingale imply that ˆW is an ( ˆFt)-Brownian motion.
Finally, we define
ˆXt := qa( ˜Xt)
and
ˆZt := 1{t>0}

s∈[0,t[
)
qa( ˜Xs + ∆˜Zs) −qa( ˜Xs)

.
(3.46)

Control of One-Dimensional Itˆo Diffusions
307
In view of (3.45), we can verify that these processes satisfy (3.32)–(3.34), while
an application of Itˆo’s formula yields
ˆXt = x +
 t
0
1
2 ˜σ2
pa( ˆXs)

q′′
a

pa( ˆXs)

ds + ˆZt
+
 t
0
˜σ

pa( ˆXs)

q′
a

pa( ˆXs)

d ˆWs.
However, this SDE, (3.41), (3.42) and the identity
˜σ

pa(x)

= p′
a(x)σ(x),
x ∈R,
which follows from the definition of ˜σ in (3.43), imply that (3.36) is satisfied,
and the construction is complete.
✷
Appendix: Proof of Lemma 3.1
Before addressing the proof of Lemma 3.1, we first establish some preliminary
results. For easy future reference, we list the formulae:
∂g
∂x(x, λ, a) = −
2
σ2(x)

h(x) −b(x)|g(x, λ, a)| −λ

,
(3.47)
∂g
∂λ(x, λ, a) =

p′
a(x)ma ([a, x]) > 0,
if x > a,
−p′
a(x)ma ([x, a]) < 0,
if x < a,
(3.48)
which follow from the definition of g in (3.15). The development of our analysis
requires the following definitions:
λ∗(a) := inf

λ ∈R | sup
x≥a
g(x, λ, a) = ∞

,
for a ∈R,
(3.49)
∗λ(a) := inf

λ ∈R | inf
x≤a g(x, λ, a) = −∞

,
for a ∈R,
(3.50)
with the usual convention inf ∅= ∞.
Lemma 3.2. Fix a ∈R and suppose that Assumption 2.1 is true. If λ∗(a) and
∗λ(a) are defined by (3.49) and (3.50), respectively, then λ∗(a), ∗λ(a) ∈]0, ∞],
and
lim
x→∞g(x, λ, a) =

−∞,
if λ < λ∗(a),
∞,
if λ ∈[λ∗(a), ∞] ∩R,
(3.51)
lim
x→−∞g(x, λ, a) =

∞,
if λ < ∗λ(a),
−∞,
if λ ∈[∗λ(a), ∞] ∩R.
(3.52)

308
A. Jack and M. Zervos
Proof. We first prove that, given any λ, a ∈R,
the equation g(x, λ, a) = 0 has at most two solutions x ∈]a, ∞[, (3.53)
and at most two solutions x ∈] −∞, a[.
Fix λ, a ∈R, and consider the solvability of g(x, λ, a) = 0 for x ∈]a, ∞[.
Assumption 2.1.(c) implies that there exist at most two points x > a such
that h(x) = λ. Also, (3.47) implies that
given any x > a such that g(x, λ, a) = 0,
(3.54)
∂g
∂x(x, λ, a) = −
2
σ2(x) [h(x) −λ] .
Combining these observations with the boundary condition g(a, λ, a) = 0, we
can conclude that the number of solutions of g(x, λ, a) = 0 inside ]a, ∞[ is less
than or equal to the number of solutions of h(x) = λ inside ]a, ∞[, which is
at most two. Similarly, we show that the number of solutions of g(x, λ, a) = 0
inside ] −∞, a[ is also less than or equal to two.
Now, we show that
lim
x→∞g(x, λ, a),
lim
x→−∞g(x, λ, a) ∈{−∞, ∞},
for all a, λ ∈R.
(3.55)
With reference to (3.53), the conclusion limx→∞g(x, λ, a) ∈{−∞, ∞} will
follow if we show that either of
lim inf
x→∞g(x, λ, a) ∈[0, ∞[,
lim sup
x→∞g(x, λ, a) ∈] −∞, 0],
(3.56)
leads to a contradiction. Assuming that the first relation in (3.56) is true, we
choose a sequence xn →∞such that
lim
n→∞g(xn, λ, a) = lim inf
x→∞g(x, λ, a)
and
lim
n→∞
∂g
∂x(xn, λ, a) = 0.
Assuming that the second relation in (3.56) holds, we choose a sequence (xn) in
a similar fashion. In either case, we define γ := supn≥1 |g(xn, λ, a)|. Observing
that γ ∈R, and referring to (3.47) we calculate:
0 = lim
n→∞
−2
σ2(xn) [h(xn) −b(xn)g(xn, λ, a) −λ]
≤lim
n→∞
−2
σ2(xn) [h(xn) −b(xn)γ −λ]
= −∞,
the inequality following because b ≥0, and the last equality following thanks
to Assumption 2.1.(d). This calculation provides the required contradiction.
Likewise, we can show that limx→−∞g(x, λ, a) ∈{−∞, ∞}.

Control of One-Dimensional Itˆo Diffusions
309
We can now prove the claims made relative to λ∗(a). With regard to the
definition of g in (3.15), the positivity of h and a simple continuity argu-
ment, we can see that λ∗(a) ∈]0, ∞]. Also, the fact that g(x, ·, a) is strictly
increasing, for all x > a, which follows from (3.48), implies that
sup
x≥a
g(x, λ, a)

< ∞,
for all λ < λ∗(a),
= ∞,
for all λ ∈]λ∗(a), ∞] ∩R.
To show that supx≥a g(x, λ∗(a), a) = ∞, and thus, in the light of (3.55),
complete the proof of (3.51), we argue by contradiction. To this end, we assume
that λ∗(a) < ∞and
lim
x→∞g(x, λ∗(a), a) = −∞.
This limit and Assumption 2.1.(c) imply that there exists ˆx(a) > a such that
g(x, λ∗(a), a) < 0
and
h(x) −λ∗(a) > 0,
for all x ≥ˆx(a).
(3.57)
In view of the fact that limx→∞g(x, λ, a) = ∞, for all λ > λ∗(a), (3.54)
and the second inequality in (3.57), we can appeal to a simple contradiction
argument to see that
g(x, λ, a) > 0,
for all x ≥ˆx(a) and λ > λ∗(a).
However, this and the first inequality in (3.57) imply that
lim
λ↓λ∗(a) g(x, λ, a) ≥0 > g(x, λ∗(a), a),
for all x ≥ˆx(a),
contradicting the continuity of g.
Proving the statements relating to ∗λ(a) involves similar arguments.
✷
It is worth noting that the consideration of λ∗and ∗λ is not a redundant
exercise. Indeed, we can easily construct examples in which λ∗(0), ∗λ(0) < ∞.
With reference to the structure of the system of equations (3.18)–(3.21), which
involves the functions g(·, ·, ·)+K+ and g(·, ·, ·)−K−, we consider the following
definitions:
λ∗(a) := inf

λ > 0 | sup
x≥a
g(x, λ, a) ≥K−

,
(3.58)
∗λ(a) := inf

λ > 0 | inf
x≤a g(x, λ, a) ≤−K+

.
(3.59)
Lemma 3.3. Given a ∈R, λ∗(a) > λ∗(a) > 0, the equation g(x, λ, a) = K−
defines uniquely two C1-functions x1(·, a), x2(·, a) : ]λ∗(a), λ∗(a)[ →R such
that
a < x1(λ, a) < x2(λ, a) and a+ < x2(λ, a), for all λ ∈]λ∗(a), λ∗(a)[,
where a+ is as in Assumption 2.1.(e). Furthermore, the following statements
are true:

310
A. Jack and M. Zervos
x1(·, a) (resp., x2(·, a)) is strictly decreasing (resp., increasing),
(3.60)
lim
λ↓λ∗(a) x1(λ, a) =
lim
λ↓λ∗(a) x2(λ, a),
lim
λ↑λ∗(a) x2(λ, a) = ∞,
(3.61)
h(x) −b(x)K−−λ > 0,
for all x > x2(λ, a).
(3.62)
Proof. Fix any a ∈R. In view of (3.15) and the positivity of h, we can see
that λ∗(a) > 0. Also, the definitions of λ∗(a), λ∗(a) and the continuity of g
imply trivially that λ∗(a) < λ∗(a).
Now, observe that a simple inspection of (3.47) reveals that
if x > a satisfies g(x, λ, a) = K−, then
(3.63)
∂g
∂x(x, λ, a) = −
2
σ2(x)

h(x) −b(x)K−−λ

.
With regard to the definitions of λ∗(a) and λ∗(a), (3.51) in Lemma 3.2, the fact
that g(a, λ, a) = 0, Assumption 2.1.(e) and the continuity of g, this observation
implies the following:
(I) If λ < λ∗(a), then the equation g(x, λ, a) = K−has no solutions
x ∈]a, ∞[.
(II) If λ ∈]λ∗(a), λ∗(a)[, then the equation g(x, λ, a) = K−has one solu-
tion x1(λ, a) > a such that
h(x1(λ, a)) −b(x1(λ, a))K−−λ < 0,
(3.64)
and one solution x2(λ, a) > x1(λ, a) such that
h(x2(λ, a)) −b(x2(λ, a))K−−λ > 0.
(3.65)
Moreover, (3.62) is true.
(III) If λ ≥λ∗(a), then the equation g(x, λ, a) = K−has one solution
x1(λ, a) > a such that
h(x1(λ, a)) −b(x1(λ, a))K−−λ < 0.
(3.66)
Since λ∗(a) > 0, Assumption 2.1.(e) and (3.65) imply that the solution x2
in (II) above satisfies x2(λ, a) > a+. Also, (I) and (II) and the continuity of g
imply the first equality in (3.61), while (II), (III) and (3.60) imply the second
equality in (3.61). To prove (3.60), we differentiate g(xj(λ, a), λ, a) = K−with
respect to λ to calculate that
∂xj
∂λ (λ, a) =
σ2(xj(λ, a)) ∂g
∂λ(xj(λ, a), λ, a)
2 [h(xj(λ, a)) −b(xj(λ, a))K−−λ],
for all λ ∈]λ∗(a), λ∗(a)[, j = 1, 2. However, this calculation, (3.48) and (3.64)
(resp., (3.65)) imply that the function x1(·, a) (resp., x2(·, a)) is strictly de-
creasing (resp., increasing), and the proof is complete.
✷
With regard to the problem’s data symmetry, we can trivially modify the
arguments of the preceding proof to establish the following result.

Control of One-Dimensional Itˆo Diffusions
311
Lemma 3.4. Given a ∈R, ∗λ(a) > ∗λ(a) > 0, and the equation g(x, λ, a) =
−K+ defines uniquely two C1 functions y1(·, a), y2(·, a) : ]∗λ(a), ∗λ(a)[→R
such that
y2(λ, a) < y1(λ, a) < a and y2(λ, a) < α−, for all λ ∈]∗λ(a), ∗λ(a)[
where α−is as in Assumption 2.1.(f). Furthermore,
y2(·, a) (resp., y1(·, a)) is strictly decreasing (resp., increasing),
(3.67)
lim
λ↓∗λ(a) y1(λ, a) =
lim
λ↓∗λ(a) y2(λ, a),
lim
λ↑∗λ(a) y2(λ, a) = −∞,
(3.68)
h(x) −b(x)K+ −λ > 0,
for all x < y2(λ, a).
(3.69)
Proof of Lemma 3.1. With reference to (3.20)–(3.21), we define the functions
Q∗(·, a) : ]λ∗(a), λ∗(a)[ →R and ∗Q(·, a) : ]∗λ(a), ∗λ(a)[ →R by
Q∗(λ, a) =
 x2(λ,a)
x1(λ,a)

g(s, λ, a) −K−
ds −c−,
(3.70)
∗Q(λ, a) =
 y1(λ,a)
y2(λ,a)

g(s, λ, a) + K+
ds + c+,
(3.71)
respectively, where x1, x2 are as in Lemma 3.3, and y1, y2 are as in Lemma 3.4.
Given these definitions, we will establish the claim regarding the solvability
of the system of equations (3.18)–(3.21) if we prove that
there exist ˜a ∈R and ˜λ ∈]λ∗(˜a), λ∗(˜a)[ ∩]∗λ(˜a), ∗λ(˜a)[
(3.72)
such that Q∗(˜λ, ˜a) = ∗Q(˜λ, ˜a) = 0.
Differentiating (3.70) with respect to λ, and using the fact that both of
g(x1(λ, a), λ, a) and g(x2(λ, a), λ, a) are equal to the constant K−, we calculate
∂Q∗
∂λ (λ, a) =
 x2(λ,a)
x1(λ,a)
∂g
∂λ(s, λ, a) ds > 0,
for λ ∈]λ∗(a), λ∗(a)[,
(3.73)
the inequality following thanks to (3.48) and the fact that a < x1 < x2. Also,
with regard to (3.48), (3.51) and (3.60)–(3.61) in Lemma 3.3, we can see that
lim
λ↓λ∗(a) Q∗(λ, a) = −c−< 0
and
lim
λ↑λ∗(a) Q∗(λ, a) = ∞.
(3.74)
Clearly, (3.73), (3.74) imply that there is a unique point Λ∗(a) ∈]λ∗(a), λ∗(a)[
such that Q∗(Λ∗(a), a) = 0. Similarly, we show that given any a ∈R, there is
a unique point ∗Λ(a) ∈]∗λ(a), ∗λ(a)[ such that ∗Q(∗Λ(a), a) = 0.
With regard to these calculations, (3.72) will follow if we prove that
there exists ˜a ∈R such that Λ∗(˜a) = ∗Λ(˜a).
(3.75)

312
A. Jack and M. Zervos
To this end, we differentiate Q∗(Λ∗(a), a) = 0 with respect to a to obtain
d
daΛ∗(a) = −
∂Q∗
∂a (Λ∗(a), a)
∂Q∗
∂λ (Λ∗(a), a)
.
(3.76)
Furthermore, we calculate that
∂p′
a
∂a (x) = −sgn(x −a) 2b(a)
σ2(a)p′
a(x),
for x ̸= a,
implying, in view of the definition of g in (3.15), that
∂g
∂a(x, λ, a) = 2 [h(a) −λ]
σ2(a)
p′
a(x),
for x ̸= a.
Using this calculation and the fact that g(x, λ, a) = K−for x = x1(λ, a) or
x = x2(λ, a), we can see that
∂Q∗
∂a (λ, a) = 2 [h(a) −λ]
σ2(a)
 x2(λ,a)
x1(λ,a)
p′
a(s) ds.
This, combined with (3.73) and (3.76), implies that
d
daΛ∗(a) > 0 for all a ∈R such that h(a) < Λ∗(a).
(3.77)
Using similar arguments, we can also show that
d
da
∗Λ(a) < 0, for all a ∈R such that h(a) < ∗Λ(a).
(3.78)
Now, if we assume that h(a) < Λ∗(a), for all a ∈R, then (3.77) implies
h(a) < Λ∗(a) < Λ∗(0)
for all a < 0,
which contradicts Assumption 2.1.(c). With respect to the usual convention
sup ∅= −∞, it follows that A−:= sup {a ∈R | Λ∗(a) ≤h(a)} > −∞. More-
over, since λ∗(a) < Λ∗(a), and h(a) < λ∗(a) for all a > 0 (see (3.15) and recall
the definition of λ∗(a) and Assumption 2.1.(c)), it follows that
A−:= sup {a ∈R | Λ∗(a) ≤h(a)} ∈] −∞, 0[.
(3.79)
Using a similar reasoning, we can also show that
A+ := inf {a ∈R |
∗Λ(a) ≤h(a)} ∈]0, ∞[.
(3.80)
With regard to (3.77)–(3.80), it follows that
the function Λ∗(·) −∗Λ(·) is strictly increasing
(3.81)
on the interval ]A−, A+[.

Control of One-Dimensional Itˆo Diffusions
313
To proceed further, suppose that we have the inequality ∗Λ(A+) ≥Λ∗(A+),
so that h(A+) ≥∗Λ(A+) ≥Λ∗(A+). Then, (3.15) and Assumption 2.1.(c)
combined with the fact that A+ > 0 imply the inequality
g(x, Λ∗(A+), A+) < 0
for all x > A+,
which contradicts the definition of Λ∗. However, this proves that
Λ∗(A+) −∗Λ(A+) > 0.
(3.82)
Similarly, we can prove the inequality Λ∗(A−)−∗Λ(A−) < 0, which, combined
with (3.81) and (3.82), implies (3.75), and, therefore, (3.72). Moreover, these
arguments show that
h(˜a) < ˜λ.
(3.83)
Now, with ˜a, ˜λ being as in (3.72), we define
w′(x) := g(x, ˜λ, ˜a),
for x ∈[y2, x2] ≡[y2(˜λ, ˜a), x2(˜λ, ˜a)].
(3.84)
With regard to our construction thus far, this, (3.6) and (3.8) define a unique,
modulo an additive constant, function w ∈W 2,∞
loc (R) satisfying (3.6)–(3.8).
With reference to (3.51) and (3.52) in Lemma 3.2 and (3.72), we can see that
lim
x→−∞g(x, ˜λ, ˜a) = ∞
and
lim
x→∞g(x, ˜λ, ˜a) = −∞.
With regard to the definition of g in (3.15) and (3.83), we can combine these
asymptotics with (3.53), the fact that g(˜a, ˜λ, ˜a) = 0 and the fact that
g

y2(˜λ, ˜a), ˜λ, ˜a

= −K−< 0 < K+ = g

x2(˜λ, ˜a), ˜λ, ˜a

,
to conclude that w satisfies (3.9) as well.
To complete the proof, we still need to prove that the function w satisfies
the HJB equation (3.1). With regard to its construction, this will follow if we
show that
1
2σ2(x)w′′(x) −b(x)w′(x) + h(x) −λ ≥0,
for x > x2,
(3.85)
1
2σ2(x)w′′(x) + b(x)w′(x) + h(x) −λ ≥0,
for x < y2,
(3.86)
w(x + z) −w(x) −K−z + c−≥0,
for z < 0, x ∈R,
(3.87)
w(x + z) −w(x) + K+z + c+ ≥0,
for z > 0, x ∈R.
(3.88)
In view of (3.84), inequalities (3.85) and (3.86) follow by a straightforward
calculation that shows that they are implied by the bounds (3.62) and (3.69),
respectively. Inequality (3.87) is equivalent to
−
 x
x+z

w′(s) −K−
ds + c−≥0,
for z < 0, x ∈R.
(3.89)

314
A. Jack and M. Zervos
With regard to (3.9), the inequalities
w′(x)





< K−,
for x < x1,
> K−,
for x ∈]x1, x2[,
= K−,
for x > x2,
and equation (3.70), it is straightforward to show that (3.89) is true. Finally,
the proof of (3.88) is similar.
✷
References
1. Cadenillas, A., Zapatero, F.: Optimal central bank intervention in the foreign
exchange market. J. Econom. Theory 87, 218–242, (1999)
2. Cadenillas, A., Zapatero, F.: Classical and impulse stochastic control of the
exchange rate using interest rates and reserves. Math. Finance 10, 141–156,
(2000)
3. Chiarolla, M.B., Haussmann, U.G.: Optimal control of inflation: a central bank
problem. SIAM J. Control Optim. 36, 1099–1132, (1998)
4. Harrison, J.M., Sellke, T.M., Taylor, A.J.: Impulse control of Brownian motion.
Math. Oper. Res. 8, 454–466, (1983)
5. Jack, A., Zervos, M.: Impulse control of one-dimensional Itˆo diffusions with an
ergodic criterion. Submitted.
6. Jeanblanc-Picqu´e, M.: Impulse control method and exchange rate. Math. Fi-
nance 3, 161–177, (1993)
7. Krylov, N.V.: Controlled Diffusion Processes. Springer, New York-Berlin, 1980
8. Mundaca, G., Øksendal, B.: Optimal stochastic intervention control with appli-
cation to the exchange rate. J. Math. Econom. 29, 225–243, (1998)
9. Shiryaev, A. N.: Optimal Stopping Rules. Springer, New York-Heidelberg, 1978

A Consumption–Investment Problem with
Production Possibilities
Yuri KABANOV1 ∗and Masaaki KIJIMA2
1 Universit´e de Franche-Comt´e, 16 Route de Gray,
F-25030 Besan¸con Cedex, France,
Central Economics and Mathematics Institute, Moscow, Russia.
kabanov@math.univ-fcomte.fr
2 Daiwa Chair, Graduate School of Economics, Kyoto University,
Yoshida-Honmachi, Sakyo-ku, Kyoto 606-8501, Japan.
kijima@econ.kyoto-u.ac.jp
Summary. We investigate a consumption-investment problem in the setting of cor-
porate finance considering a single agent disposing production possibilities. He can
invest funds into both manufacturing and financial assets diversifying the income.
The agent, endowed with an initial fund as well as initial production assets, strives
to maximize the total expected utility from consumption over the finite time hori-
zon. We establish for this problem a separation theorem. Namely, it can be solved
by a two-stage procedure. The first stage is an independent optimization problem
for the manufacturing arm and the second one is a standard Merton consumption-
investment (portfolio selection) problem. The input parameter of the latter, the
initial budget, is determined by the optimal value of the manufacturing problem
for which the Bismut stochastic maximum principle is the necessary and sufficient
condition of optimality. In the case of deterministic coefficients and absence of ran-
dom fluctuations the first problem is a classical deterministic problem which can be
analyzed by the classical Pontriagin maximum principle. In particular examples we
obtain closed form solutions and show that in certain cases the optimal production
trajectories exhibit a turnpike behavior.
Key words: Consumption–investment problem, portfolio, production, stochastic
equation, martingale, backward stochastic differential equation, Bismut stochastic
maximum principle, Pontriagin maximum principle, turnpike
Mathematics Subject Classification (2000): 60G44
∗This research was done during the stay of the author at Daiwa Chair of Graduate
School of Economics, Kyoto University.

316
Yu. Kabanov and M. Kijima
It is a pleasure to start this paper by a short historical comment relevant
to our anniversary volume. The mathematical tools used in the note below are
common nowadays but in the early seventies they were the newest “hot” top-
ics of the seminar leaded by Albert Shiryaev and their development, to great
extent, was inspired by him. In this period, the seminar, due to his inex-
haustible energy and charisma, became one of the world centers in stochastic
calculus and control. We can only admire Shiryaev’s intuition to concentrate
efforts on the directions which were later recognized as the most important in
the theory of random processes and its applications, in particular, in math-
ematical finance. He was one of the first who understood the importance of
the predictable representation theorem due to J.M.C. Clark (1971), related,
as we know now, with the fundamental concept of market completeness. He
suggested me, as the subject of my diploma project, to find an easier proof
of this theorem and extend it to jump processes. It was the beginning of my
studies as a mathematician. Another area of his interests was the Girsanov
theorem and problems of absolute continuity. Shiryaev and his collaborators
(many of are authors of this book) published a number of papers on this
subject which constitutes an accomplished theory. Experience in these fields
which form the heart of modern stochastic finance was very useful in sub-
sequent studies in arbitrage theory. Optimal control was another preferable
topic of the seminar. I remember our excitement when Shiryaev brought from
France the first preprints by Bismut on backward stochastic equations and
stochastic maximum principle. He explained the importance of new concepts
and inspired members of the seminar to make research in this field (several
papers by Arkin, Saksonov and myself were published more when a decade
before the revival of the interest to BSDEs elsewhere).
Yuri Kabanov
1 Introduction
We consider here a consumption–investment decision problem for a single
“small” economic agent which can be viewed as a firm having production
and financial arms. The initial endowment is in both assets. The problem is
to maximize the total expected utility of the consumption rate over a finite
time interval [0, T] investing into the production as well as in the financial
assets. It is assumed that the agent has an access to a frictionless security
market with d + 1 assets, one of which is riskless and the others are risky.
The market model is fairly standard: it is of the same type as in Karatzas et
al. [10], see also Cox and Huang [4] and the expository paper [9]. Allocating
the resources, the agent may invest funds into m production assets. This type
of assets has features different from that of financial assets in the following
two points. The investments into the manufacturing arm are irreversible. The
profit flow from the production at time t is R(t, Kt) where Kt = (K1
t , ..., Km
t )

A Consumption–Investment Problem with Production Possibilities
317
is the capital accumulation. The latter subjects random depreciations and,
eventually, fluctuations due to external factors. The production assets cannot
be cashed back before the terminal date T when the production arm can be
sold at the price Q(KT ). A similar problem was considered by Hirayama and
Kijima in [8].
The agent in this model may be an owner of a small firm that produced
some production goods. The consumption in this case can be interpreted as
the dividend flow from the firm. The owner does not want to sell the business,
since the ownership for him is very important (this is rather typical, especially,
in such country as Japan). The role of the owner is to maximize the total utility
from dividend. To do so, the owner may want to invest the limited fund in the
production assets as much as possible to earn higher profits. But, since there
is a financial market, he may also allocate a part of his wealth in securities.
The problem for the owner is to decide portfolio strategy, dividend strategy,
and production strategy so as to maximize the objective.
As we mentioned already, without the production arm, our model is
reduced to the mainstream continuous-time portfolio optimization problem
started in the famous papers by Merton [15], [16] and developed further in
numerous publications (see, e.g., [4], [9], [10], [11], [17] and references therein).
Production models were considered in [14] but without financial investments
while the equilibrium approach to production economies was discussed in [19].
In real economies, firms invest their surplus funds in financial assets. It seems
of interest to study optimal strategies in this more general context.
In our presentation we try to avoid technicalities. That is why we work with
the easily treated hypotheses, preferring, e.g., the boundedness assumption on
coefficients to that of integrability. Our main message is that for the linear
model with concave utility and production functions the problem can be split
into two separate stages. First, the optimal production investment process
Io = (Io
t ) can be found independently of the other counterparts of the optimal
control as the optimal solution of a certain auxiliary control problem. Finding
Io, we have to solve, as the second stage, a classical portfolio problem which,
as well-known, consists itself of two separate parts: a search for the optimal
consumption and a search for the optimal investment (that is why we can say
also that the whole problem has three stages).
This separation principle is the main feature of the considered model. It
is quite understandable because in the case of a complete market a suitably
integrable stochastic income (from the production, in our case) leads only to
a change of the initial endowment of the Merton problem. This fact (used
already in [8]) is now well-known, see, e.g., the paper [5] where the stochastic
income is bounded. Our hypothesis and the definition of admissible strategies
ensures the applicability of this principle.
We prove the needed existence of the optimal solution for the auxiliary
problem (using the Koml´os theorem) and derive necessary and sufficient con-
ditions of optimality in the form of the Bismut maximum principle providing
a self-contained exposition of the latter for the considered case.

318
Yu. Kabanov and M. Kijima
We investigate in more details a particular case of the model where the pro-
duction block is not directly influenced by random perturbations. In this case
the first stage is a deterministic control problem, still interesting, which can be
analyzed on the basis of the Pontryagin maximum principle. We give examples
where the optimal production policy is of the bang–bang type. We provide
also an example showing that in a long-run the optimal production trajecto-
ries follow a “turnpike”. This means that there exists a function, independent
on the initial endowment and the terminal (liquidation) cost, with which the
optimal production trajectory coincides except its first part (depending on
the “starting point”) and its final part (depending on the “destination”, i.e.
of the terminal cost functional).
We use vector notations; in particular, xy stands for the scalar product
and diag x denotes the diagonal operator corresponding to the vector x.
2 Model Description
We shall work in the standard probabilistic framework assuming that the
stochastic basis (Ω, F, F = (Ft), P) is fixed and the filtration is spanned by a
d-dimensional Wiener process W. The time horizon T is finite.
First, we describe the production arm of the firm. It disposes m assets and
if K ∈Rm
+ is a vector of values of these assets, the rate of the profit flow at
time t is R(t, K). The production asset i is depreciated with the rate λi which
is, in general, a non-negative bounded predictable process. Its value also may
fluctuate due to external factors. The capital accumulation evolves according
to the stochastic differential equations
dKi
t = (Ii
t −λi
tKi
t)dt + Ki
tdLi
t,
Ki
0 = ki,
(2.1)
where L is a martingale with
dLi
t =
d

j=1
σij
t dW j
t ,
i ≤m,
for some bounded predictable matrix-valued process σ.
The investments are assumed to be irreversible, i.e. the capital accumula-
tion may decrease only by depreciation and by random fluctuations (if σ = 0,
the latter are not taken into account). The production strategy I is a pre-
dictable process with values in a compact convex subset Γ of Rm
+. It follows
(by a standard arguments based on the Gronwall–Bellman lemma) that the
sup norm of the capital accumulation process are bounded by a square inte-
grable random variable.
The production assets cannot be sold before T, but they can be liquidated
at the price Q(KT ) at the terminal date. It is natural to assume that in the

A Consumption–Investment Problem with Production Possibilities
319
variable K the functions R and Q are concave and increasing (component-
wise).
Since the concave function is dominated by a linear one, the family of
random variables Q(KT ), K is a capital accumulation process, is dominated
by a random variable from L2. The same property holds for the family of
random variables
 T
0 R(s, Ks)ds when
R(s, K) ≤f(s)(1 + lK),
where l ∈Rm and f is a function integrable on the interval [0, 1]; we assume
that this condition is always fulfilled.
Thus, our set of assumptions ensures the following important property:
 T
0
R(s, Ks)ds + Q(KT ) ≤ζ ∈L2.
(2.2)
The agent also has an access to a frictionless financial market of the Black–
Scholes type with d+1 securities. One of them is non-risky (“bond” or “bank
account”) and has the price evolving as
dP 0
t
P 0
t
= rtdt,
P 0
0 = p0 = 1.
(2.3)
For simplicity, mainly, notational, we suppose from the very beginning that
r = 0, i.e. bond is the num´eraire and all investments are measured in its units.
The prices of remaining assets, (risky) stocks, are modelled by the sto-
chastic equations
dP i
t
P i
t
= bi
tdt + dM i
t,
P i
0 = pi,
(2.4)
where M is a square integrable martingale generating our basic filtration F
(of the Wiener process W). We assume more specifically that
dM i
t =
d

j=1
Σij
t dW j
t ,
i ≤d.
The vector of instantaneous rate of returns b and the (non-degenerate) volatil-
ity matrix Σ and its inverse Σ−1 are assumed to be bounded predictable
processes.
The agent’s portfolio at date t contains ni
t units of the asset i. His holdings
in risky assets of the financial market πi
t = ni
tP i
t , 1 ≤i ≤d, are predictable
processes such that
 T
0
|πt|2dt < ∞.
The agent consumption intensity is a predictable non-negative process c = (ct)
with

320
Yu. Kabanov and M. Kijima
 T
0
ctdt < ∞.
The triplet of the investment processes and consumption u = (π, I, c) is
the control strategy. The optimization problem can be formulated as:
E
 T
0
e−βtU(ct)dt →max,
(2.5)
with the controlled dynamics of the total fund given by the following stochastic
differential equation where 1 := (1, ..., 1):
dXt = (R(t, Kt) −1It −ct)dt + πt(btdt + dMt),
X0 = x.
(2.6)
To avoid technicalities, we suppose that the utility function U : R+ →R+
in (2.5) is a concave increasing function vanishing at zero with U ′(0) = ∞
and U ′(∞) = 0 (note that U is differentiable everywhere except at most a
countable number of points).
In addition to the constraints indicated above we impose a constraint on
the controls which prevents a “bankruptcy” before the date T. Namely, we
shall consider as admissible only the controls u such that
Vt := Xt + ˜E
B T
t
R(s, Ks)ds + Q(KT )|Ft
C
≥0,
∀t ≤T.
(2.7)
The symbol ˜E indicates that the expectation is taken with respect to the
(unique) martingale measure ˜P. The corresponding term can be interpreted
as the market evaluation of the manufacturing arm of the company. This
makes plausible the assumption that the agent may borrow funds until this
level.
The set of admissible strategies, denoted by A(y), depends on the initial
endowment y := (x, k).
We shall assume that A(y) ̸= ∅, i.e. at least one admissible strategy u does
exist. Obviously, this is always the case when R and Q are non-negative, since
u = (0, 0, 0) belongs to A(y).
Recall that ˜P = ZT P where
Zt = exp
 t
0
θsdWs −1
2
 t
0
|θs|2ds

,
with θs := −Σ−1
s bs. Under ˜P
˜Wt := Wt −
 t
0
θsds
is a Wiener process. Due to the boundedness of θ the random variable ZT is
square integrable. Thus, the random variable ζ in (2.2) belongs to L1( ˜P). In

A Consumption–Investment Problem with Production Possibilities
321
particular, the conditional expectation in (2.7) is well-defined. Moreover, for
an admissible strategy, we have
 T
0
R(s, Ks)ds + Q(KT ) ∈L1( ˜P).
Remark. The completeness of the financial market, i.e. the uniqueness of the
martingale measure, is essential for our further development: we rely on the
martingale representation theorem. The latter does not hold for more general
models of incomplete market (which may constitute one of possible directions
of future studies) where the natural extension of the admissibility condition
(2.7) involves the supremum of expectations over the set of all martingale
measures.
3 Existence and Structure of the Optimal Control
Take an arbitrary admissible control. Under the measure ˜P the dynamics of
the phase variable (2.6) can be rewritten as follows:
Xt = x +
 t
0
(R(s, Ks) −1Is −cs)ds +
 t
0
πsd ˜
Ms,
(3.1)
where ˜
M is a (square integrable) martingale with respect to ˜P. Notice that
X ≥0 while the ordinary integral above is less or equal to ζ ∈L1( ˜P), see
the assumption (2.2). Thus, with respect to ˜P, the stochastic integral, being a
local martingale dominating an integrable random variable, namely, −(x+ζ),
is a supermartingale.
Substituting the expression (3.1) into (2.7), we obtain the formula
Vt = x + ˜E
B T
0
R(s, Ks)ds + Q(KT )|Ft
C
−
 t
0
(1Is + cs)ds +
 t
0
πsd ˜
Ms.
The definition of admissibility implies, in particular, that ˜EVT ≥0. Due to
the supermartingale property, the expectation of the stochastic integral with
respect to ˜P is negative and we infer the inequality
˜E
 T
0
csds ≤x −H(I)
(3.2)
where
H(I) := ˜E
B T
0
(1Is −R(s, Ks))ds −Q(KT )
C
.
(3.3)
Let us denote by C(y) the set of pairs of production and investment
processes (I, c) for which (3.2) holds.
The next lemma is established in the same way as in the classical consump-
tion–investment model, see, e.g., the textbook [12].

322
Yu. Kabanov and M. Kijima
Lemma 3.1. For any given (I, c) ∈C(y) there exists a portfolio process π
such that (π, I, c) ∈A(y).
Proof. Let (I, c) ∈C(y). Noticing that H(I) is finite, we consider the non-
negative process V with
Vt := ˜E
B T
0
(1Is + cs)ds|Ft
C
−
 t
0
(1Is + cs)ds
+x −˜E
B T
0
(1Is + cs −R(s, Ks))ds −Q(KT )
C
.
It can be written in the form
Vt = x + ˜E
B T
0
R(s, Ks)ds + Q(KT )|Ft
C
−
 t
0
(1Is + cs)ds + M V
t −M V
0 ,
where
M V
t := ˜E
B T
0
(1Is + cs −R(s, Ks))ds −Q(KT )|Ft
C
.
By the martingale representation theorem
M V
t −M V
0 =
 t
0
πsd ˜
Ms
and we infer easily from (2.7) and (3.1) that the triplet (π, I, c) ∈A(y).
✷
The conclusion following from this lemma is very important: solving the
original problem with a seemingly complicated “pointwise” constraint (2.7) is
reduced to the solving of a much simpler problem with a single “traditional”
inequality constraint given by a convex functional, with a consequent search
for the corresponding investment strategy. Moreover, it is easily seen that the
search for the optimal production and optimal consumption also can be done
in a separate consecutive way. Indeed, since the utility function is increasing,
for a given production strategy I with H(I) ≤x (such a strategy exists as
there is an admissible strategy u), the corresponding maximal value of the
functional is attended on a consumption strategy for which (3.2) holds with
the equality. The maximal possible value will correspond to Io on which H(I)
attains minimum. The existence of the optimal Io as well as the solution of
the consumption problem satisfying (3.2) follows from the Koml´os theorem -
we recall the arguments in Proposition 1 of the next section dealing with the
optimal production strategy. Summarizing, we arrive to the following
Theorem 3.1. In the solution (πo, Io, co)
∈
A(y) of the consumption-
investment problem with production possibilities the optimal investment Io
in manufacturing arm is the minimizer for the problem with the functional
(3.3) and the dynamics (2.1). The optimal consumption process co ≥0 is the

A Consumption–Investment Problem with Production Possibilities
323
solution of the maximization problem (2.5) under the constraint (3.2). The op-
timal portfolio strategy πo is the unique square-integrable predictable process
satisfying the identity
M V o
t
= M V o
0
+
 t
0
πo
sd ˜
Ms
with
M V o
t
:= ˜E
B T
0
(1Io
s + co
s −R(s, Ko
s))ds −Q(Ko
T )|Ft
C
.
4 Optimal Production Investment
Let us consider separately the optimal control problem
H(I) := ˜E
B T
0
(1Is −R(s, Ks))ds −Q(KT )
C
→min
(4.1)
over the convex set I of all Γ-valued predictable processes I and where K
is given by (2.1)3. This problem belongs to the well-studied class of convex
problems for which one can use duality methods.
Proposition 1. The minimization problem (2.1), (4.1) has a solution.
Proof. Now standard (and fast) way to prove the existence in the convex
optimal control problems is the reference to the Koml´os theorem. The latter
claims that for any L1-bounded sequence of random variables ξn there exist
a random variable ξ ∈L1 and a subsequence ξnk converging to ξ a.s. in the
Cesaro sense.
Let Ho = infI∈I H(I) and let H(In) →Ho for some In ∈I. Due to the
boundedness of Γ we can apply the Koml´os theorem to In considering these
processes as random variables on the space (Ω×[0, T], P, d ˜Pdt), where P is the
predictable σ-algebra. Renumbering, we may assume without loss of generality
that the original sequence converges d ˜Pdt-a.e. to some I in Cesaro sense. This
means simply that the controls ¯In := n−1 n
j=1 Ij converge (a.e.) to Io which
is, clearly, an element of I. Let us denote by ¯Kn and Ko the corresponding
capital accumulation processes. The solution of (2.1) can be written explicitly
via the (stochastic) Cauchy formula. The latter implies that, outside a null-set,
the sequence ¯Kn
t (ω) converges to Ko
t (ω) whatever is t ∈[0, T]. Moreover, the
sequence supt ¯Kn
t (ω) is bounded (by a constant depending on ω). Recalling
the hypothesis R(s, K) ≤f(s)(1 + lK), we deduce from here, using the Fatou
lemma for the integral and the continuity of R and Q in K, that
3Economically, this form suggests the minimization of losses, i.e. the manufac-
turing, presumably, is non-rentable; in more optimistic situation one could consider
the problem −H(I) →max, the maximization of profits.

324
Yu. Kabanov and M. Kijima
 T
0
(1Io
s−R(s, Ko
s))ds−Q(Ko
T ) ≤lim inf
B T
0
(1Io
s −R(s, ¯Kn
s ))ds −Q( ¯Kn
T )
C
.
Taking the ˜P-expectation with of the both side of this inequality and applying
again the Fatou lemma, this time with respect to ˜P (justified because the
random variable ζ in (2.2) belongs to L1( ˜P)) we obtain:
H(Io) ≤lim inf H(¯In) ≤lim inf n−1
n

j=1
H(Ij) = Ho.
Thus, H(Io) = Ho, i.e. Io is the optimal control.
✷
We shall assume from now on that R(t, K) and Q(K) have derivatives in
the variable K. The particular structure of the problem (2.1), (4.1) (linear
dynamics and convex functional) implies that the necessary condition of op-
timality given the Bismut stochastic maximum principle, see [2], [3], is also a
sufficient one. For the considered case the arguments are easy and the proof
can be done in a few lines. For the reader’s convenience we give them instead
sending him to a general theory presented in [20].
Isolating the ˜P-martingale term and using the abbreviation µt := λt−σtθt,
we rewrite the dynamics of manufacturing capital in vector notations as
dKt = (It −diag Ktµt)dt + diag Kt σtd ˜Wt,
K0 = k,
(4.2)
and introduce the Hamiltonian
H(t, K, I, p, h) := ⟨p, I −diag K µt⟩+ ⟨h, diag K σt⟩+ R(t, K) −⟨1, I⟩,
where p ∈Rm while h and diag K σt are m × d-matrices interpreted as ele-
ments of Rmd. Exceptionally, we use here the notation ⟨., .⟩for scalar products
following the traditional and easy to memorize form which was suggested by
Bismut. Note that the second term can be written as tr h(diag K σt)∗, where
∗denotes the transpose and tr the trace.
The maximum principle claims that the pair (Io, Ko) satisfying the equa-
tion
dKo
t = (Io
t −diag Ko
t µt)dt + diag Ko
t σtd ˜Wt,
Ko
0 = k,
(4.3)
is optimal for the problem (4.1), (4.2) if there exist a continuous pre-
dictable processes p with square integrable sup norm and a process h ∈
L2(Ω× [0, T], P, d ˜Pdt) solving the m-dimensional backward stochastic dif-
ferential equation (BSDE)
dpt = −∇H(t, Ko
t , Io
t , pt, ht)dt + htd ˜Wt,
pT = ∇Q(Ko
T ),
(4.4)
where ∇is the gradient in the variable K, specifically,
dpt = (diag µt pt −∇R(t, Ko
t ) −ht)dt + htd ˜Wt,
pT = ∇Q(Ko
T ),
(4.5)

A Consumption–Investment Problem with Production Possibilities
325
where hi
t = 
j hij
t σij
t and the following relation holds:
H(t, Ko
t , Io
t , pt, ht) = max
I∈Γ H(t, Ko
t , I, pt, ht)
d ˜Pdt-a.e.
(4.6)
For brevity we shall call any quadruplet of processes Io, Ko, p, and h sat-
isfying the above relations and the integrability assumption a Bismut quadru-
plet.
Knowing that the processes p and h satisfying (4.5) exist, there is almost
nothing to prove. Indeed, let I be an arbitrary Γ-valued predictable process.
Using (4.3) and (4.5) we get by the Ito formula that
d(ptKt) = (ptdiag µt Kt −∇R(t, Ko
t )Kt −tr h(diag K σt)∗)dt
+pt(It −diag Ktµt)dt + tr h(diag K σt)∗dt + dNt
= (ptIt −∇R(t, Ko
t )Kt)dt + dNt
where N is a square integrable martingale with respect to ˜P.
Writing this in the integral form and observing that the expectation of
stochastic integral vanishes we arrive to the formula
˜E
 T
0
ptItdt = ˜E∇Q(Ko
T )KT −p0k + ˜E
 T
0
∇R(t, Ko
t )Ktdt.
This formula holds, in particular, for Io and Ko. Taking the difference of the
identities for the optimal and an arbitrary and using the concavity of R and
Q, we obtain easily that
˜E
 T
0
pt(Io
t −It)dt ≤˜E
 T
0
(R(t, Ko
t ) −R(t, Kt))dt + ˜E(Q(Ko
T ) −Q(KT )).
(4.7)
But the maximum principle (4.6) implies
 T
0
1(Io
t −It)dt ≤
 T
0
pt(Io
t −It)dt
˜P-a.s.
(4.8)
and we deduce from these two inequalities that H(Io) ≤H(I).
Due to the simplicity of our problem we can see easily that the stochastic
maximum principle is the necessary condition: the optimal pair is the compo-
nent of a Bismut quadruplet. Indeed, starting from the optimal pair (Io, Ko)
we can define p and h satisfying (4.5). The optimality of (Io, Ko) implies
that in (4.7) and (4.8) we have equalities. But the fulfillment of (4.8) for any
I = (It) is equivalent to (4.6).
Summarizing, we have the following.
Proposition 2. A pair (Io, Ko) satisfying (4.3) is an optimal solution of the
problem (3.3), (4.2) if and only if it can be complimented to a Bismut quadru-
plet.

326
Yu. Kabanov and M. Kijima
In the case where σ = 0 and, therefore, h appears only in the diffusion
term, the linear backward equation is especially simple and can be “solved”
easily. Indeed, the m-dimensional random variable
ξ :=
 T
0
e−λ
s ∇R(s, Ko
s)ds + e−λ
T ∇Q(Ko
T )
with
eλ
t := diag

e
 t
0 λ1
sds, ..., e
 t
0 λm
s ds

is a square integrable functional of the Wiener process. By the martingale
representation theorem
˜E(ξ|Ft) = ˜Eξ +
 t
0
ϕsd ˜
Ms
for some matrix-valued process ϕ ∈L2(Ω× [0, T], P, d ˜Pdt) of an appropriate
dimension. It is easy to see that ht := eλ
t ϕt and
pt := eλ
t ˜Eξ −eλ
t
 t
0
e−λ
s ∇R(s, Ko
s)ds + eλ
t
 t
0
ϕsd ˜
Ms
is the solution of the backward stochastic equation (4.5).
In the case d = 1 we can get an “explicit” solution of the BSDE for arbi-
trary σ by making at first the equivalent change of the probability measure,
removing the term h from the drift (under this measure the process with
d ˜W ′
t := d ˜Wt + σtdt Wiener). In general case we use just a reference to an
existence theorem for the solution of a linear BSDE. An appropriate result
can be found, e.g., in [6].
However, though attractive, the stochastic maximum principle is not very
helpful in getting the optimal solution. In the case when σ = 0 and the
coefficients are deterministic, it is “degenerated” to the ordinary Pontryagin
maximum principle (of a deterministic problem). The latter is a powerful tool
of the optimal control theory which allows to analyze the structure of the
optimal control. We do this by considering examples.
5 Special Cases
5.1 Deterministic Dynamics: Examples.
The separation result has an important consequence for the case of the model
where the values of the production assets may only depreciate (i.e. σ = 0) and
the parameters λi are deterministic. The problem becomes deterministic:
H(K) :=
 T
0
(1It −R(t, Kt))dt −Q(KT ) →min,
(5.1)

A Consumption–Investment Problem with Production Possibilities
327
˙Ki
t = Ii
t −λi
tKi
t,
Ki
0 = ki,
(5.2)
where I = (It) is a Borel function taking values in Γ ⊂Rm
+.
The necessary and sufficient condition of optimality is the classical Pon-
triagin maximum principle. More specifically, a pair (Io, Ko) is optimal for
the problem (5.1), (5.2) if and only if it is a part of the “Pontryagin triplet”
(Io, Ko, p) satisfying the following relations:
˙Ko
t = Io
t −diag λtKo
t ,
Ko
0 = k,
(5.3)
˙pt = ptdiag λt −∇R(t, Ko
t ),
pT = ∇Q(Ko
T ),
(5.4)
(pt −1)Io
t = max
I∈Γ (pt −1)It
a.e.
(5.5)
Due to the number of parameters involved, the complete analysis of this sys-
tem seems to be rather complicated. We restrict ourselves to the scalar prob-
lem with constant coefficients and Γ = [0, a] and provide several examples
where the solution can be obtained explicitly. For m = 1 we have:
˙Ko
t = Io
t −λKo
t ,
Ko
0 = k,
(5.6)
˙pt = λpt −R′(Ko
t ),
pT = Q′(Ko
T ),
(5.7)
(pt −1)Io
t = max
I∈Γ (pt −1)It
a.e.
(5.8)
Case study: scalar homogeneous model with Q = const (such a situation
may arise in practice) and R(K) = (κ/γ)Kγ, κ > 0, γ ∈]0, 1[.
Due to the continuity, near the right extremity T of the time interval the
dual variable p is close to the value pT = 0; more precisely, it decreases to zero
because the equation (5.7) implies that the derivative ˙pT = −κ(Ko
T )γ−1 < 0.
Now put T1 := sup{t ≥0 :
pt ≥1} (with the convention that T1 = 0 if
the set is empty). The maximum relation ensures that Io
t = 0 on ]T1, T]. If
T1 = 0, the phase trajectory is the decreasing exponential Ko
t = ke−λt while
the trajectory of the dual variable is
pt = eλt
 T
t
e−λsR′(Ko
s)ds = kγ−1 κ
λγ eλt(e−λγt −e−λγT ).
To be compatible with the maximum principle the right-hand side should be
less or equal to unity on the whole interval [0, T] and this requirement is met
when the initial endowment k ≥kc where the threshold is given by
kc = sup
t≤T
 κ
λγ eλt(e−λγt −e−λγT )

1
1−γ
.
Thus, for large k the control Io
t = 0. We shall have, for large initial endow-
ments in production assets, the similar structure of the optimal control also
for the model where Q′(K) →0 as K →∞.

328
Yu. Kabanov and M. Kijima
Qualitatively, this result means that in the case of small marginal liquida-
tion value the investor having high level of initial manufacturing facilities is
not motivated in their further development.
The situation seems to be rather different for k < kc. Then necessarily Io
is not equal to zero on a certain non-null subset of [0, T1]. Let us show that
for some range of parameters, Io
t = aI[0,T1].
So, suppose that on [0, T1] the control Io
t = a and, therefore, on this
interval the state dynamics is given by the formula
Ko
t = ke−λt + a
λ(1 −e−λt) = a
λ +

k −a
λ

e−λt.
(5.9)
First, we consider the simplest particular case where k = a/λ. Then Ko
t =
k on [0, T1[ (the maximal level of investments keeps the production capacity
constant) and, according to (5.7), ˙pT1 = λ −κkγ−1. For t ∈[T1, T] we have
the formula Ko
t = keλT1e−λt and, hence, on this interval
pt = kγ−1eλ(γ−1)T1 κ
λγ eλt(e−λγt −e−λγT ).
Note that the point T1 ∈]0, T[ can be defined from the equation pT1 = 1 which
solution does exist for k < kc. On the interval [0, T1] the function p solving
the differential equation
˙pt = λpt −κkγ−1,
pT1 = 1,
and hence given by the formula
pt = κ
λkγ−1 +

1 −κ
λkγ−1
e−λ(T1−t)
should be larger or equal to unity. If also k < (κ/λ)
1
1−γ , the value of deriv-
ative ˙pT1 < 0. Taking into account that the trajectory cannot cross the unit
level upwards with negative value of derivative (always equal to λ −κkγ−1),
we conclude that the control aI[0,T1] is optimal for such values of the initial
endowment k.
If k > a/λ, the trajectory supposed to be optimal decreases on [0, T1] from
its initial value k. For k < (λ/κ)
1
1−γ , we have ˙pT1 < 0, i.e. the dual variable
cross the unit level at T1 and cannot do this before.
If k < a/λ, the candidate for the optimal trajectory on [0, T1] increases
from k to a certain value which is less than a/λ. At least, in the case of the
small ratio a/λ (i.e., when λ < κ(a/λ)γ−1), we can conclude again that pt > 1
on [0, T1[ and, therefore, Io
t = aI[0,T1] is the optimal control.
In short, for initial endowments k less than a certain critical value kc (in
some case, with appropriate restrictions on other parameters), the optimal
strategy is of the bang-bang form and requires at the beginning of the planning
interval intensive investments in the production assets.
However, in the range ]kc, kc[ the structure of the optimal control may be
more involved and even not of the bang-bang type.

A Consumption–Investment Problem with Production Possibilities
329
5.2 Deterministic Dynamics: Turnpike Behavior
To investigate the general structure of the optimal control in the problem (5.1),
(5.2), we exclude the control variable from the functional using the expressions
Ii
t = ˙Ki
t + λi
t given by (5.2). After simple transformations we arrive to the
problem with the functional depending only of the phase variable:
 T
0
Φ(t, Kt)dt + S(KT ) →min,
(5.10)
˙Ki
t = Ii
t −λi
tKi
t,
Ki
0 = ki,
(5.11)
where the functions Φ(t, K) := λtK −R(t, K) and S(K) := 1K −Q(K) −1k
are convex in K.
It is well-known that, under minor assumptions, the optimal trajectory in
models of such type exhibits, on a large time interval, a turnpike behavior: it
coincides, except initial and final periods, with the function K where Kt is the
minimizer of the function Φ(t, .), i.e. the root of the equation ∇Φ(t, K) = 0.
To be specific, we consider again the one-dimensional time-homogeneous
model assuming also that k < a/λ, Φ′(a/λ) > 0, Φ′(0) = −∞. Then any
trajectory K evolves in the interval [0, a/λ]; it increases if I = a and decreases
if I = 0.
Now the dual variable ψ = p −1 solves the equation
˙ψt = λψt + Φ′(Ko
t ),
ψT = −S′(Ko
T ).
(5.12)
and the maximum principle says that Io
t = 0 if ψt < 0, and Io
t = a if ψt > 0.
It is convenient to introduce an auxiliary function qt := e−λtψt having the
same sign as ψt; its derivative ˙qt = e−λtΦ′(Ko
t ).
Let t1 := inf{t : qt = 0}, t2 := sup{t : qt = 0}. Notice that if [t1, t2] is
not a singleton, then on this interval q = 0. Indeed, suppose that there is a
subinterval ]t′, t′′[ where q < 0 but qt′ = qt′′ = 0. Since on this subinterval
the control Io = 0, the trajectory Ko is decreasing, the trajectory Φ′(Ko)
is also decreasing and so is −˙q. This is impossible and, therefore, q cannot
deviate from zero downwards. Similarly, if q > 0 on ]t′, t′′[ and q vanishes at
the extremities, then on this interval Io = a, the trajectory Ko increases as
well as Φ′(Ko). Thus,
˙ψt′ = Φ′(Ko
t′) < Φ′(Ko
t′′) = ˙ψt′′
in contradiction with the inequalities ˙ψt′ ≥0, ˙ψt′′ ≤0.
The equation (5.12) necessitates that Φ′(Ko) = 0 on [t1, t2], i.e. Ko = K
where K is the minimizer of Φ; the optimal control is Io = Kλ. The left
extremity coincides with zero if and only if k = K. If t1 > 0, there are two
possible cases: 1) on [0, t1[ the dual variable ψ is strictly negative, Io = 0
and the trajectory Ko decreases from k to the value K; 2) on [0, t1[ the dual
variable ψ is strictly positive, Io = a and the trajectory Ko increases from

330
Yu. Kabanov and M. Kijima
k to the value K. In both cases the interval [0, t1] does not depend on the
terminal part of the functional and t1 < T for sufficiently large T.
The case t2 = T is exceptional. This means that 0 = ψT = −S′( K), i.e., K
minimizes also the function S. Otherwise, the interval [t2, T] is not a singleton.
The optimal control on this interval depends on the sign of S′( K). Suppose,
e.g., that S′( K) > 0. Let Io = 0. Then ψ is strictly negative, the trajectory Ko
decreases from the value K, Φ′(Ko) < 0 and, therefore, ˙ψ = λψ +Φ′(Ko) < 0,
i.e., the trajectory ψ decreases from zero. Since −S′ is a decreasing function,
the transversality condition ψT = −S′(Ko
T ) will be met for a certain (uniquely
defined) value of t2 (of course, the time horizon should be large enough).
The above arguments show that, for a long time interval, the optimal in-
vestments in the manufacturing consist in keeping the production on a specific
“turnpike” level which depends only of the technology used and not of the
initial capital and the liquidation value. This level should be attained in the
fastest way at the beginning of the planning period. At the end of the period,
the investment policy is to leave the turnpike quickly to profit from the selling
of the manufacturing arm.
5.3 Remark on the HJB equation
The case where the fluctuations of the price of production assets are assumed
(i.e. σ is not zero) can be studied by methods of dynamic programming.
The problem of interest can be imbedded in the family of stochastic control
problems parameterized by initial date t and the initial endowment x (we
prefer x to k here for notational convenience). The HJB equation is as follows:
Vt +
inf
I∈[0,a]
1
2σ2x2Vxx + (I −µx)Vx + (I −R(x))

= 0
with the terminal condition V (T, x) = −Q(x). The number Ho we are inter-
ested in is V (0, k). The above equation can be rewritten in the form
Vt + 1
2σ2x2Vxx −µxVx + aI{Vx<−1} −R(x) = 0.
One can prove that the Bellman function V of the problem is a viscosity
solutions of this equation which is unique in an appropriate class but a detailed
discussion is beyond the scope of the present paper.
5.4 Piecewise-linear utility function
As we just see, in some cases the production problem may admit an explicit
solution otherwise the value Ho can be find numerically. An attractive feature
of the considered setting is that the investing problem is well-studied and also
admits cases with explicit solutions. The most famous one is the problem with
U(c) = ρ/cρ found by Merton.

A Consumption–Investment Problem with Production Possibilities
331
We discuss here an example where the utility function is linear up to a
saturation point, i.e.
U(c) = cI{c≤C} + CI{c>C}.
Thus, the optimal control problem is read now:
J(c) := E
 T
0
e−βtU(ct)dt →max
over all non-negative predictable processes c such that
E
 T
0
Ztctdt ≤x −H(Io).
Clearly, in our search for the optimum we can consider the subset of controls
for which the constraint is satisfied with an equality.
The solution can be found easily using the Lagrange multiplier method
removing the above constraint. Arguing formally, we write the unconstrained
problem
E
 T
0
[e−βtU(ct) −θZtct]dt →max
where the multiplier θ ≥0. Its solution is any non-negative predictable process
c = (ct) maximizing pointwise the integrand. Of course, the solution depends
of the unknown Lagrange multiplier θ. Let
c∗
t (θ) := CI{θZt>e−βt}.
Define on R+ the function
f(θ) := E
 T
0
Ztc∗
t (θ)dt = C
 T
0
˜P(eβtZt < 1/θ)dt
which is continuous and decreasing from f(0) = CT to f(∞) = 0.
Let us show that the optimal consumption process is co := c∗(θ∗) where θ∗
is defined as the solution of the equation f(θ∗) = x −H(Io) and this solution
we assume existing (otherwise the problem is trivial with the optimal solution
co
t = C). Indeed, let c = (ct) be an arbitrary consumption process satisfying
the constraint with the equality. Then
J(co) −J(c) = E
 T
0
[e−βtU(co) −θ∗Ztco
t −e−βtU(ct) + θ∗Ztct]dt
and we get the result because the right-hand side is non-negative due to
the choice of co as the maximizer of the unconstrained problem with the
multiplier θ∗.
Acknowledgment
The authors are grateful to Andrei Dmitruk to whom they are indebted for
the arguments on the turnpike behavior used in Subsection 4.2. His expertise

332
Yu. Kabanov and M. Kijima
in the Pontriagin maximum principle is greatly appreciated. We expressed
also our thanks to the anonymous referee for helpful remarks.
References
1. Aubin, J.-B.: Optima and Equilibria. An Introduction to Nonlinear Analysis.
Berlin Heidelberg New York: Springer 1993
2. Bismut J.-M. Conjugate convex functions in optimal stochastic control. J. Math.
Anal. Appl. 44, 384–404 (1973)
3. Bismut J.-M. An introductory approach to duality in optimal stochastic control.
SIAM Review 20, 1, 62–78 (1978)
4. Cox J.C., Huang C.: Optimal consumption and portfolio policies when asset
prices follow a diffusion process. J. Econ. Theory 49, 33–83 (1989)
5. Cuoco D.: Optimal consumption and equilibrium prices with portfolio contraints
and stochastic income. J. Econ. Theory 72, 33–73 (1997)
6. El Karoui N., Peng S., Quenez M.-C.: Backward stochastic differential equation
in finance. Math. Finance, 7, 1, 1–71 (1997)
7. Harrison M., Pliska S.: Martingales and stochastic integrals in the theory of
continuous trading. Stochastic Processes and their Applications 11, 215–260
(1981)
8. Hirayama T., Kijima M.: A generalized consumption/investment decision prob-
lem with production possibilities. Working paper (1991)
9. Karatzas I.: Optimization problems in the theory of continuous trading. SIAM
J. Control and Optimization 27, 1221–1259 (1989)
10. Karatzas I., Lehoczky J.P, Shreve S.E.: Optimal portfolio and consumption
decisions for a “small investor” on a finite horizon. trading. SIAM J. Control
and Optimization 25, 1557–1586 (1987)
11. Karatzas I., Lehoczky J.P, Sethi S.P., Shreve S.E.: Explicit solution of a gen-
eral consumption/investment problem. trading. Math. Oper. Res. 11, 261–294
(1986)
12. Karatzas I., Shreve S.E.: Brownian Motion and Stochastic Calculus. Berlin Hei-
delberg New York: Springer 1988
13. Karatzas I., Shreve S.E.: Methods of Mathematical Finance. Berlin Heidelberg
New York: Springer 1998
14. Kort P.M.: The influence of a stochastic environement on the firm’s optimal
dynamic investment policy. Optimal Control Theory and Economic Analysis 3,
247–257. Ed.: G. Feichtinger. Amsterdam: North-Holland 1971
15. Merton R.C.: Lifetime portfolio selection under uncertainty: the continuous-time
case. Rev. Econ. Stat. 51, 247–257 (1969)
16. Merton R.C.: Optimum consumption and portfolio rules in a continuous-time
model. J. Econ. Theory 3, 373–413 (1971)
17. Pliska S.: A stochastic calculus model of continuous trading: optimal portfolio.
Math. Oper. Res. 11, 371–382 (1986)
18. Rockafellar R.T.: Convex Analysis. Princeton: Princeton University Press 1970
19. Zame W.R.: Competetive equilibria in production economies with an infinite
dimensional space. Econometrica 55, 1075–1108 (1987)
20. Yong J., Zhou X.Y. Stochastic Control. Hamiltonian Systems and HJB Equa-
tions. Berlin Heidelberg New York: Springer 1999

Multiparameter Generalizations of the
Dalang–Morton–Willinger Theorem
Yuri KABANOV1, Yuliya MISHURA2, and Ludmila SAKHNO2
1 Universit´e de Franche-Comt´e, 16 Route de Gray, F-25030 Besan¸con Cedex,
France, and Central Economics and Mathematics Institute, Moscow, Russia
e-mail: kabanov@math.univ-fcomte.fr
2 Department of Mechanics and Mathematics, Kyiv Taras Shevchenko National
University, Kyiv, 01033, Ukraine
e-mails: myus@univ.kiev.ua, lms@univ.kiev.ua
Summary. We investigate possible generalizations of Dalang–Morton–Willinger
theorem in the context of Cairoli– Walsh theory of random fields on the discrete
rectangle.
Key words: No-arbitrage criteria, Dalang–Morton–Willinger theorem, random
fields, Cairoli–Walsh model.
Mathematics Subject Classification (2000): 60G44
1 Introduction.
The classical Dalang–Morton–Willinger theorem [2] says that in the standard
discrete time finite-horizon model of a frictionless financial market there are
no arbitrage opportunities if and only if there exists an equivalent martingale
measure with bounded density. In the probabilistic language this theorem can
be formulated as follows.
We are given an Rd+1-valued adapted process
¯S = (S0
t , St) = (S0
t , S1
t , ..., Sd
t )
where t = 0, 1, ..., T.
With any Rd+1-valued adapted process ¯ϕ = (ϕ0
t, ϕt) with ¯ϕ0 = 0 we
associate the scalar process Vt = ¯ϕt ¯St = ϕ0
tS0
t + ϕtSt. In financial modelling
¯S is the price process, ¯ϕ is the strategy, representing holdings in various assets
(in nominal units), and V is the corresponding value process of the portfolio.
For a specified class K of strategies we define the set of random variables
RK
T := { ¯ϕT ¯ST :
¯ϕ ∈K}. We shall say that the NA(K)-property holds if
RK
T ∩L0
+ = {0}.

334
Yu. Kabanov et al.
In the standard model S0
t = 1 identically, i.e. the corresponding asset (usu-
ally called bank account) is the num´eraire, and K is the class of self-financing
strategies described as follows: the process ¯ϕ is predictable (in symbols: ¯ϕ ∈P)
and
∆ϕ0
t + St−1∆ϕt = 0,
t = 1, ..., T,
(1)
with the usual definition ∆Xt = Xt−Xt−1. The above relation can be written
also as ¯St−1∆¯ϕt = 0. Thus, by the product formula, for the strategies from
this class we have
∆( ¯St ¯ϕt) = ¯St−1∆¯ϕt + ¯ϕt∆¯St = ϕt∆St
and, therefore, RK
T = RT := {ϕ·ST : ϕ ∈P}, i.e. the set of the resulting ran-
dom variables is just the set of discrete time integrals ϕ · ST := T
t=1 ϕt∆St
where ϕ is an arbitrary d-dimensional predictable process without any con-
straints. With this AT := RT −L0
+ is the set of hedgeable claims. We consider
also the subset RT (t) of RT corresponding to strategies which are zero except
the date t, that is RT (t) = {ϕt∆St : ϕt ∈Ft−1}. The notation AT (t) is clear.
The condition RT ∩L0
+ = 0 (obviously equivalent to AT ∩L0
+ = 0) is
referred to as the NA-property.
The introduced concepts serve to model the situation when an agent revise
the portfolio between the trading days t −1 and t using the information
available (ϕt is Ft−1-measurable) without retracting or adding funds (the
relation (1) is a “fund conservation law”); in this case, RK
T is the set of all
possible “results” achieved from zero initial endowment and absence of non-
risky profits corresponds to the absence of arbitrage opportunities on the
market.
The extended formulation of the Dalang–Morton–Willinger theorem is a
long list of equivalent conditions but we retain only four here:
(a) AT ∩L0
+ = {0} (NA);
(b) AT ∩L0
+ = {0} and AT = ¯AT (closure in probability);
(c) AT (t) ∩L0
+ = {0} for all t ≤T (NA for all one-step models);
(d) there is a probability measure ˜P ∼P with d ˜P/dP ∈L∞such that S
is a ˜P-martingale.
The DMW theorem is widely recognized as one of the most important
results in the arbitrage pricing theory and we have no need to discuss its
various aspects. It is a (deep!) generalization of the pioneering Harrison–Pliska
theorem which has exactly the same formulation but under hypothesis that
Ωis finite. Of course, in the latter case the property (b) coincides with (a)
(AT is polyhedral cone) and (d) sounds simpler as all random variables are
bounded.
These result are the starting points of intensive mathematical studies and
their numerous generalizations and ramifications are known, see, e.g. the sur-
vey [6] with further references therein and more recent papers [3], [4], [5], [7],

Multiparameter Generalizations of the DMW Theorem
335
[9], [10]. In the present note we make an attempt to explore relationships be-
tween possible versions of the above conditions in the setting of random fields.
To our knowledge, the syntheses of both theories is not done yet.
A specific feature of random fields is that there are several rather natural
definitions of the “past” and consequently, several definitions of the martingale
property. We shall investigate analogs of NA criteria in the standard frame-
work of Cairoli–Walsh, using an appropriate techniques which sometimes is
quite different from that of one-parameter processes.
First, recall the basic definitions.
Let (Ω, F, (Ft)t∈T, P) be a stochastic basis where T stands for the rectan-
gle [0, T] := {0, 1, ..., T1} × {0, 1, ..., T2} of the integer lattice Z2; the notation
]0, T] := {1, ..., T1} × {1, ..., T2} also will be used. We shall suppose that the
σ-algebras of the axes are trivial: Fi0 = F0k = {∅, Ω}.
Put i := (1, 0), j := (0, 1), and 1 := i + j = (1, 1).
Let X = (Xt)t∈T be a random field. We shall use the following notations:
∆1Xt := Xt−Xt−i,
∆2Xt := Xt−Xt−j,
∆Xt = Xt−Xt−i−Xt−j+Xt−1.
Also X−i := (Xt−i) and, in the same spirit, X−j, X−1.
Clearly, knowing the field X on the axes as well as the elementary ”areas”
∆Xt, one can recover X on the whole rectangle T.
Define the σ-algebras Ft := Ft+i ∨Ft+j and also ˜F1
t := Ft1,T2 ∨Ft+i,
˜F2
t := Ft+j ∨FT1,t2 (the parentheses in subscripts are omitted).
Definition 1. An integrable adapted field X constant on the coordinate axes
is called:
1) strong martingale if E(∆Xt| Ft−1) = 0;
2) weak martingale if E(∆Xt|Ft−1) = 0;
31) 1-martingale if E(∆Xt|Ft−i) = 0;
32) 2-martingale if E(∆Xt|Ft−j) = 0.
Definition 2. The filtration (Ft) satisfies the Cairoli–Walsh condition (F4
of [1]) if for any F-measurable integrable random variable Z and for any
t = (t1, t2) ∈T
E(E(Z|Ft1,T2)|FT1,t2) = E(E(Z|FT1,t2)|Ft1,T2) = E(Z|Ft1,t2).
Definition 3. We say that a random field H is:
1) weakly predictable if Ht+1 ∈Ft, t + 1 ∈T;
2) predictable if Ht+1 ∈Ft, t + 1 ∈T.
Let X and Y be two random fields constant on the coordinate axes. We
define two lattice integrals as
X · Yt :=

s∈]0,t]
Xs∆Ys,
X ∗Yt :=

s∈]0,t]
[∆2Xs−i∆1Ys + ∆1Xs−j∆2Ys]

336
Yu. Kabanov et al.
with the convention that they are equal to zero when t belongs to the axes.
It is easy to see that ∆(X · Y )t = Xt∆Yt and the following product formula
holds:
XtYt = X−1 · Yt + X ∗Yt + Y · Xt.
(2)
We fix an Rd-valued adapted random field S which components on the
coordinate axes are equal to the unit and put ¯S := (1, S), i.e. we add to
S one more component identically equal to the unit everywhere. With any
Rd+1-valued adapted random field ¯ϕ = (ϕ0, ϕ) we associate a scalar field
Vt = ¯ϕt ¯St = ϕ0
t + ϕtSt.
By analogy with the one-parameter case we shall call strategy the field ¯ϕ
vanishing on the axes and V its value field.
For a class K of strategies define the set of random variables
RK
T := { ¯ϕT ¯ST : ¯ϕ ∈K}.
We say that the NA(K)-property holds if RK
T ∩L0
+ = {0}, or, equivalently,
AK
T ∩L0
+ = {0} with AK
T = RK
T −L0
+.
2 Strong martingale, weakly predictable strategies
We say that a weakly predictable strategy ¯ϕ satisfies the strong SF-property
if
¯St−1∆¯ϕt + ∆2 ¯St−i∆1 ¯ϕt + ∆1 ¯St−j∆2 ¯ϕt = 0
∀t.
(1)
This relation plays the role of (1): in this case from the product formula (2)
we have that Vt = ϕ · St for all t ∈T.
In this section we fix as K the class of weakly predictable strategies satis-
fying the strong SF-property abbreviated as SSF.
It is easily seen that if ϕ is a weakly predictable d-dimensional field, then
it is the component of a certain strategy ¯ϕ = (ϕ0, ϕ) from SSF. Indeed,
suppose that ¯ϕ is already known outside of the rectangle [t, T]. We use the
self-financing condition (1) to define ϕ0
t ∈Ft−1 and get that
ϕ0
t = ϕ0
t−i + ϕ0
t−j −ϕ0
t−1 −St−1∆ϕt −∆2St−i∆1ϕt −∆1St−j∆2ϕt.
Let us consider the point t + i. Since ¯ϕ is already defined at the “preceding”
points t, t+i−j, t+i−1 and ϕt+i is known, the relation (1) corresponding to
the point t + i serves as an equation to define the remaining component ϕ0
t+i.
These arguments can be repeated also for t+2i, t+3i, and so on, allowing us
to define the SSF-strategy ¯ϕ outside of the rectangle [t + j, T]. By symmetry,
we have the same recurrent structure along the y-axis. As a result, we obtain
the weakly predictable strategy ¯ϕ satisfying the strong SF-property on the
whole rectangle [0, T].
Since the d-dimensional weakly predictable field ϕ can be chosen arbitrar-
ily, we have the following

Multiparameter Generalizations of the DMW Theorem
337
Proposition 1. Assume that the NA(SSF)-property holds. Let α ∈Ft−1
and α∆St ≥0. Then α∆St = 0.
Remark 1. Note that this does not require any additional assumption on
the filtration and the probability space. In particularly, we do not use the
Cairoli–Walsh condition.
The next result is an analog of the Harrison–Pliska theorem and its proof
is exactly the same as the latter.
Proposition 2. Let Ωbe finite. Then the following conditions are equivalent:
(a) the NA(SSF)-property holds;
(b) there exists a probability measure ˜P ∼P such that S is a strong mar-
tingale with respect to ˜P.
Proposition 1 asserts that the NA(SSF)-property implies the NA(SSF)-
property for the increments (i.e., for all “one-step models”). Surprisingly, the
inverse implication fails to be true. We present an example where the NA
property does not hold though there is no-arbitrage for the increments, i.e.
the situation is similar to the observed already in models with restricted in-
formation, [8].
Example. It is very simple: the field S is one-dimensional, T1 = T2 = 2, and
the probability space consists only of five points. The filtration is natural. The
values of the field are given by the following table:
S11
S12
S21
S22
ω1
5/ 6
1/ 2
5/ 3
4/3
ω2
5/ 6
2/ 3
7/ 6
1
ω3
5/ 6
4/ 3
1/ 2
1
ω4
7/ 6
1
7/ 6
1
ω5
7/ 6
4/ 3
7/ 6
4/ 3
Recall that S equals 1 on the axes. Note that the values of S2
22 are chosen
to get the identity ∆S2
22 = 0, that is S2
22 = S2
12 + S2
21 −S2
11.
Let us show that the constant strategy ¯ϕ = (−1, 1) (obviously, weakly
predictable and strongly SF) is an arbitrage opportunity in our sense.
We have V22 = ¯ϕ22 ¯S22 = ϕ22S22 −1 and, hence,
V22(ω1) = V22(ω5) = 1
3,
V22(ω2) = V22(ω3) = V22(ω4) = 0.
It remains to verify that for each point t = (1, 2), t = (2, 1), and t = (2, 2)
the relation α∆St ≥0 with α ∈Ft−1 may hold only if α∆St = 0.
Note that F00 = F00,
F10 = F11,
F01 = F11,
△S11 = S11 −S00, △S21 = S21 −S11, △S12 = S12 −S11.
We want to prove that for α ∈F00, β ∈F11, γ ∈F11 the inequalities

338
Yu. Kabanov et al.
α(S11 −S00) ≥0,
β(S21 −S11) ≥0,
γ(S12 −S11) ≥0,
may hold only as the equalities
α(S11 −S00) = 0,
β(S21 −S11) = 0,
γ(S12 −S11) = 0.
But this is obvious: on each atom the increments take values of different
signs.
The next proposition is a technical one. It deals with the case of SSF-
strategies measurable with respect to a wider σ-algebra.
Proposition 3. Let K be the class of d-dimensional fields ϕ = (ϕt) such that
ϕt ∈˜F1
t−1. Then the following conditions are equivalent:
(i) AK
T ∩L0
+ = {0};
(ii) AK
T ∩L0
+ = {0}, AK
T = ¯AK
T;
(iii) The relation α∆St ≥0 for t ∈T and α ∈˜F1
t−1 holds only if α∆St = 0;
(iv) There exists a probability measure ˜P ∼P with d ˜P/dP ∈L∞such that
∆St ∈L1( ˜P) and ˜E(∆St| ˜F1
t−1) = 0 for all t ∈T (i.e. S is a strong
martingale with respect to the filtration ( ˜F1
t ) and ˜P).
This result is easily reduced to the DMW-theorem. To see this we define
the bijection L of ]0, T] onto the set {1, 2, ..., T1T2} by the formula
L : t →(t1 −1)T2 + t2.
The one-parametric process Wn := 
k≤n ξk where ξk = ∆SL−1k is adapted
with respect to the filtration formed by the σ-algebras Fn := ˜F1
L−1n. The
conditions of the above proposition are those of the DMW-theorem for W.
3 Weak martingales, predictable strategies
We say that a predictable strategy ¯ϕ satisfies the weak SF-property if
¯St−1∆¯ϕt = 0
∀t.
(1)
In this case the value field is given by the formula
Vt = ¯ϕ · ¯St + ¯ϕ ∗¯St.
For the no-arbitrage property in this case we shall use the notation NA(WSF).
The latter implies the no-arbitrage property for he increments. Namely, we
have
Proposition 1. Assume that the NA(WSF)-property holds. Let α ∈Ft−1 be
such that α∆St ≥0. Then α∆St = 0.

Multiparameter Generalizations of the DMW Theorem
339
Proof. Suppose that the claim fails and there is α ∈Ft−1 such that the
probability P(α∆St > 0) is strictly positive. We come to a contradiction by
constructing a predictable strategy ¯ϕ satisfying (1) and such that the end
value VT = ¯ϕT ¯ST = α∆St. The ϕ-component of ¯ϕ will be zero except the
point t where it coincides with −α. To this aim, we put ¯ϕ equal to zero outside
of [t, T]. We use the self-financing condition (1) to define ϕ0
t and get that
ϕ0
t = αSt−1 ∈Ft−1.
Let us consider the point t + i. Since that ¯ϕ is already defined at the points
t , t + i −j , t + i −1 and we have ϕt+i = 0, the relation (1) corresponding
to the point t + i takes the form:
ϕ0
t+i −ϕ0
t + St−j∆ϕt+i = 0
which suggests us to define
ϕ0
t+i = −α(St−j −St−1) = −α∆1St−j ∈Ft−j.
Similar observations for the point t + j lead us to define
ϕ0
t+j = −α(St−i −St−1) = −α∆2St−i ∈Ft−i.
Next we consider the condition (1) at the point t + 1. We get
∆ϕ0
t+1 + St∆ϕt+1 = 0,
or
ϕ0
t+1 −ϕ0
t+j −ϕ0
t+1 + ϕ0
t + Stϕt = 0,
With the already defined values of the strategy ϕ, we come to the following
expression for ϕ0
t+1:
ϕ0
t+1 = α∆St ∈Ft.
Now with such a strategy ϕ we get at the point t + 1 the following expression
for the value field
Vt+1 = ¯ϕt+1 ¯St+1 = α∆St.
It is left to finalize our construction by setting
ϕ0
t+mi = ϕ0
t+i,
m = 2, . . . , T1 −t1,
ϕ0
t+mj = ϕ0
t+j,
m = 2, . . . , T2 −t2,
and
ϕ0
t+mi+lj = ϕ0
t+1,
m = 2, . . . , T1 −t1,
l = 2, . . . , T2 −t2.
In such a way we obtain a predictable strategy satisfying WSF-property such
that VT = ¯ϕT ¯ST = α∆St. Since α∆St ̸= 0 we obtain an arbitrage opportu-
nity, that is the contradiction.
⊓⊔
Remark 2. The same example as in the previous section demonstrates that
the inverse implication is not true.
Introduce the notations: t1
T := (T1, t2), t2
T := (t1, T2), and Z := d ˜P/dP.

340
Yu. Kabanov et al.
Proposition 2. (a) Suppose that there is a measure ˜P ∼P with Z ∈L∞such
that S is a weak ˜P-martingale and the Cairoli–Walsh commutation condition
is fulfilled for ˜P. Then the inequality

t∈[0,T−1]
αtE(∆St+1ξt|Ft+i) ≥0
with αt ∈Ft2
T and ξt = Z/E(Z|Ft+i) may hold only as the equality.
(b) Suppose that the inequality

t∈[0,T−1]
αtE(∆St+1|Ft+i) ≥0
with αt ∈Ft2
T may hold only as the equality. Then there is ˜P ∼P with Z ∈
L∞such that ˜E(E(∆St+1|Ft+i)|Ft2
T ) = 0 for all t ∈[0, T −1]. If, in addition,
the Cairoli–Walsh condition is fulfilled for ˜P, then ˜E(∆St+1 ˆξt|Ft) = 0, where
ˆξt = Z−1/E(Z−1|Ft+i).
Proof. (a) We have that ˜E(∆St+1|Ft) = 0. Thus, for any αt ∈Ft2
T we get,
taking into account the Cairoli–Walsh, that
˜E



t∈[0,T−1]
αt ˜E(∆St+1|Ft+i)
Ft2
T

= 0.
The proof follows now immediately from DMW theorem and the identity
˜E(∆St+1|Ft+i) = E(∆St+1ξt|Ft+i).
(b) We have, in particular, that the inequality

t∈[0,T−1]
αtE(∆St+1|Ft+i) ≥0
with αt ∈Ft2
T may hold only as the equality. In this case DMW theorem
guarantees that there exists ˜P ∼P with Z ∈L∞such that

t∈[0,T−1]
αt ˜E(E(∆St+1|Ft+i)|Ft2
T ) = 0.
The last step is obvious.
⊓⊔
References
1. Cairoli R., Walsh J. B.: Stochastic integrals in the plane. Acta Math., 134,
111–183 (1975)

Multiparameter Generalizations of the DMW Theorem
341
2. Dalang R. C., Morton A., Willinger W.: Equivalent martingale measures and
no-arbitrage in stochastic securities market model. Stochastics and Stochastics
Reports, 29, 185–201 (1990)
3. Delbaen F., Schachermayer W.: A general version of the fundamental theorem
of asset pricing. Math. Ann., 312, 215–250 (1998)
4. Jacod J., Shiryaev A. N.: Local martingales and fundamental asset pricing the-
orem in the discrete-time case. Finance and stochastics, 2, 3, 259–273 (1998)
5. Harrison J., Kreps D.: Martingales and arbitrage in multiperiod securities mar-
kets. J. Econom. theory, 20, 381–408 (1979)
6. Kabanov Yu.M.: Arbitrage theory. Jouini, E. et al. (eds.), Option pricing, inter-
est rates and risk management. Cambridge: Cambridge University Press. Hand-
books in Mathematical Finance. 3–42 (2001)
7. Kabanov Y., Stricker Ch.: A teachers’ note on no-arbitrage criteria. S´eminaire de
Probabilit´es XXXV. Berlin: Springer. Lect. Notes Math. 1755, 149–152 (2001)
8. Kabanov Y., Stricker Ch. The Dalang–Morton–Willinger theorem under delayed
and restricted information. S´eminaire de Probabilit´es XXXIX. Berlin: Springer.
Lect. Notes Math. (2005)
9. Rogers L. C. G. Equivalent maqrtingale measures and no-arbitrage. Stochastics
and Stochastics Reports, 51, 41–51 (1994)
10. Stricker Ch. Arbitrage et lois de martingale. Annales de L’Institut Henri
Poincar´e. Probabilite et Statistiques, 26, 3, 451–460 (1990)


A Didactic Note on Affine Stochastic Volatility
Models
Jan KALLSEN∗
HVB-Stiftungsinstitut f¨ur Finanzmathematik, Zentrum Mathematik
TU M¨unchen, Boltzmannstraße 3, D-85747 Garching bei M¨unchen, Germany.
kallsen@ma.tum.de
Summary. Many stochastic volatility (SV) models in the literature are based on
an affine structure, which makes them handy for analytical calculations. The un-
derlying general class of affine Markov processes has been characterized completely
and investigated thoroughly by Duffie, Filipovic, and Schachermayer (2003). In this
note, we take a look at this set of processes and, in particular, affine SV models
from the point of view of semimartingales and time changes. In the course of doing
so, we explain the intuition behind semimartingale characteristics.
Key words: semimartingale characteristics, affine process, time change, stochastic
volatility
Mathematics Subject Classification (2000): 60G99, 91B70
1 Introduction
Semimartingale calculus is by now a standard tool which is covered in many
textbooks. However, this holds true to a lesser extent for the notion of semi-
martingale characteristics – despite of its practical use in many applications.
A first goal of this note is to convince readers (who are not already convinced)
that semimartingale characteristics are a very natural and intuitive concept.
We do so in Section 2 by taking ordinary calculus as a starting point
and by restricting attention to the important special case of absolutely con-
tinuous characteristics. We argue that differential characteristics and certain
martingale problems can be viewed as natural counterparts or extensions of
derivatives and ordinary differential equations (ODE’s). In this sense, affine
processes are the solutions to particularly simple martingale problems, which
extend affine ODE’s to the stochastic case. They are considered in Section 3.
∗This paper has been inspired by fruitful discussions with Arnd Pauwels.

344
Jan Kallsen
Affine processes have been characterized completely and investigated thor-
oughly in an extremely useful and impressive paper by Duffie et al. ([7], hence-
forth DFS). They work predominantly in the context of Markov processes and
their generators. But in a semimartingale setting, their results yield an explicit
solution to the affine martingale problem.
Next to interest rate theory and credit risk, stochastic volatility (SV) mod-
els constitute one of the main areas in finance where the power of the affine
structure has been exploited. In Section 4 we review a number of affine SV
models under the perspective of semimartingale characteristics.
Unexplained notation is typically used as in [12]. Superscripts refer gen-
erally to coordinates of a vector or vector-valued process rather than powers.
The few exceptions as e.g. ex, σ2, v1/α
t
should be obvious from the context.
The notion of a L´evy process X = (Xt)t∈R+ is applied slightly ambigiously.
In the presence of a given filtration F = (Ft)t∈R+, X is supposed to denote a
L´evy process relative to this filtration (PIIS in the language of [12]), otherwise
an intrinsic L´evy process in the sense of [19], i.e. a PIIS relative to its own
natural filtration.
2 Differential semimartingale calculus
In this section we want to provide non-experts in the field with an intuitive
feeling for semimartingale characteristics. It is not the aim to explain the
mathematics behind this concept in detail. This is done exemplarily in the
standard reference [12] (henceforth JS) or in [11], [23].
We hope that the reader does not feel offended by the following digres-
sion on Rd-valued deterministic functions X = (Xt)t∈R+ of time. Specifically,
linear functions Xt = bt are distinguished by constant growth. They are com-
pletely characterized by a single vector b ∈Rd. Many arbitrary functions
behave “locally” as linear ones. This local behavior is expressed in terms of
the derivative
d
dtXt of X at time t ∈R+. Of course, linear functions are up to
the starting value X0 the only ones with constant derivative. In many appli-
cations, functions occur as solutions to ODE’s rather than explicitly, i.e. their
derivative is expressed implicitly as
d
dtXt = f(Xt),
X0 = x0.
(2.1)
In simple cases, the solution to the initial value problem (2.1) can be found
in a closed form, e.g., if f is a linear or, more generally, an affine function.
Linear ODE’s are solved by exponential functions.
We now want to extend the above concepts to a probabilistic setting.
Firstly note that stochastic processes (Xt)t∈R+ are nothing else but random
functions of time. A natural interpretation of constant growth in stochas-
tic terms is stationary, independent increments. Therefore, the L´evy pocesses
(processes with stationary, independent increments) can be viewed as random

A Didactic Note on Affine Stochastic Volatility Models
345
counterparts of linear functions. This is also reflected by the importance of
L´evy processes in applications. The slope b of a linear function is paralleled
by the L´evy–Khintchine triplet (b, c, F) of a L´evy process, where the vector
b ∈Rd stands for a linear drift as in the deterministic case, the symmetric
non-negative d × d matrix c denotes the covariance matrix of the Brownian
motion part of the process, and the L´evy measure F on Rd reflects the inten-
sity of jumps of different sizes. By virtue of the L´evy–Khintchine formula, this
triplet characterizes the distribution of a L´evy process X uniquely. Indeed, we
have Eeiλ⊤Xt = etψ(iλ), where the L´evy exponent ψ is given by
ψ(u) = u⊤b + 1
2u⊤cu +

(eu⊤x −1 −u⊤h(x))F(dx)
(2.2)
and h : Rd →Rd denotes a fixed truncation function as, e.g., h(x) = x1{|x|≤1}.
If h is replaced with another truncation function *h, only the drift coefficient
b changes according to
b(*h) = b(h) +

(*h(x) −h(x))F(dx).
(2.3)
It may seem less obvious how to extend derivatives and initial value prob-
lems to the stochastic case. A classical approach is provided within the theory
of Markov processes. Infinitesimal generators describe the local behaviour of
a Markov process X in terms of the current value Xt, which means that
they naturally generalize ODE’s. In this note, however, we focus instead on
semimartingale characteristics and martingale problems as an alternative tool.
Although the general theory behind Markov processes and semimartingales
looks quite different in the first place, there exist close relationships between
the corresponding concepts (cf. [11], [8]).
Finally, one can use stochastic differential equations (SDE’s) to describe a
process in terms of its local behavior. Even though there is a natural connec-
tion between martingale problems and SDE’s, “linear” martingale problems
do not correspond to linear SDE’s as we shall see below.
The characteristics of a Rd-valued semimartingale X can be defined in
several equivalent ways. In the following definition they occur in an equation
which resembles (2.2).
Definition 1. Suppose that B is a predictable Rd-valued process, C a pre-
dictable process whose values are non-negative symmetric d×d matrices, both
with components of finite variation, and ν a predictable random measure on
R+ × Rd (i.e. a family (ν(ω; ·))ω∈Ωof measures on R+ × Rd with a certain
predictability property, cf. JS for details). Then (B, C, ν) is called character-
istics of X if and only if eiλ⊤X −
 ·
0 eiλ⊤Xt−dΨt(iλ) is a local martingale for
any λ ∈Rd, where
Ψt(u) := u⊤Bt + 1
2u⊤Ctu +

[0,t]×Rd(eu⊤x −1 −u⊤h(x))ν(d(s, x)).

346
Jan Kallsen
It can be shown that any semimartingale has unique characteristics up
to a P-null set. This integral version of the characteristics can alternatively
be written in differential form. More specifically, there exist an increasing
predictable process A, predictable processes b, c, and a transition kernel F
from (Ω× R+, P) into (Rd, Bd) such that
Bt =
 t
0
bsdAs,
Ct =
 t
0
csdAs,
ν([0, t] × G) =
 t
0
Fs(G)dAs,
G ∈Bd.
This decomposition is, of course, not unique. However, in most applications
the characteristics (B, C, ν) are actually absolutely continuous, which means
that one may choose At = t. In this case we call the triplet (b, c, F) differential
characteristics of X. It is unique up to some P(dω) ⊗dt-null set.
Definition 2. Suppose that b is a predictable Rd-valued process, c a predictable
process whose values are non-negative symmetric d × d matrices, and F a
transition kernel from (Ω× R+, P) to (Rd, Bd) such that F·({0}) = 0 and

(1 ∧|x|2)F·(dx) < ∞. We call the triplet (b, c, F) differential characteristics
of X if eiλ⊤X −
 ·
0 eiλ⊤Xt−ψt(iλ)dt is a local martingale for any λ ∈Rd, where
ψt(u) := u⊤bt + 1
2u⊤ctu +

Rd(eu⊤x −1 −u⊤h(x))Ft(dx)
denotes the L´evy exponent of (b, c, F)(ω, t). For want of a handy notation in
the literature, we write ∂X := (b, c, F) in this case.
From an intuitive viewpoint one can interpret the differential characteris-
tics as a local L´evy–Khintchine triplet. Very loosely speaking, a semimartin-
gale with differential characteristics (b, c, F) resembles locally after t a L´evy
process with triplet (b, c, F)(ω, t). Since this local behaviour may depend on
the history up to t, the differential characteristics may be random albeit pre-
dictable. In this sense, the connection between L´evy processes and differential
characteristics parallels the one between linear functions and derivatives of
deterministic functions. In fact, b equals the ordinary derivative if X has ab-
solutely continuous paths (and c = 0, F = 0 in this case). As is well-known, X
is a L´evy process if and only if the differential characteristics are deterministic
and constant (cf. JS, II.4.19):
Proposition 1 (L´evy process). A Rd-valued semimartingale X, X0 = 0,
is a L´evy process if and only if it has a version (b, c, F) of the differential
characteristic which does not depend on (ω, t). In this case, (b, c, F) equals
the L´evy-Khintchine triplet.
As for the ordinary derivative, a number of rules allows to calculate the
differential characteristics comfortably by using L´evy processes as building
blocks.

A Didactic Note on Affine Stochastic Volatility Models
347
Proposition 2 (Stochastic integration). Let X be a Rd-valued semi-
martingale and H a Rn×d-valued predictable process with Hj· ∈L(X),
j = 1, . . . , n (i.e. integrable with respect to X). If ∂X = (b, c, F), then the
differential characteristics of the Rn-valued integral process
H • X := (Hj· • X)j=1,...,n
equals ∂(H • X) = (*b, *c, *F), where
*bt = Htbt +

(*h(Htx) −Hth(x))Ft(dx),
*ct = HtctH⊤
t ,
*Ft(G) =

1G(Htx)Ft(dx),
G ∈Bn.
Here, *h : Rn →Rn denotes the truncation function which is used on Rn.
Variants of Proposition 2 are stated in JS, IX.5.3 or [17], Lemma 3. The effect
of C2-functions on the characteristics follows directly from Itˆo’s formula (cf.
[9], Corollary A.6):
Proposition 3 (C2-function). Let X be a Rd-valued semimartingale with
differential characteristics ∂X = (b, c, F). Suppose that f : U →Rn is twice
continuously differentiable on some open subset U ⊂Rd such that X, X−are
U-valued. Then the Rn-valued semimartingale f(X) has differential charac-
teristics ∂(f(X)) = (*b, *c, *F), where
*bi
t =
d

k=1
∂kf i(Xt−)bk
t + 1
2
d

k,l=1
∂klf i(Xt−)ckl
t
+
 	
*hi (f(Xt−+ x) −f(Xt−)) −
d

k=1
∂kf i(Xt−)hk(x)

Ft(dx),
*cij
t =
d

k,l=1
∂kf i(Xt−)ckl
t ∂lf j(Xt−),
*Ft(G) =

1G (f(Xt−+ x) −f(Xt−)) Ft(dx),
G ∈Bn.
Here, ∂k etc. denote partial derivatives and *h again the truncation function
on Rn.
A Girsanov-type theorem due to Jacod and M´emin studies the behaviour
of the characteristics under absolutely continuous changes of the probability
measure (cf. JS, III.3.24). We state here the following version.

348
Jan Kallsen
Proposition 4 (Change of the probability measure). Let X be a Rd-
valued semimartingale with differential characteristics ∂X = (b, c, F). Suppose
that *P
loc
≪P with the density process
Z = E(H • Xc + W ∗(µX −νX))
(2.4)
for some H ∈L(Xc), W ∈Gloc(µX), where Xc denotes the continuous mar-
tingale part of X and µX, νX the random measure of jumps of X and its
compensator (cf. JS for details). Then the differential characteristics (*b, *c, *F)
of X relative to *P are given by
*bt = bt + H⊤
t ct +

W(t, x)h(x)Ft(dx),
*ct = ct,
*Ft(G) =

1G(x)(1 + W(t, x))Ft(dx),
G ∈Bn.
In applications, the density process can typically be stated in the form (2.4).
Alternatively, one may use a version of Proposition 4 where (*b, *c, *F) is ex-
pressed in terms of the joint characteristics of (X, Z) (cf. [15], Lemma 5.1).
Finally, we consider the effect of absolutely continuous time changes (cf.
[17], Lemma 5 and [11], Chapter 10 for details). They play an important role
in SV models as we shall see in Section 4.
Proposition 5 (Absolutely continuous time change). Let X be a Rd-
valued semimartingale with differential characteristics ∂X = (b, c, F). Suppose
that (Tθ)θ∈R+ is a finite, absolutely continuous time change (i.e. Tθ is a finite
stopping time for any θ and Tθ =
 θ
0 ˙Tρdρ with non-negative derivative ˙Tρ).
Then the time-changed process ( *
Xθ)θ∈R+ := ((X ◦T)θ)θ∈R+ := (XTθ)θ∈R+
is a semimartingale relative to the time-changed filtration
(*Fθ)θ∈R+ := (FTθ)θ∈R+
with differential characteristics ∂*
X = (*b, *c, *F) given by
*bθ = bTθ ˙Tθ,
*cθ = cTθ ˙Tθ,
*Fθ(G) = FTθ(G) ˙Tθ,
G ∈Bn.
Let us now turn to the stochastic counterpart of the initial value problem
(2.1), where the local dynamics of X are expressed in terms of X itself. This
can be interpreted as a special case of a martingale problem in the sense of
JS, III.2.4 and III.2.18.
Definition 3. Suppose that P0 is a distribution on Rd and functions β : Rd ×
R+ →Rd, γ : Rd × R+ →Rd×d, ϕ : Rd × R+ × Bd →R+ are given.

A Didactic Note on Affine Stochastic Volatility Models
349
We call (Ω, F, F, P, X) solution to the martingale problem related to P0 and
(β, γ, ϕ) if X is a semimartingale on (Ω, F, F, P) such that L(X0) = P0 and
∂X = (b, c, F) with
bt(ω) = β(Xt−(ω), t),
ct(ω) = γ(Xt−(ω), t),
(2.5)
Ft(ω, G) = ϕ(Xt−(ω), t, G).
More in line with the common language of martingale problems, one may also
call the distribution P X of X solution to the martingale problem. In any case,
uniqueness refers only to the law P X because solution processes on different
probability spaces cannot be reasonably compared otherwise.
Since ODE’s are particular cases of this kind of martingale problems, one
cannot expect that unique solutions generally exist, let alone to solve them
(cf. JS, III.2c and [11] in this respect). In this note we will only consider
particularly simple martingale problems, namely linear and affine ones.
3 Affine processes
Parallel to affine ODE’s, we assume that the differential characteristics (2.5)
are affine functions of Xt−in the following sense:
β((x1, . . . , xd), t) = β0 +
d

j=1
xjβj,
γ((x1, . . . , xd), t) = γ0 +
d

j=1
xjγj,
(3.1)
ϕ((x1, . . . , xd), t, G) = ϕ0(G) +
d

j=1
xjϕj(G),
where (βj, γj, ϕj), j = 0, . . . , d are given L´evy–Khintchine triplets on Rd. As
in the deterministic case, it is possible not only to prove existence of a unique
solution but also to solve the affine martingale problem related to (3.1) in a
sense explicitly. This has been done by DFS. More precisely, they characterize
affine Markov processes and their laws. However, applied to the present setup
one obtains the statement below on affine martingale problems (cf. Theorem
3.1).
It is obvious that the d+1 L´evy–Khintchine triplets (βj, γj, ϕj) cannot be
chosen arbitrarily. It has to be ensured that the local covariance matrix c and
the local jump measure F in the differential characteristics ∂X = (b, c, F) of
the solution remain positive even if some of the components Xj turn negative.
This leads to a number of conditions:

350
Jan Kallsen
Definition 4. Let m, n ∈N with m + n = d. L´evy–Khintchine triplets
(βj, γj, ϕj), j = 0, . . . , d are called admissible if the following conditions hold:
βk
j −

hk(x)ϕj(dx) ≥0
ϕj((Rm
+ × Rn)C) = 0

hk(x)ϕj(dx) < ∞


if 0 ≤j ≤m,
1 ≤k ≤m,
k ̸= j;
γkl
j = 0
if 0 ≤j ≤m,
1 ≤k, l ≤m
unless k = l = j;
βk
j = 0
if j ≥m + 1,
1 ≤k ≤m;
γj = 0
ϕj = 0

if j ≥m + 1.
A deep result of DFS shows that the martingale problem related to (3.1)
has a unique solution for essentially any admissible choice of triplets:
Theorem 3.1. Let (βj, γj, ϕj), j = 0, . . . , d, be admissible L´evy–Khintchine
triplets and denote by ψj the corresponding L´evy exponents in the sense of
(2.2). Suppose in addition that

{|x|≥1}
|x|kϕj(dx) < ∞,
1 ≤j, k ≤m.
(3.2)
Then the martingale problem related to (β, γ, ϕ) as in (3.1) and any ini-
tial distribution P0 on Rm
+ × Rn has a solution (Ω, F, F, P, X), where X is
Rm
+ × Rn-valued. Its distribution is uniquely characterized by its conditional
characteristic function
E

eiλ⊤Xs+t
Fs

= exp

Ψ 0(t, iλ) + Ψ (1,...,d)(t, iλ)⊤Xs

,
λ ∈Rd,
(3.3)
where the mappings Ψ (1,...,d) = (Ψ 1, . . . , Ψ d) : R+ ×(Cm
−×iRn) →(Cm
−×iRn)
and Ψ 0 : R+ × (Cm
−× iRn) →C solve the following system of generalized
Riccati equations:
Ψ 0(0, u) = 0,
Ψ (1,...,d)(0, u) = u,
d
dtΨ j(t, u) = −ψj(Ψ (1,...,d)(t, u)),
j = 0, . . . , d
(3.4)
(and Cm
−:= {z ∈Cm : Re(zj) ≤0, j = 1, . . . , m}).
Proof. Up to two details, the assertion follows directly from DFS, Theorems
2.7, 2.12 and Lemma 9.2. Equation (3.3) is derived in DFS under the additional
assumptions that the initial distribution is of degenerate form P0 = ǫx for
x ∈Rm
+ × Rn and that the filtration F is generated by X. Hence, it suffices
to reduce the general statement to this case.
Let (Dd, Dd, Dd) be the Skorohod path space of Rd-valued c`adl`ag functions
on R+ endowed with its natural filtration (cf. JS, Chapter VI). Denote by Y
the canonical process, i.e. Yt(α) = α(t) for α ∈Dd.

A Didactic Note on Affine Stochastic Volatility Models
351
Fix s ∈R+, ω ∈Ω. From the characterization in Definition 1 (more pre-
cisely, from the slightly more general formulation in JS, II.2.42, because we do
not know in the first place that Y is a semimartingale) it follows that Y has
differential characteristics of the form (2.5) and (3.1) relative to the probabil-
ity measure *Ps,ω := P (Xs+t)t∈R+|Fs(ω, ·) on (Dd, Dd) (except for some P-null
set of ω’s). Therefore, Y solves the affine martingale problem corresponding
to (3.1) and it has degenerate initial distribution *P Y0
s,ω = ǫXs(ω). Theorem 2.12
in DFS yields that
E

eiλ⊤Xs+t
Fs

(ω) = *Es,ωeiλ⊤Yt
= *Es,ω

*Es,ω

eiλ⊤Yt
D0

= *Es,ω exp

Ψ 0(t, iλ) + Ψ (1,...,d)(t, iλ)⊤Y0

,
= exp

Ψ 0(t, iλ) + Ψ (1,...,d)(t, iλ)⊤Xs(ω)

for P-almost all ω ∈Ω.
□
Remarks.
1. The restriction X1, . . . , Xm ≥0 has to be naturally imposed because
otherwise γ(Xt−, t), ϕ(Xt−, t, G) in (3.1) may turn negative which does
not make sense. The remaining n components Xm+1, . . . , Xd, on the other
hand, affect the characteristics of X only through the drift rate βj. Due
to the conditions γj = 0, ϕj = 0, j ≥m + 1, parts of the ODE system
(3.4) are reduced actually to simple integrals and linear equations which
can be solved in closed form (cf. (2.13)–(2.15) in DFS and Corollary 3.2
below for a special case).
2. Condition (3.2) guaranties that the solution process does not explode in
finite time and hence is a semimartingale on R+ in the usual sense. It
can be relaxed by a weaker necessary and sufficient condition (cf. DFS,
Proposition 9.1).
3. By introducing the zeroth component X0
t = 1, it is easy to see that an
affine process in Rm
+ ×Rn ⊂Rd can be interpreted as a process with linear
characteristics in R1+m
+
× Rn ⊂R1+d. Since the solution to linear ODE’s
are exponential functions, one could be tempted to call the solutions to
such linear martingale problems “stochastic exponentials.” However, this
notion usually refers to the solutions to linear SDE’s and the latter typi-
cally do not have linear characteristics. For example, Propositions 1 and 2
yield that the differential characteristics of the geometric Wiener process
Xt = 1 +
 t
0 XsdWs are of the form ∂X = (0, X2, 0). Hence they are
quadratic rather than linear in X.

352
Jan Kallsen
4. Observe that the solution depends on the involved triplets only through
their L´evy exponents, which is agreeable for concrete models where the
latter are known in closed form.
For such applications as, e.g., estimation purposes it is useful to dispose
of a closed form expression of the finite-dimensional marginals. It follows by
induction from Theorem 3.1.
Corollary 3.1. The joint characteristic function of Xt1, . . . , Xtν is given by
E exp
	
i
ν

k=1
λk·Xtk

= ˆP0

Ψν(t1 −t0, . . . , tν −tν−1; iλ1·, . . . , iλν·)

exp
	 ν

k=1
Ψ 0(tk −tk−1, iλk·)

,
for any 0 = t0 ≤t1 ≤· · · ≤tν and any λ ∈Rν×d, where ˆP0(u) :=

euxP0(dx)
and Ψν is defined recursively via
Ψ1(τ1; u1) := Ψ (1,...,d)(τ1, u1)
and
Ψk(τ1, . . . , τk; u1, . . . , uk)
:= Ψk−1

τ1, . . . , τk−1; u1, . . . , uk−2, uk−1 + Ψ (1,...,d)(τk, uk)

.
Since an affine process is characterized by at most d + 1 L´evy–Khintchine
triplets, one may wonder whether it can in fact be expressed pathwise in
terms of d + 1 L´evy processes with the corresponding triplets. We give a
partial answer to this question.
Theorem 3.2 (Time change representation of affine processes). Let
X be an affine process as in Theorem 3.1. On a possibly enlarged proba-
bility space, there exist intrinsic Rd-valued L´evy processes L(j) with triplets
(βj, γj, ϕj), j = 0, . . . , d, such that
Xt = X0 + L(0)
t
+
d

j=1
L(j)
Θj
t ,
(3.5)
where
Θj
t =
 t
0
Xj
s−ds.
(3.6)
Proof. By an enlargement of the probability space (Ω, F, P) we refer, specifi-
cally, to a space of the form (Ω×Dd′, F⊗Dd′, P ′) such that P ′(A×Dd′) = P(A)
for A ∈F. Here Dd′ denotes as before the space of Rd′-valued c`adl`ag func-
tions. The process X is identified with the process X′ on the enlarged space
which is given by X′
t(ω, α) := Xt(ω) for (ω, α) ∈Ω× Dd′.

A Didactic Note on Affine Stochastic Volatility Models
353
Step 1: Firstly, we choose triplets (*βj, *γj, *ϕj), j = 0, . . . , (d+2)d, on R(d+2)d
as follows. For j = 0, . . . , d, we define (*βj, *γj, *ϕj) as the L´evy–Khintchine
triplet of the R(d+2)d-valued L´evy process (V, U 0, . . . , U d) given by
U k :=
V
if k = j
0 ∈Rd if k ̸= j,
where V denotes a Rd-valued L´evy process with triplet (βj, γj, ϕj). For
j > d, we set (*βj, *γj, *ϕj) = (0, 0, 0). One verifies easily that the new
triplets (*βj, *γj, *ϕj), j = 0, . . . , (d + 2)d are admissible (with *d := (d + 2)d,
*m := m, *n := *d −m). By Theorem 3.1 (resp. DFS) there is an R(d+2)d-
valued affine process ( *
X, *Y 0, . . . , *Y d) corresponding to the initial distribution
*P0 = P0 ⊗Jd
j=0 ǫ0 and the triplets (*βj, *γj, *ϕj); namely, the canonical process
on the path space (D(d+2)d, D(d+2)d, D(d+2)d) relative to some law Q on that
space.
Step 2: By applying Proposition 3 to the mapping f(x, y0, . . . , yd) = x,
we observe that the characteristics of the first d components *
X coincide with
those of the original Rd-valued affine process X. Since P0 is the distribution
of both X0 and *
X0, we have that P X = Q*
X, i.e. the laws of X and *
X coincide
as well.
Step 3: On the product space (Ω′, F′) := (Ω×D(d+1)d, F ⊗D(d+1)d) define
a probability measure
P ′(dω × dy) := P(dω)Q(*
Y 0,...,*
Y d)|*
X=X(ω)(dy)
and a R(d+2)d-valued process (X′, Y 0, . . . , Y d) with
(X′, Y 0, . . . , Y d)t(ω, y) := (Xt(ω), y(t)).
Its distribution P ′(X′,Y 0,...,Y d) equals Q by Step 2. If the filtration F′ on
(Ω′, F′) is chosen to be generated by (X′, Y 0, . . . , Y d), then this process is
affine in the sense of Theorem 3.1 corresponding to the triplets (*βj, *γj, *ϕj).
As suggested before Step 1, we identify X′ on the enlarged space with X on
the original space.
Step 4: Applying Proposition 3 to the mapping
f(x, y0, . . . , yd) = x −
d

j=0
yj
yields that X −d
j=0 Y j has differential characteristics (0, 0, 0), which implies
that it is constant, i.e.
X = X0 +
d

j=0
Y j.

354
Jan Kallsen
Step 5: Finally, applying Proposition 3 to f(x, y0, . . . , yd) = yj yields that
Y j has differential characteristics
∂Y j = (Xj
−βj, Xj
−γj, Xj
−ϕj)
(3.7)
for j = 1, . . . , d and ∂Y 0 = (β0, γ0, ϕ0). In particular, L(0) := Y 0 is a L´evy
process.
Step 6: Let j ∈{m + 1, . . . , d}. Since γj = 0, ϕj = 0, we have that
Y j
t = βj
 t
0
Xj
s−ds = L(j)
Θj
t
for the deterministic L´evy process L(j)
θ
:= βjθ and the (not necessarily in-
creasing) “time change” (3.6).
Step 7: Now, let j ∈{1, . . . , m}. For θ ∈R+ define
T j
θ := inf{t ∈R+ : Θj
t > θ}.
Since Θj = (Θj
t)t∈R+ is adapted, we have that its inverse T j = (T j
θ )θ∈R+ is a
time change in the sense of [11], §10.1a.
For H := 1{Xj
−=0} we have ∂(H • Y j) = (0, 0, 0) by Proposition 2, which
implies that H
• Y j = 0. For fixed ω′ ∈Ω′ consider u < v with Θj
u = Θj
v.
Then (u, v] ⊂{t ∈R+ : Xj
t−(ω′) = 0}, which implies that
Y j
v −Y j
u = H • Y j
v −H • Y j
u = 0.
In view of [11], (10.14), it follows that Y j is T j-adapted.
Define the time-changed process L(j) := Y j ◦T j (in the sense of [11], (10.6)
if T j
θ = ∞for finite θ, i.e. if Θj
∞< ∞). The integral characteristics of L(j)
relative to the corresponding time-changed filtration equal ( *B, *C, *ν) with
*Bθ = BT j
θ ,
*Cθ = CT j
θ ,
*ν([0, θ] × ·) = ν([0, T j
θ ] × ·),
(3.8)
where (B, C, ν) denote the integral characteristics of Y j. This is stated in
[16], Lemma 5, for the case Θj
∞= ∞. In the general case L(j) may only be a
semimartingale on [[0, Θj
∞[[ in the sense of [11], (5.4). Then (3.8) holds on this
stochastic interval as can be deduced from [11], (10.17), (10.27).
Consequently,
*Bθ = BT j
θ = βj
 T j
θ
0
Xj
s−ds = βj(Θj ◦T j)θ = βjθ
and accordingly for *C, *ν if θ < Θj
∞. This means that L(j) is a “L´evy process
on [[0, Θj
∞[[” in the sense that its characteristics on [[0, Θj
∞[[ equal those of a
L´evy process with triplet (βj, γj, ϕj).

A Didactic Note on Affine Stochastic Volatility Models
355
Step 8: By “glueing” (L(j)
θ )θ∈[0,Θj
∞) together with another L´evy process on
[[Θj
∞, ∞[[ having the same triplet, we extend L(j) to the whole R+. This can
be done along the lines of [11], (10.32) and §10.2b after an enlargement of the
probability space.
Since Y j is T j-adapted (cf. Step 7), we have Y j
t = L(j)
Θj
t for any t ∈R+.
The assertion follows now from Step 4.
□
The previous result is not entirely satisfactory in some aspects. E.g., it is
not shown that X is a measurable function of L(j), j = 0, . . . , d, i.e., loosely
speaking, that X is a strong solution of the time change equations (3.5)-(3.6).
For the purposes of the subsequent section, let us state a simple special case
of Theorem 3.1. We suppose that m = n = 1, where the second component X2
will denote a logarithmic asset price in the affine SV models considered below.
We assume that it has no mean-reverting term. Secondly, we suppose that
the “volatility” process X1 is of the Ornstein–Uhlenbeck type. This means
that the Riccati-type equation (3.4) is an affine ODE, which can be solved
explicitly.
Corollary 3.2. In the case m = n = 1 suppose that (βj, γj, ϕj), j = 0, 1, 2,
are L´evy–Khintchine triplets such that
β1
0 −

h1(x)ϕ0(dx) ≥0,
γkl
0 = 0
unless k = l = 2,
ϕ0((R+ × R)C) = 0,

h1(x)ϕ0(dx) < ∞,
γkl
1 = 0
unless k = l = 2,
ϕ1(({0} × R)C) = 0,
(β2, γ2, ϕ2) = (0, 0, 0).
Then the martingale problem related to (β, γ, ϕ) as in (3.1) and any initial
distribution P0 on R+ × R has a solution (Ω, F, F, P, X), where X is R+ × R-
valued. Its distribution is uniquely characterized by its conditional character-
istic function
E

eiλ1X1
s+t+iλ2X2
s+t
Fs

= exp

Ψ 0(t, iλ1, iλ2) + Ψ 1(t, iλ1, iλ2)X1
s + iλ2X2
s

,
where Ψ j : R+ × (C−× iR) →C, j = 0, 1, are given by
Ψ 1(t, u1, u2) = eβ1
1tu1 −1 −eβ1
1t
β1
1
ψ1(0, u2),
Ψ 0(t, u1, u2) =
 t
0
ψ0(Ψ 1(s, u1, u2), u2)ds.

356
Jan Kallsen
4 Affine stochastic volatility models
In the empirical literature, a number of so-called stylized facts has been re-
ported repeatedly, namely semi-heavy tails in the return distribution, volatil-
ity clustering, and a negative correlation between changes in volatility and
asset prices (leverage effect). These features are reflected in the SV models
that have been suggested. At the same time, it seems desirable to work in set-
tings which are analytically tractable. Here, affine models play an important
role. The fact that the characteristic function is known in closed or semi-
closed form opens the door to derivative pricing, calibration, hedging, and
estimation.
If the model is set up under the risk-neutral measure, European option
prices can be computed by Laplace transform methods. This approach re-
lies on the fact that the characteristic function or Laplace transform can be
interpreted as a set of prices of complex-valued contingent claims. A large
class of arbitrary payoffs can be represented explicitly as a linear combination
or, more precisely, integral of such “simple” claims (cf. e.g. [4], [20]). As far
as estimation is concerned, the knowledge of the joint characteristic function
can be exploited for generalized moment estimators (cf. [13] and [26] for an
overview).
Typically, (broad-sense) stochastic volatility models fall into two groups.
Either market activity is expressed in terms of the time-varying size or mag-
nitude of price movements, or alternatively, by their speed or arrival rate. The
models of the first group are often stated in terms of an equation
dXt = σtdLt,
(4.1)
possibly modified by an additional drift term. Here, X denotes the logarithm
of an asset price and L a L´evy process as, e.g., Brownian motion. In this
equation, the SV process σ affects the size of relative price moves.
Models of the second kind arise from time-changed L´evy processes
Xt = X0 + LVt.
(4.2)
Again, L denotes a L´evy process and X the logarithm of the asset price.
Here, the time change Vt =
 t
0 vsds affects the speed of price moves. Often Vt
is interpreted as business time. Measured on this operational time scale, log
prices evolve homogeneously but due to randomly changing trading activity
vt, this is not true relative to calender time.
If the L´evy process L is a Wiener process and if L, σ, respectively L, v, are
independent, then the two approaches lead essentially to the same models.
This fact is due to the self-similarity of Brownian motion and it is reflected
by Propositions 2 and 5, where the choice vt = σ2
t leads to the same dif-
ferential characteristics of X in either case. Again due to self-similarity, the
correspondence between (4.1) and (4.2) remains true for α-stable L´evy mo-
tions L. In this case, vt = σα
t leads to the same characteristics (cf. also [17]

A Didactic Note on Affine Stochastic Volatility Models
357
in this respect). For general L´evy processes, however, (4.1) and (4.2) lead to
quite different models because the change of measure in Proposition 2 does
not lead to a multiple of F as in Proposition 5. Except for α-stable L´evy
motions L, models of type (4.1), in general, do not lead to affine processes.
Typically, the distribution of X is not known in closed form.
Another important distinction refers to the sources of randomness that
drive the L´evy process L and the volatility process σ resp. v in (4.1) and
(4.2). In the simplest case, these two are supposed to be independent. This,
however, excludes the above-mentioned leverage effect, i.e. it does not allow
for negative correlation between volatility and asset price changes. Whereas
such a correlation can be incorporated easily in models of type (4.1), this is
less obvious in (4.2) because L and v live on different time scales (business
vs. calender time).
The other extreme would be to use a common source of randomness for
both L and σ or L and v, respectively. This can be interpreted in the sense
that changes in volatility are caused by changes in asset prices. This spirit un-
derlies the ARCH-type models in the econometric literature. An interesting
and natural continuous-time extension of GARCH(1,1) has recently been sug-
gested in [18]. But since ARCH models are based on rescaling the innovations
in the sense of (4.1), they do not lead to an affine structure. Nevertheless, the
idea to use a common driver for volatility and price moves can be carried out
in the context of affine processes as well (cf. Subsection 4.6).
We will now discuss a number of well-known affine SV models from the
point of view of characteristics. For a more exhaustive coverage of the litera-
ture, see DFS and [5]. We express the characteristics of the affine processes in
terms of triplets (3.1). By straightforward insertion one can derive closed-form
expressions for the corresponding L´evy exponents ψj, j = 0, . . . , d, in terms
of the L´evy exponents of the involved L´evy processes and the additional pa-
rameters in the corresponding model.
In all the examples, it is implicitly assumed that the filtration is generated
by the affine process under consideration (cf. the last remark of Subsection 4.8
in this context). Moreover, we assume generally that the identity h(x) = x is
used as “truncation” function because this simplifies some of the expressions
considerably. This choice implies that the corresponding L´evy measures have
first moments in the tails. The general formulation without such moment
assumptions can be derived immediately from (2.3).
4.1 Stein and Stein (1991)
Slightly generalized, the model in [24] is of the form
dXt = (µ + δσ2
t )dt + σtdWt,
dσt = (κ −λσt)dt + αdZt
(4.3)
with constants κ ≥0, µ, δ, λ, α and Wiener processes W, Z having constant
correlation ρ. As can be seen from straightforward application of Propositions

358
Jan Kallsen
1-3, neither (σ, X) nor (σ2, X) have affine characteristics in the sense of (3.1)
unless the parameters are chosen in a very specific way (e.g. κ = 0). However,
the R3-valued process (σ, σ2, X) is “almost” the solution to an affine martin-
gale problem related with (3.1), namely, for (βj, γj, ϕj), j = 0, . . . , 3, given
by
(β0, γ0, ϕ0) =
		 κ
α2
µ

,
	 α2 0 0
0 0 0
0 0 0

, 0

,
(β1, γ1, ϕ1) =
		 −λ
2κ
0

,
	 0
2α2 αρ
2α2
0
0
αρ
0
0

, 0

,
(β2, γ2, ϕ2) =
		
0
−2λ
δ

,
	 0
0
0
0 4α2 2αρ
0 2αρ
1

, 0

,
(β3, γ3, ϕ3) = (0, 0, 0) .
Since γ1 is not non-negative definite, (β1, γ1, ϕ1) is not a L´evy–Khintchine
triplet in the usual sense and hence Theorem 3.1 cannot be applied. Nev-
ertheless, the Riccati-type equation (3.4) leads to the correct characteristic
function in this case (see, e.g., the derivation in [22]). The process (σ, σ2, X)
is closely related to the non-degenerate example in DFS, Subsection 12.2 of
an affine Markov process with a non-standard maximal domain.
4.2 Heston (1993)
If κ is chosen to be 0 in the Ornstein-Uhlenbeck equation (4.3), then the Stein
and Stein model reduces to a special case of the model in [10]:
dXt = (µ + δvt)dt + √vtdWt,
dvt = (κ −λvt)dt + σ√vtdZt.
(4.4)
Here, κ ≥0, µ, δ, λ, σ denote constants and W, Z Wiener processes with con-
stant correlation ρ. Calculation of the characteristics yields that (v, X) is an
affine process with triplets (βj, γj, ϕj), j = 0, 1, 2, in (3.1) given by
(β0, γ0, ϕ0) =

κ
µ

, 0, 0

,
(β1, γ1, ϕ1) =

−λ
δ

,

σ2 σρ
σρ 1

, 0

,
(β2, γ2, ϕ2) = (0, 0, 0) .
4.3 Barndorff-Nielsen and Shephard (2001)
In the article [1] (henceforth BNS) it is considered a model of the form

A Didactic Note on Affine Stochastic Volatility Models
359
dXt = (µ + δvt−)dt + √vt−dWt + ρdZt,
dvt = −λvt−dt + dZt.
(4.5)
Here, µ, δ, ρ, λ denote constants, W a Wiener processes, and Z a subordina-
tor (i.e. an increasing L´evy process) with L´evy–Khintchine triplet (bZ, 0, F Z).
Compared to the Heston model, the square-root process (4.4) is replaced with
a L´evy-driven Ornstein–Uhlenbeck (OU) process. Since W and Z are neces-
sarily independent, leverage is introduced by the ρdZt term. Again, Proposi-
tions 1 and 2 yield that (v, X) is an affine process with triplets (βj, γj, ϕj),
j = 0, 1, 2, in (3.1) of the form
β0 =

bZ
µ + ρbZ

,
γ0 = 0,
ϕ0(G) =

1G(y, ρy)F Z(dy),
G ∈B2,
(β1, γ1, ϕ1) =

−λ
δ

,

0 0
0 1

, 0

,
(β2, γ2, ϕ2) = (0, 0, 0) .
Due to the simple structure of the characteristics, we are in the situation of
Corollary 3.2.
BNS consider also a slightly extended version of the above model. They ar-
gue that the autocorrelation pattern of volatility is not appropriately matched
by a single OU process. As a way out they suggest a linear combination of
independent OU processes, i.e. a model of the form
dXt = (µ + δvt−)dt + √vt−dWt +
ν

k=1
ρkdZk
t ,
vt =
ν

k=1
αkv(k)
t
,
dv(k)
t
= −λkv(k)
t−dt + dZk
t ,
with constants α1, . . . , αν ≥0, µ, δ, ρ1, . . . , ρν, λ1, . . . , λν, a Wiener processes
W, and a Rν-valued L´evy process Z with triplet (bZ, 0, F Z) whose components
are independent subordinators. (v(1), . . . , v(ν), v, X) is a Rν+2-valued affine
process whose triplets (βj, γj, ϕj), j = 0, . . . , ν + 2 are of the form
β0 =







bZ1
...
bZν

k αkbZk
µ + 
k ρkbZk







,
γ0 = 0,
ϕ0(G) =

1G(y1, . . . , yν, ν
k=1 αkyk, ν
k=1 ρkyk)F Z(dy),
G ∈Bν+2,

360
Jan Kallsen
(βk, γk, ϕk) =

(0, . . . , 0, −λk, 0, . . . , 0, −αkλk, 0)⊤, 0, 0

, k = 1, . . . , ν,
(βν+1, γν+1, ϕν+1) =








0
...
0
δ



,




0 . . . 0 0
... ... ...
...
0 · · · 0 0
0 · · · 0 1



, 0



,
(βν+2, γν+2, ϕν+2) = (0, 0, 0) .
In order to preserve this affine structure, the subordinators Z1, . . . , Zν do
not have to be independent. The other extreme case Z1 = . . . = Zν, leads to
the realm of continuous-time ARMA processes proposed in [2].
4.4 Carr, Geman, Madan, Yor (2003)
The paper [3] (henceforth CGMY) generalizes both the Heston and the BNS
model by allowing for jumps in the asset price. As noted at the beginning of
this section, one must consider time changes in order to preserve the affine
structure unless the driver of the asset price changes is a stable L´evy motion
(cf. Subsection 4.5).
The analogue of the Heston model is
Xt = X0 + µt + LVt + ρ(vt −v0),
dVt = vtdt,
dvt = (κ −λvt)dt + σ√vtdZt,
(4.6)
where κ ≥0, µ, ρ, λ, σ are constants, L denotes a L´evy process with triplet
(bL, cL, F L) and Z an independent Wiener process. Again, (v, X) is an affine
process whose triplets (βj, γj, ϕj), j = 0, 1, 2 meet the equations
(β0, γ0, ϕ0) =

κ
µ + ρκ

, 0, 0

,
β1 =

−λ
bL −ρλ

, γ1 =

σ2
σ2ρ
σ2ρ σ2ρ2 + cL

, ϕ1(G) =

1G(0, x)F L(dx),
(β2, γ2, ϕ2) = (0, 0, 0) .
Observe that we recover the characteristics of the Heston model – up to a
rescaling of the volatility process v – if L is chosen to be a Brownian motion
with drift.
Proof. It remains to be shown that the differential characteristics of (v, X)
are as claimed above. Note that ∂v and ∂(L◦V ) are obtained from Propositions
2 and 5, respectively. For any R2-valued semimartingale Y with ∂Y = (b, c, F)

A Didactic Note on Affine Stochastic Volatility Models
361
we have ∂Y 1 = (b1, c11, F 1) with F 1(G) := F((G \ {0}) × R) and likewise for
Y 2, e.g., by Proposition 3.
Since v does not jump, this yields Ft(G) =

1G(0, x)F L◦V
t
(dx), G ∈B, for
the joint L´evy measure F of (v, L ◦V ). Consequently, ∂(v, L ◦V ) =: (b, c, F)
is completely determined if we know c12 (= c21). Since L is independent of Z
and hence of v, it follows from some technical arguments that ⟨v, L ◦V ⟩= 0,
which implies that c12 = 0 by JS, II.2.6. Applying Proposition 3 to the map-
ping f(y, x) = (y, x + ρy) yields ∂(v, X) in the case µ = 0. The modification
µ ̸= 0 just affects the drift coefficient of X.
□
In order to generalize the BNS model, the square-root process (4.6) is
replaced with a L´evy-driven OU process:
Xt = X0 + µt + LVt + ρZt,
dVt = vt−dt,
(4.7)
dvt = −λvt−dt + dZt.
Here, µ, ρ, λ are constants and L, Z denote independent L´evy processes with
triplets (bL, cL, F L) and (bZ, 0, F Z), respectively, and Z is supposed to be
increasing. The triplets (βj, γj, ϕj), j = 0, 1, 2, of the affine process (v, X) are
given by
β0 =

bZ
µ + ρbZ

,
γ0 = 0,
ϕ0(G) =

1G(y, ρy)F Z(dy),
G ∈B2,
β1 =
 −λ
bL

,
γ1 =
 0 0
0 cL

,
ϕ1(G) =

1G(0, x)F L(dy),
G ∈B2,
(β2, γ2, ϕ2) = (0, 0, 0) .
For a Brownian motion with drift L, we recover the dynamics of the BNS
model (4.5). As in that case, Corollary 3.2 can be applied.
Proof. The differential characteristics of (v, X) are derived similarly as
above. Again, ∂v and ∂(L ◦V ) are obtained from Propositions 2 and 5, re-
spectively. If we write ∂(v, L ◦V ) =: (b, c, F), then c11 = 0 and hence also
c12 = c21 = 0. The marginal of the instantaneous L´evy measure Ft are given
by the corresponding L´evy measures of v and L ◦V , respectively. Since L is
independent of Z, we have that v and L ◦V never jump at the same time
(up to some P-null set). Consequently, F is concentrated on the coordinate
axes, which implies that F(G) =

1G(y, 0)F v(dy) +

1G(0, x)F L◦V (dx). As
above, Proposition 3 yields the characteristics of (v, *
X) for *
X := LVt + ρvt.
Since dXt = d *
Xt + (µ + λvt)dt, a correction of the drift yields ∂(v, X).
□

362
Jan Kallsen
4.5 Carr and Wu (2003)
The study [5] considers a modification of the Heston model where the Wiener
process W is replaced by an α-stable L´evy motion L with α ∈(1, 2) and
L´evy–Khintchine triplet (0, 0, F L):
dXt = µdt + v1/α
t
dLt,
dvt = (κ −λvt)dt + σ√vtdZt.
The self-similarity of L is reflected by the fact that

1G(c1/αx)F L(dx) =
cF L(G) for c > 0, G ∈B. An application of Propositions 1 and 2 shows that
(v, X) is an affine process with triplets (βj, γj, ϕj), j = 0, 1, 2, of the form
(β0, γ0, ϕ0) =

κ
µ

, 0, 0

,
β1 =

−λ
0

,
γ1 =

σ2 0
0 0

,
ϕ1(G) =

1G(0, x)F L(dy),
G ∈B2,
(β2, γ2, ϕ2) = (0, 0, 0) .
4.6 Carr and Wu (2004) and affine ARCH-like models
In the paper [6] it is considered a number of models, two of which could be
written in the form
Xt = X0 + µt + LVt,
(4.8)
dVt = vt−dt,
(4.9)
vt = v0 + κt + ZVt
(4.10)
with constants κ ≥0,
µ and a L´evy process (Z, L) in R2 with triplet
(b(Z,L), c(Z,L), F (Z,L)), where Z has only non-negative jumps and finite ex-
pected value E(Z1).
Note that the above equation vt = v0+κt+Z t
0 vs−ds is implicit. It may not
be evident in the first place that a unique solution to this time change equation
exists. On the other hand, the affine martingale problem corresponding to
triplets (βj, γj, ϕj), j = 0, 1, 2, of the form
(β0, γ0, ϕ0) =

κ
µ

, 0, 0

,
(β1, γ1, ϕ1) =

b(Z,L), c(Z,L), F (Z,L)
,
(β2, γ2, ϕ2) = (0, 0, 0)
has a unique solution by Theorem 3.1. In view of Theorem 3.2, the solution
process (v, X) can be expressed in the form (4.8)–(4.10) for some L´evy process
(Z, L) with triplet (b(Z,L), c(Z,L), F (Z,L)).

A Didactic Note on Affine Stochastic Volatility Models
363
The paper [6] discusses two particular cases of the above setup, namely
a joint compound Poisson process with drift (Z, L) and, alternatively, the
completely dependent case Zt = −λt −σLt with constants λ, σ and some
totally skewed α-stable L´evy motion L, where α ∈(1, 2]. The latter model
has an ARCH-like structure in the sense that the same source of randomness
L drives both the volatility and the asset price process. This extends to a more
general situation where L is an arbitrary L´evy process and ∆Zt = f(∆Lt)
for some deterministic function f : R →R+ as e.g. f(x) = x2. If L or f are
asymmetric, such models allow for leverage. A drawback of this setup is that
it is not of the simple structure in Corollary 3.2. Non-trivial ODE’s may have
to be solved in order to obtain the characteristic function.
4.7 A model with flexible leverage
Any affine SV model can be defined directly in terms of the involved L´evy–
Khintchine triplets, sometimes in the simple form of Corollary 3.2. Since this
leads automatically to handy formulas for characteristic functions as well as
differential characteristics, there is in principle no need for a stochastic differ-
ential equation or the like. Still, concrete equations of the above type may be
useful in order to reduce generality and to give more insight in the structure
of a model.
Observe that the dependence structure between changes in asset prices and
volatility in (4.7) is quite restrictive in the sense that any rise ∆Zt in volatility
results in a perfectly correlated move ρ∆Zt of the asset. This cannot be relaxed
easily by considering dependent L´evy processes L, Z because these two live
on different time scales. In this subsection, we suggest a class of models in the
spirit of (4.7), which is more flexible as far as the leverage effect is concerned.
Nevertheless, we retain the simple structure of Corollary 3.2, where no Riccati-
type equations have to be solved.
Xt = X0 + LVt + Yt,
dVt = vt−dt,
(4.11)
dvt = −λvt−dt + dZt.
Here, λ is a constant and L a L´evy process with triplet (bL, cL, F L), which is
assumed to be independent of another L´evy process (Z, Y ) in R2 with triplet
(b(Z,Y ), c(Z,Y ), F (Z,Y )) and Z is supposed to be a subordinator. As before,
(v, X) is an affine process with triplets (βj, γj, ϕj), j = 0, 1, 2, given by
(β0, γ0, ϕ0) =

b(Z,Y ), c(Z,Y ), F (Z,Y )
,
(4.12)
β1 =
 −λ
bL

,
γ1 =
 0 0
0 cL

,
ϕ1(G) =

1G(0, x)F L(dx),
G ∈B2,
(β2, γ2, ϕ2) = (0, 0, 0) .

364
Jan Kallsen
Proof. This follows similarly as in Subsection 4.4. In a first step, one derives
∂(v, Y ) and ∂(L ◦V ) from Propositions 2 and 5. Since these two processes
have zero covariation and never jump together, this leads to the joint charac-
teristics ∂(v, Y, L ◦V ) in the same way as for (4.7). Applying Proposition 3
yields ∂(v, X).
□
The model (4.11) remains vague about how to choose the dependence
structure between Z and Y . Therefore, we consider the following more con-
crete special case of the above setup:
Xt = X0 + µt + LVt + UZt,
dVt = vt−dt,
dvt = (κ −λvt−)dt + dZt,
where κ ≥0, λ are constants and L, U, Z three independent L´evy processes.
The triplet of L is denoted by (bL, cL, F L) and Z is supposed to be a subor-
dinator which equals the sum of its jumps, i.e. with triplet (bZ, 0, F Z) where
bZ =

zF Z(dz). The triplets in (3.1) of the affine process (v, X) are of the
form
β0 =

κ + bZ
µ + bZE(U1)

,
γ0 = 0,
ϕ0(G) =

1G(z, x)P Uz(dx)F Z(dz),
β1 =
 −λ
bL

,
γ1 =
 0 0
0 cL

,
ϕ1(G) =

1G(0, x)ϕL(dx),
G ∈B2,
(β2, γ2, ϕ2) = (0, 0, 0) ,
where P Uθ denotes the law of Uθ for θ ∈R+. Since the structure of the
corresponding L´evy exponent ψ0 is less obvious in this case, we express it
explicitly in terms of the L´evy exponents ψL, ψU, ψZ of L, Z, U, respectively.
ψ0(u1, u2) = κu1 + µu2 + ψZ 
u1 + ψU(u2)

,
ψ1(u1, u2) = −λu1 + ψL(u2)
Proof. To determine the triplets (4.12), it remains to derive the joint charac-
teristics of ( *Z, *Y )t := (κt + Zt, µt + UZt). Note that ( *Zt −κt, *Yt −µt) = *U ◦Z
for the R2-valued L´evy process *Uθ = (θ, Uθ). Here, Proposition 5 cannot be
applied because the time change Z is not continuous. But [21], Theorem 30.1,
yields that *U ◦Z is a L´evy process with triplet (b*
U◦Z, 0, F *
U◦Z), where
b*
U◦Z =

bZ
bZE(U1)

,
F *
U◦Z(G) =

1G(z, x)P Uz(dx)F Z(dz),
G ∈B2.
Since

A Didactic Note on Affine Stochastic Volatility Models
365
E exp

u1 *Zt + u2 *Yt

= E

E

exp

u1(κt + Zt) + u2(µt + UZt)
 Z

= exp(u1κt + u2µt)E exp

u1Zt + ZtψU(u2)

= exp

t

κu1 + µu2 + ψZ 
u1 + ψU(u2)

,
the L´evy exponent of ( *Z, *Y ) is given by
ψ(*
Z,*
Y )(u1, u2) = κu1 + µu2 + ψZ(u1 + ψU(u2)).
The L´evy exponents ψ0, ψ1 follow now directly from (4.12).
□
To be more specific, assume that Uθ = ρ + σWθ for some Wiener process
W and constants ρ, σ, in which case ψU(u) = ρu + σ2
2 u. This means that,
conditionally on an upward move ∆v of the “volatility” process v, the log
asset price X exhibits a Gaussian jump with mean ρ∆v and variance σ2∆v.
For σ = 0 we are back in the setup of (4.7). For L, Z one may e.g. choose any
of the tried and tested processes in CGMY.
4.8 Further remarks
Ordinary versus stochastic exponential
In the literature, positive asset prices are modelled typically either as ordinary
or as stochastic exponential, i.e.
St = S0eXt = S0E( *
X)t.
Above, we considered the first representation in terms of X or, more precisely,
X + log(S0). In [16], the process *
X is called the exponential transform of X.
One can compute *
X from X and vice versa quite easily. It is well-known that
X is a L´evy process if and only if *
X is a L´evy process. A similar statement
holds for the affine SV models above, where the differential characteristics of
(v, X) (resp. (v(1), . . . , v(ν), v, X) in the BNS case) do not depend on Xt. By
applying Propositions 3 and 2 one observes in a straightforward manner that
(v, *
X) (resp. (v(1), . . . , v(ν), v, *
X)) is affine as well. However, for purposes of
estimation or option pricing it is often more convenient to work with X rather
than *
X.
Statistical versus risk-neutral modelling
Statistical estimators based on historical data yield parameters of the model
under the physical probability measure P. By contrast, option pricing and
calibration refers to expectations relative to some risk-neutral measure *P.
For both purposes, affine models offer considerable computational advantages.
Therefore one may wonder whether a given measure change preserves the

366
Jan Kallsen
affine structure. This can be checked quite easily with the help of Proposition
4. E.g., if X is a Rd-valued affine process and if, in (2.4), Ht(ω) is constant
and W(ω, t, x) depends only on x, then the affine structure carries over to *P.
Only the triplets in (3.1) have to be adapted accordingly.
Martingale property of the asset price
Suppose that the process X in the examples above denotes the logarithm of
a discounted asset price. If the model is set up under some “risk-neutral”
probability measure, one would like eX to be a martingale or at least a local
martingale. The latter property can be directly read from the characteristics.
If ∂X = (b, c, F), then eX is a local martingale if and only if EeX0 < ∞and
bt + ct
2 +

(ex −1 −h(x))Ft(dx) = 0,
t ∈R+,
(4.13)
(cf. [16], Theorems 2.19, 2.18). In the context of the affine SV processes (v, X)
in the previous examples (i.e., in particular, with ψ2 = 0), Expression (4.13)
equals
ψ0(0, 1) + ψ1(0, 1)vt.
Since vt is random, both ψ0(0, 1) and ψ1(0, 1) typically have to be 0 in order
for eX to be a local martingale.
It is a more delicate to decide whether eX is a true martingale. This holds
automatically if X is a L´evy process (cf. [14], Lemma 4.4). In the affine case
a sufficient condition can be derived from DFS.
Proposition 1. Let (v, X) be an affine SV process as in the previous examples
(and hence the conditions in Theorem 3.1 hold). Suppose that (0, 1) ∈U and
(0, 0) ∈U for an open convex set U ⊂C2 such that, for any u ∈U,
1. ψj(Re(u)) < ∞,
j = 0, 1,
2. there exists an U-valued solution Ψ (1,2)(·, u) on R+ to the initial value
problem (3.4).
If EeX0 < ∞and ψ0(0, 1) = 0 = ψ1(0, 1), then eX is a martingale.
Proof. From Lemmas 5.3, 6.5 and Theorem 2.16 in DFS it follows that (3.3)
holds also for λ = (0, −i), i.e.
E(eXs+t|Fs) = exp

Ψ 0(t, 0, 1) + Ψ 1(t, 0, 1)⊤(vs, Xs)

= eXs,
which yields the assertion.
□
The previous result carries over to the BNS case (v(1), . . . , v(ν), v, X) or to
more general affine situations. The point is to verify that exponential moments
can actually be calculated from (3.3).

A Didactic Note on Affine Stochastic Volatility Models
367
Observability of the volatility process
In the examples above we assumed implicitly that the affine process under
consideration as, e.g., (v, X) is adapted to the given filtration. In practice,
however, only the logarithmic asset price X but not the volatility process v
can be observed directly. Therefore, the canonical filtration of X would be a
natural choice. Fortunately, v is typically adapted to the latter if X is driven
by an infinite activity process. The intuitive reason is that one can recover
v in an almost sure fashion from X by observing the quadratic variation
of the continuous martingale part or by counting the jumps in the purely
discontinuous case (cf. e.g. [25], Theorem 1). This holds even in models with
leverage as e.g. (4.7) if the L´evy measure of L has considerably more mass
near the origin than the one of Z.
References
1. Barndorff-Nielsen O., Shephard N.: Non-Gaussian Ornstein-Uhlenbeck-based
models and some of their uses in financial economics.
Journal of the Royal
Statistical Society, Series B 63, 167–241 (2001)
2. Brockwell P.: Representations of continuous-time ARMA processes. Journal of
Applied Probability 41A, 375–382 (2004)
3. Carr P., Geman H., Madan D., Yor M.: Stochastic volatility for L´evy processes.
Mathematical Finance 13, 345–382 (2003)
4. Carr P., Madan D.: Option valuation using the fast Fourier transform. The
Journal of Computational Finance 2, 61–73 (1999)
5. Carr P., Wu L.: The finite moment log stable process and option pricing. The
Journal of Finance 58, 753–777 (2003)
6. Carr P., Wu L.: Time-changed L´evy processes and option pricing. Journal of
Financial Economics 71, 113–141 (2004)
7. Duffie D., Filipovic D., Schachermayer, W.: Affine processes and applications
in finance. The Annals of Applied Probability 13 984–1053 (2003)
8. Ethier S., Kurtz T.: Markov Processes. Characterization and Convergence. New
York: Wiley 1986
9. Goll T., Kallsen J.:
Optimal portfolios for logarithmic utility.
Stochastic
Processes and their Applications 89, 31–48 (2000)
10. Heston S.: A closed-form solution for options with stochastic volatilities with
applications to bond and currency options. The Review of Financial Studies 6,
327–343 (1993)
11. Jacod J.: Calcul Stochastique et Probl`emes de Martingales, volume 714 of Lecture
Notes in Mathematics. Berlin: Springer 1979
12. Jacod J., Shiryaev A.: Limit Theorems for Stochastic Processes. Berlin: Springer,
second edition 2003.
13. Jiang G., Knight J.: Estimation of continuous-time processes via the empirical
characteristic function. Journal of Business & Economic Statistics, 20, 198–212
(2002)
14. Kallsen J.: Optimal portfolios for exponential L´evy processes. Mathematical
Methods of Operations Research 51, 357–374 (2000)

368
Jan Kallsen
15. Kallsen J.:
σ-localization and σ-martingales.
Theory of Probability and Its
Applications 48, 152–163 (2004)
16. Kallsen J., Shiryaev A.: The cumulant process and Esscher’s change of measure.
Finance & Stochastics 6, 397–428 (2002)
17. Kallsen J., Shiryaev A.:
Time change representation of stochastic integrals.
Theory of Probability and Its Applications 46, 522–528 (2002)
18. Kl¨uppelberg C., Lindner A., Maller R.:
A continuous-time GARCH process
driven by a L´evy process: Stationarity and second order behaviour. Journal of
Applied Probability 41, 601–622 (2004)
19. Protter, P.: Stochastic Integration and Differential Equations. Berlin: Springer,
second edition 2004
20. Raible, S.: L´evy Processes in Finance: Theory, Numerics, and Empirical Facts.
Dissertation Universit¨at Freiburg 2000
21. Sato, K.:
L´evy Processes and Infinitely Divisible Distributions.
Cambridge:
Cambridge University Press 1999
22. Sch¨obel R., Zhu, J.: Stochastic volatility with an Ornstein-Uhlenbeck process:
An extension. European Finance Review, 3 23–46 (1999)
23. Shiryaev, A.: Essentials of Stochastic Finance. Singapore: World Scientific 1999
24. Stein E., Stein J.: Stock price distributions with stochastic volatility: An analytic
approach. The Review of Financial Studies 4, 727–752 (1991)
25. Winkel M.: The recovery problem for time-changed L´evy processes. Preprint
2001.
26. Yu J.: Empirical characteristic function estimation and its applications. Econo-
metric Reviews 23 93–123 (2004)

Uniform Optimal Transmission of Gaussian
Messages
Pavel K. KATYSHEV
Central Economics and Mathematics Institute & New Economic School,
Nakhimovskii pr. 47, Moscow.
pkatish@nes.ru
Summary. We consider the transmission of Gaussian processes through the white
Gaussian noise channel with the feedback, under a mean power constraint. The
existence of uniformly optimal coding and decoding is proved and the minimal mean
square error of reconstruction of the message is calculated. The main feature of the
schemes of transmission under consideration is the possibility at each time moment
of using the whole cumulative information on the transmitted process. It is shown
that the results of the paper generalize the results of previous works in this area.
Key words: white noise, Gaussian processes, optimal coding
Mathematics Subject Classification (2000): 60G35, 94A40
1 Introduction
Let θ be some Gaussian message that should be transmitted through the white
Gaussian noise channel with the feedback. Such a channel is modelled by the
stochastic differential equation
dξt = A(t, θ, ξ)dt + dwt, ξ0 = 0, t ∈[0, T],
(1.1)
where A(t, θ, ξ) and ξt are the input and output signals at time moment t
respectively, w is a Wiener process (white noise) independent of θ. The func-
tion A is called a coding function. At time r ∈[0, T] the reconstruction of
the message θ using the observations ξ[0, r] = {ξs, 0 ≤s ≤r} is made by
means of some function θ(r, ξ[0, r]), the decoding function. Let also ∆(A, θ; r)
be a function that measures (for given coding A and decoding θ) the error of
reconstruction of initial message θ at time r. Then the general problem of op-
timal transmission may be formulated as follows: calculate the minimal error
infA,θ ∆(A, θ; r) = ∆(r) and find the optimal (or ε-optimal) coding and de-
coding functions. Obviously, in order to solve this problem we have to specify

370
P. K. Katyshev
the nature of the message θ and the constraints imposed on the coding and de-
coding functions. In this paper we suppose that θ is a Gaussian process, and
the coding A satisfies (besides some regularity conditions) the mean power
constraint:
EA2(t, θ, ξ) ≤P,
(1.2)
where P > 0 is some constant.
Ihara [1] proved that if θ is a Gaussian random variable with variance
γ and ∆(A, θ; r) = E

θ −θ(r, ξ[0, r])
2
then ∆(A, θ; r) ≥γe−P r and there
exists an optimal transmission scheme. In [2] a similar result was obtained
for the case when θ is a Gaussian random vector and ∆(A, θ; r) is the sum of
mean square errors of its components.
The problem of transmission of Gaussian and Markovian process θ satis-
fying the stochastic differential equation
dθt = a(t)θtdt + b(t)dvt,
where a and b are non random functions and v is a Wiener process independent
on w, was considered in [3]. It was supposed that
∆(A, θ; r) = E

θr −θ(r, ξ[0, r])
2
and the coding function A at each time moment t depends on θt. The results
of the work [3] were generalized in [4]. In that paper it was assumed that θ
is an arbitrary Gaussian and Markovian process with continuous correlation
function and coding A at each time moment t may depend on the whole
“history” θ[0, t] = {θs, 0 ≤s ≤t} of the process θ.
It is worth noting that basically the coding and decoding functions mini-
mizing the error ∆(A, θ; r) at time r may depend on r. But all optimal coding
and decoding functions obtained in the works mentioned above do not depend
on r. It is natural to call such functions uniform (on r) optimal coding and de-
coding. It was shown ([5]) that uniform optimal coding of Gaussian messages
may not exist.
In this paper we suggest a general scheme of transmission and prove the
existence of a uniform optimal coding and decoding functions. The main the-
orem of the paper generalizes the results obtained in [1–4].
The basis of the proposed scheme is the following. Let a random variable
ζ and a stochastic process θ = {θt, t ∈[0, T]} be such that (ζ, θ) is a Gaussian
system. It is supposed that the coding function A at each time moment t may
depend on the whole “history” θ[0, t] = {θs, 0 ≤s ≤t} of the process θ up to
t. The error function is
∆(A, θ; r) = E

ζ −θ(r, ξ[0, r])
2
.
In other words, the random variable ζ is not “observed” and only the process
θ can be used in the coding A. We find the minimal mean square error and

Uniform Optimal Transmission of Gaussian Messages
371
prove the existence of uniform optimal coding and decoding functions. It may
be easily verified that the proposed scheme includes all models considered in
the works [1], [3] and [4].
2 The formulation of the problem and main result
Let θ = {θt, t ∈[0, T]} be a measurable Gaussian process with trajectories
belonging to the measurable space (L2
T , L2
T ) of square integrable functions
g = {gt, t ∈[0, T]} with the σ-field L2
T generated by the cylindrical sets. Let
also ζ be a random variable such that (ζ, {θt, t ∈[0, T]}) is a Gaussian system.
Without loss of generality we may assume that E(ζ) = E(θt) = 0. Suppose
that continuous stochastic process ξ = {ξt, t ∈[0, T]} satisfies the equation
(1.1) where w = {wt, t ∈[0, T]} is a standard Wiener process independent of
(ζ, θ).
Now we define the set of admissible coding functions A. Let’s denote by
(CT , CT ) the measurable space of continuous functions x = {xt, t ∈[0, T]}
with Borel σ-field CT . Let also
Ct = σ{xs, 0 ≤s ≤t},
L2
t = σ{gs, 0 ≤s ≤t}
be the σ-fields in the spaces CT and L2
T respectively generated by the values
of functions up to time moment t. By BT we denote the Borel σ-field of [0, T].
Definition 1. A function A( · , · , · ) in equation (1.1) is called an admissi-
ble coding function (or simply coding) if the following conditions are fulfilled:
1) It is defined on the space ([0, T], BT )⊗(L2
T , L2
T )⊗(CT , CT ) and is jointly
measurable.
2) For any t ∈[0, T] the function A(t, · , · ) is L2
t ⊗Ct-measurable.
3) For any Gaussian process θ = {θt, t ∈[0, T]} with trajectories from
L2
T the equation (1.1) has a continuous strong solution ξ = {ξt, t ∈[0, T]}
on [0, T], i.e. for each t ∈[0, T] the random variable ξt is Fθ,w
t
–measurable,
where Fθ,w
t
= σ {θu, ws, 0 ≤u, s ≤t}, or equivalently Fξ
t ⊆Fθ,w
t
, where
Fξ
t = σ {ξs, 0 ≤s ≤t}.
4) Let {θn, n = 1, 2, ...} be a sequence of Gaussian processes with trajec-
tories from L2
T such that E (θn
t −θt)2 →0 as n →∞uniformly in t ∈[0, T]
and let ξn be the solution of the equation
dξn
t = A(t, θn, ξn)dt + dwt,
ξn
0 = 0,
t ∈[0, T].
(2.1)
Then E (ξn
t −ξt)2 →0 and EA2(t, θn, ξn) →EA2(t, θ, ξ) as n →∞uniformly
in t ∈[0, T].
5) For each time t ∈[0, T] the mean power constraint (1.2) holds.

372
P. K. Katyshev
Remarks.
1. It is known (see, for example, [6, Ch. 1]) that if the correlation function
of the process θ is continuous then almost all trajectories of the process θ
belong to L2
T .
2. According to condition 2) any admissible coding A is a non-anticipative
function with respect both to θ and ξ. It means that all successive information
on θ can be used in coding and that there is an instantaneous and noiseless
feedback in the channel.
3. It can be shown ([7, Ch.4]) that the conditions 3) and 4) are fulfilled if
function A satisfies the integral Lipschitz condition
|A(t, g, x) −A(t, h, y)|2 ≤N1


t

0
|gs −hs|2 ds +
t

0
|xs −ys|2 dK(s)


+ N2
)
|gt −ht|2 + |xt −yt|2
,
and has linear growth
A2(t, g, x) ≤N1


t

0
(1 + gs)2ds +
t

0
(1 + xs)2dK(s)

+ N2(1 + g2
t + x2
t),
where N1, N2 are positive constants and K(s) is a non decreasing right con-
tinuous function, 0 ≤K(s) ≤1, g, h ∈L2
T , x, y ∈CT .
Conditions 3) and 4) are also fulfilled if equation (1.1) has the following
form:
dξt = ft

θt −
t

0
ϕ(s, t)dξs

dt + dwt, ξ0 = 0,
where f and ϕ are non random and continuous functions ([8]).
Let us denote by A the set of all admissible coding functions.
Definition 2. A function θ( · , · ) defined on the product of the spaces
([0, T], BT ) ⊗(CT , CT ) is called an admissible decoding function (or sim-
ply decoding) if for each t ∈[0, T] function θ(t, · ) is Ct–measurable and
E θ2(t, ξ) < ∞for each A ∈A.
We denote by D the set of all admissible decoding functions.
For any A ∈A and θ ∈D let us denote ∆(A, θ; r) = E

ζ −θ(r, ξ)
2
and
∆(r) = inf{∆(A, θ; r): A ∈A, θ ∈D}. The function ∆(r) is the minimal
mean square error of reconstruction of the message ζ at time moment r.
Functions A∗∈A,
θ∗∈D, for which ∆(A∗, θ∗; r) = ∆(r) are called optimal
coding and decoding functions (at time moment r).
Let A ∈A, θ ∈D and let ξ be a corresponding solution of the equation
(1.1). Put
Fθ
t = σ(θs, 0 ≤s ≤t},
mt(ζ) = E

ζ | Fξ
t

.

Uniform Optimal Transmission of Gaussian Messages
373
Since ∆(A, θ; r) ≥∆(A; r) ≡E (ζ −mr(ζ))2 for any θ ∈D,
∆(r) = inf{∆(A; r): A ∈A}.
So the optimal decoding function is a conditional mean. Therefore, the main
problem is to find the optimal coding function. Basically, even if the optimal
coding exists for given r, it may depend on this r. If we can find coding
function that is optimal for any r then we call it uniform optimal coding:
Definition 3. A function A∗∈A is called the uniform optimal coding if
∆(A∗; r) = ∆(r) for any r ∈[0, T].
Finally, let us denote ηt = E

ζ
Fθ
t

, λt = ζ −ηt and γ(t) = Eη2
t . Since
the process η is a (Gaussian) martingale its increments are uncorrelated and
therefore γ(t) is a non decreasing function. Let also z = inf{t ≤T : γ(t) > 0}
and z = T if γ(t) = 0 for any t ∈[0, T]. Obviously if γ(t) = 0 then the random
variable ζ and σ-field Fθ
t are independent.
The main result of the paper is the following theorem.
Theorem. Let the following conditions hold:
(1) The correlation function of the process θ is continuous on [0, T] × [0, T];
(2) The function γ(t) is continuous on [0, T].
Then:
(a)
∆(r) = γ(r) −P
r

0
γ(s) exp [−P(r −s)] ds + Eλ2
r,
r ∈[0, T],
(2.2)
where P is the bound in (1.2).
(b) There exists a uniform optimal coding function A∗∈A. The correspond-
ing process ξ∗satisfies the stochastic differential equation
dξ∗
t = ft

ηt −
t

0
ϕ(s, t)dξ∗
s

dt + dwt,
ξ∗
0 = 0,
(2.3)
where the functions ft and ϕ(s, t) are non random functions, ϕ(s, t) = 0 for
0 ≤s ≤t ≤z,
T
0
T
0
ϕ2(s, t) ds dt < ∞and
t

0
ϕ(s, t) dξ∗
s = E

ηt
Fξ∗
t

≡m∗
t (η),
(2.4)
f 2
t E (ηt −m∗
t (η))2 = P,
t > z.
(2.5)
In order to prove this theorem we need some preliminary results.

374
P. K. Katyshev
3 Auxiliary results
Let (Ω, F, P) be a complete probability space. Suppose that there is a filtra-
tion {Ft ⊆F, t ∈[0, T]} in it. Let us assume that A = {(At, Ft), t ∈[0, T]}
is a measurable stochastic process such that
T
0
E

A2
t

dt < ∞. Define the
process ξ = {(ξt, Ft), t ∈[0, T]} by the formula
ξt =
t

0
As ds + wt,
where w = {(wt, Ft), t ∈[0, T]} is a standard Wiener process. Let also θ be a
random element (defined on (Ω, F, P)) with values in some measurable space
(Y, Y). Suppose that Fθ = σ(θ) ⊆F0 (it means in particular that θ and w
are independent).
Lemma 1 ([4, 9]). Let us assume that there exists a regular conditional
distribution on F with respect to θ, i. e. there exists a function p(ω, F), ω ∈Ω,
F ∈F such that (i) p(ω, ·) is a probability measure on F for any ω ∈Ω; (ii)
p(ω, F) = P

F
Fθ 
(ω) P–a.s. for any F ∈F.
Then
I(θ, ξ) = 1
2
T

0
E

A
2
t −A
2
t

dt = 1
2
T

0
E

At −At
2
dt,
where I(θ, ξ) is a mutual information of the random elements θ and ξ,
At = E

At
Fθ,ξ
t

,
At = E

At
Fξ
t

,
Fθ,ξ
t
= σ

Fθ, Fξ
t

.
Remark. When At = A (t, θ, ξ[0, t]), i.e when the random variable At is
Fθ,ξ
t
–measurable for each t, this result is obtained in [10].
Henceforth we shall denote by I(x, y) the mutual information of two ran-
dom elements x and y.
Lemma 2 ([1]). Let θ be a Gaussian random variable and let ψ be some
other random variable with Eψ2 < ∞. Then E(θ−ψ)2 ≥V(θ) exp [−2I(θ, ψ)],
where V(θ) is a variance of θ.
Consider now the situation when θ is a piecewise constant process, namely,
suppose that there is a partition 0 = t0 < t1 < ... < tn−1 < tn = T of the time
interval [0, T] and a Gaussian random vector (θ1, θ2, ..., θn) such that θt = θi
if ti−1 < t ≤ti,
i = 1, ..., n,
θ0 = θ1. In this case any admissible coding A
at time t depends on (θ1, ..., θi) if ti−1 < t ≤ti, i = 1, ..., n. Denote
ηi = E (ζ |θ1, ..., θi ) ,
i = 1, ..., n;
R = ζ −ηn;
ε1 = η1,
εi = ηi −ηi−1,
i = 2, ..., n;
δi = Eε2
i ,
d = ER2

Uniform Optimal Transmission of Gaussian Messages
375
(recall that Eθi = Eζ = 0). Here ηi, εi are Gaussian random variables, εi and
εj are independent if i ̸= j, and the random variable εi does not depend on
(θ1, ..., θi−1), i ≥2. Moreover, the random variable R does not depend on the
random vector (θ1, θ2, ..., θn). Clearly,
ηi =
i

k=1
εk, i = 1, ..., n,
ζ =
n

k=1
εk + R.
(3.1)
Let A be some admissible coding and let ξ = {ξt, t ∈[0, T]} be the
corresponding solution of the equation (1.1). Let us denote
mt(ηi) = E

ηi
Fξ
t

,
mt(εi) = E

εi
Fξ
t

, i = 1, ..., n.
Lemma 3. For any admissible coding A and for each k = 0, ..., n −1 the
following inequality holds:
V(ηk+1) exp (−2I(ηk+1, ξ[0, tk])) ≥δ1 exp (−Ptk)
+ δ2 exp (−P(tk −t1)) + ... + δk exp (−P(tk −tk−1)) + δk+1.
(3.2)
Proof. For k = 0 the inequality (3.2) obviously holds. Let k ≥1.
It is known (see, for example [7]), that the a posteriori
distribution
P

ηk+1 ≤x
Fξ
tk

has the density πk(x) =
d
dxP

ηk+1 ≤x
Fξ
tk

. Let us de-
note by pk(x) the (a priori) density of the random variable ηk+1. Then the
mutual information I (ηk+1, ξ[0, tk]) can be represented as follows:
I (ηk+1, ξ[0, tk]) = H(ηk+1) −Hk(ηk+1),
(3.3)
where H(ηk+1) = E ln pk(ηk+1) is the entropy and
Hk(ηk+1) = E ln πk(ηk+1)
is the conditional entropy of the random variable ηk+1. Since equation (1.1)
has a strong solution, Fξ
tk ⊆σ

Fw
tk, θ1, ..., θk

. Moreover, the random variable
εk+1 does not depend on w and θ1, ..., θk and, therefore, the pair (ηk, ξ[0, tk])
and εk+1 are independent. In [11] it is proven that in this case the following
inequality holds:
e2Hk(ηk+1) = e2Hk(ηk+εk+1) ≥e2Hk(ηk) + e2Hk(εk+1)
= e2Hk(ηk) + e2H(εk+1).
(3.4)
From (3.3) and (3.4) we get that
V(ηk+1) exp (−2I(ηk+1, ξ[0, tk])) = V(ηk+1)e2Hk(ηk+1)−2H(ηk+1)
≥V(ηk+1)
)
e2Hk(ηk+1) + e2H(ηk+1)
[2πeV(ηk+1)]−1
= (2πe)−1 )
e2H(ηk)e2Hk(ηk)−2H(ηk) + 2πeδk+1

= V(ηk+1) exp (−2I(ηk, ξ[0, tk])) + δk+1.
(3.5)

376
P. K. Katyshev
By virtue of Lemma 1 we have
I(ηk, ξ[0, tk]) = 1
2
tk−1

0
E

A
2
s −A
2
s

ds + 1
2
tk

tk−1
E

A
2
s −A
2
s

ds,
where As = E

As
Fθ,ξ
s

, As = E

As
Fξ
s

. Thus, from (3.5) we get:
V(ηk+1) exp (−2I(ηk+1, ξ[0, tk]))
≥V(ηk) exp (−2I(ηk, ξ[0, tk−1])) e−P (tk−tk−1) + δk+1,
since EA
2
s ≤EA2
s ≤P,
EA
2
s ≥0. Induction completes the proof of the
lemma.
Lemma 4. For any admissible coding function A the following inequality
holds:
∆(A; r) ≥δ1e−P r +δ2e−P (r−t1) +...+δie−P (r−ti−1) +δi+1 +...+δn +d (3.6)
for ti−1 < r ≤ti, i = 1, ..., n.. In particular,
∆(A; T) ≥δ1e−P T + δ2e−P (T −t1) + ... + δne−P (T −tn−1) + d.
(3.7)
Proof. Let A ∈A and ti−1 < r ≤ti. Due to (3.1) we have that
ζ = ηi + εi+1 + ... + εn + R
and, hence,
mr(ζ) = mr(ηi) + mr(εi+1) + ... + mr(εn) + mr(R).
Recall that that the random variables εj, j = i + 1, ..., n, R and σ-field Fξ
r
are independent, therefore, mr(ζ) = mr(ηi) and
∆(A; r) = E (ζ −mr(ζ))2 = E (ηi −mr(ηi))2 + δi+1 + ... + δn + d.
Using Lemmas 1, 2 and well-known properties of mutual information we get
that
E (ηi −mr(ηi))2 ≥V(ηi) exp (−2I(ηi, mr(ηi))
≥V(ηi) exp (−2I(ηi, ξ[0, r]) ≥V(ηi) exp (−2I(ηi, ξ[0, ti−1]) e−P (r−ti−1).
Finally, applying Lemma 3 we get the inequality (3.6).
Remark. It can be shown that there exists admissible coding function A∗
for which the relation (3.6) holds as an equality.

Uniform Optimal Transmission of Gaussian Messages
377
4 The proof of theorem
Let A be some admissible coding function and let ξ be the corresponding
solution of the equation (1.1). Let us denote ηt = E

ζ
Fθ
t

, fix r ∈[0, T] and
put λr = ζ −ηr. Clearly, the Gaussian random variable λr does not depend
on σ-field Fθ
r . Moreover λr and Fw
r are obviously independent. Since Fθ
r and
Fw
r are also independent this implies that λr does not depend on Fθ,w
r
. By
virtue of condition 3 from Definition 1 it follows that λr does not depend on
σ-field Fξ
r . Therefore,
mr(ζ) = E

ζ
Fξ
r

= E

ηr
Fξ
r

+ E

λr
Fξ
r

= E

ηr
Fξ
r

+ E (λr) = mr(η)
and
∆(A; r) = E (ζ −mr(ζ))2 = E (ηr + λr −mr(η))2
= E (ηr −mr(η))2 + Eλ2
r.
(4.1)
Note that the value of Eλ2
r does not depend on the coding function A.
Confine now the time interval to [0, r] and for each n = 1, 2, ... define piece
wise constant process θn: θn
t = θ ir
n if (i−1)r
n
< t ≤ir
n , i = 1, ..., n, θn
0 = θ r
n .
Let {ξn
t , 0 ≤t ≤r}, n = 1, 2, ..., be a sequence of solutions of equation
(2.1). The correlation function of the process θ is continuous and, therefore,
E (θn
t −θt)2 →0 as n →∞uniformly on t ∈[0, r]. So, the condition 4 from
Definition 1 implies that
E (ξn
t −ξt)2 →0,
EA2(t, θn, ξn) →EA2(t, θ, ξ)
as n →∞uniformly in t ∈[0, r]. This easily implies that there exists the
sequence of numbers {Pn, n = 1, 2, ...} such that
EA2(t, θn, ξn) ≤Pn,
lim
n→∞Pn = P.
(4.2)
Denote ηn
t = E

ζ
Fθn
t

, mn
t (η) = E

ηn
t
Fξn
t

and γn(t) = E (ηn
t )2. Using
Lemma 4 with ζ = ηr and T = r we get that
E (ηr −mn
r (η))2 ≥
n

i=1
δn
i exp

−Pn

r −i −1
n
r

,
(4.3)
where
δn
i = E
)
E

ηr
θ r
n , ..., θ ir
n

−E

ηr
θ r
n , ..., θ (i−1)r
n
2
= E
)
E

ηr
θ r
n , ..., θ ir
n
2
−E
)
E

ηr
θ r
n , ..., θ (i−1)r
n
2
= E
)
E

ζ
Fθn
ir
n
2
−E
)
E

ζ
Fθn
(i−1)r
n
2
= γn
ir
n

−γn
(i −1)r
n

,
i ≥2,
δn
1 = γn  r
n

.

378
P. K. Katyshev
Hence, the inequality (4.3) can be rewritten as follows:
E (ηr −mn
r (η))2 ≥
n

i=1

γn
ir
n

−γn
(i −1)r
n

× exp

−Pn

r −i −1
n
r

.
Making routine calculations we get that
E (ηr −mn
r (η))2 ≥γn(r) exp

−Pnr
n

+
n

i=1
γn
ir
n
 
exp

−Pn

r −(i −1)r
n

−exp

−Pn

r −ir
n

= γn(r) exp

−Pnr
n

−
n

i=1
γn
ir
n

exp

−Pn

r −ir
n
 Pnr
n
+ αn,
(4.4)
where αn →0 as n →∞because the functions γn(t) and exp(Pnt) are
uniformly bounded on interval [0, r]. (Here we use the elementary formula
eb −ea = ea(b −a) + o(b −a).) Now take the sub-sequence {nk, k = 1, 2, ...}
such that Fθnk
t
⊆Fθnk+1
t
for each t ∈[0, r] (for example, we can take the
subsequence of binary rational partitions of the time interval [0, r]). We do
not complicate notations and (without loss of generality) may assume that
Fθn
t
⊆Fθn+1
t
.
Since Fθn
t
↑Fθ
t for each t ∈[0, r], by the L´evy theorem we have that
almost surely
E

ζ
Fθn
t

→E

ζ
Fθ
t

= ηt as n →∞.
(4.5)
The (ζ, θ) is a Gaussian system, therefore, the a.s.–convergence implies the
L2-convergence (see, for example [6]), so from (4.5) we get that
γn(t) →γ(t) = Eη2
t as n →∞
(4.6)
for each t ∈[0, r].
Let us consider the function
gn(t) = Pn exp

−Pn

r −ir
n

, if (i −1)r
n
< t ≤ir
n ,
i = 1, ..., n.
By virtue of (4.2) we have that
gn(t) →P exp (−P(r −t)) as n →∞
(4.7)
for each t ∈[0, r].

Uniform Optimal Transmission of Gaussian Messages
379
Now consider the second term in the right-hand side of (4.4). Clearly,
n

i=1
γn
ir
n

Pn exp

−Pn

r −ir
n
 r
n =
 r
0
γn(s)gn(s)ds.
Finally, we get that
E (ηr −mn
r (η))2 ≥γn(r) exp

−Pnr
n

−
 r
0
γn(s)gn(s)ds.
(4.8)
It is easily seen that γn(t)gn(t) →γ(t)g(t) = γ(t)P exp (−P(r −t)) as
n →∞and |γn(t)gn(t)| ≤C for all n and t ∈[0, r]. So, by the Lebesgue
theorem
lim
n→∞

γn(r) exp

−Pnr
n

−
 r
0
γn(s)gn(s)ds

= γ(r) −P
 r
0
γ(s) exp(−P(r −s))ds.
(4.9)
We cannot directly take the limit of the left hand side of (4.8). Neverthe-
less, we can show that
E (ηr −mr(η))2 ≥γ(r) −P
 r
0
γ(s) exp(−P(r −s))ds.
In order to prove this inequality we construct a set of Fξn
r -measurable random
variables βn,N,k such that
lim
k→∞lim
N→∞lim
n→∞E (βn,N,k −mr(η))2 = 0.
(4.10)
Let (R∞, B∞) be the measurable space of countable sequences. Then there
is a sequence {ri ≤r, i = 1, 2, . . . }, and B∞-measurable function G such that
mr(η) = E

ηr
Fξ
r

= G(ξr1, ξr2, . . . ). Now select a Bk-measurable function
F (depending on k) such that E (ηr |ξr1, . . . , ξrk ) = F (ξr1, . . . , ξrk). Let us
denote by µk the measure in the space Rk generated by the random vector
(ξr1, . . . , ξrk). Using the Luzin theorem we find functions FN(y), y ∈Rk,
N = 1, 2, . . . , with the following properties:
1) each function FN(y) is continuous and bounded in Rk;
2) FN(y) →F(y) µk-a.s., N →∞;
3) EF 4
N (ξr1, . . . , ξrk) ≤EF 4 (ξr1, . . . , ξrk) + 1 for every N.
Note that EF 4 (ξr1, . . . , ξrk) = E [E(ηr|ξr1, . . . , ξrk)]4 ≤E(ηr)4 ≤const. From
2) and 3) it follows that
lim
N→∞E |FN(ξr1, . . . , ξrk) −F(ξr1, . . . , ξrk)|2 = 0.
(4.11)
Put now βn,N,k = FN(ξn
r1, . . . , ξn
rk) and verify the validity of (4.10). Since
E (ξn
t −ξt)2 →0 as n →∞uniformly in t ∈[0, r], we may assume that
ξn
ri →ξri P–a.s. as n →∞. Therefore,

380
P. K. Katyshev
lim
n→∞E
mr(η) −FN(ξn
r1, . . . , ξn
rk)
2 = E |mr(η) −FN(ξr1, . . . , ξrk)|2
(4.12)
since the functions FN(y) are bounded and continuous. Then, using (4.11),
we infer that
lim
N→∞lim
n→∞E
mr(η) −FN(ξn
r1, . . . , ξn
rk)
2
= lim
N→∞E |mr(η) −FN(ξr1, . . . , ξrk)|2 = E |mr(η) −F(ξr1, . . . , ξrk)|2 .
(4.13)
Due to the L´evy theorem
lim
k→∞F(ξr1, . . . , ξrk) = mr(η)
P–a.s.
(4.14)
Since Em4
r(η) ≤C < ∞and EF 4(ξr1, . . . , ξrk) ≤C < ∞, the set of random
variables {|mr(η) −F(ξr1, . . . , ξrk)|2 , k = 1, 2, . . . } is uniformly integrable
and because of (4.14) we have
lim
k→∞E |mr(η) −F(ξr1, . . . , ξrk)|2 = 0.
(4.15)
So, the inequality (4.10) follows from (4.12), (4.13), and (4.15).
Since the random variables βn,N,k are Fξn
r –measurable for every n,
E (ηr −βn,N,k)2 ≥E (ηr −mn
r (η))2 ,
and from (4.8), (4.9), (4.10) it follows that
E (ηr −mr(η))2 ≥γ(r) −P
 r
0
γ(s) exp(−P(r −s))ds
Finally, from (4.1) we get that
∆(A; r) ≥γ(r) −P
 r
0
γ(s) exp(−P(r −s))ds + Eλ2
r
(4.16)
for any admissible coding function A.
Now we construct the admissible coding A∗for which (4.16) holds with
the equality. Put
h(t) = γ(t) −P
 t
0
γ(s) exp(−P(t −s))ds.
Since γ is a nondecreasing function,
h(t) ≥γ(t) −P γ(t)
 t
0
exp(−P(t −s))ds = γ(t)e−P t,

Uniform Optimal Transmission of Gaussian Messages
381
and if t > z then h(t) > 0 (recall that z = inf{t ≤T : γ(t) > 0}). There-
fore, we can define the function ft =
H
P
h(t) for t > z, ft = 0 for t ≤z,
and the process vt =
 t
0 fsηsds + wt. Denote mv
t (η) = E (ηt |Fv
t ) ,
nt =
E (ηt −mv
t (η))2. It is proven in [12] that the function nt satisfies the follow-
ing equation:
nt = γ(t) −
 t
0
f 2
s n2
s ds.
By direct calculation we check that the function nt = h(t) is a solution of this
equation.
It is shown in [13] that there exists a non random function ϕ(s, t) and a
process {µt, t ∈[0, T]} such that
dµt = ft

ηt −
 t
0
ϕ(s, t) dµs

dt + dwt,
(4.17)
and
 t
0
ϕ(s, t) dµs = E (ηt |Fµ
t ) ≡mµ
t (η).
In [13] it is also shown that Fv
t = Fµ
t for each t ∈[0, T]. Then
E (ηt −mµ
t (η))2 = Eη2
t −E (mµ
t (η))2 = Eη2
t −E (mv
t (η))2
= E (ηt −mµ
t (η))2 = h(t)
and
E

ft

ηt −
 t
0
ϕ(s, t) dµs
2
= f 2
t E (ηt −mµ
t (η))2 = f 2
t h(t) = P.
So, the scheme of transmission (4.17) is admissible and for it the relationship
(4.16) holds with the equality sign.
Finally, since the scheme (4.17) does not depend on r, it is uniformly
optimal.
The theorem is proven.
This theorem helps to obtain the uniform optimal scheme of the trans-
mission of Gaussian Markov processes and to calculate the minimum mean
square error ∆(r).
5 Transmission of Gaussian Markov processes
Suppose now that θ = {θt, t ∈[0, T]} is a Gaussian Markov process with
continuous correlation function Γ(s, t). Let the process ξ = {ξt, t ∈[0, T]}
satisfies the equation (1.1) with some admissible coding function A. Let us

382
P. K. Katyshev
denote mt = E

θt
Fξ
t

and suppose that ∆(A; r) = E (θr −mr)2. Using the
theorem we may obtain the following result.
Corollary. Let the correlation function Γ(s, t) of the process θ be contin-
uous in [0, T] × [0, T] and Γ(t, t) ̸= 0 for all t ∈[0, T]. Then:
1) ∆(r) = Γ(r, r) −P
 r
0
Γ 2(r,s)
Γ (s,s) e−P (r−s)ds.
2) There exists an uniformly optimal coding function A∗such that the
corresponding process ξ∗satisfies the equation
dξ∗
t =
>
P
∆(t) (θt −m∗
t ) dt + dwt, ξ∗
0 = 0,
(5.1)
where m∗
t = E

θt
Fξ∗
t

.
3) There is a non random function g(s, t), s, t ∈[0, T], s ≤t, such that
 T
0
 T
0
g2(s, t) ds dt < ∞,
m∗
t =
 t
0
g(s, t) dξ∗
s,
and g(s, t) satisfies the Wiener–Hopf equation
Γ(s, t) −
 s
0
g(u, s)g(u, t)du =

∆(s)
P
g(s, t).
(5.2)
(The equation (5.1) means that the optimal coding function at each time t
depends only on θt and does not use the past values of the process θ.)
Proof. 1), 2) Let A be any admissible coding function. Fix some time
r ∈[0, T] and use the theorem with ζ = θr. Since the process θ is a Markov
process,
ηt = E

θr
Fθ
t

= E (θr |θt ) = Γ(r, t)
Γ(t, t) θt, γ(t) = Eη2
t = Γ 2(r, t)
Γ(t, t) .
Obviously λr = 0. Therefore, from (4.16) it follows that
∆(A; r) ≥∆(r) = Γ(r, r) −P
 r
0
Γ 2(r, s)
Γ(s, s) e−P (r−s)ds.
(5.3)
The optimal scheme of transmission (4.17) has the form (5.1) in this case
and the relationship (5.3) holds for it with equality. Since the corresponding
coding function does not depend on r, it is uniformly optimal.
3) The existence of the function g(s, t) follows directly from the proof of
the theorem. It is easily seen that the equation
E

θt
 t
0
f(s, t) dξ∗
s

= E

m∗
t
 t
0
f(s, t) dξ∗
s

holds for each bounded measurable function f(s, t), and the process ξ∗is a
Wiener process because it coincides with its innovation process (see [7, Ch.
7]). These facts directly imply the equation (5.2). Corollary is proven.

Uniform Optimal Transmission of Gaussian Messages
383
6 Conclusions
It may be easily checked that the theorem generalizes the results of the works
[1, 3, 4].
It was mentioned above that in some models the uniformly optimal scheme
does not exist. The results of this work allow us to make the hypothesis
that the existence of uniform optimal scheme is strongly connected with the
possibility to accumulate the information on the process θ and to use at each
time t the whole “history” of the process up to time t.
References
1. Ihara S.: Optimal coding in white Gaussian channel with feedback. Lecture
Notes Math., 330, 120–123.
2. Katyshev P.K.: Transmission of Gaussian vector through the channel with the
noiseless feedback. Probability Theory and its Applications, 20, N 1, 188–196
(1975)
3. Liptser R.Sh.: Optimal coding and decoding functions in transmissions of
Gaussian Markovian process through the channel with the noiseless feedback.
Problems of Transmission of Information, 10, N 4, 3–15 (1974)
4. Katyshev P.K.: On some problem of the control of stochastic process in infor-
mation theory. In: Stochastic processes and control. Moscow, “Nauka”, 75–93
(1978)
5. Katyshev P.K.: On uniformly optimal coding of Gaussian messages in white
Gaussian channels with feedback. In: New Trends in Probability and Statistics,
Eds. V. Sazonov, T. Shervashidze, Moscow, 436–444 (1991)
6. Ibraghimov I.A. and Rozanov Yu.A.: Gaussian Random Processes. Moscow,
“Nauka” (1970)
7. Liptser R.Sh. and Shiryaev A.N.: Statistics of Stochastic Processes. Moscow,
“Nauka” (1974)
8. Ihara S.: Coding theory in Gaussian channel with feedback II: Evaluation of the
filtering error. Nagoya Mathematical Journal, 58, 127–147 (1975)
9. Glonti O.A.: On a mutual information of the signals in transmission through the
channel with “noisy” feedback. Probability Theory and its Applications, 23, N
2, 395–397 (1978).
10. Kadota T., Zakai M., Ziv J.: Mutual information in white Gaussian channel
with feedback. IEEE, Trans. on Inf. Th., IT-17, 4, 368–371 ( 1971).
11. Blachman N.M.: The convolution inequality for entropy powers. IEEE, Trans.
on Inf. Th., IT-12, 2, 267–270 (1965)
12. Liptser R.Sh.: Gaussian martingales and generalization of the Kalman–Bucy
filter. Probability Theory and its Applications, 20, N 2, 292–308 (1975)
13. Ihara S.: Coding theory in white Gaussian channel with feedback. Journal of
Multivariate Analysis, 5, N 1, 106–118 (1975)


A Note on the Brownian Motion
Kiyoshi KAWAZU
Department of Mathematics, Faculty of Education, Yamaguchi University,
Yamaguchi 753-8513, Japan.
kawazu@yamaguchi-u.ac.jp
Summary. This is a discussion about the exceptional role of the Brownian motion
in the theory of stochastic processes and their applications.
Key words: Brownian motion, hitting time, distribution of bottom
Mathematics Subject Classification (2000): 60J60, 60J65
1 Introduction
The First Soviet–Japan Symposium on Probability Theory (Khabarovsk, Rus-
sia, 1969) was an important event in the author’s professional life. The variety
of topics discussed and the reported results were so impressive that the author
was convinced that the basic of stochastic processes is ruled by the Brownian
motion {B(t), t ≥0}.
For example, the continuous state branching process with immigration,
studied in [13], can be represented in a differential form as follows:
dXt = a

Xt dB(t) + h(Xt) dt,
t ≥0,
X0 > 0.
The Sinai’s Random Walk [16] had astonished many researchers in the area
of stochastic processes and theoretical physics. Sinai succeeded to change the
imagination of mathematicians and confirm a real phenomenon in physics.
Brox [2] has found out the mechanism. It is the Brownian motion. It is well-
known, that
dXt = dB(t) + 1
2W ′(Xt) dt,
t ≥0,
where {W(x), x ∈R} is a Brownian motion independent of {B(t), t ≥0}.
This process {Xt, t ≥0} is called a diffusion process in random environ-
ment. By using Brownian motion properties, Brox showed that for large t,
the process Xt behaves like log2 t. Notice, it is not of order
√
t. Kesten, [14],

386
K. Kawazu
found the limit distribution of Xt as t →∞by analyzing the Brownian paths,
see also [8] and [9].
The Brownian motion {B(t), t ≥0} is associated with many strange
phenomena which has been fascinating many mathematicians. For example,
Ikeda [4] mentions details of research history of Brownian motion and some
charming points.
The great book by Itˆo and McKean [7] provides us with so wide world.
The book by Ikeda and Watanabe [5] contains exhaustive description for the
expectation of integral functionals of Brownian motion. The book by Revuz
and Yor [15] is full of results, many of them describing phenomena which
involve the Brownian motion. Another face of the Brownian motion can be
seen reading the paper “States spaces of the snake and its tour – convergence
of the discrete snake” by Marckett and Mokkadem [6].
The present paper is organized as follows. In Section 2 we formulate two
statements and one open question. In Section 3 we prove Proposition 1 which
is based on an amazing calculation used previously in [12]. Next in Section 4
we show an interesting calculation involving a Brownian path property, which
allows us to prove Proposition 2. The idea is contained in [11] without details,
see also [10]. Finally, in Section 5, we give comments on our open question
about the expectation of integral functionals of the Brownian motion.
2 Main results and an open question
Throughout the paper we assume that {B(t), t ≥0} is a one-dimensional
Brownian motion.
Proposition 1.
E
B x
0
eB(u) du
−1C
∼
1
√
2πx,
as
x →∞.
For a ∈R, let σa = inf
1
t > 0 : B(t) = a
2
, the first hitting time of level a
by the Brownian motion. Set
M = inf

x > 0 : B(x) −
inf
0<y<x B(y) = 1

.
Further, we define the random time b over the random interval (0, M) as
follows:
b = inf

x > 0 : B(x) =
inf
0<y<M B(y)

.
Proposition 2. The following identity is true:
E
)
ezb, σ−1
2 < σ 1
2

=
sinh(
√
2z/2)
√
2z cosh(
√
2z),
z > 0.

A Note on the Brownian Motion
387
An open problem. What is the value of the following expectation:
E
B 1
0
B2n(u) du
−1C
,
for
n = 1, 2, . . . ?
We are going to comment on this question in Section 5.
3 The proof of Proposition 1. Some comments
First, for any fixed x > 0, we have (by time reversing) the elementary property
of the Brownian motion:
{B(u), 0 < u < x}
law
= {B(x −u) −B(x), 0 < u < x}.
Then we have
E
B x
0
eB(u) du
−1C
= E

1/
 x
0 eB(x−u)−B(x) du

= E
)
eB(x)/
 x
0 eB(u) du

= E
 d
dx

log
 x
0
eB(u) du

= d
dxE

log
 x
0
eB(u) du

.
Also we use another elementary property (self-similarity) of the Brownian
motion: for any fixed positive x,
{B(xu), u > 0}
law
= {√xB(u), u > 0}.
Therefore, we have
E

log
 x
0
eB(u)du

= E

log
 1
0
e
√xB(u) du + log x

.
We use the Laplace method for continuous functions, hence, for Brownian
paths, to conclude that
lim
x→∞
1
√x log
 1
0
e
√xB(u) du = max
0≤u≤1 B(u).
Thus,
E

log
 1
0
e
√xB(u) du

∼√x E

max
0≤u≤1 B(u)

as
x →∞.

388
K. Kawazu
Simple calculation shows that
E

max
0≤u≤1 B(u)

=

2
π .
By de l’Hˆospital rule, we obtain
E
B x
0
eB(u) du
−1C
∼
1
√
2πx,
as
x →∞.
This is exactly the statement in Proposition 1.
⊓⊔
Now we use the Girsanov theorem allowing us to conclude that
E
B x
0
eB(u)+u du
−1C
∼
1
√
2πxe−x/2,
as
x →∞.
This formula was used in [12]. The above formula seems applicable in finance
calculations. The key point is that we cannot use the Markov property or the
martingale property when calculating the quantity E[(
 x
0 eB(u)+u du)−1].
4 The proof of Proposition 2. Some comments
Let us make first some useful relevant comments. Kesten [14] showed the
pivotal importance of the random time b when studying the limit distribution
of the Sinai random walk. Namely, b is the limit of the so-called bottom of the
random environment. Golosov [3] suggests a useful explanation. Let us recall
that the expectation E[e−zb], z > 0 has been calculated:
E[e−zb] =
sinh
√
2z
√
2z cosh
√
2z = tanh
√
2z
√
2z
.
This, however, is valid only for the Brownian motion {B(t), t ≥0}. Let us
notice that Kesten considered the bottom of {B(x), x ∈R} whose Laplace
transform is slightly different.
When considering a one-sided Brownian environment, the situation
changes dramatically and differs from that in the Sinai’s Brownian motion,
where we work with a two-sided Brownian environment. We have published
an interesting result in [11] in the case of one-sided Brownian environment.
To mention especially that the condition {σ−1
2 < σ 1
2 } plays a key role of a
strange phenomenon.
Now let us establish Proposition 2. The random variable b is not a stopping
time. Its Laplace transform is brought out by considering the stopping times
σa.
Before proceeding further we introduce the following notations:

A Note on the Brownian Motion
389
ξk = σ−1
2 −k
n ,
ηk = σ 1
2 −k
n ,
k = 1, 2, . . . , n;
ξ0 = σ−1
2 ,
η0 = σ 1
2 .
We also use the time shift ω+, see [7].
We use the continuity property of the Brownian paths, thus arriving at
the following chain of relations:
E[e−zb, σ−1
2 < σ 1
2 ]
= E[e−zb, ξ0 < η0]
= lim
n→∞
n

k=1
E[exp{−z[ξ0 + ξ1(ω+
ξ0) + . . . + ξk(ω+
ξk−1)]}, Ak],
where the event Ak is given by
Ak = {ξ0 < η0, ξ1(ω+
ξ0) < η1(ω+
ξ0), . . . , ξk(ω+
ξk−1) < ηk(ω+
ξk−1),
ξk+1(ω+
ξk) > ηk+1(ω+
ξk)}
It is well-known that for x < 0 < y, we have
E[e−zσx, σx < σy] =
sinh(y
√
2z)
sinh((y −x)
√
2z),
E[e−zσx, σy < σx] =
sinh(−x
√
2z)
sinh((y −x)
√
2z),
P(σy < σx) =
−x
y −x.
By using the Markov property and the space homogeneous property, we reach
the following :
lim
n→∞
n

k=1
E[exp(−zσ−1/2), σ−1/2 < σ1/2]
×
1
E[exp(−zσ−1/n), σ−1/n < σ1−1/n]
2k
1
n + 1
= lim
n→∞
sinh(
√
2z
2 )
sinh(
√
2z)
sinh((1−1/n)
√
2z)
sinh(
√
2z)
1 −sinh((1−1/n)
√
2z)
sinh(
√
2z)
1
n + 1
=
sinh(
√
2z/2)
√
2z cosh(
√
2z).
This completes the proof of Proposition 2.
⊓⊔

390
K. Kawazu
5 Comments on the open question
The random variable
 1
0
B2(u) du is well-known to probabilists and to many
physicists. The author tried to calculate the expectation
E
B 1
0
B2(u) du
−1C
,
however, without a success. In a correspondence, Yor [18] suggested to use
Laplace transform and then integration. The formula for this expectation is
given in [1]:
E

exp

−z
 1
0
B2(u) du

= 1/
H
cosh(
√
2z),
z > 0.
Yor’s suggestion was to make the next step:
E
B 1
0
B2(u) du
−1C
=
 ∞
0
1/
H
cosh(
√
2z) dz.
This integral seems difficult, the author was not successful. Also, the author
tried to use Mathematica, and the system answered it is impossible.
A colleague of the author, Takuya Kitamoto, used Mathematica to obtain
the following approximate value:
N[Integrate[1/Sqrt[Cosh[Sqrt[2x]]], {x, 0, Infinity},
Method -> DoubleExponential, WorkingPrecision -> 50]
=5.56286034255567484171772972234712712361085467055
Mathematica also tells the following:
N[Pi^(3/2), 50]
=5.5683279968317078452848179821188357020136243902832
Therefore, comparing those values it seems likely to expect that
E
B 1
0
B2(u) du
−1C
∼π3/2.
However, it would be incorrect to conclude that we have the equality. Recall
that Kesten [14] has found an error in such a computer calculation. We do not
know if this true. Hence we have formulated this as an open question. Yor,
[18], provided the author the formula
E
)  1
0
B2(u)du
−1
= 4
√
2
∞

n=0
(−1)n
(2n)!
22n(n!)2
1
(4n + 1)2 .

A Note on the Brownian Motion
391
Moreover, we can suggest the following extension, which we believe, it is a
fascinating problem: Find the exact value of
E
B 1
0
B2n(u) du
−1C
for n = 1, 2, . . . .
We notice the following relation:
E
B x
0
B2n(u) du
−1C
=
1
xn+1 E
B 1
0
B2n(u) du
−1C
.
Acknowledgements
The author congratulates Professor Albert Shiryaev on the occasion of his
70th Birthday.
The author thanks Prof. J. Stoyanov and Prof. Yu. Kabanov for their
attention and useful suggestions when preparing this paper. Prof. H. Tanaka
and Prof. M. Yor provided the author many important suggestions.
Finally, the author is grateful to Prof. Takuya Kitamoto for his support
in operating Mathematica to perform the above approximate calculations.
References
1. Borodin, A.N. and Salminen, P.: Handbook of Brownian Motion: Facts and
Formulae. Birkh¨auser, Basel (1996)
2. Brox, T.: A one-dimensional diffusion process in a Wiener medium. Ann.
Probab. 14, 1206–1218 (1986)
3. Golosov, A.O.: Limit distributions for random walks in random environments.
Soviet Math. Dokl. 28, 13–22 (1983)
4. Ikeda, N.: Sparkle Out of Randomness – Brownian Motion (1990) (in Japanese)
5. Ikeda, N. and Watanabe, S.: Stochastic Differential Equations and Diffusion
Processes, 2nd ed. North-Holland, Amsterdam (1989)
6. Marckett, J.F. and Mokkadem, A.: States spaces of the snake and its tour –
Convergence of the discrete snake. J. Theoret. Probab. 16, 1015–1046 (2003)
7. Itˆo, K. and McKean, H.P.: Diffusion Processes and Their Sample Paths, 2nd ed.
Springer, Berlin (1974)
8. Kawazu, K. and Kesten, H.: On the birth and death processes in symmetric
random environment. J. Statist. Phys. 37, 67–84 (1984)
9. Kawazu, K. and Tanaka, H.: A diffusion process in a Brownian environment
with drift. J. Math. Soc. Japan 49, 189–211 (1997)
10. Kawazu, K., Suzuki, Y. and Tanaka, H.: A diffusion process with a one-sided
Brownian potential. Tokyo J. Math. 24, 211–229 (2001)
11. Kawazu, K. and Suzuki, Y.: Limit theorems for a diffusion process with a one-
sided Brownian potential. (Unpublished manuscript) (2004)

392
K. Kawazu
12. Kawazu, K. and Tanaka, H.: On the maximum of a diffusion process in a drifted
Brownian environment. Lecture Notes in Math. (Springer) 1557, 78–85 (1991)
13. Kawazu, K. and Watanabe, S.: Branching processes with immigration and re-
lated theorems. Theory Probab. Appl., 16, 34–51 (1971)
14. Kesten, H.: The limit distribution of Sinai’s random walk in a random environ-
ment. Physica 138A, 299–309 (1986)
15. Revuz, D. and Yor, M.: Continuous Martingale and Brownian Motion, 2nd ed.
Springer, Berlin (1994)
16. Sinai, Ya.G.: The limiting behavior of a one-dimensional random walk in a
random medium. Theory Probab. Appl. 27, 256–268 (1982)
17. Yor, M.: Sur certaines fonctionelles du mouvement brownien r´eel. J. Appl.
Probab. 29, 202–208 (1992)
18. Yor, M.: Private communication (2004)

Continuous Time Volatility Modelling:
COGARCH versus Ornstein–Uhlenbeck
Models
Claudia KL¨UPPELBERG1, Alexander LINDNER1, and Ross MALLER2
1 Center for Mathematical Sciences, Munich University of Technology,
D-85747 Garching, Germany.
{cklu,lindner}@ma.tum.de
2 Centre for Mathematical Analysis, School of Finance & Applied Statistics,
Australian National University, Canberra, ACT, Australia.
Ross.Maller@anu.edu.au
Summary. We compare the probabilistic properties of the non-Gaussian Ornstein–
Uhlenbeck based stochastic volatility model of Barndorff-Nielsen and Shephard
(2001) with those of the COGARCH process. The latter is a continuous time
GARCH process introduced by the authors (2004). Many features are shown to
be shared by both processes, but differences are pointed out as well. Furthermore,
it is shown that the COGARCH process has Pareto like tails under weak regularity
conditions.
Key words: COGARCH, continuous time GARCH, GARCH, generalized Ornstein–
Uhlenbeck process, L´evy process, self-decomposable distribution, stochastic volatil-
ity model, tail behaviour
Mathematics Subject Classification (2000): 60E07, 60G10, 60G70,
91B70
1 Introduction
It is common wisdom among financial researchers and the banking industry
that volatility is stochastic, has jumps, and often exhibits long range depen-
dence. Since such financial data as log-prices and exchange rates often come
as high-frequency intra-day data, continuous time models are useful. There
have been two main approaches.
The first, mathematical one is based on semimartingale (no arbitrage)
theory, takes its starting point as the Black–Scholes model, and introduces

394
C. Kl¨uppelberg et al.
a stochastic volatility process. For an introduction and overview of stochas-
tic volatility models, we refer to Shephard [25]. The second, econometric, ap-
proach is based on empirical properties of financial time series. A recent model
fitting into both these approaches and having received much attention is the
stochastic volatility model of Barndorff-Nielsen and Shephard [2, 3, 4]. There,
the volatility process is modelled as an Ornstein–Uhlenbeck (OU) type process
driven by a L´evy process (or a superposition of such OU type processes), and
thus can exhibit jumps. The price process is then obtained using an indepen-
dent Brownian motion as driving noise.
The majority of the models arising from the econometric approach are in
discrete time. In particular, GARCH models and their extensions have been
in the limelight as appropriate models to capture certain empirical facts of
the empirical volatility process; see Engle [13] for an overview on GARCH
modelling. In this area, motivated again by the availability of high-frequency
data and by the option pricing problem, classical diffusion limits have been
used in a natural way to suggest continuous time limits; see, e.g., Nelson [23]
and Duan [12].
Unfortunately, in these situations, the limiting models can lose certain es-
sential properties of the discrete time GARCH models. Moreover, they can
have distinctly different statistical properties. As has been shown recently
by Wang [28], parameter estimation in the discrete time GARCH and the
corresponding continuous time limit stochastic volatility model may yield dif-
ferent estimates. Thus the continuous time models are probabilistically and
statistically different from their discrete time progenitors.
It is surprising and counter-intuitive that Nelson’s diffusion limit of the
GARCH process is driven by two independent Brownian motions, i.e. has
two independent sources of randomness, whereas the discrete time GARCH
process is driven only by a single white noise sequence. One of the features of
the GARCH process is the idea that large innovations in the price process are
almost immediately manifested as innovations in the volatility process, but
this feedback mechanism is lost in models such as the Nelson continuous time
version.
The phenomenon that a diffusion limit is driven by two independent
Brownian motions, while the discrete time model is given in terms of a single
white noise sequence, is not restricted to the classical GARCH process. Indeed,
Duan [12] has shown that this occurs for many GARCH like processes. In this
respect, Jeantheau [20] only recently developed a discrete time model having
many features with the GARCH model in common, but having a diffusion
limit driven by a single Brownian motion only.
In Kl¨uppelberg, Lindner and Maller [22], the authors proposed a different
approach to obtain a continuous time model. This “COGARCH” (continuous
time GARCH) model, based on a single background driving L´evy process, is
different from, though related to, other continuous time stochastic volatility
models that have been proposed. It generalizes the essential features of the
discrete time GARCH process in a direct way.

COGARCH versus Ornstein–Uhlenbeck models
395
It is natural to compare the two main approaches outlined above, i.e.
stochastic volatility and GARCH type modelling. An empirical, likelihood
inference based comparison between discrete time stochastic volatility and
discrete time GARCH processes is given in Kim, Shephard and Chib [21].
In the present paper, we aim to compare the probabilistic properties of the
COGARCH process with those of the stochastic volatility model of Barndorff-
Nielsen and Shephard. It turns out that they share many mathematical prop-
erties, but that there are also certain differences. A striking difference is
manifested in the behaviour (lightness or heaviness) of the tails of their one-
dimensional distributions. The stochastic volatility model can exhibit many
different kinds of tail behaviour, depending on the driving L´evy process,
whereas the COGARCH model has Pareto like (heavy) tails for essentially
most driving L´evy processes.
The paper is structured as follows: in the next section, we recall the ba-
sic definitions of L´evy processes and give the definitions of the models under
consideration. We then proceed to collect the properties of the models and
compare them. The most obvious differences are pointed out in Section 2.3,
while in Section 3 we consider properties of the process itself, such as strict sta-
tionarity, Markovian properties and pathwise behaviour. Then, in Section 4,
second order properties are considered. It is shown that both processes have
essentially the same kind of autocovariance structure. Section 5 focusses on
distributional properties of both models. While it is well-known that the
stationary distribution of the squared volatility of the OU type process of
Barndorff-Nielsen and Shephard is self-decomposable, in Section 5.1 the same
is shown to hold for the COGARCH volatility. Then, in Section 5.3, we prove
some new results, showing that the COGARCH model has Pareto like tails
under wide conditions. Finally, a short conclusion is given in Section 6.
2 Definition of the models
Both the OU as well as the COGARCH model are driven by a L´evy process
L = (Lt)t≥0, assumed to be c`adl`ag and defined on a probability space with
appropriate filtration, satisfying the “usual conditions”, i.e. right-continuity
and completeness. We recall some properties of L´evy processes, see Bertoin [6]
and Sato [24]: for each t ≥0 the characteristic function of Lt at θ ∈R can be
written in the form
E(eiθLt)
= exp

t

iγLθ −τ 2
L
θ2
2 +
 ∞
−∞

eiθx −1 −iθx1{|x|≤1}

ΠL(dx)

.(2.1)
The constants γL ∈R, τ 2
L ≥0 (Gaussian part) and the measure ΠL on R form
the characteristic triplet of L; the L´evy measure ΠL is required to satisfy

R min(1, x2)ΠL(dx) < ∞. If in addition

R min(1, |x|)ΠL(dx) < ∞, then

396
C. Kl¨uppelberg et al.
γL,0 := γL −

[−1,1] xΠL(dx) is called the drift of L. A L´evy process is of finite
variation if and only if

R min(1, |x|)ΠL(dx) < ∞and τ 2
L = 0. In that case,
the sample paths of (Lt)t≥0 have finite variation on compacts. A L´evy process
with nondecreasing sample paths is called a subordinator. These are exactly
the L´evy processes of finite variation with non-negative drift and having L´evy
measure concentrated on (0, ∞). In the following considerations, we will only
be interested in the situation when the L´evy measure is non-trivial, i.e. we
always assume that ΠL is nonzero.
2.1 The Barndorff-Nielsen and Shephard OU process
The stochastic volatility model presented in [2, 3, 4] specifies the volatility as
an Ornstein-Uhlenbeck process, driven by a subordinator. More precisely, let
(Lt)t≥0 be a subordinator and α > 0. Then the volatility process (*σt)t≥0 is
defined by the stochastic differential equation (SDE)
d*σ2
t = −α*σ2
t dt + dLαt,
t ≥0 ,
(2.2)
where *σ2
0 is a finite random variable independent of (Lt)t≥0 and *σt :=

*σ2
t .
The solution to (2.2) is the Ornstein-Uhlenbeck type process (“OU process”)
*σ2
t =
 t
0
eαsdLαs + *σ2
0

e−αt ,
t ≥0 .
(2.3)
The (logarithmic) price process ( *Gt)t≥0 is then modelled by the SDE
d *Gt = (µ + b*σ2
t )dt + *σt dWt ,
t ≥0 ,
*G0 = 0 ,
(2.4)
where µ and b are constants and (Wt)t≥0 is standard Brownian motion, inde-
pendent of *σ2
0 and the L´evy process (Lt)t≥0. The Itˆo solution of this SDE is
given by
*Gt = µt + b
 t
0
*σ2
s ds +
 t
0
*σs dWs ,
t ≥0 .
The logarithmic asset returns over time periods of length r > 0 are then given
by *G(r)
t
:= *Gt+r −*Gt, t ≥0. In the following, the notation *Gt and *σt (with
tildes) will always refer to the processes of Barndorff-Nielsen and Shephard
just defined. In contrast, the COGARCH process defined below will always be
denoted by Gt with volatility σt (without tildes). If the driving L´evy process
(Lt)t≥0 refers to the OU process, then it will always be assumed to be a
subordinator.
2.2 The COGARCH(1,1) model
The COGARCH(1,1) process (see [22]) is motivated by the discrete time
GARCH(1,1) process (Yn)n∈N0, satisfying

COGARCH versus Ornstein–Uhlenbeck models
397
Yn = εnσn,disc,
where
σ2
n,disc = β + λY 2
n−1 + δσ2
n−1,disc,
n ∈N,
(2.5)
σn,disc :=
H
σ2
n,disc, and (εn)n∈N0 is a sequence of independent and identically
distributed random variables, independent of σ2
0,disc. Here, N = {1, 2, 3, . . .}
denotes the set of positive integers and N0 = N ∪{0}. The recursion in (2.5)
can be solved to give
σ2
n,disc
=

β
 n
0
exp


−
⌊s⌋

j=0
log(δ + λε2
j)


ds + σ2
0,disc

exp



n−1

j=0
log(δ + λε2
j)


.
In the continuous time version, the innovations εn are replaced by the jumps
of a L´evy process. Let (Lt)t≥0 be a L´evy process with jumps ∆Lt = Lt −Lt−,
and let 0 < δ < 1, λ ≥0. Define a c`adl`ag process (Xt)t≥0 by
Xt = −t log δ −

0<s≤t
log(1 + (λ/δ)(∆Ls)2),
t ≥0 .
(2.6)
Then, with β > 0 and σ2
0 a finite random variable, independent of (Lt)t≥0,
define the (left-continuous) volatility process (σt)t≥0 by
σ2
t =

β
 t
0
eXsds + σ2
0

e−Xt−,
t ≥0,
(2.7)
where σt :=

σ2
t , and define the integrated continuous time GARCH process
(“COGARCH”) (Gt)t≥0 as the c`adl`ag process satisfying
dGt = σt dLt ,
t ≥0 ,
G0 = 0 .
(2.8)
Thus, G has jumps at the same times as L but of the size ∆Gt = σt∆Lt. The
logarithmic asset returns over time periods of length r > 0 are then modelled
by G(r)
t
:= Gt+r −Gt, t ≥0.
In [22], Proposition 3.1, it is shown that the process (Xt)t≥0 is itself a spec-
trally negative L´evy process of finite variation, with drift γX,0 = −log δ and
zero Gaussian component τ 2
X = 0. The L´evy measure ΠX is the image measure
of ΠL under the transformation R →(−∞, 0], x →−log(1 + (λ/δ)x2).
2.3 A first comparison
Despite their arising and being motivated in quite different ways, the volatility
processes σ2 and *σ2 are strikingly analogous in satisfying the general Ornstein-
Uhlenbeck equations (2.3) and (2.7). But an obvious difference between the
price processes is that the OU process of Barndorff-Nielsen and Shephard is fed
into a Hull-White model, driven by an independent Brownian motion, whereas

398
C. Kl¨uppelberg et al.
the COGARCH price process is driven by the same L´evy process as is used in
the volatility. Furthermore, the SDE defining *Gt has an additional drift term
(µ+b*σ2
t )dt, which does not occur in (2.8). It is possible to add such a drift term
to (2.8) as well, but we will not do this since there is already a correspondence
of G to the discrete time GARCH process without the necessity for an extra
drift term.
Another obvious difference concerns the sample path properties of the
price processes: ( *Gt)t≥0 will have continuous sample paths, inherited from
the driving Brownian motion (see e.g. Jacod and Shiryaev [19]), while (Gt)t≥0
exhibits jumps. Both these factors can be useful in different ways in practice.
For the volatility processes, note that both (*σ2
t )t≥0 and (σ2
t )t≥0 exhibit
jumps. While (*σt)t≥0 is right-continuous, (σt)t≥0 is left-continuous. This is a
minor difference, since *Gt is driven by Brownian motion, and hence *σt in (2.4)
could equally well be replaced by *σt−. A more striking difference between the
volatility processes is that in (2.3) the driving L´evy process of the volatility is
in the integrator, while in (2.7) it appears in the integrand. Despite these facts,
we will see that both volatility processes nevertheless share many common
features.
3 Properties of the processes
In this section we shall consider Markov and stationarity properties, link the
integrated squared volatility and the quadratic variation for both processes,
and exhibit some pathwise properties of the volatility processes. We start
by mentioning that not only does *σt satisfy an SDE, but so does σt, see
Proposition 3.1 below, which was proved in [22], Proposition 3.2.
Proposition 3.1. [SDE and solution for σ]
The squared volatility process (σ2
t )t≥0 of the COGARCH process satisfies the
stochastic differential equation
dσ2
t+ = βdt + σ2
t eXt−d(e−Xt) ,
t > 0 ,
and we have
σ2
t = βt + log δ
 t
0
σ2
sds + (λ/δ)

0<s<t
σ2
s(∆Ls)2 + σ2
0,
t ≥0.
(3.1)
Both volatility processes are Markovian:
Theorem 3.1. [Markov properties of the processes]
Both the squared volatility processes (*σ2
t )t≥0 and (σ2
t )t≥0, as given by (2.3) and
(2.7), respectively, are time-homogeneous Markov processes. Furthermore, the
bivariate processes (*σt, *Gt)t≥0 and (σt, Gt)t≥0 are time-homogeneous Markov
processes.

COGARCH versus Ornstein–Uhlenbeck models
399
Proof. For the fact that (*σ2
t )t≥0 is a time homogeneous Markov process if
α = 1 see Sato [24], Lemma 17.1 and its preceding discussion. For general
α > 0, the assertions on (*σ2
t )t≥0 and (*σt, *Gt)t≥0 can be seen as follows. We
have
*σ2
t = *σ2
y eα(y−t) +
 t
y
eα(s−t)dLαs = eα(y−t)
	
*σ2
y +
 α(t−y)
0
ev dLv+αy

.
Since {Lαs}y≤s≤t is independent of the σ-algebra generated by (*σ2
u)0≤u≤y,
the first equation gives the Markov property for *σt, and since the distribution
of the expression on the righthand side depends only on t −y we see that *σ2
is time homogeneous. The Markov property of (*σt, *Gt)t≥0 follows from
*Gt = *Gy + µ(t −y) + b
 t
y
*σ2
s ds +
 t
y
*σs dWs, 0 ≤y < t.
For the corresponding results on (σ2
t )t≥0 and (σt, Gt)t≥0, see [22], Theorem 3.2
and Corollary 3.1.
The Markov property of the squared volatility processes can be regarded
as a special case of a result on more general Ornstein-Uhlenbeck processes.
Carmona, Petit and Yor [10] consider processes of the form
Vt = eξt
 t
0
e−ξs−dηs + V0

,
t ≥0 ,
where (ξt, ηt)t≥0 is a two-dimensional L´evy process independent of V0. Then
(Vt)t≥0 is a time-homogeneous Markov process, [10], Corollary 5.2. If (ξt)t≥0
and (ηt)t≥0 are independent, then Vt
D=
 t
0 eξs−dηs+V0eξt, see [10]. (Through-
out, “
D=” means “equal in distribution”.) Without assuming independence of
ξ and η, Erickson and Maller [16], Theorem 2, give necessary and sufficient
conditions for the a.s. existence of the integral
 ∞
0
eξt−dηt. When this occurs
and ξ and η are independent, there is a stationary solution, V∞, say, and Vt
converges in distribution to this as t →∞(see Carmona et al. [11], Theo-
rem 3.1 and its proof). Theorem 3.2 below can be deduced from these results.
(We remark that separate proofs for the two types of volatility process can be
given without appealing to properties of the generalized OU-process (Vt)t≥0.
For (*σ2
t )t≥0, see [2, 3] or Sato [24], Theorems 17.5, 17.11 and Corollary 17.9
(apart from part (c) below), while for (σ2
t )t≥0 see [22], Theorems 3.1, 3.2 and
Corollary 3.1.)
Theorem 3.2. [Stationarity condition for *σ and σ]
(a) The squared volatility process (*σ2
t )t≥0 of the OU model converges in dis-
tribution to a finite random variable *σ2
∞as t →∞if and only if
 ∞
1
log y ΠL(dy) < ∞.
(3.2)

400
C. Kl¨uppelberg et al.
In that case,
*σ2
∞
D=
 ∞
0
e−s dLs.
(3.3)
(b) The squared volatility process (σ2
t )t≥0 of the COGARCH model converges
in distribution to a finite random variable σ2
∞as t →∞if and only if

R
log(1 + (λ/δ)y2) ΠL(dy) < −log δ
(3.4)
(which, since δ > 0, incorporates the requirement that the integral be finite),
in which case
σ2
∞
D= β
 ∞
0
e−Xtdt.
(c) If (3.2) or (3.4) are not satisfied, respectively, then the squared volatility
process diverges in probability to ∞as t →∞.
(d) A stationary solution of (*σ2
t )t≥0 or (σ2
t )t≥0 exists if and only if (3.2)
or (3.4) are satisfied, in which case the stationary distribution at time t is the
distribution of *σ2
∞or σ2
∞, respectively. In that case, ( *Gt)t≥0 and (Gt)t≥0 have
stationary increments, i.e. the increment processes ( *G(r)
t )t≥0 and (G(r)
t )t≥0
are stationary for each fixed r > 0.
It is interesting to observe that the stationarity condition for (*σ2
t )t≥0 and
the distribution of *σ2
∞depend on the L´evy measure ΠL only, whereas (3.4)
and σ2
∞depend on ΠL and on the parameters δ and λ. For the OU model,
this is a consequence of the unusual timing dLαt in (2.2), chosen deliberately
by Barndorff-Nielsen and Shephard [3] to separate the stationary distribution
from the dynamical structure, which depends on α.
Next we investigate pathwise properties of the volatility processes, espe-
cially the behaviour between jumps if the driving L´evy process is compound
Poisson.
Proposition 3.2. [Pathwise behaviour of *σ and σ]
(a) The volatility σt at time t of the GOGARCH process satisfies
σ2
t ≥
β
−log δ (1 −et log δ), for all t ≥0.
If σ2
t0 ≥
β
−log δ for some t0, then σ2
t ≥
β
−log δ for every t ≥t0.
If σ2
t
D= σ2
∞is the stationary version, then
σ2
∞≥
β
−log δ
a.s.
(3.5)
The stationary version *σ2
∞of the OU-process is bounded from below (i.e.
bounded away from 0) if and only if the drift term γL,0 of the subordina-
tor (Lt)t≥0 is strictly positive.

COGARCH versus Ornstein–Uhlenbeck models
401
(b) The jumps of both squared volatility processes at time t > 0 are described
by
*σ2
t −*σ2
t−= ∆Lαt,
σ2
t+ −σ2
t = (λ/δ) σ2
t (∆Lt)2.
(c) Let (Lt)t≥0 be a compound Poisson process with jump times 0 = T0 <
T1 < . . . Then the OU volatility satisfies for t ∈(Tj/α, Tj+1/α), j ∈N0,
d
dt*σ2
t = −α*σ2
t ,
*σ2
t = *σ2
Tj/α e−(αt−Tj),
while the COGARCH volatility satisfies for t ∈(Tj, Tj+1),
d
dtσ2
t = β + (log δ)σ2
t ,
σ2
t =
β
−log δ +

σ2
Tj+ +
β
log δ

e(t−Tj) log δ.
Proof. (a) From (2.6) follows that for 0 ≤s < t,
Xs −Xt−= (t −s) log δ +

s<u<t
log

1 + (λ/δ)(∆Lu)2
≥(t −s) log δ. (3.6)
In particular,
σ2
t = β
 t
0
eXs−Xt−ds + σ2
0 e−Xt−
≥β
 t
0
e(t−s) log δ ds =
β
−log δ

1 −et log δ
.
Then (3.5) follows as t →∞. Now let t > t0 and suppose that σ2
t0 ≥
β
−log δ.
In equation (3.12) of [22] it was shown that
σ2
t = eXt0−−Xt−σ2
t0 + β
 t
t0
eXs−Xt−ds.
From (3.6) then follows
σ2
t ≥e(t−t0) log δ σ2
t0 + β
 t
t0
e(s−t0) log δ ds
≥e(t−t0) log δ

β
−log δ

+

β
−log δ

(1 −e(t−t0) log δ) =
β
−log δ .
That *σ2
∞is bounded from below if and only if the drift is non-zero follows
from (3.3) and Sato [24], Example 17.10.
The proof of (b) and (c) follows easily from (2.3), (2.7) and (3.1).
Proposition 3.2 shows in particular that the stationary version of the CO-
GARCH volatility process is always bounded away from 0 once t > 0, which
is not necessarily the case for the OU volatility. From (b) it follows that if a

402
C. Kl¨uppelberg et al.
volatility jump occurs for either process, then this jump is necessarily positive.
For compound Poisson driving processes, between jumps the processes show
similarities, since both decay exponentially (more precisely, the COGARCH
process decays only once it rises above the lower bound β/(−log δ), and before
that it increases). However, note that (*σ2
t ) satisfies a homogeneous differential
equation, while (σ2
t ) satisfies an inhomogeneous differential equation, between
jumps.
Next, we link the integrated squared volatilities
 t
0 *σ2
s ds and
 t
0 σ2
s ds with
the quadratic variations of the process *G and G, respectively. For the definition
and elementary properties of the quadratic variation [Y, Y ]t of a semimartin-
gale (Yt)t≥0, we refer to Jacod and Shiryaev [19], Chapter 1.
Proposition 3.3. [Quadratic variation and integrated squared volatility]
(a) For the stochastic volatility model of Barndorff-Nielsen and Shephard we
have
[ *G, *G]t =
 t
0
*σ2
s ds,
t ≥0.
(3.7)
(b) For the COGARCH model we have
λ
δ [G, G]t−= (λ
δ τ 2
L −log δ)
 t
0
σ2
s ds + σ2
t −σ2
0 −βt ,
t ≥0.
(3.8)
Proof. (a) is clear from the general properties of stochastic integrals, see
e.g. [19], while (b) follows from
[G, G]t−=
 t−
0
σ2
s d[L, L]s
=
 t−
0
σ2
s d(sτ 2
L +

0<u≤s
(∆Lu)2) = τ 2
L
 t
0
σ2
s ds +

0<u<t
σ2
s(∆Ls)2.
Plugging this into (3.1) gives (3.8).
The integrated quadratic variation is a key measure for stochastic volatil-
ity models. Its importance can be seen from equation (5.3) below. Now (3.7)
means that the integrated volatility can be recovered from the quadratic vari-
ation. Equation (3.8) shows that for the COGARCH process, the integrated
volatility can at least be expressed with the aid of the quadratic variation and
the volatility at times t and 0 by a reasonably simple formula. An expression
in terms of the quadratic variation only cannot be expected, since the L´evy
process in (2.8) has jumps.
4 Second order properties
In this section we shall concentrate on moments and autocorrelation functions
of both the volatility processes and the price process. A short discussion of
the cumulant transform for the OU process is included.

COGARCH versus Ornstein–Uhlenbeck models
403
From now on, in order to avoid the trivial case of a deterministic volatility,
we shall always assume λ > 0 when dealing with the COGARCH process.
4.1 The volatility process
In this section we derive moments and autocorrelation functions of the squared
stochastic volatility processes (*σ2
t )t≥0 and (σ2
t )t≥0. For convenience we shall
restrict ourselves to the case of the stationary versions of these volatility
processes. We start with a preparatory lemma on exponential moments of
(Xt)t≥0 for the COGARCH volatility, which by (2.7) are related to moments
of σ2
t .
Lemma 4.1. [Exponential moments of X]
Let Xt be given by (2.6), and keep κ > 0 throughout.
(a) Ee−κXt < ∞for some t > 0, or, equivalently, for all t > 0, if and only if
E|L1|2κ < ∞.
(b) When Ee−κX1 < ∞, put Ψ(κ) = ΨX(κ) = log Ee−κX1. Then |Ψ(κ)| < ∞,
Ee−κXt = etΨ(κ), and
Ψ(κ) = κ log δ +

R

(1 + (λ/δ)y2)κ −1

ΠL(dy).
(4.1)
(c) If Ψ(κ) < 0 for some κ > 0, then Ψ(d) < 0 for all 0 < d < κ.
(d) If E|L1|2κ < ∞and Ψ(κ) ≤0 for some κ > 0, then (3.4) holds, and a
stationary version of (σ2
t )t≥0 exists.
Proof. (a), (b) and (c) are proved in Lemma 4.1 of [22]. For (d), note that
Ψ(κ) ≤0 is equivalent to
1
κ

R

1 + λ
δ y2
κ
−1

ΠL(dy) ≤−log δ.
Since log(1 + (λ/δ)y2) < (1/κ)((1 + (λ/δ)y2)κ −1) for any y ̸= 0 (as a conse-
quence of x > 1 + log x for x > 1), this implies (3.4).
Next we give conditions for the existence of moments of the squared volatil-
ity processes. For *σ2
∞this is done in terms of the cumulants. Recall that the cu-
mulant transform of a random variable Y is defined as cumY (θ) := log EeiθY ,
and that the kth cumulant cumY,k exists if and only if E|Y |k < ∞, in which
case it is given by
cumY,k := 1
ik
dk
dθk cumY (0).
In particular,
cumY,1 = EY,
cumY,2 = Var(Y ).

404
C. Kl¨uppelberg et al.
Theorem 4.1. [Moments and ACF of *σ and σ]
Let *σ2
∞and σ2
∞have the stationary distributions of the volatility processes,
respectively.
(a) The kth moment of *σ2
∞is finite if and only if ELk
1 < ∞, k ∈N. In this
case, the kth cumulants of *σ2
∞and L1 satisfy the relation
cum*σ2
∞,k = k−1 cumL1,k.
In particular, E*σ2
∞= EL1, Var(*σ2
∞) = 2−1Var(L1). If EL2
1 < ∞, then the
autocovariance function of the stationary squared volatility process satisfies
cov(*σ2
t , *σ2
t+h) = 2−1Var(L1) e−αh,
t, h ≥0.
(4.2)
(b) The kth moment of σ2
∞is finite if and only if EL2k
1
< ∞and Ψ(k) < 0,
k ∈N. In this case,
Eσ2k
∞= k! βk
k
(
l=1
1
−Ψ(l).
(4.3)
In particular, Eσ2
∞=
β
−Ψ(1), Var(σ2
∞) = β2(2Ψ −1(1)Ψ −1(2) −Ψ −2(1)). If
EL4
1 < ∞and Ψ(2) < ∞, then the autocovariance function of the stationary
squared volatility process satisfies
cov(σ2
t , σ2
t+h) = β2

2
Ψ(1)Ψ(2) −
1
Ψ 2(1)

e−|Ψ(1)|h ,
t, h ≥0 .
(4.4)
Proof. (a) The existence of the moments of *σ2
∞is a consequence of
ELk
1 ≤ek E
 1
0
e−s dLs
k
≤ek E
 ∞
0
e−s dLs
k
(recall that Lt is a subordinator in the tilde setup) and
E
 ∞
0
e−s dLs
k
≤E
	 ∞

i=0
e−i(Li+1 −Li)

k
=
∞

i1=0
. . .
∞

ik=0
e−i1−...−ikE ((Li1+1 −Li1) · · · (Lik+1 −Lik)) ,
and the latter is finite if ELk
1 < ∞by independence and identical distribution
of the increments Lij+1 −Lij. The relation between the cumulants (when
they exist) and the formula for the autocovariance function can be found
in [3], page 172.
The proof of (b) can be found in [22], Proposition 4.2 and Corollary 4.1.
For (4.3), see also Carmona, Petit and Yor [10], Proposition 3.3.

COGARCH versus Ornstein–Uhlenbeck models
405
Note that the moment condition EL2k
1
and Ψ(k) < 0 for the COGARCH
volatility already imply the existence of a stationary version by Lemma 4.1(d).
The same is true for the Ornstein-Uhlenbeck process, since EL1 < ∞is
equivalent to
 ∞
1
xΠL(dx) < ∞, implying (3.2).
It should be noted that, for *σ2
∞, the existence of moments depends only
on the driving L´evy process (Lt)t≥0, while for σ2
∞it depends on the driving
L´evy process as well as on the parameters. This is highlighted in the following
Proposition, see [22], Proposition 4.3.
Proposition 4.1. [Dependence on parameters for moments of σ]
(a) For any L´evy process (Lt)t≥0 with nonzero L´evy measure such that

R log(1 + y2) ΠL(dy) is finite, there exist parameters δ, λ ∈(0, 1) for which
σ2
∞exists, but Eσ2
∞= ∞.
(b) For any L´evy process (Lt)t≥0 such that EL2k
1
< ∞(k ∈N) and for any
δ ∈(0, 1) there exists λδ > 0 such that the limit variable σ2
∞exists with
Eσ2k
∞< ∞for any pair of parameters (δ, λ) such that 0 < λ ≤λδ.
(c) Suppose 0 < δ < 1, λ > 0. Then for no L´evy process (Lt)t≥0 (with nonzero
L´evy measure) do the moments of all orders of σ2
∞exist. In particular, the
Laplace transform Ee−θσ2
∞of σ2
∞does not exist for any θ < 0.
Much of the analysis in [3] is based on the connection between the cumulant
functions of L1 and *σ2
∞. In [1], page 178, it is shown that
cum*σ2
∞(θ) =
 ∞
0
cumL1(e−sθ) ds,
cumL1(θ) = θ d
dθcum*σ2
∞(θ)
(provided they exist), see also [5], page 282, where a similar relation for
the logarithms of the Laplace transforms is established. In contrast, for the
COGARCH volatility, a feasible expression for the cumulant transform or
the Laplace transform does not seem to be at hand. By Proposition 4.1, the
Laplace transform of σ2
∞does not exist in a (two-sided) neighborhood of the
origin. However, the Laplace transform of the random variable σ−2
∞exists in
a neighborhood of the origin and σ2
∞is determined by all its negative integer
moments. This was shown by Bertoin and Yor [7], Proposition 2, who also
give an expression for the negative integer moments.
4.2 The price process
In this section we investigate second order properties of the increments of the
price processes ( *Gt)t≥0 and (Gt)t≥0. From Section 2 recall the notation
*G(r)
t
:= *Gt+r −*Gt,
G(r)
t
:= Gt+r −Gt,
t ≥0,
r > 0,
corresponding to logarithmic asset returns over time periods of length r. We
will work with the stationary version of the volatility process. By Theorem 3.2
this implies strict stationarity of the processes ( *G(r)
t )t≥0 and (G(r)
t )t≥0, respec-
tively.

406
C. Kl¨uppelberg et al.
Theorem 4.2. [ACF of the price process]
Let r > 0 be a fixed constant, and let t ≥0.
(a) Let the price process ( *Gt)t≥0 be defined by (2.4) for the stationary volatility
process (*σt)t≥0. Assume that EL2
1 < ∞. Then
E( *G(r)
t ) = (µ + bEL1)r,
Var( *G(r)
t ) = rEL1 + b2 Var(L1)

r/α −(1 −e−αr)/α2
.
If µ = b = 0, then
cov( *G(r)
t , *G(r)
t+h) = 0
for any h ≥r. If additionally EL4
1 < ∞, then there is a strictly positive
constant *Cr (not depending on t) such that
cov(( *G(r)
t )2, ( *G(r)
t+h)2) = *Cr e−αh
∀h ∈rN.
(b) Let the COGARCH process (Gt)t≥0 be defined by (2.8) for the stationary
volatility process (σt)t≥0. Suppose (Lt)t≥0 is a quadratic pure jump process
(i.e. τ 2
L = 0 in (2.1)) with EL2
1 < ∞, EL1 = 0, and that Ψ(1) < 0. Then for
any h ≥r > 0,
E(G(r)
t ) = 0,
E(G(r)
t )2 =
βr
−Ψ(1)EL2
1,
cov (G(r)
t , G(r)
t+h) = 0.
Assume further that EL4
1 < ∞and Ψ(2) < 0. Then there is a non-negative
constant Cr (not depending on t) such that
cov((G(r)
t )2, (G(r)
t+h)2) = Cr e−|Ψ(1)|h
∀h ≥r.
Assume further that EL8
1 < ∞, ψ(4) < 0, that (Lt)t≥0 is of finite variation
and that

R x3ΠL(dx) = 0. Then Cr is strictly positive.
The proof of (a) can be found in Section 4 of [3], while the proof of (b) is
given in [22], Proposition 5.1.
Theorem 4.2 tells us that for both models the returns are uncorrelated,
while the squared returns are correlated. This agrees very much with empirical
findings. In both models, the autocorrelation function of the squared returns
decreases exponentially. Furthermore, we see that Var(G(r)
t ) is linear in r,
while Var( *G(r)
t ) is asymptotically (affine) linear in r as r approaches 0 or ∞
(however, with different slopes for r →0 and r →∞).
5 Distributional properties of the models
In this section we investigate further properties of the stationary distribution
of the volatility processes and the price processes.

COGARCH versus Ornstein–Uhlenbeck models
407
5.1 Self-decomposability
The distribution of a random variable Y is called self-decomposable if for any
c ∈(0, 1) there exists a random variable Zc, independent of Y , such that
Y
D= cY + Zc.
Every self-decomposable distribution is infinitely divisible, and an infinitely
divisible distribution is self-decomposable if and only if its L´evy measure has
a L´evy density w, which can be represented as
w(x) = k+(x)
x
1x>0 + k−(|x|)
|x|
1x<0,
x ∈R,
(5.1)
where k+ and k−are non-increasing non-negative functions on (0, ∞). Not
only has the L´evy measure a density, but also the distribution itself has.
See Sato [24], Theorem 27.13, and Sections 15-17 there for examples and
properties of self-decomposable distributions. As a further example, the class
of generalized inverse Gaussian distributions is considered in [3].
The stationary distributions *σ2
∞of the Ornstein–Uhlenbeck model of
Barndorff-Nielsen and Shephard [3] now have the nice property that they
are self-decomposable. Furthermore, as L varies over all subordinators, they
constitute the class of all possible self-decomposable distributions whose sup-
port is contained in [0, ∞), see Sato [24], Example 17.10 and Theorem 24.10.
The correspondence between the L´evy density w of *σ2
∞and the L´evy measure
ΠL of the driving L´evy process (Lt)t≥0 is given by
w(x) = x−1ΠL((x, ∞)),
x > 0,
(5.2)
see [4], equation (4.17). Interestingly, the stationary distribution σ2
∞of the
COGARCH process is self-decomposable, too. This was communicated to us
by Samorodnitsky [27], who more generally showed that
 ∞
0
e−Xtdt is self-
decomposable for any spectrally negative L´evy process (Xt)t≥0 such that
Xt →+∞a.s. We state this as a Theorem, and include Samorodnitsky’s
proof.
Theorem 5.1. The stationary distributions *σ2
∞and σ2
∞of both the squared
volatility processes of the OU-process and the COGARCH process are self-
decomposable.
Proof. We only need to show the result for σ2
∞. The process (Xt)t≥0 defined
in (2.6) is spectrally negative. Further, Xt →+∞a.s. as t →∞as a conse-
quence of (3.4) (see [22], proof of Theorem 3.1). From this follows that the
stopping time Th, defined for arbitrary but fixed h > 0 by
Th := inf{t ≥0 : Xt = h},

408
C. Kl¨uppelberg et al.
is almost surely finite. Let Ft be the σ-algebra generated by (Xs)0≤s≤t,
and consider the stopping time σ-algebra FTh. Then by the strong Markov
property of L´evy processes, see Bertoin [6], Proposition 6 of Chapter I,
(XTh+t −XTh)t≥0 is independent of FTh and has the same distribution as
(Xt)t≥0. Writing
σ2
∞
D= β
 ∞
0
e−Xtdt = β
 Th
0
e−Xtdt + β
 ∞
Th
e−Xtdt =: Ah + Bh,
say,
we see that Ah is FTh-measurable and that
Bh = β
 ∞
Th
e−(Xt−Xh)e−XThdt = e−hβ
 ∞
Th
e−(Xt−XTh)dt
is independent of Ah and has the same distribution as e−hσ2
∞. Thus we have
for every h > 0,
σ2
∞
D= Ah + e−hσ2
∞
with Ah and σ2
∞being independent, showing that σ2
∞is self-decomposable.
The self-decomposability of σ2
∞is somewhat surprising, for
 ∞
0
e−Xtdt
does not even need to be infinitely divisible for every L´evy process Xt tending
to +∞a.s. For example, if Xt = Nt+ct, t ≥0, with a Poisson process (Nt)t≥0
and a constant c > 0, then
0 ≤
 ∞
0
e−Xtdt =
 ∞
0
e−Nt−ctdt ≤
 ∞
0
e−ctdt = 1/c,
showing that
 ∞
0
e−Xtdt is not infinitely divisible as a bounded non-constant
random variable (see Sato [24], Corollary 24.4). This example was constructed
by Samorodnitsky [27].
As a self-decomposable distribution, σ2
∞has a density, l say. Moreover, if
EL2
1 < ∞, then l is infinitely many times differentiable on (β/(−log δ), ∞)
and satisfies the integro-differential equation
((−log δ)x −β)l(x)
=
 x
β/(−log δ)
ΠL

{y ∈R : |y| >

(x
v −1)δ/λ}

l(v) dv, x >
β
−log δ .
This follows from Proposition 2.1 of Carmona, Petit and Yor [10]. In Sec-
tion 5.3 we shall derive another property of σ2
∞, showing that its distribution
has Pareto like tails under suitable conditions.
5.2 Conditional distributions and tail behaviour of the OU process
Since the price process ( *Gt)t≥0 in the model of Barndorff-Nielsen and Shep-
hard [2, 3] is driven by a Brownian motion independent of the volatility, it

COGARCH versus Ornstein–Uhlenbeck models
409
is not surprising that conditional returns are normally distributed. More pre-
cisely, for t ≥0, r > 0, let *G(r)
t
= *Gt+r −*Gt as in Section 2, and set
(*σ2∗
t )(r) :=
 t+r
t
*σ2
s ds,
i.e. the increments of length r of the integrated squared volatility. Then the
conditional distribution of *G(r)
t
given (*σ2∗
t )(r) is normal, more precisely
*G(r)
t |(*σ2∗
t )(r) ∼N(µr + b(*σ2∗
t )(r), (*σ2∗
t )(r)),
(5.3)
see [3], page 170. This is one indication of the fundamental importance of the
integrated squared volatility in stochastic volatility models.
For the COGARCH process no easy expression for the returns of the price
process is known. However, if (Lt)t≥0 has Gaussian part τ 2
L, drift γL,0 and
finite L´evy measure coming from a compound Poisson process with jump
times T1 < T2 < . . . and jump distribution ρ = ΠL/ΠL(R), then from ∆GTj =
σTj∆LTj follows
∆GTj|σTj ∼ρ.
For the increments between two jumps, observe that (with (τ 2
LWs)s≥0 denoting
the Brownian motion component of (Lt)t≥0)
GTj+1−−GTj−
= ∆GTj + GTj+1−−GTj
= σTj∆LTj + γL,0
 Tj+1
Tj
σs ds + τ 2
L
 Tj+1
Tj
σs dWs.
In particular, it can be seen that GTj+1−−GTj−, conditioned on Tj+1 −Tj,
σTj and ∆LTj, is normally distributed.
The tail behaviour of *σ2
∞in the OU model depends heavily on the driving
L´evy process (Lt)t≥0. Recall that the L´evy density of *σ2
∞and the tail of the
L´evy measure of L1 are connected by the simple formula (5.2). Since any pos-
itive self-decomposable distribution can occur as *σ2
∞, this allows for many dif-
ferent tail behaviours. For example, if k+(x) in (5.1) is chosen to decrease like
x−κ as x →∞where κ > 0, then limx→∞xκP(*σ2
∞> x) = 1/κ, see Embrechts
and Goldie [14] or also Embrechts, Goldie and Veraverbeke [15] in this context.
On the other hand, if *σ2
∞is generalized inverse Gaussian GIG(a1, a2, a3), then
it has a probability density given by f(x) = cxa1−1 exp{−a2
2x−1/2 −a2
3x/2},
x > 0, with a positive constant c (see, e.g., [3], page 173), so it will not have
Pareto like tails unless a3 = 0.
For *Gt, from (5.3) it should be expected that the tail behaviour of
 t
0 *σ2
sds
carries somehow over to the tail behaviour of *Gt. In order to get insight into
the tail behaviour of
 t
0 *σ2
sds, Barndorff-Nielsen and Shephard [5], equation
(31), give a formula for the L´evy density v of
 t
0 *σ2
sds in terms of the L´evy

410
C. Kl¨uppelberg et al.
density of L1 (provided L1 has a L´evy density; infinite divisibility of the in-
tegrated squared volatility can be seen from equation (4) in [5] and the fact
that the class of infinitely divisible distributions is closed under convolution
and weak convergence). In particular, if either L1 or *σ2
∞is tempered sta-
ble or gamma distributed, it is shown that v(x) behaves asymptotically like
d1x−d2 exp{−d3x} as x →∞, where d1, d3 > 0, d2 ∈[1, 3), see [5], Table 3. In
particular, Pareto like tails of *Gt are not to be expected in these cases. This
is in contrast to the COGARCH process, as will be shown next.
5.3 Tail behaviour of the COGARCH process
We now concentrate on the tail behaviour of the COGARCH process, and
show that both the tail of the stationary volatility σ∞as well as the tail of
Gt are Pareto like under weak assumptions, given in terms of the parameters
δ, λ and the driving L´evy process (Lt)t≥0. Recall the notion of Ψ(κ) from
Lemma 4.1. Also, for x ≥0, denote log+ x = log(max{x, 1}). Further, as in
Section 4, we assume λ > 0 throughout to avoid a deterministic volatility.
We start with the tail behaviour of σ2
∞. It can be derived by a simple
transformation applied to Lemma 4 of Rivero [26]. For completeness, we shall
not deduce it from his result, but rather include a short proof along the lines
of [26].
Theorem 5.2. [Pareto tail behaviour of σ]
Suppose there is κ > 0 such that
E|L1|2κ log+ |L1| < ∞
and
Ψ(κ) = 0.
(5.4)
Let (σ2
t )t≥0 be the stationary version of the squared volatility process (which
exists by Lemma 4.1(d)). Then there is a constant C > 0 (which does not
depend on t) such that, for any t ≥0,
lim
x→∞xκP(σ2
t > x) = C.
(5.5)
Proof. From (2.7) it is seen that the volatility process (σ2
t )t≥0 satisfies
σ2
t = e−Xt−σ2
0 + β
 t
0
eXs−Xt−ds,
t > 0,
where σ2
0 is independent of

e−Xt−, β
 t
0 eXs−Xt−ds

by definition of the
COGARCH volatility. Thus (since σ2
0
D= σ2
t
D= σ2
∞) the stationary solution
σ2
∞satisfies for every t > 0 the distributional fixed point equation
σ2
∞
D= Mtσ2
∞+ Qt,
where σ2
∞is independent of (Mt, Qt) and

COGARCH versus Ornstein–Uhlenbeck models
411
Mt
D= e−Xt,
Qt
D= β
 t
0
e−Xs ds.
The claim then follows from Theorem 4.1 in Goldie [18], once we have shown
that there is some t > 0 such that
(i) For no r > 0 is the law of −Xt concentrated on rZ
(ii) E|Mt|κ = 1
(iii)E|Mt|κ log+ |Mt| < ∞
(iv)E|Qt|κ < ∞.
To show (i), recall that (−Xs)s≥0 is a L´evy process of finite variation
with drift γ0,−X1 := γ0,−X = log δ, zero Gaussian component and non-zero
L´evy measure Π−X1 := Π−X being concentrated on (0, ∞). The character-
istic triplet of the L´evy process (−Xs)s≥0 is the characteristic triplet of the
infinitely divisible distribution −X1. For fixed t, the characteristic triplet of
−Xt is t times the characteristic triplet of −X1. In particular, the drift and
L´evy measure of −Xt satisfy γ0,−Xt = tγ0,−X1 and Π−Xt = tΠ−X1. Now let
r > 0. Then −Xt is supported on rZ if and only if −r−1Xt is supported on
Z, which is equivalent to −r−1Xt having drift γ0,−r−1Xt in Z and its L´evy
measure being supported on Z, see Sato [24], Corollary 24.6. In terms of −Xt
this is equivalent to r−1t log δ ∈Z and Π−Xt being supported on rZ. Since
the supports of the L´evy measures Π−X1 and Π−Xt are the same for every
t > 0, but since the drift terms differ by a factor t, there cannot exist positive
numbers r1 and r2 such that
r−1
1
log δ ∈Z,
supp (Π−X1) ⊂r1Z,
r−1
2
√
2 log δ ∈Z
and
supp (Π−X√
2) ⊂r2Z.
This gives (i), by chosing t either equal to 1 or to
√
2.
For (ii), note that
E|Mt|κ = exp{log Ee−κXt} = exp{tΨ(κ)} = 1
by assumption. Furthermore, E max(0, −Xt)e−κXt
< ∞if and only if

x>1 xeκxΠ−X(dx) < ∞, see Sato [24], Theorem 25.3. Using the fact that
ΠX is the image measure of ΠL under the transformation R →(−∞, 0],
y →−log(1 + (λ/δ)y2), this is equivalent to

|y|>√
(e−1)δ/λ

1 + λ
δ y2
κ
log

1 + λ
δ y2

ΠL(dy) < ∞,
which again is equivalent to E|L1|2κ log+ L2
1 < ∞, showing (iii).
From (3.6) follows −Xt ≥t log δ. Thus Ee−κXt < ∞implies Eeκ|Xt| < ∞,
giving E exp{κ sup0≤s≤t |Xs|} < ∞, see Sato [24], Theorem 25.18. Claim (iv)
then follows from
E|Qt|κ = βκE
 t
0
e−Xs ds
κ
≤(βt)κE exp{κ sup
0≤s≤t
|Xs|} < ∞.

412
C. Kl¨uppelberg et al.
A sufficient condition for (5.4) to hold is:
Proposition 5.1. [A sufficient condition]
Suppose that (3.4) holds. Let D := {d ∈[0, ∞) : E|L1|2d < ∞} and d0 :=
sup D ∈[0, ∞]. Suppose that d0 ̸∈D, or that there is θ0 > 0 such that
0 < Ψ(θ0) < ∞. Then (5.4) holds.
Proof. Suppose d0 ̸∈D. Then d0 > 0 and D is an interval containing [0, ε)
for some ε > 0. Lemma 4.1 shows that Ψ(d) is finite for d ∈D, while
limdրd0 Ψ(d) = Ψ(d0) = +∞. This follows by application of Fatou’s Lemma
to (4.1). Choose θ0 ∈(0, d0) such that Ψ(θ0) > 0. Now Ψ is C1 on (0, θ0), and
it follows from (4.1) that
Ψ ′(d) = log δ +

R

1 + λ
δ y2
d
log

1 + λ
δ y2

ΠL(dy)
for 0 < d < d0. Letting d ց 0, it follows that
lim
dց0 Ψ ′(d) = log δ +

R
log

1 + λ
δ y2

ΠL(dy) < 0
by (3.4). Since Ψ(0) = 0 and Ψ is continuous on [0, θ0), it follows that there
is θ1 > 0 such that Ψ(θ1) < 0, and hence there exists κ ∈(θ1, θ0) such that
Ψ(κ) = 0. Since 0 < κ < θ0 < d0, finiteness of E|L1|2θ0 implies finiteness of
E|L1|2κ log+ |L1|.
If there is a θ0 > 0 such that 0 < Ψ(θ0) < ∞then (4.1) shows that
E|L1|2θ0 < ∞, so θ0 ∈D. We then find κ > 0 such that Ψ(κ) = 0 as before.
Example 1. (a) Let 0 < δ < 1, λ > 0, and suppose that (3.4) holds. Then if all
moments of L1 exist, or if |L1| has a Pareto like tail, then σ2
∞has Pareto like
tail. This follows readily from Proposition 5.1 and Theorem 5.2. For example
when L1 is generalized inverse Gaussian GIG(a1, a2, a3) with a3 > 0 (see
Section 5.2), then all moments of L1 exist.
(b) Suppose that E|L1|2d < ∞for some d > 0. Then for every κ ∈(0, d) there
exist δκ ∈(0, 1) and λκ > 0 such that σ2
∞exists and has Pareto like tails. To
see this, define
δκ := λκ := exp

−1
κ

R

(1 + y2)κ −1

ΠL(dy)

.
Then δκ ∈(0, 1) and with these parameters, Ψ(κ) = 0. The claim then follows
from Theorem 5.2.
Our next aim is to show how the Pareto like tail of σ2
∞carries over to
a Pareto like tail of the distribution of Gt for the COGARCH process itself.
Before we start proving this, we need the following two lemmas. The first is
well known, but for convenience we outline a short proof. Note that no inde-
pendence assumptions are made. For the definition and properties of regularly
varying functions we refer to Bingham et al. [8], or also Feller [17].

COGARCH versus Ornstein–Uhlenbeck models
413
Lemma 5.1. Let Y and Z be random variables an a common probability space
such that Y has regularly varying right tail with index −κ < 0. Let d > κ and
suppose that E|Z|d < ∞. Then
lim
x→∞
P(Y + Z > x)
P(Y > x)
= 1.
Proof. E|Z|d < ∞implies limx→∞xd′P(|Z| > x) = 0 for every d′ < d, so
limx→∞
P (|Z|>x)
P (Y >x) = 0. Then lim supx→∞
P (Y +Z>x)
P (Y >x)
≤1 follows from
P(Y + Z > x) ≤P(Y > x(1 −ε)) + P(Z > xε),
x > 0,
ε > 0.
To show lim infx→∞
P (Y +Z>x)
P (Y >x)
≥1, note that for arbitrary ε > 0,
P(Y +Z > x) ≥P(Y > (1+ε)x, Z > −εx) ≥P(Y > (1+ε)x)−P(Z ≤−εx)),
so that
lim inf
x→∞
P(Y + Z > x)
P(Y > x)
≥lim
n→∞
P(Y > (1 + ε)x)
P(Y > x)
−lim sup
x→∞
P(Z ≤−εx)
P(Y > x)
= (1 + ε)−κ.
The following lemma seems intuitively clear. However, its proof requires
some technicalities.
Lemma 5.2. Let (Lt)t≥0 be a L´evy process of finite variation, and let Xt be
given by (2.6). Let θ > 0 and t0 > 0. Then P
 t0
0 e−θXs−dLs > 0

> 0 if
and only if (−Lt)t≥0 is not a subordinator.
Proof. For simplicity in notation we assume θ = 1 throughout. It is clear that
if (−Lt)t≥0 is a subordinator, then P
 t0
0 e−Xs−dLs > 0

= 0, so we only
have to prove the converse. So suppose that (Lt)t≥0, with L´evy measure ν and
drift γ0, is not the negative of a subordinator. Suppose first that ν|(0,∞) ̸= 0.
Then there are 0 < a < b < ∞such that ν|(a,b) > 0.
Let t0 > 0 be fixed. Let 0 < ε < min{1/2, a, t0} and k ∈N0. Define the
sets B1,ε, B2,ε and B3,ε,k by
B1,ε :=


ω :

0<s≤t0−ε
|∆Ls(ω)| < ε


,
B2,ε :=


ω :

t0−ε<s≤t0,|∆Ls(ω)|≤a
|∆Ls(ω)| < ε


,
B3,ε,k := {ω : ∆Ls(ω) ∈(a, b) happens for exactly k values of s in (t0 −ε, t0]}
∩{ω : ∆Ls(ω) ∈R \ [−a, b) never happens for s in (t0 −ε, t0]} .

414
C. Kl¨uppelberg et al.
Since (Lt)t≥0 is of finite variation and ν(a, b) > 0, it follows that P(B1,ε) >
0, P(B2,ε) > 0 and P(B3,ε,k) > 0 (see Sato [24], Theorems 21.9 and 24.10).
Moreover, since (Ls)0≤s≤t0−ε and (Ls −Lt0−ε)s≥t0−ε are independent and
since for any L´evy process the occurence of large jumps is independent from
the occurence of small jumps, it follows that B1,ε, B2,ε and B3,ε,k are all
independent. In particular, for Bε,k := B1,ε ∩B2,ε ∩B3,ε,k it follows that
P(Bε,k) > 0.
From (2.6) follows, for any t > 0,
t log δ ≤−Xt ≤

0<s≤t
log

1 + λ
δ (∆Ls)2

.
In particular, on the set Bε,k,
−Xt ≤λ
δ

0<s≤t
(∆Ls)2 ≤λ
δ

0<s≤t0−ε
|∆Ls| ≤λε
δ ≤λ
δ ,
0 ≤t ≤t0 −ε,
−Xt ≤

0<s≤t
log

1 + λ
δ (∆Ls)2

≤λ
δ + k log

1 + λ
δ b2

,
t0 −ε < t ≤t0.
Setting c1 := et0 log δ and c2 := eλ/δ, we obtain for 0 < ε < min{1/2, a, t0}
and k ∈N0 on the set Bε,k,
c1 ≤e−Xs−≤

c2,
for s ≤t0 −ε,
c2

1 + λ
δ b2k ,
for t0 −ε < s ≤t0.
From this we derive on Bε,k the estimate
 t0
0
e−Xs−dLs
=



0<s≤t0−ε
+

t0−ε<s≤t0,|∆Ls|≤a
+

t0−ε<s≤t0,∆Ls∈(a,b)

e−Xs−∆Ls
+γ0
 t0−ε
0
e−Xs−ds + γ0
 t0
t0−ε
e−Xs−ds
≥−c2ε −c2

1 + λ
δ b2
k
ε + kc1a −|γ0|c2t0 −|γ0|c2

1 + λ
δ b2
k
ε.
Choosing k so large such that kc1a−|γ0|c2t0 > 0 and then ε sufficiently small,
the last estimate will be strictly positive and we obtain for such ε and k that
 t0
0 e−Xs−(ω) dLs(ω) > 0 for ω ∈Bε,k. Since P(Bε,k) > 0, the claim follows
for ν|(0,∞) ̸= 0.
Now suppose that ν|(0,∞) = 0. Since (−Lt)t≥0 is not a subordinator,
the drift γ0 of (Lt)t≥0 must be strictly positive. Define the set Dε,k as

