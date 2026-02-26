# Advanced Topics: Affine Processes & Optimal Stopping (Festschrift)

!!! info "Source"
    **From Stochastic Calculus to Mathematical Finance: The Shiryaev Festschrift** edited by Yu. Kabanov, R. Liptser, and J. Stoyanov, Springer, 2006.
    These notes are used for educational purposes.

## Affine Processes and Optimal Stopping

COGARCH versus Ornstein–Uhlenbeck models
415
/
ω : 
0<s≤t0 |∆Ls(ω)| < ε
0
. Then P(Dε,k) > 0, and with c1 and c2 as before
it is the case that, on Dε,k,
 t0
0
e−Xs−dLs =

0<s≤t0
e−Xs−∆Ls + γ0
 t0
0
e−Xs−ds ≥−c2ε + γ0c1t0,
showing that P
 t0
0 e−Xs−dLs > 0

> 0 when ε < γ0c1t0/c2.
The following theorem now gives the Pareto type tail behaviour of Gt.
We need slightly more stringent moment conditions than in Theorem 5.2, and
assume that the driving L´evy process is of finite variation.
Theorem 5.3. [Tail behaviour of G]
Suppose there is κ > 0 and d > 4κ such that
E|L1|d < ∞
and
Ψ(κ) = 0.
(5.6)
Suppose further that (Lt)t≥0 is of finite variation. Let (σ2
t )t≥0 be the stationary
version of the volatility process, and Gt =
 t
0 σs dLs the corresponding CO-
GARCH process. Then if (−Lt)t≥0 is not a subordinator, for every t > 0 there
exists a positive constant C1,t such that
lim
x→∞x2κP(Gt > x) = C1,t,
and if (−Lt)t≥0 is a subordinator, then Gt ≤0 a.s. Similarly, if (Lt)t≥0 is
not a subordinator, then there exists C2,t > 0 such that
lim
x→∞x2κP(Gt ≤−x) = C2,t,
and if (Lt)t≥0 is a subordinator, then Gt ≥0 a.s.
Proof. For s ≤t, define
As := e−Xs−,
Bs := β
 s
0
eXu−Xs−du.
Then from (2.7)
σs =
H
Asσ2
0 + Bs =

Asσ0 +
Bs

Asσ2
0 + Bs +

Asσ2
0
.
Defining
Yt := σ0
 t
0

As dLs,
ζs :=
Bs

Asσ2
0 + Bs +

Asσ2
0
,
and
Zt :=
 t
0
ζs dLs,

416
C. Kl¨uppelberg et al.
we obtain
Gt =
 t
0
σsdLs = Yt + Zt,
t > 0.
From Theorem 5.2 we know that limx→∞x2κP(σ0 > x) = C for some
positive constant C. Suppose we show that there is an d′ > 2κ such that
E

 t
0
√As dLs

d′
< ∞. Then a classical result of Breiman [9], using the in-
dependence of σ0 and
 t
0
√As dLs, yields the existence of strictly positive
constants C1,t, C2,t such that
lim
x→∞x2κP(Yt > x) = C1,t,
lim
x→∞x2κP(Yt ≤−x) = C2,t,
(5.7)
provided P
 t
0
√As dLs > 0

> 0 and P
 t
0
√As dLs < 0

> 0, respectively.
We shall verify the required moment condition with d′ := d/2. Note that

 t
0

As dLs
 ≤sup
0≤s≤t
e−Xs/2 ∥Lt∥TV,
where ∥Lt∥TV denotes the total variation of (Ls)0≤s≤t on [0, t], and we also
have that E sup0≤s≤t e−d′Xs < ∞since Ee−d′X1 < ∞(as in the proof of
Theorem 5.2), and that E∥Lt∥2d′
TV is finite since E|L1|2d′ is finite by assumption
(see Sato [24], Theorem 21.9); also, it follows from H¨older’s inequality that
E

sup
0≤s≤t
e−Xs/2∥Lt∥TV
d′
≤

E sup
0≤s≤t
e−d′Xs
1/2 
E∥Lt∥2d′
TV
1/2
< ∞.
So the moment condition is established, with d′ = d/2 > 2κ.
To get an estimate for Zt, note that Xu ≤−u log δ by (2.6), so that for
0 ≤s ≤t,
ζs ≤

Bs =

β

As
> s
0
eXu du ≤

β
√
tδ−t
As.
This implies, with d′ as above,
E|Zt|d′ ≤βd′/2td′/2δ−d′t/2E
 sup
0≤s≤t
e−Xs/2∥Lt∥TV

d′
< ∞,
as already shown. Now if P
 t
0
√As dLs > 0

> 0, i.e. (−Lt)t≥0 is not a
subordinator by Lemma 5.2, an application of Lemma 5.1 to (5.7) gives the
result. On the other hand, if P
 t
0
√As dLs > 0

= 0, i.e. if (−Lt)t≥0 is a
subordinator, then also Gt =
 t
0 σs dLs ≤0 a.s. The assertion for the left tail
behaviour of Gt follows similarly.

COGARCH versus Ornstein–Uhlenbeck models
417
Examples for the application of Theorem 5.3, similar to Example 1(a) in
the case when all moments of L1 exist, or Example 1(b) can be easily stated.
We conclude this section with the observation that with the same methods of
proof the tail behaviour of the integrated squared volatility can be determined.
Here, a weaker moment condition is sufficient:
Proposition 5.2. [Tail behaviour of the integrated squared volatility]
Let the conditions of Theorem 5.2 be satisfied. In addition assume that there
is d > 2κ such that E|L1|d < ∞. Let (σ2
t )t≥0 be the stationary version. Then,
for any t > 0 there is a constant Ct > 0 such that
lim
x→∞xκP
 t
0
σ2
sds > x

= Ct.
6 Conclusion
We have compared the probabilistic properties of both the stochastic volatil-
ity model of Barndorff-Nielsen and Shephard and the COGARCH process.
Both volatility models are positive Markov processes, which exhibit jumps
and decrease exponentially between jumps. Although the log price process is
defined in terms of an independent Brownian motion for the OU model and
in terms of the same driving L´evy process for the COGARCH process, the
autocorrelation structure of the returns is similar for both processes. Further-
more, we have seen that the tail behaviour in the OU model depends heavily
on the driving L´evy process, while for the COGARCH model Pareto like tails
occur in most cases under weak regularity conditions.
Acknowledgements
We thank Marc Yor and Victor Rivero for interesting discussions and their
considerable efforts concerning the tail behaviour of the COGARCH model.
Further, we thank Gennady Samorodnitsky for answering the question if the
stationary distribution of the COGARCH process is self-decomposable, and
for his generosity in allowing us to include this result in Theorem 5.1.
Thanks also to Ole Barndorff-Nielsen for helpful comments on the paper, and
in particular for drawing our attention to the quadratic variation of the CO-
GARCH process, which led to Proposition 3.3.
Parts of this research were carried out while A. Lindner was visiting the Cen-
tre for Mathematical Analysis and the School of Finance & Applied Statistics
at ANU in Canberra. He takes pleasure in thanking both for their hospitality.
This research was partially supported by ARC grant DP0210572. A. Lindner
was supported by the German Science Foundation (Deutsche Forschungsge-
meinschaft).

418
C. Kl¨uppelberg et al.
References
1. Barndorff-Nielsen, O.E.: Superposition of Ornstein-Uhlenbeck type processes.
Theory Probab. Appl. 45, 175–194 (2001)
2. Barndorff-Nielsen, O.E., Shephard, N.: Modelling by L´evy processes for financial
econometrics. In: O.E. Barndorff-Nielsen, T. Mikosch, S. Resnick (Eds.), L´evy
processes, theory and applications, pp. 283–318. Boston: Birkh¨auser 2001
3. Barndorff-Nielsen, O.E., Shephard, N.: Non–Gaussian Ornstein–Uhlenbeck–
based models and some of their uses in financial economics (with discussion).
J. R. Statist. Soc. Ser. B 63, 167–241 (2001)
4. Barndorff-Nielsen, O.E., Shephard, N.: Econometric analysis of realised volatil-
ity and its use in estimating stochastic volatility models. J. R. Statis. Soc. Ser.
B 64, 253–280 (2002)
5. Barndorff-Nielsen, O.E., Shephard, N.: Integrated OU processes and non-
Gaussian OU-based stochastic volatility models. Scand. J. Statist. 30, 277–295
(2003)
6. Bertoin, J.: L´evy Processes. Cambridge: Cambridge University Press 1996
7. Bertoin, J., Yor, M.: On the entire moments of self-similar Markov processes
and exponential functionals of L´evy processes. Ann. Fac. Sci. Toulouse Math.
(6) 11, 33–45 (2002)
8. Bingham, N.H., Goldie, C.M., Teugels, J.L.: Regular Variation. Cambridge:
Cambridge University Press 1987
9. Breiman, L.: On some limit theorems similar to the arc-sine law. Theory Probab.
Appl. 10, 323–331 (1965)
10. Carmona, P., Petit, F., Yor, M.: On the distribution and asympotic results for
exponential functionals of L´evy processes. In: M. Yor (Ed.), Exponential func-
tionals and principal values related to Brownian motion, pp. 73–121. Madrid:
Biblioteca de le Revista Matem`atica Iberoamericana 1997
11. Carmona, P., Petit, F., Yor, M.: Exponential functionals of L´evy processes. In:
O.E. Barndorff-Nielsen, T. Mikosch, S. Resnick (Eds.), L´evy Processes, Theory
and Applications, pp. 41–55. Boston: Birkh¨auser 2001
12. Duan, J.C.: Augmented GARCH(p,q) process and its diffusion limit. J. of Econo-
metrics 79, 97–127 (1997)
13. Engle, R.F.: ARCH: selected readings. Oxford: Oxford University Press 1995
14. Embrechts, P., Goldie, C.M.: On convolution tails. Stoch. Proc. Appl. 13, 263–
278 (1982)
15. Embrechts, P., Goldie, C.M., Veraverbeke, N.: Subexponentiality and infinite
divisibility. Zeit. Wahrsch. Verw. Gebiete 49, 335–347 (1979)
16. Erickson, K.B., Maller, R.A.: Generalised Ornstein–Uhlenbeck processes and
the convergence of L´evy integrals. In: M. Emery, M. Ledoux, M. Yor (Eds.),
Seminaire de Probabilites XXXIII, pp. 70–94, Lect. Notes Math. 1857. Berlin:
Springer 2004.
17. Feller, W.: An Introduction to Probability Theory and its Applications II. New
York: Wiley 1971
18. Goldie, C.M.: Implicit renewal theory and tails of solutions of random equations.
Ann. Appl. Probab. 1(1), 126–166 (1991)
19. Jacod, J. and Shiryaev, A.N.: Limit Theorems for Stochastic Processes. 2nd edn.
Heidelberg: Springer 2003
20. Jeantheau, T.: A link between complete models with stochastic volatility and
ARCH models. Finance Stochast. 8, 111–131 (2004)

COGARCH versus Ornstein–Uhlenbeck models
419
21. Kim, S., Shephard, N., Chib, S.: Stochastic volatility: likelihood inference and
comparison with ARCH models. Review of Economic Studies 65, 361–393 (1998)
22. Kl¨uppelberg, C., Lindner, A., Maller, R.: A continuous time GARCH process
driven by a L´evy process: stationarity and second order behaviour. J. Appl.
Probab. 41(3) (to appear) (2004)
23. Nelson, D.B.: ARCH models as diffusion approximations. J. of Econometrics
45, 7–38 (1990)
24. Sato, K.-I.: L´evy Processes and Infinitely Divisible Distributions. Cambridge:
Cambridge University Press 1999
25. Shephard, N.: Stochastic Volatility: Selected Readings. Oxford: Oxford Univer-
sity Press 2004
26. Rivero, V.: Recurrent extensions of self-similar Markov processes and Cram´er’s
condition. Bernoulli (to appear) (2005).
27. Samorodnitsky, G.: Private communication (2004)
28. Wang, Y.: Asymptotic nonequivalence of GARCH models and diffusions. Ann.
Statist. 30, 754–783 (2002)


Tail Distributions of Supremum and Quadratic
Variation of Local Martingales
Robert LIPTSER1 and Alexander NOVIKOV2
1 Electrical Engineering-Systems, Tel Aviv University, 69978 Tel Aviv Israel,
Institute of Information Transmission, Moscow, Russia.
liptser@eng.tau.ac.il
2 School of Mathematical Sciences, UTS, NSW 2007, Australia.
prob@maths.uts.edu.au
Summary. We extend some known results concerning the tail distribution of supre-
mum and quadratic variation of a continuous local martingale to the case of locally
square integrable martingales with bounded jumps. The predictable and optional
quadratic variations are involved in the main result.
Key words: tail distribution, martingale supremum, quadratic variation
Mathematics Subject Classification (2000): 60G44, 60HXX, 40E05
1 Introduction and main result
Let M = (Mt)t≥0 be a local martingale starting from zero and with paths in
the Skorohod space D[0,∞). We assume that it is defined on a stochastic basis
(Ω, F, (Ft)t≥0, P) with usual conditions. We shall use the standard notation
Mloc for the class of local martingales and M2
loc Mc, M, M2 for its subclasses.
Recall that a adapted process X with paths in D[0,∞) defined on this
stochastic basis belongs to the class D if the family (Xτ, τ ∈T ), where T is
the set of stopping times τ, is uniformly integrable.
Henceforth △Mt := Mt −Mt−, ⟨M⟩t and [M, M]t denote the jumps,
predictable quadratic variation and optional quadratic variation of M.
It is well-known (see, e.g., [9], [7] and references therein) that for any
M ∈M2
loc:
⟨M⟩∞< ∞a.s. ⇒

[M, M]∞< ∞a.s.
lim
t→∞Mt = M∞∈R a.s.
(1.1)

422
R. Liptser and A. Novikov
There are many other remarkable relations between M∞and ⟨M⟩∞(e.g.,
Burkholder–Gundy–Davis’s inequalities, law of large numbers for martingales,
etc.). For M ∈M ∩D we have the Wald equality
EM∞= 0,
which plays a fundamental role in many applications of the stochastic calculus.
Recall that the condition E⟨M⟩∞< ∞implies that M ∈M2 and notice
that ⟨M⟩∞< ∞̸⇒M ∈M. However, the condition ⟨M⟩∞< ∞, implying the
existence of the limit value M∞(see, (1.1)), jointly with EM∞= 0 ensures
M ∈M. One may ask which condition on ⟨M⟩∞can provide the equality
EM∞= 0? A positive answer for M ∈Mc
loc with ⟨M⟩∞< ∞is known from
Novikov, [10], and Elworthy, Li and Yor, [2], under the additional assumption:
EeεM+
∞< ∞for sufficiently small ε > 0,
lim
λ→∞λP

⟨M⟩1/2
∞> λ

= 0.
More precisely, the following statement is valid.
Theorem. ([10]) Let M ∈Mc
loc and ⟨M⟩∞< ∞. Assume supt>0 EeεMt < ∞
for some sufficiently small ε > 0. Then:
0 ≤EM∞≤EM +
∞< ∞,
lim
λ→∞λP

⟨M⟩1/2
∞> λ

=

2
π EM∞.
For related topics see Az´ema, Gundy and Yor [1], Gundy [5], Galtchouk
and Novikov [6], Takaoka, [14], Peskir and Shiryaev [13], and Vondra˘cek [15]).
The aim of this paper is to extend the statement of this Theorem for local
martingales with bounded jumps.
Theorem 1.1. Let M ∈M2
loc, ⟨M⟩∞< ∞and M + ∈D. Then
(i) M∞= limt→∞Mt possesses the following properties:
0 ≤EM∞≤EM +
∞< ∞;
(ii) the uniform integrability of (|△Mt|)t>0 and (i) imply
lim
λ→∞λP

sup
t≥0
M −
t > λ

= EM∞;
(iii) |△M| ≤K and EeεM∞< ∞for some K > 0 and sufficiently small
ε > 0 imply
lim
λ→∞λP

⟨M⟩1/2
∞> λ

= lim
λ→∞λP

[M, M]1/2
∞> λ

=

2
π EM∞.

Tail Distributions of Supremum and Quadratic Variation
423
For M + ∈D, Theorem 1.1 gives necessary and sufficient conditions for
M ∈M expressed in terms of supt≥0 M −
t , ⟨M⟩∞, and [M, M]∞. Concerning
an effectiveness of these conditions see Jacod and Shiryaev [8].
Corollary 1.1. Under the assumptions of Theorem 1.1, the process M ∈M
iffany of the following conditions hold:
lim
λ→∞λP

sup
t≥0
M −
t > λ

= 0,
lim
λ→∞λP

⟨M⟩1/2
∞> λ

= 0,
lim
λ→∞λP

[M, M]1/2
∞> λ

= 0.
The proofs of statements (i) and (ii) of Theorem 1.1 are obvious and
might even be known. The proof of (iii) exploits a combination of techniques:
“Stochastic exponential + Tauberian theorem”
used by Novikov in [11] and [12].
The necessary information on the stochastic exponential is gathered in
Section 2. The proof of Theorem 1.1 is given in Section 3. We mention also a
result, formulating in Theorem 3.1 (Section 3), presenting conditions alterna-
tive to |△M| ≤K.
2 Stochastic exponential
We start with recalling necessary notions and objects (for details see, e.g., [9]
or [7]).
For any M ∈M2
loc we have the decomposition M = M c + M d where
M c, M d ∈M2
loc are continuous and purely discontinuous martingales, re-
spectively. Since ⟨M⟩= ⟨M c⟩+ ⟨M d⟩, the assumption ⟨M⟩∞< ∞implies
⟨M c⟩∞< ∞, ⟨M d⟩∞< ∞. The jump process △M ≡△M d generates the
integer-valued measure µ = µ(dt, dz) with µ((0, t] × A) = 
s≤t
I(△Ms ∈A).
We denote by ν = ν(dt, dz) the compensator of µ. The condition |△M| ≤K
guarantees the existence of a version ν such that ν(R+ ×{|z| > K}) = 0. This
version of ν is used in the sequel.
The purely discontinuous martingale M d can be represented as the Itˆo
integral with respect to µ −ν:
M d
t =
 t
0

|z|≤K
z

µ(ds, dz) −ν(ds, dz)

.
Recall that

|z|≤K zν({t}, dz) = 0 and, so that,

424
R. Liptser and A. Novikov
⟨M d⟩t =
 t
0

|z|≤K
z2ν(ds, dz) < ∞, t > 0.
Hence, ⟨M⟩∞< ∞implies
 ∞
0

|z|≤K z2ν(ds, dz) < ∞and the existence of
the cumulant process (for λ ∈R)
Gt(λ) =
 t
0

|z|≤K

eλz −1 −λz

ν(ds, dz),
△Gt(λ) =

|z|≤K

eλz −1 −λz

ν({t}, dz).
We emphasize that Gt(λ) increases in t ↑to G∞(λ) := limt→∞Gt(λ) < ∞
and △Gt(λ) ≥0.
The process
Et(λ) = exp
λ2
2 ⟨M c⟩t + Gt(λ)
 (
0<s≤t

1 + △Gs(λ)

e−△Gs(λ)
is called “stochastic exponential” for the martingale M. Since △G(λ) ≥0,
the stochastic exponential is nonnegative. A remarkable property of Et(λ) is
that the process
zt(λ) = eλMt−log Et(λ)
(2.1)
is a positive local martingale with respect to the filtration (Ft)t≥0. This prop-
erty is readily verified with the help of Itˆo’s formula applied to (2.1):
dzt(λ) = λzt(λ)dM c
t +

|z|≤K
zt−(λ)

eλz −1

1 + △Gt(λ)(µ −ν)(dt, dz).
As any nonnegative local martingale, zt(λ) is also a supermartingale (see, e.g.,
Problem 1.4.4 in Liptser and Shiryaev [9]) and, therefore, has a finite limit at
infinity
z∞(λ) := lim
t→∞zt(λ) ∈R+
and Ezτ(λ) ≤1 for any stopping time τ. In particular, Ez∞≤1.
Proposition 2.1. Under the conditions from statement (iii) of Theorem 1.1
we have:
1) Ez∞(λ) = 1.
2) E∞(λ) = lim
t→∞Et(λ) ∈(0, ∞).
Proof. 1) Let (τn) be a sequence of stopping times increasing to infinity and
such that (Mt∧τn)t≥0 and (zt∧τn(λ))t≥0 are uniformly integrable martingales
for any n. Then Ezτn(λ) ≡1. By Jensen’s inequality,
E

eλM+
∞|Fτn

≥eλE(M +
∞|Fτn) ≥eλM+
τn ≥zτn(λ).

Tail Distributions of Supremum and Quadratic Variation
425
In other words, the martingale

zτn(λ), Fτn

n≥1 is majorized by the uniformly
integrable martingale

E

eλM+
∞|Fτn

, Fτn

n≥1, that is,

zτn(λ), Fτn

n≥1 is the
uniformly martingale itself. Consequently, 1 = limn→∞Ezτn(λ) = Ez∞(λ).
2) Notice that |M∞| < ∞, E∞(λ) < ∞and z∞(λ) = eλM∞−log E∞(λ) imply
that
1 ≥EI(E∞(λ) = 0)z∞(λ) ≥NP(E∞(λ) = 0)
for any N > 0.
Hence, P(E∞(λ) = 0) = 0.
3 The proof of Theorem 1.1
3.1 The proof of (i) and (ii)
(i) Let (τn)n≥1 be an increasing sequence of stopping times with tending
to infinity and such that (Mτn)n≥1 ∈M. Therefore, EM −
τn −EM +
τn = 0, n ≥1.
By M + ∈D, we have lim
n→∞EM +
τn = EM +
∞< ∞. Further, by the Fatou lemma
limn→∞EM −
τn ≥EM −
∞, so that EM +
∞−EM −
∞≥0.
Hence, EM∞= (EM +
∞−EM −
∞) ≥0.
(ii) Notice that {supt≥0 M −
t > λ} = {Sλ < ∞}, where
Sλ = inf{t : M −
t ≥λ},
inf{∅} = ∞.
Since (|△Mt|)t>0 is uniformly integrable process and M + ∈D, we have
(Mt∧Sλ)t≥0 ∈M, that is,
0 = EMSλ = EM∞I{Sλ=∞} + EMSλI{Sλ<∞}.
We derive the desired statement from the relations
lim
λ→∞EM∞I{Sλ=∞} = EM∞,
lim
λ→∞EMSλI{Sλ<∞} = −λP

sup
t≥0
M −
t > λ

.
(3.1)
By (i), EM −
∞≤EM +
∞< ∞. Consequently, M −
∞< ∞and, therefore, we have
limλ→∞Sλ = ∞. The first part of (3.1) is implied by the inequality
EM∞I{Sλ=∞} −EM∞
 ≤E|M∞|I{Sλ<∞}
and the Lebesgue dominated theorem. The second part in (3.1) follows from
MSλI{Sλ<∞} = −λI{Sλ<∞} + (MSλ + λ)I{Sλ<∞} since
E|MSλ + λ|I{Sλ<∞} ≤E|△MSλ|I{Sλ<∞} ≤KP(Sλ < ∞) −−−−→
λ→∞0.

426
R. Liptser and A. Novikov
3.2 Proof of (iii)
Auxiliary lemmas
Lemma 3.1. Under assumptions from the statement (iii) of Theorem 1.1,
lim
λ↓0 E 1
λ

1 −e−log E∞(λ)
= EM∞.
Proof. With λ ≤ε for ε involved in (iii), by Proposition 2.1 we have the
equality Ez∞(λ) = 1. Hence,
E 1
λ

1 −e−log E∞(λ)
= E 1
λ

z∞(λ) −e−log E∞(λ)
= E 1
λ

eλM∞−1

e−log E∞(λ).
The required statement follows from the relations
lim
λ↓0
1
λe−log E∞(λ)
eλM∞−1

= M∞,
1
λe−log E∞(λ)eλM∞−1
 ≤eεM∞
and EeεM∞< ∞by the Lebesgue dominated theorem.
Lemma 3.2. Under assumptions from the statement (iii) of Theorem 1.1,
lim
λ↓0 E 1
λ

1 −e−λ2
2 ⟨M⟩∞
= EM∞.
Proof. According to Lemma 3.1, it suffices to show that
lim
λ↓0 E 1
λ
e−log E∞(λ) −e−λ2
2 ⟨M⟩∞
 = 0.
(3.2)
The verification of (3.2) uses the following estimates: for some C > 0 and
sufficiently small λ > 0,
0 <

1 −Cλ
λ2
2 ⟨M⟩∞≤log E∞(λ) ≤

1 + Cλ
λ2
2 ⟨M⟩∞.
(3.3)
The estimate from above is implied by log E∞(λ) ≤λ2
2 ⟨M c⟩∞+ G∞(λ)
and the property of ν(dt, dz) to be supported, in z, on [−K, K].
The estimate from below is determined in the following way. Denote by
Φ(λ, K) = 1 −λKeλK and
Gc
∞(λ) =
 ∞
0

|z|≤K

eλz −1 −λz

νc(dt, dz),

Tail Distributions of Supremum and Quadratic Variation
427
where νc(dt, dz) := ν(dt, dz) −ν({t}, dz). Write
log E∞(λ) = λ2
2 ⟨M c⟩∞+ Gc
∞(λ) +

t>0
log

1 + △Gt(λ)

≥λ2
2 ⟨M c⟩∞+ Φ(λ, K)
 ∞
0

|z|≤K
λ2
2 z2νc(dt, dz)
+

t>0
log
	
1 + Φ(λ, K)

|z|≤K
λ2
2 z2ν({t}, dz)

.
(3.4)
We choose λ so small to keep 1 −λKeλK > 0 and estimate from below the
“
t>0 log” in the last line of (3.4) by applying log(1 + x) ≥x −1
2x2, x ≥0.
This gives the lower bound

t>0
log
	
1 + Φ(λ, K)

|z|≤K
λ2
2 z2ν({t}, dz)

≥Φ(λ, K)

|z|≤K
λ2
2 z2ν({t}, dz) −1
2Φ2(λ, K)
	
|z|≤K
λ2
2 z2ν({t}, dz)

2
.
Taking into account ν({t}, |z| ≤K) ≤1, by the Cauchy–Schwarz inequality
we find the upper bound
	
|z|≤K
λ2
2 z2ν({t}, dz)

2
≤λ4
4

|z|≤K
z4ν({t}, dz) ≤λ4K2
4

|z|≤K
z2ν({t}, dz)
providing the inequality

t>0
log
	
1 + Φ(λ, K)

|z|≤K
λ2
2 z2ν({t}, dz)

≥

Φ(λ, K) −λ2
8 K2Φ2(λ, K)
 
|z|≤K
λ2
2 z2ν({t}, dz).
We choose λ so small to keep
Φ(λ, K) −λ2
8 K2Φ2(λ, K) ≥1 −λc > 0
for some constant c > 0.
Now, we may choose a positive constant C such that (3.3) is valid for both
the upper and lower bounds.
From (3.3), we derive that

428
R. Liptser and A. Novikov
1
λ
e−log E∞(λ) −e−λ2
2 ⟨M⟩∞
 ≤C λ2
2 ⟨M⟩∞e−λ2
2 ⟨M⟩∞−−−→
λ→0 0.
and, due to xe−x ≤e−1, it remains to apply the Lebesgue dominated theorem.
Lemma 3.3. Under assumptions from the statement (iii) of Theorem 1.1,
lim
λ→∞λP

⟨M⟩1/2
∞> λ

= ϑ ⇔lim
λ→∞λP

[M, M]1/2
∞> λ

= ϑ.
Proof. Obviously, the desired result holds true if
lim
λ→0
P

[M, M]1/2
∞> λ

P

⟨M⟩1/2
∞> λ

≤1,
lim
λ→0
P

[M, M]1/2
∞> λ

P

⟨M⟩1/2
∞> λ

≥1.
(3.5)
Denote L = [M, M] −⟨M⟩and notice that [M, M]∞≤⟨M⟩∞+ supt≥0 |Lt|.
By an obvious inequality (c + d)1/2 ≤c1/2 + d1/2, we obtain that
P

[M, M]1/2
∞> λ

≤P

[⟨M⟩∞+ sup
t≥0
|Lt|]1/2 > λ

≤P

⟨M⟩1/2
∞+ sup
t≥0
|Lt|1/2 > λ

≤P

⟨M⟩1/2
∞> (1 −a)λ

+ P

sup
t≥0
|Lt| > aλ

, a ∈(0, 1).
With λa = (1 −a)λ, the resulting bound can be rewritten as:
λP

[M, M]1/2
∞> λ

≤(1 −a)−1λaP

⟨M⟩1/2
∞> λa

+ λP

sup
t≥0
|Lt|1/2 > aλ

.
(3.6)
Now, we evaluate from from above P

supt≥0 |Lt|1/2 > aλ

. A helpful tool
here is the inequality: for some C > 0, any stopping time τ and K being a
bound for |△M|,
E sup
t≤τ
|Lt|2 ≤CK2E⟨M⟩τ.
(3.7)
In order to establish (3.7), we use the following facts:
- L is the purely discontinuous local martingale with
[L, L]t =

s≤t
(△Ls)2 =

s≤t

(△Ms)2 −△⟨M⟩s
2
=

s≤t
	
|z|≤K
z2(µ({s}, dz) −ν({s}, dz)

2
,
- ⟨L⟩t =
 t
0

|z|≤K z4(ν(ds, dz) −
s≤t
 
|z|≤K z2ν({s}, dz)
2
,

Tail Distributions of Supremum and Quadratic Variation
429
- ⟨L⟩t ≤
 t
0

|z|≤K
z4ν(ds, dz) ≤K2
 t
0

|z|≤K
z2ν({ds, dz) ≤K2⟨M⟩t,
- K2⟨M⟩−⟨L⟩is the increasing process.
Now, we refer to the Burkholder–Gundy inequality (see, e.g., Theorem 1.9.7
in [9]): for any stopping time τ,
E sup
t≤τ
|Lt|2 ≤CE[L, L]τ.
Due to the relations E[L, L]τ = E⟨L⟩τ and K2⟨M⟩τ ≥⟨L⟩τ (recall that
K2⟨M⟩≥⟨L⟩), we have E⟨L⟩τ ≤K2E⟨M⟩τ, that is, (3.7) is valid.
By (3.7) and the fact that ⟨M⟩is a predictable process, the Lenglart–
Rebolledo inequality (see, e.g., Theorem 1.9.3 in [9]) is applicable (notice that
{supt≥0 |Lt|1/2 > aλ} ≡{supt≥0 |Lt| > a2λ2}), so that,
P

sup
t≥0
|Lt|1/2 > aλ

≤λ5/2
a4λ4 + P

CK2⟨M⟩∞> λ5/2
= λ5/2
a4λ4 + P

⟨M⟩1/2
∞> λ5/4/(C1/2K)

.
Hence, with r = 1/(C1/2K) and λr = rλ5/4,
λP

sup
t≤Tx
|Lt|1/2 > aλ

≤
1
a4λ1/2 +
1
rλ1/4 λrP

⟨M⟩1/2
∞> λr

.
(3.8)
Now, (3.6) and (3.8) imply the inequality
λP

[M, M]1/2
∞> λ

≤(1 −a)−1λaP

⟨M⟩1/2
∞> λa

+
1
a4λ1/2 +
r
λ1/4 λrP

⟨M⟩1/2
∞> λr

.
If ϑ > 0, by
P

[M, M]1/2
∞> λ

P

⟨M⟩1/2
∞> λ

≤(1 −a)−1λaP

⟨M⟩1/2
∞> λa

λP

⟨M⟩1/2
∞> λ

+
1
a4λ1/2 +
r
λ1/4 λrP

⟨M⟩1/2
∞> λr

λP

⟨M⟩1/2
∞> λ

−−−−→
λ→∞
1
1 −a −−−→
a→0 1
and the first part from (3.5) is valid. The second part from (3.5) is established
similarly and we give only a sketch of the proof. The use of the bound
P

⟨M⟩1/2 > λ

≤P

[M, M]1/2 > (1 −a)λ

+ P

sup
t≥0
|Lt| > aλ

, a ∈(0, 1),

430
R. Liptser and A. Novikov
implies that
P

[M, M]⟩1/2
∞> (1 −a)λ

P

⟨M⟩1/2
∞> λ

≥1 −P

supt≥0 |Lt| > aλ

P

⟨M⟩1/2
∞> λ

and we get the result.
If ϑ = 0, we replace M by M + δM ′, where δ > 0 and M ′ ∈Mc with
⟨M ′⟩∞< ∞possessing limλ→∞λP

⟨M ′⟩1/2
∞
> λ

= ϑ′
ϑ′ϑ′ > 0, is independent
of M c. Therefore, by ⟨M + δM ′⟩= ⟨M⟩+ δ2⟨M ′⟩, we have
lim
λ→∞λP

⟨M + δM ′⟩1/2
∞> λ

= δ2ϑ′
ϑ′ϑ′ > 0.
Hence, by using the result already proved, it holds
lim
λ→∞λP

⟨M + δM ′⟩1/2
∞> λ

= δ2ϑ′
ϑ′ϑ′
⇔lim
λ→∞λP

[M + δM ′, M + δM ′]1/2
∞> λ

= δ2ϑ′ϑ′
ϑ′
and, by the arbitrariness of δ,
lim
λ→∞λP

⟨M > λ

= 0 ⇔lim
λ→∞λP

[M, M]1/2
∞> λ

= 0.
Final part of the proof for (iii)
We refer to the Tauberian theorem.
Theorem. (Feller, [4], XIII.5, Example (c)) Let X be a nonnegative random
variable such that lim
λ↓0
1
λ

1 −Ee−λ2
2 X
∈R.
Then,

2
π lim
λ↓0
1
λ

1 −Ee−λ2
2 X
= lim
λ→∞λP(X1/2 > λ).
Letting X = ⟨M⟩∞, we find that

2
π lim
λ↓0
1
λ

1 −Ee−λ2
2 ⟨M⟩∞
= lim
λ→∞λP(⟨M⟩1/2
∞> λ),
while, by Lemmas 3.1, 3.2 and 3.3,
lim
λ↓0
1
λ

1 −Ee−λ2
2 ⟨M⟩∞
=

2
π EM∞,
lim
λ→∞λP

[M, M]1/2
∞> λ

=

2
π EM∞.

Tail Distributions of Supremum and Quadratic Variation
431
3.3 Supplement
The condition |△M| ≤K might be too restrictive to be valid for serving some
examples. Following [10], we show that this condition can be replaced by one
seems to be more suitable for applications.
Theorem 3.1. Assume conditions for the statement (iii) of Theorem 1.1 are
valid except the boundedness |△M| ≤K replaced by the two inequalities
λ2
2 ⟨M⟩∞(1 −|λ|ζ1)+ ≤log E∞(λ) ≤λ2
2 ⟨M⟩∞(1 + |λ|ζ2)
(3.9)
with sufficiently small λ > 0 and nonnegative integrable random variables
ζ1, ζ2.
Then
lim
λ→∞λP

⟨M⟩1/2
∞> λ

=

2
π EM∞.
Proof. Since (3.2) has to be verified only, by (3.9) we have
1
λ
e−log E∞(λ) −e−λ2
2 ⟨M⟩∞
 ≤

ζ2 ∨|1 −(1 −ζ1λ)+|
λ
λ2
2 ⟨M⟩∞e−λ2
2 ⟨M⟩∞
≤

ζ2 ∨ζ1
λ2
2 ⟨M⟩∞e−λ2
2 ⟨M⟩∞.
The right-hand side of this inequality converges to zero, as λ →0, and is
bounded by e−1(ζ2 ∨ζ1). So, (3.2) holds by the Lebesgue dominated theorem.
Acknowledgements
The authors gratefully acknowledge their colleagues J. Stoyanov, E. Shin-
jikashvili and anonymous reviewers for comments improving presentation of
the material.
References
1. Azema, J., Gundy, R.F., Yor, M.: Sur l’int´egrabilit´e uniforme des martingales
continues. S´eminaire de Probabilit`es. XIV, LNM 784, 249–304, Springer (1980)
2. Elworthy, K.D., Li, X.M., Yor, M.: On the tails of the supremum and the
quadratic variation of strictly local martingales. S`eminaire de Probabilit`es
XXXI, Lecture Notes in Math. 1655, 113–125, Springer (1997)
3. Ethier, S.N.: A gambling system and a Markov chain. Ann.Appl.Probab. 6, no.4,
1248–1259 (1996)
4. Feller, W.: An Introduction to Probability and its Applications. 2, 2nd ed. Wiley
(1971)

432
R. Liptser and A. Novikov
5. Gundy, R. F.: On a theorem of F. and M. Riesz and an equation of A. Wald.
Indiana Univ. Math. J. 30, no. 4, 589–605
6. Galchouk, L. and Novikov, A.: On Wald’s equation. Discrete time case.
S´eminaire de Probabilit´es. XXXI, Lecture Notes in Math., 1655, 126–135,
Springer, Berlin (1997)
7. Jacod J., Shiryaev A.N.: Limit Theorems for Stochastic Processes. 2nd ed.
Springer-Verlag, Berlin (2003)
8. Jacod J., Shiryaev A.N.: Local martingales and the fundamental asset pricing
theorrems in the discrete time case. Finance and Stochastics. 2, 255–273 (1998)
9. Liptser, R.Sh., Shiryayev, A.N.: Theory of Martingales. Kluwer Acad. Publ.
Dordrecht (1989)
10. Novikov, A.: Martingales, Tauberian theorem and gambling. Theory Prob., Appl.
41, no. 4, 716–729 (1996)
11. Novikov, A.A.: Martingale appproach to first passage problems of nonlinear
boundaries. Proc. Steklov Inst. Math., v. 158, 130–152 (1981)
12. Novikov, A.: On the time of crossing a one-sided nonlinear boundary by sums of
independent random variables. Theory Prob., Appl. 27, no. 4, 643–656 (1982)
13. Peskir, G., Shiryaev, A.N.: On the Brownian first-passage time over a one-sided
stochastic boundary. Theory Probab. Appl. 42 (1998), no. 3, 444–453 (1997)
14. Takaoka, K.: Some remark on the uniform integrability of continuous martin-
gales. S´eminaire de Probabilit´es. XXXIII, Lecture Notes in Math., 1709., 327–
333, Springer, Berlin (1999)
15. Vondra˘cek, Z.: Asymptotics of first passage time over a one-sided stochastic
boundary. J. Theoret. Prob. 13, no.1, 171–173 (1997)

Stochastic Differential Equations: A Wiener
Chaos Approach
Sergey LOTOTSKY1 ∗and Boris ROZOVSKII2†
1 Department of Mathematics, USC Los Angeles, CA 90089 USA.
lototsky@math.usc.edu
2 Department of Mathematics, USC Los Angeles, CA 90089 USA.
rozovski@math.usc.edu
Summary. A new method is described for constructing a generalized solution for
stochastic differential equations. The method is based on the Cameron–Martin ver-
sion of the Wiener Chaos expansion and provides a unified framework for the study
of ordinary and partial differential equations driven by finite- or infinite-dimensional
noise with either adapted or anticipating input. Existence, uniqueness, regularity,
and probabilistic representation of this Wiener Chaos solution is established for
a large class of equations. A number of examples are presented to illustrate the
general constructions. A detailed analysis is presented for the various forms of the
passive scalar equation and for the first-order Itˆo stochastic partial differential equa-
tion. Applications to nonlinear filtering of diffusion processes and to the stochastic
Navier–Stokes equation are also discussed.
Key words: anticipating equations, generalized random elements, degenerate par-
abolic equations, Malliavin calculus, passive scalar equation, Skorohod integral, S-
transform, weighted spaces
Mathematics Subject Classification (2000): 60H15, 35R60, 60H40
Contents
1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434
2. Traditional Solutions of Linear Parabolic Equations . . . . . . 437
3. White Noise Solutions of Stochastic Parabolic Equations . 441
4. Generalized Functions on the Wiener Chaos Space . . . . . . . 446
5. The Malliavin Derivative and its Adjoint . . . . . . . . . . . . . . . . . 449
6. The Wiener Chaos Solution and the Propagator. . . . . . . . . .452
∗The work of S. Lototsky was partially supported by the Sloan Research Fellow-
ship, by the NSF CAREER award DMS-0237724, and by the ARO Grant DAAD19-
02-1-0374
†The work of B. Rozovskii was partially supported by the ARO Grant DAAD19-
02-1-0374 and ONR Grant N0014-03-1-0027.

434
S. Lototsky and B. Rozovskii
7. Weighted Wiener Chaos Spaces and S-Transform . . . . . . . . 460
8. General Properties of the Wiener Chaos Solutions . . . . . . .466
9. Regularity of the Wiener Chaos Solution . . . . . . . . . . . . . . . . 469
10. Probabilistic Representation of Wiener Chaos Solutions . 480
11. Wiener Chaos and Nonlinear Filtering . . . . . . . . . . . . . . . . . 486
12. Passive Scalar in a Gaussian Field . . . . . . . . . . . . . . . . . . . . . . 491
13. Stochastic Navier-Stokes Equation . . . . . . . . . . . . . . . . . . . . . . 497
14. First-Order Itˆo Equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 502
1 Introduction
Consider a stochastic evolution equation
du(t) = (Au(t) + f(t))dt + (Mu(t) + g(t))dW(t),
(1.1)
where A and M are differential operators, and W is a noise process on a
stochastic basis F = (Ω, F, {Ft}t≥0, P). Traditionally, this equation is studied
under the following assumptions:
(i) The operator A is elliptic, the order of the operator M is at most half the
order of A, and a special parabolicity condition holds.
(ii) The functions f and g are predictable with respect to the filtration
{Ft}t≥0, and the initial condition is F0-measurable.
(iii) The noise process W is sufficiently regular.
Under these assumptions, there exists a unique predictable solution u of
(1.1) such that u belongs to L2(Ω× (0, T); H) for T > 0 and a suitable
function space H (see, for example, Chapter 3 of [42]). Moreover, there are
examples showing that the parabolicity condition and the regularity of noise
are necessary to have a square integrable solution of (1.1).
The objective of the current paper is to study stochastic differential equa-
tions of the type (1.1) without making the above assumptions (i)–(iii). We
show that, with a suitable definition of the solution, solvability of the stochas-
tic equation is essentially equivalent to solvability of a deterministic evolution
equation dv = (Av + ϕ)dt for certain functions ϕ; the operator A does not
even have to be elliptic.
Generalized solutions have been introduced and studied for stochastic dif-
ferential equations, both ordinary and with partial derivatives, and definitions
of such solutions relied on various forms of the Wiener Chaos decomposition.
For stochastic ordinary differential equations, Krylov and Veretennikov [20]
used multiple Wiener integral expansion to study Itˆo diffusions with non-
smooth coefficients, and more recently, LeJan and Raimond [22] used a sim-
ilar approach in the construction of stochastic flows. Various versions of the
Wiener Chaos appear in a number of papers on nonlinear filtering and related

Wiener Chaos for Stochastic Equations
435
topics [2, 25, 33, 39, 46, etc.] The book by Holden et al. [12] presents a sys-
tematic approach to the stochastic differential equations based on the white
noise theory. See also [10], [40] and the references therein.
For stochastic partial differential equations, most existing constructions
of the generalized solution rely on various modifications of the Fourier trans-
form in the infinite-dimensional Wiener Chaos space L2(W) = L2(Ω, FW
T , P).
The two main modifications are known as the S-transform [10] and the Her-
mite transform [12]. The key elements in the development of the theory are
the spaces of the test functions and the corresponding distributions. Several
constructions of these spaces were suggested by Hida [10], Kondratiev [17],
and Nualart and Rozovskii [38]. Both S- and Hermite transforms establish
a bijection between the space of generalized random elements and a suitable
space of analytic functions. Using the S-transform, Mikulevicius and Rozovskii
[33] studied stochastic parabolic equations with non-smooth coefficients, while
Nualart and Rozovskii [38] and Potthoffet al. [40] constructed generalized so-
lutions for the equations driven by space-time white noise in more than one
spatial dimension. Many other types of equations have been studied, and the
book [12] provides a good overview of literature on the corresponding results.
In this paper, generalized solutions of (1.1) are defined in the spaces that
are even larger than of Hida or Kondratiev distributions. The Wiener Chaos
space is a separable Hilbert space with a Cameron–Martin basis [3]. The
elements of the space with a finite Fourier series expansion provide the nat-
ural collection of test functions D(L2(W)), an analog of the space D(Rd) of
smooth compactly supported functions on Rd. The corresponding space of
distributions D′(L2(W)) is the collection of generalized random elements rep-
resented by formal Fourier series. A generalized solution u = u(t, x) of (1.1)
is constructed as an element of D′(L2(W)) such that the generalized Fourier
coefficients satisfy a system of deterministic evolution equations, known as
the propagator. If the equation is linear the propagator is a lower-triangular
system. We call this solution a Wiener Chaos solution.
The propagator was first introduced by Mikulevicius and Rozovskii in
[32], and further studied in [25], as a numerical tool for solving the nonlinear
filtering problem. The propagator can also be derived for certain nonlinear
equations; in particular, it was used in [31, 34, 35] to study the stochastic
Navier–Stokes equation.
The propagator approach to defining the solution of (1.1) has two advan-
tages over the S-transform approach. First, the resulting construction is more
general: there are equations for which the Wiener Chaos solution is not in
the domain of the S-transform. Indeed, it is shown in Section 14 that, for
certain initial conditions, equation du = uxdWt has a Wiener Chaos solution
for which the S-transform is not defined. On the other hand, by Theorem 8.1
below, if the generalized solution of (1.1) can be defined using the S-transform,
then this solution is also a Wiener Chaos solution. Second, there is no problem
of inversion: the propagator provides a direct approach to studying the prop-

436
S. Lototsky and B. Rozovskii
erties of Wiener Chaos solution and computing both the sample trajectories
and statistical moments.
Let us emphasize also the following important features of the Wiener Chaos
approach:
•
The Wiener Chaos solution is a strong solution in the probabilistic sense,
that is, it is uniquely determined by the coefficients, free terms, initial
condition, and the Wiener process.
•
The solution exists under minimal regularity conditions on the coefficients
in the stochastic part of the equation and no special measurability restric-
tion on the input.
•
The Wiener Chaos solution often serves as a convenient first step in the in-
vestigation of the traditional solutions or solutions in weighted stochastic
Sobolev spaces that are much smaller then the spaces of Hida or Kon-
dratiev distributions.
To better understand the connection between the Wiener Chaos solution
and other notions of the solution, recall that, traditionally, by a solution of a
stochastic equation we understand a random process or field satisfying the
equation for almost all elementary outcomes. This solution can be either
strong or weak in the probabilistic sense.
Probabilistically strong solution is constructed on a prescribed probability
space with a specific noise process. Existence of strong solutions requires cer-
tain regularity of the coefficients and the noise in the equation. The tools for
constructing strong solutions often come from the theory of the corresponding
deterministic equations.
Probabilistically weak solution includes not only the solution process but
also the stochastic basis and the noise process. This freedom to choose the
probability space and the noise process makes the conditions for existence of
weak solutions less restrictive than the similar conditions for strong solutions.
Weak solutions can be obtained either by considering the corresponding mar-
tingale problem or by constructing a suitable Hunt process using the theory
of the Dirichlet forms.
There exist equations that have neither weak nor strong solutions in the
traditional sense. An example is the bi-linear stochastic heat equation driven
by a multiplicative space-time white noise in two or more spatial dimensions:
the irregular nature of the noise prevents the existence of a random field that
would satisfy the equation for individual elementary outcomes. For such equa-
tions, the solution must be defined as a generalized random element satisfying
the equation after the randomness has been averaged out.
White noise theory provides one approach for constructing these gener-
alized solutions. The approach is similar to the Fourier integral method for
deterministic equations. The white noise solution is constructed on a special
white noise probability space by inverting an integral transform; the special
structure of the probability space is essential to carry out the inversion. We

Wiener Chaos for Stochastic Equations
437
can therefore say that the white noise solution extends the notion of the prob-
abilistically weak solution. Still, this extension is not a true generalization:
when the equation satisfies the necessary regularity conditions, the connec-
tion between the white noise and the traditional weak solution is often not
clear.
The Wiener chaos approach provides the means for constructing a gener-
alized solution on a prescribed probability space. The Wiener Chaos solution
is a formal Fourier series in the corresponding Cameron–Martin basis. The
coefficients in the series are uniquely determined by the equation via the
propagator system. This representation provides a convenient way for com-
puting numerically the solution and its statistical moments. As a result, the
Wiener Chaos solution extends the notion of the probabilistically strong so-
lution. Unlike the white noise approach, this is a bona fide extension: when
the equation satisfies the necessary regularity conditions, the Wiener Chaos
solution coincides with the traditional strong solution.
After a general discussion of the Wiener Chaos space in Sections 4 and 5,
the Wiener Chaos solution for equation (1.1) and the main properties of the
solution are studied in Section 6. Several examples illustrate how the Wiener
Chaos solution provides a uniform treatment of various types of equations:
traditional parabolic, non-parabolic, and anticipating. In particular, for equa-
tions with non-predictable input, the Wiener Chaos solution corresponds to
the Skorohod integral interpretation of the equation. The initial solution space
D′(W) is too large to provide much of interesting information about the solu-
tion. Accordingly, Section 7 discusses various weighted Wiener Chaos spaces.
These weighted spaces provide the necessary connection between the Wiener
Chaos, white noise, and traditional solutions. This connection is studied in
Section 8. In Section 9, the Wiener Chaos solution is constructed for degener-
ate linear parabolic equations and new regularity results are obtained for the
solution. Probabilistic representation of the Wiener Chaos solution is studied
in Section 10, where a Feynmann–Kac type formula is derived. Sections 11
– 14 discuss the applications of the general results to particular equations:
the Zakai filtering equation, the stochastic transport equation, the stochastic
Navier–Stokes equation, and a first-order Itˆo SPDE.
The following notation will be in force throughout the paper: ∆is the
Laplace operator, Di = ∂/∂xi, i = 1, . . . , d, and summation over the repeated
indices is assumed. The space of continuous functions is denoted by C, and
Hγ
2 , γ ∈R, is the Sobolev space

f :

R
| ˆf(y)|2(1 + |y|2)γdy < ∞

, where ˆf is the Fourier transform of f.
2 Traditional Solutions of Linear Parabolic Equations
Below is a summary of the Hilbert space theory of linear stochastic parabolic
equations. The details can be found in the books [41] and [42]; see also [19].

438
S. Lototsky and B. Rozovskii
For a Hilbert space X, (·, ·)X and ∥· ∥X denote the inner product and the
norm in X.
Definition 2.1 The triple (V, H, V ′) of Hilbert spaces is called normal if and
only if
1. V ֒→H ֒→V ′ and both embeddings V ֒→H and H ֒→V ′ are dense and
continuous;
2. The space V ′ is the dual of V relative to the inner product in H;
3. There exists a constant C > 0 such that |(h, v)H| ≤C∥v∥V ∥h∥V ′ for all
v ∈V and h ∈H.
E.g., the Sobolev spaces (Hℓ+γ
2
(Rd), Hℓ
2(Rd), Hℓ−γ
2
(Rd)), γ > 0, ℓ∈R, form
a normal triple.
Denote by ⟨v′, v⟩, v′ ∈V ′, v ∈V , the duality between V and V ′ relative
to the inner product in H. The properties of the normal triple imply that
|⟨v′, v⟩| ≤C∥v∥V ∥v′∥V ′, and, if v′ ∈H and v ∈V , then ⟨v′, v⟩= (v′, v)H;
Let F = (Ω, F, {Ft}t≥0, P) be a stochastic basis with the usual assump-
tions. In particular, the σ-algebras F and F0 are P-complete, and the filtration
{Ft}t≥0 is right-continuous; for details, see [23, Definition I.1.1]. We assume
that F is rich enough to carry a collection wk = wk(t), k ≥1, t ≥0, of
independent standard Wiener processes.
Given a normal triple (V, H, V ′) and a family of linear bounded operators
A(t) : V →V ′, Mk(t) : V →H, t ∈[0, T], consider the following equation:
u(t) = u0 +
 t
0
(Au(s) + f(s))ds +
 t
0
(Mku(s) + gk(s))dwk(s),
t ∈[0, T],
(2.1)
where T < ∞is fixed and non-random and the summation convention is in
force.
Assume that, for all v ∈V ,

k≥1
∥Mk(t)v∥2
H < ∞,
t ∈[0, T].
(2.2)
The input data u0, f, and gk are chosen so that
E

∥u0∥2
H +
 T
0
∥f(t)∥2
V ′dt +

k≥1
 T
0
∥gk(t)∥2
Hdt

< ∞,
(2.3)
u0 is F0-measurable, and the processes f, gk are Ft-adapted, that is, f(t) and
each gk(t) are Ft-measurable for each t ≥0.
Definition 2.2 An Ft-adapted process u ∈L2(F; L2((0, T); V )) is called a
traditional, or square-integrable, solution of equation (2.1) if, for every v ∈V ,
there exists a measurable subset Ω′ of Ωwith P(Ω′) = 1, such that the equality

Wiener Chaos for Stochastic Equations
439
(u(t), v)H = (u0, v)H+
 t
0
⟨Au(s)+f(s), v⟩ds+

k≥1
(Mku(s)+gk(s), v)Hdwk(s)
(2.4)
holds on Ω′ for all t ∈[0, T].
Existence and uniqueness of the traditional solution for (2.1) can be es-
tablished when the equation is parabolic.
Definition 2.3 Equation (2.1) is called strongly parabolic if there exists a
positive number ε and a real number C0 such that, for all v ∈V and t ∈[0, T],
2⟨A(t)v, v⟩+

k≥1
∥M(t)kv∥2
H + ε∥v∥2
V ≤C0∥v∥2
H.
(2.5)
Equation (2.1) is called weakly
parabolic (or degenerate parabolic) if con-
dition (2.5) holds with ε = 0.
Theorem 2.1. If (2.3) and (2.5) hold, then there exists a unique traditional
solution of (2.1). The solution process u is an element of the space
L2(F; L2((0, T); V ))
?
L2(F; C((0, T), H))
and satisfies
E
	
sup
0<t<T
∥u(t)∥2
H +
 T
0
∥u(t)∥2
V dt

≤C(C0, δ, T)E

∥u0∥2
H +
 T
0
∥f(t)∥2
V ′dt +

k≥1
 T
0
∥gk(t)∥2
Hdt

.
(2.6)
Proof. This follows, for example, from Theorem 3.1.4 in [42].
A somewhat different solvability result holds for weakly parabolic equa-
tions [42, Section 3.2].
As an application of Theorem 2.1, consider the equation
du(t, x) = (aij(t, x)DiDju(t, x) + bi(t, x)Diu(t, x) + c(t, x)u(t, x) + f(t, x))dt
+ (σik(t, x)Diu(t, x) + νk(t, x)u(t, x) + gk(t, x))dwk(t)
(2.7)
with 0 < t ≤T, x ∈Rd, and initial condition u(0, x) = u0(x). Assume that
(CL1) The functions aij are bounded and Lipschitz continuous, the functions bi,
c, σik, and ν are bounded measurable.
(CL2) There exists a positive number ε > 0 such that
(2aij(x) −σik(x)σjk(x))yiyj ≥ε|y|2,
x, y ∈Rd, t ∈[0, T].

440
S. Lototsky and B. Rozovskii
(CL3) There is a positive number K such that, for all x ∈Rd, 
k≥1 |νk(x)|2 ≤K.
(CL4) The initial condition u0 ∈L2(Ω; L2(Rd)) is F0-measurable, the processes
f ∈L2(Ω× [0, T]; H−1
2 (Rd)) and gk ∈L2(Ω× [0, T]; L2(Rd)) are Ft-
adapted, and 
k≥1
 T
0 E∥gk∥2
L2(Rd)(t)dt < ∞.
Theorem 2.2. Under assumptions (CL1)–(CL4), equation (2.7) has a unique
traditional solution
u ∈L2(F; L2((0, T); H1
2(Rd)))
?
L2(F; C((0, T), L2(Rd))),
and the solution satisfies
E
	
sup
0<t<T
∥u∥2
L2(Rd)(t) +
 T
0
∥u∥2
H1
2(Rd)(t)dt

≤C(K, ε, T)E

∥u0∥2
L2(Rd) +
 T
0
∥f∥2
H−1
2
(Rd)(t)dt+

k≥1
 T
0
∥gk∥2
L2(Rd)(t)dt

.
(2.8)
Proof. Apply Theorem 2.1 to the normal triple (H1
2(Rd), L2(Rd), H−1
2 (Rd));
condition (2.5) in this case is equivalent to assumption (CL2). The details of
the proof are in [42, Section 4.1].
Condition (2.5) essentially means that the deterministic part of the equa-
tion dominates the stochastic part. Accordingly, there are two main ways to
violate (2.5):
1. The order of the operator M is more than half the order of the operator
A. The equation du = uxdw(t) is an example.
2. The value of 
k ∥Mk(t)v∥2
H is too large. This value can be either finite,
as for the equation du(t, x) = uxx(t, x)dt + 5ux(t, x)dw(t), or infinite, as
for the equation
du(t, x) = ∆u(t, x)dt + σk(x)udwk, σk −CONS in L2(Rd), d ≥2. (2.9)
Indeed, it is shown in [38] that, for equation (2.9), we have

k≥1
∥Mk(t)v∥2
H = ∞
in every Sobolev space Hγ.
Without condition (2.5), analysis of equation (2.1) requires new technical
tools and a different notion of solution. The white noise theory provides one
possible collection of such tools.

Wiener Chaos for Stochastic Equations
441
3 White Noise Solutions of Stochastic Parabolic
Equations
The central part of the white noise theory is the mathematical model for the
derivative of the Brownian motion. In particular, the Itˆo integral
 t
0 f(s)dw(s)
is replaced with the integral
 t
0 f(s) ⋄˙W(s)ds, where
˙W is the white noise
process and ⋄is the Wick product. The white noise formulation is very dif-
ferent from the Hilbert space approach of the previous section, and requires
several new constructions. The book [10] is a general reference about the
white noise theory, while [12] presents the white noise analysis of stochastic
partial differential equations. Below is the summary of the main definitions
and results.
Denote by S = S(Rℓ) the Schwartz space of rapidly decreasing functions
and by S′ = S′(Rℓ), the Schwartz space of tempered distributions. For the
properties of the spaces S and S′ see [43].
Definition 3.1 The white noise probability space is the triple
S = (S′, B(S′), µ),
where B(S′) is the Borel σ-algebra of subsets of S′, and µ is the normalized
Gaussian measure on B(S′).
The measure µ is characterized by the property

S′ e
√−1⟨ω,ϕ⟩dµ(ω) = e
−1
2 ∥ϕ∥2
L2(Rd),
where ⟨ω, ϕ⟩, ω ∈S′, ϕ ∈S, is the duality between S and S′. Existence of
this measure follows from the Bochner–Minlos theorem [12, Appendix A].
Let {ηk, k ≥1} be the Hermite basis in L2(Rℓ), consisting of the normal-
ized eigenfunctions of the operator
Λ = −∆+ |x|2, x ∈Rℓ.
(3.1)
Each ηk is an element of S [12, Section 2.2].
Consider the collection of multi-indices
J1 =
/
α = (αi, i ≥1) : αi ∈{0, 1, 2, . . .},

i
αi < ∞
0
.
The set J1 is countable, and, for every α ∈J , only finitely many of αi are
not equal to zero. For α ∈J1, write α! = K
i αi! and define
ξα(ω) =
1
√
α!
(
i
Hαi(⟨ω, ηi⟩), ω ∈S′,
(3.2)
where ⟨·, ·⟩is the duality between S and S′, and

442
S. Lototsky and B. Rozovskii
Hn(t) = (−1)net2/2 dn
dtn e−t2/2
(3.3)
is nth Hermite polynomial. In particular, H1(t) = 1, H1(t) = t, H2(t) = t2−1.
If, for example, α = (0, 2, 0, 1, 3, 0, 0, . . .) has three non-zero entries, then
ξα(ω) = H2(⟨ω, η2⟩)
2!
· ⟨ω, η4⟩· H3(⟨ω, η5⟩)
3!
.
Theorem 3.1. The collection {ξα, α ∈J1} is an orthonormal basis in L2(S).
Proof. This is a version of the classical result of Cameron and Martin [3]. In
this particular form, the result is stated and proved in [12, Theorem 2.2.3].
By Theorem 3.1, every element ϕ of L2(S) is represented as a Fourier series
ϕ = 
α ϕαξα, where ϕα =

S′ ϕ(ω)ξα(ω)dµ, and ∥ϕ∥2
L2(S) = 
α∈J1 |ϕα|2.
For α ∈J1 and q ∈R, we write
(2N)qα =
(
j
(2j)qαj.
Definition 3.2 For ρ ∈[0, 1] and q ≥0,
1. the space (S)ρ,q is the collection of elements ϕ from L2(S) such that
∥ϕ∥2
ρ,q =

α∈J1
(α!)ρ(2N)qα|ϕα|2 < ∞;
2. the space (S)−ρ,−q is the closure of L2(S) relative to the norm
∥ϕ∥2
−ρ,−q =

α∈J1
(α!)−ρ(2N)−qα|ϕα|2;
(3.4)
3. the space (S)ρ is the projective limit of (S)ρ,q as q changes over all non-
negative integers;
4. the space (S)−ρ is the inductive limit of (S)−ρ,−q as q changes over all
non-negative integers.
It follows that
•
For each ρ ∈[0, 1] and q ≥0, ((S)ρ,q, L2(S), (S)−ρ,−q) is a normal triple
of Hilbert spaces.
•
The space (S)ρ is a Frechet space with topology generated by the countable
family of norms ∥·∥ρ,n, n = 0, 1, 2, . . ., and ϕ ∈(S)ρ if and only if ϕ ∈(S)ρ,q
for every q ≥0.
•
The space (S)−ρ is the dual of (S)ρ and ϕ ∈(S)−ρ if and only if ϕ ∈
(S)−ρ,−q for some q ≥0. Every element ϕ from (S)ρ is identified with a
formal sum 
α∈J1 ϕαξα such that (3.4) holds for some q ≥0.

Wiener Chaos for Stochastic Equations
443
•
For ρ ∈(0, 1),
(S)1 ⊂(S)ρ ⊂(S)0 ⊂L2(S) ⊂(S)−0 ⊂(S)−ρ ⊂(S)−1,
with all inclusions strict.
The spaces (S)0 and (S)1 are known as the spaces of Hida and Kon-
dratiev test functions. The spaces (S)−0 and (S)−1 are known as the spaces
of Hida and Kondratiev distributions. Sometimes, the spaces (S)ρ and (S)−ρ,
0 < ρ ≤1, go under the name of Kondratiev test functions and Kondratiev
distributions, respectively.
Let h ∈S and hk =

Rℓh(x)ηk(x)dx. Since the asymptotics of nth eigen-
value of the operator Λ in (3.1) is n1/d [11, Chapter 21] and Λkh ∈S for every
positive integer k, it follows that

k≥1
|hk|2kq < ∞
(3.5)
for every q ∈R.
For α ∈J1 and hk as above, write hα = K
j(hj)αj, and define the stochas-
tic exponential
E(h) =

α∈J1
hα
√
α!
ξα
(3.6)
Lemma 3.1. The stochastic exponential E = E(h), h ∈S, has the following
properties:
•
E(h) ∈(S)ρ, 0 < ρ < 1;
•
For every q > 0, there exists δ > 0 such that E(h) ∈(S)1,q as long as

k≥1 |hk|2 < δ.
Proof. Both properties are verified by direct calculation [12, Chapter 2].
Definition 3.3 The S-transform Sϕ(h) of an element ϕ = 
α∈J ϕαξα from
(S)−ρ is the number
Sϕ(h) =

α∈J1
hα
√
α!
ϕα,
(3.7)
where h = 
k≥1 hkηk ∈S and hα = K
j(hj)αj.
The definition implies that if ϕ ∈(S)−ρ,−q for some q ≥0, then Sϕ(h) =
⟨ϕ, E(h)⟩, where ⟨·, ·⟩is the duality between (S)ρ,q and (S)−ρ,−q for suitable
q. Therefore, if ρ < 1, then Sϕ(h) is well-defined for all h ∈S, and, if ρ = 1,
the Sϕ(h) is well-defined for h with sufficiently small L2(Rℓ) norm. To give
a complete characterization of the S-transform, an additional construction is
necessary.
Let Uρ, 0 ≤ρ < 1, be the collection of mappings F from S to the complex
numbers such that

444
S. Lototsky and B. Rozovskii
1. For every h1, h2 ∈S, the function F(h1 + zh2) is an analytic function of
the complex variable z.
2. There exist positive numbers K1, K2 and an integer number n so that, for
all h ∈S and all complex number z,
|F(zh)| ≤K1 exp

K2∥Λnh∥
2
1−ρ
L2(Rd)|z|
2
1−ρ

.
For ρ = 1, let U1 be the collection of mappings F from S to the complex
numbers such that
1′. There exist ε > 0 and a positive integer n such that, for all h1, h2 ∈S with
∥Λnh1∥L2(Rℓ) < ε, the function of a complex variable z →F(h1 + h2z) is
analytic at zero, and
2′. There is a constant K > 0 such that, for all h ∈S with ∥Λnh∥L2(Rℓ) < ε,
|F(h)| ≤K.
Two mappings F, G with properties 1′ and 2′ are identified with the same
element of U1 if F = G on an open neighborhood of zero in S.
The following result holds.
Theorem 3.2. For every ρ ∈[0, 1], the S-transform is a bijection from (S)−ρ
to Uρ.
In other words, for every ϕ ∈(S)−ρ, the S-transform Sϕ is an element of Uρ,
and, for every F ∈Uρ, there exists a unique ϕ ∈(S)−ρ such that Sϕ = F.
This result is proved in [10] when ρ = 0, and in [17] when ρ = 1.
Definition 3.4 For ϕ and ψ from (S)−ρ, ρ ∈[0, 1], the Wick product ϕ ⋄ψ
is the unique element of (S)−ρ whose S-transform is Sϕ · Sψ.
If S−1 is the inverse S-transform, then
ϕ ⋄ψ = S−1(Sϕ · Sψ),
Note that, by Theorem 3.2, the Wick product is well-defined, because the
space Uρ, ρ ∈[0, 1] is closed under the point-wise multiplication. Theorem 3.2
also ensures the correctness of the following definition of the white noise.
Definition 3.5 The white noise ˙W on Rℓis the unique element of (S)0 whose
S transform satisfies S ˙W(h) = h.
Remark 3.1 If g ∈Lp(S), p > 1, then g ∈(S)−0 [12, Corollary 2.3.8], and the
Fourier transform
ˆg(h) =

S′ exp
√
−1⟨ω, h⟩

g(ω)dµ(ω)
is defined. Direct calculations [12, Section 2.9] show that, for those g,
Sg(
√
−1 h) = ˆg(h) e
1
2 ∥h∥2
L2(Rℓ).
As a result, the Wick product can be interpreted as a convolution on the
infinite-dimensional space (S)−ρ.

Wiener Chaos for Stochastic Equations
445
In the study of stochastic parabolic equations, ℓ= d + 1, so that the
generic point from Rd+1 is written as (t, x), t ∈R, x ∈Rd. As was mentioned
earlier, the terms of the type fdW(t) become f ⋄˙Wdt. The precise connection
between the Itˆo integral and Wick product is discussed, for example, in [12,
Section 2.5].
As an example, consider the following equation:
ut(t, x) = a(x)uxx(t, x) + b(x)ux(t, x) + ux(t, x) ⋄˙W(t, x), 0 < t < T, x ∈R,
(3.8)
with initial condition u(0, x) = u0(x). In (3.8),
(WN1)
˙W is the white noise process on R2.
(WN2) The initial condition u0 and the coefficients a, b are bounded and have
continuous bounded derivatives up to second order.
(WN3) There exists a positive number ε such that a(x) ≥ε, x ∈R.
(WN4) The second-order derivative of a is uniformly H¨older continuous.
The equivalent Itˆo formulation of (3.8) is
du(t, x) = (a(x)uxx(t, x) + b(x)ux(t, x))dt + ek(x)ux(t, x)dwk(x),
(3.9)
where {ek, k ≥1} is the Hermite basis in L2(R).
With Mkv = ekvx, we see that condition (2.2) does not hold in any Sobolev
space Hγ
2 (R). In fact, no traditional solution exists in any normal triple of
Sobolev spaces. On the other hand, with a suitable definition of solution,
equation (3.8) is solvable in the space (S)−0 of Hida distributions.
Definition 3.6 A mapping u : Rd →(S)−ρ is called weakly differentiable
with respect to xi at a point x∗∈Rℓif and only if there exists Ui(x∗) ∈(S)−ρ
so that, for all ϕ ∈(S)ρ, Di⟨u(x), ϕ⟩|x=x∗= ⟨Ui(x∗), ϕ⟩. In that case, we
write Ui(x∗) = Diu(x∗).
Definition 3.7 A mapping u from [0, T] × R to (S)−0 is called a white noise
solution of (3.8) if and only if
1. The weak derivatives ut, ux, and uxx exist, in the sense of Definition 3.6,
for all (t, x) ∈(0, T) × R.
2. Equality (3.8) holds for all (t, x) ∈(0, T) × Rd.
3. limt↓0 u(t, x) = u0(x) in the topology of (S)−0.
Theorem 3.3. Under assumptions (WN1)–(WN4), there exists a white noise
solution of (3.8). This solution is unique in the class of weakly measurable
mappings v from (0, T) × R to (S)−0, for which there exists a non-negative
integer q and a positive number K such that
 T
0

R
∥v(t, x)∥−0,−qe−Kx2dxdt < ∞.

446
S. Lototsky and B. Rozovskii
Proof. Consider the S-transformed equation
Ft(t, x; h) = a(x)Fxx(t, x; h) + b(x)Fx(t, x; h) + Fx(t, x; h)h,
(3.10)
0 < t < T, x ∈R, h ∈S(R), with initial condition F(0, x; h) = u0(x). This
a deterministic parabolic equation, and one can show, using the probabilistic
representation of F, that F, Ft, Fx, and Fxx belong to U0. Then the inverse
S-transform of F is a solution of (3.8), and the uniqueness follows from the
uniqueness for equation (3.10). The details of the proof are in [40], where a
similar equation is considered for x ∈Rd.
Even though the initial condition in (3.8) is deterministic, there are no
measurability restrictions on u0 for the white noise solution to exist; see [12]
for more details.
With appropriate modifications, the white noise solution can be defined
for equations more general than (3.8). The solution F = F(t, x; h) of the
corresponding S-transformed equation determines the regularity of the white
noise solution [12, Section 4.1].
Two main advantages of the white noise approach over the Hilbert space
approach are:
1. No need for parabolicity condition.
2. No measurability restrictions on the input data.
Still, there are substantial limitations:
1. There seems to be little or no connection between the white noise solution
and the traditional solution. While the white noise solution can, in princi-
ple, be constructed for equation (2.7), this solution will be very different
from the traditional solution.
2. There are no clear ways of computing the solution numerically, even with
available representations of the Feynmann-Kac type [12, Chapter 4].
3. The white noise solution, being constructed on a special white noise prob-
ability space, is weak in the probabilistic sense. Path-wise uniqueness does
not apply to such solutions because of the ”averaging” nature of the so-
lution spaces.
4 Generalized Functions on the Wiener Chaos Space
The objective of this section is to introduce the space of generalized random
elements on an arbitrary stochastic basis.
Let F = (Ω, F, {Ft}t≥0, P) be a stochastic basis with the usual assump-
tions and Y , a separable Hilbert space with inner product (·, ·)Y and an or-
thonormal basis {yk, k ≥1}. On F and Y , consider a cylindrical Brownian
motion W, that is, a family of continuous Ft-adapted Gaussian martingales
Wy(t), y ∈Y , such that Wy(0) = 0 and E(Wy1(t)Wy2(s)) = min(t, s)(y1, y2)Y .
In particular,

Wiener Chaos for Stochastic Equations
447
wk(t) = Wyk(t), k ≥1, t ≥0,
(4.1)
are independent standard Wiener processes on F.
Equivalently, instead of the process W, the starting point can be a system
of independent standard Wiener processes {wk, k ≥1} on F. Then, given
a separable Hilbert space Y with an orthonormal basis {yk, k ≥1}, the
corresponding cylindrical Brownian motion W is defined by
Wy(t) =

k≥1
(y, yk)Y wk(t).
(4.2)
Fix a non-random T ∈(0, ∞) and denote by FW
T
the σ-algebra generated
by wk(t), k ≥1, t < T. Denote by L2(W) the collection of FW
T -measurable
square integrable random variables.
We now review construction of the Cameron–Martin basis in the Hilbert
space L2(W).
Let m = {mk, k ≥1} be an orthonormal basis in L2((0, T)) such that
each mk belongs to L∞((0, T)). Define the independent standard Gaussian
random variables
ξik =
 T
0
mi(s)dwk(s).
Consider the collection of multi-indices
J =
/
α = (αk
i , i, k ≥1) : αk
i ∈{0, 1, 2, . . .},

i,k
αk
i < ∞
0
.
The set J is countable, and, for every α ∈J , only finitely many of αk
i are
not equal to zero. The upper and lower indices in αk
i represent, respectively,
the space and time components of the noise process W. For α ∈J , define
|α| =

i,k
αk
i , α! =
(
i,k
αk
i !,
and
ξα =
1
√
α!
(
i,k
Hαk
i (ξik),
(4.3)
where Hn is nth Hermite polynomial. For example, if
α =





0 1 0 3 0 0 · · ·
2 0 0 0 4 0 · · ·
0 0 0 0 0 0 · · ·
... ... ... ... ... ... · · ·





with four non-zero entries α1
2 = 1; α1
4 = 3; α2
1 = 2; α2
5 = 4, then
ξα = ξ2,1 · H3(ξ4,1)
√
3!
· H2(ξ1,2)
√
2!
· H4(ξ5,2)
√
4!
.
There are two main differences between (3.2) and (4.3):

448
S. Lototsky and B. Rozovskii
1. The basis (4.3) is constructed on an arbitrary probability space.
2. In (4.3), there is a clear separation of the time and space components
of the noise, and explicit presence of the time-dependent functions mi
facilitates the analysis of evolution equations.
Definition 4.1 The space L2(W) is called the Wiener Chaos space. The N-th
Wiener Chaos is the linear subspace of L2(W), generated by ξα, |α| = N.
The following is another version of the classical results of Cameron and
Martin [3].
Theorem 4.1. The collection Ξ = {ξα, α ∈J } is an orthonormal basis in
L2(W).
We refer to Ξ as the Cameron–Martin basis in L2(W). By Theorem 4.1, every
element v of L2(W) can be written as
v =

α∈J
vαξα,
where vα = E(vξα).
We now define the space D(L2(W)) of test functions and the space
D′(L2(W); X) of X-valued generalized random elements.
Definition 4.2
(1) The space D(L2(W)) is the collection of elements from L2(W) that can
be written in the form
v =

α∈Jv
vαξα
for some vα ∈R and a finite subset Jv of J .
(2) A sequence vn converges to v in D(L2(W)) if and only if Jvn ⊆Jv for all
n and lim
n→∞|vn,α −vα| = 0 for all α.
Definition 4.3 For a linear topological space X define the space D′(L2(W); X)
of X-valued generalized random elements as the collection of continuous linear
maps from the linear topological space D(L2(W)) to X. Similarly, the elements
of D′(L2(W); L1((0, T); X)) are called X-valued generalized random processes.
The element u of D′(L2(W); X) can be identified with a formal Fourier series
u =

α∈J
uαξα,
where uα ∈X are the generalized Fourier coefficients of u. For such a series
and v ∈D(L2(W)), we have
u(v) =

α∈Jv
vαuα.

Wiener Chaos for Stochastic Equations
449
Conversely, for u ∈D′(L2(W); X), we define the formal Fourier series of u by
setting uα = u(ξα). If u ∈L2(W), then u ∈D′(L2(W); R) and u(v) = E(uv).
By Definition 4.3, a sequence {un, n ≥1} converges to u in D′(L2(W); X)
if and only if un(v) converges to u(v) in the topology of X for every v ∈D(W).
In terms of generalized Fourier coefficients, this is equivalent to lim
n→∞un,α = uα
in the topology of X for every α ∈J .
The construction of the space D′(L2(W); X) can be extended to Hilbert
spaces other than L2(W). Let H be a real separable Hilbert space with an
orthonormal basis {ek, k ≥1}. Define the space
D(H) =
/
v ∈H : v =

k∈Jv
vkek, vk ∈R, Jv −a finite subset of {1, 2, . . .}
0
.
By definition, vn converges to v in D(H) as n →∞if and only if Jvn ⊆Jv
for all n and lim
n→∞|vn,k −vk| = 0 for all k.
For a linear topological space X, D′(H; X) is the space of continuous linear
maps from D(H) to X. An element g of D′(H; X) can be identified with a
formal series 
k≥1 gk ⊗ek such that gk = g(ek) ∈X and, for v ∈D(H),
g(v) = 
k∈Jv gkvk. If X = R and 
k≥1 g2
k < ∞, then g = 
k≥1 gkek ∈
H and g(v) = (g, v)H, the inner product in H. The space X is naturally
imbedded into D′(H; X): if u ∈X, then 
k≥1 u ⊗ek ∈D′(H; X).
A sequence gn = 
k≥1 gn,k ⊗ek, n ≥1, converges to g = 
k≥1 gk ⊗ek in
D′(H; X) if and only if, for every k ≥1, lim
n→∞gn,k = gk in the topology of X.
A collection {Lk, k ≥1} of linear operators from X1 to X2 naturally
defines a linear operator L from D′(H; X1) to D′(H; X2):
L


k≥1
gk ⊗ek

=

k≥1
Lk(gk) ⊗ek.
Similarly, a linear operator L : D′(H; X1) →D′(H; X2) can be identified
with a collection {Lk, k ≥1} of linear operators from X1 to X2 by setting
Lk(u) = L(u ⊗ek). Introduction of spaces D′(H; X) and the corresponding
operators makes it possible to avoid conditions of the type (2.2).
5 The Malliavin Derivative and its Adjoint
In this section, we define an analog of the Itˆo stochastic integral for generalized
random processes.
All notations from the previous section will remain in force. In particular,
Y is a separable Hilbert space with a fixed orthonormal basis {yk, k ≥1},
and Ξ = {ξα, α ∈J }, the Cameron–Martin basis in L2(W) defined in (4.3).
We start with a brief review of the Malliavin calculus [37].
The Malliavin derivative D is a continuous linear operator from

450
S. Lototsky and B. Rozovskii
L1
2(W) =
/
u ∈L2(W) :

α∈J
|α|u2
α < ∞
0
(5.1)
to L2 (W; (L2((0, T)) × Y )). In particular,
(Dξα)(t) =

i,k
H
αk
i ξα−(i,k)mi(t)yk,
(5.2)
where α−(i, k) is the multi-index with the components

α−(i, k)
l
j =
max(αk
i −1, 0), if i = j and k = l,
αl
j,
otherwise.
Note that, for each t ∈[0, T], Dξα(t) ∈D(L2(W)×Y ). Using (5.2), we extend
the operator D by linearity to the space D′(L2(W)):
D
	
α∈J
uαξα

=

α∈J

uα

i,k
H
αk
i ξα−(i,k)mi(t)yk

.
For the sake of completeness and to justify further definitions, let us es-
tablish connection between the Malliavin derivative and the stochastic Itˆo
integral.
If u is an arbitrary FW
t -adapted process from L2 (W; L2((0, T); Y )), then
u(t) = 
k≥1 uk(t)yk, where the random variable uk(t) is FW
t -measurable for
each t and k, and

k≥1
 T
0
E|uk(t)|2dt < ∞.
We define the stochastic Itˆo integral
U(t) =
 t
0
(u(s), dW(s))Y =

k≥1
 t
0
uk(s)dwk(s).
(5.3)
Note that U(t) is FW
t -measurable and E|U(t)|2 = 
k≥1
 t
0 E|uk(s)|2ds.
The next result establishes a connection between the Malliavin derivative
and the stochastic Itˆo integral.
Lemma 5.1. Suppose that u is an FW
t -adapted process from
L2 (W; L2((0, T); Y )), and define the process U according to (5.3). Then, for
every t ≤T and α ∈J ,
E(U(t)ξα) = E
 t
0
(u(s), (Dξα)(s))Y ds.
(5.4)

Wiener Chaos for Stochastic Equations
451
Proof. Define ξα(t) = E(ξα|FW
t ). It is known (see [33] or Remark 8.2 below)
that
dξα(t) =

i,k
H
αk
i ξα−(i,k)(t)mi(t)dwk(t).
(5.5)
Due to FW
t -measurability of uk(t), we have
uk,α(t) = E

uk(t)E(ξα|FW
t )

= E(uk(t)ξα(t)).
(5.6)
The definition of U implies dU(t) = 
k≥1 uk(t)dwk(t), so that, by (5.5),
(5.6), and the Itˆo formula,
Uα(t) = E(U(t)ξα) =
 t
0

i,k
H
αk
i uk,α−(i,k)(s)mi(s)ds.
(5.7)
Together with (5.2), the last equality implies (5.4). Lemma 5.1 is proved.
Note that the coefficients uk,α of u ∈L2(W; L2((0, T); H)) belong to
L2((0, T)). We therefore define uk,α,i =
 T
0 uk,α(t)mi(t)dt. Then, by (5.7),
Uα(T) =

i,k
H
αk
i uk,α−(i,k),i.
(5.8)
Since U(T) = 
α∈J Uα(T)ξα, we shift the summation index in (5.8) and
conclude that
U(T) =

α∈J

i,k
H
αk
i + 1uk,α,iξα+(i,k),
(5.9)
where

α+(i, k)
l
j =
αk
i + 1, if i = j and k = l,
αl
j,
otherwise.
(5.10)
As a result, U(T) = δ(u), where δ is the adjoint of the Malliavin deriva-
tive, also known as the Skorohod integral (called also the Skorohod–Hitsuda
integral); see [10], [37] or [38] for details.
Lemma 5.1 suggests the following definition.
For an FW
t -adapted process u from L2 (W; L2((0, T))), let D∗
ku be the
FW
t -adapted process from L2 (W; L2((0, T))) such that
(D∗
ku)α(t) =
 t
0

i
H
αk
i uα−(i,k)(s)mi(s)ds.
(5.11)
If u ∈L2 (W; L2((0, T); Y )) is FW
t -adapted, then u is in the domain of the
operator δ and δ(uI(s < t)) = 
k≥1(D∗
kuk)(t).
We now extend the operators D∗
k to the generalized random processes. Let
X be a Banach space with norm ∥· ∥X.

452
S. Lototsky and B. Rozovskii
Definition 5.1 If u is an X-valued generalized random process, then D∗
ku is
the X-valued generalized random process such that
(D∗
ku)α(t) =

i
 t
0
uα−(i,k)(s)
H
αk
i mi(s)ds.
(5.12)
If g ∈D′
Y ; D′ (L2(W); L1((0, T); X))

, then D∗g is the X-valued generalized
random process such that, for g = 
k≥1 gk⊗yk, gk ∈D′(L2(W); L1((0, T); X)),
(D∗g)α(t) =

k
(D∗
kgk)α(t) =

i,k
 t
0
gk,α−(i,k)(s)
H
αk
i mi(s)ds.
(5.13)
Using (5.2), we get a generalization of equality (5.4):
(D∗g)α(t) =
 t
0
g(Dξα(s))(s)ds.
(5.14)
Indeed, by linearity,
gk
H
αk
i mi(s)ξα−(i,k)

(s) =
H
αk
i mi(s)gk,α−(i,k))(s).
Theorem 5.1. If T < ∞, then D∗
k and D∗are continuous linear operators.
Proof. It is enough to show that, if u, un ∈D′ 
L2(FW
T ); L1((0, T); X)

and
limn→∞∥uα −un,α∥L1((0,T );X) = 0 for every α ∈J , then, for every k ≥1 and
α ∈J ,
lim
n→∞∥(D∗
ku)α −(D∗
kun)α∥L1((0,T );X) = 0.
Using (5.12), we find that
∥(D∗
ku)α −(D∗
kun)α∥X(t) ≤

i
 T
0
H
αk
i ∥uα−(i,k) −un,α−(i,k)∥X(s)|mi(s)|ds.
Note that the sum contains finitely many terms. By assumption, |mi(t)| ≤Ci,
and so
∥(D∗
ku)α−(D∗
kun)α∥L1((0,T );X) ≤C(α)

i
H
αk
i ∥uα−(i,k)−un,α−(i,k)∥L1((0,T );X).
Theorem 5.1 is proved.
6 The Wiener Chaos Solution and the Propagator
In this section we build on the ideas from [25] to introduce the Wiener Chaos
solution and the corresponding propagator for a general stochastic evolution

Wiener Chaos for Stochastic Equations
453
equation. The notations from Sections 4 and 5 will remain in force. It will
be convenient to interpret the cylindrical Brownian motion W as a collection
{wk, k ≥1} of independent standard Wiener processes. As before, T ∈(0, ∞)
is fixed and non-random. Introduce the following objects:
•
The Banach spaces A, X, and U such that U ⊆X.
•
Linear operators
A : L1((0, T); A) →L1((0, T); X),
Mk : L1((0, T); A) →L1((0, T); X).
•
Generalized random processes f ∈D′ (L2(W); L1((0, T); X)) and
gk ∈D′ (L2(W); L1((0, T); X)) .
•
The initial condition u0 ∈D′ (L2(W); U).
Consider the deterministic equation
v(t) = v0 +
 t
0
(Av)(s)ds +
 t
0
ϕ(s)ds,
(6.1)
where v0 ∈U and ϕ ∈L1((0, T); X).
Definition 6.1 A function v is called a w(A, X) solution of (6.1) if and only
if v ∈L1((0, T); A) and equality (6.1) holds in the space L1((0, T); A).
Definition 6.2 An A-valued generalized random process u is called a w(A, X)
Wiener Chaos solution of the stochastic differential equation
du(t) = (Au(t)+f(t))dt+(Mku(t)+gk(t))dwk(t), t ≤T, u|t=0 = u0, (6.2)
if and only if the equality
u(t) = u0 +
 t
0
(Au + f)(s)ds +

k≥1
(D∗
k(Mku + gk))(t)
(6.3)
holds in D′ (L2(W); L1((0, T); X)).
Sometimes, to stress the dependence of the Wiener Chaos solution on the
terminal time T, the notation wT (A, X) will be used.
Equalities (6.3) (5.13) mean that, for every α ∈J , the generalized Fourier
coefficient uα of u satisfies the equation
uα(t) = u0,α +
 t
0
(Au+f)α(s)ds+
 t
0

i,k
H
αk
i (Mku+gk)α−(i,k)(s)mi(s)ds.
(6.4)
Definition 6.3 System (6.4) is called the propagator for equation (6.2).

454
S. Lototsky and B. Rozovskii
The propagator is a lower triangular system. Indeed, If α = (0), that is,
|α| = 0, then the corresponding equation in (6.4) becomes
u(0)(t) = u0,(0) +
 t
0
(Au(0)(s) + f(0)(s))ds.
(6.5)
If α = (jℓ), that is, αℓ
j = 1 for some fixed j and ℓand αk
i = 0 for all other
i, k ≥1, then the corresponding equation in (6.4) becomes
u(jℓ)(t) = u0,(jℓ) +
 t
0
(Au(jℓ)(s) + f(jℓ)(s))ds
+
 t
0
(Mku(0)(s) + gℓ,(0)(s))mj(s)ds.
(6.6)
Continuing in this way, we conclude that (6.4) can be solved by induction on
|α| as long as the corresponding deterministic equation (6.1) is solvable. The
precise result is as follows.
Theorem 6.1. If, for every v0 ∈U and ϕ ∈L1((0, T); X), equation (6.1) has
a unique w(A, X) solution v(t) = V (t, v0, ϕ), then equation (6.2) has a unique
w(A, X) Wiener Chaos solution such that
uα(t) = V (t, u0,α, fα) +

i,k
H
αk
i V (t, 0, miMkuα−(i,k))
+

i,k
H
αk
i V (t, 0, migk,α−(i,k)).
(6.7)
Proof. Using the assumptions of the theorem and linearity, we conclude that
(6.7) is the unique solution of (6.4).
To derive a more explicit formula for uα, we need some additional con-
structions. For every multi-index α with |α| = n, define the characteristic
set Kα of α as
Kα = {(iα
1 , kα
1 ), . . . , (iα
n, kα
n)},
iα
1 ≤iα
2 ≤. . . ≤iα
n, and if iα
j = iα
j+1, then kα
j ≤kα
j+1. The first pair (iα
1 , kα
1 )
in Kα is the position numbers of the first nonzero element of α. The second
pair is the same as the first if the first nonzero element of α is greater than
one; otherwise, the second pair is the position numbers of the second nonzero
element of α and so on. As a result, if αk
i > 0, then exactly αk
i pairs in Kα
are equal to (i, k). For example, if
α =





0 1 0 2 3 0 0 · · ·
1 2 0 0 0 1 0 · · ·
0 0 0 0 0 0 0 · · ·
...
...
...
...
...
...
... · · ·






Wiener Chaos for Stochastic Equations
455
with nonzero elements
α2
1 = α1
2 = α6
1 = 1, α2
2 = α1
4 = 2, α1
5 = 3,
then the characteristic set is
Kα ={(1, 2), (2, 1), (2, 2), (2, 2), (4, 1), (4, 1), (5, 1), (5, 1), (5, 1), (6, 2)}.
Theorem 6.2. Assume that:
1. For every v0 ∈U and ϕ ∈L1((0, T); X), equation (6.1) has a unique
w(A, X) solution v(t) = V (t, v0, ϕ),
2. The input data in (6.4) satisfy gk = 0 and fα = u0,α = 0 if |α| > 0.
Let u(0)(t) = V (t, u0, 0) be the solution of (6.4) for |α| = 0. For α ∈J with
|α| = n ≥1 and the characteristic set Kα, define functions F n = F n(t; α) by
induction as follows:
F 1(t; α) = V (t, 0, miMku(0)) if Kα = {(i, k)};
F n(t; α) =
n

j=1
V (t, 0, mijMkjF n−1(·; α−(ij, kj)))
if Kα = {(i1, k1), . . . , (in, kn)}.
(6.8)
Then
uα(t) =
1
√
α!
F n(t; α).
(6.9)
Proof. If |α| = 1, then representation (6.9) follows from (6.6). For |α| > 1,
observe that:
•
If ¯uα(t) =
√
α!uα and |α| ≥1, then (6.4) implies the relation
¯u(t) =
 t
0
A¯uα(s)ds +

i,k
 t
0
αk
i mi(s)Mk¯uα−(i,k)(s)ds.
•
If Kα = {(i1, k1), . . . , (in, kn)}, then, for every j = 1, . . . , n, the character-
istic set Kα−(ij,kj) of α−(ij, kj) is obtained from Kα by removing the pair
(ij, kj).
•
By the definition of the characteristic set,

i,k
αk
i mi(s)Mk¯uα−(i,k)(s) =
n

j=1
mij(s)Mkj ¯uα−(ij,kj)(s).
As a result, representation (6.9) follows by induction on |α| using (6.7):
if |α| = n > 1, then

456
S. Lototsky and B. Rozovskii
¯uα(t) =
n

j=1
V (t, 0, mijMkj ¯uα−(ij,kj))
=
n

j=1
V (t, 0, mijMkjF (n−1)(·; α−(ij, kj)) = F n(t; α).
(6.10)
Theorem 6.2 is proved.
Corollary 6.1 Assume that the operator A is a generator of a strongly con-
tinuous semigroup Φ = Φt,s, t ≥s ≥0, in some Hilbert space H such that
A ⊂H, each Mk is a bounded operator from A to H, and the solution
V (t, 0, ϕ) of equation (6.1) is written as
V (t, 0, ϕ) =
 T
0
Φt,sϕ(s)ds,
ϕ ∈L2((0, T); H)).
(6.11)
Denote by Pn the permutation group of {1, . . . , n}. If u(0) ∈L2((0, T); H)),
then, for |α| = n > 1 with the characteristic set Kα = {(i1, k1), . . . , (in, kn)},
representation (6.9) becomes
uα(t) =
1
√
α!

σ∈Pn
 t
0
 sn
0
. . .
 s2
0
Φt,snMkσ(n) · · · Φs2,s1Mkσ(1)u(0)(s1)miσ(n)(sn) · · · miσ(1)(s1)ds1 . . . dsn.
(6.12)
Also,

|α|=n
uα(t)ξα =

k1,...,kn≥1
 t
0
 sn
0
. . .
 s2
0
Φt,snMkn · · · Φs2,s1

Mk1u(0) + gk1(s1)

dwk1(s1) · · · dwkn(sn), n ≥1,
(6.13)
and, for every Hilbert space X, the following energy equality holds:

|α|=n
∥uα(t)∥2
X =
∞

k1,...,kn=1
 t
0
 sn
0
. . .
 s2
0
∥Φt,snMkn · · · Φs2,s1Mk1u(0)(s1)∥2
Xds1 . . . dsn;
(6.14)
both sides in the last equality can be infinite. For n = 1, formulas (6.12) and
(6.14) become
u(ik)(t) =
 t
0
Φt,sMku(0)(s) mi(s)ds;
(6.15)

|α|=1
∥uα(t)∥2
X =
∞

k=1
 t
0
∥Φt,sMku(0)(s)∥2
Xds.
(6.16)

Wiener Chaos for Stochastic Equations
457
Proof. Using the semigroup representation (6.11), we conclude that (6.12) is
just an expanded version of (6.9).
Since {mi, i ≥1} is an orthonormal basis in L2(0, T), equality (6.16)
follows from (6.15) and the Parcevall identity. Similarly, equality (6.14) will
follow from (6.12) after an application of an appropriate Parcevall’s identity.
To carry out the necessary arguments when |α| > 1, denote by J1 the
collection of one-dimensional multi-indices β = (β1, β2, . . .) such that each βi
is a non-negative integer and |β| = 
i≥1 βi < ∞. Given a β ∈J1 with |β| = n,
we define Kβ = {i1, . . . , in}, the characteristic set of β and the function
Eβ(s1, . . . , sn) =
1
√β!n!

σ∈Pn
mi1(sσ(1)) · · · min(sσ(n)).
(6.17)
By construction, the collection {Eβ, β ∈J1, |β| = n} is an orthonormal basis
in the subspace of symmetric functions in L2((0, T)n; X).
Next, we rewrite (6.12) in a symmetrized form. To make the notations
shorter, denote by s(n) the ordered set (s1, . . . , sn) and write dsn = ds1 . . . dsn.
Fix t ∈(0, T] and the set k(n) = {k1, . . . , kn} of the second components of the
characteristic set Kα. Define the symmetric function
G(t, k(n); s(n))
=
1
√
n!

σ∈Pn
Φt,sσ(n)Mkn · · · Φsσ(2),sσ(1)Mk1u(0)(sσ(1))1sσ(1)<···<sσ(n)<t(s(n)).
(6.18)
Then (6.12) becomes
uα(t) =

[0,T ]n G(t, k(n); s(n))Eβ(α)(s(n))dsn,
(6.19)
where the multi-indices α and β(α) are related via their characteristic sets: if
Kα = {(i1, k1), . . . , (in, kn)},
then
Kβ(α) = {i1, . . . , in}.
Equality (6.19) means that, for fixed k(n), the function uα is a Fourier coef-
ficient of the symmetric function G(t, k(n); s(n)) in the space L2((0, T)n; X).
Parcevall’s identity and summation over all possible k(n) yield the equality

|α|=n
∥uα(t)∥2
X = 1
n!
∞

k1,...,kn=1

[0,T ]n ∥G(t, k(n); s(n))∥2
Xdsn,
which, due to (6.18), is the same as (6.14).

458
S. Lototsky and B. Rozovskii
To prove equality (6.13), relating the Cameron–Martin and multiple Itˆo
integral expansions of the solution, we use the following result [13, Theorem
3.1]:
ξα =
1
√
α!
 T
0
 sn
0
· · ·
 s2
0
Eβ(α)(s(n))dwk1(s1) · · · dwkn(sn);
see also [37, pp. 12–13]. Since the collection of all Eβ is an orthonormal basis,
equality (6.13) follows from (6.19) after summation over al k1, . . . , kn.
Corollary 6.1 is proved.
We now present several examples to illustrate the general results.
Example 6.1 Consider the following equation:
du(t, x) = (auxx(t, x) + f(t, x))dt + (σux(t, x) + g(t, x))dw(t), x ∈R, (6.20)
where a > 0, σ ∈R, f ∈L2((0, T); H−1
2 (R)), g ∈L2((0, T); L2(R)), and
u|t=0 = u0 ∈L2(R). By Theorem 2.2, if σ2 < 2a, then equation (6.20) has a
unique traditional solution u ∈L2

W; L2((0, T); H1
2(R))

.
By FW
t -measurability of u(t), we have
E(u(t)ξα) = E(u(t)E(ξα|FW
t )).
Using the relation (5.5) and the Itˆo formula, we find that uα satisfy
duα = a(uα)xxdt +

i
√αiσ(uα−(i))xmi(t)dt,
which is precisely the propagator for equation (6.20). In other words, in the
case 2a > σ2 the traditional solution of (6.20) coincides with the Wiener
Chaos solution.
On the other hand, the heat equation
v(t, x) = v0(x) +
 t
0
vxx(s, x)ds +
 t
0
ϕ(s, x)ds, v0 ∈L2(R),
with ϕ ∈L2((0, T); H−1
2 (R)) has a unique w(H1
2(R), H−1
2 (R)) solution. There-
fore, by Theorem 6.1, the unique w(H1
2(R), H−1
2 (R)) Wiener Chaos solution
of (6.20) exists for all σ ∈R.
In the next example, the equation, although not parabolic, can be solved
explicitly.
Example 6.2 Consider the following equation:
du(t, x) = ux(t, x)dw(t), t > 0, x ∈R;
u(0, x) = x.
(6.21)
Clearly, u(t, x) = x + w(t) satisfies (6.21).

Wiener Chaos for Stochastic Equations
459
To find the Wiener Chaos solution of (6.21), note that, with one-
dimensional Wiener process, αk
i = αi, and the propagator in this case becomes
uα(t, x) = xI(|α| = 0) +
 t
0

i
√αi(uα−(i)(s, x))xmi(s)ds.
Then uα = 0 if |α| > 1, and
u(t, x) = x +

i≥1
ξi
 t
0
mi(s)ds = x + w(t).
(6.22)
Even though Theorem 6.1 does not apply, the above arguments show that
u(t, x) = x + w(t) is the unique w(A, X) Wiener Chaos solution of (6.21) for
suitable spaces A and X, for example,
X =

f :

R
(1 + x2)−2f 2(x)dx < ∞

and A = {f : f, f ′ ∈X}.
Section 14 provides a more detailed analysis of equation (6.21).
If equation (6.2) is anticipating, that is, the initial condition is not de-
terministic and/or the free terms f, g are not FW
t -adapted, then the Wiener
Chaos solution generalizes the Skorohod integral interpretation of the equa-
tion.
Example 6.3 Consider the equation
du(t, x) = 1
2uxx(t, x)dt + ux(t, x)dw(t), x ∈R,
(6.23)
with initial condition u(0, x) = x2w(T). Since w(T) =
√
Tξ1, we find that
(uα)t(t, x) = 1
2(uα)xx(t, x) +

i
√αimi(t)(uα−(i))x(t, x)
(6.24)
with initial condition uα(0, x) =
√
Tx2I(|α| = 1, α1 = 1). By Theorem 6.1,
there exists a unique w(A, X) Wiener Chaos solution of (6.23) for suitable
spaces A and X. For example, we can take
X =

f :

R
(1 + x2)−8f 2(x)dx < ∞

and A = {f : f, f ′, f ′′ ∈X}.
System (6.24) can be solved explicitly. Indeed, uα ≡0 if |α| = 0 or |α| > 3 or
if α1 = 0. Otherwise, writing Mi(t) =
 t
0 mi(s)ds, we find:

460
S. Lototsky and B. Rozovskii
uα(t, x) = (t + x2)
√
T, if |α| = 1, α1 = 1;
uα(t, x) = 2
√
2 xt, if |α| = 2, α1 = 2;
uα(t, x) = 2
√
T xMi(t), if |α| = 2, α1 = αi = 1, 1 < i;
uα(t, x) =

6
T t2, if |α| = 3, α1 = 3;
uα(t, x) = 2
√
2T M1(t)Mi(t), if |α| = 3, α1 = 2, αi = 1, 1 < i;
uα(t, x) =
√
2T M 2
i (t), if |α| = 3, α1 = 1, αi = 2, 1 < i;
uα(t, x) = 2
√
T Mi(t)Mj(t), if |α| = 3, α1 = αi = αj = 1, 1 < i < j.
Then
u(t, x) =

α∈J
uαξα = w(T)w2(t)−2tw(t)+2(W(T)w(t)−t)x+x2w(T) (6.25)
is the Wiener Chaos solution of (6.23). It can be verified using the properties
of the Skorohod integral [37] that the function u defined by (6.25) satisfies
u(t, x) = x2w(T) + 1
2
 t
0
uxx(s, x)ds +
 t
0
ux(s, x)dw(s), t ∈[0, T], x ∈R,
where the stochastic integral is in the sense of Skorohod.
7 Weighted Wiener Chaos Spaces and S-Transform
The space D′(L2(W); X) is too big to provide any reasonable information
about regularity of the Wiener Chaos solution. Introduction of weighted
Wiener chaos spaces makes it possible to resolve this difficulty.
As before, let Ξ = {ξα, α ∈J } be the Cameron–Martin basis in L2(W),
and D(L2(W); X), the collection of finite linear combinations of ξα with co-
efficients in a Banach space X.
Definition 7.1 Given a collection {rα, α ∈J } of positive numbers, the space
RL2(W; X) is the closure of D(L2(W); X) with respect to the norm
∥v∥2
RL2(W;X) :=

α∈J
r2
α∥vα∥2
X.
The operator R defined by (Rv)α := rαvα is a linear homeomorphism
from RL2(W; X) to L2(W; X).
There are several special choices of the weight sequence R = {rα, α ∈J }
and special notations for the corresponding weighted Wiener Chaos spaces.

Wiener Chaos for Stochastic Equations
461
•
If Q = {q1, q2, . . .} is a sequence of positive numbers, define
qα =
(
i,k
qαk
i
k .
The operator R, corresponding to rα = qα, is denotes by Q. The space
QL2(W; X) is denoted by L2,Q(W; X) and is called a Q-weighted Wiener
Chaos space. The significance of this choice of weights will be explained
shortly (see, in particular, Proposition 7.2).
•
If
r2
α = (α!)ρ (
i,k
(2ik)γαk
i , ρ, γ ∈R,
then the corresponding space RL2(W; X) is denoted by (S)ρ,γ(X). As
always, the argument X will be omitted if X = R. Note the analogy with
Definition 3.2.
The structure of weights in the spaces L2,Q and (S)ρ,γ is different, and
in general these two classes of spaces are not related. There exist generalized
random elements that belong to some L2,Q(W; X), but do not belong to any
(S)ρ,γ(X). For example, u = 
k≥1 ek2ξ1,k belongs to L2,Q(W) with qk =
e−2k2, but to no (S)ρ,γ, because the sum 
k≥1 e2k2(k!)ρ(2k)γ diverges for
every ρ, γ ∈R. Similarly, there exist generalized random elements that belong
to some (S)ρ,γ(X), but to no L2,Q(W; X). For example, u = 
n≥1
√
n!ξ(n),
where (n) is the multi-index with α1
1 = n and αk
i = 0 elsewhere, belongs to
(S)−1,−1, but does not belong to any L2,Q(W), because the sum 
n≥1 qnn!
diverges for every q > 0.
The next result is the space-time analog of Proposition 2.3.3 in [12].
Proposition 7.1 The sum

α∈J
(
i,k≥1
(2ik)−γαk
i
converges if and only if γ > 1.
Proof. Note that

α∈J
(
i,k≥1
(2ik)−γαk
i =
(
i,k≥1


n≥0
((2ik)−γ)n

=
(
i,k
1
(1 −(2ik)−γ), γ > 0
(7.1)
The infinite product on the right of (7.1) converges if and only if each of the
sums 
i≥1 i−γ, 
k≥1 k−γ converges, that is, if an only if γ > 1.
Corollary 7.1 For every u ∈D′(W; X), there exists an operator R such that
Ru ∈L2(W; X).

462
S. Lototsky and B. Rozovskii
Proof. Define
r2
α =
1
1 + ∥uα∥2
X
(
i,k≥1
(2ik)−2αk
i .
Then
∥Ru∥2
L2(W;X) =

α∈J
∥uα∥2
X
1 + ∥uα∥2
X
(
i,k≥1
(2ik)−2αk
i ≤

α∈J
(
i,k≥1
(2ik)−2αk
i < ∞.
The importance of the operator Q in the study of stochastic equations
is due to the fact that the operator R maps a Wiener Chaos solution to a
Wiener Chaos solution if and only R = Q for some sequence Q. Indeed, direct
calculations show that the functions uα, α ∈J , satisfy the propagator (6.4)
if and only if vα = (Ru)α satisfy the equation
vα(t) = (Ru0)α +
 t
0
(Av + Rf)α(s)ds
+
 t
0

i,k
H
αk
i
ρα
ρα−(i,k)
(MkRu + Rgk)α−(i,k)(s)mi(s)ds.
(7.2)
Therefore, the operator R preserves the structure of the propagator if and
only if
ρα
ρα−(i,k)
= qk,
that is, ρα = qα for some sequence Q.
Below is the summary of the main properties of the operator Q.
Proposition 7.2
1. If qk ≤q < 1 for all k ≥1, then L2,Q(W) ⊂(S)0,−γ for some γ > 0.
2. If qk ≥q > 1 for all k, then L2,Q(W) ⊂Ln
2(W) for all n ≥1, that is, the
elements of L2,Q(W) are infinitely differentiable in the Malliavin sense.
3. If u ∈L2,Q(W; X) with generalized Fourier coefficients uα satisfying the
propagator (6.4), and v = Qu, then the corresponding system for the
generalized Fourier coefficients of v is
vα(t) = (Qu0)α +
 t
0
(Av + Qf)α(s)ds
+
 t
0

i,k
H
αk
i (Mkv + Qgk)α−(i,k)(s)qkmi(s)ds.
(7.3)
4. The function u is a Wiener Chaos solution of
u(t) = u0 +
 t
0
(Au(s) + f(s))dt +
 t
0
(Mu(s) + g(s), dW(s))Y
(7.4)

Wiener Chaos for Stochastic Equations
463
if and only if v = Qu is a Wiener Chaos solution of
v(t) = (Qu)0 +
 t
0
(Av(s) + Qf(s))dt +
 t
0
(Mv(s) + Qg(s), dW Q(s))Y ,
(7.5)
where, for h ∈Y , W Q
h (t) = 
k≥1(h, yk)Y qkwk(t).
The following examples demonstrate how the operator Q helps with the
analysis of various stochastic evolution equations.
Example 7.1 Consider the w(H1
2(R), H−1
2 (R)) Wiener Chaos solution u of
equation
du(t, x) = (auxx(t, x) + f(t, x))dt + σux(t, x)dw(t),
x ∈R,
(7.6)
with f ∈L2(Ω× (0, T); H−1
2 (R)), g ∈L2(Ω× (0, T); L2(R)), and the initial
data u|t=0 = u0 ∈L2(R). Assume that σ > 0 and define the sequence Q such
that qk = q for all k ≥1 and q <
√
2a/σ. By Theorem 2.2, the equation
dv = (avxx + f)dt + (qσux + g)dw
with v|t=0 = u0, has a unique traditional solution
v ∈L2

W; L2((0, T); H1
2(R))
 ?
L2 (W; C((0, T); L2(R))) .
By Proposition 7.2, the w(H1
2(R), H−1
2 (R)) Wiener Chaos solution u of equa-
tion (7.6) satisfies u = Q−1v and
u ∈L2,Q

W; L2((0, T); H1
2(R))
 ?
L2,Q (W; C((0, T); L2(R))) .
Note that if equation (7.6) is strongly parabolic, that is, 2a > σ2, then the
weight q can be taken bigger than one, and, according to the first statement
of Proposition 7.2, regularity of the solution is better than the one guaranteed
by Theorem 2.2.
Example 7.2 The Wiener Chaos solutions can be constructed for stochastic
ordinary differential equations. Consider, for example,
u(t) = 1 +
 t
0

k≥1
u(s)dwk(s),
(7.7)
which clearly does not have a traditional solution. On the other hand,
the unique w(R, R) Wiener Chaos solution of this equation belongs to
L2,Q (W; L2((0, T)) for every Q satisfying 
k q2
k < ∞. Indeed, for (7.7), equa-
tion (7.5) becomes
v(t) = 1 +
 t
0

k
v(s)qkdwk(s).
If 
k q2
k < ∞, then the traditional solution of this equation exists and belongs
to L2 (W; L2((0, T))).

464
S. Lototsky and B. Rozovskii
There exist equations for which the Wiener Chaos solution does not be-
long to any weighted Wiener chaos space L2,Q. An example is given below in
Section 14.
To define the S-transform, consider the following analog of the stochastic
exponential (3.6).
Lemma 7.1. If h ∈D (L2((0, T); Y )) and
E(h) = exp
	 T
0
(h(t), dW(t))Y −1
2
 T
0
∥h(t)∥2
Y dt

,
then
•
E(h) ∈L2,Q(W) for every sequence Q.
•
E(h) ∈(S)ρ,γ for ρ ∈[0, 1) and γ ≥0.
•
E(h) ∈(S)1,γ, γ ≥0, as long as ∥h∥2
L2((0,T );Y ) is sufficiently small.
Proof. Recall that, if h ∈D(L2((0, T); Y )), then h(t) = 
i,k∈Ih hk,imi(t)yk,
where Ih is a finite set. Direct computations show that
E(h) =
(
i,k


n≥0
Hn(ξik)
n!
(hk,i)n

=

α∈J
hα
√
α!
ξα
where hα = K
i,k hαk
i
k,i. In particular,
(E(h))α = hα
√
α!
.
(7.8)
Consequently, for every sequence Q of positive numbers,
∥E(h)∥2
L2,Q(W) = exp


i,k∈Ih
h2
k,iq2
k

< ∞.
(7.9)
Similarly, for ρ ∈[0, 1) and γ ≥0,
∥E(h)∥2
(S)ρ,γ =

α∈J
(
i,k
((2ik)γhk,i)2αk
i
(αk
i !)1−ρ
=
(
i,k∈Ih


n≥0
((2ik)γhk,i)2n
(n!)1−ρ

< ∞,
(7.10)
and, for ρ = 1,
∥E(h)∥2
(S)1,γ =

α∈J
(
i,k
((2ik)γhk,i)2αk
i =
(
i,k∈Ih


n≥0
((2ik)γhk,i)2n

< ∞,
(7.11)
if 2

max(m,n)∈Ih)(mn)γ 
i,k h2
k,i < 1. Lemma 7.1 is proved.

Wiener Chaos for Stochastic Equations
465
Remark 7.1
It is well-known (see, for example, [24, Proof of Theorem 5.5])
that the family {E(h), h ∈D (L2((0, T); Y ))} is dense in L2(W) and conse-
quently in every L2,Q(W) and every (S)ρ,γ, −1 < ρ ≤1, γ ∈R.
Definition 7.2 If u ∈L2,Q(W; X) for some Q, or if u ∈I
q≥0(S)−ρ,−γ(X),
0 ≤ρ ≤1, then the deterministic function
Su(h) =

α∈J
uαhα
√
α!
∈X
(7.12)
is called the S-transform of u. Similarly, for g ∈D′ (Y ; L2,Q(W; X)) the
S-transform Sg(h) ∈D′(Y ; X) is defined by setting (Sg(h))k = (Sgk)(h).
Note that if u ∈L2(W; X), then Su(h) = E(uE(h)). If u belongs to
L2,Q(W; X) or to I
q≥0(S)−ρ,−γ(X), 0 ≤ρ < 1, then Su(h) is defined for
all h ∈D (L2((0, T); Y )) . If u ∈I
γ≥0(S)−1,−γ(X), then Su(h) is defined
only for h sufficiently close to zero.
By Remark 7.1, an element u from L2,Q(W; X) or I
γ≥0(S)−ρ,−γ(X), 0 ≤
ρ < 1, is uniquely determined by the collection of deterministic functions
Su(h), h ∈D (L2((0, T); Y )) . Since E(h) > 0 for all h ∈D (L2((0, T); Y )),
Remark 7.1 also suggests the following definition.
Definition 7.3 An element u from L2,Q(W) or I
γ≥0(S)−ρ,−γ, 0 ≤ρ < 1,
is called non-negative (u ≥0) if and only if the inequality Su(h) ≥0 holds
whatever is h ∈D (L2((0, T); Y )).
The definition of the operator Q and Definition 7.3 imply the following
result.
Proposition 7.3 A generalized random element u from L2,Q(W) is non-
negative if and only if Qu ≥0.
For example, the solution of equation (7.7) is non-negative because
Qu(t) = exp


k≥1
(qkwk(t) −(1/2)q2
k)

.
We conclude this section with one technical remark.
Definition 7.2 expresses the S-transform in terms of the generalized Fourier
coefficients. The following results makes it possible to recover generalized
Fourier coefficients from the corresponding S-transform.
Proposition 7.4 If u belongs to some L2,Q(W; X) or I
γ≥0(S)−ρ,−γ(X) with
0 ≤ρ ≤1, then
uα =
1
√
α!

(
i,k
∂αk
i Su(h)
∂h
αk
i
k,i



h=0
.
(7.13)

466
S. Lototsky and B. Rozovskii
Proof. For each α ∈J with K non-zero entries, equality (7.12) and Lemma
7.1 imply that the function Su(h), as a function of K variables hk,i, is analytic
in some neighborhood of zero. Then (7.13) follows after differentiation of the
series (7.12).
8 General Properties of the Wiener Chaos Solutions
Using notations and assumptions from Section 6, consider the linear evolution
equation
du(t) = (Au(t) + f(t))dt + (Mu(t) + g(t), dW(t))Y ,
u|t=0 = u0.
(8.1)
The objective of this section is to study how the Wiener Chaos compares with
the traditional and white noise solutions.
To make the presentation shorter, we shall call an X-valued generalized
random element S-admissible if and only if it belongs to L2,Q(FW ; X) for
some Q or to (S)ρ,q(X) for some ρ ∈[−1, 1] and q ∈R. It was shown in
Section 7 that, for every S-admissible u, the S-transform Su(h) is defined
when h = 
i,k hk,imiyk ∈D(L2((0, T); Y )) and is an analytic function of
hk,i in some neighborhood of h = 0.
The next result describes the S-transform of the Wiener Chaos solution.
Theorem 8.1. Assume that:
1. There exists a unique w(A, X) Wiener Chaos solution u of (8.1) and u is
S-admissible.
2. For each t ∈[0, T], the linear operators A(t), Mk(t) are bounded from A
to X.
3. The generalized random elements u0, f, gk are S-admissible.
Then, for every h ∈D(L2((0, T); Y )) with ∥h∥2
L2((0,T );Y ) sufficiently small,
the function v = Su(h) is a w(A, X) solution of the deterministic equation
v(t) = Su0(h) +
 t
0

Av + Sf(h) + (Mkv + Sgk(h))hk

(s)ds.
(8.2)
Proof. By assumption, Su(h) exists for suitable functions h. Then the S-
transformed equation (8.2) follows from the definition of the S-transform
(7.12) and the propagator equation (6.4) satisfied by the generalized Fourier
coefficients of u. Indeed, continuity of operator A implies
S(Au)(h) =

α
hα
√
α!
Auα = A

α
hα
√
α!
uα = A(Su(h)).

Wiener Chaos for Stochastic Equations
467
Similarly,

α
hα
√
α!

i,k
H
αk
i Mkuα−(i,k)mi =

α

i,k
hα−(i,k)

α−(i, k)!
Mkuα−(i,k)mihk,i
=

i,k
	
α
hα
√αMkuα

mihk,i = Mk(Su(h))hk.
Computations for the other terms are similar. Theorem 8.1 is proved.
Remark 8.1 If h ∈D(L2((0, T); Y )) and
Et(h) = exp
 t
0
(h(s), dW(s))Y −1
2
 t
0
∥h(t)∥2
Y dt

,
(8.3)
then, by the Itˆo formula,
dEt(h) = Et(h)(h(t), dW(t))Y .
(8.4)
If u0 is deterministic, f and gk are FW
t -adapted, and u is a square-integrable
solution of (8.1), then equality (8.2) is obtained by multiplying equations (8.4)
and (8.1) according to the Itˆo formula and taking the expectation.
Remark 8.2 Rewriting (8.4) as
dEt(h) = Et(h)hk,imi(t)dwk(t)
and using the relations
Et(h) = E(ET (h)|FW
t ), ξα =
1
√
α!

(
i,k
∂αk
i ET (h)
∂h
αk
i
k,i



h=0
,
we arrive at representation (5.5) for E(ξα|FW
t ).
A partial converse of Theorem 8.1 is that, under some regularity conditions,
the Wiener Chaos solution can be recovered from the solution of the S-
transformed equation (8.2).
Theorem 8.2. Assume that the linear operators A(t), Mk(t), t ∈[0, T], are
bounded from A to X, the input data u0, f, gk are S-admissible, and, for
every h ∈D(L2((0, T); Y )) with ∥h∥2
L2((0,T );Y ) sufficiently small, there exists
a w(A, X) solution v = v(t; h) of equation (8.2). We write h = hk,imiyk and
consider v as a function of the variables hk,i. Assume that all the derivatives
of v at the point h = 0 exists, and, for α ∈J , define
uα(t) =
1
√
α!

(
i,k
∂αk
i v(t; h)
∂h
αk
i
k,i



h=0
.
(8.5)
Then the generalized random process u(t) = 
α∈J uα(t)ξα is a w(A, X)
Wiener Chaos solution of (8.1).

468
S. Lototsky and B. Rozovskii
Proof. Differentiation of (8.2) and application of Proposition 7.4 show that
the functions uα satisfy the propagator (6.4).
Remark 8.3 The central part in the construction of the white noise solution
of (8.1) is proving that the solution of (8.2) is an S-transform of a suitable
generalized random process. For many particular cases of equation (8.1), the
corresponding analysis is carried out in [10, 12, 33, 40]. The consequence of
Theorems 8.1 and 8.2 is that a white noise solution of (8.1), if exists, must
coincide with the Wiener Chaos solution.
The next theorem establishes the connection between the Wiener Chaos
solution and the traditional solution. Recall that the traditional, or square-
integrable, solution of (8.1) was introduced in Definition 2.2. Accordingly, the
notations from Section 2 will be used.
Theorem 8.3. Let (V, H, V ′) be a normal triple of Hilbert spaces. Take a
deterministic function u0 and FW
t -adapted random processes f and gk so that
(2.3) holds. Under these assumptions we have the following two statements.
1. An FW
t -adapted traditional solution of (8.1) is also a Wiener Chaos so-
lution.
2. If u is a w(V, V ′) Wiener Chaos solution of (8.1) such that

α∈J
	 T
0
∥uα(t)∥2
V dt + sup
0≤t≤T
∥uα(t)∥2
H

< ∞,
(8.6)
then u is an FW
t -adapted traditional solution of (8.1).
Proof. (1) If u = u(t) is an FW
t -adapted traditional solution, then
uα(t) = E(u(t)ξα) = E

u(t)E(ξα|FW
t )

= E(u(t)ξα(t)).
Then the propagator (6.4) for uα follows after applying the Itˆo formula to the
product u(t)ξα(t) and using (5.5).
(2) Assumption (8.6) implies that
u ∈L2(Ω× (0, T); V )
?
L2(Ω; C((0, T); H)).
Then, by Theorem 8.1, for every ϕ ∈V and h ∈D((0, T); Y ), the S-transform
uh of u satisfies the equation
(uh(t), ϕ)H = (u0, ϕ)H +
 t
0
⟨Auh(s), ϕ⟩ds +
 t
0
⟨f(s), ϕ⟩ds
+

α∈J
hα
α!

i,k
 t
0
H
αk
i mi(s)

(Mkuα−(i,k)(s), ϕ)H
+(gk(s), ϕ)HI(|α| = 1)

ds.

Wiener Chaos for Stochastic Equations
469
If I(t) =
 t
0(Mku(s), ϕ)Hdwk(s), then
E(I(t)ξα(t)) =
 t
0

i,k
H
αk
i mi(s)(Mkuα−(i,k)(s), ϕ)Hds.
(8.7)
Similarly,
E

ξα(t)
 t
0
(gk(s), ϕ)Hdwk(s)

=

i,k
 t
0
H
αk
i mi(s)(gk(s), ϕ)HI(|α| = 1)ds.
Therefore,

α∈J
hα
α!

i,k
 t
0
H
αk
i mi(s)(Mkuα−(i,k)(s), ϕ)Hds
= E

E(h)
 t
0
((Mku(s), ϕ)H + (gk(s), ϕ)H) dwk(s)

.
As a result,
E (E(h)(u(t), ϕ)H) = E (E(h)(u0, ϕ)H)
+ E

E(h)
 t
0
⟨Au(s), ϕ⟩ds

+ E

E(h)
 t
0
⟨f(s), ϕ⟩ds

+ E

E(h)
 t
0
((Mku(s), ϕ)H + (gk(s), ϕ)H) dwk(s)

.
(8.8)
Equality (8.8) and Remark 7.1 imply that, for each t and each ϕ, (2.4)
holds with probability one. Continuity of u implies that, for each ϕ, a sin-
gle probability-one set can be chosen for all t ∈[0, T]. Theorem 9.3 is proved.
9 Regularity of the Wiener Chaos Solution
Let F = (Ω, F, {Ft}t≥0, P) be a stochastic basis with the usual assumptions
and wk = wk(t), k ≥1, t ≥0, a collection of standard Wiener processes
on F. As in Section 2, let (V, H, V ′) be a normal triple of Hilbert spaces and
A(t) : V →V ′, Mk(t) : V →H, linear bounded operators; t ∈[0, T].
In this section we study the linear equation
u(t) = u0 +
 t
0
(Au(s) + f(s))ds +
 t
0
(Mku(s) + gk(s))dwk(s), t ≤T, (9.1)
under the following assumptions:

470
S. Lototsky and B. Rozovskii
A1 There exist positive numbers C1 and δ such that
⟨A(t)v, v⟩+ δ∥v∥2
V ≤C1∥v∥2
H, v ∈V, t ∈[0, T].
(9.2)
A2 There exists a real number C2 such that
2⟨A(t)v, v⟩+

k≥1
∥Mk(t)v∥2
H ≤C2∥v∥2
H, v ∈V, t ∈[0, T].
(9.3)
A3 The initial condition u0 is non-random and belongs to H; the process
f = f(t) is deterministic and
 T
0 ∥f(t)∥2
V ′dt < ∞; each gk = gk(t) is a
deterministic processes and 
k≥1
 T
0 ∥gk(t)∥2
Hdt < ∞.
Note that condition (9.3) is weaker than (2.5). Traditional analysis of
equation (9.1) under (9.3) requires additional regularity assumptions on the
input data and additional Hilbert space constructions beyond the normal
triple [42, Section 3.2]. In particular, no existence of a traditional solution is
known under assumptions A1-A3, and the Wiener Chaos approach provides
new existence and regularity results for equation (9.1). A different version of
the following theorem is presented in [29].
Theorem 9.1. Under assumptions A1–A3, for every T > 0, equation (9.1)
has a unique w(V, V ′) Wiener Chaos solution. This solution u = u(t) has the
following properties:
1. There exists a weight sequence Q such that
u ∈L2,Q(W; L2((0, T); V ))
?
L2,Q(W; C((0, T); H)).
2. For every t ≤T, u(t) ∈L2(Ω; H) and
E∥u(t)∥2
H ≤3eC2t

∥u0∥2
H + Cf
 t
0
∥f(s)∥2
V ′ds +

k≥1
 t
0
∥gk(s)∥2
Hds

,
(9.4)
where the number C2 is from (9.3) and the positive number Cf depends
only on δ and C1 from (9.2).
3. For every t ≤T,
u(t) = u(0) +

n≥1

k1,...,kn≥1
 t
0
 sn
0
. . .
 s2
0
Φt,snMkn · · · Φs2,s1

Mk1u(0) + gk1(s1)

dwk1(s1) · · · dwkn(sn),
(9.5)
where Φt,s is the semigroup of the operator A.

Wiener Chaos for Stochastic Equations
471
Proof. Assumption A2 and the properties of the normal triple imply that
there exists a positive number C∗such that

k≥1
∥Mk(t)v∥2
H ≤C∗∥v∥2
V , v ∈V, t ∈[0, T].
(9.6)
Define the sequence Q such that
qk =
 µδ
C∗
1/2
:= q, k ≥1,
(9.7)
where µ ∈(0, 2) and δ is from Assumption A1. Then, by Assumption A2,
2⟨Av, v⟩+

k≥1
q2∥Mkv∥2
H ≤−(2 −µ)δ∥v∥2
V + C1∥v∥2
H.
(9.8)
It follows from Theorem 2.1 that equation
v(t) = u0 +
 t
0
(Av + f)(s)ds +

k≥1
 t
0
q(Mkv + gk)(s)dwk(s)
(9.9)
has a unique solution
v ∈L2(W; L2((0, T); V ))
?
L2(W; C((0, T); H)).
Comparison of the propagators for equations (9.1) and (9.9) shows that u =
Q−1v is the unique w(V, V ′) solution of (9.1) and
u ∈L2,Q(W; L2((0, T); V ))
?
L2,Q(W; C((0, T); H)).
(9.10)
If C∗< 2δ, then equation (9.1) is strongly parabolic and q > 1 is an
admissible choice of the weight. As a result, for strongly parabolic equations,
the result (9.10) is stronger than the conclusion of Theorem 2.1.
The proof of (9.4) is based on the analysis of the propagator
uα(t) = u0I(|α| = 0) +
 t
0

Auα(s) + f(s)I(|α| = 0)

ds
+
 t
0

i,k
H
αk
i (Mkuα−(i,k)(s) + gk(s)I(|α| = 1))mi(s)ds.
(9.11)
We consider three particular cases: (1) f = gk = 0 (the homogeneous equa-
tion); (2) u0 = gk = 0; (3) u0 = f = 0. The general case will then follow by
linearity and the triangle inequality.
Let us denote by (Φt,s, t ≥s ≥0) the semigroup generated by the oper-
ator A(t); Φt := Φt,0. One of the consequence of Theorem 2.1 is that, under
Assumption A1, this semigroup exists and is strongly continuous in H.

472
S. Lototsky and B. Rozovskii
Consider the homogeneous equation: f = gk = 0. By Corollary 6.1,

|α|=n
∥uα(t)∥2
H =

k1,...,kn≥1
 t
0
 sn
0
· · ·
 s2
0
∥Φt,snMkn· · · Φs2,s1Mk1Φs1u0∥2
Hdsn,
(9.12)
where dsn = ds1 . . . dsn. Define Fn(t) = 
|α|=n ∥uα(t)∥2
H, n ≥0. Direct
application of (9.3) shows that
d
dtF0(t) ≤C2F0(t) −

k≥1
∥MkΦtu0∥2
H.
(9.13)
For n ≥1, equality (9.12) implies that
d
dtFn(t) =

k1,...,kn≥1
 t
0
 sn−1
0
· · ·
 s2
0
∥MknΦt,sn−1 · · · Mk1Φs1u0∥2
Hdsn−1
+

k1,...,kn≥1
 t
0
 sn
0
. . .
 s2
0
⟨AΦt,snMkn . . . Φs1u0, Φt,snMkn . . . Φs1u0⟩dsn.
(9.14)
By (9.3),

k1,...,kn≥1
 t
0
 sn
0
. . .
 s2
0
⟨AΦt,snMkn . . . Φs1u0, Φt,snMkn . . . Φs1u0⟩dsn
≤−

k1,...,kn+1≥1
 t
0
 sn
0
. . .
 s2
0
∥Mkn+1Φt,snMkn . . . Mk1Φs1u0∥2
Hdsn
+C2

k1,...,kn≥1
 t
0
 sn
0
. . .
 s2
0
∥Φt,snMkn . . . Mk1Φs1u0∥2
Hdsn.
(9.15)
As a result, for n ≥1,
d
dtFn(t) ≤C2Fn(t)
+

k1,...,kn≥1
 t
0
 sn−1
0
. . .
 s2
0
∥MknΦt,sn−1Mkn−1 . . . Mk1Φs1u0∥2
Hdsn−1
−

k1,...,kn+1≥1
 t
0
 sn
0
. . .
 s2
0
∥Mkn+1Φt,snMkn . . . Mk1Φs1u0∥2
Hdsn.
(9.16)

Wiener Chaos for Stochastic Equations
473
Consequently,
d
dt
N

n=0

|α|=n
∥uα(t)∥2
H ≤C2
N

n=0

|α|=n
∥uα(t)∥2
H,
(9.17)
so that, by the Gronwall inequality,
N

n=0

|α|=n
∥uα(t)∥2
H ≤eC2t∥u0∥2
H
(9.18)
or
E∥u(t)∥2
H ≤eC2t∥u0∥2
H.
(9.19)
Next, let us assume that u0 = gk = 0. Then the propagator (9.11) becomes
uα(t) =
 t
0
(Auα(s) + f(s)I(|α| = 0))ds +
 t
0

i,k
H
αk
i Mkuα−(i,k)(s)mi(s)ds.
(9.20)
Denote by u(0)(t) the solution corresponding to α = 0. Note that
∥u(0)(t)∥2
H = 2
 t
0
⟨Au(0)(s), u(0)(s)⟩ds + 2
 t
0
⟨f(s), u(0)(s)⟩ds
≤C2
 t
0
∥u(0)(s)∥2
Hds −
 t
0

k≥1
∥Mku(0)(s)∥2
Hds + Cf
 t
0
∥f(s)∥2
V ′ds.
By Corollary 6.1,

|α|=n
∥uα(t)∥2
H =

k1,...,kn≥1
 t
0
 sn
0
. . .
 s2
0
∥Φt,snMkn . . . Mk1u(0)(s1)∥2
Hdsn
(9.21)
for n ≥1. Then, repeating the calculations (9.14)–(9.16), we conclude that
N

n=1

|α|=n
∥uα(t)∥2
H ≤Cf
 t
0
∥f(s)∥2
V ′ds+C2
 t
0
N

n=1

|α|=n
∥uα(s)∥2
Hds, (9.22)
and, by the Gronwall inequality,
E∥u(t)∥2
H ≤CfeC2t
 t
0
∥f(s)∥2
V ′ds.
(9.23)
Finally, let us assume that u0 = f = 0. Then the propagator (9.11) be-
comes
uα(t) =
 t
0
Auα(s)ds
+
 t
0


i,k
H
αk
i Mkuα−(i,k)(s) + gk(s)I(|α| = 1)

mi(s)ds.
(9.24)

474
S. Lototsky and B. Rozovskii
Even though uα(t) = 0 if α = 0, we have
u(ik) =
 t
0
Φt,sgk(s)mi(s)ds,
(9.25)
and then the arguments from the proof of Corollary 6.1 apply, resulting in

|α|=n
∥uα(t)∥2
H =

k1,...,kn≥1
 t
0
 sn
0
. . .
 s2
0
∥Φt,snMkn . . . Φs2,s1gk1(s1)∥2
Hdsn
for n ≥1. Note that

|α|=1
∥uα(t)∥2
H =

k≥1
 t
0
∥gk(s)∥2
Hds + 2

k≥1
 t
0
⟨AΦt,sgk(s), Φt,sgk(s)⟩ds.
Then, repeating the calculations (9.14)–(9.16), we conclude that
N

n=1

|α|=n
∥uα(t)∥2
H ≤

k≥1
 t
0
∥gk(s)∥2
Hds + C2
 t
0
N

n=1

|α|=n
∥uα(s)∥2
Hds,
(9.26)
and, by the Gronwall inequality,
E∥u(t)∥2
H ≤eC2t 
k≥1
 t
0
∥gk(s)∥2
Hds.
(9.27)
To derive (9.4), it remains to combine (9.19), (9.23), and (9.27) with the
elementary inequality (a + b + c)2 ≤3(a2 + b2 + c2).
Representation (9.5) of the Wiener Chaos solution as a sum of iterated Itˆo
integrals now follows from Corollary 6.1. Theorem 9.1 is proved.
Corollary 9.1 If

α∈J
 T
0
∥uα(s)∥2
V ds < ∞, then

α∈J
sup
0≤t≤T
∥uα(t)∥2
H < ∞.
Proof. The proof of Theorem 9.1 shows that it is sufficient to consider the
homogeneous equation. Then, by inequalities (9.15)–(9.16),
n1

ℓ=n+1

|α|=ℓ
∥uα(t)∥2
H =
n1

ℓ=n+1
Fℓ(t)
≤eC2T

k1,...,kn+1≥1
 T
0
 t
0
 sn
0
. . .
 s2
0
∥Mkn+1Φt,snMkn . . . Φs1u0∥2
Hdsndt.
(9.28)
By Corollary 6.1,

Wiener Chaos for Stochastic Equations
475
 T
0
∥uα(s)∥2
V ds
=

n≥1

k1,...,kn≥1
 T
0
 t
0
 sn
0
. . .
 s2
0
∥MknΦt,snMkn . . . Φs1u0∥2
V dsndt < ∞.
(9.29)
As a result, (9.6) and (9.29) imply that
lim
n→∞
 T
0
 t
0
 sn
0
. . .
 s2
0
∥Mkn+1Φt,snMkn . . . Mk1Φs1u0∥2
Hdsndt = 0,
which, by (9.28), implies uniform, with respect to t, convergence of the series

α∈J ∥uα(t)∥2
H. Corollary 9.1 is proved.
Corollary 9.2 Let aij, bi, c, σik, νk be deterministic measurable functions of
(t, x) such that
|aij(t, x)| + |bi(t, x)| + |c(t, x)| + |σik(t, x)| + |νk(t, x)| ≤K,
i, j = 1, . . . , d, k ≥1, x ∈Rd, 0 ≤t ≤T;

aij(t, x) −1
2σik(t, x)σjk(t, x)

yiyj ≥0,
x, y ∈Rd, 0 ≤t ≤T; and

k≥1
|νk(t, x)|2 ≤Cν < ∞,
x ∈Rd, 0 ≤t ≤T. Consider the equation
du = (Di(aijDju) + biDiu + c u + f)dt + (σikDiu + νku + gk)dwk.
(9.30)
Assume that the input data satisfy u0 ∈L2(Rd), f ∈L2((0, T); H−1
2 (Rd)),

k≥1 ∥gk∥2
L2((0,T )×Rd) < ∞, and there exists an ε > 0 such that
aij(t, x)yiyj ≥ε|y|2, x, y ∈Rd, 0 ≤t ≤T.
Then there exists a unique Wiener Chaos solution u = u(t, x) of (9.30). The
solution has the following regularity:
u(t, ·) ∈L2(W; L2(Rd)), 0 ≤t ≤T,
(9.31)
and
E∥u∥2
L2(Rd)(t) ≤C∗
∥u0∥2
L2(Rd) + ∥f∥2
L2((0,T );H−1
2
(Rd))
+

k≥1
∥gk∥2
L2((0,T )×Rd)

,
(9.32)
where the positive number C∗depends only on Cν, K, T, and ε.

476
S. Lototsky and B. Rozovskii
Remark 9.1
(1) If (2.5) holds instead of (9.3), then the proof of Theorem 9.1, in particular,
(9.15)–(9.16), shows that the term E∥u(t)∥2
H in the left-hand-side of inequality
(9.4) can be replaced with
E

∥u(t)∥2
H + ε
 t
0
∥u(s)∥2
V ds

.
(2) If f = gk = 0 and the equation is fully degenerate, that is,
2⟨A(t)v, v⟩+

k≥1
∥Mk(t)v∥2
H = 0,
t ∈[0, T],
then it is natural to expect conservation of energy. Once again, analysis of
(9.15)–(9.16) shows that equality
E∥u(t)∥2
H = ∥u0∥2
H
holds if and only if
lim
n→∞
 T
0
 t
0
 sn
0
. . .
 s2
0
∥Mkn+1Φt,snMkn . . . Mk1Φs1u0∥2
Hdsndt = 0.
The proof of Corollary 9.1 shows that for the conservation of energy in a
fully degenerate homogeneous equation the condition E
 T
0 ∥u(t)∥2
V dt < ∞is
sufficient.
One of applications of the Wiener Chaos solution is new numerical methods
for solving the evolution equations. Indeed, an approximation of the solution
is obtained by truncating the sum 
α∈J uα(t)ξα. For the Zakai filtering equa-
tion, these numerical methods were studied in [25, 26, 27]; see also Section 11
below. The main question in the analysis is the rate of convergence, in n, of the
series 
n≥1

|α|=n ∥u(t)∥2
H. In general, this convergence can be arbitrarily
slow. For example, consider the equation
du = 1
2uxxdt + uxdw(t), t > 0, x ∈R,
in the normal triple (H1
2(R), L2(R), H−1
2 (R)), with the initial condition
u|t=0 = u0 ∈L2(R). It follows from (9.12) that
Fn(t) =

|α|=n
∥u∥2
L2(R)(t) = tn
n!

R
|y|2ne−y2t|ˆu0|2dy,
where ˆu0 is the Fourier transform of u0. If
|ˆu0(y)|2 =
1
(1 + |y|2)γ , γ > 1/2,

Wiener Chaos for Stochastic Equations
477
then the rate of decay of Fn(t) is close to n−(1+2γ)/2. Note that, in this ex-
ample, E∥u∥2
L2(R)(t) = ∥u0∥2
L2(R).
An exponential convergence rate that is uniform in ∥u0∥2
H is achieved un-
der strong parabolicity condition (2.5). An even faster factorial rate is achieved
when the operators Mk are bounded on H.
Theorem 9.2. Assume that there exist a positive number ε and a real number
C0 such that
2⟨A(t)v, v⟩+

k≥1
∥Mk(t)v∥2
H + ε∥v∥2
V ≤C0∥v∥2
H, t ∈[0, T], v ∈V.
Then there exists a positive number b such that, for all t ∈[0, T],

|α|=n
∥uα(t)∥2
H ≤∥u0∥2
H
(1 + b)n .
(9.33)
If, in addition, 
k≥1 ∥Mk(t)ϕ∥2
H ≤C3∥ϕ∥2
H, then

|α|=n
∥uα(t)∥2
H ≤(C3t)n
n!
eC1t∥u0∥2
H.
(9.34)
Proof. If C∗is from (9.6) and b = ε/C∗, then the operators
√
1 + bMk satisfy
the inequality
2⟨A(t)v, v⟩+ (1 + b)

k≥1
∥Mk(t)∥2
H ≤C0∥v∥2
H.
By Theorem 9.1,
(1 + b)n

k1,...,kn≥1
 t
0
 sn
0
. . .
 s2
0
∥Φt,snMkn . . . Mk1Φs1u0∥2
Hdsn ≤∥u0∥2
H,
and (9.33) follows.
To establish (9.34), note that, by (9.2),
∥Φtf∥2
H ≤eC1t∥f∥2
H,
and therefore the result follows from (9.12). Theorem 9.2 is proved.
The Wiener Chaos solution of (9.1) is not, in general, a solution of the
equation in the sense of Definition 2.2. Indeed, if u ̸∈L2(Ω× (0, T); V ), then
the expressions ⟨Au(s), ϕ⟩and (Mku(s), ϕ)H are not defined. On the other
hand, if there is a possibility to move the operators A and M from the solution
process u to the test function ϕ, then equation (9.1) admits a natural analog
of the traditional weak formulation (2.4).

478
S. Lototsky and B. Rozovskii
Theorem 9.3. In addition to A1–A3, assume that there exist operators
A∗(t), M∗
k(t) and a dense subset V0 of the space V such that:
1. A∗(t)(V0) ⊆H, M∗
k(t)(V0) ⊆H, t ∈[0, T].
2. For every v ∈V , ϕ ∈V0, and t ∈[0, T], ⟨A(t)v, ϕ⟩= (v, A∗(t)ϕ)H,
(Mk(t)v, ϕ)H = (v, M∗
k(t)ϕ)H.
If u = u(t) is the Wiener Chaos solution of (9.1), then, for every ϕ ∈V0 and
every t ∈[0, T], the equality
(u(t), ϕ)H = (u0, ϕ)H +
 t
0
(u(s), A∗(s)ϕ)Hds +
 t
0
⟨f(s), ϕ⟩ds
+
 t
0
(u(s), M∗
k(s)ϕ)Hdwk(s) +
 t
0
(gk(s), ϕ)Hdwk(s)
(9.35)
holds in L2(W).
Proof. The arguments are identical to the proof of Theorem 8.3(2).
As was mentioned earlier, the Wiener Chaos solution can be constructed
for anticipating equations, that is, equations with FW
T -measurable input data.
With obvious modifications, inequality (9.4) holds if each of the input func-
tions u0, f, and gk in (9.1) is a finite linear combination of the basis elements
ξα. The following example demonstrates that inequality (9.4) is impossible for
a general anticipating equation.
Example 9.1 Let u = u(t, x) be a Wiener Chaos solution of an ordinary dif-
ferential equation
du = udw(t), t ≤1,
(9.36)
with u0 = 
α∈J aαξα. For n ≥0, denote by (n) the multi-index with α1 = n
and αi = 0, i ≥2, and assume that a(n) > 0, n ≥0. Then
Eu2(1) ≥C

n≥0
e
√na2
(n).
(9.37)
Indeed, the first column of propagator for α = (n) is u(0)(t) = a(0) and
u(n)(t) = a(n) + √n
 t
0
u(n−1)(s)ds,
so that
u(n)(t) =
n

k=0
√
n!

(n −k)!k!
a(n−k)
√
k!
tk.
Then u2
(n)(1) ≥n
k=0
n
k
 a2
(n−k)
k!
and

Wiener Chaos for Stochastic Equations
479

n≥0
u2
(n)(1) ≥

n≥0


k≥0
1
k!
n + k
n

a2
(n).
Since

k≥0
1
k!
n + k
n

≥

k≥0
nk
(k!)2 ≥Ce
√n,
the result follows.
The consequence of Example 9.1 is that it is possible, in (9.1), to have
u0 ∈Ln
2(W; H) for every n, and still get E∥u(t)∥2
H = +∞for all t > 0.
More generally, the solution operator for (9.1) is not bounded on any L2,Q or
(S)−ρ,−γ. On the other hand, the following result holds.
Theorem 9.4. In addition to Assumptions A1, A2, let u0 be an element of
D′(W; H), f, an element of D′(W; L2((0, T), V ′)), and each gk, an element
of D′(W; L2((0, T), H)). Then the Wiener Chaos solution of equation (9.1)
satisfies
L
M
M
N
α∈J
∥uα(t)∥2
H
α!
≤C

α∈J
1
√
α!
	
∥u0α∥H +
 t
0
∥fα(s)∥2
V ′ds
1/2
+


k≥1
 t
0
∥gk,α(s)∥2
Hds


1/2 
,
(9.38)
where C > 0 depends only on T and the numbers δ, C1, and C2 from (9.2)
and (9.3).
Proof. To simplify the presentation, assume that f = gk = 0. For fixed γ ∈J ,
denote by u(t; ϕ; γ) the Wiener Chaos solution of the equation (9.1) with initial
condition u(0; ϕ; γ) = ϕξγ. Denote by (0) the zero multi-index. The structure
of the propagator implies the following relation:
uα+γ(t; ϕ; γ)

(α + γ)!
=
uα

t;
ϕ
√
γ!; (0)

√
α!
.
(9.39)
Clearly, uα(t; ϕ; γ) = 0 if |α| < |γ|. If
∥v(t)∥2
(S)−1,0(H) =

α∈J
∥vα(t)∥2
H
α!
,
then, by linearity and the triangle inequality,
∥u(t)∥(S)−1,0(H) ≤

γ∈J
∥u(t; u0γ; γ)∥(S)−1,0(H).

480
S. Lototsky and B. Rozovskii
We also have by (9.39) and Theorem 9.1
∥u(t; u0γ; γ)∥2
(S)−1,0(H) =
u

t; u0γ
√γ!; (0)

2
(S)−1,0(H)
≤E
u

t; u0γ
√γ!; (0)

2
H
≤eC2t ∥u0γ∥2
H
γ!
.
Inequality (9.38) then follows. Theorem 9.4 is proved.
Remark 9.2 Using Proposition 7.1 and the Cauchy–Schwartz inequality,
(9.38) can be rewritten in a slightly weaker form to reveal continuity of the
solution operator for equation (9.1) from (S)−1,γ to (S)−1,0 for every γ > 1:
∥u(t)∥2
(S)−1,0(H) ≤C
	
∥u0∥2
(S)−1,γ(H) +
 t
0
∥f(s)∥2
(S)−1,γ(V ′)ds
+

k≥1
 t
0
∥gk(s)∥2
(S)−1,γ(H)ds

.
10 Probabilistic Representation of Wiener Chaos
Solutions
The general discussion so far has been dealing with the abstract evolution
equation
du = (Au + f)dt +

k≥1
(Mku + gk)dwk.
By further specifying the operators A and Mk, as well as the input data u0, f,
and gk, it is possible to get additional information about the Wiener Chaos
solution of the equation.
Definition 10.1 For r ∈R, the space L2,(r) = L2,(r)(Rd) is the collection of
real-valued measurable functions such that f ∈L2,(r) if and only if

Rd |f(x)|2(1 + |x|2)rdx < ∞.
The space H1
2,(r) = H1
2,(r)(Rd) is the collection of real-valued measurable func-
tions such that f ∈H1
2,(r) if and only if f and all the first-order generalized
derivatives Dif of f belong to L2,(r).
It is known, for example, from Theorem 3.4.7 in [42], that L2,(r) is a Hilbert
space with the norm
∥f∥2
0,(r) =

Rd |f(x)|2(1 + |x|2)rdx,

Wiener Chaos for Stochastic Equations
481
and H1
2,(r) is a Hilbert space with the norm
∥f∥1,(r) = ∥f∥0,(r) +
d

i=1
∥Dif∥0,(r).
Denote by H−1
2,(r) the dual of H1
2,(r) with respect to the inner product in L2,(r).
Then (H1
2,(r), L2,(r), H−1
2,(r)) is a normal triple of Hilbert spaces.
Let F = (Ω, F, {Ft}t≥0, P) be a stochastic basis with the usual assump-
tions and wk = wk(t), k ≥1, t ≥0, a collection of standard Wiener processes
on F. Consider the linear equation
du = (aijDiDju + biDiu + cu + f)dt + (σikDiu + νku + gk)dwk
(10.1)
under the following assumptions:
B0 All coefficients, free terms, and the initial condition are non-random.
B1 The functions aij = aij(t, x) and their first-order derivatives with respect
to x are uniformly bounded in (t, x), and the matrix (aij) is uniformly
positive definite, that is, there exists δ > 0 such that, for all vectors
y ∈Rd and all (t, x), aijyiyj ≥δ|y|2.
B2 The functions bi = bi(t, x), c = c(t, x), and νk = νk(t, x) are measurable
and bounded in (t, x).
B3 The functions σik = σik(t, x) are continuous and bounded in (t, x).
B4 The functions f = f(t, x) and gk = gk(t, x) belong to L2((0, T); L2,(r)) for
some r ∈R.
B5 The initial condition u0 = u0(x) belongs to L2,(r).
Under Assumptions B2–B4, there exists a sequence Q = {qk, k ≥1} of
positive numbers with the following properties:
P1 The matrix A with Aij = aij−(1/2) 
k≥1 qkσikσjk satisfies the inequality
Aij(t, x)yiyj ≥0,
x, y ∈Rd, 0 ≤t ≤T.
P2 There exists a number C > 0 such that

k≥1
	
sup
t,x |qkνk(t, x)|2 +
 T
0
∥qkgk∥p
0,(r)(t)dt

≤C.
For the matrix A and each t, x, we have Aij(t, x) = ˜σik(t, x)˜σjk(t, x),
where the functions ˜σik are bounded. This representation might not be unique;
see, for example, [7, Theorem III.2.2] or [44, Lemma 5.2.1]. Given any such
representation of A, consider the following backward Itˆo equation

482
S. Lototsky and B. Rozovskii
Xt,x,i (s) = xi +
 t
s
Bi (τ, Xt,x (τ)) dτ +

k≥1
qkσik (τ, Xt,x (τ)) ←−−
dwk (τ)
+
 t
s
˜σik (τ, Xt,x (τ)) ←−
d ˜wk (τ) ; s ∈(0, t), t ∈(0, T], t −fixed,
(10.2)
where Bi = bi −
k≥1 q2
kσikνk and ˜wk, k ≥1, are independent standard
Wiener processes on F that are independent of wk, k ≥1. This equation might
not have a strong solution, but does have a weak, or martingale, solution due
to Assumptions B1–B3 and properties P1 and P2 of the sequence Q; this
weak solution is unique in the sense of probability law [44, Theorem 7.2.1].
The following result is a variation of Theorem 4.1 in [29].
Theorem 10.1. Under assumptions B0–B5 equation (10.1) has a unique
w(H1
2,(r), H−1
2,(r)) Wiener Chaos solution. If Q is a sequence with properties
P1 and P2, then the solution of (10.1) belongs to
L2,Q

W; L2((0, T); H1
2,(r))
 ?
L2,Q

W; C((0, T); L2,(r))

and has the following representation:
u(t, x) = Q−1E
	  t
0
f(s, Xt,x(s))γ(t, s, x)ds
+

k≥1
 t
0
qkgk(s, Xt,x(s))γ(t, s, x)←−−
dwk(s) + u0(Xt,x(0))γ(t, 0, x)
FW
t

, t ≤T,
(10.3)
where Xt,x(s) is a weak solution of (10.2), and
γ(t, s, x) = exp
	  t
s
c(τ, Xt,x(τ))dτ +

k≥1
 t
s
qkνk(τ, Xt,x(τ))←−−
dwk(τ)
−1
2
 t
s

k≥1
q2
k|νk(τ, Xt,x(τ))|2dτ

.
(10.4)
Proof. It is enough to establish (10.3) when t = T. Consider the equation
dU = (aijDiDjU +biDiU +cU +f)dt+

k≥1
(σikDiU +νkU +gk)qkdwk (10.5)
with initial condition U(0, x) = u0(x). Applying Theorem 2.1 in the normal
triple (H1
2,(r), L2,(r), H−1
2,(r)), we conclude that there is a unique solution

Wiener Chaos for Stochastic Equations
483
U ∈L2

W; L2((0, T); H1
2,(r))
 ?
L2

W; C((0, T); L2,(r))

of this equation. By Proposition 7.2, the process u = Q−1U is the corre-
sponding Wiener Chaos solution of (10.1). To establish representation (10.3),
consider the S-transform Uh of U. According to Theorem 8.1, the function Uh
is the unique w(H1
2,(r), H−1
2,(r)) solution of the equation
dUh = (aijDiDjUh + biDiUh + cUh + f)dt +

k≥1
(σikDiUh + νkUh + gk)qkhkdt
(10.6)
with initial condition Uh|t=0 = u0. We also define
Y (T, x) =
 T
0
f(s, XT,x(s))γ(T, s, x)ds
+

k≥1
 T
0
gk(s, XT,x(s))γ(T, s)qk
←−−
dwk(s) + u0(XT,x(0))γ(T, 0, x).
(10.7)
By direct computation,
E

E

E(h)Y (T, x)|FW
T

= E (E(h)Y (T, x)) = E′Y (T, x),
where E′ is the expectation with respect to the measure dP′
T = E(h)dPT and
PT is the restriction of P to FW
T .
To proceed, let us first assume that the input data u0, f, and gk are all
smooth functions with compact support. Then, applying the Feynmann–Kac
formula to the solution of equation (10.6) and using Girsanov’s theorem (see,
e.g., Theorems 3.5.1 and 5.7.6 in [15]), we conclude that Uh(T, x) = E′Y (T, x)
or
E

E(h)EY (t, x)|FW
T

= E (E (h) U(T, x)) .
By Remark 7.1, the last equality implies U (T, ·) = E

Y (T, ·)|FW
T

as elements
of L2

Ω; L2,(r)(Rd)

.
To remove the additional smoothness assumption on the input data, let
un
0, f n, and gn
k be sequences of smooth compactly supported functions such
that
lim
n→∞
	
∥u0 −un
0∥2
L2,(r)(Rd) +
 T
0
∥f −f n∥2
L2,(r)(Rd)(t)dt
+

k≥1
 T
0
q2
k∥gk −gn
k ∥2
L2,(r)(Rd)(t)dt

= 0.
(10.8)
Denote by U n and Y n the corresponding objects defined by (10.5) and (10.7)
respectively. By Theorem 9.1, we have

484
S. Lototsky and B. Rozovskii
lim
n→∞E∥U −U n∥2
L2,(r)(Rd)(T) = 0.
(10.9)
To complete the proof, it remains to show that
lim
n→∞E
E

Y (T, ·) −Y n(T, ·)
FW
T

2
L2,(r)(Rd) = 0.
(10.10)
To this end, introduce a new probability measure
dP
′′
T = exp
	
2

k≥1
 T
0
νk(s, XQ
T,x(s))qk
←−−
dwk(s)
−2
 T
0

k≥1
q2
k|νk(s, XQ
T,x(s))|2ds

dPT .
By Girsanov’s theorem, equation (10.2) can be rewritten as
XT,x,i (s) = xi +
 T
s

k≥1
σik (τ, XT,x (τ)) hk (τ) qkdτ
+
 t
s
(bi +

k≥1
q2
kσikνk) (τ, XT,x (τ)) dτ
+
 t
s

k≥1
qkσik (τ, XT,x (τ))
←−−
dw′′
k (τ) +
 t
s
˜σik (τ, XT,x (τ))
←−−
d ˜
w′′k (τ) ,
(10.11)
where w′′
k and
˜
w′′k are independent Wiener processes with respect to the
measure P′′
T . Denote by p(s, y|x) the corresponding distribution density of
XT,x(s) and write ℓ(x) = (1+|x|2)r. It then follows by the H¨older and Jensen
inequalities that
E
E
	 T
0
γ2(T, s, ·)(f −f n)(s, XT,·(s))ds
FW
T


2
L2,(r)(Rd)
≤K1

Rd
	 T
0
E

γ2(T, s, x)(f −f n)2(s, XT,x(s))

ds

ℓ(x)dx
≤K2

Rd
	 T
0
E′′(f −f n)2(s, XT,x(s))ds

ℓ(x)dx
= K2

Rd
 T
0

Rd(f(s, y) −f n(s, y))2p(s, y|x)dy ds ℓ(x)dx,
(10.12)
where the number K1 depends only on T, and the number K2 depends only
on T and sup(t,x) |c(t, x)| + 
k≥1 q2
k sup(t,x) |νk(t, x)|2. Assumptions B0–B2
imply that there exist positive numbers K3 and K4 such that

Wiener Chaos for Stochastic Equations
485
p(s, y|x) ≤
K3
(T −s)d/2 exp

−K4
|x −y|2
T −s

;
(10.13)
see, for example, [6]. As a result,

Rd p(s, y|x)ℓ(x)dx ≤K5ℓ(y),
and

Rd
 T
0

Rd(f(s, y) −f n(s, y))2p(s, y|x)dy ds ℓ(x)dx
≤K5
 T
0
∥f −f n∥2
L2,(r)(Rd)(s)ds →0, n →∞,
(10.14)
where the number K5 depends only on K3, K4, T, and r.
Calculations similar to (10.12)–(10.14) show that
E
E

γ2(T, 0, ·)(u0 −un
0)(XT,·(0))
W

2
L2,(r)(Rd)
+ E

E


 T
0

k≥1
(gk −gn
k )(s, XT,·(s))γ(t, s, ·)qk
←−−
dwk(s)
W



2
L2,(r)(Rd)
→0
(10.15)
as
n →∞. Then convergence (10.10) follows, which, together with (10.9),
implies that U (T, ·) = E

U Q(T, ·)|FW
T

as elements of L2

Ω; L2,(r)(Rd)

. It
remains to note that u = Q−1U. Theorem 10.1 is proved.
Given f ∈L2,(r), we say that f ≥0 if and only if

Rd f(x)ϕ(x)dx ≥0
for every non-negative ϕ ∈C∞
0 (Rd). Then Theorem 10.1 implies the following
result.
Corollary 10.1 In addition to Assumptions B0–B5, let u0 ≥0, f ≥0, and
gk = 0 for all k ≥1. Then u ≥0.
Proof. This follows from (10.3) and Proposition 7.3.
Example 10.1 (Krylov–Veretennikov formula)
Consider the equation
du = (aijDiDju + biDiu) dt +
d

k=1
σikDiudwk, u (0, x) = u0 (x) .
(10.16)

486
S. Lototsky and B. Rozovskii
Assume B0–B5 and suppose that aij(t, x) = 1
2σik(t, x)σjk(t, x). By Theorem
9.1, equation (10.16) has a unique Wiener chaos solution such that
E∥u∥2
L2(Rd)(t) ≤C∗∥u0∥2
L2(Rd)
and
u (t, x) =
∞

n=1

|α|=n
uα(t, x)ξα = u0 (x) +
∞

n=1
d

k1,...,kn=1
 t
0
 sn
0
. . .
 s2
0
Φt,snσjknDj · · · Φs2,s1σik1DiΦs1,0u0(x)dwk1(s1) · · · dwkn(sn),
(10.17)
where Φt,s is the semigroup generated by the operator A = aijDiDju+biDiu.
On the other hand, in this case, Theorem 10.1 yields
u(t, x) = E
	
u0(Xt,x(0))
FW
t

,
where W = (w1, ..., wd) and
Xt,x,i (s) = xi +
 t
s
bi (τ, Xt,x (τ)) dτ +
d

k=1
σik (τ, Xt,x (τ)) ←−−
dwk (τ) ,
s ∈(0, t), t ∈(0, T], t −fixed.
(10.18)
Thus, we have arrived at the Krylov–Veretennikov formula [20, Theorem 4]
E

u0 (Xt,x (0)) |FW
t

= u0 (x) +
∞

n=1
d

k1,...,kn=1
 t
0
 sn
0
. . .
 s2
0
Φt,snσjknDj · · · Φs2,s1σik1DiΦs1,0u0(x)dwk1(s1) · · · dwkn(sn).
(10.19)
11 Wiener Chaos and Nonlinear Filtering
In this section, we discuss some applications of the Wiener Chaos expansion
to numerical solution of the nonlinear filtering problem for diffusion processes;
the presentation is essentially based on [25].
Let (Ω, F, P) be a complete probability space with independent standard
Wiener processes W = W(t) and V = V (t) of dimensions d1 and r respec-
tively. Let X0 be a random variable independent of W and V . In the diffu-
sion filtering model, the unobserved d-dimensional state (or signal) process
X = X(t) and the r-dimensional observation process Y = Y (t) are defined by
the stochastic ordinary differential equations

Wiener Chaos for Stochastic Equations
487
dX(t) = b(X(t))dt + σ(X(t))dW(t) + ρ(X(t))dV (t),
dY (t) = h(X(t))dt + dV (t), 0 < t ≤T;
X(0) = X0,
Y (0) = 0,
(11.1)
where b(x) ∈Rd, σ(x) ∈Rd×d1, ρ(x) ∈Rd×r, h(x) ∈Rr.
Denote by Cn(Rd) the Banach space of bounded, n times continuously
differentiable functions on Rd with finite norm
∥f∥Cn(Rd) = sup
x∈Rd |f(x)| + max
1≤k≤n sup
x∈Rd |Dkf(x)|.
Assumption R1. The components of the functions σ and ρ are in C2(Rd),
the components of the functions b are in C1(R), the components of the func-
tion h are bounded measurable, and the random variable X0 has a density
u0.
Assumption R2. The matrix σσ∗is uniformly positive definite: there
exists ε > 0 such that
d

i,j=1
d1

k=1
σik(x)σjk(x)yiyj ≥ε|y|2, x, y ∈Rd.
Under Assumption R1 system (11.1) has a unique strong solution [15,
Theorems 5.2.5 and 5.2.9]. Extra smoothness of the coefficients in assumption
R1 insure the existence of a convenient representation of the optimal filter.
If f is a scalar measurable function on Rd with supt≤T E|f(X(t))|2 < ∞,
then the filtering problem for (11.1) is to find the best mean square estimate
ˆft of f(X(t)), t ≤T, given the observations Y (s), s ≤t.
Denote by FY
t the σ-algebra generated by Y (s), s ≤t. Then the properties
of the conditional expectation imply that the solution of the filtering problem
is
ˆft = E

f(X(t))|FY
t

.
To derive an alternative representation of ˆft, some additional constructions
will be necessary.
Define on (Ω, F) the probability measure d*P = Z−1
T dP where
Zt = exp
 t
0
h∗(X(s))dY (s) −1
2
 t
0
|h(X(s))|2ds

(here and below, if ζ ∈Rk, then ζ is a column vector, ζ∗= (ζ1, . . . , ζk), and
|ζ|2 = ζ∗ζ). If the function h is bounded, then the measures P and *P are
equivalent. The expectation with respect to the measure *P will be denoted
by *E.
The following properties of the measure *P are well known [14, 42]:

488
S. Lototsky and B. Rozovskii
P1. Under the measure *P, the distributions of the Wiener process W and
the random variable X0 are unchanged, the observation process Y is a
standard Wiener process, and, for t ≤T, the state process X satisfies:
dX(t) = b(X(t))dt + σ(X(t))dW(t) + ρ(X(t)) (dY (t) −h(X(t))dt) ,
X(0) = X0.
P2. Under the measure *P, the Wiener processes W and Y and the random
variable X0 are independent of one another.
P3. The optimal filter ˆft satisfies the relation
ˆft =
*E

f(X(t))Zt|FY
t

*E[Zt|FY
t ]
.
(11.2)
Because of property P2 of the measure *P the filtering problem will be
studied on the probability space (Ω, F, *P). In particular, we will consider
the stochastic basis *F = {Ω, F, {FY
t }0≤t≤T , *P} and the Wiener Chaos space
*L2(Y) of FY
T -measurable random variables η with *E|η|2 < ∞.
If the function h is bounded, then, by the Cauchy–Schwarz inequality,
E|η| ≤C(h, T)
H
*E|η|2, η ∈*L2(Y).
(11.3)
Next, consider the partial differential operators
Lg(x) = 1
2
d

i,j=1
((σ(x)σ∗(x))ij + (ρ(x)ρ∗(x))ij) ∂2g(x)
∂xi∂xj
+
d

i=1
bi(x)∂g(x)
∂xi
;
Mlg(x) = hl(x)g(x) +
d

i=1
ρil(x)∂g(x)
∂xi
, l = 1, . . . , r;
and their adjoints
L∗g(x) = 1
2
d

i,j=1
∂2
∂xi∂xj
((σ(x)σ∗(x))ijg(x) + (ρ(x)ρ∗(x))ijg(x))
−
d

i=1
∂
∂xi
(bi(x)g(x)) ;
M∗
l g(x) = hl(x)g(x) −
d

i=1
∂
∂xi
(ρil(x)g(x)) , l = 1, . . . , r.
Note that, under the assumptions R1 and R2, the operators L, L∗are
bounded from H1
2(Rd) to H−1
2 (Rd), operators M, M∗are bounded from
H1
2(Rd) to L2(Rd), and

Wiener Chaos for Stochastic Equations
489
2⟨L∗v, v⟩+
r

l=1
∥M∗
l v∥2
L2(Rd)+ε∥v∥2
H2
1(Rd) ≤C∥v∥2
L2(Rd), v ∈H1
2(Rd), (11.4)
where ⟨·, ·⟩is the duality between H1
2(Rd) and H−1
2 (Rd). The following result
is well known [42, Theorem 6.2.1].
Proposition 11.1 In addition to Assumptions R1 and R1 suppose that the
initial density u0 belongs to L2(Rd). Then there is a random field u = u(t, x),
t ∈[0, T], x ∈Rd, with the following properties:
1. u ∈*L2(Y; L2((0, T); H1
2(Rd))) ∩*L2(Y; C([0, T], L2(Rd))).
2. The function u(t, x) is a traditional solution of the stochastic partial
differential equation
du(t, x) = L∗u(t, x)dt +
r

l=1
M∗
l u(t, x)dYl(t), 0 < t ≤T, x ∈Rd;
u(0, x) = u0(x).
(11.5)
3. The equality
*E

f(X(t))Zt|FY
t

=

Rd f(x)u(t, x)dx
(11.6)
holds for all bounded measurable functions f.
The random field u = u(t, x) is called the unnormalized filtering density
(UFD) and the random variable ϕt[f] = *E

f(X(t))Zt|FY
t

, the unnormalized
optimal filter.
A number of authors studied the nonlinear filtering problem using the
multiple Itˆo integral version of the Wiener Chaos [2, 21, 39, 46, etc.]. In
what follows, we construct approximations of u and ϕt[f] using the Cameron–
Martin version.
By Theorem 8.3,
u(t, x) =

α∈J
uα(t, x)ξα,
(11.7)
where
ξα =
1
√
α!
(
i,k
Hαk
i (ξik), ξik =
 T
0
mi(t)dYk(t), k = 1, . . . , r;
(11.8)
as before, Hn(·) is the Hermite polynomial (3.3) and mi ∈m, an orthonormal
basis in L2((0, T)). The functions uα satisfy the corresponding propagator
∂
∂tuα(t, x) = L∗uα(t, x)
+

k,i
H
αk
i M∗
kuα−(i,k)(t, x)mi(t), t ≤T, x ∈Rd;
u(0, x) = u0(x)I(|α| = 0).
(11.9)

490
S. Lototsky and B. Rozovskii
Writing
fα(t) =

Rd f(x)uα(t, x)dx,
we also get a Wiener chaos expansion for the unnormalized optimal filter:
ϕt[f] =

α∈J
fα(t)ξα, t ∈[0, T].
(11.10)
For a positive integer N, define
uN(t, x) =

|α|≤N
uα(t, x)ξα.
(11.11)
Theorem 11.1. Under Assumptions R1 and R2, there exists a positive num-
ber ν, depending only on the functions h and ρ, such that
*E∥u −uN∥2
L2(Rd)(t) ≤
∥u0∥2
L2(Rd)
ν(1 + ν)N , t ∈[0, T].
(11.12)
If, in addition, ρ = 0, then there exists a real number C, depending only on
the functions b and σ, such that
*E∥u −uN∥2
L2(Rd)(t) ≤(4h∞t)N+1
(N + 1)! eCt∥u0∥2
L2(Rd), t ∈[0, T],
(11.13)
where h∞= maxk=1,...,r supx |hk(x)|.
For positive integers N, n, define a set of multi-indices
J n
N = {α = (αk
i , k = 1, . . . , r, i = 1, . . . , n) : |α| ≤N}.
and let
un
N(t, x) =

α∈J n
N
uα(t, x)ξα.
(11.14)
Unlike Theorem 11.1, to compute the approximation error in this case we
need to choose a special basis m — to do the error analysis for the Fourier
approximation in time. We also need extra regularity of the coefficients in the
state and observation equations — to have the semi-group generated by the
operator L∗continuous not only in L2(Rd) but also in H2
2(Rd). The resulting
error bound is presented below; the proof can be found in [25].
Theorem 11.2. Assume that
1. The basis m is the Fourier cosine basis
m1(t)= 1
√
T
; mk(t)=

2
T cos
π(k −1)t
T

, k > 1; t ≤T,
(11.15)

Wiener Chaos for Stochastic Equations
491
2. The components of the functions σ are in C4(Rd), the components of the
functions b are in C3(R), the components of the function h are in C2(Rd);
ρ = 0; u0 ∈H2
2(Rd).
Then there exist a positive number B1 and a real number B2, both depending
only on the functions b and σ such that
*E∥u−un
N∥2
L2(Rd)(T)≤B1eB2T
(4h∞T)N+1
(N + 1)!
eCt∥u0∥2
L2(Rd) + T 3
n ∥u0∥2
H2
2(Rd)

,
(11.16)
where h∞= maxk=1,...,r supx |hk(x)|.
12 Passive Scalar in a Gaussian Field
This section presents the results from [29] and [28] about the stochastic trans-
port equation.
The following viscous transport equation is used to describe the time evo-
lution of a scalar quantity θ in a given velocity field v:
˙θ(t, x) = ν∆θ(t, x) −v(t, x) · ∇θ(t, x) + f(t, x); x ∈Rd, d > 1.
(12.1)
The scalar θ is called passive because it does not affect the velocity field v.
We assume that v = v(t, x) ∈Rd is an isotropic Gaussian vector field with
zero mean and covariance
E(vi(t, x)vj(s, y)) = δ(t −s)Cij(x −y),
where C = (Cij(x), i, j = 1, . . . , d) is a matrix-valued function such that C(0)
is a scalar matrix; with no loss of generality we will assume that C(0) = I,
the identity matrix.
It is known from [22, Section 10.1] that, for an isotropic Gaussian vector
field, the Fourier transform ˆC = ˆC(z) of the function C = C(x) is
ˆC(y) =
A0
(1 + |y|2)(d+α)/2

ayy∗
|y|2 +
b
d −1

I −yyT
|y|2

,
(12.2)
where y∗is the row vector (y1, . . . , yd), y is the corresponding column vector,
|y|2 = y∗y; γ > 0, a ≥0, b ≥0, A0 > 0 are real numbers. Similar to [22], we
assume that 0 < γ < 2. This range of values of γ corresponds to a turbulent
velocity field v, also known as the generalized Kraichnan model [8]; the original
Kraichnan model [18] corresponds to a = 0. For small x, the asymptotics of
Cij(x) is (δij −cij|x|γ) [22, Section 10.2].
By direct computation (cf. [1]), the vector field v = (v1, . . . , vd) can be
written as
vi(t, x) = σi
k(x) ˙wk(t),
(12.3)

492
S. Lototsky and B. Rozovskii
where {σk, k ≥1} is an orthonormal basis in the space HC, the reproducing
kernel Hilbert space corresponding to the kernel function C. It is known from
[22] that HC is all or a part of the Sobolev space H(d+γ)/2(Rd; Rd).
If a > 0 and b > 0, then the matrix ˆC is invertible and
HC =

f ∈Rd :

Rd
ˆf ∗(y) ˆC−1(y) ˆf(y)dy < ∞

= H(d+γ)/2(Rd; Rd),
because ∥ˆC(y)∥∼(1 + |y|2)−(d+γ)/2.
If a > 0 and b = 0, then
HC =

f ∈Rd :

Rd | ˆf(y)|2(1 + |y|2)(d+γ)/2dy < ∞; yy∗ˆf(y) = |y|2 ˆf(y)

,
the subset of gradient fields in H(d+γ)/2(Rd; Rd), that is, the vector fields f
for which ˆf(y) = y ˆF(y) for some scalar F ∈H(d+γ+2)/2(Rd).
If a = 0 and b > 0, then
HC =

f ∈Rd :

Rd | ˆf(y)|2(1 + |y|2)(d+γ)/2dy < ∞; y∗ˆf(y) = 0

,
the subset of divergence-free fields in H(d+γ)/2(Rd; Rd).
By the embedding theorems, each σi
k is a bounded continuous function on
Rd; in fact, every σi
k is H¨older continuous of order γ/2. In addition, being an
element of the corresponding space HC, each σk is a gradient field if b = 0
and is divergence-free if a = 0.
Equation (12.1) becomes
dθ(t, x) = (ν∆θ(t, x) + f(t, x))dt −

k
σk(x) · ∇θ(t, x)dwk(t).
(12.4)
We summarize the above constructions in the following assumptions:
S1 There is a fixed stochastic basis F = (Ω, F, {Ft}t≥0, P) with the usual as-
sumptions and (wk(t), k ≥1, t ≥0) is a collection of independent standard
Wiener processes on F.
S2 For each k, the vector field σk is an element of the Sobolev space
H(d+γ)/2
2
(Rd; Rd), 0 < γ < 2, d ≥2.
S3 For all x, y in Rd, 
k σi
k(x)σj
k(y) = Cij(x−y) such that the matrix-valued
function C = C(x) satisfies (12.2) and C(0) = I.
S4 The input data θ0, f are deterministic and satisfy
θ0 ∈L2(Rd), f ∈L2((0, T); H−1
2 (Rd));
ν > 0 is a real number.

Wiener Chaos for Stochastic Equations
493
Theorem 12.1. Let Q be a sequence with qk = q <
√
2ν, k ≥1.
Under assumptions S1–S4, there exits a unique w(H1
2(Rd), H−1
2 (Rd))
Wiener Chaos solution of (12.4). This solution is an FW
t -adapted process
and satisfies the inequality
∥θ∥2
L2,Q(W;L2((0,T );H1
2(Rd))) + ∥θ∥2
L2,Q(W;C((0,T );L2(Rd)))
≤C(ν, q, T)

∥θ0∥2
L2(Rd) + ∥f∥2
L2((0,T );H−1
2
(Rd))

.
Theorem 12.1 provides new information about the solution of equation
(12.1) for all values of ν > 0. Indeed, if
√
2ν > 1, then q > 1 is an admissible
choice of the weights, and, by Proposition 7.2(1), the solution θ has Malliavin
derivatives of every order. If
√
2ν ≤1, then equation (12.4) does not have a
square-integrable solution.
Note that if the weight is chosen such that q =
√
2ν, then equa-
tion (12.1) can still be analyzed using Theorem 9.1 in the normal triple
(H1
2(Rd), L2(Rd), H−1
2 (Rd)).
If ν = 0, equation (12.4) must be interpreted in the sense of Stratonovich:
du(t, x) = f(t, x)dt −σk(x) · ∇θ(t, x) ◦dwk(t).
(12.5)
To simplify the presentation, we assume that f = 0. If (12.2) holds with a = 0,
then each σk is divergence free and (12.5) has an equivalent Itˆo form
dθ(t, x) = 1
2∆θ(t, x)dt −σi
k(x)Diθ(t, x)dwk(t).
(12.6)
Equation (12.6) is a model of non-viscous turbulent transport [5]. The prop-
agator for (12.6) is
∂
∂tθα(t, x) = 1
2∆θα(t, x) −

i,k
H
αk
i σj
kDjθα−(i,k)(t, x)mi(t), t ≤T,
(12.7)
with initial condition θα(0, x) = θ0(x)I(|α| = 0).
The following result about solvability of (12.6) is proved in [29] and, in a
slightly weaker form, in [28].
Theorem 12.2. In addition to S1–S4, assume that each σk is divergence
free. Then there exits a unique w(H1
2(Rd), H−1
2 (Rd)) Wiener Chaos solution
θ = θ(t, x) of (12.6). This solution has the following properties:
(A) For every ϕ ∈C∞
0 (Rd) and all t ∈[0, T], the equality
(θ, ϕ)(t) = (θ0, ϕ) + 1
2
 t
0
(θ, ∆ϕ)(s)ds +
 t
0
(θ, σi
kDiϕ)dwk(s)
(12.8)
holds in L2(FW
t ), where (·, ·) is the inner product in L2(Rd).
(B) If X = Xt,x is a weak solution of the equation

494
S. Lototsky and B. Rozovskii
Xt,x = x +
 t
0
σk (Xs,x) dwk (s) ,
(12.9)
then, for each t ∈[0, T],
θ (t, x) = E

θ0 (Xt,x) |FW
t

.
(12.10)
(C) For 1 ≤p < ∞and r ∈R, define Lp,(r)(Rd) as the Banach space of
measurable functions with the norm
∥f∥p
Lp,(r)(Rd) =

Rd |f(x)|p(1 + |x|2)pr/2dx < ∞.
Then there exits a number K depending only on p, r such that, for each t > 0,
E∥θ∥p
Lp,(r)(Rd)(t) ≤eKt∥θ0∥p
Lp,(r)(Rd).
(12.11)
In particular, if r = 0, then K = 0.
It follows that, for all s, t and almost all x, y,
Eθ (t, x) = θα (t, x) I|α|=0,
Eθ (t, x) θ (s, y) =

α∈J
θα (t, x) θα (s, y) .
If the initial condition θ0 belongs to L2(Rd) ∩Lp(Rd) for p ≥3, then,
by (12.11), higher-order moments of θ exist. To obtain the expressions of the
higher-order moments in terms of the coefficients θα, we need some auxiliary
constructions.
For α, β ∈J , define α + β as the multi-index with components αk
i + βk
i .
Similarly, we define the multi-indices |α −β| and α ∧β = min(α, β). We write
β ≤α if and only if βk
i ≤αk
i for all i, k ≥1. If β ≤α, we define
α
β

:=
(
i,k
αk
i !
βk
i !(αk
i −βk
i )!.
Definition 12.1 We say that a triple of multi-indices (α, β, γ) is complete
and write (α, β, γ) ∈△if all the entries of the multi-index α + β + γ are even
numbers and |α −β| ≤γ ≤α + β. For fixed α, β ∈J , we write
△(α) := {γ, µ ∈J : (α, γ, µ) ∈△}
and
△(α, β) := {γ ∈J : (α, β, γ) ∈△}.

Wiener Chaos for Stochastic Equations
495
For (α, β, γ) ∈△, we define
Ψ (α, β, γ) :=

α!β!γ!
α −β + γ
2

!
β −α + γ
2

!
α + β −γ
2

!
−1
.
(12.12)
Note that the triple (α, β, γ) is complete if and only if any permutation of
the triple (α, β, γ) is complete. Similarly, the value of Ψ (α, β, γ) is invariant
under permutation of the arguments.
We also define
C (γ, β, µ) :=
γ + β −2µ
γ −µ
γ
µ
β
µ
1/2
, µ ≤γ ∧β.
(12.13)
It is readily checked that if f is a function on J , then for γ, β ∈J ,

µ≤γ∧β
C (γ, β, p) f (γ + β −2µ) =

µ∈(γ,β)
f (µ) Φ (γ, β, µ)
(12.14)
The next theorem presents the formulas for the third and fourth moments
of the solution of equation (12.6) in terms of the coefficients θα.
Theorem 12.3. In addition to S1–S4, assume that each σk is divergence-free
and the initial condition θ0 belongs to L2(Rd) ∩L4(Rd). Then
Eθ(t, x)θ (t′, x′) θ(s, y) =

(α,β,γ)∈△
Ψ (α, β, γ) θα(t, x)θβ(t′, x′)θγ (s, y)
(12.15)
and
Eθ(t, x)θ(t′, x′)θ (s, y) θ (s′, y′)
(12.16)
=

ρ∈△(α,β)∩△(γ,κ)
Ψ (α, β, ρ) Ψ (ρ, γ, κ) θα (t, x) θβ(t′, x′)θγ (s, y) θκ (s′, y′) .
Proof. It is known, [30], that
ξγξβ =

µ≤γ∧β
C (γ, β, µ) ξγ+β−2µ.
(12.17)
Let us consider the triple product ξαξβξγ. By (12.17),
Eξαξβξγ = E

µ∈△(α,β)
ξγξµΨ (α, β, µ) =

Ψ (α, β, γ) ,
(α, β, γ) ∈△;
0,
otherwise.
(12.18)
Equality (12.15) now follows.
To compute the fourth moment, note that

496
S. Lototsky and B. Rozovskii
ξαξβξγ =

µ≤α∧β
C (α, β, µ) ξα+β−2µξγ
=

µ≤α∧β
C (α, β, µ)

ρ≤(α+β−2µ)∧γ
C (α + β −2µ, γ, ρ) ξα+β+γ−2µ−2ρ.
(12.19)
Repeated applications of (12.14) yield
ξαξβξγ =

µ≤α∧β
C (α, β, µ)

ρ∈△(α+β−2µ,γ)
ξρΨ (α + β −2µ, γ, ρ)
=

µ∈△(α,β)

ρ∈△(µ,γ)
Ψ (α, β, µ) Ψ (µ, γ, ρ) ξρ
Thus,
Eξαξβξγξκ =

µ∈△(α,β)

ρ∈△(µ,γ)
Ψ (α, β, µ) Ψ (µ, γ, ρ) I{µ=κ}
=

ρ∈△(α,β)∩△(γ,κ)
Ψ (α, β, ρ) Ψ (ρ, γ, κ) .
Equality (12.16) now follows.
In the same way, one can get formulas for fifth- and higher-order moments.
Remark 12.1 Expressions (12.15) and (12.16) do not depend on the structure
of equation (12.6) and can be used to compute the third and fourth moments
of any random field with a known Cameron–Martin expansion. The interested
reader should keep in mind that the formulas for the moments of orders higher
then two should be interpreted with care. In fact, they represent the pseudo-
moments (for detail see [35]).
We now return to the analysis of the passive scalar equation (12.4). By
reducing the smoothness assumptions on σk, it is possible to consider velocity
fields v that are more turbulent than in the Kraichnan model, for example,
vi(t, x) =

k≥0
σi
k(x) ˙wk(t),
(12.20)
where {σk, k ≥1} is an orthonormal basis in L2(Rd; Rd). With v as in (12.20),
the passive scalar equation (12.4) becomes
˙θ(t, x) = ν∆θ(t, x) + f(t, x) −∇θ(t, x) · ˙W(t, x),
(12.21)
where ˙W = ˙W(t, x) is a d-dimensional space-time white noise and the Itˆo sto-
chastic differential is used. Previously, such equations have been studied using
white noise approach in the space of Hida distributions [4, 40]. A summary of
the related results can be found in [12, Section 4.3].

Wiener Chaos for Stochastic Equations
497
The Q-weighted Wiener chaos spaces allow us to state a result that is fully
analogous to Theorem 12.1. The proof is derived from Theorem 9.1; see [29]
for details.
Theorem 12.4. Suppose that ν > 0 is a real number, each |σi
k(x)| is a
bounded measurable function, and the input data are deterministic and satisfy
u0 ∈L2(Rd), f ∈L2

(0, T); H−1
2 (Rd)

.
Fix ε > 0 and let Q = {qk, k ≥1} be a sequence so that, for all x, y ∈Rd,
2ν|y|2 −

k≥1
q2
kσi
k(x)σj
k(x)yiyj ≥ε|y|2.
Then, for every T > 0, there exits a unique w(H1
2(Rd), H−1
2 (Rd)) Wiener
Chaos solution θ of the equation
dθ(t, x) = (ν∆θ(t, x) + f(t, x))dt −σk(x) · ∇θ(t, x)dwk(t),
(12.22)
The solution is an Ft-adapted process and satisfies the ineq21uality
∥θ∥2
L2,Q(W;L2((0,T );H1
2(Rd))) + ∥θ∥2
L2,Q(W;C((0,T );L2(Rd)))
≤C(ν, q, T)

∥θ0∥2
L2(Rd) + ∥f∥2
L2((0,T );H−1
2
(Rd))

.
If maxi supx |σi
k(x)| ≤Ck, k ≥1, then a possible choice of Q is
qk = (δν)1/2/(d2kCk), 0 < δ < 2.
If σi
k(x)σj
k(x) ≤Cσ < ∞, i, j = 1, . . . , d, x ∈Rd, then a possible choice of
Q is
qk = ε (2ν/(Cσd))1/2 , 0 < ε < 1.
13 Stochastic Navier–Stokes Equation
In this section, we review the main facts about the stochastic Navier–Stokes
equation and indicate how the Wiener Chaos approach can be used in the
study of non-linear equations. Most of the results of this section come from
the two papers [35] and [31].
A priori, it is not clear in what sense the motion described by Kraichnan’s
velocity (see Section 12) might fit into the paradigm of Newtonian mechanics.
Accordingly, relating the Kraichnan velocity field v to classic fluid mechanics
naturally leads to the question whether we can compensate v (t, x) by a field
u (t, x) that is more regular with respect to the time variable, so that there is
a balance of momentum for the resulting field U (t, x) = u (t, x) + v (t, x) or,
equivalently, that the motion of a fluid particle in the velocity field U (t, x)
satisfies the Second Law of Newton.

498
S. Lototsky and B. Rozovskii
A positive answer to this question is given in [35], where it is shown that
the equation for the smooth component u = (u1, . . . , ud) of the velocity is
given by

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

dui = [ν∆ui −ujDjui −DiP + fi]dt
+

gi
k −Di ˜Pk −Djσj
kui
dwk,
i = 1, . . . , d,
0 < t ≤T;
div u = 0, u(0, x) = u0(x).
(13.1)
where wk, k ≥1 are independent standard Wiener processes on a sto-
chastic basis F, the functions σj
k are given by (12.3), the known functions
f = (f 1, . . . , f d), gk = (gi
k), i = i, . . . , d, k ≥1, are, respectively, the drift and
the diffusion components of the free force, and the unknown functions P, ˜Pk
are the drift and diffusion components of the pressure.
Remark 13.1 It is useful to study equation (13.1) for more general coefficients
σj
k. So, in the future, σj
k are not necessarily the same as in Section 12.
We make the following assumptions:
NS1
The functions σi
k = σi
k(t, x) are deterministic and measurable,

k≥1
	 d

i=1
|σi
k(t, x)|2 + |Diσi
k(t, x)|2

≤K,
and there exists ε > 0 such that, for all y ∈Rd,
ν|y|2 −1
2σi
k(t, x)σj
k(t, x)yiyj ≥ε|y|2,
t ∈[0, T], x ∈Rd.
NS2
The functions f i, gi
k are non-random and
d

i=1

∥f i∥2
L2((0,T );H−1
2
(Rd)) +

k≥1
∥gi
k∥2
L2((0,T );L2(Rd))

< ∞.
Remark 13.2 In NS1, the derivatives Diσi
k are understood as Schwartz dis-
tributions, but it is assumed that div σ := d
i=1 ∂iσi is a bounded L2-valued
function. Obviously, the latter assumption holds in the important case when
d
i=1 ∂iσi = 0.
Our next step is to use the divergence-free property of u to eliminate the
pressure P and ˜P from equation (13.1). For that, we need the decomposition
of L2(Rd; Rd) into potential and solenoidal components.
Write S(L2(Rd; Rd)) = {V ∈L2(Rd; Rd) : div V = 0}. It is known (see
e.g. [16]) that

Wiener Chaos for Stochastic Equations
499
L2(Rd; Rd) = G(L2(Rd; Rd)) ⊕S(L2(Rd; Rd)),
where G(L2(Rd; Rd)) is a Hilbert subspace orthogonal to S(L2(Rd; Rd)).
The functions G(V) and S(V) can be defined for V from any Sobolev
space Hγ
2 (Rd; Rd) and are usually referred to as the potential and the
divergence-free or solenoidal projections, respectively, of the vector field V.
Now let u be a solution of equation (13.1). Since div u = 0, we have
Di(ν∆ui −ujDjui −DiP + f i) = 0; Di(σj
kDjujui + gi
k −Di ˜Pk) = 0, k ≥1.
As a result,
DiP = G(ν∆ui −ujDjui +f i); Di ˜Pk = G(σj
kDjui +gi
k), i = 1, . . . , d, k ≥1.
So, instead of equation (13.1), we can and will consider its equivalent form for
the unknown vector u = (u1, . . . , ud):
du = S(ν∆u −ujDju + f)dt + S(σj
kDju + gk)dwk, 0 < t ≤T,
(13.2)
with initial condition u|t=0 = u0.
Definition 13.1 An Ft-adapted random process u ∈L2(Ω×[0, T]; H1
2(Rd; Rd))
is called a solution of equation (13.2) if:
1. With probability one, the process u is weakly continuous in L2(Rd; Rd).
2. For every ϕ ∈C∞
0 (Rd, Rd) with div ϕ = 0 there exists a measurable set
Ω′ ⊂Ωsuch that, for all t ∈[0, T], the equality
(ui, ϕi)(t) = (ui
0, ϕi) +
 t
0

(νDjui, Djϕi)(s) + ⟨f i, ϕi⟩(s)

ds
 t
0

σj
kDjui + gi, ϕi)dwk(s)
(13.3)
holds on Ω′. In (13.3), (·, ·) is the inner product in L2(Rd) and ⟨·, ·, ⟩is
the duality between H1
2(Rd) and H−1
2 (Rd).
The following existence and uniqueness result is proved in [31].
Theorem 13.1. In addition to NS1 and NS2, assume that the initial con-
dition u0 is non-random and belongs to L2(Rd; Rd). Then there exist a sto-
chastic basis F = (Ω, F, {Ft}t≥0, P) with the usual assumptions, a collection
{wk, k ≥1} of independent standard Wiener processes on F, and a process u
such that u is a solution of (13.2) and
E
	
sup
s≤T
∥u(s)∥2
L2(Rd;Rd) +
 T
0
∥∇u(s)∥2
L2(Rd;Rd) ds

< ∞.
If, in addition, d = 2, then the solution of (13.2) exists on any prescribed
stochastic basis, is strongly continuous in t, is FW
t -adapted, and is unique,
both path-wise and in distribution.

500
S. Lototsky and B. Rozovskii
When d ≥3, the existence of a strong solution as well as uniqueness (strong
or weak) for equation (13.2) are important open problems.
By the Cameron–Martin theorem,
u(t, x) =

α∈J
uα(t, x)ξα.
If the solution of (13.2) is FW
t -adapted, then, using the Itˆo formula together
with relation (5.5) for the time evolution of E(ξα|FW
t ) and relation (12.17)
for the product of two elements of the Cameron–Martin basis, we can derive
the propagator system for coefficients uα [31, Theorem 3.2]:
Theorem 13.2. In addition to NS1 and NS2, assume that u0 ∈L2(Rd; Rd)
and equation (13.2) has an FW
t -adapted solution u such that
sup
t≤T
E∥u∥2
L2(Rd;Rd)(t) < ∞.
(13.4)
Then
u (t, x) =

α∈J
uα (t, x) ξα,
(13.5)
and the Hermite–Fourier coefficients uα(t, x) are L2(Rd; Rd)-valued weakly
continuous functions such that
sup
t≤T

α∈J
∥uα∥2
L2(Rd;Rd)(t) +
 T
0

α∈J
∥∇uα∥2
L2(Rd;Rd×d)(t) dt < ∞.
(13.6)
The functions uα (t, x) , α ∈J , satisfy the (nonlinear) propagator
∂
∂tuα = S

∆uα −

γ,β∈∆(α)
Ψ (α, β, γ) (uγ, ∇uβ) + I{|α|=0}f
+

j,k
H
αk
j

σk, ∇

uα−(j,k) + I{|α|=1}gk
mj (t)

, 0 < t ≤T;
uα|t=0 = u0I{|α|=0};
(13.7)
recall that the numbers Ψ(α, β, γ) are defined in (12.12).
One of the questions in the theory of the Navier–Stokes equation is com-
putation of the mean value ¯u = Eu of the solution. The traditional approach
relies on the Reynolds equation for the mean
∂t¯u −ν∆¯u + ( u, ∇) u = 0,
(13.8)
which is not really an equation with respect to ¯u. Decoupling (13.8) has been
an area of active research: Reynolds approximations, coupled equations for the

Wiener Chaos for Stochastic Equations
501
moments, Gaussian closures, and so on (see, e.g., [36], [45] and the references
therein)
Another way to compute ¯u (t, x) is to find the distribution of v (t, x) us-
ing the infinite-dimensional Kolmogorov equation associated with (13.2). The
complexity of this Kolmogorov equation is prohibitive for any realistic appli-
cation, at least for now.
The propagator provides a third way: expressing the mean and other sta-
tistical moments of u in terms of uα. Indeed, by Cameron–Martin Theorem,
Eu(t, x) = u0(t, x),
Eui(t, x)u
j (s, y) =

α∈J
ui
α(t, x)uj
α(s, y).
If exist, the third- and fourth-order moments can be computed using (12.15)
and (12.16).
The next theorem, proved in [31], shows that the existence of a solution
of the propagator (13.7) is not only necessary but, to some extent, sufficient
for the global existence of a probabilistically strong solution of the stochastic
Navier–Stokes equation (13.2).
Theorem 13.3. Let NS1 and NS2 hold and u0 ∈L2(Rd; Rd). Assume that
the propagator (13.7) has a solution {uα (t, x) , α ∈J } on the interval (0, T]
such that, for every α, the process uα is weakly continuous in L2(Rd; Rd) and
the inequality
sup
t≤T

α∈J
∥uα∥2
L2(Rd;Rd)(t) +
 T
0

α∈J
∥∇uα∥2
L2(Rd;Rd×d)(t) dt < ∞
(13.9)
holds. If the process
¯U (t, x) :=

α∈J
uα (t, x) ξα
(13.10)
is FW
t -adapted, then it is a solution of (13.2).
The process ¯U satisfies
E
	
sup
s≤T
∥¯U(s)∥2
L2(Rd;Rd) +
 T
0
∥∇¯U(s)∥2
L2(Rd;Rd×d) ds

< ∞
and, for every v ∈L2(Rd; Rd), E
 ¯U, v

is a continuous function of t.
Since ¯U is constructed on a prescribed stochastic basis and over a pre-
scribed time interval [0, T], this solution of (13.2) is strong in the probabilistic
sense and is global in time. Being true in any space dimension d, Theorem 13.3
suggests another possible way to study equation (13.2) when d ≥3. Unlike the
propagator for the linear equation, the system (13.7) is not lower-triangular
and not solvable by induction, so the analysis of (13.7) is an open problem.

502
S. Lototsky and B. Rozovskii
14 First-Order Itˆo Equations
The objective of this section is to study the equation
du(t, x) = ux(t, x)dw(t), t > 0, x ∈R,
(14.1)
and its analog for x ∈Rd.
Equation (14.1) was first encountered in Example 6.2; see also [9]. With a
non-random initial condition u(0, x) = ϕ(x), direct computations show that,
if exists, the Fourier transform ˆu = ˆu(t, y) of the solution must satisfy
dˆu(t, y) =
√
−1yˆu(t, y)dw(t), or ˆu(t, y) = ˆϕ(y)e
√−1yw(t)+ 1
2 y2t.
(14.2)
The last equality shows that the properties of the solution essentially depend
on the initial condition, and, in general, the solution is not in L2(W).
The S-transformed equation, vt = h(t)vx, has a unique solution
v(t, x) = ϕ

x +
 t
0
h(s)ds

, h(t) =
N

i=1
himi(t).
The results of Section 3 imply that a white noise solution of the equation can
exist only if ϕ is a real analytic function. On the other hand, if ϕ is infinitely
differentiable, then, by Theorem 8.2, the Wiener Chaos solution exists and
can be recovered from v.
Theorem 14.1. Assume that the initial condition ϕ belongs to the Schwarz
space S = S(R) of tempered distributions. Then there exists a generalized
random process u = u(t, x), t ≥0, x ∈R, such that, for every γ ∈R and
T > 0, the process u is the unique w(Hγ
2 (R), Hγ−1
2
(R)) Wiener Chaos solution
of equation (14.1).
Proof. The propagator for (14.1) is
uα(t, x) = ϕ(x)I(|α| = 0) +
 t
0

i
√αi(uα−(i)(s, x))xmi(s)ds.
(14.3)
Even though Theorem 6.1 is not applicable, the system can be solved by
induction if ϕ is sufficiently smooth. Denote by Cϕ(k), k ≥0, the square of
the L2(R)-norm of the kth derivative of ϕ:
Cϕ(k) =
 +∞
−∞
|ϕ(k)(x)|2dx.
(14.4)
By Corollary 6.1, for every k ≥0 and n ≥0,

|α|=k
∥(u(n)
α )x∥2
L2(R)(t) = tkCϕ(n + k)
k!
.
(14.5)
The statement of the theorem now follows.

Wiener Chaos for Stochastic Equations
503
Remark 14.1 Once interpreted in a suitable sense, the Wiener Chaos solution
of (14.1) is FW
t -adapted and does not depend on the choice of the Cameron–
Martin basis in L2(W). Indeed, choose the weight sequence so that
r2
α =
1
1 + Cϕ(|α|).
By (14.5), we have u ∈RL2(W; L2(R)).
Next, define
ψN(x) = 1
π
sin(Nx)
x
.
Direct computations show that the Fourier transform of ψN is supported in
[−N, N] and

R ψN(x)dx = 1. Consider equation (14.1) with initial condition
ϕN(x) =

R
ϕ(x −y)ψN(y)dy.
By (14.2), this equation has a unique solution uN such that uN(t, ·) is in
L2(W; Hγ
2 (R)) for every t ≥0, γ ∈R. Relation (14.5) and the definition of
uN imply that
lim
N→∞

|α|=k
∥uα −uN,α∥2
L2(R)(t) = 0, t ≥0, k ≥0,
so that, by the Lebesgue dominated convergence theorem,
lim
N→∞∥u −uN∥2
RL2(W;L2(R))(t) = 0, t ≥0.
In other words, the solution of the propagator (14.3) corresponding to any
basis m in L2((0, T)) is a limit in RL2(W; L2(R)) of the sequence {uN, N ≥1}
of FW
t -adapted processes.
The properties of the Wiener Chaos solution of (14.1) depend on the
growth rate of the numbers Cϕ(n). In particular,
•
If Cϕ(n) ≤Cn(n!)γ, C > 0, 0 ≤γ < 1, then
u ∈L2 (W; L2((0, T); Hn
2 (R))) for all T > 0 and every n ≥0.
•
If Cϕ(n) ≤Cnn!, C > 0, then
–
for every n ≥0, there is a T > 0 such that u ∈L2 (W; L2((0, T); Hn
2 (R))).
In other words, the square-integrable solution exists only for sufficiently
small T.
–
for every n ≥0 and every T > 0, there exists a number δ ∈(0, 1) such
that u ∈L2,Q (W; L2((0, T); Hn
2 (R))) with Q = (δ, δ, δ, . . .).
•
If the numbers Cϕ(n) grow as Cn(n!)1+ρ, ρ ≥0, then, for every T > 0,
there exists a number γ > 0 such that
u ∈(S)−ρ,−γ (L2(W); L2((0, T); Hn
2 (R))). If ρ > 0, then this solution does
not belong to any L2,Q (W; L2((0, T); Hn
2 (R))). If ρ > 1, then this solution
does not have an S-transform.

504
S. Lototsky and B. Rozovskii
•
If the numbers Cϕ(n) grow faster than Cn(n!)b for any b, C > 0, then the
Wiener Chaos solution of (14.1) does not belong to any
(S)−ρ,−γ (L2((0, T); Hn
2 (R))), ρ, γ > 0, or L2,Q (W; L2((0, T); Hn
2 (R))).
To construct a function ϕ with the required rate of growth of Cϕ(n),
consider
ϕ(x) =
 ∞
0
cos(xy)e−g(y)dy,
where g is a suitable positive, unbounded, even function. Note that, up to a
multiplicative constant, the Fourier transform of ϕ is e−g(y), and so Cϕ(n)
grows with n as
 ∞
0
|y|2ne−2g(y)dy.
A more general first-order equation can be considered:
du(t, x) = σik(t, x)Diu(t, x)dwk(t), t > 0, x ∈Rd.
(14.6)
Theorem 14.2. Assume that in equation (14.6) the initial condition u(0, x)
belongs to S(Rd) and each σik is infinitely differentiable with respect to x such
that sup(t,x) |Dnσik(t, x)| ≤Cik(n), n ≥0. Then there exists a generalized
random process u = u(t, x), t ≥0, x ∈Rd, such that, for every γ ∈R
and T > 0, the process u is the unique w(Hγ
2 (Rd), Hγ−1
2
(Rd)) Wiener Chaos
solution of equation (14.1).
Proof. The arguments are identical to the proof of Theorem 14.1.
Note that the S-transformed equation (14.6) is vt = hkσikDiv and has
a unique solution if each σik is a Lipschitz continuous function of x. Still,
without additional smoothness, it is impossible to relate this solution to any
generalized random process.
References
1. Baxendale, P., Harris, T.E.: Isotropic stochastic flows. Annals of Probabability
14(4), 1155–1179 (1986)
2. Budhiraja, A., Kallianpur, G: Approximations to the solution of the Zakai equa-
tions using multiple Wiener and Stratonovich integral expansions. Stochastics
and Stochastics Reports 56(3–4), 271–315 (1996)
3. Cameron, R.H., Martin, W.T.: The orthogonal development of nonlinear func-
tionals in a series of Fourier–Hermite functions. Annals of Mathematics 48(2),
385–392 (1947)
4. Deck, T., Potthoff, J.: On a class of stochastic partial differential equations
related to turbulent transport. Probability Theory and Related Fields 111, 101–
122 (1998)
5. E, W., Vanden Eijden, E.: Generalized flows, intrinsic stochasticity, and turbu-
lent transport. Proc. Nat. Acad. Sci. 97(15), 8200–8205 (2000)
6. Eidelman, S.D.: Parabolic systems, Groningen, Wolters-Noordhoff1969
7. Freidlin, M.I.: Functional Integration and Partial Differential Equations. Prince-
ton University Press 1985.

Wiener Chaos for Stochastic Equations
505
8. Gaw¸edzki, K., Vergassola, M.: Phase transition in the passive scalar advection.
Physica D 138, 63–90 (2000)
9. Gikhman, I.I., Mestechkina, T.M.: The Cauchy problem for stochastic first-order
partial differential equations. Theory of Random Processes 11, 25–28 (1983)
10. Hida, T., Kuo, H-H., Potthoff, J., Sreit, L.: White Noise. Kluwer 1993
11. Hille, E., Phillips, R.S.: Functional Analysis and Semigroups. Amer. Math. Soc.
Colloq. Publ., Vol. XXXI 1957
12. Holden, H., Øksendal, B., Ubøe, J., Zhang, T.: Stochastic Partial Differential
Equations. Birkh¨auser 1996
13. Ito, K.: Multiple Wiener integral. J. Math. Soc. Japan 3, 157–169 (1951)
14. Kallianpur, G.: Stochastic Filtering Theory. Springer 1980
15. Karatzas, I., Shreve, S.: Brownian Motion and Stochastic Calculus, 2nd Ed.
Springer 1991
16. Kato, T., Ponce, G.: On nonstationary flows of viscous and ideal fluids in Lp
s(R2).
Duke Mathematical Journal 55, 487–489 (1987)
17. Kondratiev, Yu.G., Leukert, P., Potthoff, J., Streit, L., Westerkamp, W.: Gen-
eralized functionals in Gaussian spaces: the characterization theorem revisited.
Journal of Functional Analysis 141(2), 301–318 (1996)
18. Kraichnan, R.H.: Small-scale structure of a scalar field convected by turbulence.
Phys. Fluids 11, 945–963 (1968)
19. Krylov, N.V.: An analytic approach to SPDEs. In: Stochastic Partial Differential
Equations. Six Perspectives. Eds. B. L. Rozovskii, R. Carmona, Mathematical
Surveys and Monographs, AMS 185–242 (1999)
20. Krylov, N.V., Veretennikov, A.J.: On explicit formula for solutions of stochastic
equations. Mathematical USSR Sbornik 29(2), 239–256 (1976)
21. Kunita, H.: Cauchy problem for stochastic partial differential equations arising
in nonlinear filtering theory. System and Control Letters 1(1), 37–41 (1981)
22. LeJan, Y., Raimond, O.: Integration of Brownian vector fields. Annals of Prob-
ability 30(2), 826–873 (2002)
23. Liptser, R.S., Shiryayev, A.N.: Theory of Martingales. Kluwer 1989
24. Liptser, R.S., Shiryaev, A.N.: Statistics of Random Processes. 2nd Ed. Springer
2001
25. Lototsky, S.V., Mikulevicius, R., Rozovskii, B.L.: Nonlinear filtering revisited: a
spectral approach. SIAM Journal on Control and Optimization 35(2) 435–461
(1997)
26. Lototsky, S.V., Rozovskii, B.L.: Recursive multiple Wiener integral expansion
for nonlinear filtering of diffusion processes. In: Stochastic Processes and Func-
tional Analysis. Eds. J.A. Goldstein, N.E. Gretsky, and J.J. Uhl, Marsel Dekker
199–208 (1997)
27. Lototsky, S.V., Rozovskii, B.L.: Recursive nonlinear filter for a continuous - dis-
crete time model: separation of parameters and observations. IEEE Transactions
on Automatic Control 43(8), 1154–1158 (1998)
28. Lototsky, S.V., Rozovskii, B.L.: Passive scalar equation in a turbulent incom-
pressible Gaussian velocity field. To be published in Russian Mathematical Sur-
veys
29. Lototsky, S.V., Rozovskii, B.L.: Wiener chaos solutions of linear stochastic evo-
lution equations. Submitted to Annals of Probability
30. Meyer, P-A.: Quantum Probability for Probabilists. Lecture Notes in Mathe-
matics, 1538 (1993)

506
S. Lototsky and B. Rozovskii
31. Mikulevicius, R., Rozovskii, B.L.: Global L2-solutions of stochastic Navier–
Stokes equations. To be published in Annals of Probability
32. Mikulevicius, R., Rozovskii, B.L.: Separation of observations and parameters in
nonlinear filtering. In: Proceedings of the 32nd IEEE Conference on Decision
and Control 1564–1559 (1993)
33. Mikulevicius, R., Rozovskii, B.L.: Linear parabolic stochastic PDE’s and Wiener
chaos. SIAM Journal on Mathematical Analysis 29(2), 452–480 (1998)
34. Mikulevicius, R., Rozovskii, B.L.: Stochastic Navier–Stokes equations. Propa-
gation of chaos and statistical moments. In: Optimal Control and Partial Dif-
ferential Equations. Eds. J.L. Menaldi, E. Rofman, and A. Sulem, IOS Press
258–267 (2001)
35. Mikulevicius, R., Rozovskii, B.L.: Stochastic Navier–Stokes equations for tur-
bulent flows. SIAM Journal on Mathematical Analysis 35(5), 1250–1310 (2004)
36. Monin, A.S., Yaglom, A.M.: Statistical Fluid Mechanics: Mechanics of Turbu-
lence, Vol. 1. MIT Press 1971
37. Nualart, D: Malliavin Calculus and Related Topics. Springer 1995
38. Nualart, D., Rozovskii, B.L.: Weighted stochastic Sobolev spaces and bilinear
SPDE’s driven by space-time white noise. Journal of Functional Analysis 149(1),
200–225 (1997)
39. Ocone, D.: Multiple integral expansions for nonlinear filtering. Stochastics 10(1),
1–30 (1983)
40. Potthoff, J., V˚age, G., Watanabe, H.: Generalized solutions of linear parabolic
stochastic partial differential equations. Applied Mathematics and Optimization
38, 95–107 (1998)
41. G. Da Prato, G., Zabczyk, J.: Stochastic Equations in Infinite Dimensions. Cam-
bridge University Press 1992
42. Rozovskii, B.L.: Stochastic Evolution Systems. Kluwer 1990
43. Rudin, W.: Functional Analysis. McGraw-Hill 1973
44. Stroock,
D.W.,
Varadhan,
S.R.S.:
Multidimensional
Diffusion
Processes.
Springer 1979
45. Vishik, M.I., Fursikov, A.V.: Mathematical Problems of Statistical Hydrome-
chanics. Kluwer 1979
46. Wong, E.: Explicit solutions to a class of nonlinear filtering problems. Stochastics
16(5), 311–321 (1981)

A Martingale Equation of Exponential Type
Michael MANIA1 ∗and Revaz TEVZADZE2
1 A.Razmadze Mathematical Institute, 1 Alexidze Street, Tbilisi, 0193, Georgia.
mania@rmi.acnet.ge
2 Institute of Cybernetics, 5 Euli Street, Tbilisi, 0186, Georgia.
tevza@cybernet.ge
Summary. We establish the existence of unique solution of an exponential martin-
gale equation in the class of BMO martingales. The solution is used to characterize
variance-optimal martingale measures.
Key words: backward stochastic differential equation, exponential martingale,
martingale measures
Mathematics Subject Classification (2000): 90A09, 60H30, 90C39
JEL Classification Numbers: G11
1 Introduction
Let (Ω, F, P) be a probability space with filtration F = (Ft)t∈[0,T ]. We assume
that all local martingales with respect to F are continuous. Here T is a fixed
time horizon and F = FT .
Let M be a stable subspace of the space of square integrable martingales
H2. Its ordinary orthogonal M⊥is a stable subspace of H2 and any element
of M is strongly orthogonal to any element of M⊥(see, e.g., [4]).
We consider the following exponential equation
ET (m)
ET (m⊥) = ceη,
(1.1)
where η is a given FT -measurable random variable. Solution of equation (1.1)
is a triple (c, m, m⊥), where c is a constant, m ∈M and m⊥∈M⊥. Here
E(X) is the Dol´eans-Dade exponential of X.
∗Research supported by Grant INTAS 99 00559.

508
Michael Mania and Revaz Tevzadze
If M and M⊥are stable subspaces of H2 generated by given local martin-
gales M and N, strongly orthogonal to each other, then equation (1.1) takes
the form
ET (
 .
0 ZsdMs)
ET (
 .
0 Z⊥
s dNs) = ceη
(1.2)
and solution of (1.2) is a triple (c, Z, Z⊥), where Z and Z⊥are predictable M
and N integrable processes, respectively. Equations of such type are arising
in mathematical finance. They are used to characterize the variance-optimal
martingale measure (see [1], [12], [13] for such characterizations and also [3]
and [14] for the definition of the variance-optimal martingale measure and
related results). Note that the exponential equation of the form (1.1) can also
be applied to the financial market models with infinitely many assets.
Our aim is to prove the existence of (unique) solution of equation (1.1)
in the class of BMO-martingales. The main statement of the paper is the
following:
Theorem 1. Let η
∈
L∞(FT ). Then there exists a unique triple
(c, m, m⊥), where c ∈R+, m ∈BMO ∩M, m⊥∈BMO ∩M⊥, that sat-
isfies equation (1.1).
One can show that equation (1.1) is equivalent to the semimartingale back-
ward equation
Yt = Y0 −⟨L⟩t + ⟨L⊥⟩t + Lt + L⊥
t ,
YT = 1
2η.
(1.3)
We show that there exists a unique triple (Y, L, L⊥), where Y is a bounded
continuous semimartingale, L ∈BMO ∩M, L⊥∈BMO ∩M⊥, satisfying
equation (1.3). If the filtration F is generated by a multidimensional Brownian
motion ˜W = (W 1, ..., W n) and M, M⊥are stable subspaces of H2 generated
by W = (W 1, ..., W k), W ⊥= (W k+1, ..., W n) respectively, then equation (1.3)
takes the form of the usual backward stochastic differential equation (BSDE)
Yt = 1
2η +
 T
t
|Zs|2ds −
 T
t
|Z⊥
s |2ds −
 T
t
ZsdWs −
 T
t
Z⊥
s dW ⊥
s . (1.4)
The existence of a solution of equation (1.4) follows from the results of [9] and
[10], where the BSDEs with drivers satisfying the quadratic growth conditions
(and η ∈L∞(FT )) were considered. To our knowledge, there are no general
results on BSDEs driven by martingales and including drivers with quadratic
growth. In [2] and [6] the well-posedness of BSDEs driven by martingales with
drivers satisfying global Lipschitz type conditions was established.
It is easy to see that if in front of square characteristics ⟨L⟩and ⟨L⊥⟩(of
equation (1.3)) we were have the identical signs, then such an equation would
admit an explicit solution. For example, a solution of the equation
Yt = Y0 −⟨L⟩t −⟨L⊥⟩t + Lt + L⊥
t ,
YT = 1
2η,

Exponential Martingale Equation
509
(which corresponds to the exponential equation ET (m)ET (m⊥) = ceη) is the
triple (Y, L, L⊥):
Lt = 1
2
 t
0
1
E(eη|Fs)dms(η),
L⊥
t = 1
2
 t
0
1
E(eη|Fs)dm⊥
s (η),
Yt = E
1
2η + ⟨L⟩T −⟨L⟩t + ⟨L⊥⟩T −⟨L⊥⟩t
Ft

,
where the martingales m(η) and m⊥(η) are defined by the orthogonal decom-
position
E(eη|Ft) = Eeη + mt(η) + m⊥
t (η),
m(η) ∈M,
m⊥(η) ∈M⊥.
Note that the problem to find the solution of equation (1.3) is caused here only
by opposite signs at the square characteristics of martingales L and L⊥, but
the method of the proof of Theorem 1 can be extended for semimartingale
BSDEs with more general drivers (see, e.g., the remark at the end of the
paper). The paper [12] seems to be the first one where the theory of BMO-
martingales was used for BSDEs. For BSDEs similar to (1.3) it was shown that
the martingale part of any bounded solution Y of (1.3) belongs to the class
BMO. This fact shows, that it should be convenient to operate with BMO-
norms in order to prove the existence of solution for equation (1.3) or for
more general BSDEs with drivers satisfying the quadratic growth condition.
Using the BMO-norms for martingales L, L⊥and the | · |∞-norm for the
semimartingale Y , we apply the contraction principle to show the existence
of a solution, first in case where the | · |L∞-norm of η is sufficiently small and
then, applying a specific result (see Lemma 1) we construct a solution for an
arbitrary η ∈L∞.
For all unexplained notations concerning the martingale theory used below
we refer to [7], [4] and [11]. About BMO-martingales see [5] or [8].
2 Proof of the Main Result
First let us introduce some notations.
We say that the process B strongly dominates the process A and write A ≺
B, if the difference B −A ∈A+
loc, i.e. B −A is a locally integrable increasing
process. We shall use also the notation ψ · X for the stochastic integral with
respect to the semimartingale X. For the process of finite variation A we
denote by vart
s(A) the variation of A on the interval [s, t].
We use R∞to denote the space of all adapted c`adl`ag processes Y such
that
|Y |∞= |Y ∗
T |L∞< ∞,
where Y ∗
t = sups≤t |Ys|.
As stated before, we deal entirely with continuous local martingales and
for convenience we shall use the following definition of BMO-martingales.

510
Michael Mania and Revaz Tevzadze
The square integrable martingale M belongs to the class BMO if there is
a constant C > 0 such that
E1/2(⟨M⟩T −⟨M⟩τ|Fτ) ≤C,
P-a.s.
for every stopping time τ. The smallest constant with this property (or +∞if
it does not exist) is called the BMO-norm of M and is denoted by |M|BMO.
Since the class BMO depends on the underlying probability measure, we shall
use notation BMO(Q) if the measure Q is different from the basic probability
measure P.
Let N ∈BMO and dQ = ET (N)dP. Then Q is a probability measure
equivalent to P by Theorem 2.3 of [8]. Denote by ψ = ψN(X) = ⟨X, N⟩−X
the Girsanov transformation. It is well known (see [8]) that if N ∈BMO, then
both H2 and BMO are invariant under the transformation ψ. Let M(Q) and
M⊥(Q) be the images of the mapping ψ for M and M⊥, respectively. Note
that M(Q) and M⊥(Q) are stable orthogonal subspaces of the space H2(Q)
of square integrable martingales with respect to Q.
In the sequel we shall need the following
Lemma 1. Suppose that there are m1, m⊥
1 ∈BMO, m1 ∈M, m⊥
1 ∈M⊥
such that
ET (m1)
ET (m⊥
1 ) = c1eη1.
(1.5)
Let Q be a probability measure defined by
dQ = ET (m1 + m⊥
1 )dP
and assume that there exist m2, m⊥
2 ∈BMO(Q), m2 ∈M(Q), m⊥
2 ∈M⊥(Q)
such that
ET (m2)
ET (m⊥
2 ) = c2eη2.
(1.6)
Then there exists a solution of the equation
ET (m)
ET (m⊥) = ceη1+η2.
(1.7)
Proof. Note that
dP
dQ = E−1
T (m1 + m⊥
1 ) = ET ( ˜m1 + ˜m⊥
1 ),
where ˜m1 = ⟨m1⟩−m1 and ˜m⊥
1 = ⟨m⊥
1 ⟩−m⊥
1 ∈BMO(Q).
By the Girsanov theorem m2 and m⊥
2 are special semimartingales under
P with the decomposition

Exponential Martingale Equation
511
m2 = ˆm2 + ⟨m2, ˜m1⟩, m⊥
2 = ˆm⊥
2 + ⟨m⊥
2 , ˜m⊥
1 ⟩,
(1.8)
where ˆm2 = m2−⟨m2,
˜m1⟩and ˆm⊥
2 = m⊥
2 −⟨m⊥
2 , ˜m⊥
1 ⟩are BMO-martingales
under P according to Theorem 3.6 of [8].
It is evident that
⟨ˆm2, m1⟩= −⟨m2, ˜m1⟩,
⟨ˆm⊥
2 , m⊥
1 ⟩= −⟨m⊥
2 , ˜m⊥
1 ⟩.
(1.9)
Multiplying now equations (1.5) and (1.6), using the Yor formula and decom-
position (1.8) we obtain that
ET (m1 + m2 + ⟨ˆm2, m1⟩)
ET (m⊥
1 + m⊥
2 + ⟨ˆm⊥
2 , m⊥
1 ⟩) = c1c2eη1+η2.
(1.10)
By equality (1.9) and Theorem 3.6 of [8] m2 + ⟨ˆm2, m1⟩and m⊥
2 + ⟨ˆm⊥
2 , m⊥
1 ⟩
are BMO-martingales under P. It is easy to see that these martingales are
strongly orthogonal to each other. Thus, c = c1c2, m = m1 + m2 + ⟨ˆm2, m1⟩
and m⊥= m⊥
1 + m⊥
2 + ⟨ˆm⊥
2 , m⊥
1 ⟩satisfy equation (1.7).
⊓⊔
The proof of Theorem 1.
Uniqueness. Let (c, m, m⊥) and (c′, l, l⊥) be two solutions of (1.1) from
the class BMO. Then (1.1) implies that
c′ ET (m)
ET (m⊥) = c ET (l)
ET (l⊥),
(1.11)
and, by Yor’s formula,
c′ET (m + l⊥) = cET (m⊥+ l).
(1.12)
Since m + l⊥and m⊥+ l are BMO-martingales, according to Theorem 2.3
of [8], E(m + l⊥) and E(m⊥+ l) are uniformly integrable martingales. Hence,
equality (1.12) holds for any t ∈[0, T]. Therefore, c = c′ and m+l⊥= m⊥+l.
Consequently, m = l and m⊥= l⊥.
Existence. It is evident that equation (1.1) is equivalent to the following
martingale equation
−ln c′ −1
2⟨m⟩T + 1
2⟨m⊥⟩T + mT −m⊥
T = η.
(1.13)
Denoting c′ = −1
2 ln c, L = 1
2m, L⊥= −1
2m⊥and ξ = 1
2η one can write this
equation as
c −⟨L⟩T + ⟨L⊥⟩T + LT + L⊥
T = ξ.
(1.14)
This equation can also be written in the following equivalent semimartingale
form as a BSDE:
Yt = Y0 −⟨L + L⊥, L −L⊥⟩t + Lt + L⊥
t ,
YT = ξ.
(1.15)

512
Michael Mania and Revaz Tevzadze
Let us show first that there exists a solution (c, L, L⊥) of equation (1.14) if
|ξ|∞is small enough.
For brevity we shall use the notation ⟨m⟩tT = ⟨m⟩T −⟨m⟩t for the incre-
ment of square characteristic ⟨m⟩of a martingale m.
Let us consider the mapping
Lt + L⊥
t = E(ξ + ⟨l + l⊥, l −l⊥⟩T |Ft)
(1.16)
−E(ξ + ⟨l + l⊥, l −l⊥⟩T ),
Yt = E(ξ + ⟨l + l⊥, l −l⊥⟩tT |Ft),
(1.17)
which transforms BMO-martingales l and l⊥into a triple (Y, L, L⊥), where L
and L⊥are BMO-martingales and Y is a semimartingale. Using |Y |∞-norms
for semimartingales and the BMO-norms for martingales, we shall show that
if the norm |ξ|∞is sufficiently small, then there exists r > 0 such that the
mapping (1.16) is a contraction in the ball
Br = {(l, l⊥) : |l + l⊥|BMO ≤r}.
Using the Itˆo formula for Y 2
T −Y 2
t and (1.16), (1.17) we have
Y 2
t −Y 2
T = −2
 T
t
Ysd(Ls + L⊥
s )
+2
 T
t
Ysd⟨l + l⊥, l −l⊥⟩s −⟨L + L⊥⟩tT .
(1.18)
Since ξ ∈L∞, equations (1.16) and (1.17) imply that for any l, l⊥∈BMO
the process Y is bounded and the processes L and L⊥are square integrable
martingales. Therefore, the stochastic integral Y · (L + L⊥) is a martingale.
Taking conditional expectations in (1.18) we have
Y 2
t + E(⟨L + L⊥⟩tT |Ft) = E(ξ2|Ft) + 2E
	 T
t
Ysd⟨l + l⊥, l −l⊥⟩s
Ft

.
Since ⟨l+l⊥, l−l⊥⟩≺⟨l+l⊥⟩, using the elementary inequality 1
2a2+2b2 ≥2ab,
we get that
Y 2
t + E(⟨L + L⊥⟩tT |Ft)
≤|ξ|2
∞+ 2|Y |∞E(⟨l + l⊥⟩tT |Ft)
≤|ξ|2
∞+ 1
2|Y |2
∞+ 2E2(⟨l + l⊥⟩tT |Ft)
≤|ξ|2
∞+ 1
2|Y |2
∞+ 2|l + l⊥|4
BMO.
(1.19)
From (1.19) we have
Y 2
t ≤|ξ|2
∞+ 1
2|Y |2
∞+ 2|l + l⊥|4
BMO;

Exponential Martingale Equation
513
taking the | · |∞-norm of the left-hand side of this inequality we obtain the
bound
1
2|Y |2
∞≤|ξ|2
∞+ 2|l + l⊥|4
BMO.
(1.20)
From (1.19) we also have
E(⟨L + L⊥⟩tT |Ft) ≤|ξ|2
∞+ 1
2|Y |2
∞+ 2|l + l⊥|4
BMO.
Therefore, from (1.20) we obtain that
E(⟨L + L⊥⟩tT |Ft) ≤2|ξ|2
∞+ 4|l + l⊥|4
BMO
and, hence,
|L + L⊥|2
BMO ≤2|ξ|2
∞+ 4|l + l⊥|4
BMO.
(1.21)
If |ξ|∞≤
1
4
√
2 then there exists r ≥0 that satisfies the inequality
2|ξ|2
∞+ 4r4 ≤r2
(1.22)
It is easy to see that for such r (i.e. for r satisfying inequality (1.22)), from
|l + l⊥|BMO ≤r it follows that |L + L⊥|BMO ≤r. Indeed, if |l + l⊥|BMO ≤r then
from (1.21) we have
|L + L⊥|2
BMO ≤2|ξ|2
∞+ 4r4,
which implies that |L + L⊥|2
BMO ≤r2 because r satisfies inequality (1.22).
Now we shall show that the mapping (1.16) is a contraction on the ball
Br. Let Yi, Li, L⊥
i , i = 1, 2, correspond to li, li by the transformation (1.16),
(1.17). Since Y1(T) −Y2(T) = 0, we obtain similarly to (1.19), by applying
the Ito formula to (Y1 −Y2)2 that
(Y1(t) −Y2(t))2 + E(⟨L1 −L2 + L⊥
1 −L2
⊥⟩tT |Ft)
= 2E
  T
t
(Y1(s) −Y2(s))
×d(⟨l1 + l⊥
1 , l1 −l⊥
1 ⟩−⟨l2 + l⊥
2 , l2 −l⊥
2 ⟩)
Ft

(1.23)
≤1
2|Y1 −Y2|2
∞
+2E2(varT
t (⟨l1 + l⊥
1 , l1 −l⊥
1 ⟩−⟨l2 + l⊥
2 , l2 −l⊥
2 ⟩)|Ft).
Note that the process
⟨l1 + l⊥
1 , l1 −l⊥
1 ⟩−⟨l2 + l⊥
2 , l2 −l⊥
2 ⟩
coincides with the process
⟨l1 + l⊥
1 −l2 −l⊥
2 , l1 −l⊥
1 ⟩+ ⟨l1 + l⊥
1 −l2 −l⊥
2 , l2 −l⊥
2 ⟩.

514
Michael Mania and Revaz Tevzadze
Using successively the elementary inequalities
varT
t (A + B) ≤varT
t (A) + varT
t (B),
(a + b)2 ≤2(a2 + b2) and the Kunita–Watanabe inequality, we get that
E2(varT
t (⟨l1 + l⊥
1 , l1 −l⊥
1 ⟩−⟨l2 + l⊥
2 , l2 −l⊥
2 ⟩)|Ft)
≤2E2(varT
t ⟨l1 + l⊥
1 −l2 −l⊥
2 , l1 −l⊥
1 ⟩|Ft)
+2E2(varT
t ⟨l1 + l⊥
1 −l2 −l⊥
2 , l2 −l⊥
2 ⟩|Ft)
≤2E(⟨l1 −l⊥
1 ⟩tT |Ft)E(⟨ll + l⊥
1 −l2 −l⊥
2 ⟩tT |Ft)
+2E(⟨l2 −l2
⊥⟩tT |Ft)E(⟨ll + l⊥
1 −l2 −l⊥
2 ⟩tT |Ft).
(1.24)
Since for any l + l⊥∈Br we have the bound E(⟨l −l⊥⟩tT |Ft ≤r2, we obtain
from (1.24) that for all l1 + l⊥
1 , l2 + l⊥
2 ∈Br
E2(varT
t (⟨l1 + l⊥
1 , l1 −l⊥
1 ⟩−⟨l2 + l⊥
2 , l2 −l⊥
2 ⟩)|Ft)
≤2E(⟨l1 + l⊥
1 −l2 −l⊥
2 ⟩tT |Ft)
×[E(⟨l1 −l⊥
1 ⟩tT |Ft) + E(⟨l2 −l2
⊥⟩tT |Ft)]
≤4r2E(⟨l1 + l⊥
1 −l2 −l⊥
2 ⟩tT |Ft)
≤4r2|l1 + l⊥
1 −l2 −l⊥
2 |2
BMO.
(1.25)
Inequalities (1.23) and (1.25) imply that for all l1 + l⊥
1 , l2 + l⊥
2 ∈Br
(Y1(t) −Y2(t))2 + E(⟨L1 −L2 + L⊥
1 −L2
⊥⟩tT |Ft)
≤1
2|Y1 −Y2|2
∞+ 8r2|l1 + l⊥
1 −l2 −l⊥
2 |2
BMO.
(1.26)
Using similar arguments as above (see equations (1.19) – (1.21) ) we obtain
that the estimate
|L1 −L2 + L⊥
1 −L2
⊥|BMO ≤4r|l1 −l2 + l⊥
1 −l⊥
2 |BMO
holds. Finally, we remark that, if |ξ|∞≤
1
6 and
1
32 ≤r2 <
1
16, then the
inequalities (1.22) and r < 1
4 are satisfied simultaneously. Thus, we obtain
that if |ξ|∞is small enough (namely, if |ξ|∞< 1
6), then the mapping (1.16) is
a contraction in Br and by the fixed point theorem there exists a unique pair
(˜L, ˜L⊥) such that
˜Lt + ˜L⊥
t = E(ξ + ⟨˜L + ˜L⊥, ˜L −˜L⊥⟩T |Ft)
(1.27)
−E(ξ + ⟨˜L + ˜L⊥, ˜L −˜L⊥⟩T )
and
Yt = E(ξ + ⟨˜L + ˜L⊥, ˜L −˜L⊥⟩tT |Ft).
Taking t = T in (1.27) we obtain that the triple (c, ˜L, ˜L⊥), where the constant
c = E(ξ + ⟨˜L + ˜L⊥, ˜L −˜L⊥⟩T ), satisfies equation (1.14) and, hence, equation

Exponential Martingale Equation
515
(1.1) admits a unique solution. Namely, if |ξ|∞≤1
6 then the BMO-norm of
the solution is less than 1
4.
To get rid of the assumption that |ξ|∞is sufficiently small, we shall use
Lemma 1. Let us take an integer n ≥1 such that the equation
ET (m)
ET (m⊥) = c1e
1
n ξ
(1.28)
admits a solution. Let dQ = ET (m1 + m⊥
1 )dP, where (m1, m⊥
1 ) ∈BMO(P)
be a solution of (1.28). Since the norm |ξ|∞is invariant with respect to an
equivalent change of measure and since the Girsanov transformation is an
isomorphism of BMO(P) onto BMO(Q), similarly as above one can show
that there exists a pair m2, m⊥
2 ∈BMO(Q) that satisfies equation (1.28).
Therefore, by Lemma 1, there exists a solution of equation
ET (m)
ET (m⊥) = c2e
2
n ξ.
(1.29)
Using now Lemma 1 to equation (1.29) by induction we obtain that there
exists a solution of the equation (1.1) for an arbitrary ξ ∈L∞.
⊓⊔
Remark. By the same way one can show the solvability of the following,
more general, BSDE
Yt = Y0 +
 t
0
g(s)d⟨L⟩s +
 t
0
g⊥(s)⟨L⊥⟩s + Lt + L⊥
t ,
YT = ξ,
for given bounded predictable processes g, g⊥and ξ ∈L∞(FT ).
References
1. Biagini F., Guasoni P., Pratelli M.: Mean variance hedging for stochastic volatil-
ity models. Math. Finance, 10, 109–123 (2000)
2. Chitashvili R.: Martingale ideology in the theory of controlled stochastic
processes. Lect. Notes in Math., Springer, Berlin, 1021, 73–92 (1983)
3. Delbaen F., Schachermayer W.: Variance-optimal martingale measure for con-
tinuous processes. Bernoulli 2 1, 81–105 (1986)
4. Dellacherie C., Meyer P.-A.: Probabilit´es et potentiel. Chapitres V a VIII.
Th´eorie des martingales. Actualit´es Scientifiques et Industrielles Hermann,
Paris, 1980
5. Dol/’eans-Dade K., Meyer P.-A.: In´egalit´es de normes avec poinds. S´eminaire de
Probabilit´es XIII, Lect. Notes in Math., Springer, Berlin, 721, 204–215 (1979)
6. El Karoui N., Huang S.J.: A general result of existence and uniqueness of back-
ward stochastic differential equations. Pitman Res. Notes Math., 364, Longman,
Harlow, 27–36 (1997)
7. Jacod J.: Calcul Stochastique et Probl`emes des Martingales. Lecture Notes in
Math., Springer, Berlin, 714, 1979.

516
Michael Mania and Revaz Tevzadze
8. Kazamaki N.: Continuous exponential martingales and BMO, Lecture Notes in
Math., 1579, Springer, Berlin, N., 1994
9. Kobylanski M.: Backward stochastic differential equation and partial differential
equations with quadratic growth. The Annals of Probability, 28, 558–602 (2000)
10. Lepeltier J.P., San Martin J.: Existence for BSDE with superlinear-quadratic
coefficient. Stoch. Stoch. Rep. 63, 227–240 (1998)
11. Liptser R.Sh., Shiryayev A.N.: Martingale theory, Nauka, Moscow, 1986
12. Mania M., Tevzadze R.: A Semimartingale Bellman equation and the variance-
optimal martingale measure,. Georgian Math. J. 7, 765–792 (2000)
13. Mania M., Tevzadze R.: A Semimartingale Bellman equation and the variance-
optimal martingale measure under general information flow. SIAM Journal on
Control and Optimization, 42, 1703–1726 (2003)
14. Schweizer M.: Approximation pricing and the variance optimal martingale mea-
sure. The Annals of Probab. 24, 206–236 (1996)

On Local Martingale and its Supremum:
Harmonic Functions and beyond.
Jan OB`L´OJ1,2 and Marc YOR1
1 Laboratoire de Probabilit´es et Mod`eles Al´eatoires, Universit´e Paris 6,
4 pl. Jussieu, Boˆıte 188, 75252 Paris Cedex 05, France.
2 Wydzia^l Matematyki, Uniwersytet Warszawski
Banacha 2, 02-097 Warszawa, Poland.
obloj@mimuw.edu.pl
Summary. We discuss certain facts involving a continuous local martingale N and
its supremum N. A complete characterization of (N, N)-harmonic functions is given.
This yields an important family of martingales, the usefulness of which is demon-
strated, by means of examples involving the Skorohod embedding problem, bounds
on the law of the supremum, or the local time at 0, of a martingale with a fixed
terminal distribution, or yet in some Brownian penalization problems. In particular
we obtain new bounds on the law of the local time at 0, which involve the excess
wealth order.
Key words: continuous local martingale, supremum process, harmonic function,
Skorohod’s embedding problem, excess wealth order.
Mathematics Subject Classification (2000): 60G44 (Primary), 60G42,
60G40, 60E15
Dedication. The first time I met Prof. A. Shiryaev was in January 1977,
during a meeting dedicated to Control and Filtering theories, in Bonn. This
was a time when meeting a Soviet mathematician was some event! Among the
participants to that meeting, were, apart from A. Shiryaev, Prof. B. Grige-
lionis, and M. Yershov, who was by then just leaving Soviet Union in hard
circumstances. To this day, I vividly remember that A.S, M.Y. and myself
spent a full Sunday together, trying to solve a succession of problems raised
by A.S., who among other things, explained at length about Tsirel’son’s ex-
ample of a one-dimensional SDE, with path dependent drift, and no strong
solution ([32]; this motivated me to give - in [37] - a more direct proof than
the original one by Tsirel’son, see also [38], and Revuz and Yor [24] p. 392).
Each of my encounters with A.S. has had, roughly, the same flavor: A.S. would
present, with great enthusiasm, some recent or not so recent result, and ask

518
Jan Ob^l´oj and Marc Yor
me for some simple proof, extension, etc... I have often been hooked into that
game, which kept reminding me of one of my favorite pedagogical sentences
by J. Dixmier: When looking for the 50th time at a well-known proof of some
theorem, I would discover a new twist I had never thought of, which would cast
a new light on the matter. I hope that the following notes, which discuss some
facts about local martingales and their supremum processes, and are closely
related to the thesis subject of the first author, may also have some this “new
twist” character for some readers, and be enjoyed by Albert Shiryaev, on the
occasion of his 70th birthday.
Marc Yor
1 Introduction
In this article we focus on local martingales, functions of two-dimensional
processes, whose components are a continuous local martingale (Nt : t ≥0)
and its supremum N t = supu≤t Nu, i.e. on local martingales of the form
(H(Nt, N t) : t ≥0), where H : R × R+ →R. We call functions H such that
(H(Nt, N t) : t ≥0) is a local martingale, (N, N)-harmonic functions. Some
examples of such local martingales are
F(N t) −f(N t)(N t −Nt),
t ≥0,
(1.1)
where F ∈C1 and F ′ = f, introduced by Az´ema and Yor [3]. We show that
(1.1) defines a local martingale for any Borel, locally integrable function f.
We conjecture that these are the only local martingales, that is that the only
(N, N)-harmonic functions are of the form H(x, y) = F(y) −f(y)(y −x) + C,
with f a locally integrable function, F(y) =
 y
0 f(u)du, and C a constant.
We explain, in an intuitive manner, how these local martingales, which we
call max-martingales, may be used to find the Az´ema–Yor solution to the
Skorohod embedding problem. We then go on and develop, with the help of
these martingales, the well-known bounds on the law of the supremum of a
uniformly integrable martingale with a fixed terminal distribution. Using the
L´evy and Dambis–Dubins–Schwarz theorems, we reformulate the results in
terms of the absolute value |N| and the local time LN at 0, of the local mar-
tingale N. This leads to some new bounds on the law of the local time of a
uniformly integrable martingale with fixed terminal distribution. A recently
introduced and studied stochastic order, called the excess wealth order (see
Shaked and Shanthikumar [28]), plays a crucial role. We also point out that the
max-martingales appear naturally in some Brownian penalization problems.
Finally, we try to sketch a somewhat more general viewpoint linked with the
balayage formula. The organization of this paper is as follows. We start in Sec-
tion 3 with a discrete version of the balayage formula and show how to deduce
from it Doob’s maximal and Lp inequalities. In the subsequent Section 4, in
Theorem 4.1, we formulate the result about the harmonic functions of (N, N)

On Brownian Motion and its Supremum
519
and prove it in a regular case. Section 5 is devoted to some applications: it
contains three subsections concentrating respectively on the Skorohod embed-
ding problem, bounds on the laws of N and LN, and Brownian penalizations.
The last section contains a discussion of the balayage formula.
2 Notation
Throughout this paper (Nt : t ≥0) denotes a continuous local martingale
with N0 = 0 and ⟨N⟩∞= ∞a.s., and N t = sups≤t Ns denotes its maximum
process. We have adopted this notation so that there is no confusion with
stock-price processes, which are often denoted St. The local time at 0 of N is
denoted (LN
t : t ≥0). For processes either in discrete or in continuous time,
when we say that a process is a (sub/super) martingale without specifying
the filtration, we mean the natural filtration of the process.
B = (Bt : t ≥0) shall denote a one-dimensional Brownian motion, starting
from 0, and Bt = sups≤t Bs. The natural filtration of B is denoted (Ft) and
is taken completed.
The indicator function is denoted 1. We use the notations a ∨b = max{a, b}
and a ∧b = min{a, b}. The positive part is given by x+ = x ∨0. For µ a
probability measure on R, µ(x) := µ([x, ∞)) is its tail distribution function;
X ∼µ means X has distribution µ.
3 Balayage in discrete time and some applications
We start with the discrete time setting, and present a simple idea, which
corresponds to balayage in continuous time, and which proves an efficient tool,
as it allows, for example, to obtain easily Doob’s maximal and Lp inequalities.
Let (Ω, F, (Fn)n∈N, P) be a filtered probability space and (Yn : n ≥0) be some
real-valued adapted discrete stochastic process. Let (ϕn : n ≥0) be also an
adapted process, which further satisfies ϕn1Yn̸=0 = ϕn−11Yn̸=0, for all n ∈N.
The last condition can be also formulated as “the process (ϕn) is constant on
excursions of (Yn) away from 0”.
Lemma 3.1. Let (Yn, ϕn) be as above, Y0 = 0. The following identities hold:
ϕnYn = ϕn−1Yn =
n

k=1
ϕk−1(Yk −Yk−1),
n ≥1.
(3.1)
Proof. The first equality is obvious as ϕnYn = ϕnYn1Yn̸=0 = ϕn−1Yn, and the
second one is obtained by telescoping.
✷
To see how the above can be used, let us give some examples of pairs
(Yn, ϕn) involving in particular an adapted process Xn and its maximum Xn:
•
Yn = Xn −Xn and ϕn = f(Xn), for some Borel function f;

520
Jan Ob^l´oj and Marc Yor
•
Yn = Xn, ϕn = n
k=0 1Xk=0 (note that Yn = |Xn| works as well);
•
Yn = X∗
n−|Xn|, ϕn = f(X∗
n), for some Borel function f, where the process
X∗
n = maxk≤n |Xk|;
•
Yn = Xn −Xn, ϕn = f
 n
k=1 1(Xk=Xk)

, for some Borel function f,
where Xn = | mink≤n Xk|.
We now use the discrete balayage formula with the first of the above examples
to establish a useful supermartingale property.
Proposition 3.1. Let (Xn : n ∈N) be a submartingale in its natural filtra-
tion (Fn), X0 = 0, and let f be some increasing, locally integrable, positive
function. Assume that Ef(Xn) < ∞and EF(Xn) < ∞for all n ∈N, where
F(x) =
 x
0 f(s)ds. Then the process Sf
n = f(Xn)(Xn −Xn) −F(Xn) is a
(Fn)-supermartingale.
Proof. Since the pair (Xn −Xn, f(Xn)) satisfies the assumptions of Lemma
3.1, we have:
Sf
n =
n

k=1
f(Xk−1)(Xk −Xk −Xk−1 + Xk−1) −F(Xn)
=
n

k=1
f(Xk−1)(Xk −Xk−1) −
n

k=1
f(Xk−1)(Xk −Xk−1) −
 Xn
0
f(x)dx
=
n

k=1
 Xk
Xk−1

f(Xk−1) −f(x)

dx −
n

k=1
f(Xk−1)(Xk −Xk−1).
(3.2)
Using (3.2), the fact that f is increasing, and (Xn) is a submartingale, we
obtain the supermartingale property for Sf
n.
✷
The above Proposition allows to recover Doob’s maximal and Lp inequal-
ities in a very easy way. Indeed, consider the function f(x) = 1x≥λ for some
λ > 0. Then the process Sf
n = S(λ)
n
= 1Xn≥λ(λ −Xn) is a supermartingale,
which yields Doob’s maximal inequality
λP

Xn ≥λ

≤E
)
1(Xn≥λ)Xn

.
(3.3)
To obtain the Lp inequalities we consider the function f(x) = pxp−1 for
some p > 1, and we suppose that (Xn : n ≥0) is a positive submartingale
with EXp
n < ∞. This implies, as X
p
n ≤n
k=1 Xp
k, that EX
p
n < ∞. The process
Sf
n = S(p)
n
= (p −1)(Xn)p −p(Xn)p−1Xn is then a supermartingale, which
yields
(p −1)E
)
(Xn)p
≤pE
)
(Xn)p−1Xn

and hence, applying H¨older’s ineq.,
E
)
(Xn)p
≤

p
p −1
p
E
)
Xp
n

,
which is Doob’s Lp ineq.
(3.4)

On Brownian Motion and its Supremum
521
To our best knowledge, this small wrinkle about Doob’s inequalities for
positive submartingales involving supermartingales does not appear in any of
the books on discrete martingales, such as Neveu [17], Garsia [12] or Williams
[36]. We point out also, that our method allows to obtain other variants of
Doob’s inequalities, such as L log L inequalities, etc.
4 The Markov process ((Bt, Bt) : t ≥0) and its
harmonic functions
In the rest of the paper we will focus on the continuous-time setup. It follows
immediately from the strong Markov property of B, or rather the indepen-
dence of its increments, that for s < t, and f : R×R+ →R+ a Borel function,
one has:
E
)
f(Bt, Bt)
Fs

= ˜E
)
f

Bs + ˜Bt−s, Bs ∨sup
u≤t−s
(Bs + ˜Bu)

,
(4.1)
where on the RHS, the notation ˜E indicates integration with respect to func-
tionals of the Brownian motion ( ˜Bu : u ≥0), which is assumed to be inde-
pendent of (Bt : t ≥0).
In particular, the two-dimensional process ((Bt, Bt) : t ≥0) is a nice
Markov process, hence a strong Markov process, and its semigroup can be
computed explicitly thanks to the well-known, and classical formula:
P

Bt ∈dx, Bt ∈dy

=
 2
πt3
1/2
(2y −x) exp

−(2y −x)2
2t

1(y≥x+)dxdy.
We are now interested in a description of the harmonic functions H of
(B, B) that is of Borel functions such that (H(Bt, Bt) : t ≥0) is a local
martingale. Note that this question is rather natural and interesting since
H is (B, B)-harmonic if and only if, thanks to the Dambis–Dubins–Schwarz
theorem, for any continuous local martingale (Nt : t ≥0), H is also (N, N)-
harmonic. The following proposition is an extension of Proposition 4.7 in
Revuz and Yor [24].
Theorem 4.1. Let N = (Nt : t ≥0) be a continuous local martingale with
⟨N⟩∞= ∞a.s., f a Borel, locally integrable function, and H defined through
H(x, y) = F(y) −f(y)(y −x) + C,
(4.2)
where C is a constant and F(y) =
 y
0 f(s)ds. Then, the following holds:
H(Nt, N t) = F(N t) −f(N t)(N t −Nt) + C
 t
0
f(N s)dNs + C,
t ≥0, (4.3)
and (H(Nt, N t) : t ≥0) is a local martingale.

522
Jan Ob^l´oj and Marc Yor
Remarks. Local martingales of the form (4.3) were first introduced by Az´ema
and Yor [3] and used to solve the Skorohod embedding problem (cf. Sec-
tion 5.1 below). In the light of the above theorem, we will call them max-
martingales and the functions given in (4.2) will be called MM-harmonic
functions (max-martingale harmonic) or (N, N)-harmonic. Note the resem-
blance of (4.3) with the discrete time process Sf
n given in Proposition 3.1.
It is known (see Revuz and Yor [24, Prop. VI.4.7]) that if H ∈C2,1 then the
reverse statement holds. That is, if H is (N, N)-harmonic then there exists
a continuous function f such that (4.2) holds. We present below a proof of
this fact. We conjecture that the same holds true if we only suppose that H
finely-continuous3.
Proof. As mentioned above, thanks to the Dambis–Dubins–Schwarz theorem,
it suffices to prove the theorem for N = B. We first recall how to prove the
converse of the theorem for the regular case. We assume that H ∈C2,1, with
obvious notation, and that H is (B, B)-harmonic. We denote by H′
x and H′
y
the partial derivatives of H in the first and the second argument respectively,
and H′′
x2 the second derivative of H in the first argument. Without loss of
generality, we assume that H(0, 0) = 0. Under the present assumptions we
can apply Itˆo’s formula to obtain:
H(Bt, Bt) =
 t
0
H′
x(Bs, Bs)dBs +
 t
0
H′
y(Bs, Bs)dBs + 1
2
 t
0
H′′
x2(Bs, Bs)ds,
where we used the fact that Bs = Bs, dBs-a.s. Now, since H(Bt, Bt) is a local
martingale, the above identity holds if and only if:
H′
y(Bs, Bs)dBs + 1
2H′′
x2(Bs, Bs)ds = 0,
s ≥0.
(4.4)
The random measures dBs and ds are mutually singular since we have dBs =
1(Bs−Bs=0)dBs and ds = d⟨B⟩s = 1(Bs−Bs̸=0)d⟨B⟩s. Equation (4.4) holds
therefore if and only if
H′
y(y, y) = 0
and
H′′
x2(x, y) = 0.
(4.5)
The second condition implies that H(x, y) = f(y)x + g(y) and the first one
then gives f ′(y)y+g′(y) = 0. Thus, g(y) = −
 y
0 uf ′(u)du =
 y
0 f(u)du−f(y)y.
This yields formula (4.2).
Furthermore, the above reasoning grants us that the formula (4.3) holds
for f of class C1. As C1 is dense in the class of locally integrable functions (in
an appropriate norm), if we can show that the quantities given in (4.3) are
well defined and finite for any locally integrable f on [0, ∞), then the formula
(4.3) extends to such functions through monotone class theorems. For f a
locally integrable function, F(x) is well defined and finite, so all we need to
3This conjecture is proved in Ob^l´oj [19].

On Brownian Motion and its Supremum
523
show is that
 t
0 f(Bs)dBs is well defined and finite a.s. This is equivalent to
 t
0

f(Bs)
2
ds < ∞a.s., which we now show.
Write Tx = inf{t ≥0 : Bt = x} for the first hitting time of x, which is a
well defined, a.s. finite, stopping time. Thus
 t
0

f(Bs)
2
ds < ∞a.s., if and
only if, for all x > 0,
 Tx
0

f(Bs)
2
ds < ∞. However, the last integral can be
rewritten as
 Tx
0
ds

f(Bs)
2
=

0≤u≤x
 Tu
Tu−
ds

f(Bs)
2
=

0≤u≤x
f 2(u)

Tu −Tu−

=
 x
0
f 2(u)dTu.
(4.6)
Now it suffices to note that (see Ex. III.4.5 in Revuz and Yor [24])
E
)
exp

−1
2
 x
0
f 2(u)dTu

= exp

−
 x
0
|f(u)|du

,
(4.7)
to see that the last integral in (4.6) is finite if and only if
 x
0 |f(u)|du < ∞,
which is precisely our hypothesis on f.
Note that the function H given by (4.2) is locally integrable as both func-
tions x →f(x) and x →xf(x) are locally integrable.
✷
L´evy’s theorem guarantees that the processes
((Bt, Bt) : t ≥0)
and
((Lt −|Bt|, Lt) : t ≥0) have the same distribution, where Lt denotes local
time at 0 of B. Theorem 4.1 yields therefore also a complete description of
(L, |B|)-harmonic functions, which again through Dambis–Dubins–Schwarz
theorem, extends to any local continuous martingale. We have the following
Corollary 4.1. Let N = (Nt : t ≥0) be a continuous local martingale with
⟨N⟩∞= ∞a.s., and LN = (LN
t
: t ≥0) its local time at 0. Let g a Borel,
locally integrable function, and H be defined through
H(x, y) = G(y) −g(y)x + C,
(4.8)
where C is a constant and G(y) =
 y
0 g(s)ds. Then, the following holds:
H(|Nt|, LN
t ) = G(LN
t )−g(LN
t )|Nt|+C = −
 t
0
g(LN
s )sgn (Ns) dNs+C,
t ≥0,
(4.9)
and (H(|Nt|, LN
t ) : t ≥0) is a local martingale.
5 Some appearances of the MM-harmonic functions
We now present some easy applications of the martingales described in the
previous section. (Nt : t ≥0) denotes always a continuous local martingale

524
Jan Ob^l´oj and Marc Yor
with ⟨N⟩∞= ∞a.s. We will show an intuitive way to obtain a solution to
the Skorohod embedding problem, as given by Az´ema and Yor [3]. We will
also discuss relations between the law of N T and the conditional law of NT
knowing N T , for some stopping time T. In the second subsection we will derive
well-known bounds on the law of N T , when the law of NT is fixed. We will
then continue in the same vein and describe the law of LN
T , when the law of
|NT | is fixed. We will end with a discussion of penalization of Brownian motion
with a function of its supremum and some absolute continuity relations.
5.1 On the Skorohod embedding problem
The classical Skorohod embedding problem can be formulated as follows: for
a given centered probability measure µ, find a stopping time T such that
NT ∼µ and (Nt∧T : t ≥0) is a uniformly integrable martingale. Numerous
solutions to this problem are known; for an extensive survey see Ob`l´oj [18].
Here we make a remark about the solution given by Az´ema and Yor in [3].
Namely we point out how one can arrive intuitively to this solution using the
max-martingales (4.3). Naturally, this might be extracted from the original
paper, but it may not be so obvious to do so.
The basic observation is that the max-martingales allow to express the law
of the terminal value of N, that is N T , in terms of the conditional distribution
of NT given N T . One then constructs a stopping time which actually binds
both terminal values through a function and sees that the function can be
obtained in terms of the target measure µ.
Proposition 5.1 (Vallois [35]). Let T be a stopping time, such that the
stopped process (Nt∧T : t ≥0) is a uniformly integrable martingale. Write ν
for the law of N T and suppose that ν is equivalent to the Lebesgue measure
on its interval support [0, b], b ≤∞. Then the law of N T is given by:
P

N T ≥y

= exp

−
 y
0
ds
s −ϕ(s)

,
0 ≤y ≤b,
(5.1)
where ϕ(x) = E[NT |N T = x], i.e. E[NT h(NT )] = E[ϕ(N T )h(N T )], for any
positive Borel function h.
Remark. Note that the above formula in the special case when NT = ϕ(N T )
a.s., and actually in the more general context of time-homogeneous diffusions,
was obtained already by Lehoczky [16]. Vallois [35] studied this issues in detail
and has some more general formulae.
Proof. Suppose first that EN T < ∞. With the help of the max-martingales
for any f : R+ →R, bounded with compact support, we get that
E
)
F(N T ) −f(N T )(N T −NT )

= 0.
Upon conditioning with respect to N T we obtain:

On Brownian Motion and its Supremum
525
E
)
F(N T ) −f(N T )(N T −ϕ(N T ))

= 0.
(5.2)
We can rewrite the above as a differential equation involving ν ∼N T , which
yields (5.1).
When EN T is possibly infinite we can stop conveniently and pass to the limit.
More precisely, let Rn = inf{t : N t = n} and ϕn(x) = E[NT ∧Rn|N T ∧Rn = x],
x ≤n. A refinement of the argumentation above shows that for any x < n,
P(N T ∧Rn ≥x) = exp{−
 x
0 ds/(s −ϕn(s))}. Observe however that for any
0 ≤x < n, P(N T ∧Rn ≥x) = P(N T ≥x) and ϕn(x) = ϕ(x). In consequence,
letting n →∞, we see that (5.1) holds for all x > 0.
✷
Let us define the Az´ema–Yor stopping time, as suggested above, through
Tϕ = inf{t ≥0 :
Nt = ϕ(N t)}, for some strictly increasing, continuous
function ϕ : R+ →R. Obviously NTϕ = ϕ(N Tϕ). We look for a function
ϕ = ϕµ such that NTϕµ ∼µ. To this end, we take x in the support of µ and
write
µ(x) = P(NTϕµ ≥x) = ν(ϕ−1
µ (x)) = exp

−
 ϕ−1
µ (x)
0
ds
s −ϕµ(s)

,
which may be considered as an equation on ϕµ in terms of µ. Solving this
equation, one obtains
ϕ−1
µ (x) = Ψµ(x) =
1
µ(x)

[x,∞)
s dµ(s),
(5.3)
the Hardy–Littlewood maximal function, or barycentre function, of µ.
Proposition 5.2 (Az´ema–Yor [3]). Let µ be a centered probability measure.
Define the function Ψµ through (5.3) for x such that µ(x) ∈(0, 1) and put
Ψµ(x) = 0 for x such that µ(x) = 1, Ψµ(x) = x for x such that µ(x) = 0.
Then the stopping time Tµ := inf{t ≥0 : N t ≥Ψµ(Nt)} satisfies NTµ ∼µ
and (Nt∧Tµ : t ≥0) is a uniformly integrable martingale.
The arguments presented above contain the principal ideas behind the Az´ema–
Yor solution to the Skorohod embedding problem. Naturally, they work well
for measures with positive density on R. A complete proof of Proposition 5.2
requires some rigorous arguments involving, for example, a limit procedure,
but this can be done, as shown by Michel Pierre [23].
We now develop a link between formula (5.1) and work of Rogers [25].
Let us carry out some formal computations. Write ρ for the law of the couple
(N T , N T −NT ) ∈R+ × R+, and ν for its first marginal (as above). Differen-
tiating (5.1) we find
dν(y)
= −ν(y)dy
y −ϕ(y),
hence
ν(y)dy = (y −ϕ(y))dν(y),
which we rewrite in terms of ρ
 
(y,∞)×R+
ρ(ds, dx)

dz =

(0,∞)
zρ(ds, dz).
(5.4)

526
Jan Ob^l´oj and Marc Yor
The last condition appears in Rogers [25] and is shown to be equivalent to the
existence of a continuous, uniformly integrable martingale (Nt∧T : t ≥0) such
that (N T , N T −NT ) ∼ρ. Our formulation in (5.1) is less general, as it is not
valid when the law of BT has atoms. However, when it is valid, it provides an
intuitive reading of (5.4).
To close this section, we point out that arguments similar to the ones
presented above, can be developed to obtain a solution to the Skorohod em-
bedding problem for |N| based on LN: it suffices to use the martingales given
by (4.9) instead of those given by (4.3). For a probability measure m on R+,
define the dual Hardy–Littlewood function (see Ob`l´oj and Yor [20]) through
ψm(x) =

[0,x]
y
m(y)dm(y),
for x such that m(x) ∈(0, 1),
(5.5)
and put ψm(x) = 0 for x such that m(x−) = 1 and ψm(x) = ∞for x such
that m(x+) = 0.
Proposition 5.3 (Vallois [33], ObPl´oj and Yor [20]). Let m be a non-
atomic probability measure on R+ and define the function ψm through (5.5).
Let ϕm(y) = inf{x ≥0 : ψm > y} be the right inverse of ψm. Then the
stopping time T m := inf{t > 0 : |N|t = ϕm(LN
t )} satisfies |N|T m ∼m.
Furthermore, (Nt∧T m : t ≥0) is a uniformly integrable martingale if and only
if
 ∞
0
xdm(x) < ∞.
The theorem is valid for probability measures with atoms upon proper exten-
sion of the definition of ψµ. We note that the law of LN
T m is given through
P(LN
T m ≥x) = exp

−
 x
0
ds
ϕm(s)

(cf. (5.4) in [20]). An easy analogue of
Proposition 5.1, is that this formula is also true for general stopping time
T, such that the law of LT has a density, with the function ϕm replaced by
ϕ(x) = E

|NT |
LN
T = x

.
5.2 Bounds on the laws of N T and LN
T
We present a classical bound on the law of N T , which was first obtained by
Blackwell and Dubins [4] and Dubins and Gilat [7] (see also Az´ema and Yor
[2], Kertz and R¨osler [14] and Hobson [13]).
Proposition 5.4. Let µ be a centered probability measure and T a stopping
time, such that NT ∼µ and (Nt∧T : t ≥0) is a uniformly integrable martin-
gale. Then the following bound is true:
P(N T ≥λ) ≤P(N Tµ ≥λ) = µ(Ψ −1
µ (λ)),
λ ≥0,
(5.6)
where Tµ is given in Proposition 5.2, Ψµ is displayed in (5.3) and its inverse
is taken right-continuous.

On Brownian Motion and its Supremum
527
In other words, for the partial order given by tails domination, the law of
N T is bounded by the image of µ through the Hardy–Littlewood maximal
function (5.3).
Proof. Suppose for simplicity that µ has a positive density, which is equiv-
alent to Ψµ being continuous and strictly increasing. We consider the max-
martingale (4.3) for f(x) = 1(x≥λ), for some fixed λ > 0, and apply the
optional stopping theorem. We obtain:
λP(N T ≥λ) = E
)
NT 1(N T ≥λ)

,
(5.7)
that is Doob’s maximal equality for continuous-time martingales. Let p :=
P(N T ≥λ). As NT ∼µ, then the RHS is smaller than E[NT 1(NT ≥µ−1(p))]
which, by definition in (5.3), is equal to pΨµ(µ−1(p)). We obtain therefore:
λP(N T ≥λ) = λp ≤E
)
NT 1(NT ≥µ−1(p))

= pΨµ

µ−1(p)

,
hence
λ ≤Ψµ

µ−1(p)

,
thus
p ≤µ

Ψ −1
µ (λ)

since µ is decreasing.
(5.8)
To end the proof is suffice to note that P(BTµ ≥λ) = µ(Ψ −1
µ (λ)), which is
obvious from the definition of Tµ.
✷
Investigation of similar quantities with N T replaced by T is also possible.
Numerous authors studied the limit
√
λP(T ≥λ). It goes back to Az´ema,
Gundy and Yor [1] with more recent works by Elworthy, Li and Yor [10] and
Peskir and Shiryaev [21]4.
Integrating (5.6) one obtains bounds on the expectation of N T . Another
bound on EN T can be obtained using the max-martingales. Take f(x) = 2x,
then by (4.3) the process N 2
t −2N tNt = (N t−Nt)2−N 2
t is a local martingale.
For a stopping time T with E⟨N⟩T < ∞, we have then E(N T −NT )2 = EN 2
T ,
which yields:
EN T = E(N T −NT ) ≤
H
E(N T −NT )2 =
H
EN 2
T

E⟨N⟩T .
(5.9)
The inequality EN T ≤

E⟨N⟩T extends to any stopping time, through the
monotone convergence theorem. This inequality was generalized for Bessel
processes by Dubins, Shepp and Shiryaev [9] and for Brownian motion with
drift by Peskir and Shiryaev [22]. These problems are also in close relation with
the so-called Russian options developed mainly by L. Shepp and A. Shiryaev
[29, 30, 31].
More elaborate arguments, using optimal stopping, yield:
E
)
sup
s≤T
|Ns|

≤

2E⟨N⟩T ,
(5.10)
4See also the note by Liptser and Novikov in this volume.

528
Jan Ob^l´oj and Marc Yor
as shown in Dubins and Schwarz [8]. We also learned from L. Dubins [6] that
E
)
sup
s≤T
Ns −inf
s≤T Ns

≤

3E⟨N⟩T ,
(5.11)
and in (5.9), (5.10) and (5.11) the constants are optimal.
Bounds on the law of the local time similar to (5.6) were studied in detail
by Vallois [34]. He showed that the law of the local time of a uniformly in-
tegrable continuous martingale with a fixed terminal distribution is bounded
from above and below in the convex order. Vallois [34] also gave explicit con-
structions which realize the upper and lower bounds.
We derive now a complement to the study of Vallois [34]. Namely, we examine
the possible laws of the local time, when the distribution of the absolute value
of the terminal value of a martingale is fixed. We follow the same approach
as above, only starting with the martingales given in Corollary 4.1.
Proposition 5.5. Let m be a probability on R+ with
 ∞
0
xdm(x) < ∞, and
let T be a stopping time, such that |NT | ∼m and (Nt∧T : t ≥0) is a uniformly
integrable martingale. Denote ρT the law of LN
T . Then the following bound is
true
E
)
LN
T −ρ−1
T (p)
+
≤E
)
LN
T m −ρ−1
T m(p∗)
+
,
p ∈[0, 1],
(5.12)
where T m is given in Proposition 5.3, the inverses ρ−1
·
are taken left-
continuous and p∗= m

m−1(p)

≥p.
Remarks. It follows from (5.14) in our proof that the RHS of (5.12) is inde-
pendent of N and equal to
 ∞
m−1(p) xdm(x).
For m with no atoms, p∗≡p. In other words, for m with no atoms, we have
ρT ⪯ρT m, where ρT m is the image of m through the dual Hardy–Littlewood
function ψm, and “⪯” indicates the excess wealth order, defined through
ρ1 ⪯ρ2 ⇔∀p ∈[0, 1]

[ρ1−1(p),∞)
xdρ1(x) ≤

[ρ2−1(p),∞)
xdρ2(x).
(5.13)
We point out that the excess wealth order, was introduced recently by
Shaked and Shanthikumar in [28] (it is also called the right-spread or-
der, cf. Fernandez-Ponce et al. [11]) and studied in Kochar et al. [15], and
the above justifies some further investigation. Since in our case we have
ELT = ELT m =
 ∞
0
xdm(x), the excess wealth order is equivalent to the
TTT and NBUE orders and implies the convex order (see Kochar et al. [15]).
We recall that Vallois [34] showed that when the law of NT is fixed,
NT ∼µ, then the law of LT is bounded in the convex ordering of proba-
bility measures and he gave an explicit construction of the stopping time T µ
V
which realizes the upper bound. If we associate with m its symmetric exten-
sion on R defined via µm(x) = m(x)/2, x ≥0, then we have NT m ∼µm and

On Brownian Motion and its Supremum
529
our stopping time T m coincides with the stopping time of Vallois, T m = T µm
V .
However, typically, there exist many measures µ on R such that if X ∼µ then
|X| ∼m. In consequence, our result which states that under |NT | ∼m, T m
maximizes the law of LT in the excess wealth order and hence in the convex
order, complements the result of Vallois [34].
Proof. Our proof relies on the martingales given in (4.9). Assertion (5.12) is
trivial for p = 1. It holds also for p = 0, as it just means that ELN
T = ELN
T m,
which is true, as both quantities are equal to
 ∞
0
xdm(x). This follows from
the fact that (LN
t −|Nt| : t ≥0) is a local martingale and ELN
T ∧Rn ր ELT
by monotone convergence, and E|NT ∧Rn| →E|NT | by uniform integrability
of (NT ∧t : t ≥0), where Rn is a localizing sequence for LN −|N|.
Take p ∈(0, 1), z = ρ−1
T (p) and put g(x) = 1(x>z). Using the optional
stopping theorem for the martingale in (4.9), we obtain:
E
)
LN
T −z
+
= E
)
|NT |1(LN
T >z)

,
hence
(5.14)
E
)
LN
T −z
+
≤E
)
|NT |1(|NT |≥m−1(p))

= E
)
|NT m|1(ϕm(LN
T m)≥m−1(p))

= E
)
|NT m|1(LN
T m≥ρ−1
T m(p∗))

= E
)
LN
T m −ρ−1
T m(p∗)
+
,
which ends the proof.
✷
5.3 Penalizations of Brownian motion with a function of its
supremum
We sketch here yet another instance, where the MM-harmonic functions play
a natural role.
Let f : R+ →R+ denote a probability density on R+, and consider the
family of probabilities (Wf
t : t ≥0) on Ω= C(R+, R), where Xt(ω) = ω(t),
and Fs = σ(Xu : u ≤s), F∞= .
s≥0 Fs, which are defined by:
Wf
t =
f(Xt)
EW
)
f(Xt)
 · W,
(5.15)
where W denotes the Wiener measure. Roynette, Vallois and Yor [27, 26]
show that
Wf
t
(w)
−−−→
t→∞Wf
∞,
i.e.: ∀s > 0, ∀Γs ∈Fs, Wf
t (Γs) −−−→
t→∞Wf
∞(Γs), (5.16)
where the probability Wf
∞may be described as follows: for s > 0 and Γs ∈Fs,
Wf
∞(Γs) = EW

1ΓsSf
s ),
where
Sf
s = 1 −F(Xs) + f(Xs)(Xs −Xs) = 1 −
 s
0
f(Xu)dXu. (5.17)

530
Jan Ob^l´oj and Marc Yor
We recognize instantly in the process Sf the max-martingale given by
(4.3). Another description of Wf
∞is that, under this measure the process Xt
satisfies:
Xt = Xf
t −
 t
0
f(Xu)du
1 −F(Xu) + f(Xu)(Xu −Xu),
(5.18)
where Xf is a Wf
∞-Brownian motion, and F(x) =
 x
0 f(u)du. Naturally, we
see the max-martingales (4.3) intervene again. Further descriptions of Wf
∞
are given in Roynette, Vallois and Yor [26].
6 A more general viewpoint: the balayage formula
To end this paper, we propose a slightly more general viewpoint on results
mentioned sofar. In order to present the (B, B)-harmonic functions (4.2), we
relied on Itˆo’s formula. However, it is possible to obtain these functions (and
the corresponding martingales) as a consequence of the so-called balayage
formula (see, e.g. Revuz and Yor [24] pp. 260-264 and a series of papers in
[5]).
Let (Σt : t ≥0) denote a continuous semimartingale, with Σ0 = 0, and
define gt = sup{s ≤t :
Σs = 0}, dt = inf{s > t :
Σs = 0}. Then, the
balayage formula is: for any locally bounded predictable process (ku : u ≥0),
one has:
kgtΣt =
 t
0
kgsdΣs,
t ≥0.
(6.1)
The intuitive meaning of this formula is that a “global multiplication” of Σ
over its excursions away from 0 coincides with the stochastic integral of the
multiplicator with respect to (dΣs). As applications, we give some examples:
•
for Σt = N t −Nt and ku = f(N u), f a locally integrable function, (6.1)
reads f(N t)(N t −Nt) =
 t
0 f(N s)d(N s −Ns), which yields (4.3);
•
for Σt = Nt and ku = f(LN
u ), f a locally integrable function, we obtain
f(LN
t )Nt =
 t
0 f(LN
s )dNs;
•
for Σt
=
|N|t and ku
=
f(LN
u ), f a locally integrable function,
we obtain f(LN
t )|Nt|
=
 t
0 f(LN
s )d|Ns|. This in turn is equal to
 t
0 f(LN
s )sgn(Ns)dNs −F(LN
t ) by Itˆo–Tanaka’s formula, and so we ob-
tain (4.9).
7 Closing remarks
Max-martingales, or max-harmonic functions, described in (4.2) and (4.3),
occur in a number of studies of either Brownian motion, or martingales. They
often lead to simple calculations, and/or formulae, mainly due to the (obvious,

On Brownian Motion and its Supremum
531
but crucial) fact that dN t is carried by {t : Nt = N t}. This has been used
again and again by a number of researchers, e.g: Hobson and co-workers, and,
of course, Albert Shiryaev and co-workers. We tried to present in this article
several such instances. More generally, this leads to a “first order stochastic
calculus”, as in Section 6, which is quite elementary in comparison with Itˆo’s
second order calculus.
References
1. Az´ema, J., Gundy, R. F. and Yor, M.: Sur l’int´egrabilit´e uniforme des martin-
gales continues. In Seminar on Probability, XIV (Paris, 1978/1979) (French),
volume 784 of Lecture Notes in Math., pages 53–61. Springer, Berlin, 1980.
2. Az´ema, J. and Yor, M.: Le probl`eme de Skorokhod: compl´ements `a “Une solution
simple au probl`eme de Skorokhod”. In S´eminaire de Probabilit´es, XIII, volume
721 of Lecture Notes in Math., pages 625–633. Springer, Berlin, 1979.
3. Az´ema, J. and Yor, M.: Une solution simple au probl`eme de Skorokhod. In
S´eminaire de Probabilit´es, XIII, volume 721 of Lecture Notes in Math., pages
90–115. Springer, Berlin, 1979.
4. Blackwell, D. and Dubins,L. E.:
A converse to the dominated convergence
theorem. Illinois J. Math., 7:508–514, 1963.
5. Dellacherie, C. and Weil, M. (editors):
S´eminaire de Probabilit´es. XIII, vol-
ume 721 of Lecture Notes in Mathematics. Springer, Berlin, 1979. Held at the
Universit´e de Strasbourg, Strasbourg, 1977/78.
6. Dubins, L. E.: Personal communication with M. Yor. 2004.
7. L. E. Dubins and D. Gilat. On the distribution of maxima of martingales. Proc.
Amer. Math. Soc., 68(3):337–338, 1978.
8. Dubins, L. E. and Schwarz, G.:
A sharp inequality for sub-martingales and
stopping-times. Ast´erisque, (157-158):129–145, 1988. Colloque Paul L´evy sur
les Processus Stochastiques (Palaiseau, 1987).
9. Dubins, L. E., Shepp, L. A. and Shiryaev, A. N.:
Optimal stopping rules
and maximal inequalities for Bessel processes. Teor. Veroyatnost. i Primenen.,
38(2):288–330, 1993.
10. Elworthy, K. D., Li, X. M. and Yor, M.: On the tails of the supremum and the
quadratic variation of strictly local martingales. In S´eminaire de Probabilit´es,
XXXI, volume 1655 of Lecture Notes in Math., pages 113–125. Springer, Berlin,
1997.
11. Fernandez-Ponce, J. M., Kochar, S. C. and Mu˜noz-Perez, J.: Partial orderings of
distributions based on right-spread functions. J. Appl. Probab., 35(1):221–228,
1998.
12. Garsia, A. M.:
Martingale Inequalities: Seminar Notes on Recent Progress.
W.A. Benjamin, Inc., Reading, Mass.-London-Amsterdam, 1973. Mathemat-
ics Lecture Notes Series.
13. Hobson, D. G.:
The maximum maximum of a martingale.
In S´eminaire de
Probabilit´es, XXXII, volume 1686 of Lecture Notes in Math., pages 250–263.
Springer, Berlin, 1998.
14. Kertz, R. P. and R¨osler, U.:
Martingales with given maxima and terminal
distributions. Israel J. Math., 69(2):173–192, 1990.

532
Jan Ob^l´oj and Marc Yor
15. Kochar, S. C., Li, X. and Shaked, M.: The total time on test transform and
the excess wealth stochastic orders of distributions.
Adv. in Appl. Probab.,
34(4):826–845, 2002.
16. Lehoczky, J. P.: Formulas for stopped diffusion processes with stopping times
based on the maximum. Ann. Probability, 5(4):601–607, 1977.
17. Neveu, J.: Discrete-parameter Martingales. North-Holland Publishing Co., Am-
sterdam, revised edition, 1975.
Translated from the French by T. P. Speed,
North-Holland Mathematical Library, Vol. 10.
18. Ob^l´oj, J.:
The Skorokhod embedding problem and its offspring.
Probability
Surveys, 1:321–392, 2004.
19. Ob^l´oj, J.: A complete characterization of local martingales which are functions of
Brownian motion and its supremum. Technical Report 984, LPMA - University
of Paris 6, 2005. ArXiv: math.PR/0504462.
20. Ob^l´oj, J. and Yor, M.: An explicit Skorokhod embedding for the age of Brownian
excursions and Az´ema martingale.
Stochastic Process. Appl., 110(1):83–110,
2004.
21. Pe˘skir, G. and Shiryaev, A. N.:
On the Brownian first-passage time over a
one-sided stochastic boundary. Teor. Veroyatnost. i Primenen., 42(3):591–602,
1997.
22. Peskir, G. and Shiryaev, A. N.: Maximal inequalities for reflected Brownian
motion with drift. Teor. Imovir. Mat. Stat., (63):125–131, 2000.
23. Pierre, M:
Le probl`eme de Skorokhod: une remarque sur la d´emonstration
d’Az´ema-Yor. In S´eminaire de Probabilit´es, XIV (Paris, 1978/1979) (French),
volume 784 of Lecture Notes in Math., pages 392–396. Springer, Berlin, 1980.
24. Revuz, D. and Yor, M.: Continuous Martingales and Brownian Motion, volume
293 of Grundlehren der Mathematischen Wissenschaften [Fundamental Princi-
ples of Mathematical Sciences]. Springer-Verlag, Berlin, third edition, 1999.
25. Rogers, L. C. G.: The joint law of the maximum and terminal value of a mar-
tingale. Probab. Theory Related Fields, 95(4):451–466, 1993.
26. Roynette, B., Vallois, P. and Yor, M.: Limiting laws associated with brown-
ian motion perturbed by its maximum, minimum and local time II. Technical
Report 51, Institut Elie Cartan, 2004. to appear in Studia Sci. Math. Hungar.
27. Roynette, B., Vallois, P. and Yor, M.: P´enalisations et extensions du th´eor`eme de
Pitman, relatives au mouvement brownien et `a son maximum unilat`ere. Techni-
cal Report 31, Institut Elie Cartan, 2004. To appear in S´eminaire de Probabilit´es
XXXIX, Lecture Notes in Math., Springer, 2005.
28. Shaked, M. and Shanthikumar, J. G.: Two variability orders. Probab. Engrg.
Inform. Sci., 12(1):1–23, 1998.
29. Shepp, L. and Shiryaev, A. N.: The Russian option: reduced regret. Ann. Appl.
Probab., 3(3):631–640, 1993.
30. Shepp, L. A. and Shiryaev, A. N.: A new look at the “Russian option”. Teor.
Veroyatnost. i Primenen., 39(1):130–149, 1994.
31. L. A. Shepp and A. N. Shiryaev.:
The Russian option under conditions of
possible “freezing” of prices. Uspekhi Mat. Nauk, 56(1(337)):187–188, 2001.
32. Tsirel′son, B. S.: An example of a stochastic differential equation that has no
strong solution. Teor. Verojatnost. i Primenen., 20(2):427–430, 1975.
33. Vallois, P.: Le probl`eme de Skorokhod sur R: une approche avec le temps local.
In S´eminaire de Probabilit´es, XVII, volume 986 of Lecture Notes in Math., pages
227–239. Springer, Berlin, 1983.

On Brownian Motion and its Supremum
533
34. Vallois, P.: Quelques in´egalit´es avec le temps local en zero du mouvement brown-
ien. Stochastic Process. Appl., 41(1):117–155, 1992.
35. Vallois, P.: Sur la loi du maximum et du temps local d’une martingale continue
uniformement int´egrable. Proc. London Math. Soc. (3), 69(2):399–427, 1994.
36. Williams, D.:
Probability with martingales.
Cambridge Mathematical Text-
books. Cambridge University Press, Cambridge, 1991.
37. Yor, M.: De nouveaux r´esultats sur l’´equation de Tsirel′son. C. R. Acad. Sci.
Paris S´er. I Math., 309(7):511–514, 1989.
38. Yor, M.: Tsirel′son’s equation in discrete time. Probab. Theory Related Fields,
91(2):135–152, 1992.


On the Fundamental Solution of the
Kolmogorov–Shiryaev Equation
Goran PESKIR ∗
Department of Mathematical Sciences, University of Aarhus,
Ny Munkegade, 8000 Aarhus, Denmark.
goran@maths.manchester.ac.uk
Summary. We derive an integral representation for the fundamental solution of
the Kolmogorov forward equation
ft = −((1+µx)f)x + (ν x2f)xx
associated with the Shiryaev process X solving the linear SDE
dXt = (1+µXt) dt + σXt dBt
where µ ∈IR, ν = σ2/2 > 0 and B is a standard Brownian motion. The method of
proof is based upon deriving and inverting a Laplace transform. Basic properties of
X needed in the proof are reviewed.
Key words: Shiryaev process, Kolmogorov forward equation, integral of geometric
Brownian motion, parabolic partial differential equation, Laplace transform, conflu-
ent hypergeometric function, modified Bessel function, Hartman–Watson distribu-
tion, Hankel’s contour integral.
Mathematics Subject Classification (2000): 60J60, 35K15, 60J65, 35C15
1 Introduction
We consider the Kolmogorov forward equation:
ft = −((1+µx)f)x + (ν x2f)xx
(1.1)
associated with the Shiryaev process X = (Xt)t≥0 solving:
∗Network in Mathematical Physics and Stochastics (funded by the Danish Na-
tional Research Foundation) and Centre for Analytical Finance (funded by the Dan-
ish Social Science Research Council).

536
G. Peskir
dXt = (1+µXt) dt + σXt dBt
(1.2)
with X0 = x0 in IR where µ ∈IR, ν = σ2/2 > 0 and B = (Bt)t≥0 is a
standard Brownian motion. The problem of finding the fundamental solution
f = f(t, x) of (1.1) appears naturally in a number of fields (most notably in
sequential analysis and financial mathematics).
The unique (strong) solution of (1.2) is given by:
Xt = Yt

x0 +
 t
0
1
Ys
ds

(1.3)
where Y = (Yt)t≥0 is a geometric Brownian motion solving:
dYt = µYt dt + σYt dBt
(1.4)
with Y0 = 1. The unique (strong) solution of (1.4) is given by:
Yt = exp

σBt + (µ−ν)t

.
(1.5)
Inserting (1.5) into (1.3) one obtains an explicit representation of X in terms
of B.
From this representation and the invariance of B on time reversal one sees
that the following identity in law is satisfied:
Xt
law
=
 t
0
Ys ds
(1.6)
when x0 = 0. This shows that the problem of finding the fundamental solution
of (1.1) when x0 = 0 is equivalent to the problem of finding the distribution of
the random variable
 t
0 Ys ds. The latter problem has been intensively studied
in the last 10-15 years (see [20], [4], [15] and the references therein) but none
of these approaches attempts to tackle the forward equation (1.1) directly (see
[14] for numerical results of a related approach).
The purpose of the present paper is to search for the fundamental so-
lution of (1.1) by simple probabilistic and analytic means (cf. [5]). It will
be seen below that this approach readily leads to the Laplace transform of
t →
 x
0 f(t, y) dy expressed in terms of confluent hypergeometric functions
(modified Bessel functions) providing a link to the Hartman-Watson distrib-
ution [9]. The problem thus reduces to inverting the Laplace transform. This
can be done using Hankel’s contour integrals for these functions (cf.[19]) lead-
ing to representations of the solution in terms of single or double integrals.
For simplicity and comparison we only treat a particular case of the equation
(1.1) in complete detail. A treatment of other cases is briefly indicated and it
is hoped that their study will be continued.
A disadvantage of the previous inversion approach is that the analytic
expressions obtained are numerically unstable for small t. This fact was ob-
served independently by several authors (see e.g. [2]). While this may not be

The Kolmogorov–Shiryaev Equation
537
such a big drawback for applications to Asian options of European type (cf.
[3]), in the case of Asian options of American type such a numerical stability
becomes fundamentally important (see [13]). A similar need for stable analytic
expressions arises in quickest detection problems (sequential analysis) when
the horizon is finite (see [8]). Further research of the Kolmogorov–Shiryaev
equation (1.1) thus appears to be necessary.
The stochastic differential equation (1.2) has been derived by Shiryaev
[16, Eq. (9)] in the context of quickest detection problems (sequential analy-
sis). These problems play a prominent role in diverse applications ranging
from quality control in industry to structural analysis of DNA in medicine.
Applications in financial data analysis (detection of arbitrage) are recently
discussed in [17]. The Kolmogorov backward and forward equation (of which
(1.1) is a particular case) have been derived in [11]. In the physical literature
the forward equation is often referred to as the Fokker–Planck equation (cf.
[7], [12]).
2 The Shiryaev process
In this section we present basic properties of the Shiryaev process X solving
(1.2). Note that the initial point x0 of X belongs to IR and may be negative
as well.
1. The Shiryaev process X is a strong Markov process with continuous
sample paths (a diffusion process). The drift of X is given by µ(x) = 1 −µx
and the diffusion coefficient of X is given by σ(x) = σx. Recall that µ ∈IR
and ν = σ2/2 > 0.
2. Since σ(0) = 0 we see that the state space of X splits into (−∞, 0] and
[0, ∞). From the representation (1.3) it is evident that:
The point 0 is an entrance boundary point for [0, ∞).
(2.1)
Likewise it will be formally verified below that:
The point 0 is an exit boundary point for (−∞, 0].
(2.2)
3. The scale function of X is given by:
s(x) =
 x
1
z−µ/ν e1/νz dz
for x > 0
(2.3)
s(x) =
 1
−x
z−µ/ν e−1/νz dz
for x < 0.
(2.4)
Hence s(0+) = −∞always, and s(∞) = ∞if and only if µ ≤ν. This shows
that X is recurrent in [0, ∞) if and only if µ ≤ν. Note also that s(−∞) = −∞
if and only if µ ≤ν, and s(0−) < ∞always. This shows that X exists (−∞, 0]

538
G. Peskir
almost surely at 0 if and only if µ ≤ν. We also see that X can never be
recurrent in (−∞, 0].
4. The speed measure of X is given by:
m(dx) = ν−1 x−2+µ/ν e−1/νx dx
for x > 0
(2.5)
m(dx) = ν−1 (−x)−2+µ/ν e−1/νx dx
for x < 0.
(2.6)
Since
 ∞
0
m(dx) = νµ/ν Γ(1−µ/ν) < ∞if and only if µ < ν, it follows that
X has an invariant density function on [0, ∞) given by:
f(x) =
1
ν1−µ/ν Γ(1−µ/ν)
1
x2−µ/ν e−1/νx
for x > 0
(2.7)
if and only if µ < ν. Noting that
 0
−∞m(dx) = ∞we see that X cannot have
an invariant density function on (−∞, 0] as already indicated above.
5. By the law of iterated logarithm for B one easily sees that
 ∞
0
Ys ds < ∞
almost surely if and only if µ < ν. Hence when µ < ν we find using (1.3) and
(1.6) that:
Xt
d
−→
 ∞
0
Ys ds
(2.8)
as t →∞where the density function of
 ∞
0
Ys ds is given by (2.7) above.
Likewise one sees that
 ∞
0 (1/Ys) ds < ∞almost surely if and only if µ > ν.
Hence when µ > ν we find using (1.3) that:
Xt →+∞
if
x0 +
 ∞
0 (1/Ys) ds > 0
(2.9)
Xt →−∞
if
x0 +
 ∞
0 (1/Ys) ds < 0
(2.10)
as t →∞. The probabilities of the latter two events can readily be computed
upon noting that the density function of
 ∞
0 (1/Ys) ds is given by:
g(x) =
1
νµ/ν−1 Γ(µ/ν−1)
1
xµ/ν e−1/νx
for x > 0
(2.11)
when µ > ν. This follows from the identity in law stated after (2.8) above
with a new drift ˆµ = 2ν −µ and a new Brownian motion ˆB = −B. Another
way to compute these probabilities is to make use of the scale function in
(2.4). This gives that the probability of the event in (2.9) equals one minus
the probability of the event in (2.10) which, in turn, is equal to the ratio
(S(0−)−S(x0))/(S(0−)−S(−∞)).
Finally, when µ = ν then X is recurrent in [0, ∞) no matter if x0 is positive
or negative. Recall that X hits zero almost surely if x0 < 0 never returning
to zero again.
6. A formal verification of (2.1) and (2.2) can be made upon invoking
the standard boundary classification for one-dimensional diffusions (cf. [6]).

The Kolmogorov–Shiryaev Equation
539
Firstly, since m′ ∈L1((0, ∞)) and s m′ ∈L1((0, ∞)) but s′ /∈L1((0, ∞))
we see that (2.1) follows. Secondly, since m′ /∈L1((−∞, 0)) and s′m ∈
L1((−∞, 0)) we see that (2.2) follows as claimed.
7. We will conclude this section by deriving boundary conditions which will
be used in the next section. For this, let F denote the transition distribution
function of X, and let f denote the transition density function of X. Since X
is a time-homogeneous Markov process, it is no restriction to assume that the
initial time point equals zero. We thus have:
F(0, x0; t, x) = P(Xt ≤x | X0 = x0)
(2.12)
f(0, x0; t, x) = Fx(0, x0; t, x).
(2.13)
In the sequel we will only study the case when x0 ≥0. From the facts
exposed above we then know that the state space of X equals [0, ∞) and
that X can only start at 0 and never arrive at it (recall (2.1) above). Hence
the following boundary conditions at 0 are in agreement with what we would
expect to hold:
f(0, x0; t, 0+) = 0
(2.14)
fx(0, x0; t, 0+) = 0.
(2.15)
In fact, all higher derivatives of f with respect to x satisfy the same zero
condition, but we will only make use of the conditions (2.14) and (2.15) below.
8. A formal proof of (2.14) and (2.15) is simple. Denote Xt from (1.3) by
Xx0
t
to indicate its dependence on x0, note that Xx0
t
> 0, and set Z = 1/Xx0
t .
Then for any p > 0 given and fixed we find by the Markov inequality that:
F(0, x0; t, h) = P(Xt ≤h | X0 = x0) = P(Xx0
t
≤h)
(2.16)
= P(Z ≥1/h) = P(Zp ≥1/hp) ≤hp E(Zp)
where E(Zp) < ∞by the well-known properties of B. From (2.16) we see that:
F(0, x0; t, h) = O(hp)
(2.17)
as h →h0 for h0 ≥0 whenever p > 0 is given and fixed. Taking p = 3 and
using (2.17) one finds that (2.14) and (2.15) hold as claimed.
3 The fundamental solution
In this section we study the problem of finding the fundamental solution of
the Kolmogorov–Shiryaev equation (1.1). For simplicity we will only examine
the case when x0 ≥0 (cf. Section 2). By the fundamental solution we thus
mean a non-negative solution f = f(t, x) for t > 0 and x > 0, satisfying
 ∞
0
f(t, x) dx = 1 for each t > 0, and f(t, x) →δ(x−x0) weakly as t ↓0
(where δ denotes the Dirac delta function).

540
G. Peskir
1. Recall that X solving (1.2) is time-homogeneous so that there is no
restriction to assume that the initial time point equals zero. We will moreover
suppress the dependence on 0 and x0 in (2.12) and (2.13) and simply write:
F(t, x) = P(Xt ≤x | X0 = x0)
(3.1)
f(t, x) = Fx(t, x).
(3.2)
Standard Markovian arguments (cf. [11]) imply that the transition density
function (3.2) solves the equation (1.1), and thus the initial problem is equiv-
alent to the problem of finding the transition density function (3.2).
2. Let us set:
g = −(1+µx)f + (ν x2f)x.
(3.3)
Then (1.1) can be written as:
ft = gx.
(3.4)
In view of taking the Laplace transform with respect to t and making use of
the initial condition for t = 0 we shall integrate both sides of (3.4) from 0 to
x upon using that:
F(t, x) =
 x
0
f(t, y) dy.
(3.5)
Since g(t, 0+) = 0 by (2.14) and (2.15) this gives:
Ft = g(t, x) −g(t, 0+) = g(t, x) = −(1+µx)f + (ν x2f)x
(3.6)
= −(1+µx)Fx + (ν x2Fx)x = ((2ν−µ)x−1)Fx + ν x2Fxx.
Setting α = 2ν−µ we see that (3.6) reads:
Ft = (αx−1)Fx + ν x2Fxx.
(3.7)
3. To simplify technicalities we will assume that x0 = 0 in the sequel. Then
F satisfies the following initial condition:
F(0, x) = 1
(3.8)
for all x ≥0. Moreover, since Xt remains positive almost surely for all t > 0,
we see that F satisfy the following boundary conditions:
F(t, 0+) = 0
(3.9)
F(t, ∞) = 1
(3.10)
for all t > 0.
4. Taking the Laplace transform in (3.7) with respect to t upon setting:
¯F(λ, x) =
 ∞
0
e−λtF(t, x) dt
(3.11)

The Kolmogorov–Shiryaev Equation
541
we obtain the following ordinary differential equation:
λ ¯F −F(0, x) = (αx−1) ¯Fx + ν x2 ¯Fxx.
(3.12)
(Note that by taking the Laplace transform with respect to x, we would
arrive instead to a new second-order partial differential equation. This is in
sharp contrast with the equation studied in [5] where one has x instead of
x2 in (1.1) which makes such a transform profitable since the new partial
differential equation is of the first order.) Making use of (3.8) we see that the
equation (3.12) reads:
ν x2 ¯Fxx + (αx−1) ¯Fx −λ ¯F = −1.
(3.13)
By (3.9) and (3.10) we obtain the following boundary conditions:
¯F(λ, 0+) = 0
(3.14)
¯F(λ, ∞) = 1/λ.
(3.15)
5. Note that a particular solution of the equation (3.13) is given by
¯F ≡1/λ. To find the general solution we need to consider the homogeneous
equation which reads:
x2y′′ + (Ax+B)y′ + C y = 0
(3.16)
where A = α/ν = 2−µ/ν, B = −1/ν and C = −λ/ν. A standard substitution
for this equation (cf. (2.188) in [10, p. 447]) is given by:
y(x) = (1/xp) z(B/x).
(3.17)
Inserting (3.17) into (3.16) one finds that z = z(x) solves the Kummer equa-
tion:
xz′′ + (b −x)z′ −ax = 0
(3.18)
where a and b are given by:
a = p
(3.19)
b = 2(p+1)−A
(3.20)
and p > 0 solves the quadratic equation:
p2 + (1−A)p + C = 0.
(3.21)
Solving (3.21) we find that:
a = 1
2

1 −µ
ν +

1 −µ
ν
2
+ 4λ
ν

(3.22)
b = 1 +

1 −µ
ν
2
+ 4λ
ν .
(3.23)

542
G. Peskir
6. Two linearly independent solutions of the Kummer equation (3.18) are
the confluent hypergeometric function of the first kind:
M(a, b, x) = 1 + a
b x + a(a+1)
b(b+1)
x2
2! + · · ·
(3.24)
and the confluent hypergeometric function of the second kind U(a, b, x). (We
refer to [1, pp. 504-510] for basic properties of these functions.) Summarizing
the preceding facts about (3.16) and (3.17) it follows that the equation (3.13)
has the general solution given by:
¯F(λ, x) = C1 x−a M(a, b, −1/νx) + C2 x−a U(a, b, −1/νx) + 1/λ.
(3.25)
7. Letting x →∞and using that x−a M(a, b, −1/νx) →0 it follows from
(3.15) that we may take C2 = 0. Using the known relation (cf. (13.1.5) in [1,
p. 504]):
xa M(a, b, −x) =
Γ(b)
Γ(b−a)

1 + O(x−1)

(3.26)
as x →∞, we find that:
x−a M(a, b, −1/νx) →νa
Γ(b)
Γ(b−a)
(3.27)
as x ↓0. Hence by (3.14) we get:
C1 = −Γ(b−a)
λ νa Γ(b).
(3.28)
Inserting this into (3.25) upon recalling that C2 = 0, we obtain the following
closed-form expression for the Laplace transform (3.11) above:
¯F(λ, x) = 1
λ

1 −Γ(b−a)
Γ(b)
(νx)−a M(a, b, −1/νx)

(3.29)
where a = a(λ) and b = b(λ) are given by (3.22) and (3.23) respectively.
8. By the inversion formula we have:
F(t, x) =
1
2πi
 c+i∞
c−i∞
etz ¯F(z, x) dz
(3.30)
for any c > 0 given and fixed. The initial problem is thus reduced to com-
puting the complex integral (3.30). The representation (3.29) possesses a rich
structure which opens various ways to tackle the inversion problem. Some of
these possibilities will now be addressed.
9. By the convolution theorem we see that:
F(t, x) = 1 −
 t
0
G(s, x) ds
(3.31)

The Kolmogorov–Shiryaev Equation
543
where the Laplace transform of s →G(s, x) is given by:
¯G(λ, x) =
 ∞
0
e−λs G(s, x) ds = Γ(b−a)
Γ(b)
(νx)−a M(a, b, −1/νx)
(3.32)
upon recalling that a = a(λ) and b = b(λ) are given by (3.22) and (3.23)
respectively. The problem thus reduces to inverting the Laplace transform on
the right-hand side of (3.32).
10. Consider the case when µ = 0 and ν = 1/2 i.e. σ = 1. Then from (3.22)
and (3.23) we see that a = (1/2)(1+
√
1+8λ) and b = 2a so that:
¯G(λ, x) = Γ(a)
Γ(2a) (x/2)−a M(a, 2a, −2/x).
(3.33)
Using the well-known relation (cf. (13.6.3) in [1, p. 509]):
M(p +1/2, 2p +1, 2z) = Γ(1+p) ez (z/2)−p Ip(z)
(3.34)
where Ip(z) is the modified Bessel function of the first kind (cf. [1, pp. 374-
385]), together with the fact that (−z)−p Ip(−z) = z−p Ip(z) (see (9.6.10) in
[1, p. 375]), and the duplication formula for the gamma function (cf. (6.1.18)
in [1, p. 256]):
Γ(2z) = (2π)−1/2 22z−1/2 Γ(z) Γ(z+1/2)
(3.35)
we find that the following identity holds:
Γ(a)
Γ(2a) (x/2)−a M(a, 2a, −2/x) =

2π
x e−1/x Ia−1/2(1/x).
(3.36)
Inserting this expression into (3.32) we find that:
¯G(λ, x) =

2π
x e−1/x I√
1/4+2λ (1/x).
(3.37)
This provides a link to the Hartman–Watson distribution (cf. [9]).
Since by (3.37) the Laplace transform of s →e−s/4 G(s, x) equals

2π/x
e−1/x I√
2λ (1/x), denoting by L−1
λ [ · ] the inverse Laplace transform in the
argument λ, we see that:
G(s, x) =

2π
x es/4−1/x L−1
λ

I√
2λ (1/x)

(s).
(3.38)
Using the classic Hankel’s contour integral (see [18, Chapter XVII] for more
details):
I√
2λ (y) =
1
2πi

C
ey cosh(z)−(
√
2λ)z dz
(3.39)

544
G. Peskir
for y > 0 and the well-known identity L−1
λ [e−(
√
2λ)x](t) = (2πt3)−1/2 x e−x2/2t
it is possible to perform the inversion in (3.38) by expressing the result in
terms of a single integral (cf. [19, pp. 86-87]):
L−1
λ

I√
2λ (y)

(s) = y eπ2/2s
√
2π3s
 ∞
0
e−z2/2s−y cosh(z) sinh(z) sin
 πz
s

dz. (3.40)
Inserting (3.40) into (3.38) and then (3.38) back into (3.31) we obtain the
following expression for the distribution function (3.1) above:
F(t, x) = 1−
 t
0
es/4+π2/2s−1/x
π√s x3/2
(3.41)
 ∞
0
e−z2/2s−(1/x) cosh(z) sinh(z) sin
 πz
s

dz ds
when µ = 0 and ν = 1/2. Clearly the formula (3.41) extends along the same
lines to the case of general ν > 0 when µ = 0.
11. In the case of general µ ∈IR and ν > 0 we may proceed differently
from (3.34) and exploit the following integral representation (cf.(13.2.1) in [1,
p. 505]):
Γ(b−a)Γ(a)
Γ(b)
M(a, b, z) =
 1
0
ezr ra−1 (1−r)b−a−1 dr.
(3.42)
Hence the right-hand side of (3.32) reads:
¯G(λ, x) = (νx)−a
Γ(a)
 1
0
e−r/νx ra−1 (1−r)b−a−1 dr.
(3.43)
To handle the term 1/Γ(a) recall the Hankel’s contour integral (cf. (6.1.4) in
[1, p. 255]):
1
Γ(a) =
1
2πi

C
ezz−a dz
(3.44)
where the path of integration C starts at −∞on the real axis, circles the origin
in the anticlockwise direction, and returns to the starting point. Inserting
(3.44) into (3.43) and recalling (3.22) and (3.23) we find that:
¯G(λ, x) = (νx)µ/2ν−1/2
 1
0
e−r/νx r−µ/2ν−1/2 (1−r)µ/2ν−1/2 H(r) dr (3.45)
where the function H(r) = H(λ, x, µ, ν, r) is given by:
H(r) =
1
2πi

C
ezzµ/2ν−1/2
(3.46)
exp

−log
 ν xz
r(1−r)
 
1
4 (1−µ/ν)2 + λ/ν

dz.

The Kolmogorov–Shiryaev Equation
545
Recalling the well-known identity:
L−1
λ

e−w√
α+βλ 
(t) =
√β w e−αt/β−βw2/4t
2
√
πt3
(3.47)
that is valid for all complex numbers w = w1 +iw2 such that Re(w) = w1 > 0
and Re(w2) = w2
1 −w2
2 > 0, letting z = reiϕ in (3.46) and choosing C not too
close to the origin in the sense that r ≥R where R > 0 is taken large enough,
we see that it is possible to perform the inversion in (3.45) by expressing the
result in terms of a double integral. A more systematic study of the expressions
obtained appears worthy of further consideration.
References
1. Abramowitz M., Stegun I.A.: Handbook of Mathematical Functions. The Na-
tional Bureau of Standards 1964.
2. Barrieu P., Rouault A., Yor M.: A study of the Hartman–Watson distri-
bution motivated by numerical problems related to Asian options pricing.
Pr´epublication PMA 813, Universit´e Pierre et Marie Curie, Paris (2003).
3. Carr P., Schr¨oder M.: Bessel processes, the integral of geometric Brownian mo-
tion, and Asian options. Theory Probab. Appl. 48, 400–425 (2004).
4. Dufresne D.: The integral of geometric Brownian motion. Adv. Appl. Probab.
33, 223–241 (2001).
5. Feller W.: Two singular diffusion problems. Ann. of Math. 54, 173–182 (1951).
6. Feller W.: The parabolic differential equations and the associated semi-groups
of transformations. Ann. of Math. 55, 468–519 (1952).
7. Fokker A.D.: Die mittlere Energie rotierender elektrischer Dipole im Strahlungs-
feld. Ann. Phys. 43, 810–820 (1914).
8. Gapeev P.V., Peskir G.: The Wiener disorder problem with finite horizon. Re-
search Report No. 435, Dept. Theoret. Statist. Aarhus (2003).
9. Hartman P., Watson G.S.: ”Normal” distribution functions on spheres and the
modified Bessel functions. Ann. Probab. 2, 593–607 (1974).
10. Kamke E.: Differentialgleichungen. Chelsea 1948.
11. Kolmogorov A.N. ¨Uber die analytischen Methoden in der Wahrscheinlichkeit-
srechnung. Math. Ann. 104, 415–458 (1931).
12. Planck M.: ¨Uber einen Satz der statistischen Dynamik and seine Erweiterung
in der Quantentheorie. Sitzungsber. Preuß. Akad. Wiss. 24, 324–341 (1917).
13. Peskir G., Uys N.: On Asian options of American type. Research Report No.
436, Dept. Theoret. Statist. Aarhus (2003).
14. Rogers L.C.G., Shi Z.: The value of an Asian option. J. Appl. Probab. 32, 1077–
1088 (1995).
15. Schr¨oder M.: On the integral of geometric Brownian motion. Adv. Appl. Probab.
35, 159–183 (2003).
16. Shiryaev A.N.: The problem of the most rapid detection of a disturbance in a
stationary process. Soviet Math. Dokl. 2, 795–799 (1961).
17. Shiryaev A.N.: Quickest detection problems in the technical analysis of the fi-
nancial data. Math. Finance Bachelier Congress (Paris 2000), 487–521, Springer
2002.

546
G. Peskir
18. Whittaker E.T., Watson G.N.: A Course of Modern Analysis. Cambridge Univ.
Press 1927.
19. Yor M.: Loi de l’indice du lacet Brownien, et distribution de Hartman–Watson.
Z. Wahrsch. Verw. Gebiete 53, 71–95 (1980).
20. Yor M.: On some exponential functionals of Brownian motion. Adv. Appl.
Probab. 24, 509–531 (1992).

Explicit Solution to an Irreversible Investment
Model with a Stochastic Production Capacity
Huyˆen PHAM
Laboratoire de Probabilit´es et Mod`eles Al´eatoires CNRS, UMR 7599,
Universit´e Paris 7, and CREST, France.
pham@math.jussieu.fr
Summary. This paper studies the problem of a company which expands its sto-
chastic production capacity in irreversible investments by purchasing capital at a
given price. The profit production function is of a very general form satisfying min-
imal standard assumptions. The objective of the company is to find optimal pro-
duction decisions to maximize its expected total net profit in an infinite horizon.
The resulting dynamic programming principle is a singular stochastic control prob-
lem. The value function is analyzed in great detail relying on viscosity solutions of
the associated Bellman variational inequality: we state several general properties
and in particular regularity results on the value function. We provide a complete
solution with explicit expressions of the value function and the optimal control: the
firm invests in capital so as to maintain its capacity above a certain threshold. This
boundary can be computed quite explicitly.
Key words: singular stochastic control, viscosity solutions, Skorohod problem, ir-
reversible investment, production.
Mathematics Subject Classification (2000): 93E20, 60G40, 91B28
1 Introduction
This paper focuses on the problem of a company which wants to expand its
stochastic production capacity. The investments in capital for expanding the
capacity are irreversible in the sense that the company cannot recover the
investment by reducing the capacity. In addition, there is a transaction cost
for purchasing capital. We refer to the book by Dixit and Pindick (1994) for
a review where such problems occur. There are several papers in the litera-
ture dealing with irreversible investments models. For instance, Kobila (1993)
consider a model with deterministic capacity in an uncertain market and with-
out transaction costs on buying capital. Recently, Chiarolla and Haussmann

548
H. Pham
(2003) studied an irreversible investment model in a finite horizon and ob-
tained an explicit solution for a power type production function.
We consider a concave production function of very general form, satisfying
minimal standard assumptions. The buying capital decision is modelled by a
singular control. This allows for instantaneous purchase of capital of arbitrary
large amounts and various other sorts of behavior. The company’s objective is
to maximize the expected net production profit over an infinite horizon, with
choice of control of its buying. The resulting dynamic programming principle
leads to a singular stochastic control problem. There is by now a number of
papers on singular controls related to financial problems, see, e.g., Davis and
Norman (1990) and Jeanblanc-Picqu´e and Shiryaev (1995).
We solve mathematically this problem by a viscosity solution approach.
This contrasts with the classical approach on investment models where the
principal activity is to construct by ad hoc methods a solution to the
Hamilton–Jacobi–Bellman equation, and validate the optimality of the so-
lution by a verification theorem argument for smooth functions. We, on the
other hand, start by studying and deriving the general properties via the dy-
namic programming principle and viscosity arguments. Using the concavity
property of the value function, we prove that it satisfies in fact the HJB in
the classical C2-sense. Similar approach is done in the paper by Shreve and
Soner (1994) for optimal consumption models with transaction costs.
The rest of the paper goes as follows. In the next section, we give a math-
ematical formulation of the problem. We analyze and derive some general
properties of the value function in Section 3. By means of viscosity solutions
arguments, we state in Section 4 the C2-smoothness of the value function
that satisfies then in a classical sense the associated HJB equation. Section 5
is devoted to the explicit construction of the solution to this singular control
problem and the optimal control.
2 Formulation of the problem
Let (Ω, F, P) be a complete probability space equipped with a filtra-
tion (Ft)t≥0 satisfying the usual conditions, and carrying a standard one-
dimensional Brownian motion W.
We consider a firm producing some output from stochastic capacity pro-
duction Kt and possibly also from other inputs. The firm can buy capital
at any time t at constant price p > 0. The production rate process is then
described by a control L ∈A, set of right-continuous with left-hand limits
adapted processes, nonnegative and nondecreasing, with L0−= 0. Here, Lt
represents the cumulative purchase of capital until time t. Given the initial
capital k ≥0, and control L ∈A, the firm’s capacity production evolves
according to the linear SDE
dKt = Kt (−δdt + γdWt) + dLt,
K0−= k.
(2.1)

Explicit Solution to an Irreversible Investment Model
549
Here δ ≥0 is the depreciation rate of the capacity production and γ > 0
represents its volatility.
The instantaneous operating profit of the firm is a function Π(Kt) of
the capacity production. The production profit function Π is assumed to be
continuous on R+, nondecreasing, concave and C1 on (0, ∞), with Π(0) = 0
and satisfying the standing usual Inada conditions :
Π′(0+) := lim
k↓0 Π′(k) = ∞and Π′(∞) :=
lim
k→∞Π′(k) = 0.
(2.2)
We define the Fenchel–Legendre transform of Π, which is finite on (0, ∞)
under the Inada conditions:
˜Π(z) := sup
k≥0
[Π(k) −kz] < ∞,
∀z > 0.
(2.3)
A typical example arising from the Cobb–Douglas production function leads
to a profit function of the form
Π(k) = Ckα,
with C > 0, 0 < α < 1.
(2.4)
The firm’s objective is to maximize the expected profit on the infinite time
horizon
J(k, L) = E
 ∞
0
e−rt (Π(Kt)dt −pdLt)

(2.5)
over all controls L ∈A. Here r > 0 is a fixed positive discount factor. Without
loss of generality, one may consider the strategies L in A for which
E
 ∞
0
e−rtdLt

< ∞,
(2.6)
Accordingly, we define the value function
v(k) = sup
L∈A
J(k, L),
k ≥0.
(2.7)
Notice that since J(k, 0) ≥0, the value function v takes value in [0, ∞].
3 Some properties of the value function
Problem (2.7) is a singular stochastic control problem and its associated
Hamilton–Jacobi–Bellman equation is
min {rv −Lv −Π , −v′ + p} = 0,
(3.1)
where L is the second order operator

550
H. Pham
Lϕ = 1
2γ2k2ϕ′′ −δkϕ′
for any C2-function ϕ.
We first state a standard comparison theorem, which says that any smooth
function, being a supersolution of the HJB equation (3.1), dominates v.
To this end, we first recall in our context how Itˆo’s formula for c`adl`ag
semimartingales (see, e.g., [8]) is written. Let ϕ ∈C2(0, ∞) and let τ be a
finite stopping time, k > 0 and L ∈A. Then, we have:
e−rτϕ(Kτ) = ϕ(k) +
 τ
0
e−rt (−rϕ + Lϕ) (Kt)dt +
 τ
0
e−rtγKtϕ′(Kt)dWt
+
 τ
0
e−rtϕ′(Kt)dLc
t +

0≤t≤τ
e−rt [ϕ(Kt) −ϕ(Kt−)] ,
(3.2)
where
Lc
t = Lt −

0≤s≤t
∆Ls,
is the continuous part of L.
Proposition 3.1. Let ϕ be a nonnegative C2-function which is a supersolu-
tion on (0, ∞) to (3.1), i.e.:
min {rϕ −Lϕ −Π(k) , −ϕ′ + p} ≥0,
k > 0.
(3.3)
Then,
v(k) ≤ϕ(k),
∀k > 0.
Proof. For L ∈A define the stopping time τn = inf{t ≥0 : Kt ≥n} ∧n
and apply Itˆo’s formula (3.2) between 0 and τn. Then, taking expectation and
noting that the integrand in the stochastic integral is bounded on [0, τn), we
get that
E

e−rτnϕ(Kτn)

= ϕ(k) + E
 τn
0
e−rt (−rϕ + Lϕ) (Kt)dt

+ E
 τn
0
e−rtϕ′(Kt)dLc
t

+ E


0≤t≤τn
e−rt [ϕ(Kt) −ϕ(Kt−)]

.
Since ϕ′ ≤p, and Kt −Kt−= ∆Lt, the mean-value theorem implies that
ϕ(Kt) −ϕ(Kt−) ≤p∆Lt.

Explicit Solution to an Irreversible Investment Model
551
Using again the inequality ϕ′ ≤p in the integrals with respect to dLc and
taking into account that −rϕ + Lϕ ≤−Π, we obtain:
E

e−rτnϕ(Kτn)

≤ϕ(k) −E
 τn
0
e−rtΠ(Kt)dt

+ E
 τn
0
e−rtpdLc
t

+ E


0≤t≤τn
e−rtp∆Lt


= ϕ(k) −E
 τn
0
e−rtΠ(Kt)dt

+ E
 τn
0
e−rtpdLt

,
and so
E
 τn
0
e−rt (Π(Kt)dt −pdLt)

+ E

e−rτnϕ(Kτn)

≤ϕ(k).
Since ϕ is nonnegative,
ϕ(k) ≥E
 τn
0
e−rtΠ(Kt)dt

−E
 ∞
0
e−rtpdLt

.
Applying Fatou’s lemma we get that
E
 ∞
0
e−rt (Π(Kt)dt −pdLt)

≤ϕ(k),
and so, finally, v(k) ≤ϕ(k) from the arbitrariness of L.
✷
We now give some properties on the value function v.
Lemma 3.1. For all k ≥0 and l ≥0, we have:
v(k) ≥−pl + v(k + l).
(3.4)
Proof. For L ∈A we consider the control ˜L with ˜L0−= 0 and ˜Lt = Lt +l, for
t ≥0. Let ˜K be the solution of (2.1) with the control ˜L and initial condition
˜K0−= k. Then, ˜Kt = Kt + l for t ≥0, and so ˜L ∈A. Thus,
v(k) ≥J(k, ˜L) = E
 ∞
0
e−rt 
Π( ˜Kt)dt −pd˜Lt

= J(k + l, L) −pl.
We obtain the required result from the arbitrariness of L.
✷
Moreover, recalling the standing assumption (2.3), we have:
Lemma 3.2. The value function v is finite and for any q ∈[0, p]
0 ≤v(k) ≤
˜Π((r + δ)q)
r
+ kq,
k ≥0.
(3.5)

552
H. Pham
Proof. The zero lower bound has been already noticed in Section 2. To prove
the upper bound, consider for q ∈[0, p] the nonnegative function
ϕ(k) = kq +
˜Π((r + δ)q)
r
.
Then, ϕ′ ≤p and
rϕ −Lϕ −Π = ˜Π((r + δ)q) + (r + δ)kq −Π(k) ≥0,
∀k ≥0,
by definition of ˜Π in (2.3). This implies that the nonnegative function ϕ is a
super-solution to (3.1), and we conclude with Proposition 3.1.
✷
Lemma 3.3. a) The value function v is nondecreasing, concave and contin-
uous on (0, ∞).
b) We have the inequalities: 0 ≤v(0+) ≤
˜
Π((r+δ)p)
r
.
Proof. a) The nondecreasing monotonicity of v follows from the nondecreas-
ing property of the process K with respect to the initial condition k given an
admissible control L, and from the nondecreasing monotonicity of Π.
The proof of concavity of v is standard: it is established by considering
convex combinations of initial states and controls and using the linearity of
dynamics (2.1) and concavity of Π.
b) The limit v(0+) exists from the nondecreasing property of v. By taking
q = p in the inequality of Lemma 3.2, we obtain the required estimation on
this limit.
✷
Since v is concave on (0, ∞), it admits a right derivative v′
+(k) and a left
derivative v′
−(k) at any k > 0, and v′
+(k) ≤v′
−(k). Moreover, inequality (3.4)
shows that
v′
−(k) ≤p,
∀k > 0.
(3.6)
We then define the so-called no-transaction region :
NT =
1
k > 0 : v′
−(k) < p
2
.
Lemma 3.4. There exists kb ∈[0, ∞] such that:
NT = (kb, ∞),
(3.7)
v is differentiable on (0, kb) and
v′(k) = p
on B = (0, kb).
(3.8)
Proof. Put kb = inf{k ≥0 : v′
+(k) < p}. Then p ≤v′
+(k) ≤v′
−(k) if k < kb.
Together with (3.6), this proves (3.8). Finally, the concavity of v shows (3.7).
✷
Remark 3.1. We shall see later that 0 < kb < ∞, and the optimal strategy for
the firm consists in doing nothing when it is in the region NT = (kb, ∞), and
in buying capital when it is below kb in order to reach the threshold kb. The
region B = (0, kb) will be then called the buy region.

Explicit Solution to an Irreversible Investment Model
553
4 Viscosity solutions and regularity of the value function
The concept of viscosity solutions is known to be a general power tool for
characterizing the value function of a stochastic control problem, see, e.g., [4].
It is based on the dynamic programming principle which we now recall in our
context.
Dynamic programming principle: Assume that v is continuous on (0, ∞).
Then for all k > 0, we have
v(k) = sup
L∈A
E
B θ
0
e−rt (Π(Kt)dt −pdLt) + e−rθv(Kθ)1θ<∞
C
,
(4.1)
where θ = θ(L) is any stopping time, possibly depending on the control L ∈
A. The precise meaning of this assertion is:
v(k) = sup
L∈A
sup
τ∈T
E
B θ
0
e−rt (Π(Kt)dt −pdLt) + e−rθv(Kθ)1θ<∞
C
= sup
L∈A
inf
τ∈T E
B θ
0
e−rt (Π(Kt)dt −pdLt) + e−rθv(Kθ)1θ<∞
C
.
Here T denotes the set of stopping times in [0, ∞]. The DPP is frequently used
in this form in the literature. However, many proofs cannot be considered as
rigorous. Clearly, DPP holds for the case where Ωis a path space. However,
it is difficult to give a precise reference which covers the situation we consider
here. We use this result for granted and left the detailed discussion of this
issue for further studies.
We recall the definition of viscosity solutions for a PDE of the form
F(x, v, Dxv, D2
xxv) = 0,
x ∈O,
(4.2)
where O is an open subset in Rn and F is a continuous function and nonin-
creasing in its last argument (with respect to the order of symmetric matrices).
Definition 1. Let v be a continuous function on O. We say that v is a vis-
cosity solution to (4.2) on O if it is
(i) a viscosity supersolution to (4.2) on O: for any x0 ∈O and any C2-
function ϕ in a neighborhood of x0 such that x0 is a local minimum of v −ϕ
and (v −ϕ)(x0) = 0, we have:
F(x0, ϕ(x0), Dxϕ(x0), D2
xxϕ(x0)) ≥0;
(ii) a viscosity subsolution to (4.2) on O: for any x0 ∈O and any C2-function
ϕ in a neighborhood of x0 such that x0 is a local maximum of v −ϕ and
(v −ϕ)(x0) = 0, we have:
F(x0, ϕ(x0), Dxϕ(x0), D2
xxϕ(x0)) ≤0.

554
H. Pham
Theorem 4.1. The value function v is a continuous viscosity solution of the
Hamilton–Jacobi–Bellman equation (3.1) on (0, ∞).
Proof. The argument is based on the dynamic programming principle and
Itˆo’s formula. It is standard, but somewhat technical in this singular control
context. We give it in the appendix.
✷
Based on the property that the value function is a concave viscosity solu-
tion of the HJB equation, we can now prove that it belongs to C2.
Theorem 4.2. The value function v is a classical C2-solution on (0, ∞) to
the Hamilton–Jacobi–Bellman equation
min {rv −Lv −Π(k) , −v′(k) + p} = 0,
k > 0.
Proof. Step 1. We first prove that v is a C1-function on (0, ∞). Since v is
concave, the left and right derivatives v′
−(k) and v′
+(k) exist for any k > 0 and
v′
+(k) ≤v′
−(k). We argue by contradiction and suppose that v′
+(k0) < v′
−(k0)
for some k0 > 0. Fix some q in (v′
+(k0), v′
−(k0)) and consider the function
ϕε(k) = v(k0) + q(k −k0) −1
2ε(k −k0)2,
with ε > 0. Then k0 is a local maximum of (v −ϕε) with ϕε(k0) = v(k0).
Since ϕ′
ε(k0) = q < p by (3.6) and ϕ′′
ε(k0) = 1/ε, the subsolution property for
v to (3.1):
min {rϕ(k0) −Lϕ(k0) −Π(k0) , −ϕ′(k0) + p} ≤0,
implies that we must have the inequality
rϕ(k0) + δk0q + 1
ε −Π(k0) ≤0.
(4.3)
With ε sufficiently small, this leads to a contradiction and, hence, proves that
v′
+(k0) = v′
−(k0).
Step 2. By Lemma 3.4, v belongs to C2 on (0, kb) and satisfies v′(k) = p,
k ∈(0, kb). From Step 1, we have NT = (kb, ∞) = {k > 0 : v′(k) < p}. We
now check that v is a viscosity solution of :
rv −Lv −Π = 0,
on (kb, ∞).
(4.4)
Let k0 ∈(kb, ∞) and ϕ be a C2-function on (kb, ∞) such that k0 is a local
maximum of v −ϕ, with (v −ϕ)(k0) = 0. Since ϕ′(k0) = v′(k0) < p, the
subsolution property for v to (3.1):
min {rϕ(k0) −Lϕ(k0) −Π(k0) , −ϕ′(k0) + p} ≤0,
implies the inequality

Explicit Solution to an Irreversible Investment Model
555
rϕ(k0) −Lϕ(k0) −Π(k0) ≤0.
Thus, v is a viscosity subsolution of (4.4) on (kb, ∞). The proof of the vis-
cosity supersolution property is similar. Now for arbitrary k1 ≤k2 ∈(kb, ∞),
consider the Dirichlet boundary problem
rV −LV −Π(k) = 0,
on (k1, k2),
(4.5)
V (k1) = v(k1),
V (k2) = v(k2).
(4.6)
Classical results provide the existence and uniqueness of a C2-function V on
(k1, k2) which is a solution to (4.5)-(4.6). In particular, this smooth function
V is a viscosity solution of (4.4) on (k1, k2). From standard uniqueness results
on viscosity solutions (here for a linear PDE in a bounded domain), we deduce
that v = V on (k1, k2). From the arbitrariness of k1, k2, it follows that v is in
C2 on (kb, ∞) and satisfies (4.4) in the classical sense.
Step 3. It remains to prove the C2-condition at kb in the case 0 < kb < ∞.
Let k ∈(0, kb). Since v is in C2 on (0, kb) with v′(k) = p, the supersolution
property for v to (3.1) applied at the point k and the test function ϕ = v:
min {rϕ(k) −Lϕ(k) −Π(k) , −ϕ′(k) + p} ≥0,
implies that v satisfies (in the classical sense) the inequality:
rv(k) −Lv(k) −Π(k) ≥0,
0 < k < kb.
The derivative of v being constant equal to p on (0, kb), this yields:
rv(k) + δkp −Π(k) ≥0,
0 < k < kb,
and, therefore,
rv(kb) + δkbp −Π(kb) ≥0.
(4.7)
On the other hand, from the C1-smooth fit at kb, we have by sending k
downwards to kb into (4.4):
rv(kb) + δkbp −Π(kb) = 1
2γ2k2
bv′′(k+
b ).
(4.8)
From the concavity of v, the right-hand side of (4.8) is nonpositive, and this
fact, combined with (4.7), implies that v′′(k+
b ) = 0. This proves that v is C2
at kb with v′′(kb) = 0.
✷
5 Solution of the optimization problem
5.1 Some preliminary results on an ODE
We recall some useful results on the second order linear differential equation

556
H. Pham
rv −Lv −Π = 0.
(5.1)
arising from the HJB equation (3.1).
It is well-known that the general solution to the ODE (5.1) with Π = 0 is
given by the formula
ˆV (k) = Akm + Bkn,
where
m = δ
γ2 + 1
2 −
> δ
γ2 + 1
2
2
+ 2r
γ2 , < 0
n = δ
γ2 + 1
2 +
> δ
γ2 + 1
2
2
+ 2r
γ2 > 1
are the roots of
1
2γ2m(m −1) + δm −r = 0.
Moreover, the ODE (5.1) admits a twice continuously differentiable particular
solution on (0, ∞) given, accordingly, e.g. [6], by the formula
ˆV0(k) = J(k, 0) = E
 ∞
0
e−rtΠ( ˆKk
t )dt

,
where ˆKk is the solution to the linear SDE
d ˆKt = ˆKt (−δdt + γdWt) ,
ˆK0 = k.
In other words, ˆV0 is the expected profit corresponding to the zero control L
= 0.
Remark 5.1. The function ˆV0 can be expressed analytically as
ˆV0(k) = knG1(k) + kmG2(k),
with
G1(k) =
2
γ2(n −m)
 ∞
k
s−n−1Π(s)ds,
k > 0,
G2(k) =
2
γ2(n −m)
 k
0
s−m−1Π(s)ds,
k > 0.
Under assumption (2.2), the limiting behavior of the derivative ˆV ′
0 as k
tends to zero and infinity is described as follows.

Explicit Solution to an Irreversible Investment Model
557
Lemma 5.1.
ˆV ′
0(0+) := lim
k↓0
ˆV ′
0(k) = ∞and
ˆV ′
0(∞) :=
lim
k→∞
ˆV ′
0(k) = 0.
Proof. We rewrite ˆV0 as
ˆV0(k) = E
 ∞
0
e−rtΠ(kYt)dt

,
k > 0,
where Yt = e−δtMt, and M is the martingale Mt = exp(γWt−γ2
2 t). It is easily
checked by the Lebesgue theorem that one can differentiate the expression of
ˆV0 inside the expectation and the integral so that its derivative is given by
the equality
ˆV ′
0(k) = E
 ∞
0
e−rtYtΠ′(kYt)dt

,
k > 0.
Using the positivity and nonincreasing monotonicity of Π′, we may apply
the monotone convergence theorem as k tends to zero and obtain from the
Inada condition Π′(0+) = ∞that limk↓0 ˆV ′
0(k) = ∞. On the other hand, we
may also apply the dominated convergence theorem as k tends to infinity and
obtain from the other Inada condition Π′(∞) = 0 that limk→∞ˆV ′
0(k) = 0. ✷
5.2 Explicit form of the value function
Lemma 5.2. The buying threshold satisfies the inequalities
0 < kb < ∞.
Proof. We first check that kb > 0. If it is not the case, the buying region is
empty, and we would have from Lemma 3.4 and Theorem 4.2 that
rv −Lv −Π = 0,
k > 0.
Hence, v would be of the form
v(k) = Akm + Bkn + ˆV0(k),
k > 0.
Since m < 0 and |v(0+)| < ∞, this implies that A = 0. Now, since n > 1, we
get that v′(0+) = ˆV ′
0(0+) = ∞, a contradiction with the bound v′(k) ≤p for
all k > 0.
We also have kb < ∞. Otherwise, v would be on the form
v(k) = kp + v(0+),
∀k > 0.
This contradicts to the growth condition (3.5).
✷
We can now explicitly determine the value function v.

558
H. Pham
Theorem 5.1. The value function v has the following structure:
v(k) =
 kp + v(0+),
k ≤kb,
Akm + ˆV0(k), kb < k,
(5.2)
where the three constants v(0+), A and kb are determined by the continuity,
C1- and C2-smooth fit conditions at kb:
Akm
b + ˆV0(kb) = kbp + v(0+),
(5.3)
mAkm−1
b
+ ˆV ′
0(kb) = p,
(5.4)
m(m −1)Akm−2
b
+ ˆV ′′
0 (kb) = 0.
(5.5)
Proof. We already know from Lemma 3.4 that on the interval (0, kb), which is
nonempty by Lemma 5.2, v has the structure described in (5.2). Moreover, on
(kb, ∞), the derivative v′ < p in virtue of Lemma 3.4. Therefore, by Theorem
4.2, v satisfies the equation rv −Lv −Π = 0, and so, according to Subsection
5.1, it is of the form
v(k) = Akm + Bkn + ˆV0(k),
k > kb.
Since m < 0, n > 1, ˆV ′
0(k) →0 as k →∞, and ≤v′(k) ≤p, we must have
necessarily B = 0, and so v has the form written in (5.2). Finally, the three
conditions resulting from the continuity, C1- and C2-smooth fit conditions at
kb determine the constants A, kb and v(0+).
✷
Remark 5.2. By the viscosity solutions method adopted here we know the
existence of a triple (v(0+), A, kb) ∈R+ × R × (0, ∞) which is solution to the
system of equations (5.3)-(5.4)-(5.5). Indeed, this results from the continuity,
C1- and C2-properties of v at kb that we proved to hold a priori. This contrasts
with the classical verification approach where one tries to find a C2-solution
to (3.1), so of the form
˜v(k) =
 kp + ˜v(0+),
k ≤˜kb,
˜Akm + ˆV0(k), ˜kb < k,
(5.6)
and, hence, to prove the existence of a triple (˜v(0+), ˜A, ˜kb) ∈R+ × R × (0, ∞)
which is a solution to (5.3)-(5.4)-(5.5). By a verification argument, one then
shows that ˜v = v proving a posteriori the C2-property of v.
On the other hand, it is easily seen that we have uniqueness of a solution
(ˆv(0+), A, kb) ∈R+ × R × (0, ∞) to the system of equations (5.3) – (5.5).
Indeed, otherwise we could find another smooth C2-function ˜v of the form
(5.6), with the linear growth condition, and solving (3.1). This contradicts
the standard uniqueness results for PDE (3.1).
Remark 5.3. The value function v satisfies in (kb, ∞) the second order ODE

Explicit Solution to an Irreversible Investment Model
559
rv(k) + δkv′(k) −1
2γ2k2v′′(k) −Π(k) = 0,
k ∈(kb, ∞).
From the continuity and C1- and C2-conditions of v at kb, i.e. the relations
v(kb) = kbp + v(0+), v′(kb) = p and v′′(kb) = 0, we then deduce that
(r + δ)kbp + rv(0+) = Π(kb).
(5.7)
Remark 5.4. Computation of v
From a computational viewpoint, the constants A, kb, v(0+) can be determined
as follows. From equations (5.4)-(5.5), we obtain an equation for kb and express
A in terms of kb :
F(kb) := (1 −m) ˆV ′
0(kb) + kb ˆV ′′
0 (kb) = p(1 −m),
(5.8)
A = k1−m
b
m

p −ˆV ′
0(kb)

.
(5.9)
The value v(0+) is then computed from relation (5.3) or, equivalently, (5.7).
Note that a straightforward calculation provides the explicit expression of F:
F(k) = n(n −m)kn−1G1(k) −2
γ2
Π(k)
k
,
k > 0.
Example 1. Special case of the power profit function
We consider the case where Π is the Cobb–Douglas profit function, and we
assume, without loss of generality, that Π(k) = kα with 0 < α < 1. Then
ˆV0(k) = Ckα,
with
C =
1
r + αδ + γ2
2 α(1 −α)
.
Then, from (5.8), kb is explicitly written as :
kb =
 p(1 −m)
αC(α −m)

1
α−1
.
5.3 Optimal control
We recall the following well-known Skorohod lemma, see, e.g., [7].
Lemma 5.3. For any initial state k ≥0 and given a boundary kb ≥0, there
exist unique c`adl`ag adapted processes K∗and nondecreasing processes L∗sat-
isfying the following Skorohod problem S(k, kb) :
dK∗
t = K∗
t (−δdt + γdWt) + dL∗
t , t ≥0,
K∗
0−= k,
(5.10)
K∗
t ∈[kb, ∞)
a.e., t ≥0,
(5.11)
 ∞
0
1K∗
u>kbdL∗
u = 0.
(5.12)
Moreover, if k ≥kb, then L∗is continuous. When k < kb, L∗
0 = kb −k, and

560
H. Pham
K∗
0 = kb.
Remark 5.5. The solution K∗to the above equations is a reflected diffusion at
the boundary kb and the process L∗is the local time of K∗at kb. Condition
(5.12) means that L∗increases only when K∗hits the boundary kb. It is
also known that the r-potential of L∗is finite, i.e. E
 ∞
0
e−rtdL∗
t

< ∞, see
Chapter X in [9], so that
E
 ∞
0
e−rtK∗
t dt

< ∞.
(5.13)
Theorem 5.2. For k ≥0, let (K∗, L∗) be the solution to the Skorohod problem
S(k, kb). Then
v(k) = J(k, L∗),
k ≥0.
Proof. 1) We first consider the case where k ≥kb. Then, the processes K∗,
L∗are continuous. In view of (5.11) and Theorem 4.2, we have
rv(K∗
t ) −Lv(K∗
t ) −Π(K∗
t ) = 0, a.e.
t ≥0.
By applying Itˆo’s formula to e−rtv(K∗
t ) between 0 and T, we thus get:
E

e−rT v(K∗
T )

=
v(k) −E
B T
0
e−rtΠ(K∗
t )dt
C
+ E
B T
0
e−rtv′(K∗
t )dL∗
t
C
.
(5.14)
(Notice that the stochastic integral appearing in the Itˆo formula has zero
expectation because of (5.13)). Now, in view of (5.12), we have
E
B T
0
e−rtv′(K∗
t )dL∗
t
C
= E
B T
0
e−rtv′(K∗
t )1K∗
t =kbdL∗
t
C
= E
B T
0
e−rtpdL∗
t
C
,
since v′(kb) = p. Plugging into (5.14) yields:
v(k) = E

e−rT v(K∗
T )

+ E
B T
0
e−rtΠ(K∗
t )dt
C
−E
B T
0
e−rtpdL∗
t
C
.
(5.15)
From (5.13), we have that limT →∞E[e−rT K∗
T ] = 0. Since v satisfies a linear
growth condition in k, this implies that also
lim
T →∞E[e−rT v(K∗
T )] = 0.

Explicit Solution to an Irreversible Investment Model
561
By sending T to infinity into (5.15), we obtain, by the dominated convergence
theorem, the required result:
v(k) = J(k, L∗) = E
 ∞
0
e−rt (Π(K∗
t ) −pdL∗
t )

.
2) If k < kb, and since then L∗
0 = k −kb, we have:
J(k, L∗) = J(kb, L∗) −p(k −kb)
= v(kb) −p(k −kb) = v(k),
by recalling that v′ = p on (0, kb).
✷
Conclusion. The main results of this paper in Theorems 5.1 and 5.2
provide a complete and explicit solution to our irreversible investment under
uncertainty. They mathematically formulate the economic intuition that a
company will invest in buying capital in order to maintain its production
capacity above a threshold kb, which can be computed quite explicitly.
Appendix : Proof of Theorem 4.1
(i) Viscosity supersolution property.
Fix k0 > 0 and C2-function ϕ such that v(k0) = ϕ(k0) and ϕ(k) ≤v(k) for
all k in a neighborhood ¯Bε(k0) = [k0 −ε, k0 + ε] of k0 (0 < ε < k0). Consider
the admissible control L ∈A defined by
Lt =
0, t = 0
η, t ≥0,
where 0 ≤η < ε. Define the exit time τε = inf{t ≥0 : Kt /∈¯Bε(x0)}. Here K
is the capacity production starting from k0 and controlled by L above. Notice
that K has at most one jump at t = 0 and is continuous on (0, τε]. By the
dynamic programming principle (4.1) with θ = τε ∧h, h > 0, we have :
ϕ(k0) = v(k0) ≥E
B τε∧h
0
e−rt(Π(Kt)dt −pdLt) + e−r(τε∧h)v(Kτε∧h)
C
≥E
B τε∧h
0
e−rt(Π(Kt)dt −pdLt) + e−r(τε∧h)ϕ(Kτε∧h)
C
.
(5.16)
Applying Itˆo’s formula to the process e−rtϕ(Kt) between 0 and τε ∧h, and
taking the expectation, we obtain similarly as in the proof of Proposition 3.1
by noting also that dLc
t = 0:

562
H. Pham
E[e−r(τε∧h)ϕ(Kτε∧h)] = ϕ(k0) + E
B τε∧h
0
e−rt (−rϕ + Lϕ) (Kt)dt
C
+ E



0≤t≤τε∧h
e−rt [ϕ(Kt) −ϕ(Kt−)]

.
(5.17)
Combining relations (5.16) and (5.17), we see that
E
B τε∧h
0
e−rt (rϕ −Lϕ −Π) (Kt)dt
C
+ E
B τε∧h
0
e−rtpdLt
C
−E



0≤t≤τε∧h
e−rt [ϕ(Kt) −ϕ(Kt−)]

≥0.
(5.18)
⋆Taking first η = 0, i.e. L = 0, we see that K is continuous, and only
the first term in the left-hand side of (5.18) is non zero. By dividing the
above inequality by h with h →0, we conclude by the dominated convergence
theorem:
rϕ(k0) −Lϕ(k0) −Π(k0) ≥0.
(5.19)
⋆Now, by taking η > 0 in (5.18), and noting that L and K jump only at
t = 0 with the jump size η, we get that
E
B τε∧h
0
e−rt (rϕ −Lϕ −Π) (Kt)dt
C
+ pη −ϕ(k0 + η) + ϕ(k0) ≥0.
(5.20)
Taking h →0, then dividing by η and letting η →0, we obtain the inequality
p −ϕ′(k0) ≥0.
(5.21)
This proves the required viscosity supersolution property:
min {rϕ(k0) −Lϕ(k0) −Π(k0), −ϕ′(k0) + p} ≥0.
(5.22)
(ii) Viscosity sub-solution property.
We prove this part by contradiction. Suppose the claim is not true. Then,
there is k0 > 0, ε ∈(0, k0), a ϕ C2-function with ϕ(k0) = v(k0) and ϕ ≥v in
¯Bε(k0) = [k0 −ε, k0 + ε], and ν > 0 such that for all k ∈¯Bε(k0) we have:
rϕ(k) −Lϕ(k) −Π(k) ≥δ,
(5.23)
ϕ′(k) ≤p −ν.
(5.24)

Explicit Solution to an Irreversible Investment Model
563
For a control L ∈A, consider the exit time τε = inf{t ≥0 : Kt /∈¯Bε(x0)}.
(Here K is the capacity production starting from k0 and controlled by L). By
applying Itˆo’s formula to e−rtϕ(Kt), we get :
E
)
e−rτεϕ(Kτ −
ε )

= ϕ(k0) + E
 τε
0
e−rt (−rϕ + Lϕ) (Kt)dt

+ E
 τε
0
e−rtϕ′(Kt)dLc
t

+ E


0≤t<τε
e−rt [ϕ(Kt) −ϕ(Kt−)]

.
(5.25)
Notice that for all t ∈[0, τε), Kt ∈¯Bε(k0). Then, from Taylor’s formula and
(5.24), noting that ∆Kt = ∆Lt, we obtain for t ∈[0, τε):
ϕ(Kt) −ϕ(Kt−) = ∆Kt
 1
0
ϕ′(Kt + z∆Kt)dz
≤(p −ν)∆Lt.
(5.26)
Due to relations (5.23) – (5.26), we thus obtain:
E
)
e−rτεϕ(Kτ −
ε )

≤ϕ(k0) + E
 τε
0
e−rt (−Π −ν) (Kt)dt

+ E
B τ −
ε
0
e−rt(p −ν)dLt
C
= ϕ(k0) + E
 τε
0
e−rt (−Π(Kt)dt + pdLt)

−E

e−rτεp∆Lτε

−ν

E
 τε
0
e−rtdt

+ E
B τ −
ε
0
e−rtdLt
C
.
(5.27)
Notice that while Kτ −
ε ∈¯Bε(k0), Kτε is either on the boundary ∂Bε(k0) or
out of ¯Bε(k0). However, there is some random variable α taking values in [0, 1]
such that
kα := Kτ −
ε + α∆Kτε
= Kτ −
ε + α∆Lτε ∈∂¯Bε(k0) = {k0 −ε, k0 + ε}.
Then, similarly as in (5.26), we have :
ϕ(kα) −ϕ(Kτ −
ε ) ≤α(p −ν)∆Lτε.
(5.28)
Notice that Kτε = kα + (1 −α)∆Lτε, and so from Lemma 3.1 we have:

564
H. Pham
v(kα) ≥−p(1 −α)∆Lτε + v(Kτε).
(5.29)
Recalling that ϕ(kα) ≥v(kα), inequalities (5.28), (5.29) imply:
ϕ(Kτ −
ε ) ≥v(Kτε) −(p −αν)∆Lτε.
Plugging the last inequality into (5.27) and recalling that ϕ(k0) = v(k0), we
obtain:
v(k0) ≥E
 τε
0
e−rt (Π(Kt)dt −pdLt) + v(Kτε)

+ ν

E
 τε
0
e−rtdt

+ E
B τ −
ε
0
e−rtdLt
C
+ E

e−rτεα∆Lτε


.
(5.30)
⋆We now claim that there is a constant g0 > 0 such that for all L ∈A :
E
 τε
0
e−rtdt

+ E
B τ −
ε
0
e−rtdLt
C
+ E

e−rτεα∆Lτε

≥g0. (5.31)
Indeed, one can always find some constant G0 > 0 such that the C2-function
ψ(k) = G0((k −k0)2 −ε2),
satisfies the relations
min {rψ −Lψ + 1, 1 −|ψ|} ≥0,
on
¯Bε(k0),
ψ = 0,
on ∂¯Bε(k0).
For instance, we can choose:
G0 = min

1
rε2 + 2εδ(k0 + ε) + γ2(k0 + ε)2 , 1
2ε

> 0.
By applying again Itˆo’s lemma, we get that
E
)
e−rτεψ(Kτ −
ε )

≤ψ(k0) + E
 τε
0
e−rtdt

+ E
B τ −
ε
0
e−rtdLt
C
(5.32)
Since ψ′(k) ≥−1, we have:
ψ(Kτ −
ε ) −ψ(kα) ≥−

Kτ −
ε −kα

= α∆Lτε ≥0.
Plugging into (5.32) yields:
E
 τε
0
e−rtdt

+ E
B τ −
ε
0
e−rtdLt
C
≥E

e−rτεψ(kα)

−ψ(k0) = −ψ(k0) = G0ε2.
(5.33)

Explicit Solution to an Irreversible Investment Model
565
Hence, the claim (5.31) holds with g0 = G0ε2.
⋆Finally, by taking supremum over all (L, M) ∈A in (5.30), and invoking
the dynamic programming principle (4.1), we have that v(k0) ≥v(k0) + νg0,
which is the required contradiction.
References
1. Chiarolla, M. and Haussmann, U.: Explicit solution of a stochastic irreversible
investment problem and its moving threshold. Preprint, 2003.
2. Davis, M., Norman, A.: Portfolio selection with transaction costs. Math. Oper.
Res., 15, 676–713, 1990.
3. Dixit, A.K., Pindick, R.: Investment under Uncertainty. Princeton University
Press, 1994.
4. Fleming, W., Soner, M.: Controlled Markov Processes and Viscosity Solutions.
Springer-Verlag, New York, 1993.
5. Jeanblanc-Picqu´e, M. and Shiryaev, A.: Optimization of the flow of dividends.
Russian Math. Surveys, 50, 257–277, 1995.
6. Kobila, T.O.: A class of solvable investment problems involving singular controls.
Stoch. and Stoch. Reports., Vol. 43, 20–63, 1993.
7. Lions, P.L., Snitzman, A.: Stochastic differential equations with reflecting
boundary conditions. Comm. Pure. Appl. Math., Vol. 37, 511–537.
8. Meyer, P.A.: S´eminaire de Probabilit´es, Lect. Notes in Math., 511, Springer-
Verlag, 1976.
9. Revuz, D., Yor, M.: Continuous Martingale and Brownian Motion¿ Springer-
Verlag, 1991.
10. Rockafellar, T.: Convex Analysis. Princeton University Press.
11. Shreve, S. and Soner, M.: Optimal investment and consumption with transaction
costs. Annals of Appl. Prob., Vol. 4, 609–692, 1994.


Gittins Type Index Theorem for Randomly
Evolving Graphs
Ernst PRESMAN1 and Isaac SONIN2,1
1 Central Economics and Mathematics Institute, Nakhimovskii prospect, 47,
Moscow, Russia.
presman@cemi.rssi.ru
2 Department of Mathematics, University of North Carolina at Charlotte,
Charlotte,NC, 28223, USA.
imsonin@email.uncc.edu
Summary. We consider the problem which informally can be described as follows.
Initially a finite set of independent trials is available. If a Decision Maker (DM)
chooses to test a specific trial she receives a reward, and with some probability, the
process of testing is terminated or the tested trial becomes unavailable but some
random finite set (possibly empty) of new independent trials is added to the set of
initial trials, and so on. The total number of potential trials is finite. A DM knows
the rewards and transition probabilities depending on the trials. On each step she
can either quit (i.e. stop the process of testing), or continue. Her goal is to select
an order to test trials and an quitting (stopping) time to maximize the expected
total reward. We simplify and generalize some results obtained earlier for similar
problems, we prove that an index can be assigned to each possible trial and an
optimal strategy uses on each step the trial with maximal index between available
ones. We present a recursive procedure with a transparent interpretation to calculate
the index. We discuss the connection between introduced index and Gittins index.
Key words: Markov decision process, graph, Gittins index, priority rules.
Mathematics Subject Classification (2000): 90B36, 90C40, 62L05
1 Introduction
The goal of this paper is twofold. First, to generalize the main result and to
simplify the proof of the paper by Denardo et al. [3]. In that paper a model of
R&D projects is considered. Each stage of a project in the model is represented
by an edge of a directed forest. To activate an edge e one needs to pay a certain
amount r(e). Each activated edge can pass or fail. The successful completion of
a path from a root to a leaf brings certain reward and terminates the activity.
In case of failure all edges which follow the failed edge become unavailable. The

568
I. Sonin and E. Presman
goal is to maximize the expected reward. The optimal strategy in the model
is an index strategy. Each time one should use an edge with the highest value
of the index among the available indices. An index for an edge is specified
only by the parameters of the directed tree above this edge. We consider more
general model where an optimal strategy is also an index strategy. The notion
of the index in both papers is a generalization of the corresponding notion in
the model, which we call below a binary elementary (BE) model, studied in
early sixties in Mitten (1960) [9].
The second goal of our paper is to show that the index described above
is a generalization of the well-known Gittins index (GI). Thus GI, beside the
original papers of Gittins [6] and Gittins and Jones [7], has the second root
of its origin in the mentioned paper by Mitten [9]. It seems that the proper
credit never was given to Mitten and his model.
The strategies of the type, when for selecting an action on each stage it
suffices to solve much simpler problem, for example the one-step optimization
problem, are called myopic or greedy. They are very popular and intensively
studied though in contrast to model above they usually are not optimal. We
call a strategy a Priority Rule (PR) if an index is calculated for each action
and an action with the highest value of index among available is selected.
The myopic strategies form a nucleus of developed later so called Multi-
armed Bandit (MAB) Theory (for independent (!) arms) (see Gittins [6], Whit-
tle [15], and Berry and Fristedt [1]), where the corresponding strategy is called
Gittins index strategy.
The Gittins index, denoted by G(x), where x is a state of Markov chain,
plays an important role in theory of MAB with independent arms but it also
appears in other problems like the optimal replacement problems. The main
result of this theory states that if there are a finite number of independent
MC and a decision maker at each moment can engage (test) one of these MC
while all other remain frozen then the optimal strategy is to test MC whose
state xj at this moment has the largest value Gj(xj), where Gj(xj) is the
value of GI of MC j at state xj.
Note also that the same term Multi-armed bandit problem is used also
in the classical papers by R. Bellman [2], D. Feldman [4] as well as in the
book of Presman and Sonin [10] and in some sections of the book by Berry
and Fristedt where arms are dependent, i.e. a trial of one arm provides an
information about the parameters of other arms also. In this case a myopic
Gittins index strategy is not optimal in general.
The traditional Gittins index G(x) for a Markov chain (MC) is defined as
the maximal value of a discounted expected reward per expected discounted
length of a cycle starting from x, i.e.
G(x) = sup
τ
Ex
τ−1
n=o βnr(Zn)
Ex
τ−1
n=o βn
,
(1.1)
where β is a discount factor, 0 < β < 1, τ is a stopping time, τ ≥1, r(·) is a
reward function, and Zn is the state of Markov chain at time n.

Gittins Index Theorem for Randomly Evolving Graphs
569
Note, that as usual in the theory of Markov Decision Processes, one can
consider the discount factor β as a probability of survival of a MC at each
step. Formally one can introduce an absorbing state and to introduce new
probabilities such that the probability of transition to an absorbing state is
equal to 1−β and all other transition probabilities are multiplied by the factor
β. Then the denominator in formula (1.1) multiplied by (1 −β) is equal to
the probability of absorption during the time interval (0, τ),
Qτ(x) = 1 −Exβτ.
(1.2)
In our paper we will consider the specific Markov decision process on a
forest with one absorption state, when probability of absorption q(A) depends
on chosen action A. We introduce notion of index for control actions as follows.
For fixed strategy π with stopping time τ and control process (Ai), with
A0 = e, we consider the reward Rπ(e), and the probability of absorption
Qπ(e). Following the footsteps of Mitten [9], Granot and Zuckerman [8] and
Denardo et al. [3], we define the index
α(e) = sup Rπ(e)
Qπ(e) ,
(1.3)
where supremum is taken over some set of strategies.
Note that the reward Rπ(e) can be represented in the form
Rπ(e) = Eπ
Bτ−1

i=0
r(Ai)
C
= ˜Eπ


τ−1

i=0
r(Ai)
i−1
(
j=0
(1 −q(Aj))

,
where ˜E denote the expectation with respect to corresponding Markov chain
without absorbing state. The probability of absorption Qπ(e) can be repre-
sented in the same way with q(·) instead of r(·). In case q(Ai) = 1 −β for all
i, the denominator in (1.3) coincides with (1.2). So, (1.3) generalizes (1.1) to
the case of Markov decision process with probability of absorption depending
on the current state.
In the sequel we consider only the case of finite forest but most of the
results can be extended to the case of an infinite forest with some extra con-
ditions.
The plan of our paper is as follows. In Section 2 and 3 we consider cor-
respondingly the BE-model and the model studied in Denardo et al. [3]. In
Section 4 we formulate our model and present the main result. In Section 5
we discuss main ideas of the proofs. In Section 6 we present and prove some
auxiliary results leaving the proof of one lemma to the Appendix (Section 9).
In Section 6 we give the proof of the main result. In Section 8 we present an
algorithm for calculating the index. In Section 9 we discuss connection with
Gittins index and some open problems.

570
I. Sonin and E. Presman
2 A binary elementary (BE) model of independent trials
Suppose that there is a finite set of independent Bernoulli trials e1, e2, ..., em,
with two possible outcomes in each trial, “continuation” with probability pi, in
the i-th trial, and “termination”, with probability qi. A decision maker (DM)
can choose an order in which to conduct (test) the trials. Each trial can be
tested only once. The test of the i-th trial brings a reward ri, and in the case of
“continuation” she may continue testing or quit. In the case of “termination”
the testing has to be terminated. The goal of DM is to select the optimal order
to maximize the expected total reward. Such formulation is equivalent to a
formulation where DM has to pay an amount ci in advance, obtains ai with
probability pi, and bi with probability qi, and ri = −ci + aipi + biqi.
This problem is a reformulation of a “least cost testing sequencing” prob-
lem solved independently by a few authors in 1960 (see Mitten [9]). We call
it BE-model (Binary Elementary model). A rather simple proof shows that
the optimal strategy has a remarkably simple structure and is based on an
index α calculated for each trial ei, α(ei) equal to expected profit divided by
probability of termination, i.e.
α(ei) = ri
qi
.
(2.1)
The optimal strategy has the following form: test the trials with positive
index in the order of decreasing. If all trials must be tested then all they should
be tested in the above order. Mitten analyzed the model when ci < 0, ai = 0,
and bi > 0 but this makes no difference for the analysis of the problem.
3 Independent trials on a forest, binary forest (BF)
model
A model described above was generalized by Granot and Zuckerman [8] in
the context of multi-stage R&D models. That paper has many interesting
developments but contrary to their claim the Theorem 1 in their paper can
be obtained from the Mitten result by transforming semi-Markov discounting
into absorption probabilities.
This model in turn was recently generalized in a paper by Denardo et al.
[3]. The latter model can be described briefly as follows.
At initial moment a set of independent trials with two possible outcomes
are available. For some of trials the nature of two outcomes is the same as
in BE model - “continuation” and “termination”. For other trials for both
of outcomes one can continue but differently. to pone of outcomes leads to
a possibility to continue the process of testing. In the case of one outcome a
“continuation” is the same as above, but the second of outcomes adds to the
set of available trial a set of new trials, some of them with a similar feature and

Gittins Index Theorem for Randomly Evolving Graphs
571
so on, and so on. Each trial e of the second kind and all trials that “follow” e
in one or more steps can be represented by edges of a directed tree T(e). A tree
corresponding to the trial of the first kind consists of one edge. The total set
of potentially available trials is finite and is represented by a union of directed
trees, i.e. by a directed forest F0. The trials of the first kind correspond to
the leaves of this forest, i.e. to the edges such that no edges follows. All other
edges are called stems. The initially available edges are called the roots of F0.
If edge e is tested (used) it can pass with some probability or fail with
complimentary probability. These events are independent of similar events for
other edges. If an edge e “fails” than e and all edges that follow e are not
available any more, but other available edges can be tested. If a stem e passed
then it becomes unavailable but all edges that immediately follow e are added
to the set of available edges. If a leaf e passed then the testing has to be
terminated. An edge e′ can be tested only once and only if all edges on the
path from one of the roots of F0 to e′ “passed” before. The reward on stems
(costs) are negative, positive rewards (prizes) are available only on leaves,
i.e. on edges such that no edge follows. The testing can be conducted till the
termination, when a prize is obtained, i.e. a leaf is reached and “passed”, or
till the moment when DM decides to quit, i.e. to stop testing. The goal of a
DM is to maximize the expected value of either linear or exponential function
of the profit (total reward) over all possible strategies to test edges. We call
this model BF-model (Binary Forest model) since the result of each trial has
two outcomes.
The main result of paper [3] is that the optimal strategy is based again on
an index generalizing (2.1). This index α(e) is defined as α(e) = sup
π
Rπ(e)
Qπ(e),
where Rπ(e) and Qπ(e) are correspondingly the expected total reward and the
probability of termination (to obtain a prize) in linear case and corresponding
function in exponential case. Supremum is taken over some class of strategies,
which authors call “candidates”. The authors also noted that their problem
can be described in terms of so called MAB processes and their index is similar
to the Gittins index.
We gratefully acknowledge the possibility to read the manuscript of [3]
before its publication.
The proof of the main theorem in [3] is complicated and long. Responding
to their hope “that someone will devise a simpler proof than theirs” we ob-
tained in the linear case a different, shorter and more transparent inductive
proof of this important and interesting result. We found also that our proof
covers also more general situation when:
1) a binary result of testing of an edge (a trial) can be replaced by a
finite number of outcomes in the spirit of general theory of Markov Decision
Processes (MDP);
2) two separate functions, the prize function b(e) > 0 for leaves and the
cost function c(e) < 0 for all other edges are replaced by a general reward

572
I. Sonin and E. Presman
function r(e), which can take any finite values (positive, negative or zero) for
any edge;
3) the termination when a prize is obtained, is replaced by a possibility of
termination with probability depending on the trial tested at any stage.
The last possibility implies also that the discounting with coefficient β, 0 <
β < 1 can be considered as a special case of our model since it is equivalent
to a termination with a fixed probability 1 −β.
We will consider only the linear function of the profit.
Note also that the optimal strategy in BF-model takes the form of a series
of “depth first” searches of paths to leaves. In our model this property is not
true generally due to generalization 2.
In the MAB literature the term arm is usually understood as a stochastic
process which can be engaged again and again. In the BE, BF models and
the model presented below each edge can be used only once so we prefer not
to use the term arm at all.
4 Multiple forest (MF) model: formulation and results
We present our model in a standard frame of Markov Decision Processes
(MDP). A MDP model is given (see e.g. Feinberg and Schwartz [5]) by a
tuple M = (S, A(x), p(y|x, a), L), where S is a state space, x ∈S represents
a state of a system under consideration, A(x) is a set of actions a available
at state x, p(y|x, a) is a probability that the next state is y if at state x an
action a was chosen (transition operator), and L is a functional defined on
the trajectories of a system.
By hn = (x0, a0, x1, . . . , xn−1, an−1, xn) we denote a trajectory of length
n,
n ≤∞, h∞= h. A general (randomized) strategy π in MDP is a se-
quence πn(·|hn), n = 0, 1, 2, ... of distributions on action set A(xn) possibly
depending on the whole past history. An initial state x and a strategy π de-
fine a measure P π
x in the space of infinite trajectories, i.e. the distribution of
the state-action process (Xn, An), Xn(h) = xn, An(h) = an, n = 0, 1, . . .. We
denote by Eπ
x the corresponding expectation. If a distribution πn(·|hn) is a
function π(xn) with values in A(xn), a strategy π is a stationary (nonran-
domized) strategy. A stationary strategy π defines the transition probabilities
p(y|x, π(x)) for the (homogeneous) Markov chain (Xn) describing the evo-
lution of the system. The goal of the DM is to maximize the expected total
reward Rπ(x) = Eπ
xL = Eπ
x
∞
i=0 r(Xi, Ai). From the general theory of MDP
it follows that for such a functional it suffices to consider only the station-
ary strategies. The value function R(x) = supπ Rπ(x) satisfies the Bellman
(optimality) equation R(x) =
sup
a∈A(x)
B
r(x, a) +

y
p(y|x, a)R(y)
C
.
Let some initial forest F0 be given. We say that edge e′ follows e, if e is
on a unique path from a root of a tree to e′. Denote by N(e) the edges from

Gittins Index Theorem for Randomly Evolving Graphs
573
T(e) that immediately follow e. Leaves are edges such that no edge follows.
Other edges are stems.
The state space S = {x} in MF-model consists of absorbing state x∗,
empty set ∅, and all subsets of edges of F0 which do not contain any two
edges such that one follows other, i.e. if e, e′ ∈x for some x and e ̸= e′ then
T(e) = T(e′) = ∅.
The action set A(x) = x ∪{e∗} for x ̸= x∗, A(x∗) = e∗, where e∗is a quit
action, i.e. at each stage a DM can test any of edges in x or select an action
e∗which at the next moment moves a system to x∗.
The following parameters are defined for every edge e: 1) a number
q(e), 0 ≤q(e) ≤1, 2) for each subset D of the set N(e) (including empty
set and the full set N(e)) a number pD(e) ≥0 such that 
D⊂N(e) pD(e) =
1 −q(e), 3) a reward r(e) such that r(e∗) = 0.
The meaning of these parameters is as follows. Edges correspond to trials.
If edge e is tested, it becomes unavailable, and with probability q(e) the system
moves to the absorbing state x∗, and with probability pD(e) all edges from
the set D are added to the set of edges available for testing.
Formally, the transitional probabilities have the following form: p(x∗|x, e∗)
= 1; if e ̸= e∗then p(y|x, e) = pD(e) for y = {x \ e} ∪D and p(x∗|x, e) = q(e).
Note that the independence of arms (edges e) is manifested by the property
that p(y|x, e) depends only on e ∈x, and does not depend on other e′ from x,
and that the “coordinates” of a new state y for edges e′ ̸= e remain the same.
Given an initial state x and strategy π, the goal is to maximize the expected
total reward, Rπ(x) = Eπ
x
∞

i=0
r(Ai), where Ai is the edge tested at moment i.
Main Problem A: Given an initial state x, maximize Rπ(x) over all
strategies.
Main Problem B: Given an initial state x, maximize Rπ(x) over all
strategies such that a quit action e∗is available only if x = ∅, or x = x∗.
As we mentioned, the general theory of MDP implies that for these prob-
lem the stationary nonrandomized strategies form a sufficient class. Still,
stationary strategies may have rather complicated structure. For example,
a strategy can test edge e if edges e, e′, and e′′ are available and test edge e′
if only edges e, and e′ are available. We can expect that the optimal strategy
will be among stationary strategies having the following simpler structure.
Let us consider an ordered list of different edges π = (e1, ..., ek). We shall
say that ei is senior than ej for π if ei is listed earlier i.e. if i < j. We
shall denote {π} = {e1, ..., ek}, i.e. the set of elements of π. List π defines a
(nonrandomized) stationary strategy, which we denote also π, as follows: if
there is no available edges, i.e. if x ∩{π} = ∅, then π(x) = e∗, otherwise π(x)
equals to the most senior element in x∩{π}. Such strategy is called a priority
rule (PR).

574
I. Sonin and E. Presman
Note that if ei is senior than ej, it does not imply that edge ei for a
particular history will be used earlier then ej. It may happens because ei may
be not available when ej is already available. More than that, it is possible
that two different lists define the same PR because the same states have
positive probabilities and both lists define the same order for each state that
has positive probability.
Example. Consider the forest given on Fig.1.
a10= -2
9
10
11
12
13
14
15
a9=8
a11=11
a12= -4
a13=1
a14=3
a15= -3
a4=6
a7=2
3
4
5
7
a3=6.4
a5= -1
a6=9
a8=10
a1ª5.05
a2=4
1
2
6
8
Fig. 1. Example of a forest with γ(i) = αi.
Edges 1 - 3, 5, 7 are stems, N(1) = {3, 4, 5}, N(2) = {6, 7, 8}, N(3) =
{9, 10, 11}, N(5) = {12, 13}, N(7) = {14, 55}. Edges 4, 6, 8 - 15 are leafs, so
that N(j) = ∅for j = 4, 6, 8 −15. p{3,4}(1) > 0, p{5}(1) > 0, p{6,7}(2) > 0,
p{8}(2) > 0, p{9,10}(3) > 0, p{11}(3) > 0, p{12,13}(5) > 0, p{14}(7) > 0,
p{15}(7) > 0, p∅(j) > 0 for all j = 1, . . . , 15, pD(j) = 0 for all other subsets
of N(j), j = 1, 2, 3, 5, 7. Let π0 = (11, 8, 6, 9, 3, 4, 1, 2, 14, 7, 13, 5, 10, 15, 12).
Although 11, 8, 6, 3, 9 are senior then 1 for π0, DM will use 1 earlier than
these edges because at the initial state {1, 2} edge 1 is senior among available.
All trajectories of maximal length corresponding to π0 and having positive
probabilities are given on Fig.2. In each state an exit action e∗is also available
so there are also shortened trajectories. In Fig. 2 edges in states are listed in
the order of seniority in π0.

Gittins Index Theorem for Randomly Evolving Graphs
575
{14,5}
{5}
{6,7,5}
{7,5}
{5,15}
{13,15,12}
{13,15,12}
{2,5}
{5}
{13,12}
{15,12}
{15,12}
{8,5}
{5}
{13,12}
{12}
{12}
{12}
{12}
{5}
{13,12}
{12}
{2}
{6,7}
{7}
{14}
∆
∆
∆
∆
∆
{8}
{15}
{15}
{7}
{1,2}
∆
∆
∆
{8}
{14}
{15}
{8}
{6,7}
{7}
{14}
{10}
{4,2}
{2}
{6,7}
{10}
{10}
{14,10}
{15}
{3,4,2}
{11,4,2}
{4,2}
{2}
{8,10}
{7,10}
{10,15}
{9,4,2,10}
{4,2,10}
{2,10}
{6,7,10}
x0
x1
x2
x3
x4
x7
x6
x5
x8
x9
Fig. 2. Possible trajectories of maximal length corresponding to π0
It follows from Fig. 2 that a list π1 = (6, 8, 9, 3, 11, 4, 1, 7, 2, 14, 10, 5, 13, 15,
12) defines the same PR as π0.
Each PR can also be specified as follows. Let γ = γ(e) be a function
defined on edges from F0. Then by definition an edge e is senior than e′ if
γ(e) > γ(e′). For simplicity we assume that if e, e′ ∈x for some state x and
e ̸= e′ then γ(e) ̸= γ(e′). In opposite case we assume that from the very
beginning all edges are numbered and for the edges with equal values of γ(·)
a senior is with greater initial number. We call a strategy π a (γ, c)-PR if
{π} = {e : γ(e) ≥c}. In other words π assigns to use each time the edge with
highest value of γ(e) among all available with values greater or equal to c,
and use e∗if there is no available edges with γ(e) ≥c. The value c is called a
cutoffvalue.
Below in Section 8 we consider concrete values of p, q and r for all edges
in the Example. We show that the PR π0 is an optimal strategy in problem
B and it corresponds in particular to γ(i) = αi, where αi are given in Fig 1,
α11 = 11, α8 = 10, α6 = 9, α9 = 8, α3 = 6.4, α4 = 6, α1 ≈5, 05, α2 = 4,
α14 = 3, α7 = 2, α13 = 1, α5 = −1, α10 = −2, α15 = −3, α12 = −4.
Denote the class of all PRs by Π.
For any x ∈S, x ̸= ∅or x∗let us define F(x) = I
e∈x T(e). Given x ∈S
and π ∈Π let us define
F π(x) =
/
e : P π
x {An = e} > 0 for some n ≥0
0
.
(4.1)

576
I. Sonin and E. Presman
Note that F π(x) is also a forest, but some of its leaves can be stems for
the initial forest F0. If x = {e} then F π(e) is a tree and we will denote it
T π(e). Here and in what follows we use the same notation for a forest F and
for the set of edges of F. We say that π ∈Π(x) if {π} = F π(x). Given x ∈S
and π ∈Π we always can assume that π ∈Π(x) eliminating “inaccessible”
edges, i.e. such e ∈{π} that P π
x {An = e} = 0 for all n. If x = {e}, i.e. x
consists only of one edge, we use notation e instead of {e}, for example we
write Π(e), Rπ(e), P π
e and so on. Therefore if π is a (γ, c)-PR and π ∈Π(e)
it means that {π} contains only those edges e′ with γ(e′) ≥c which are
accessible from e.
For example, PR π2 = (1, 3, 10) in Fig. 1 defines the same PR as π3 =
(1, 3, 10, 12) but only π2 ∈Π(x) for x = (1, 2).
On a set of trajectories h = (x0, e0, x1, . . . , ) let us define a stopping time
τ∗= τ∗(h) = min(n : An = e∗or Xn = x∗). Since forest F0 is finite and
any PR uses quit action e∗if there is no available actions, we always have
P π
x {Aτ∗= e∗or Xτ∗= x∗} = 1, for any x ∈S and π ∈Π(x). Thus τ∗can
be described as a random time when either the system runs out of edges in
F π(x), and therefore at this moment an action e∗was chosen (a quit moment),
or at a previous moment some edge e ̸= e∗from F π(x) was chosen and
the transition to x∗has occurred now (at a termination moment). For the
sake of brevity we call τ∗an exit time. Since r(e∗) = 0, we have obviously
Rπ(x) = Eπ
x
τ∗−1
i=0 r(Ai). For any initial state x and PR π let us define
Qπ(x) = P π
x {Xτ∗= x∗},
απ(x) = Rπ(x)
Qπ(x),
(4.2)
where απ(x) = −∞if Qπ(x) = 0.
Note that the probability of final absorption, i.e. limn P π
x (Xn = x∗) equals
to 1 for any PR π. The value Qπ(x) is the probability of termination, i.e.
probability of transition to x∗without using a quit action e∗. Thus Qπ(x) ≥0
and −∞≤απ(x) ≤∞.
Now we define index α(e) for all e. As it was done in [3], we could define
it α(e) = supπ Rπ(e)/Qπ(e) over all π ∈Π(e), but it is more convenient to
specify α(e) recursively as follows. For any leaf e we set α(e) = r(e)/q(e) if
q(e) > 0. If q(e) = r(e) = 0 then we set α(e) = 0. If q(e) > 0, r(e) > 0 or
r(e) < 0 we set α(e) = +∞(or −∞correspondingly. For stems we define
α(e) as follows. If α(·) is not defined for e but is defined for all other elements
of T(e) we set α(e) = supc απc, where πc ≡πc(e) is a PR which first tests e
and after that uses (α, c) -PR from Π(N(e)). Let us denote by π∗(e) the PR
where α(e) is attained. We also will call such PR α -optimizer.
Auxiliary Problem C(e): For an edge e to find π∗(e) and α(e).
Later we present an algorithm to calculate α(e). It requires no more than
n2 operations.
To slightly simplify our proofs sometimes we will assume

Gittins Index Theorem for Randomly Evolving Graphs
577
A uniqueness assumptions U: α(e) ̸= 0 for all e, and if e ̸= e′ then
α(e) ̸= α(e′).
Theorem 1. (a) An (α, 0)-PR is an optimal strategy in the Main Problem
A;
(b) an (α, −∞)-PR is an optimal strategy in the Main Problem B;
(c) an (α, α(e))-PR π, π ∈Π(e) is an optimal strategy in the Auxiliary
Problem C(e).
Under the assumption U the optimal strategies in (a), (b), and (c) are
unique.
If assumption U is not true we can modify the notion of α-PR so that
statements (a)-(c) of Theorem 1 will still hold.
5 One simple idea and three elementary situations
In this section we describe heuristically the key elements of the proof. There
are different proofs of Gittins result (see an interesting paper [14]) but it seems
none of them can be immediately applied to our case. At the same time our
solution is based on a simple key idea, though its implementation in the case
of a random forest is technically cumbersome, and will be presented in the
next section. We describe this idea using as illustrations three elementary sit-
uations, which can be described as three elementary forests. For the simplicity
we will assume that all rewards are positive so a quit action is not at all.
The first situation (a) describes in fact the simplest case of Mitten ele-
mentary model when there are two interchangeable actions a1 and a2. If used,
an action ai brings a reward ri and after that with probability qi the other
action becomes unavailable (the process is terminated), with complimentary
probability decision process may continue. This situation can be described
by a forest consisting of two trees {e1} and {e2}. We must compare two PR
πij, i, j = 1, 2, i ̸= j with corresponding expected rewards Rij. In this case
it is optimal to use first an action with highest index αi = ri/qi. This state-
ment can be checked easily algebraically, but we prefer to demonstrate this as
follows.
First, note that the corresponding probability of termination is the same
for the both orderings, i.e. we have
Q12 = q1 + (1 −q1)q2 = q2 + (1 −q2)q1 = Q21.
(5.1)
This important property in a general situation is proved in Lemma 1 in Section
6. This property implies that to maximize Rij is the same as to maximize
αij = Rij/Qij. Let us consider
α12 = r1 + (1 −q1)r2
q1 + (1 −q1)q2
= α1q1 + α2(1 −q1)q2
q1 + (1 −q1)q2
.
(5.2)

578
I. Sonin and E. Presman
It is easy to see that this is a formula for a center of gravity of two
masses q1 and (1 −q1)q2 located on a horizontal axis with coordinates α1
and α2. The formula for α21 corresponds to a center of gravity for masses
(1 −q2)q1 and q2 with the same coordinates α1 and α2. Since the sum of
masses is the same for both cases, the center of gravity will have higher value
when larger mass will be placed into higher position, i.e.
α12 > α21 iffα1 > α2.
(5.3)
We described situation (a) for two actions but this case implies also that
the similar statement is true for any m interchangeable actions, i.e. for BE
model. This property for a general situation corresponds to Corollary 2, pre-
sented at Section 6.
It is important to observe that the reasoning above does not depend on
whether each actions ai is really one time action or consists of a series of
actions. In the latter case we must calculate corresponding quantities R and
Q for the whole series.
Let us explain heuristically how the index α(e) should be calculated for
the situation (b), when some action is followed by a set of actions, i.e. when a
forest consists of a tree T1 = {e0, e1, e2, ..., em}, where N(e0) = {e1, e2, ..., em},
N(ei) = ∅, i = 1, ..., m, and p0 := pN(e0)(e0) = 1−q(e0)−p∅(e0). The indices
for the leaves of this tree, αi := α(ei), i = 1, 2, .., m are known, α(ei) = ri/qi,
where ri := r(ei), qi := q(ei). Without loss of generality we assume that edges
are numbered in such a way that α1 > α2 > ... > αm.
According to definition, to find α(e0) we have to choose k∗, possibly equal
to zero, that maximizes αk = Rk/Qk, where Rk and Qk are the reward and
termination probability for a PR πk = (e0, e1, e2, ..., ek). Using the notation
β0 = r0/q0, we obtain
αk = r0 + r1p0 + r2p0p1 + . . . + rk
Kk−1
i=0 pi
q0 + q1p0 + q2p0p1 + . . . + qk
Kk−1
i=0 pi
= β0m0 + α1m1 + . . . + αkmk
m0 + m1 + . . . + mk
,
(5.4)
where m0 = q0, mi = (p0 · · · pi−1)qi, i = 1, ..., k. Thus expression αk also
represents a position of a center of gravity for a system of masses and to
find the value k which brings the maximum value to (5.4) we can use the
following
Proposition 1. Suppose that mi are the masses and αi the positions of
these masses on the real line, i = 0, 1, 2, ..., N, and α1 > α2 > ... > αN.
Suppose that our goal is to select a subset Jmax of a set {0, 1, ..., N} which
contains a subset
J0 = {0} and has the largest possible center of gravity.
Then
a) Jmax can be obtained by adding sequentially masses
m1, m2, · · · , to a
set J0 = {0} till the center of gravity of a system Jk = {0, 1, ..., k} will stop
to increase;
b) Jmax = {0} ∪{i : α∗< αi}, where α∗is the center of gravity of Jmax.

Gittins Index Theorem for Randomly Evolving Graphs
579
If there are αi = α∗then Jmax is not unique in an obvious way.
Note that both points of Proposition 1 describe the optimal set: b) de-
scribes it in inexplicit form, since α∗is not known yet, and a) describes it
algorithmically and allows one to calculate α(e0) in situation b) sequentially
step by step.
The proof of Proposition 1 follows from the elementary properties of pro-
portions. (A similar statement was used in a paper by Sonin [11]).
The simplest version of situation b) for m = 1 gives
α1 > β0 iffα1 > β0.
(5.5)
The proof of Theorem 1 in Section 7 is based on the induction with re-
spect to the number of edges, and on Lemma 1, which corresponds to (5.1),
Corollary 1, which corresponds to (5.3), and Corollary 2, which corresponds to
(5.5). These statements are more general than (5.1), (5.3), (5.5) because each
action in Lemma and corollaries consists of some series of actions and after
application some action (which corresponds to some PR) the system transits
to a random set and the choice of the next action depends on this set.
To illustrate this fact and an algorithm of calculation of α(e) consider the
more complicated situation c), when in situation b) one of leaves e1, e2, ..., em,
let say an edge e3, is replaced by a tree T(e3). Then the first two steps of our
procedure of maximization of center of gravity will be the same. Suppose that
the value of α(e3) is achieved on some PR π = (e3, v1, ..., vk) and α(e3) =
R3/Q3. Then in formula (5.4) the value r3 should be replaced by R3 = α(e3)Q3
and correspondingly the mass m3 will be also modified. After that the set
N(e3) will be added to the set of available edges, where N(e3) is the set
of elements of T(e3) which does not belong to π, but follows immediately
elements of π. By the property of α optimizer, all elements of N(e3) have the
values of index less then α(e3), and on the next step we will choose an edge
with maximal value of α in enlarged set of available edges.
6 Auxiliary results
To prove Theorem 1 we introduce some new notations and prove some auxil-
iary statements.
Let π1 and π2 are PR and π1 ∈Π(x). Let us define a new PR from Π(x) -
we denote it π = (π1, π2) - which uses first all available edges from π1 and after
that switches to π2, i.e. all edges in the list π1 are defined now as senior than
all edges in π2. The list π can be obtained as follows. First, list all elements
of π1 in their order and after that list those elements of π2 - in their order -
which does not belong to π1 and which are accessible from x. We call PR π2
a continuation of π1. The similar meaning has notation π = (π1, π2, π3) and
so on.

580
I. Sonin and E. Presman
Remark 1. Let π be a (γ, c)-PR and π1 be a (γ, c1)-PR, where c1 > c.
Then obviously π can be represented as π = (π1, π2), where π2 is a (γ, c)-PR.
For a PR π = (π1, π2) let us define a random time σ = min(n : Xn = x∗
or An ∈{π2}), i.e. a time of termination or first usage of edges from π2. For
the sake of brevity we call time σ a time of switching from π1 to π2.
Remark 2. Note that for any trajectory σ ≤τ∗, but at the same time
P π1
x {Xτ∗= y} = P π
x {Xσ = y} for any y. Equivalently, a moment of termi-
nation for π1 is a moment of switching from π1 to π2 in π.
Using strong Markov property and the total probabilities formula it is easy
to obtain for a π = (π1, π2)
Rπ(x) = Eπ1
x
Bσ−1

i=0
ri + Rπ2(Xσ)
C
= Rπ1(x) +

y
P π1
x (Xσ = y)Rπ2(y). (6.1)
Lemma 1. If
π1, π2 ∈Π(x) and {π1} = {π2}, then
P π1
x {Xτ∗= y} = P π2
x {Xτ∗= y}
(6.2)
for all y ∈S, and, in particular, for y = x∗, i.e. Qπ1(x) = Qπ2(x).
This lemma is an analog of the simple statement that for a set of inde-
pendent trials the probability of at least one success does not depend on the
order in which these trials are tested. We prove this lemma in an Appendix.
Let us call PRs π1 and π2 disjoint if π1 ∈Π(x1), π2 ∈Π(x2), and F(x1)∩
F(x2) = ∅.
Let π1 ∈Π(x1) and π2 ∈Π(x2) are disjoint and π ∈Π. Then for any x,
x1∪x2 ⊂x we can define PRs π12 = (π1, π2, π) and π21 = (π2, π1, π) such that
both belong to Π(x). Where no confusion is possible we will use shorthand
notations Rπi(x) = Ri, Qπi(x) = Qi, απi(x) = αi and so on.
Lemma 2. Consider two PRs πij = (πi, πj, π) ∈Π(x), i, j = 1, 2, i ̸= j,
where π1, π2 are disjoint, and πi ∈Π(xi). Then for any x, x1 ∪x2 ⊂x
Rij = Ri + diRj + R,
(6.3)
where di = 1 −Qi, and the term R is the same for both π12 and π21.
Proof. Given PR πij = (πi, πj, π) let us define σi as the switching moment
from (πi, πj) to π. Since π1 and π2 are disjoint we have {(π1, π2)} = {(π2, π1)}
and therefore by Lemma 1 the distributions P πij
x
{Xσi = y} coincide. Hence,
according to (6.1) the term R is the same for both π12 and π21. The equality
in Lemma 3 follows from formula (6.1) applied to the moments τi of switching
from πi to (πj, π) and the fact that for disjoint PRs the second factor of each
term in the sum 
y P πi
x (Xτi = y)Rπ(y) is the same for all y such that y ̸= x∗
and P πi
x (Xτi = y) ̸= 0.
Notice that any equality for R always implies similar a equality for Q
because Qπ = Rπ if all rewards r(e) are put equal r(e) = q(e). Indeed,

Gittins Index Theorem for Randomly Evolving Graphs
581
let us consider a reward function r′(e, x) defined by r′(ei, xi+1) = 1 if
ei ̸= e∗,
xi+1 = x∗, and r′(ei, xi+1) = 0 otherwise. Then for such func-
tion we have Qπ(x) = Rπ(x). It remains to note that averaging of such r′
gives r(ei) = q(ei).
Therefore, we have an equality similar to (6.3) for Q, and hence
αij = αiQi + αjdiQj + R
Qi + diQj + Q
.
(6.4)
Corollary 1. If under assumptions of Lemma 2 α1 > α2 then α12 > α21
(and therefore R12 > R21).
Proof. The assertion follows from (6.3) and (6.4), using the obvious equal-
ity Q1 + (1 −Q1)Q2 = Q2 + (1 −Q2)Q1.
The next lemma shows how the “isolated tail” of a PR π contributes to
the value of Rπ. If π ∈Π(x) we will omit sometimes the dependence on x of
R, Q and α.
Lemma 3. Let π1 ∈Π(x), π2 ∈Π(e), e /∈{π1}, π = (π1, π2). Then
Rπ(x) = Rπ1(x) + d1Rπ2(e),
(6.5)
where d1 = P π1
x {e ∈Xσ}.
Proof follows directly from the second equality in (6.1) and the relations
Rπ2(y) = Rπ2(e) for e ∈y, and Rπ2(y) = 0 if Xσ = y and e /∈y. Note that
the assumption π2 ∈Π(e) is crucial for validity of (6.5).
According to our remark after Lemma 2, Lemma 3 implies that the formula
similar to (6.1) (with replacement R by Q) holds for Qπ, and hence we have
απ = R1 + d1R2
Q1 + d1Q2
= α1Q1 + α2d1Q2
Q1 + d1Q2
.
(6.6)
Formula (6.6) and elementary properties of proportions imply
Corollary 2. Under the assumptions of Lemma 3 either απ1 = απ2 = απ
or
min{απ1, απ2} < απ < max{απ1, απ2}.
(6.7)
7 Proof of Theorem 1
We prove theorem 1 by induction on the number k of edges in the forest F(x)
of an initial state x. We denote by |C| the number of elements in a finite set C.
For k = 1 the theorem is trivial. Suppose it is proved for all x with |F(x)| ≤k,
and suppose an initial state is x with |F(x)| = k + 1. We consider separately
two cases: (A) when |x| > 1, and (B) when |x| = 1. In both cases we will use a
well-known Bellman Optimality Principle, a corollary of a Bellman equation
for the expected total reward: if π is an optimal strategy (for the problem A

582
I. Sonin and E. Presman
or B) for an initial state x, then after the first step it remains optimal for all
states that follow x. We prove theorem under the Uniqueness assumption U.
The proof for the general case is similar.
Case (A). In this case point (c) of the theorem is trivial since each |T(e)| ≤
k for each e ∈F(x) so, it remains to prove (a) and (b). For any e ∈x
let π0 be an α-PR (with cutoffvalue c = 0 in Problem A and cutoffvalue
c = −∞in Problem B). According to the induction assumption it is an
optimal PR for any state in F(x)\e. So, if π is optimal on F(x), and applies
e on the first step, by Optimality Principle, PR (e, π0) is also optimal. Let
α1 = α(e1) = maxe∈x α(e). Let us show that π = (e, π0) is not optimal if
α = α(e) < α1.
Using the description of π0 by point (a) of Theorem 1 and Remark 1 we
have π = (e, ν1, π1, ν), where ν1 is an α-PR defined on a set T(e)\e with cutoff
value c1 = mine′∈T (e)\e {e′ : α(e′) > α1} > α1; PR π1 is an α-PR with cutoff
value c = α1, and ν is a continuation of α-PR (with cutoffvalue c(ν) = 0 in
Problem A and cutoffvalue c = −∞in Problem B). Note that it is possible
that ν1 = ∅. According to the definitions of α-PR and the value c1, all edges
used by π1 belong to T(e1).
Note that PRs π1 and π2 = (e, ν1) are disjoint because they are defined on
different trees T(e1) and T(e), and that απ2(e) ≤α = α(e) because PR (e, ν1)
can be different than πe which gives a solution to the Auxiliary Problem. Let
us show that PR ϕ = (π1, π2, ν) is better than π = (e, ν1, π1, ν) = (π2, π1, ν).
According to the induction assumption απ1(e1) = α1, so απ1(e1) = α1 > α ≥
απ2(e). Applying Corollary 1 to π1 and π2 we obtain that Rϕ > Rπ, i.e. π is
not an optimal strategy. It means that an optimal strategy either coincides
with (e1, π0) or appoints to quit from the very beginning.
Case (B). In this case x consists only of one edge and we denote it e0. The
first step for any policy is defined uniquely and the resulting state has a forest
with no more than k edges, so by the Optimality Principle the points (a) and
(b) of the Theorem are trivial but point (c) is trivial for all edges except e0.
Let πe0 = (e0, ν), where πe0 be a solution of an Auxiliary Problem for e0,
α-PR ν ∈Π(N(e0)) and c is a corresponding cutoffvalue. Let us show that
1) if e ∈F ν(e0), then α(e) ≥α(e0),
2) if e /∈F ν(e0) and e ∈N(e′) for some e′ which is a leaf of F ν(e0) then
α(e) < α(e0).
This will prove that c can be taken equal to α(e0), i.e. satisfying point (c).
Suppose that 1) is not true and e ∈F ν(e0) is such that α(e) < α(e′)
for all e′ ∈F ν(e0), and α(e) < α(e0.) By the definition of (α, α(e))-PR all
edges that can be used in ν after e belong to T(e). So, PR (e0, ν) can be
represented in a form π = (π1, π2) where π2 ∈Π(e) is an α-PR. Consequently
απ2(e) ≤α(e) < α(e0) = α(e0,ν). But Lemma 3 and Corollary 2 applied to PR
(e0, ν) = (π1, π2) imply that α(e0,ν) < απ1. This contradicts to the definition
of π(e0).

Gittins Index Theorem for Randomly Evolving Graphs
583
Suppose that 2) is not true and we select e ∈N(e′) such that e′ is a leaf of
F ν(e0), α(e) > α(e0) and e is the smallest among such e. Let π2 is (α, α(e))
-PR, π2 ∈Π(e). Consider PR π = (π1, π2), where π1 = (e0, ν). Then π is a
PR with c = α(e). Applying Lemma 1 and Corollary 2 to PR π and using that
απ1(e0) = α(e0) < α(e) = απ2(e) we obtain that α(π) > απ1. This contradicts
to the definition of π1.
8 A recursive algorithm to calculate α(e) and π∗(e)
To formulate the algorithm we first consider the structure of (α, c)-PR πc ∈
Π(x) for an initial state x. Recall that for any PR π and initial state x we can
consider Rπ(x), Qπ(x), F π(x) (or T π(e) if x consists of one edge e) (see (4.1)).
We will consider also N π(x) = N(F π(x)), where N(F) for any subforest of
initial forest F0 denotes the set of all edges that follow immediately “leafs”
of F, i.e. the set of all edges that do not belong to F, but follow immediately
elements of F. For any D ⊂N π(x) (including empty set) we will consider also
the probability pπ
D(x) = P π
x {Xτ∗= D}, i.e. the probability that our decision
to quit was taken at the state D.
Proposition 2. For any x ∈S there exist a natural number k(x), non-
increasing (decreasing in case of Assumption U) numbers
ck = ck(x), with
c0 = +∞, and edges gk = gk(x) ∈F(x), k = 0, 1, · · · , k(x), such that for
(α, c)-PR πc ∈Π(x)
πc = πck for ck+1 < c ≤ck,
ck+1 = α(gk),
πck+1 = (πck, π∗(gk)), for 0 ≤k < k(x);
πc = πck(x) for c ≤ck(x),
(8.1)
where π∗(gk) is α-optimizer of gk. Using indices “k” and “*” instead of index
π for π = πck and π = π∗correspondingly we get: π0(x) = (∅), R0(x) = 0,
Q0(x) = 0, F 0(x) = (∅), N 0(x) = x, p0
x(x) = 1 and if N k(x) ̸= ∅then
F k+1(x) = F k(x)
A
T∗(gk),
(8.2)
N k+1(x) =

N k(x) \ gk
 A
N∗(gk),
(8.3)
Rk+1(x) = Rk(x) + R∗(gk)

D: gk∈D⊂Nk(x),
pk
D(x),
(8.4)
Qk+1(x) = Qk(x) + Q∗(gk)

D: gk∈D⊂Nk(x)
pk
D(x).
(8.5)
If D ⊂N k+1(x) then there exist unique D1 ⊂N k(x)\{gk} and D2 ⊂N∗(gk)
such that D = D1
I D2, and
if D1 = ∅, D2 ̸= ∅, then pk+1
D
(x) = pk
{gk}(x)p∗
D2(gk),
(8.6)

584
I. Sonin and E. Presman
if D2 = ∅, then pk+1
D
(x) = pk
D1(x) + pk
{gk}I
D1(x)p∗
∅(gk),
(8.7)
if D1 ̸= ∅, D2 ̸= ∅, then pk+1
D
(x) = pk
{gk}I
D1(x)p∗
D2(gk).
(8.8)
Proof. For the sake of simplicity we will prove Proposition 2 under Assump-
tion U. The changes for the general case is straightforward. Let for some k ≥0
we know ck, πck, Rk(x), Qk(x), F k(x), N k(x), and pk
D(x) for any D ⊂N k(x).
The set N k(x) corresponds to all potentially available edges after application
of πck. If N k(x) = ∅then k = k(x) and evidently we obtain the last equal-
ity in (8.1). If N k(x) = ∅then according to the definition of (α, c)-PR, all
elements of N k(x) have the value of α less or equal to ck. Consider the edge
in N k(x) with maximal value of α and denote it gk. Denote ck+1 = α(gk).
Since there is no edges in N k(x) with ck+1 < α(e) < ck we have proved the
first equality in (8.1). According to Remark 1 πck+1(x) = (πck, π2), where
π2 ∈Π(gk) is (α, α(gk))-PR. according to statement c) of Theorem 1 this PR
coincides with π∗(gk). It proves third equality in (8.1) and equalities (8.2),
(8.3. Equalities (8.4)-(8.8) are the results of application of total probability
formula. It completes the proof of Proposition 2.
Note that if α(e) is known for all e ∈F(x) then Proposition 2 gives the
algorithm for calculation of optimal value of functional in Main Problems A
and B. In case of Problem B it coincides with Rk(x)(x), and in case of Problem
A it coincides with Rk0(x), where k0 = inf{k : α(gk−1) > 0}.
Now we can formulate algorithm for finding α(e). Recall that we defined
α(e) as r(e)/q(e) for leaves, and if α(e′) is defined for all e′ ∈T(e)\e then as a
maximum of Rπc(e)/Qπc(e) over c, where πc ≡πc(e) is a PR which first tests
e and after that uses (α, c) -PR from Π(N(e)). It is evident that Proposition 2
is valid also for πc(e) with initial values c0 = +∞, π0(e) = (e), R0(e) = r(e),
Q0(e) = q(e), α0(e) = R0(e)/Q0(e), T 0(e) = {e}, N 0(e) = N(e), p0
D(e) =
pD(e) for all D ⊂N 0(e). Define αk(e) = Rk(e)/Qk(e). According to Corollary
2 (see also Proposition 1 and (5.5)) there exists k∗= k∗(e) such that αk(e)
increases for k < k∗and decreases for k > k∗and k∗= inf{k : α(gk) ≤αk}.
It means that for finding α(e) we need to conduct calculations (8.4)-(8.8)
sequentially from k = 0 till the time when α(gk) < αk and set α(e) = αk∗.
Note that if e ∈π∗(e′) for some e′, then we do not need to remember all
data for e. We need remember only the data for e′.
Consider now example 1 with
q(1) = 0.2, p∅(1) = 0.1 p{3,4}(1) = 0.4, p{5}(1) = 0.3, r(1) = 0.8;
q(2) = 0.08, p∅(2) = 0.17, p{6,7}(2) = 0.5, p{8}(2) = 0.25, r(2) = 0.1;
q(3) = 0.1, p∅(3) = 0.24, p3,{9,10}(3) = 0.5, p{11}(3) = 0.16, r3 = 0.2;
q(4) = 0.3, p∅(4) = 0.7, r(4) = 1.8;
q(6) = 0.04, p∅(6) = 0.96, r(6) =
0.36;
q(5) = 0.24, p∅(5) = 0.71, p{12,13}(5) = 0.05, r(5) = −0.3;
q(7) = 0.05, p∅(7) = 0.45, p{14}(7) = 0.5, p{15}(7) = 0.3, r(7) = 0.05;
q(8) = 0.08, p∅(8) = 0.92,
r(8) = 0.8;
q(9) = 0.09, p∅(9) = 0.91,
r(9) = 0, 72;

Gittins Index Theorem for Randomly Evolving Graphs
585
q(10) = 0.7, p∅(10) = 0.3,
r(10) = −1.4;
q(11) = 0.5, p∅(11) = 0.5,
r(11) = 5.5;
q(12) = 0.2, p∅(12) = 0.8,
r(12) = −0.8;
q(13) = 0.6, p∅(13) = 0.4,
r(13) = 0.6;
q(14) = 0.01, p∅(14) = 0.99,
r(14) = 0.3;
q(15) = 0.4, p∅(15) = 0.6,
r(15) = −1.2.
For leaves we have:
α(4) = r(4)
q(4) = 6, α(6) = r(6)
q(6) = 9, α(8) = r(8)
q(8) = 10, α(9) = r(9)
q(9) = 8,
α(10) = r(10)
q(10) = −2, α(11) = r(11)
q(11) = 11, α(12) = r(12)
q(12) = −4,
α(13) = r(13)
q(13) = 1, α(14) = r(14)
q(14) = 3, α(15) = r(15)
q(15) = −3.
To calculate values of α for stems we use the algorithm.
α0(3) = r(3)
q(3) = 2. Since N(3) = {9, 10, 11} and α(11) = 11 > α(9) = 8 >
α0(3) > α(10) = −2, we set g0(3) = 11. Since N(11) = ∅we have from (8.3)-
(8.5): N 1(3) = {9, 10}, R1(3) = r(3)+p{11}(3)r(11) = 0.2+0.16∗5.5 = 1.08,
Q1
3 = q3 +p3,{11}q11 = 0.1+0.16∗0.5 = 0.18. Using (8.7) we get: p1
{9,10}(3) =
p{9,10}(3) = 0.5, p1
∅(3) = p∅(3) + p{g}(3)p∗
∅(11) = 0.24 + 0.16 ∗0.5 = 0.32,
α1(3) = R1(3)
Q1(3) = 1.08
0.18 = 6.
Since N 1(3) = {9, 10} and α(9) = 8 > α1(3) > α(10) = −2, we set g1 = 9.
Since N(9) = ∅we have from (8.3)-(8.5): N 2(3) = {10}, R2(3) = R1(3) +
p1
{9,10}(3)r(9) = 1.08 + 0.5 ∗0.72 = 1.44, Q2(3) = Q1(3) + p1
{9,10}(3)q(9) =
0.18 + 0.5 ∗0.09 = 0.225. Using (8.7) we get:
p2
{10}(3) = p1
{9,10}(3)p∅(9) =
0.5 ∗0.91 = 0.455, p2
∅(3) = p1
∅(3) = 0.32, α2(3) = R2(3)
Q2(3) = 1.44
0.225 = 6.4.
Since N 2(3) = {10} and α(10) = −2 < α2(3) = 6.4 we have: π∗(3) =
π8(3) = (3, 11, 9), N∗(3) = N 2(3) = {10},
R∗(3) = R2(3) = 1, 44, Q∗(3) =
Q2(3) = 0.225, p∗
{10}(3) = p2
{10}(3) = 0.455,
p∗
∅(3) = p2
∅(3) = 0.32, α(3) =
α2(3) = 6.4.
Calculations for the edges 5,7,1, and 2 are absolutely analogous and we
omit them. This calculations give:
π∗(5) = π1(5) = (5, 13), N∗(5) = {12},
R∗(5) = −0.27, Q∗(5) = 0.27,
p∗
{12}(5) = 0.02, p∗
∅(5) = 0.71, α(5) = −1;
π∗(7) = π3(7) = (7, 14), N∗(7) = {15}, R∗(7) = 0.2,
Q∗(7) = 0.1,
p∗
{15}(7) = 0.3, p∗
∅(7) = 0.6, α(7) = 2;
π∗(1) = π6.4(1) = (1, 3, 11, 9, 4), N∗(1) = {5, 10}, R∗(1) = 1, 934, Q∗(1) =
0.383, p∗
{10}(1) = 0.1274, p∗
{5}(1) = 0.3,
p∗
∅(1) = 0.1896,
α(1) =≈5.05;
π∗(2) = π9(2) = (2, 8, 6),
N∗(2) = {7}, R∗(2) = 0, 48, Q∗(2) = 0.12,
p∗
{7}(2) = 0.48, p∗
∅(2) = 0.4, α(2) = 4.

586
I. Sonin and E. Presman
9 Connection with the Gittins index and concluding
remarks
Now we outline how to obtain the proof of the celebrated Gittins result from
Theorem 1. Suppose that there is a fixed number m of finite Markov chains
with transition probabilities pk(i, j), j = 1, 2, ..., m, and a discount factor
β, 0 < β < 1. Each time a DM can engage one of these MC and a reward
rk(i) is obtained if k-th MC was engaged at state i. Without loss of gen-
erality these MCs have common state space S = {1, 2, ..., N} and we can
describe the possible transitions of these MCs using infinite forest F0 which
consists of m trees T1, ..., Tm. The set N(e) = {e1, ..., eN} and partitions of
N(e) = {e1} ∪{e2} ∪...{eN} are the same for each e ∈F0. The probability
p(Nj) for an edge ei ∈Tk is equal to βpk(i, j), and q(e) = (1−β), i.e. we use a
standard way to replace a discount by a transition to an absorbing state. The
reward r(e) = rk(i) if e = ei ∈Tk. We can prove that for any given ε > 0 we
can specify n sufficiently large so that the value function for an initial problem
and a problem with finite forest Fn will be different less than in ε. For such
finite forest we can apply Theorem 1 where the optimality of PR based on
indices all αn(e) was established. It can be proved also that if if e = ei ∈Tk
then limn→∞αn(e) = αk(i), where αk(i) is the value of the classical Gittins
index (GI) for the k-th MC at state i. This proves the optimality of PR based
on GI.
Note also that the value of GI will be obtained as a limit. At the same
time there are algorithms that calculate GI for finite case in a finite number
of steps, e.g in [13]. A new recursive algorithm to calculate GI even in a more
general model is proposed in [12].
Not also that the idea of an infinite forest can be applied to the case of
a countable state space under assumption e.g. that the ratio r(e)/q(e), e ∈F
is bounded by a constant c. Note that this assumption holds for the classical
Gittins case if Markov chain is finite or r(e) is bounded if it is countable.
10 Appendix
Proof of Lemma 1. We prove lemma 1 by induction on n = |{π}|. For n = 1
lemma is trivial. For n = 2 we have {πi} = {e1, e2}. If x contains only one
of these edges then both PRs use this edge on the first step and the other
one on the second, so they coincide. Let ei ∈x for i = 1, 2, then there are
two possible PRs, π1 = (e1, e2), and π2 = (e1, e2). From the definition of
transition probabilities P πi
x {Xτ∗= y} > 0 only if either y = x∗, or y has a
form ykQ = ((x \ (e1, e2)) ∪Nk(e1) ∪NQ(e1)) for some 0 ≤k ≤j(e1), 0 ≤
Q ≤j(e2), and P πi
x {xτ∗= yiQ} = pi(e1)pQ(e2) for i = 1, 2. For y = x∗we
have P πi
x {xτ∗= x∗} = 1 −
y̸=e∗P π1
x {xτ∗= y} for i = 1, 2. This completes
the proof of Lemma 1 for the case |{π}| = 2.

Gittins Index Theorem for Randomly Evolving Graphs
587
Suppose now that (6.2) is proved for n = k, k ≥2, and |{πi}| = k + 1.
Given x ∈S, denote ei the senior edge among edges in x for a PR πi. Then
each πi can be represented as πi = (ei, νi), where νi is a continuation of πi and
|{ν1}| = k. Note that if e1 = e2 then {ν1} = {ν2} and lemma 1 holds because
the first step for both PRs will be the same and after the first step we can
apply an induction assumption to PRs νi. Suppose that e1 ̸= e2. Then let us
introduce two new PRs π′
1 = (e1, e2, ν) and π′
2 = (e2, e1, ν), where ν is a PR
with {ν} = {π} \ {e1, e2}. For two pairs of PRs; π1 and π′
1, and for π2 and π′
2
lemma 1 holds because each pair has the same first edge and we discussed this
case earlier. Thus we have to show that Lemma 1 holds for a pair of PRs π′
1
and π′
2. This pair of PRs is different only for the first two steps but according
to our proof for the case of n = 2 the distributions of X2 coincide. After that
we can apply an induction assumption. This completes the proof of Lemma 1.
Acknowledgement
This work was partly supported by RFBR (grant 03–01–00479).
References
1. Berry, D.A., Fristedt, B.: Bandit problems. Sequential Allocation of Experi-
ments. Monographs on Statistics and Applied Probability. Chapman & Hall,
London (1985)
2. Bellman, R.: A problem in the sequential design of experiments. Sankhya 16,
221–229 (1956)
3. Denardo, E.V., Rothblum, U.G., Van der Heyden, L.: Index policies for stochas-
tic search in a forest with an application to R&D project management. Math.
Oper. Res. 29, no. 1, 162–181 (2004)
4. Feldman, D.: Contributions to the “two-armed bandit” problem. Ann. Math.
Statist. 33, 847–856 (1962)
5. Feinberg E., Schwartz A. (eds): Handbook of Markov Decision Processes. Kluwer
Acad. Publ. (2002)
6. Gittins, J. C.: A Multi-armed Bandit Allocation indices. Wiley , Ney York (1989)
7. Gittins, J.C., Jones, D.M.: A dynamic allocation index for the sequential design
experiments. In: Gani, J., Sarkadi, K., Vince, I. (eds) Progress in Statistics, Eu-
ropean Meeting of Statisticians I. North Holland, Amsterdam, 241–266 (1974).
8. Granot, D., Zuckerman, D.,: Optimal sequencing and resource allocation in re-
search and development projects. Management Science 37, 140–156 (1991)
9. Mitten, L.G.: An analytic solution to the least cost testing sequence problem.
J. of Industr. Eng., 11, no. 1, 17 (1960)
10. Presman, E.L., Sonin, I.M.: Sequential Control with Incomplete Information.
The Bayesian Approach to Multi-armed Bandit Problems. Academic Press
(1990)
11. Sonin, I.M.: Increasing the reliability of a machine reduces the period of its
work. J. Appl. Probab. 33, no. 1, 217–223 (1996)

588
I. Sonin and E. Presman
12. Sonin, I.M.: A Generalized Gittins index for Markov chain and its recursive
calculation. Manuscript (2004)
13. Varaiya, P., Walrand J., Buyukkoc, C.: Extensions of the multiarmed bandit
problem: the discounted case. IEEE Trans. Autom. Control AC-30, no. 5, 426–
439 (1985)
14. Weiss, G.: Branching bandit processes. Probability in the Engineering and In-
formation Sciences 2, 269–278 (1988)
15. Whittle, P.: Arm-acquiring bandits. Annals of Probability 9, 284–292 (1981)

On the Existence of Optimal Portfolios for the
Utility Maximization Problem in Discrete
Time Financial Market Models ∗
Mikl´os R´ASONYI and `Lukasz STETTNER
Computer and Automation Institute Hungarian Academy of Sciences,
1111 Budapest, Kende utca 13-17, Hungary.
rasonyi@sztaki.hu
Institute of Mathematics, Polish Academy of Sciences, ´Sniadeckich 8, 00-950
Warsaw, Poland.
stettner@impan.gov.pl
Summary. We consider an investor whose preferences are described by a concave
nondecreasing function U : (0, ∞) →R and prove that in an arbitrage-free discrete-
time market model there is a strategy attaining the supremum of expected utility
at the terminal date provided that this supremum is finite.
Key words: utility function, portfolio optimization, dynamic programming
Mathematics Subject Classification (2000): 93E20, 91B28, 91B16
1 Introduction and main result
In this paper we study the existence of optimal portfolios for maximizing
expected utility of the terminal wealth. His or her preferences are described
by a concave nondecreasing function U : (0, ∞) →R, trading dates occur at
discrete time instants.
Recently, [8, 9] have treated the same problem, concentrating rather on the
construction of pricing operators using optimal strategies. In this paper we
apply the machinery which was developed in [7] for utility functions U : R →R
and establish the existence of optimal strategies under minimal conditions (U
is concave nondecreasing, absence of arbitrage, the value function is finite).
This general theorem has already been anticipated in Section 3.1 of [3] where
the authors proved it for a one-step model and nonnegative price process.
∗L. Stettner was supported by PBZ KBN 016/P03/99; M. R´asonyi by OTKA
grant T 047193 and F049094.

590
M. R´asonyi and ^L. Stettner
A usual setting for discrete-time market models is considered: a probability
space (Ω, F, P); a filtration (Ft)0≤t≤T such that F0 contains P-null sets and
a d-dimensional adapted process (St)0≤t≤T describing the prices of d risky
assets in a given economy.
It is implicitly assumed that investors also dispose of a risk-free asset
S0
t := 1, 0 ≤t ≤T; hence trading strategies can be arbitrary d-dimensional
predictable processes (ϕt)1≤t≤T , where ϕi
t denotes the investor’s holding in
asset i at time t. Predictability means that ϕt is Ft−1-measurable, i.e. the
portfolio is chosen before new prices St are revealed. Let Φ denote the family
of all predictable trading strategies.
The value of a portfolio ϕ starting from initial capital c is given by
V c,ϕ
t
= c +
t

i=1
⟨ϕi, ∆Si⟩,
where ⟨·, ·⟩denotes scalar product in Rd, ∆Si := Si −Si−1 and c > 0.
Introduce for each t = 1, ..., T a random subset Dt(ω) of Rd: the affine hull
of the support of the (regular) conditional distribution of ∆St given Ft−1, see
Proposition 4.1.
In this paper we impose the following (fairly natural) trading constraint:
portfolio value should not become negative. Define for c > 0 the set of admis-
sible trading strategies as
A(c) := {ϕ ∈Φ : V c,ϕ
t
≥0 a.s., 0 ≤t ≤T}.
(1.1)
In what follows, Ξt will denote the set of Ft-measurable d-dimensional
random variables. When a date t is fixed, ϕt is called admissible for the initial
capital x if ϕt ∈Ξx
t−1, where
Ξx
t := {ξ ∈Ξt : x + ⟨ξ, ∆St+1⟩≥0 a.s.},
x ∈[0, ∞).
Define for any Ft-measurable nonnegative random variable H
Ξt(H) := {ξ ∈Ξt : H + ⟨ξ, ∆St+1⟩≥0 a.s.},
and also
˜Ξt := {ξ ∈Ξt : |ξ(ω)| = 1, ξ(ω) ∈Dt+1(ω) a.s.}.
Assumption 1.1 U : (0, ∞) →R is a concave nondecreasing function.
We extend U by continuity to zero (U(0) = U(0+) may be −∞) and set
U(x) = −∞, x < 0. By convention, U ′(x) denotes the left-hand derivative of
U at x; U + is the positive part of U.
We are dealing with maximizing the expected utility of the terminal
wealth:
EU(V c,ϕ
T
) →max,
ϕ ∈A(c).
(1.2)

On the Existence of Optimal Portfolios
591
So as to have a well-posed problem the following absence of arbitrage (NA)
property will be imposed:
(NA)
∀c > 0 ∀ϕ ∈A(c) (V c,ϕ
T
≥c a.s. =⇒V c,ϕ
T
= c a.s.).
(1.3)
Theorem 1.1. Let Assumption 1.1 hold and let S satisfy (1.3). Suppose that
the expectations in the definition below exist (though might take the value −∞)
u(c) :=
sup
ϕ∈A(c)
EU(V c,ϕ
T
),
(1.4)
and
u(c) < ∞for all c ∈(0, ∞).
(1.5)
Then for each c ∈(0, ∞) there exists a strategy ϕ∗(c) satisfying
u(c) = EU(V c,ϕ∗(c)
T
),
moreover one has ϕ∗
t (c) ∈Dt a.s.
We will present the proof of Theorem 1.1 in Sections 2 and 3. A possible
extension (Theorem 3.1) to random utility functions is sketched in Remarks
2.2 and 3.1.
Remark 1.1. In fact, it is sufficient to suppose that there exists c > 0 such
that u(c) < ∞. In this case Lemma 2.2 entails that for any strategy ϕ and
any λ ≥1 we have the bound
U +(V λc,ϕ
T
) ≤2λ[U +(V c,ϕ/λ
T
) + U(2)],
with the right-hand side having a finite expectation as u(c) < ∞. This means
that for any c′ > c the expectations in the definition (1.4) of u(c′) exist. It is
easy to see that u(·) is concave, hence if we had u(c′) = ∞for some c′ > c
then
u (c/2) = u(αc′ + (1 −α)c/4) ≥αu(c′) + (1 −α)u(c/4) = ∞,
where α ∈(0, 1) is a suitable number. But this is impossible, as by monotonic-
ity
u (c/2) ≤u(c) < ∞.
Remark 1.2. Theorem 1.1 fails to be true in general semimartingale models.
As it was shown by counterexamples of [6], in the continuous-time case certain
additional properties have to be imposed on U to guarantee the existence of
optimal strategies.
We mention a uniqueness result whose proof is omitted as it is identical
to that of Theorem 2.8 in [7].

592
M. R´asonyi and ^L. Stettner
Theorem 1.2. If U is strictly concave then there is a unique optimal strategy
ϕ∗satisfying
ϕ∗
t ∈Dt a.s.
We will need an alternative characterization of (NA), see the Proposition
below. This statement is implicit in Theorem 3 of [4], where it is shown that
absence of arbitrage is equivalent to the fact that the origin lies in the relative
interior of the convex hull of the support of conditional distribution of ∆St
given Ft−1. We make this more explicit and “quantitative”:
Proposition 1.1. Under (NA) the set Dt(ω) is a linear subspace of Rd, al-
most surely. The (NA) condition implies the existence of Ft-measurable ran-
dom variables βt, κt > 0, 0 ≤t ≤T −1, such that for any p ∈˜Ξt
P(⟨p, ∆St+1⟩< −βt|Ft) ≥κt
(1.6)
almost surely.
Proof. The “standard” absence of arbitrage property is the following
(NA’)
∀ϕ ∈Φ (V 0,ϕ
T
≥0 a.s. ⇒V 0,ϕ
T
= 0 a.s.)
It follows from Theorem 3 of [4] and Proposition 3.3 of [7] that if (NA’) holds
then Dt is a linear subspace and (1.6) holds. So it suffices to establish that
(NA) and (NA’) are equivalent. The (NA’) condition trivially implies (NA)
since if we had a ϕ violating (NA) we would immediately get
V 0,ϕ
T
= V c,ϕ
T
−c ≥0,
P(V 0,ϕ
T
> 0) > 0,
which contradicts (NA’). The other direction is also clear: if there is ϕ such
that (NA’) fails then we know from the implication (b) ⇒(a) of Theorem 3
in [4] that there is ψ such that V 0,ψ
t
≥0, 0 ≤t ≤T and P(V 0,ψ
T
> 0) > 0.
For such a strategy
V c,ψ
t
≥c a.s., 0 ≤t ≤T,
P(V c,ψ
T
> c) > 0,
so ψ ∈A(c) and (NA) is violated.
2 Optimal strategy in the one-step case
Let V : [0, ∞) × Ω→R ∪{−∞} be a function such that for almost all ω,
V (·, ω) is a nondecreasing continuous concave function, V (x, ω) is finite for
x ∈(0, ∞) and V (x, ·) is F-measurable for any fixed x. Let H ⊂F be a
σ-algebra containing P-null sets. Let Y be a d-dimensional random variable.
Denote by Ξ the family of H-measurable d-dimensional random variables. Put

On the Existence of Optimal Portfolios
593
˜Ξ := {ξ ∈Ξ : |ξ(ω)| = 1, ξ(ω) ∈D(ω) a.s.},
Ξx := {ξ ∈Ξ : x + ⟨ξ, Y ⟩≥0 a.s.}, x ∈[0, ∞),
here D denotes the smallest affine subspace containing the support of the
conditional distribution of Y with respect to H (see Section 4). We suppose
that D is actually a linear subspace a.s. and that
P(⟨p, Y ⟩< −δ|H) ≥κ, for all p ∈˜Ξ,
(2.1)
with some H-measurable random variables κ, δ > 0.
Introduce also
ΞH := {ξ ∈Ξ : H + ⟨ξ, Y ⟩≥0 a.s.},
for each H-measurable nonnegative random variable H.
This setting will be applied in Section 3 with H = Ft−1, D = Dt, and
Y = ∆St; V will be the supremum of conditional expected utility if trading
begins at time t.
Assume that
V (1) ≥0 a.s.
(2.2)
and for all x ∈[0, ∞)
ess. sup
ξ∈Ξx E(V (x + ⟨ξ, Y ⟩)|H) < ∞
a.s.
(2.3)
We need some preparatory results.
Proposition 2.1. Let ξ ∈Ξx be fixed. There exists a version of
y →E(V (y + ⟨ξ, Y ⟩)|H), y ≥x,
such that it is a nondecreasing upper semicontinuous concave function (per-
haps taking the value −∞), for almost all ω.
Proof. Fix a version of F(q, ω) := E(V (q +⟨ξ, Y ⟩)|H) for q ∈Q+. The follow-
ing inequalities hold almost surely for any pairs q1 ≤q2 of rational numbers:
F(q1) ≤F(q2),
F(q1 + q2
2
) ≥F(q1) + F(q2)
2
.
Let us fix a P-zero set N such that outside this set the above inequalities
hold. Fix y ∈[x, ∞) and take rationals qn ց y. The monotone convergence
theorem yields
F(y+) = lim
n F(qn) = lim
n E(V (qn + ⟨ξ, Y ⟩)|H) =
E(V (y + ⟨ξ, Y ⟩)|H), a.s.
showing that the right-continuous pathwise extension of F is as required.

594
M. R´asonyi and ^L. Stettner
Remark 2.1. If E(V (x + ⟨ξ, Y ⟩)|H) is almost surely finite then, by concavity,
we get an almost surely continuous version from the above proposition.
Proposition 2.2. Let x > 0, ξ ∈Ξx. Let ˆξ(ω) be the orthogonal projection
of ξ(ω) on the subspace D(ω). Then ˆξ ∈Ξx. Furthermore,
E(V (x + ⟨ˆξ, Y ⟩)|H) = E(V (x + ⟨ξ, Y ⟩)|H),
almost everywhere.
Proof. To check that
x + ⟨ˆξ, Y ⟩≥0 a.s.
(2.4)
we proceed as follows: take a regular version µ(dx, ω) of P(Y ∈dx|H). Notice
that for almost all ω:
supp µ(·, ω) ⊂D(ω),
µ({y : x + ⟨ξ(ω), y⟩≥0}, ω) = 1,
so necessarily
µ({y : x + ⟨ˆξ(ω), y⟩≥0}, ω) = 1,
which shows (2.4). For the rest of this technical proof we refer to Proposition
4.6 of [7].
Lemma 2.1. Let us fix x0 > 0. There exists a H-measurable random variable
K = K(x0) > 0 such that for any x ≤x0 and ξ ∈Ξx satisfying ξ ∈D we
have |ξ| ≤K almost surely.
Proof. Indeed, we know from (2.1) that if |ξ| > x0/δ then necessarily for any
x ≤x0
P(x + ⟨ξ, Y ⟩< 0|H) ≥κ > 0,
which means that ξ /∈Ξx, hence we may set K := x0/δ.
When showing the existence of an optimal strategy we will use a Fatou-
lemma argument for which we need the two lemmata below.
Lemma 2.2. Let V : (0, ∞) →R be a concave nondecreasing function such
that V (1) ≥0. Then for all x > 0 and λ ≥1
V +(λx) ≤2λ[V +(x) + V (2)].
Proof. First let us suppose x ≥2. In this case
V +(λx) = V (λx) ≤V (x) + V ′(x)(λx −x) ≤
V (x) + V (x) −V (1)
x −1
x(λ −1) ≤V (x) + 2(λ −1)(V (x) −V (1)) ≤
2λV (x),

On the Existence of Optimal Portfolios
595
where we used the concavity and the inequalities x ≥2 and V (x) ≥V (1) ≥0.
For x < 2 by monotonicity
V +(λx) ≤V (2λ) ≤2λV (2).
Putting these estimations together, we get, for any x > 0, that
V +(λx) ≤2λ max{V (2), V +(x)} ≤2λ[V +(x) + V (2)],
as desired.
Lemma 2.3. Fix x > 0. There exists a nonnegative random variable L such
that for any ξ ∈Ξx, ξ ∈D
V +(x + ⟨ξ, Y ⟩) ≤L,
E(L|H) < ∞a.s.
(2.5)
Proof. Take the random set M(ω, x) of Proposition 4.2 and its linear span
R(ω, x), see Proposition 4.3. It suffices to carry out the majoration separately
on the sets
Ak := {ω : dim R(ω) = k} ∈H,
0 ≤k ≤d,
i.e. finding Lk such that
V +(x + ⟨ξ, Y ⟩)IAk ≤Lk,
E(Lk|H) < ∞.
The case k = 0 being trivial we may and will suppose that dim R = m ≥1
is a fixed constant. Let the Rd-valued random variables ζj, 1 ≤j ≤m, be
such that they form a (random) orthonormal bases of R, almost surely. Define
W := {−1, +1}m and introduce the vectors
θi :=
m

j=1
i(j)ζj,
i ∈W.
It is clear from Lemma 2.1 that M(x) is contained in the m-dimensional cube
with edges Kθi, i ∈W, almost surely. As a linear function defined on a
polyhedral set attains its maximum on the extreme points, we immediately
have for all selectors ξ ∈M(x), i.e. for any ξ ∈Ξx, ξ ∈D
x + ⟨ξ, Y ⟩≤
@
i∈W
(x + K⟨θi, Y ⟩) a.s.
So by monotonicity
V (x + ⟨ξ, Y ⟩) ≤
@
i∈W
V (x + K⟨θi, Y ⟩) a.s.
Thus,
V +(x + ⟨ξ, Y ⟩) ≤

i∈W
V +(x + K⟨θi, Y ⟩) a.s.
(2.6)

596
M. R´asonyi and ^L. Stettner
The relative interior ri M is also a random set by Proposition 4.3. Let ρ be
an H-measurable selector of ri M. Then the projection on Ωof each set
Bi := {(ω, a) ∈Ω× (0, 1] : ρ + a(Kθi −ρ) ∈M(x)} ∈H ⊗B((0, 1]),
i ∈W,
is of full measure. Hence Bi admit H-measurable selectors ψi. Now Lemma
2.2 implies that
V +(x + K⟨θi, Y ⟩) = V +(x + ⟨ρ, Y ⟩+ ⟨Kθi −ρ, Y ⟩) ≤
(2.7)
2 1
ψi
[V +(ψi(x + ⟨ρ, Y ⟩) + ψi⟨Kθi −ρ, Y ⟩) + V (2)] ≤
2
ψi
[V +(x + ⟨ρ, Y ⟩+ ⟨ψi(Kθi −ρ), Y ⟩) + V (2)],
i ∈W.
where we used Lemma 2.2, monotonicity of V , ψi ≤1 and ρ ∈Ξx. Define
L := 2

i∈W
1
ψi
[V +(x + ⟨ρ, Y ⟩+ ⟨ψi(Kθi −ρ), Y ⟩) + V (2)].
As ψi is chosen in such a manner that
ρ + ψi(Kθi −ρ) ∈M(x),
i ∈W,
we have, using (2.3)
E(L|H) = 2

i∈W
1
ψi
E(V +(x + ⟨ρ, Y ⟩+ ⟨ψi(Kθi −ρ), Y ⟩)|H)+
+2m+1E(V (2)|H) < ∞.
The bounds (2.6) and (2.7) imply (2.5).
Now a regular version of the essential supremum is shown to exist.
Proposition 2.3. There is a function G : [0, ∞) × Ω→R ∪{−∞} which is
a version of
ess. sup
ξ∈Ξx E(V (x + ⟨ξ, Y ⟩)|H)
for each fixed x ∈[0, ∞); nondecreasing, concave, continuous on [0, ∞) and
finite valued for x ∈(0, ∞), for almost all ω.
Proof. Take a version G(q, ω) of the essential supremum, for q ∈Q+. As
0 ∈Ξx for all x, E(V (x + ⟨ξ, Y ⟩)|H) is almost surely finite-valued for each
x ∈(0, ∞). Outside a P-null set the monotonicity and convexity relations
G(q1) ≤G(q2), if q1 ≤q2,
G
1
2 (q1 + q2)

≥G(q1) + G(q2)
2
, q1, q2 ∈Q+,

On the Existence of Optimal Portfolios
597
hold, hence on a set of probability one we may extend G by monotonicity to
a nondecreasing concave function on (0, ∞) which is finite-valued (and hence
continuous).
Take any x ∈(0, ∞) and two sequences of rationals qn ր x, rn ց x. As
for y ≤z the relation Ξy ⊆Ξz holds, we get that
ess. sup
ξ∈Ξx E(V (x + ⟨ξ, Y ⟩)|H) ≥lim sup
n
G(qn) = G(x),
ess. sup
ξ∈Ξx E(V (x + ⟨ξ, Y ⟩)|H) ≤lim inf
n
G(rn) = G(x),
showing that G(x) is a version of the essential supremum for each x ∈(0, ∞).
By construction G(0) is a version of the essential supremum at x = 0, so it
remains to check the continuity of G at zero, i.e. the equality
lim
l→∞ess. sup
ξ∈Ξ1/l E(V (1/l + ⟨ξ, Y ⟩)|H) = ess. sup
ξ∈Ξ0 E(V (⟨ξ, Y ⟩)|H).
(2.8)
The limit exists by monotonicity on a set of probability one and certainly
greater than or equal to the right-hand side above. The particular structure
of the family whose essential supremum is taken guarantees that for each l ∈N
there exists ηl ∈Ξ1/l such that
|ess. sup
ξ∈Ξ1/l E(V (1/l + ⟨ξ, Y ⟩)|H) −E(V (1/l + ⟨ηl, Y ⟩)|H)| ≤1/l
a.s.
We may supppose ηl ∈D by Proposition 2.2. Then Lemmata 2.1 and 4.1
imply that a random subsequence ηlk exists such that ηlk →˜η a.s., as k →∞
and ˜η ∈∩x>0Ξx = Ξ0. The continuity of V , Lemma 2.3 and the Fatou lemma
guarantee that
lim
k→∞E(V (1/lk + ⟨ηlk, Y ⟩)|H) ≤E(V (⟨˜η, Y ⟩)|H) ≤ess. sup
ξ∈Ξ0 E(V (⟨ξ, Y ⟩)|H),
hence assertion (2.8) follows.
We construct a sequence of strategies converging to the optimal value for
all x ∈(0, ∞).
Lemma 2.4. There exist B(R+) ⊗H-measurable functions ξn(x, ω) and suit-
able versions Gn(x, ω) of
E(V (x + ⟨ξn(x), Y ⟩)|H),
such that outside a fixed P-null set we have for all x ∈(0, ∞)
lim
n→∞Gn(x) = G(x),
(2.9)
and the limit is attained in a nondecreasing way.

598
M. R´asonyi and ^L. Stettner
Proof. It suffices to prove this for x ∈[1, 2); in an analogous way we get
sequences ξn for all the intervals [n, n + 1), [1/(n + 1), 1/n), n ∈N, and then
by ”pasting together” we finally get an approximation along all the positive
axis.
Fix a version G(·, ω) of the essential supremum given by Proposition 2.3.
First notice that, for fixed x ∈(0, ∞), the family of functions
E(V (x + ⟨ξ, Y ⟩)|H), ξ ∈Ξx,
(2.10)
is directed upwards, so there is a sequence ηn(x) ∈Ξx such that
lim
n→∞↑E(V (x + ⟨ηn(x), Y ⟩)|H) = ess. sup
ξ∈Ξx E(V (x + ⟨ξ, Y ⟩)|H),
almost surely. Let us fix such a sequence for each dyadic rational q ∈[1, 2).
Now set
ξ0(x, ω) := 0.
Let us suppose that ξ0, . . . , ξn−1 have been defined, as well as ξn(x, ω) for
x ∈[1, 1 + k/2n) for some 0 ≤k ≤2n −1. If k = 0 we set ξn(x, ω) := κ0
n for
x ∈[1, 1 + 1/2n), where κ0
n is chosen such that
E(V (1 + ⟨κ0
n, Y ⟩)|H)
≥E (V (1 + ⟨ξn−1(1), Y ⟩) |H) ∨E (V (1 + ⟨ηn(1), Y ⟩) |H) .
If 1 ≤k ≤2n −1 we set
ξn(x, ω) := κk
n(ω),
x ∈

1 + k
2n , 1 + k + 1
2n

,
where κk
n ∈Ξ1+k/2n is chosen in such a way that almost everywhere
E(V (1 + k/2n + ⟨κk
n, Y ⟩)|H) ≥uk
n ∨vk
n ∨wk
n.
(2.11)
Here we use the notations
uk
n := E

V

1 + k
2n +
O
ξn

1 + k −1
2n

, Y
P H

,
vk
n := E

V

1 + k
2n +
O
ηn

1 + k
2n

, Y
P H

,
wk
n := E

V

1 + k
2n +
O
ξn−1

1 + k
2n

, Y
P H

.
This is possible, as the family (2.10) is directed upwards and Ξy ⊆Ξz for
y ≤z. The latter fact implies also that actually κk
n ∈Ξy for y from the
interval [1 + k/2n, 1 + (k + 1)/2n), so ξn(x) ∈Ξx for all x ∈[1, 2).
Using Propositions 2.1 and 2.3 as well as (2.11) it is easy to see that there
is a P-null set N such that outside this set G(·, ω) is continuous and suitable
versions Gn(·, ω) of

On the Existence of Optimal Portfolios
599
E(V (x + ⟨ξn(x), Y ⟩)|H)(ω)
are nondecreasing and continuous on subintervals of the form [1 + k/2n, 1 +
(k + 1)/2n), 0 ≤k ≤2n −1, for all n ∈N. By the definitions of ηn(x) and
ξn(x) we see immediately that (outside another P-null set N ′) for all dyadic
rationals q ∈[1, 2)
G(q) = lim
n→∞↑Gn(q).
Consequently, outside N ∪N ′ the sequence Gn(x) is nondecreasing in n, for
all x ∈[1, 2). For any x ∈[1, 2) and dyadic rationals q1 < x < q2,
Gn(q1) ≤Gn(x) ≤Gn(q2)
outside N, so necessarily
G(q1) ≤lim inf
n
Gn(x) ≤lim sup
n
Gn(x) ≤G(q2),
outside N ∪N ′. The function G being continuous at x, we get almost sure
convergence to G in all points x ∈[1, 2).
The following lemma contains the actual construction of the one-step op-
timal strategy.
Lemma 2.5. There exists a B(R+)⊗H-measurable function ˜ξ(x, ω) such that
for each x ∈(0, ∞)
E(V (x + ⟨˜ξ(x), Y ⟩)|H) = ess. sup
ξ∈Ξx E(V (x + ⟨ξ, Y ⟩)|H).
Proof. It suffices to prove this, e.g., when x ∈[1, 2), then one can ”paste
together” the optimal strategy for x ∈(0, ∞). We take an approximating
sequence ξn as provided by Lemma 2.4, then change to the projections ˆξn
figuring in Proposition 2.2. Using Proposition 2.1 and the structure of the
approximating sequence one can see that Gn is a version of
E(V (x + ⟨ˆξn, Y ⟩)|H),
and almost surely
E(V (x + ⟨ˆξn, Y ⟩)|H) →G(x), for all x ∈[1, 2).
Then take x0 := 2 and apply Lemma 2.1. It follows that, almost surely,
|ˆξn(x)| ≤K(x0), for all x ∈[1, 2).
Now use Lemma 4.1 to find a random subsequence ˜ηk := ˆξnk of ˆξn con-
verging to some ˜ξ. Apply the Fatou lemma (we shall justify its use in a while):
E(V (x + ⟨˜ξ(x), Y ⟩)|H) ≥lim sup
k→∞
E(V (x + ⟨˜ηk(x), Y ⟩)|H).

600
M. R´asonyi and ^L. Stettner
By the structure of the random subsequence in Proposition 4.1
E(V (x + ⟨˜ηk(x), Y ⟩)|H) ≥E(V (x + ⟨ξnk(x), Y ⟩)|H),
so the construction of the approximating sequence in Lemma 2.4 implies that
for all x
E(V (x + ⟨˜ξ(x), Y ⟩)|H) ≥G(x) a.s.
hence by the definition of G
E(V (x + ⟨˜ξ(x), Y ⟩)|H) = G(x) a.s.
It remains to check that we were allowed to invoke the Fatou lemma. This
follows from Lemma 2.3, the random variable L figuring there is a suitable
majorant.
Proposition 2.4. The ˜ξ constructed in the proof of Lemma 2.5 is such that
˜ξ(H) ∈ΞH and
G(H) = E(V (H + ⟨˜ξ(H), Y ⟩)|H) = ess. sup
ξ∈ΞH E(V (H + ⟨ξ, Y ⟩)|H) a.s.,
for any H-measurable [0, ∞)-valued random variable H; here G is the function
constructed in Proposition 2.3.
Proof. By the piecewise constant structure of the approximating sequence of
Lemma 2.4 we have that
P(∀x ∀n
x + ⟨ˆξn(x, ω), Y ⟩≥0) = 1.
Random subsequences do not change this, so
P(∀x
x + ⟨˜ξ(x, ω), Y ⟩≥0) = 1,
which implies that ˜ξ(H) ∈ΞH.
For the proof of “≤” in the first equality we refer to Proposition 4.10 of
[7]. The left-hand side of the second equality is clearly not greater than the
right-hand side, so we need only to show that for fixed ξ ∈ΞH we have:
G(H, ω) ≥E(V (H + ⟨ξ, Y ⟩)|H) a.s.
(2.12)
For step functions H (2.12) is clearly true. Now for general H take a decreasing
step-function approximation Hn of H. Then ξ ∈ΞH ⊆ΞHn for all n, hence
G(Hn) ≥E(V (Hn + ⟨ξ, Y ⟩)|H) a.s.,
the left-hand side converges by path regularity of G, the right-hand side by
monotone convergence, so (2.12) is proved.

On the Existence of Optimal Portfolios
601
Remark 2.2. Results of the present section may be extended to a slightly more
general setting. We briefly sum up the major modifications.
Let V : [0, ∞) × Ω→R ∪{−∞} be a function such that V (x, ·) is F-
measurable for each x and for almost all ω the function V (·, ω) is nondecreas-
ing, concave and upper semicontinuous. Put
Θ(ω) := 0 ∨sup{q ∈Q+ : V (q, ω) = −∞}.
Assume that Θ is a bounded random variable and introduce the random
variable
θ := ess. inf{X : σ(X) ⊂H, ∃ϕ ∈Ξ s.t. X + ⟨ϕ, Y ⟩≥Θ a.s.}.
Redefine ΞH for each H-measurable H ≥θ as
ΞH := {ξ ∈Ξ : H + ⟨ξ, Y ⟩≥Θ a.s.}.
Replace (2.3) by
∀x ∈[0, ∞)
ess.
sup
ξ∈Ξθ+x E(V (x + ⟨ξ, Y ⟩)|H) < ∞
and (2.2) by
V (F) ≥0,
(2.13)
where F > 0 is some constant. Otherwise let the notations and hypotheses at
the beginning of this section be valid.
One needs to construct regular versions of
y →E(V (θ + y + ⟨ξ, Y ⟩)|H), y ≥x,
for ξ ∈Ξθ+x in Proposition 2.1.
Proposition 2.2 and Lemma 2.1 remain almost unchanged except for re-
placing Ξx by Ξx+θ. The estimation of Lemma 2.2 is slightly modified due to
(2.13), Lemma 2.3 remains practically the same.
Instead of Proposition 2.3 one has to establish the following:
Proposition 2.5. There is a function G : [0, ∞) × Ω→R ∪{−∞} such that
G(θ + y) is a version of
ess.
sup
ξ∈Ξθ+y E(V (θ + y + ⟨ξ, Y ⟩)|H)
for each fixed y ∈[0, ∞); G(x, ω) = −∞if x < θ(ω), G(·, ω) is a nondecreas-
ing, concave, continuous function on [θ(ω), ∞) and finite-valued on (θ(ω), ∞),
for almost all ω.
In Lemma 2.4 the approximating sequence should be constructed on the
random interval (θ, ∞). Then along the same arguments we finally get:
Proposition 2.6. There exists a B(R) ⊗H-measurable function ˜ξ such that
for any H-measurable random variable H ≥θ we have ˜ξ(H) ∈ΞH and
G(H) = E(V (H + ⟨˜ξ(H), Y ⟩)|H) = ess. sup
ξ∈ΞH E(V (H + ⟨ξ, Y ⟩)|H),
almost surely.

602
M. R´asonyi and ^L. Stettner
3 Dynamic programming
From now on we suppose that
U(1) = 0.
(3.1)
This is to assure (2.2), which plays a role in Lemma 2.2. Obviously there is no
loss of generality here: by adding a constant to the utility function one may
always have (3.1) without changing the optimal strategy.
Define by recursion the following random functions. The existence of the
conditional expectations will be shown in Proposition 3.1 below. Set
UT (x, ω) := U(x),
x ∈[0, ∞),
ω ∈Ω,
(3.2)
and, for t < T,
Ut(x, ω) := ess. sup
ξ∈Ξx
t
E(Ut+1(x + ⟨ξ, ∆St+1⟩)|Ft)(ω), x ∈[0, ∞), ω ∈Ω;
(3.3)
later on we shall omit the dependence on ω in notations. Set Ut(x) := −∞,
x < 0.
Proposition 3.1. The functions Ut, 0 ≤t ≤T, have versions which are
almost surely nondecreasing, concave and continuous on [0, ∞), finite-valued
on (0, ∞) and
Ut(1) ≥0, 0 ≤t ≤T,
(3.4)
ess. sup
ξ∈Ξx
t−1
E(Ut(x + ⟨ξ, ∆St⟩)|Ft−1) < ∞, x ∈[0, ∞), 1 ≤t ≤T,
(3.5)
where the expectations are well-defined. There exist B(R+) ⊗Ft-measurable
functions ˜ξt+1, 0 ≤t ≤T −1, such that for all x ∈(0, ∞)
Ut(x, ω) = E(Ut+1(x + ⟨˜ξt+1(x), ∆St+1⟩)|Ft).
(3.6)
Proof. Going backwards from T to 0, we apply Lemma 2.5 with V := Ut,
H = Ft−1, D := Dt, Y := ∆St.
We need to verify the conditions of Section 2: D is a random subspace by
Propositions 1.1 and 4.1; (2.1) follows from (1.6); (2.2) and (2.3) will come
from (3.4) and (3.5). We will check (3.4) and (3.5) in a little while.
Expectations exist by (2.3), a good version for Ut is provided by Proposi-
tion 2.3. Denote the resulting ˜ξ of Lemma 2.5 by ˜ξt, 1 ≤t ≤T; it certainly
satisfies (3.6).
It remains to establish (3.4) and (3.5). The first statement is true, since
Ut(x) ≥E(Ut+1(x)|Ft) ≥· · · ≥E(UT (x)|Ft) = U(x),
(3.7)
and U(1) = 0 by Assumption 1.1. As to the second statement, it holds for
t = T by (1.5). For t = T −1 consider

On the Existence of Optimal Portfolios
603
UT −1(x + ⟨ξ, ∆ST −1⟩) =
E(UT (x + ⟨ξ, ∆ST −1⟩+ ⟨˜ξT −1(x + ⟨ξ, ∆ST −1⟩), ∆ST ⟩)|FT −1),
so the statement holds by (1.5) again. For other values of t the notation gets
more and more complicated but the same argument applies.
Now set ϕ∗
1(c) := ˜ξ1(c) and define recursively:
ϕ∗
t+1(c) := ˜ξt+1(c +
t

j=1
⟨ϕ∗
j, ∆Sj⟩), 1 ≤t ≤T −1.
Joint measurability of ˜ξt assures that ϕ∗= ϕ∗(c) is a predictable process
with respect to the given filtration.
Proposition 3.2. We have ϕ∗∈A(c) and for any strategy ϕ ∈A(c)
E(U(V c,ϕ
T
)|F0) ≤E(U(V c,ϕ∗
T
)|F0) = U0(c).
(3.8)
Proof. Notice that ϕ∗
t ∈Ξt−1(V c,ϕ∗
t−1 ), so ϕ∗∈A(c). Remembering UT = U
and using Proposition 2.4, we may rewrite the right-hand side of (3.8) as
follows:
E(UT (V c,ϕ∗
T
)|F0) = E(E(UT (V c,ϕ∗
T −1 + ⟨ϕ∗
T , ∆ST ⟩)|FT −1)|F0) =
= E(UT −1(V c,ϕ∗
T −1 )|F0).
Continuing the procedure, we finally arrive at ϕ∗∈A(c) and
E(U(V c,ϕ∗
T
)|F0) = E(U1(V c,ϕ∗
1
)|F0) = E(U1(c + ⟨ϕ∗
1, ∆S1⟩)|F0) = U0(c).
(3.9)
We remark that all conditional expectations below exist by Proposition 3.1.
By the definition of UT −1 and ϕ ∈A(c) one has ϕT ∈ΞT −1(V c,ϕ
T −1) and
E(UT (V c,ϕ
T
)|FT −1) = E(UT (V c,ϕ
T −1 + ⟨ϕT , ∆ST ⟩)|FT −1) ≤UT −1(V c,ϕ
T −1) a.s.
Iterate the same argument and obtain
E(U(V c,ϕ
T
)|F0) ≤U0(c) a.s.
(3.10)
Putting (3.9) and (3.10) together, one gets exactly (3.8).
Proof (of Theorem 1.1). Proposition 3.2 shows that u(c) = EU0(c) and the
ϕ∗constructed in the last two sections is a maximizer such that ϕ∗
t ∈Dt.
Remark 3.1. We indicate how Theorem 1.1 can be generalized. Let B ≥0 be a
bounded random variable, interpreted as a contingent claim. Define recursively
the superhedging prices as follows:

604
M. R´asonyi and ^L. Stettner
πT (B) := B,
πt(B) := ess. inf{X : σ(X) ⊂Ft, ∃ϕ ∈Ξt X + ⟨ϕ, ∆St+1⟩≥πt+1(B) a.s.},
for 0 ≤t ≤T −1.
Define for c > π0(B)
A(B, c) := {ϕ ∈Φ : V c,ϕ
t
≥πt(B) a.s., 0 ≤t ≤T},
and redefine for each Ft-measurable H ≥πt(B)
Ξt(H) := {ξ ∈Ξt : H + ⟨ξ, ∆St+1⟩≥πt+1(B) a.s.}
Theorem 3.1. Suppose that the conditions of Theorem 1.1 hold and F0 is
trivial. Then for all c > π0(B)
u(B, c) :=
sup
ϕ∈A(B,c)
EU(V c,ϕ
T
−B) < ∞,
(3.11)
and there exists ϕ∗(c) ∈A(B, c) such that
u(B, c) = EU(V c,ϕ∗(c)
T
−B).
Proof. As F0 is trivial, π0(B) is a constant; (3.11) follows from (1.5) and the
boundedness of B. Since B is bounded, by Assumption 1.1 there exists F > 0
such that UT (F) ≥0, and this will remain true for each Ut by (3.7).
Replace (3.2) by
UT (x, ω) := U(x −B(ω)), x ≥B(ω), UT (x, ω) = −∞, x < B(ω),
set for y ∈[0, ∞)
Ut(πt(B) + y, ω) := ess.
sup
ξ∈Ξt(πt(B)+y)
E(Ut+1(πt(B) + y + ⟨ξ, ∆St+1⟩)|Ft),
and
Ut(x, ω) = −∞,
x < πt(B)(ω),
instead of (3.3) and follow the argument of this section. Use the extended
setting of section 2 as explained in Remark 2.2. Apparently, Θ, θ will corre-
spond to πt+1(B), πt(B) in the backward induction. The rest of the argument
is essentially unchanged.
4 Auxiliary results
We shall often rely on the measurable selection theorem, see III. 70-73 of [2].
Let H ⊂F be a σ-algebra containing P-null sets. An H-measurable random
set or measurable multifunction A is an element of H ⊗B(Rd), where B(Rd)
denotes the Borel sets of Rd. A random affine subspace A is an H-measurable
random set such that A(ω) is an affine subspace of Rd for each ω.
Let Y be a d-dimensional random variable and µ(·, ω) := P(Y ∈·|H) a
regular version of its conditional distribution. Let D(ω) be the smallest affine
subspace of Rd containing the support of µ(·, ω).

On the Existence of Optimal Portfolios
605
Proposition 4.1. D is an H-measurable random affine subspace.
Proof. We begin by showing that supp µ(·, ω) or, equivalently, its complement
suppCµ(·, ω) is a random set. Let G be a countable base for the topology of
Rd. Then
suppCµ(·, ω) :=
A
{G ∈G : µ(G, ω) = 0},
which proves the assertion. Actually, Z(ω) := conv(suppµ(·, ω)) is a random
set, where conv(·) denotes closed convex hull, this follows from Theorem III.
40 on p. 87 of [1].
Take a measurable selector ν(ω) of Z(ω); Z −Z contains the origin in its
relative interior and
B A
n∈N
{nz : z ∈Z(ω) −Z(ω)}
C
+ ν(ω),
equals D(ω), which proves the proposition.
Proposition 4.2. Fix x > 0. There exists M(x) ∈H⊗B(Rd) which is convex,
compact (a.s.) and
ξ ∈Ξx and ξ ∈D a.s. ⇐⇒ξ ∈M(x) a.s.
Proof. Take a sequence of H-measurable random variables σi such that for
almost all ω the sequence σi(ω), i ∈N, is dense in suppµ(·, ω). Such a sequence
exists by Theorem III. 22 on p. 74 of [1]. Define the convex closed random set
˜
M(x) :=
?
i∈N
{(ω, p) : x + ⟨p, σi(ω)⟩≥0}.
The following series of equivalences is clear:
ξ ∈Ξx ⇐⇒P(x + ⟨ξ, Y ⟩≥0) = 1 ⇐⇒P(x + ⟨ξ, Y ⟩≥0|H) = 1, a.s.
⇐⇒µ({y ∈Rd : x + ⟨ξ(ω), y⟩≥0}, ω) = 1 a.s. ⇐⇒
{y ∈Rd : x + ⟨ξ(ω), y⟩≥0} ⊇suppµ(·, ω) a.s. ⇐⇒
{y ∈Rd : x + ⟨ξ(ω), y⟩≥0}σi(ω) a.s., i ∈N,
and this last one means precisely ξ ∈˜
M(x) a.s. Define M(x) := ˜
M(x) ∩D.
The argument of Lemma 2.1 implies that M(x) is compact, almost surely, so
M(x) is as desired.
Let ri M(x, ω) denote the relative interior of M(x, ω) and let R = R(x, ω)
denote the linear span of M(x, ω).
Proposition 4.3. Both ri M(x) and R(x) are H-measurable random sets.

606
M. R´asonyi and ^L. Stettner
Proof. The set M −M contains zero in its relative interior, hence
R =
A
n∈N
{nz : z ∈M −M}
and this is indeed a random set. Take H-measurable random variables
ζi(ω), 1 ≤i ≤d, which are orthogonal and generate R(x) (some of them
might be 0), this follows easily from the measurable selection theorem. The
function
[dim R(x)](ω) :=
d

j=1
I{ζj̸=0}(ω)
is H-measurable. It suffices to prove the proposition separately on the events
{ω : dim R(x, ω) = m} ∈H,
for each m ≤d. The case m = 0 is trivial, so we suppose, without loss of
generality, that dim R(x, ω) = m ≥1 for a fixed m. We may assume that
ζi(ω), 1 ≤i ≤m is an orthonormed basis of R(x, ω).
The interior points are precisely those, around which a little cube can
be drawn in R(x) which still belongs to M(x). As M(x) is convex, this is
equivalent to the fact that the edges of that cube belong to M(x). Hence
ri M(x) =
A
n∈N


(ω, p) : p + 1
n
m

j=0
i(j)ζj(ω) ∈M(ω, x), ∀i ∈{−1, +1}m


,
which is clearly a measurable multifunction.
Lemma 4.1. Let a, b ∈R, a < b. Let ηn : [a, b] × Ω→Rd be a sequence of
B([a, b]) ⊗H-measurable functions such that for almost all ω
∀x lim inf
n→∞|ηn(x, ω)| < ∞.
Then there is a sequence nk of B([a, b]) ⊗H-measurable N-valued functions,
nk < nk+1, k ∈N, such that ˜ηk(x, ω) := ηnk(x, ω) converges for all x to
some ˜η(x, ω) as k →∞, for almost all ω. To put it more concisely, there is a
convergent random subsequence.
Proof. This is just a variant of Lemma 2 in [5].
5 Conclusions
Finally, we present a concrete model class where there exists an optimal in-
vestment strategy. Let W denote the family of random variables with finite
moments of all orders.

On the Existence of Optimal Portfolios
607
Proposition 5.1. Let U satisfy Assumption 1.1. Let |St| ∈W, 0 ≤t ≤T,
and supppose that (1.6) holds with 1/βt ∈W, 0 ≤t ≤T −1. Then (1.5) holds
and the assertion of Theorem 1.1 is true.
Proof. For notational simplicity let ξ∆St denote scalar product. We shall show
by backward induction that there exists Jt ∈W such that
Ut(x) ≤Jtx < ∞,
x ∈(0, ∞),
0 ≤t ≤T.
Indeed, for t = T this is true with JT := U ′(1). Now suppose that this
statement has been established for s ≥t + 1. Proposition 2.2 and Lemma 2.1
imply that
ess. sup
ξ∈Ξx
t
E(Ut+1(x + ξ∆St+1)|Ft) = ess.
sup
ξ∈Ξx
t ,ξ∈Dt+1
E(Ut+1(x + ξ∆St+1)|Ft)
≤E(Ut+1(x + |∆St+1|x/βt)|Ft) ≤E(Jt+1x + Jt+1x|∆St+1|/βt|Ft),
so we may set Jt := E(Jt+1(1 + |∆St+1|/βt)|Ft). Finally we arrive at the
bound U0(x) ≤J almost surely, where J ∈W so we get for all x > 0
u(x) = EU0(x) < ∞,
i.e. (1.5) holds true. The proof of Theorem 1.1 shows that there exists an
optimal ϕ∗.
Remark 5.1. The previous proposition applies, in particular, when βt = β is a
deterministic constant. The hypothesis that (1.6) holds with deterministic β
is called uniform no-arbitrage condition. This assumption has been introduced
in [8].
Remark 5.2. One may consider concave nondecreasing functions U : R →R.
Under (NA), (1.5) and additional hypotheses on U there exists an optimal
strategy in Φ, see [7]. We may also look at “tame” portfolios, i.e. ϕ such that
there exists a ∈R satisfying
V c,ϕ
t
≥a a.s., 0 ≤t ≤T.
(5.1)
Theorem 1.1 of the present paper immediately implies that (under (NA) and
(1.5)) there exists an optimal strategy among ϕ satisfying (5.1) with a fixed a.
It is an intriguing question under what kind of conditions there is an optimal
control among all tame strategies.
References
1. Castaing, C., Valadier, M.: Convex Analysis and Measurable Multifunctions. Lec-
ture Notes in Mathematics, 580, Springer, Berlin, 1977.

608
M. R´asonyi and ^L. Stettner
2. Dellacherie, C., Meyer, P.-A.: Probabilities and Potential. Mathematical Studies
29, North-Holland, Amsterdam, 1978.
3. F¨ollmer, H., Schied, A.: Stochastic Finance. Walter de Gruyter, Berlin, 2002.
4. Jacod, J., Shiryaev, A.N.: Local martingales and the fundamental asset pricing
theorems in the discrete-time case. Finance and Stochastics, 2, 259–273, 1998.
5. Kabanov, Yu. M., Stricker, Ch.: A teachers’ note on no-arbitrage criteria.
S´eminaire de Probabilit´es, XXXV, 149–152, Springer, Berlin, 2001.
6. Kramkov, D.O., Schachermayer, W.: The asymptotic elasticity of utility functions
and optimal investment in incomplete markets. Ann. Appl. Probab., 9, 904–950,
1999.
7. R´asonyi, M., Stettner, L.: On the utility maximization problem in discrete-time
financial market models. Forthcoming in Annals of Applied Probability.
8. Sch¨al, M.: Portfolio optimization and martingale measures. Math. Finance, 10,
289–303, 2000.
9. Sch¨al, M.: Price systems constructed by optimal dynamic portfolios. Math. Meth-
ods Oper. Res., 51, 375–397, 2000.

The Optimal Stopping of a Markov Chain and
Recursive Solution of Poisson and Bellman
Equations
Isaac M. SONIN
Department of Mathematics, University of North Carolina at Charlotte,
Charlotte, NC, 28223, USA.
imsonin@email.uncc.edu
Summary. We discuss a modified version of the Elimination algorithm proposed
earlier by the author to solve recursively the problem of optimal stopping of a
discrete-time Markov chain with finite or countable state space. This algorithm and
the idea behind it are applied to solve recursively discrete versions of the Poisson
and Bellman equations.
Key words: Markov chain, optimal stopping, Elimination algorithm, State Reduc-
tion approach, Poisson equation, Bellman equation.
Mathematics Subject Classification (2000): 60J22, 62L15, 65C40
1 Introduction
The main goal of this paper is to present a unified recursive approach to the
following two related but nevertheless different problems.
Problem 1. Find the solution f of the discrete Poisson equation
f = c + Pf,
(1.1)
where Pf(x) = 
y p(x, y)f(y) is the averaging operator, defined by a transi-
tion matrix P, and c is a given function defined on a countable or finite state
space X.
Problem 2. Solve the problem of optimal stopping (OS) for a Markov
chain (MC) with an immediate reward (one-step cost) function c and a ter-
minal reward function g. This means to describe an optimal strategy (or
ε-optimal strategies if there is no optimal strategy), and to find the value
function v, which is the minimal solution of the corresponding Bellman (op-
timality) equation

610
I. Sonin
v = max(g, c + Pv).
(1.2)
The main tool to study these problems in this article is the recursive algo-
rithm for Problem 2, which we call the Elimination algorithm (EA), described
in the papers [12] and [13] by the author (see also [11]). We present EA here in
a modified form, and we prove also a new important Lemma 3. We limit our
presentation to the case of a finite state space though one of the advantages
of our approach is that in many cases it can be applied also to the countable
state space. This algorithm is better understood in the context of a group
of algorithms which are based on a similar idea and can be called the State
Reduction algorithms. We will refer to this idea as the State Reduction (SR)
approach. Problem 1 was analyzed on the basis of this approach in Sheskin
(1999) [8], see also the references there to the earlier works of Kohlas (1986)
and Heyman and Reeves (1989).
Note, that formally, Problem 1 can be considered as a special case of
Problem 2 when g(x) = −∞but we will treat them separately. We start with
Problem 2.
The author would like to thank Robert Anderson who read the first version
of this paper and made valuable comments.
2 Optimal stopping of a MC
The optimal stopping problem (OSP) is one of the most developed and exten-
sively studied fields of stochastic control. There are two different approaches
to OSP, usually called “the martingale theory of OSP of general stochastic se-
quences (processes)” (formulated by Snell) and “the OSP of Markov chains”.
The first one is is exposed in the well-known monograph by Chow, Robbins
and Sigmund (1971) [2] (see also the book of T. Ferguson on his website for
a modern presentation). The second approach is due to Albert Shiryaev is
presented in his classical books (1969, 1978), [9], [10]. (See also Dynkin and
Yushkevich (1969), [4]). There are also dozens of books and monographs with
chapters or sections on OSP, see, e.g. [1], [7], and more than a thousand pa-
pers on this topic. These two approaches basically represent nonstationary
and stationary (nonhomogeneous versus homogeneous) situations and though
formally they are equivalent, the second approach is more transparent for
study and discussion.
Formally, OSP of MC is specified by a tuple M = (X, P, c, g, β), where
X is a finite (countable) state space, P = {p(x, y)} is a transition matrix,
c(x) is a one step-cost function, g(x) is a terminal reward function, and β is a
discount factor, 0 < β ≤1. We call such a model an OS model. A tuple without
the terminal reward, M = (X, P, c, β), we call a reward model, and a tuple
M = (X, P), we call a Markov model. A Markov chain (MC) from a family of
MCs defined by a Markov model is denoted by (Zn). The probability measure
and the expectation for the Markov chain with initial point x are denoted by

Optimal Stopping and Solution of Poisson and Bellman Equations
611
Px and Ex, respectively. The value function v(x) for an OS model is defined
as v(x) = supτ≥0 Ex[τ−1
i=0 βic(Zi) + βτg(Zτ)], where the sup is taken over
all stopping times τ ≤∞. If τ = ∞with positive probability we assume that
g(Z∞) = 0.
It is well-known that the discounted case can be treated as not discounted
if an absorbing point x∗and new transition probabilities are introduced:
pβ(x, y) = βp(x, y) for x, y ∈X, pβ(x, x∗) = 1 −β, pβ(x∗, x∗) = 1. In other
words, with probability β the Markov chain ”survives” and with complimen-
tary probability it transits to an absorbing state x∗. Further we will assume
that this transformation is made and we skip the superscript β. More than
that, all subsequent results are valid if the constant β is replaced by a function
β(x), 0 ≤β(x) ≤1, the probability of ”survival”, β(x) = Px(Z1 ̸= x∗). We
will also assume that c(x∗) = g(x∗) = 0.
Let Pf(x) be the averaging operator and let Ff(x) = c(x)+Pf(x) be the
reward operator. If G ⊆X, let us denote by τG the moment of the first visit
to G, i.e., τG = min(n ≥0 : xn ∈G). The following statement is the main
result for OSP with finite and countable X.
Theorem 1. (Shiryaev, [9]) (a) The value function v(x) is the minimal
solution of Bellman (optimality) equation (2), i.e. the minimal function sat-
isfying the inequalities v(x) ≥g(x), v(x) ≥Fv(x) for all x ∈X;
(b) v(x) = limn vn(x), where vn(x) is the value function for the OSP on
a finite time interval of length n;
(c) for any ε > 0 the random time τε = min{n ≥0 : g(Zn) ≥v(Zn)−ε)},
is an ε-optimal stopping time;
(d) if Px(τ0 < ∞) = 1 then τ0 = min{n ≥0 :
g(Zn) = v(Zn)} is an
optimal stopping time;
(e) if the state space X is finite then set S = {x : g(x) = v(x)} is not
empty and τ0 is an optimal stopping time.
The classical tools to solve the OSP of a MC are: the direct solution of
the Bellman equation, which is possible only for very specific MCs; the value
iteration method based on the equality v(x) = limn vn(x), mentioned in the
item (b) of Theorem 1; and for finite X, the value function v(x) can be found
as the solution of a linear programming problem. See also the paper of Davis
and Karatzas [3].
The Elimination Algorithm (EA) solves the finite space OS problem in
no more than |X| steps, and allows us also to find the distribution of MC
at the moment of stopping in the optimal stopping set S, and the expected
number of visits to other states before stopping. Using the EA we also can
prove in a new and shorter way Theorem 1. As a byproduct we also obtain a
new recursive way to solve the Poisson equation. It works also for many OSP
with countable X.
Before describing the EA in Section 4, in the next section we describe a
more general framework of the State Reduction (SR) approach. This is a brief
version of a section from ([13]).

612
I. Sonin
3 Recursive calculation of the MC characteristics and
the SR approach
Let M1 = (X1, P1) be a Markov model and let D ⊂X1, X2 = X1 \ D.
Let (Zn) be a Markov chain specified by the model M1 with the starting
point x ∈X2. We introduce the sequence of Markov times τ0, τ1, ..., τn, ..., the
moments of zero, first, and so on, visits of (Zn) to the set X2 = X1 \ D, i.e.
τ0 = 0, τn+1 = min{k > τn : Zk ∈(X1\D)}, 0 < τ1 < ... Let us consider
the random sequence Yn = Zτn, n = 0, 1, 2, ... For the sake of brevity we
assume that τn < ∞for all n = 0, 1, 2, ... with probability one. Otherwise we
can complement X2 by an additional absorbing point x∗and correspondingly
modify the transition probabilities participating in Lemma 1. Let us denote
by u1(z, ·) the distribution of the Markov chain (Zn) for the initial model M1
at the moment τ1 of the first visit to set X2 (the first exit from D) starting
at z ∈D. The strong Markov property and standard probabilistic reasoning
imply the following basic lemma of the SR approach:
Lemma 1. (Kolmogorov, Doeblin) (a) The random sequence (Yn) is a
Markov chain in a model M2 = (X2, P2), where
(b) the transition matrix P2 = {p2(x, y)} is given by the formula
p2(x, y) = p1(x, y) +

z∈D
p1(x, z)u1(z, y),
(x, y ∈X2).
(3.1)
Part (a) is immediately implied by the strong Markov property for (Zn), while
the proof of (b) is straightforward. Formula (3.1) can be represented in the
matrix form (see, e.g., [6]). If the matrix P1 is decomposed as
P1 =
Q1 T1
R1 P ′
1

,
(3.2)
where sub-stochastic matrix Q1 describes the transitions inside of D, P ′
1 de-
scribes the transitions inside of X2 and so on, then
P2 = P ′
1 + R1U1 = P ′
1 + R1N1T1.
(3.3)
In this formula U1 is the matrix of distribution of an MC at the moment of
the first exit from D (exit probabilities matrix), and N1 is the fundamental
matrix for the sub-stochastic matrix Q1, i.e.
N1 =
∞

n=0
Qn
1 = (I −Q1)−1,
(3.4)
where I is the |D| × |D| identity matrix. Formula (3.4) implies obviously:
N1 = I + Q1N1 = I + N1Q1.
(3.5)

Optimal Stopping and Solution of Poisson and Bellman Equations
613
Both equalities in (3.5) have relatively simple probabilistic interpretations.
The first is almost trivial statement while the second recalls the words of Kai
Lai Chung ”Last exit is a deeper concept than first entrance”.
Given the set D, the matrices N1 and U1 are related by the equality
U1 = N1T1.
(3.6)
We call model M2 the X2-reduced model of M1. For the sake of brevity
we will call two such models adjacent. An important case is when the set D
consists of one not absorbing point z. In this case formula (3.1) obviously
takes the form
p2(x, ·) = p1(x, ·) + p1(x, z)n1(z)p1(z, ·),
(x ∈X2),
(3.7)
where n1(z) = 1/(1 −p1(z, z)).
According to this formula, each row-vector of the new stochastic matrix
P2 is a linear combination of two rows of P1 (with the z-column deleted). For
a given row of P2, these two rows are the corresponding row of P1 and the zth
row of P1. This transformation corresponds formally to a step of the Gaussian
elimination method for solving a linear system.
If an initial Markov model M1 = (X1, P1), is finite, |X1| = k, and only
one point is eliminated at each step, then a sequence of stochastic matrices
(Pn), n = 2, ..., k, can be calculated recursively on the basis of formula (3.7), in
which the subscripts ”1” and ”2” are replaced by ”n” and ”n+1” respectively.
This sequence provides an opportunity to calculate many characteristics
of the initial Markov model M1 recursively starting from some reduced model
Ms, 1 < s ≤k. For this goal one needs also a relationship between a charac-
teristic in a reduced model and a model with one more point. Sometimes this
relationship is obvious or simple, sometimes it has a complicated structure.
The EA algorithm for the problem of optimal stopping (OS) of a Markov
chain was developed independently of other SR algorithms and shares with
them the common idea of elimination. It also has very distinct specific fea-
tures. The number of points to be eliminated and the order in which they are
eliminated depend on some auxiliary procedure, and the value function of the
problem is recovered on the second stage.
For the problem of OS it is natural to try to find not only the optimal
stopping set but as well the distribution of the stopping moment and the
distribution of a MC at the moment of stopping. The next lemma provides
tools for the sequential calculation of these characteristic.
Lemma 2. (Lemma 3 in ([13])). Let the models M1, M2 be defined as in
Lemma 1 and let G ⊂X2 = X1 \ D,. Let ui(x, ·) be the distribution of the
Markov chain (Zn) for the model Mi at the moment of the first visit to G in
the model Mi, i = 1, 2, and let mi(x, v) be the mean time spent at point v
till such a visit with an initial point x ∈X2 \ G. Then for any x ∈X2

614
I. Sonin
u1(x, y) = u2(x, y),
y ∈G,
(3.8)
m1(x, v) = m2(x, v),
v ∈X2 \ G.
(3.9)
4 The Elimination Algorithm
The Elimination algorithm for the OSP of a MC is based on the three following
facts.
1. Though in the OSP it may be difficult to find the states where it is
optimal to stop, it is easy to find a state (states) where it is optimal not to
stop. Obviously, it is optimal to stop at z if g(z) ≥c(z) + Pv(z) ≡Fv(z), but
v is unknown until the problem is solved. On the other hand, it is optimal
not to stop at z if g(z) < Fg(z), i.e. the expected reward of doing one more
step is larger than the reward from stopping. (Generally, it is optimal not to
stop at any state where the expected reward of doing some, perhaps random
number of steps, is larger than the reward from stopping).
2. After we have found states (state) which are not in the optimal stop-
ping set, we can eliminate them and recalculate the transition matrix using
(3.7) if one state is eliminated or (3.1) if a larger subset of the state space
is eliminated. According to Lemma 2 this will keep the distributions at the
moments of visits to any subset of the remaining states the same and the
excluded states do not matter since it is not optimal to stop there. After that
in the reduced model we can repeat the first step and so on.
3. Finally, though if g(z) ≥Fg(z) at a particular point z, we can not make
a conclusion about whether this point belongs to the stopping set or not, but
if this inequality is true for all points in the state space then we have the
following well-known statement:
Proposition 1. Let M = (X, P, g) be an optimal stopping problem, and
g(x) ≥Fg(x) for all x ∈X. Then X is the optimal stopping set in the problem
M, and v(x) = g(x) for all x ∈X.
Proposition 1 follows immediately from Theorem 1 because the function
g(x) in this case is its own excessive majorant.
The formal justification of the transition from the initial model M1 to the
reduced model M2 is given by Theorem 2 below. This theorem was formulated
by the author in [11] and its proof was given in [12] when c(x) = 0 for all
x. Here we prove this theorem in a shorter way and for any c(x) but, for
simplicity, only for the case of finite X.
Let us introduce a transformation of the cost function c1(x) (or any func-
tion f(x)) defined on X1 into the cost function c2(x) defined on X2, under
the transition from model M1 to model M2.
Given the set D ⊂X1, let τ be the moment of the first return to X2, i.e.
τ = min(n ≥1 : Zn ∈X2). Then given a function c1(x) defined on X1 let us
define the function c2(x) on X2 by the formula

