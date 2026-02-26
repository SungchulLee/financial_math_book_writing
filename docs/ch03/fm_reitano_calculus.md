# Calculus for Finance: Differentiation & Integration

!!! info "Source"
    **An Introduction to Quantitative Finance** by Robert R. Reitano, MIT Press.
    These notes are used for educational purposes.

## Calculus I: Differentiation

9 Calculus I: Di¤erentiation
9.1
Approximating Smooth Functions
Calculus is the mathematical discipline that studies properties of ‘‘smooth’’ functions.
Intuitively a function is smooth if its values vary in a somewhat predictable way. So
based on knowledge of its values and behavior at a given point, we can approximate
its values ‘‘near’’ that given point. There are moreover various degrees of smooth-
ness, and these in turn provide various degrees of accuracy in the approximation.
We begin by recalling the definition of a function introduced in chapter 2, and then
introduce the simplest notion of smoothness, known as continuity, and some if its
refinements. We will spend some time on these concepts because of their impor-
tance and subtlety. The next section then studies derivatives of a function, as well as
Taylor series expansions, which are seen to both provide a formal basis for approxi-
mating function values, and for quantifying the notion of the accuracy of such an
approximation.
In the process, we will finally be able to justify the earlier assumed power series
expansions for ex and ln x, as well as demonstrate the validity of the limits needed
in the development of the Poisson distribution, such as
1  l
n

n
! el;
as n ! y:
Remark 9.1
In general, the functions that appear to be addressed in calculus are real-
valued functions of a real variable. In other words, functions
f : X ! Y
where
X; Y H R:
However, while the assumption that the domain of f ðxÞ is real is critical, and so X ¼
Dmnð f Þ H R, there is often no essential di‰culty in assuming f to be a complex-
valued function of a real variable so that the range of f ðxÞ, Y ¼ Rngðf Þ H C. This is
not often needed in finance, and the characteristic function is one of the few examples in
finance where complex-valued functions are encountered.
One reason that Dmnð f Þ H R is critical in the development of calculus is that we
will often utilize the natural ordering of the real numbers. In other words, given
x; y A R with x 0 y, it must be the case that either x < y or y < x. None of these
proofs would generalize easily to functions of a complex variable where no such order-
ing exists. Indeed it turns out that the calculus of such functions is quite di¤erent and
studied in what is called complex analysis. On the other hand, the only essential prop-
erty of Rngð f Þ that is often assumed is that there is a metric with which one can define
closeness and limits. Since C has a metric as noted in chapter 3, any proof that only

relies on the standard metric in R, the absolute value, works equally well in C with
its standard metric or any equivalent metric. In other words, the existence of an order-
ing in the range space doesn’t matter for most results, and we simply need a metric
structure.
One counterexample to this statement on the range space is any result that addresses
both f ðxÞ and its inverse function, f 1ðyÞ, since in such a development, Dmnðf 1Þ ¼
Rngð f Þ. Another relates to statements about maximum or minimum values of f ðxÞ, or
intermediate values, which by definition implies an ordering. Such statements must be
reviewed carefully to determine if only metric properties are needed, as may be the
case for maximum or minimum values, or if the existence of an ordering is also needed,
as is the case for an intermediate value.
Because of the rarity of encountering complex-valued functions of a real variable
in finance, all the statements in this chapter are either silent on the location of Y, or
explicitly assume Y H R. In particular, no e¤ort was made to explicitly frame all
proofs in the general case Y H C, since this overt generality seemed to have little pur-
pose given the objectives of this book. However, any proof that is silent and relies only
on a metric in Y will virtually always be seen to extend to the case where Y H C.
When a proof explicitly states that Y H R, its generality must be thought through
step by step, and in many cases it will be seen that again, only the metric in Y is used.
The applicability of many results to a complex-valued function can also be justified
by splitting the function values into real and imaginary parts. If Y H C, we write
f ðxÞ ¼ gðxÞ þ ihðxÞ;
where both gðxÞ and hðxÞ are real valued. The theory in this chapter can typically then
be justifiably applied to f ðxÞ by applying it separately to gðxÞ and hðxÞ and combining
results.
9.2
Functions and Continuity
9.2.1
Functions
Definition 9.2
A function is a rule, often represented notationally by f , g, and so
forth, by which each element of one set of values, called the domain and denoted
Dmnð f Þ, is identified with a unique element of a second set of values, call the range
and denoted Rngðf Þ.
The rule is often expressed by a formula such as
f ðxÞ ¼ x2 þ 3:
418
Chapter 9
Calculus I: Di¤erentiation

Here x is an element of the domain of the function f , while f ðxÞ is an element of the
range of f . Functions are also thought of as ‘‘mappings’’ between their domain and
range. The imagery of x being mapped to f ðxÞ, is intuitively helpful at times. In this
context, one might use the notation
f : X ! Y;
where X denotes the domain of f , and Y the range. It is also common to write f ðxÞ
for both the function, which ought to be denoted only by f , and the value of the
function at x. This bit of carelessness rarely causes confusion.
Note that while the definition of a function requires that f ðxÞ be unique for any x,
it is not required that x be unique for any f ðxÞ. For instance, the function above has
f ðxÞ ¼ f ðxÞ for any x 0 0. Another way of expressing this is that a function can be
a ‘‘many-to-one’’ rule, which includes one-to-one, but it cannot be a one-to-many
rule.
An example of a one-to-many rule that is therefore not a function is
f ðxÞ ¼
ffiffiffix
p ;
which assigns two values to every positive value of x, such as f ð4Þ ¼G2. In many
applications one can transform such a rule into a function by simply defining its
value to be one of the possible ‘‘branches’’ in the range. For example, the positive
square root (or negative square root) are both functions.
A function that is in fact one-to-one, meaning that it satisfies f ðxÞ ¼ f ðx0Þ i¤
x ¼ x0, has the special property that it has an inverse that is also a function.
Definition 9.3
Given a one-to-one function f ðxÞ, f : X ! Y, the inverse function,
denoted f 1, is defined by
f 1 : Y ! X;
f 1ðyÞ ¼ x
if f ðxÞ ¼ y:
In other words, Dmnðf 1Þ ¼ Rngðf Þ and Rngð f 1Þ ¼ Dmnðf Þ. More generally, for
an arbitrary function f and set A, the set f 1ðAÞ, the pre-image of A under f is defined
by
f 1ðAÞ ¼ fx A Dmnðf Þ j f ðxÞ A Ag:
Example 9.4
The function f ðxÞ ¼ x2 þ 3 has no inverse if defined as a function with
domain equal to all real numbers R because it is many-to-one on this domain, but it
does have an inverse if the domain is restricted to any subset of the nonnegative or
9.2
Functions and Continuity
419

nonpositive real numbers. On the other hand, f 1ðAÞ is defined for any set A H R. For
example, f 1ð½1; 0Þ ¼ 0 and f 1ð½1; 4Þ ¼ ½1; 2 U ½1; 2.
Functions can also be combined, or ‘‘composed,’’ to produce so-called composite
functions.
Definition 9.5
If g : X ! Y and f : Y ! Z, the composition of f and g, denoted
f  g or f ðgÞ is a function: X ! Z defined by
f  gðxÞ ¼ f ðgÞðxÞ 1 f ðgðxÞÞ:
More generally, it is not necessary that Dmnðf Þ ¼ RngðgÞ, and f ðgÞ is well defined as
long as RngðgÞ H Dmnð f Þ.
Compositions of more than two functions are defined analogously, with the nota-
tional convention that functions are applied right to left. For instance,
f  g  hðxÞ 1 f ðgðhðxÞÞÞ;
which is evaluated as a mapping
x ! hðxÞ ! gðhðxÞÞ ! f ðgðhðxÞÞÞ:
Note finally that a composition of functions is not a ‘‘commutative’’ process, in
that even when the domains and ranges of the functions allow the definition of both
f  g and g  f , in only the most trivial exceptional cases will these be equal. The
rule is
f  g 0 g  f ;
and so order matters!
9.2.2
The Notion of Continuity
Intuitively a function is said to be continuous at a given point x0 if f ðxÞ must be close
to f ðx0Þ whenever x is close to x0. In other words, j f ðxÞ  f ðx0Þj will be ‘‘small’’
whenever jx  x0j is ‘‘small.’’ Mathematicians formalize this notion with a logically
complex statement that receives some discussion below.
Definition 9.6
A function f ðxÞ is continuous at a point x0 if for any value  > 0, one
can find a d > 0, so that:
 j f ðxÞ  f ðx0Þj <  whenever jx  x0j < d, or equivalently,
 jx  x0j < d implies that j f ðxÞ  f ðx0Þj < .
420
Chapter 9
Calculus I: Di¤erentiation

The function f ðxÞ is continuous on an interval if it is continuous at every point of
that interval, and f ðxÞ is continuous if it is continuous at every point of its domain.
Remark 9.7
1. By convention, a function is defined to be continuous at the endpoint(s) of a closed
interval ½a; b if the definition applies with x restricted to that interval. The formal ter-
minology is that f ðxÞ is continuous from the left at b, or continuous from the right at a.
However, this formal language is often not used and a statement such as, f ðxÞ is con-
tinuous on ½a; b, is universally understood in this sense.
2. Note that in this definition, the numerical value of d depends on the value of . In a
given application it is in fact required that this dependency can be formalized by a func-
tion so that d 1 dðÞ.
Continuity at a point x0 means that however small an open interval one constructs
around f ðx0Þ, here the interval ðf ðx0Þ  ; f ðx0Þ þ Þ, one can find an open interval
around x0, here the interval ðx0  d; x0 þ dÞ, that gets mapped into it. In the case
where x0 is an endpoint of a closed interval ½a; b, this statement says that however
small an open interval one constructs around f ðx0Þ, here the interval ðf ðx0Þ  ;
f ðx0Þ þ Þ, one can find a half-open interval, here the interval ðb  d; b or ½a; a þ dÞ,
that gets mapped into it.
Now the statement above about  and d is subtle, and even passive in tone. But this
definition can be stated in a more active way.
Definition 9.8
f ðxÞ is continuous at a point x0 if for any sequence n ! 0 we can
find a sequence dn so that j f ðxÞ  f ðx0Þj < n whenever jx  x0j < dn. In other words,
by choosing xn arbitrarily in the intervals jx  x0j < dn, we can be assured that
j f ðxnÞ  f ðx0Þj < n, and hence j f ðxnÞ  f ðx0Þj ! 0.
In general, it will also be the case that dn ! 0, but the example of f ðxÞ 1 1 for all
x shows that this need not be the case.
This -d definition is one of many in mathematics, and it is close in structure to the
-N definition used to define convergence of a sequence in chapter 5. This definition
may seem sti¤ and formal. This is because continuity, which is intuitively a simple
notion, is also quite subtle and somewhat di‰cult to define precisely. So this and
other such definitions periodically fall in and out of favor among mathematics edu-
cators, and it is fair to say that at least some mathematicians have a love–hate rela-
tionship with this string of words that with practice rolls o¤ their tongues like a
religious chant.
9.2
Functions and Continuity
421

In this book we pay homage to the tradition of such definitions, but at the same
time acknowledge the pain and su¤ering they cause many students of the subject.
So we do invest a bit more time in exploring their meaning. In point of fact, the tra-
ditional continuity chant is: ‘‘. . . for any  > 0, there is a d > 0 so that . . . ,’’ which we
have adapted as above to make the point that determining if such a d exists is typi-
cally an exercise in finding one that does work.
To explore this complicated notion, let’s informally say that f ðxÞ is continuous at
x0 if we can make j f ðxÞ  f ðx0Þj as small as we want by choosing jx  x0j small
enough. We can also think of this as saying that the value of f ðx0Þ can be predicted
if we know the value of f ðxÞ for all x arbitrarily close to x0. That is, we cannot be
surprised at the value of f ðx0Þ once we know the values of f ðxÞ for x near x0.
The cause of the complexity in the definition is that continuity means more than
simply that ‘‘we can find an x near x0 so that f ðxÞ is near f ðx0Þ,’’ or even ‘‘so that
f ðxÞ is arbitrarily close to f ðx0Þ.’’ Let’s formalize these simpler statements and see
what goes wrong.
Definition 9.9 (Version 1)
f ðxÞ is almost continuous at a point x0 if for any  > 0
there is an x so that j f ðxÞ  f ðx0Þj < .
Well this version does not tell us very much, since it does not even ensure that x is
anywhere near x0.
Definition 9.10 (Version 2)
f ðxÞ is almost continuous at a point x0 if for any  > 0
there is an x so that jx  x0j <  and j f ðxÞ  f ðx0Þj < .
This version 2 makes a bit more sense because at least we can be sure that
as we require f ðxÞ to be nearer to f ðx0Þ, that there are x-values that work for
which x becomes nearer to x0. On the other hand, this definition allows there to be
lots of x-values that are close to x0 for which f ðxÞ is far, perhaps very far, from
f ðx0Þ.
Example 9.11
The classical example of this almost continuous situation is
f ðxÞ ¼
sin 1
x ;
x 0 0;
0;
x ¼ 0,

as graphed in figure 9.1. This graph satisfies the definition of ‘‘almost continuous (ver-
sion 2) at x0 ¼ 0,’’ where f ð0Þ ¼ 0, since it is clear that ‘‘for any  > 0, there is an x so
that jx  x0j <  and j f ðxÞ  f ðx0Þj < .’’ In fact ‘‘for any  > 0, there is an x so that
jx  x0j <  and f ðxÞ ¼ f ð0Þ’’.
422
Chapter 9
Calculus I: Di¤erentiation

The inadequacy of this ‘‘almost continuous (version 2)’’ notion is further illus-
trated by the fact that if we arbitrarily define f ð0Þ as any number between 1 and
1, this definition is still satisfied. So the point is, what conclusions could be made
about such a function at x ¼ 0 if we can arbitrarily define its value there and still sat-
isfy the definition? Obviously we cannot predict this value of f ð0Þ from knowing the
value of f ðxÞ for x near 0.
Example 9.12
The example above can be made even more compelling by considering
gðxÞ ¼
1
x sin 1
x ;
x 0 0;
0;
x ¼ 0:

We then have that gðxÞ is ‘‘almost continuous (version 2) at x ¼ 0,’’ and and this will
be true even if we define gð0Þ as any real number! This is displayed in figure 9.2, where
it is noted that gðxÞ is unbounded both positively and negatively as x ! 0.
The important detail that the definition of continuity adds to the definition of ‘‘al-
most continuous (version 2),’’ is that it demands that the function f make all the
values of f ðxÞ close to f ðx0Þ, for x near x0, not just some of them. In doing so, it
allows the distance between x and x0 to di¤er from the distance between f ðxÞ and
f ðx0Þ, as long as we can choose the latter distance for any . So the final logic
becomes the chant, ‘‘. . . for any value  > 0, one can find a d > 0 . . . .’’
Figure 9.1
f ðxÞ ¼
sin 1
x ;
x 0 0
0;
x ¼ 0

9.2
Functions and Continuity
423

Example 9.13
The price of a 5-year zero-coupon bond per $1 par, in terms of an an-
nual rate, is given by PðrÞ ¼ ð1 þ rÞ5. To see that this is a continuous function at
r0 A ð0; yÞ, the goal is to be able to make jð1 þ rÞ5  ð1 þ r0Þ5j small by making
jr  r0j small. To this end, note that
jð1 þ rÞ5  ð1 þ r0Þ5j ¼ ð1 þ r0Þ5  ð1 þ rÞ5
ð1 þ rÞ5ð1 þ r0Þ5


< jð1 þ r0Þ5  ð1 þ rÞ5j;
since ð1 þ rÞ5ð1 þ r0Þ5 b 1 for r b 0, which we can assume by choosing  < r0. Now,
by the binomial theorem, ð1 þ r0Þ5  ð1 þ rÞ5 ¼ P5
j¼1
5
j
 	
½r j
0  r j, since the j ¼ 0
terms cancel. Each of the remaining terms r j
0  r j for j b 1 can be factored:
r j
0  r j ¼ ðr0  rÞ
X
j1
k¼0
rk
0 r jk1:
Combining, we get that jð1 þ rÞ5  ð1 þ r0Þ5j < Kjr0  rj, where K is choosen as the
largest numerical value of the P5
j¼1
5
j
 	 P j1
k¼0 rk
0 r jk1 factor. This bound would be de-
termined by noting that r < r0 þ  ¼ ar0, for some a > 1, and then
Figure 9.2
gðxÞ ¼
1
x sin 1
x ;
x 0 0
0;
x ¼ 0

424
Chapter 9
Calculus I: Di¤erentiation


K ¼ max
r<r0þ
X
5
j¼1
5
j

 X
j1
k¼0
rk
0 r jk1
¼
X
5
j¼1
5
j


r j1
0
X
j1
k¼0
a jk1 ¼
X
5
j¼1
5
j

 a j  1
a  1


r j1
0
:
Finally, from this we have that for any  > 0, jð1 þ rÞ5  ð1 þ r0Þ5j <  if jr0  rj <

K . That is, we define dðÞ ¼ 
K . In fact PðrÞ is continuous on r0 A ð1; yÞ, but more
care is needed for the numerical estimates, since there is an apparent problem at
r ¼ 1.
Note that in this example, no e¤ort was made to determine the best value of K, for
instance, by further restricting the range of allowable r-values in this maximum. To
simply verify continuity, the analysis can be crude to simplify the derivation, or more
refined. The conclusion of continuity does not depend on the size of this K, only that
there was some function dðÞ that worked for any .
The Meaning of ‘‘Discontinuous’’
Because of the logical complexity of the continuity definition, it makes sense to for-
malize the meaning of the notion that f ðxÞ is not continuous at x0, that is, f ðxÞ is
discontinuous at a point x0. This idea could be needed for the proof of any statement
of the form:
If property S, then f ðxÞ is continuous at x0.
For example, we could choose to use a contrapositive proof, whereby we would
attempt to prove
If f ðxÞ is discontinuous at x0, then @S,
or a proof by contradiction, whereby we would attempt to prove
If property S and f ðxÞ is discontinuous at x0, then @S.
In other words, for either of these approaches to a proof, a clear understanding is
needed of the meaning of the statement that ‘‘f ðxÞ is discontinuous at x0.’’
Using the ideas from chapter 1, we temporarily introduce statement notation:
P 1 f ðxÞ is continuous at x0;
QðÞ 1 j f ðxÞ  f ðx0Þj < ;
RðdÞ 1 jx  x0j < d:
9.2
Functions and Continuity
425

Then we have that P is defined by
P , EbdExðRðdÞ ) QðÞÞ:
The logical development of @P proceeds as follows, recalling that the universal
quantifiers are negations of each other:
@P $ @½EbdExðRðdÞ ) QðÞÞ
$ b @ ½bdExðRðdÞ ) QðÞÞ
$ bEd @ ½ExðRðdÞ ) QðÞÞ
$ bEdbx @ ðRðdÞ ) QðÞÞ
$ bEdbxðRðdÞ5@QðÞÞ:
Summarizing, we obtain:
Definition 9.14
f ðxÞ is discontinuous at a point x0 if there is an  > 0 so that for
any d > 0 we can find an x with jx  x0j < d and yet j f ðxÞ  f ðx0Þj b . More gener-
ally given this , for any sequence dn ! 0, we can find xn so that jxn  x0j < dn and
j f ðxnÞ  f ðx0Þj b . So xn ! x0 but f ðxnÞ n f ðx0Þ.
As will be seen below, every continuous function has the useful property that it pre-
serves convergence of sequences. To set the stage for this, first recall the -N defini-
tion of convergence from chapter 5, which is generalized here to functions. To obtain
this generalization, note that if fxng is a sequence, we can define a function
f : N ! R by
f ðnÞ ¼ xn:
Definition 9.15
A sequence fxng converges to x < y as n ! y, denoted xn ! x, if,
given any  > 0, one can find an N A N so that
jxn  xj < 
whenever
n b N:
Analogously, a function f ðxÞ converges to a limit L < y as x ! y, denoted
limx!y f ðxÞ ¼ L, if, given any  > 0, one can find an N so that
j f ðxÞ  Lj < 
whenever
x b N:
More generally, a function f ðxÞ converges to a limit L < y as x ! x0 < y, denoted
limx!x0 f ðxÞ ¼ L, if, given any  > 0, one can find a d > 0 so that
426
Chapter 9
Calculus I: Di¤erentiation

j f ðxÞ  Lj < 
whenever
jx  x0j < d:
In other words, convergence of a sequence implies that eventually all the terms of
the sequence get arbitrarily close to the limiting value. For convergence of a function
we require that f ðxÞ can be made arbitrarily close to L by choosing x close enough
to x0, or in the case of x0 ¼ y, the definition is adapted to ensure that f ðxÞ can be
made arbitrarily close to L by choosing x large enough.
Remark 9.16
It is important to understand that the notion of a limit of a function in
the definition above is two sided. That is to say, because of the absolute values in the
convergence criterion, the statement limx!x0 f ðxÞ ¼ L means that a limiting value for
f ðxÞ exists whether x ! x0 ‘‘from the right,’’ so that x > x0, or ‘‘from the left,’’ so that
x < x0, and that these limits are equal. ‘‘One-sided’’ limits can also be defined:
Definition 9.17
A function f ðxÞ converges to a limit L < y from the left as
x ! x0 < y, denoted limx!x
0 f ðxÞ ¼ L, if, given any  > 0, one can find a d > 0 so
that
j f ðxÞ  Lj < 
whenever
x0  d < x < x0:
A function f ðxÞ converges to a limit L < y from the right as x ! x0 < y, denoted
limx!xþ
0 f ðxÞ ¼ L, if, given any  > 0, one can find a d > 0 so that
j f ðxÞ  Lj < 
whenever
x0 < x < x0 þ d:
Notation 9.18
To economize on language, it is common to say that limx!x0 f ðxÞ
exists for all x0 A ½a; b, as a brief way of stating that limx!x0 f ðxÞ exists for all
x0 A ða; bÞ, and also that limx!aþ f ðxÞ and limx!b f ðxÞ exist.
Example 9.19
It is instructive to demonstrate by the definitions above that if f ðxÞ ¼
x2
1x2 , then limx!0 f ðxÞ ¼ 0 and limx!y f ðxÞ ¼ 1.
1. For the limit limx!0 f ðxÞ, we can arbitrarily restrict attention to jxj < 0:1 say,
since we only care about the limit at x ¼ 0. To make
x2
1x2


 small for jxj small, note
that
x2
1  x2


 < 100
99 x2 < 100
99 jxj;
since jxj < 0:1 implies that
1
1x2 < 100
99 and x2 < x. So to make
x2
1x2


 < , we can choose
jxj < dðÞ 1 99
100 .
9.2
Functions and Continuity
427

2. For the limit limx!y f ðxÞ, to make
x2
1x2  ð1Þ


 small for x large, note that
x2
1  x2 þ 1


 ¼
1
x2  1


 < 1
x ;
since x2  1 > x for x > 3, say. So to make
x2
1x2  ð1Þ


 < , we can choose N 1 1
 .
From the definitions above it should also be apparent that the statement: f ðxÞ is
continuous at x0, is equivalent to the statement that limx!x0 f ðxÞ ¼ f ðx0Þ. To say
that f ðxÞ is continuous on ða; bÞ is equivalent to the statement that limx!x0 f ðxÞ ¼
f ðx0Þ for all x0 A ða; bÞ. Finally, the notion of one-sided limits implies that the state-
ment, f ðxÞ is continuous on ½a; b is equivalent to the statement that limx!x0 f ðxÞ
¼ f ðx0Þ for all x0 A ða; bÞ, and also that limx!aþ f ðxÞ ¼ f ðaÞ, and limx!b f ðxÞ ¼
f ðbÞ.
This observation provides another simple way to think about functions that are
discontinuous at a point x0.
Definition 9.20
The function f ðxÞ is discontinuous at x0 if either:
1. limx!x0 f ðxÞ does not exist, or
2. limx!x0 f ðxÞ does exist and equals L, but f ðx0Þ 0 L.
For example, f ðxÞ ¼ 1
x is discontinuous at x ¼ 0 both because limx!0 1
x does not
exist, and because f ð0Þ is not defined. On the other hand,
gðxÞ ¼
x;
x 0 0
1;
x ¼ 0

is discontinuous at x ¼ 0 not because limx!0 gðxÞ does not exist but because gð0Þ 0
limx!0 gðxÞ ¼ 0.
*The Metric Notion of Continuity
Stated as in the definition above, continuity is seen to be a fundamentally ‘‘metric’’
notion. Recall from chapter 3 that jxj is a norm on R that gives rise to a metric or
distance function, defined by
dða; bÞ ¼ ja  bj:
Consequently the definition of continuity explicitly utilizes this notion of distance,
and with this notion it requires that we can make j f ðxÞ  f ðx0Þj as small as we
want by choosing jx  x0j small enough. In other words, for any value of  > 0, one
can find a d > 0 so that dðf ðxÞ; f ðx0ÞÞ <  whenever dðx; x0Þ < d.
428
Chapter 9
Calculus I: Di¤erentiation

The importance of this observation is that all of the development below for real-
valued functions of a real variable, f ðxÞ, carries over with only a notational change
to functions defined between any two metric spaces. For example, the notion of a
continuous complex-valued function of a complex variable, as well as other examples,
can be framed directly in terms of the respective metrics. We leave this general point
here for now, and continue to develop the theory in the more familiar setting of
Dmnð f Þ H R.
Also more generally, one can develop additional intuition for continuity by intro-
ducing a more geometric interpretation. Recall the open ball constructions from
chapter 4 in (4.1):
BrðxÞ ¼ fy A R j jx  yj < rg:
The definition of continuity can then be restated in two ways, each of which has
apparent application to the more general framework of later chapters and more
advanced mathematical treatments.
Definition 9.21
1. f ðxÞ is continuous at a point x0 if for any value  > 0 one can find a d > 0 so that
f ðBdðx0ÞÞ H Bðf ðx0ÞÞ:
2. f ðxÞ is continuous at a point x0 if for any integer n > 0 one can find an integer
m > 0 so that
f ðB1=mðx0ÞÞ H B1=nðf ðx0ÞÞ:
In other words, continuity at x0 means that however small an open ball one con-
structs around f ðx0Þ, one can find an open ball around x0 that gets mapped into it.
Interpreted this way, it is again apparent that the notion of continuity is very gen-
erally applicable to all metric spaces. Below it will be seen to be applicable even be-
yond metric spaces.
Sequential Continuity
Another notion of continuity that is equivalent to that above is the notion of sequen-
tial continuity, which we define next.
Definition 9.22
f ðxÞ is sequentially continuous at x0 if, given any sequence fxng such
that xn ! x0, then f ðxnÞ ! f ðx0Þ. Similarly f ðxÞ is sequentially continuous on an in-
terval if it has this property at every point of the interval.
9.2
Functions and Continuity
429

Proposition 9.23
f ðxÞ is continuous at x0 if and only if it is sequentially continuous
at x0.
Proof
See exercise 28.
n
9.2.3
Basic Properties of Continuous Functions
While providing various intuitive frameworks for continuity, none of the preceding
definitions provide an accessible approach to demonstrating that a given function is
continuous in any but the simplest cases. For example, how might one prove that
f ðxÞ ¼ x5 þ x4 þ x3
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðx6 þ 4Þ
p
þ xðx2þxÞ is continuous for all x > 0? Certainly the
prospect of determining d for a given  > 0 is not appealing, and determining
the general formula for dðÞ is even less so.
The following propositions state that the notion of continuity combines well arith-
metically, and in a variety of other ways.
Proposition 9.24
If f ðxÞ and gðxÞ are continuous at x0, then the following are also
continuous at x0:
1. af ðxÞ þ b, for a; b A R
2. f ðxÞ þ gðxÞ
3. f ðxÞ  gðxÞ
4. f ðxÞgðxÞ
5.
f ðxÞ
gðxÞ if gðx0Þ 0 0
Proof
In each case the objective is to show that if we can make both j f ðxÞ  f ðx0Þj
and jgðxÞ  gðx0Þj arbitrarily small by choosing jx  x0j small, that this property
transfers to the given combinations. Denoting by dðÞ the value that works for both
f and g given , which is defined as the smaller of the respective values, we find d0ðÞ,
the value that is needed for the given combination.
1. j½af ðxÞ þ b  ½af ðx0Þ þ bj ¼ jaj j f ðxÞ  f ðx0Þj, so we can choose d0ðÞ ¼ d

jaj
 	
.
2. j½ f ðxÞ þ gðxÞ  ½ f ðx0Þ þ gðx0Þj a j f ðxÞ  f ðx0Þj þ jgðxÞ  gðx0Þj by the triangle
inequality, so we choose d0ðÞ ¼ d 
2
 
.
3. This follows from part 1, with a ¼ 1 and b ¼ 0, and then part 2 applied to the
continuous f ðxÞ and gðxÞ.
4. By the triangle inequality,
j f ðxÞgðxÞ  f ðx0Þgðx0Þj ¼ j½f ðxÞgðxÞ  f ðx0ÞgðxÞ þ ½ f ðx0ÞgðxÞ  f ðx0Þgðx0Þj
a Mj f ðxÞ  f ðx0Þj þ j f ðx0Þj jgðxÞ  gðx0Þj;
430
Chapter 9
Calculus I: Di¤erentiation

where M denotes any upper bound for jgðxÞj on jx  x0j < d. Such an upper bound
must exist; that is, if we are given that jgðxÞ  gðx0Þj < , then since gðxÞ ¼ gðx0Þ þ
ðgðxÞ  gðx0ÞÞ, we have by the triangle inequality that jgðxÞj < jgðx0Þj þ . We can
hence choose d0ðÞ ¼ min d

2M


; d

2j f ðx0Þj

	
h
i
if f ðx0Þ 0 0. Otherwise, if f ðx0Þ ¼ 0,
then j f ðxÞgðxÞ  f ðx0Þgðx0Þj a Mj f ðxÞ  f ðx0Þj, and we take d0ðÞ ¼ d

M
 
.
5. First o¤, since gðx0Þ 0 0, and gðxÞ is continuous at x0, for  ¼ gðx0Þ
2
there is a d00 so
that jgðxÞ  gðx0Þj < gðx0Þ
2
for jx  x0j < d00. Consequently gðxÞ 0 0 for jx  x0j < d00.
Next
f ðxÞ
gðxÞ  f ðx0Þ
gðx0Þ


 ¼ f ðxÞgðx0Þ  f ðx0ÞgðxÞ
gðxÞgðx0Þ


¼ f ðxÞgðx0Þ  f ðx0Þgðx0Þ þ f ðx0Þgðx0Þ  f ðx0ÞgðxÞ
gðxÞgðx0Þ


a f ðxÞ  f ðx0Þ
gðxÞ


 þ f ðx0Þ
gðx0Þ
gðx0Þ  gðxÞ
gðxÞ


a mj f ðxÞ  f ðx0Þj þ cmjgðxÞ  gðx0Þj;
where m is the maximum value of
1
gðxÞ for jx  x0j < d00 and c ¼
f ðx0Þ
gðx0Þ


. We can now
choose d0ðÞ ¼ min d

2m


; d

2cm


; d00


.
n
Example 9.25
Returning to the question on verification of the continuity of compli-
cated functions, the proposition above provides useful tools. Since f ðxÞ ¼ x is obviously
continuous with dðÞ ¼ , it follows that every integer power of x is also continuous,
since these are products of f ðxÞ, as is any polynomial in x, since this equals sums and
scalar multiples of these continuous integer powers of x. Similarly every rational func-
tion, defined as a ratio of polynomials, is continuous everywhere the denominator poly-
nomial is nonzero.
The final building blocks for confirming the continuity of complicated functions fol-
low in a series of propositions below:
1. The first proposition addresses inverses of one-to-one functions, which will imply
that f ðxÞ ¼ x1=n is continuous on x b 0 for all integer n A N, as is f ðxÞ ¼ x1=n for
x > 0.
2. The second proposition addresses compositions of continuous functions, from which
one derives the continuity of many common functions, for instance, f ðxÞ ¼ xm=n for all
integers m; n 0 0, as well as various linear combinations of such functions and ratios of
these combinations with nonzero denominators.
9.2
Functions and Continuity
431

3. Last, the common exponential functions f ðxÞ ¼ ax for some real number a > 0 re-
quire direct verification of continuity, from which the associated logarithms gðxÞ ¼
loga x will be continuous for x > 0 as these are inverse functions to the exponentials.
Then for irrational exponents q the continuity of f ðxÞ ¼ xq follows for x > 0 by noting
that f ðxÞ ¼ eq ln x, which is a composition of continuous functions.
Proposition 9.26
If f ðxÞ is continuous at x0 and one-to-one in an open interval about
x0, then f 1 is continuous at f ðx0Þ.
Proof
Assume that f ðxÞ is continuous at x0 and one-to-one on an open interval I
about x0, and let J H I be the closure of a bounded open subinterval, with x0 A J.
We restrict f to J and show that f 1 is then continuous at f ðx0Þ by a proof by con-
tradiction. If f 1 is discontinuous at f ðx0Þ, then there exists an 0 > 0 and a sequence
fyng H f ðJÞ so that jyn  f ðx0Þj < 1
n yet j f 1ðynÞ  f 1ðf ðx0ÞÞj ¼ jxn  x0j > 0 for
all n. Now, since J is compact and fxng H J, there is an accumulation point x0 A J
and a subsequence fx0
ng H fxng so that x0
n ! x0. Hence, since jxn  x0j > 0 for all
n, it follows that jx0
n  x0j > 0, and so jx0  x0j b 0. However, jyn  f ðx0Þj ¼
j f ðxnÞ  f ðx0Þj < 1
n implies that j f ðx0
nÞ  f ðx0Þj ! 0. But x0
n ! x0 and continuity of
f ðxÞ then implies j f ðx0
nÞ  f ðx0Þj ! 0 and so f ðx0Þ ¼ f ðx0Þ. We now have a contra-
diction. Namely jx0  x0j > 0 and f ðx0Þ ¼ f ðx0Þ contradicts that f is one-to-one. n
The following proposition applies to the composition of any collection of continu-
ous functions, by iteration:
Proposition 9.27
If gðxÞ is continuous at x0, and f ðxÞ is continuous at gðx0Þ, then
f ðgðxÞÞ is continuous at x0.
Proof
Given  > 0, the goal is to find dðÞ so that j f ðgðxÞÞ  f ðgðx0ÞÞj < 
when jx  x0j < dðÞ. By continuity of f ðxÞ, we conclude for any  < 0 that
j f ðgðxÞÞ  f ðgðx0ÞÞj <  if jgðxÞ  gðx0Þj < d0ðÞ, where d0 denotes the associated
function for f ðxÞ. Next, by the continuity of gðxÞ, we conclude that jgðxÞ  gðx0Þj
< d0ðÞ when jx  x0j < d00ðd0ðÞÞ, where d00 denotes the associated function for gðxÞ.
Hence we choose dðÞ ¼ d00ðd0ðÞÞ.
n
Finally, we address the exponential and logarithmic functions.
Proposition 9.28
The function f ðxÞ ¼ ex is continuous for all x A R.
Proof
Given x0, ex  ex0 ¼ ex0½exx0  1 so that ex is continuous at x0 if, for any ,
we can find a d so that ex0jexx0  1j <  whenever jx  x0j < d. Since ex0 is just a
number, this result will follow if ey is continuous at y ¼ 0. Then for any 0 we can
find a d0 so that jey  1j < 0 whenever jyj < d0, and so given , we define 0 ¼

e x0
432
Chapter 9
Calculus I: Di¤erentiation

and d ¼ d0. In summary, if ey is continuous at y ¼ 0, it is continuous everywhere.
Now by section 9.3.3, e > 1, and we have that ey > 1 and ey < 1 for y > 0. Hence
ex is a monotonically increasing function on R, meaning, if x0 < x, then ex 0 < ex.
This is because if x ¼ x0 þ x00 for some x00 > 0, then ex ¼ ex 0ex 00 > ex 0. Also, since
ðey  1Þ2 b 0, we derive by expansion that
ey  1 b 1  ey b 0:
So, if for any  > 0, there is a d so that 0 a ey  1 <  whenever 0 a y < d; then also
0 < 1  ey < , and hence for jyj < d it follows that jey  1j <  and the proof of
continuity at y ¼ 0 will be complete. To this end, let  > 0 be given, and consider
the sequence xn ¼ eyn where yn > 0 and yn ! 0 monotonically. Consequently xn > 1
for all n. Also the monotonicity of ex implies that xn is a monotonically decreasing
sequence. It is also bounded from below by 1, and hence it has a unique accumula-
tion point x0. If x0 ¼ 1, we are done. But assume that x0 > 1. Then xn ! x0, and is
monotonically decreasing. Therefore
e ¼ x1=yn
n
> x1=yn
0
;
but this is a contradiction, since x0 > 1 and yn ! 0 implies x1=yn
0
! y. Consequently
x0 ¼ 1.
n
Example 9.29
The continuity of ex implies the continuity of its inverse function, ln x
for x > 0, since ex is one-to-one. For a > 0 the function f ðxÞ ¼ ax is then continuous
as a composite function, since ax ¼ ex ln a. Similarly the continuity of loga x follows for
x > 0 and a > 0, since loga x ¼ ln x
ln a , and also of xx ¼ ex ln x for x > 0.
9.2.4
Uniform Continuity
As noted in the preceding section, a formal demonstration of continuity requires an
explicit expression for d as a function of , d 1 dðÞ. It should also be noted that such
a demonstration can be complicated by the fact that while the value of d in the defi-
nition of continuity apparently depends on , it can also in general depend on x0, so
d 1 dð; x0Þ.
Example 9.30
The function
f ðxÞ ¼ 1=x is continuous throughout its domain:
Dmnð f Þ ¼ fx j x 0 0g. However, it is not di‰cult to verify that for a given  and pos-
itive x0, that the associated d is also a function of  and x0:
dð; x0Þ ¼
x2
0
1 þ jx0j :
9.2
Functions and Continuity
433

This is justified for x0 > 0 say, by noting that if jx  x0j < d, with d < x0
2 to keep x > 0;
then
1
x  1
x0


 <
d
xx0
<
d
ðx0  dÞx0
:
To have
1
x  1
x0


 < , we solve for d producing the formula above. Consequently, for a
given , d can be arbitrarily large if jx0j is large, yet it must be choosen increasingly
small as jx0j approaches 0. This is, of course, also apparent from the graph of f ðxÞ.
An important notion is that of uniform continuity, whereby it is possible to choose
d to be independent of x0.
Definition 9.31
f ðxÞ is uniformly continuous on an interval if for any value  > 0 one
can find a d > 0 so that for all x and y in the interval, j f ðxÞ  f ðyÞj <  whenever
jx  yj < d. Similarly f ðxÞ is uniformly continuous if it satisfies this property for all x
and y in its domain.
Example 9.32
f ðxÞ ¼ 1=x is uniformly continuous on any closed interval ½a; b not
containing the origin. This is easily demonstrated using example 9.30 in that one
chooses d to equal the minimum value of dðx0Þ for x0 in the interval, which is appar-
ently the value of dðxÞ at the endpoint of the interval closest to 0.
This example is generalized below. But note that the idea of uniform continuity is
that for any  > 0 the associated d in the definition of continuity, which in general is
a function of both x and , dðx; Þ, satisfies dðx; Þ > dðÞ > 0 for all x for some other
function, dðÞ. So what keeps a continuous function from being uniformly continuous
is that for a given , the dðx; Þ values get arbitrarily close to 0 as x varies. This was
seen in example 9.30, where f ðxÞ ¼ 1=x.
We return to this point after the next result. Its proof relies on a simple but impor-
tant property of closed and bounded intervals which we have encountered before in
chapter 4 in proposition 4.17. We prove this simpler version directly.
Proposition 9.33
If frjg is a bounded infinite sequence of reals frjg H ½a; b, then there
is a subsequence fr0
jg and a point r A ½a; b so that r0
j ! r as j ! y.
Proof
Divide the interval into halves:
a; aþb
2


and
aþb
2 ; b


. Then one or both of
these subintervals contains an infinite subsequence of frjg, and we choose that sub-
interval if unique, or an arbitrary subinterval otherwise. We also choose r0
1 to be any
point in the choosen interval. We then divide that subinterval in half, and once again
observe that one or both of the new subintervals contains an infinite subsequence. So
434
Chapter 9
Calculus I: Di¤erentiation

we choose one, as well as r0
2 in that subinterval. Continuing in this manner, we obtain
a sequence of nested intervals of length aþb
2 j , each of which contains one member of
the desired sequence fr0
jg. It is clear that the intersection of all choosen subintervals is
a single point r, since, if it contained more than one point, it would also contain the
interval spanning the two points, in contradiction to the fact that the lengths of these
subintervals converge to 0 by the halving property of the construction. Finally, by
construction jr0
j  rj < aþb
2 j , so r0
n ! r as required.
n
By the Heine–Borel theorem, the closed and bounded interval ½a; b is compact.
This result is then a special case of the general chapter 4 result noted above that if a
compact set K contains an infinite sequence frjg, then there is a subsequence fr0
jg and
a point r A K so that r0
j ! r as j ! y. However, this proof was supplied rather than
simply quoting the proposition 4.17 result because in this application, as in many, the
construction in the special case is revealing and too simple to avoid.
Note that this proposition addresses the existence of such a point r, and it cannot
be improved to assert the uniqueness of this point. Indeed it is possible that in every
subinterval of the construction above there is an infinite subsequence of the original
sequence frjg.
Example 9.34
Let frjg denote an arbitrary enumeration of the rational numbers in
½a; b. Then the construction above shows that for every real number r A ½a; b there is
a subsequence fr0
jg H ½a; b so that r0
j ! r as j ! y. One simply chooses, at each step,
the subinterval that contains the given point, r.
Proposition 9.35 (Version 1)
If f ðxÞ is continuous on a closed and bounded interval
½a; b, then it is uniformly continuous on this interval.
Proof
Assume that  > 0 is given. For each number r A ½a; b, let dðrÞ 1 dðr; Þ de-
note the associated delta for this . We claim that fdðrÞg is bounded away from 0,
and that we can take d in the definition of uniform continuity to be equal to any non-
zero lower bound for this collection. To show this boundedness, assume that it is not,
and a contradiction will be revealed. That is, assume that there is a sequence of real
numbers rj with dðrjÞ ! 0. Then for each positive integer k there is an associated rk
and xk so that j f ðrkÞ  f ðxkÞj b  and jrk  xkj < 1
k . If such points did not exist for
k b K, say, then f ðxÞ would be uniformly continuous with d ¼ 1
K . Now we demon-
strate a contradiction to the continuity of f ðxÞ. The sequences frkg and fxkg have
subsequences that converge by the proposition above, and must converge to the
same point in ½a; b, since jrk  xkj < 1
k . But since j f ðrkÞ  f ðxkÞj b , we cannot
have f f ðrkÞg and f f ðxkÞg convergent to the same point, contradicting the sequential
9.2
Functions and Continuity
435

continuity, and hence continuity of f ðxÞ. Hence fdðrÞg is bounded away from 0 and
the proof is complete.
n
From the comments above on compactness, one would have to think that this
result is somehow related to the compactness of the interval ½a; b, and that on this
basis the result will generalize. Recall that by compactness is meant that every collec-
tion of open intervals that cover ½a; b contains a finite subcover, which is to say, a
finite subcollection that also covers this interval. We demonstrate this general case
with an alternative proof.
Proposition 9.36 (Version 2)
If f ðxÞ is continuous on a compact set, K H R, then it is
uniformly continuous on K.
Proof
Assume that  > 0 is given. For each number r A K, let dðrÞ denote the
associated delta for 
2 . Next consider the interval defined by dðrÞ for a given r:
Ir ¼
r0 j jr  r0j < dðrÞ
2
n
o
. The reason for this sleight of hand of dividing  by 2 will
be apparent in a moment. Now consider fIrg for all r A K. Clearly, this is an
open cover for K, which due to compactness, has a finite subcover, fIrjgn
j¼1.
Define dðÞ ¼ 1
2 minfdðrjÞg and let r0; r00 A K with jr0  r00j < dðÞ. Then, since r0 A Irj
for some j, jr0  rjj < dðrjÞ
2 , and so j f ðr0Þ  f ðrjÞj < 
2 . Also, by the triangle in-
equality,
jr00  rjj a jr00  r0j þ jr0  rjj
< dðÞ þ dðrjÞ
2
a dðrjÞ;
and hence j f ðrjÞ  f ðr00Þj < 
2 . Finally, by another application of the triangle
inequality,
j f ðr0Þ  f ðr00Þj a j f ðr0Þ  f ðrjÞj þ j f ðrjÞ  f ðr00Þj
< :
n
Remark 9.37
A few comments are in order:
1. There are basically two approaches to the kind of proof just given:
 Reverse engineer all the intermediate steps so that one gets the desired conclusion that
j f ðr0Þ  f ðr00Þj <  in the last line of the proof. This is the approach used above. It fits
right into the definition that ‘‘for any  > 0 one can find a d so that . . . .’’ The advantage
436
Chapter 9
Calculus I: Di¤erentiation

is that the continuity definition is produced verbatim; the disadvantage, which the
reader undoubtedly encountered, is the temporary mystery associated with the 1
2 factors,
which in other proofs may be 1
3 , 1
4 , and so forth.
 Ignore the reverse engineering and ultimately derive something like j f ðr0Þ  f ðr00Þj <
4. Then we prove a statement like ‘‘given  > 0 there is a d so that if jr0  r00j < d, then
j f ðr0Þ  f ðr00Þj < 4.’’ Of course, this is logically equivalent to the original idea, but
some find the presence of the 4 in the conclusion to be aesthetically unpleasant.
The present author alternates between these approaches, and generally prefers the sec-
ond approach in personal research, and the first approach in communications. However,
the reverse engineering required to produce a clean conclusion can at times add unjusti-
fiable complexity to the derivation, and so will sometimes be abandoned.
2. One can easily imagine going through the proof above almost verbatim if K is a
compact subset of any metric space ðX; dÞ and f ðxÞ is a continuous function from X
to R, or from X to another metric space ðY; d 0Þ. See exercises 5 and 30.
9.2.5
Other Properties of Continuous Functions
A few other fundamental results on continuous functions are addressed next. The
first is simple but powerful. Namely the sign of a continuous function at a point
must be preserved in some open interval about that point.
Proposition 9.38
If f ðxÞ is continuous at x0, and f ðx0Þ 0 0, then there is an interval
about x0, say I ¼ ðx0  a; x0 þ aÞ for some a > 0, so that
f ðx0Þ > 0 ) f ðxÞ > 0
for all x A I;
f ðx0Þ < 0 ) f ðxÞ < 0
for all x A I:
Proof
We demonstrate the result for f ðx0Þ > 0. By continuity, for  ¼ 1
2 f ðx0Þ say,
there is a d so that
j f ðxÞ  f ðx0Þj < 1
2 f ðx0Þ
when
jx  x0j < d:
If this inequality is rewritten without the absolute values, it implies that
1
2 f ðx0Þ < f ðxÞ < 3
2 f ðx0Þ
for x0  d < x < x0 þ d;
and this completes the proof with a ¼ d.
n
9.2
Functions and Continuity
437

The next result is that a continuous function is bounded on a compact interval, but
far more important, such a function actually achieves these bounds at points within
the interval.
Proposition 9.39
If f ðxÞ is continuous on a closed and bounded (i.e., compact) inter-
val ½a; b, then f ðxÞ attains its maximum and minimum values within this interval. That
is, there are points xmin; xmax A ½a; b, so that for all x A ½a; b,
f ðxminÞ a f ðxÞ a f ðxmaxÞ:
Proof
Because f ðxÞ is uniformly continuous on ½a; b, it must be bounded from
above and below. Indeed, for an arbitrary value of , there is an associated d so that
j f ðxÞ  f ðyÞj <  whenever jx  yj < d. This implies that the range of f ðxÞ must be
contained in an interval of length N, where integer N > ðbaÞ
d
, since we can then
cover ½a; b with N intervals of length d. Now, because f ðxÞ is bounded, there must
be a greatest lower bound, and least upper bound, which we denote by L and U. By
definition, we can construct two sequences fxL
n g and fxU
n g, both in ½a; b and so that
f ðxL
n Þ ! L, and f ðxU
n Þ ! U. By the proposition above, these sequences must each
have subsequences that converge to points in ½a; b, xL
n ! xmin and xU
n ! xmax, and
by the continuity of f ðxÞ, this convergence is preserved by f so that f ðxL
n Þ !
f ðxminÞ and f ðxU
n Þ ! f ðxmaxÞ. Hence, again by continuity, L ¼ f ðxminÞ and U ¼
f ðxmaxÞ.
n
Remark 9.40
Note that the idea of a maximum or minimum in mathematics is di¤er-
ent from what one may understand of these terms informally. Outside mathematics, the
notion of a maximum is one of biggest, while the notion of a minimum is one of small-
est. In mathematics, the term maximum simply means that there is no value of x with
f ðxÞ > f ðxmaxÞ; it does not preclude the possibility that there are many values of x
with f ðxÞ ¼ f ðxmaxÞ, and likewise for the term minimum. While in the real world,
such an interpretation is not excluded by the language, it tends to be excluded in prac-
tice. For example, the statement, ‘‘I got the maximum grade in my class on the math
final’’ would generally not be expected to include the possibility that everyone got the
same grade. In mathematics the possibility that f ðxÞ ¼ f ðxmaxÞ for all x is explicitly
allowed and encompassed by the notion that ‘‘ f ðxÞ attains its maximum at x0.’’
The final result reinforces the intuitive notion that the graph of a continuous func-
tion must be drawn without the pencil leaving the paper, or in updated imagery, on
your computer without your finger leaving the mouse button. In other words, with
no holes or gaps in the graph.
438
Chapter 9
Calculus I: Di¤erentiation

Proposition 9.41 (Intermediate Value Theorem)
If f ðxÞ is continuous on a closed and
bounded (i.e., compact) interval ½a; b, then f ðxÞ attains every value between its maxi-
mum and minimum values. That is, for any point y so that f ðxminÞ a y a f ðxmaxÞ,
there is a point c A ½a; b with
f ðcÞ ¼ y:
ð9:1Þ
Proof
Let y be given. We define A ¼ fx A ½a; b j f ðxÞ a yg. Let xA denote the least
upper bound of the set A, and let fxng H A be a sequence so that xn ! xA. Then, by
continuity, f ðxnÞ ! f ðxAÞ a y. Because xA is a least upper bound for A, it must
also be the case that there is sequence fx0
ng H ~
A 1 fx j f ðxÞ b yg with x0
n ! xA. By
continuity, we have that f ðx0
nÞ ! f ðxAÞ, and hence that f ðxAÞ b y. Combining, we
see that f ðxAÞ ¼ y, and the conclusion follows.
n
While the notion of continuity assures us what the value of f ðx0Þ will be based on
values of f ðxÞ for x ‘‘near’’ x0, it provides no insight as to how quickly the value of
f ðxÞ approaches this value. The notions of Lipschitz and Ho¨lder continuity address
this question next.
9.2.6
Ho¨lder and Lipschitz Continuity
Definition 9.42
f ðxÞ is Ho¨lder continuous at a given point x0 of order a > 0 if there is
a constant C 1 Cðx0Þ so that
j f ðxÞ  f ðx0Þj a Cjx  x0ja:
ð9:2Þ
More generally, we say that f ðxÞ is Ho¨lder continuous of order a > 0 on an interval or
simply Ho¨lder continuous of order a > 0, if it is Ho¨lder continuous at every point of the
interval or of its domain. In the special case when a ¼ 1, f ðxÞ is called Lipschitz con-
tinuous instead of Ho¨lder continuous of order 1.
Notation 9.43
To simplify terminology, the statement that ‘‘f ðxÞ is Ho¨lder continuous
of order a > 0’’ will be be intended to include the a ¼ 1 Lipschitz case.
Lipschitz continuity is named for Rudolf Lipschitz (1832–1903), and Ho¨lder conti-
nuity is named for Otto Ho¨lder (1859–1937). In practice, one only considers Ho¨lder
continuity of order a a 1, since the only functions that can be continuous of higher
order, except at isolated points, are the constant functions: f ðxÞ ¼ c. The demonstra-
tion of this follows in the next section in two steps:
1. Once derivatives are defined and studied, we will see that such a function has a
derivative that is identically 0 everywhere.
9.2
Functions and Continuity
439

2. With the help of the mean value theorem, we will then see that the only continu-
ous functions with an identically 0 derivative are the constant functions.
These notions of continuity can also be thought of as providing an explicit func-
tional relationship between the  and d in the definition of continuity. Specifically, a
Ho¨lder continuous function can be defined as a continuous function for which given
 one can choose dðÞ by
dðÞ ¼

C
 1=a
:
Knowing that a function is Ho¨lder continuous is valuable, since this knowledge
provides an explicit estimate of exactly how fast f ðxÞ converges to f ðx0Þ in terms of
the distance between x and x0. For instance, a Lipschitz continuous function con-
verges with speed jDxj 1 jx  x0j, whereas a Ho¨lder continuous function of order
1
2 converges with speed
ffiffiffiffiffiffiffiffi
jDxj
p
. In general, this speed of convergence implies an ap-
proximation formula:
f ðx0Þ  Cjx  x0ja a f ðxÞ a f ðx0Þ þ Cjx  x0ja:
ð9:3Þ
This notion of speed of convergence is formalized in mathematics in terms of ‘‘Big
O’’ and ‘‘Little o’’ notation as follows.
Big O and Little o Convergence
Definition 9.44
A function f ðxÞ is Big O of gðxÞ as x ! a, denoted
f ðxÞ ¼ OðgðxÞÞ
as x ! a;
if there is a C 0 0 and d > 0 so that
j f ðxÞj
jgðxÞj a C
for jx  aj < d:
Similarly a function f ðxÞ is Little o of gðxÞ as x ! a, denoted
f ðxÞ ¼ oðgðxÞÞ
as x ! a;
if
j f ðxÞj
jgðxÞj ! 0
as x ! a:
440
Chapter 9
Calculus I: Di¤erentiation

Remark 9.45
In most applications in this book, we will be interested in expressing
jDf j 1 j f ðx þ DxÞ  f ðxÞj in terms of gðxÞ ¼ jDxja. The common language we use is,
‘‘Df is Big O of order a’’ or ‘‘Little o of order a.’’ Also of interest in this context is
Oð1Þ, which means j f ðxÞj a C as x ! a, and especially oð1Þ, which means f ðxÞ ! 0
as x ! a.
Example 9.46
If f ðxÞ is Ho¨lder continuous at x of order a, then
jDf j ¼ OðjDxjaÞ;
where Df 1 f ðx þ DxÞ  f ðxÞ, but if f ðxÞ is simply continuous at x, then
jDf j ¼ oð1Þ
as Dx ! 0.
Because the definition of continuity can be informally summarized by
jDf j ! 0
as jDxj ! 0;
it is tempting to think that every continuous function must be Ho¨lder continuous of
some order a, perhaps a value of a quite close to 0, In other words:
Question:
If jDf j ! 0, as jDxj ! 0, must it be the case that jDf j ¼ OðjDxjaÞ for
some a > 0?
Answer:
‘‘No.’’ A continuous function’s speed of convergence can be slower than
Ho¨lder at any order.
Example 9.47
Consider:
f ðxÞ ¼
1
lnjxj ;
x 0 0,
0;
x ¼ 0.
(
First o¤, this function is continuous at x ¼ 0, as can be seen by considering xn ¼ en,
for example, and evaluating f ðxÞ. But it is not Ho¨lder continuous of any order. This
is demonstrated by considering xn ¼ en=a for an arbitrary value of a > 0. Then since
f ðxnÞ ¼  a
n , and xa
n ¼ en, if f ðxÞ was Ho¨lder continuous of order a, then there would
exist C > 0 so that
j f ðxnÞj a Cjxa
nj
as n ! y;
which in turn implies that
9.2
Functions and Continuity
441

a a Cnen
as n ! y:
But since nen ! 0, no such a > 0 can exist.
It is also tempting to think that because Little o convergence is faster than Big O
convergence, it must be the case that Little o implies Big O convergence at a higher
order. In other words:
Question:
If jDf j ¼ oðjDxjaÞ, must jDf j ¼ OðjDxjaþÞ for some  > 0?
Answer:
‘‘No.’’ While oðjDxjaÞ is faster than OðjDxjaÞ, it can be slower than
OðjDxjaþÞ for any  > 0.
Example 9.48
Take gðxÞ ¼ xaf ðxÞ, with f ðxÞ defined in example 9.27 above. Then
the same analysis shows that at x ¼ 0, jDgj ¼ oðjDxjaÞ, but that we do not have
jDgj ¼ OðjDxjaþÞ for any  > 0.
9.2.7
Convergence of a Sequence of Continuous Functions
There is another important notion related to continuity which we introduce with the
following question:
Question:
If fnðxÞ is a sequence of continuous functions, and there is a function
f ðxÞ so that for every x, fnðxÞ ! f ðxÞ as n ! y, must f ðxÞ be continuous?
Answer:
In general, the answer is no, and this conclusion is easy to exemplify.
Example 9.49
Define
f ðxÞ ¼
1;
x a 0;
0;
x > 0;

and
fnðxÞ ¼
1;
x a 0,
1  nx;
0 < x a 1
n,
0;
x > 1
n.
8
>
<
>
:
ð9:4Þ
It is clear that fnðxÞ is continuous for all n, and that f ðxÞ is not continuous at x ¼ 0.
Also, for every x, fnðxÞ ! f ðxÞ as n ! y. To understand why f ðxÞ n f ð0Þ ¼ 1 as
x ! 0, we expand for any given n,
f ðxÞ  f ð0Þ ¼ ½ f ðxÞ  fnðxÞ þ ½ fnðxÞ  fnð0Þ þ ½ fnð0Þ  f ð0Þ:
442
Chapter 9
Calculus I: Di¤erentiation

As x ! 0, only the first term in brackets requires analysis, since by continuity of each
fnðxÞ, the second term goes to 0 for any n and the third term is identically 0. Now note
that
f ðxÞ  fnðxÞ ¼
0;
x a 0;
nx  1;
0 < x a 1
n,
0;
x > 1
n.
8
>
<
>
:
In other words, although fnðxÞ ! f ðxÞ for each x as n ! y, it does so increasingly
slowly as x ! 0. That is, for any x > 0 we have fnðxÞ ! f ðxÞ because fnðxÞ ¼ f ðxÞ
¼ 0 for n > 1
x . But for 0 < x a 1
n we have
f ðxÞ  f ð0Þ ¼ ½ f ðxÞ  fnðxÞ  nx
¼ 1:
The following definition introduces an important notion of convergence that proves
to give the a‰rmative conclusion to the question above. It will be seen that this def-
inition eliminates the problem observed in this example, whereby the speed of con-
vergence varies greatly with n.
Definition 9.50
A function sequence fnðxÞ is said to converge pointwise to f ðxÞ on an
interval I if for every x A I, fnðxÞ ! f ðxÞ as n ! y. That is, for any  > 0 there is an
integer N ¼ NðxÞ so that j fnðxÞ  f ðxÞj <  for n > NðxÞ. Pointwise convergence on
an arbitrary set K H R is defined similarly. A function sequence fnðxÞ is said to con-
verge uniformly to f ðxÞ on an interval I if for any  > 0 there is an integer N, indepen-
dent of x, so that for x A I: j fnðxÞ  f ðxÞj <  for n > N. Uniform convergence on an
arbitrary set K H R is defined similarly.
It should be clear from the definition that uniform convergence implies pointwise
convergence. Also example 9.49 provides an illustration that this implication cannot
be reversed in general. In that example fnðxÞ ! f ðxÞ pointwise for every x A R, but
this convergence is not uniform. For example, with  ¼ 1
2 , since j fnðxÞ  f ðxÞj ¼
1  nx for 0 < x a 1
n , we have that for any n, j fnðxÞ  f ðxÞj > 1
2 for 0 < x a 1
2n . In
other words, we cannot have j fnðxÞ  f ðxÞj <  for all n and all jxj < d independent
of how small a value of d is chosen since for any n with 1
2n < d, the calculations above
show that j fnðxÞ  f ðxÞj > 1
2 for 0 < x < 1
2n .
The next result demonstrates that unlike what was seen to be the case for pointwise
convergence, uniform convergence preserves continuity.
9.2
Functions and Continuity
443

Proposition 9.51
If fnðxÞ is a sequence of continuous functions that converge uni-
formly to f ðxÞ on an interval I, then f ðxÞ is continuous on I.
Remark 9.52
Note that by the proposition 9.33, if I is a closed and bounded (i.e.,
compact) interval, ½a; b, then each fnðxÞ is in fact uniformly continuous on ½a; b, and
the same will be true for f ðxÞ once it is shown to be continuous.
Proof
Let x0 A ½a; b and  > 0 be given. To prove that f ðxÞ is continuous at x0, we
show that there exists d so that j f ðxÞ  f ðx0Þj <  when jx  x0j < d. To this end, let
N be given as in the definition of uniform continuity to ensure that j fnðxÞ  f ðxÞj < 
3
for all x provided that n > N. For any such n, let d be the value associated with fnðxÞ
to ensure that j fnðxÞ  f ðx0Þj < 
3 for jx  x0j < d. We write
f ðxÞ  f ðx0Þ ¼ ½ f ðxÞ  fnðxÞ þ ½ fnðxÞ  fnðx0Þ þ ½ fnðx0Þ  f ðx0Þ;
and by the triangle inequality, for jx  x0j < d, we have
j f ðxÞ  f ðx0Þj a j f ðxÞ  fnðxÞj þ j fnðxÞ  fnðx0Þj þ j fnðx0Þ  f ðx0Þj
< 
3 þ 
3 þ 
3 ¼ :
n
Remark 9.53
The term ‘‘uniform’’ in the context of convergence is conceptually iden-
tical to the use of that term in the context of continuity.
1. For continuity, the general requirement is the existence of a d for every , but in gen-
eral, this d can depend on both  and the point x. What is required for uniform continu-
ity is that d may depend on  but not the point x.
2. For pointwise convergence, the general requirement is the existence of an N for
every , but again this N can depend on both  and the point x. What is required for
uniform convergence is that N may depend on  but not the point x.
The notion of ‘‘uniformity’’ in both contexts removes the dependency on x.
The property of uniform convergence can also be stated in terms of the
Cauchy criterion, as was the case for convergence of numerical sequences in chap-
ter 5.
Proposition 9.54
A function sequence fnðxÞ converges uniformly to a function f ðxÞ
on K H R if and only if for any  > 0 there is an integer N so that if n; m > N, then
j fnðxÞ  fmðxÞj <  for all x A K.
444
Chapter 9
Calculus I: Di¤erentiation

Proof
If fnðxÞ converges uniformly to f ðxÞ, then for  > 0 there is an integer N so
that j fnðxÞ  f ðxÞj < 
2 for all x provided that n > N. Now if n; m > N, we have by
the triangle inequality,
j fnðxÞ  fmðxÞj a j fnðxÞ  f ðxÞj þ j f ðxÞ  fmðxÞj
< ;
which is the Cauchy criterion. Conversely, given the Cauchy criterion, the numerical
sequence fnðxÞ is a Cauchy sequence by chapter 4 for every x, and hence it converges
to some number for every x, which we denote by f ðxÞ. Now given  > 0, the Cauchy
criterion states that for all x, j fnðxÞ  fmðxÞj <  if n; m > N. Letting m ! y, we
conclude that for all x, j fnðxÞ  f ðxÞj <  if n > N, and so fnðxÞ ! f ðxÞ uniformly.
n
*Series of Functions
An important corollary to proposition 9.51 above relates to series of functions,
Py
j¼1 gjðxÞ. First a definition.
Definition 9.55
Given a sequence of functions gjðxÞ defined on a common interval I,
and a function gðxÞ also defined on I, the function series Py
j¼1 gjðxÞ is said to converge
pointwise to gðxÞ if with fnðxÞ 1 Pn
j¼1 gjðxÞ for any  > 0 there is an integer
N ¼ NðxÞ so that j fnðxÞ  gðxÞj <  for n > NðxÞ. A function series Py
j¼1 gjðxÞ is
said to converge uniformly to gðxÞ on an interval J H I if for any  > 0 there is an
integer N, independent of x, so that for x A J: j fnðxÞ  gðxÞj <  for n > N. Pointwise
and uniform convergence of a series of functions on an arbitrary set K H R are defined
analogously.
There is an immediate application of proposition 9.51 to series of continuous func-
tions that converge uniformly.
Proposition 9.56
If gjðxÞ is a sequence of continuous functions defined on an interval
I, and Py
j¼1 gjðxÞ converges uniformly to a function gðxÞ, then gðxÞ is continuous on I.
Proof
Define the function sequence fnðxÞ 1 Pn
j¼1 gjðxÞ. Then each fnðxÞ is con-
tinuous on I, as a finite sum of continuous functions, and fnðxÞ ! gðxÞ uniformly
by assumption. Consequently the continuity of gðxÞ follows from proposition 9.51
above.
n
*Interchanging Limits
There is another important consequence to proposition 9.51 that is useful in practice
and relates to interchanging the order of limits. This is a manipulation that is always
9.2
Functions and Continuity
445

dangerous in mathematics and one that needs to be approached with caution. Specif-
ically, the question here is:
Question:
If fnðxÞ ! f ðxÞ for each x as n ! y, when is
lim
x!y lim
n!y fnðxÞ ¼ lim
n!y lim
x!y fnðxÞ?
Partial Answer:
The functions in (9.4) of example 9.49 show that pointwise conver-
gence fnðxÞ ! f ðxÞ is not enough to allow this interchange.
Example 9.57
With y ¼ 0 in example 9.49, we have that limn!y limx!0 fnðxÞ ¼ 1,
while limx!0 limn!y fnðxÞ ¼ limx!0 f ðxÞ is not even defined, since this limit is 0 if
approached from the right and 1 if approached from the left. In the notation introduced
in definition 9.17, limx!0þ f ðxÞ ¼ 0, and limx!0 f ðxÞ ¼ 1. So it appears that this ex-
ample fails because f ðxÞ is not continuous at y.
The a‰rmative result for interchanging limits is again provided by uniform con-
vergence. We provide a simple result first that is often adequate in practice, and a
more general result in proposition 9.59. In section 9.4 on convergence of a sequence
of derivatives we will return to this question. The simple result follows immediately
from the proposition above.
Proposition 9.58
If fnðxÞ is a sequence of continuous functions that converge uni-
formly to f ðxÞ on a closed and bounded (i.e., compact) interval ½a; b, then for any
y A ½a; b,
lim
x!y lim
n!y fnðxÞ ¼ lim
n!y lim
x!y fnðxÞ:
ð9:5Þ
Proof
This result is immediate from proposition 9.51 by the restatement of
(9.5) which is justified by the sequential convergence and continuity assumptions,
as:
lim
x!y f ðxÞ ¼ lim
n!y fnðyÞ:
Since f ðxÞ is continuous on ½a; b, limx!y f ðxÞ ¼ f ðyÞ. Also, since y A ½a; b, we have
limn!y fnðyÞ ¼ f ðyÞ.
n
Surprisingly, it turns out that the property of uniform convergence is so strong that
it allows the interchange of limits even when the point y is outside the interval of uni-
form convergence as long as it is a limit point of this interval, and limx!y fnðxÞ exists
for all n.
446
Chapter 9
Calculus I: Di¤erentiation

Proposition 9.59
Let fnðxÞ be a sequence of continuous functions that converge uni-
formly to f ðxÞ on an interval I, and let y A I, the closure of I. If limx!y fnðxÞ exists
for all n, then (9.5) holds.
Proof
Since this limit is assumed to exist, we define fnðyÞ 1 limx!y fnðxÞ. Of course,
if y A I, then this definition reproduces the original value of fnðyÞ by continuity but
otherwise extends the domain and range of fnðxÞ when y A I @ I. By the Cauchy cri-
terion for uniform convergence, we conclude that for any  > 0 there is an N so that
for all x A I,
j fnðxÞ  fmðxÞj < ;
n; m > N:
Also the assumption that limx!y fnðxÞ exists for all n justifies letting x ! y in this
inequality and yields that
j fnðyÞ  fmðyÞj a ;
n; m > N:
So fnðyÞ is a Cauchy numerical sequence as n ! y, and hence converges to a
number by chapter 5, which is labeled f ðyÞ. Note that by construction, f ðyÞ ¼
limn!y limx!y fnðxÞ. The goal is to now show that f ðyÞ ¼ limx!y limn!y fnðxÞ ¼
limx!y f ðxÞ. To do this, note that for x A I, by the triangle inequality,
j f ðxÞ  f ðyÞj a j f ðxÞ  fnðxÞj þ j fnðxÞ  fnðyÞj þ j fnðyÞ  f ðyÞj:
This summation can be made small for n large enough, since for  > 0 given above
and the various definitions of convergence:
1. fnðxÞ ! f ðxÞ uniformly for x A I, means there is an N1 so that j f ðxÞ  fnðxÞj < 
for all x for n > N1.
2. fnðyÞ ! f ðyÞ, means there is an N2 so that j fnðyÞ  f ðyÞj <  for n > N2.
3. fnðxÞ ! fnðyÞ for any n, means there is dn so that jx  yj < dn implies that
j fnðxÞ  fnðyÞj < .
Combining, we conclude that for N 0 ¼ maxðN1; N2Þ, and jx  yj < dN 0 that
j f ðxÞ  f ðyÞj < 3:
In other words, f ðyÞ ¼ limx!y f ðxÞ.
n
Remark 9.60
In the example of I ¼ ða; bÞ, the proposition 9.59 result states that if
limx!a fnðxÞ 1 fnðaÞ exists for all n, then uniform convergence on I gives more infor-
mation about what happens at a. This result assures that it must be the case that:
9.2
Functions and Continuity
447

1. limn!y fnðaÞ exists,
2. limx!a f ðxÞ exists, and
3. limn!y fnðaÞ ¼ limx!a f ðxÞ.
*9.2.8
Continuity and Topology
In addition to the interpretation that the continuity of a function implies metric
properties—that f ðxÞ can be made arbitrarily close to f ðx0Þ by choosing x close to
x0—continuity also has topological implications. That is, continuous functions have
predictable behaviors on open, closed, connected, and compact sets.
Remark 9.61
In the statement and proof below, recall that f 1ðAÞ, the pre-image of a
set A under f , is defined even if f is not one-to-one, which is to say, even when f 1 is
not defined as a function. Specifically, f 1ðAÞ ¼ fx j f ðxÞ A Ag.
Proposition 9.62
If f ðxÞ is a continuous function, f : R ! R, then:
1. f 1ðGÞ is open for every open set G H R
2. f 1ðF Þ is closed for every closed set F H R
3. f ðCÞ is connected for every connected set C H R
4. f ðKÞ is compact for every compact set K H R
Proof
1. Given G H R open, to show that f 1ðGÞ is open is to show that for any
x0 A f 1ðGÞ, there is an open ball about x0, Brðx0Þ, with Brðx0Þ H f 1ðGÞ. Now
since G is open, there is a ball about f ðx0Þ contained in G. That is, for some  > 0
we have Bðf ðx0ÞÞ H G. Given , by the continuity of f there is a d > 0 so that
jx  x0j < d implies that j f ðxÞ  f ðx0Þj < . That is, f ðBdðx0ÞÞ H Bðf ðx0ÞÞ. Conse-
quently Bdðx0Þ H f 1ðGÞ, and hence f 1ðGÞ is open.
2. Given F H R closed, the complement of F: ~F 1 R @ F, is open, so by 1, f 1ð ~FÞ
is also open. Consequently
g
f 1ð ~FÞ
f 1ð ~FÞ is closed. The final step is to show that
g
f 1ð ~FÞ
f 1ð ~FÞ ¼
f 1ðF Þ. The proof of the equivalent statement that f 1ð ~FÞ ¼
g
f 1ðFÞ
f 1ðFÞ, for an arbi-
trary set F, is left as exercise 31.
3. We argue by contradiction. Suppose that C H R is connected but that f ðCÞ is
not. Then there are open sets G1 and G2 so that f ðCÞ H G1 U G2 yet G1 V G2 ¼ j.
Now, by definition, C H f 1ðG1 U G2Þ, but also f 1ðG1 U G2Þ ¼ f 1ðG1Þ U f 1ðG2Þ
as is easily demonstrated. However, G1 V G2 ¼ j, implies that f 1ðG1Þ V f 1ðG2Þ ¼
j, and by part 1, both f 1ðG1Þ and f 1ðG2Þ are open, contradicting the assumption
that C is connected.
448
Chapter 9
Calculus I: Di¤erentiation

4. Assume that K H R is compact, and let fGag be an open cover of f ðKÞ. That is,
f ðKÞ H 6 Ga. We need to show that there is a finite subcollection fGjgn
j¼1 H fGag
so that f ðKÞ H 6n
j¼1 Gj. Now by part 1, ff 1ðGaÞg is an open cover of K, and since
K is compact, there is a finite subcover K H 6n
j¼1 f 1ðGjÞ. Hence f ðKÞ H 6n
j¼1 Gj,
demonstrating that f ðKÞ is compact.
n
Remark 9.63
Note that parts 1 and 2 in this proposition can be stated in terms of ‘‘if
and only if,’’ and not just as an implication. In other words, a function is continuous if
and only if f 1ðGÞ is open for every open set G, or equivalently f 1ðF Þ is closed for
every closed set F. For example, if f 1ðGÞ is open for every open set G, then for
f ðx0Þ A G there is an open ball Bðf ðx0ÞÞ H G, and by assumption, f 1ðBðf ðx0ÞÞÞ is
an open set that contains x0. So, by definition, there is an open ball Bdðx0Þ H
f 1ðBð f ðx0ÞÞÞ, which means that f ðBdðx0ÞÞ H Bðf ðx0ÞÞ, and these are the e and d
needed for the definition of continuity.
The importance of this observation is that it motivates the definition of continuous
function on, or between, general topological spaces.
Definition 9.64
If f : X ! Y is a function defined on a topological space X, and tak-
ing values in a topological space Y, then we define f to be continuous if f 1ðGÞ is open
in X for all G open in Y.
The proposition 9.62 result on preserving openness is explicitly related to the in-
verse of a continuous function, as it is not true in general that a continuous function
itself will preserve openness. As an example of G open but f ðGÞ closed:
Example 9.65
Consider the function: f ðxÞ ¼ x2ðx2  2Þ in figure 9.3. It is clear from
the graph that f ðGÞ need not be open when G is open. For instance, if G ¼ ða; aÞ for
any 1 < a a
ffiffi
2
p
, then f ðGÞ ¼ ½1; 0.
It is also the case that in general, F closed does not imply that f ðF Þ is closed.
However, from part 4 of the proposition above, such an example would have to be
one for which the set F is closed and unbounded. This is because if F is closed and
bounded it is compact by the Heine–Borel theorem, and hence so too is f ðF Þ by part
4. But in a metric space, compact means closed and bounded, and so f ðF Þ must then
also be closed and bounded.
Example 9.66
The classic example of F closed and unbounded and f ðF Þ not closed is
F ¼ fnp j n ¼ 0; 1; 2; 3; . . .g and the continuous function f ðxÞ ¼ ex cos x. Of course,
since the complement of F is the union of open intervals, F is clearly closed. However,
f ðF Þ is seen to equal fð1Þnenp j n ¼ 0; 1; 2; 3; . . .g, since cosðnpÞ ¼ ð1Þn. The set
f ðF Þ is not closed because a closed set must contain all of its limit points. However,
x ¼ 0, is apparently a limit point of this set but not an element of this set.
9.2
Functions and Continuity
449

Note that in each of these counterexamples the given function f ðxÞ was seen to be
a many-to-one function. This was necessary because, for one-to-one continuous func-
tions, all the statements of the proposition above generalize:
Proposition 9.67
If f ðxÞ is a continuous one-to-one function, f : R ! R, then:
1. f ðGÞ is open for every open set G H R.
2. f ðF Þ is closed for every closed set F H R.
3. f 1ðCÞ is connected for every connected set C H R.
4. f 1ðKÞ is compact for every compact set K H R.
Proof
The proof follows from the fact that because f ðxÞ is a continuous one-to-one
function, f 1ðxÞ is also continuous by proposition 9.26, and hence we can apply
proposition 9.62.
n
9.3
Derivatives and Taylor Series
9.3.1
Improving an Approximation I
In the preceding section various notions of continuity were reviewed and their prop-
erties discussed. To motivate the discussion of this section, we begin with an informal
attempt to improve upon the definition of continuity in terms of its implication for
Figure 9.3
f ðxÞ ¼ x2ðx2  2Þ
450
Chapter 9
Calculus I: Di¤erentiation

approximating a function’s values. Recall that if f ðxÞ is continuous at x0, then f ðxÞ
can be approximated by f ðx0Þ for x ‘‘near’’ x0. In the case of Ho¨lder continuity, we
can even determine the order of magnitude of this error as seen in (9.3).
Furthering this investigation, it is natural to inquire into the approximation of
f ðxÞ near x0, not simply by a constant f ðx0Þ but instead by a ‘‘linear’’ term that
varies proportionally with Dx ¼ x  x0:
f ðxÞA f ðx0Þ þ aDx;
where a is a constant.
To be e¤ective as an approximation tool, we require that the error in this approx-
imation goes to 0 as Dx ! 0. That is, at the minimum, we require that
f ðxÞ  ½ f ðx0Þ þ aDx ! 0
as Dx ! 0;
or equivalently
f ðxÞ  f ðx0Þ  aDx ¼ oð1Þ
as Dx ! 0:
Here we recall definition 9.44 that oð1Þ means that this expression converges to 0 as
Dx ! 0.
However, a moment of thought reveals the weakness in this idea. Namely, if f ðxÞ
is continuous at x0, the minimal requirement above is satisfied for any constant a, so
we have gained nothing with the addition of the extra term of aDx in the approxima-
tion. This approximation would be an improvement, however, if the error term could
somehow be changed from oð1Þ to oðDxÞ.
To this end, we rewrite:
f ðxÞ  f ðx0Þ  aDx 1
f ðxÞ  f ðx0Þ
Dx
 a


Dx:
In order for this expression to go to 0 in a way that supports better approximations,
and provides a method of determining the appropriate value of a, we require that
f ðxÞ  f ðx0Þ
Dx
 a ¼ oð1Þ
as Dx ! 0:
ð9:6Þ
Then, by recognizing the extra Dx term above and recalling that oð1ÞDx ¼ oðDxÞ,
we see that we can improve the approximation of f ðxÞ for x near x0 by the resulting
value of a, and that for this value
f ðxÞ  f ðx0Þ  aDx ¼ oðDxÞ:
ð9:7Þ
9.3
Derivatives and Taylor Series
451

In other words, if the limit in (9.6) exists, we can dramatically improve our ability
to approximate from the case of general continuity,
f ðxÞ  f ðx0Þ ! 0
as x ! x0;
with no information on speed of convergence, to (9.7). This tells us that the conver-
gence f ðxÞ ! f ðx0Þ is OðDxÞ, and once we account for the linear term aDx, we
achieve an approximation and convergence that is in fact oðDxÞ. This discussion
motivates the following development.
9.3.2
The First Derivative
We formalize in a definition the condition required in (9.6).
Definition 9.68
f ðxÞ is di¤erentiable at x0, or has a first derivative at x0, denoted
f 0ðx0Þ, or df
dx


x¼x0, if the following limit exists:
f 0ðx0Þ ¼ lim
Dx!0
f ðx0 þ DxÞ  f ðx0Þ
Dx
:
ð9:8Þ
Similarly f ðxÞ is di¤erentiable on an open interval ða; bÞ 1 fx j a < x < bg, or has a
first derivative everywhere on ða; bÞ, if the limit in (9.8) exists for all x0 A ða; bÞ.
Remark 9.69
1. The ratio
f ðx0þDxÞ f ðx0Þ
Dx
represents the slope of the secant line between the points
ðx0; f ðx0ÞÞ and ðx0 þ Dx; f ðx0 þ DxÞÞ, on the graph of y ¼ f ðxÞ. Consequently, as
Dx ! 0, the derivative can be interpreted as the slope of the tangent line to the graph
of y ¼ f ðxÞ at the point ðx0; f ðx0ÞÞ. The equation of this tangent line, which can be
used to approximate f ðxÞ for x near x0, is then
y ¼ f ðx0Þ þ f 0ðx0Þðx  x0Þ:
ð9:9Þ
2. One can introduce the notion of a one-sided derivative at the endpoints of a closed
interval ½a; b, by restricting the limit in (9.8) to limDx!0þ for f 0ðaÞ, or limDx!0 for
f 0ðbÞ. In general, however, most of our applications will relate to the standard two-
sided limit.
From the earlier discussion in section 9.3.1, it should be clear that there is an alter-
native way to define the notion that f ðxÞ is di¤erentiable at x0 that avoids the some-
times troublesome division by Dx and can be easier to apply in derivations to come.
Specifically:
452
Chapter 9
Calculus I: Di¤erentiation

Definition 9.70
f ðxÞ is di¤erentiable at x0 if there is number f 0ðx0Þ and an ‘‘error’’
function ef ðx0 þ DxÞ with ef ðx0 þ DxÞ ! 0 as Dx ! 0, and for which
f ðx0 þ DxÞ  f ðx0Þ ¼ Dxðf 0ðx0Þ þ ef ðx0 þ DxÞÞ:
ð9:10Þ
That this definition is equivalent to the former follows from the observation that
the limit in (9.8) means that for any given Dx 0 0, we have that
f ðx0þDxÞ f ðx0Þ
Dx
¼
f 0ðx0Þ þ error. This error term, denoted ef ðx0 þ DxÞ in (9.10), must converge to 0 as
Dx ! 0.
Example 9.71
1. If f ðxÞ ¼ c, a constant, then trivially, f 0ðxÞ ¼ 0. Not so obviously, but as was noted
in section 9.2.6, constant functions are the only continuous functions with this property.
2. One easily derives that for any positive integer n, f ðxÞ ¼ xn is di¤erentiable, and
dxn
dx


x¼x0
¼ nxn1
0
:
ð9:11Þ
This result is immediate for n ¼ 1 by the definition, while for n b 2 one derives this
from the binomial formula:
ðx þ DxÞn ¼ xn þ nxn1Dx þ OðDx2Þ:
3. The absolute value function f ðxÞ ¼ jxj is di¤erentiable for x 0 0. We obtain, by
definition,
f 0ðxÞ ¼
1;
x > 0,
1;
x < 0.

The absolute value function is not di¤erentiable at x ¼ 0 because the limit in (9.8) pro-
duces þ1 when Dx > 0, and 1 when Dx < 0.
From (9.8) we derive the following:
Proposition 9.72
If f ðxÞ is di¤erentiable at x0, then it is continuous there. Moreover
f ðxÞ is Lipschitz continuous at x0.
Proof
From (9.8), as Dx ! 0,
f ðx0 þ DxÞ  f ðx0Þ ¼ Dx f ðx0 þ DxÞ  f ðx0Þ
Dx
! 0  f 0ðx0Þ ¼ 0;
9.3
Derivatives and Taylor Series
453

so f ðxÞ is continuous. This derivation also shows that
f ðx0 þ DxÞ  f ðx0Þ ¼ OðDxÞ
as Dx ! 0;
so f ðxÞ is Lipschitz continuous.
n
Remark 9.73
The converse of this proposition is false because Lipschitz continuity
simply requires that with x 1 x0 þ Dx,
f ðxÞ  f ðx0Þ
Dx


a C
as Dx ! 0:
Lipschitz continuity does not require that this ratio converge to a limit. The simplest
example of this is the next:
Example 9.74
f ðxÞ ¼ jxj is Lipschitz continuous at x ¼ 0 but not di¤erentiable there,
since the left- and right-sided limits produced by (9.8) are 1 and þ1, respectively as
noted in example 9.71.
9.3.3
Calculating Derivatives
Demonstrating that complicated functions are di¤erentiable, and finding their deriv-
atives, can be di‰cult and tedious based on the definitions above. The following
three results provide a systematic approach to verifying di¤erentiability and deter-
mining derivatives of many common functions.
Proposition 9.75
If f ðxÞ and gðxÞ are di¤erentiable at x0, then so too is:
1. hðxÞ ¼ af ðxÞ G bgðxÞ, with h0ðx0Þ ¼ af 0ðx0Þ G bg0ðx0Þ
2. hðxÞ ¼ f ðxÞgðxÞ, with h0ðx0Þ ¼ f 0ðx0Þgðx0Þ þ f ðx0Þg0ðx0Þ
3. hðxÞ ¼
1
gðxÞ if gðx0Þ 0 0, with h0ðx0Þ ¼ g 0ðx0Þ
g2ðx0Þ
4. hðxÞ ¼ f ðxÞ
gðxÞ if gðx0Þ 0 0, with h0ðx0Þ ¼ f 0ðx0Þgðx0Þ f ðx0Þg 0ðx0Þ
g2ðx0Þ
Proof
See exercises 6 and 32. See also exercise 34 for a generalization of 2 known as
the Leibniz rule, which is reminiscent of the binomial theorem.
n
The next two results are more subtle, so we provide details of the proofs.
Proposition 9.76
If gðxÞ is di¤erentiable at x0 and f ðxÞ is di¤erentiable at gðx0Þ, then
so too is
5. hðxÞ ¼ f ðgðxÞÞ at x0, with h0ðx0Þ ¼ f 0ðgðx0ÞÞg0ðx0Þ
454
Chapter 9
Calculus I: Di¤erentiation

Proof
Note that if gðxÞ is di¤erentiable at x0 and f ðxÞ is di¤erentiable at y0 ¼
gðx0Þ, then from (9.10),
gðx0 þ DxÞ  gðx0Þ ¼ Dxðg0ðx0Þ þ egðx0 þ DxÞÞ;
f ðy0 þ DyÞ  f ðy0Þ ¼ Dyðf 0ðy0Þ þ ef ðy0 þ DyÞÞ:
Consequently, noting that y0 þ Dy ¼ gðx0 þ DxÞ, we write
hðx0 þ DxÞ  hðx0Þ ¼ f ðgðx0 þ DxÞÞ  f ðgðx0ÞÞ
¼ ½gðx0 þ DxÞ  gðx0Þ½ f 0ðgðx0ÞÞ þ ef ðgðx0 þ DxÞÞ
¼ Dx½g0ðx0Þ þ egðx0 þ DxÞ½f 0ðgðx0ÞÞ þ ef ðgðx0 þ DxÞÞ:
By definition that gðxÞ is di¤erentiable at x0, egðx0 þ DxÞ ! 0 as Dx ! 0. Also
ef ðy0 þ DyÞ ! 0 as Dy ! 0, but since Dy ¼ gðx0 þ DxÞ  gðx0Þ, we have by the con-
tinuity of gðxÞ that Dy ! 0 as Dx ! 0. Multiplying out the final expression, we de-
rive with a notational change
hðx0 þ DxÞ  hðx0Þ ¼ Dx½ f 0ðgðx0ÞÞg0ðx0Þ þ ehðx0 þ DxÞ;
where ehðx0 þ DxÞ ! 0 as Dx ! 0, with the error term given by
ehðx0 þ DxÞ ¼ g0ðx0Þef ðgðx0 þ DxÞÞ þ f 0ðgðx0ÞÞegðx0 þ DxÞ
þ egðx0 þ DxÞef ðgðx0 þ DxÞÞ:
Hence hðxÞ is di¤erentiable by (9.10).
n
Proposition 9.77
If gðxÞ is di¤erentiable at x0, g0ðx0Þ 0 0, and g0ðxÞ is continuous on
an interval about x0, then
6. hðyÞ ¼ g1ðyÞ is di¤erentiable at y0 ¼ gðx0Þ, with h0ðy0Þ ¼
1
g0ðx0Þ
Remark 9.78
Note that we do not explicitly assume that gðxÞ is one-to-one, or even
one-to-one ‘‘near’’ x0. While this result may appear odd, since we require the existence
of g1ðyÞ ‘‘near’’ y0 so that its derivative there is well defined, this requirement on gðxÞ
is assured by the assumption that g0ðx0Þ 0 0 and the continuity of g0ðxÞ (see exercise 7).
Proof
From (9.10), we need to show that if g0ðx0Þ 0 0,
g1ðy0 þ DyÞ  g1ðy0Þ ¼ Dy
1
g0ðx0Þ þ eg1ðy0 þ DyÞ


9.3
Derivatives and Taylor Series
455

for some error function with eg1ðy0 þ DyÞ ! 0 as Dy ! 0. Now, if g1ðy0Þ 1 x0,
and g1ðy0 þ DyÞ 1 x0 þ Dx, then Dy ¼ gðx0 þ DxÞ  gðx0Þ, and the equation above
is notationally equivalent to showing that
Dx ¼ ½gðx0 þ DxÞ  gðx0Þ
1
g0ðx0Þ þ eg1ðgðx0 þ DxÞÞ


:
This in turn is equivalent to
gðx0 þ DxÞ  gðx0Þ ¼
Dxg0ðx0Þ
1 þ g0ðx0Þeg1ðgðx0 þ DxÞÞ
¼ Dxðg0ðx0Þ þ ~eg1ðgðx0 þ DxÞÞÞ;
where with some algebra, we can derive
~eg1ðgðx0 þ DxÞÞ 1  ½g0ðx0Þ2eg1ðgðx0 þ DxÞÞ
1 þ g0ðx0Þeg1ðgðx0 þ DxÞÞ :
Now, by the di¤erentiability of gðxÞ at x0, we have that there is an egðx0 þ DxÞ so that
gðx0 þ DxÞ  gðx0Þ ¼ Dxðg0ðx0Þ þ egðx0 þ DxÞÞ:
Comparing expressions, we will be done if we can solve
egðx0 þ DxÞ ¼  ½g0ðx0Þ2eg1ðgðx0 þ DxÞÞ
1 þ g0ðx0Þeg1ðgðx0 þ DxÞÞ
for the needed error function, eg1ðgðx0 þ DxÞÞ, and demonstrate that it has the right
properties. A bit of algebra yields
eg1ðgðx0 þ DxÞÞ ¼
egðx0 þ DxÞ
½g0ðx0Þ2 þ g0ðx0Þegðx0 þ DxÞ
:
Finally, as Dy 1 gðx0 þ DxÞ  gðx0Þ ! 0, we can conclude that Dx ! 0 because
of the one-to-oneness assured by exercise 7. Hence as Dy ! 0, we have that
egðx0 þ DxÞ ! 0 and also eg1ðgðx0 þ DxÞÞ ¼ eg1ðy0 þ DyÞ ! 0, and the proof is
complete.
n
Remark 9.79
After the somewhat detailed proof of the derivative of the inverse func-
tion, here is a really easy proof—provided that hðyÞ ¼ g1ðyÞ is explicitly assumed to
456
Chapter 9
Calculus I: Di¤erentiation

be one-to-one near y0 and di¤erentiable at y0. Since the composition gðhðyÞÞ is the
simple function gðhðyÞÞ ¼ y, we can take the derivative of both sides using the compo-
sition formula in property 5 of proposition 9.76 above, evaluated at y0, to obtain
g0ðhðy0ÞÞh0ðy0Þ ¼ 1:
The conclusion follows with hðy0Þ ¼ x0. Now exercise 7 demonstrates that g1ðyÞ is
one-to-one near y0, but there is no easy way to demonstrate that g1ðyÞ is di¤erenti-
able at y0 without the added details of the proof above.
Example 9.80
Some examples of the wide applicability of these propositions are:
1. From (9.11) and property 1 above, one easily finds the derivative of any polynomial
function, while with property 4, one finds the derivative of any rational function, which
is a ratio of polynomials, at points for which the denominator polynomial is nonzero.
Similarly one finds the derivative of various composites of polynomial and rational
functions using property 5. In addition, 6 is useful in generalizing (9.11) from positive
integers to rationals of the form 1
m , since gðyÞ ¼ y1=m is inverse to f ðxÞ ¼ xm, which
with properties 5 and 3 can be further generalized to all rational number exponents
(positive or negative) of the form n
m . For these non-integer rational exponents, the
domains of the functions are restricted to x b 0 for positive exponents, and x > 0 for
negative exponents.
As a specific case,
If f ðxÞ ¼
X
n
i¼0
aixi; then f 0ðxÞ ¼
X
n
i¼1
iaixi1;
since the derivative of the constant a0 is zero. Similarly, with f ðxÞ as above, and
gðxÞ ¼ xq for q rational, define the function hðxÞ 1 gðf ðxÞÞ:
If hðxÞ 1
X
n
i¼0
aixi
"
#q
; then h0ðxÞ ¼ q
X
n
i¼0
aixi
"
#q1X
n
i¼1
iaixi1:
2. However, these formulas do not confirm di¤erentiability, nor provide the derivative
of the exponential functions f ðxÞ ¼ ax for a > 1. In exercise 8 it is noted that
dax
dx ¼ ax ln a;
a > 1;
ð9:12Þ
is a corollary of the formula for the natural exponential:
9.3
Derivatives and Taylor Series
457

dex
dx ¼ ex:
ð9:13Þ
For this latter formula it is easy to see that
f ðx þ DxÞ  f ðxÞ
Dx
¼ ax aDx  1
Dx
;
and the base of the ‘‘natural exponential,’’ e, can be defined as the real number that
satisfies
lim
Dx!0
eDx  1
Dx
¼ 1;
ð9:14Þ
from which (9.13) follows immediately. That there exists such a number e that satisfies
the limit in (9.14) is not apparent, but this numerical value can be expressed in an
equivalent way as in (9.19) below, and shown to exist by direct arguments (see case 7
below and the following section).
For a derivative example with f ðxÞ as in case 1, and gðxÞ ¼ ex, define the function
hðxÞ 1 gð f ðxÞÞ:
If hðxÞ ¼ eT n
i¼0 aix i; then h0ðxÞ ¼ ðeT n
i¼0 aix iÞ
X
n
i¼1
iaixi1:
3. The natural exponential provides a basis for extending (9.11) to any real number
exponent. That is, for any real number r, gðxÞ 1 xr can be defined by gðxÞ ¼ er ln x on
the domain x > 0. Applying (9.13) and property 5 in the proposition, we get g0ðxÞ ¼
r
x er ln x ¼ r
x xr ¼ rxr1. In other words,
If gðxÞ ¼ xr; x > 0; r A R; then g0ðxÞ ¼ rxr1:
ð9:15Þ
4. Let f ðxÞ ¼ eix, where i ¼
ffiffiffiffiffiffi
1
p
. We have from Euler’s formula in (2.5) that
eix ¼ cos x þ i sin x:
Now, if b A R and gðxÞ ¼ ebx ¼ ðebÞx, then from (9.12) we derive g0ðxÞ ¼ bebx. This
formula also turns out to be true for b A C, but we do not prove this since it is not es-
sential to this book’s goals. But this fact allows an easy derivation of the derivatives of
sin x and cos x. Namely
ieix ¼ deix
dx ¼ d cos x
dx
þ i d sin x
dx
;
458
Chapter 9
Calculus I: Di¤erentiation

but also
ieix ¼ sin x þ i cos x:
Comparing, we derive (with a bit of cheating that the derivative formula above is valid
for b A C):
d sin x
dx
¼ cos x;
d cos x
dx
¼ sin x:
ð9:16Þ
Remark 9.81
To make these ideas rigorous, we must first derive (9.16) directly from
the definition of f 0ðxÞ using trigonometric identities. These formulas imply each func-
tion is infinitely di¤erentiable (see definition 9.91). From the methods of Taylor series
used below, it turns out that ex, sin x, and cos x are each analytic and have convergent
series representations. The function eix, or generally eibx for b A R, can then be defined
in terms of the Taylor series expansion for ex by substitution, and shown to be abso-
lutely convergent. Moreover, if c A C, c ¼ a þ bi, then define ecx ¼ eaxeibx. Finally, the
associated Taylor series for eibx, sin bx and cos bx, can be shown to satisfy
eibx ¼ cos bx þ i sin bx;
which for b ¼ 1 is Euler’s formula.
5. Because f ðyÞ ¼ ln y, defined on y > 0, is the inverse function of gðxÞ ¼ ex defined
on R, we can apply property 6 in the proposition above to conclude that
d ln y
dy
¼ 1
y :
ð9:17Þ
Also, since loga y ¼
1
ln a ln y for a > 1, we obtain from property 1 of the proposition,
since
1
ln a is a constant,
d loga y
dy
¼
1
y ln a :
ð9:18Þ
6. With the formula for the derivative of ln x, we are now in the position to clarify a
couple of limits that were used in the chapter 7 development of the Poisson distribution.
Specifically, we need to show that for any real number l and constant k,
1  l
n þ k
n2

n
! el
as n ! y:
9.3
Derivatives and Taylor Series
459

Taking natural logarithms, this is equivalent to showing that
n ln 1  l
n þ k
n2


! l
as n ! y:
Consider the function f ðxÞ ¼ lnð1  lx þ kx2Þ, which is di¤erentiable for 1  lx þ
kx2 > 0, and this in turn is valid for any choice of constants for x close enough to 0.
In particular, f ðxÞ is di¤erentiable at x ¼ 0, and from the development above we have
that f 0ðxÞ ¼
lþ2kx
1lxþkx2 , and so f 0ð0Þ ¼ l. Applying the formula for the derivative
f 0ð0Þ, and observing that f ð0Þ ¼ 0, we have
l ¼ lim
Dx!0
f ðDxÞ
Dx
:
Finally, substituting Dx ¼ 1
n and letting n ! y completes the derivation.
7. A simple yet elegant corollary to case 6 is the following definition of e, obtained with
k ¼ 0 and l ¼ 1:
e ¼ lim
n!y 1 þ 1
n

n
;
ð9:19Þ
which also follows from (9.14) by setting Dx ¼ 1
n and letting n ! y.
Remark 9.82
Obviously, to avoid circular logic, one of cases 2, 5, 6, and 7 of example
9.80 must be independently derived, and the others then follow. The usual approach, as
noted above, is to first establish the limit in (9.19) directly by analysis of the sequence
an ¼ 1 þ 1
n

n (see the following section). From this the limit in (9.14) and di¤erenti-
ability of ex and ax follow, as then does the di¤erentiability of ln x and loga x, and then
finally the limits in case 6 above.
8. As noted above, f ðxÞ ¼ jxj is di¤erentiable everywhere except for x ¼ 0. However,
if p > 1, the function gðxÞ ¼ jxjp is di¤erentiable everywhere. This follows from noting
that since
gðxÞ ¼
xp;
x b 0,
ðxÞp;
x a 0,

we can apply (9.15) in example 9.80 to produce for x 0 0,
g0ðxÞ ¼
pxp1;
x > 0,
pðxÞp1;
x < 0.
(
460
Chapter 9
Calculus I: Di¤erentiation

For x ¼ 0,
gðDxÞ  gð0Þ
Dx
¼
ðDxÞp1;
Dx > 0;
jDxjp1;
Dx < 0;
(
and hence g0ð0Þ ¼ 0. Combining, we obtain the result:
If gðxÞ ¼ jxjp, p > 1, then
g0ðxÞ ¼
pjxjp1;
x b 0;
pjxjp1;
x a 0:
(
ð9:20Þ
A Discussion of e
The simplest approach to deriving the numerical value of e involves two steps:
Step 1. Define e by
e ¼
X
y
n¼0
1
n! :
That this summation converges follows directly from chapter 6 and the ratio test.
Since bn ¼ 1
n! , we see that as n ! y,
bnþ1
bn
¼
1
n þ 1 ! 0:
It is also apparent that 1
n! a
1
2 n1 for n b 1, so by evaluation of the geometric series,
e ¼ 1 þ
X
y
n¼1
1
n!
a 1 þ
X
y
n¼0
1
2n ¼ 3:
In fact
eA2:718281828459 . . . :
ð9:21Þ
Step 2. Define an ¼ 1 þ 1
n

n as in (9.19) of case 7 of example 9.80 above. We now
show that an ! e. By the binomial theorem,
9.3
Derivatives and Taylor Series
461

an ¼
X
n
j¼0
n
j

 1
n j
¼ 1 þ
X
n
j¼1
Y
j1
k¼0
1  k
n


"
#
1
j! :
From this result we conclude that since Q j1
k¼0 1  k
n


a 1,
an a en < e;
where en ¼ Pn
j¼0
1
j! is the partial sum that converges to e above. It is also apparent
that
an < anþ1;
since anþ1 has one more positive term in the summation above, and for the other
terms, the coe‰cients of
1
j!
n on
j¼1 increase from Q j1
k¼0 1  k
n


to Q j1
k¼0 1 
k
nþ1

	
. Be-
cause an is an increasing sequence and is bounded above by e, this sequence con-
verges by chapter 5 to a say, where a a e. To see that a ¼ e, note that for m > n,
am ¼ 1 þ
X
m
j¼1
Y
j1
k¼0
1  k
m


"
#
1
j!
> 1 þ
X
n
j¼1
Y
j1
k¼0
1  k
m


"
#
1
j! :
Letting m ! y, we conclude that since am ! a and Q j1
k¼0 1  k
m


! 1,
a b en:
Combining, we have
an a en a a;
and hence an ! e as desired.
9.3.4
Properties of Derivatives
One important and well-known result for di¤erentiable functions is the following
mean value theorem, which often goes under the moniker of the MVT. Graphically,
recalling (9.9), the MVT states that if f ðxÞ satisfies the given properties on ½a; b, then
462
Chapter 9
Calculus I: Di¤erentiation

there is a point c A ða; bÞ so that the slope of the tangent line to y ¼ f ðxÞ at c, or
f 0ðcÞ, equals the slope between the endpoints of the graph of f ðxÞ on ½a; b. The end-
points are, of course, ða; f ðaÞÞ and ðb; f ðbÞÞ.
Proposition 9.83 (Mean Value Theorem)
If f ðxÞ is di¤erentiable on ða; bÞ and contin-
uous on ½a; b, then there is a number c A ða; bÞ, so that
f 0ðcÞ ¼ f ðbÞ  f ðaÞ
b  a
:
ð9:22Þ
Proof
Define a new function
gðxÞ ¼ f ðxÞ  f ðbÞ  f ðaÞ
b  a
ðx  aÞ:
Then gðaÞ ¼ gðbÞ ¼ f ðaÞ, and g0ðxÞ ¼ f 0ðxÞ  f ðbÞ f ðaÞ
ba
, so the proof follows if we
can show that there is a c A ða; bÞ with g0ðcÞ ¼ 0. The next proposition provides this
conclusion.
n
Proposition 9.84 (Rolle’s Theorem)
If gðxÞ is di¤erentiable on ða; bÞ and continuous
on ½a; b, with gðaÞ ¼ gðbÞ, then there is a number c A ða; bÞ, so that g0ðcÞ ¼ 0.
Proof
If gðxÞ is constant on ½a; b, then the conclusion follows for all c A ða; bÞ. If
not constant, then as a continuous function on ½a; b, gðxÞ must achieve both its max-
imum and minimum value on this interval. Since gðxÞ is assumed to be nonconstant
and gðaÞ ¼ gðbÞ, at least one of these must occur within ða; bÞ, and we denote this
value by c. Now, if gðcÞ is a maximum, we conclude that
gðxÞ  gðcÞ
x  c
a 0;
x b c;
b 0;
x a c;

and with the opposite inequalities at a minimum. Since the limit must exist as x ! c,
and equal g0ðcÞ, we conclude that the only possible value for this limit is 0.
n
Remark 9.85
1. With the aid of the mean value theorem, we return to the point made in section 9.2.6
on Ho¨lder continuity, that being, if f ðxÞ is Ho¨lder continuous of order a > 1 on an
interval ða; bÞ, then f ðxÞ ¼ c, a constant on this interval. To see this, first note that if
f ðxÞ has this order of continuity at x0, then
f ðxÞ  f ðx0Þ
Dx


 ¼ OðDxa1Þ;
9.3
Derivatives and Taylor Series
463

and hence f 0ðx0Þ ¼ 0. Consequently, if f ðxÞ has this order of continuity throughout an
interval ða; bÞ, then f 0ðxÞ ¼ 0 for all x A ða; bÞ. By the MVT, for any interval ½c; d H
ða; bÞ there is e A ½c; d with
f ðdÞ f ðcÞ
dc
¼ f 0ðeÞ, and we conclude from f 0ðeÞ ¼ 0 that
f ðdÞ ¼ f ðcÞ, so f ðxÞ is constant. Of course, there is no such conclusion if f ðxÞ satisfies
this Ho¨lder condition at an isolated point, as the functions f ðxÞ ¼ xa for a > 1 demon-
strate at x ¼ 0.
2. Another consequence of (9.22) noted in item 1 is that if f 0ðxÞ 1 0 on an interval
ða; bÞ, then for any c; d A ða; bÞ, we must have that f ðcÞ ¼ f ðdÞ. In other words, the
only functions with identically 0 first derivatives are the constant functions.
The proof of Rolle’s theorem produces a necessary condition on a point c A ða; bÞ
to be a relative maximum or a relative minimum of f ðxÞ on ½a; b, but first a
definition.
Definition 9.86
A point c is a relative minimum of a function f ðxÞ if there is an
open interval I, with c A I, so that for all x A I, f ðcÞ a f ðxÞ. The point c is a relative
maximum of f ðxÞ if there is an open interval I containing c so that for all x A I,
f ðcÞ b f ðxÞ.
When f ðxÞ is a di¤erentiable function, it is often easy to find all possible candi-
dates for relative minimums and relative maximums. Specifically, at any such point,
f 0ðcÞ ¼ 0.
Proposition 9.87
If c is a relative maximum or relative minimum of f ðxÞ, and f ðxÞ is
di¤erentiable at c, then f 0ðcÞ ¼ 0.
Proof
As in the proof of Rolle’s theorem, at a relative minimum,
f ðxÞ  f ðcÞ
x  c
b 0;
x b c;
a 0;
x a c;

and the inequalities reverse at a relative maximum. As x ! c, the existence of f 0ðcÞ
implies that these ratios converge to the same value, which must therefore be 0.
n
Example 9.88
1. Note that a di¤erentiable function does not necessarily have f 0ðxÞ ¼ 0 at a global
maximum or global minimum on ½a; b, since such extreme values may occur at an in-
terval endpoint. For example, f ðxÞ ¼ x is a simple function that achieves its global
maximum and minimum on the endpoints of every closed interval ½a; b, and yet
f 0ðxÞ 1 1.
464
Chapter 9
Calculus I: Di¤erentiation

2. Also f 0ðcÞ ¼ 0 is only a necessary condition for a relative maximum or minimum; it
is not su‰cient as the function f ðxÞ ¼ x3 exemplifies at c ¼ 0.
Because of the importance of the points at which the derivative of a function is
zero, these points warrant a special name.
Definition 9.89
Given a di¤erentiable function f ðxÞ, the points for which f 0ðcÞ ¼ 0
are known as the critical points of f ðxÞ.
Critical points are the first place one looks to find relative maximums or mini-
mums of a di¤erentiable function. Because such an analysis will only reveal a func-
tion’s relative maximums and minimums, for global maximums and minimums on a
closed and bounded interval, the second place to be evaluated are the interval’s end-
points. For global maximums and minimums on an open interval, ða; bÞ, bounded or
unbounded, one needs to consider the function’s values as x ! a and x ! b, and in
such cases the function may be unbounded, meaning the global maximum (respec-
tively, minimum) is y (respectively, y).
A final simple property, but a useful one to highlight, was noted in the proof of the
derivative formula for the inverse function in proposition 9.77. Its proof is assigned
as exercise 7, and will be omitted.
Proposition 9.90
If f ðxÞ is di¤erentiable at x0, f 0ðx0Þ 0 0, and f 0ðxÞ is continuous in
an open interval containing x0 then there is an open interval about x0, say I ¼ ðx0  a;
x0 þ aÞ for some a > 0, so that on I, f ðxÞ is one-to-one and monotonic. Specifically, if
x; y A I and x < y, then
f 0ðx0Þ > 0 ) f ðxÞ < f ðyÞ;
f 0ðx0Þ < 0 ) f ðxÞ > f ðyÞ:
9.3.5
Improving an Approximation II
Another significant conclusion that can be drawn from the mean value theorem is
a numerical refinement of the rate of convergence of f ðxÞ to f ðx0Þ in the case where
f ðxÞ has a bounded derivative. Specifically, if M ¼ maxff 0ðxÞ j x A ða; bÞg, then for
any x; x0 A ða; bÞ, we have from (9.10) and the triangle inequality that
j f ðxÞ  f ðx0Þj a Mjx  x0j:
ð9:23Þ
While this bound is in theory less powerful than (9.7), which we rewrite here for
comparability,
9.3
Derivatives and Taylor Series
465

j f ðxÞ  f ðx0Þj a f 0ðx0Þjx  x0j þ oðjx  x0jÞ;
in practice, it can be more valuable when M is easily estimated, since this inequality
works uniformly for any x and x0 in the interval, rather than only at a point, x0. This
estimate also avoids the extra Little o term that, while useful when we have Dx ! 0,
is not useful for numerical estimates when Dx is fixed and finite, since its exact for-
mula is unknown.
Also note that by rewriting (9.7) with a ¼ f 0ðx0Þ, we achieve the following
approximation:
f ðxÞ ¼ f ðx0Þ þ f 0ðx0ÞDx þ oðDxÞ;
ð9:24Þ
where as usual, x ¼ x0 þ Dx. We will see below that this is a special case of a Taylor
series expansion of f ðxÞ.
Comparing (9.24) with (9.9), we identify the error between the tangent line approxi-
mation and the graph of the function to be oðDxÞ.
9.3.6
Higher Order Derivatives
In order to pursue higher order approximations to f ðxÞ near x0, we define the fol-
lowing notion:
Definition 9.91
For each integer n > 1, the nth derivative of f ðxÞ at x0, denoted
f ðnÞðx0Þ, or, d nf
dxn


x¼x0, is defined iteratively by
f ðnÞðx0Þ 1 lim
Dx!0
f ðn1ÞðxÞ  f ðn1Þðx0Þ
Dx
;
ð9:25Þ
when this limit exists. One then says that f ðxÞ is n-times di¤erentiable at x0, or on an
interval ða; bÞ, and so forth. If f ðnÞðx0Þ exists for all n, we say that f ðxÞ is infinitely
di¤erentiable at x0, or infinitely di¤erentiable on an interval, and so forth. The exis-
tence of the nth derivative of f ðxÞ can also be expressed in a way that is analogous to
(9.10):
f ðn1Þðx0 þ DxÞ  f ðn1Þðx0Þ ¼ Dxðf ðnÞðx0Þ þ ef ðn1Þðx0 þ DxÞÞ:
Note that if f ðxÞ is n-times di¤erentiable at x0, then by proposition 9.72 each of
the first ðn  1Þ derivatives must be continuous at x0. Also note above that a func-
tion’s nth derivative is calculated sequentially, by calculating in turn the function’s
derivatives, first, then second, and so on. Below we investigate numerical estimation
of derivatives that are developed directly from values of the function.
466
Chapter 9
Calculus I: Di¤erentiation

Example 9.92
Let f ðxÞ ¼ xN, where N is a positive integer. Then as was shown in
example 9.71 above, f 0ðxÞ ¼ NxN1. By iteration, we derive that
dxN
dxn ¼
N!
ðNnÞ! xNn;
n a N;
0;
n > N;
(
where we recall below the factorial notation and related binomial coe‰cients.
Definition 9.93
1. If N is a positive integer, then N!, or N factorial is defined as
N! ¼ NðN  1ÞðN  2Þ . . . 2  1;
and also 0! ¼ 1 (see chapter 10, the gamma distribution, for a compelling motivation
for the definition of 0!).
2. If N and M are nonnegative integers, 0 a M a N, the binomial coe‰cient,
N
M
 
is
defined as
N
M


¼
N!
M!ðN  MÞ! :
9.3.7
Improving an Approximation III: Taylor Series Approximations
Generalizing the analysis above that led to (9.24), we introduce next the general Tay-
lor series. To this end, assume that we want to approximate f ðxÞ with an nth order
polynomial, generalizing the first order approximation in (9.24). In other words, the
goal is to approximate f ðxÞ by
f ðxÞA
X
n
j¼0
ajðx  x0Þ j;
where here we express Dx as x  x0 for specificity below.
If we assume that f ðxÞ is n-times di¤erentiable, we can di¤erentiate this expression
using example 9.92 above, and substitute x ¼ x0 to solve for the coe‰cients aj. For
example,
f ðx0Þ ¼
X
n
j¼0
ajðx0  x0Þ j ¼ a0;
f 0ðx0Þ ¼
X
n
j¼1
jajðx0  x0Þ j1 ¼ a1;
9.3
Derivatives and Taylor Series
467

f ð2Þðx0Þ ¼
X
n
j¼2
jðj  1Þajðx0  x0Þ j2 ¼ 2a2;
..
.
f ðmÞðx0Þ ¼
X
n
j¼m
j!
ðj  mÞ! ajðx0  x0Þ jm ¼ m!am
for m a n:
From this calculation we derive the nth-order Taylor polynomial for f ðxÞ centered
at x0:
f ðxÞA
X
n
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j:
ð9:26Þ
This expansion is named for Brook Taylor (1685–1731) who published the approxi-
mation result in (9.26) in the early 1700s, although it was apparently discovered some
time earlier by James Gregory (1638–1675). When x0 ¼ 0, this series approximation
is sometimes referred to as a Maclaurin series, named for Colin Maclaurin (1698–
1746), who applied this idea to trigonometric functions.
As a first application we derive the nth-order Taylor polynomial for ex, first refer-
enced in chapter 6 and applied in chapter 7.
Example 9.94
With f ðxÞ ¼ ex, and x0 ¼ 0, we have that f ðnÞðx0Þ ¼ ex0 ¼ 1 for all n,
and so
ex A
X
n
j¼0
1
j! x j:
We next investigate the error in the approximation in (9.26). Of course, if f ðxÞ is a
polynomial of degree n, the nth-order Taylor polynomial will exactly reproduce f ðxÞ.
In fact from (9.26) it is apparent that for any such polynomial, the coe‰cient of x j
equals the jth-derivative of the polynomial divided by j!, where these derivatives are
evaluated at x ¼ 0. In general, however, there will be a remainder, also called the
error term.
We now investigate one property of this remainder.
Proposition 9.95
If f ðxÞ is n-times di¤erentiable on an interval ða; bÞ, with f ð jÞðxÞ
continuous on ½a; b for j a n  1, then for x; x0 A ½a; b,
468
Chapter 9
Calculus I: Di¤erentiation

f ðxÞ ¼
X
n
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j þ OðDxnÞ;
ð9:27Þ
where Dx ¼ x  x0. In addition, if f ðnÞðxÞ is continuous on ½a; b, then the error
improves slightly to
f ðxÞ ¼
X
n
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j þ oðDxnÞ:
ð9:28Þ
Proof
For x; x0 A ½a; b given, with x0 < x for specificity, define the constant A 1
Aðx; x0Þ, so that
f ðxÞ ¼
X
n1
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j þ A ðx  x0Þn
n!
;
and define the residual function
gðyÞ ¼ f ðxÞ 
X
n1
j¼0
1
j! f ð jÞðyÞðx  yÞ j  A ðx  yÞn
n!
:
Now by the assumptions of the proposition, gðyÞ is continuous on ½a; b and di¤eren-
tiable on ða; bÞ. Also gðxÞ ¼ gðx0Þ ¼ 0. So by Rolle’s theorem, there is a value c A
ðx0; xÞ so that g0ðcÞ ¼ 0. A calculation, using the product rule for derivatives, pro-
duces g0ðyÞ:
g0ðyÞ ¼ 
X
n1
j¼0
1
j! f ð jþ1ÞðyÞðx  yÞ j þ
X
n1
j¼1
1
ðj  1Þ! f ð jÞðyÞðx  yÞ j1
þ A ðx  yÞn1
ðn  1Þ! :
A careful look at the two summations reveals that the first n  1 terms of the first
sum cancel with the n  1 terms of the second, leaving
g0ðyÞ ¼ 
1
ðn  1Þ! f ðnÞðyÞðx  yÞn1 þ A ðx  yÞn1
ðn  1Þ! :
The conclusion of Rolle’s theorem, that there is a c A ðx0; xÞ so that g0ðcÞ ¼ 0, can be
rewritten as
9.3
Derivatives and Taylor Series
469

f ðnÞðcÞ ¼ A:
Hence we have that for some c A ðx0; xÞ,
f ðxÞ ¼
X
n1
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j þ f ðnÞðcÞ ðx  x0Þn
n!
:
ð9:29Þ
The same conclusion follows if x0 > x. From (9.29) we have then that for some
c A ðx0; xÞ or c A ðx; x0Þ,
f ðxÞ ¼
X
n
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j þ ½ f ðnÞðcÞ  f ðnÞðx0Þ ðx  x0Þn
n!
:
The error term is seen to be OðDxnÞ if we only know that f ðnÞðxÞ exists. However, if
f ðnÞðxÞ is also continuous so that f ðnÞðcÞ  f ðnÞðx0Þ ! 0 as Dx ! 0, then this error is
seen to be oðDxnÞ.
n
Notation 9.96
Given x; x0 A ða; bÞ, there is a convenient notational devise for identify-
ing a point c that is ‘‘between’’ x and x0, which is to say that c A ðx0; xÞ if x0 < x, and
c A ðx; x0Þ if x < x0. Stated more succinctly, there exists y, with 0 < y < 1, so that
c ¼ x0 þ yDx, where Dx ¼ x  x0, and this is used below.
Example 9.97
From example 9.94, we have that since ex is infinitely di¤erentiable,
and hence has continuous derivatives of all orders, then for any n,
ex 
X
n
j¼0
1
j! x j ¼ oðxnÞ
as x ! 0:
Analytic Functions
It turns out that in many applications, the Taylor polynomials not only provide high-
order approximations to the given function at x0 as Dx ! 0, but also these polyno-
mials approximate the function everywhere as n ! y. Such functions are called
analytic functions.
Definition 9.98
A function f ðxÞ is called analytic in a neighborhood of x0 if it can be
expanded in a convergent Taylor series:
f ðxÞ ¼
X
y
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j;
ð9:30Þ
for x in an open interval centered on x0. In other words, for every x in this interval,
470
Chapter 9
Calculus I: Di¤erentiation

f ðxÞ ¼ lim
n!y
X
n
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j:
It is apparent that every polynomial is analytic, since all but a finite number of
derivatives satisfy f ð jÞðx0Þ ¼ 0, as are many familiar functions such as ex, ln x,
sin x, and cos x. Each is analytic everywhere in their respective domains of defini-
tion. Proving analyticity, however, requires some new tools, as developed in (9.34)
below. The formula (9.27) does not help, even if we know that f ðxÞ is infinitely dif-
ferentiable and this formula holds for all n. The reason is that this expression only
provides information about the behavior of the Taylor polynomial as Dx ! 0. To
be analytic at x0 requires that fnðxÞ ! f ðxÞ as n ! y for x in a neighborhood of
x0, where fnðxÞ denotes the nth-degree Taylor polynomial in (9.26).
While analyticity requires the existence of infinitely many derivatives, the follow-
ing classical example demonstrates that it requires more than just this. In other
words, infinite di¤erentiability is a necessary condition for a function to be analytic,
but it is not a su‰cient condition.
Example 9.99
Define f ðxÞ by
f ðxÞ ¼
e1=x2;
x 0 0;
0;
x ¼ 0:
(
Then every derivative of f ðxÞ is a finite sum of terms of the form
c e1=x2
x j
:
So f ðnÞðxÞ exists for all x 0 0, but also it is possible to justify that for all n, f ðnÞðxÞ ! 0
as x ! 0. To see this, substitute y ¼ 1
x , obtaining sums of terms of the form cy jey2,
and let y ! y. Then, as y ! y, since y j < ey for any j, we conclude that
cy jey2 < ceyðy1Þ ! 0
as y ! y:
In other words, f ðnÞð0Þ ¼ 0 for all n, and hence the Taylor polynomials evaluated at
x0 ¼ 0 satisfy fnðxÞ 1 0 for all n. Consequently we cannot have that fnðxÞ ! f ðxÞ as
n ! y for x in a neighborhood of 0, and we conclude that f ðxÞ is infinitely di¤erentia-
ble but not analytic at 0.
Note that the definition of analytic above does not require that the Taylor
series converge absolutely, only that it converges. This is in contrast to the definition
of a power series in chapter 6 for which the interval of convergence and radius of
9.3
Derivatives and Taylor Series
471

convergence are defined in a way to ensure that these series converge absolutely.
However, many analytic functions do indeed converge absolutely, and using chapter
6 methods, we can readily identify two conditions that assure absolute convergence.
Both conditions relate to the growth of f f ðnÞðx0Þg as n ! y.
Proposition 9.100
Let f ðxÞ be an analytic function given by (9.30) in the interval
jx  x0j < R.
1. If
lim sup
n
f ðnþ1Þðx0Þ
ðn þ 1Þ f ðnÞðx0Þ


 ¼ L < y;
ð9:31Þ
then the Taylor series is absolutely convergent for jx  x0j < R0, where R0 ¼ 1
L .
2. If there is an x0 so that
f ðnÞðx0Þ
n!
ðx0  x0Þn


a C
for all n;
ð9:32Þ
then the Taylor series is absolutely convergent for jx  x0j < R00, where R00 ¼
jx0  x0j.
Proof
Statement 1 follows from the ratio test in chapter 6, which assures absolute
convergence if the limit superior of the ratios of successive terms is less than 1. Let-
ting cn 1 f ðnÞðx0Þ
n!
ðx  x0Þn, we write
lim sup
n
cnþ1
cn


 ¼ lim sup
n
f ðnþ1Þðx0Þ
ðn þ 1Þf ðnÞðx0Þ


 jx  x0j;
¼ Ljx  x0j;
so absolute convergence is assured if Ljx  x0j < 1. Statement 2 follows from the
comparison test. Specifically, (9.32) implies that
f ðnÞðx0Þ
n!
ðx  x0Þn


a C x  x0
x0  x0


n
< Crn;
where r < 1 if jx  x0j < jx0  x0j, and this Taylor series is therefore bounded by a
convergent geometric series.
n
472
Chapter 9
Calculus I: Di¤erentiation

A useful corollary of this result is as follows:
Proposition 9.101
If
f ðxÞ ¼
X
y
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j;
gðxÞ ¼
X
y
j¼0
1
j! gð jÞðx0Þðx  x0Þ j;
are analytic functions that are absolutely convergent for jx  x0j < R, then for any
a; b A R, hðxÞ 1 af ðxÞ þ bgðxÞ is analytic, absolutely convergent for jx  x0j < R, and
hðxÞ ¼ Py
j¼0
1
j! hð jÞðx0Þðx  x0Þ j.
Proof
That hðxÞ is absolutely convergent follows from the triangle inequality and
the absolute convergence of f ðxÞ and gðxÞ:
a
X
y
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j þ b
X
y
j¼0
1
j! gð jÞðx0Þðx  x0Þ j


a jaj
X
y
j¼0
1
j! j f ð jÞðx0Þðx  x0Þ jj þ jbj
X
y
j¼0
1
j! jgð jÞðx0Þðx  x0Þ jj:
That the Taylor series for hðxÞ is given in terms of the derivatives of hðxÞ also follows
by the absolute convergence of the series
a
X
y
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j þ b
X
y
j¼0
1
j! gð jÞðx0Þðx  x0Þ j;
which justifies the rearrangement of these terms to
X
y
j¼0
1
j! ½af ð jÞðx0Þ þ bgð jÞðx0Þðx  x0Þ j.
n
Remark 9.102
While the Taylor series of an analytic function need not be absolutely
convergent, the partial sums of these series are pointwise convergent. Hence these
partial sums will be uniformly convergent on any compact set inside the interval of
convergence.
9.3.8
Taylor Series Remainder
In this section we present a useful and explicit expression for the remainder term im-
plicit in (9.26) and seen in the development of (9.27) and (9.28). Another expression
for this remainder will be seen in section 10.8.
9.3
Derivatives and Taylor Series
473

Defining fnðxÞ as the nth-order Taylor polynomial in (9.26), we write
fnðxÞ ¼
X
n
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j:
Proposition 9.95 provides qualitative information on the error term:
f ðxÞ ¼ fnðxÞ þ RnðxÞ:
Summarizing, we have from (9.27) and (9.28) that:
1. RnðxÞ ¼ OðDxnÞ in all cases, requiring only that f ðnÞðxÞ exists on ða; bÞ.
2. RnðxÞ ¼ oðDxnÞ if f ðnÞðxÞ is also continuous on this interval.
Now, what if f ðnÞðxÞ is also di¤erentiable on this interval? Then proposition
9.95 states that f ðxÞ can be approximated by fnþ1ðxÞ with an error of Rnþ1ðxÞ ¼
OðDxnþ1Þ. Alternatively, the last term in fnþ1ðxÞ can be moved to the error term so
that f ðxÞ can be approximated by fnðxÞ, with an error of
R0
nðxÞ ¼ Rnþ1ðxÞ þ
1
ðn þ 1Þ! f ðnþ1Þðx0Þðx  x0Þnþ1 ¼ OðDxnþ1Þ:
However, it turns out that in this case where we assume that f ðxÞ has one addi-
tional derivative f ðnþ1ÞðxÞ, an explicit expression for this remainder can also be
derived. If this additional derivative is continuous, this explicit expression provides
a useful upper bound for this error everywhere in the given interval. This remainder
is often used for proving convergence of a Taylor series, as well as providing nu-
merical estimates for given x0 and Dx, while the upper bound is used for proving
analyticity on a given interval.
Proposition 9.103
If f ðxÞ is ðn þ 1Þ-times di¤erentiable on an interval ða; bÞ, with
f ð jÞðxÞ continuous on ½a; b for j a n, and x; x0 A ða; bÞ, then there exists y, with
0 < y < 1, so that
f ðxÞ ¼
X
n
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j þ
1
ðn þ 1Þ! f ðnþ1ÞðcÞðx  x0Þnþ1;
ð9:33Þ
where c ¼ x0 þ yDx. In other words, c is between x and x0, and so c A ðx0, xÞ if x0 < x,
and c A ðx; x0Þ if x < x0. In addition, if f ðnþ1ÞðxÞ is continuous on ½a; b, then there
exists M > 0 so that for all x; x0 A ða; bÞ,
474
Chapter 9
Calculus I: Di¤erentiation

f ðxÞ 
X
n
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j


a
M
ðn þ 1Þ! jx  x0jnþ1:
ð9:34Þ
Proof
The expression in (9.33) follows immediately from (9.29) in the proof of
proposition 9.95. In addition, if f ðnþ1ÞðxÞ is continuous on ½a; b, then from proposi-
tion 9.39 this function attains its upper and lower bounds in this interval. Here M
denotes the larger of the absolute values of these bounds.
n
Remark 9.104
The remainder term in the Taylor series expansion in (9.33) is known
as the Lagrange form of the remainder, after Joseph-Louis Lagrange (1736–1813),
who proved the mean value theorem and derived this remainder term from this result.
Another form of this remainder, named for Augustin Louis Cauchy, will be developed
in section 10.8.
Example 9.105
1. We can apply this proposition to the infinite product encountered in section 8.4.1, in
the discussion preceding the strong law of large numbers. Given fxngy
n¼1 with xn > 0
and xn ! 0 as n ! y, we show that
Y
y
n¼1
ð1  xnÞ ¼
0;
if P xn diverges;
c > 0;
if P xn converges:

Applying (9.33) with n ¼ 1 to f ðxÞ ¼ lnð1  xÞ, and recalling that f 0ðxÞ ¼ 1
1x and
f 00ðxÞ ¼
1
ð1xÞ2 , we obtain the following with x0 ¼ 0, where it is also assumed that
xn < 1:
lnð1  xnÞ ¼ xn  1
2 ðynxnÞ2;
0 < yn < 1:
Consequently, since all but a finite number of xn satisfy xn < 1, we can ignore these
exceptions since they do not influence the conclusion, and obtain
ln
Y
N
n¼1
ð1  xnÞ ¼ 
X
N
n¼1
xn  1
2
X
N
n¼1
ðynxnÞ2:
Now, if Py
n¼1 xn ¼ y, then we have that ln Qy
n¼1ð1  xnÞ ¼ y, and hence
Qy
n¼1ð1  xnÞ ¼ 0. On the other hand, if Py
n¼1 xn ¼ s < y, then since yn; xn < 1,
it is apparent that Py
n¼1ðynxnÞ2 ¼ s0 < s. So ln Qy
n¼1ð1  xnÞ ¼ s  1
2 s0, and
Qy
n¼1ð1  xnÞ ¼ esðs 0=2Þ.
9.3
Derivatives and Taylor Series
475

2. If fxngy
n¼1 satisfies xn ! 0 as n ! y without the restriction xn > 0, the same sec-
ond convergence conclusion follows provided that P jxnj converges. This condition
assures that Py
n¼1ðynxnÞ2 converges, since for jxnj < 1,
X
y
n¼1
ðynxnÞ2 <
X
y
n¼1
x2
n <
X
jxnj:
Note that xn ¼ ð1Þnffiffin
p
demonstrates the necessity of this condition of absolute conver-
gence, since although Py
n¼1 xn ¼ s < y, all that can be said about this second summa-
tion is that Py
n¼1ðynxnÞ2 < Py
n¼1
1
n , which is divergent.
The upper bound for the remainder term is often useful in proving analyticity of a
given function. However, we will see that this estimate sometimes fails to provide a
proof of convergence of a Taylor series because it is somewhat crude, reflecting the
maximum of f ðnþ1ÞðxÞ on ½a; b in general, or more specifically for given x, x0, the
maximum of f ðnþ1ÞðxÞ on ½x; x0 or ½x0; x. According to (9.29) in the proof of prop-
osition 9.95, we really only need an estimate of the absolute value of f ðnþ1ÞðxÞ at an
intermediate point c, which is generally unknown. This crudeness can be a problem
when this interval maximum is large.
As noted above, there are other forms of the remainder, and the Cauchy form,
which reflects an average of f ðnþ1ÞðtÞ between x and x0, will be developed in section
10.8, and seen to succeed in proving analyticity in cases where the Lagrange remain-
der fails.
Example 9.106
We now address three Taylor series quoted and used in prior chap-
ters. The series for f ðxÞ ¼
1
1x was used in example 6.47 in chapter 6, the exponential
series ex was used in chapter 7 in the development of moment relationships, and the nat-
ural logarithm series lnð1 þ xÞ was needed for the chapter 8 development of Stirling’s
formula and other results.
1. With
f ðxÞ ¼
1
1x ¼ ð1  xÞ1 and x0 ¼ 0 it is easy to derive that
f ðnÞðxÞ ¼
n!ð1  xÞn1 and so f ðnÞð0Þ ¼ n!. Noting that ð1  xÞn1 is an increasing function
on ðy; 1Þ, and hence
max
½0;x ð1  yÞn1 ¼
ð1  xÞn1;
0 < x < 1;
1;
x a 0;
(
we obtain from (9.34) that
1
1  x 
X
n
j¼0
x j


a
x
1x


nþ1;
0 < x < 1;
jxjnþ1;
x a 0:
(
476
Chapter 9
Calculus I: Di¤erentiation

In chapter 6 it was shown that Py
j¼0 x j converges for jxj < 1. Consequently the
Lagrange remainder only proves that
1
1x ¼ Py
j¼0 x j in the second case where 1 <
x a 0, since then jxjnþ1 ! 0 as n ! y. For 0 < x < 1,
x
1x > 1, and hence
x
1x


nþ1!
y as n ! y. We will return to this example in chapter 10 with a di¤erent remainder
estimate and proof of convergence to f ðxÞ in this case.
2. With f ðxÞ ¼ ex in (9.34) and x0 ¼ 0, recall that f ð jÞðxÞ ¼ ex and f ð jÞð0Þ ¼ 1 for
all j, and so
ex 
X
n
j¼0
1
j! x j


a
e x
ðnþ1Þ! jxjnþ1;
x > 0;
1
ðnþ1Þ! jxjnþ1;
x a 0;
8
<
:
since the maximum value of f ðnþ1ÞðyÞ over ½0; x is ex when x > 0 and is 1 when x a 0.
Now in chapter 6 it was shown that Py
j¼0
1
j! x j converges for all x A R. By Simpson’s
rule applied to ðn þ 1Þ!,
ðn þ 1Þ!
ffiffiffiffiffi
2p
p
ðn þ 1Þnþð3=2Þeðnþ1Þ ¼
ðn þ 1Þ!
ffiffiffiffiffiffiffi
2pn
p
nþ1
e

nþ1 ! 1;
and so ðn þ 1Þ! grows faster than
nþ1
e

nþ1 and hence much faster than xnþ1 for any x.
This shows that for any value of x, this error goes to zero, and the Taylor series con-
verges to ex as n ! y. In other words, ex is an analytic function, and as was noted in
(7.63),
ex ¼
X
y
j¼0
1
j! x j
for all x A R:
ð9:35Þ
3. With f ðxÞ ¼ lnð1 þ xÞ, we obtain
f 0ðxÞ ¼
1
1 þ x ; f ð2ÞðxÞ ¼
1
ð1 þ xÞ2 ; . . . ; f ðnÞðxÞ ¼ ð1Þnþ1ðn  1Þ!
ð1 þ xÞn
:
Consequently with x0 ¼ 0, f ð0Þ ¼ 0 and f ðnÞð0Þ ¼ ð1Þn1ðn  1Þ! for n b 1. Also, to
find M, note that since
1
ð1þyÞ nþ1 is a decreasing function for y > 1,
max
½0;x
1
ð1 þ yÞnþ1 ¼
1;
0 a x;
1
ð1þxÞ nþ1 ;
1 < x < 0:
(
By (9.34) we obtain
9.3
Derivatives and Taylor Series
477

lnð1 þ xÞ 
X
n
j¼1
ð1Þ jþ1
j
x j


a
1
nþ1 jxjnþ1;
y A ½0; x; x b 0;
1
nþ1
x
1þx


nþ1;
y A ½x; 0; 1 < x a 0:
(
It was shown in chapter 6 that Py
j¼1
ð1Þ jþ1
j
x j converges absolutely for jxj < 1 and con-
ditionally for x ¼ 1, and diverges for x ¼ 1. So as in case 1 of this example, the
Lagrange remainder only yields a partial result. That is, lnð1 þ xÞ ¼ Py
j¼1
ð1Þ jþ1
j
x j in
the first case where 0 a x a 1, since then jxjnþ1
ðnþ1Þ ! 0 as n ! y, and in part of the sec-
ond case where 1 < x a 0. Specifically, for this latter range of x, we have that
x
1þx


a 1 if  1
2 a x a 0 and hence
1
nþ1
x
1x


nþ1! 0 as n ! y. But for 1 < x <  1
2 ,
we see that
x
1þx


 > 1, so
1
nþ1
x
1x


nþ1! y as n ! y. We will return to this example in
chapter 10 with a di¤erent remainder estimate and proof of convergence in this case.
With this analysis applied to x ¼ 1, we can conclude that
ln 2 ¼
X
y
j¼1
ð1Þ jþ1
j
;
ð9:36Þ
deriving the numerical value of the alternating harmonic series as was noted in example
6.10.
9.4
Convergence of a Sequence of Derivatives
Expanding the discussion in section 9.2.7 on convergence of a sequence of continu-
ous functions, there is an analogous discussion related to derivatives which we intro-
duce with the following questions:
Question 1:
If fnðxÞ is a sequence of di¤erentiable functions, and there is a function
f ðxÞ so that fnðxÞ ! f ðxÞ pointwise as n ! y, must f ðxÞ be di¤erentiable?
Question 2:
If f ðxÞ in question 1 is di¤erentiable, must f 0
n ðxÞ ! f 0ðxÞ for every x
as n ! y?
Question 3:
If fnðxÞ ! f ðxÞ uniformly rather than pointwise, do the answers to
questions 1 and 2 change?
Answer:
The answer to all three questions is, in general, ‘‘no,’’ and this is easy to
exemplify.
Example 9.107
1. Define
fnðxÞ ¼
x1þð1=nÞ;
x b 0;
ðxÞ1þð1=nÞ;
x < 0:
(
478
Chapter 9
Calculus I: Di¤erentiation

Then each fnðxÞ is di¤erentiable, with
f 0
n ðxÞ ¼
1 þ 1
n


x1=n;
x b 0;
 1 þ 1
n


ðxÞ1=n;
x < 0:
(
Now fnðxÞ ! f ðxÞ 1 jxj, which is not di¤erentiable at x ¼ 0, and for x 0 0, f 0ðxÞ ¼ 1
for x > 0 and f 0ðxÞ ¼ 1 for x < 0. Also, it is the case that f 0
n ðxÞ ! f 0ðxÞ for x 0 0,
since jxj1=n ! 1 as n ! y for all x 0 0. This observation provides hope, albeit tempo-
rary, that the answer to the second question might be ‘‘yes.’’
2. Define
fnðxÞ ¼ sin nx
ffiffin
p
:
Then each fnðxÞ is di¤erentiable, with
f 0
n ðxÞ ¼
ffiffin
p cos nx:
Now fnðxÞ ! f ðxÞ 1 0 for all x since jsin nxj a 1, and f ðxÞ is di¤erentiable every-
where with f 0ðxÞ 1 0. However, f 0
n ð0Þ ¼
ffiffin
p ! y, while f 0
n ðpÞ alternates between
G ffiffin
p , and f 0
n
p
2
 
cycles through the sequence f0; 
ffiffin
p ; 0;
ffiffin
p g, and so forth.
3. Finally, although uniform convergence provided a positive result in section 9.2.7
above in terms of preserving continuity it does not help here. Case 1 converges uni-
formly on compact sets and case 2 converges uniformly, so the same negative conclu-
sions follow. Note, however, that in case 1 the sequence of derivatives, f 0
n ðxÞ, does not
converge uniformly by the Cauchy criterion on any interval that contains 0, since as
n ! y:
f 0
n ðxÞ !
1;
x > 0;
1;
x < 0:

For case 2, the sequence of derivatives f 0
n ðxÞ does not converge uniformly on any
interval.
Although not the most general statement, the following positive result is adequate
in most applications.
Proposition 9.108
If fnðxÞ is a sequence of continuously di¤erentiable functions and
there is a function f ðxÞ so that on some interval I, fnðxÞ ! f ðxÞ uniformly and f 0
n ðxÞ
9.4
Convergence of a Sequence of Derivatives
479

converge uniformly by the Cauchy criterion, then f ðxÞ is di¤erentiable and f 0
n ðxÞ !
f 0ðxÞ.
Proof
From propositions 9.51 and 9.54 on uniform convergence in section 9.2.7,
the assumption that f 0
n ðxÞ are continuous and converge uniformly by the Cauchy cri-
terion implies that there is a continuous function, gðxÞ say, so that f 0
n ðxÞ ! gðxÞ uni-
formly. What is left to prove is that f ðxÞ is di¤erentiable and f 0ðxÞ ¼ gðxÞ. To this
end, fix x0 A I, and define the ‘‘finite di¤erence functions’’ for x 0 x0:
DnðxÞ ¼ fnðxÞ  fnðx0Þ
x  x0
;
DðxÞ ¼ f ðxÞ  f ðx0Þ
x  x0
:
The assumption that fnðxÞ ! f ðxÞ uniformly implies that for x 0 x0,
DnðxÞ ! DðxÞ
as n ! y:
Since fnðxÞ is di¤erentiable,
lim
x!x0 DnðxÞ ¼ f 0
n ðx0Þ
for all n:
We now show that for fixed x 0 x0, DnðxÞ converges uniformly as n ! y. This fol-
lows in two steps. First o¤, the mean value theorem applied to fnðxÞ  fmðxÞ yields
that for some y between x and x0,
j fnðxÞ  fmðxÞ  fnðx0Þ þ fmðx0Þj ¼ j f 0
n ðyÞ  f 0
mðyÞj jx  x0j:
Second, the uniform convergence of f 0
n ðxÞ means that for any  > 0 there is an N so
that for n; m > N and any y A I,
j f 0
n ðyÞ  f 0
mðyÞj < :
Combining these steps, we derive that for n; m > N and x 0 x0,
jDnðxÞ  DmðxÞj < ;
and so DnðxÞ converges uniformly as n ! y for x 0 x0. Combining these pieces, and
noting that since x0 is a limit point of the set I  x0, the limits below can be reversed
because of proposition 9.60. This produces
f 0ðx0Þ 1 lim
x!x0 DðxÞ
¼ lim
x!x0 lim
n!y DnðxÞ
480
Chapter 9
Calculus I: Di¤erentiation

¼ lim
n!y lim
x!x0 DnðxÞ
¼ lim
n!y f 0
n ðx0Þ:
n
9.4.1
Series of Functions
The preceding proposition 9.108 generalizes easily to a series of functions.
Proposition 9.109
If gjðxÞ is a sequence of continuously di¤erentiable functions, and
there is a function gðxÞ so that on some interval I, Pn
j¼1 gjðxÞ converges uniformly to
gðxÞ as n ! y and Pn
j¼1 g0
jðxÞ converges uniformly by the Cauchy criterion, then gðxÞ
is di¤erentiable and Pn
j¼1 g0
jðxÞ ! g0ðxÞ. In other words,
g0ðxÞ ¼ lim
n!y
X
n
j¼1
g0
jðxÞ:
Remark 9.110
In plain language, the uniform convergence of a series of continuously
di¤erentiable functions yields a di¤erentiable function when the series of derivatives
also converge uniformly, and the derivative of this limit function equals the sum of the
derivatives of terms in the series. That is, uniform convergence of the series and its
derivatives justifies di¤erentiating term by term, which means that
X
y
j¼1
gjðxÞ
 
!0
¼
X
y
j¼1
g0
jðxÞ:
Proof
Define fnðxÞ ¼ Pn
j¼1 gðxÞ. Then fnðxÞ is continuously di¤erentiable for all n
as a finite sum of continuously di¤erentiable functions, and by assumption, fnðxÞ !
gðxÞ uniformly. Also f 0
n ðxÞ 1 Pn
j¼1 g0
jðxÞ, and so f 0
n ðxÞ converges uniformly by the
Cauchy criterion. The result follows from proposition 9.108 above.
n
9.4.2
Di¤erentiability of Power Series
We have seen that in order to have any hope of expanding a given function as a Tay-
lor series, such a function must be infinitely di¤erentiable. However, not all infinitely
di¤erentiable functions can be represented as convergent Taylor series, as
f ðxÞ ¼
e1=x2;
x 0 0;
0;
x ¼ 0;
(
9.4
Convergence of a Sequence of Derivatives
481

analyzed in example 9.99 above illustrates. Here f ðnÞð0Þ ¼ 0 for all n, so the Taylor
series centered at x0 ¼ 0 satisfies
X
y
j¼0
1
j! f ð jÞð0Þx j 1 0;
and so cannot possibly represent this function in any neighborhood of this point.
The property of f ðxÞ called analytic above, or more precisely, analytic in a neigh-
borhood of x0, means more than just that this function is infinitely di¤erentiable
at x0. It means that the function can be represented by a Taylor series centered at
x ¼ x0, and that this series is convergent to the function values in some neighborhood
of this point. The emphasis on ‘‘to the function values’’ is deliberate, since the func-
tion above has a Taylor series centered on x0 ¼ 0 that is convergent everywhere, but
it does not converge to f ðxÞ for any x 0 0.
Now a Taylor series is a special case of a power series introduced in chapter 6, and
it is natural to ask:
Question:
If a function f ðxÞ is defined as the power series f ðxÞ ¼ Py
j¼0 cjðx  x0Þ j
that is convergent for jx  x0j < R for some R > 0:
1. Is f ðxÞ infinitely di¤erentiable, and if so, how is f ðnÞðxÞ evaluated?
2. If infinitely di¤erentiable, is f ðxÞ an analytic function in the sense of (9.30)?
3. If an analytic function, and f ðxÞ is expanded in a Taylor series about x0, must it
be the case that
cn ¼ f ðnÞðx0Þ
n!
?
The following proposition addresses these questions, and provides a‰rmative
responses. It is largely a corollary to proposition 9.109 above on series of functions,
but it is stated here to clarify that a small amount of thought needs to be applied to
assure that the uniformity of convergence needed for the result above applies.
Proposition 9.111
If a function f ðxÞ is defined by the power series
f ðxÞ ¼
X
y
j¼0
cjðx  x0Þ j
ð9:37Þ
and has an interval of convergence given by jx  x0j < R for some R > 0, then:
482
Chapter 9
Calculus I: Di¤erentiation

1. f ðxÞ is infinitely di¤erentiable, and
f ðnÞðxÞ ¼
X
y
j¼n
cj
j!
ð j  nÞ! ðx  x0Þ j
ð9:38Þ
is absolutely convergent for jx  x0j < R. In other words, power series are infinitely dif-
ferentiable and can be di¤erentiated term by term.
2. f ðxÞ is analytic in the sense of (9.30), so
f ðxÞ ¼
X
y
n¼0
f ðnÞðx0Þ
n!
ðx  x0Þn;
and this series is absolutely convergent on jx  x0j < R. Further
f ðnÞðx0Þ
n!
¼ cn:
ð9:39Þ
In other words, power series expansions are unique.
Proof
Define fnðxÞ as the partial summation associated with f ðxÞ:
fnðxÞ ¼
X
n
j¼0
cjðx  x0Þ j:
For the moment, assume the radius of convergence, R < y, where we recall that R is
defined in chapter 6 by R ¼ 1
L , where L is given in (6.20):
L ¼ lim sup
j!y
jcjþ1j
jcjj


:
Then it is apparent that fnðxÞ is continuous, fnðxÞ ! f ðxÞ pointwise on jx  x0j < R,
and hence by exercise 30(b) converges uniformly on the compact jx  x0j a R  ,
for any  > 0. Also fnðxÞ is di¤erentiable,
f 0
n ðxÞ ¼
X
n
j¼1
jcjðx  x0Þ j1;
and we now show that f 0
n ðxÞ converges pointwise on jx  x0j < R by demonstrating
that the series Py
j¼1 jcjðx  x0Þ j1 has the same interval of convergence as the series
for f ðxÞ. By the ratio test,
9.4
Convergence of a Sequence of Derivatives
483

lim sup
j!y
jð j þ 1Þcjþ1ðx  x0Þ jj
j jcjðx  x0Þ j1j
(
)
¼ lim sup
j!y
j þ 1
j
jcjþ1j
jcjj jx  x0j


¼ lim sup
j!y
jcjþ1j
jcjj


jx  x0j
¼ Ljx  x0j:
So the series f 0
n ðxÞ converges on jx  x0j < R and hence also converges uniformly
by the Cauchy criterion on jx  x0j a R  . By proposition 9.108, it follows that
f ðxÞ is di¤erentiable, and f 0ðxÞ ¼ limn!y f 0
n ðxÞ for all jx  x0j a R  . Since this
is true for all  > 0, the result in (9.38) follows for n ¼ 1. However, f 0ðxÞ ¼
Py
j¼1 jcjðx  x0Þ j1 is now a power series to which the same argument applies, and
by iteration, (9.38) follows for all n. If R ¼ y, the same argument applies except that
compact sets needed for uniform convergence are defined, jx  x0j a R0 for any
R0 < y. This proves part 1 of the proposition.
For part 2, it is apparent from (9.38) by substitution that f ðnÞðx0Þ ¼ n!cn, and so
the Taylor series centered on x0 converges absolutely for jx  x0j < R because it is
identical to the power series.
n
Remark 9.112
Of course, the notion that power series representations are unique, as
stated in part 2 of proposition 9.111, is meant in the sense that if for some x0,
f ðxÞ ¼
X
y
j¼0
cjðx  x0Þ j ¼
X
y
j¼0
djðx  x0Þ j
for jx  x0j < R with R > 0, then cj ¼ dj ¼ f ð jÞðx0Þ
j!
for all j. A given analytic function
has many Taylor series expansions for di¤erent values of x0, of course. For example,
expanding about x ¼ 0 and x ¼ 1, we have
ex ¼
X
y
j¼0
x j
j! ¼
X
y
j¼0
eðx  1Þ j
j!
:
By the proposition above, every power series is an analytic function in its interval
of convergence in the sense of definition 9.98 in section 9.3.7.
Example 9.113
In section 7.5.1 formulas were introduced for the moment-generating
function and characteristic function of a discrete random variable, and it was claimed
that each was equal to a power series reflecting the moments of the given random vari-
484
Chapter 9
Calculus I: Di¤erentiation

able. For example, if f ðxÞ is the probability density function of a given discrete random
variable X : S ! fxigy
i¼1 H R, the moment-generating function is defined by
MXðtÞ ¼
X
y
i¼1
etxif ðxiÞ;
when this series converges, and also converges absolutely, for t in an interval I about
t ¼ 0. Now etxi is an analytic function for all t, and expressing it as a Taylor series,
we have
MXðtÞ ¼
X
y
i¼1
X
y
j¼0
ðtxiÞ j
j!
f ðxiÞ:
Since this series is absolutely convergent on I, we can interchange the order of summa-
tion by the analysis in section 6.1.4 to produce (7.64):
MXðtÞ ¼
X
y
j¼0
t j
j!
X
y
i¼1
x j
i f ðxiÞ
¼
X
y
j¼0
t jm0
j
j! :
As a convergent power series on I, we now have that MXðtÞ is infinitely di¤erentiable
on I, and (9.38) can be applied to produce
MðnÞ
X ðtÞ ¼
X
y
j¼n
t jnm0
j
ðj  nÞ! ;
which produces (7.65) when t ¼ 0 is substituted:
m0
n ¼ MðnÞ
X ð0Þ:
The same analysis works for the characteristic function CXðtÞ, when all moments exist,
and demonstrates the analogous properties of this function. As noted before, this
requires the use of the power series expansion for eitxj, with a complex exponent, and
this series is seen to be absolutely convergent by the triangle inequality. However,
CXðtÞ need not be infinitely di¤erentiable at t ¼ 0, and will have the same number of
derivatives there as f ðxÞ has moments.
9.4
Convergence of a Sequence of Derivatives
485

Product of Taylor Series
The next discussion in this section relates to the product of two analytic functions.
Obviously, if f ðxÞ and gðxÞ are any two analytic functions, the function hðxÞ 1
f ðxÞgðxÞ is well defined. The question here is, if f ðxÞ and gðxÞ are given as abso-
lutely convergent Taylor series centered on x0, with respective radii of convergence
of R and R0, is hðxÞ analytic? If so, what is the power series representation of hðxÞ
and what is its radius of convergence?
The following proposition addresses this question, and expands the result in prop-
osition 9.101, which addressed the analyticity of af ðxÞ þ bgðxÞ for a; b A R, when
f ðxÞ and gðxÞ are analytic.
Proposition 9.114
Let f ðxÞ and gðxÞ be analytic functions and given as convergent
power series centered on x0:
f ðxÞ ¼
X
y
n¼0
f ðnÞðx0Þ
n!
ðx  x0Þn;
gðxÞ ¼
X
y
n¼0
gðnÞðx0Þ
n!
ðx  x0Þn;
which are absolutely convergent for jx  x0j < R. Then hðxÞ 1 f ðxÞgðxÞ is an analytic
function, absolutely convergent for jx  x0j < R:
hðxÞ ¼
X
y
n¼0
dnðx  x0Þn;
ð9:40Þ
where
dn ¼
X
n
k¼0
f ðkÞðx0ÞgðnkÞðx0Þ
k!ðn  kÞ!
:
ð9:41Þ
Proof
Because f ðxÞ and gðxÞ are absolutely convergent, the conclusion follows di-
rectly from proposition 6.52. Specifically, (9.41) follows from (6.22).
n
We now have an immediate corollary from this proposition, known as the Leibniz
rule for the nth-derivative of the product of two n-times di¤erentiable functions,
named for Gottfried Wilhelm Leibniz (1646–1716). This corollary applies to the
product of analytic functions, but is true under the weaker assumption that the func-
tions each are simply n-times di¤erentiable. Exercise 34 assigns the proof of this for-
mula in this general case, using mathematical induction.
Proposition 9.115
If f ðxÞ and gðxÞ are analytic functions, absolutely convergent for
jx  x0j < R, then for hðxÞ ¼ f ðxÞgðxÞ,
486
Chapter 9
Calculus I: Di¤erentiation

hðnÞðxÞ ¼
X
n
k¼0
n
k


f ðkÞðxÞgðnkÞðxÞ
for jx  x0j < R:
ð9:42Þ
Proof
This formula for hðnÞðxÞ is true for x ¼ x0 because hðxÞ is analytic, and hence
hðxÞ ¼
X
y
n¼0
hðnÞðx0Þ
n!
ðx  x0Þn:
Comparing this expansion with (6.22), produces hðnÞðx0Þ ¼ n!dn and the result follows
since
n
k
 
¼
n!
k!ðnkÞ! . For any other x with jx  x0j < R, a Taylor series can be cen-
tered on x, and will be absolutely convergent on any interval ðx  R0; x þ R0Þ H
ðx0  R; x0 þ RÞ. With this Taylor series, and the above derivation, (9.42) follows
for all such x.
n
*Division of Taylor Series
The last discussion in this section relates to the division of two analytic functions, or
the reciprocal of an analytic function. Obviously, if f ðxÞ and hðxÞ are any two ana-
lytic functions, the function gðxÞ 1 hðxÞ
f ðxÞ is well defined if f ðxÞ 0 0. When hðxÞ 1 1,
the function gðxÞ is the reciprocal of f ðxÞ. The question here is, if f ðxÞ and hðxÞ are
given as absolutely convergent Taylor series centered on x0, with f ðx0Þ 0 0, and
common radius of convergence of R, is gðxÞ analytic? If so, what is the power series
representation of hðxÞ and what is its radius of convergence?
The following proposition addresses this question:
Proposition 9.116
Let f ðxÞ and hðxÞ be analytic functions and given as convergent
power series centered on x0,
f ðxÞ ¼
X
y
n¼0
f ðnÞðx0Þ
n!
ðx  x0Þn;
hðxÞ ¼
X
y
n¼0
hðnÞðx0Þ
n!
ðx  x0Þn;
which are absolutely convergent for jx  x0j < R and where f ðx0Þ 0 0. Then gðxÞ 1
hðxÞ
f ðxÞ is an analytic function,
gðxÞ ¼
X
y
n¼0
cnðx  x0Þn;
ð9:43Þ
where
c0 ¼ hðx0Þ
f ðx0Þ
ð9:44aÞ
9.4
Convergence of a Sequence of Derivatives
487

cn ¼
1
f ðx0Þ
hðnÞðx0Þ
n!

X
n1
k¼0
f ðnkÞðx0Þck
ðn  kÞ!
"
#
;
ð9:44bÞ
which is absolutely convergent for jx  x0j < R0 for some R0 > 0.
Proof
Because f ðxÞ and hðxÞ are absolutely convergent, the conclusion follows di-
rectly from proposition 6.53, which also showed that
1
f ðxÞ is absolutely convergent.
Specifically, (9.44) follows from (6.25).
n
Remark 9.117
In section 9.8.10 below on the risk-neutral probability qðDtÞ will be an
analysis of the ratio of analytic functions and an application of this result, or equiva-
lently, an application of formulas (6.25). However, it is often the case that the power
series for the ratio can be derived directly and more easily by a ‘‘long division’’ of the
power series of hðxÞ by the power series of f ðxÞ rather than by generating these coe‰-
cients iteratively through formulas such as in (9.44) or (6.25). The importance of the
proposition above is that it assures that this ratio function is analytic in a neighborhood
of x0, so we can generate only a few of the terms and still be sure that the remainder
will converge to 0 with the order of magnitude implied by the number of terms gener-
ated. Without such a result, we could be generating and using a partial sum of a series
for which the remainder did not converge.
Because cn ¼ gðnÞðx0Þ
n!
, we have an immediate corollary from this proposition for the
nth-derivative of the ratio of two analytic functions within the interval of convergence.
This corollary applies to the ratio of analytic functions because we use the result above,
but is true under the general assumption that the functions are each n-times di¤erentia-
ble, as can be proved using mathematical induction.
Proposition 9.118
If gðxÞ 1 hðxÞ
f ðxÞ , with hðxÞ and f ðxÞ given in proposition 9.116, then
gðnÞðxÞ ¼
1
f ðxÞ hðnÞðxÞ 
X
n1
k¼0
n
k


f ðnkÞðxÞgðkÞðxÞ
"
#
;
n b 1:
Proof
This result follows from (9.44), and also follows from the Leibniz rule in
(9.42) by writing hðxÞ ¼ f ðxÞgðxÞ and iteratively solving for gðnÞðxÞ.
n
9.5
Critical Point Analysis
9.5.1
Second-Derivative Test
With the help of section 9.3.8 on Taylor series, it is now possible to classify the criti-
cal points of a di¤erentiable function. Proposition 9.87 above provided a necessary
488
Chapter 9
Calculus I: Di¤erentiation

condition in order that x0 be a relative maximum or relative minimum of f ðxÞ,
namely that f 0ðx0Þ ¼ 0. In other words, a necessary condition is that x0 be a critical
point of f ðxÞ. The second and higher derivatives now provide a sorting of these
cases.
Proposition 9.119
If f ðxÞ is a twice di¤erentiable function with f 0ðx0Þ ¼ 0, and
f 00ðxÞ is continuous in a neighborhood of x0, then:
1. x0 is a relative minimum of f ðxÞ if f 00ðx0Þ > 0
2. x0 is a relative maximum of f ðxÞ if f 00ðx0Þ < 0
3. x0 can be either or neither if f 00ðx0Þ ¼ 0
Proof
First o¤, in cases 1 and 2, as was demonstrated in proposition 9.38, if f 00ðxÞ
is continuous at x0, then there is an interval about x0, say I ¼ ðx0  a; x0 þ aÞ, within
which f 00ðxÞ has the same sign as it does at x0. The result in these cases then fol-
lows immediately from the Taylor series representation in (9.33) with n ¼ 1. Since
f 0ðx0Þ ¼ 0,
f ðxÞ ¼ f ðx0Þ þ 1
2 f 00ðyÞðx  x0Þ2;
where y ¼ x0 þ yDx with 0 < y < 1. Choosing x in the interval I within which the
sign of f 00ðyÞ equals the sign of f 00ðx0Þ, the result follows. Case 3 is easily handled
by examples below.
n
Example 9.120
1. Simple examples of a relative maximum and minimum in cases 1 and 2 are given by
f ðxÞ ¼Gx2 with x0 ¼ 0. We then have f 0ðx0Þ ¼ 0 and f 00ðx0Þ ¼G2.
2. For case 3, we use f ðxÞ ¼Gx4 with x0 ¼ 0 for examples of a maximum and mini-
mum when f 0ðx0Þ ¼ 0 and f 00ðx0Þ ¼ 0; and f ðxÞ ¼ x3 provides a simple example of
f 0ð0Þ ¼ 0 and f 00ðx0Þ ¼ 0 but with x0 ¼ 0 being neither a maximum or minimum. A
critical point that is not a maximum or minimum is a point of inflection or inflection point
of f ðxÞ, although inflection points need not be critical points. See also definition 9.137.
Definition 9.121
Given twice di¤erentiable f ðxÞ, the point x0 is a point of inflection or
inflection point of f ðxÞ if f 00ðxÞ changes sign between x < x0 and x > x0.
Example 9.122
For continuous f 00ðxÞ, we note that f 00ðx0Þ ¼ 0 is therefore a neces-
sary condition for a point of inflection by proposition 9.41, but not a su‰cient condi-
tion, as f ðxÞ ¼ x4 exemplifies at x0 ¼ 0. Also a point of inflection need not be a
critical point, as f ðxÞ ¼ x3  x exemplifies at x0 ¼ 0.
9.5
Critical Point Analysis
489

Remark 9.123
In the case where f 0ðx0Þ ¼ 0 and f 00ðx0Þ ¼ 0, we can resolve the na-
ture of f ðxÞ at x0 if f ðxÞ has enough derivatives by determining the first value of n for
which f ðnÞðx0Þ 0 0. Again based on (9.24), as long as f ðnÞðxÞ is continuous in a neigh-
borhood of x0, we can conclude that:
1. If n is even, x0 will be a relative minimum if f ðnÞðx0Þ > 0 and a relative maximum if
f ðnÞðx0Þ < 0.
2. If n is odd, x0 will be an inflection point, independent of the sign of f ðnÞðx0Þ.
Functions of the form f ðxÞ ¼Gxm provide simple examples of this generalization with
x0 ¼ 0. See section 9.6 on concave and convex functions for more details on points of
inflection, and especially example 9.140.
As will be seen in an lp-norm example in example 9.129 in the next section, it is
not always convenient or even possible to evaluate f 00ðx0Þ to determine if x0 is a
maximum or a minimum. In such cases there is an alternative first derivative test
that is sometimes more convenient to apply.
Proposition 9.124
Let f ðxÞ be a di¤erentiable function, with f 0ðx0Þ ¼ 0, and assume
that there is an open interval I, with x0 A I, on which f 0ðxÞ is continuous. Then:
1. If f 0ðxÞ is a strictly increasing function on I, then x0 is a relative minimum of f ðxÞ.
2. If f 0ðxÞ is a strictly decreasing function on I, then x0 is a relative maximum of f ðxÞ.
Proof
By (9.33) and n ¼ 0, for x A I there is y ¼ x0 þ yDx, with 0 < y < 1, so that
f ðxÞ ¼ f ðx0Þ þ f 0ðyÞDx:
Now, if f 0ðxÞ is a strictly increasing function on I, then since f 0ðx0Þ ¼ 0, we con-
clude that f 0ðxÞ < 0 for x < x0 and f 0ðxÞ > 0 for x > x0. But for x A I, by definition
of y A I, it must be the case that f 0ðyÞDx > 0. So f ðxÞ > f ðx0Þ and x0 is a relative
minimum of f ðxÞ. When f 0ðxÞ is a strictly decreasing function on I, then f 0ðyÞDx <
0, so f ðxÞ < f ðx0Þ and x0 is a relative maximum of f ðxÞ.
n
*9.5.2
Critical Points of Transformed Functions
When pursuing a critical point analysis of a given function f ðxÞ, it is often conve-
nient to first transform the function by taking a composite of f ðxÞ with another func-
tion gðxÞ and consider the critical points of gðf ðxÞÞ. For example, if f ðxÞ is given as
an exponential function f ðxÞ ¼ e jðxÞ, it would be natural to prefer to evaluate the
derivatives of ln f ðxÞ ¼ jðxÞ rather than derivatives of f ðxÞ. This same idea applies
when f ðxÞ is the ratio of functions, f ðxÞ ¼ jðxÞ
kðxÞ , or the product, f ðxÞ ¼ jðxÞkðxÞ,
490
Chapter 9
Calculus I: Di¤erentiation

where again ln f ðxÞ would be simpler to di¤erentiate than f ðxÞ as long as the various
functions are positive so that the logarithm is well defined. In these examples the
function used in the composition is given by gðxÞ ¼ ln x.
Similar considerations apply if f ðxÞ is given as the natural logarithm of a positive
function f ðxÞ ¼ ln jðxÞ, where composing with gðxÞ ¼ ex gives e f ðxÞ ¼ jðxÞ, or if
f ðxÞ is a power of a function f ðxÞ ¼ jðxÞa; where forming the composition with
gðxÞ ¼ x1=a produces a simpler function. In each case composition produces a sim-
pler function to di¤erentiate.
In all such cases the question is: What is the relationship between the critical points
of f ðxÞ and those of gðf ðxÞÞ? The next proposition summarizes the result.
Proposition 9.125
Let f ðxÞ be a di¤erentiable function, and gðxÞ a di¤erentiable
function that is well defined on Rngðf Þ. Then, if x0 is a critical point of f ðxÞ, it will
also be a critical point of gðf ðxÞÞ.
Proof
The function hðxÞ 1 gðf ðxÞÞ is di¤erentiable on Dmnð f Þ, and using the
results from proposition 9.76 produces
h0ðxÞ ¼ g0ð f ðxÞÞ f 0ðxÞ:
Consequently, if f 0ðx0Þ ¼ 0, then h0ðx0Þ ¼ 0.
n
In other words, the critical points of f ðxÞ will be a subset of the critical points of
hðxÞ. However, we see from the formula above for h0ðxÞ that critical points of the
transformed function hðxÞ need not be critical points of f ðxÞ unless one knows that
g0ð f ðx0ÞÞ 0 0.
Example 9.126
Take gðxÞ ¼ ex, ln x, or x1=a. Then g0ðxÞ ¼ ex, 1
x , and 1
a xð1aÞ=a, re-
spectively. In the first two cases, since g0ðxÞ has no zero values, the critical points of
f ðxÞ and those of hðxÞ agree. In the third case of gðxÞ ¼ x1=a, it appears possible for
hðxÞ to inherit extra critical points at any value of x for which f ðx0Þ ¼ 0, since then
h0ðx0Þ ¼ g0ð f ðx0ÞÞ f 0ðx0Þ ¼ 1
a ðf ðx0ÞÞð1aÞ=af 0ðx0Þ ¼ 0:
But this conclusion requires that 1a
a > 0, which is equivalent to 1
a > 1 or 0 < a < 1,
since otherwise, ð0Þð1aÞ=a is meaningless. On the other hand, this transformation would
typically only be considered when f ðxÞ ¼ jðxÞa, which equals 0 only when jðx0Þ ¼ 0.
But, if 0 < a < 1, such an f ðxÞ is not di¤erentiable when jðx0Þ ¼ 0, so the di¤erenti-
ability of f ðxÞ assures that jðx0Þ 0 0 and no additional critical points are inherited in
this case as well.
9.5
Critical Point Analysis
491

In summary, the three simple transformations illustrated above will exactly pre-
serve the critical points of f ðxÞ, as long as the di¤erentiability assumptions of the
proposition are satisfied. For more general transformations, for which g0ðf ðx0ÞÞ ¼ 0
for some x0, the critical points of f ðxÞ will be augmented by the critical points of
gðxÞ on Rngðf Þ.
We turn next to the second derivative test:
Proposition 9.127
Let f ðxÞ be a twice di¤erentiable function, and gðxÞ a twice di¤er-
entiable function that is well defined on Rngðf Þ. Then, if x0 is a critical point of f ðxÞ
that is a relative maximum or relative minimum of f ðxÞ, x0 will have the same property
for gð f ðxÞÞ if g0ð f ðx0ÞÞ > 0, and the opposite property if g0ðf ðx0ÞÞ < 0.
Proof
The function hðxÞ 1 gðf ðxÞÞ is twice di¤erentiable on Dmnðf Þ, and
h00ðxÞ ¼ g00ð f ðxÞÞ½f 0ðxÞ2 þ g0ð f ðxÞÞ f 00ðxÞ:
Consequently, if f 0ðx0Þ ¼ 0, then
h00ðx0Þ ¼ g0ð f ðx0ÞÞ f 00ðx0Þ;
and f 00ðx0Þ and h00ðx0Þ will have the same sign if g0ðf ðx0ÞÞ > 0, and opposite signs if
g0ð f ðx0ÞÞ < 0.
n
Example 9.128
1. If the transforming function, gðxÞ, is an increasing function so that g0ðxÞ > 0 for all
x, proposition 9.125 ensures that the critical points of f ðxÞ and hðxÞ coincide, while
proposition 9.127 ensures that maximums will coincide with maximums, and minimums
with minimums. As examples, gðxÞ ¼ ex is an increasing function for all x, while ln x is
an increasing function for x > 0, as is x1=a as long as a > 0.
2. If the transforming function is a decreasing function so that g0ðxÞ < 0 for all x, the
critical points of f ðxÞ and hðxÞ will again coincide, but maximums and minimums will
be reversed. In such a case is is easier to work with the transforming function: ~gðxÞ 1
gðxÞ, which is increasing, to avoid the necessity of remembering that maximums and
minimums will reverse under gðxÞ.
Recall the following problem from section 3.3.2 on tractability of the lp-norms:
Suppose that we are given a collection of data points fxign
i¼1 that we envision either
as distributed on the real line R or as a point x ¼ ðx1; x2; . . . ; xnÞ A Rn. Assume that
for notational simplicity we arrange the data points in increasing order x1 a x2 a   
492
Chapter 9
Calculus I: Di¤erentiation

a xn. The goal is to find a single number xp that best approximates these points in
the lp-norm, where p b 1. That is, find xp so that
kðx1  xp; x2  xp; . . . ; xn  xpÞkp is minimized:
This problem can be envisioned as a problem in R or as a problem in Rn, but we
choose the former to apply the tools of this chapter. The problem then becomes
Minimize:
f ðxÞ ¼
X
n
i¼1
jxi  xjp
 
!1=p
:
This problem was solved in chapter 3 by direct methods in the cases of p ¼ 1; 2; y,
where we recall that for p ¼ y the lp-norm problem is defined as
Minimize:
f ðxÞ ¼ max
i
fjxi  xjg:
We now return to this example for other values of p.
Example 9.129
To apply the tools of this chapter, we require f ðxÞ to be di¤erentia-
ble, and we have seen in example 9.80 (case 8) that this requires that 1 < p < y. Be-
cause gðxÞ ¼ xp is an increasing function, the maximums and minimums of f ðxÞ and
f ðxÞp agree as noted in example 9.128 above, with
1
a ¼ p. This follows because
f ðxÞ > 0 for all x except in the trivial case where all xj ¼ c, and so f ðcÞ ¼ 0. We ig-
nore this case, since then xp ¼ c apparently.
Suppose that fxjgn
j¼1 contain m di¤erent values, which we denote by fyjgm
j¼1 in
increasing order, and that the original set contains nj of each yj. The goal is then to
find the minimum of hðxÞ ¼ gð f ðxÞÞ:
hðxÞ ¼
X
m
j¼1
njjyj  xjp;
1 < p < y:
From (9.20), we have that
h0ðxÞ ¼
p Pm
j¼1 njðyj  xÞp1;
x a y1;
p Pk
j¼1 njðx  yjÞp1  p Pm
j¼kþ1 njðyj  xÞp1;
yk a x a ykþ1;
p Pm
j¼1 njðx  yjÞp1;
ym a x:
8
>
>
<
>
>
:
Note that h0ðxÞ is continuous, since its values at the interval endpoints fyjgm
j¼1 are well
defined even though they are defined piecewise continuously on intervals. Also h0ðxÞ is
9.5
Critical Point Analysis
493

negative for x a y1 and positive for ym a x. So by the intermediate value theorem,
there is at least one point x0, with
y1 < x0 < ym
and
h0ðx0Þ ¼ 0:
Specifically, if yk a x0 a ykþ1, then
X
k
j¼1
nj pðx0  yjÞp1 ¼
X
m
j¼kþ1
nj pðyj  x0Þp1:
When p ¼ 2, this equation can be explicitly solved, producing
x0 ¼
Pm
j¼1 njyj
Pm
j¼1 nj
¼ 1
n
X
n
j¼1
xj;
as derived in chapter 3.
We can confirm that x0 is always unique for 1 < p < y, since h0ðxÞ is a strictly
increasing function. This is apparent for x a y1 and ym a x but also for yk a x a
ykþ1, since as x increases, the positive summation increases and the negative summa-
tion decreases. This analysis also confirms that x0 is a minimum of hðxÞ, as noted in
proposition 9.124, so x0 ¼ xp.
Note that in general, we can not use a second derivative test to confirm that x0 is a
minimum, since h0ðxÞ is di¤erentiable only if p b 2. The di¤erentiability problem for
1 < p < 2 occurs for x ¼ yj for any j, as h0ðxÞ is di¤erentiable otherwise for any x. If
we assume that p b 2, or if 1 < p < 2 and x0 0 yj for any j, then the second derivative
test can be used:
h00ðxÞ ¼ pðp  1Þ
X
m
j¼1
njjyj  xjp2:
From this we can conclude that h00ðx0Þ > 0, even though x0 is not explicitly known, and
hence x0 is a minimum.
9.6
Concave and Convex Functions
9.6.1
Definitions
In previous chapters the notions of convexity and concavity have been encountered.
First we recall the definitions:
494
Chapter 9
Calculus I: Di¤erentiation

Definition 9.130
A function f ðxÞ is concave on an interval I, which can be open,
closed or semi-closed, finite or infinite, if for any x; y A I,
f ðtx þ ð1  tÞyÞ b tf ðxÞ þ ð1  tÞf ðyÞ
for t A ½0; 1:
ð9:45Þ
A function f ðxÞ is convex on I if, for any x; y A I,
f ðtx þ ð1  tÞyÞ a tf ðxÞ þ ð1  tÞf ðyÞ
for t A ½0; 1:
ð9:46Þ
When the inequalities are strict for t A ð0; 1Þ, such functions are referred to as strictly
concave and strictly convex, respectively.
Remark 9.131
Note that f ðxÞ is concave if and only if f ðxÞ is convex, and con-
versely. Consequently most propositions need only be proved in one case, and the other
case will follow once the e¤ect of the minus sign on the result is reflected.
Interestingly, the properties of concavity and convexity are quite strong. As it
turns out, concave and convex functions are always continuous on open intervals
and are in fact Lipschitz continuous.
Proposition 9.132
If f ðxÞ is concave or convex on an open interval I, then it is Lip-
schitz continuous on I.
Proof
We demonstrate this for a convex function f ðxÞ. Then, if gðxÞ is concave,
the result follows from the continuity of the convex gðxÞ. To this end, let y A I be
given, and let J ¼ ðy  a; y þ aÞ be defined so that ½y  a; y þ a H I. Since I is
open, there is an open interval about y contained in I by definition, and we simply
choose a smaller open interval J whose closure is also in I. Let M ¼ maxðf ðy  aÞ;
f ðy þ aÞÞ. For any x A J, we conclude that f ðxÞ a M, since any such point can be
expressed x ¼ ð1  tÞðy  aÞ þ tðy þ aÞ for some t A ð0; 1Þ, and since f ðxÞ is convex,
(9.46) provides this conclusion. Now let x A J be given and assume for the moment
that x b y. To standardize notation, let x ¼ y þ ta for some t A ½0; 1, then we have
that
y  a < y a x 1 y þ ta < y þ a:
Now, by construction,
x ¼ ð1  tÞy þ tðy þ aÞ:
In order to write x as a linear combination of y  a and this same y, an algebraic
exercise produces
9.6
Concave and Convex Functions
495

y ¼
t
1 þ t ðy  aÞ þ
1
1 þ t x;
where both
t
1þt ; 1
1þt A ½0; 1. Now, from the convexity of f ðxÞ, and the definition of
M, we conclude that
f ðxÞ a ð1  tÞf ðyÞ þ tM;
f ðyÞ a
t
1 þ t M þ
1
1 þ t f ðxÞ:
Using the first inequality for an upper bound, the second for the lower bound,
provides
t½M  f ðyÞ a f ðxÞ  f ðyÞ a t½M  f ðyÞ:
That is,
j f ðxÞ  f ðyÞj a tjM  f ðyÞj:
Since t ¼ xy
a , we have the final result for Lipschitz continuity:
j f ðxÞ  f ðyÞj a jM  f ðyÞj
a
ðx  yÞ
for x b y:
An identical construction applies when x a y, by expressing x ¼ y  ta, so y  a <
x a y < y þ a. Combining the resulting inequalities, we get
j f ðxÞ  f ðyÞj a Cjx  yj:
n
Example 9.133
It is important to note that this proposition does not extend to the re-
sult that a convex/concave function on a closed interval is continuous. For example, on
the interval ½0; 1, define
f ðxÞ ¼
xðx  1Þ;
0 < x a 1;
1;
x ¼ 0:

Then f ðxÞ is apparently concave, and equally apparently, not continuous.
When a function is di¤erentiable, it is relatively easy to confirm when it is either
concave or convex.
Proposition 9.134
There are two derivatives-based tests that characterize convexity
and concavity:
496
Chapter 9
Calculus I: Di¤erentiation

1. If f ðxÞ is di¤erentiable, then:
(a) f ðxÞ is concave on an interval if and only if f 0ðxÞ is a decreasing function on that
interval.
(b) f ðxÞ is convex on an interval if and only if f 0ðxÞ is an increasing function on that
interval.
(c) f ðxÞ is strictly concave i¤ f 0ðxÞ is strictly decreasing, and strictly convex i¤ f 0ðxÞ
is strictly increasing.
2. If f ðxÞ is twice di¤erentiable, then:
(a) f ðxÞ is concave on an interval if and only if f 00ðxÞ a 0 on that interval.
(b) f ðxÞ is convex on an interval if and only if f 00ðxÞ b 0 on that interval.
(c) Strict concavity and strict convexity follow from
f 00ðxÞ < 0, or
f 00ðxÞ > 0,
respectively.
Remark 9.135
1. We use the term ‘‘decreasing’’ in case 1 when we could have used the more compli-
cated notion of ‘‘nonincreasing.’’ The point is that ‘‘decreasing’’ here means that if
x < y, then f ðxÞ b f ðyÞ. When we want to specify that x < y ) f ðxÞ > f ðyÞ, we use
the terminology ‘‘strictly decreasing. Similar remarks apply to the term ‘‘increasing.’’
2. It may be apparent that the first five statements in this proposition were stated in
terms of ‘‘f ðxÞ is concave/convex if and only if . . . .’’ For part 2(c), the second de-
rivative statement is not a characterization of strict concavity or convexity but is a
su‰cient condition. That this second derivative restriction is not necessary is easily
exemplified by f ðxÞ ¼Gx4 on the interval ½1; 1, say. It is apparent that these func-
tions are strictly convex ðþÞ and concave ðÞ on the interval, yet f 00ð0Þ ¼ 0.
Proof
Treating these statements in turn:
1. Given di¤erentiable f ðxÞ, and y < x, define the function:
gðtÞ ¼ f ðtx þ ð1  tÞyÞ;
for t A ½0; 1. Note that g0ðtÞ ¼ f 0ðtx þ ð1  tÞyÞðx  yÞ. Applying (9.33) with n ¼ 0,
and t0 ¼ 0; 1, we get
gðtÞ ¼ gð0Þ þ tg0ðy1Þ;
0 < y1 < t;
gðtÞ ¼ gð1Þ þ ðt  1Þg0ðy2Þ;
t < y2 < 1:
9.6
Concave and Convex Functions
497

Substituting back the original functions produces
f ðtx þ ð1  tÞyÞ ¼ f ðyÞ þ tðx  yÞ f 0ðy þ y1ðx  yÞÞ;
f ðtx þ ð1  tÞyÞ ¼ f ðxÞ þ ðt  1Þðx  yÞf 0ðy þ y2ðx  yÞÞ:
Next, multiplying the first equation by 1  t and the second by t and adding produces
f ðtx þ ð1  tÞyÞ ¼ ð1  tÞf ðyÞ þ tf ðxÞ þ EðtÞ
where the error function is defined as
EðtÞ ¼ ðx  yÞtð1  tÞ½ f 0ðy þ y1ðx  yÞÞ  f 0ðy þ y2ðx  yÞÞ:
To investigate the sign of EðtÞ, recall y < x. So the sign of EðtÞ is the same as the
sign of the term in square brackets. Now since y1 < y2 by construction, y þ y1ðx  yÞ
< y þ y2ðx  yÞ and we conclude that:
EðtÞ b 0 i¤ f 0ðxÞ is decreasing, and then f ðxÞ is concave,
EðtÞ a 0 i¤ f 0ðxÞ is increasing, and then f ðxÞ is convex.
If f 0ðxÞ is strictly monotonic, then f ðxÞ is either strictly concave or strictly convex,
since then EðtÞ > 0 or EðtÞ < 0, respectively.
2. Turning next to twice di¤erentiable f ðxÞ, let y < x be given. Applying (9.33) to
f 0ðxÞ with n ¼ 0, and x0 ¼ y, we get
f 0ðxÞ ¼ f 0ðyÞ þ ðx  yÞ f 00ðyÞ;
y < y < x:
Now, if f 00ðyÞ a 0, for all y, it is apparent that f 0ðxÞ a f 0ðyÞ, and hence f 0ðxÞ is a
decreasing function and f ðxÞ is concave by part 1. Similarly, if f 00ðyÞ b 0, we con-
clude that f ðxÞ is convex.
So the restrictions on f 00ðxÞ in parts 2(a) and 2(b) assure concavity and convexity.
To demonstrate that these restrictions on f 00ðxÞ are assured by the assumptions of
convavity or convexity, we argue the concavity result by contradiction, and the con-
vexity result is identical. Assume that f ðxÞ is concave on an interval and that there is
some x in the interval with f 00ðxÞ > 0. Then
lim
t!0
f 0ðx þ tÞ  f 0ðxÞ
t
> 0:
By definition of limit, we conclude that there exists  > 0 so that f 0ðxþtÞ f 0ðxÞ
t
> 0 for
jtj < . Hence, taking 0 < t < , we conclude that
498
Chapter 9
Calculus I: Di¤erentiation

f 0ðx þ tÞ > f 0ðxÞ:
So f 0ðxÞ is a strictly increasing function on ½x; x þ Þ, contradicting the concavity of
f ðxÞ by part 1(a).
Finally, for part 2(c) if f 00ðyÞ < 0 or f 00ðyÞ > 0 for all y, then strict concavity (re-
spectively, strict convexity) is assured by the identity above between f 0ðxÞ and f 0ðyÞ
for y < x.
n
Example 9.136
1. As noted in section 3.1.5 for the proof of Young’s inequality, f ðxÞ ¼ ln x is concave,
in fact strictly concave, on ð0; yÞ. This function has derivatives f 0ðxÞ ¼ 1
x and f 00ðxÞ ¼
 1
x2 . Observing that f 0ðxÞ is strictly decreasing, or that f 00ðxÞ < 0, on ð0; yÞ, the con-
clusion follows.
2. As noted in section 3.2.2 and in the proof of proposition 6.33, f ðxÞ ¼ xp is strictly
convex on ð0; yÞ for p > 1. Here f 0ðxÞ ¼ pxp1 and f 00ðxÞ ¼ pðp  1Þxp2. Observ-
ing that f 0ðxÞ is strictly increasing, or that f 00ðxÞ > 0, on ð0; yÞ, the conclusion
follows.
3. As a third example, f ðxÞ ¼ ex is strictly convex on R, since f 0ðxÞ ¼ ex is strictly
increasing. Alternatively, f 00ðxÞ ¼ ex > 0 for all x.
Returning to the discussion on points of inflection, we begin with a definition.
Definition 9.137
A point x0 is a point of inflection of f ðxÞ if there is an interval ða; bÞ
containing x0 so that f ðxÞ is concave on ða; x0Þ and convex on ðx0; bÞ, or conversely.
Example 9.138
The point x ¼ 0 is a point of inflection of f ðxÞ ¼ x3, since f 00ðxÞ ¼
6x, which is positive for x > 0, and hence f ðxÞ is convex on ð0; yÞ. Also f 00ðxÞ is neg-
ative for x < 0, and so f ðxÞ is concave on ðy; 0Þ. For this example, f 0ðxÞ ¼ 0, so
x ¼ 0 is also a critical point. But inflection points need not be critical points. For exam-
ple, gðxÞ ¼ x3 þ bx satisfies g00ðxÞ ¼ 6x, so x ¼ 0 is again an inflection point, and yet
g0ð0Þ ¼ b can be any value we choose.
In the same way that potential relative maximums and minimums can be identified
by inspecting the critical points of a function where f 0ðxÞ ¼ 0, there is a necessary
condition in order for a point to be a point of inflection.
Proposition 9.139
If x0 is a point of inflection of a twice di¤erentiable function f ðxÞ
with f 00ðxÞ continuous, then f 00ðx0Þ ¼ 0.
Proof
This follows immediately from proposition 9.134 above, since a twice di¤er-
entiable function satisfies f 00ðxÞ a 0 when concave and f 00ðxÞ b 0 when convex.
9.6
Concave and Convex Functions
499

Since f 00ðxÞ is continuous, f 00ðx0Þ ¼ limx!x0 f ðxÞ, and this common value must
therefore be 0.
n
Example 9.140
As noted in section 9.5.1, functions of the form, f ðxÞ ¼ axn, for inte-
ger n > 2, and a A R, provide a variety of possible behaviors when f 00ð0Þ ¼ 0. For n
even, it is apparent that x0 ¼ 0 is a relative minimum if a > 0, and a relative maximum
if a < 0. For n odd, it is also apparent that for a > 0, the second derivative satisfies
f 00ðxÞ > 0 for x > 0 and conversely for x < 0. Hence x0 ¼ 0 is a point in inflection.
The same conclusion is reached for a < 0.
More generally, as noted in remark 9.123, if f ðxÞ is a function with f ð jÞðx0Þ ¼ 0 for
j ¼ 1; . . . ; n  1, and f ðnÞðx0Þ 0 0, with f ðnÞðxÞ continuous, then if n is even, x0 will be
a relative minimum if f ðnÞðx0Þ > 0 and a relative maximum if f ðnÞðx0Þ < 0. This fol-
lows from (9.24):
f ðxÞ ¼ f ðx0Þ þ 1
n! f ðnÞðyÞðx  x0Þn;
where y is between x and x0. Since f ðnÞðxÞ is continuous, there is an interval about x0,
I, within which f ðnÞðyÞ has the same sign as f ðnÞðx0Þ, as noted in proposition 9.38. Con-
sequently, if f ðnÞðyÞ > 0 for y A I, then since n is even, f ðxÞ b f ðx0Þ and x0 is a rela-
tive minimum, and the same argument applies if f ðnÞðyÞ < 0.
It was also noted that if n is odd, x0 will be a point of inflection independent of the
sign of f ðnÞðx0Þ. To see this, note that (9.24) can also be applied to the function gðxÞ ¼
f 00ðxÞ, for which gðx0Þ ¼ 0 and gð jÞðx0Þ ¼ 0 for j ¼ 1; . . . ; n  3:
gðxÞ ¼
1
ðn  2Þ! gðn2ÞðyÞðx  x0Þn2:
In other words,
f 00ðxÞ ¼
1
ðn  2Þ! f ðnÞðyÞðx  x0Þn2:
Now, if f ðnÞðyÞ > 0 for y A I, then since n is odd, f 00ðxÞ < 0 for x < x0 and conversely
for x > x0. If f ðnÞðyÞ < 0 for y A I, the same argument applies and produces f 00ðxÞ > 0
for x < x0, and conversely for x > x0. So since f 00ðxÞ changes sign at x ¼ x0, this point
is a point of inflection by proposition 9.134.
9.6.2
Jensen’s Inequality
An important consequence of a function f ðxÞ being concave or convex is that it
allows the prediction of the relationship between
500
Chapter 9
Calculus I: Di¤erentiation

E½ f ðXÞ
and
f ðE½XÞ;
where X is a random variable with a given probability density function gðxÞ, and
E denotes the expectation of the given quantity as defined in chapter 7. The result
that will be developed here will apply only to discrete p.d.f.s at this time, but once
the necessary tools are developed, it can be shown to be true in a far more general
context.
To this end, first note that the definition of convexity and concavity, while given in
the context of two points, is true for any finite number.
Proposition 9.141
If f ðxÞ is concave on an interval I, and fxign
i¼1 H I and ftign
i¼1 H
R with ti b 0 for all i and P ti ¼ 1, then
f
X
n
i¼1
tixi
 
!
b
X
n
i¼1
ti f ðxiÞ:
ð9:47Þ
Similarly, if f ðxÞ is convex, then
f
X
n
i¼1
tixi
 
!
a
X
n
i¼1
ti f ðxiÞ:
ð9:48Þ
Proof
The proof is by induction. The result is true for n ¼ 2 by definition. Assum-
ing it is true for n, let fxignþ1
i¼1 H I, and ftign¼1
i¼1 H R be given. Define
t ¼ t1;
x ¼ x1;
1  t ¼
X
nþ1
i¼2
ti;
y ¼
Pnþ1
i¼2 tixi
Pnþ1
i¼2 ti
;
and apply the definition to f ðtx þ ð1  tÞyÞ, obtaining in the convex case
f
X
n
i¼1
tixi
 
!
a t1 f ðx1Þ þ
X
nþ1
i¼2
ti
 
!
f
X
nþ1
i¼2
sixi
 
!
;
where si ¼
ti
T nþ1
i¼2 ti . Now since Pnþ1
i¼2 si ¼ 1, apply the assumption that the result holds
for n to this last term, obtaining
f
X
nþ1
i¼2
sixi
 
!
a
X
nþ1
i¼2
si f ðxiÞ;
and the proof is complete after substitution for si and multiplication by ðPnþ1
i¼2 tiÞ. n
9.6
Concave and Convex Functions
501

This result has two immediate applications. The first is to the proof of the
arithmetic-geometric mean inequality.
Proposition 9.142
If fxign
i¼1 H R, and xi b 0 for all i, then
1
n
X
n
i¼1
xi b
Y
n
i¼1
xi
 
!1=n
:
ð9:49Þ
Proof
See exercise 12.
n
Now consider the earlier question on the relationship between E½ f ðXÞ and
f ðE½XÞ. If X is a finite discrete random variable, with p.d.f. gðxÞ and range fxign
i¼1,
then since gðxiÞ > 0 for all i, and Pn
i¼1 gðxiÞ ¼ 1, proposition 9.141 assures that
E½ f ðXÞ a f ðE½XÞ
if f ðxÞ is concave;
E½ f ðXÞ b f ðE½XÞ
if f ðxÞ is convex:
Both results follow from
E½ f ðXÞ ¼
X
n
i¼1
f ðxiÞgðxiÞ;
f ðE½XÞ ¼ f
X
n
i¼1
xigðxiÞ
 
!
:
Rather than formalize this limited result, we generalize it to the case of an arbi-
trary discrete p.d.f., for which we need a new approach.
Proposition 9.143
If f ðxÞ is di¤erentiable, then for any a,
f ðxÞ a f ðaÞ þ f 0ðaÞðx  aÞ
if f ðxÞ is concave;
f ðxÞ b f ðaÞ þ f 0ðaÞðx  aÞ
if f ðxÞ is convex:
In addition, if f ðxÞ is strictly concave or strictly convex, then the inequalities are
strict.
Remark 9.144
This result is true without the assumption of di¤erentiability, but
where f 0ðaÞ is replaced by a di¤erent function of a. This function is closely related to
the ‘‘derivative,’’ and in fact is defined as a one-sided derivative whereby in the defini-
tion in (9.8), Dx is restricted to be only positive or only negative. It then turns out that
502
Chapter 9
Calculus I: Di¤erentiation

concave and convex functions have both of these one-sided derivatives at every point,
and that they agree, except perhaps on a countable collection of points. In other words,
concave or convex f ðxÞ is not only Lipschitz continuous as proved in proposition 9.132,
but also di¤erentiable, except perhaps on a countable collection of points. However, we
have no further use for this generalization, so we will not develop it. We will instead
simply assume di¤erentiability.
Proof
By the mean value theorem, we have that for any a,
f ðxÞ ¼ f ðaÞ þ f 0ðyÞðx  aÞ;
where y is between x and a. For example, if x > a, then x > y > a. Now, if f ðxÞ
is concave, f 0ðxÞ is a decreasing function, and hence f 0ðyÞ a f ðaÞ if x > a, and
f 0ðyÞ b f ðaÞ if x < a. In both cases f 0ðyÞðx  aÞ a f 0ðaÞðx  aÞ. If f ðxÞ is convex,
the inequalities reverse. When strictly concave or strictly convex, the first derivative
inequalities are sharp and so too are the inequalities in the conclusion.
n
We now turn to an important result related to concave and convex functions,
known as Jensen’s inequality, and named for its discoverer, Johan Jensen, (1859–
1925).
Proposition 9.145 (Jensen’s Inequality)
Let f ðxÞ be a di¤erentiable function, and X
a discrete random variable with range contained in the domain of
f , namely
RngðXÞ H Dmnð f Þ. Then
E½ f ðXÞ a f ðE½XÞ
if f ðxÞ is concave;
ð9:50aÞ
E½ f ðXÞ b f ðE½XÞ
if f ðxÞ is convex:
ð9:50bÞ
If strictly concave or strictly convex, the inequalities are strict.
Proof
Let
a ¼ E½X
in
the
proposition
9.143.
Since
E½ f 0ðaÞðx  aÞ ¼
f 0ðaÞE½ðx  aÞ ¼ 0, the result follows.
n
Remark 9.146
1. Continuous probability distributions will be studied in chapter 10, but it is noted here
that once introduced and the notion of E½ f ðXÞ is defined, the simplicity of the proof
above will carry over to this case without modification.
2. Note that an easy calculation directly demonstrates that if f ðxÞ is an a‰ne function,
f ðxÞ ¼ ax þ b for constants a and b, which is both concave and convex, then
E½ f ðXÞ ¼ f ðE½XÞ:
9.6
Concave and Convex Functions
503

9.7
Approximating Derivatives
As it turns out, the Taylor series approximations in the earlier sections can be used
not only to approximate a given function but also in developing approximation for-
mulas for its various derivatives.
9.7.1
Approximating f O(x)
For a function with only one derivative, we have directly from the definition in (9.8)
that f 0ðx0Þ can be approximated by f ðxÞ f ðx0Þ
Dx
, but this provides no information on
the rate of convergence. Using (9.27) with n ¼ 1 does not help, as even in the case
of continuous f 0ðxÞ the error is seen to be oðDxÞ=Dx ¼ oð1Þ, which just means the
error goes to 0 at some rate of speed, a fact already known from the existence of
f 0ðxÞ.
If we assume that f ðxÞ has two derivatives, we can use (9.27) with n ¼ 2. Spe-
cifically, from f ðxÞ ¼ P2
j¼0
1
j! f ð jÞðx0Þðx  x0Þ j þ OðDx2Þ we obtain by subtracting
f ðx0Þ, dividing by Dx, and solving for f 0ðx0Þ,
f 0ðx0ÞA f ðx0 þ DxÞ  f ðx0Þ
Dx
þ OðDxÞ:
ð9:51Þ
This approximation formula is known as the forward di¤erence approximation, and
the error of OðDxÞ comes from the second derivative term in (9.27) divided by Dx.
This approximation can be improved if there are three derivatives, by applying
(9.27) with n ¼ 3 to both f ðx0 þ DxÞ and f ðx0  DxÞ and subtracting. Then the sec-
ond derivative terms cancel out, and we obtain
f 0ðx0ÞA f ðx0 þ DxÞ  f ðx0  DxÞ
2Dx
þ OðDx2Þ:
ð9:52Þ
This approximation formula is known as the central di¤erence approximation, and
the error term comes from the OðDx3Þ term in (9.27) divided by Dx.
The formula in (9.52) can also be applied if f ðxÞ has only two derivatives, but then
the error is again OðDxÞ as in (9.51).
9.7.2
Approximating f P(x)
Once again applying (9.27) with n ¼ 3 to both f ðx0 þ DxÞ and f ðx0  DxÞ and add-
ing, then subtracting 2f ðx0Þ, we obtain in the case of three derivatives:
f 00ðxÞA f ðx0 þ DxÞ þ f ðx0  DxÞ  2f ðx0Þ
ðDxÞ2
þ OðDxÞ:
ð9:53Þ
504
Chapter 9
Calculus I: Di¤erentiation

This approximation formula is also known as the central di¤erence approximation,
and the error term comes from the OðDx3Þ term in (9.27) divided by Dx2. If f ðxÞ
has four derivatives at x0, we can apply (9.27) with n ¼ 4. The resulting error term
will be OðDx2Þ, since then the third derivatives will cancel.
9.7.3
Approximating f (n)(x), n I 2
Methods similar to those above can be applied but are somewhat more complex. The
reason is that one needs to determine collections of increments, fDxjgn
j¼1, and numer-
ical coe‰cients, fajgn
j¼1, so that the Taylor polynomial for Pn
j¼1 aj f ðx0 þ DxjÞ will
have all derivative terms cancel, except for the last, which we wish to approximate.
One then solves for this last derivative, producing the desired approximation formula
and associated error term. This problem is readily solvable with the tools of linear
algebra.
9.8
Applications to Finance
9.8.1
Continuity of Price Functions
Continuity is a pervasive notion in many applications, including those in finance, and
one that tends to be assumed in virtually every situation without question, or even
explicit recognition. For example, the value at time t of a $100 investment at time 0
with an annual rate of interest of r is given by
f ðr; tÞ ¼ 100ð1 þ rÞt:
Fixing r for the moment, it would be nearly universally assumed that f is a continu-
ous function of t, in that for any t0,
lim
t!t0 f ðr; tÞ ¼ f ðr; t0Þ:
In other words, the value of the investment grows smoothly with time; there are no
unexpected jumps in the account value. One similarly assumes that for t fixed, if r is
close to r0, it would be expected to be the case that f ðr; tÞ will be close to f ðr0; tÞ, and
limr!r0 f ðr; tÞ ¼ f ðr0; tÞ.
Of course, this function is not uniformly continuous in either r or t unless we re-
strict the range of allowable values to a closed and bounded interval. A 25 basis
point change in r has a much smaller absolute e¤ect on f when r is large than when
r is small. In other words, given , the value of d needed so that jr  r0j < d implies
9.8
Applications to Finance
505

that j f ðr; tÞ  f ðr0; tÞj <  increases as r0 increases. For t ¼ 15 and r0 ¼ 0:05, a value
of  ¼ $1 can be achieved with dA0:0007 or about 7 basis points, whereas for
r0 ¼ 0:25, the associated dA0:00082 or about 8:2 basis points.
This lack of uniform continuity is fairly mild and uneventful over the typical range
of market rates, and is also mild compared to that observed when one considers f as
a function of t. In this case, d decreases as t0 increases. Again starting with t0 ¼ 15
and r ¼ 0:05, a value of  ¼ $1 can be achieved with dA0:0007, whereas for t0 ¼ 30,
the associated dA0:00035 or about 3:5 basis points.
Similar remarks apply to the host of fixed income type pricing formulas. For ex-
ample, a general discounted present value of a series of cash flows
f ðrÞ ¼
X
n
t¼0
ctð1 þ rÞt;
as well as the counterpart formula for an n-year semiannual coupon bond in (2.15),
Pði; rÞ ¼ F r
2 a2n;i=2 þ Fv2n
i=2;
are given by continuous functions.
A similar conclusion applies to the price of a preferred stock in (2.21),
Pði; rÞ ¼ Fr
i ;
i > 0;
or the valuation of common stock using the discounted dividend model with growth
in (2.22),
VðD; g; rÞ ¼ D 1 þ g
r  g ;
r > g;
as well as to forward prices on a given traded security in (2.24),
F0ðS0; rT; TÞ ¼ S0ð1 þ rTÞT:
Within the domains of these functions, identified with the tools in this chapter as
functions of a single variable by holding the others constant, intuition compels that
each will produce continuous pricing results, although typically not uniformly con-
tinuous. Based on the theory above, we easily confirm that such intuition if formally
verifiable on the respective price function domains.
506
Chapter 9
Calculus I: Di¤erentiation

9.8.2
Constrained Optimization
The notion of continuity is important for constrained optimization problems. As seen
in chapters 3 and 4, a general problem can be framed as
Maximize ðminimizeÞ:
gðxÞ;
Given:
x A A 1 fx A Rn j f ðxÞ ¼ cg:
Since A ¼ f 1ðcÞ, if f 1 is continuous, then the topological result in proposition
9.67 generalizes and A will be a compact set because c is compact. In addition, gen-
eralizing the proposition 9.39 result for continuous functions on closed and bounded
intervals, if gðxÞ is continuous, it must attain its maximum and minimum on every
compact set. So continuity provides a theoretical assurance of the existence of at least
one solution to such optimization problems. A similar analysis applies if A ¼ fx j
f ðxÞ A Cg where C is any compact set, or if the problem has a finite number of con-
straints, and A ¼ 7jfx j fjðxÞ A Cjg where Cj is compact for all j.
9.8.3
Interval Bisection
Another example comes from chapters 4 and 5 where interval bisection was intro-
duced as a method to solve equations of the form
f ðxÞ ¼ c:
In those chapters this method was illustrated with f ðxÞ denoting the price of a bond
with yield x and c denoting the bond’s current price. In other words, the goal was to
find the bond’s yield to maturity.
This method involves constructing two sequences of values: fxþ
n g and fx
n g with
the property that:
1. xþ
n a x
n ,
2. f ðx
n Þ a c a f ðxþ
n Þ,
3. jxþ
n  x
n j a
jxþ
0 x
0 j
2 n
; that is, jxþ
n  x
n j ¼ Oð2nÞ.
In chapter 5 it was shown that xþ
n  x
n ! 0 implies that there is an x to which
both sequences converge. Then, if f ðxÞ is a continuous function, as is the case
for the price function of a bond, it is also sequentially continuous. Consequently,
xþ=
n
! x assures that f ðxþ=
n
Þ ! f ðxÞ. Finally, because f ðx
n Þ a c a f ðxþ
n Þ, we
conclude that f ðxÞ ¼ c.
9.8
Applications to Finance
507

Of course, if f ðxÞ is a continuous function, the intermediate value theorem assures
the existence of x with f ðxÞ ¼ c as soon as the first two terms of the sequences are
found with f ðx
0 Þ a c a f ðxþ
0 Þ. The method of interval bisection simply provides a
numerical procedure for estimating this value.
9.8.4
Minimal Risk Asset Allocation
Say that two risky assets are given, A1 and A2, to which we desire to allocate a given
dollar investment with weights w1 and w2 ¼ 1  w1. Let the return random variables
be denoted Rj, j ¼ 1; 2, and analogously, the mean returns and standard deviation of
returns denoted mj and sj, j ¼ 1; 2; let the correlation between these returns be r.
The portfolio random return is given as a function of weight w 1 w1:
R ¼ wR1 þ ð1  wÞR2:
Using the results from chapter 7, we derive
E½R ¼ wm1 þ ð1  wÞm2;
ð9:54aÞ
Var½R ¼ w2s2
1 þ ð1  wÞ2s2
2 þ 2wð1  wÞrs1s2:
ð9:54bÞ
Considered as a function of w, it is apparent that E½R ¼ m2 þ ðm1  m2Þw achieves
its maximum and minimum only at the endpoints of any allowable interval for w,
such as ½0; 1 if no short positions are allowed. In other words, E½R has no critical
points. On the other hand,
Var½R ¼ ðs2
1 þ s2
2  2rs1s2Þw2 þ 2s2ðrs1  s2Þw þ s2
2;
is a quadratic function of w, and hence it has a minimum or maximum depending on
the sign of the coe‰cient of w2.
This coe‰cient of w2 is evidently positive when s1 0 s2, since 1 a r a 1 by
proposition 7.43, and
s2
1 þ s2
2  2rs1s2 ¼ ðs1  s2Þ2 þ 2ð1  rÞs1s2:
Hence there is a minimal risk allocation. If s1 ¼ s2, the same conclusion applies
unless r ¼ 1, in which case Var½R is constant and E½R is linear, and acheives its
maximum and minimum at the endpoints of any allowable interval for w.
Denoting Var½R as VðwÞ, we have that
V0ðwÞ ¼ 2ðs2
1 þ s2
2  2rs1s2Þw þ 2s2ðrs1  s2Þ:
508
Chapter 9
Calculus I: Di¤erentiation

Hence the risk-minimizing critical point, where V0ðwminÞ ¼ 0, is given by
wmin ¼
s2ðs2  rs1Þ
s2
1 þ s2
2  2rs1s2
:
ð9:55Þ
Since V00ðwÞ ¼ 2ðs2
1 þ s2
2  2rs1s2Þ > 0 except in the trivial case of s1 ¼ s2 and
r ¼ 1, the second derivative test confirms what we already knew, that wmin is a rela-
tive minimum of this variance function.
Since the denominator of wmin is, with one exception, always positive, the sign of
wmin is determined by the sign of the numerator, s2ðs2  rs1Þ, which is determined
by the sign of s2  rs1. Specifically, the risk-minimizing allocation to A1 satisfies
wmin > 0
if r < s2
s1
;
ð9:56aÞ
wmin ¼ 0
if r ¼ s1
s2
;
ð9:56bÞ
wmin < 0
if r > s2
s1
:
ð9:56cÞ
It is easy to verify that if one of these assets is the risk-free asset, this analysis
yields the obvious conclusion that the minimal risk allocation is wj ¼ 1 in the risk-
free asset. (See exercise 39.)
9.8.5
Duration and Convexity Approximations
The same way that many of the most common pricing functions above can be shown
to be continuous, they are easily shown to be di¤erentiable on their domains of defi-
nition. For instance, the price of an n-year bond with annual cash flows and annual
yield, f ðrÞ ¼ Pn
t¼0 ctð1 þ rÞt, is easily di¤erentiated to produce
f 0ðrÞ ¼ 
X
n
t¼1
tctð1 þ rÞt1;
f 00ðrÞ ¼
X
n
t¼1
tðt þ 1Þctð1 þ rÞt2:
For the price of a preferred stock, with PðiÞ ¼ Fr
i , we have P0ðiÞ ¼  Fr
i2 and
P00ðiÞ ¼ 2Fr
i3 .
9.8
Applications to Finance
509

With such derivatives, one can then approximate the bond price at r based on
information on the bond price function at r0, and similarly for the preferred stock,
using (9.26) and error estimates based on (9.33) or (9.27). In general, for fixed income
applications, such approximations are restated in terms of relative derivatives,
defined as follows:
Definition 9.147
If f ðrÞ denotes the price of a fixed income security as a function of
its yield r, the (modified) duration of f ðrÞ at r0, denoted Dðr0Þ, and the convexity
of f ðrÞ at r0, denoted Cðr0Þ, are defined when f ðr0Þ 0 0 by
Dðr0Þ ¼  f 0ðr0Þ
f ðr0Þ
ð9:57aÞ
¼
Pn
t¼1 tctð1 þ r0Þt1
Pn
t¼0 ctð1 þ r0Þt
;
ð9:57bÞ
Cðr0Þ ¼ f 00ðr0Þ
f ðr0Þ
ð9:58aÞ
¼
Pn
t¼1 tðt þ 1Þctð1 þ r0Þt2
Pn
t¼0 ctð1 þ r0Þt
:
ð9:58bÞ
Of course, duration and convexity are functions of r as is the original price func-
tion, but in practice, one is often focused on the value of these functions at the cur-
rent yield level of r0 rather than in their functional attributes. The formulas above
reflect the assumption of annual cash flows and an annual yield rate r and are easily
generalized. For instance, with semiannual yields and cash flows we have for an
n-year security: f ðrÞ ¼ P2n
t¼0 ct=2 1 þ r
2

t; and duration and convexity are again
defined as relative derivatives of this function. For instance,
Dðr0Þ ¼  f 0ðr0Þ
f ðr0Þ ¼
P2n
t¼1
1
2 tct=2 1 þ r0
2

t1
P2n
t¼0 ct=2 1 þ r0
2

t
:
For the preferred stock, one has Dði0Þ ¼ 1
i0 .
Also note that the definition of duration above is often labeled modified duration
to distinguish it from an earlier notion of Macaulay duration, named for Frederick
Macaulay (1882–1970). Macaulay introduced this calculation in 1938, which in the
annual yield case is
510
Chapter 9
Calculus I: Di¤erentiation

DMacðr0Þ ¼
Pn
t¼1 tctð1 þ r0Þt
Pn
t¼0 ctð1 þ r0Þt ;
ð9:59Þ
with analogous definitions for other yield nominal bases. Modified duration is then
easily seen to equal Macaulay duration divided by ð1 þ rÞ, or in the semiannual case
by 1 þ r
2


, and so forth.
Note that this Macaulay duration formula can be interpreted as a weighted ‘‘time
to cash receipt’’ measure:
DMacðr0Þ ¼
X
n
t¼1
twt;
wt ¼
ctð1 þ rÞt
Pn
t¼0 ctð1 þ rÞt :
Using the values in (9.57) and (9.58), one then has the following approximations
from (9.26):
f ðrÞA f ðr0Þ½1  Dðr0Þðr  r0Þ;
ð9:60Þ
known as the duration approximation, as well as
f ðrÞA f ðr0Þ 1  Dðr0Þðr  r0Þ þ 1
2 Cðr0Þðr  r0Þ2


;
ð9:61Þ
known as the duration approximation with a convexity adjustment. The second for-
mula provides one way to understand and quantify the price sensitivity ‘‘benefit’’ of
a large, positive convexity value. Whether rates increase or decrease, a large positive
convexity value will improve the benefit of duration when this duration e¤ect is pos-
itive, and it will mitigate somewhat the harm of duration when this duration e¤ect is
negative. This convexity benefit is o¤set, of course, by the price one predictably pays
for this extra convexity in terms of a lower yield.
Note that the historical justification for labeling the measure in (9.57) as ‘‘modified
duration’’ was that it was recognized that Macaulay duration could be used to ap-
proximate the price change of a bond, as in (9.60), if this measure was first modified
by dividing by a factor ð1 þ rÞ, or in the semiannual case,
1 þ r
2


, and so forth,
thereby producing a modified duration measure.
Dollar-Based Measures
In the case where f ðr0Þ ¼ 0, which can easily happen when f ðrÞ denotes the price of
a net portfolio such as a long/short bond portfolio, or a hedged bond portfolio,
9.8
Applications to Finance
511

or when f ðrÞ is the price of a derivatives contract such as an interest rate swap or
futures contract, duration and convexity are not defined. In this case one works
with dollar duration, D$ðr0Þ, and dollar convexity, C $ðr0Þ. In general, these measures
are defined in one of two ways as follows:
D$ðr0Þ 1 Dðr0Þf ðr0Þ ¼  f 0ðr0Þ;
ð9:62aÞ
C $ðr0Þ 1 Cðr0Þf ðr0Þ ¼ f 00ðr0Þ:
ð9:62bÞ
When f ðr0Þ ¼ 0 and duration and convexity are not defined, these dollar measures
are defined directly in terms of the price functions derivatives.
In this case of f ðr0Þ ¼ 0, the approximation formulas in (9.60) and (9.61) more
closely resemble standard Taylor series polynomials in (9.34), except for the conven-
tional use of D$ðr0Þ ¼  f 0ðr0Þ. So the formulas become
f ðrÞA f ðr0Þ  D$ðr0Þðr  r0Þ;
ð9:63Þ
f ðrÞA f ðr0Þ  D$ðr0Þðr  r0Þ þ 1
2 C $ðr0Þðr  r0Þ2:
ð9:64Þ
From (9.27) we see that in all cases the error in the duration approximation is
OðDrÞ, while with a convexity adjustment it is OðDrÞ2. Using (9.34), one can also
express the maximum error in the duration approximation for
f ðrÞ
f ðr0Þ in terms of the
maximum of the convexity function between r and r0:
f ðrÞ
f ðr0Þ  ½1  Dðr0Þðr  r0Þ


a M
2 ðr  r0Þ2;
M ¼ max
~r A fr;r0g jCð~rÞj:
Similarly the formula with a convexity adjustment involves the maximum of
f ð3ÞðrÞ
f ðrÞ


on fr; r0g where this notation is intended to denote the interval ½r; r0 or ½r0; r,
depending on which of r0 and r is larger.
When f ðr0Þ ¼ 0, these error bounds follow directly from (9.34). So M reflects the
maximum of j f 00ðrÞj on fr; r0g for the duration approximation and the maximum of
j f ð3ÞðrÞj on fr; r0g for the approximation with a convexity adjustment.
Embedded Options
For more complicated fixed income price functions, such as those associated with
securities with embedded options, the approximations above are again used. How-
ever, because there is no formulaic approach to calculating derivatives in this case,
such derivatives are approximated using formulas such as in (9.51), (9.52), and (9.53)
512
Chapter 9
Calculus I: Di¤erentiation

for an appropriately choosen value of Dr. In such cases one often calls the associated
duration and convexity measures e¤ective duration and e¤ective convexity, in part to
highlight the fact that embedded options have been accounted for and in part to
highlight the dependency on an assumed Dr value used in the estimate. More impor-
tant, this terminology is intended to distance such calculations from those for fixed
cash flow securities for which these measures also have interpretations in terms of
the time distribution of the cash flows. When embedded options are present, all
such connections may cease to exist.
For example, a security such as an interest only (IO) strip of a collateralized mort-
gage obligation (CMO) can have a negative e¤ective duration, despite the fact that
all payments are made in the future. This is because such securities have the property
that they increase in value when rates rise. On the other hand, a principal only (PO)
strip of a CMO, because of the extreme sensitivities of the price function, can have an
e¤ective duration measure significantly in excess of the maximum time to receipt of
the last projected cash flow. In both cases this is because of the embedded prepay-
ment option in the underlying mortgages.
Naturally duration approximations apply equally well to price functions of com-
mon and preferred stock, and one sometimes even sees notions of duration and con-
vexity applied to such securities calculated as above. For example, the price of a
common stock with fixed growth rate dividends is given as VðrÞ ¼ D 1þg
rg , where here
D denotes the dollar value of the last dividend. This function is clearly di¤erentiable
for r > g, the logical domain of definition. The modified duration of this price func-
tion is then calculated as
Dðr0Þ ¼
1
r0  g :
Rate Sensitivity of Duration
In addition to providing a second-order adjustment to the duration approximation
in (9.61), convexity is relevant for determining the sensitivity of the duration measure
to changes in interest rates, and this is in turn relevant in terms of suggesting how
often duration rebalancing may be necessary for the applications of the next section.
Defining the duration and convexity functions, DðrÞ and CðrÞ, as in (9.57) and (9.58)
on the assumption that PðrÞ 0 0, we have
DðrÞ ¼  P0ðrÞ
PðrÞ ;
CðrÞ ¼ P00ðrÞ
PðrÞ :
It is straightforward to evaluate D0ðrÞ and obtain
9.8
Applications to Finance
513

D0ðrÞ ¼ D2ðrÞ  CðrÞ:
ð9:65Þ
Consequently, from the first-order Taylor series for DðrÞ,
DðrÞ ¼ Dðr0Þ þ ½D2ðr0Þ  Cðr0Þðr  r0Þ;
ð9:66Þ
it is apparent that as yields increase, duration will decrease if D2ðr0Þ < Cðr0Þ, and
conversely, and the opposite is true as yields decrease.
This provides another way to understand the price sensitivity benefit associated
with large positive convexity. Specifically, when Cðr0Þ exceeds D2ðr0Þ, the duration
of the security decreases as rates rise, and increases as rates fall. Consequently the
duration e¤ect on price is enhanced when positive, and mitigated when negative. Of
course, small, and especially negative, convexity works oppositely, enhancing the du-
ration e¤ect on price when negative, and mitigating this e¤ect when positive.
But again it is important to note that convexity in a security is not a ‘‘free good’’
when positive, nor a ‘‘free bad’’ when negative. Convexity attributes of a security in-
fluence its desirability, and hence price, so there is an expected price and yield o¤set
to the e¤ect of the convexity adjustment.
9.8.6
Asset–Liability Management
The most important application of the notions of duration and convexity may be to
hedging interest rate risk in a portfolio, which is a major component of asset–liability
management, also called asset–liability risk management, and to the cognoscenti,
ALM. The general setup is that one has an asset portfolio AðiÞ whose value is mod-
eled as a function which depends on the single interest rate i, as well as a liability
portfolio, LðiÞ, which depends on the same rate. The focus of asset–liability manage-
ment is then on the surplus, net worth, or capital of this entity:
SðiÞ ¼ AðiÞ  LðiÞ:
In particular, the focus is on managing the interest rate risk of this net position or
some function of this net position. In this sense, asset–liability risk management is
in fact surplus risk management or capital risk management. As will be seen below,
neither label for this endeavor adequately describes the broad range and applicability
of this theory.
That A, L, and hence S depend on a single interest rate is of course an oversimpli-
fying assumption in the real world, where both assets and liabilities are likely to be
multivariate functions dependent on many interest rates and, in general, di¤erent in-
terest rates. However, in one application of this general theory, A and L are eval-
514
Chapter 9
Calculus I: Di¤erentiation

uated on their respective collections of interest rates, and the parameter i denotes the
common change in all rates. In other words, in this application, while the initial in-
terest rate structures are realistic, the simplifying assumption is that all structures
move in parallel. In this application the model is often referred to as the parallel shift
model.
To address these general multivariate price function models requires additional
tools from multivariate calculus. That said, even in this simplistic context, important
notions can be introduced and understood which underlie the generalizations possi-
ble in that framework.
To ground the reader in specific applications of this theory, consider the following:
Example 9.148
1. Assets, liabilities, and surplus for a financial intermediary such as a life insurer,
property and casualty insurer, commercial bank, or pension fund correspond to the re-
spective portfolios on the entities’ balance sheets. However, in these applications it is
important to recognize that the function values AðiÞ, LðiÞ, and SðiÞ are not intended to
denote the firms’ carrying values on their balance sheets. Carrying values are reflective
of various accounting conventions prescribed by generally accepted accounting princi-
ples (GAAP) for publicly traded firms, which can vary from country to country, al-
though these principles are now in the process of converging to an international
accounting standard (IAS). In the case of US insurance companies, there is also an ac-
counting framework known as statutory accounting, promulgated by the state insurance
regulators, the focus of which is on a conservative estimation of the firms’ capital ade-
quacy. For a pension plan, valuation accounting is the common basis which is reflective
of both regulatory and market valuation principles.
Instead of carrying values, the values implied by AðiÞ, LðiÞ, and SðiÞ are intended to
be market values, or in the case of illiquid or nontradable positions, fair values defined
as the market price ‘‘between a willing seller and willing buyer in a competitive mar-
ket.’’ Of course, in many accounting frameworks, it is the market value that determines
the carrying value. The point here is that whether or not it is defined that way, the focus
of asset–liability management is on market value, broadly defined. That said, one im-
portant responsibility of an ALM manager is to ensure that strategies formulated in
this environment will have well-understood, and favorable, or at least acceptably ad-
verse, e¤ects in the respective accounting regime(s).
2. For a fixed income hedge fund or trading desk of an investment bank, AðiÞ and LðiÞ
could denote the market values of the long and short positions, respectively.
9.8
Applications to Finance
515

3. In a general asset-hedging application, AðiÞ is a portfolio of assets, and LðiÞ, which
may not exist at the moment, is the intended hedging portfolio which intuitively will
represent a ‘‘short’’ position in the market, or a financial derivatives overlay. In such
an application, defining SðiÞ ¼ AðiÞ  LðiÞ as the net position is a notational conve-
nience, and one must be careful about ‘‘signs.’’ If LðiÞ denotes the market value of
securities, and if these securities are shorted, then the net risk position is AðiÞ  LðiÞ.
On the other hand, if LðiÞ denotes the market value of the hedging position, then the
net position is AðiÞ þ LðiÞ. To avoid confusion, hedges are often set up within the for-
mer framework, where LðiÞ denotes the value of a position, which is then shorted, and
hence the math works out with a ‘‘’’ sign.
4. For a general liability-hedging application, such as that related to the issuance of
debt, it is the LðiÞ that is the given, and one might be interested in establishing a hedg-
ing position AðiÞ. Again, it is important to be mindful of the signs used in the analysis.
5. Finally, in fixed income portfolio management such as for a mutual fund, AðiÞ would
naturally denote the value of the portfolio, and one can notionally define LðiÞ as a
position in the portfolio’s benchmark index of the same initial dollar value. Then
AðiÞ  LðiÞ can be evaluated by the portfolio manager to identify interest rate risk posi-
tions vis-a`-vis the benchmark, and trades evaluated in the asset portfolio to manage this
exposure.
To develop some results and unambiguously address the sign problem, imagine
that we wish to quantify the risk profile of SðiÞ ¼ AðiÞ  LðiÞ for a firm as in the first
example above. We assume that initially the interest rate variable has value i0, and
hence the initial value of surplus is Sði0Þ ¼ Aði0Þ  Lði0Þ. In the parallel shift model,
i0 ¼ 0, reflecting valuation on today’s interest rate structures, and the general shift
i0 ! i is really 0 ! i.
To calculate duration and convexity of any portfolio is easy, since the portfolio
values reflect simple weighted averages of the individual securities’ values. For exam-
ple, assume that the asset portfolio value is a sum of security values:
AðiÞ ¼
X
n
j¼1
AjðiÞ;
where to avoid definitional problems we assume that Ajði0Þ 0 0 for all j and
Aði0Þ 0 0. The second condition is not superfluous, since fAjði0Þg values may be
both positive and negative.
Then because derivatives of sums equal sums of derivatives by proposition 9.75, it
is straightforward to derive (see exercise 19) with wj ¼ Ajði0Þ
Aði0Þ :
516
Chapter 9
Calculus I: Di¤erentiation

DAði0Þ ¼
X
n
j¼1
wjDjði0Þ;
ð9:67aÞ
C Aði0Þ ¼
X
n
j¼1
wjCjði0Þ;
ð9:67bÞ
Of course, Pn
j¼1 wj ¼ 1, although fwjg may contain both positive and negative
values.
Depending on the goals of the ALM program, the risk in Sði0Þ associated with a
change in interest rates may be defined in one of several ways. If TðiÞ denotes the
target risk measure, three of which are illustrated below, the first step is to calculate
the second-order Taylor series expansion of TðiÞ as in (9.61):
TðiÞATði0Þ 1  DTði0Þði  i0Þ þ 1
2 C Tði0Þði  i0Þ2


:
The error in this approximation is OðDi3Þ by (9.27) if Tð3ÞðiÞ exists, and oðDi3Þ by
(9.28) if Tð3ÞðiÞ is continuous.
The risk to this function from the shift i0 ! i comes from duration risk DTði0Þ,
which presents a signed risk of order OðDiÞ, and from convexity risk C Tði0Þ, which
presents an unsigned risk of order OðDi2Þ. By a signed risk is meant that the e¤ect
on TðiÞ by the shift i0 ! i 1 i0 þ Di, depends on the sign of Di, as in G, and on the
magnitude of Di, whereas for an unsigned risk the e¤ect does not depend on sign but
only the magnitude of Di.
The Holy Grail of ALM is then to seek to achieve the following structure:
DTði0Þ ¼ 0;
ð9:68aÞ
C Tði0Þ > 0:
ð9:68bÞ
This then results in a target risk measure with the classical immunized risk profile as
graphed in figure 9.4.
To some practitioners, the goal of risk immunization is considered unrealistic, since
the resulting portfolio would appear to represent a risk-free arbitrage in the market.
No matter what becomes of interest rates, a profit is made. This criticism has some
merit as a cautionary statement about what is and is not possible, but the simple no-
tion that ‘‘immunization is impossible because to do so would be to create a risk-free
arbitrage, a free lunch, and this is impossible,’’ overstates the case.
9.8
Applications to Finance
517

In order to be a true risk-free arbitrage, all of the following would need to be true,
and in practice, they never are:
1. The trade from the original target portfolio, to the immunized portfolio, can be
done in a cost free way.
2. The resulting immunized portfolio earns more than the risk-free rate at all times.
3. The risk associated with i0 ! i summarizes all the risks of the portfolio; no other
risks exist and no new risks are added.
So, in practice, the pursuit of immunization will not create a risk-free arbitrage but
will create a framework within which many of the risks of the portfolio can be sum-
marized, and various hedging trades evaluated from a cost/benefit perspective.
Three approaches to TðiÞ are developed next. The goal here is not to present the
only, or even the best, approaches but to illustrate the broad applicability of this gen-
eral methodology.
Surplus Immunization, Time t F 0
The target measure is simply the current value of surplus:
TðiÞ ¼ SðiÞ:
Because S 0ðiÞ ¼ A0ðiÞ  L0ðiÞ, and similarly for S 00ðiÞ, a simple calculation produces
the following as long as Sði0Þ 0 0, and these should be understood as special cases of
(9.67):
Figure 9.4
TðiÞATði0Þ

1 þ 1
2 C Tði0Þði  i0Þ2
518
Chapter 9
Calculus I: Di¤erentiation

DSði0Þ ¼ Aði0Þ
Sði0Þ DAði0Þ  Lði0Þ
Sði0Þ DLði0Þ;
ð9:69Þ
C Sði0Þ ¼ Aði0Þ
Sði0Þ C Aði0Þ  Lði0Þ
Sði0Þ C Lði0Þ:
ð9:70Þ
To achieve the objectives in (9.68) then requires that
DAði0Þ ¼ Lði0Þ
Aði0Þ DLði0Þ;
ð9:71Þ
C Aði0Þ > Lði0Þ
Aði0Þ C Lði0Þ:
ð9:72Þ
In the case of Aði0Þ ¼ Lði0Þ, and hence Sði0Þ ¼ 0, these conditions formally reduce
to
DAði0Þ ¼ DLði0Þ;
ð9:73Þ
C Aði0Þ > C Lði0Þ:
ð9:74Þ
But note that (9.73) is not a legitimate deduction from (9.71), since this latter formula
was developed under the assumption that Sði0Þ 0 0, which is to say, Aði0Þ 0 Lði0Þ.
Still, in the case where Sði0Þ ¼ 0, one can work directly with the original Taylor
series expansions of SðiÞ in (9.27), which is to say, the dollar duration and dollar con-
vexity approach, and it will be seen that the immunizing conditions in (9.73) and
(9.74) are produced, and legitimately so (see exercise 42).
Surplus Immunization, Time t I 0
If ZtðiÞ denotes the market price of a t-period, risk-free zero-coupon bond that
matures for $1 at time t, the forward value of surplus, denoted StðiÞ, is defined by
StðiÞ 1 SðiÞ
ZtðiÞ :
The intuition for this definition is that if surplus was now liquidated and invested in
zeros, this would be the value produced at time t with certainty. In that sense, StðiÞ is
the value achievable at time t with the current portfolio and interest rates at level i if
liquidated and reinvested.
Immunizing the forward value of surplus means that
TðiÞ ¼ StðiÞ;
9.8
Applications to Finance
519

and this requires conditions that depend on t that reduce to those above when t ¼ 0.
To this end, we first calculate S 0
tðiÞ and S 00
t ðiÞ. Although a bit messy, the following is
produced if Sði0Þ 0 0 (see exercise 46):
DStði0Þ ¼ DSði0Þ  DZtði0Þ;
ð9:75aÞ
C Stði0Þ ¼ C Sði0Þ  C Ztði0Þ  2DZtði0Þ½DSði0Þ  DZtði0Þ:
ð9:75bÞ
Applying (9.68), the immunizing conditions are
DSði0Þ ¼ DZtði0Þ;
ð9:76aÞ
C Sði0Þ > C Ztði0Þ:
ð9:76bÞ
Note that as t ! 0, it is apparent that DZtði0Þ ! 0 and C Ztði0Þ ! 0, and so the
conditions in (9.76) reduce to those in (9.71) and (9.72). Also, in the case of
Sði0Þ ¼ 0, one can work directly with the Taylor series for StðiÞ ¼ ðAðiÞ  LðiÞÞ=
ZtðiÞ to produce the conditions in (9.73) and (9.74), and hence the result is then inde-
pendent of t.
Surplus Ratio Immunization
The surplus ratio, denoted RðiÞ, is defined by
RðiÞ ¼ SðiÞ
AðiÞ :
It is unnecessary to specify whether this is the time 0 surplus ratio or the time t > 0
ratio, since it is easy to see that
RtðiÞ 1 StðiÞ
AtðiÞ ¼ SðiÞ
AðiÞ :
To immunize the surplus ratio is to set
TðiÞ ¼ RðiÞ:
As a ratio, the duration and convexity formulas for RðiÞ are identical to those of
the ratio function StðiÞ in (9.75), with only a change in notation, which we record
here, when Sði0Þ 0 0:
DRði0Þ ¼ DSði0Þ  DAði0Þ;
ð9:77aÞ
C Rði0Þ ¼ C Sði0Þ  C Aði0Þ  2DAði0Þ½DSði0Þ  DAði0Þ:
ð9:77bÞ
520
Chapter 9
Calculus I: Di¤erentiation

Applying (9.68) to these formulas produces
DSði0Þ ¼ DAði0Þ;
ð9:78aÞ
C Sði0Þ > C Aði0Þ:
ð9:78bÞ
Note that (9.78) reduces to (9.73) and (9.74) when (9.69) and (9.70) are used to elim-
inate the dependence on SðiÞ.
It is also the case that (9.73) and (9.74) present the correct immunizing conditions
for the surplus ratio when Sði0Þ ¼ 0, as can be derived by working directly with R0ðiÞ
and R00ðiÞ, or simply recognizing that immunizing SðiÞ when Sði0Þ ¼ 0 is identical to
immunizing RðiÞ in this case, and hence, (9.73) and (9.74) follow immediately.
9.8.7
The ‘‘Greeks’’
Although duration and convexity, which are relative derivative measures, are the
conventional way to measure and quote the sensitivities of fixed income instruments
and associated interest rate based derivative securities, for most other financial
instruments, sensitivities are expressed directly in terms of the derivatives of the price
functions. For example, the price of a put or call option based on the Black–
Scholes–Merton formulas in chapter 8 is clearly a function of:
S0: stock price
s: stock price volatility
r: risk-free rate
t or T: time to expiry
The name ‘‘Greeks’’ is given to the various derivatives of this price function, and
further applied to other financial derivative securities on currencies, commodities,
common stock indexes, futures contracts, and so forth. With O used to denote the
price of the given security, which is a function of these variables, the derivatives of
O are labeled with Greek letters, and sometimes with a fictional ‘‘Greek’’ letter:
delta:
D ¼ dO
dS ;
ð9:79aÞ
gamma:
G ¼ d 2O
dS2 ;
ð9:79bÞ
rho:
r ¼ dO
dr ;
ð9:79cÞ
9.8
Applications to Finance
521

‘‘vega’’:
n ¼ dO
ds ;
ð9:79dÞ
theta:
y ¼ dO
dt :
ð9:79eÞ
Note that the Greek symbol for ‘‘vega’’ is actually the lowercase Greek letter nu.
While we will not formally address multivariate functions, for the purposes of the
definitions above, derivatives can be defined as if the price function in question is a
function of only the variable of interest. Also with this convention the Taylor series
results above can be applied. For instance,
OðSÞAOðS0Þ þ DðS  S0Þ þ 1
2 GðS  S0Þ2;
and we know that the error is OðDS2Þ. However, to approximate this price func-
tion simultaneously in all variables will require some new tools from multivariate
calculus.
From the formulas above, the Greeks allow the risk evaluation of general equity-
based and financial derivatives-based portfolios, and with this model, hedging strat-
egies can be formulated that are parallel to those discussed in section 9.8.6 on
asset-liability management.
9.8.8
Utility Theory
An important application of the notions of concavity and convexity in finance and
economics is within the subject of utility theory, which provides a mathematical
framework and model for understanding a given person’s choices among various
risky alternatives. Such risk preferences are expressed all the time, of course, such as
when an individual chooses among various risky investments, or between risky and
risk-free assets, as well as when that individual decides what kind of insurance to
buy, or how much, or even whether or not to buy. Indeed it is also expressed in terms
of an individual’s propensity to gamble, as well as in the particular games of chance
that attract more versus attract less.
While this subject can be studied within a formal axiomatic framework, we instead
take an informal approach but note its origins. The key result is called the von
Neumann–Morgenstern theorem, named for its discoverers: John von Neumann
(1903–1957) and Oskar Morgenstern (1902–1977). This theorem states that if an in-
dividual has risk preferences that are consistent and satisfy certain other logical rela-
tionships, then there is a function uðxÞ, the utility function, so that ‘‘preference’’ can
522
Chapter 9
Calculus I: Di¤erentiation

be predicted by the expected value of uðWðXÞÞ, where WðXÞ denotes the value of
the individual’s wealth as a function of the realization of the risky variable X. The
calibration of uðxÞ as an increasing function is done so that ‘‘more is better than
less,’’ or ‘‘greater utility is preferred to less,’’ and hence the objective of a decision
maker is to maximize the ‘‘expected utility’’ of wealth, E½uðWðXÞÞ.
In this setting, W0 is often used to denote the initial wealth of the decision maker
at the time of the decision.
Investment Choices
Within this risk-preference framework an investment of I a W0 over time period
½0; T with risky returns defined by a random variable Y will be deemed attractive
compared to a risk-free investment if and only if
E½uðWðYÞÞ > uðW0ð1 þ rÞTÞ:
Here r denotes the annual risk-free rate for the period, and
WðYÞ ¼ Ið1 þ YÞ þ ðW0  IÞð1 þ rÞT:
This framework also works for I > W0, in which case the investment involves a short
position in the risk-free asset.
More generally, this investment will be preferred to another investment with risky
returns defined by a random variable Y 0, for an investment of I, if and only if
E½uðWðYÞÞ > E½uðWðY 0ÞÞ;
where the wealth functions, WðYÞ and WðY 0Þ are defined as above.
Of course, the decision of how much to invest can also be addressed in this frame-
work, since the optimum I, given Y, is the value that maximizes E½uðWðYÞÞ, for a
given investment. This maximum might well be at I < 0, I ¼ 0, or I > W0.
Insurance Choices
Insurance decisions can also be posed in this framework, where now X denotes a
risky loss that an individual confronts and is contemplating insuring. If insurance
costs P, then the individual will insure if
uðW0  PÞ > E½uðW0  XÞ:
For partial versus complete insurance, the choice would be to completely insure if
uðW0  PÞ > E½uðW0  Pl  ð1  lÞXÞ;
9.8
Applications to Finance
523

where Pl is the cost to insure 100l% of the loss. One could also determine the value
of l which maximizes E½uðW0  Pl  ð1  lÞXÞ.
Gambling Choices
For a gambling choice, say the purchase of a lottery ticket with a cost of L, the deci-
sion will be to gamble if
E½uðW0  L þ YÞ > uðW0Þ;
where Y is the random pay-o¤ from the gamble.
Utility and Risk Aversion
As noted above, utility functions are calibrated as increasing functions, and hence
given the assumption of di¤erentiability it is always the case that u0ðxÞ > 0. The es-
sence of the risk preference, however, is defined by the sign of the second derivative,
u00ðxÞ. Specifically, we have the terminology:
Risk averse:
u00ðxÞ < 0; and so uðxÞ is strictly concave:
ð9:80aÞ
Risk neutral:
u00ðxÞ 1 0; and so uðxÞ is linear ðaffineÞ:
ð9:80bÞ
Risk seeking:
u00ðxÞ > 0; and so uðxÞ is strictly convex:
ð9:80cÞ
The motivation for this terminology comes from an application of Jensen’s in-
equality to specific risk preference questions, as will be seen below. Note that by
(9.33) with n ¼ 1, we have u00ðxÞ 1 0 if and only if uðxÞ ¼ ax þ b, and hence justify-
ing the terminology that this is a linear utility function (the formal term is ‘‘a‰ne’’
unless b ¼ 0).
To evaluate an investment over a fixed horizon, it must be recognized that the de-
cision to not invest in a risky asset should not be modeled as if the funds will remain
dormant. The more logical alternative would be to assume that the choice is between
a risky and a risk-free investment. Assume that over the investment horizon in ques-
tion, the risk-free rate per period, a year say, can be expressed as r. To invest over
½0; T, measured in an integer number of periods, with X denoting the risky period
return, the choice is between
Risk-free investment:
uðW0 þ Iðð1 þ rÞT  1ÞÞ;
Risky investment:
E u W0 þ I
Y
T
j¼1
ð1 þ XjÞ  1
 
!
 
!
"
#
:
524
Chapter 9
Calculus I: Di¤erentiation

The following proposition summarizes the result for an investment choice, and
exercises 22 and 47 assign the task of developing the conclusions as they apply to an
insurance choice or a gamble.
Proposition 9.149
Given a planning horizon of ½0; T, a decision maker will be indif-
ferent between the risky investment and the risk-free investment, depending on the rela-
tionship between E½QT
j¼1ð1 þ XjÞ and ð1 þ rÞT, as follows:
1. If risk averse, indi¤erence requires E½QT
j¼1ð1 þ XjÞ ¼ ð1 þ r þ aÞT; for some
a > 0.
2. If risk neutral, indi¤erence requires E½QT
j¼1ð1 þ XjÞ ¼ ð1 þ rÞT.
3. If risk seeking, indi¤erence requires E½QT
j¼1ð1 þ XjÞ ¼ ð1 þ r  aÞT for some
a > 0.
Remark 9.150
1. Note the intuitive justification for the risk preference terminology. For a risk-averse
investor, in order to be indi¤erent between the risky and risk-free investment, the risky
investment must have an expected return in excess of the risk-free rate. In other words,
a risk-averse investor requires a ‘‘positive risk premium’’ on the expected return in
order to be willing to take the risk of a possible lower return. A risk seeker will be in-
di¤erent even with an expected return below the risk-free rate. In essence, such an in-
vestor is willing to give up expected return for the opportunity to do better with a risky
return. Finally, a risk-neutral investor is ‘‘neutral’’ to risk, and is willing to take risk
with no associated adjustment to the expected return versus the risk-free rate.
2. The proposition above is stated in terms of an annual or period nominal interest rate
r, but it can be equivalently stated in terms of a continuously compounded risk-free rate
r0. For example, for a risk-neutral investor the condition becomes
E
Y
T
j¼1
ð1 þ XjÞ
"
#
¼ er0T:
Proof
The decision maker will be indi¤erent if
uðW0 þ Iðð1 þ rÞT  1ÞÞ ¼ E u W0 þ I
Y
T
j¼1
ð1 þ XjÞ  1
 
!
 
!
"
#
:
Now, if the investor is risk averse, and hence with a strictly concave utility function,
we have from Jensen’s inequality in (9.50a) that
9.8
Applications to Finance
525

E u W0 þ I
Y
T
j¼1
ð1 þ XjÞ  1
 
!
 
!
"
#
< u W0 þ I
E
Y
T
j¼1
ð1 þ XjÞ
"
#
 1
 
!
 
!
:
Comparing, we see that for a risk-averse investor to be indi¤erent requires that
uðW0 þ Iðð1 þ rÞT  1ÞÞ < u W0 þ I
E
Y
T
j¼1
ð1 þ XjÞ
"
#
 1
 
!
 
!
;
and recalling that uðxÞ is an increasing function, we obtain the first result. That is, for
some a > 0,
W0 þ Iðð1 þ r þ aÞT  1Þ ¼ W0 þ I
E
Y
T
j¼1
ð1 þ XjÞ
"
#
 1
 
!
:
For the risk-neutral investor, this second last equation is
uðW0 þ Iðð1 þ rÞT  1ÞÞ ¼ u W0 þ I
E
Y
T
j¼1
ð1 þ XjÞ
"
#
 1
 
!
 
!
;
and hence the second result. Finally, for a risk seeker with strictly convex utility
function, by (9.50b),
E u W0 þ I
Y
T
j¼1
ð1 þ XjÞ  1
 
!
 
!
"
#
> u W0 þ I
E
Y
T
j¼1
ð1 þ XjÞ
"
#
 1
 
!
 
!
;
and the final equation to solve is
uðW0 þ Iðð1 þ rÞT  1ÞÞ > u W0 þ I
E
Y
T
j¼1
ð1 þ XjÞ
"
#
 1
 
!
 
!
:
Since uðxÞ is increasing, we obtain the third conclusion.
n
Example 9.151
1. The risk-neutral probability was introduced in section 7.8.6, and generalized in sec-
tion 8.8.3 to an arbitrary period of length Dt, and is defined by
qðDtÞ ¼ erDt  edðDtÞ
euðDtÞ  edðDtÞ :
526
Chapter 9
Calculus I: Di¤erentiation

Here r denotes the annualized risk-free rate, assumed constant, uðDtÞ and dðDtÞ the
assumed upstate and downstate returns of the stock in the period, and qðDtÞ the proba-
bility of an upstate. As was shown in chapter 7, and easily generalized to a period of
length Dt, the expected value of the stock at time Dt under q satisfies
Eq½SDt ¼ erDtS0:
In other words, with 1 þ X ¼ SDt
S0 equal to the random period return,
E½1 þ X ¼ erDt;
justifying by the proposition above that qðDtÞ is the probability of an upstate for a risk
neutral investor willing to pay S0 for this security.
2. A special risk-averter probability was also introduced in chapter 8 in connection
with the Black–Scholes–Merton pricing formulas and defined in (8.55) by
qðDtÞ ¼ qðDtÞeuðDtÞerDt:
A simple calculation now produces, dropping the Dt for notational simplicity, that
1  q ¼ ð1  qÞederDt and
Eq½SDt ¼ qðS0euÞ þ ð1  qÞðS0edÞ
¼ ½eu  euþdrDt þ edS0:
Although not immediately apparent, Eq½1 þ X > erDt, and so qðDtÞ is the probability
of an upstate for a risk-averse investor willing to pay S0 for this security. This conclu-
sion follows from the algebraic steps:
eu  euþdrDt þ ed > erDt
i¤ :
eurDt  euþd2rDt þ edrDt  1 > 0
i¤ :
ðeurDt  1Þð1  edrDtÞ > 0:
The validity of this last inequality follows from dðDtÞ < rDt < uðDtÞ.
Examples of Utility Functions
Remark 9.152
Note that by the definition above of risk preference, we can conclude
that:
9.8
Applications to Finance
527

1. If uðxÞ is any utility function, then ~uðxÞ 1 auðxÞ þ b has the same properties for any
a; b A R and a > 0 in terms of risk aversion, risk neutrality or risk seeking because
~u00ðxÞ ¼ au00ðxÞ.
2. In addition, for a; b A R and a > 0, a decision maker with utility function ~uðxÞ will
make identical decisions as one with uðxÞ. This conclusion follows from the fact that
E½~uðWðxÞÞ ¼ aE½uðWðxÞÞ þ b, and hence in any of the preceding decision inequal-
ities between an expected utility and a fixed utility, or between two expected utilities,
the a and b play no role.
3. Because of 1 and 2, utility functions are sometimes calibrated so that uðW0Þ ¼ 0
and/or uð0Þ ¼ 1.
4. If uðxÞ is a risk-averse utility function, then auðxÞ þ b is risk-seeking for a < 0 and
any b, and conversely.
A few common examples of risk-averse utility functions defined on x b 0 follow.
Each can be made to represent risk seeking preference by multiplying by 1 by re-
mark 4 above.
Example 9.153
1. Exponential Utility:
uðxÞ ¼ 1  ekx;
k > 0:
2. Quadratic Utility:
uðxÞ ¼ ax  bx2;
a; b > 0:
Note that this utility function violates the u0ðxÞ > 0 assumption, at least for x > a
2b .
3. Power Utility:
uðxÞ ¼ 1
l xl;
l > 0:
4. Logarithmic Utility:
uðxÞ ¼ ln 1 þ x
c


;
c > 0:
9.8.9
Optimal Risky Asset Allocation
Assume that an investor with utility function uðxÞ and initial wealth W0 wants to
make an optimal allocation between a risky asset, with period return random vari-
528
Chapter 9
Calculus I: Di¤erentiation

able X, and the risk-free asset, with period return r. If I denotes the investment in the
risky asset, this investor’s risky utility after investment for T periods is
u W0ð1 þ rÞT þ I
Y
T
j¼1
ð1 þ XjÞ  ð1 þ rÞT
 
!
 
!
:
For notational ease, we assume the planning horizon T ¼ 1, so the risky utility value
is
uðW0ð1 þ rÞ þ IðX  rÞÞ:
Here r can denote the fixed risk-free return for the period, or the variable com-
pounded risk-free returns over subperiods.
Now, if we temporarily assume that uðxÞ is an analytic function, this risky utility
can be expanded about W0ð1 þ rÞ to produce
uðW0ð1 þ rÞ þ IðX  rÞÞ ¼
X
y
k¼0
1
k! uðkÞðW0ð1 þ rÞÞðIðX  rÞÞk:
If only di¤erentiable to order m, this expansion holds up to the mth derivative as a
Taylor series, with error no worse than OðDxmÞ with Dx 1 IðX  rÞ. For notational
simplicity, we maintain the upper summation limit of y.
To simplify the analysis, and because of the second point made in remark 9.152,
this utility function can be transformed to the form: ~uðxÞ ¼ auðxÞ þ b with a > 0,
without changing any conclusions that we may draw. Since we assume that
u0ðW0ð1 þ rÞÞ > 0, we define
~uðxÞ ¼ uðxÞ  uðW0ð1 þ rÞÞ
u0ðW0ð1 þ rÞÞ
:
This then produces
~uðW0ð1 þ rÞ þ IðX  rÞÞ ¼
X
y
k¼1
1
k!
uðkÞðW0ð1 þ rÞÞ
u0ðW0ð1 þ rÞÞ I kðX  rÞk
¼
X
y
k¼1
1
k! ~ukI kðX  rÞk;
with
9.8
Applications to Finance
529

~uk ¼ uðkÞðW0ð1 þ rÞÞ
u0ðW0ð1 þ rÞÞ ;
and so ~u1 1 1.
The Arrow–Pratt measure of absolute risk aversion, rAP, is defined by
rAP ¼ ~u2 ¼  u00ðW0ð1 þ rÞÞ
u0ðW0ð1 þ rÞÞ ;
ð9:81Þ
and named for Kenneth J. Arrow (b. 1921) and John W. Pratt (b. 1931). Since
u0ðW0ð1 þ rÞÞ > 0, this measure of risk aversion is positive for a risk-averter, nega-
tive for a risk-seeker, and identically zero for a risk-neutral investor. Moreover a
larger positive rAP implies greater risk aversion, and a more negative rAP implies
greater risk seeking, as will be seen below.
Taking expected values, we derive
E½~uðW0ð1 þ rÞ þ IðX  rÞÞ ¼
X
y
k¼1
1
k! ~ukI kE½ðX  rÞk:
ð9:82Þ
Using only the first two terms of this series,
E½~uðW0ð1 þ rÞ þ IðX  rÞÞAIE½ðX  rÞ  I 2rAP
2
E½ðX  rÞ2;
ð9:83Þ
and an optimum value of I can be found for a risk-averse investor, where by opti-
mum is meant utility maximizing.
Letting f2ðIÞ denote the right-hand side of (9.83) as a function of I, we derive
f 0
2 ðIÞ ¼ E½ðX  rÞ  IrAPE½ðX  rÞ2;
f 00
2 ðIÞ ¼ rAPE½ðX  rÞ2:
So this expected utility function has a critical point at
I0 ¼
E½ðX  rÞ
rAPE½ðX  rÞ2
;
ð9:84Þ
which will be a relative maximum if f 00
2 ðI0Þ < 0.
For a risk-averse investor, with rAP > 0, or equivalently u00ðW0ð1 þ rÞÞ < 0, I0 is
always a relative maximum of the expected utility. If E½ðX  rÞ > 0, the typical case
530
Chapter 9
Calculus I: Di¤erentiation

for risky assets, then I0 > 0, and such an investor will go long to maximize expected
utility. If E½ðX  rÞ < 0, this investor will short the risky asset, since then I0 < 0.
Note that in either case, as the Arrow–Pratt measure increases, this investor will go
long less (respectively, short less) to obtain the optimum utility.
For a risk-seeker, with rAP < 0, or equivalently u00ðW0ð1 þ rÞÞ > 0, I0 is always a
relative minimum of the expected utility. This is logical since in this case, considered
as a function of I, the expression in (9.83) is of the form gðIÞ ¼ aI þ bI 2, with b > 0,
and so utility is only maximized at the endpoints of whatever interval for I is
allowed. In other words, a risk-seeker will maximize utility by comparing a long po-
sition with maximal leverage, to the maximal short position in the risky asset, and
choose the option with greater utility.
The value of the expected utility function at I0 is given by
E½~uðW0ð1 þ rÞ þ I0ðX  rÞÞ ¼
E½ðX  rÞ2
2rAPE½ðX  rÞ2
:
This maximum expected utility can be equivalently expressed in terms of the Sharpe
ratio developed by William F. Sharpe (b. 1934):
E½~uðW0ð1 þ rÞ þ I0ðX  rÞÞ ¼
s2
2rAP
;
ð9:85Þ
where the Sharpe ratio is defined by
s ¼
E½ðX  rÞ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
E½ðX  rÞ2
q
:
ð9:86Þ
Remark 9.154
The significance of the Sharpe ratio is that for every risk-averse inves-
tor, optimal utility in (9.85) can be increased by choosing the risky asset with the larg-
est Sharpe ratio.
When r is assumed constant, maximizing s is equivalent to maximizing
s0 ¼ m  r
s
;
ð9:87Þ
where m and s are the mean and standard deviation of X. This follows since X  r ¼
ðX  mÞ þ ðm  rÞ and a calculation produces s ¼
s0
ffiffiffiffiffiffiffiffiffiffiffi
1þðs0Þ2
p
. Consequently s is maxi-
mized when s0 is maximized. The formula in (9.87) is also called the Sharpe ratio.
9.8
Applications to Finance
531

9.8.10
Risk-Neutral Binomial Distribution as Dt ? 0
In section 8.8.2 was shown that the real world binomial model for equity prices con-
verged to the lognormal distribution. Specifically, as defined in (8.46) and repeated
here, let
SðnÞ
T ¼ S0eT Bj;
where
Bj ¼
mDt þ as
ffiffiffiffiffi
Dt
p
;
Pr ¼ p;
mDt  1
a s
ffiffiffiffiffi
Dt
p
;
Pr ¼ p0;
j ¼ 1; 2; . . . ; n;
(
with a ¼
ffiffiffi
p0
p
q
¼
p 0ffiffiffiffiffi
pp 0
p
, and  1
a ¼
pffiffiffiffiffi
pp 0
p
.
Then as Dt ! 0, we have as in (8.50),
ln SðnÞ
T !p Nðln S0 þ mT; s2TÞ;
where we emphasize the real world probability with the notation ‘‘!p’’. With ST
denoting the limiting random variable, this can be equivalently written as in (8.51):
ST ¼ S0eX;
where X @ NðmT; s2TÞ. This is the definition of a lognormal random variable (see
chapter 10 for more details on this distribution).
In this section we investigate the limiting distribution of the same equity prices, but
rather than using the binomial probability p appropriate for real world modeling,
we use the risk-neutral probability q, as is implicitly assumed in the option pricing
formulas in chapters 7 and 8. This limiting distribution is needed for the Black–
Scholes–Merton pricing formulas for European put and call options introduced in
section 8.8.3.
In the next section we investigate the limiting distribution under the special risk
averter probability q, also needed for the Black–Scholes–Merton pricing formulas,
defined in (8.55) by q ¼ qeuerDt, where u ¼ mDt þ as
ffiffiffiffiffi
Dt
p
.
The added complexity in these investigations is the fact that unlike p, the probabil-
ity q, and hence also q, is a function of Dt as noted in (8.52):
qðDtÞ ¼ erDt  edðDtÞ
euðDtÞ  edðDtÞ :
532
Chapter 9
Calculus I: Di¤erentiation

Here r is the assumed constant risk-free interest rate, and rðDtÞ ¼ rDt is assumed lin-
ear in Dt, while the upstate and downstate equity returns for Bj are again given as
uðDtÞ ¼ mDt þ as
ffiffiffiffiffi
Dt
p
;
dðDtÞ ¼ mDt  1
a s
ffiffiffiffiffi
Dt
p
:
To facilitate this first inquiry, we require a more accessible formula for qðDtÞ that
makes the functional dependence on Dt more manageable.
Analysis of the Risk-Neutral Probability: q(Dt)
The goal of this section is to derive the following expansion:
Proposition 9.155
With qðDtÞ defined as above, we have that
qðDtÞ ¼ p þ r  m  1
2 s2


sffiffiffiffiffi
pp0
p
ffiffiffiffiffi
Dt
p
þ
p  1
2


r  m  s2
6


Dt
þ
ðr  mÞ2 þ ðr  mÞs2
1
6pp 0  1

	
þ s4
12
2sffiffiffiffiffi
pp0
p
2
4
3
5Dt3=2 þ O½Dt2:
ð9:88Þ
First o¤, to investigate the behavior of qðDtÞ as Dt ! 0, we need to do some anal-
ysis, since direct substitution of Dt ¼ 0 leads to 0
0 . Dividing out the common term
edðDtÞ, and then applying (9.35) to each exponential term in this expression produces
qðDtÞ ¼ exp 1
a s
ffiffiffiffiffi
Dt
p
þ ðr  mÞDt


 1
exp
a þ 1
a


s
ffiffiffiffiffi
Dt
p


 1
¼
1
a s
ffiffiffiffiffi
Dt
p
þ
1
2
1
a s

2þðr  mÞ
h
i
Dt þ OðDt3=2Þ
a þ 1
a


s
ffiffiffiffiffi
Dt
p
þ 1
2
a þ 1
a


s

2Dt þ OðDt3=2Þ
:
In this format, we can divide numerator and denominator by the common factor
ffiffiffiffiffi
Dt
p
, substitute Dt ¼ 0 and obtain
qð0Þ ¼
1
a
a þ 1
a
¼ p:
Perhaps surprisingly, as Dt ! 0 the risk-neutral probability converges to p, the real
world probability:
9.8
Applications to Finance
533

qðDtÞ ! p
as Dt ! 0:
It would be entirely justified at this point to expect that this conclusion should im-
ply that the limiting distribution under this risk-neutral probability qðDtÞ is the same
as that derived in chapter 8 for the real world probability p. Quite remarkably, this
expectation will be proved to be false, and we will see that although qðDtÞ ! p, it
does so slowly enough that the limiting distribution of prices is changed from what
was earlier derived.
To see this, we need to complete the analysis of qðDtÞ, in e¤ect by deriving more
terms in its Taylor series than the constant term p. To do this, we could just start
taking derivatives of qðDtÞ, but a moment of reflection will prove it a painful pursuit,
so we explore another approach. An approach that is appealing is based on proposi-
tion 9.116 of section 9.4.2. To this end, let us assume that
qðDtÞ ¼ p þ
X
y
n¼1
qnð
ffiffiffiffiffi
Dt
p
Þn:
ð9:89Þ
Then since both numerator and denominator of the function qðDtÞ are analytic func-
tions of the variable
ffiffiffiffiffi
Dt
p
about
ffiffiffiffiffi
Dt
p
¼ 0, so too is this ratio function qðDtÞ, as
proved in that section.
Remark 9.156
Note that we do not claim that the numerator or denominator of qðDtÞ,
or qðDtÞ itself, are analytic functions of Dt about Dt ¼ 0, which they cannot be since
ffiffiffiffiffi
Dt
p
is not even di¤erentiable at Dt ¼ 0. For example, while f ðxÞ ¼ ex is an every-
where analytic function of x, gðxÞ ¼ e
ffiffix
p
is not even di¤erentiable at x ¼ 0, since
g0ðxÞ ¼
1
2 ffiffix
p e
ffiffix
p
. On the other hand, while not analytic in Dt, all three functions have
absolutely convergent series as functions of
ffiffiffiffiffi
Dt
p
. For example, since the numerator
of qðDtÞ is an analytic function of
ffiffiffiffiffi
Dt
p
, it is absolutely convergent for j
ffiffiffiffiffi
Dt
p
j < R, for
some R, which in this case we know to be R ¼ y. The same is true for the denominator
of qðxÞ, and hence for qðxÞ itself for 0 a
ffiffiffiffiffi
Dt
p
< R0 for some R0 > 0.
To simplify notation, it is appealing to substitute x ¼
ffiffiffiffiffi
Dt
p
, and express qðxÞ as
qðxÞ ¼ expðpdx þ cx2Þ  1
expðdxÞ  1
;
c ¼ r  m;
d ¼
sffiffiffiffiffiffi
pp0
p
:
The Taylor series for numerator and denominator then become
534
Chapter 9
Calculus I: Di¤erentiation

qðxÞ ¼
Py
j¼1
1
j! ðpdx þ cx2Þ j
Py
k¼1
1
k! ðdxÞk
:
Expanding these expressions to Oðx4Þ to put in the format of a ratio of power se-
ries, with rðxÞ and sðxÞ denoting the numerator and denominator, respectively, we
obtain
rðxÞ ¼ ðpdÞx þ
c þ 1
2 d 2p2


x2 þ
cdp þ 1
6 d 3p3


x3 þ Oðx4Þ;
sðxÞ ¼ dx þ 1
2 d 2x2 þ 1
6 d 3x3 þ Oðx4Þ:
The goal is to determine fqng in (9.89) so that
p þ
X
y
n¼1
qnxn
 
!
sðxÞ ¼ rðxÞ;
ð9:90Þ
which we can implement using (6.24). Although algebraically tedious, and prone to
initial missteps, this approach is significantly easier than evaluating the derivatives of
qðxÞ directly as a ratio function.
Alternatively, since qn ¼ qðnÞð0Þ
n!
, we could evaluate the derivatives of qðxÞ indirectly
by di¤erentiating the identity
rðxÞ ¼ qðxÞsðxÞ;
ð9:91Þ
and solving. Specifically, we have by the Leibniz formula in (9.42), that for x in the
interval about 0 for which qðxÞ is analytic and hence infinitely di¤erentiable,
rðnÞðxÞ ¼
X
n
k¼0
n
k


qðkÞðxÞsðnkÞðxÞ:
This can be solved iteratively at x ¼ 0. Then recalling that sð0Þ ¼ 0, we obtain
qð0Þ ¼ r0ð0Þ
s0ð0Þ ;
ð9:92aÞ
qðn1Þð0Þ ¼
1
ns0ð0Þ rðnÞð0Þ 
X
n2
k¼0
n
k


qðkÞð0ÞsðnkÞð0Þ
"
#
;
n b 2;
ð9:92bÞ
and substituting qn ¼ qðnÞð0Þ
n!
into (9.89) will produce the desired result.
9.8
Applications to Finance
535

This is a di¤erent approach only methodologically from what was developed in
(6.24) and not a new approach in theory. Here we developed an iteration for deriva-
tive values of qðxÞ from those of rðxÞ and sðxÞ, and constructed qðxÞ as a Taylor se-
ries. To use (6.24), we would first construct the Taylor series for rðxÞ and sðxÞ, which
reflect these derivatives, and then iteratively generate the coe‰cients of the series for
qðxÞ.
An easy calculation using the definition that sðxÞ ¼ expðdxÞ  1 produces
sðkÞð0Þ ¼ d k;
k b 1:
The function rðxÞ ¼ expðpdx þ cx2Þ  1 is a bit more complicated because of the
quadratic in the exponent, but to four derivatives we have
r0ðxÞ ¼ ðpd þ 2cxÞ expðpdx þ cx2Þ;
r00ðxÞ ¼ ½2c þ ðpd þ 2cxÞ2 expðpdx þ cx2Þ;
rð3ÞðxÞ ¼ ½6cðpd þ 2cxÞ þ ðpd þ 2cxÞ3 expðpdx þ cx2Þ;
rð4ÞðxÞ ¼ ½12c2 þ 12cðpd þ 2cxÞ2 þ ðpd þ 2cxÞ4 expðpdx þ cx2Þ:
Correspondingly,
r0ð0Þ ¼ pd;
r00ð0Þ ¼ 2c þ ðpdÞ2;
rð3Þð0Þ ¼ 6cdp þ ðpdÞ3;
rð4Þð0Þ ¼ 12c2 þ 12cðpdÞ2 þ ðpdÞ4:
Substituting into (9.92), we get
qð0Þ ¼ p;
q0ð0Þ ¼
1
2s0ð0Þ ½rð2Þð0Þ  qð0Þð0Þsð2Þð0Þ
¼ c
d  dpp0
2
;
536
Chapter 9
Calculus I: Di¤erentiation

q00ð0Þ ¼
1
3s0ð0Þ rð3Þð0Þ 
X
1
k¼0
3
k


qðkÞð0Þsð3kÞð0Þ
"
#
¼ 2
p  1
2


c  d 2pp0
6


;
qð3Þð0Þ ¼
1
4s0ð0Þ rð4Þð0Þ 
X
2
k¼0
4
k


qðkÞð0Þsð4kÞð0Þ
"
#
¼ 3c2
d þ 3cd 1
6  pp0


þ 1
4 ðpp0Þ2d 3:
Recalling that qn ¼ qðnÞð0Þ
n!
, c ¼ r  m, and d ¼
sffiffiffiffiffi
pp0
p
, we obtain the final result in (9.88)
after a bit more algebra.
Of course, ~qðDtÞ 1 1  qðDtÞ, needed below, is easily developed from this expres-
sion by replacing p with p0 and changing the sign of all other coe‰cients from posi-
tive to negative.
Notation 9.157
Note that we use ~qðDtÞ to denote the complementary probability of
qðDtÞ, whereas in other applications the complement of p was denoted p0. The notation
q0ðDtÞ will be avoided for this purpose because of the confusion it would cause with the
standard notation for the derivative of qðDtÞ.
Remark 9.158
In remark 8.31 was discussed the relationship between the choice of
the real world probability of an upstate, denoted p, and the speed of convergence of
the distribution of binomial lattice prices to the normal distribution in (8.50). There it
was concluded that p ¼ 1=2 provided faster convergence by changing the error term in
the development from Oðn1=2Þ to Oðn1Þ. Because the risk neutral probabilities are
also functions of Dt ¼ T=n, it is natural to expect that speed of convergence of the bi-
nomial lattice under the risk-neutral probability depends not only on p but also on other
parameters used in the lattice calibration. Indeed (9.88) indicates that qðDtÞ converges
to p relatively slowly, with order of magnitude Oð
ffiffiffiffiffi
Dt
p
Þ ¼ Oðn1=2Þ. But it is also ap-
parent that if a lattice is to be developed only for option pricing, then choosing m ¼
r  s2=2 causes qðDtÞ to converge to p with order of magnitude OðDtÞ ¼ Oðn1Þ. If
additionally we select p ¼ 1=2, the convergence improves to OððDtÞ3=2Þ ¼ Oðn3=2Þ.
Of course, choosing p ¼ 1=2 is harmless, but choosing m ¼ r  s2=2 does not provide
a lattice that will, in general, be useful for real world stock price modeling. But this
9.8
Applications to Finance
537

calibration is often used in practice for option pricing because it accelerates option
price convergence as a function of Dt. And this choice is further justified by the obser-
vation that in the limit of the Black–Scholes–Merton option-pricing formulas, the real
world parameter m plays no role in any case, as noted in remark 8.34 of section 8.8.3,
so we are justified to choose this value at will. Of course, if the goal is to produce a re-
alistic stock price lattice for real world modeling and option pricing, one must choose a
realistic m and tolerate the fact that option prices will converge more slowly as Dt ! 0.
Risk-Neutral Binomial Distribution as Dt ? 0
We are now in a position to investigate the limiting distribution of the binomial
model under the risk-neutral probabilities. First o¤, with the analogous setup from
chapter 8 in (8.46), we define
SðnÞ
T ¼ S0eT Bj;
where for j ¼ 1; 2; . . . ; n,
Bj ¼
uðDtÞ 1 mDt þ as
ffiffiffiffiffi
Dt
p
;
Pr ¼ qðDtÞ;
dðDtÞ 1 mDt  1
a s
ffiffiffiffiffi
Dt
p
;
Pr ¼ 1  qðDtÞ;
(
with a ¼
ffiffiffi
p0
p
q
¼
p 0ffiffiffiffiffi
pp 0
p
,  1
a ¼
pffiffiffiffiffi
pp0
p
and qðDtÞ ¼ e rDte dðDtÞ
e uðDtÞe dðDtÞ .
The goal of this section is to prove the following:
Proposition 9.159
With SðnÞ
T
and qðDtÞ defined as above, then as Dt ! 0, in contrast
to (8.50),
ln SðnÞ
T
S0
"
#
!q ln ST
S0


@ N
r  1
2 s2


T; s2T


;
ð9:93aÞ
or
ln SðnÞ
T !q ln ST @ N
ln S0 þ
r  1
2 s2


T; s2T


;
ð9:93bÞ
where the limit symbol ‘‘!q’’ is used to emphasize the dependence of this result on the
risk-neutral probability structure.
With ST denoting the limiting random variable, this can be equivalently written as
ST ¼ S0eX;
ð9:94Þ
538
Chapter 9
Calculus I: Di¤erentiation

where X @ N
r  1
2 s2


T; s2T


. So ST satisfies the definition of a lognormal random
variable (see chapter 10 for more details on this distribution).
This is truly a remarkable result when contrasted with the limits under the real
world probability p stated in proposition 8.30. Of course, it may not seem remark-
able that changing the binomial probability from p to qðDtÞ changes the moments of
the limiting distribution of ln½ST=S0, here from NðmT; s2TÞ to N r  1
2 s2


T; s2TÞ.
What is remarkable is that as seen above, this change occurs despite the fact that
qðDtÞ ! p as Dt ! 0.
As a first step in the investigation, we first note that under qðDtÞ, using (9.88),
E ln StþDt
St




¼
r  1
2 s2


Dt þ O½Dt3=2;
ð9:95aÞ
Var ln StþDt
St




¼ s2Dt þ O½Dt3=2:
ð9:95bÞ
This derivation is assigned in exercise 24 below. So even with this relatively simple
calculation it is apparent that despite the fact that qðDtÞ ! p as Dt ! 0, this conver-
gence occurs in a way that introduces a permanent shift in the mean of this distribu-
tion compared to the earlier result.
To now demonstrate the result on the limiting distribution, we again resort to a
moment-generating function argument. Because of the e¤ect qðDtÞ has on the mean
of the distribution, there is no benefit in attempting to parallel the development in
section 8.8.2 in which we worked with the normalized random variable Y ðnÞ rather
than the actual random variable BðnÞ ¼ Pn
j¼1 Bj 1 ln½SðnÞ
T =S0. There, with Y ðnÞ we
could eliminate the Dt-terms and only work with simplified
ffiffiffiffiffi
Dt
p
-terms of Bj. Here,
the normalized variable is actually more di‰cult to work with than the original ran-
dom variable, so we work directly with BðnÞ.
For the moment-generating function of BðnÞ, first note that with a ¼
ffiffiffi
p 0
p
q
¼
p0ffiffiffiffiffi
pp 0
p
,
 1
a ¼
pffiffiffiffiffi
pp 0
p
and d ¼
sffiffiffiffiffi
pp 0
p
as in the qðDtÞ analysis above,
MBjðsÞ ¼ emsDt
qðDtÞeass ffiffiffi
Dt
p
þ ~qðDtÞeðss ffiffiffi
Dt
p
Þ=a	
¼ emsDt
qðDtÞedsp 0 ffiffiffi
Dt
p
þ ~qðDtÞedsp ffiffiffi
Dt
p 	
;
where ~qðDtÞ 1 1  qðDtÞ. Because the fBjg are independent and identically distrib-
uted, MBðnÞðsÞ ¼ Qn
j¼1 MBjðsÞ, and so since nDt ¼ T,
9.8
Applications to Finance
539

MBðnÞðsÞ ¼ emTs
qðDtÞedsp 0 ffiffiffi
Dt
p
þ ~qðDtÞedsp ffiffiffi
Dt
p 	T=Dt
:
The goal is to show that
MBðnÞðsÞ ! eðrs2=2ÞTsþðs2Ts2Þ=2:
The challenge here is to evaluate
lim
Dt!0

qðDtÞedsp 0 ffiffiffi
Dt
p
þ ~qðDtÞedsp ffiffiffi
Dt
p 	1=Dt
:
Since f ðyÞ ¼ yT is a continuous function for T b 0, if it is shown that yðDtÞ ! y0 as
Dt ! 0, where
yðDtÞ 1

qðDtÞedsp 0 ffiffiffi
Dt
p
þ ~qðDtÞedsp ffiffiffi
Dt
p 	1=Dt
;
then f ðyðDtÞÞ ! f ðy0Þ, so we can exponentiate this limit after it is evaluated. This
limit of yðDtÞ can in turn be evaluated by working with zðDtÞ 1 ln yðDtÞ, since
gðyÞ ¼ ey is continuous, and hence, if zðDtÞ ! z0, then yðDtÞ ¼ ezðDtÞ ! ez0 ¼ y0.
Working with zðDtÞ, which we express for notational simplicity as zðxÞ, we have
zðxÞ ¼
ln

qðxÞedsp0 ffiffix
p
þ ~qðxÞedsp ffiffix
p 	
x
;
and the goal is to determine limx!0 zðxÞ. Note that by reversing the above sequence
of steps, we have
MBðnÞðsÞ ¼ emTsh
ezð0ÞiT
:
So once z0 1 limx!0 zðxÞ is determined, we will conclude from the continuity of the
exponential and power functions that
MBðnÞðSÞ ! emTsþz0T:
ð9:96Þ
Of course, in order for the claim above in (9.93) to be validated by this derivation,
we must show that
z0 ¼
r  m  1
2 s2


s þ 1
2 s2s2:
ð9:97Þ
The details are a bit messy, and provided below for completeness.
540
Chapter 9
Calculus I: Di¤erentiation

*Details of the Limiting Result
To derive (9.97), note that with
AðxÞ 1 qðxÞedsp 0 ffiffix
p
þ ~qðxÞedsp ffiffix
p
;
where d ¼
sffiffiffiffiffi
pp0
p
:
1. AðxÞ is continuous on x b 0 and Að0Þ ¼ 1.
2. The series expansions of the 4 functions in the definition of AðxÞ are absolutely
convergent for some interval, 0 a x < R0 for s ¼ 1 as noted in the remark 9.156 fol-
lowing (9.89), and hence this remains true for 0 a s a 1. Consequently the series ex-
pansion for AðxÞ can be developed by manipulating these series, and rearranging as
desired (recall the section 6.1.4 discussion on rearrangements of absolutely conver-
gent series).
3. Because of item 1, for any  > 0 there is a d so that if 0 a x < d, we have that
jAðxÞ  1j < . So we let  ¼ 1
2 , say, and conclude that AðxÞ ¼ 1 þ BðxÞ, where
jBðxÞj < 1
2 for 0 a x < d. As a small technicality, we only consider 0 a x < R0, with
R0 defined in item 2 above if R0 < d.
4. By item 2, the series expansion for BðxÞ is also absolutely convergent for 0 a x <
minðd; R0Þ.
We now complete the derivation of this section’s result by the proof of two claims.
Claim 9.160
If AðxÞ ¼ 1 þ x½z0 þ CðxÞ, where CðxÞ has an absolutely convergent
series expansion on 0 a x < minðd; R0Þ, with Cð0Þ ¼ 0, then
lim
x!0 zðxÞ ¼ z0:
Proof
Because zðxÞ ¼ 1
x ln½AðxÞ ¼ 1
x ln½1 þ xðz0 þ CðxÞÞ, and jxðz0 þ CðxÞÞj ¼
jBðxÞj < 1
2 for 0 a x < minðd; R0Þ by item 3 above, the power series for lnð1 þ yÞ
can be utilized, and this is an absolutely convergent series:
ln½1 þ xðz0 þ CðxÞÞ ¼
X
y
j¼1
ð1Þ jþ1x jðz0 þ CðxÞÞ j
j
¼ xðz0 þ CðxÞÞ þ x2 X
y
j¼2
ð1Þ jþ1x j2ðz0 þ CðxÞÞ j
j
:
Consequently
9.8
Applications to Finance
541

zðxÞ ¼ ðz0 þ CðxÞÞ þ x
X
y
j¼2
ð1Þ jþ1x j2ðz0 þ CðxÞÞ j
j
:
Since Cð0Þ ¼ 0, we conclude that zðxÞ ! z0 as x ! 0 as claimed.
n
We now show that AðxÞ has the required properties with z0 as given in (9.97) and,
hence by (9.96), will complete the proof of (9.93).
Claim 9.161
AðxÞ ¼ 1 þ x
r  m  1
2 s2


s þ 1
2 s2s2 þ CðxÞ


, where CðxÞ has an ab-
solutely convergent series expansion on 0 a x < minðd; R0Þ, with Cð0Þ ¼ 0.
Proof
With AðxÞ 1 qðxÞedsp 0 ffiffix
p
þ ~qðxÞedsp ffiffix
p
, we have, since qðxÞ þ ~qðxÞ ¼ 1,
AðxÞ ¼ 1 þ qðxÞðedsp0 ffiffix
p
 1Þ þ ~qðxÞðedsp ffiffix
p
 1Þ
¼ 1 þ
X
y
i¼0
qixi=2 X
y
j¼1
ðdsp0Þ jx j=2
j!
þ
X
y
i¼0
~qixi=2 X
y
j¼1
ðdspÞ jx j=2
j!
;
where all series are absolutely convergent for 0 a x < minðd; R0Þ as noted above.
Here fqig are defined as in (9.89) using (9.88) and f~qig are defined as the correspond-
ing coe‰cients for ~qðxÞ. Consequently
~q0 ¼ 1  q0 ¼ p0;
~qi ¼ qi;
i b 1:
Each of these two series products in the expansion of AðxÞ can be expanded as in
(6.22) and (6.23), and combined to produce
AðxÞ ¼ 1 þ
X
y
n¼1
ðdn þ ~dnÞxn=2;
with
dn ¼
X
n
k¼1
qnk
ðdsp0Þk
k!
;
~dn ¼
X
n
k¼1
~qnk
ðdspÞk
k!
:
The claim will be complete by now showing that d1 þ ~d1 ¼ 0 and d2 þ ~d2 ¼
r  m  1
2 s2


s þ 1
2 s2s2. To this end, recall that d ¼
sffiffiffiffiffi
pp 0
p
,
d1 þ ~d1 ¼ q0ðdsp0Þ þ ~q0ðdspÞ
¼ pðdsp0Þ  p0ðdspÞ ¼ 0:
542
Chapter 9
Calculus I: Di¤erentiation

Also, since q1 ¼ ½rmðs2=2Þ
s=
ffiffiffiffiffi
pp 0
p
by (9.88),
d2 þ ~d2 ¼ q1ðdsp0Þ þ ~q1ðdspÞ þ q0
ðdsp0Þ2
2
þ ~q0
ðdspÞ2
2
¼ q1ds þ 1
2 d 2pp0s2
¼
r  m  1
2 s2


s þ 1
2 s2s2:
n
Putting this all together, we have from (9.96) and the above claims that
MBðnÞðSÞ ! emTsþðrmð1=2Þs2ÞTsþð1=2Þs2Ts2
¼ eðrð1=2Þs2ÞTsþð1=2Þs2Ts2:
In other words, as in (9.93),
BðnÞ 1 ln SðnÞ
T
S0
"
#
!q N
r  1
2 s2


T; s2T


:
*9.8.11
Special Risk-Averter Binomial Distribution as Dt ? 0
Fortunately, we do not need to repeat the long section above to determine the other
limiting distribution needed for the Black–Scholes–Merton pricing formulas for Eu-
ropean put and call options as noted in section 8.8.3. We simply need to adapt the
work above to this modified situation.
Analysis of the Special Risk-Averter Probability: q(Dt)
Because qðDtÞ ¼ qðDtÞeuðDtÞerDt, we can relatively easily determine the series expan-
sion for qðDtÞ from the series expansion for qðDtÞ given in (9.88), and the series ex-
pansion for euðDtÞrDt. This derivation is possible because each of these series is
absolutely convergent for 0 a Dt < R for some R > 0. So we can multiply, using the
section 6.3.1 results on multiplying series in (6.22) and (6.23), and rearrange summa-
tions at will. Consequently, as will be needed below, the series for qðDtÞ is also abso-
lutely convergent.
The goal of this section is to derive the following expansion:
Proposition 9.162
With qðDtÞ defined as above, we have that
9.8
Applications to Finance
543

qðDtÞ ¼ p þ r  m þ 1
2 s2


s=
ffiffiffiffiffiffi
pp0
p
ffiffiffiffiffi
Dt
p
þ
p  1
2


r  m  7s2
6


 p2 r  m þ 1
2 s2




Dt
þ O½Dt3=2:
ð9:98Þ
Denoting the coe‰cients of the qðDtÞ series as fqig as above, and the correspond-
ing coe‰cients of the qðDtÞ series by fqig, we have from qðDtÞ ¼ qðDtÞeuðDtÞerDt that
X
y
n¼0
qnðDtÞn=2 ¼
X
y
k¼0
qkðDtÞk=2 X
y
j¼0
½cDt þ dp0
ffiffiffiffiffi
Dt
p
 j
j!
:
Here, as in the development of (9.88), we use the simplifying notation c ¼ r  m and
d ¼
sffiffiffiffiffi
pp 0
p
. If each of these series is then expanded, (6.23) can be applied to derive the
needed qi-terms.
Knowing from the proof of the second claim for the qðDtÞ analysis that we only
require this expansion up to the
ffiffiffiffiffi
Dt
p
, but calculating the Dt term for good measure,
we derive
X
y
k¼0
qkðDtÞk=2 ¼ q0 þ q1
ffiffiffiffiffi
Dt
p
þ q2Dt þ    ;
X
y
j¼0
½cDt þ dp0
ffiffiffiffiffi
Dt
p
 j
j!
¼ 1 þ dp0
ffiffiffiffiffi
Dt
p
þ
c þ 1
2 ðdp0Þ2


Dt þ    ;
and so
q0 ¼ q0;
q1 ¼ q1 þ q0dp0;
q2 ¼ q2 þ q1dp0 þ q0 c þ 1
2 ðdp0Þ2


:
Implementing the necessary algebra with the coe‰cients from (9.88), recalling
c ¼ r  m and d ¼
sffiffiffiffiffi
pp 0
p
, produces (9.98).
544
Chapter 9
Calculus I: Di¤erentiation

Special Risk-Averter Binomial Distribution as Dt ? 0
We are now in a position to derive the limiting distribution of the binomial model
under the special risk-averter probabilities. Specifically, we begin with the analogous
setup to that above for the risk-neutral analysis:
SðnÞ
T ¼ S0eT Bj;
where for j ¼ 1; 2; . . . ; n,
Bj ¼
uðDtÞ 1 mDt þ as
ffiffiffiffiffi
Dt
p
;
Pr ¼ qðDtÞ;
dðDtÞ 1 mDt  1
a s
ffiffiffiffiffi
Dt
p
;
Pr ¼ 1  qðDtÞ;
(
with qðDtÞ ¼ qðDtÞeuðDtÞerDt, a ¼
ffiffiffi
p 0
p
q
¼
p0ffiffiffiffiffi
pp 0
p
, and  1
a ¼
pffiffiffiffiffi
pp 0
p
.
The goal of this section is to prove the following:
Proposition 9.163
With SðnÞ
T
and qðDtÞ defined as above, then as Dt ! 0, in contrast
to both (8.50) and (9.93):
ln SðnÞ
T
S0
"
#
!q ln ST
S0


@ N
r þ 1
2 s2


T; s2T


;
ð9:99aÞ
or
ln SðnÞ
T !q ln ST @ N
ln S0 þ
r þ 1
2 s2


T; s2T


;
ð9:99bÞ
where the limit symbol ‘‘!q’’ is used to emphasize the dependence of this result on the
special risk-averter probability structure.
With ST denoting the limiting random variable, this can be equivalently written as
ST ¼ S0eX;
ð9:100Þ
where X @ N
r þ 1
2 s2


T; s2T


. So once again, ST has a lognormal distribution, as
defined and studied in chapter 10.
As a first step in the investigation, we note that under qðDtÞ, using (9.98),
E ln StþDt
St




¼
r þ 1
2 s2


Dt þ O½Dt3=2;
ð9:101aÞ
Var ln StþDt
St




¼ s2Dt þ O½Dt3=2:
ð9:101bÞ
9.8
Applications to Finance
545

This derivation is assigned in exercise 48 below. So even with this relatively simple
calculation, it is apparent that even though qðDtÞ ! p and qðDtÞ  qðDtÞ ! 0 as
Dt ! 0, this convergence occurs slowly enough to cause a di¤erent permanent shift
in the mean of this distribution compared to the earlier results in sections 8.8.2 and
9.8.10.
Details of the Limiting Result
For the limiting result, a moment of review in the risk-neutral case will confirm that
there was only one step in that long derivation where the series for qðDtÞ actually
mattered, and that was in the derivation of the second claim at the end of the section,
in which the z0 needed in (9.97) was derived. We state the modified second claim
here, with all notation the same as before.
Claim 9.164
With AðxÞ defined by AðxÞ 1 qðxÞedsp 0 ffiffix
p
þ ~qðxÞedsp ffiffix
p
, where ~qðxÞ ¼
1  qðxÞ, then AðxÞ ¼ 1 þ x
r  m þ 1
2 s2


s þ 1
2 s2s2 þ CðxÞ


, where CðxÞ has an ab-
solutely convergent series expansion on 0 a x < minðd; R0Þ, with Cð0Þ ¼ 0.
Proof
The derivation that AðxÞ ¼ 1 þ Py
n¼1ðdn þ ~dnÞxn=2 is identical to that above,
with the series coe‰cients in (9.98), qi, replacing those from (9.88), qi. That is,
AðxÞ ¼ 1 þ qðxÞðedsp0 ffiffix
p
 1Þ þ ~qðxÞðedsp ffiffix
p
 1Þ
¼ 1 þ
X
y
i¼0
qixi=2 X
y
j¼1
ðdsp0Þ jx j=2
j!
þ
X
y
i¼0
~qixi=2 X
y
j¼1
ðdspÞ jx j=2
j!
¼ 1 þ
X
y
n¼1
ðdn þ ~dnÞxn=2:
Here
dn ¼
X
n
k¼1
qnk
ðdsp0Þk
k!
;
~dn ¼
X
n
k¼1
~qnk
ðdspÞk
k!
:
The only steps of the proof that di¤er and need to be checked relate to the first 2
terms of the series. For example,
d1 þ ~d1 ¼ 0
because q0 ¼ q0 ¼ p, and d ¼
sffiffiffiffiffi
pp0
p
. Also
546
Chapter 9
Calculus I: Di¤erentiation

d2 þ ~d2 ¼ q1ds þ 1
2 d 2pp0s2
¼
r  m þ 1
2 s2


s þ 1
2 s2s2;
which follows from q1 ¼
rmþ1
2s2
½

s=
ffiffiffiffiffi
pp0
p
.
n
9.8.12
Black–Scholes–Merton Option-Pricing Formulas II
We began the derivation of the famous Black–Scholes–Merton pricing formulas for
European put and call options in section 8.8.3. For a T-period European call on an
equity S, with a strike price of K, it was derived that the price at time 0, defined as
the price of a replicating portfolio on a binomial lattice with Dt ¼ T
n , is given in the
equation preceding (8.56) by
L0ðS0Þ ¼ S0 Pr BðnÞ b ln K
S0




 erTK Pr BðnÞ b ln K
S0




:
Recall than BðnÞ ¼ Pn
i¼1 Bi in the Binðq; nÞ model, where fBig are i.i.d. binomials
and have upstate and downstate values of uðDtÞ and dðDtÞ with special risk-averter
probabilities qðDtÞ and 1  qðDtÞ, respectively, and BðnÞ is identically defined in the
Binðq; nÞ model, but with the risk-neutral probability q 1 qðDtÞ.
The proofs in the prior two sections show that BðnÞ ! N
r þ 1
2 s2


T; s2T


and
that BðnÞ ! N
r  1
2 s2


T; s2T


. Consequently, with Z1 and Z2 denoting these nor-
mal variates, and FðzÞ the unit normal cumulative distribution function,
Pr BðnÞ b ln K
S0




! Pr Z1 b ln K
S0




¼ 1  F
ln K
S0
h i
 r þ 1
2 s2


T
s
ffiffiffiffi
T
p
0
@
1
A
¼ F
ln S0
K
h i
þ r þ 1
2 s2


T
s
ffiffiffiffi
T
p
0
@
1
A;
where the last step follows from the symmetry of the normal distribution, which
implies that 1  FðzÞ ¼ FðzÞ.
9.8
Applications to Finance
547

Similarly
Pr BðnÞ b ln K
S0




! Pr Z2 b ln K
S0




¼ F
ln S0
K
h i
þ r  1
2 s2


T
s
ffiffiffiffi
T
p
0
@
1
A:
Combining results, we have derived the Black–Scholes–Merton pricing formula for a
European call option:
LC
0 ðS0Þ ¼ S0Fðd1Þ  erTKFðd2Þ;
ð9:102aÞ
d1 ¼ ln S0
K þ r þ 1
2 s2


T
s
ffiffiffiffi
T
p
;
ð9:102bÞ
d2 ¼ ln S0
K þ r  1
2 s2


T
s
ffiffiffiffi
T
p
:
ð9:102cÞ
A European put option is now easy to price. While the payo¤ function at expiry
for a call is
LCðSTÞ ¼ maxðST  K; 0Þ;
ð9:103Þ
for a put option we have
LPðSTÞ ¼ maxðK  ST; 0Þ:
ð9:104Þ
Consequently the payo¤ function for a portfolio that includes a short put and a long
call is
LCðSTÞ  LPðSTÞ ¼ ST  K:
In other words, this portfolio has value equal to ST  K at time T, which means is
can be replicated by a portfolio of one long share, and a short position in a T-bill
that matures for K. Consequently the price of this options portfolio at t ¼ 0 equals
the price of this replicating portfolio and therefore satisfies
LC
0 ðS0Þ  LP
0 ðS0Þ ¼ S0  KerT:
ð9:105Þ
548
Chapter 9
Calculus I: Di¤erentiation

This famous identity in prices, forced by this replication argument, is known as put-
call parity.
Exercise 23 assigns the task of deriving the Black–Scholes–Merton pricing formula
for a European put option using put-call parity, the price above of a European call
option, and symmetry properties of the unit normal distribution. The formula with
the same notation as for a call is
LP
0 ðS0Þ ¼ erTKFðd2Þ  S0Fðd1Þ:
ð9:106Þ
Exercises
Practice Exercises
1. For each of the following collections of functions, determine the given composite
functions:
(a) f ðxÞ ¼ xn and gðiÞ ¼ 1 þ i
2 : f ðgðiÞÞ and gðf ðxÞÞ
(b) f ðxÞ ¼ Pn
j¼1 xj and gðiÞ ¼ 1 þ i
2: f ðgðiÞÞ and gð f ðxÞÞ
(c) f ðxÞ ¼ erx, gðyÞ ¼ ln y, hðzÞ ¼ Pn
j¼1 z j: f  g  hðzÞ, g  f  hðzÞ and f  h  gðyÞ
2. Demonstrate that the following functions are continuous at the given points.
(Hint: Demonstrate directly or make use of the propositions on combining known
continuous functions.)
(a) rðiÞ ¼ ð1 þ iÞ2 for all i A R.
(b) sðiÞ ¼ ð1 þ iÞn for all i A R, where n A N.
(c) f ðxÞ ¼ ð1 þ xÞn for all x > 1, where n A N.
(d) gðzÞ ¼ PN
j¼0 bjz j for z A R, where bj A R, N A N.
(e) aðiÞ ¼
1ð1þiÞn
i
;
i > 1; i 0 0
n;
i ¼ 0
(
where n A N. (Hint: Consider ð1 þ iÞnaðiÞ and
recall the binomial theorem.)
3. Demonstrate that the following functions are not continuous as indicated:
(a) f ðxÞ ¼
sin 1
x ;
x 0 0;
0;
x ¼ 0;
is not continuous at x ¼ 0:

(b) gðyÞ ¼
1;
x b 3;
1;
x < 3,
is not continuous at y ¼ 3:

4. Of the functions in exercise 2, demonstrate that 2(a), (b), and (d) are uniformly
continuous on ð1; 1, and that 2(c) and (e) are not.
Exercises
549

5. Explicitly write out the definitions of continuous, sequentially continuous, and
uniformly continuous for a function f ðxÞ defined on a metric space ðX; dÞ, and with
range in:
(a) R, under the standard metric
(b) a general metric space ðY; d 0Þ
6. Show that if f ðxÞ and gðxÞ are di¤erentiable at x0, then so is hðxÞ. (Hint: The goal
is to express hðxÞ  hðx0Þ in terms of f ðxÞ  f ðx0Þ, gðxÞ  gðx0Þ and other terms that
are easy to work with. Consider (9.10).)
(a) hðxÞ ¼ af ðxÞ G bgðxÞ, and h0ðx0Þ ¼ af 0ðx0Þ G bg0ðx0Þ
(b) hðxÞ ¼ f ðxÞgðxÞ and h0ðx0Þ ¼ f 0ðx0Þgðx0Þ þ f ðx0Þg0ðx0Þ
7. Show that if gðxÞ is di¤erentiable and g0ðxÞ continuous in an open interval con-
taining x0 and g0ðx0Þ 0 0, then there is an interval about x0, say ðx0  a; x0 þ aÞ, for
some a > 0, where gðxÞ is one-to-one. (Hint: Assume g0ðx0Þ > 0, and note that if
limDx!0
gðx0þDxÞgðx0Þ
Dx
¼ g0ðx0Þ > 0, then for  ¼ 1
2 g0ðx0Þ there is a d so that
gðx0 þ DxÞ  gðx0Þ
Dx
 g0ðx0Þ


 < 1
2 g0ðx0Þ;
for jDxj < d. What does this say about gðx0 þ DxÞ  gðx0Þ? Consider also g0ðx0Þ <
0:)
8. Show that da x
dx ¼ ax ln a, for a > 0 follows from the identity: ax ¼ ex ln a. (Hint:
ax ¼ f ðgðxÞÞ with gðxÞ ¼ x ln a and f ðyÞ ¼ ey:Þ
9. Calculate the derivative of the functions in exercise 2, and determine if any restric-
tions are needed on the domains given there.
10. Find the Taylor series expansions for the following functions, and determine
when they converge.
(a) f ðxÞ ¼ ð1 þ xÞ1 with x0 ¼ 0
(b) gðyÞ ¼ ð1  yÞn with y0 ¼ 0
(c) hðzÞ ¼ erz with z0 ¼ 0
11. Confirm where each of the following functions is concave or convex on their
respective domains:
(a) f ðxÞ ¼ ex2, x A R
(b) hðyÞ ¼ ð1 þ yÞn, n a positive integer, y > 1
(c) lðzÞ ¼ lnð1 þ zÞ, z > 1
550
Chapter 9
Calculus I: Di¤erentiation

12. Prove the arithmetic-geometric means inequality. If xi b 0 for all i,
1
n
X
n
i¼1
xi b
Y
n
i¼1
xi
 
!1=n
:
(Hint: The result is apparently true if some xi ¼ 0, so assume all xi > 0. Take loga-
rithms and consider if ln x is a concave or convex function.)
Remark 9.165
When fxig are both positive and negative, this inequality is satisfied
with the collection, fjxijg.
13. Show by considering the product of Taylor series, that for a; b A R: eaxebx ¼
eðaþbÞx. Justify the reordering of these summations to get the intended result. (Hint:
Use the binomial theorem and (9.41).)
14. Show, using a Taylor series expansion, that if f ðxÞ ¼ lnð1 þ xÞ, for x > 1, then
f 0ðxÞ ¼
1
1þx . Justify di¤erentiating term by term as well as the convergence of the
final series to the desired answer.
15. Derive the risk-minimizing allocation between two assets, as well as the resulting
portfolio’s mean return and standard deviation of return:
(a) If m1 ¼ 0:05, s1 ¼ 0:09, m1 ¼ 0:08, s1 ¼ 0:15, r ¼ 0:4
(b) If m1 ¼ 0:05, s1 ¼ 0:09, m1 ¼ 0:08, s1 ¼ 0:15, r ¼ 0:6
(c) If m1 ¼ 0:05, s1 ¼ 0:09, m1 ¼ 0:08, s1 ¼ 0:15, r ¼ 0:8
16. For the exponential ðk ¼ 9  105Þ, quadratic (a ¼ 1, b ¼ 4  106Þ, power
(l ¼ 0:01Þ, and logarithmic ðc ¼ 10;000Þ utility functions, determine the optimal
risky asset allocation between the risk-free asset with r ¼ 0:03 and a risky asset with
m ¼ 0:10 and s ¼ 0:18, where W0 ¼ 100;000. (Hint: See exercise 38.)
17. Calculate the duration and convexity of the following price functions exactly,
and using the approximation formulas with both Di ¼ 0:01, and Di ¼ 0:001. For du-
ration, compare the results of (9.52) with (9.51). Assume 100 par.
(a) 10-year zero coupon bond with a yield of 8% semiannual
(b) 3-year, 6% semiannual coupon bond, with a yield of 7% semiannual.
18. For each of the price functions in exercise 17, compare the prices predicted by
the forward di¤erence duration approximation with Di ¼ 0:01 to those predicted
with the convexity adjustment, again using the convexity approximation with Di ¼
0:01, and then to the exact prices. Do this exercise shifting the original pricing yields
G3%, G2%, G1% , G0.5% , G0.1%.
Exercises
551

19. Prove for a portfolio of fixed income securities with price function given by
PðiÞ ¼
X
n
j¼1
PjðiÞ
that the duration and convexity of the portfolio, assuming PðiÞ 0 0, and PjðiÞ 0 0
for all j, is given by
DðiÞ ¼
X
n
j¼1
wjDjðiÞ;
CðiÞ ¼
X
n
j¼1
wjCjðiÞ;
where wj ¼ PjðiÞ
PðiÞ , and hence Pn
j¼1 wj ¼ 1.
Remark 9.166
It is important to note that you will not need to make an assumption
about the signs of fPjðiÞg to prove this result. So this result applies equally well to long
positions, PjðiÞ > 0, short positions, PjðiÞ < 0, or a mixed portfolio of longs and shorts.
20. Given an asset portfolio of $250 million of duration 6 bonds, and $225 million
of liabilities of duration 4.5, determine the necessary ‘‘target’’ duration for assets to
achieve immunization of surplus in the following cases, as well as the necessary asset
trade. Assume that bonds are homogeneous and can be sold in any amount, and that
cash is to be reinvested in duration 1 assets. (Hint: Surplus is a long portfolio of
assets and a short portfolio of liabilities. See exercise 19.)
(a) Surplus immunization at t ¼ 0
(b) Surplus immunization at t ¼ 2, where Z2ðiÞ is priced at i ¼ 0:03 semiannual
(c) Surplus ratio immunization
21. Using the Black–Scholes–Merton formula for a call option, from (9.102), derive
the Delta of a call option as
DC ¼ Fðd1Þ:
(Hint: This is a challenging calculation. It is seductive to think that because the first
part of the BSM formula is S0Fðd1Þ, that this derivative, dD
dS0 is obvious, but it is not,
since both d1 and d2 are functions of S0 also. Once you have the derivative expres-
sion, see what is needed to achieve the desired answer.)
22. Develop the relationship between an individual’s risk preference and their will-
ingness to insure a given risk, where the indi¤erence equation is
552
Chapter 9
Calculus I: Di¤erentiation

uðW0  PÞ ¼ E½uðW0  XÞ;
with P as the insurance premium and X the risk insured against. In other words, how
is the resulting relationship between P and E½X determined by u00ðxÞ? (Hint: Use
Jensen’s inequality.)
23. Derive the Black–Scholes–Merton pricing formula for a European put option in
(9.106) using put-call parity, and the Black–Scholes–Merton price of a European call
option in (9.102).
24. Investigate the moments of ln½StþDt=St under the risk-neutral probability.
(a) Derive (9.95) using the expansion of qðDtÞ in (9.88). (Hint: Only keep track of the
terms in qðDtÞ and 1  qðDtÞ up to Oð
ffiffiffiffiffi
Dt
p
Þ, since the higher order terms will be part
of the error, O½Dt3=2, as will be confirmed next.)
(b) Demonstrate that this shift in the mean is caused only by the coe‰cient of
ffiffiffiffiffi
Dt
p
in the expansion of qðDtÞ, and that the higher order terms have no e¤ect on these
moments larger than O½Dt3=2.
Assignment Exercises
25. For each of the following collections of functions, determine the given composite
functions:
(a) f ðxÞ ¼ erx and gðzÞ ¼ Pn
j¼1 z j: f ðgðzÞÞ and gðf ðxÞÞ
(b) f ðxÞ ¼ 1
x and gðyÞ ¼ Pn
j¼1 yj: f ðgðyÞÞ and gðf ðxÞÞ
(c) f ðxÞ ¼ 1 þ i
12

x,
gðyÞ ¼ ln y,
hðzÞ ¼ Pn
j¼1
z
j :
f  g  hðzÞ,
g  f  hðzÞ
and
f  h  gðyÞ
26. Demonstrate that the following functions are continuous at the given points.
(Hint: demonstrate directly or make use of the propositions on combining continuous
functions.)
(a) hðxÞ ¼ erx for all x A R, for any r A R.
(b) gðzÞ ¼
1ffiffiffiffi
2p
p
ez2 for all z A R.
(c) hðzÞ ¼ PN
j¼0
bj
z j , where bj A R, N A N, for z > 0.
(d) rðiÞ ¼ m ln 1 þ i
m


for m A N and all i > 1. (Note: rðiÞ is the continuous rate
equivalent to the mthly nominal rate i, as will be studied in chapter 10.)
(e) f ðxÞ ¼ 1
x2 for x 0 0.
27. Demonstrate that the following functions are not continuous as indicated:
(a) iðzÞ ¼
1;
z rational,
1;
z irrational,
is not continuous at any z A R:

Exercises
553

(b) f ðxÞ ¼
n;
x ¼ n A Z,
1
x2 ;
x B Z,
is not continuous at any n A Z except n ¼ 1:

28. Prove that f ðxÞ is continuous at x0 if and only if it is sequentially contin-
uous at x0. (Hint: If continuous, consider the definition in conjunction with def-
inition of xn ! x0. Prove the reverse implication by contradiction, if f ðxÞ is not
continuous. . . .)
29. Of the functions in exercise 26, demonstrate that the functions in (a), and (b) are
uniformly continuous on ð1; 1, that the function in (d) is uniformly continuous on
ð1; 1 only when m > 1, and that the functions in (c) and (e) are not uniformly con-
tinuous on ð0; 1. (Note: The function in (c) is constant and hence uniformly continu-
ous in the trivial case when N ¼ 0, so assume N > 0 for this exercise.)
30. (a) Prove that if f ðxÞ is continuous on a compact set K H X, where ðX; dÞ is a
metric space, then it is uniformly continuous on K. Assume that the range of f ðxÞ is
a general metric space ðY; d 0Þ, or if easier, first consider the case where f : X ! R.
(Hint: First review the chapter proof when X ¼ R:Þ
(b) Show that if f ðxÞ ¼ Py
j¼0 ajðx  x0Þ j is a power series that converges on
I ¼ fx j jx  x0j < Rg;
and if fnðxÞ denotes the partial sum of this series, then fnðxÞ ! f ðxÞ uniformly on
any compact set K H I.
31. Show that if f ðxÞ is an arbitrary function, f : R ! R, then f 1ð ~FÞ ¼
g
f 1ðFÞ
f 1ðFÞ
for any set F H R.
32. Show that if f ðxÞ and gðxÞ are di¤erentiable at x0, then so is hðxÞ. (Hint: The
goal is to express hðxÞ  hðx0Þ in terms of f ðxÞ  f ðx0Þ, gðxÞ  gðx0Þ, and other
terms that are easy to work with. Consider (9.10).)
(a) hðxÞ ¼
1
gðxÞ if gðx0Þ 0 0, and h0ðx0Þ ¼ g 0ðx0Þ
g2ðx0Þ
(b) hðxÞ ¼ f ðxÞ
gðxÞ if gðx0Þ 0 0, and h0ðx0Þ ¼ f 0ðx0Þgðx0Þ f ðx0Þg0ðx0Þ
g2ðx0Þ
33. Calculate the derivative of the functions in exercise 26, and determine if any
restrictions are needed on the domains given there.
34. Prove the Leibniz rule for the nth-derivative of the product of two n-times di¤er-
entiable functions as given in (9.42). Namely, if hðxÞ ¼ f ðxÞgðxÞ, then
hðnÞðxÞ ¼
X
n
k¼0
n
k


f ðkÞðxÞgðnkÞðxÞ;
554
Chapter 9
Calculus I: Di¤erentiation

where
f ð0ÞðxÞ 1 f ðxÞ,
and
similarly
gð0ÞðxÞ 1 gðxÞ.
(Hint:
Use
mathematical
induction.)
35. Find the Taylor series expansions for the following functions, and determine
when they converge:
(a) PðrÞ ¼ D
r with r0 ¼ 0:05.
(b) f ðxÞ ¼ sin x with x0 ¼ 0. (Hint: Use (9.16).)
(c) gðxÞ ¼ cos x with x0 ¼ 0.
(d) Confirm using parts (b) and (c), that in terms of the resulting Taylor series,
eix ¼ cos x þ i sin x;
which is Euler’s formula from (2.5) in chapter 2.
36. Confirm where each of the following functions is concave or convex on their re-
spective domains:
(a) jðwÞ ¼ wr, for r > 0, w b 0
(b) aðuÞ ¼ 1
u , u 0 0
(c) zðvÞ ¼ ev, v A R
37. Show, using a Taylor series expansion, that if f ðxÞ ¼ erx for r > 0, that f 0ðxÞ ¼
rf ðxÞ. Justify di¤erentiating term by term.
38. Derive the Arrow–Pratt measure of absolute risk aversion, rAP, for the exponen-
tial ðk ¼ 9  105Þ, quadratic (a ¼ 1, b ¼ 4  106), power ðl ¼ 0:01Þ, and logarithmic
ðc ¼ 10;000Þ utility functions where r ¼ 0:03 and W0 ¼ 100;000.
39. Using the general formula for the risk of a portfolio in (9.54b), derive the obvi-
ous result that the risk-minimizing allocation between a risky asset and a risk-free
asset is wj ¼ 1 in the risk-free asset.
40. Calculate the duration and convexity of the following price functions exactly,
and using the approximation formulas with both Di ¼ 0:01, and Di ¼ 0:001. For the
duration, compare the results of (9.52) with (9.51). Assume 100 par for part (a), and
a loan of 100 in part (b).
(a) 8% annual dividend preferred stock, with an annual yield of 10%
(b) A 5-year, monthly repayment schedule loan made with a monthly loan rate of
10%, priced with a yield of 12% monthly
41. For each of the price functions in exercise 40, compare the prices predicted by
the forward di¤erence duration approximation with Di ¼ 0:01, to those predicted
with the convexity adjustment, again using the convexity approximation with Di ¼
Exercises
555

0:01, and then to the exact prices. Do this exercise shifting the original pricing yields
G3%, G2%, G1%, G0.5%, G0.1%.
42. Derive the immunizing conditions in (9.73) where Sði0Þ ¼ 0. (Hint: Determine
what conditions ensure that S 0ði0Þ ¼ 0 and S 00ði0Þ > 0:)
43. Given a fixed income hedge fund with asset portfolio of $900 million of duration
4.5 bonds, and $850 million of debt of duration 2.5, determine the necessary ‘‘target’’
duration for assets to achieve immunization of the hedge fund equity in the following
cases, as well as the necessary asset trade. Assume that bonds are homogeneous and
can be sold in any amount, and reinvested in duration 0.25 assets. (Hint: Equity is a
long portfolio of assets and a short portfolio of liabilities. See exercise 19.)
(a) Equity immunization at t ¼ 0
(b) Equity immunization at t ¼ 1, where Z1ðiÞ is priced at i ¼ 0:025 semiannual
(c) Equity ratio immunization
44. Derive the Delta of a put option as priced by the Black–Scholes–Merton for-
mula from (9.106):
DP ¼ Fðd1Þ  1:
(Hint: Consider exercise 21 and put-call parity from (9.105).)
45. Using exercises 21 and 44, calculate the gamma of a put and call option as priced
by the Black–Scholes–Merton formulas, and show that they are the same:
GP=C ¼ F0ðd1Þ
S0s
ffiffiffiffi
T
p
;
where F0 is the derivative of the normal distribution function, which is the normal
density function: F0ðd1Þ ¼ fðd1Þ. (See section 10.5.2.)
46. With the forward value of surplus, StðiÞ, defined as
StðiÞ 1 SðiÞ
ZtðiÞ ;
calculate S 0
tðiÞ and S 00
t ðiÞ, as well as the duration and convexity formulas:
DStði0Þ ¼ DSði0Þ  DZtði0Þ;
C Stði0Þ ¼ C Sði0Þ  C Ztði0Þ  2DZtði0Þ½DSði0Þ  DZtði0Þ:
556
Chapter 9
Calculus I: Di¤erentiation

47. Develop the relationship between an individual’s risk preference and their will-
ingness to engage in a given bet, where the indi¤erence equation is
E½uðW0  L þ YÞ ¼ uðW0Þ;
with L ¼ cost of gamble, and Y ¼ potential payo¤. In other words, how is the result-
ing relationship between L and E½Y determined by u00ðxÞ? (Hint: Use Jensen’s
inequality.)
48. Repeat exercise 24 for the moments of the special risk-averter distribution in
(9.101).
Exercises
557



## Calculus II: Integration

10 Calculus II: Integration
10.1
Summing Smooth Functions
In this chapter we study the earliest conception of the integral, or generalized sum-
mation, of a function as it applies to continuous and certain generalizations of con-
tinuous functions. This approach to integration was first introduced on a rigorous
basis by Bernhard Riemann (1826–1866), who despite his short life was responsible
for a remarkable number of acclaimed mathematical discoveries, many of which
bear his name. Here we also develop the relationship between this integral and deriv-
ative, and explore some of the consequences of this relationship. In the final section,
we explore the strengths and limitations of the Riemann integral. This will serve as
background for the more general integration theories of real analysis.
Remark 10.1
In general, the functions that appear to be addressed in calculus are
real-valued functions of a real variable. In other words, these are functions
f : X ! Y;
where X; Y H R. However, while the assumption that the domain of f ðxÞ is real is
critical, X ¼ Dmnð f Þ H R, there is often no essential di‰culty in assuming f to be a
complex-valued function of a real variable so that the range of f ðxÞ, Y ¼ Rngð f Þ H C.
This generalization is not often needed in finance, and the characteristic function is one
of the few examples in finance where complex-valued functions are encountered.
One reason that Dmnð f Þ H R is critical in the development of calculus is that
we will often utilize the natural ordering of the real numbers. In other words, given
x; y A R with x 0 y, then it must be the case that either x < y or y < x. None of these
proofs would generalize easily to functions of a complex variable where no such order-
ing exists. Indeed it turns out that the calculus of such functions is quite di¤erent and
studied in what is called complex analysis.
Because of the rarity of encountering complex-valued functions of a real variable in
finance, all the statements in this chapter are either silent on the location of Y, or
explicitly assume Y H R. In particular, no e¤ort was made to explicitly frame all
proofs in the general case Y H C, since this overt generality seemed to have little pur-
pose given the objectives of this book.
The applicability of many of the results of calculus to a complex-valued function can
often be justified by splitting the function values into ‘‘real’’ and ‘‘imaginary’’ parts. If
Y H C, we write
f ðxÞ ¼ gðxÞ þ ihðxÞ;
where both gðxÞ and hðxÞ are real valued. For an integration theory, ordering in the
range space matters as will be immediately observed, and so splitting f ðxÞ into ‘‘real’’

and ‘‘imaginary’’ parts, where both gðxÞ and hðxÞ are real valued, is how one must pro-
ceed. The integration theory in this chapter can usually then be applied to f ðxÞ by
applying it separately to gðxÞ and hðxÞ and combining results.
10.2
Riemann Integration of Functions
10.2.1
Riemann Integral of a Continuous Function
The intuitive idea behind the definition of a Riemann integral is that of finding the
‘‘signed area’’ between the graph of a given continuous function f ðxÞ and the x-axis
over the interval ½a; b, where a < b. By ‘‘signed’’ is meant that area above the x-axis
is counted as ‘‘positive’’ area and that below is ‘‘negative’’ area. This is done by first
approximating this area with a collection of non-overlapping rectangles.
For example, splitting the interval ½a; b into n-subintervals of length Dx ¼ ba
n ,
and choosing one point in each subinterval, ~xi A ½a þ ði  1ÞDx; a þ iDx for i ¼ 1;
2; . . . ; n, we can produce an approximation
Signed areaA
X
n
i¼1
f ð~xiÞDx:
Of course, the goal is then to determine conditions on f ðxÞ that assure that this ap-
proximation converges as Dx ! 0, or equivalently as n ! y, and that it converges
independently of how one chooses the ~xi values in the subintervals.
When f ðxÞ is a nonnegative function f ðxÞ b 0, this signed area corresponds with
the usual notion of area. However, for general f ðxÞ, it is important to note that for
functions that are both positive and negative, the integral provides the ‘‘net’’ area be-
tween the function’s graph and x-axis, whereby area above the axis is counted as pos-
itive area and that below as negative. The integral then provides a ‘‘netting’’ of the
two values, which could be positive, negative, or zero.
If we assume that f ðxÞ is a continuous function, then on every closed subinterval,
½a þ ði  1ÞDx; a þ iDx, it attains its maximum value, Mi, and minimum value, mi,
and we can conclude that for any choice of the exixi values,
X
n
i¼1
miDx a
X
n
i¼1
f ð~xiÞDx a
X
n
i¼1
MiDx:
The smaller summation is referred to as a lower Riemann sum, while the larger sum is
correspondingly referred to as an upper Riemann sum. All other summations of this
type are simply called Riemann sums.
560
Chapter 10
Calculus II: Integration

More generally, one can define these summations with respect to an arbitrary par-
tition of the interval ½a; b into subintervals ½xi1; xi:
a ¼ x0 < x1 <    < xn1 < xn ¼ b;
where we again choose exixi A ½xi1; xi and define Dxi ¼ xi  xi1. We obtain
mðb  aÞ a
X
n
i¼1
miDxi a
X
n
i¼1
f ð~xiÞDxi a
X
n
i¼1
MiDxi a Mðb  aÞ;
ð10:1Þ
where Mi and mi denote the maximum and minimum values of the continuous f ðxÞ
on the subinterval ½xi1; xi, while M and m denote these defined on the full interval
½a; b.
Even more generally, if f ðxÞ is not continuous on ½a; b but is bounded, we can
achieve the same set of inequalities by defining Mi, and mi, as the least upper bound,
or l.u.b., and greatest lower bound, or g.l.b., respectively, of f ðxÞ on each subinterval.
Specifically, for i ¼ 1; . . . ; n,
Mi ¼ l:u:b:ff ðxÞ j x A ½xi1; xig
¼ minfy j y b f ðxÞ
for x A ½xi1; xig;
ð10:2Þ
mi ¼ g:l:b:f f ðxÞ j x A ½xi1; xig
¼ maxfy j y a f ðxÞ
for x A ½xi1; xig:
The question of convergence of Riemann sums in the context of a general partition is
now defined in terms of the partition becoming increasingly fine. Specifically, with
m 1 max
1aianfxi  xi1g;
ð10:3Þ
convergence is investigated as m ! 0. The measure m is often referred to as the mesh
size of the partition.
From (10.1) it is clear that both the question of convergence of the Riemann sums,
as well as the independence of these limits from the choice of the exixi values can be
addressed together. Namely both questions can be answered in the a‰rmative if we
can show that the upper and lower Riemann sums converge to the same value as
m ! 0. With this in mind, we have the following definition.
Definition 10.2
f ðxÞ is Riemann integrable on an interval ½a; b if as m ! 0 we have
that
10.2
Riemann Integration of Functions
561

X
n
i¼1
MiDxi 
X
n
i¼1
miDxi
"
#
! 0;
ð10:4Þ
where Mi and mi are defined in (10.2). In this case we define the Riemann integral of
f ðxÞ over ½a; b, by
ð b
a
f ðxÞ dx ¼ lim
m!0
X
n
i¼1
f ð~xiÞDxi;
ð10:5Þ
which exists and is independent of the choice of ~xi A ½xi1; xi by (10.1). The function
f ðxÞ is then called the integrand, and the constants a and b the limits of integration of
the integral.
Remark 10.3
Sometimes, for added clarity, the above integral is called a definite inte-
gral, in contrast to an indefinite integral introduced in section 10.5.2 on the derivative
of an integral.
The following result is central to the theory, but it is not the most general result. It
requires both that f ðxÞ be continuous and that the interval ½a; b be bounded.
Proposition 10.4
If f ðxÞ is continuous on bounded ½a; b, then f ðxÞ is Riemann
integrable.
Proof
Since f ðxÞ must be uniformly continuous on closed and bounded ½a; b by
proposition 9.35, we have that for any  > 0 there is a d so that
j f ðxÞ  f ðx0Þj < 
if jx  x0j < d:
Hence, if the mesh size of a given partition of ½a; b satisfies m a d, then on any
subinterval
jMi  mij < :
The triangle inequality then produces
X
n
i¼1
MiDxi 
X
n
i¼1
miDxi


 a
X
n
i¼1
jMi  mijDxi
< ðb  aÞ;
so the di¤erence between upper and lower summations converges to 0 as  ! 0.
n
562
Chapter 10
Calculus II: Integration

Next a Riemann integral over an interval can in fact be calculated in pieces.
Proposition 10.5
If f ðxÞ is continuous on bounded ½a; b and a < c < b, then
ð b
a
f ðxÞ dx ¼
ð c
a
f ðxÞ dx þ
ð b
c
f ðxÞ dx:
ð10:6Þ
Proof
Clearly, if we choose partitions of the interval ½a; b so that one of the parti-
tion points xi ¼ c, this result is immediate as we simply split the upper and lower
Riemann sums into those applicable to ½a; c and those applicable to ½c; b. More gen-
erally, assume that the point c is within one of the subintervals of a partition. That is,
assume that c A ½xi1; xi. Denoting by M 1
i the l.u.b. of f ðxÞ on ½xi1; c, and M 2
i the
l.u.b. of f ðxÞ on ½c; xi, it is clear that M k
i a Mi, the l.u.b. of f ðxÞ on ½xi1; xi where
k ¼ 1; 2. With analogous notation, mk
i b mi. Hence, with Dx1
i used as notation for
c  xi1, and Dx2
i as notation for xi  c,
½M 1
i  m1
i Dx1
i þ ½M 2
i  m2
i Dx2
i a ½Mi  miDxi;
and hence, as Dxi ! 0, the terms in the Riemann sums that reflect intervals that con-
tain c converge to 0.
n
Remark 10.6
It should be noted that the above proof demonstrated that the terms in
the Riemann sums that reflect intervals that contained c could be discarded since they
converged to 0. In other words, it was demonstrated that for this function, as  ! 0,
ð c
a
f ðxÞ dx !
ð c
a
f ðxÞ dx;
ð10:7aÞ
ð b
cþ
f ðxÞ dx !
ð b
c
f ðxÞ dx:
ð10:7bÞ
This observation provides an easy generalization to the proposition above in the case
where f ðxÞ is only continuous on the bounded open interval ða; bÞ, as long as it is also
bounded there.
Proposition 10.7
If f ðxÞ is continuous and bounded on bounded ða; bÞ, then f ðxÞ is
Riemann integrable on ½a; b. Further, for any 1; 2 ! 0,
ð b
a
f ðxÞ dx ¼
lim
1;2!0
ð b2
a1
f ðxÞ dx:
ð10:8Þ
10.2
Riemann Integration of Functions
563

Proof
Given any partition of the interval ½a; b, say
a ¼ x0 < x1 <    < xn1 < xn ¼ b;
we must prove (10.4). Now, since ½x1; xn1 H ða; bÞ, we conclude that f ðxÞ is contin-
uous and hence Riemann integrable on this interval. Also, since it is bounded, we can
assume that on ða; x1 U ½xn1; bÞ the function f ðxÞ satisfies m a f ðxÞ a M. Finally,
with Dxi ¼ xi  xi1, then as m ! 0,
X
n
i¼1
MiDxi 
X
n
i¼1
miDxi


a
X
n
i¼1
jMi  mijDxi
¼ jM  mj½Dx1 þ Dxn þ
X
n1
i¼2
jMi  mijDxi
! 0:
So f ðxÞ is Riemann integrable on ½a; b. Also, since j f ðxÞj a M 0 on ða; a  1 U
½b  2; bÞ, we have
ð b
a
f ðxÞ dx 
ð b2
a1
f ðxÞ dx


 a M 0ð1 þ 2Þ;
proving (10.8).
n
A useful result in applications is that the Riemann integral of a linear combination
of functions can be easily simplified to integrals of the components summands. In its
simplest form, and one that has an obvious generalization, we have:
Proposition 10.8
If f ðxÞ and gðxÞ are Riemann integrable on ½a; b, then so too is
cf ðxÞ þ dgðxÞ for any c; d A R, and
ð b
a
½cf ðxÞ þ dgðxÞ dx ¼ c
ð b
a
f ðxÞ dx þ d
ð b
a
gðxÞ dx:
ð10:9Þ
Proof
That f ðxÞ and gðxÞ are Riemann integrable on ½a; b implies that each can be
expressed as
564
Chapter 10
Calculus II: Integration

ð b
a
f ðxÞ dx ¼ lim
m!0
X
n
i¼1
f ð~xiÞDxi;
ð b
a
gðxÞ dx ¼ lim
m!0
X
n
i¼1
gð~xiÞDxi;
where m denotes the mesh size of the partition, and f~xig are arbitrary points in the
subintervals of each partition. Now, for any partition and collection of subinterval
points,
X
n
i¼1
½cf ð~xiÞ þ dgð~xiÞDxi ¼ c
X
n
i¼1
f ð~xiÞDxi þ d
X
n
i¼1
gð~xiÞDxi:
Consequently, by taking the limit as m ! 0, we conclude both the integrability of
cf ðxÞ þ dgðxÞ as well as the formula in (10.9).
n
Finally, there is a triangle inequality for Riemann integrals that is useful in many
estimation problems.
Proposition 10.9
If f ðxÞ is continuous on bounded ½a; b, then
ð b
a
f ðxÞ dx


 a
ð b
a
j f ðxÞj dx:
ð10:10Þ
Proof
First o¤, note that if f ðxÞ is continuous on bounded ½a; b, so too is j f ðxÞj,
and hence the second integral is well defined (see exercise 23). Also, if fxng is any
convergent numerical sequence, then
lim
n!y xn


 ¼ lim
n!y jxnj;
since if xn ! x, then by (10.139) in exercise 23, jxnj ! jxj. Using these facts and the
definition of this integral in (10.5), we have by the triangle inequality,
ð b
a
f ðxÞ dx


 ¼ lim
m!0
X
n
i¼1
f ð~xiÞDxi


¼ lim
m!0
X
n
i¼1
f ð~xiÞDxi


10.2
Riemann Integration of Functions
565

a lim
m!0
X
n
i¼1
j f ð~xiÞjDxi
¼
ð b
a
j f ðxÞj dx:
n
Remark 10.10
It is important to note that while f ðxÞ being continuous implies that
j f ðxÞj is continuous, the reverse implication is patently false. A simple example defined
on ½0; 1 is
f ðxÞ ¼
1;
x rational;
1;
x irrational:

Then j f ðxÞj 1 1 and is therefore continuous, but f ðxÞ is not continuous at any point.
10.2.2
Riemann Integral without Continuity
The result that continuous functions are Riemann integrable on closed and bounded
intervals is a good example of mathematical overkill. Just the brevity of the proof
indicates that continuity is a very powerful assumption, and probably far more than
is actually needed to make the Riemann sums converge. The case of continuous func-
tions on infinite intervals will be addressed below as so-called improper integrals.
Here we address the issue of continuity on the bounded interval ½a; b.
Finitely Many Discontinuities
Example 10.11
Define the function
f ðxÞ ¼
x2;
0 a x < 1;
x2 þ 5;
1 a x a 2;

with graph in figure 10.1. Based on the proof of (10.6) above, one could hardly be sur-
prised that f ðxÞ is Riemann integrable, and that
ð 2
0
f ðxÞ dx ¼
ð 1
0
x2 dx þ
ð2
1
ðx2 þ 5Þ dx;
where the first integral is defined by (10.8). As we will see below, this integral sum has
value 23
3 . The formal verification of this splitting reflects the proofs of (10.6) and
(10.8). The central idea was the fact that the terms in the Riemann sums that reflect
the subintervals that contain any given point c could be shown to converge to 0. In point
566
Chapter 10
Calculus II: Integration

of fact, the proof of (10.6) did not utilize the assumption that f ðxÞ was continuous at c,
but only that the function was bounded in each of the partitions’ subintervals that con-
tained c. This boundedness assumption was explicit in the proof of (10.8). The value of
f ðcÞ is entirely irrelevant as long as the function is bounded in an interval about c.
This example easily generalizes to the case of a bounded function f ðxÞ, continuous
on an interval ½a; b except at a finite collection of points f^xjgn
j¼1, that may contain
one or both of the interval endpoints. Such a function is called piecewise continuous
on ½a; b. The proof, as in the example above, simply notes that the terms of the Rie-
mann sums that reflect these points of discontinuity add nothing to the value of the
integral in the limit as m ! 0.
Formalizing this notion:
Definition 10.12
A function f ðxÞ is piecewise continuous on ½a; b if there exists points
a a ^x0 < ^x1 < ^x2 <    < ^xn a b
so that on each open interval, ð^xj1; ^xjÞ, f ðxÞ is bounded and continuous.
Remark 10.13
Depending on the application, one might be distressed that this defini-
tion does not require that f ð^xjÞ is even defined. For the existence of the Riemann inte-
gral we do not need these values to be defined, but only that f ðxÞ is bounded as noted in
Figure 10.1
f ðxÞ ¼
x2;
0 a x < 1
x2 þ 5;
1 a x a 2

10.2
Riemann Integration of Functions
567

the proof of (10.8). However, if one wishes to define values for f ð^xjÞ in this definition,
it would typically be required that f ð^xjÞ is defined as one of the limits: limx!^xþ
j f ðxÞ or
limx!^x
j f ðxÞ.
Of course, the boundedness assumption on f ðxÞ is critical, since this is what limits
the values of Mi and mi in each such interval of the Riemann sum, and is necessary
to support the conclusion that these exceptional terms decrease to 0 as m ! 0. That
is, if ½xij1; xij is any such interval in the partition containing the point of discontinu-
ity ^xj, the associated term of the Riemann sum, for any ~xij A ½xij1; xij satisfies
mijDxij a f ð~xijÞDxij a MijDxij:
Consequently, as Dxij ! 0, so too does f ð~xijÞDxij ! 0, since Mij cannot increase and
mij cannot decrease, as the intervals about the given point of discontinuity decrease.
Notation 10.14
The notation in the above paragraph and in some of what follows is a
bit cumbersome, but necessary. The problem is that each of the exceptional points f^xjg
will be found in one subinterval of every partition which defines a Riemann sum, but not
the same subinterval. So it is inaccurate to claim that ^xj A ½xj1; xj, for instance, since
each ^xj is fixed, yet the number of subintervals in the partition increases with n. So each
^xj will be in a di¤erent subinterval in each partition. So the notation used is ^xj A
½xij1; xij, indicating that ½xij1; xij is one of the partition’s ½xi1; xi subintervals, and
in particular the subinterval that contains ^xj.
In addition to boundedness, another critical assumption in this demonstration of
integrability is that the collection of points of discontinuity f^xjgn
j¼1 was finite, so
that this collection of points could be contained in a collection of partition sub-
intervals f½xij1; xijgn
j¼1, the total lengths of which could be made as small as desired.
Then, despite the fact that Mij  mij n 0 on these subintervals, as in the example
above and figure 10.1, one still has the desired result that these terms will add noth-
ing to the Riemann sum in the limit. This is because the total length of these inter-
vals, PðMij  mijÞDxij, can then be made arbitrarily small as m ! 0 even if Mij  mij
do not decrease to 0.
This discussion leads to the following proposition, which we state without separate
proof, relying on the discussion above and proofs that the reader can formalize. Also
in the next section this result will be further generalized with proof.
Proposition 10.15
Let f ðxÞ be a bounded function, continuous on bounded ½a; b ex-
cept at points f^xjgn
j¼1 H ½a; b written in increasing order. Then f ðxÞ is Riemann inte-
grable on ½a; b. Generalizing (10.6), we have
568
Chapter 10
Calculus II: Integration

ð b
a
f ðxÞ dx ¼
ð ^x1
a
f ðxÞ dx þ
X
n1
j¼1
ð ^xjþ1
^xj
f ðxÞ dx þ
ð b
^xn
f ðxÞ dx;
ð10:11Þ
where the first integral is 0 if a ¼ ^x1, and the last is 0 if ^xn ¼ b. Each integral is to be
interpreted in the sense of (10.8).
*Infinitely Many Discontinuities
The proposition above relied on an important ‘‘covering property’’ of a finite col-
lection of points that is referred to as the property of being a set of measure 0.
The Cantor ternary set in section 4.2 was a set of measure 0. This property means
that this collection of points f^xjgn
j¼1 can be contained in a collection of intervals
f½xij1; xijgn
j¼1, the total lengths of which, P Dxij, can be made as small as desired.
This allows the conclusion that despite the fact that Mij  mij n 0 on ½xij1; xij, the
total contribution to the Riemann sum satisfies
X
ðMij  mijÞDxij ! 0:
This property of being a set of measure 0 is in fact shared by any countable collec-
tion of points. For example, given f^xjgy
j¼1 and any  > 0, the closed intervals
^xj 

2 jþ1 ; ^xj þ

2 jþ1



y
j¼1
have lengths

2 j
n oy
j¼1 and total length Py
j¼1

2 j ¼ . In other words, f^xjgy
j¼1 is a set of
measure 0.
This generalizes to:
Proposition 10.16
If fEjgy
j¼1 is a countable collection of sets of measure 0, then 6 Ej
has measure 0.
Proof
First, we cover each set Ej with intervals of total length 
2 j , which is possible
since Ej has measure 0. Then 6 Ej can be covered by the unions of these covering
intervals, and their total length will be no greater than  as noted above.
n
We now pursue a proposition that identifies how far the arguments above on the
continuity of f ðxÞ can be pushed and still maintain the conclusion of Riemann inte-
grability. This result was proved by Bernhard Riemann. The critical observation is
that if Mi and mi are defined as in (10.2) for a collection of intervals: fðxi1; xiÞg,
where all such intervals contain a given point, x0, then Mi  mi ! 0 as Dxi ! 0 if
10.2
Riemann Integration of Functions
569

and only if f ðxÞ is continuous on x0 1 7ðxi1; xiÞ. This result follows from the defi-
nition of continuity (see exercise 3).
Generalizing this idea, we introduce a convenient notation which measures the
variability of a function on a given interval, as well as its continuity or discontinuity
at a given point.
Definition 10.17
Given an open interval, I ¼ ðxi1; xiÞ, denote by oðx; IÞ, the oscilla-
tion of f ðxÞ on I:
oðx; IÞ ¼ ½Mi  mi;
where Mi and mi are defined as in (10.2) but applied to the open interval I. In addition,
denote by oðxÞ, the oscillation of f ðxÞ at x:
oðxÞ ¼ g:l:b:foðx; IÞg
for all I with x A I:
We also define EN by
EN ¼
x j oðxÞ b 1
N


;
and E 1 6Nb1 EN ¼ fx j oðxÞ > 0g.
By the discussion preceding this definition and exercise 3:
 oðxÞ ¼ 0 if and only if f ðxÞ is continuous at x, and equivalently,
 oðxÞ > 0 if and only if f ðxÞ is discontinuous at x.
Consequently E is the collection of discontinuities if f ðxÞ.
Example 10.18
The function graphed in figure 10.1 has oð1Þ ¼ 5, and oðxÞ ¼ 0 for
all x A ð0; 1Þ U ð1; 2Þ.
We next demonstrate two facts that will be necessary for the proposition below.
Proposition 10.19
The set EN is a closed set for every N. Hence the set of discontinu-
ities of any function is equal to a countable union of closed sets.
Proof
Because a set is closed if and only if it contains all of its limit points, we dem-
onstrate that if x is a limit point of EN, then oðxÞ b 1
N and so x A EN. To this end, if
I is any open interval containing x, I also contains a point x0 A EN by definition of
limit point. Hence, with M and m defined on I by (10.2), we have that M  m b
oðx0Þ since oðx0Þ is the g.l.b. of all such values over all such intervals I. But also
570
Chapter 10
Calculus II: Integration

oðx0Þ b 1
N , since x0 A EN. Since M  m b 1
N for any open interval containing x, the
g.l.b. of such values also satisfies this inequality, and hence oðxÞ b 1
N and x A EN. n
Remark 10.20
1. A set that is the countable union of closed sets is sometimes referred to as an Fs-set,
pronounced ‘‘F-sigma set.’’ The F represents the standard notation for a closed set, as
this notion apparently originated in France with the word ‘‘ferme´,’’ while the ‘‘sigma’’
denotes the French word for summation or ‘‘union’’ of closed sets, ‘‘somme.’’ An Fs-
set can be open, closed or neither as demonstrated by the examples of
1
n ; 1  1
n




,
 1
n ; 1 þ 1
n




, and
1
n ; 1 þ 1
n




, with respective unions of ð0; 1Þ, ½1; 2, and ð0; 2.
The rational numbers are also an Fs-set and another example of one that is neither
open nor closed.
2. The complement of the sets EN, defined by
~EN ¼
x j oðxÞ < 1
N


;
are consequently open sets. So the set of continuity points of a given function is the
countable intersection of these open sets. Such a set is sometimes referred to as a Gd-
set, pronounced ‘‘G-delta set.’’ The G represents the standard notation for an open set,
as this notion apparently originated in Germany with the word for area, ‘‘Gebiet,’’
while the ‘‘delta’’ denotes the German word for ‘‘intersection’’ of these closed sets, or
‘‘Durchschnitt.’’ A Gd-set can be open, closed, or neither and can be exemplified as
above. The irrational numbers are also a Gd-set that is neither open nor closed, since
this set equals the intersection of the open sets:
Gq ¼ ðy; qÞ U ðq; yÞ
for all q A Q.
3. By De Morgan’s laws, the complement of a Gd-set is an Fs-set, and conversely. For
example, the complement of a countable union of closed sets is a countable intersection
of open sets, and conversely.
The oscillation function is also important in that knowing its values sheds light on
the maximum potential di¤erence between a function’s upper and lower Riemann
sums, as the next proposition formalizes.
Proposition 10.21
If oðxÞ < c for all x A ½a; b, then there is a partition of this interval
so that
10.2
Riemann Integration of Functions
571

X
n
i¼1
MiDxi 
X
n
i¼1
miDxi < cðb  aÞ:
Proof
Since oðxÞ ¼ g:l:b:foðx; IÞg for all I with x A I, for every x we can choose
an open interval I with oðx; IÞ < c, and by shrinking each such I as necessary, we
can find an open interval J with closure J H I, and oðx; JÞ < c. The collection of
all such J is an open cover of the compact interval ½a; b, so there is a finite subcover
fJkgm
k¼1. The desired partition is now defined by the collection of endpoints of this
family of intervals that are within ½a; b, as well as the points a and b. On every such
partition interval fJ 0
kgn
k¼1 we have oðx; J 0
kÞ < c, and so
X
n
i¼1
½Mi  miDxi < c
X
n
i¼1
Dxi ¼ cðb  aÞ:
n
We now present the main result, which provides a necessary and su‰cient condi-
tion on a bounded function f ðxÞ in order to ensure Riemann integrability on any
bounded interval ½a; b. It was proved by Bernhard Riemann.
Proposition 10.22 (Riemann Existence Theorem)
If f ðxÞ is a bounded function on the
finite interval ½a; b, then
Ð b
a f ðxÞ dx exists if and only if f ðxÞ is continuous except on a
collection of points E 1 fxag of measure 0. That is, for any  > 0, there is a countable
collection of intervals fIag so that xa A Ia for all a, and P jIaj < , where jIaj denotes
the length of the interval Ia.
Proof
We first assume that
Ð b
a f ðxÞ dx exists, which means that Pn
i¼1½Mi  miDxi
! 0 for any partition with m 1 maxfDxig ! 0. For a given  and integer N, choose
a partition with
X
n
i¼1
½Mi  miDxi < 
N :
We now show that EN has measure 0, and hence the countable union E ¼ 6 EN
that equals the set of all discontinuities also has measure 0 by proposition 10.16.
Any points of discontinuity of f ðxÞ in EN that happen to be among the endpoints
of this partition’s intervals clearly have measure 0, since there are at most n þ 1
such points. So we consider only such discontinuity points within these subintervals.
Let fIjgm
j¼1 denote the subset of partition intervals that have at least one point of dis-
continuity from EN in their interior. Then on any such interval 1
N a Mj  mj, since 1
N
572
Chapter 10
Calculus II: Integration

is defined as the g.l.b. of such values among all intervals which contain points of EN.
Consequently, as a subset of the original partition,
1
N
X
m
j¼1
jIjj a
X
n
i¼1
½Mi  miDxi < 
N ;
and hence P jIjj <  as was to be proved.
Next assume that bounded f ðxÞ is continuous except on a collection of points
E 1 fxag of measure 0. For any N, EN H E and must also have measure 0, and
hence for any  > 0 there is a family of open intervals fIag so that EN H 6 Ia and
P jIaj < . Now, since EN is closed and a subset of the compact set ½a; b, it must
also be compact and there is a finite subcollection fIjgn
j¼1 with the same properties:
EN H 6jan Ij and P
jan jIjj < . Also note that since f ðxÞ is bounded on ½a; b, there
is an M and m so that for any partition of ½a; b, the associated Mi and mi satisfy:
m a mi a Mi a M:
Now ½a; b  6jan Ij equals a finite collection of closed intervals, say fKjgm
j¼1, and
oðxÞ < 1
N for any x A Kj, since each Kj is in the complement of EN. By proposition
10.21, there is then a partition of each closed interval Kj so that
X
m 0
i¼1
MiDxi 
X
m 0
i¼1
miDxi <
X jKjj
N ;
where m0 denotes the total number of subintervals in these partitions. With these
partitions for fKjgm
j¼1, and the Ij intervals as their own partitions, we have that the
associated Riemann upper and lower sums can be split between the two groups of
intervals:
X
n
i¼1
MiDxi 
X
n
i¼1
miDxi <
P jKjj
N
þ ðM  mÞ
X
jIjj
< ðb  aÞ
N
þ ðM  mÞ;
where M and m are the bounds for f ðxÞ throughout ½a; b. Since N and  were arbi-
trary, we see that there exist partitions which make the upper and lower Riemann
sums di¤er by an arbitrarily small amount. Now given arbitrary partitions with
m ! 0, these will eventually become finer than the partitions constructed, and
10.2
Riemann Integration of Functions
573

hence will satisfy the same bounds. Consequently f ðxÞ is Riemann integrable on
½a; b.
n
Remark 10.23
1. Sets of ‘‘measure 0,’’ play a central role in real analysis. There, an integration
theory is introduced which is more general than Riemann integration, and for which
sets of measure 0 again do not matter. However, unlike the Riemann integral, which
requires continuity outside this set, this generalized integral requires less. It is known
as the Lebesgue integral and named for Henri Le´on Lebesgue (1875–1941). This gen-
eralization eliminates the counterintuitive properties of the Riemann integral that are
discussed in section 10.3 below on examples of the Riemann integral.
2. As a point on terminology, when a function f ðxÞ has a certain property, ‘‘except on
a set of measure 0,’’ it is often said that f ðxÞ has the certain property almost every-
where, and this is often shortened to (a.e.). For example, proposition 10.22 states that
a bounded function f ðxÞ is Riemann integrable on a bounded interval ½a; b if and only
if f ðxÞ is continuous (a.e.).
10.3
Examples of the Riemann Integral
In this section we illustrate the range of applicability of the notion of the Riemann
integral to functions that are continuous except on a set of measure 0, and then use
one example to illustrate when the integral fails to exist.
The first example provides the classic case of how one often thinks about Riemann
integration as it applies to functions that are continuous except on a set of measure 0.
This classic example is for a function sðxÞ that is piecewise continuous, which is to say
that sðxÞ is defined as a bounded and continuous function on each of a collection of
non-overlapping intervals. These functions were introduced in section 10.2.2.
The piecewise continuous terminology is descriptive because it literally means
‘‘continuous in pieces.’’ When this continuous function is constant on each interval,
it is typically called a step function, for apparent reasons. A Riemann sum can then
be thought of as an approximation to the integral with a step function defined so that
on each subinterval, the step function assumes some value of f ðxÞ in that interval.
For the upper and lower Riemann sums, these values of f ðxÞ are chosen as the max-
imum and minimum values of the function on each subinterval.
574
Chapter 10
Calculus II: Integration

Example 10.24
1. Define a function on the interval ½0; 2 as follows: First split the interval into
½0; 2 ¼ ½0; 1Þ U 1; 1 1
2


U 1 1
2 ; 1 3
4


U 1 3
4 ; 1 7
8


U    U ½2:
In other words, split ½0; 2 ¼ 6y
n¼0 In U ½2, where I0 1 ½0; 1Þ and
In ¼
X
n1
j¼0
1
2 j ;
X
n
j¼0
1
2 j
"
!
for n ¼ 1; 2; 3; . . . :
Next, define a function by
sðxÞ ¼
1
2 n ;
x A In;
1;
x ¼ 2;

which is graphed in figure 10.2. Since this bounded function is continuous except on the
countable collection of points
Pn
j¼0
1
2 j
n
oy
n¼0 U f2g, it must be Riemann integrable by
proposition 10.22. As the length of In is 1
2n for all n, and the Riemann sums containing
the points of discontinuity add nothing in the limit, we have that
Figure 10.2
Piecewise continuous sðxÞ
10.3
Examples of the Riemann Integral
575

ð 2
0
sðxÞ dx ¼
X
y
n¼0
ð
In
sðxÞ dx
¼
X
y
n¼0
1
2n
1
2n
¼
X
y
n¼0
1
4n ¼ 4
3 ;
using the methods of chapter 6 on geometric series.
The next examples generalize this idea, in that there are no longer intervals on
which f ðxÞ is piecewise continuous.
Example 10.25
2. Define a function on the interval ½0; 1 by
f ðxÞ ¼
1;
x ¼ 0;
1
n ;
x rational; x ¼ m
n in lowest terms;
0;
x irrational,
8
<
:
which is graphed for n up to n ¼ 13 in figure 10.3. This function is not continuous
at any rational number. For example, if x ¼ m
n in lowest terms, f ðxÞ ¼ 1
n and yet any
interval that contains x also contains irrational numbers for which f ðxÞ ¼ 0. So, if
0 <  < 1
n , there can be no d for which
f
m
n
 
 f ðxÞ


 <  for all x with
m
n  x


 < d,
since there are always irrational x for which f
m
n
 
 f ðxÞ


 ¼ 1
n . What may be surpris-
ing is that f ðxÞ is continuous at every irrational number. To see this, let x be an irra-
tional number and  > 0 be given. Choose N so that 1
N < . From the finite collection
of rationals
m
n j n a N; m a n


, there is one that is closest to x; choose d to be smaller
than this closest distance. That is, define
d < min
x  m
n


 j n a N; m a n


:
By construction, any rational in the interval ðx  d; x þ dÞ must be of the form m
M for
M > N, and so
f ðxÞ  f
m
M
 


 ¼
1
M


 

 < 1
N < . Consequently f ðxÞ is continuous at
irrational x.
Since the points of discontinuity are the rational numbers that are a set of measure 0,
this function is Riemann integrable by proposition 10.22. It is apparent that
576
Chapter 10
Calculus II: Integration

ð1
0
f ðxÞ dx ¼ 0;
since f ðxÞ ¼ 0 on the points of continuity. This result can also be justified directly by
Riemann sums. For any N, we can construct non-overlapping intervals of total length 
that cover
m
n j n a N; m a n


. Since f
m
n
 
a 1 at every point of this set, these Rie-
mann sums add up to no more than . Moreover, since f ðxÞ a
1
Nþ1 outside these inter-
vals by construction, Riemann sums associated with these points can contribute no more
than
1
Nþ1 . In other words, for any  and N we can find a Riemann sum so that
0 a
X
n
i¼1
f ð~xiÞDxi a  þ
1
N þ 1 ;
and these Riemann sums can be made to converge to 0 by choosing  ! 0 and N ! y.
3. In the preceding case 2, f ðxÞ can be redefined in many ways in terms of the assign-
ment of values for f
m
n
 
. All that is needed is that the sequence f
m
n
 
! 0 as n ! y.
Such an assignment of values is critical for continuity on the irrationals, and hence crit-
ical for the existence of the Riemann integral. For example, if gðnÞ ! 0 monotonically
as n ! y, redefining f
m
n
 
¼ gðnÞ provides a comparable result.
Figure 10.3
f ðxÞ ¼
1;
x ¼ 0
1
n ;
x ¼ m
n in lowest terms
0;
x irrational
8
>
<
>
:
10.3
Examples of the Riemann Integral
577

4. Note that with f ðxÞ defined above in case 2, if we define
gðxÞ ¼ 1  f ðxÞ;
then gðxÞ is Riemann integrable with integral equal to 1, and gðxÞ is again only contin-
uous on the irrational numbers where it has value identically equal to 1. For the ratio-
nal numbers, gðxÞ assumes values g m
n
 
¼ 1  1
n , where m
n is given in lowest terms.
The next example nudges cases 2 through 4 of example 10.25 one more step and
Riemann integrability now fails.
Example 10.26
5. Define hðxÞ on ½0; 1 by
hðxÞ ¼
1;
x irrational;
0;
x rational:

Note that except on the rationals, a set of measure 0, hðxÞ ¼ gðxÞ in case 4 of example
10.25. And yet gðxÞ is Riemann integrable with integral 1 and hðxÞ is not integrable.
That hðxÞ is not Riemann integrable is easy to see, since for any partition of ½0; 1 the
upper Riemann sum will equal 1 while the lower sum equals 0.
This series of examples presents much of the range of applicability of Riemann in-
tegration, from its beauty and power as applied to continuous functions and certain
generalizations to its inherent shortcomings, which can be summarized as a con-
flicted relationship between this integral and sets of measure zero:
1. If f ðxÞ is continuous except on a set of measure 0, it is Riemann integrable. This
implies that in this sense, sets of measure 0 are irrelevant.
2. On the other hand, if one starts with a continuous function, say tðxÞ 1 1 on ½0; 1,
and redefines it on a set of measure 0, sometimes integrability is preserved as was the
case for gðxÞ in example 4 above, and sometimes it is not, as is the case for hðxÞ in
example 5 above.
3. For some sets of measure zero, such as finite sets, one can redefine the function at
these points arbitrarily without influencing integrability. This is the case for simple
step functions, with finitely many steps.
4. On the other hand, infinite sets of measure zero can create di¤erent outcomes:
 If the set has accumulation points, like the rationals, an integrable function must be
redefined carefully on this set to maintain Riemann integrability.
578
Chapter 10
Calculus II: Integration

 If the set is sparse with no accumulation points, such as the integers, Riemann
integrability will be independent of the definition of values of the function at these
points. In other words, the integral will exist or not, independent of these values.
As it turns out, this conflicted relationship has more to do with the Riemann
approach to integration than it has to do with some intrinsic property of continuous
functions. In real analysis a di¤erent approach to the integral will eliminate all the
confusion about sets of measure 0 in favor of the simplest answer. Namely, sets of
measure 0 will not matter in that they will not influence integrability, and this conclu-
sion will be independent of whether the set is finite or infinite, and in the latter case,
whether the set has accumulation points, like the rationals, or is sparsely distributed
like the integers.
10.4
Mean Value Theorem for Integrals
The next result is an immediate consequence of the intermediate value theorem for
continuous functions introduced in proposition 9.41. It is known as the ‘‘first’’ mean
value theorem for integrals for a reason that will be seen below in proposition 10.52.
Proposition 10.27 (First Mean Value Theorem for Integrals)
Let f ðxÞ be continuous
on bounded ½a; b. Then there is a c A ½a; b so that
ð b
a
f ðxÞ dx ¼ f ðcÞðb  aÞ:
ð10:12Þ
Proof
Because f ðxÞ is continuous, it achieves its maximum M and minimum m on
this interval, and hence
mðb  aÞ a
ð b
a
f ðxÞ dx a Mðb  aÞ:
Consequently
1
ba
Ð b
a f ðxÞ dx also has value within the same bounds as f ðxÞ. By the
intermediate value theorem of chapter 9, there must therefore be a c A ½a; b with
f ðcÞ ¼
1
ba
Ð b
a f ðxÞ dx.
n
Remark 10.28
Rewrite (10.12) as
f ðcÞ ¼
1
b  a
ð b
a
f ðxÞ dx;
10.4
Mean Value Theorem for Integrals
579

and consider the integral as the net area under f ðxÞ on the interval ½a; b. Then the
value f ðcÞ can be interpreted as the average value of f ðxÞ on this interval in that this
signed area also equals the signed area of a rectangle with base length b  a, and height
f ðcÞ.
One application of this result that is more interesting than it is applicable in prac-
tice is the following. For any partition of an interval, there is a set of intermediate
points for which the Riemann sum is exact. This is another classic example of an
‘‘existence’’ theorem in mathematics. It confirms existence but provides no insight to
how one identifies or constructs these points.
Proposition 10.29
Let f ðxÞ be continuous on bounded ½a; b. Then given any partition
a ¼ x0 < x1 <    < xn1 < xn ¼ b;
there exists f~xign
i¼1, with ~xi A ½xi1; xi so that with Dxi ¼ xi  xi1,
ð b
a
f ðxÞ dx ¼
X
n
i¼1
f ð~xiÞDxi:
ð10:13Þ
Proof
By (10.6), we can conclude that
ð b
a
f ðxÞ dx ¼
X
n
i¼1
ð xi
xi1
f ðxÞ dx;
and the proposition above and (10.12) assure that for each integral on the right, there
is a point ~xi A ½xi1; xi that gives the stated result.
n
Remark 10.30
This proof demonstrates that for a continuous function and any par-
tition, one can in theory choose the intermediate ~xi values so that the Riemann sum
exactly reproduces the limiting integral value. Of course, this proof and conclusion
rely on the first mean value theorem for integrals, which sheds no light on how such
intermediates values can be determined; it only confirms their existence. Consequently
this result is not useful in practice in terms of obtaining exact integrals with Riemann
sums.
Two other important corollaries to this Proposition provide simple and also useful
results:
Proposition 10.31
Let f ðxÞ be continuous on bounded ½a; b, and assume that for
every ½c; d H ½a; b,
580
Chapter 10
Calculus II: Integration

ð d
c
f ðxÞ dx ¼ 0:
Then f ðxÞ 1 0 on ½a; b.
Proof
By proposition 10.27, we conclude that for every ½c; d H ½a; b, there is a
point c0 A ½c; d with
Ð d
c f ðxÞ dx ¼ f ðc0Þðd  cÞ, and hence f ðc0Þ ¼ 0 for every such
c0. Letting d ¼ c þ Dc, we conclude that for every Dc there is a c0 A ½c; c þ Dc with
f ðc0Þ ¼ 0. Letting Dc ! 0, we have c0 ! c and the continuity of f ðxÞ provides
f ðcÞ ¼ 0. This proves f ðcÞ ¼ 0 for all c A ½a; bÞ, and hence f ðbÞ ¼ 0 by continuity.
n
Proposition 10.32
Let f ðxÞ and gðxÞ be continuous on bounded ½a; b, and assume
that for every ½c; d H ½a; b,
ð d
c
f ðxÞ dx ¼
ð d
c
gðxÞ dx:
Then f ðxÞ 1 gðxÞ on ½a; b.
Proof
The conclusion is immediate, since f ðxÞ  gðxÞ satisfies the hypothesis of
proposition 10.31, and so
Ð d
c ½ f ðxÞ  gðxÞ dx ¼ 0.
n
10.5
Integrals and Derivatives
There are two related results which connect the notions of derivative, as developed in
chapter 9, and that of Riemann integral as developed above. The first is the result
obtained when a derivative is integrated.
10.5.1
The Integral of a Derivative
Proposition 10.33 (Fundamental Theorem of Calculus, Version I )
Let f ðxÞ be a dif-
ferentiable function so that f 0ðxÞ is continuous on bounded ½a; b. Then
ð b
a
f 0ðxÞ dx ¼ f ðbÞ  f ðaÞ:
ð10:14Þ
Proof
We know that the integral exists since f 0ðxÞ is assumed to be continuous.
Consequently we can define it in terms of any Riemann sums, which is to say, any
partition with m ! 0. Given any partition, we have by the mean value theorem of
10.5
Integrals and Derivatives
581

proposition 9.83 that in every subinterval, ½xi1; xi there is an ~xi so that f 0ð~xiÞDxi
¼ f ðxiÞ  f ðxi1Þ. Choosing these ~xi, we have
X
n
i¼1
f 0ð~xiÞDxi ¼
X
n
i¼1
½ f ðxiÞ  f ðxi1Þ ¼ f ðbÞ  f ðaÞ;
since this middle summation ‘‘telescopes’’ by cancellation to only the first and last
terms.
n
Notation 10.34
It is common in calculus to use the notation f ðxÞjb
a for the right-hand
side of (10.14). In other words,
f ðxÞjb
a 1 f ðbÞ  f ðaÞ:
Example 10.35
1. With f ðxÞ ¼ ex, since f 0ðxÞ ¼ f ðxÞ, we have that for any closed interval ½a; b,
ð b
a
ex dx ¼ eb  ea:
2. With
f ðxÞ ¼
x2;
0 a x < 1;
x2 þ 5;
1 a x a 2;

the example in figure 10.1, then on ð0; 1Þ U ð1; 2Þ, we have that f ðxÞ ¼ F 0ðxÞ, where
FðxÞ ¼
x3
3 ;
0 a x < 1;
x3
3 þ 5x;
1 a x a 2:
(
So
ð 2
0
f ðxÞ dx ¼ lim
!0
ð1
0
x2 dx þ
ð2
1
ðx2 þ 5Þ dx
¼ lim
!0
x3
3


1
0
þ
x3
3 þ 5x



2
1
¼ 23
3 :
582
Chapter 10
Calculus II: Integration

The applicability of the Fundamental Theorem of Calculus I is apparent. If one is
attempting to integrate a continuous function, f ðxÞ, and this function is recognized
as the derivative of another function FðxÞ, so that F 0ðxÞ ¼ f ðxÞ, then the Riemann
summation and limiting process to evaluating the integral can be circumvented,
since
ð b
a
f ðxÞ dx ¼ FðbÞ  FðaÞ:
ð10:15Þ
Because of the Fundamental Theorem, it is the case that in many calculus texts,
integration of a function f ðxÞ is transformed into techniques for determining the
associated function FðxÞ, the so-called antiderivative of f ðxÞ, since then integration
is simplified. Unfortunately, not all continuous functions are the derivatives of other
recognizable functions, and even for those that are, finding the functional form of the
correct FðxÞ can be di‰cult at best. Consequently e‰cient numerical techniques are
often useful and will be discussed in section 10.10.
Definition 10.36
Given a continuous function f ðxÞ, the antiderivative of f ðxÞ, some-
times denoted
Ð
f ðxÞ dx and sometimes FðxÞ when f ðxÞ is clear from the context, is
any function such that
F 0ðxÞ ¼ f ðxÞ:
ð10:16Þ
It is important to note that the antiderivative of a function is not unique. In partic-
ular, if FðxÞ is an antiderivative, so too is FðxÞ þ C for any C A R. Of course, as is
easily seen, for the purpose of evaluating an integral by (10.15), any antiderivative
works equally well, and in practice, one typically uses C ¼ 0.
Also note that the notational convention FðxÞ ¼
Ð
f ðxÞ dx is a bit careless and yet
not uncommon. On the left, the variable x denotes the label for the domain variable
of the function F, while on the right, the variable x is a so-called dummy variable,
which could be denoted y, z, l, a, or any other letter. It is the same as the dummy
variable in a summation, in the sense that Pb
j¼a j2 is identical to Pb
k¼a k2. What is
meant by this notation is that FðxÞ is a function with derivative f ðxÞ. Although nota-
tionally careless, to instead define FðxÞ ¼
Ð
f ðyÞ dy, say, is notationally ambiguous.
This notation will be made precise in section 10.5.2, where the second statement of
the Fundamental Theorem is developed.
Remark 10.37
The intuitive framework for the Riemann integral,
Ð b
a f ðxÞ dx, is one
of ‘‘net area’’ between the curve, y ¼ f ðxÞ, and the x-axis, over the interval ½a; b, as
10.5
Integrals and Derivatives
583

noted above. For this purpose it was assumed that a < b. However, in this case the
meaning of
Ð a
b f ðxÞ dx can also be introduced in a consistent way by proposition 10.33
above. Namely from (10.14) we can conclude that the definition
ð a
b
f ðxÞ dx 1 
ð b
a
f ðxÞ dx
ð10:17Þ
provides a consistent generalization of the definition of the Riemann integral.
The version above of the Fundamental Theorem in (10.14) also provides another
simple and often utilized conclusion. First recall:
1. It is apparent from the definition of f 0ðxÞ, that if f ðxÞ is increasing, in that
f ðxÞ a f ðx0Þ for all x a x0, then f 0ðxÞ b 0 for all x.
2. If f ðxÞ is strictly increasing, in that f ðxÞ < f ðx0Þ for all x < x0, then it is not true
that f 0ðxÞ > 0 for all x, and the conclusion remains only that f 0ðxÞ b 0 for all x. For
example, consider f ðxÞ ¼ x3, which is strictly increasing but f 0ð0Þ ¼ 0.
3. Similarly, if f ðxÞ is decreasing or strictly decreasing, then f 0ðxÞ a 0 for all x.
The question addressed next is the reversal of these implications. Namely, what if
anything does the ‘‘sign’’ of f 0ðxÞ predict about the behavior of f ðxÞ? The conclu-
sions below will be seen to be a bit weaker than those drawn with the tools of chapter
9. Specifically, using (9.33) with n ¼ 0 provides the same conclusions without the
assumed continuity of f 0ðxÞ. However, there is value in comparing results with dif-
ferent approaches.
Proposition 10.38
Let f ðxÞ be continuous with continuous f 0ðxÞ on an interval ½a; b.
Then for any ½c; d H ½a; b,
1. f 0ðxÞ b 0 on ½c; d ) f ðcÞ a f ðdÞ, and f ðxÞ is increasing
2. f 0ðxÞ > 0 on ½c; d ) f ðcÞ < f ðdÞ, and f ðxÞ is strictly increasing
3. f 0ðxÞ a 0 on ½c; d ) f ðcÞ b f ðdÞ, and f ðxÞ is decreasing
4. f 0ðxÞ < 0 on ½c; d ) f ðcÞ > f ðdÞ, and f ðxÞ is strictly decreasing
Proof
Each of these statements easily follows from (10.14), which in the notation
here states that:
ð d
c
f 0ðxÞ dx ¼ f ðdÞ  f ðcÞ:
584
Chapter 10
Calculus II: Integration

Now by the definition of the Riemann integral, the sign of
Ð d
c f 0ðxÞ dx follows from
the sign of f 0ðxÞ on ½c; d if this sign is consistent, and the proposition’s four state-
ments follow from this observation.
n
10.5.2
The Derivative of an Integral
The second result on the relationship between derivative and Riemann integral looks
somewhat di¤erent, but is equivalent. To this end, we introduce the notion of an in-
definite integral, whereby the variable x is used as one of the limits of integration.
This terminology is complemented by sometimes calling
Ð a
b f ðxÞ dx a definite integral
as noted in remark 10.3 following the definition of this Riemann integral.
Definition 10.39
The indefinite integral of a continuous function f ðxÞ is defined by
FðxÞ ¼
ð x
a
f ðyÞ dy:
ð10:18Þ
If a < x, the value is given directly by the definition of Riemann integral, whereas if
x < a, this function is defined as in (10.17) of remark 10.37 above as 
Ð a
x f ðyÞ dy.
The next result provides an alternative view of the connection between integral
and derivative.
Proposition 10.40 (Fundamental Theorem of Calculus, Version II )
Let f ðxÞ be a
continuous function on bounded ½a; b, and define
FðxÞ ¼ FðaÞ þ
ð x
a
f ðyÞ dy;
a a x a b;
ð10:19Þ
where FðaÞ is arbitrarily defined. Then FðxÞ is di¤erentiable on ða; bÞ, and
F 0ðxÞ ¼ f ðxÞ:
ð10:20Þ
Proof
First o¤, it may not be obvious that FðxÞ is even continuous. However, the
MVT for integrals in proposition 10.27 assures us that for x0 < x,
FðxÞ  Fðx0Þ ¼
ð x
x 0 f ðyÞ dy
¼ f ðcÞðx  x0Þ
for some c A ½x0; x:
Now since f ðxÞ is assumed continuous on ½x0; x, we conclude that Fðx0Þ ! FðxÞ as
x0 ! x, and so FðxÞ is continuous. This same equation also shows that
10.5
Integrals and Derivatives
585

FðxÞ  Fðx0Þ
x  x0
¼ f ðcÞ
for some c A ½x0; x:
Hence, as x0 ! x, FðxÞFðx 0Þ
ðxx 0Þ
! f ðxÞ, again due to the continuity of f ðxÞ.
n
Remark 10.41
1. This proposition is also called the Fundamental Theorem of Calculus because it is
equivalent to the statement in proposition 10.33 above. Letting x ¼ b, and using the
conclusion that F 0ðxÞ ¼ f ðxÞ, we derive from the FTC II proposition that
FðbÞ ¼ FðaÞ þ
ð b
a
F 0ðyÞ dy;
which is the statement of the earlier Fundamental Theorem of Calculus I in (10.14)
with a small change in notation.
On the other hand, FTC I clearly holds with b replaced by x, and can be rearranged
to produce
f ðxÞ ¼ f ðaÞ þ
ð x
a
f 0ðyÞ dy;
where f ðxÞ is given and assumed di¤erentiable with continuous derivative. If this same
f ðxÞ could be achieved with a di¤erent continuous function gðxÞ,
f ðxÞ ¼ f ðaÞ þ
ð x
a
gðyÞ dy;
we would conclude that
Ð x
a ½gðyÞ  f 0ðyÞ dy ¼ 0 for all x. Therefore, by subtraction,
Ð xþDx
x
½gðyÞ  f 0ðyÞ dy ¼ 0 for any x and Dx, and by the proposition 10.32 result
from the MVT we would conclude that gðyÞ ¼ f 0ðyÞ for all y.
2. This statement of the Fundamental Theorem also makes precise the notational care-
lessness of the expression often used for antiderivatives: FðxÞ ¼
Ð
f ðxÞ dx. This is
shorthand for FðxÞ ¼ FðaÞ þ
Ð x
a f ðyÞ dy, in (10.19), utilizing the fact that the values
of both a and FðaÞ are irrelevant.
Example 10.42
1. A simple application of FTCII is that it provides an interesting new definition of
ln x. Specifically, since f 0ðxÞ ¼ 1
x for f ðxÞ ¼ ln x, and ln 1 ¼ 0, we can conclude that
for x b 1,
586
Chapter 10
Calculus II: Integration

ln x ¼
ð x
1
dy
y :
ð10:21Þ
2. As another application with f ðxÞ ¼ ex, since f 0ðxÞ ¼ ex, we have for any a and
x b a,
ex ¼ ea þ
ð x
a
ey dy:
Letting a ! y, we obtain an example of an ‘‘improper integral’’ discussed below:
ex ¼
ð x
y
ey dy:
10.6
Improper Integrals
10.6.1
Definitions
The preceding sections provide insight as to how one can attempt to extend the
integral of some functions in one of two ways:
1. Define
Ð b
a f ðxÞ dx for continuous f ðxÞ where b ¼ y and/or a ¼ y.
2. Define
Ð b
a f ðxÞ dx for f ðxÞ that is continuous on every closed interval ½c; d H ½a; b
but is unbounded at a and/or b.
In both cases the resulting integrals are called improper integrals if they exist
because they are defined outside the general framework of the Riemann existence
theorem in proposition 10.22 above. Recall that this theorem applied to bounded
functions on a bounded interval ½a; b that are continuous almost everywhere, which
is to say, everywhere except on a set of measure 0.
Each of these extensions can potentially be defined as a limit of well-defined Rie-
mann integrals. For example, if F 0ðxÞ ¼ f ðxÞ is continuous on ½M; N for all M,
N, then define
ðy
y
f ðxÞ dx 1
lim
N;M!y
ð N
M
f ðxÞ dx ¼
lim
N;M!y½FðNÞ  FðMÞ:
ð10:22Þ
Similarly, if F 0ðxÞ ¼ f ðxÞ is continuous on ½a þ d; b   for all ; d > 0, then define
10.6
Improper Integrals
587

ð b
a
f ðxÞ dx 1 lim
;d!0
ð b
aþd
f ðxÞ dx ¼ lim
;d!0½Fðb  Þ  Fða þ dÞ:
ð10:23Þ
The only remaining question is the existence of these limits. Since such limits in-
volve two variates, we formalize the definition in the predictable way:
Definition 10.43
limx;y!a f ðx; yÞ ¼ L for a < y and L < y, if for any  > 0
there is a d so that j f ðx; yÞ  Lj <  when jx  aj < d and jy  aj < d. Also,
limx;y!y f ðx; yÞ ¼ L if for any  > 0 there is an N so that j f ðx; yÞ  Lj <  when
x; y > N.
Example 10.44
1.
Ð y
1 xa dx is well defined i¤ a > 1, since by (10.14), for a 0 1,
ðy
1
xa dx ¼ lim
x!y
x1a
1  a 
1
1  a


¼
1
a1 ;
if a > 1;
y;
if a < 1:

Also, if a ¼ 1,
ðy
1
x1 dx ¼ lim
N!y ln N ¼ y:
2.
Ð 1
0 xa dx is well defined i¤ a > 1 since for a 0 1,
ð 1
0
xa dx ¼
1
a þ 1  lim
!0
aþ1
a þ 1
¼
1
aþ1 ;
if a > 1;
y;
if a < 1:

Also, if a ¼ 1,
ð 1
0
x1 dx ¼  lim
!0 ln  ¼ y:
10.6.2
Integral Test for Series Convergence
In this section is introduced another test for the convergence of a numerical series,
the so-called integral test, as noted in chapter 6. At first it may seem odd that the
588
Chapter 10
Calculus II: Integration

Riemann integral can be used to determine the convergence of a series. But since
these integrals are limits of Riemann sums, and each Riemann sum is a finite series,
and for an improper integral, an infinite series, the connection is not so surprising.
To motivate the method, we provide yet another proof of the divergence of the
harmonic series:
Example 10.45
Consider the series: Py
n¼1
1
n . For f ðxÞ ¼ ln x, we have from (10.21)
that ln x ¼
Ð x
1
dy
y , and so by definition,
Ð y
1
dy
y ¼ y. Now splitting the integral into unit
intervals, we conclude that
X
y
n¼1
ð nþ1
n
dy
y ¼ y:
Note that on each unit interval, by using a single upper and lower Riemann sum, we
have
1
n þ 1 <
ð nþ1
n
dy
y < 1
n ;
and hence
X
y
n¼1
ð nþ1
n
dy
y <
X
y
n¼1
1
n ;
proving divergence.
With this example as motivation, we now present the integral test for a series.
Proposition 10.46 (Integral Test)
Let Py
n¼1 an be a given series, and f ðxÞ a continu-
ous function on ½1; yÞ with
anþ1 a f ðxÞ a an
for x A ½n; n þ 1:
ð10:24Þ
Then Py
n¼1 an and
Ð y
1 f ðxÞ dx both converge or both diverge.
Proof
By the given assumptions, for all n b 1,
anþ1 a
ð nþ1
n
f ðxÞ dx a an;
and by addition,
10.6
Improper Integrals
589

X
y
n¼1
an
 
!
 a1 a
ðy
1
f ðxÞ dx a
X
y
n¼1
an:
The result follows by comparison.
n
It is important to note that this test not only gives insight to the convergence or
divergence of a given series, but it is also useful for numerical estimates in the case
of convergence, and a growth rate analysis in the case of divergence. To this end,
consider the partial sum version of the inequalities above from n ¼ 1 to N  1.
It produces
X
N
n¼1
an
 
!
 a1 a
ð N
1
f ðxÞ dx a
X
N
n¼1
an
 
!
 aN:
Rearranging, we obtain
ð N
1
f ðxÞ dx þ aN a
X
N
n¼1
an a
ð N
1
f ðxÞ dx þ a1:
ð10:25Þ
In the case of series divergence the integral provides an estimate of the rate of
divergence.
In the case of convergence, and so aN ! 0 by letting N ! y, the integral pro-
duces an estimate of the summation:
ðy
1
f ðxÞ dx a
X
y
n¼1
an a
ðy
1
f ðxÞ dx þ a1
ð10:26Þ
We next consider an example of each case.
Example 10.47
1. As an application in the case of convergence, recall the power harmonic series
Py
n¼1
1
n p for p > 1, which converges by the analysis in example 6.9. With f ðxÞ ¼ xp,
a calculation gives that
ðy
1
f ðxÞ dx ¼
x1p
1  p



y
x¼1
¼
1
p  1 ;
and so
590
Chapter 10
Calculus II: Integration

1
p  1 a
X
y
n¼1
1
np a
p
p  1 :
For the partial sums of this series, the same approach provides for all N,
1  N 1p
p  1
þ N p a
X
N
n¼1
1
np a p  N 1p
p  1
:
2. As an application in the case of divergence, we return to the harmonic series and
f ðxÞ ¼ 1
x . Since
Ð N
1
dx
x ¼ ln N,
ln N þ 1
N a
X
N
n¼1
1
n a ln N þ 1;
and so the harmonic series partial sums are larger than, but within 1 unit of, the value
of ln N. A more detailed analysis below demonstrates that the following limit exists:
lim
N!y
X
N
n¼1
1
n  ln N
"
#
¼ gA0:577215664902 . . . :
ð10:27Þ
This constant, g, is known as the Euler constant, after its discoverer, Leonhard Euler
(1707–1783).
Note that by expressing N ¼ QN1
n¼1
nþ1
n


, we derive that
X
N
n¼1
1
n  ln N ¼ 1
N þ
X
N1
n¼1
1
n  ln 1 þ 1
n




:
Consequently, applying (9.33) and n ¼ 1 to lnð1 þ xÞ, we obtain that there is fcng with
0 < cn < 1, so that
X
N1
n¼1
1
n  ln 1 þ 1
n




¼
X
N1
n¼1
1
2
n
n þ cn

2 1
n2
"
#
a
X
N1
n¼1
1
2n2 < y:
So the sequence in (10.27), minus the inconsequential term
1
N , is increasing and
bounded, and hence converges as N ! y by proposition 5.18.
10.6
Improper Integrals
591

10.7
Formulaic Integration Tricks
The most important trick for formulaically evaluating an integral, Ð b
a f ðxÞ dx, is
given by the Fundamental Theorem of Calculus in (10.15). Namely one attempts to
find the antiderivative of f ðxÞ, which means any function FðxÞ so that F 0ðxÞ ¼ f ðxÞ.
We use the term ‘‘any’’ function FðxÞ, since we know that if FðxÞ is one such func-
tion, then FðxÞ þ C is another for any constant C. Of course, this constant is elimi-
nated in the application of (10.15).
There are many tricks that one can use to assist in the identification of such an
antiderivative. In general, these methods allow one to simplify the problem, in one
or many steps, and thereby reveal the antiderivative in pieces. In this section we con-
sider two approaches. The emphasis will be on definite integrals. However, any pro-
cess that allows the general evaluation of a definite integral provides the formula for
an antiderivative by (10.15).
Specifically, any formula of the sort
ð b
a
f ðxÞ dx ¼ FðbÞ  FðaÞ;
can be rewritten with b ¼ y, say, to produce
FðyÞ ¼ FðaÞ þ
ð y
a
f ðxÞ dx:
This is an antiderivative of the integrand, f ðyÞ, for any value of a; and any assign-
ment of the value of FðaÞ.
Remark 10.48
In practice, a simple implementation of this idea of finding an anti-
derivative is to convert b to x in the expression FðbÞ  FðaÞ, discard any terms in the
formula that are constant and independent of x, and add the arbitrary constant C.
10.7.1
Method of Substitution
The method of substitution is more akin to trompe-l’œil, the art form of tricking the
eye, than it is a new mathematical method. But sometimes tricking the eye into see-
ing a simpler problem is exactly what is needed to get an integration problem started.
This method is an application of the formula for di¤erentiation of a composite
function:
½FðGðxÞÞ0 ¼ f ðGðxÞÞgðxÞ;
592
Chapter 10
Calculus II: Integration

where, of course, F 0ðxÞ ¼ f ðxÞ and G 0ðxÞ ¼ gðxÞ. By the Fundamental Theorem, the
integral of the derivative is easy to evaluate, and
ð b
a
f ðGðxÞÞgðxÞ dx 1
ð b
a
½FðGðxÞÞ0 dx
¼ FðGðbÞÞ  FðGðaÞÞ:
So the di‰culty in applying this result is recognizing when a given integrand is in
fact of this form, and that is where trompe-l’œil helps. We illustrate first with an ex-
ample.
Example 10.49
Let’s evaluate
Ð b
a exðex þ 4Þ20 dx. One elementary but tedious
approach is to expand the integrand into a summation of terms of the form P ciedix,
which is easy to integrate term by term by the Fundamental Theorem since
Ð
ciedix dx
¼ ci
di edix þ ei for arbitrary constant ei. Alternatively, we may observe that this is a com-
posite function, where f ðyÞ ¼ y20, GðxÞ ¼ ex þ 4, and exðex þ 4Þ20 ¼ f ðGðxÞÞgðxÞ,
and hence since FðyÞ ¼ y21
21 ,
ð b
a
exðex þ 4Þ20 dx ¼ 1
21 ½ðeb þ 4Þ21  ðea þ 4Þ21:
Written as an antiderivative,
ð
exðex þ 4Þ20 dx ¼ 1
21 ðex þ 4Þ21 þ C:
Admittedly, this calculation required us to keep track of the various components
of the composite function, and in many cases this mental tracking can be complex.
The method of substitution is intended to simplify the tracking with a neat notational
device.
For this example, the method of substitution is to define a new ‘‘variable’’ u, which
is indeed a function of x by u ¼ ex þ 4, and correspondingly define the ‘‘di¤erential’’
du ¼ du
dx dx ¼ ex dx. We then have the eye fooled into seeing:
ð
exðex þ 4Þ20 dx ¼
ð
u20 du;
where this second antiderivative is elementary and equals u21
21 . One can then substitute
back to get
Ð
exðex þ 4Þ20 dx ¼ ðe xþ4Þ21
21
, and with the antiderivative in hand, the Fun-
damental Theorem provides the integration result above.
10.7
Formulaic Integration Tricks
593

Note that we in fact could have modified this process to apply directly to the in-
tegral with limits, by introducing the u limits that correspond to the x limits. That is,
ð b
a
exðex þ 4Þ20 dx ¼
ð e bþ4
e aþ4
u20 du:
In this example, the variable u is taking the place of the function GðxÞ in the com-
posite function above, while du is accounting for the gðxÞ dx term. So the method of
substitution can be described as converting something complex looking into some-
thing simple looking. In other words, tricking the eye,
ð b
a
f ðGðxÞÞgðxÞ dx ¼
ð GðbÞ
GðaÞ
f ðuÞ du;
ð10:28Þ
where the substitution is: u ¼ GðxÞ, du ¼ gðxÞ dx, and the x-limits of integration are
converted into u-limits.
In applications, one sometimes guesses as to an appropriate definition for the vari-
able u and sees how the integral is transformed. For substitution to succeed two
things must occur:
1. There is some substitution u ¼ GðxÞ into the initial integral that converts it into
an integral of the form
Ð
f ðuÞ du in (10.28).
2. The integral produced can be handled directly, or with the further application of
this or another technique.
10.7.2
Integration by Parts
As the name suggests, integration by parts provides an algorithm for reducing an
integrand to a new integrand that is hopefully simper to deal with. It gives ‘‘part’’
of the final result, and is derived from the formula for the derivative of a product of
two functions.
Let FðxÞ and GðxÞ be two di¤erentiable functions with derivatives f ðxÞ and gðxÞ,
respectively. In other words, F 0ðxÞ ¼ f ðxÞ and G 0ðxÞ ¼ gðxÞ. Then the derivative of
FðxÞGðxÞ is given by
½FðxÞGðxÞ0 ¼ f ðxÞGðxÞ þ FðxÞgðxÞ:
By the Fundamental Theorem, it is easy to integrate ½FðxÞGðxÞ0, namely
ð b
a
½FðxÞGðxÞ0 dx ¼ FðbÞGðbÞ  FðaÞGðaÞ:
594
Chapter 10
Calculus II: Integration

So the integration by parts idea is to convert the integral of something ‘‘hard,’’ say
f ðxÞGðxÞ, into an integral of something that is hopefully easier, namely FðxÞgðxÞ,
and a second very easy integral of ½FðxÞGðxÞ0. We then get the integration by parts
formula:
ð b
a
f ðxÞGðxÞ dx ¼ FðbÞGðbÞ  FðaÞGðaÞ 
ð b
a
FðxÞgðxÞ dx:
ð10:29Þ
Note that the application of (10.29) requires two things in order to succeed in solv-
ing the problem:
1. The integrand can be split into a product f ðxÞGðxÞ of a function f ðxÞ for which
we can find the antiderivative FðxÞ, and a function GðxÞ that we can di¤erentiate to
obtain gðxÞ;
2. This splitting produces a final integrand FðxÞgðxÞ, which is easier to work with
than the initial integrand f ðxÞGðxÞ.
In some applications, this process is implemented repeatedly. In other applica-
tions, trial and error and/or creative thinking is required, as the next few examples
illustrate.
Example 10.50
1. Consider the evaluation of
Ð b
a x3ex2 dx. Since we do not know the antiderivative
of ex2, it is natural to guess that we ought to define f ðxÞ ¼ x3 and GðxÞ ¼ ex2, produc-
ing FðxÞ ¼ x4
4 and gðxÞ ¼ 2xex2. Unfortunately, the final integral in (10.29) is then
1
2
Ð b
a x5ex2 dx, which is worse than what we started with. So, if this method is to work,
and in many cases it does not, we must find a way to move ex2 into the definition of
f ðxÞ. A little thought reveals that while finding the antiderivative of ex2 appears impos-
sible, the antiderivative of f ðxÞ ¼ xex2 is FðxÞ ¼ 1
2 ex2. So we define GðxÞ ¼ x2 with
gðxÞ ¼ 2x and obtain
ð b
a
x3ex2 dx ¼ 1
2 ½b2eb2  a2ea2 
ð b
a
xex2 dx
¼ 1
2 ½b2eb2  a2ea2  1
2 ½eb2  ea2:
Written as an antiderivative,
ð
x3ex2 dx ¼ 1
2 ½x2ex2  ex2 þ C:
10.7
Formulaic Integration Tricks
595

2. Let’s next evaluate
Ð b
a ln x dx where we assume b > a > 0, to ensure that the inte-
grand is well defined and continuous. The case a > b > 0 is similarly handled by re-
mark 10.37. In this case we have only one function visible, implying that this method
has no chance of success. Certainly we would likely choose GðxÞ ¼ ln x, with gðxÞ ¼ 1
x ,
since to assign ln x to f ðxÞ is to require the calculation of its antiderivative FðxÞ, which
we do not know or else we would just apply the Fundamental Theorem. With this defi-
nition of GðxÞ, there is no other choice than to try f ðxÞ ¼ 1, with FðxÞ ¼ x, and hope
for the best. We then get
ð b
a
ln x dx ¼ b ln b  a ln a 
ð b
a
1 dx
¼ b ln b  a ln a  ðb  aÞ:
Again, written as an antiderivative,
ð
ln x dx ¼ x ln x  x þ C:
3. Consider
Ð b
a xnex dx for integer n. Since both xn and ex are easily di¤erentiated as
well as easily integrated, it appears that there is some choice in their assignment to
f ðxÞ and GðxÞ. However, if we assign GðxÞ ¼ ex and f ðxÞ ¼ xn, it is clear that we
are moving in the wrong direction and that the final integral is 1
nþ1
Ð b
a xnþ1ex dx. Revers-
ing the assignment, we obtain a final integral of n
Ð b
a xn1ex dx, and the process can
be repeated until the final integral is K
Ð b
a ex dx, for constant K ¼ Gn!, at which point it
is easily completed. See exercises 8 and 27.
*10.7.3
Wallis’ Product Formula
As a final application of the method underlying integration by parts, we return
to the development of Wallis’ product formula, introduced in section 8.5.1 in the
derivation of Stirling’s formula. Recall that this product formula, as stated in (8.25),
is
p
2 ¼
Y
y
n¼1
ð2nÞ2
ð2n  1Þð2n þ 1Þ :
ð10:30Þ
To this end, first note that if hðxÞ ¼ sinn1 x cos x, then by (9.16) is derived
that
596
Chapter 10
Calculus II: Integration

h0ðxÞ ¼ ðn  1Þ sinn2 x cos2 x  sinn x
¼ ðn  1Þ sinn2 xð1  sin2 xÞ  sinn x
¼ ðn  1Þ sinn2 x  n sinn x;
where this derivation also used
sin2 x þ cos2 x ¼ 1:
ð10:31Þ
Now, for n > 1, Ð p=2
0
h0ðxÞ dx ¼ h p
2
 
 hð0Þ ¼ 0, and hence
ð p=2
0
sinn x dx ¼ n  1
n
ð p=2
0
sinn2 x dx;
n > 1:
ð10:32Þ
This identity can then be applied to even, n ¼ 2m, and odd, n ¼ 2m þ 1, integers
and iterated to produce
ð p=2
0
sin2m x dx ¼ 2m  1
2m
2m  3
2m  2 . . . 1
2
ð p=2
0
dx
¼ p
2
Y
m1
j¼0
2m  2j  1
2m  2j


;
and similarly since
Ð p=2
0
sin x dx ¼ 1,
ð p=2
0
sin2mþ1 x dx ¼
2m
2m þ 1
2m  2
2m  1 . . . 2
3
ð p=2
0
sin x dx
¼
Y
m1
j¼0
2m  2j
2m  2j þ 1


:
For the next step, we must divide these expressions and solve for p
2 , producing
p
2 ¼
Y
m1
j¼0
2m  2j
2m  2j þ 1

 Y
m1
j¼0
2m  2j
2m  2j  1

 Ð p=2
0
sin2m x dx
Ð p=2
0
sin2mþ1 x dx
¼
Y
m1
j¼0
ð2m  2jÞ2
ð2m  2j þ 1Þð2m  2j  1Þ
Ð p=2
0
sin2m x dx
Ð p=2
0
sin2mþ1 x dx
:
10.7
Formulaic Integration Tricks
597

This formula is then rewritten by defining n ¼ m  j and changing the j product to
an n product from n ¼ 1 to n ¼ m:
p
2 ¼
Y
m
n¼1
ð2nÞ2
ð2n þ 1Þð2n  1Þ
Ð p=2
0
sin2m x dx
Ð p=2
0
sin2mþ1 x dx
:
The final step is to let m ! y, but to do so requires a demonstration that the ratio
of integrals converges to 1. Because 0 < sin x < 1 for 0 < x < p
2 , it follows that for
any m,
ð p=2
0
sin2mþ1 x dx <
ð p=2
0
sin2m x dx <
ð p=2
0
sin2m1 x dx:
If this set of inequalities is divided by
Ð p=2
0
sin2mþ1 x dx, and (10.32) applied, we obtain
1 <
Ð p=2
0
sin2m x dx
Ð p=2
0
sin2mþ1 x dx
< 1 þ 1
2m ;
and so this ratio of integrals converges to 1, and (10.30) is demonstrated.
10.8
Taylor Series with Integral Remainder
In sections 9.3.7 and 9.3.8 Taylor series were introduced and some properties studied.
In this section we revisit this idea, and with the aid of integration by parts, develop a
new form for the remainder term which can be contrasted with the representation in
(9.33).
To this end, we first observe that given x0, we have by the second form of the Fun-
damental Theorem in (10.19) that
hðxÞ ¼ hðx0Þ þ
ð x
x0
h0ðzÞ dz;
where we use the general notation hðxÞ to avoid confusion with the functions in
(10.29). We can now apply integration by parts, expressing h0ðzÞ ¼ f ðzÞGðzÞ with
f ðzÞ ¼ 1 and GðzÞ ¼ h0ðzÞ, and using the arbitrary yet convenient constant term to
express FðzÞ ¼ ðx  zÞ; and we obtain
hðxÞ ¼ hðx0Þ þ h0ðx0Þðx  x0Þ þ
ð x
x0
h00ðzÞðx  zÞ dz:
598
Chapter 10
Calculus II: Integration

We then express h00ðzÞðx  zÞ ¼ f ðzÞGðzÞ with f ðzÞ ¼ ðx  zÞ, GðzÞ ¼ h00ðzÞ, and
FðzÞ ¼  1
2 ðx  zÞ2, and so on, producing the following:
Proposition 10.51
Let hðxÞ be ðn þ 1Þ-times di¤erentiable on ða; bÞ, with all deriva-
tives continuous on ½a; b. Then for x; x0 A ða; bÞ,
hðxÞ ¼
X
n
j¼0
1
j! hð jÞðx0Þðx  x0Þ j þ 1
n!
ð x
x0
hðnþ1ÞðzÞðx  zÞn dz:
ð10:33Þ
Proof
This follows by mathematical induction, using integration by parts as noted
above.
n
The remainder term in the Taylor series expansion in (10.33) is known as the
Cauchy form of the remainder after Augustin Louis Cauchy (1789–1857), who is
credited with the first rigorous proof of the Taylor theorem. Another form of this re-
mainder, named for Joseph-Louis Lagrange was developed in section 9.3.8.
If we compare the remainder terms of Cauchy and Lagrange, adjusting for nota-
tion, we obtain
1
n!
ð x
x0
f ðnþ1ÞðzÞðx  zÞn dz ¼
1
ðn þ 1Þ! f ðnþ1ÞðyÞðx  x0Þnþ1;
ð10:34Þ
where the point y depends on x and satisfies x0 < y < x or x < y < x0. It turns out
that this relationship between these remainders is a special case of what is known as
the second mean value theorem for integrals:
Proposition 10.52 (Second Mean Value Theorem for Integrals)
Let f ðxÞ and gðxÞ be
continuous on bounded ½a; b, and gðxÞ b 0. Then there is a point c A ½a; b so that
ð b
a
f ðxÞgðxÞ dx ¼ f ðcÞ
ð b
a
gðxÞ dx:
ð10:35Þ
Proof
Since this result is obviously true if gðxÞ 1 0, we can assume that gðxÞ > 0
somewhere on this interval and hence that
Ð b
a gðxÞ dx > 0. Now as f ðxÞ is continuous
on ½a; b, it attains its maximum, M, and minimum, m, on this interval. From the def-
inition of Riemann integral, we have that m a f ðxÞ a M implies that
m
ð b
a
gðxÞ dx a
ð b
a
f ðxÞgðxÞ dx a M
ð b
a
gðxÞ dx;
10.8
Taylor Series with Integral Remainder
599

which in turn implies that
m a
Ð b
a f ðxÞgðxÞ dx
Ð b
a gðxÞ dx
a M:
Since this ratio is between the minimum and maximum values attained by f ðxÞ, we
conclude from the intermediate value theorem in (9.1) of proposition 9.41 that there
is a c A ½a; b so that f ðcÞ equals this ratio.
n
Of course, the expression in (10.12), the first mean value theorem for integrals, is a
special case of this result for which gðxÞ 1 1. Also the Taylor remainders in (10.34)
are another special case, since is is easy to evaluate the remaining integral:
ð x
x0
ðx  zÞn dz ¼ ðx  x0Þnþ1
n þ 1
:
One advantage of the Cauchy form of the remainder is that it reflects an averaging
of the f ðnþ1ÞðzÞ values on the given interval, whereas the Lagrange remainder is a
point estimate. Consequently, to prove convergence of a Taylor series, and hence
the analyticity of a given function, the Cauchy remainder can give more useful esti-
mates than those based on the maximum value of f ðnþ1ÞðzÞ as is required in proposi-
tion 9.103 with the Lagrange remainder.
Recall example 9.106 in the cases for which the Lagrange remainder provided only
partial results.
Example 10.53
1. With f ðxÞ ¼
1
1x ¼ ð1  xÞ1 and x0 ¼ 0, it is easy to justify that f ðnÞðxÞ ¼
n!ð1  xÞn1 and so f ðnÞð0Þ ¼ n!. Although in chapter 6 it was shown that Py
j¼0 x j
converges for jxj < 1, it was seen in example 9.106 that the Lagrange remainder only
proved that
1
1x ¼ Py
j¼0 x j in the case 1 < x a 0, since then the Lagrange remainder
converged to 0 as n ! y. For 0 < x < 1 this remainder diverged. Using the Cauchy
form above, we have
1
n!
ð x
0
f ðnþ1ÞðzÞðx  zÞn dz ¼ ðn þ 1Þ
ð x
0
ð1  zÞn2ðx  zÞn dz
¼ ðn þ 1Þ
ð x
0
x  z
1  z

n
ð1  zÞ2 dz:
600
Chapter 10
Calculus II: Integration

Now on the interval 0 a z a x, where 0 < x < 1, the function gðzÞ ¼ xz
1z is positive and
deceasing and gðzÞ a x. Also on this same interval hðzÞ ¼ ð1  zÞ2 is positive and in-
creasing and hðzÞ a ð1  xÞ2. Consequently we obtain that
1
1  x 
X
n
j¼0
x j


 a ðn þ 1Þ
xn
ð1  xÞ2
ð x
0
dz ¼ ðn þ 1Þ
xnþ1
ð1  xÞ2 ;
and so for 0 < x < 1, this remainder converges to 0 as n ! y. This completes the
demonstration that f ðxÞ ¼
1
1x is an analytic function on ð1; 1Þ and given by the series
expansion
1
1  x ¼
X
y
j¼0
x j;
1 < x < 1:
2. With f ðxÞ ¼ lnð1 þ xÞ we obtain
f 0ðxÞ ¼
1
1 þ x ; f ð2ÞðxÞ ¼
1
ð1 þ xÞ2 ; . . . ; f ðnÞðxÞ ¼ ð1Þnþ1ðn  1Þ!
ð1 þ xÞn
:
Consequently f ð0Þ ¼ 0 and f ðnÞð0Þ ¼ ð1Þn1ðn  1Þ! for n b 1. It was shown in ex-
ample 9.106 that Py
j¼1
ð1Þ jþ1
j
x j converges for jxj < 1 and x ¼ 1. But as in case 1,
the Lagrange remainder only yields a partial result, that lnð1 þ xÞ ¼ Py
j¼1
ð1Þ jþ1
j
x j
in the case of  1
2 a x a 1, since then the Lagrange remainder converged to 0 as
n ! y. For 1 < x <  1
2 this remainder diverged. Using the Cauchy form above
obtains
1
n!
ð x
0
f ðnþ1ÞðzÞðx  zÞn dz ¼ ð1Þnþ2
ð x
0
ðx  zÞnð1 þ zÞn1 dz
¼ ð1Þnþ3
ð0
x
x  z
1 þ z

n
ð1 þ zÞ1 dz;
where it is noted that the limits of integration were reversed and o¤set by multiplica-
tion by 1 to better accommodate the x-values contemplated. Repeating the analysis
above on this integrand, we have that on the interval x a z a 0 for 1 < x <  1
2 ,
the function gðzÞ ¼
xz
1þz


 is positive and increasing and gðzÞ a jxj, while the function
hðzÞ ¼ ð1 þ zÞ1 is positive and decreasing and hðzÞ a ð1 þ xÞ1. We now obtain,
using (10.10),
10.8
Taylor Series with Integral Remainder
601

lnð1 þ xÞ 
X
n
j¼1
ð1Þ jþ1
j
x j


 a
ð0
x
x  z
1 þ z


n
ð1 þ zÞ1 dz
a jxjnþ1
1 þ x ;
and so for 1 < x <  1
2 , this remainder converges to 0 as n ! y. This completes the
demonstration that f ðxÞ ¼ lnð1 þ xÞ is an analytic function on ð1; 1 and given by the
series expansion
lnð1 þ xÞ ¼
X
y
j¼1
ð1Þ jþ1
j
x j;
1 < x a 1:
10.9
Convergence of a Sequence of Integrals
10.9.1
Review of Earlier Convergence Results
An important situation that often arises in mathematics is related to a sequence of
functions ffnðxÞg that is known to converge in some sense to a function f ðxÞ. If
each function in the sequence is known to have a certain property, can it be con-
cluded that f ðxÞ will also have this property? The typical application, of course,
is where the functions are simple in some way and have a desirable property that is
easy to establish, and the question pursued is whether we can infer that this desirable
property is also shared by f ðxÞ.
For example, it was shown in chapter 9 in section 9.2.7 on convergence of a se-
quence of continuous functions that continuity is a property that does not in general
transfer well from the functions fnðxÞ to the function f ðxÞ if convergence is defined
pointwise. In other words, if for each x the numerical sequence fnðxÞ converges to the
point f ðxÞ, it is possible that each function in the sequence is continuous, yet f ðxÞ is
not. The simple example given there was
f ðxÞ ¼
1;
x a 0;
0;
x > 0;

and
fnðxÞ ¼
1;
x a 0;
1  nx;
0 < x a 1
n ;
0;
x > 1
n :
8
>
<
>
:
602
Chapter 10
Calculus II: Integration

Although fnðxÞ ! f ðxÞ for all x, the continuity of fnðxÞ is lost at x ¼ 0 because
the convergence becomes increasingly slow, the closer x is to 0. This insight also pro-
duces the solution to the problem, and that is, if fnðxÞ ! f ðxÞ uniformly, continuity
is preserved, where by ‘‘uniformly’’ is meant that j fnðxÞ  f ðxÞj can be made arbi-
trarily small for all x by making n large enough.
For the property of di¤erentiability, it was shown in section 9.4 on convergence
of a sequence of derivatives that neither pointwise nor uniform convergence of
fnðxÞ ! f ðxÞ was enough to ensure that the di¤erentiability of fnðxÞ would either
imply the di¤erentiability of f ðxÞ or, in the case where f 0ðxÞ existed, imply the con-
vergence f 0
n ðxÞ ! f 0ðxÞ. An example for nonexistence of f 0ðxÞ was given by
fnðxÞ ¼
x1þð1=nÞ;
x b 0;
ðxÞ1þð1=nÞ;
x a 0;

f ðxÞ ¼ jxj;
since here f 0ð0Þ does not exist.
The example for when f 0ðxÞ exists for all x but f 0
n ðxÞ n f 0ðxÞ was given by
fnðxÞ ¼ sin nx
ffiffin
p
;
f ðxÞ 1 0:
10.9.2
Sequence of Continuous Functions
The general questions of this section are:
Question 1:
If fnðxÞ is Riemann integrable over ½a; b for all n and fnðxÞ ! f ðxÞ
pointwise, will it be the case that
Ð b
a f ðxÞ dx exists and
Ð b
a fnðxÞ dx !
Ð b
a f ðxÞ dx?
Question 2:
In general, what kind of convergence of integrable functions fnðxÞ will
ensure integrability of f ðxÞ and the convergence of integral values, and what if any
bearing do properties of the interval of integration have on these results?
As it turns out, question 1 is relatively easy, but question 2 is far more subtle and
di‰cult than is the related investigation on continuity or di¤erentiability. We address
question 1 and an important portion of question 2 here. This discussion will be
greatly expanded within the framework of real analysis.
Answer 1:
Pointwise convergence of
fnðxÞ that are Riemann integrable over
bounded ½a; b assures neither the integrability of f ðxÞ nor, in the case where f ðxÞ is
integrable, the convergence of integral values. Examples of these behaviors follow.
10.9
Convergence of a Sequence of Integrals
603

Example 10.54
1. For any ordering of the rational numbers in ½0; 1, frjgy
j¼1, define
fnðxÞ ¼
1;
x ¼ rj; 1 a j a n;
1
n ;
elsewhere:

Then fnðxÞ is continuous except at n points and hence is integrable, and
Ð 1
0 fnðxÞ dx ¼
1
n . However, fnðxÞ ! f ðxÞ pointwise, where
f ðxÞ ¼
1;
x rational;
0;
x irrational;

which is nowhere continuous and hence not Riemann integrable.
2. Define for n b 1,
fnðxÞ ¼
2n;
1
2n a n a
1
2 n1 ;
0;
elsewhere:

Then fnðxÞ converges pointwise on ½0; 1, but not uniformly, to the continuous and hence
integrable function f ðxÞ 1 0. Also, for all n, a simple calculation gives that
Ð 1
0 fnðxÞ dx
¼ 1, but obviously,
Ð 1
0 f ðxÞ dx ¼ 0.
Answer 2:
The next two propositions in this and the next section provide two cases
where the desired conclusions follow. The first result calls for the uniform conver-
gence of continuous functions on a bounded interval, the second, found in the next
section, generalizes this result.
Proposition 10.55
If f fnðxÞg is a sequence of continuous functions on a closed and
bounded interval ½a; b, and there is a function f ðxÞ so that fnðxÞ ! f ðxÞ uniformly,
then f ðxÞ is Riemann integrable and
ð b
a
fnðxÞ dx !
ð b
a
f ðxÞ dx:
ð10:36Þ
In other words,
ð b
a
f ðxÞ dx ¼ lim
n!y
ð b
a
fnðxÞ dx:
ð10:37Þ
Proof
First o¤,
Ð b
a fnðxÞ dx exists for all n, since these functions are continuous and
the interval is bounded. Also uniform convergence assures the continuity of f ðxÞ by
604
Chapter 10
Calculus II: Integration

proposition 9.51, and hence the existence of
Ð b
a f ðxÞ dx, so the only question is one of
convergence of the values of the integrals in (10.36), that
Ð b
a ½ fnðxÞ  f ðxÞ dx ! 0.
To this end, uniform convergence implies that for any  > 0 there is an NðÞ so that
j fnðxÞ  f ðxÞj <  for all x A ½a; b for n > N. Hence for any partition a ¼ x0 < x1
<    < xn ¼ b, where yj A ½xjþ1  xj, the Riemann sum is bounded:
X
j
½ fnðyjÞ  f ðyjÞ½xjþ1  xj


 a
X
j fnðyjÞ  f ðyjÞj½xjþ1  xj
< 
X
½xjþ1  xj
¼ ðb  aÞ;
n > N:
Consequently
Ð b
a ½ fnðxÞ  f ðxÞ dx ! 0, and because of the linearity of the integral in
(10.9) this result is equivalent to demonstrating (10.36).
n
Remark 10.56
Note that (10.37) can be rewritten to emphasize that this is another
example of reversing the order of two limiting operations as in proposition 9.58. Recall
that the integral is defined as the limit of Riemann sums, and (10.37) becomes
ð b
a
lim
n!y fnðxÞ
h
i
dx ¼ lim
n!y
ð b
a
fnðxÞ dx


:
10.9.3
Sequence of Integrable Functions
The preceding result can be generalized, in that the assumption of the continuity of
fnðxÞ can be relaxed to just the assumptions of boundedness and Riemann integrable.
Proposition 10.57
If ffnðxÞg is a sequence of bounded, Riemann integrable functions
on a closed and bounded interval ½a; b, and there is a function f ðxÞ so that fnðxÞ !
f ðxÞ uniformly, then f ðxÞ is Riemann integrable and (10.36) holds.
Proof
First o¤, we show f ðxÞ is indeed Riemann integrable. By the characteriza-
tion of integrability on bounded intervals in the Riemann existence theorem of prop-
osition 10.22, it is enough to prove that f ðxÞ is bounded and continuous except on a
set of measure zero.
To this end, let En denote the set of discontinuity points of fnðxÞ that has measure
0 because of the integrability assumption, and let E ¼ 6 En. Then E also has mea-
sure 0 by proposition 10.16, and we will show that f ðxÞ is continuous outside E. It is
important to note that f ðxÞ will also in general be continuous on many, even all, of
10.9
Convergence of a Sequence of Integrals
605

the points in E, but we cannot be assured of this and in any case do not need this for
the desired result.
By uniform convergence we have that for any  > 0 there is an N ¼ NðÞ so that
j f ðyÞ  fnðyÞj <  for all y A ½a; b and all n b N. Let x A ½a; b  E, and since fNðxÞ
is continuous at x, there is a dN for this same  so that j fNðxÞ  fNðyÞj <  if jx  yj
< dN. By the triangle inequality, if jx  yj < dN, then
j f ðxÞ  f ðyÞj a j f ðxÞ  fNðxÞj þ j fNðxÞ  fNðyÞj þ j fNðyÞ  f ðyÞj
< 3;
and so f ðxÞ is continuous outside E, a set of measure 0.
Boundedness of f ðxÞ also follows from the uniform convergence and the bounded-
ness of fnðxÞ. For n b N above,
j f ðxÞj a j f ðxÞ  fnðxÞj þ j fnðxÞj
<  þ Cn;
where Cn denotes the maximum of bounded j fnðxÞj on ½a; b.
To next show the convergence of integrals in (10.36), uniform continuity implies
that for all x A ½a; b and n b N,
 < f ðxÞ  fnðxÞ < ;
which implies that for n b N,
ðb  aÞ <
ð b
a
½ f ðxÞ  fnðxÞ dx < ðb  aÞ:
As  is arbitrary, this demonstrates (10.36).
n
10.9.4
Series of Functions
As was the case in section 9.27 on sequences of continuous functions and section 9.4
on sequences of di¤erentiable functions, the propositions above on sequences of inte-
grable functions easily yield comparable results on series of functions which converge
uniformly. We state only the more general case.
Proposition 10.58
If gjðxÞ is a sequence of bounded, Riemann integrable functions,
and there is a function gðxÞ so that on some interval ½a; b the series Py
j¼1 gjðxÞ con-
verges uniformly to gðxÞ, then gðxÞ is Riemann integrable, and Pn
j¼1
Ð b
a gjðxÞ dx !
Ð b
a gðxÞ dx as n ! y.
606
Chapter 10
Calculus II: Integration

Remark 10.59
The uniform convergence of a series of integrable functions yields an
integrable function whose integral equals the sum of the integrals of terms in the series.
That is, uniform convergence justifies integrating term by term, then summing, which
means
ð b
a
gðxÞ dx ¼ lim
n!y
X
n
j¼1
ð b
a
gjðxÞ dx:
Proof
Define fnðxÞ ¼ Pn
j¼1 gðxÞ. Then fnðxÞ is bounded and Riemann integrable
for all n as a finite sum of bounded integrable functions, and by assumption,
fnðxÞ ! gðxÞ uniformly. Also
Ð b
a fnðxÞ dx 1 Pn
j¼1
Ð b
a gjðxÞ dx. So the result follows
from proposition 10.57.
n
10.9.5
Integrability of Power Series
We next apply the above result on series of functions to the special case of a power
series. It is largely a corollary to the proposition above on series of functions, but it is
stated here to clarify that a small amount of thought needs to be applied to ensure
the uniformity of convergence as the above result requires.
Proposition 10.60
Assume that a function f ðxÞ is defined by the power series
f ðxÞ ¼
X
y
j¼0
cjðx  x0Þ j
ð10:38Þ
and has an interval of convergence given by I ¼ fx j jx  x0j < Rg for some R > 0.
Then f ðxÞ is Riemann integrable on any bounded interval ½a; b H I, and
ð b
a
f ðxÞ dx ¼
X
y
j¼0
cj
j þ 1 ½ðb  x0Þ jþ1  ða  x0Þ jþ1:
ð10:39Þ
In other words, a power series can be integrated term by term within its interval of
convergence.
Proof
Of course, f ðxÞ is infinitely di¤erentiable as was demonstrated in section
9.42, and hence it is continuous on I and Riemann integrable on any bounded inter-
val within I. Define fnðxÞ as the partial summation associated with f ðxÞ,
fnðxÞ ¼
X
n
j¼0
cjðx  x0Þ j:
10.9
Convergence of a Sequence of Integrals
607

The function fnðxÞ is continuous and hence Riemann integrable for all n. As a finite
summation the integral is given as
ð b
a
fnðxÞ dx ¼
X
n
j¼0
ð b
a
cjðx  x0Þ j dx
¼
X
n
j¼0
cj
j þ 1 ½ðb  x0Þ jþ1  ða  x0Þ jþ1:
Because fnðxÞ ! f ðxÞ pointwise on jx  x0j < R, this convergence is uniform on the
compact ½a; b H I by exercise 30(b) of chapter 9. So by proposition 10.55:
ð b
a
f ðxÞ dx ¼ lim
n!y
ð b
a
fnðxÞ dx
¼
X
y
j¼0
cj
j þ 1 ½ðb  x0Þ jþ1  ða  x0Þ jþ1:
n
Remark 10.61
1. Note that in this result on the integral of a series of functions, it is apparent that the
series of integrals is convergent, in fact absolutely convergent. First o¤, by the triangle
inequality,
X
y
j¼0
cj
j þ 1 ½ðb  x0Þ jþ1  ða  x0Þ jþ1


a
X
y
j¼0
jcjj
j þ 1 jðb  x0Þj jþ1 þ
X
y
j¼0
jcjj
j þ 1 jða  x0Þj jþ1:
Now, by the ratio test, for any x A I,
lim sup
j!y
jcjþ1j
jþ2 jðx  x0Þj jþ2
jcjj
jþ1 jðx  x0Þj jþ1 ¼ lim sup
j!y
jcjþ1j
jcjj jðx  x0Þj;
and this limit is less than 1 exactly when jðx  x0Þj < R, since by definition,
1
R ¼
lim supj!y
jcjþ1j
jcjj .
608
Chapter 10
Calculus II: Integration

2. This proposition applies to absolutely convergent Taylor series of analytic functions,
of course, since the partial sums of these converge pointwise and hence uniformly on
any bounded interval, ½a; b.
10.10
Numerical Integration
When an integral of a function f ðxÞ is required, there may be no apparent way to
apply the result of the Fundamental Theorem of Calculus version I because the given
function is not the derivative of a recognized function. In such a case a numerical
algorithm is required, and there are many to choose from.
The most basic approach comes from the definition of the Riemann integral itself,
in (10.5). We simply partition the interval into a finite collection of subintervals,
of equal or unequal size, choose a point from each subinterval, and use the
approximation:
ð b
a
f ðxÞ dxA
X
n
i¼1
f ð~xiÞDxi;
where
~xi A a þ
X
i1
j¼1
Dxj; a þ
X
i
j¼1
Dxj
"
#
:
This is an approximation to the result because, by definition, the exact value of the
integral is produced by this procedure as the mesh size of the partition m, defined in
(10.3), converges to 0. What is unknown, of course, is the quality of this approxima-
tion for a given partition, or the rate at which the error of the approximation goes to
0 as m ! 0.
In the following, we consider only the case of equal partitions, where m ¼
Dx 1 ba
n .
10.10.1
Trapezoidal Rule
One useful way of defining the ‘‘quality of an approximation methodology’’ is to
determine the class of functions for which the methodology produces an exact re-
sult. The bigger the class, the better is the quality of the approximation. For example,
upper and lower Riemann sums will, in general, only provide an exact answer for
a constant function f ðxÞ ¼ d, or more generally, a piecewise constant function
f ðxÞ ¼ di for x A ½xi; xiþ1, where x0 ¼ a and xn ¼ b. This piecewise constant func-
tion is also known as a step function.
10.10
Numerical Integration
609

Using a slight modification of this technique, we can expand this class of functions
to include all linear or a‰ne functions f ðxÞ ¼ cx þ d, as well as piecewise linear
functions f ðxÞ ¼ cix þ di for x A ½xi; xiþ1. The simple modification involves defining
f ð~xiÞ in the Riemann summation above at the midpoint of the interval or, more gen-
erally, for other applications, replacing f ð~xiÞ with the average of the value of the
function at the endpoints of each subinterval:
ð b
a
f ðxÞ dxA
X
n
i¼1
f ðxi1Þ þ f ðxiÞ
2


Dx:
This methodology produces what is known as the trapezoidal rule and can be re-
written as
ð b
a
f ðxÞ dxA 1
2
f ðx0Þ þ 2
X
n1
i¼1
f ðxiÞ þ f ðxnÞ
"
#
Dx:
ð10:40Þ
It is apparent from geometric considerations that this approximation is exact for
a‰ne functions, and for properly chosen partitions, piecewise a‰ne functions.
To evaluate the error in this approximation, recall from (10.6) that we can evalu-
ate this integral over each subinterval separately, and then simply add up the results.
Similarly we can investigate the quality of a proposed approximation over each sub-
interval, and the overall error of the approximation is simply the sum of the
subinterval errors.
For notational simplicity we evaluate the trapezoidal approximation over the first
subinterval, ½a; a þ Dx. From the Taylor series expansion in (9.33) with n ¼ 1 and
x0 ¼ a, and assuming continuous f ð2ÞðxÞ, we get
f ðxÞ ¼ f ðaÞ þ f 0ðaÞðx  aÞ þ 1
2 f ð2ÞðyÞðx  aÞ2;
where y 1 yðxÞ and a < yðxÞ < x. Since f ðxÞ is continuous, we infer that f ð2ÞðyÞ is
also a continuous function of x.
Integrating
this
formula
over
the
interval
½a; a þ Dx
produces
for
I 1
Ð aþDx
a
f ðxÞ dx,
I ¼ f ðaÞDx þ 1
2 f 0ðaÞDx2 þ 1
2
ð aþDx
a
f ð2ÞðyðxÞÞðx  aÞ2 dx
¼ f ðaÞDx þ 1
2 f 0ðaÞDx2 þ 1
3! f ð2ÞðzÞDx3:
610
Chapter 10
Calculus II: Integration

Note that the last step is justified by the second MVT for integrals in (10.35) applied
to the function f ð2ÞðyðxÞÞ. In other words, f ð2ÞðzÞ is defined as f ð2ÞðyðcÞÞ for some
c A ½a; a þ Dx, and consequently since a < yðxÞ < x, we conclude that z A ½a; a þ Dx.
The trapezoidal approximation over this interval, using the Taylor expansion
above, is:
I T ¼ 1
2 ½ f ðaÞ þ f ða þ DxÞDx
¼ 1
2 2f ðaÞDx þ f 0ðaÞDx2 þ 1
2 f ð2ÞðyÞDx3


;
where y 1 yðDxÞ and a < yðDxÞ < a þ Dx. Subtracting these expressions produces
I  I T ¼  1
4 f ð2ÞðzÞ  1
6 f ð2ÞðyÞ


Dx3
for a < y; z < a þ Dx:
Finally, for d > b > 0, consider the expression
df ð2ÞðzÞ  bf ð2ÞðyÞ
d  b
¼ f ð2ÞðzÞ þ
b
d  b ½ f ð2ÞðzÞ  f ð2ÞðyÞ:
It is apparent that this expression is strictly between f ð2ÞðzÞ and f ð2ÞðyÞ, and hence
by the continuity of f ð2ÞðxÞ and the intermediate value theorem in (9.1), there is a w
between y and z so that f ð2ÞðwÞ ¼ df ð2ÞðzÞbf ð2ÞðyÞ
db
. Applying this to the trapezoidal ap-
proximation above, where d ¼ 1
4 and b ¼ 1
6 , we conclude that
I  I T ¼  1
12 f ð2ÞðwÞDx3
for a < w < a þ Dx:
Summarizing, we have derived the following result:
Proposition 10.62
If f ðxÞ is a twice di¤erentiable function with continuous f ð2ÞðxÞ on
the bounded interval ½a; b, with partition given by fxign
i¼0 ¼ fa þ iDxgn
i¼0 and Dx ¼
ba
n , then the error in the trapezoidal approximation defined in (10.40) is given by
I  I T ¼  1
12 f ð2ÞðwÞ ðb  aÞ3
n2
ð10:41Þ
for some w A ½a; b. If j f ð2ÞðxÞj a M2 on ½a; b, the absolute error bound is given by
jI  I Tj a M2ðb  aÞ3
12n2
:
ð10:42Þ
10.10
Numerical Integration
611

Proof
Applying the analysis above to each subinterval and adding, we derive
I  I T ¼  1
12
X
n
i¼1
f ð2ÞðwiÞDx3
for a þ ði  1ÞDx < wi < a þ iDx. Now, since 1
n
Pn
i¼1 f ð2ÞðwiÞ is bounded by the max-
imum and minimum values of f ð2ÞðxÞ on ½a; b, by the intermediate value theorem
there is a w A ½a; b that equals this value. Substituting Dx ¼ ba
n completes the proof
of (10.41). From this, (10.42) follows by taking absolute values and bounding f ð2ÞðwÞ
by its maximum, M2.
n
Remark 10.63
Note that the error estimate of the trapezoidal approximation is
OðDx2Þ. Specifically, since Dx ¼ ba
n , we have from (10.42) that
jI  I Tj a M2ðb  aÞ
12
Dx2:
ð10:43Þ
10.10.2
Simpson’s Rule
With a bit more e¤ort, Simpson’s rule improves the error in the trapezoidal rule ap-
proximation from OðDx2Þ to OðDx4Þ. The additional e¤ort required is to utilize the
midpoint and endpoints from each subinterval defined by the partition above, rather
than just the endpoints. However, Simpson’s rule requires the continuity of the fourth
derivative f ð4ÞðxÞ on ½a; b.
Specifically, on a given subinterval, say ½a; a þ Dx for simplicity, the Simpson’s
rule approximation is defined as
ð aþDx
a
f ðxÞ dxA 1
6
f ðaÞ þ 4f
2a þ Dx
2


þ f ða þ DxÞ


Dx;
where Dx ¼ ba
n . Adding over all subintervals produces Simpson’s rule:
ð b
a
f ðxÞ dxA 1
6
X
n
i¼1
f ðxi1Þ þ 4f
xi1 þ xi
2


þ f ðxiÞ


Dx:
In terms of the resulting coe‰cients of the function values, a simple calculation
produces the following:
ð b
a
f ðxÞ dxA 1
6
f ðx0Þ þ 2
X
n1
i¼1
f ðxiÞ þ 4
X
n
i¼1
f
xi1 þ xi
2


þ f ðxnÞ
"
#
Dx:
ð10:44Þ
612
Chapter 10
Calculus II: Integration

The development of the error in this approximation follows that above for the
trapezoidal rule but utilizes the Taylor approximation up to the f ð4ÞðxÞ term. We
present the final result of these calculations without proof (see exercise 12):
Proposition 10.64
If f ðxÞ is a four times di¤erentiable function with continuous
f ð4ÞðxÞ on the bounded interval ½a; b, with partition given by fxign
i¼0 ¼ fa þ iDxgn
i¼0
and Dx ¼ ba
n , then the error in Simpson’s rule defined in (10.44) is given by
I  I S ¼  1
180 f ð4ÞðwÞ ðb  aÞ5
ð2nÞ4
ð10:45Þ
for some w A ½a; b. If j f ð4ÞðxÞj a M4 on ½a; b, the absolute error bound is given by
jI  I Sj a M4ðb  aÞ5
180ð2nÞ4 :
ð10:46Þ
Remark 10.65
Note that the error estimate of Simpson’s rule is OðDx4Þ. Specifically,
since Dx ¼ ba
n , we have from (10.46) that
jI  I Tj a M4ðb  aÞ
2880
Dx4:
ð10:47Þ
10.11
Continuous Probability Theory
10.11.1
Probability Space and Random Variables
Recall that chapter 6 on series provided the needed tools to develop most of a dis-
crete probability theory. Exceptions included (7.67), which required some chapter 9
tools, and the statement that the moment-generating function or characteristic func-
tion uniquely characterize a probability density, addressed somewhat in section 8.1.
Similarly the tools of Riemann integration in this chapter 10 are su‰cient to develop
most of the ‘‘continuous’’ counterpart to this theory.
As in chapter 7, we begin with a sample space, S, which we do not require to be
finite or discrete as was the case for discrete probability theory. We might imagine S
to be the real numbers R or Euclidean space Rn, for example. The critical observa-
tion in this generalization is that we can no longer rely on the restriction that S has a
countable collection of sample points.
In this section we introduce many of the relevant aspects of this continuous theory,
and provide a more general ‘‘mixed’’ discrete and continuous model in exercises 40
through 42. The more formal and mathematically more complete development,
10.11
Continuous Probability Theory
613

which provides a framework for an even more general probability theory which
encompasses both the discrete and continuous theories, and more, requires the tools
of real analysis.
Given S, we define the complete collection of events as in definition 7.2, but begin
to emphasize the alternate terminology noted in remark 7.3.
Definition 10.66
Given a sample space, S, a collection of events, E ¼ fA j A HSg, is
called complete, or is a sigma algebra, if it satisfies the following properties:
1. j;S A E.
2. If A A E, then ~
A A E.
3. If Aj A E for j ¼ 1; 2; 3; . . . , then 6j Aj A E.
In other words, we require that a sigma algebra of events contain the null event j,
the certain event S, the complement of all events, and that it be closed under count-
able unions. However, while item 3 is stated only for countable unions, it is also true
for countable intersections because of property 2 and De Morgan’s laws. Hence it is
also the case that 7j Aj A E. Similarly, if A; B A E, then A @ B A E, where A @ B 1
fx A S j x A A and x B Bg, since A @ B ¼ A V ~B.
Remark 10.67
1. In the discrete sample spaces of chapter 7, E usually contained each of the sample
points and all subsets of S, and was consequently always complete. In a general sample
space that is uncountably infinite, the collection of events will virtually always be a
proper subset of the collection of all subsets. Consequently the structure of the collec-
tion of events implied by the sigma algebra definition is all that we will have to work
with, and hence all that can be assumed about E in the development of this theory.
2. It was noted in chapter 7 that the use of the term ‘‘complete’’ was not standard, but
was introduced there for simplicity. The three conditions in the definition above are
general requirements for E to be a sigma algebra, and this is a more natural language
here given the greater generality of this collection.
3. Although perhaps not formally, but at least intuitively, it should be clear that the
generality of the definition of a sigma algebra of events implies that on any given sam-
ple space, any number of sigma algebras can be defined as long as they satisfy the con-
ditions above. Once that is contemplated, it becomes clear that one might find two
sigma algebras, E and E 0 where E HE 0 in the sense that every event in E is an event in
E 0. In that sense, E 0 is a finer sigma algebra because it contains more events, and E a
coarser sigma algebra because it contains fewer events. One also imagines that there
614
Chapter 10
Calculus II: Integration

may be two sigma algebras where neither E HE 0 nor E 0 HE is true. Outstanding ques-
tions to be pursued in more advanced treatments using the tools of real analysis are:
 If D is any collection of subsets of S, is there a sigma algebra E that contain the sets
in D so that D HE?
 If yes, is there a smallest such sigma algebra?
For example, if E and E 0 are two sigma algebras on S, is there a sigma algebra E 00
so that E UE 0 HE 00? For another example, if X : S ! R is a given function, is there
a sigma algebra that contains all sets of the form X 1ða; bÞ for all open intervals
ða; bÞ H R?
The notion of a probability measure on E is identical to that in chapter 7. Because
of the generality of the event space and the fact that E does not contain sample points
as events, we use the general notation m, which is standard in the theory, rather than
the notation for the discrete theory of Pr.
Definition 10.68
Given a sample space S, and a sigma algebra of events E ¼ fA j
A HSg, a probability measure is a function m : E ! ½0; 1, which satisfies the following
properties:
1. mðSÞ ¼ 1.
2. If A A E, then mðAÞ b 0 and mð ~
AÞ ¼ 1  mðAÞ.
3. If Aj A E for j ¼ 1; 2; 3; . . . are mutually exclusive events, that is, with Aj V Ak ¼ j
for all j 0 k, then
m 6
j
Aj
 
!
¼
X
mðAjÞ:
In this case the triplet: ðS;E; mÞ is called a probability space.
Definition 10.69
An event A A E is a null event under m if mðAÞ ¼ 0. If A is a null
event and every A0 H A satisfies:
1. A0 A E,
2. mðA0Þ ¼ 0,
then the triplet, ðS;E; mÞ is called a complete probability space.
Remark 10.70
Questions on probability spaces to be pursued in more advanced treat-
ments using the tools of real analysis are:
1. If ðS;E; mÞ is a probability space that is not complete, can E be expanded to a sigma
algebra E 0 that is complete and hence includes all subsets of null sets?
10.11
Continuous Probability Theory
615

2. If ðS;E; mÞ is a probability space which is not complete, and E is expanded to include
all subsets of null sets, can the definition of m be expanded to E 0 without changing its
values on E?
3. Given ðS;E; mÞ, define n-trial sample space, denoted S n, by
S n ¼ fðs1; s2; . . . ; snÞ j sj A Sg:
How can an associated sigma algebra of events E n be defined and reflective of the sigma
algebra E? Also, how can a probability measure mnðAÞ be defined for A A E n in a way
that allows the identification of up to n-events in E with n-independent events in E n,
which have the same probability measures?
So far not too much of what has been defined is materially di¤erent from the dis-
crete setting of chapter 7. What really distinguishes the discrete and continuous mod-
els is the nature of a random variable defined on S.
Definition 10.71
Given a sample space S, and a sigma algebra of events E ¼ fA j A H
Sg, a continuously distributed random variable is a function
X : S ! R;
so that:
1. For any bounded or unbounded interval fa; bg H R, where fa; bg denotes that this
interval may be open, closed, or half-open,
X 1fa; bg A E:
2. There is a continuous function, denoted f or fX, with f ðxÞ b 0, the probability
function (p.f.), or probability density function (p.d.f.) of X so that given any interval
fa; bg,
ð b
a
f ðxÞ dx ¼ m½X 1fa; bg:
ð10:48Þ
The distribution function (d.f.), or cumulative distribution function (c.d.f.) associ-
ated with X, denoted F or FX, is then defined on R by
FðxÞ ¼ m½X 1ðy; x
ð10:49aÞ
¼
ð x
y
f ðyÞ dy:
ð10:49bÞ
616
Chapter 10
Calculus II: Integration

Note that for any point a A R, X 1½a A E, since X 1 a; a þ 1
n


A E for all n, and by
the property of a sigma algebra,
7
n
X 1 a; a þ 1
n


¼ X 1½a A E:
Of course, if a B Rng½X, then X 1½a ¼ j. Also, by (10.48), it must be the case that
m½X 1½a ¼ 0
for all a A R:
Consequently the pre-image of any point under X has probability measure 0 and is
a null event in E. In addition the pre-image of any countable collection of points is
again a null event, since given fajgy
j¼1, the collection of events fX 1½ajgy
j¼1 are mu-
tually exclusive since X is a function, and so by definition 10.68,
m 6
j
X 1½aj
"
#
¼
X
j
m½X 1½aj ¼ 0:
Remark 10.72
These conclusions highlight a stark contrast between continuous and
discrete probability theory. In chapter 7, given any random variable X, there is a finite
or countable collection fajgy
j¼1 H R so that fX 1½ajgy
j¼1 HE are mutually independent
events, and Pr½6j X 1½aj ¼ 1. In continuous probability theory, for any collection
fajgy
j¼1 H R, while it is still true that fX 1½ajgy
j¼1 HE and are mutually independent
events, we now have m½6j X 1½aj ¼ 0.
Note that since the c.d.f. is the integral of a continuous function, we have from the
Fundamental Theorem of Calculus version II that FðxÞ is a di¤erentiable function
and
F 0ðxÞ ¼ f ðxÞ:
ð10:50Þ
Note also from the definition of FðxÞ that:
1. FðyÞ ¼ 1, since FðxÞ ¼ m½X 1ðy; xÞ, and as x ! y, m½X 1ðy; xÞ ! mðSÞ
¼ 1.
2. FðxÞ is nondecreasing, that is, x < x0 ) FðxÞ a Fðx0Þ, since f ðxÞ b 0 and by
(10.49),
Fðx0Þ  FðxÞ ¼
ð x 0
x
f ðyÞ dy b 0:
10.11
Continuous Probability Theory
617

3. FðyÞ ¼ 0, since for any x we have S ¼ X 1ðy; x U X 1ðx; yÞ. Consequently
FðxÞ ¼ m½X 1ðy; x ¼ 1  m½X 1ðx; yÞ;
and by item 1 above, FðxÞ ! 0 as x ! y.
Remark 10.73
Note that no comment has been made about the random variable X
being a continuous function defined on S. It would seem natural that a continuous prob-
ability theory ought to be the probability theory of continuous random variables. But to
do so would require that S has more structure than is guaranteed by the sigma algebra
of events. Specifically, in order to be able to define that X is a continuous function
requires either that:
1. S is a metric space so X can be defined to be continuous in the usual   d sense, or
equivalently, by the condition that X 1½G is open for any open G H R, or
2. S is a topological space, so X can be defined to be continuous by the condition that
X 1½G is open in S for any open G H R.
Since it also must be the case that X 1½G HE for all intervals and hence all open sets,
the sigma algebra must then be defined to contain all the open sets in S. In other words,
in order to be able to define X to be a continuous random variable requires that S have
a topology of sets, and that the sigma algebra E contain all these open sets. In more
advanced treatments based on the tools of real analysis, the minimal sigma algebra
with this property will be called a Borel sigma algebra, and the associated events called
Borel sets, after E´ mile Borel (1871–1956).
While this extra structure is needed to define the notion of a continuous random vari-
able, it would not be enough to ensure, without a lot of math tools we have not yet
developed, that there is a continuous function f ðxÞ so that (10.48) is satisfied. So this
development is circumvented and continuous probability theory is, in e¤ect, defined
as the probability theory of random variables with continuous probability density
functions.
10.11.2
Expectations of Continuous Distributions
The general structure of the formulas below will be seen to be analogous to those in
section 7.5.1. These formulas again represent what are known as expected value cal-
culations, and sometimes referred to as taking expectations. The general structure of
this calculation is defined first and then specific examples are presented.
Definition 10.74
Given a continuously distributed random variable X : S ! R with
continuous probability density function f ðxÞ, and a continuous function gðxÞ defined on
618
Chapter 10
Calculus II: Integration

the range of X, Rng½X H R, the expected value of gðXÞ, denoted E½gðXÞ, is defined
as
E½gðXÞ ¼
ðy
y
gðxÞ f ðxÞ dx;
ð10:51Þ
as long as the associated integral is absolutely convergent. In other words, since
f ðxÞ b 0, it is required that
ðy
y
jgðxÞj f ðxÞ dx < y:
ð10:52Þ
If (10.52) is not satisfied, we say that E½gðXÞ does not exist.
Remark 10.75
1. If there is a small disappointment in the above definition vis-a-vis the discrete case in
definition 7.35, it is that there is no natural counterpart to formula (7.35):
E½gðXÞ ¼
X
sj AS
gðXðsjÞÞ PrðsjÞ;
where fxjg H R denotes the range of X. In other words, in chapter 7 expected values
could be equivalently defined as a calculation on S using the probability measure Pr, or
as a calculation on R using the probability density function f ðxÞ. At the moment, with-
out the more general tools of real analysis, there is no way to define E½gðXÞ as a cal-
culation on S using the probability measure m. If there was, we might expect that this
definition would look something like:
E½gðXÞ ¼
ð
S
gðXðsÞÞ dmðsÞ;
although some amount of work needs to be done to define exactly what such an integral
means.
2. The condition in (10.52) is automatically satisfied if gðxÞ is a bounded function on
the range of X, jgðxÞj a K, since then
ðy
y
jgðxÞj f ðxÞ dx a K
ðy
y
f ðxÞ dx ¼ K:
So this restriction is ‘‘only’’ important for unbounded functions. That said, in practice
we are primarily interested in the expected value of unbounded functions, so this condi-
tion cannot in general be assumed to be valid.
10.11
Continuous Probability Theory
619

*10.11.3
Discretization of a Continuous Distribution
The goal of this section is to better link the notions of expected value in the discrete
and continuous contexts. At the moment it might appear that the summations of def-
inition 7.35 of chapter 7 were simply converted to integrals. To see why this is the
correct answer, and not just a notational trick, we begin with a somewhat long defi-
nition. The idea is simple and natural, but it takes a lot of words to convey.
Definition 10.76
Given a continuously distributed random variable, X : S ! R, a dis-
cretization of X of mesh size d, denoted Xd, is a discrete random variable defined on the
discretization of the sample space S, denoted Sd, constructed as follows:
1. A partition of R is defined with mesh size, d. In other words, there is given
fxigy
i¼0; fyigy
i¼0 H R, with
   < y2 < y1 < y0 ¼ x0 < x1 < x2 <    ;
with xiþ1  xi a d and yi  yiþ1 a d for all i, and the partition is defined as
f½xi; xiþ1Þgy
i¼0 U f½yiþ1; yiÞgy
i¼0.
2. From each partition interval is chosen a point, or interval tag,
~xi A ½xi; xiþ1Þ;
~yi A ½yiþ1; yiÞ;
i b 0:
3. Mutually exclusive events are defined in E by
Aþ
i ¼ X 1½xi; xiþ1Þ;
A
i ¼ X 1½yiþ1; yiÞ;
i b 0:
Then Sd is defined as the discrete sample space in which these events are sample points
Sd ¼ fAþ
i gy
i¼0 U fA
i gy
i¼0;
ð10:53Þ
with the complete collection of events, denoted Ed, defined as these sample points plus
all unions and complements of unions of these sample points.
The probability measure, Prd, is then defined on sample points by
Prd½Aþ
i  ¼ m½X 1½xi; xiþ1Þ;
ð10:54aÞ
Prd½A
i  ¼ m½X 1½yiþ1; yiÞ;
ð10:54bÞ
and extended additively to all events, where in this definition, X 1½xi; xiþ1Þ and
X 1½yiþ1; yiÞ are considered as events in S.
620
Chapter 10
Calculus II: Integration

Finally, the discrete random variable Xd : Sd ! R is defined by
XdðAþ
i Þ ¼ ~xi;
XdðA
i Þ ¼ ~yi;
ð10:55Þ
with associated probability density function, fdðxÞ, defined by
fdð~xiÞ 1 Prd½X 1
d ½~xi ¼ Fðxiþ1Þ  FðxiÞ;
ð10:56aÞ
fdð~yiÞ 1 Prd½X 1
d ½~yi ¼ FðyiÞ  Fðyiþ1Þ:
ð10:56bÞ
Example 10.77
Other continuous distributions are introduced below, but the unit
normal distribution was introduced in section 8.6 and can be discretized as follows.
In the background is ðS;E; mÞ, representing a sample space, sigma algebra, and proba-
bility measure, and also a continuously distributed random variable X : S ! R. So
for any interval fa; bg, which we take to be closed for definitiveness, we have that
X 1½a; b A E and
m½X 1½a; b ¼
1ffiffiffiffiffi
2p
p
ð b
a
ex2=2 dx:
Although not necessary, it is natural to define a discretization that is symmetric in
terms of the collection of interval tags since fðxÞ ¼
1ffiffiffiffi
2p
p
ex2=2 is symmetric about
x ¼ 0. To this end, and with mesh size d ¼ 1
n , it is notationally convenient to eliminate
y0 and x0, and define
xi ¼ 2i  1
2n
;
yi ¼ xi; i ¼ 1; 2; 3; . . . ;
and associated events in S by
A0 ¼ X 1  1
2n ; 1
2n


;
Aþ
i ¼ X 1 2i  1
2n
; 2i þ 1
2n


;
A
i ¼ X 1  2i þ 1
2n
;  2i  1
2n


;
i b 1:
The discrete sample space Sd is then defined as the collection of sample points as in
(10.53) with probability measure Prd as in (10.54). In this case, note that with FðxÞ
denoting the normal cumulative distribution function as defined in (10.49):
Prd½A0 ¼ F
1
2n


 F  1
2n


;
10.11
Continuous Probability Theory
621

Prd½Aþ
i  ¼ F 2i þ 1
2n


 F 2i  1
2n


;
Prd½A
i  ¼ F  2i  1
2n


 F  2i þ 1
2n


:
Finally, with interval tags f~xi; ~yig defined as interval midpoints,
~x0 ¼ 0;
~xi ¼ i
n ;
~yi ¼  i
n ;
i b 1;
the discretized normal random variable Xd is defined as
XdðA0Þ ¼ 0;
XdðAþ
i Þ ¼ i
n ;
XdðA
i Þ ¼  i
n ;
i b 1;
with probability density function given in (10.56).
We can compare the cumulative distribution functions of the normal and its discreti-
zation with d ¼ 0:5 in figure 10.4. Note that using midpoint tags produced a balanced
discretization, in that within each interval of the partition, for example, ½0:25; 0:25Þ
the discretized normal c.d.f. is below FðxÞ on ½0:25; 0Þ and above on ½0; 0:25Þ.
Figure 10.4
FðxÞ and FdðxÞ compared for d ¼ 0:5, midpoint tags
622
Chapter 10
Calculus II: Integration

Analogously, left- and right-endpoint tagging produces discretized c.d.f.s that are
almost always above, or below, the continuous c.d.f. FðxÞ.
The connection between expected values in a discrete and continuous context can
now be formulated by the next result. For notational ease, assume yi ¼ xi.
Proposition 10.78
Given a continuously distributed random variable, X : S ! R, and
discretizations of X of mesh size d, Xd, defined on Sd, then for gðxÞ a continuous func-
tion for which (10.52) holds:
E½gðXdÞ ! E½gðXÞ
as d ! 0:
ð10:57Þ
Proof
By (7.36) applied with (10.56),
E½gðXdÞ ¼
X
y
i¼0
gðxþ
i Þ½Fðxiþ1Þ  FðxiÞ þ
X
y
i¼0
gðx
i Þ½FðxiÞ  Fðxiþ1Þ:
We detail the convergence of the first summation, and leave the analogous derivation
for the second summation as an exercise. Now, since FðxÞ is di¤erentiable, the mean
value theorem in (9.22) yields that
Fðxiþ1Þ  FðxiÞ ¼ F 0ðx0
iÞDxi;
where Dxi ¼ xiþ1  xi and x0
i A ðxi; xiþ1Þ. Hence, because F 0ðx0
iÞ ¼ f ðx0
iÞ by (10.50),
X
y
i¼0
gðxþ
i Þ½Fðxiþ1Þ  FðxiÞ ¼
X
y
i¼0
gðxþ
i Þ f ðx0
iÞDxi:
As gðxÞf ðxÞ is a continuous function, it achieves its maximum and minimum in
every compact set, and hence in the closure of every interval in the partition. Conse-
quently for every i there exists xmax
i
; xmin
i
A ½xi; xiþ1 so that
f ðxmin
i
Þgðxmin
i
Þ a gðxþ
i Þf ðx0
iÞ a f ðxmax
i
Þgðxmax
i
Þ:
As gðxÞf ðxÞ is assumed absolutely integrable, it is certainly integrable, and so the
Riemann sums defined by either xmax
i
or xmin
i
converge to this integral as Dxi ! 0.
Consequently, as d ! 0, we have by definition that Dxi ! 0 and can conclude that
X
y
i¼0
gðxþ
i Þ f ðx0
iÞDxi !
ðy
0
gðxÞ f ðxÞ dx:
10.11
Continuous Probability Theory
623

The same argument can be applied to the second summation in the definition of
E½gðXdÞ, which together produces
E½gðXdÞ !
ðy
y
gðxÞf ðxÞ dx:
Finally, this last integral equals E½gðXÞ since by assumption, gðxÞ satisfies (10.52).
n
Remark 10.79
The proposition above was stated with the relatively strong assumption
that gðxÞ is a continuous function. A review of the proof provides the insight that all
that was needed was that: 1) gðxÞ be continuous except on a set of measure 0 so that
Ð y
y gðxÞ f ðxÞ dx is defined, and, 2) gðxÞ is bounded on every bounded interval, so
that we could produce an upper and lower bound for gðxþ
i Þ f ðx0
iÞ on each subinterval.
10.11.4
Common Expectation Formulas
We now list a collection of expectation formulas which includes the moments of X.
As noted above, in each case the expectation is defined only when (10.52) is satisfied.
The notation is consistent with that in section 7.5.1.
nth Moment
m0
n 1
ðy
y
xn f ðxÞ dx;
n ¼ 1; 2; 3; . . .
ð10:58Þ
Mean
m 1 m0
1 ¼
ðy
y
xf ðxÞ dx
ð10:59Þ
nth Central Moment
mn 1
ðy
y
ðx  mÞnf ðxÞ dx;
n ¼ 1; 2; 3; . . .
ð10:60Þ
Variance
s2 1 m2 ¼
ðy
y
ðx  mÞ2f ðxÞ dx
ð10:61Þ
624
Chapter 10
Calculus II: Integration

Standard Deviation
s ¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ðy
y
ðx  mÞ2f ðxÞ dx
s
ð10:62Þ
Moment-Generating Function
MXðtÞ is defined only when the integral is convergent for t in an interval about 0,
MXðtÞ 1
ðy
y
extf ðxÞ dx
ð10:63Þ
Characteristic Function
CXðtÞ 1
ðy
y
eixtf ðxÞ dx
ð10:64Þ
CXðtÞ is defined for all t since by (10.10),
jCXðtÞj a
ðy
y
jeixtj f ðxÞ dx
¼
ðy
y
f ðxÞ dx ¼ 1;
because by Euler’s formula in (2.5), jeixtj ¼ jcos xt þ i sin xtj ¼ 1.
Example 10.80
All of the many formulas in section 7.5.1 involving expectations can
now be shown to be valid in this continuous probability model, except for those that
involve probability density functions of two or more variables. As we do not yet have
either a di¤erential or an integral calculus for these functions, the continuous counter-
parts to the formulas relating to the joint, conditional, and marginal probability densities,
the law of total probability, sample statistics, or sums of independent and identically
distributed random variables must be deferred as an application of multivariate cal-
culus. However, once these tools are developed, these discrete results will again prove
to be applicable in this continuous and in even more general settings.
Examples of formulas that can be derived now follow (see exercises 13 and 32).
1. As in (7.45):
s2 ¼ E½X 2  E½X2:
ð10:65Þ
10.11
Continuous Probability Theory
625

2. As in exercise 12 in chapter 7:
mn ¼
X
n
j¼0
ð1Þnj
n
j


m0
jmnj;
ð10:66aÞ
m0
n ¼
X
n
j¼0
n
j


mjmnj:
ð10:66bÞ
3. As in (7.64) and (7.65):
MXðtÞ ¼
X
y
n¼0
m0
ntn
n! ;
ð10:67Þ
m0
n ¼ MðnÞ
X ð0Þ;
ð10:68Þ
if all moments exist.
4. As in (7.71) and (7.72):
CXðtÞ ¼
X
y
n¼0
m0
nðitÞn
n!
;
ð10:69Þ
m0
n ¼ 1
in CðnÞ
X ð0Þ;
ð10:70Þ
if all moments exist.
10.11.5
Continuous Probability Density Functions
As was the case in section 7.6, there are infinitely many continuous probability den-
sity functions in theory. Specifically, if hðxÞ is any continuous function with abso-
lutely convergent integral,
0 <
ðy
y
jhðxÞj dx ¼ C < y;
then a p.d.f. can be defined by
f ðxÞ ¼
jhðxÞj
Ð y
y jhðxÞj :
626
Chapter 10
Calculus II: Integration

While true in theory, it is another question altogether whether this p.d.f. will be
found to be useful or reflective of the probability density of a random variable of
interest.
In this section we identify several of the common continuous probability distribu-
tions, and some of their properties.
Continuous Uniform Distribution
Perhaps the simplest continuous probability density that can be imagined is one
which assumes the same value on every point. The domain of this distribution is
arbitrary, and is conventionally denoted as the interval ½a; b. The p.d.f. of the contin-
uous uniform distribution, sometimes called the continuous rectangular distribution, is
defined on ½a; b by the density function
fUðxÞ ¼
1
ba ;
x A ½a; b;
0;
x B ½a; b:

ð10:71Þ
It is an easy calculation to derive the mean and variance of this distribution:
mU ¼ 1
2 ðb þ aÞ;
ð10:72aÞ
s2
U ¼ 1
12 ðb  aÞ2:
ð10:72bÞ
Similarly the moment-generating function can be calculated from the integral of
ext, producing
MUðtÞ ¼ ebt  eat
tðb  aÞ ;
t A R:
ð10:73Þ
Although MUðtÞ has an apparent singularity at t ¼ 0, the numerator can be
expanded in a Taylor series, and one finds that
MUðtÞ ¼ 1 þ
X
y
n¼2
bn  an
b  a

 tn1
n! ;
which converges for all t.
Letting a ¼ 0 and b ¼ 1 in these formulas produces the limiting results as n ! y
of the discrete rectangular distribution developed in section 7.6.1. Moreover the dis-
crete rectangular distribution can be seen to be a discretization of this continuous
distribution, with d ¼ 1
n and right-endpoint tags.
10.11
Continuous Probability Theory
627

An example of this density function is seen in figure 10.5.
Beta Distribution
The beta distribution contains two shape parameters v > 0 and w > 0, and it is
defined on the interval ½0; 1 by the density function
fbðxÞ ¼ xv1ð1  xÞw1
Bðv; wÞ
:
ð10:74Þ
Here the beta function Bðv; wÞ is one of the ‘‘special functions’’ in mathematics
defined by a definite integral that, in general, requires numerical evaluation:
Bðv; wÞ ¼
ð1
0
yv1ð1  yÞw1 dy:
ð10:75Þ
By definition, therefore
Ð 1
0 fbðxÞ dx ¼ 1.
If v or w or both parameters are less than 1, the beta density is unbounded at x ¼ 0
or x ¼ 1, or both, and this integral converges as an improper integral discussed
in section 10.6 because the exponent of both x and 1  x exceeds 1. If both
parameters are greater than 1, this density function is 0 at the interval endpoints,
and by the methods of section 9.5 has a unique maximum at x ¼
v1
vþw2 . Examples
Figure 10.5
fUðxÞ ¼ 1
4 , 1 a x a 5
628
Chapter 10
Calculus II: Integration

of this density function are displayed in figure 10.6. In this figure the parameters are
defined by
ðv; wÞ ¼
ð0:5; 0:5Þ;
dashed line,
ð2; 6Þ;
light line,
ð5; 3Þ;
bold line.
8
>
<
>
:
By definition, one has for any positive integer n,
E½xn ¼ Bðv þ n; wÞ
Bðv; wÞ
:
Now the beta function Bðv; wÞ satisfies an important identity that is useful in evaluat-
ing moments of this distribution:
Bðv þ 1; wÞ ¼
v
v þ w Bðv; wÞ;
ð10:76Þ
which is exercise 14.
Applying the iterative formula in (10.76), we have
mb ¼
v
v þ w ;
ð10:77aÞ
Figure 10.6
fbðxÞ ¼ x v1ð1xÞ w1
Bðv; wÞ
10.11
Continuous Probability Theory
629

m0
nb ¼
Y
n1
i¼0
v þ i
v þ w þ i


;
ð10:77bÞ
s2
b ¼
vw
ðv þ wÞ2ðv þ w þ 1Þ
:
ð10:77cÞ
Using this same iterative formula, we derive by mathematical induction that if n, m
are positive integers,
Bðn; mÞ ¼ ðn  1Þ!ðm  1Þ!
ðn þ m  1Þ!
;
ð10:78Þ
which is exercise 33.
Exponential Distribution
The exponential distribution is defined on ½0; yÞ, and with a single scale parameter
l > 0, by the density function:
fEðxÞ ¼ lelx:
ð10:79Þ
It is apparent that
Ð y
0 fEðxÞ dx ¼ 1 as an improper integral for any l > 0, that
fEð0Þ ¼ l and that fEðxÞ is strictly decreasing over ½0; yÞ. This distribution is a spe-
cial case of the gamma distribution discussed next.
Gamma Distribution
The gamma distribution is defined on ½0; yÞ, reflects a scale parameter b > 0 and a
shape parameter c > 0, and is given by the density function
fGðxÞ ¼ 1
b
x
b
 c1ex=b
GðcÞ :
ð10:80Þ
As in the case of the beta distribution, the gamma function GðcÞ is another ‘‘special
function’’ defined by the integral
GðcÞ ¼
ðy
0
yc1ey dy;
c > 0:
ð10:81Þ
When c ¼ 1 and b ¼ 1
l , the gamma density function is the exponential density func-
tion noted above.
The gamma function exists as an improper integral, and for its evaluation both the
unboundedness of the interval and, in the case of c < 1, the unboundedness of the
630
Chapter 10
Calculus II: Integration

integrand near x ¼ 0 must be considered. The fact that
Ð y
0 fGðxÞ dx ¼ 1 then follows
from the substitution y ¼ x
b and (10.81).
When c a 1, the gamma density is a strictly decreasing function, since f 0
GðxÞ < 0,
whereas for c > 1, the gamma density has a unique maximum at x ¼ bðc  1Þ. Also,
as noted above, when c < 1 the gamma density is unbounded at x ¼ 0. Gamma den-
sities are displayed in figure 10.7 for various parameters. In particular, the density
displayed with a bold line is an exponential, with l ¼ 0:5:
ðb; cÞ ¼
ð2; 0:5Þ;
light line,
ð2; 2Þ;
medium line,
ð2; 1Þ;
bold line.
8
>
<
>
:
The gamma function GðcÞ satisfies an iterative formula that is useful for generating
moments of this distribution, and which follows from an integration by parts:
GðcÞ ¼ ðc  1ÞGðc  1Þ:
ð10:82Þ
From the substitution y ¼ x
b ,
E½xn ¼ bnGðc þ nÞ
GðcÞ
;
and this iterative formula produces
Figure 10.7
fGðxÞ ¼ 1
b
x
b
 c1ex=b
GðcÞ
10.11
Continuous Probability Theory
631

mG ¼ bc;
ð10:83aÞ
m0
nG ¼ bn Y
n1
j¼0
ðc þ jÞ;
ð10:83bÞ
s2
G ¼ b2c:
ð10:83cÞ
The moment-generating function can also be calculated (see exercise 15):
MGðtÞ ¼ ð1  btÞc;
jtj < 1
b :
ð10:84Þ
As noted above, when c ¼ 1 and b ¼ 1
l , the gamma density function becomes the ex-
ponential density function, and so the moment and m.g.f. formulas above are easily
converted to that case.
The gamma function GðcÞ satisfies Gð1Þ ¼ 1 by direct integration, so mathematical
induction can be used with (10.82) to prove that for any positive integer n,
GðnÞ ¼ ðn  1Þ!;
ð10:85Þ
and so GðcÞ can be seen to be a continuous generalization of the discrete factorial
function for c > 0. This factorial identity is also the motivation behind defining
0! ¼ 1, which makes perhaps little sense directly. However, considering GðcÞ as a
generalization of this discrete function, the statement 0! ¼ 1 really means that by
(10.85), 0! is defined in terms of the gamma function, and so
0! 1 Gð1Þ ¼ 1:
Cauchy Distribution
The Cauchy distribution, named for Augustin Louis Cauchy (1789–1857), is of inter-
est as an example of a p.d.f. that has no finite moments. This density function is
defined on R as a function of a location parameter, x0 A R, and a scale parameter
l > 0, by
fCðxÞ ¼ 1
pl
1
1 þ
xx0
l

2 :
ð10:86Þ
This function is symmetric about x ¼ x0, at which point fCðx0Þ ¼ 1
pl , the density’s
maximum value. The parameter l is a scaling parameter that determines how
quickly (l small) or how slowly (l large) fCðxÞ decreases from this maximum as
jx  x0j ! y.
632
Chapter 10
Calculus II: Integration

When x0 ¼ 0 and l ¼ 1, this function is the probability density of a ratio of inde-
pendent unit normal random variables, but we do not derive this.
That Ð y
y f ðxÞ dx ¼ 1 as an improper integral follows from two substitutions. First
o¤, substituting y ¼ xx0
l
produces
ðy
y
fCðxÞ dx ¼ 1
p
ðy
y
1
1 þ y2 dy:
The second substitution is
y ¼ tan z, which produces 1 þ y2 ¼ sec2 z. Since
tan z ¼ sin z
cos z , this function can then be di¤erentiated using the tools of chapter 9,
and in particular (9.16), to produce that ðtan zÞ0 ¼ sec2 z. Finally, this substitution
changes the limits of integration from y A ðy; yÞ to z A  p
2 ; p
2


, so
ðy
y
fCðxÞ dx ¼ 1
p
ð p=2
p=2
dz ¼ 1:
This function has no finite moments, even though it would appear by a cancella-
tion argument that m ¼ x0. But recall that in order for an expectation to be defined,
the associated integral must be absolutely convergent. Simplifying the calculation to
x0 ¼ 0 and l ¼ 1, which is equivalent to making a substitution of y ¼ xx0
l , consider
ðy
y
jyj fCðyÞ dy ¼ 2
ðy
0
yfCðyÞ dy
¼ 2
p
ðy
0
y
1 þ y2 dy:
This integral can be explicitly evaluated by the substitution, z ¼ 1 þ y2, producing
ðy
y
jyj fCðyÞ dy ¼ lim
N!y
1
p
ð N
1
dz
z
¼ 1
p lim
N!y½ln zjN
1
¼ 1
p lim
N!y ln N ¼ y:
So the Cauchy distribution has no finite mean nor higher moments, and hence no
moment-generating function. It does have a characteristic function, although (10.70)
10.11
Continuous Probability Theory
633

can not be valid here. As it turns out, CCðtÞ is not di¤erentiable at t ¼ 0 since it is a
function of jtj.
This density is graphed in bold in figure 10.8 with x0 ¼ 0 and l ¼ 1. For compari-
son, also graphed are the standard unit normal density (dashed line) and another
normal but with s ¼
ffiffip
2
p A1:2533 (light line) to have the same maximum value as
the Cauchy. The ‘‘fat tails’’ of the Cauchy density are evident.
Normal Distribution
The normal distribution is defined on ðy; yÞ, and depends on a location parame-
ter, m A R, and a scale parameter, s2 > 0, and is defined by the density function,
where we use exp A 1 eA to simplify notation:
fNðxÞ ¼
1
s
ffiffiffiffiffi
2p
p
exp  ðx  mÞ2
2s2
 
!
:
ð10:87Þ
When m ¼ 0 and s2 ¼ 1, this is known as the unit normal distribution, and often
denoted fðxÞ,
fðxÞ ¼
1ffiffiffiffiffi
2p
p
exp  x2
2


;
ð10:88Þ
introduced in (8.26) with the De Moivre theorem.
Figure 10.8
fCðxÞ ¼ 1
p
1
1þx2 , fðxÞ ¼
1
s ffiffiffiffi
2p
p
exp  x2
2s2

	
634
Chapter 10
Calculus II: Integration

The normal density is displayed in figure 10.8 with m ¼ 0, for s ¼ 1 (dashed line)
and s ¼ 1:2533 (light line).
The substitution y ¼ xm
s into the integral of fNðxÞ shows that this integral equals
the integral of fðyÞ. Unfortunately, there is no approach to demonstrating that this
latter integral has value 1 with the tools currently at our disposal, so a formal proof
will be deferred as an application, surprisingly, of multivariate calculus. We simply
state the result:
ðy
y
fðyÞ dy ¼ 1:
However, since exp  x2
2

	
< xN as x ! y for any N, it is easy to validate that
Ð y
y ynfðyÞ dy < y for any n b 0 using the results from section 10.6 on improper
integrals.
In general, it is easiest to calculate the central moments mnN and to use (10.66b) if
the corresponding moments m0
nN are needed. To this end, note that using the sub-
stitution y ¼ xm
s produces
ðy
y
ðx  mÞnfNðxÞ dx ¼ sn
ðy
y
ynfðyÞ dy:
For n odd, it is apparent that
Ð y
y ynfðyÞ dy ¼ 0, since with the substitution of
z ¼ y in the second integral,
ðy
y
ynfðyÞ dy ¼
ðy
0
ynfðyÞ dy þ
ð0
y
ynfðyÞ dy
¼
ðy
0
ynfðyÞ dy 
ð0
y
ðzÞnfðzÞ dz
¼
ðy
0
ynfðyÞ dy 
ðy
0
znfðzÞ dz
¼ 0:
Here ðzÞn ¼ zn since n is odd, fðzÞ ¼ fðzÞ from (10.88), and the interchange of
limits follows from (10.17).
The mean of the normal is easily calculated from this result with the same
substitution:
10.11
Continuous Probability Theory
635

ðy
y
xfNðxÞ dx ¼
ðy
y
ðsy þ mÞfðyÞ dy
¼ m;
so mN ¼ m.
For n ¼ 2m even, exercise 34 develops the iterative formula:
ðy
y
y2mfðyÞ dy ¼ ð2m  1Þ
ðy
y
y2m2fðyÞ dy;
and this plus mathematical induction will prove that
ðy
y
y2mfðyÞ dy ¼ ð2mÞ!
2mm! :
Combining with the above, we derive
mnN ¼
0;
n ¼ 2m þ 1;
s2mð2mÞ!
2 mm! ;
n ¼ 2m;
(
ð10:89aÞ
mN ¼ m;
ð10:89bÞ
m2N 1 s2
N ¼ s2:
ð10:89cÞ
So predictably the parameters m and s2 equal the mean and the variance of this
distribution.
The final derivation is for the moment-generating function:
MNðtÞ ¼
ðy
y
etxfNðxÞ dx
¼
1
s
ffiffiffiffiffi
2p
p
ðy
y
exp  ðx  mÞ2  2s2tx
2s2
 
!
dx:
Now completing the square produces
ðx  mÞ2  2s2tx ¼ ½x  ðm þ s2tÞ2  2s2t
m þ 1
2 s2t


;
and so
636
Chapter 10
Calculus II: Integration

MNðtÞ ¼
1
s
ffiffiffiffiffi
2p
p
exp
mt þ 1
2 s2t2

 ðy
y
exp  ½x  ðm þ s2tÞ2
2s2
 
!
dx:
The substitution y ¼ xðmþs2tÞ
s
in this integral produces
Ð y
y fðyÞ dy, which equals
ffiffiffiffiffi
2p
p
, and so
MNðtÞ ¼ exp
mt þ 1
2 s2t2


:
ð10:90Þ
Correspondingly for the m.g.f. of the unit normal,
MFðtÞ ¼ exp 1
2 t2


:
ð10:91Þ
An analogous derivation produces the following results for the characteristic
function:
CNðtÞ ¼ exp imt  1
2 s2t2


;
ð10:92Þ
CFðtÞ ¼ exp  1
2 t2


:
ð10:93Þ
Lognormal Distribution
The lognormal distribution is defined on ½0; yÞ, depends on a location parameter
m A R and a shape parameter s2 > 0, and unsurprisingly is intimately related to the
normal distribution introduced in section 8.6 and discussed above. However, to some
the name ‘‘lognormal’’ appears to be opposite of the relationship that exists. Stated
one way, a random variable X is lognormal with parameters ðm; s2Þ if X ¼ eZ where
Z is normal with the same parameters. So X can be understood as an exponentiated
normal. Stated another way, a random variable X is lognormal with parameters
ðm; s2Þ if ln X is normal with the same parameters. The name comes from the second
statement, in that the log of a lognormal is normal.
The probability density function of the lognormal is defined as follows, again using
exp A 1 eA to simplify notation:
fLðxÞ ¼
1
sx
ffiffiffiffiffi
2p
p
exp  ðln x  mÞ2
2s2
 
!
:
ð10:94Þ
The substitution y ¼ ln xm
s
produces
10.11
Continuous Probability Theory
637

ðy
0
fLðxÞ dx ¼
1ffiffiffiffiffi
2p
p
ðy
y
exp  y2
2


dy
¼
ðy
y
fðyÞ dy:
In other words, the integral of the lognormal density over ½0; yÞ equals 1.
This density function is well defined at x ¼ 0, and fLð0Þ ¼ 0. To see this, let
x ¼ ey and consider y ! y. With this transformation,
fLðeyÞ ¼
ey
s
ffiffiffiffiffi
2p
p
exp  ðy þ mÞ2
2s2
 
!
¼
1
s
ffiffiffiffiffi
2p
p
exp
y  ðy þ mÞ2
2s2
 
!
:
As y ! y, it is apparent that
y  ð yþmÞ2
2s2
h
i
! y, and so fLðeyÞ ! 0.
Also the density function fLðxÞ has a unique critical point, a maximum, and this is
found at x ¼ expðm  s2Þ. In figure 10.9 is displayed the lognormal (bold line) with
m ¼ 0 and s ¼ 1. A gamma density is also displayed (thin line), and was engineered
to have the same critical point as the lognormal, namely to have a maximum at
Figure 10.9
fLðxÞ ¼
1
x ffiffiffiffi
2p
p
exp  ðln xÞ2
2

	
, fGðxÞ ¼ 1
b
x
b
 c1ex=b
GðcÞ
638
Chapter 10
Calculus II: Integration

x ¼ e1 equal to
1
e1 ffiffiffiffi
2p
p
exp  ðln e1Þ2
2

	
A0:65774. From the analysis above of the
gamma, the location of the maximum requires bðc  1Þ ¼ e1, and the parameters
were numerically estimated as
cA1:5;
bA2e1 ¼ 0:73576:
Finally, fLðxÞ has moments of all orders. Specifically, using the substitution y ¼
ln xm
s
, we write
m0
nL ¼
ðy
0
xnfLðxÞ dx
¼
ðy
y
expðnsy þ nmÞfðyÞ dy
¼ enmMFðnsÞ:
In other words, the moments of the lognormal can be calculated from the moment-
generating function of the unit normal. Specifically, using (10.91), we obtain
m0
nL ¼ enmþðnsÞ2=2;
ð10:95aÞ
mL ¼ emþs2=2;
ð10:95bÞ
s2
L ¼ e2mþs2ðes2  1Þ:
ð10:95cÞ
Surprisingly, although the lognormal distribution has moments of all orders, it
does not have a convergent moment-generating function. To see this, assume that
the m.g.f. exists and by (10.67),
MLðtÞ ¼
X
y
n¼0
m0
ntn
n!
¼
X
y
n¼0
enmþðnsÞ2=2tn
n!
;
jtj < R:
Then as a power series, its interval of convergence is related to the limits superior and
inferior of the coe‰cient ratios as noted in proposition 6.24 on the ratio test.
10.11
Continuous Probability Theory
639

Letting cn ¼ e nmþðnsÞ2=2t n
n!
, we have lim supn!y
cnþ1
cn


 ¼ lim infn!y
cnþ1
cn


, and so
L ¼ lim
n!y
cnþ1
cn


¼ lim
n!y
emþð2nþ1Þs2=2
n þ 1
t


¼ y;
for all t 0 0. So by the ratio test this series is divergent for t 0 0, and MLðtÞ only
exists at t ¼ 0. The moments simply grow to fast to allow convergence for any
jtj > 0.
10.11.6
Generating Random Samples
In chapter 7 was introduced a general approach to generating independent and iden-
tically distributed random samples given any discrete probability density function.
The proof of this result depended on the structure of the n-trial sample space, denoted
S n, which was associated with the original sample space S on which this random
variable was defined. This sample space was endowed with a complete collection of
events, denoted E n, and associated probability measure Pn, each intimately related to
the respective notions on S. An independent and identically distributed (i.i.d.) sample
of the random variable X could then be defined as stated in proposition 7.60, which
we repeat for completeness, with additional clarifying references.
Proposition 10.81
Let X be a discrete random variable on a sample space S, with
range fxkg H R, and distribution function FðxÞ. Then, if frjgn
j¼1 H ½0; 1 is a uniformly
distributed random sample in the sense of (7.117), then fF 1ðrjÞgn
j¼1 is a random
sample of X in the sense of (7.7), where F 1ðrjÞ is defined in (7.118). In other words,
if fxkjgn
j¼1 H Rng½X, then
f ðxk1; xk2; . . . ; xknÞ ¼
Y
n
j¼1
f ðxkjÞ:
Unfortunately, we do not yet have the necessary tools to generalize this result to
the continuous distribution case. However, the discretization result above provides a
useful approach which is nearly identical with the theoretical result in practice.
To develop this application, suppose that we are given a continuously distributed
random variable X for which we wish to generate i.i.d. random samples of size n. To
simplify notation, we assume that Rng½X is unbounded in only one direction, say
640
Chapter 10
Calculus II: Integration

Rng½X H ½a; yÞ. Then for any d > 0 a discretization of X with mesh size d can be
constructed, denoted Xd, with range f~xig H R, with ~xi A ½xi; xiþ1Þ, and with probabil-
ity density fdðxÞ defined as in (10.56) by fdð~xiÞ 1 Fðxiþ1Þ  FðxiÞ. Recall that the sig-
nificance of d is that xiþ1  xi a d for all i.
The result above for discrete random variables then assures us that for a uniformly
distributed random sample frjgn
j¼1 H ½0; 1, that fF 1
d ðrjÞgn
j¼1 is independent and
identically distributed, so that for any f~xkjgn
j¼1 H Rng½Xd,
fdð~xk1; ~xk2; . . . ; ~xknÞ ¼
Y
n
j¼1
fdð~xkjÞ:
On the other hand, since fdð~xiÞ 1 Fðxiþ1Þ  FðxiÞ, we conclude that
fdð~xk1; ~xk2; . . . ; ~xknÞ ¼
Y
n
j¼1
½Fðxkjþ1Þ  FðxkjÞ
¼
Y
n
j¼1
Pr½X A ½xkj; xkjþ1Þ:
In other words, for any discretization of the random variable X, the procedure above
provides a methodology for generating i.i.d. random samples of size n that have the
correct probability structures. The one compromise in this procedure is that for any
interval ½xi; xiþ1Þ defined by the discretization, the only value of X that can be
sampled is the tagged point ~xi A ½xi; xiþ1Þ.
In practice, this is of little consequence, since the discretization can be made as fine
as desired. For example, in theory one can define a discretization for which d is
smaller that the precision we wish to use in the measurement of the sample points
~xi. For example, if one wants a random sample with one decimal accuracy, one could
choose d ¼ 0:05, say, or smaller.
10.12
Applications to Finance
10.12.1
Continuous Discounting
A common application of integrals in finance is for interest manipulations with con-
tinuous compounding. Given an annual rate, r, the equivalent rate based on com-
pounding m times per year, denoted rðmÞ, is defined in (2.14) by
10.12
Applications to Finance
641

1 þ r ¼
1 þ rðmÞ
m

m
:
ð10:96Þ
The continuous rate of compounding is defined as
rðyÞ 1 lim
m!y rðmÞ:
This limit is easily calculated as follows, where we substitute m ¼ 1
Dx and evaluate
the result as Dx ! 0:
rðmÞ ¼ m½ð1 þ rÞ1=m  1
¼ ð1 þ rÞDx  1
Dx
:
For Dx ! 0, we recognize this expression from (9.8) as the derivative of the function
f ðxÞ ¼ ð1 þ rÞx at x ¼ 0, which from (9.12) is
rðyÞ ¼ lnð1 þ rÞ;
or
ð10:97aÞ
1 þ r ¼ erðyÞ:
ð10:97bÞ
Put another way, the present value function with continuous compounding for $1
at time t is given by edt, while the accumulated value function at time t of $1 at time
0 is edt, using the simplifying notation, d 1 rðyÞ. This follows from (10.96) by raising
each side to Gt, then taking the limit as m ! y as above.
An alternative approach to this notion of continuous compounding is to denote by
AðtÞ the value at time t of $1 invested at time 0, assuming continuous compounding.
Then, using an annual rate, Aðt þ DtÞ ¼ AðtÞð1 þ rÞDt, we conclude that
Aðt þ DtÞ  AðtÞ
Dt
¼
ð1 þ rÞDt  1
Dt
 
!
AðtÞ;
and from the calculation above conclude that AðtÞ is a di¤erentiable function and
that A0ðtÞ ¼ dAðtÞ.
Then from A 0ðtÞ
AðtÞ ¼ d, and A0ðtÞ
AðtÞ ¼ d
dt ½ln AðtÞ, we derive
d
dt ½ln AðtÞ ¼ d;
642
Chapter 10
Calculus II: Integration

ð T
0
d
dt ½ln AðtÞ dt ¼ dT;
AðTÞ ¼ Að0ÞedT;
where the last step comes from the Fundamental Theorem of Calculus version I:
ð T
0
d
dt ½ln AðtÞ dt ¼ ln AðTÞ  ln Að0Þ ¼ ln AðTÞ
Að0Þ :
Naturally one does not need continuous compounding for discrete cash flows, but
this provides a framework for considering the value of a continuously paid cash
flow stream. A continuous function CðtÞ represents a continuously payable cash flow
stream if over any interval of time ½a; b the total cash paid is given by
Cða; bÞ ¼
ð b
a
CðtÞ dt:
The function CðtÞ represents the ‘‘annualized’’ rate of payment at time t, in that the
amount of cash payable over ½t; t þ Dt is approximately CðtÞDt. This follows from
the first MVT for integrals in (10.12), which can be restated so that for t0 A ½t; t þ Dt,
ð tþDt
t
CðsÞ ds ¼ Cðt0ÞDt:
Also this integral is approximated by CðtÞDt, a single term of a Riemann sum for Dt
small.
The present value at time a, or accumulated value at time b, given continuous
compounding at rate d, then proceeds by starting with a discrete approximation, and
recognizing the Riemann integral in the limit. For example, the present value calcu-
lation requires cash flow over ½t; t þ Dt, which equals Cðt0ÞDt, to be discounted to
time a, and this is approximated by a factor of edðt 0aÞ. So with Dt ¼ ba
n , we have
a partition defined by fa þ jDtgn
j¼0 and subinterval tags denoted t0
j A ða þ ð j  1ÞDt;
a þ jDtÞ:
PV½a;b½CðtÞ ¼ lim
Dt!0
X
n1
j¼0
Cðt0
jÞedðt 0
j aÞDt:
In other words,
10.12
Applications to Finance
643

PV½a;b½CðtÞ ¼
ð b
a
CðtÞedðtaÞ dt:
ð10:98Þ
When CðtÞ ¼ C, a constant cash flow stream, we get
PV½a;b½C ¼ C 1  edðbaÞ
d


:
ð10:99Þ
Similarly the accumulated value of this cash flow stream requires cash flow over
½t; t þ Dt to be accumulated to time b, and this is approximated by a factor of
edðbs0Þ:
AV½a;b½CðtÞ ¼ lim
Dt!0
X
n1
j¼0
Cðs0
jÞedðbs0
j ÞDt;
which is to say
AV½a;b½CðtÞ ¼
ð b
a
CðtÞedðbtÞ dt:
ð10:100Þ
When CðtÞ ¼ C, a constant cash flow stream, we get
AV½a;b½C ¼ C edðbaÞ  1
d


:
ð10:101Þ
Note that in general,
AV½a;b½CðtÞ ¼ edðbaÞPV½a;b½CðtÞ;
ð10:102Þ
a formula that simply adjusts the valuation from t ¼ a to t ¼ b.
10.12.2
Continuous Term Structures
In chapter 3 was introduced discrete interest rate term structure models, whereby
based on market observations, one calculates the term structure in one or all of the
available bases of bond yields, spot rates, or forward rates. In this section this model
is generalized to a continuous framework.
Bond Yields
Although mathematically possible, the continuous counterpart to the bond yield
structure is rarely used in practice, since to be meaningful, a continuous bond
yield at each time t, denoted it say, would represent the bond yield on a t-period
644
Chapter 10
Calculus II: Integration

bond that paid coupons continuously at rate rt say. Generalizing (3.36) using (10.99),
we obtain the price of this bond, Pt, for a par amount of Ft, is given by
Pt ¼ Ftrt
1  eitt
it


þ Fteitt:
ð10:103Þ
Note that the annuity symbol
at;it 1 1  eitt
it
ð10:104Þ
appears to be the continuous counterpart to the discrete formula in chapter 2 in
(2.11) for continuous interest rates. But it is important to understand that the conti-
nuity of the cash flows is explicitly reflected in (10.104), and that this formula is not
equivalent to the formula in (2.11) under the assumption that the rate alone is con-
tinuous. Indeed, by (10.97), if r ¼ it denotes a continuous rate, and n ¼ t is assumed
an integer, the formula from chapter 2 becomes
an;it 1 1  eitt
eit  1 :
Both annuity factors reflect the present value of payment streams of 1 per year using
a continuous rate of interest. But at;it treats this payment as made continuously,
while an;it treats this payment as a lump sum at the end of each year. So intuitively
at;it > an;it, since cash is received earlier. More formally, the continuous cash flow
underlying at;it can be accumulated to the end of each year with (10.101), producing
AV½1 ¼
ð1
0
eitð1tÞ dt ¼ eit  1
it
:
Logically at;it should then equal the value of an annual payment annuity, which pays
AV½1 at the end of each year, and not surprisingly, we have
at;it ¼ eit  1
it
an;it:
Forward Rates
It is often convenient to assume that continuous spot rates and forward rates are con-
tinuously denominated in time, and denoted st and ft respectively. This is motivated
by an interest in developing models of future rates that evolve ‘‘stochastically’’ in
10.12
Applications to Finance
645

continuous time, which is to say randomly, and an interest in what these models can
tell us about today’s pricing of bonds. These stochastic pricing topics are quite
advanced for the tools developed up to this point. But we can develop the relation-
ship between the continuous forward term structure model at a given point in time
and the prices of bonds.
Imagine a model specification for continuous forward interest rates ft for t > 0.
Intuitively this means that the present value at time t, of 1 payable at time t þ Dt, is
approximately eDtft. Extending this idea, the present value at time 0 of 1 payable at
time T is approximately
ZT Aexp 
X
n1
j¼0
fjDtDt
"
#
;
where ZT denotes the price of this T-period zero coupon bond, and with Dt ¼ T
n .
It is apparent that if the ft model is continuous, which is more than is needed but
often the case in models in practice, this approximate price converges as Dt ! 0. Spe-
cifically, the price of a T -period zero-coupon bond, given a continuous forward rate
specification, satisfies
ZT ¼ exp 
ð T
0
ft dt


:
ð10:105Þ
Since a fixed cash flow coupon bond is just a portfolio of zero-coupon bonds, the for-
mula in (10.105) can also be used for these bonds, generalizing (3.39).
So given a model specification for forward rates, one can price fixed cash flow
bonds using this formula. Of course, in practice, such models do not produce a single
specification of this structure, since if that is all one wants, that can generally be
observed in today’s financial markets. The goal of such models is to produce ran-
domly generated collections of future forward rate ‘‘paths,’’ a sample space of such
paths, on which one can then interpret ZT as a random variable. Once done, an en-
tire theory exists for translating these statistical distributions of rate paths and prices
into logical prices for today’s fixed and variable cash flow securities that rely on
these future rates. This is an advanced subject that requires the tools of stochastic
processes.
Fixed Income Investment Fund
A model of interest rates can also be interpreted in the context of providing invest-
ment returns in a fund, such as a money market fund, in which the forward rate ft
646
Chapter 10
Calculus II: Integration

is earned from time t to time t þ Dt. Again, assuming that such a rate path is contin-
uous, if At denotes the fund balance at time t, then
AtþDt AAte ftDt:
Consequently, since AT
A0 ¼ Qn1
j¼0
Að jþ1ÞDt
AjDt
, where Dt ¼ T
n , we conclude that
AT
A0
Aexp
X
n1
j¼0
fjDtDt
"
#
:
As above, if ft is a continuous function, this summation converges as Dt ! 0, pro-
ducing the investment fund model
AT ¼ A0 exp
ð T
0
ft dt


:
ð10:106Þ
This model makes sense in both a ‘‘deterministic’’ setting, where a forward rate path
is specified, or in a statistical context, where various rate paths are generated and the
resulting fund balance, AT for fixed T, is treated as a random variable on the sample
space of rate paths.
Because of the Fundamental Theorem of Calculus version II, AT is a di¤erentiable
function of T when ft is continuous, and we have that
dAT
dT ¼ fTAT:
In this interpretation the instantaneous change in the fund balance at time T is pro-
portional to the fund balance, with proportionality factor of fT. This formula is
sometimes expressed in the di¤erential notation:
dAt ¼ ftAt dt:
ð10:107Þ
This notation is best understood in the context of integration theory, as was seen in
section 10.7.1 on integration by the substitution method. In other words, a di¤eren-
tial of a function is a mathematical object one integrates to determine how a function
changes. Now, if we simply integrate both sides of this equation, we get
ð T
0
dAt ¼
ð T
0
ftAt dt;
10.12
Applications to Finance
647

which doesn’t appear very promising. Logically, the left-hand side is the integral of 1,
and so
ð T
0
dAt ¼ AtjT
t¼0 ¼ AT  A0:
But the right-hand side is not readily evaluated.
But if we first divide the equation in (10.107) by At, which is justified since At > 0,
and then integrate, we get
ð T
0
dAt
At
¼
ð T
0
ft dt:
The left-hand integral is now
ð T
0
dAt
At
¼ ln AtjT
t¼0 ¼ ln AT
A0
;
and when equated to the right-hand integral, (10.106) is reproduced.
Spot Rates
If sT denotes the continuous spot rate for term T, it must be the case that in addition
to (10.105), we have by definition,
ZT ¼ exp½TsT;
ð10:108Þ
and hence from (10.105),
sT ¼ 1
T
ð T
0
ft dt:
ð10:109Þ
Recall the first mean value theorem for integrals in proposition 10.27. The contin-
uous spot rate at time T is seen to equal the average value of the continuous forward
rates over the interval ½0; T.
This continuous spot-forward relationship can be reversed with the help of the Fun-
damental Theorem of Calculus version II above. First, note that if ft is continuous,
then sT is a di¤erentiable function of T for T > 0, since it is the product of 1
T , which
is di¤erentiable for T 0 0, and
Ð T
0 ft dt, which is di¤erentiable by this theorem. Also
dsT
dT ¼ 1
T 2
ð T
0
ft dt þ 1
T fT;
648
Chapter 10
Calculus II: Integration

which can be rewritten as
dsT
dT ¼ 1
T ð fT  sTÞ
ð10:110Þ
and also
fT ¼ dðTsTÞ
dT
:
ð10:111Þ
This analysis allows some easy conclusions based on (10.110) and chapter 9 tools:
1. Spot rates increase as a function of t if and only if dst
dt > 0 for all t, which occurs if
and only if ft > st for all t.
2. Spot rates decrease as a function of t if and only if dst
dt < 0 for all t, which occurs if
and only if ft < st for all t.
3. If spot rates increase then decrease, or conversely, there is a time t0 so that
dst
dt


t0 ¼ 0, and hence ft0 ¼ st0.
Note further that from (10.111) we can conclude that fT > 0 for all T if and only
if the function gðTÞ ¼ TsT is a strictly increasing function of T. It is not necessary to
have sT an increasing function in order for fT > 0. Indeed, dðTsTÞ
dT
> 0 simply implies
that dsT
dT >  sT
T .
10.12.3
Continuous Stock Dividends and Reinvestment
The analysis above for a fixed income fund carries over readily to the context of an
equity fund. Specifically, if Rt denotes the equity fund return at time t, then with the
same derivation, we have that with ET denoting the fund balance at time T:
ET ¼ E0 exp
ð T
0
Rt dt


:
ð10:112Þ
As before, ET is a di¤erentiable function of T when Rt is a continuous function, so
this composite function can be di¤erentiated and expressed in di¤erential notation
as
dEt ¼ RtEt dt:
ð10:113Þ
Now, it is often assumed that such an equity will pay continuous cash dividends,
and that these dividends are continuously reinvested in more equity. By continuous
10.12
Applications to Finance
649

dividends is meant that if Dt denotes the rate of dividend payout at time t, the total
change in value to the investor at time t is approximately
Total returnAðRtEt þ DtEtÞDt.
The investor receives RtEtDt as appreciation/depreciation in the fund, and DtEtDt in
cash dividends.
In this form it is di‰cult to model total investor wealth at some time in the future.
Although this cash could be invested in a risk free asset like a T-bill, the position in
the T-bill is not risk free, since the principal flows into that fund, DtEtDt, reflect the
riskiness of the equity fund. Because it is common to want to partition total invest-
ments between risk assets and risk-free assets, for example when one is replicating a
option, there is a motivation to reinvest these dividends in stock, rather than to accu-
mulate this risky asset in T-bills.
With that goal, we now seek to determine the total value of the fund when divi-
dends are so reinvested. To this end, let Et again denote the value of the equity fund
when dividends are disbursed in cash to the investor, and let Ft denote the value of
this fund when all dividends are continuously reinvested in more stock. Logically the
change in the total fund, FtþDt  Ft, reflects two components:
1. An increment or decrement based on the performance of the equities, as implied
by Rt, which can be captured by the return in the E fund, scaled to reflect the assets
in the F fund:
½EtþDt  Et
Et
Ft:
2. An increment, since Dt b 0, based on the payment of continuous cash dividends
on the total fund balance of Ft, equal to
FtDtDt;
that are then reinvested in more equities in the F fund.
Combining, we derive that
FtþDt  Ft ¼ ½EtþDt  Et
Et
Ft þ FtDtDt;
or
FtþDt  Ft
DtFt
¼ EtþDt  Et
DtEt
þ Dt:
650
Chapter 10
Calculus II: Integration

As Dt ! 0, the limit on the right side of the equation exists because Et is di¤erentia-
ble as noted above. Consequently Ft is also di¤erentiable and
F 0
t
Ft
¼ E 0
t
Et
þ Dt:
Now E 0
t
Et ¼ Rt is continuous by assumption, as is Dt, and hence so too is F 0
t
Ft . Inte-
grating this expression from t ¼ 0 to t ¼ T, and recalling that d ln f ðxÞ
dx
¼ f 0ðxÞ
f ðxÞ , we
obtain
ln FT
F0


¼ ln ET
E0


þ
ð T
0
Dt dt:
Finally, assuming that F0 ¼ E0, so both funds begin with the same level of assets, we
obtain that
FT ¼ ET exp
ð T
0
Dt dt


:
ð10:114Þ
When Dt ¼ D is constant, this simplifies to
FT ¼ ETeDT:
ð10:115Þ
Combining (10.114) with (10.112), we obtain
FT ¼ E0 exp
ð T
0
ðRt þ DtÞ dt


:
ð10:116Þ
10.12.4
Duration and Convexity Approximations
In section 9.8.5 Taylor series approximations were applied to model the price sensi-
tivity of a fixed income security or portfolio. Using the tools of this chapter, we de-
velop an alternative price sensitivity model.
Recall the definition of the duration of the price function in (9.57):
DðrÞ ¼  P0ðrÞ
PðrÞ :
Assuming continuity of DðrÞ and PðrÞ > 0, we can integrate this expression from i0
to i, obtaining
10.12
Applications to Finance
651

ð i
i0
DðrÞ dr ¼ 
ð i
i0
P0ðrÞ
PðrÞ dr
¼ ln PðiÞ
Pði0Þ


:
A little algebra then provides the identity
PðiÞ ¼ Pði0Þe
Ð i
i0DðrÞ dr;
ð10:117Þ
which can be transformed to an approximation formula with a one-step Riemann
sum:
PðiÞAPði0ÞeDði0Þðii0Þ:
ð10:118Þ
This approximation can then be improved by analyzing the function in the expo-
nential in (10.117):
f ðiÞ ¼
ð i
i0
DðrÞ dr;
and applying the Fundamental Theorem of Calculus version II in (10.20), and then
(9.65), to obtain
f 0ðiÞ ¼ DðiÞ;
f 00ðiÞ ¼ D2ðiÞ  CðiÞ:
Expanding the second-order Taylor series of f ðiÞ about i0, and noting that f ði0Þ ¼ 0,
we obtain an improvement to (10.118):
PðiÞAPði0ÞeDði0Þðii0Þð1=2Þ½D2ði0ÞCði0Þðii0Þ2:
ð10:119Þ
It is interesting to compare the approximations above to those developed in chap-
ter 9. To this end, if we apply the formula for an exponential power series in (7.63) to
the approximation in (10.118), we obtain
PðiÞAPði0Þ 1  Dði0Þði  i0Þ þ 1
2 D2ði0Þði  i0Þ2


þ OðDi3Þ:
Expanding (10.119) in the same way obtains
PðiÞAPði0Þ 1  Dði0Þði  i0Þ þ 1
2 Cði0Þði  i0Þ2


þ OðDi3Þ:
652
Chapter 10
Calculus II: Integration

So to an error of OðDi3Þ, (10.119) provides the same result as the second-order
Taylor approximation in (9.61). The same can be said for (10.118) and (9.60) to an
error of OðDi2Þ. However, for price functions with positive convexity, (10.118) will
generally provide better approximations using only Dði0Þ than will (9.60) because of
the 1
2 D2ði0Þði  i0Þ2 adjustment above.
Finally, as an application of Riemann sums, we demonstrate that by partitioning
the interval ½i0; i, and applying the simple approximation in (9.60) to each sub-
interval, that in the limit the identity in (10.117) is produced. To this end, define
ij ¼ i0 þ j
n Di for j ¼ 0; 1; . . . ; n, where Di ¼ i  i0. Apparently,
PðiÞ
Pði0Þ ¼
Y
n
j¼1
PðijÞ
Pðij1Þ ;
and each factor in this product can be approximated by (9.60):
PðijÞ
Pðij1Þ ¼ 1  Dðij1Þ Di
n þ O
1
n2


:
Consequently
Y
n
j¼1
PðijÞ
Pðij1Þ


¼
Y
n
j¼1
1  Dðij1Þ Di
n þ O
1
n2




;
and by assuming that DðiÞ is continuous and hence bounded on this interval, we con-
clude that all factors in this product are positive for n large enough, justifying the
taking of natural logarithms. This produces
ln
Y
n
j¼1
1  Dðij1Þ Di
n þ O
1
n2




"
#
¼
X
n
j¼1
ln 1  Dðij1Þ Di
n þ O
1
n2




¼ 
X
n
j¼1
Dðij1Þ Di
n þ O 1
n
 
;
using (8.20). Note that in this calculation, although the error in each logarithmic
power series is O
1
n2
 	
, this error increases to O 1
n
 
because there are n terms in the
summation.
Letting n ! y, the last expression converges as a Riemann sum to the integral of
the continuous function, DðiÞ. In other words,
10.12
Applications to Finance
653

ln
Y
n
j¼1
1  Dðij1Þ Di
n þ O
1
n2




"
#
! 
ð i
i0
DðrÞ dr:
Now, since gðxÞ ¼ ex is a continuous function, and hence sequentially continuous,
we can exponentiate this sequence and limit to obtain that as n ! y:
PðiÞ
Pði0Þ ¼
Y
n
j¼1
1  Dðij1Þ Di
n þ O
1
n2




! e
Ð i
i0DðrÞ dr:
10.12.5
Approximating the Integral of the Normal Density
The unit normal density function was introduced in section 8.6 and studied in more
detail in section 10.11.5. As given in (10.88), it is defined as
fðxÞ ¼
1ffiffiffiffiffi
2p
p
ex2=2:
It was shown to be a critically important function in chapter 8 due to the De
Moivre–Laplace theorem, and the more general central limit theorem, and this is
even more so because the statement and proof of the latter result can be generalized
much further. The tools that will be needed to generalize this result relate to proper-
ties of multivariate functions that will be used in the study of independent, identically
distributed random variables, as well as a more general integration theory and prob-
ability theory.
In this section we apply some of the results studied above to the question of
approximating integrals of fðxÞ. Of course, if X is a random variable with density
function fðxÞ, then
Pr½a a X a b ¼
ð b
a
fðxÞ dx:
On the other hand, if Y is a random variable with density function equal to the more
general fNðyÞ, then by a substitution x ¼ ym
s ,
Pr½c a Y a d ¼
ð d
c
fNðyÞ dy ¼
ð b
a
fðxÞ dx;
where a ¼ c  m
s
; b ¼ d  m
s
:
654
Chapter 10
Calculus II: Integration

Consequently, all probability statements about Y can be translated to probabil-
ity statements about X, and so it is the integral of fðxÞ that is addressed in this
section.
As was noted in section 8.6, the most common probability values to develop are of
the form
FðbÞ ¼
ð b
y
fðxÞ dx;
b > 0;
since all other statements can be derived from these as seen in (8.32). However, if
b > 0, it is apparent since Fð0Þ ¼ 0:5, that
FðbÞ ¼ 0:5 þ
ð b
0
fðxÞ dx;
b > 0;
and only integrals of the form
Ð b
0 fðxÞ dx, for b > 0 need be addressed.
Power Series Method
As was seen in section 10.9.5 on the integrability of power series, a power series can
be integrated term by term over any subinterval of its interval of convergence. Since
fðxÞ is an analytic function which converges for all x, this approach can be utilized
over any interval. To this end, recall that by the Taylor series expansion of the expo-
nential function,
fðxÞ ¼
1ffiffiffiffiffi
2p
p
X
y
j¼0
 1
2 x2

 j
j!
¼
1ffiffiffiffiffi
2p
p
X
y
j¼0
ð1Þ jx2j
2 jj!
:
Integrating term by term, as noted in (10.39), we get for b > 0,
ð b
0
fðxÞ dx ¼
1ffiffiffiffiffi
2p
p
X
y
j¼0
ð1Þ jb2jþ1
ð2j þ 1Þ2 jj! :
ð10:120Þ
This expression converges absolutely by the above noted section, and as an alternat-
ing series, we have an error estimate associated with any partial summation from sec-
tion 6.1.5. Specifically, by the alternating series convergence test for n large to ensure
that series terms decrease,
10.12
Applications to Finance
655

ð b
0
fðxÞ dx 
1ffiffiffiffiffi
2p
p
X
n1
j¼0
ð1Þ jb2jþ1
ð2j þ 1Þ2 jj!


 a
1ffiffiffiffiffi
2p
p
b2nþ1
ð2n þ 1Þ2nn! :
This error term decreases to 0 quickly as n increases, as can be seen by an applica-
tion of Stirling’s formula from (8.24):
e1=ð12nþ1Þ <
n!
ffiffiffiffiffi
2p
p
nnþð1=2Þen < e1=12n;
which produces an error estimate after a bit of algebra:
ð b
0
fðxÞ dx 
1ffiffiffiffiffi
2p
p
X
n1
j¼0
ð1Þ jb2jþ1
ð2j þ 1Þ2 jj!


 a
be1=ð12nþ1Þ
2p
ffiffin
p ð2n þ 1Þ
b2e
2n

n
:
ð10:121Þ
Upper and Lower Riemann Sums
Because fðxÞ is a strictly decreasing function on ½0; b for b > 0, the upper Riemann
sums are defined by the left subinterval endpoints, while the lower sums are defined
by the right endpoints. Consequently, defining the partition of ½0; b, with Dx ¼ b
n , we
obtain
1ffiffiffiffiffi
2p
p
X
n
j¼1
Dx exp  1
2 ½ jDx2


a
ð b
0
fðxÞ dx
a
1ffiffiffiffiffi
2p
p
X
n1
j¼0
Dx exp  1
2 ½ jDx2


:
This can be simplified by defining the sum S ¼ Pn1
j¼1 Dx exp

 1
2 ½ jDx2
, to produce
1ffiffiffiffiffi
2p
p
S þ Dx exp  1
2 b2




a
ð b
0
fðxÞ dx a
1ffiffiffiffiffi
2p
p
ðS þ DxÞ:
ð10:122Þ
With the given definition of S, the range between the upper and lower bounds is
Dxffiffiffiffi
2p
p
1  exp  1
2 b2




, and so a midpoint estimate gives half this error. Defining I U=L
as this midpoint value produces
I U=L ¼
1ffiffiffiffiffi
2p
p
S þ Dx
2
1 þ exp  1
2 b2






;
and we get
656
Chapter 10
Calculus II: Integration

ð b
0
fðxÞ dx  I U=L


 a
Dx
2
ffiffiffiffiffi
2p
p
1  exp  1
2 b2




:
ð10:123Þ
So given b > 0, the error on this approach is OðDxÞ ¼ O 1
n
 
.
Trapezoidal Rule
The trapezoidal rule is defined as the average of the Riemann sums defined with the
left endpoints and the right endpoints, as is clear from (10.40). Consequently in
the case of a monotonic function like fðxÞ, the trapezoidal approximation can also
be defined as the average of the upper and lower Riemann sums. So here the trape-
zoidal approximation I T equals I U=L above.
However, the error estimate for the trapezoidal rule reflects higher order derivative
values of fðxÞ. Specifically, we have from (10.42),
ð b
0
fðxÞ dx  I T


 a M2b
12 ðDxÞ2;
ð10:124Þ
where M2 is an upper bound for jfð2ÞðxÞj on ½0; b. Taking these derivatives, we
obtain
f0ðxÞ ¼ 
xffiffiffiffiffi
2p
p
ex2=2;
fð2ÞðxÞ ¼ ðx2  1Þ
ffiffiffiffiffi
2p
p
ex2=2:
To estimate M2, we can locate the critical points of f ðxÞ 1 fð2ÞðxÞ by the methods
of section 9.5.1. Evaluating f 0ðxÞ, we have that
f 0ðxÞ ¼ ½xð3  x2Þ
ffiffiffiffiffi
2p
p
ex2=2;
so it is apparent that the critical points of f 0ðxÞ occur at x ¼ 0;G
ffiffi
3
p
. Also, as
jxj ! y, fð2ÞðxÞ ! 0, and so since fð2Þð0Þ < 0 and fð2ÞðG
ffiffi
3
p
Þ > 0,
M2 ¼ max½jfð2Þð0Þj; fð2ÞðG
ffiffi
3
p
ÞA0:3989:
Consequently we obtain the trapezoidal error estimate:
ð b
0
fðxÞ dx  I T


a 0:03325bðDxÞ2;
ð10:125Þ
which is considerably better than the estimate in (10.123), despite using the same
approximation. This is due to the use of information on this function’s second
10.12
Applications to Finance
657

derivative which is ignored above. This information reduces the error to OðDx2Þ
where Dx ¼ b
n . The graph of fð2ÞðxÞ is seen in figure 10.10.
Note that this graph also indicates that the normal density has second derivative
that is negative on the interval ½1; 1, which is the interval ½s; s in the general
case, implying that this function is concave on this interval and changes to convex
outside this interval. The points x ¼ G1, or more generally x ¼ Gs, are therefore
inflection points, or points of inflection, of the normal density function, as noted in
section 9.6. It is also the case that in this example, these inflection points are exactly
the points where fð2ÞðxÞ ¼ 0.
Simpson’s Rule
Simpson’s rule, as can be observed in (10.44), requires three Riemann sums, the same
two used for the trapezoidal rule defined in terms of the subinterval left and right
endpoints, as well as a third Riemann sum defined by the subinterval midpoints.
The weight put on the endpoint Riemann sums is 1
6 each, while the weight on the
midpoint Riemann sum is 4
6 . Denoting by I S the Simpson approximation using the
same partition as above with Dx ¼ b
n , we obtain by (10.46) that
Figure 10.10
jð2ÞðxÞ ¼
1ffiffiffiffi
2p
p
ðx2  1Þeðx2=2Þ
658
Chapter 10
Calculus II: Integration

jI  I Sj a M4b
2880 ðDxÞ4;
ð10:126Þ
where M4 is an upper bound for jfð4ÞðxÞj on ½0; b.
Continuing to take these derivatives, we have
fð3ÞðxÞ ¼ ½xð3  x2Þ
ffiffiffiffiffi
2p
p
ex2=2;
fð4ÞðxÞ ¼ ½x4  6x2 þ 3
ffiffiffiffiffi
2p
p
ex2=2:
Again seeking the critical points of f ðxÞ ¼ fð4ÞðxÞ, we obtain
f 0ðxÞ ¼ x½x4  10x2 þ 15
ffiffiffiffiffi
2p
p
ex2=2;
and the critical points are obtained by the quadratic formula applied to y2  10y þ 15
with y ¼ x2, producing
x ¼ 0;G
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
3 þ
ffiffi
6
p
q
;G
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
3 
ffiffi
6
p
q
:
The upper bound for jfð4ÞðxÞj is again seen to occur at x ¼ 0 by substitution,
producing
M4 ¼ fð4Þð0ÞA1:1968:
Consequently the Simpson error estimate becomes
jI  I Sj a 0:00042bðDxÞ4:
ð10:127Þ
This error is significantly better than the trapezoidal estimate above due to the error
being OðDx4Þ compared to OðDx2Þ, although it could be argued that the comparison
is not quite fair since Simpson’s rule uses midpoints of subintervals, and hence a finer
partition.
Had the trapezoidal estimate been implemented using this same number of interval
evaluation points, the implied partition would be Dx0 ¼ b
2n ¼ Dx
2 , and the revised
trapezoidal estimate, denoted I T 0, stated in terms of the original Dx, would have
an error:
ð b
0
fðxÞ dx  I T 0


 a 0:00832bðDxÞ2:
10.12
Applications to Finance
659

So, despite using the same interval points in both estimates, Simpson’s rule is seen to
be far superior because of the way it weighted the various points, and not because it
included more points. The graph of fð4ÞðxÞ can be seen in figure 10.11.
*10.12.6
Generalized Black–Scholes–Merton Formula
This section develops a generalization of the classical Black–Scholes–Merton option
pricing formulas. It is a generalization in that is applies the earlier methodology to
a more general European-style derivative than a European put or call option. By
European-style derivative is meant a financial contract with a general payo¤ function
at time T that depends on the value of an underlying investment asset at time T, and
that does not allow early exercise. As always, we use the language that S is a com-
mon stock, but as noted in section 7.8.6, we really only need to assume that S is an
investment asset to justify the replicating portfolio pricing argument.
It is important to note that this section does not generalize these famous formulas
in the sense that these are ‘‘new’’ and would have been unknown to the authors. In-
deed the mathematical tools used in the original papers certainly handle the payo¤
functions considered here, and the authors certainly knew this. But we have not yet
developed the tools used by these authors, so we will solve these problems, the spe-
cific and the general, with the tools of this chapter.
Figure 10.11
jð4ÞðxÞ ¼
1ffiffiffiffi
2p
p
ðx4  6x2 þ 3Þeðx2=2Þ
660
Chapter 10
Calculus II: Integration

The goals of this section are as follows:
1. Derive a general integration formula for the price of a European-style derivative,
based on a replicating portfolio approach, that reduces to the classical B-S-M formu-
las when the payo¤ function is a European put or call.
2. Demonstrate that this evaluation only utilizes the risk-neutral probability distribu-
tion of stock prices.
3. Develop this formula using the tools of integration theory studied in this chapter,
because the tools of chapter 9, while adequate for a put or call option, do not readily
apply to this general situation.
To begin with, recall the chapter 7 price of a European derivative with expiry
at time T, in (7.147) as generalized in section 8.8.3. The lattice-based price of a
European option or other European-style derivative security on an investment
asset, exercisable in n periods and derived based on a replicating portfolio argument,
is
L0ðS0Þ ¼ enr X
n
j¼0
n
j


q jð1  qÞnjLðS j
nÞ;
S j
n ¼ S0e juþðnjÞd:
In the generalized chapter 8 setting where T is fixed, and time-step periods are
defined by Dt ¼ T
n , this formula is applicable with risk-neutral probability as in (8.52):
qðDtÞ ¼ erðDtÞ  edðDtÞ
euðDtÞ  edðDtÞ ;
where by (8.53) and (8.54), the binomial asset period returns and risk-free rate are
given by
uðDtÞ ¼ mDt þ
ffiffiffiffi
p0
p
s
s
ffiffiffiffiffi
Dt
p
;
dðDtÞ ¼ mDt 
ffiffiffiffip
p0
r
s
ffiffiffiffiffi
Dt
p
;
rðDtÞ ¼ rDt;
where 0 < p < 1 is the real world probability of uðDtÞ and p0 1 1  p.
10.12
Applications to Finance
661

We state the main result of this section in proposition 10.84 below. The only
requirement on the payo¤ function at time T, LðSTÞ, is that it is bounded and piece-
wise continuous with limits. The notion of piecewise continuous was encountered in
section 10.2.2 and will be generalized here with a definition.
Definition 10.82
A function f ðxÞ is piecewise continuous with limits on R if there
exist points
   < a2 < a1 < a0 < a1 < a2 <    :
so that:
1. On each open interval, ðaj; ajþ1Þ, f ðxÞ is bounded and continuous
2. For each aj, limx!aþ
j f ðxÞ and limx!a
j f ðxÞ exist, and f ðajÞ is defined as one of
these limits
3. The collection fajg, if infinite, has no accumulation points, so that min½ajþ1  aj ¼
m > 0
A function f ðxÞ is piecewise continuous with limits on ½a; b if there exist points
a a a0 < a1 < a2 <    < an a b
with the same properties.
For the purposes of the existence of the Riemann integral below, as was seen in
section 10.2.2 on the Riemann integral without continuity, only constraint 1 in this
definition is needed, which is the typical definition of piecewise continuous. In order
for such a function to make sense as a payo¤ function for a European-style deriva-
tive, we add constraint 2.
Besides being logical in the financial markets, constraint 2 will also allow us to ex-
press f ðxÞ as a continuous function on each closed interval, ½aj; ajþ1, redefining f ðxÞ
at the endpoints in terms of its one-sided limits. This partitioning of f ðxÞ will not
change the value of its integral, of course, and will be seen to provide for a needed
technicality in the proof of the proposition below.
Example 10.83
A European binary call option, with an expiry of T and strike price of
K, is defined with the payo¤ function
LðSTÞ ¼
A;
ST > S0;
0;
ST a S0;

ð10:128Þ
for some fixed amount A > 0. A European binary put option is defined with
662
Chapter 10
Calculus II: Integration

LðSTÞ ¼
0;
ST b S0;
A;
ST < S0:

ð10:129Þ
European binary options are the simplest examples of derivative securities with payo¤
functions that are piecewise continuous with limits.
The main result is stated next for bounded payo¤ functions, and will be proved
over the next few sections. In the real world every payo¤ function is of necessity
a bounded function, say jLðSTÞj a M, where M represents global gross domestic
product, say. Strictly speaking, we do not need to assume boundedness for the state-
ment of this result. However, if not bounded, there is the question of the existence of
the integral in the statement of the proposition, and this generalization will create
some unnecessary technical di‰culties since this boundedness assumption is not a re-
striction in any real world application.
Proposition 10.84
For any bounded payo¤ function, LðSTÞ, that is piecewise continu-
ous with limits, we have that as Dt ! 0,
L0ðS0Þ ! erT
ðy
y
LðS0exÞf ðxÞ dx;
ð10:130Þ
where f ðxÞ is the probability density function for N
r  1
2 s2


T; s2T


, and L0ðS0Þ is
the binomial summation defined in (7.147) generalized for Dt ¼ T=n.
Remark 10.85
Note that by the section 9.8.10 analysis, N
r  1
2 s2


T; s2T


is the
limiting distribution of the log-ratio of equity prices under the risk-neutral probability
as developed in (9.93). In other words, (10.130) states that the price of a European-
style derivative, based on a replicating portfolio on a binomial lattice, converges to the
expected present value of the payo¤ function values. This expectation is calculated
under the assumption that future stock prices are lognormally distributed, with mean
returns consistent with the assumption that investors are risk neutral. Here, as in
(7.144), risk neutrality means that investors will pay S0 for the security, equal to the
expected present value of future stock prices:
S0 ¼ erT
ðy
y
ðS0exÞ f ðxÞ dx;
ð10:131Þ
where f ðxÞ is the probability density function for N
r  1
2 s2


T; s2T


. This iden-
tity follows because the right-hand expression equals S0erTMZð1Þ, where Z @
N
r  1
2 s2


T; s2T


, which reduces to S0.
We now develop the tools needed to prove this general result.
10.12
Applications to Finance
663

The Piecewise ‘‘Continuitization’’ of the Binomial Distribution
In section 10.11.3 the discretization of a continuously distributed random variable
was introduced. Here we introduce the first step in the opposite concept, and that is
for the continuitization of a discrete random variable, where we note that pronunci-
ation of this term is facilitated with meter: ‘‘ba-ba-boom-ba-ba-boom-ba’’. We con-
centrate on the binomial distribution of equity returns, as this is the application in
hand, but it will be clear from the construction that this approach is more generally
applicable.
We first define a piecewise continuitization of the probability density function of
the binomial Binðn; qÞ used in the derivative pricing formula above. Specifically,
given fBð jÞ ¼
n
j
 	
q jð1  qÞnj for j ¼ 0; 1; . . . ; n, and interval tags equal to the stock
returns on a binomial lattice after n time steps,
xj ¼ nd þ ðu  dÞj;
j ¼ 0; 1; . . . ; n þ 1;
the piecewise continuitization of fBðjÞ is defined on the interval ½x0; xnþ1Þ by
~fnðxÞ ¼
1
u  d fBð jÞ;
xj a x < xjþ1;
ð10:132Þ
and is defined to be 0 outside the interval ½x0; xnþ1Þ.
With the formulas in (8.53) for uðDtÞ and dðDtÞ, and recalling that n 1 T
Dt , we have
x0 ¼ T m 
ffiffiffiffip
p0
r
sffiffiffiffiffi
Dt
p


;
xnþ1 ¼ T m þ
ffiffiffiffi
p0
p
s
sffiffiffiffiffi
Dt
p
"
#
þ s
ffiffiffiffiffi
Dt
p
ffiffiffiffiffiffi
pp0
p
:
So the interval ½x0; xnþ1Þ grows without bound as Dt ! 0.
In figure 10.12 the piecewise continuitization of the binomial distribution with
n ¼ 6, q ¼ 0:55, u ¼ 0:05 and d ¼ 0:04 is represented by the seven horizontal lines
in bold. On an n period binomial lattice, only fxjgn
j¼0 are produced as equity returns,
of course. Here xnþ1 is defined consistently to simplify the model. To avoid this ex-
traneous return, each of the horizontal bars in this figure could have been ‘‘centered’’
on fxjgn
j¼0, and defined as
^fnðxÞ ¼
1
u  d fBð jÞ;
xj  1
2 ðu  dÞ a x < xj þ 1
2 ðu  dÞ;
but this will make the subsequent work a bit messier with little apparent payo¤.
664
Chapter 10
Calculus II: Integration

Note that ~fnðxÞ is piecewise continuous and has integral 1, since xjþ1  xj ¼ u  d.
In this case the integral is just the area of rectangles:
ð xnþ1
x0
~fnðxÞ dx ¼
X
n
j¼0
ð xjþ1
xj
~fnðxÞ dx
¼ ðu  dÞ
X
n
j¼0
1
u  d fBð jÞ ¼ 1:
In exercise 19 is assigned the development of the following expectation formulas,
with ~Xn denoting the piecewise continuously distributed random variable with prob-
ability density ~fnðxÞ, and X B
n the discrete random variable with probability density
fBð jÞ and domain fxjgn
j¼0:
E½ ~Xn ¼ E½X B
n  þ 1
2 ½u  d;
ð10:133aÞ
E½ð ~XnÞ2 ¼ E½ðX B
n Þ2 þ ½u  dE½X B
n  þ ½u  d2
3
;
ð10:133bÞ
Figure 10.12
Piecewise continuitization and continuitization of the binomial f ðxÞ
10.12
Applications to Finance
665

Var½ ~Xn ¼ Var½X B
n  þ ½u  d2
12
;
ð10:133cÞ
M ~
XnðtÞ ¼ etðudÞ  1
tðu  dÞ MX B
n ðtÞ:
ð10:133dÞ
Recall that u  d ¼ s ffiffiffi
Dt
p
ffiffiffiffiffi
pp0
p
, and by a Taylor series expansion,
e tðudÞ1
tðudÞ ¼ 1 þ
Oðu  dÞ. Hence, as Dt ! 0, the moments above and the moment-generating func-
tion for ~Xn approach the respective values for X B
n , which we recall from section
9.8.10 approach the respective values for Z @ N
r  1
2 s2


T; s2T


.
The ‘‘Continuitization’’ of the Binomial Distribution
Next we define the continuitization of fBðjÞ in a way that makes integrating this
function easy. In figure 10.12 this continuous function is made up of the the light di-
agonal curves and the connecting portions of the bold horizontal lines. As can be
seen, this function, denoted fnðxÞ, is defined so that
Ð
fnðxÞ dx ¼
Ð ~fnðxÞ dx, since the
di¤erence in functions is simply a summation of o¤setting triangles.
To formally define fnðxÞ, we choose fjgnþ1
j¼0 with the restriction that 0 < j < ud
2 ,
although the goal will later be to better specify the rate of convergence of j ! 0.
This continuitization is now defined for x A ½x0  0; xnþ1 þ n by
fnðxÞ ¼
~fnðxÞ;
x A ½xj þ j; xjþ1  j;
ð1  tÞ ~fnðxj  jÞ þ t ~fnðxj þ jÞ;
x ¼ ð1  tÞðxj  jÞ þ tðxj þ jÞ:
(
ð10:134Þ
We define fnðxÞ ¼ 0 outside the interval ½x0  0; xnþ1 þ n. For this definition, j ¼
0; 1; . . . ; n, in the first line, which defines the horizontal portions of fnðxÞ, and j ¼ 0;
1; . . . ; n þ 1 and 0 < t < 1 for the second line, which defines the diagonal portions of
fnðxÞ. Also recall that ~fnðxÞ ¼ 0 outside ½x0; xnþ1, and so in particular, this is used in
the second line for ~fnðx0  0Þ and ~fnðxnþ1 þ nþ1Þ.
In figure 10.12 is displayed the continuitization of the binomial with n ¼ 6,
q ¼ 0:55, u ¼ 0:05 and d ¼ 0:04 using j ¼ 0:02 for all j. Note that fnðxÞ is contin-
uous, since at each point xj  j; we have that fnðxj  jÞ ¼ ~fnðxj  jÞ ¼ ~fnðxj1Þ by
the first line, while by the second, t ¼ 0 at this point, and hence the same result is
produced. The same analysis shows continuity at all xj þ j.
In order to show that fnðxÞ is a probability density function, we show that
Ð
½ fnðxÞ  ~fnðxÞ dx ¼ 0. To do this, we only need to demonstrate that this equation
holds over each of the diagonal portions of fnðxÞ, since this integral will of course
equal 0 on the horizontal portions.
666
Chapter 10
Calculus II: Integration

Consider the interval ½xj  j; xj þ j for j ¼ 0; 1; . . . ; n þ 1. We have that with
x ¼ ð1  tÞðxj  jÞ þ tðxj þ jÞ,
fnðxÞ  ~fnðxÞ ¼
t½ ~fnðxj þ jÞ  ~fnðxj  jÞ;
xj  j a x < xj;
ð1  tÞ½ ~fnðxj þ jÞ  ~fnðxj  jÞ;
xj a x a xj þ j:
(
Now for
Ð xjþj
xjj ½ fnðxÞ  ~fnðxÞ dx, we first need to express fnðxÞ  ~fnðxÞ explicitly as
a function of x, rather than implicitly in terms of t. To do this, we have from x ¼
ð1  tÞðxj  jÞ þ tðxj þ jÞ that
t ¼ x  ðxj  jÞ
2j
;
1  t ¼ ðxj þ jÞ  x
2j
;
and so with an algebraic step,
fnðxÞ  ~fnðxÞ ¼
xðxjjÞ
2j
h
i
½ ~fnðxj þ jÞ  ~fnðxj  jÞ;
x A ½xj  j; xjÞ;
 ðxjþjÞx
2j
h
i
½ ~fnðxj þ jÞ  ~fnðxj  jÞ;
x A ½xj; xj þ j:
8
>
<
>
:
Factoring out the common terms of ½ ~fnðxj þ jÞ  ~fnðxj  jÞ and 2j, and splitting
the integral due to the discontinuity at x ¼ xj, we derive for j ¼ 0; 1; . . . ; n þ 1,
2j
½ ~fnðxj þ jÞ  ~fnðxj  jÞ
ð xjþj
xjj
½ fnðxÞ  ~fnðxÞ dx
¼
ð xj
xjj
½x  ðxj  jÞ dx 
ð xjþj
xj
½ðxj þ jÞ  x dx
¼ 0:
This approach also provides an e‰cient way to evaluate the moments and
moment-generating function for Xn, the continuously distributed random variable
with density function fnðxÞ, in terms of the respective values for ~Xn identified in
(10.133). In other words, for any function gðxÞ,
ð
gðxÞfnðxÞ dx ¼
ð
gðxÞ ~fnðxÞ dx þ
X
nþ1
j¼0
ð xjþj
xjj
gðxÞ½ fnðxÞ  ~fnðxÞ dx:
ð10:135Þ
In exercise 38 is assigned the application of (10.135) to gðxÞ ¼ x and x2 to produce
the following formulas:
10.12
Applications to Finance
667

E½Xn ¼ E½ ~Xn þ 1
6
X
n
j¼0
fBð jÞ
2
jþ1  2
j
u  d
 
!
;
ð10:136aÞ
E½X 2
n  ¼ E½ð ~XnÞ2 þ 1
3
X
n
j¼0
fBðjÞ
2
jþ1  2
j
u  d
 
!
xj þ 2
jþ1
"
#
;
ð10:136bÞ
Var½Xn ¼ Var½ ~Xn þ 1
3
X
n
j¼0
fBðjÞ
2
jþ1  2
j
u  d
 
!
ðxj  E½ ~XnÞ þ 2
jþ1
"
#
þ 1
36
X
n
j¼0
fBðjÞ
2
jþ1  2
j
u  d
 
!
"
#2
:
ð10:136cÞ
Note that if 2
j ¼ 2 for all j, these messy formulas simplify greatly to
E½Xn ¼ E½ ~Xn;
Var½Xn ¼ Var½ ~Xn þ 2
3 :
If f2
j g are not constant, some care is needed to ensure that these summations con-
verge as Dt ! 0, since n ¼ O½ðDtÞ1. For example, the first moment formula sug-
gests that in order for this summation to converge as Dt ! 0, since Pn
j¼0 fBðjÞ ¼ 1,
it is simply necessary that
2
jþ12
j
ud


must converge to 0 uniformly in j. As
u  d ¼ O½ðDtÞ1=2, if 2
jþ1  2
j ¼ O½ðDtÞð1=2Þþd for some d > 0, the resulting summa-
tion will be O½ðDtÞd and converge to 0 with Dt. This condition on 2
jþ1  2
j is gener-
ally stronger than the original defining condition that 0 < j < ud
2 ¼ O½ðDtÞ1=2.
For the second moment and variance, because maxfjxjjg ¼ O½ðDtÞ1=2, which
follows from the definition of xj, we need 2
jþ1  2
j ¼ O½ðDtÞ1þd as well as 2
jþ1 ¼
O½ðDtÞd to ensure that the terms involving f2
jþ1  2
j g and those involving f2
j g con-
verge to 0 as Dt ! 0.
In the next section, f2
j g will be chosen to do more than stabilize the limit of
these two moments of Xn as n ! y. The goal will be to ensure that the moment-
generating function of Xn converges to that of ~Xn as n ! y.
The Limiting Distribution of the ‘‘Continuitization’’
The goal of this section is to show that as Dt ! 0, the moment-generating func-
tion for the continuitization of this binomial converges to the m.g.f. of the
N
r  1
2 s2


T; s2T


. This will be demonstrated by showing that the moment-
668
Chapter 10
Calculus II: Integration

generating function of this continuitization converges with the m.g.f. of the original
binomial distribution, which, as was demonstrated in section 9.8.10, converges to the
m.g.f. of the N
r  1
2 s2


T; s2T


as Dt ! 0.
To this end, and to avoid a messy integral with fnðxÞ, we again apply (10.135):
ð
etxfnðxÞ dx ¼
ð
etx ~fnðxÞ dx þ
X
nþ1
j¼0
ð xjþj
xjj
etx½ fnðxÞ  ~fnðxÞ dx:
We now show in two steps that the first integral produces the desired result, and that
f2
j g can be chosen so that for all t the second term converges to 0 as n ! y, or
equivalently, as Dt ! 0.
1. As noted in (10.133),
ð
etx ~fnðxÞ dx ¼ etðudÞ  1
tðu  dÞ MBðtÞ;
where MBðtÞ is the moment generating function of the binomial random variable
denoted X B
n above, which takes values fxjg.
Recall that in section 9.8.10 it was demonstrated that MBðtÞ ! MZðtÞ as Dt ! 0,
with Z @ N
r  1
2 s2


T; s2T


. Also, by expanding etðudÞ as a Taylor series, and us-
ing that u  d ¼ s ffiffiffi
Dt
p
ffiffiffiffiffi
pp0
p
, we have
etðudÞ  1
tðu  dÞ ¼ 1 þ Oððu  dÞÞ
¼ 1 þ O½ðDtÞ1=2;
and so
ð
etx ~fnðxÞ dx ¼ ð1 þ O½ðDtÞ1=2ÞMBðtÞ
! MZðtÞ as Dt ! 0:
2. For the second integral, note that by the analysis in the previous section, only the
subintervals ½xj  j; xj þ j need to be evaluated, since fnðxÞ ¼ ~fnðxÞ elsewhere. As
noted above,
fnðxÞ  ~fnðxÞ ¼
xðxjjÞ
2j
h
i
½ ~fnðxj þ jÞ  ~fnðxj  jÞ;
x A ½xj  j; xjÞ;

ðxjþjÞx
2j
h
i
½ ~fnðxj þ jÞ  ~fnðxj  jÞ;
x A ½xj; xj þ j:
8
>
<
>
:
10.12
Applications to Finance
669

Now note that the coe‰cient functions of x are bounded in absolute value by 1
2 , and
since ~fnðxÞ ¼
1
ud fBðjÞ for x A ½xj; xjþ1Þ and fBðjÞ a 1 for all j, we conclude that by
the triangle inequality,
j fnðxÞ  ~fnðxÞj a
1
u  d :
So by (10.10),
ð
etx½ fnðxÞ  ~fnðxÞ dx


 a
1
u  d
X
n
j¼0
ð xjþj
xjj
etx dx
¼
1
u  d
X
n
j¼0
etðxjþjÞ  etðxjjÞ
t
:
Now, using a Taylor series expansion, we derive as j ! 0,
etðxjþjÞ  etðxjjÞ
2jt
¼ etxjð1 þ O½ðjtÞ2Þ:
From this we conclude that
ð
etx½ fnðxÞ  ~fnðxÞ dx


 a
2
u  d
X
n
j¼0
jetxjð1 þ O½ðjtÞ2Þ
¼
2
u  d
X
n
j¼0
jetnde jðudÞð1 þ O½ðjtÞ2Þ:
We are free to choose fjg at will, subject to the constraints above to preserve
moments, and so we set
j ¼
ffiffiffiffiffi
Dt
p
ejðudÞ ¼
ffiffiffiffiffi
Dt
p
exp js
ffiffiffiffiffi
Dt
p
ffiffiffiffiffiffi
pp0
p
"
#
:
ð10:137Þ
Then, since 0 a j a n ¼ T
Dt , we have that j ! 0 as Dt ! 0:
ffiffiffiffiffi
Dt
p
exp
s
ffiffiffiffiffi
Dt
p
ffiffiffiffiffiffi
pp0
p
"
#
a j a
ffiffiffiffiffi
Dt
p
;
670
Chapter 10
Calculus II: Integration

and it can be checked that these j values also satisfy the necessary moment condi-
tions above.
Substituting nd ¼ T
Dt mDt  ps ffiffiffi
Dt
p
ffiffiffiffiffi
pp 0
p


and u  d ¼ Oð
ffiffiffiffiffi
Dt
p
Þ, we derive with constants
C, c > 0, since O½ðtjÞ2 ¼ t2OðDtÞ and n ¼ T
Dt ,
ð
etx½ fnðxÞ  ~fnðxÞ dx


 a Cð1 þ t2OðDtÞÞ
X
n
j¼0
ect= ffiffiffi
Dt
p
¼ Cð1 þ t2OðDtÞÞ
T
Dt þ 1


ect= ffiffiffi
Dt
p
:
That is because there are n þ 1 constant terms in this summation.
To see that as Dt ! 0 this integral converges to 0 for all t, substitute s ¼
1ffiffiffi
Dt
p
, and
consider the limit of this upper bound as s ! y:
C 1 þ t2O
1
s2




ðTs2 þ 1Þects ! 0:
The Generalized Black–Scholes–Merton Formula
We are now in a position to address the result quoted above in (10.130). To simplify
notation, we ignore the erT term, which is simply a multiplicative factor in both the
discrete and limiting continuous pricing formulas. The major steps in this demonstra-
tion are:
1. With fnðxÞ defined as in (10.134), and f ðxÞ the normal distribution in (10.130), we
first show that as n ! y, or equivalently, Dt ! 0,
ðy
y
LðS0exÞ fnðxÞ dx !
ðy
y
LðS0exÞf ðxÞ dx:
As shown above, MXnðtÞ ! MXðtÞ pointwise for all t as Dt ! 0. Restricting to any
compact interval ½N; N, this pointwise convergence of analytic functions is there-
fore uniform.
Also, by (10.136), the collection of variances, fs2
ng is bounded, and by the Cheby-
shev inequality, for any  > 0 there is an N so that
Pr½jXj > N < ;
Pr½jXnj > N < 
for all n:
10.12
Applications to Finance
671

As noted previously but not proved, the convergence of moment-generating func-
tions also implies the pointwise convergence of fnðxÞ ! f ðxÞ, and as continuous
functions, this convergence is uniform on any compact interval, ½N; N. On this
interval, splitting LðS0exÞ into its finite number of piecewise continuous functions
on the subintervals ½aj; ajþ1 H ½N; N, we have LðS0exÞfnðxÞ ! LðS0exÞf ðxÞ uni-
formly on each subinterval, and consequently as well as on ½N; N. Hence, by
proposition 10.55,
ð ajþ1
aj
LðS0exÞfnðxÞ dx !
ð ajþ1
aj
LðS0exÞf ðxÞ dx;
for all ½aj; ajþ1 H ½N; N, and the same is then true for the integrals over ½N; N.
Putting this all together, we can split the integral over ðy; yÞ into integrals over
½N; N, ðy; N, and ½N; yÞ. We then have by the triangle inequality and (10.10),
the Chebyshev bounds above, and the assumption that LðS0exÞ is bounded and
hence jLðS0exÞj < M for some M,
ðy
y
LðS0exÞ fnðxÞ dx 
ðy
y
LðS0exÞ f ðxÞ dx


a
ð N
N
LðS0exÞ fnðxÞ dx 
ð N
N
LðS0exÞf ðxÞ dx


 þ 2M:
Since the di¤erence of integrals over ½N; N converges to 0 as n ! y, we have
shown that the di¤erence of integrals over ðy; yÞ can be made as small as desired,
proving the result.
2. Next we convert the integrals with fnðxÞ into a summation with binomial proba-
bilities, where we begin with the observation
ðy
y
LðS0exÞ fnðxÞ dx ¼
X
j
ð ajþ1
aj
LðS0exÞ fnðxÞ dx:
On each interval ½aj; ajþ1 the integrand LðS0exÞfnðxÞ is continuous by defining
LðS0exÞ at the endpoints in terms of its limiting values. Also fnðxÞ is identically 0
outside the interval ½x0; xnþ1 ¼ ½nd; ðn þ 1Þu  d. With Dx ¼ xnþ1x0
nþ1
¼ u  d, and in-
terval partition defined with xj ¼ nd þ ðu  dÞj, for j ¼ 0; 1; . . . ; n þ 1, each integral
in the summation above can be expressed as follows, where aj a xk < xkþ1 <    <
xl a ajþ1:
672
Chapter 10
Calculus II: Integration

ð ajþ1
aj
LðS0exÞfnðxÞ dx ¼
ð xk
aj
LðS0exÞ fnðxÞ dx þ
X
j
ð xjþ1
xj
LðS0exÞfnðxÞ dx
þ
ð ajþ1
xl
LðS0exÞ fnðxÞ dx:
Now by the first mean value theorem for integrals in (10.12), there is ^xj A ðxj; xjþ1Þ
with
ð xjþ1
xj
LðS0exÞ fnðxÞ dx ¼ LðS0e ^xjÞfnð^xjÞðxjþ1  xjÞ;
and similarly for the first and last integrals. For the integrals in the summation, since
^xj A ðxj; xjþ1Þ, and this interval’s value of j can be chosen smaller than defined in
(10.137), we can assume that ^xj A ðxj þ j; xjþ1  jþ1Þ and so fnð^xjÞ ¼ ~fnð^xjÞ ¼
1
ud fBð jÞ. Then, since xjþ1  xj ¼ u  d,
ð xjþ1
xj
LðS0exÞ fnðxÞ dx ¼ LðS0e ^xjÞ ~fnð^xjÞðxjþ1  xjÞ
¼ LðS0e ^xjÞ
n
j


q jð1  qÞnj:
Now, for the integrals that involve a given aj, say xk < aj < xkþ1, we combine the
integral over ½xk; aj and the integral over ½aj; xkþ1, and a similar argument produces
the following, where ^xk1 A ðxk þ k; ajÞ, ^xk2 A ðaj; xkþ1  kþ1Þ, lk1 ¼
ajxk
xkþ1xk , and
lk2 ¼ 1  lk1 ¼ xkþ1aj
xkþ1xk :
ð xkþ1
xk
LðS0exÞ fnðxÞ dx
¼
n
k


qkð1  qÞnk½lk1LðS0e ^xk1Þ þ lk2LðS0e ^xk2Þ
¼
n
k


qkð1  qÞnkLðS0e ^xk1Þ þ
n
k


qkð1  qÞnklk2½LðS0e ^xk2Þ  LðS0e ^xk1Þ:
Combining all integrals, we have that
10.12
Applications to Finance
673

ðy
y
LðS0exÞ fnðxÞ dx
¼
X
n
j¼0
n
j


q jð1  qÞnjLðS0e ^xjÞ
þ
X
ak A ðxj;xjþ1Þ
n
j


q jð1  qÞnjlj2½LðS0e ^xj2Þ  LðS0e ^xj1Þ;
ð10:138Þ
where the second summation includes only those values of j for which ak A ðxj; xjþ1Þ
for some k.
3. The final step is to show that the summations in (10.138) converge to the binomial
summation represented by L0ðS0Þ in (10.130). To this end, we show that the first
summation converges to L0ðS0Þ, and the second converges to 0 as n ! y. First o¤,
L0ðS0Þ 
X
n
j¼0
n
j


q jð1  qÞnjLðS0e ^xjÞ
¼
X
n
j¼0
n
j


q jð1  qÞnj½LðS0exjÞ  LðS0e ^xjÞ;
where by construction, ^xj A ðxj þ j; xjþ1  jþ1Þ. Also LðS0exÞ can be assumed to be
continuous at each xj, perhaps not for a fixed n for which it may happen that xj ¼ ak
for some j and k, but as n ! y, which is our concern. Consequently ^xj ! xj as
n ! y for each j. Now, because the binomial density in this summation has
bounded variance for all n, we again apply the Chebyshev inequality to derive that
for any  > 0 there is an interval ½N; N so that Pr½X B
n A ½N; N b 1   for all n.
On this interval, since LðS0exÞ is piecewise continuous with limits, and there are only
a finite number of intervals, ½ak; akþ1 H ½N; N, we conclude that as n ! y,
max
xj A ½N;N jLðS0exjÞ  LðS0e ^xjÞj ! 0:
Hence summing over all j for which xj A ½N; N produces
X
xj A ½N;N
n
j


q jð1  qÞnjjLðS0exjÞ  LðS0e ^xjÞj ! 0:
Now for all j for which xj B ½N; N, we apply the triangle inequality
674
Chapter 10
Calculus II: Integration

X
xj B ½N;N
n
j


q jð1  qÞnjjLðS0exjÞ  LðS0e ^xjÞj a 2M;
since LðS0exÞ is bounded by M and Pr½X B
n B ½N; N < . Consequently the first
summation in (10.138) converges to L0ðS0Þ as claimed.
For the second summation in (10.138), by the triangle inequality,
X
ak A ðxj;xjþ1Þ
n
j


q jð1  qÞnjlj2jLðS0e ^xj2Þ  LðS0e ^xj1Þj
a 2M
X
ak A ðxj;xjþ1Þ
n
j


q jð1  qÞnj;
since LðS0exÞ is bounded by M and 0 a lj2 a 1. We can split this summation into
the finite collection of fakg H ½N; N, and the rest, and obtain
X
ak A ðxj;xjþ1Þ
n
j


q jð1  qÞnj <
X
ak A ½N;N
n
j


q jð1  qÞnj þ :
Now, since this summation includes only those values of j for which ak A ðxj; xjþ1Þ
for some k, this finite summation converges to 0 as n ! y, completing the
derivation.
Exercises
Practice Exercises
1. Demonstrate by explicit evaluation of the Riemann sums, the following integrals
for c A R, where for simplicity assume that 0 a a < b:
(a)
Ð b
a c dx ¼ ðb  aÞc
(b)
Ð b
a cx dx ¼ c
2 ðb2  a2Þ (Hint: Pn
j¼1 j ¼ nðnþ1Þ
2
.)
(c) Ð b
a cx2 dx ¼ c
3 ðb3  a3Þ (Hint: Pn
j¼1 j2 ¼ nðnþ1Þð2nþ1Þ
6
.)
2. For the function,
f ðxÞ ¼
x2;
0 a x < 1
x2 þ 5;
1 a x a 2

Exercises
675

(a) Verify explicitly that
ð 2
0
f ðxÞ dx ¼
ð 1
0
x2 dx þ
ð2
1
ðx2 þ 5Þ dx ¼ 23
3 ;
by demonstrating that the contribution of the terms in the Riemann sums containing
the point x ¼ 1 converge to 0.
(b) Confirm that this conclusion is independent of the definition of f ð1Þ.
3. Consider a collection of intervals containing a point x0: fIjg ¼ fðx0  aj; x0 þ bjÞg,
where fajg and fbjg are positive sequences which converge to 0. Prove that for a
given function, f ðxÞ, with Mj and mj defined as in (10.2), that Mj  mj ! 0 if and
only if f ðxÞ is continuous at x0.
4. For each of the functions in exercise 1, determine the value of d as promised by
the mean value theorem for which
ð b
a
f ðxÞ dx ¼ f ðdÞðb  aÞ:
5. Using the Fundamental Theorem of Calculus version I in (10.15):
(a) Confirm the formulas in exercise 1.
(b) Generalize exercise 1 to show that for a; b A R:
ð b
a
cxn dx ¼
c
n þ 1 ðbnþ1  anþ1Þ;
n A R; n 0 1:
(c) Confirm that for part (b), if n ¼ 1,
ð b
a
cx1 dx ¼ c ln b
a
 
;
b > a > 0:
(d) Generalize part (c) if a < b < 0. (Hint: Compare
Ð b
a cx1 dx to 
Ð b
a cx1 dx to

Ð a
b cx1 dx.)
6. Use the integral test in the following analyses:
(a) Show that Py
n¼1 en converges and estimate its value. (Note: This can also be
summed exactly as a geometric series, of course, but that is not what is to be done
here.)
(b) Show that Py
n¼1 nm, for m b 1, diverges, and estimate the rate of growth of the
partial sums.
676
Chapter 10
Calculus II: Integration

(c) For 0 < q < 1, determine whether Py
n¼1 nqn converges or diverges, and corre-
spondingly estimate its summation value, or the growth rate of its partial sums.
(Hint: Integrate f ðxÞ ¼ xqx ¼ xex ln q using integration by parts.)
7. Evaluate the following definite integrals using the method of substitution, and
then identify an antiderivative of the integrand:
(a)
Ð y
0 xex2 dx (Hint: First consider
Ð N
0 xex2 dx as a definite integral.)
(b)
Ð y
0 ð4z3 þ 6zÞðz4 þ 3z2 þ 5Þ2 dz
(c)
Ð 10
0
e2x dx
4e2x1
8. Evaluate the following definite integrals using integration by parts, and then iden-
tify an antiderivative of the integrand. (General hint: Once a potential antiderivative
is found, this formula can be verified by di¤erentiation.)
(a)
Ð 10
0 xmex dx for positive integer m (Hint: Implement two or three integration by
parts steps and observe the pattern.)
(b)
Ð 20
3 xmex2 dx for positive odd integer m ¼ 2n þ 1 (Hint: Implement two or three
integration by parts steps and observe the pattern, using xex2.)
9. Show using a Taylor series expansion that if f ðyÞ ¼
1
1þy , for jyj < 1, that
Ð x
0 f ðyÞ dy ¼ lnð1 þ xÞ. Justify integrating term by term as well as the convergence
of the final series to the desired answer.
10. Using the definite integrals over bounded intervals in exercise 7(c), 8(a), and 8(b)
(use m ¼ 5 for exercise 8):
(a) Implement both the trapezoidal rule and Simpson’s rule for several values of n
and compare the associated errors. (Hint: Try n ¼ 5; 10; 25, and 100, say.)
(b) For each approximation, evaluate the error as n increases significantly, to see
if the respective orders of convergence, O
1
n2
 	
and O
1
n4
 	
, are apparent. (Hint: If
T
n ¼ jI  I Tj for Dx ¼ ba
n , the error T
n ¼ O
1
n2
 	
means that n2T
n a C T for some
constant C T as n ! y, and similarly for S
n ¼ jI  I Sj, that n4S
n a C S as n ! y.
Attempt to verify that the C T and C S values obtained are no bigger than the values
predicted in theory using the maxima of the derivatives of the given functions.)
11. Evaluate Pr½1 a X a 2 for the Cauchy distribution with x0 ¼ 1, and a scale
parameter l ¼ 2, by:
(a) Trapezoidal rule with n ¼ 30
(b) Simpson’s rule with n ¼ 30
(c) Evaluate the error in each approximation
Exercises
677

12. Derive the error estimate for Simpson’s rule over the subinterval ½a; a þ Dx.
(Hint: Use the Taylor approximation:
f ðxÞ ¼ f ðaÞ þ f 0ðaÞðx  aÞ þ 1
2 f ð2ÞðaÞðx  aÞ2
þ 1
3! f ð3ÞðaÞðx  aÞ3 þ 1
4! f ð4ÞðyÞðx  aÞ4;
for some y A ½a; a þ Dx. Calculate
Ð aþDx
a
f ðxÞ dx, using the second MVT for inte-
grals in (10.35), and also evaluate the expression for I S over this interval, and sub-
tract, recalling the intermediate value theorem in (9.1).)
13. Prove the following identities:
(a) As in (10.65): s2 ¼ E½X 2  E½X2.
(b) As in (10.66):
i. mn ¼ Pn
j¼0ð1Þnj
n
j
 	
m0
jmnj (Hint: Use the binomial theorem.)
ii. m0
n ¼ Pn
j¼0
n
j
 	
mjmnj (Hint: X ¼ ½X  m þ m.)
14. Prove the iterative formula for the beta function in (10.76):
Bðv þ 1; wÞ ¼
v
v þ w Bðv; wÞ:
(Hint: Integrate by parts to first show: Bðv þ 1; wÞ ¼ v
w Bðv; w þ 1Þ. Then by express-
ing ð1  xÞw ¼ ð1  xÞð1  xÞw1, and simplifying, that Bðv; w þ 1Þ ¼ Bðv; wÞ 
Bðv þ 1; wÞ.)
15. Derive the moment-generating function formula for the gamma distribution:
MGðtÞ ¼ ð1  btÞc;
jtj < 1
b :
(Hint:
Ð
etxfGðxÞ dx ¼
1
GðcÞ
Ð 1
b
x
b
 c1eðð1tbÞ=bÞx dx;
substitute
y ¼ x
b ,
then
z ¼
ð1  tbÞy, or do this in one step.)
16. Evaluate the present value of a 50 year annuity, payable continuously at the rate
of $1000 per year, at the continuous rate of 6%.
17. Repeat exercise 16, in the case where the annuity is continuously payable, and
continuously increasing, so that the annualized rate of payment at time t is CðtÞ ¼
1000ð1:08Þt. (Hint: Consider converting the 8% annual rate to another basis.)
18. Repeat exercise 18 of chapter 9 using the price function approximations in
(10.118) and (10.119).
678
Chapter 10
Calculus II: Integration

19. Derive (10.133). (Hint: Split each integral, such as
ð xnþ1
x0
x~fnðxÞ dx ¼
X
n
j¼0
ð xjþ1
xj
x~fnðxÞ dx:Þ
20. Assume that the price of a t-period zero-coupon bond is given by Zt ¼
1
1þt for all
t b 0.
(a) Evaluate the implied continuous forward rates, ft, and spot rates, st for all t b 0.
(b) Confirm (10.111).
21. With r ¼ 0:03 on a continuous basis, S0 ¼ 100, and ln Stþ1
St
h
i
@ Nð0:12; ð0:18Þ2Þ
over annual periods:
(a) Determine the value of a 0:5-year binary call option on a stock with payo¤
function
LðS0:5Þ ¼
10;
S0:5 > 105;
0;
S0:5 a 105:

(b) Evaluate the corresponding price for a binary put option, with payo¤ function
LðS0:5Þ ¼
0;
S0:5 b 105;
10;
S0:5 < 105:

(c) Derive put-call parity for these binary options:
LPðS0Þ þ LCðS0Þ ¼ 10e0:015:
Assignment Exercises
22. Repeat exercise 1 in the cases where:
(a) a < 0 < b
(b) a < b < 0
(Hint: Consider
Ð b
a ¼
Ð 0
a þ
Ð b
0 for part (a), and identify the relationship between
Ð 0
a
and Ð a
0
of the given functions. For part (b), consider the relationship between Ð b
a and
Ð a
b of the given functions. In both cases keep track of the sign of f ðxÞ.)
23. Show that if f ðxÞ is continuous on bounded ½a; b, so too is j f ðxÞj. In other
words, show that f ðxÞ ! f ðx0Þ implies that j f ðxÞj ! j f ðx0Þj. (Hint: To show this,
prove that
j jaj  jbj j a ja  bj:Þ
ð10:139Þ
Exercises
679

(a) Give a di¤erent example from what is in the text of where j f ðxÞj continuous does
not imply that f ðxÞ is continuous.
(b) Give a second example where the continuity of f ðxÞ2 does not imply the conti-
nuity of f ðxÞ.
24. For the functions in exercise 5(b) and 5(c), explicitly determine the value of d as
promised by the mean value theorem for which
ð b
a
f ðxÞ dx ¼ f ðdÞðb  aÞ:
25. Use the integral test in the following analyses:
(a) Show that Py
n¼1 n2en converges and estimate its value. (Hint: integrate by
parts.)
(b) Show that Py
n¼1
n
n2þ10 diverges, and estimate the rate of growth of the partial
sums.
(c) For 0 < q < 1, determine whether Py
n¼1 n2qn converges or diverges, and corre-
spondingly estimate its summation value, or the growth rate of its partial sums.
(Hint: Integrate f ðxÞ ¼ x2qx ¼ x2ex ln q using integration by parts.)
26. Evaluate the following definite integrals using the method of substitution, and
then identify an antiderivative of the integrand:
(a) Ð y
y yey2 dy (Hint: First consider Ð N
M yey2 dy as a definite integral.)
(b)
Ð 20
2
ln ffiffiw
p
w dw (Hint: Focus on ln
ffiffiffiw
p .)
(c)
Ð 10
0 ð8x3 þ 10x  3Þð2x4 þ 5x2  3xÞ1=2 dx (Hint: First consider
Ð 10
a
f ðxÞ dx for
a > 0.)
27. Evaluate the following definite integrals using integration by parts, and then
identify an antiderivative of the integrand (General hint: Once a potential antideriva-
tive is found, this formula can be verified by induction on n:):
(a)
Ð 20
0 xnerx dx for positive integer n, positive real r
(b)
Ð 10
0 xnex2 dx for positive integer odd n ¼ 2m þ 1
28. Show using a Taylor series expansion that if f ðyÞ ¼ ey, then
Ð x
0 f ðyÞ dy ¼
ex  1. Justify integrating term by term as well as the convergence of the final series
to the desired answer.
29. Assume that the value of a t-period continuous forward rate is given by ft ¼
0:03
1þ0:1t for all t b 0.
680
Chapter 10
Calculus II: Integration

(a) Evaluate the implied continuous spot rates, st, and zero-coupon bond prices, Zt,
for all t b 0.
(b) Confirm (10.111).
30. Using the definite integrals over bounded intervals in exercises 26(b) and 26(c),
and 27(a) and 27(b) (use n ¼ 10 and r ¼ 0:10 in exercise 27):
(a) Implement both the trapezoidal rule and Simpson’s rule for several values of n
and compare the associated errors. (Hint: Try n ¼ 5; 10; 25, and 100, say.)
(b) For each, evaluate the error as n increases significantly, to see if the respective
orders of convergence, O
1
n2
 	
and O
1
n4
 	
, are apparent. (Hint: If T
n ¼ jI  I Tj for
Dx ¼ ba
n , the error T
n ¼ O
1
n2
 	
means that n2T
n a C T for some constant C T as
n ! y, and similarly for S
n ¼ jI  I Sj, that n4S
n a C S as n ! y. Attempt to verify
that the C T and C S values obtained are no bigger than the values predicted in theory
using the maxima of the derivatives of the given functions.)
31. Evaluate Pr½1 a X a 5 for the gamma distribution with b ¼ 1 and shape pa-
rameter c ¼ 3, by:
(a) Trapezoidal rule with n ¼ 100
(b) Simpson’s rule with n ¼ 100
(c) Evaluate the error in each approximation
32. Prove the following identities:
(a) As in (10.67) that MXðtÞ ¼ Py
n¼0
m 0
nt n
n! (Hint: Compare to the discrete derivation in
chapter 9, using section 10.7.2 on convergence of a sequence of integrals.)
(b) As in (10.68) that m0
n ¼ MðnÞ
X ð0Þ (Note: Justify term by term di¤erentiation and
substitution of t ¼ 0.)
33. Show directly that for the beta function: Bð1; 1Þ ¼ 1, and then using the same
hint as in exercise 14, show that
Bðv; wÞ ¼
ðv  1Þðw  1Þ
ðv þ w  1Þðv þ w  2Þ Bðv  1; w  1Þ;
and that with this and mathematical induction, derive (10.78).
34. Derive the iterative formulas for moments of the unit normal:
(a) For m ¼ 1; 2; 3; . . . :
ðy
y
y2mfðyÞ dy ¼ ð2m  1Þ
ðy
y
y2m2fðyÞ dy:
Exercises
681

(Hint: Try integration by parts, splitting the integrand into y2m1 and yfðyÞ, and
note the latter can be integrated by substitution.)
(b) For m ¼ 1; 2; 3; . . . :
ðy
y
y2m1fðyÞ dy ¼ 0:
(Hint: Consider f ðyÞ and f ðyÞ, then Riemann sums.)
35. Evaluate the present value of a perpetuity, payable continuously at the rate of
$10,000 per year, at the continuous rate of 10%.
36. Repeat exercise 35 in the case where the annuity is continuously payable, and
continuously increasing, so that the annualized rate of payment at time t is CðtÞ ¼
10;000ð1 þ 2tÞ.
37. Repeat exercise 41 of chapter 9 using the price function approximations in
(10.118) and (10.119).
38. Derive (10.136). (Hint: Use (10.135) and recall that by (10.132), for j ¼ 0; 1; . . . ;
n þ 1,
~fnðxj þ jÞ  ~fnðxj  jÞ ¼
1
u  d ½ fBðjÞ  fBðj  1Þ:Þ
39. Derive the Black–Scholes–Merton formulas for the price of a European put or
call using (10.130). (Hint: Use a substitution in the integral.)
40. The notion of Riemann integral can be generalized to become a Riemann–
Stieltjes integral, in recognition of the work of Thomas Joannes Stieltjes (1856–1894).
Definition 10.86
Given a function, gðxÞ, a function f ðxÞ is Riemann–Stieltjes integra-
ble with respect to gðxÞ on an interval ½a; b if as m ! 0, with m defined as in (10.3), we
have that
X
n
i¼1
MiDgi 
X
n
i¼1
miDgi
"
#
! 0;
ð10:140Þ
where Mi and mi are defined in (10.2). Here Dgi ¼ gðx
i Þ  gðxþ
i1Þ, where gðx
i Þ ¼
limx!x
i gðxÞ and gðxþ
i1Þ ¼ limx!xþ
i1 gðxÞ, are defined as one-sided limits from the
left ðÞ and right ðþÞ. In this case we define the Riemann–Stieltjes integral of f ðxÞ
with respect to gðxÞ over ½a; b, by
682
Chapter 10
Calculus II: Integration

ð b
a
f ðxÞ dg ¼ lim
m!0
X
n
i¼1
f ð~xiÞDgi;
ð10:141Þ
which exists and is independent of the choice of exixi A ½xi1; xi by (10.140).
(a) Show that if gðxÞ and f ðxÞ are continuous on ½a; b, and gðxÞ is di¤erentiable on
ða; bÞ with g0ðxÞ a continuous function with limits as x ! a and x ! b, then
ð b
a
f ðxÞ dg ¼
ð b
a
f ðxÞg0ðxÞ dx;
ð10:142Þ
where the integral on the right is a Riemann integral. (Hint: Consider the mean value
theorem from chapter 9.)
(b) Generalize part (a) to the case where there is a partition of ½a; b:
a ¼ y0 < y1 <    < ymþ1 ¼ b
so that gðxÞ satisfies the conditions of part (a) on each subinterval, ½yj; yjþ1 but has
‘‘jumps’’ at fyjgm
j¼1:
lim
x!yjþ gðxÞ 0 lim
x!yj gðxÞ;
j ¼ 1; 2; . . . ; m:
Show that in this case
ð b
a
f ðxÞ dg ¼
X
m
j¼0
ð yjþ1
yj
f ðxÞg0ðxÞ dx þ
X
m
j¼1
f ðyjÞ½gðyþ
j Þ  gðy
j Þ:
ð10:143Þ
41. Evaluate
Ð 10
0 x2 dg with:
(a) gðxÞ ¼ e0:04x
(b) gðxÞ ¼
e0:04x;
0 a x < 2
e0:04x  4;
2 a x < 6
e0:04x þ 4;
6 a x a 10
8
<
:
42. This exercise investigates the application of Riemann–Stieltjes integration to
probability theory.
(a) Show that if f ðxÞ is a continuous probability density function with distribution
function FðxÞ, then for any function gðxÞ for which E½gðxÞ exists,
E½gðxÞ ¼
ð
gðxÞ dF:
ð10:144Þ
(Hint: Use (10.142).)
Exercises
683

(b) Show that if f ðxÞ is a discrete probability density function with domain fxjg
assumed to have no accumulation points, and with distribution function FðxÞ, that
for any function gðxÞ for which E½gðxÞ exists, (10.144) remains valid. (Hint: Use
(10.143).)
Remark 10.87
A probability density function can be mixed, meaning both with con-
tinuous and discrete components. The distribution function FðxÞ then is nondecreasing,
0 a FðxÞ a 1, has the structure required in exercise 40.b, and E½gðxÞ is again defined
as in (10.144) using (10.143).
(c) Evaluate the mean and variance of the random variable with mixed distribution
function defined by
FðxÞ ¼
0;
x < 0;
0:25;
x ¼ 0;
1
4 1 þ
x
100


;
0 < x < 50;
0:5;
x ¼ 50;
1
3 1 þ
x
100


;
50 < x < 100;
0:75;
x ¼ 100;
1  1
4 e100x;
x > 100:
8
>
>
>
>
>
>
>
>
>
>
<
>
>
>
>
>
>
>
>
>
>
:
684
Chapter 10
Calculus II: Integration

