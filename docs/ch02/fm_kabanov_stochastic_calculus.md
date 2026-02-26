# Stochastic Calculus: Advanced Topics (Festschrift)

!!! info "Source"
    **From Stochastic Calculus to Mathematical Finance: The Shiryaev Festschrift** edited by Yu. Kabanov, R. Liptser, and J. Stoyanov, Springer, 2006.
    These notes are used for educational purposes.

## Advanced Stochastic Calculus Topics

From Stochastic Calculus to Mathematical Finance

Yu. Kabanov R. Lipster J. Stoyanov
From Stochastic
Calculus to
Mathematical Finance
The Shiryaev Festschrift
With 15 Figures
ABC

Yuri Kabanov
Université de Franche-Comté
16, route de Gray
25030 Besançon Cedex
France
e-mail: youri.kabanov@math.univ-fcomte.fr
Jordan Stoyanov
School of Mathematics & Statistics
University of Newcastle
Newcastle upon Tyne
NE1 7RU
United Kingdom
e-mail: jordan.stoyanov@newcastle.ac.uk
Robert Liptser
Department of Electrical Engineering-Systems
Tel Aviv University
P.O.B. 39040, Ramat Aviv
Tel Aviv 69978
Israel
e-mail: liptser@eng.tau.ac.il
Library of Congress Control Number: 2005938923
Mathematics Subject Classification (2000): 60-XX, 93-XX
ISBN-10 3-540-30782-6 Springer Berlin Heidelberg New York
ISBN-13 978-3-540-30782-2 Springer Berlin Heidelberg New York
This work is subject to copyright. All rights are reserved, whether the whole or part of the material is
concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting,
reproduction on microfilm or in any other way, and storage in data banks. Duplication of this publication
or parts thereof is permitted only under the provisions of the German Copyright Law of September 9,
1965, in its current version, and permission for use must always be obtained from Springer. Violations
are liable for prosecution under the German Copyright Law.
Springer is a part of Springer Science+Business Media
springer.com
cSpringer-Verlag Berlin Heidelberg 2006
Printed in Germany
The use of general descriptive names, registered names, trademarks, etc. in this publication does not imply,
even in the absence of a specific statement, that such names are exempt from the relevant protective laws
and regulations and therefore free for general use.
Typesetting by the Authors and SPI Publisher Services using a Springer LATEX macro package
Cover art: Margarita Kabanova
Cover design: design & production GmbH, Heidelberg
Printed on acid-free paper
SPIN: 11591221
41/3100/SPI
5 4 3 2 1 0

To Albert Shiryaev with love, admiration and respect

Preface
This volume contains a collection of articles dedicated to Albert Shiryaev on
his 70th birthday. The majority of contributions are written by his former
students, co-authors, colleagues and admirers strongly influenced by Albert’s
scientific tastes as well as by his charisma. We believe that the papers of this
Festschrift reflect modern trends in stochastic calculus and mathematical fi-
nance and open new perspectives of further development in these fascinating
fields which attract new and new researchers. Almost all papers of the vol-
ume were presented by the authors at The Second Bachelier Colloquium on
Stochastic Calculus and Probability, Metabief, France, January 9-15, 2005.
Ten contributions deal with stochastic control and its applications to eco-
nomics, finance, and information theory.
The paper by V. Arkin and A. Slastnikov considers a model of optimal
choice of an instant to launch an investment in the setting that permits the
inclusion of various taxation schemes; a closed form solution is obtained.
M.H.A. Davis addresses the problem of hedging in a “slightly” incomplete
financial market using a utility maximization approach. In the case of the ex-
ponential utility, the optimal hedging strategy is computed in a rather explicit
form and used further for a perturbation analysis in the case where the option
underlying and traded assets are highly correlated.
The paper by G. Di Masi and L. Stettner is devoted to a comparison of
infinite horizon portfolio optimization problems with different criteria, namely,
with the risk-neutral cost functional and the risk-sensitive cost functional
dependent on a sensitivity parameter γ < 0. The authors consider a model
where the price processes are conditional geometric Brownian motions, and the
conditioning is due to economic factors. They investigate the asymptotics of
the optimal solutions when γ tends to zero. An optimization problem for a one-
dimensional diffusion with long-term average criterion is considered by A. Jack
and M. Zervos; the specific feature is a combination of absolute continuous
control of the drift and an impulsive way of repositioning the system state.

VIII
Preface
Yu. Kabanov and M. Kijima investigate a model of corporation which
combines investments in the development of its own production potential with
investments in financial markets. In this paper the authors assume that the
investments to expand production have a (bounded) intensity. In contrast to
this approach, H. Pham considers a model with stochastic production capacity
where accumulated investments form an increasing process which may have
jumps. Using techniques of viscosity solutions for HJB equations, he provides
an explicit expression for the value function.
P. Katyshev proves an existence result for the optimal coding and decoding
of a Gaussian message transmitted through a Gaussian information channel
with feedback; the scheme considered is more general than those available in
the literature.
I. Sonin and E. Presman describe an optimal behavior of a female decision-
maker performing trials along randomly evolving graphs. Her goal is to select
the best order of trials and the exit strategy. It happens that there is a kind
of Gittins index to be maximized at each step to obtain the optimal solution.
M. R´asonyi and L. Stettner consider a classical discrete-time model of
arbitrage-free financial market where an investor maximizes the expected util-
ity of the terminal value of a portfolio starting from some initial wealth. The
main theorem says that if the value function is finite, then the optimal strategy
always exists.
The paper by I. Sonin deals with an elimination algorithm suggested ear-
lier by the author to solve recursively optimal stopping problems for Markov
chains in a denumerable phase space. He shows that this algorithm and the
idea behind it can be applied to solve discrete versions of the Poisson and
Bellman equations.
In the contribution by five authors — O. Barndorff-Nielsen, S. Graversen,
J. Jacod, M. Podolski, and N. Sheppard — a concept of bipower variation
process is introduced as a limit of a suitably chosen discrete-time version.
The main result is that the difference between the approximation and the
limit, appropriately normalizing, satisfies a functional central limit theorem.
J. Carcovs and J. Stoyanov consider a two-scale system described by ordi-
nary differential equations with randomly modulated coefficients and address
questions on its asymptotic stability properties. They develop an approach
based on a linear approximation of the original system via the averaging prin-
ciple.
A note of A. Cherny summarizes relationships with various properties of
martingale convergence frequently discussed at the A.N. Shiryaev seminar. In
another paper, co-authored with M. Urusov, A. Cherny, using a concept of
separating times makes a revision of the theory of absolute continuity and
singularity of measures on filtered space (constructed, to a large extent by
A.N. Shiryaev, J. Jacod and their collaborators). The main contribution con-
sists in a detailed analysis of the case of one-dimensional distributions.
B. Delyon, A. Juditsky, and R. Liptser establish a moderate deviation prin-
ciple for a process which is a transformation of a homogeneous ergodic Markov

Preface
IX
chain by a Lipshitz continuous function. The main tools in their approach are
the Poisson equation and stochastic exponential.
A. Guschin and D. Zhdanov prove a minimax theorem in a statistical game
of statistician versus nature with the f-divergence as the loss functional. The
result generalizes a result of Haussler who considered as the loss functional
the Kullback–Leibler divergence.
Yu. Kabanov, Yu. Mishura, and L. Sakhno look for an analog of Harrison–
Pliska and Dalang–Morton–Willinger no-arbitrage criteria for random fields
in the model of Cairolli–Walsh. They investigate the problem for various ex-
tensions of martingale property for the case of two-parameter processes.
Several studies are devoted to processes with jumps, which theory seems
to be interested from the point of view of financial applications.
To this class belong the contributions by J. Fajardo and E. Mordecki
(pricing of contingent claims depending on a two-dimensional L´evy process)
and by D. Gasbarra, E. Valkeila, and L. Vostrikova where an enlargement of
filtration (important, for instance, to model an insider trading) is considered
in a general framework including the enlargement of filtration spanned by a
L´evy process.
The paper by H.-J. Engelbert, V. Kurenok, and A. Zalinescu treats the
existence and uniqueness for the solution of the Skorohod reflection problem
for a one-dimensional stochastic equation with zero drift and a measurable
coefficient in the noise term. The problem looks exactly like the one consid-
ered previously by W. Schmidt. The essential difference is that instead of the
Brownian motion, the driving noise is now any symmetric stable process of
index α ∈]0, 2].
C. Kl¨uppelberg, A. Lindner, and R. Maller address the problem of mod-
elling of stochastic volatility using an approach which is a natural continuous-
time extension of the GARCH process. They compare the properties of their
model with the model (suggested earlier by Barndorff-Nielsen and Sheppard)
where the squared volatility is a L´evy driven Ornstein–Uhlenbeck process.
A survey on a variety of affine stochastic volatility models is given in a
didactic note by I. Kallsen.
The note by R. Liptser and A. Novikov specifies the tail behavior of distri-
bution of quadratic characteristics (and also other functionals) of local mar-
tingales with bounded jumps extending results known previously only for
continuous uniformly integrable martingales.
In their extensive study, S. Lototsky and B. Rozovskii present a newly de-
veloped approach to stochastic differential equations. Their method is based
on the Cameron–Martin version of the Wiener chaos expansion and provides a
unified framework for the study of ordinary and partial differential equations
driven by finite- or infinite-dimensional noise. Existence, uniqueness, regular-
ity, and probabilistic representation of generalized solutions are established
for a large class of equations. Applications to non-linear filtering of diffusion
processes and to the stochastic Navier–Stokes equation are also discussed.

X
Preface
The short contribution by M. Mania and R. Tevzadze is motivated by
financial applications, namely, by the problem of how to characterize variance-
optimal martingale measures. To this aim the authors introduce an exponen-
tial backward stochastic equation and prove the existence and uniqueness of
its solution in the class of BMO-martingales.
The paper by J. Obl´oj and M. Yor gives, among other results, a complete
characterization of the “harmonic” functions H(x, ¯x) for two-dimensional
processes (N, ¯N) where N is a continuous local martingale and ¯N is its run-
ning maximum, i.e. ¯Nt := sups≤t Nt. Resulting (local) martingales are used
to find the solution to the Skorohod embedding problem. Moreover, the paper
contains a new interesting proof of the classical Doob inequalities.
G. Peskir studies the Kolmogorov forward PDE corresponding to the solu-
tion of non-homogeneous linear stochastic equation (called by the author the
Shiryaev process) and derives an integral representation for its fundamental
solution. Note that this equation appeared first in 1961 in a paper by Shiryaev
in connection with the quickest detection problem. In statistical literature one
can meet also the “Shiryaev–Roberts procedure” (though Roberts worked only
with a discrete-time scheme).
The note by A. Veretennikov contains inequalities for mixing coefficients
for a class of one-dimensional diffusions implying, as a corollary, that processes
of such type may have long-term dependence and heavy-tail distributions.
N. Bingham and R. Schmidt give a survey of modern copula-based meth-
ods to analyze distributional and temporal dependence of multivariate time
series and apply them to an empirical studies of financial data.
Yuri Kabanov
Robert Liptser
Jordan Stoyanov

Contents
Albert SHIRYAEV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . XV
Publications of A.N. Shiryaev . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .XXI
On Numerical Approximation of Stochastic Burgers’ Equation
Aureli ALABERT, Istv´an GY ¨ONGY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
Optimal Time to Invest under Tax Exemptions
Vadim I. ARKIN, Alexander D. SLASTNIKOV. . . . . . . . . . . . . . . . . . . . . . 17
A Central Limit Theorem for Realised Power and Bipower
Variations of Continuous Semimartingales
Ole E. BARNDORFF–NIELSEN, Svend Erik GRAVERSEN, Jean
JACOD, Mark PODOLSKIJ, Neil SHEPHARD . . . . . . . . . . . . . . . . . . . . . 33
Interplay between Distributional and Temporal Dependence.
An Empirical Study with High-frequency Asset Returns
Nick H. BINGHAM, Rafael SCHMIDT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
Asymptotic Methods for Stability Analysis of Markov
Dynamical Systems with Fast Variables
Jevgenijs CARKOVS, Jordan STOYANOV . . . . . . . . . . . . . . . . . . . . . . . . . . 91
Some Particular Problems of Martingale Theory
Alexander CHERNY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
On the Absolute Continuity and Singularity of Measures
on Filtered Spaces: Separating Times
Alexander CHERNY, Mikhail URUSOV . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Optimal Hedging with Basis Risk
Mark H.A. DAVIS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169

XII
Contents
Moderate Deviation Principle for Ergodic Markov Chain.
Lipschitz Summands
Bernard DELYON, Anatoly JUDITSKY, Robert LIPTSER . . . . . . . . . . . . 189
Remarks on Risk Neutral and Risk Sensitive Portfolio
Optimization
Giovanni B. DI MASI, 3Lukasz STETTNER . . . . . . . . . . . . . . . . . . . . . . . . 211
On Existence and Uniqueness of Reflected Solutions
of Stochastic Equations Driven by Symmetric Stable
Processes
Hans-J¨urgen ENGELBERT, Vladimir P. KURENOK, Adrian
ZALINESCU . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
A Note on Pricing, Duality and Symmetry
for Two-Dimensional L´evy Markets
Jos´e FAJARDO, Ernesto MORDECKI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249
Enlargement of Filtration and Additional Information
in Pricing Models: Bayesian Approach
Dario GASBARRA, Esko VALKEILA, Lioudmila VOSTRIKOVA . . . . . 257
A Minimax Result for f-Divergences
Alexander A. GUSHCHIN, Denis A. ZHDANOV . . . . . . . . . . . . . . . . . . . . 287
Impulse and Absolutely Continuous Ergodic Control
of One-Dimensional Itˆo Diffusions
Andrew JACK, Mihail ZERVOS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
A Consumption–Investment Problem with Production
Possibilities
Yuri KABANOV, Masaaki KIJIMA
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
Multiparameter Generalizations of the Dalang–Morton–
Willinger Theorem
Yuri KABANOV, Yuliya MISHURA, Ludmila SAKHNO
. . . . . . . . . . . 333
A Didactic Note on Affine Stochastic Volatility Models
Jan KALLSEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
Uniform Optimal Transmission of Gaussian Messages
Pavel K. KATYSHEV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 369
A Note on the Brownian Motion
Kiyoshi KAWAZU . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 385
Continuous Time Volatility Modelling: COGARCH versus
Ornstein–Uhlenbeck Models
Claudia KL ¨UPPELBERG, Alexander LINDNER, Ross MALLER . . . . . . 393

Contents
XIII
Tail Distributions of Supremum and Quadratic Variation
of Local Martingales
Robert LIPTSER, Alexander NOVIKOV
. . . . . . . . . . . . . . . . . . . . . . . . . . . 421
Stochastic Differential Equations: A Wiener Chaos Approach
Sergey LOTOTSKY and Boris ROZOVSKII . . . . . . . . . . . . . . . . . . . . . . . . 433
A Martingale Equation of Exponential Type
Michael MANIA, Revaz TEVZADZE
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507
On Local Martingale and its Supremum:
Harmonic Functions and beyond.
Jan OB3L ´OJ, Marc YOR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 517
On the Fundamental Solution of the Kolmogorov–Shiryaev
Equation
Goran PESKIR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 535
Explicit Solution to an Irreversible Investment Model
with a Stochastic Production Capacity
Huyˆen PHAM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 547
Gittins Type Index Theorem for Randomly Evolving Graphs
Ernst PRESMAN, Isaac SONIN
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 567
On the Existence of Optimal Portfolios for the Utility
Maximization Problem in Discrete Time Financial Market
Models
Mikl´os R ´ASONYI, 3Lukasz STETTNER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 589
The Optimal Stopping of a Markov Chain and Recursive
Solution of Poisson and Bellman Equations
Isaac M. SONIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 609
On Lower Bounds for Mixing Coefficients of Markov
Diffusions
A.Yu. VERETENNIKOV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 623


Albert SHIRYAEV
Albert Shiryaev, outstanding Russian mathematician, celebrated his 70th
birthday on October 12, 2004. The authors of this biographic note, his former
students and collaborators, have the pleasure and honour to recollect briefly
several facts of the exciting biography of this great man whose personality
influenced them so deeply.
Albert’s choice of a mathematical career was not immediate or obvious. In
view of his interests during his school years, he could equally well have become
a diplomat, as his father was, or a rocket engineer as a number of his relatives
were. Or even a ballet dancer or soccer player: Albert played right-wing in
a local team. However, after attending the mathematical evening school at
Moscow State University, he decided – definitely – mathematics. Graduating
with a Gold Medal, Albert was admitted to the celebrated mechmat, the
Faculty of Mechanics and Mathematics, without taking exams, just after an
interview. In the 1950s and 1960s this famous faculty was at the zenith of
its glory: rarely in history have so many brilliant mathematicians, professors
and students – real stars and superstars – been concentrated in one place,
at the five central levels of the impressive university building dominating the
Moscow skyline. One of the most prestigious chairs, and the true heart of the
faculty, was Probability Theory and Mathematical Statistics, headed by A.N.
Kolmogorov. This was Albert’s final choice after a trial year at the chair of
Differential Equations.
In a notice signed by A.N. Kolmogorov, then the dean of the fac-
ulty, we read: “Starting from the fourth year A. Shiryaev, supervised by
R.L. Dobrushin, studied probability theory. His subject was nonhomogeneous
composite Markov chains. He obtained an estimate for the variance of the sum
of random variables forming a composite Markov chain, which is a substantial
step towards proving a central limit theorem for such chains. This year A.
Shiryaev has shown that the limiting distribution, if it exists, is necessarily
infinitely divisible”.
Besides mathematics, what was Albert’s favourite activity? Sport, of
course. He switched to downhill skiing, rather exotic at that time, and it

XVI
Albert Shiryaev
became a lifetime passion. Considering the limited facilities available in Cen-
tral Russia and the absence of equipment, his progress was simply astonish-
ing: Albert participated in competitions of the 2nd Winter Student Games in
Grenoble and was in the first eight in two slalom events! Since then he has
done much for the promotion of downhill skiing in the country, and even now
is proud to compete successfully with much younger skiers. Due to him, skiing
became the most popular sport amongst Soviet probabilists.
Albert’s mathematical talent and human qualities were noticed by Kol-
mogorov who became his spiritual father. Kolmogorov offered Albert and his
friend V. Leonov positions in the department he headed at the Steklov Math-
ematical Institute, where the two of them wrote their well-known paper of
1959 on computation of semi-invariants.
In Western surveys of Soviet mathematics it is often noted that, unlike
European and American schools, in the Soviet Union it was usual not to
limit the research interests to pure mathematics. Many top Russian mathe-
maticians renowned for their great theoretical achievements have also worked
fruitfully on the most applied, but practically important, problems arising in
natural and social sciences and engineering. The leading example was Kol-
mogorov himself, with his enormous range of contributions from turbulence
to linguistics.
Kolmogorov introduced Albert to the so-called “disorder” or “quickest de-
tection” problem. This was a major theoretical challenge but also had impor-
tant applications in connection with the Soviet Union’s air defence system. In a
series of papers the young scientist developed, starting from 1960, a complete
theory of optimal stopping of Markov processes in discrete and continuous
time, summarized later in his well-known monograph Statistical Sequential
Analysis: Optimal Stopping Rules, published in successive editions in Russian
(1969, 1977) and English (1972, 1978). It is worth noting that the passage to
continuous-time modelling turned out to be a turning point in the application
of Ito calculus. A firm theoretical foundation built by Albert gave a rigorous
treatment, replacing the heuristic arguments employed in early studies in elec-
tronic engineering, which sometimes led to incorrect results. The stochastic
differential equations (known as Shiryaev’s equations) describing the dynam-
ics of the sufficient statistics were the basis of nonlinear filtering theory. The
techniques used to determine optimal stopping rules revealed deep relations
with a moving boundary problem for the second-order PDEs (known as the
Stefan problem). Shiryaev’s pioneering publications and his monograph are
cited in almost every publication on sequential analysis and optimal stopping,
showing the deep impact of his studies.
The authors of this note were Albert’s students at the end of sixties,
charmed by his energy, deep understanding of random processes, growing eru-
dition, and extreme feeling for innovative approaches and trends. His seminar,
first taking place at Moscow State University, at the Laboratory of Statistical
Methods (organized and directed by A.N. Kolmogorov who invited Albert to
be a leader of one of his teams) and hosted afterwards at Steklov Institute,

Albert Shiryaev
XVII
became more and more popular as a prestigious place for exchanging new
ideas and presenting current research. At that period Albert concentrated his
efforts on nonlinear filtering, prediction and smoothing of partially observed
processes. Jointly with his colleagues and students, Shiryaev created a general
theory for diffusion-type processes (stochastic partial differential equation for
the filtering density) and for Markov processes with countable set of states,
extending the well-known Kalman–Bucy filtering equation to the condition-
ally Gaussian case. His students were working on topics including stochastic
differential equations, anticipating stochastic calculus, and point processes.
Naturally, these studies were not restricted to purely theoretical exercises
but followed a quest for possible applications, such as optimal control with
incomplete data, optimal coding/decoding in noisy information channels, sta-
tistical inference for diffusion processes, and even using the noise-free Kalman
filter for solving ill-posed systems of linear algebraic equations. An account
of these researches can be found in the book Statistics of Random Processes,
written with Robert Liptser. This book has been appreciated by generations
of scholars: it first appeared in Russian in 1974 while the 2nd English edition
(in two volumes) appeared in 2000!
The end of the seventies was a revolution in the theory of random
processes: the construction of stochastic calculus (i.e. theory of semimartin-
gales) as a unified theory was completed. It combines the classical Ito calculus,
jump processes and discrete-time models. This was done by the efforts of the
French and Soviet schools, especially that of P.-A. Meyer (with his funda-
mental works on the general theory of processes and stochastic integration),
J. Jacod, A.V. Skorohod, and A. Shiryaev. Symbolically, two prestigious ple-
nary talks in Probability Theory at the International Mathematical Congress
in Helsinki (1978) were given by representatives of these schools (a scarce
event because of the historical dominance of classical fields!). The talk by
Claude Dellacherie was an announcement that the calculus had achieved its
most general form: a process with respect to which one can integrate while
preserving natural properties must be a semimartingale. The talk by Albert
Shiryaev was about necessary and sufficient conditions for absolute continuity
of measures corresponding to semimartingales or, more generally, of measures
on a filtered probability space, results whose importance was fully revealed
much later, in the context of financial modelling.
At the beginning of the eighties Albert launched another ambitious project:
functional limit theorems for semimartingales as an application of stochastic
calculus to the classical branch of probability theory. He was one of the first
who understood the importance of the canonical decomposition and triplets
of predictable characteristics introduced by J. Jacod in an analogy with the
L´evy–Khinchine formula. Convergence of triplets implies convergence of dis-
tributions: the observation permitting to put many traditional limit theorems,
even the ones for models with dependent summands, into a much more general
context of weak convergence of distributions of semimartingales. These studies
resulted in two fundamental monographs, The Theory of Martingales (1986)

XVIII
Albert Shiryaev
and Limit Theorems for Stochastic Processes (1987) co-authored, respectively,
with R. Liptser and J. Jacod.
It was observed by Harrison and Pliska in 1981 that stochastic calculus is
tailor-made for financial modelling. On the other hand, pricing of American
options is reduced to a solution of an optimal stopping problem. So it is not
surprising that Albert, just starting to work in mathematical finance, imme-
diately contributed to this new field by a number of interesting results (see his
works with L. Shepp, D. Kramkov, M. Jeanblanc, M. Yor and many others).
The true surprise was perhaps a voluminous book written in record time (just
in two years): Essentials of Stochastic Finance: Facts, Models, Theory (1998),
reprinted annually because of a regularly exhausted stock.
What is the best textbook in probability for mathematical students? There
are many; but our favourite is Probability by A.N. Shiryaev (editions in
Russian, English, German,...) which can be considered as an elementary in-
troduction into the technology of stochastic calculus containing a number of
rather recent results for discrete-time models. The latest valuable addendum
to this textbook is a volume of selected problems.
Shiryaev’s charisma always attracted students who never regretted the
choice of their supervisor as “doctor father”. More than fifty scholars are
proud to be his PhD-students, and they are working worldwide. Thousands
followed his brilliant lectures at the Moscow State University where he has
been Professor since 1970 and the Head of the Chair of Probability Theory
since 1996.
Albert was engaged in editorial activity from his first days at the Steklov
Institute. He was charged by Kolmogorov with serving as an assistant for the
newly established Probability Theory and Its Applications (now subtitled ‘The
Kolmogorov Journal’); he was the deputy of the Editor Yu. V. Prohorov from
1988. He has served on the editorial boards of a long list of distinguished
mathematical, statistical, and mathematical finance journals, and is, for ex-
ample, currently a co-editor of Finance and Stochastics. Throughout his career
he has championed in a very active way the traditions of good mathematical
literature, and been a severe critic of sloppily written texts.
Among his publishing activities we should also mention his recent great
efforts in the promotion of Kolmogorov’s legacy: three volumes of inestimable
historical documents including a diary, correspondence, bibliography and
memoirs. Albert is especially proud of the production of a DVD with a doc-
umentary about the life of his great teacher and his scientific heritage.
A further aspect of his work has been enthusiastic participation in the orga-
nization of memorable international meetings and large-scale events strongly
influencing the life of the mathematical community: the Soviet–Japanese Sym-
posia in Probability Theory (starting from 1969), the First World Congress
of the Bernoulli Society (Tashkent, 1986), the Kolmogorov Centenary Confer-
ence (Moscow, 2003), and many others.

Albert Shiryaev
XIX
Albert’s mathematical achievements and services to the mathematical
community have been recognized in a series of international honours and
awards, some of which are listed below.
On October 12, 2004, Albert Shiryaev tuned seventy years old, but he
remains young as never before.
Albert N. Shiryaev: Honours and Awards
Honorary Fellow of the Royal Statistical Society (1985).
Member of the Academia Europea (1990).
Correspondent member of the Russian Academy of Sciences (1997).
Member of the New York Academy of Science (1997).
President of the Bernoulli Society (1989-1991).
President of the Russian Actuarial Society (1994-1998).
President of the Bachelier Finance Society (1998-1999).
Markov prize winner (1974), Kolmogorov prize winner (1994).
Humboldt Research Award (1996).
Doctor Rerum Naturalium Honoris Causa Albert-Ludwig-Universit¨at
Freiburg-im-Bresgau (2000).
Professor Honoris Causa of the Amsterdam University (2002).


Publications of A.N. Shiryaev
I. Monographs and textbooks
1. Additional Chapters of Probability Theory. (Russian) Moscow: Moscow
Univ. Press, 1968, 207 pp.
2. Statistical Sequential Analysis: Optimal Stopping Rules. (Russian) Moscow:
“Nauka”, 1969. 231 pp.
3. Stochastic Processes. (Russian) Moscow: Moscow Univ. Press, 1972,
241 pp.
4. Statistical Sequential Analysis. Optimal Stopping Rules. (Engl. transl. of
\[2].) Transl. Math. Monogr., 38. Providence, RI: Amer. Math. Soc., 1973.
iv+174 pp.
5. Probability, Statistics, Random Processes. I. (Russian) Moscow: Moscow
Univ. Press, 1973. 204 pp.
6. Probability, statistics, random processes. II. (Russian) Moscow: Moscow
Univ. Press, 1974. 224 pp.
7. Statistics of Random Processes. Nonlinear Filtering and Related Problems.
(Russian) Probab. Theory Math. Statist., 15. Moscow: “Nauka”, 1974.
696 pp.
8. Statistical Sequential Analysis. Optimal Stopping Rules. 2nd ed., revised.
(Russian) Moscow: “Nauka”, 1976. 272 pp.
9. Statistics of Random Processes. I. General Theory. II. Applications. (Engl.
transl. of \[7].) Appl. Math., 5, 6. New York–Heidelberg: Springer-Verlag,
1977. x+394 pp.; 1978. x+339 pp. (with R. Sh. Liptser).
10. Optimal Stopping Rules. (Engl. transl. of \[8].) Appl. Math., 8. New York–
Heidelberg: Springer-Verlag, 1978. x+217 pp.
11. Probability. (Russian) Moscow: “Nauka”, 1980. 576 pp.
12. Statistics of Random Processes. Nonlinear Filtration and Related Ques-
tions. (Polish transl. of \[7].) Warsaw: Pa´nstwowe Wydawnictwo Naukowe
(PWN), 1981. 680 pp. (with R. Sh. Liptser).
13. Probability. (Engl. transl. of \[11].) Graduate Texts in Mathematics, 95.
New York: Springer-Verlag, 1984. xi+577 pp.
14. Contiguity and the Statistical Invariance Principle. Stochastics Mono-
graphs, 1. New York: Gordon & Breach, 1985. viii+236 pp. (with
P. E. Greenwood).
15. Theory of Martingales. (Russian) Probability Theory and Mathematical
Statistics. Moscow: “Nauka”, 1986. 512 pp. (with R. Sh. Liptser).
16. Limit Theorems for Stochastic Processes. Grundlehren der Mathematis-
chen Wissenschaften, 288. Berlin: Springer-Verlag, 1987. xviii+601 pp.
(with J. Jacod).

XXII
Publications of A.N. Shiryaev
17. Wahrscheinlichkeit. (German transl. of \[11].) Hochschulbucher fur Math-
ematik, 91. Berlin: VEB Deutscher Verlag der Wissenschaften, 1988.
592 pp.
18. Probability. (Russian) 2nd ed. of \[11]. Moscow: “Nauka”, 1989. 640 pp.
19. Theory of Martingales. (Engl. transl. of \[15].) Math. Appl. (Soviet
Ser.), 49. Dordrecht: Kluwer Acad. Publ., 1989. xiv+792 pp. (with
R. Sh. Liptser).
20. Limit theorems for stochastic processes. Vol. 1, 2. (Russian transl. of \[16].)
Probab. Theory Math. Statist., 47, 48. Moscow: Fizmatlit, “Nauka”, 1994.
544 pp., 368 pp. (with J. Jacod).
21. Probability. 2nd ed. (Engl. transl. of \[18].) Graduate Texts in Mathematics,
95. New York: Springer-Verlag, 1995. xi+609 pp.
22. Essentials of Stochastic Finance. (Russian) Vol. I: Facts and Models. Vol.
II: Theory. Moscow: “FAZIS”, 1998. 1018 pp.
23. Essentials of Stochastic Finance. Facts, Models, Theory. (Engl. transl. of
\[22].) Adv. Ser. Statist. Sci. Appl. Probab., 3. River Edge, NJ: World
Scientific, 1999. xvi+834 pp. Reprinted 1999, 2000, 2001, 2003.
24. Statistical Experiments and Decision. Asymptotic Theory. River Edge, NJ:
World Scientific, 2000. xvi+281 pp. (with V. G. Spokoiny).
25. Statistics of Random Processes. 2nd rev. and expanded ed. of \[9].)
Vol. I: General Theory. Vol. II: Applications. Appl. Math. (New York),
5, 6. Berlin: Springer-Verlag, 2001. xv+427 pp., xv+402 pp. (with
R. Sh. Liptser).
26. Limit Theorems for Stochastic Processes. 2nd expanded ed. of \[16].)
Grundlehren der Mathematischen Wissenschaften. 288. Berlin: Springer-
Verlag, 2003. xx+661 pp.
27. Theory of Random Processes. (Russian) Moscow: Fizmatlit, 2003. 399 pp.
(with A. V. Bulinsky).
28. Essentials of Stochastic Finance. (Russian) Vol. I: Facts and Models.
Vol. II: Theory. 2nd corrected ed. of \[22]. Moscow: “FAZIS”, 2004.
xxxviii+1018 pp.
II. Main scientific papers
1. A central limit theorem for complex inhomogeneous Markov chains.
(Russian) Teor. Veroyatnost. i Primenen. 2 (1957), no. 4, 485–486; Engl.
transl. in Theory Probab. Appl. 2 (1957), no. 4, 477–478.
2. On a method of calculation of semi-invariants. (Russian) Teor. Veroyat-
nost. i Primenen. 4 (1959), no. 3, 341–355; Engl. transl. in Theory Probab.
Appl. 4 (1960), no. 3, 319–329 (with V. P. Leonov).
3. Some problems in the spectral theory of higher-order moments. I.
(Russian) Teor. Veroyatnost. i Primenen. 5 (1960), no. 3, 293–313; cor-
rections: ibid. no. 4; Engl. transl. in Theory Probab. Appl. 5 (1960), no. 3,
265–284; corrections: ibid. no. 4.
4. Some problems in the spectral theory of higher-order moments. II.
(Russian) Teor. Veroyatnost. i Primenen. 5 (1960), no. 4, 460–464; Engl.

Publications of A.N. Shiryaev
XXIII
transl. in Theory Probab. Appl. 5 (1960), no. 4, 417–421 (with V. P. Leo-
nov).
5. The detection of spontaneous effects. (Russian) Dokl. Akad. Nauk SSSR
138 (1961), no. 4, 799–801; Engl. transl. in Soviet Math. Dokl. 2 (1961),
no. 1, 740–743.
6. The problem of the most rapid detection of a disturbance of a stationary
regime. (Russian) Dokl. Akad. Nauk SSSR 138 (1961), no. 5, 1039–1042;
Engl. transl. in Soviet Math. Dokl. 2 (1961), 795–799.
7. A problem of quickest detection of a disturbance of a stationary regime.
(Russian) PhD Thesis. Moscow: Steklov Institute of Mathematics, 1961.
130 pp.
8. Problems of rapid detection of a moment when probabilistic characteristics
of a process change. (Russian) Teor. Veroyatnost. i Primenen. 7 (1962),
no. 2, 236–238; Engl. transl. in Theory Probab. Appl. 7 (1962), no. 2,
225–226.
9. An application of the concept of entropy to signal-detection problems in
presence of noise. (Russian) Litovsk. Mat. Sb. 3 (1963), no. 1, 107–122
(with R. L. Dobrushin and M. S. Pinsker).
10. On optimal methods in quickest detection problems. (Russian) Teor.
Veroyatnost. i Primenen. 8 (1963), no. 1, 26–51; Engl. transl. in Theory
Probab. Appl. 8 (1963), no. 1, 22–46.
11. On detecting of disorders in industrial processes. I. (Russian) Teor. Veroy-
atnost. i Primenen. 8 (1963), no. 3, 264–281; Engl. transl. in Theory
Probab. Appl. 8 (1963), no. 3.
12. On detecting of disorders in industrial processes. II. (Russian) Teor.
Veroyatnost. i Primenen. 8 (1963), no. 4, 431–443; Engl. transl. in Theory
Probab. Appl. 8 (1963), no. 4.
13. On conditions for ergodicity of stationary processes in terms of higher-
order moments. (Russian) Teor. Veroyatnost. i Primenen. 8 (1963), no. 4,
470–473; Engl. transl. in Theory Probab. Appl. 8 (1963), no. 4, 436–439.
14. On problems of quickest detection of randomly arising effects. (Russian)
Proceedings of the IV All-Union Mathematical Congress. Leningrad, 1964,
pp. 379–383.
15. On the theory of decision functions and control of a process of observa-
tion based on incomplete information. (Russian) Transactions of the Third
Prague Conference on Information Theory, Statistical Decision Functions,
Random Processes (Liblice, 1962). 1964, pp. 657–681; Engl. transl. in Se-
lect. Transl. Math. Statist. Probab. 6 (1966), 162–188.
16. On finding optimal controls. (Russian) Trudy Mat. Inst. Steklova 71
(1964), 21–25 (with V. I. Arkin and V. A. Kolemaev).
17. On control leading to optimal stationary states. (Russian) Trudy Mat.
Inst. Steklova 71 (1964), 35–45; Engl. transl. in Select. Transl. Math. Sta-
tist. Probab. 6 (1966), 71-83 (with O. V. Viskov).
18. Detection of randomly appearing target in a multichannel system.
(Russian) Trudy Mat. Inst. Steklova 71 (1964), 113–117.

XXIV
Publications of A.N. Shiryaev
19. On Markov sufficient statistics in non-additive Bayes problems of sequen-
tial analysis. (Russian) Teor. Veroyatnost. i Primenen. 9 (1964), no. 4,
670–686; Engl. transl. in Theory Probab. Appl. 9 (1964), no. 4, 604–618.
20. A Bayesian problem of sequential search in diffusion approximation.
(Russian) Teor. Veroyatnost. i Primenen. 10 (1965), no. 1, 192–199; Engl.
transl. in Theory Probab. Appl. 10 (1965), no. 1, 178–186 (with R. Sh. Lip-
tser).
21. Some exact formulas in a “disorder” problem. (Russian) Teor. Veroy-
atnost. i Primenen. 10 (1965), no. 2, 380–385; Engl. transl. in Theory
Probab. Appl. 10 (1965), no. 2, 349–354.
22. Criteria of “truncation” for the optimal stopping time in sequential analy-
sis. (Russian) Teor. Veroyatnost. i Primenen. 10 (1965), no. 4, 601–613;
Engl. transl. in Theory Probab. Appl. 10 (1965), no. 4, 541–552 (with
B. I. Grigelionis).
23. Sequential analysis and controlled random processes (discrete time).
(Russian) Kibernetika (Kiev) no. 3 (1965), 1–24.
24. On stochastic equations in the theory of conditional Markov processes.
(Russian) Teor. Veroyatnost. i Primenen. 11 (1966), no. 1, 200–205; cor-
rections: ibid. 12 (1967), no. 2; Engl. transl. in Theory Probab. Appl. 11
(1966), no. 1, 179–184; corrections: ibid. 12 (1967), no. 2, 342.
25. Stochastic equations of non-linear filtering of jump-like Markov processes.
(Russian) Problemy Peredachi Informatsii 2 (1966), no. 3, 3–22; correc-
tions: ibid., 3 (1967), no. 1, 86–87; Engl. transl. in Problems Information
Transmission 2 (1966), no. 3, 1–18.
26. On Stefan’s problem and optimal stopping rules for Markov processes.
(Russian) Teor. Veroyatnost. i Primenen. 11 (1966), no. 4, 612–631; Engl.
transl. in Theory Probab. Appl. 11 (1966), no. 4, 541–558 (with B. I. Grige-
lionis).
27. Some new results in the theory of controlled random processes. (Russian)
Transactions of the Fourth Prague Conference on Information Theory,
Statistical Decision Functions, Random Processes (Prague, 1965). Prague:
Czechoslovak Acad. Sci., 1967, pp. 131–201; Engl. transl. in Select. Transl.
Math. Statist. Probab. 8 (1969), 49–130.
28. Two problems of sequential analysis. (Russian) Kibernetika (Kiev) no. 2
(1967), 79–86; Engl. transl. in Cybernetics 3 (1967), no. 2, 63–69.
29. Studies in statistical sequential analysis. Dissertation for degree of Doc-
tor of Phys.-Math. Sci. Moscow: Steklov Institute of Mathematics, 1967.
400 pp.
30. Controllable Markov processes and Stefan’s problem. (Russian) Problemy
Peredachi Informatsii 4 (1968), no. 1, 60–72; Engl. transl. in Problems
Information Transmission 4 (1968), no. 1, 47–57 (1969) (with B. I. Grige-
lionis).
31. Nonlinear filtering of Markov diffusion processes. (Russian) Trudy Mat.
Inst. Steklova 104 (1968), 135–180; Engl. transl. in Proc. Steklov Inst.
Math. 104 (1968), 163–218 (with R. Sh. Liptser).

Publications of A.N. Shiryaev
XXV
32. The extrapolation of multidimensional Markov processes from incomplete
data. (Russian) Teor. Veroyatnost. i Primenen. 13 (1968), no. 1, 17–
38; Engl. transl. in Theory Probab. Appl. 13 (1968), no. 1, 15–38 (with
R. Sh. Liptser).
33. Cases admitting effective solution of non-linear filtration, interpolation,
and extrapolation problems. (Russian) Teor. Veroyatnost. i Primenen. 13
(1968), no. 3, 570–571; Engl. transl. in Theory Probab. Appl. 13 (1968),
no. 3, 536–537 (with R. Sh. Liptser).
34. Non-linear interpolation of components of Markov diffusion processes (di-
rect equations, effective formulas). (Russian) Teor. Veroyatnost. i Prime-
nen. 13 (1968), no. 4, 602–620; Engl. transl. in Theory Probab. Appl. 13
(1968), no. 4, 564–583 (with R. Sh. Liptser).
35. Investigations on statistical sequential analysis. (Summary of the results
of the Dissertation for degree of Doctor of Phys.-Math. Sci.) (Russian)
Mat. zametki 3 (1968), no. 6, 739–754; Engl. transl. in Math. Notes 3
(1968), 473–482.
36. Optimal stopping rules for Markov processes with continuous time. (With
discussion.) Bull. Inst. Internat. Statist. 43 (1969), book 1, 395–408.
37. Interpolation and filtering of jump-like component of a Markov process.
(Russian) Izv. Akad. Nauk SSSR, Ser. Mat. 33 (1969), no. 4, 901-914;
Engl. transl. in Math. USSR, Izv. 3 (1969), 853–865 (with R. Sh. Liptser).
38. On the density of probability measures of diffusion-type processes.
(Russian) Izv. Akad. Nauk SSSR, Ser. Mat. 33 (1969), no. 5, 1120-1131;
Engl. transl. in Math USSR, Izv. 3 (1969), 1055–1066 (with R. Sh. Liptser).
39. Sur les ´equations stochastiques aux d´eriv´ees partielles. Actes du Congr`es
International des Math´ematiciens (Nice, 1970), t. 2. Paris: Gauthier-
Villars, 1971, pp. 537–544.
40. Minimax weights in a trend detection problem of a random process.
(Russian) Teor. Veroyatnost. i Primenen. 16 (1971), no. 2, 339–345; Engl.
transl. in Theory Probab. Appl. 16 (1971), no. 2, 344–349 (with I. L. Lego-
staeva).
41. On infinite order systems of stochastic differential equations arising in
the theory of optimal non-linear filtering. (Russian) Teor. Veroyatnost. i
Primenen. 17 (1972), no. 2, 228–237; Engl. transl. in Theory Probab. Appl.
17 (1972), no. 2, 218–226 (with B. L. Rozovskii).
42. Statistics of conditionally Gaussian random sequences. Proceedings of
the Sixth Berkeley Symposium on Mathematical Statistics and Probabil-
ity (Univ. of California, Berkeley, 1970/1971). Vol. II: Probability the-
ory. Berkeley, Calif.: Univ. of Califonia Press, 1972, pp. 389–422 (with
R. Sh. Liptser).
43. On the absolute continuity of measures corresponding to processes of diffu-
sion type relative to a Wiener measure. (Russian) Izv. Akad. Nauk SSSR,
Ser. Mat. 36 (1972), no. 4, 847–889; Engl. transl. in Math USSR, Izv. 6
(1972), no. 4, 839–882 (with R. Sh. Liptser).

XXVI
Publications of A.N. Shiryaev
44. On stochastic partial differential equations. (Russian) International Con-
gress of Mathematicians (Nice, 1970). Lectures of Soviet mathematicians.
Moscow, 1972, pp. 336–344.
45. Statistics of diffusion type processes. Proceedings of the Second Japan-
USSR Symposium on Probability Theory (Kyoto, 1972). Lecture Notes in
Math., 330. Berlin: Springer-Verlag, 1973, pp. 397–411.
46. On the structure of functionals and innovation processes for the Itˆo
processes. (Russian) International Conference on Probability Theory and
Mathematical Statistics (Vilnius, 1973). Abstract of communications. Vol.
2. Vilnius: Akad. Nauk Litovsk. SSR, 1973, pp. 339–344.
47. Optimal filtering of random processes. (Russian) Probabilistic and Sta-
tistical Methods. International summer school on probability theory and
mathematical statistics (Varna, 1974). Sofia: Bulgar. Akad. Nauk, Inst.
Mat. i Meh., 1974, pp. 126–199.
48. Statistics of diffusion processes. Progress in Statistics, European meeting
of statisticians (Budapest, 1972). Vol. II. Colloq. Math. Soc. J´anos Bolyai,
9. Amsterdam: North-Holland, 1974, pp. 737–751.
49. Optimal control of one-dimensional diffusion processes. Supplementary
Preprints of the Stochastic Control Symposium (Budapest). 1974. 8 pp.
50. Reduced form of nonlinear filtering equations. Supplementary Preprints of
the Stochastic Control Symposium (Budapest). 1974. 8 pp. (with B. L. Ro-
zovsky).
51. Reduction of data with preservation of information, and innovation
processes. (Russian) Proceedings of the School and Seminar on the The-
ory of Random Processes (Druskininkai, 1974), Part II. Vilnius: Inst. Fiz.
i Mat. Akad. Nauk Litovsk. SSR, 1975, pp. 235–267.
52. Martingale methods in the theory of point processes. (Russian) Proceed-
ings of the School and Seminar on the Theory of Random Processes
(Druskininkai, 1974), Part II. Vilnius: Inst. Fiz. i Mat. Akad. Nauk
Litovsk. SSR, 1975, pp. 269–354 (with Yu. M. Kabanov and R. Sh. Liptser).
53. Criteria of absolute continuity of measures corresponding to multivari-
ate point processes. Proceedings of the Third Japan-USSR Symposium
on Probability Theory (Tashkent, 1975), pp. 232–252. Lecture Notes in
Math., 550. Berlin: Springer-Verlag, 1976 (with Yu. M. Kabanov and
R. Sh. Liptser).
54. On the question of absolute continuity and singularity of probability mea-
sures. (Russian) Mat. Sb. (N.S.) 104(146) (1977), no. 2(10), 227–247,
335; Engl. transl. in Math. USSR, Sb. 33 (1977), no. 2, 203–221 (with
Yu. M. Kabanov and R. Sh. Liptser).
55. “Predictable” criteria for absolute continuity and singularity of probability
measures (the continuous time case). (Russian) Dokl. Akad. Nauk SSSR
237 (1977), no. 5, 1016–1019; Engl. transl. in Soviet Math. Dokl. 18 (1977),
no. 6, 1515–1518 (with Yu. M. Kabanov and R. Sh. Liptser).
56. Necessary and sufficient conditions for absolute continuity of measures
corresponding to point (counting) processes. Proceedings of the Interna-

Publications of A.N. Shiryaev
XXVII
tional Symposium on Stochastic Differential Equations (Res. Inst. Math.
Sci., Kyoto Univ., Kyoto, 1976). New York–Chichester–Brisbane: Wiley,
1978, pp. 111–126 (with Yu. Kabanov and R. Liptser).
57. Absolute continuity and singularity of locally absolutely continuous prob-
ability distributions. I. (Russian) Mat. Sb. (N.S.) 107(149) (1978), no. 3,
364–415, 463; Engl. transl. in Math. USSR, Sb. 35 (1979), no. 5, 631–680
(with Yu. M. Kabanov and R. Sh. Liptser).
58. Un crit`ere pr´evisible pour l’uniforme integrabilit´e des semimartingales ex-
ponentielles. (French) S´eminaire de Probabilit´es, XIII (Univ. Strasbourg,
1977/78). Lecture Notes in Math., 721. Berlin: Springer-Verlag, 1979, pp.
147–161 (with J. Memin).
59. Absolute continuity and singularity of locally absolutely continuous prob-
ability distributions. II. (Russian) Mat. Sb. (N.S.) 108(150) (1979), no. 1,
32–61, 143; Engl. transl. in Math. USSR, Sb. 36 (1980), no. 1, 31–58 (with
Yu. M. Kabanov and R. Sh. Liptser).
60. On the sets of convergence of generalized submartingales. Stochastics 2
(1979), no. 3, 155–166 (with H. J. Engelbert).
61. On absolute continuity and singularity of probability measures. Mathemat-
ical statistics. Banach Center Publ., 6. Warsaw: Pa´nstwowe Wydawnictwo
Naukowe (PWN), 1980, pp. 121–132 (with H. J. Engelbert).
62. On absolute continuity of probability measures for Markov–Itˆo processes.
Stochastic differential systems. Proceedings of the IFIP-WG 7/1 Working
Conference (Vilnius, 1978). Lecture Notes Control Inform. Sci., 25. Berlin–
New York: Springer-Verlag, 1980, pp. 114–128 (with Yu. M. Kabanov and
R. Sh. Liptser).
63. Absolute continuity and singularity of probability measures in functional
spaces. Proceedings of the International Congress of Mathematicians (Hel-
sinki, 1978). Helsinki: Acad. Sci. Fennica, 1980, pp. 209–225.
64. On the representation of integer-valued random measures and local mar-
tingales by means of random measures with deterministic compensators.
(Russian) Mat. Sb. (N.S.) 111(153) (1980), no. 2, 293–307, 320; Engl.
transl. in Math. USSR, Sb. 39 (1981), 267–280 (with Yu. M. Kabanov and
R. Sh. Liptser).
65. Some limit theorems for simple point processes (a martingale approach).
Stochastics 3 (1980), no. 3, 203–216 (with Yu. M. Kabanov and R. Sh. Lip-
tser).
66. A functional central limit theorem for semimartingales. (Russian) Teor.
Veroyatnost. i Primenen. 25 (1980), no. 4, 683–703; Engl. transl. in Theory
Probab. Appl. 25 (1980), no. 4, 667–688 (with R. Sh. Liptser).
67. On necessary and sufficient conditions in the functional central limit the-
orem for semimartingales. (Russian) Teor. Veroyatnost. i Primenen. 26
(1981), no. 1, 132–137; Engl. transl. in Theory Probab. Appl. 26 (1981),
no. 1, 130–135 (with R. Sh. Liptser).
68. On weak convergence of semimartingales to stochastically continuous
processes with independent and conditionally independent increments.

XXVIII
Publications of A.N. Shiryaev
(Russian) Mat. Sb. (N.S.) 116(158) (1981), no. 3, 331–358, 463; Engl.
transl. in Math. USSR, Sb. 44 (1983), no. 3, 299–323 (with R. Sh. Liptser).
69. Martingales: Recent developments, results and applications. Internat. Sta-
tist. Rev. 49 (1981), no. 3, 199-233.
70. Rate of convergence in the central limit theorem for semimartingales.
(Russian) Teor. Veroyatnost. i Primenen. 27 (1982), no. 1, 3–14; Engl.
transl. in Theory Probab. Appl. 27 (1982), no. 1, 1–13 (with R. Sh. Liptser).
71. On a problem of necessary and sufficient conditions in the functional
central limit theorem for local martingales. Z. Wahrscheinlichkeitstheor.
verw. Geb. 59 (1982), no. 3, 311–318 (with R. Sh. Liptser).
72. Necessary and sufficient conditions for contiguity and entire asymptotic
separation of probability measures. (Russian) Uspekhi Mat. Nauk 37
(1982), no. 6(228), 97–124; Engl. transl. in Russian Math. Surveys 37
(1982), no. 6, 107–136 (with R. Sh. Liptser and F. Pukelsheim).
73. On the invariance principle for semi-martingales: the “nonclassical” case.
(Russian) Teor. Veroyatnost. i Primenen. 28 (1983), no. 1, 3–31; Engl.
transl. in Theory Probab. Appl. 28 (1984), no. 1, 1–34 (with R. Sh. Liptser).
74. Weak and strong convergence of the distributions of counting processes.
(Russian) Teor. Veroyatnost. i Primenen. 28 (1983), no. 2, 288–319; Engl.
transl. in Theory Probab. Appl. 28 (1984), no. 2, 303–336 (with Yu. M. Ka-
banov and R. Sh. Liptser).
75. Weak convergence of a sequence of semimartingales to a process of diffu-
sion type. (Russian) Mat. Sb. (N.S.) 121(163) (1983), no. 2, 176–200; Engl.
transl. in Math. USSR, Sb. 49 (1984), no. 1, 171–195 (with R. Sh. Liptser).
76. On the problem of “predictable” criteria of contiguity. Probability Theory
and Mathematical Statistics (Tbilisi, 1982). Lecture Notes in Math., 1021.
Berlin: Springer-Verlag, 1983, pp. 386–418 (with R. Sh. Liptser).
77. Estimates of closeness in variation of probability measures. (Russian)
Dokl. Akad. Nauk SSSR 278 (1984), no. 2, 265–268; Engl. transl. in So-
viet Math., Dokl. 30 (1984), no. 2, 351–354 (with Yu. M. Kabanov and
R. Sh. Liptser)
78. Distance de Hellinger–Kakutani des lois correspondant `a deux processus
`a accroissements ind´ependants. Z. Wahrscheinlichkeitstheor. verw. Geb.
70 (1985), no. 1, 67–89 (with J. Memin).
79. On contiguity of probability measures corresponding to semimartingales.
Anal. Math. 11 (1985), no. 2, 93–124 (with R. Sh. Liptser).
80. On the variation distance for probability measures defined on a fil-
tered space. Probab. Theory Relat. Fields 71 (1986), no. 1, 19–35 (with
Yu. M. Kabanov and R. Sh. Liptser).
81. A simple proof of “predictable” criteria for absolute continuity of proba-
bility measures. Recent Advances in Communication and Control Theory.
Volume honoring A. V. Balakrishnan on his 60th birthday. Part I: Com-
munication Systems. Ed. by R. E. Kalman et al. New York: Optimization
Software, 1987, pp. 166–176.

Publications of A.N. Shiryaev
XXIX
82. The First World Congress of the Bernoulli Society. (Russian) Uspekhi Mat.
Nauk 42 (1987), no. 6, 203–205.
83. Probabilistic-statistical methods of detecting spontaneously occurring ef-
fects. Trudy Mat. Inst. Steklova 182 (1988), 4–23; Engl. transl. in Proc.
Steklov Inst. Math. 182 (1990), no. 1, 1–21 (with A. N. Kolmogorov and
Yu. V. Prokhorov).
84. The scientific legacy of A. N. Kolmogorov. (Russian) Uspekhi Mat. Nauk
43 (1988), no. 6(264), 209–210; Engl. transl. in Russian Math. Surveys 43
(1988), no. 6, 211–212.
85. Some words in memory of Professor G. Maruyama. Probability Theory
and Mathematical Statistics (Kyoto, 1986). Lecture Notes in Math., 1299.
Berlin: Springer-Verlag, 1988, pp. 7–10.
86. Uniform weak convergence of semimartingales with applications to the
estimation of a parameter in an autoregression model of the first order.
(Russian) Statistics and Control of Stochastic Processes (Preila, 1987).
Moscow:“Nauka”, 1989, pp. 40–48 (with P. E. Greenwood).
87. Fundamental principles of martingale methods in functional limit theo-
rems. (Russian) Probability Theory and Mathematical Statistics. Trudy
Tbiliss. Mat. Inst. Razmadze Akad. Nauk Gruzin. SSR 92 (1989), 28–45.
88. Stochastic calculus on filtered probability spaces. (Russian) Itogi Nauki i
Tekh. Ser. Sovr. Probl. Mat. Fundam. Napravl. Vol. 45: Stochastic Cal-
culus. Moscow: VINITI, 1989, pp. 114–158; Engl. transl. in Probability
Theory III. Encycl. Math. Sci. 45, 1998 (with R. Sh. Liptser).
89. Martingales and limit theorems for random processes. (Russian) Itogi
Nauki i Tekh. Ser. Sovr. Probl. Mat. Fundam. Napravl. Vol. 45: Stochastic
Calculus. Moscow: VINITI, 1989, pp. 159–253; Engl. transl. in Probability
Theory III. Encycl. Math. Sci. 45, 1998 (with R. Sh. Liptser).
90. Kolmogorov: life and creative activities. Ann. Probab. 17 (1989), no. 3,
866–944.
91. On the fiftieth anniversary of the founding of the Department of Probabil-
ity Theory of the Faculty of Mechanics and Mathematics at Moscow State
University by A. N. Kolmogorov. (Russian) Teor. Veroyatnost. i Prime-
nen. 34 (1989), no. 1, 190–191; Engl. transl. in Theory Probab. Appl. 34
(1990), no. 1, 164–165 (with Ya. G. Sinai).
92. Andrei Nikolaevich Kolmogorov (April 25, 1903 – October 20, 1987): In
memoriam. (Russian) Teor. Veroyatnost. i Primenen. 34 (1989), no. 1,
5–118; Engl. transl. in Theory Probab. Appl. 34 (1990), no. 1, 1–99.
93. Large deviation for martingales with independent and homogeneous in-
crements. Probability Theory and Mathematical Statistics. Proceedings of
the fifth Vilnius conference (Vilnius, 1989). Vol. II, pp. 124–133. Vilnius:
“Mokslas”; Utrecht: VSP, 1990 (with R. Sh. Liptser).
94. Everything about Kolmogorov was unusual. . . CWI Quarterly 4 (1991),
no. 3, 189–193; Statist. Sci. 6 (1991), no. 3, 313–318.
95. Development of the ideas and methods of Chebyshev in limit theorems
of probability theory. (Russian) Vestnik Moskov. Univ. Ser. I Mat. Mekh.

XXX
Publications of A.N. Shiryaev
1991, no. 5, 24–36, 96; Engl. transl. in Moscow Univ. Math. Bull. 46 (1991),
no. 5, 20–29.
96. Asymptotic minimaxity of a sequential estimator for a first order autore-
gressive model. Stochastics Stochastics Rep. 38 (1992), no. 1, 49–65 (with
P. E. Greenwood).
97. On reparametrization and asymptotically optimal minimax estimation in
a generalized autoregressive model. Ann. Acad. Sci. Fenn. Ser. A I Math.
17 (1992), no. 1, 111–116 (with S. M. Pergamenshchikov).
98. Sequential estimation of the parameter of a stochastic difference equation
with random coefficients. (Russian) Teor. Veroyatnost. i Primenen. 37
(1992), no. 3, 482–501; Engl. transl. in Theory Probab. Appl. 37 (1993),
no. 3, 449–470 (with S. M. Pergamenshchikov).
99. In celebration of the 80th birthday of Boris Vladimirovich Gnedenko (An
interview). (Russian) Teor. Veroyatnost. i Primenen. 37 (1992), no. 4,
724–746; Engl. transl. in Theory Probab. Appl. 37 (1993), no. 4, 674–691.
100. On the concept of λ-convergence of statistical experiments. (Russian) Sta-
tistics and Control of Stochastic Processes, Trudy Mat. Inst. Steklova. 202
(1993), 282–286; Engl. transl. in Proc. Steklov Inst. Math. no. 4 (1994),
225–228 (with V. G. Spokoiny).
101. Optimal stopping rules and maximal inequalities for Bessel processes.
(Russian) Teor. Veroyatnost. i Primenen. 38 (1993), no. 2, 288–330; Engl.
transl. in Theory Probab. Appl. 38 (1994), no. 2, 226–261 (with L. E. Du-
bins and L. A. Shepp).
102. The Russian option: reduced regret. Ann. Appl. Probab. 3 (1993), no. 3,
631–640 (with L. A. Shepp).
103. Andrei Nikolaevich Kolmogorov (April 25, 1903 – October 20, 1987). A
biographical sketch of his life and creative path. (Russian) Reminiscences
about Kolmogorov (Russian). Moscow: “Nauka”, Fizmatlit, 1993, pp. 9–
143.
104. Asymptotic properties of the maximum likelihood estimators under ran-
dom normalization for a first order autoregressive model. Frontiers in
Pure and Applied Probability, 1: Proceedings of the Third Finnish–Soviet
symposium on probability theory and mathematical statistics (Turku,
1991). Ed. by H. Niemi et al. Utrecht: VSP, 1993, pp. 223–227 (with
V. G. Spokoiny).
105. On some concepts and stochastic models in financial mathematics.
(Russian) Teor. Veroyatnost. i Primenen. 39 (1994), no. 1, 5–22; Engl.
transl. in Theory Probab. Appl. 39 (1994), no. 1, 1–13.
106. Toward the theory of pricing of options of both European and Ameri-
can types. I. Discrete time. (Russian) Teor. Veroyatnost. i Primenen. 39
(1994), no. 1, 23–79; Engl. transl. in Theory Probab. Appl. 39 (1994), no. 1,
14–60 (with Yu. M. Kabanov, D. O. Kramkov, A. V. Mel’nikov).
107. Toward the theory of pricing of options of both European and Amer-
ican types. II. Continuous time. (Russian) Teor. Veroyatnost. i Prime-
nen. 39 (1994), no. 1, 80–129; Engl. transl. in Theory Probab. Appl. 39

Publications of A.N. Shiryaev
XXXI
(1994), no. 1, 61–102 (1995) (with Yu. M. Kabanov, D. O. Kramkov,
A. V. Mel’nikov).
108. A new look at the pricing of the “Russian option”. (Russian) Teor. Veroy-
atnost. i Primenen. 39 (1994), no. 1, 130–149; Engl. transl. in Theory
Probab. Appl. 39 (1994), no. 1, 103–119 (with L. A. Shepp).
109. On the rational pricing of the “Russian option” for the symmetrical bino-
mial model of a (B, S)-market. (Russian) Teor. Veroyatnost. i Primenen.
39 (1994), no. 1, 191–200; Engl. transl. in Theory Probab. Appl. 39 (1994),
no. 1, 153–162 (with D. O. Kramkov).
110. Actuarial and financial business: The current state of the art and per-
spectives of development. (Report on the constituent conference of the
Russian Society of Actuaries, Moscow, 1994.) Obozr. Prikl. Prom. Mat.
(“TVP”, Moscow) 1 (1994), no. 5, 684–697.
111. Stochastic problems of mathematical finance. (Russian) Obozr. prikl.
prom. mat. (“TVP”, Moscow) 1 (1994), no. 5, 780–820.
112. Quadratic covariation and an extension of Itˆo’s formula. Bernoulli 1
(1995), no. 1–2, 149–169 (with H. F¨ollmer and Ph. Protter).
113. Probabilistic and statistical models of evolution of financial indices.
(Russian) Obozr. prikl. prom. mat. (“TVP”, Moscow,) 2 (1995), no. 4,
527–555.
114. Optimization of the flow of dividends. (Russian) Uspekhi Mat. Nauk 50
(1995), no. 2(302), 25–46; Engl. transl. in Russian Math. Surveys 50
(1995), no. 2, 257–277 (with M. Jeanblanc-Picqu´e).
115. The Khintchine inequalities and martingale expanding of sphere of
their action. (Russian) Uspekhi Mat. Nauk 50 (1995), no. 5(305), 3–62;
Engl. transl. in Russian Math. Surveys 50 (1995), no. 5, 849–904 (with
G. Peskir).
116. Minimax optimality of the method of cumulative sums (cusum) in the case
of continuous time. (Russian) Uspekhi Mat. Nauk 51 (1996), no. 4(310),
173–174; Engl. transl. in Russian Math. Surveys 51 (1996), no. 4, 750–751.
117. Hiring and firing optimally in a large corporation. J. Econ. Dynamics
Control 20 (1996), no. 9/10, 1523–1539 (with L. A. Shepp).
118. No-arbitrage, change of measure and conditional Esscher transforms. CWI
Quarterly 9 (1996), no. 4, 291–317 (with H. B¨uhlmann, F. Delbaen, P. Em-
brechts).
119. Criteria for the absence of arbitrage in the financial market. Frontiers
in Pure and Applied Probability. II. Vol. 8: Proceedings of the Fourth
Russian–Finnish Symposium on Probability Theory and Mathematical
Statistics (Moscow, October 3–8, 1993). Ed. by A. N. Shiryaev et al.
Moscow: TVP, 1996, pp. 121–134 (with A. V. Mel’nikov).
120. A dual Russian option for selling short. Probability Theory and Mathemat-
ical Statistics (Lecture presented at the semester held in St. Peterburg,
March 2 – April 23, 1993). Ed. by I. A. Ibragimov et al. Amsterdam:
Gordon & Breach, 1996, pp. 109–218 (with L. A. Shepp).

XXXII
Publications of A.N. Shiryaev
121. Probability theory and B. V. Gnedenko. (Russian) Fundam. Prikl. Mat.
2 (1996), no. 4, 955.
122. On the Brownian first-passage time over a one-sided stochastic boundary.
Teor. Veroyanostn. i Primenen. 42 (1997), no. 3, 591–602; Theory Probab.
Appl. 42 (1997), no. 3, 444–453 (with G. Peskir).
123. On sequential estimation of an autoregressive parameter. Stochastics Sto-
chastics Rep. 60 (1997), no. 3/4, 219–240 (with V. G. Spokoiny).
124. Sufficient conditions of the uniform integrability of exponential martin-
gales. European Congress of Mathematics (ECM ) (Budapest, 1996). Vol.
I. Ed. by A. Balog et al. Progr. Math., 168. Basel: Birkh¨auser, 1998, pp.
289–295 (with D. O. Kramkov).
125. Local martingales and the fundamental asset pricing theorems in the
discrete-time case. Finance Stoch. 2 (1998), no. 3, 259–273 (with J. Jacod).
126. Solution of the Bayesian sequential testing problem for a Poisson process.
MaPhySto Publ. no. 30. Aarhus: Aarhus Univ., Centre for Mathematical
Physics and Stochastics, 1998 (with G. Peskir).
127. On arbitrage and replication for fractal models. Research report no. 20.
Aarhus: Aarhus Univ., Centre for Mathematical Physics and Stochastics,
1998.
128. Mathematical theory of probability. Essay on the history of formation.
(Russian) Appendix to: A. N. Kolmogorov. Foundations of the Theory of
Probability. Moscow: “FAZIS”, 1998, pp. 101–129.
129. On Esscher transforms in discrete finance model. ASTIN Bull. 28 (1998),
no. 2, 171–186 (with H. B¨uhlmann, F. Delbaen, and P. Embrechts).
130. On probability characteristics of “downfalls” in a standard Brownian
motion. (Russian) Teor. Veroyatnost. i Primenen. 44 (1999), no. 1, 3–
13; Engl. thansl. in Theory Probab. Appl. 44 (1999), no. 1, 29–38 (with
R. Douady and M. Yor).
131. On the history of the foundation of the Russian Academy of Sciences
and about the first articles on probability theory in Russian publications.
(Russian) Teor. Veroyatn. i Primenen. 44 (1999), no. 2, 241–248; Engl.
thansl. in Theory Probab. Appl. 44 (1999), no. 2, 225–230.
132. Some distributional properties of a Brownian motion with a drift, and an
extension of P. L´evy’s theorem. (Russian) Teor. Veroyatnost. i Primenen.
44 (1999), no. 2, 466–472; Engl. thansl. in Theory Probab. Appl. 44 (1999),
no. 2, 412–418 (with A. S. Cherny).
133. Kolmogorov and the Turbulence. MaPhySto Preprint no. 12 (Miscellanea).
Aarhus: Aarhus Univ., Centre for Mathematical Physics and Stochastics,
1999. 24 pp.
134. An extension of P. L´evy’s distributional properties to the case of a Brown-
ian motion with drift. Bernoulli 6 (2000), no. 4, 615–620 (with S. E. Gra-
versen).
135. Stopping Brownian motion without anticipation as close as possible to its
ultimate maximum. Teor. Veroyatnost. i Primenen. 45 (2000), no. 1, 125–

Publications of A.N. Shiryaev
XXXIII
136; Theory Probab. Appl. 45 (2001), no. 1, 41–50 (with S. E. Graversen
and G. Peskir).
136. Sequential testing problems for Poisson processes. Ann. Statist. 28 (2000),
no. 3, 837–859 (with G. Peskir).
137. Maximal inequalities for reflected Brownian motion with drift. Teor.
Imovir. Mat. Statist. no. 63 (2000), 125–131; Engl. transl. in Theory
Probab. Math. Statist. no. 63 (2001), 137–143 (with G. Peskir).
138. Andrei Nikolaevich Kolmogorov (April 25, 1903 – October 20, 1987). A bi-
ographical sketch of life and creative activities. Kolmogorov in Perspective.
Providence, RI: Amer. Math. Soc.; London: London Math. Soc., 2000, pp.
1–87.
139. The Russian option under conditions of a possible price “freeze”. (Russian)
Uspekhi Mat. Nauk 56 (2001), no. 1, 187–188; Engl. transl. in Russian
Math. Surveys 56 (2001), no. 1, 179–181 (with L. A. Shepp).
140. A note on the call-put parity and call-put duality. Teor. Veroyatnost. i
Primenen. 46 (2001), no. 1, 181–183; Theory Probab. Appl. 46 (2001),
no. 1, 167–170 (with G. Peskir).
141. Time change representation of stochastic integrals. Teor. Veroyatnost. i
Primenen. 46 (2001), no. 3, 579–585; Theory Probab. Appl. 46 (2001),
no. 3, 522–528 (with J. Kallsen).
142. Essentials of the arbitrage theory. Lectures in the Institute for Pure and
Applied Mathematics, UCLA, Los Angeles, 3–5 January 2001, 30 pp.
143. On criteria for the uniform integrability of Brownian stochastic exponen-
tials. Optimal Control and Partial Differential Equations. In honour of
Prof. Bensoussan’s 60th birthday. Ed. by J. L. Menaldi, E. Rofman, and
A. Sulem. Amsterdam: IOS Press, 2001, pp. 80–92 (with A. S. Cherny).
144. Quickest detection problems in the technical analysis of the financial data.
Mathematical finance — Bachelier congress 2000: Selected papers from
the First World Wongress of the Bachelier Finance Society (Paris, 2000).
Ed. by H. Geman et al. Berlin: Springer-Verlag, Springer Finance, 2002,
pp. 487–521.
145. A vector stochastic integrals and the fundamental theorems of asset pric-
ing. (Russian) Trudy Mat. Inst. Steklova 237 (2002), 12–56; Engl. transl.
in Proc. Steklov Inst. Math. 237 (2002), 6–49 (with A. S. Cherny).
146. On lower and upper functions for square integrable martingales. Trudy
Mat. Inst. Steklova 237 (2002), 290–301; Proc. Steklov Inst. Math. 237
(2002), 281–292 (with E. Valkeila and L. Vostrikova).
147. Limit behavior of the “horizontal-vertical” random walk and some exten-
sions of the Donsker–Prokhorov invariance principle. Teor. Veroyatnost.
i Primenen. 47 (2002), no. 3, 498–517; Theory Probab. Appl. 47 (2002),
no. 3, 377–394 (with A. S. Cherny and M. Yor).
148. The cumulant process and Esscher’s change of measure. Finance Stoch. 6
(2002), no. 4, 397–428 (with J. Kallsen).

XXXIV
Publications of A.N. Shiryaev
149. Solving the Poisson disorder problem. Advances in Finance and Stochas-
tics. Essays in honour of Dieter Sonderman. Ed. by K. Sandmann et al.
Berlin: Springer-Verlag, 2002, pp. 295–312 (with G. Peskir).
150. A barrier version of the Russian option. Advances in Finance and Sto-
chastics. Essays in honour of Dieter Sondermann. Ed. by K. Sandmann
et al. Berlin: Springer-Verlag, 2002, pp. 271–284 (with L. A. Shepp and
A. Sulem).
151. Change of time and measure for L´evy processes. Lecture Notes no. 13.
Aarhus: Aarhus Univ., Centre for Mathematical Physics and Stochastics,
2002. 46 pp. (with A. S. Cherny).
152. From “disorder” to nonlinear filtration and theory of martingales.
(Russian) Mathematical Events of XX century. Moscow: “FAZIS”, 2003,
pp. 491–518 .
153. Department of Probability Theory. Mathematics in Moscow University on
the Eve of the XXI century. Part III. Ed. by O. B. Lupanov and A. K.
Rybnikov. Moscow: Moscow State University, Centre of Applied Studies,
2003, pp. 3–92.
154. On the defense work of A. N. Kolmogorov during World War II. Mathe-
matics and War (Karlskrona, 2002). Basel: Birkh¨auser, 2003, pp. 103–107.
155. On stochastic integral representations of functionals of Brownian motion.
I. (Russian) Teor. Veroyatnost. i Primenen. 48 (2003), no. 2, 375–385;
Engl. transl. in Theory Probab. Appl. 48 (2003), no. 2 (with M. Yor).
156. A life in search of the truth (on the centenary of the birth of Andrei
Nikolaevich Kolmogorov). (Russian) Priroda no. 4 (2003), 36–53.
157. V poiskakh istiny \[In search of the truth]. (Russian) Introductory text to:
Kolmogorov. \[Dedicated to the 100th birthday of A. N. Kolmogorov.] \[18]
Vol. I: Biobibliography. Moscow: Fizmatlit, 2003, pp. 9–16.
158. Zhisn’ i tvorchestvo A. N. Kolmogorova \[Life and creative work of
A. N. Kolmogorov]. (Russian) Kolmogorov. \[Dedicated to the 100th birth-
day of A. N. Kolmogorov.] \[18] Vol. I: Biobibliography. Moscow: Fizmatlit,
2003, pp. 17–209.
159. Soglasnoe bienie serdets \[Unison beating of hearts]. (Russian) Introduc-
tory text to: Kolmogorov. \[Dedicated to the 100th birthday of A. N. Kol-
mogorov.] \[18] Vol. II: Selected correspondence of A. N. Kolmogorov and
P. S. Aleksandrov. Moscow: Fizmatlit, 2003, pp. 9–15.
160. Mezhdu trivial’nym i nedostupnym \[Between trivial and inaccessible].
(Russian) Introductory text to: Kolmogorov. \[Dedicated to the 100th
birthday of A. N. Kolmogorov.] \[18] Vol. III: From the diary notes of
A. N. Kolmogorov. Moscow: Fizmatlit, 2003, pp. 9–13.
161. On an effective case of solving the optimal stopping problem for random
walks. Teor. Veroyatnost. i Primenen. 49 (2004), no. 2, 373–382; Engl.
transl. in Theory Probab. Appl. 49 (2004), no. 2 (with A. A. Novikov).
162. A remark on the quickest detection problems. Statist. Decisions 22 (2004),
no. 1, 79–82.

Publications of A.N. Shiryaev
XXXV
III. Works as translator and editor of translation
1. M. G. Kendall, A. Stuart. Distribution Theory. (Russian) Translated from
the English by V. V. Sazonov and A. N. Shiryaev. Ed. by A. N. Kol-
mogorov. Moscow: “Nauka”, 1966. 587 pp.
2. A. T. Bharucha-Reid. Elements of the Theory of Markov Processes and
their Applications. Russian transl. under the title Elementy teorii markov-
skikh protsessov i ikh prilozhenia edited by A. N. Shiryaev. Moscow:
“Nauka”, 1969. 512 pp.
3. J. W. Lamperti. Probability. Russian transl. under the title Veroyatnost’
edited by A. N. Shiryaev. Moscow: “Nauka”, 1973. 184 pp.
4. P.-A. Meyer. Probability and potentials. Russian transl. under the title
Veroyatnost’ i potentsialy edited by A. N. Shiryaev. Moscow: “Mir”, 1973.
328 pp.
5. J.-R. Barra. Fundamental Concepts of Mathematical Statistics. Russian
transl. under the title Osnovnye poniatiya matematicheskoj statistiki
edited by A. N. Shiryaev. Moscow: “Mir”, 1974. 275 pp.
6. H. Robbins, D. Siegmund, Y. S. Chow. Great Expectations: The Theory
of Optimal Stopping. Russian transl. under the title Teoriya optimal’nykh
pravil ostanovki edited by A. N. Shiryaev. Moscow: “Nauka”, 1977. 167 pp.
7. W. H. Fleming, R. W. Rishel. Deterministic and Stochastic Optimal
Control. Russian transl. under the title Optimal’noe upravlenie deter-
minirovannymi i stokhasticheskimi sistemami edited by A. N. Shiryaev.
Moscow: “Mir”, 1978. 316 pp.
8. M. H. A. Davis. Linear Estimation and Stochastic Control. Russian transl.
under the title Linejnoe otsenivanie i stokhasticheskoe upravlenie edited
and with a preface by A. N. Shiryaev. Moscow: “Nauka”, 1984. 208 pp.
9. R. J. Elliott. Stochastic Calculus and Applications. Russian transl. un-
der the title Stokhasticheskij analiz i ego prilozheniya edited and with a
preface by A. N. Shiryaev. Moscow: “Mir”, 1986. 352 pp.
10. E. J. G. Pitman. Some Basic Theory for Statistical Inference. Russian
transl. under the title Osnovy teorii statisticheskikh vyvodov edited and
with a preface by A. N. Shiryaev. Moscow: “Mir”, 1986. 106 pp.
11. N. Ikeda, S. Watanabe. Stochastic Differential Equations and Diffusion
Processes. Russian transl. under the title Stokhasticheskie differentsial’nye
uravneniya i diffuzionnye protsessy edited by A. N. Shiryaev. Moscow:
“Nauka”, 1986. 448 pp.
12. Probability Theory III. Stochastic Calculus. Encyclopaedia of Mathemati-
cal Sciences, 45. Translation from the Russian edited by Yu. V. Prokhorov
and A. N. Shiryaev. Berlin: Springer-Verlag, 1998. iv+253 pp.
IV. Works as editor
1. Proceedings of the School and Seminar on the Theory of Random Processes
(Druskininkai, 1974), Part II. (Russian) Ed. by B. I. Grigelionis and

XXXVI
Publications of A.N. Shiryaev
A. N. Shiryaev. Vilnius: Inst. Fiz. i Mat. Akad. Nauk Litovsk. SSR, 1975.
354 pp.
2. Stochastic Optimization. Proceedings of the international conference
(Kiev, 1984). Ed. by V. I. Arkin, A. N. Shiryaev, and R. Wets. Lecture
Notes Control Inform. Sci., 81. Berlin: Springer-Verlag, 1986. x+754 pp.
3. A. N. Kolmogorov. Probability Theory and Mathematical Statistics. Se-
lected works. (Russian) Compiled and edited by A. N. Shiryaev. Moscow:
“Nauka”, 1986. 535 pp.
4. A. N. Kolmogorov. Information Theory and the Theory of Algorithms. Se-
lected works. (Russian) Compiled and edited by A. N. Shiryaev. Moscow:
“Nauka”, 1987. 304 pp.
5. Statistics and Control of Stochastic Processes (Steklov Institute seminar,
1985-86). Ed. by N. V. Krylov, A. A. Novikov, Yu. M. Kabanov, and
A. N. Shiryaev. New York: Optimization Software, 1989. 270 pp.
6. Statistics and Control of Random Processes. Papers from the Fourth
School-Seminar on the Theory of Random Processes held in Preila, Sep-
tember 28 – October 3, 1987. (Russian) Edited by A. N. Shiryaev. Moscow:
“Nauka”, 1989. 233 pp.
7. Probability Theory and Mathematical Statistics. Dedicated to the 70th
birthday of G. M. Maniya. (Russian) Edited by Yu. V. Prokhorov,
A. N. Shiryaev, and T. L. Shervashidze. Trudy Tbiliss. Mat. Inst. Raz-
madze Akad. Nauk Gruzin. SSR, 92. Tbilisi: “Metsniereba”, 1989. 247 pp.
8. Probability Theory and Mathematical Statistics. Proceedings of the Sixth
USSR-Japan Symposium held in Kiev, August 5–10, 1991. Ed. by
A. N. Shiryaev, V. S. Korolyuk, S. Watanabe, and M. Fukushima. River
Edge, NJ: World Scientific, 1992. xii+443 pp.
9. A. N. Kolmogorov. Selected works. Vol. II. Probability Theory and Mathe-
matical Statistics. (Engl. transl. of \[3].) Edited by A. N. Shiryayev. Math.
Appl. (Soviet Ser.), 26. Dordrecht: Kluwer Acad. Publ., 1992. xvi+597 pp.
10. Selected Works of A. N. Kolmogorov. Vol. III. Information Theory and
the Theory of Algorithms. (Engl. transl. of \[4].) Ed. by A. N. Shiryayev.
Math. Appl. (Soviet Ser.), 27. Dordrecht: Kluwer Acad. Publ., 1993.
xxvi+275 pp.
11. Kolmogorov v vospominaniyakh \[Kolmogorov in Reminiscences]. (Russian)
Compiled and edited by A. N. Shiryaev. Moscow: Fizmatlit, “Nauka”,
1993. 736 pp.
12. Frontiers in Pure and Applied Probability, 1. Proceedings of the Third
Finnish-Soviet Symposium on Probability Theory and Mathematical Sta-
tistics (Turku, 1991). Ed. by H. Niemi, G. H¨ognas, A. V. Mel’nikov, and
A. N. Shiryaev. Utrecht: VSP; Moscow: TVP, 1993. viii+296 pp.
13. Statistics and Control of Stochastic Processes. Proc. Steklov Inst. Math.,
202. Ed. by A. A. Novikov and A. N. Shiryaev. Providence, RI: Amer.
Math. Soc., 1994. ix+242 pp.
14. Probability Theory and Mathematical Statistics. Proceedings of the Sev-
enth Japan–Russia symposium, Tokyo, Japan, July 26–30, 1995. Ed. by

Publications of A.N. Shiryaev
XXXVII
S. Watanabe, M. Fukushima, Yu. V. Prohorov, and A. N. Shiryaev. Sin-
gapore: World Scientific, 1996. x+515 p.
15. Frontiers in Pure and Applied Probability, 8. Proceedings of the Fourth
Finnish-Soviet Symposium on Probability Theory and Mathematical Sta-
tistics (Moscow, 1993). Ed. by A. V. Mel’nikov, H. Niemi, A. N. Shiryaev,
and E. Valkeila). Moscow: TVP, 1996. 223 pp.
16. Research papers dedicated to the memory of B. V. Gnedenko (1.1.1912–
27.12.1995). (Russian) Ed. by A. N. Shiryaev. Fundam. prikl. mat. 2
(1996), no. 4. 313 pp.
17. Statistics and Control of Stochastic Processes. The Liptser Festschrift.
Papers from the Steklov seminar held in Moscow, Russia, 1995–1996. Ed.
by Yu. M. Kabanov, B. L. Rozovskii, and A. N. Shiryaev. Singapore:
World Scientific, 1997. xxii+354 pp.
18. Kolmogorov. \[Dedicated to the 100th birthday of A. N. Kolmogorov.] Vol.
I: Biobibliography. Vol. II: Selected correspondence of A. N. Kolmogorov
and P. S. Aleksandrov. Vol. III: From the diary notes of A. N. Kolmogorov.
Ed. by A. N. Shiryaev. Moscow: Fizmatlit, 2003, 384 pp., 672 pp., 230 pp.
V. In print
1. A. N. Shiryaev. Problems in Theory of Probability. \[Textbook.] Moscow:
MCCME, 2005 (forthcoming).
2. Kolmogorov in Reminiscences of his Pupils. Edited and with a preface by
A. N. Shiryaev. Moscow: MCCME, 2005 (forthcoming).
3. A. N. Shiryaev. Whether the Great can be seen from a far away. In-
troductory text to: Kolmogorov in Reminiscences of his Pupils. Moscow:
MCCME, 2005 (forthcoming).
4. On stochastic integral representations of functionals of Brownian motion.
II. (Russian) Teor. Veroyatnost. i Primenen., 2005, forthcoming (with
M. Yor).


On Numerical Approximation of Stochastic
Burgers’ Equation
Aureli ALABERT1 and Istv´an GY¨ONGY2
1 Departament de Matem`atiques, Universitat Aut`onoma de Barcelona,
08193 Bellaterra, Catalonia, Spain.
alabert@manwe.mat.uab.es
2 School of Mathematics, University of Edinburgh, King’s Buildings,
Edinburgh, EH9 3JZ, U.K.
gyongy@maths.ed.ac.uk
Summary. We present a finite difference scheme for stochastic Burgers’ equation
driven by space-time white noise. We estimate the rate of convergence of the the
numerical scheme to the solution of stochastic Burgers’s equation.
Key words: SPDE, Burgers’ equation
Mathematics Subject Classification (2000): 60H15, 65M10, 65M15,
93E11
1 Introduction
We consider stochastic Burgers’ equation
∂u
∂t (t, x) = ∂2u
∂x2 (t, x) + f(u(t, x)) + u(t, x)∂u
∂x(t, x) + ∂W
∂t∂x(t, x),
(1.1)
for t ∈\[0, T], x ∈\[0, 1], with Dirichlet boundary condition
u(t, 0) = u(t, 1) = 0,
t > 0,
(1.2)
and initial condition
u(0, x) = u0(x) ,
x ∈\[0, 1].
(1.3)
Here f is a Lipschitz continuous function on the real line, u0 is a square-
integrable function over \[0, 1], and
∂W
∂t∂x(t, x) is a space-time white noise. This

2
A. Albert and I. Gy¨ongy
equation is very often viewed as a model equation of the motion of turbulent
fluid. The solvability and the properties of its solution have been intensively
studied in the literature, see, e.g., \[1], \[2], \[7] and the references therein. Our
aim is to investigate a numerical scheme for this equation. We study the
following space-discretization of problem (1.1)–(1.2):
dun(t, xn
k) =

∆nun(t, xn
k) + f(u(t, xn
k)) + 1
2∂−
n \[\[un(t)]](xn
k)

dt
+d∂nW(t, xn
k) ,
k = 1, . . . , n −1,
(1.4)
un(t, xn
0) = un(t, xn
n) = 0,
t ≥0,
(1.5)
over the grid Gn := {xn
k = k/n : k = 0, 1, 2, ..., n}, where d stands for the
differential in t, and
∆nh(xn
k) := n2
h(xn
k+1) −2h(xn
k) + h(xn
k−1)

,
∂nh(xn
k) := n

h(xn
k+1) −h(xn
k)

,
∂−
n h(xn
k) :=

h(xn
k) −h(xn
k−1)

,
\[\[h]](xn
k) := 1
3

h2(xn
k+1) + h2(xn
k) + h(xn
k+1)h(xn
k)

,
h(xn
0) = h(xn
n) := 0,
for functions h defined on the grid. For fixed n ≥2 system (1.4) is a stochastic
differential equation for the (n −1)-dimensional process
un(t) = (un
k)(t) := (un(t, xn
k)).
We show that for every initial condition un(0) = (an
k) ∈Rn−1 equation (1.4)
has a unique solution {un(t) : t ∈\[0, T]}. We extend un(t) from the grid onto
\[0, 1] by un(t, x) := un(t, \[nx]/n), and show that this extension converges to u,
the solution of stochastic Burgers’ equation, provided that the initial condition
un(0) converges to u0. Moreover, we estimate the rate of convergence.
Numerical schemes for parabolic stochastic PDEs driven by space-time
white noise have been investigated thoroughly in the literature, see, e.g.,
\[3], \[6], \[10], \[11] and the references therein. The class of equations consid-
ered in these papers does not contain stochastic Burgers’ equation. A semi-
discretization in time of stochastic Burgers’ equation is studied in \[9].
2 Formulation of the main result
Let (Ω, F, {Ft}0≤t≤T , P) be a filtered probability space carrying an Ft-
Brownian sheet W = (W(t, x)) on \[0, T] × \[0, 1]. This means W is a Gaussian

Approximation of Burgers’ Equation
3
field, EW(t, x) = 0, E(W(t, x)W(s, y)) = (t ∧s)(x ∧y), W(t, x) is Ft-
measurable, and W(t, x) −W(s, x) + W(s, y) −W(t, y) is independent of Fs
for all 0 ≤s ≤t and x, y ∈\[0, 1].
Let f := f(z) be a locally bounded Borel function on R, and let u0 = u0(x)
be an F0-measurable random field such that almost surely u0 ∈L2(\[0, 1]).
We say that an L2(\[0, 1])-valued continuous Ft-adapted random process is a
solution of problem (1.1), (1.2), (1.3), if almost surely
 1
0
u(t, x)ϕ(x) dx =
 1
0
u0(x)ϕ(x) dx +
 t
0
 1
0
u(s, x)ϕ′′(x) dx ds
+
 t
0
 1
0
f(u(s, x))ϕ(x) dx ds −1
2
 t
0
 1
0
u2(s, x)ϕ′(x) dx ds
+
 t
0
 1
0
ϕ(x) dW(s, x)
for all t ∈\[0, T] and ϕ ∈C2(\[0, 1]), ϕ(0) = ϕ(1) = 0, where the last integral
in the right-hand side of this equality is understood as Itˆo’s integral, and
ϕ′, ϕ′′ denote the first and second derivatives of ϕ. We assume the following
condition.
Assumption 2.1 The force term f is Lipschitz continuous, i.e., there is a
constant L such that
|f(y) −f(z)| ≤L|y −z|
for all y, z ∈R.
It is well-known that under this condition problem (1.1), (1.2), (1.3) has a
unique solution u, which satisfies also the integral equation
u(t, x) =
 1
0
G(t, x, y)u0(y) dy +
 t
0
 1
0
G(t −s, x, y)f(u(s, y)) dy ds
−
 t
0
 1
0
Gy(t −s, x, y)u2(s, y) dy ds +
 t
0
 1
0
G(t −s, x, y) dW(s, y), (2.6)
where
G(t, x, y) :=
∞

j=1
exp{−j2π2t}ϕj(x)ϕj(y),
ϕj(x) :=
√
2 sin(jπx),
(2.7)
is the heat kernel, and
Gy(t, x, y) =
∞

j=1
jπ exp{−j2π2t}ϕj(x)ψj(y),
ψj(x) :=
√
2 cos(jπx).
(2.8)
Moreover, if u0 is a continuous random field, then the solution u has a modi-
fication which is continuous in (t, x), see \[1], \[2] and \[7].
First we formulate our result for problem (1.4)–(1.5).

4
A. Albert and I. Gy¨ongy
Theorem 2.1. Let Assumption 2.1 hold. Let n ≥2 be an integer, and let
(an
k)n−1
k=1 be an F0-measurable random vector in Rd−1. Then system (1.4)–
(1.5) with the initial condition
un(0, xn
k) = an
k,
k = 1, 2, ..., n −1,
(2.9)
admits a unique solution un = {un(t, xn
k) : k = 0, 1, 2, ..., n; t ≥0}, which
is continuous in t ≥0. Moreover, for every T > 0, there is a finite random
variable ξ such that
sup
t≤T
1
n
n−1

j=1
|un(t, xn
j )|2 ≤ξ

1
n
n−1

j=1
|an
k|2 + 1


(a.s.)
(2.10)
for all n ≥2.
In order to formulate the main result of the paper we extend (un(t, xn
k)),
the solution of system (1.4)–(1.5) with initial condition un(0, xn
k) = u0(xn
k),
k = 0, 1, 2..., n, as follows:
un(t, x) := un(t, κn(x)),
x ∈\[0, 1],
t ≥0,
where κn(x) := \[nx]/n, and \[z] denotes the integer part of z. The main result
of the present paper is the following.
Theorem 2.2. Let Assumption 2.1 hold. Assume that u0 ∈C(\[0, 1]) almost
surely. Then un(t) almost surely converges in L2(\[0, 1]) to u(t), the solution of
problem (1.1)–(1.3), uniformly in t in bounded intervals. Moreover, if almost
surely u0 ∈C3(\[0, 1]), then for each α < 1/2, T > 0 there exists a finite
random variable ζα such that
sup
t≤T
 1
0
|un(t, x) −u(t, x)|2 dx ≤ζαn−α
(a.s.)
(2.11)
for all integers n ≥2.
We prove Theorem 2.1 in the next section, and after presenting some
preliminary estimates in Section 4, we prove Theorem 2.2 in Section 5.
3 Proof of Theorem 2.1
Using the notation
un
k(t) := un(t, xn
k) = un
t, k
n

W n
k (t) := √n

W(t, xn
k+1) −W(t, xn
k)

for k = 1, 2, . . . , n −1, we can write equations (1.4)–(1.5) as

Approximation of Burgers’ Equation
5
dun
k(t) = n2
n−1

i=1
Dkiun
i (t) dt + f(un
k(t)) dt
+n
6

|un
k+1|2(t) −|un
k−1|2(t) + un
k+1(t)un
k(t) −un
k(t)un
k−1(t)

dt
+√n dW n
k (t),
k = 1, 2, . . . , n −1,
(3.12)
un
k(0) = an
k,
k = 1, 2, . . . , n −1,
(3.13)
where un
0 = un
n := 0, and Dkk = −2, Dki = 1 for |k −i| = 1, Dki = 0 for
|k −i| > 1. Notice that W n(t) := (W n
k (t)) is an (n −1)-dimensional Wiener
process. Fix n ≥2 and define the vector field
A(x) := n2Dx + F(x) + nH(x),
x ∈Rn−1,
where D = (Dij) is the (n −1) × (n −1) matrix given above, and
Fk(x1, x2, . . . , xn−1) : = f(xk),
Hk(x1, x2, . . . , xn−1) : = 1
6(x2
k+1 −x2
k−1 + xk+1xk −xkxk−1),
for k = 1, 2, . . . , n −1, with x0 = xn := 0. Then equations (3.12)–(3.13) can
be written as
dun(t) = A(un(t)) dt + √n dW n(t),
(3.14)
un(0) = an,
(3.15)
where un(t) := (un
k(t)) and an := (an
k) are column vectors in Rn−1. Notice
that
(x, Dx) = −x2
1 −x2
n−1 −
n−2

k=1
(xk+1 −xk)2,
(3.16)
(x, H(x)) = 0,
(3.17)
(x, F(x)) =
n−1

k=1
xkf(xk) ≤C
	
n +
n−1

k=1
x2
k

(3.18)
for all x ∈Rn−1, where (x, y) := n−1
k=1 xkzk is the inner product of vectors
x, y ∈Rn−1, C := L+f 2(0), and L is the Lipschitz constant from Assumption
2.1. Hence A satisfies the following growth condition:
(x, A(x)) = n2(x, Dx) + (x, F(x)) ≤C
	
n +
n−1

k=1
x2
k

for all x ∈Rn−1 and for every integer n ≥2. Clearly, A is locally Lipschitz in
x ∈Rn−1. This and the above growth condition imply that equation (3.14)

6
A. Albert and I. Gy¨ongy
with initial condition (3.15) admits a unique solution un, which is an Ft-
adapted Rn−1-valued continuous process. (See the general result, Theorem 1
in \[4], or Theorem 3.1 in \[8], for example.)
It remains to show estimate (2.10). To this end we rewrite equation (3.14)
for the solution un in the form
un(t) = en2tDan +
 t
0
en2(t−s)D
F(un(s)) + nH(un(s))

ds
+√n
 t
0
en2(t−s)D dW n(s),
(3.19)
and consider the Rn−1-valued random processes
ηn(t) := √n
 t
0
en2(t−s)D dW n(s),
v(t) := vn(t) := un(t) −ηn(t).
Then from equation (3.19) we get that v satisfies
dv(t) =

n2Dv(t) + F(v(t) + η(t)) + nH(v(t) + ηn(t))

dt,
v(0) = an.
Hence for |v(t)|2 := n−1
k=1 |vk(t)|2 we get
d|v(t)|2 = 2n2
v(t), Dv(t)

dt + 2

v(t), F(v(t) + ηn(t))

dt
+2n

v(t), H(v(t) + ηn(t))

dt
≤−2n2
n

k=1
(vk+1(t) −vk(t))2 dt + 4C(n + |v(t)|2)
+2n

v(t), H(v(t) + ηn(t)) −H(v(t))

dt
(3.20)
with v0(t) := vn(t) := 0, by virtue of (3.16), (3.17), (3.18), where C is the
constant from inequality (3.18). Taking into account that for x ∈Rn−1
Hk(x) = \[\[x]]k −\[\[x]]k−1,
k = 1, . . . , n −1
with
\[\[x]]j := 1
6(x2
j+1 + x2
j + xj+1xj),
j = 0, 1, . . . , n −1,
x0 := xn := 0,
we have
2|

v(t), H(v(t) + η(t)) −H(v(t))

| =
2|
n−1

k=0
(vk+1(t) −vk(t)){\[\[v(t) + ηn(t)]]k −\[\[v(t)]]k}|

Approximation of Burgers’ Equation
7
≤n
n−1

k=0
(vk+1(t) −vk(t))2 + n−1
n−1

k=0
{\[\[v(t) + ηn(t)]]k −\[\[v(t)]]k}2
≤n
n−1

k=0
(vk+1(t) −vk(t))2 + 100n−1
n−1

k=1

|¯ηn|2|vk|2(t) + |¯ηn|4
,
(3.21)
where
¯ηn := max
0<k<n sup
t≤T
|ηn
k (t)|.
Thus from (3.20) and (3.21) we get
1
n|v(t)|2 ≤1
n|v(0)|2 + 100|¯ηn|4 + 4Ct + (100|¯ηn|2 + 4C)
 t
0
1
n|v(s)|2 ds.
Hence by Gronwall’s inequality
sup
t≤T
1
n|v(t)|2 ≤e(100|¯ηn|2+4C)T
 1
n|v(0)|2 + 100|¯ηn|4 + 4CT

,
which implies
sup
t≤T
1
n
n−1

k=1
|un
k(t)|2 ≤ξn
	
1
n
n−1

k=1
|an
k|2 + 1

(3.22)
with
ξn := e(100|¯ηn|2+4C)T + 100|¯ηn|4 + 4CT + 2|¯ηn|2.
We are going to show that ξ := supn≥2 ξn is a finite random variable. To this
end note that the vectors e1, . . . , en−1 defined by
ej = (ej(k)) =

2
n sin

j k
nπ

,
k = 1, 2, . . . , n −1,
form an orthonormal basis in Rn−1, and that they are eigenvectors of the
matrix n2D, with eigenvalues
λn
j := −4 sin2  j
2nπ

n2 = −j2π2cn
j ,
where
4
π2 ≤cn
j := sin2 jπ
2n
  jπ
2n
2
≤1
(3.23)
for j = 1, 2, . . . , n −1 and every n ≥1. Therefore, for the random field
{ηn(t, x) : t ≥0, x ∈\[0, 1]} defined by
ηn(t, xk) := ηn
k := √n
 t
0
en2(t−s)D dW n(s)

8
A. Albert and I. Gy¨ongy
for xk := k/n, n = 1, 2, ..., n −1, and
ηn(t, 0) = ηn(t, 1) = 0,
ηn(t, x) := ηn(t, κn(x)),
x ∈(0, 1),
we have
ηn(t, x) =
 t
0
 1
0
Gn(t, x, y) dW(t, y),
for all t ≥0, x ∈\[0, 1], where
Gn(t, x, y) :=
n−1

j=1
exp(λn
j t)ϕn
j (κn(x))ϕj(κn(y)),
(3.24)
ϕj(x) :=
√
2 sin(jxπ).
(Recall that κn(y) := \[ny]/n.) Thus considering the special case f = 0, σ = 1,
u0 in Theorem 3.1 of \[5], we get that almost surely
sup
n≥2
¯ηn ≤sup
x∈\[0,1]
sup
t≤T
|ηn(t, x)| < ∞,
which obviously implies that ξ := supn≥2 ξn is a finite random variable. The
proof of Theorem 2.2 is now complete.
⊓⊔
4 Preliminary estimates
Define
Gn
y(t, x, y) := ∂nGn(t, x, y) := n(Gn(t, x, y + 1
n) −Gn(t, x, y))
=
n−1

j=1
exp{−j2π2cn
j t}ϕj(κn(x))n

ϕj(κ+
n (y)) −ϕj(κn(y))

,
(4.25)
for t ≥0, x, y ∈\[0, 1], where κ+
n (y) =: κn(y) + 1
n.
Lemma 4.1. For each T > 0 there exists a constant K > 0 such that
 1
0
(Gn
y −Gy)2(s, x, y) dx = Kn−2s−5/2
for all y ∈\[0, 1], s ∈(0, T] and all integers n ≥2.

Approximation of Burgers’ Equation
9
Proof. Clearly,
Gn
y −Gy = A1 + A2 + A3 + A4 ,
(4.26)
where
A1 :=
∞

j=1
exp{−j2π2s}

ϕj(x) −ϕj(κn(x))

jπψj(y) ,
A2 :=
∞

j=n
exp{−j2π2s}ϕj(κn(x))jπψj(y) ,
A3 :=
n−1

j=1
exp{−j2π2s}ϕj(κn(x))

jπψj(y) −n

ϕj(κ+
n (y)) −ϕj(κn(y))

,
A4 :=
n−1

j=1
{

exp(−j2π2s) −exp(−j2π2cn
j s)

×ϕj(κn(x))n

ϕj(κ+
n (y)) −ϕj(κn(y))

}.
Let ∥Ai∥denote the L2(\[0, 1])-norm of Ai in the x-variable. Fix T > 0, and
let K denote constants, which are independent of t ∈\[0, T], x, y ∈\[0, 1],
s ∈(0, T], n ≥2, but can be different even if they appear in the same line.
Then notice that
∥A1∥2 =
 1
0
Gy(s, x, y) −Gy(s, x, y)
2 dx
≤Kn−2
 1
0
Gyx(s, x, y)
2 dx = Kn−2s−5/2,
(4.27)
by the well-known estimate
|Gyx(s, x, y)| ≤Ks−3/2e−(x−y)2/s,
s ∈\[0, T], x, y ∈\[0, 1],
on the heat kernel. By the orthogonality of {ϕj} in L2(\[0, 1]),
∥A2∥2 =
∞

j=n
exp{−2j2π2s}j2π2ψj(y)2
≤
∞

j=n
j2 exp{−j2s} ≤32
∞

j=n
j2
1
(js1/2)5 ≤Kn−2s−5/2.
(4.28)
By the mean-value theorem
∥A3∥2 =
n−1

j=1
exp{−2j2π2s}

jπψj(y) −n

ϕj(κ+
n (y)) −ϕj(κn(y))

2

10
A. Albert and I. Gy¨ongy
=
n−1

j=1
exp{−2j2π2s}

jπψj(y) −jπψj(θn(y))
2 ,
where θn(y) ∈\[κn(y), κ+
n (y)]. Hence
∥A3∥2 ≤Kn−2
n−1

j=1
j4 exp{−j2s} ≤Kn−2s−2
n−1

j=1
j4s2 exp{−j2s}
≤Kn−2s−2
 n√s
0
x4 exp{−x2}s−1/2 dx ≤Kn−2s−5/2.
(4.29)
Finally,
∥A4∥2 =
n−1

j=1

exp{−j2π2s} −exp{−j2π2cn
j s}
2n2
ϕj(κ+
n (y)) −ϕj(κn(y))
2
≤K
n−1

j=1
j2
exp{−j2π2s} −exp{−j2π2cn
j s}
2
≤K
n−1

j=1
j2
j2π2 exp{−j2π2cn
j s}(1 −cn
j )s
2
≤K
n−1

j=1
j6(1 −cn
j )2s2 exp{−j2s}
by the mean-value theorem and the fact that cn
j ≤1. Hence by the definition
of cn
j in (3.23), using sin x = x + O(x3), we have
∥A4∥2 ≤K
n−1

j=1
j6(jπ/2n)4s2 exp{−j2s} ≤K
n−1

j=1
j6(j/n)4s2 exp{−j2s}
≤Kn−4
n−1

j=1
j10s2 exp{−j2s} ≤Kn−2s−2
n−1

j=1
j8s4 exp{−j2s}
≤Kn−2s−2
 s√n
0
x8 exp{−x2}s−1/2 dx ≤Kn−2s−5/2 .
(4.30)
Thus by virtue of equality (4.26) and inequalities (4.27), (4.28), (4.29) and
(4.30) the proof is complete.
⊓⊔
Lemma 4.2. For each T > 0 there exists a constant K such that
I :=
 T
0
  1
0
|Gn
y −Gy|2(s, x, y) dx
1/2
ds ≤Kn−1/2
(4.31)
for all y ∈\[0, 1].

Approximation of Burgers’ Equation
11
Proof. Clearly, I ≤I1 + I2 + I3, where
I1 :=
 ε
0
  1
0
Gy(s, x, y)2 dx
1/2
ds,
I2 :=
 ε
0
  1
0
Gn
y(s, x, y)2 dx
1/2
ds dy,
I3 :=
 T
ε
 1
0
(Gn
y −Gy)2(s, x, y) dx
1/2
ds dy.
From
Gy(s, x, y) =
∞

j=1
exp(−j2π2s)ϕj(x)jπψj(y),
using the orthogonality of {ϕj}, we get
 1
0
Gy(s, x, y)2 dx ≤
∞

j=1
exp(−2j2π2s)j2π2ψ2
j (y)
≤20
∞

j=1
exp(−j2s)j2 ≤Cs−3/2
for some constant C. Therefore,
I1 ≤
 ε
0
Cs−3/4 ds ≤4Cε1/4.
In exactly the same way, we obtain a constant C such that I2 ≤Cε1/4. By
the estimate in Lemma 4.1, there is a constant C such that
I3 ≤Cn−1
 T
ε
s−5/4 ds dy ≤Cn−1ε−1/4.
Taking ε = n−2, we obtain the statement of the lemma.
⊓⊔
5 Proof of Theorem 2.2
We prove the theorem when f = 0. The proof in the general case of a Lip-
schitz function f goes in the same way, with some additional terms in the
calculations, but without new difficulties. Notice that un(t, x) satisfies
un(t, x) =
 1
0
Gn(t, x, y)u(0, κn(y)) dy
−
 t
0
 1
0
Gn
y(t −s, x, y)\[\[un(s)]](κn(y))dy ds
+
 t
0
 1
0
Gn(t −s, x, y) dW(s, y),
(5.32)

12
A. Albert and I. Gy¨ongy
where Gn and Gn
y are defined by (4.25) and (4.25), respectively. From equa-
tions (2.6) and (5.32)
∥un(t, ·) −u(t, ·)∥≤A(t) + B(t) + C(t),
(5.33)
with
A(t) := ∥
 1
0
Gn(t, ·, y)un
0(y) dy −
 1
0
G(t, ·, y)u0(y) dy∥,
(5.34)
B(t) := ∥
 t
0
 1
0
Gy(t −s, ·, y)u(s, y)2 dy ds
−
 t
0
 1
0
Gn
y(t −s, ·, y)\[\[un(s)]](κn(y)) dy ds∥,
C(t) := ∥
 t
0
 1
0
Gn(t −s, x, y) dW(s, y) −
 t
0
 1
0
G(t −s, x, y) dW(s, y)∥.
(5.35)
Clearly, B ≤B1 + B2, where
B2
1(t) :=
 1
0
  t
0
 1
0
(Gn
y −Gy)(t −s, x, y)\[\[un(s)]](y) dy ds
2
dx,
B2
2(t) :=
 1
0
  t
0
 1
0
Gy(t −s, x, y)(\[\[un(s)]](y) −|u(s, y)|2) dy ds
2
dx.
By Minkowski’s inequality, Lemma 4.2 and Theorem 2.1 we get
B2
1(t) ≤
  1
0
 t
0
  1
0
(Gn
y −Gy)2(s, x, y) dx
1/2
\[\[un(t −s)]](y) ds dy
2
≤Kn−1  t
0
 1
0
\[\[un(s)]](y) dy ds
2
≤ξn−1
(5.36)
for all t ∈\[0, T], where K is a constant and ξ is a finite random variable,
independent of t and n. By Lemma 3.1 (i) from \[7], (take q = 1, ρ = 2,
κ = 1/2 there), we have
B2
2(t) ≤K
  t
0
(t −s)−3/4∥\[\[un(s, ·)]] −|u(s, ·)|2∥1 ds
2
(5.37)
for all t ∈\[0, T], where ∥· ∥1 denotes the L1(\[0, 1])-norm. By simple calcula-
tions, using the Cauchy–Bunyakovskii inequality we get
∥\[\[un(s, ·)]] −|u(s, ·)|2∥1 ≤K∥un(s, ·) −u(s, ·)∥(∥un(s, ·)∥+ ∥u(s, ·∥)
+K∥u(s, ·) −u(s, · + n−1)∥∥un(s, ·∥
(5.38)

Approximation of Burgers’ Equation
13
for all s ∈\[0, T] with a constant K. By Theorem 2.1 and Theorem 1 in \[7],
there is a finite random variable ξ such that almost surely
∥un(s, ·)∥2 ≤ξ,
∥u(s, ·)|2 ≤ξ
for all s ∈\[0, T] and integers n ≥2. Thus from (5.38) and (5.37) by Jensen’s
inequality we obtain
|B2(t)|2 ≤ξ
 t
0
(t −s)−3/4∥un(s, ·) −u(s, ·)∥2 ds + ξζn
(5.39)
for all t ∈\[0, T] and n ≥2, where
ζn := sup
s≤T
∥u(s, ·) −u(s, · + n−1)∥2,
(5.40)
and ξ is a finite random variable independent of t and n. By Burkholder’s
inequality for every p ≥1 there exists a constant Kp such that
E

sup
t≤T
|C(t)|2p

≤Kp

 t
0
 1
0
(Gn −G)2(t −s, ·, y) dy ds

p,
where ∥· ∥p stands for the Lp(\[0, 1]) norm. Consequently, for each p ≥1 there
exists a constant Cp such that
E

sup
t≤T
|C(t)|2p

≤Cpn−p,
since
sup
x∈\[0,1]
 ∞
0
 1
0
|Gn −G|2(t, x, y) dy dt ≤c
n
with a universal constant c by Lemma 3.2 part (i) in \[5]. Hence, by standard
arguments, for any α ∈(0, 1), one gets a finite random variable ξα such that
almost surely
sup
t≤T
|C(t)|2 ≤ξαn−α
(5.41)
for all n ≥2. From (5.33) (5.36), (5.39) and (5.41) we get that almost surely
∥un(t, ·) −u(t, ·)∥2 ≤ξ
 t
0
(t −s)−3/4∥un(s, ·) −u(s, ·)∥2 ds
+ξ(ζn + |A(t)|2 + n−1) + ξαn−α
for all t ∈\[0, T], and integers n ≥2, with a finite random variable ξ, where
A(t), ζn and ξα are defined in (5.34), (5.40) and (5.41), respectively. Hence,
applying a Gronwall-type lemma (e.g. Lemma 3.4 from \[5]), we obtain that
almost surely

14
A. Albert and I. Gy¨ongy
sup
t≤T
∥un(t, ·) −u(t, ·)∥2 ≤ξ

ζn + sup
t≤T
|A(t)|2 + n−1 + ξαn−α

(5.42)
Now we are going to investigate the behaviour of A(t) and ζn as n →∞. Set
vn(t, x) :=
 1
0
Gn(t, x, y)u0(κn(y)) dy
v(t, x) :=
 1
0
G(t, x, y)u0(y) dy.
Assume that u0 ∈C3(\[0, 1]). Then by Proposition 3.8 in \[5] we have a finite
random variable ξ such that almost surely
sup
t,∈\[0,T ]
sup
x∈\[0,1]
|vn(t, x) −v(t, x)| ≤ξn−1
for all n ≥2. Hence almost surely
sup
t∈\[0,T
|A(t)|2 =
 1
0
|vn(t, x) −v(t, x)|2 dx ≤ξ2n−2
(5.43)
for all t ∈\[0, T] and integers n ≥2. Moreover, using Lemma 3.1 (iii) from \[7]
(with ρ = 2, q = 1 and κ = 1/2 there), we get a finite random variable ξ, such
that almost surely
ζn := sup
s≤T
∥u(s, ·) −u(s, · + n−1)∥2 ≤ξn−1
(5.44)
for all n ≥2. Consequently, inequalities (5.42), (5.43) and (5.44) imply esti-
mate (2.11) of Theorem 2.2. Assume now that u0 ∈C(\[0, 1]). Then by Lemma
3.1 (iii) from \[7] and Proposition 3.8 in \[5] we have that almost surely
sup
t∈\[0,T ]
A(t) + ζn →0,
as n →∞. Hence as n →∞,
sup
t≤T
∥un(t, ·) −u(t, ·)∥2 →0
(a.s.).
The proof of Theorem 2.2 is complete.
⊓⊔
Acknowledgements
The authors thank Jessica Gaines for her help in the preparation of the first
version of this paper and for computer simulations. They also thank Jordan
Stoyanov for improvements in the presentation of the paper.

Approximation of Burgers’ Equation
15
References
1. Da Prato, G., Debussche A. and Temam, R.: Stochastic Burgers equation. Non-
linear Differential Equations and Applications 1, 389–402 (1994)
2. Da Prato, G. and Gatarek, D.: Stochastic Burgers equation with correlated
noise. Stochastics and Stochastics Reports 52, 29–41 (1995)
3. Davie, A.M. and Gaines, J.G.: Convergence of numerical schemes for the solution
of parabolic differential equations. Mathematics of Computation 70, 121–134
(2000)
4. Gy¨ongy, I. and Krylov, N.V.: On stochastic equations with respect to semi-
martingales I. Stochastics 4, 1–21 (1980)
5. Gy¨ongy, I.: Lattice approximations for stochastic quasi-linear parabolic differ-
ential equations driven by space-time white noise I. Potential Analysis 9, 1–25
(1998)
6. Gy¨ongy, I.: Lattice approximations for stochastic quasi-linear parabolic differ-
ential equations driven by space-time white noise II. Potential Analysis 11, 1–37
(1999)
7. Gy¨ongy, I.: Existence and uniqueness results for semilinear stochastic partial
differential equations. Stochastic Processes and their Applications 73, 271–299
(1988)
8. Krylov, N. V. and Rozovskii, B.: Stochastic evolution equations. J. Soviet Math-
ematics 16, 1233–1277 (1981)
9. Printems, J.: On discretization in time of parabolic stochastic partial differen-
tial equations. Mathematical Modelling and Numerical Analysis 35, 1055–1078
(2001)
10. Walsh, J.B.: Finite element methods for parabolic stochastic PDE’s, to appear
in Potential Analysis
11. Yoo, H.: Semi-discretization of stochastic partial differential equations on R1 by
a finite-difference method. Mathematics of Computation 69, 653–666 (2000)


Optimal Time to Invest under Tax Exemptions
Vadim I. ARKIN1 and Alexander D. SLASTNIKOV1
Central Economics & Mathematics Institute,
Moscow, Nakhimovskii pr. 47, Moscow, Russia.
arkin@cemi.rssi.ru
slast@cemi.rssi.ru
Summary. We develop a model of the behavior of an agent acting under uncer-
tainty and in a fiscal environment who wants to invest into a creation of new firm
and faces a timing problem. The presence of tax exemptions for newly created firms
reduces the investor planning to the optimal stopping problem for bivariate diffu-
sion process with a non-linear homogeneous reward function. We find a closed-form
formula for optimal stopping time and prove that under certain conditions it gives
indeed the optimal solution to the investment timing problem.
Key words: real options, tax exemptions, optimal stopping time, bivariate geo-
metric Brownian motion, homogeneous reward function
Mathematics Subject Classification (2000): 60G40, 91B70
1 Introduction
Uncertainty and irreversibility have long been recognized as main determi-
nants of investment. As argued in \[6], most investment decisions feature three
important characteristics: investment irreversibility, uncertainty, and the abil-
ity to choose the optimal timing of investment. In contrast with the traditional
investment theory based on the Net Present Value Criterion and Now-or-Never
Principle, the real option literature has been focused around the delay in in-
vestment decisions (see, e.g., \[6], \[17] as well as the seminal paper \[11]). This
flexibility in the investment timing gives the option to wait for new informa-
tion.
In the real option framework the optimal investment policy can be obtained
as the solution to an optimal stopping problem. In the simple case of a project
with constant (over time) investments the underlying problem is an optimal
stopping for one-dimensional process of the present value of the project, which
is usually assumed to be a geometric Brownian motion without/with jumps
(see \[6], \[11], \[12]). In a more symmetric case, when both the present value

18
V. Arkin and A. Slastnikov
and the investment required for launching the project evolve as stochastic
processes, the underlying problem will be an optimal stopping for bivariate
stochastic process (usually, of a geometric Brownian type) and reward function
which is the expected discounted difference between the present value and
the investment cost. One of the first results in this direction was obtained
by McDonald and Siegel \[11] who gave a closed-form solution for the case of
bivariate correlated geometric Brownian motion. However, they did not set the
precise conditions needed for the validity of their result. The rigorous proof of
optimality in the McDonald–Siegel formula for optimal stopping time as well
as the relevant conditions was given only a decade later by Hu and Øksendal
\[8]. Moreover, they treated a multi-dimensional case where the investment
cost is a sum of correlated geometric Brownian motions.
Another source of multi-dimensional optimal stopping problems is a valu-
ation of American options on multiple assets — see, e.g. \[5], \[7]. The Russian
option introduced by Shepp and Shiryaev \[14], also can be viewed as an opti-
mal stopping problem for a bivariate Markov process whose components are
processes of stock prices and maximal historical (up to the current time) stock
prices.
Although the theory provides general rules for finding an optimal stopping
time (see, e.g., Shiryaev’s monographs \[15], \[16]), the obtaining of closed form
formulas is a hard problem for multi-dimensional processes. Most of results in
this direction (for multivariate case) are related to geometric Brownian motion
and linear reward function. A rare exception is the paper by Gerber and
Shiu \[7], who derived a closed-form formula for bivariate correlated geometric
Brownian motion and homogeneous reward function. Their case covers such
perpetual (without the expiration date) American options on two stocks as
Margrabe exchange option, maximum option and some others. They used
first-order conditions to determine the optimal stopping boundaries, but did
not verify whether the relevant solution is indeed the optimal one to the
underlying problem.
In the present paper we demonstrate that multivariate optimal stopping
problem with non-linear reward function arises in a natural way for the mod-
els of creation of new firms in a fiscal environment (including both taxes
and tax exemptions for new firms). Namely, some not restrictive assumptions
about the structure of investor’s cash flow and tax holidays for newly created
enterprizes lead to an optimal investment timing problem with non-linear (rel-
atively to the underlying processes) reward function. We derive a closed-form
formula for optimal investment time and prove that under certain conditions
it gives indeed the optimal solution to the investment timing problem.
The paper is organized as follows. Section 2 describes the behavior of an
investor (under uncertainty and in a fiscal environment) who is interested in
investing into the project aimed at creating a new firm and faces the invest-
ment timing problem. A solution to this problem, an optimal investment rule,
is described in Section 3. As we show in 3.3, the problem under considera-
tion is reduced to an optimal stopping problem for bivariate diffusion process

Optimal Time to Invest
19
and homogeneous (of degree 1) reward function. The closed-form formula for
optimal investment time described in Theorem 1 is proved in Section 4.
2 The basic model
Before to proceed with the model description, we compare our model with
some closely related contributions.
The model is connected with an investment project directed to the creation
of a new industrial firm (enterprize). An important feature of the considered
model is the assumption that, at any moment, a decision-maker (investor)
may either accept the project and proceed with the investment or delay the
decision until he obtains a new information on the environment (prices of the
product and resources, the demand etc.). Thus, the main goal of the decision-
maker in this situation is to find, using the available information, a “good”
time for investing the project (investment timing problem).
The real options theory is a convenient and adequate tool for modelling the
process of firm creation since it allows us to study the effects connected with a
delay in the investment (investment waiting). As in the real options literature,
we model investment timing problem as an optimal stopping problem for
present values of the created firm (see, e.g. \[6], \[11]).
A creation of an industrial enterprize is usually accompanied by certain
tax benefits (in particular, the new firm can be exempted from the profit
taxes during a certain period). The distinguishing feature of our settings is
the representation of the firm present value as an integral of the profit flow.
Considerations of this type allows us to take into account in an explicit form
some peculiarities of a corporate profit taxation system, including the tax ex-
emption. Such an approach was applied by the authors in a detailed modelling
of investment project under taxation (but without tax exemptions) in \[3], and
for finding the optimal depreciation policy in \[1].
Uncertainty in an economic system is modelled by a probability space
(Ω, F, P) with a filtration F = (Ft, t ≥0). The σ-algebra Ft can be inter-
preted as the observable information about the system up to the time t.
An infinitely-lived investor faces a problem to choose when to invest in a
project aimed to launch a new firm.
The cost of investment required to create firm at time t is It. Investment
are considered to be instantaneous and irreversible so that they cannot be
withdrawn from the project any more and used for other purposes (sunk
cost). We assume that (It, t ≥0) is an adapted random process.
Let us suppose that investment into creating a firm is made at time τ ≥0.
Let πτ
τ+t be the flow of profit from the firm at time t + τ, i.e. gross income
minus production cost except depreciation charges, and Dτ
t+τ denotes the
flow of depreciation at the same time. πτ
τ+t and Dτ
t+τ are assumed to be
Ft+τ-measurable random variables (t, τ ≥0).

20
V. Arkin and A. Slastnikov
If γ is the corporate profit tax rate, then after-tax cash flow of the firm at
time t + τ is equal to
πτ
τ+t −γ(πτ
τ+t −Dτ
t+τ) = (1 −γ)πτ
τ+t + γDτ
t+τ.
(2.1)
Creating a new firm in the real economy is usually accompanied by certain
tax benefits. One of the popular incentives tools is tax holidays, when the
new firm is exempted from the profit tax during a payback period. According
to the accepted definitions, the payback period is specified as the minimal
interval (following the time of firm’s creation) during which the accumulated
discounted expected profits exceed the initial investment required for creating
the firm.
For the firm created at time τ, we define the payback period ντ as follows:
ντ = inf

ν ≥0 : E

ν

0
πτ
τ+te−ρtdt
Fτ

≥Iτ

(2.2)
where ρ is discount rate.
Note that ντ is an Fτ-measurable random variable not necessarily finite
a.s. Further we will often refer to the set of finite payback periods:
Ωτ = {ω ∈Ω: ντ < ∞}.
(2.3)
For simplicity we assume that the firm begins to generate profits right
after the investment is made. Then, accordingly to the cash flow (2.1) and tax
holidays (2.2), the present value of the firm Vτ (discounted to the investment
time τ) can be expressed by the following formula:
Vτ = E


ντ

0
πτ
τ+te−ρtdt + χΩτ
∞

ντ
\[(1 −γ)πτ
τ+t + γDτ
t+τ]e−ρt dt

Fτ

, (2.4)
where χΩτ (ω) is the indicator function of the event Ωτ defined in (2.3).
The behavior of the agent is assumed to be rational. This means that he
solves the investment timing problem: at any time τ prior to the investment
he chooses whether to pay Iτ and earn the present value Vτ, or to delay
further his investment. So, the investor’s decision problem is to find such a
stopping time τ (investment rule), that maximizes the expected net present
value (NPV) from the future activity:
E (Vτ −Iτ) e−ρτ →max
τ ,
(2.5)
where the maximum is taken over all Markov times τ and Vτ is defined in
(2.4).

Optimal Time to Invest
21
3 Solution of the investment timing problem
3.1 Main assumptions
Let (w1
t ), (w2
t ) be two independent standard Wiener processes on the given
stochastic basis. They are thought as underlying processes modelling Eco-
nomic Stochastics. We assume that σ-algebra Ft is generated by these
processes up to t, i.e. Ft = σ{(w1
s, w2
s), s ≤t}.
The process of profits πτ
τ+t is represented as follows:
πτ
τ+t = πτ+tξτ
τ+t,
t, τ ≥0,
(3.6)
where (πt) is geometric Brownian motion, specified by the stochastic equation
πt = π0 + α1
t

0
πs ds + σ1
t

0
πs dw1
s
(π0 > 0, σ1 ≥0),
t ≥0,
(3.7)
and (ξτ
τ+t, t ≥0) is a family of non-negative diffusion processes, homogeneous
in τ ≥0, defined by the stochastic equations
ξτ
τ+t = 1 +
t+τ

τ
a(s −τ, ξτ
s ) ds +
t+τ

τ
b(s −τ, ξτ
s ) dw1
s,
t, τ ≥0,
(3.8)
with given functions a(t, x), b(t, x) (satisfying the standard conditions for the
existence of the unique strong solution in (3.8) – see, e.g. \[13, Ch.5]).
The process πt in representation (3.6) can be related to the exogeneous
prices of produced goods and consumed resources (external uncertainty),
whereas fluctuations ξτ
τ+t can be generated by the firm created at time τ
(firm’s uncertainty). Obviously, πτ
τ = πτ for any τ ≥0.
The cost of the required investment It is also described by the geometric
Brownian motion as
It = I0 + α2
t

0
Is ds +
t

0
Is(σ21 dw1
s + σ22 dw2
s),
(I0 > 0)
t ≥0,
(3.9)
where σ21, σ22 ≥0. To avoid a degenerate case we assume that σ22 > 0.
Then the linear combination σ21w1
t + σ22w2
t has the same distribution as
(σ2
21 + σ2
22)1/2 ˜wt, where ˜wt is a Wiener process correlated with w1
t and the
correlation coefficient is equal to σ21(σ2
21 + σ2
22)−1/2.
Depreciation charges at the time t + τ (for the firm created at the time τ)
will be represented as:
Dτ
τ+t = Iτat,
t ≥0,
(3.10)
where (at) is the “depreciation density” (per unit of investment), character-
izing a depreciation policy, i.e. a non-negative function a : R1
+ →R1
+ such

22
V. Arkin and A. Slastnikov
that

at dt = 1. Such a scheme covers various depreciation models, accepted
by the modern tax laws (more exactly, their variants in continuous time).
For example, the well-known Declining Balance Depreciation Method can be
described by the exponential density at = ηe−ηt, where η > 0 is the DB-
depreciation rate.
3.2 Derivation of the present value
The above assumptions allow us to obtain formulas for the present value of
the future firm.
In order all values in the model were well-defined, we suppose that the
profits πτ
τ+t have finite expectations for all t, τ ≥0.
We need the following assertion.
Lemma 3.1. Let τ be a finite (a.s.) Markov time. Then for all t ≥0
E(πτ
τ+t|Fτ) = πτBt,
where Bt = E(πtξ0
t )/π0.
Proof. Recall that the process wt = w1
t+τ −w1
τ, t ≥0 is a Wiener process
independent on Fτ. Using the explicit formula for the geometric Brownian
motion one can rewrite relation (3.6) as follows:
πτ
τ+t = πτΠτ
t+τ,
where Πτ
t+τ = exp{(α1 −1
2σ2
1)t + σ1 wt}ξτ
τ+t.
Homogeneity of the family (3.8) in τ implies that the process ξτ
τ+t coincides
(a.s.) with the unique (in the strong sense) solution of the stochastic equation
ξt = 1 +
t

0
a(s, ξs) ds +
t

0
b(s, ξs) d ws.
Since (ξt, t ≥0) is independent on Fτ, the process Πτ
t+τ is independent also.
Moreover, Πτ
t+τ has the same distribution as exp{(α1 −1
2σ2
1)t + σ1 wt}ξt, or
as (πt/π0)ξ0
t . Therefore, E(πτ
τ+t|Fτ) = πτEΠτ
t+τ = πτE(πtξ0
t )/π0.
⊓⊔
Let us assume that the following condition holds:
B =
∞

0
Bte−ρt dt < ∞,
where the function Bt is defined in Lemma 1.
We will denote the conditional expectation with respect to Fτ as Eτ.
The above relations and Lemma 1 give the following formulas for the
present value (2.4).
Let τ be a finite (a.s.) Markov time.

Optimal Time to Invest
23
If payback period ντ < ∞(i.e. ω ∈Ωτ, see (2.3)), then
Vτ = Iτ + (1 −γ)

Eτ
∞

0
πτ
τ+te−ρtdt −Eτ
ντ

0
πτ
τ+te−ρtdt

+ γIτA(ντ)
= Iτ(1 + γA(ντ)) −(1 −γ)

Iτ −πτ
∞

0
Bte−ρtdt


= γIτ(1 + A(ντ)) + (1 −γ)πτB,
(3.11)
where the function A(·) is defined as
A(ν) =
∞

ν
ate−ρtdt,
ν ≥0.
(3.12)
According to (2.2) on the set Ωτ we have:
Iτ = Eτ
ντ

0
πτ
τ+te−ρtdt = πτ
ντ

0
Bte−ρtdt.
(3.13)
Let us define the function
ν(p) = min{ν > 0 :
ν

0
Bte−ρtdt ≥p−1},
p > 0
(3.14)
(we put ν(p) = ∞if min in (3.14) is not attained).
Then (3.13) implies that ντ = ν(πτ/Iτ) for ω ∈Ωτ. It is easy to see that
Ωτ = {ντ < ∞} = {ν(πτ/Iτ) < ∞}.
If ντ = ∞(i.e. ω /∈Ωτ), then
Vτ = Eτ
∞

0
πτ
τ+te−ρtdt = πτB.
(3.15)
Combining (3.11) and (3.15) we can write the following formula for the
present value of the created firm:
Vτ =

γIτ(1 + A(ν(πτ/Iτ))) + (1 −γ)πτB,
if ν(πτ/Iτ) < ∞
πτB,
if ν(πτ/Iτ) = ∞,
(3.16)
where the function ν(·) is defined in (3.14).

24
V. Arkin and A. Slastnikov
3.3 Optimal investment timing
As it was pointed out at previous section the problem faced by the investor
(2.5) can be considered as an optimal stopping problem:
E(Vτ −Iτ)e−ρτ →max
τ∈M,
(3.17)
where M is the class of all Markov times with values in R+ ∪{∞}.
Let us define the following function: for p ≥0
A(p) =

A(ν(p)),
if ν(p) < ∞,
0,
if ν(p) = ∞,
where ν(p) is specified in (3.14), and put
g(π, I) = (1 −γ)(πB −I) + γI A(π/I).
(3.18)
Obviously, g(π, I) is a homogeneous, i.e. g(λπ, λI) = λg(π, I) for all λ ≥0,
but non-linear, function. It follows from (3.16) that Vτ −Iτ ≤g(πτ, Iτ). More
precisely, Vτ −Iτ = g(πτ, Iτ) if ν(πτ/Iτ) < ∞, and Vτ −Iτ < g(πτ, Iτ) if
ν(πτ/Iτ) = ∞.
Consider the optimal stopping problem for the bivariate process (πτ, Iτ):
Eg(πτ, Iτ)e−ρτ →max
τ∈M .
(3.19)
A relation between the solutions to the problems (3.17) and (3.19) is de-
scribed by the lemma below.
Lemma 3.2. Let τ ∗be a finite (a.s.) stopping time solving the problem (3.19).
If
ν(πτ ∗/Iτ ∗) < ∞(a.s.), then τ ∗is the optimal investment time for the
investor problem (3.17).
Proof. Obviously,
max
τ
E(Vτ −Iτ)e−ρτ ≤max
τ
Eg(πτ, Iτ)e−ρτ = Eg(πτ ∗, Iτ ∗)e−ρτ ∗.
On the other hand, since ν(πτ ∗/Iτ ∗) < ∞a.s., then
max
τ
E(Vτ −Iτ)e−ρτ ≥E(Vτ ∗−Iτ ∗)e−ρτ ∗= Eg(πτ ∗, Iτ ∗)e−ρτ ∗.
Therefore,
max
τ
E(Vτ −Iτ)e−ρτ = Eg(πτ ∗, Iτ ∗)e−ρτ ∗= E(Vτ ∗−Iτ ∗)e−ρτ ∗,
i.e. τ ∗is an optimal stopping time for the problem (3.17).
⊓⊔

Optimal Time to Invest
25
So, the investment timing problem is reduced to an optimal stopping prob-
lem for bivariate geometric Brownian motion and homogeneous reward func-
tion. Similar problem was considered by Gerber and Shiu \[7] in the framework
of perpetual American options on two assets. Their study was focused on the
derivation of optimal continuation regions by the smooth pasting method, but
they did not state precise conditions for the validity of their results.
We set below the formula for optimal stopping time for such a problem,
and prove rigorously that under some additional conditions it gives indeed an
optimal solution to the investment timing problem.
Let β be a positive root of the quadratic equation
1
2 ˜σ2β(β −1) + (α1 −α2)β −(ρ −α2) = 0,
(3.20)
where ˜σ2 = (σ1−σ21)2+σ2
22 > 0 (since σ22 > 0) is the “total” volatility of
investment project. It is easy to see that β > 1 whenever ρ > max(α1, α2).
Let us denote f(p) = g(p, 1), where function g is defined in (3.18), and
h(p) = f(p)p−β,
p > 0.
(3.21)
As one can see, h(p) < 0 if p < B−1 (and ν(p) = ∞), h(p) > 0 if p > B−1,
and h(p) →0 when p →∞. Since g is continuous function, h(p) attains
maximum at some point p∗> B−1. Remind that p∗is called a strict maximum
point for the function h(p) if h(p∗) > h(p) for any p ̸= p∗.
The next theorem characterizes completely the optimal investment time.
Theorem 3.1. Let the processes of profits and required investments be de-
scribed by relations (3.6)–(3.9). Assume that ρ > max(α1, α2) and the follow-
ing condition is satisfied:
α1 −1
2σ2
1 ≥α2 −1
2(σ2
21 + σ2
22).
(3.22)
Let at, Bt ∈C1(R+), p∗be the strict maximum point for the function h(p),
and
f ′(p)p−β+1 decrease for p > p∗.
(3.23)
Then the optimal investment time for the problem (3.17) is
τ ∗= min{t ≥0 : πt ≥p∗It}.
The proof of this theorem one can find in the next section.
4 The proof
As we have seen above the investor’s problem (3.17) is reduced to the optimal
stopping problem (3.19) for bivariate process (πt, It) specified by formulas
(3.7) and (3.9).

26
V. Arkin and A. Slastnikov
For proving the Theorem 3.3 we will use the variational approach to opti-
mal stopping problems for multi-dimensional diffusion processes described in
\[2], \[3]. Besides the formal proof we demonstrate also an approach to obtain
a formula for the optimal stopping time different from the smooth pasting
method.
It is convenient to introduce the “homogeneous” notations X1
t = πt, X2
t =
It. The process Xt = (X1
t , X2
t ), is a bivariate geometric Brownian motion with
correlated components:
dX1
t = X1
t (α1dt + σ1dw1
t ),
dX2
t = X2
t \[α2dt + (σ21 dw1
t + σ22 dw2
t )],
(4.24)
and initial state (X1
0, X2
0) = (x1, x2).
Let us consider a family of regions in R2
++ = {(x1, x2) : x1, x2 > 0} of the
following type
Gp = {(x1, x2) ∈R2
++ : x1 < px2},
p > 0.
For the process Xt = (X1
t , X2
t ), described by the system (4.24) with initial
state x = (x1, x2) ∈R2
++, we denote τp(x) the exit time from the region Gp:
τp(x) = min{t ≥0 : Xt /∈Gp} = min{t ≥0 : X1
t ≥pX2
t }.
For x ∈R2
++ and homogeneous function g(x) (see (3.18)) define
Fp(x) = Exe−ρτp(x)g(Xτp(x))
(here and below the upper index at the expectation Ex denotes the initial
state x of the process Xt).
If x /∈Gp, then τp(x) = 0 and, hence, Fp(x) = g(x) for x ∈R2
++\Gp. If
x ∈Gp, then τp(x) > 0 a.s. due to continuity of diffusion process.
Lemma 4.3. If (3.22) holds, then τp(x) < ∞a.s. for any x∈R2
++ and p > 0.
Proof. It follows the explicit formulas for X1
t and X2
t that
X1
t
X2
t
= x1
x2
exp

α1−α2 + σ2
21+σ2
22−σ2
1
2

t + (σ1−σ21)w1
t −σ22w2

= x1
x2
exp

α1−α2 + σ2
21+σ2
22−σ2
1
2

t + ˜σ ˜wt

,
(4.25)
where ˜wt = σ1−σ21
˜σ
w1
t −σ22
˜σ w2 is a standard Wiener process. According to
the law of iterated logarithm for Wiener process
lim sup
t→∞| ˜wt|/

2t log log t = 1
a.s.

Optimal Time to Invest
27
and (4.25) implies lim sup
t→∞X1
t /X2
t = ∞a.s. if α1−α2+ 1
2(σ2
21+σ2
22−σ2
1) ≥0
(condition (3.22)). Therefore, τp(x) = min{t ≥0 : X1
t /X2
t ≥p} < ∞a.s. for
any x ∈R2
++ and p > 0.
⊓⊔
Now we can derive the functional Fp(x).
Lemma 4.4. If ρ > max(α1, α2) and (3.22) holds, then
Fp(x1, x2) =

h(p)xβ
1x1−β
2
, if x1 < px2
g(x1, x2),
if x1 ≥px2
,
where h(p) is defined in (3.21).
Proof. At first, show that Fp(x) is a homogeneous (of degree 1) function.
Since τp(x) is the first exit time over the level p for the process X1
t /X2
t ,
formula (4.25) implies that the function τp(x) is homogeneous of degree 0 in
x = (x1, x2), i.e. τp(λx) = τp(x) for all λ > 0. The homogeneity properties of
the process Xt (in initial state) and the function g imply:
Fp(λx) = Eλxe−ρτp(λx)g(Xτp(λx)) = Eλxe−ρτp(x)g(Xτp(x))
= Exe−ρτp(x)g(λXτp(x)) = λFp(x).
It is known that Fp(x) is the solution of Dirichlet boundary problem:
LF(x) = ρF(x),
x ∈Gp,
(4.26)
F(x) →g(a),
when x →a, x ∈Gp, a ∈∂Gp,
(4.27)
where L is the generator of the process Xt (variants of a more general state-
ment usually referred to as the Feynman–Kac formula one can find in \[9], \[10],
\[13]).
As one can see, the generator of the process (4.24) is
LF(x1, x2) = α1x1
∂F
∂x1
+ α2x2
∂F
∂x2
+ 1
2σ2
1x2
1
∂2F
∂x2
1
+ σ1σ21x1x2
∂2F
∂x1∂x2
+1
2(σ2
21 + σ2
22)x2
2
∂2F
∂x2
2
.
(4.28)
The homogeneous function Fp(x) can be represented as Fp(x1, x2) =
x2Q(y) where y = x1/x2, Q(y) = Fp(y, 1). This and formula (4.28) for the
elliptic operator L transforms PDE (4.26) to the ordinary differential equation
1
2y2Q′′(y)˜σ2 + yQ′(y)(α1 −α2) −Q(y)(ρ −α2) = 0.
(4.29)
The general solution of equation (4.29) for 0 < y < p is of the form
Q(y) = C1yβ1 + C2yβ2, where β1 > 0, β2 < 0 are the roots of quadratic
equation (3.22). Returning to initial function we have

28
V. Arkin and A. Slastnikov
Fp(x1, x2)=C1xβ1
1 x1−β1
2
+C2xβ2
1 x1−β2
2
,
0 < x1 < px2.
(4.30)
Since the homogeneous function g, defined in (3.18), is bounded by some linear
function, i.e. g(x1, x2) ≤C(x1 + x2), were C = max
0≤y≤1 g(y, 1 −y),
Fp(x1, x2) ≤C max
τ
E(X1
τ + X2
τ )e−ρτ
where max is taken over all Markov times τ. Standard martingale arguments
and the condition ρ > max(α1, α2) imply that
EX1
τ e−ρτ = x1Ee−(ρ−α1)τeσ1w1
τ −σ2
1τ/2 ≤x1Eeσ1w1
τ −σ2
1τ/2 = x1.
Similarly, EX2
τ e−ρτ ≤x2. Therefore, Fp(x1, x2) is also bounded by the linear
function C(x1 + x2).
This fact implies that C2 = 0 in representation (4.30) (otherwise Fp(x1, x2)
would be unbounded when x1 →0, x1 < px2). The constant C1 can be
found from the boundary condition (4.27) at the line {x1 = px2}, namely,
Fp(px2, x2) = C1x2pβ1 = g(px2, x2) = x2f(p), i.e. C1 = f(p)p−β1 = h(p), see
(3.21).
⊓⊔
Let M1(x) = {τp(x), p > 0} ⊂M be the class of first exit times from the
sets Gp for the process Xt (starting from the state x = (x1, x2)). Consider the
restriction of the optimal stopping problem (3.19) to the class M1(x):
Exg(Xτ)e−ρτ →
max
τ∈M1(x) .
(4.31)
Obviously, this problem is equivalent to the following extremal problem
Fp(x1, x2) →max
p>0 .
(4.32)
The explicit form of the functional Fp from Lemma 4.2 allows us to find
the solution to the problem (4.32) and, therefore, the solution to the optimal
stopping problem (4.31).
Lemma 4.5. Let the conditions of Lemma 4.2 hold, p∗be a strict maximum
point of the function h(p) (defined in (3.21)), and h(p) decrease for p > p∗.
Then the following statements hold:
1) τ ∗= min{t ≥0 :
X1
t ≥p∗X2
t } is the optimal stopping time for the
problem (4.31) for all x ∈R2
++;
2) If, in addition, τp(x) > 0 a.s. for some x ∈R2
++, p > 0, and h(p)
strictly decreases for p > p∗, then τp(x) is the optimal stopping time for the
problem (4.31) if and only if p = p∗;
3) The optimal value of the functional in the problem (4.31) is
Φ(x1, x2) =

h(p∗)xβ
1x1−β
2
, if x1 < p∗x2
g(x1, x2),
if x1 ≥p∗x2
.
(4.33)

Optimal Time to Invest
29
Proof. 1) Let us check that Fp(x) ≤Fp∗(x) for all p > 0 and x ∈R2
++.
By the definition of p∗we have for the homogeneous function g:
g(x) = x2f(x1/x2) = h(x1/x2)xβ
1x1−β
2
≤h(p∗)xβ
1x1−β
2
.
Let p<p∗. Then Lemma 4.2 gives: if x1≥p∗x2 then Fp(x)=g(x)=Fp∗(x);
if px2≤x1<p∗x2 then Fp(x)=g(x)≤h(p∗)xβ
1x1−β
2
=Fp∗(x); and if x1<px2 then
Fp(x) = h(p)xβ
1x1−β
2
< h(p∗)xβ
1x1−β
2
= Fp∗(x).
(4.34)
For p > p∗we have: if x1≥px2 then Fp(x)=g(x)=Fp∗(x); if p∗x2≤x1<px2
then Fp(x)=h(p)xβ
1x1−β
2
≤h(x1/x2)xβ
1x1−β
2
=g(x)=Fp∗(x) due to monotonicity
of h(p) for p > p∗; and if x1 < p∗x2 then
Fp(x) = h(p)xβ
1x1−β
2
< h(p∗)xβ
1x1−β
2
= Fp∗(x).
(4.35)
Thus, Fp(x) ≤Fp∗(x) for all x ∈R2
++ and p > 0. Hence, maximum at
the problem (4.32) is attained at p = p∗. From this and the definition of class
M1(x) follows statement 1).
2) Since τp(x) > 0 a.s., x1 < px2. Let us show that the optimality of τp(x)
implies that p = p∗.
Assume that p < p∗. Then we have inequality (4.34) with p = p, that
contradicts to the optimality of τp(x). Assume now that p > p∗. For x1 < p∗x2
we have (4.35) with p = p, i.e. the contradiction with the optimality. And if
p∗x2≤x1<px2, then Fp(x)=h(p)xβ
1x1−β
2
<h(x1/x2)xβ
1x1−β
2
=g(x)=Fp∗(x) due
to strict decreasing of h(p) for p > p∗. So, p = p∗that proves (together with
the optimality of p∗) statement 2) of the lemma.
Statement 3) follows directly from Lemma 4 for p = p∗.
⊓⊔
Let us emphasize that the region of optimal stopping
Gp∗= {(x1, x2)∈R2
++ : x1 ≥p∗x2}
does not depend on the initial state of the process Xt.
Proof of Theorem 3.3. In order to prove that the stopping time τ ∗, defined in
Lemma 4.3, will be optimal for the initial problem
Exg(Xτ)e−ρτ →max
τ∈M
(4.36)
(over all Markov times M) we use the following “verification theorem”, based
on variational inequalities method (see, e.g. \[4], \[13]). Below we formulated it
for our case.
Theorem 4.2 (Øksendal \[13], Hu, Øksendal \[8]). Suppose, there exists
a function Φ : R2
++ →R, satisfying the following conditions:
1) Φ ∈C1(R2
++) ∩C2(R2
++ \ ∂G) where G = {x∈R2
++ : Φ(x)>g(x)};

30
V. Arkin and A. Slastnikov
2) ∂G is locally the graph of Lipschitz function and Ex
 ∞
0
χ∂G(Xt) dt = 0
for all x ∈R2
++;
3) Φ(x) ≥g(x) for all x ∈R2
++;
4) LΦ(x) = ρΦ(x) for all x ∈G;
5) LΦ(x) ≤ρΦ(x) for all x ∈R2
++ \ ¯G
( ¯G is a closure of the set G);
6) ¯τ = inf{t ≥0 : Xt /∈G} < ∞a.s. for all x ∈R2
++;
7) the family {g(Xτ)e−ρτ, M ∋τ ≤¯τ} is uniformly integrable for all x ∈G.
Then ¯τ is the optimal stopping time for the problem (4.36), and Φ(x) is
the correspondent optimal value of the functional in (4.36).
As a candidate we try the function Φ(x1, x2), defined in (4.33). It is easy
to see that Φ∈C1(R2
++) due to first-order condition for the maximum point
p∗:
βh(p∗)(p∗)β−1 = f ′(p∗).
For x = (x1, x2) ∈R2
++ let us denote p(x) = x1/x2.
Since h(p∗)>h(p) for all p ̸= p∗, then on the set {(x1, x2)∈R2
++ : x1<p∗x2}
we have
Φ(x1, x2) = h(p∗)xβ
1x1−β
2
> h(p(x))x2 (x1/x2)β
= x2f (x1/x2) (x1/x2)−β (x1/x2)β = g(x1, x2)
(the latter equality follows from the homogeneity of the function g).
Therefore, Φ(x) ≥g(x) for all x ∈R2
++, and the domain G = {x ∈R2
++ :
Φ(x) > g(x)} coincides with {x1 < p∗x2} = {(x1, x2) : 0 ≤p(x) < p∗}. So,
∂G = {(x1, x2) : x1 = p∗x2}.
The property Φ∈C2(R2
++\∂G) follows from the twice differentiability
of g(x1, x2) on the set {(x1, x2)∈R2
++ : Bx1>x2}, due to the conditions
at, Bt∈C1(R+).
Condition 2) of Theorem 4.4 follows from local properties of geometric
Brownian motion. Condition 4) follows immediately from the construction of
the function Φ = Fp∗(see (4.26) in the proof of Lemma 4.2).
Furthermore, ¯τ = inf{t ≥0 : Xt /∈G} = inf{t ≥0 : X1
t ≥p∗X2
t } < ∞
a.s. for all x ∈R2
++ due to Lemma 4.1, i.e. 6) holds.
Let us show that condition 7) of Theorem 4.4 holds if ρ > α2. Indeed, if
τ ≤¯τ then X1
τ ≤p∗X2
τ and, therefore,
Φ(Xτ)e−ρτ=h(p∗)X2
τ
X1
τ
X2τ
β
e−ρτ≤h(p∗)(p∗)βX2
τ e−ρτ=CX2
τ e−ρτ,
where C = h(p∗)(p∗)β.
Let us denote σ2
2 = σ2
21 + σ2
22. Then ¯wt = (σ2
21w1
t + σ2
22w2
t )/σ2 is the stan-
dard Wiener process. Hence, from the explicit formula for geometric Brownian
motion using martingale arguments we have:

Optimal Time to Invest
31
Ex\[Φ(Xτ)e−ρτ]k ≤Ckxk
2Ex exp{\[−ρτ + (α2 −1
2σ2
2)τ + σ2 ¯wτ]k}
= Ckxk
2Ex exp{−\[ρ−α2−1
2σ2
2(k−1)]kτ+kσ2 ¯wτ−1
2k2σ2
2τ}
≤Ckxk
2Ex exp{kσ2 ¯wτ −1
2k2σ2
2τ} = Ckxk
2,
if k > 1 is chosen such that ρ −α2 −1
2σ2
2(k −1) ≥0. Thus, the uniform
integrability of the family {g(Xτ)e−ρτ, τ ≤¯τ} holds (since g(x) ≤Φ(x)) .
It is remained to check the condition 5) of Theorem 4.4. Let us
take x=(x1, x2)/∈¯G, i.e. x1>p∗x2. For this case p(x)>p∗and Φ(x1, x2) =
g(x1, x2) = x2f(p(x)). Repeating arguments, similar to those in the proof
of Lemma 4.2, we have:
Lg(x) −ρg(x) = x2
1
2p2(x)f ′′(p(x))˜σ2 + p(x)f ′(p(x))(α1 −α2)
−f(p(x))(ρ −α2)

.
The condition (3.23) is equivalent to the inequality pf ′′(p) ≤(β −1)f ′(p)
for p > p∗. Integrating both sides of the latter relation from p∗to p one can
obtain that pf ′(p) ≤p∗f ′(p∗) −βf(p∗) + βf(p) = βf(p), since h′(p∗) = 0.
These inequalities imply:
Lg(x) −ρg(x)
x2
= 1
2p2f ′′(p)˜σ2 + pf ′(p)(α1 −α2) −f(p)(ρ −α2)
≤1
2p2f ′′(p)˜σ2 + pf ′(p)

α1 −α2 −1
β (ρ −α2)

= 1
2p2f ′′(p)˜σ2 −pf ′(p)1
2 ˜σ2(β −1) ≤0,
where p = p(x)
(here we use the fact that β is a root of equation (3.22)). Thus, all the condi-
tions of Theorem 4.4 hold and, therefore, ¯τ = inf{t ≥0 : X1
t ≥p∗X2
t } = τ ∗
is the finite (a.s.) optimal stopping time for the problem (4.34).
As it is shown before the formulation of Theorem 3.3, p∗> 1/B. Hence
ν(p∗) = ν(X1
τ ∗/X2
τ ∗) < ∞, and, due to Lemma 3.2, τ ∗is the optimal stopping
time for the investor’s problem (3.17).
⊓⊔
Acknowledgement
This work was supported by INTAS (grant 03–51–5018), RFBR (grants 05–
06–80354, 03–01–00479) and RFH (grant 04–02–00119).

32
V. Arkin and A. Slastnikov
References
1. Arkin, V.I., Slastnikov, A.D.: Optimal tax depreciation in stochastic investment
model. In: Dzemyda, G., ˘Saltenis, V., ˘Zilinskas, A. (Eds.) Stochastic and Global
Optimization. Kluwer Academic Publ. (2002)
2. Arkin, V.I., Slastnikov, A.D.: Variational approach to optimal stopping problem
for diffusion processes. In: International conference“Kolmogorov and contempro-
rary mathimatics”. Abstracts, 386–387 (2003)
3. Arkin, V.I., Slastnikov, A.D.: Optimal stopping problem and investment models.
In: Marti, K., Ermoliev, Yu., Pflug, G. (eds) Dynamic Stochastic Optimization.
Lecture Notes in Economics and Mathematical Systems, 532, 83–98 (2004)
4. Bensoussan, A., Lions, J.L.: Applications of Variational Inequalities in Stochas-
tic Control. North-Holland (1982)
5. Broadie, M., Detemple, J.: The valuation of American options on multiple assets,
Mathematical Finance 7(3), 241-286 (1996)
6. Dixit, A.K., Pindyck, R.S.: Investment under uncertainty. Princeton, Princeton
University Press (1994)
7. Gerber, H., Shiu, E.: Martingale approach to pricing perpetual American options
on two stocks, Mathematical Finance 3, 303–322 (1996)
8. Hu, Y., Øksendal, B.: Optimal time to invest when the price processes are
geometric Brownian motion. Finance and Stochastics, 2, 295–310 (1998)
9. Karatzas, I., Shreve, S.E.: Brownian motion and stochastic calculus. Springer,
Berlin Heidelberg New York (1991)
10. Krylov, N.V.: Introduction to the theory of diffusion processes. American Math-
ematical Society (1996)
11. McDonald, R., Siegel, D.: The value of waiting to invest. Quarterly Journal of
Economics, 101, 707–727 (1986)
12. Mordecki, E.: Optimal stopping for a diffusion with jumps. Finance and Sto-
chastics, 3, 227–236 (1999)
13. Øksendal, B.: Stochastic Differential Equations. Springer, Berlin Heidelberg
New York (1998)
14. Shepp, L.A., Shiryaev, A.N.: The Russian option: reduced regret. Annals of
Applied Probability, 3, 631–640 (1993)
15. Shiryaev, A.N.: Optimal Stopping Rules. Springer, Berlin Heidelberg New York
(1978)
16. Shiryaev, A.N.: Essentials of Stochastic Finance. Facts, models, theory. World
Scientific, Singapore London (1999)
17. Trigeorgis, L.: Real options: managerial flexibility and strategy in resource allo-
cation. Cambridge, MIT Press (1996)

A Central Limit Theorem for Realised Power
and Bipower Variations of Continuous
Semimartingales
Ole E. BARNDORFF–NIELSEN1, Svend Erik GRAVERSEN2,
Jean JACOD3, Mark PODOLSKIJ4∗, and Neil SHEPHARD5
1 Dept. of Mathematical Sciences, University of Aarhus, Ny Munkegade, DK–8000
Aarhus C, Denmark.
oebn@imf.au.dk
2 Dept. of Mathematical Sciences, University of Aarhus, Ny Munkegade, DK–8000
Aarhus C, Denmark.
matseg@imf.au.dk
3 Laboratoire de Probabilit´es et Mod`eles Al´eatoires (CNRS UMR 7599) Universit´e
P. et M. Curie, 4 Place Jussieu, 75 252 - Paris Cedex, France.
jj@ccr.jussieu.fr
4 Ruhr University of Bochum, Dept. of Probability and Statistics,
Universit¨atstrasse 150, 44801 Bochum, Germany.
podolski@cityweb.de
5 Nuffield College, Oxford OX1 1NF, UK.
neil.shephard@nuf.ox.ac.uk
Summary. Consider a semimartingale of the form Yt = Y0 + t
0 asds+ t
0 σs−dWs,
where a is a locally bounded predictable process and σ (the “volatility”) is an
adapted right–continuous process with left limits and W is a Brownian motion. We
consider the realised bipower variation process
V (Y ; r, s)n
t = n
r+s
2
−1
\[nt]

i=1
|Y i
n −Y i−1
n |r|Y i+1
n −Y i
n |s,
where r and s are nonnegative reals with r + s > 0. We prove that V (Y ; r, s)n
t con-
verges locally uniformly in time, in probability, to a limiting process V (Y ; r, s)t (the
”bipower variation process”). If further σ is a possibly discontinuous semimartingale
driven by a Brownian motion which may be correlated with W and by a Poisson
random measure, we prove that √n (V (Y ; r, s)n −V (Y ; r, s)) converges in law to a
process which is the stochastic integral with respect to some other Brownian mo-
tion W ′, which is independent of the driving terms of Y and σ. We also provide a
∗This author has been partially supported by the DYNSTOCH Research Train-
ing Network, and the financial support of the Deutsche Forschungsgemeinschaft
(SFB 475, ”Reduction of complexity in multivariate data structures”) is gratefully
acknowledged.

34
O. E. Barndorff–Nielsen et al.
multivariate version of these results, and a version in which the absolute powers are
replaced by smooth enough functions.
Key words: Central limit theorem, quadratic variation, bipower variation.
Mathematics Subject Classification (2000): 60F17, 60G44
1 Introduction
For a wide class of real–valued processes Y , including all semimartingales, the
“approximate (or, realised) quadratic variation processes”
V (Y ; 2)n
t =
\[nt]

i=1
(Y i
n −Y i−1
n )2,
(1.1)
where \[x] denotes the integer part of x ∈R+, converge in probability, as
n →∞and for all t ≥0, towards the quadratic variation process V (Y ; 2)t,
usually denoted by \[Y, Y ]t.
This fact is basic in the ”general theory of processes” and is also used
in a large variety of more concrete problems, and in particular for the sta-
tistical analysis of the process Y when it is observed at the discrete times
i/n : i = 0, 1, . . . (sometimes V (Y ; 2)n
t is called the “realised” quadratic
variation, since it is explicitly calculable on the basis of the observations).
In that context, in addition to the convergence in probability one is inter-
ested in the associated CLT (Central Limit Theorem), which says that the
√n (V (Y ; 2)n
t −V (Y ; 2)t)’s converge in law, as processes, to a non–trivial lim-
iting process. Of course, for the CLT to hold we need suitable assumptions on
Y . This type of tool has been used very widely in the study of the statistics
of processes in the past twenty years. References include, for example, the
review paper \[10] in the statistics of processes and \[1], \[2], \[3], \[6] in financial
econometrics. \[2] provides a review of the literature in econometrics on this
topic.
Now, when Y describes some stock price, with a stochastic volatility possi-
bly having jumps, a whole new class of processes extending the quadratic vari-
ation has been recently introduced, and named “bipower variation processes”:
let r, s be nonnegative numbers. The realised bipower variation process of order
(r, s) is the increasing processes defined as:
V (Y ; r, s)n
t = n
r+s
2 −1
\[nt]

i=1
|Y i
n −Y i−1
n |r |Y i+1
n −Y i
n |s,
(1.2)
with the convention 00 = 1. Clearly V (Y ; 2)n = V (Y ; 2, 0)n. The bipower
variation process of order (r, s) for Y , denoted by V (Y ; r, s)t, is the limit in

CLT for bipower variations
35
probability, if it exists for all t ≥0, of V (Y ; r, s)n
t . It has been introduced
in \[4] and \[5], where it is shown that the bipower variation processes exist
for all nonnegative indices r, s as soon as Y is a continuous semimartingale
of “Itˆo type” with smooth enough coefficients. These papers also contain a
version of the associated CLT under somewhat restrictive assumptions and
when r = s = 1.
The aim of this paper is mainly to investigate the CLT, and more precisely
to give weaker conditions on Y which ensure that it holds and which cover
most concrete situations of interest, and also to precisely describe the limiting
process. We prove the existence of the bipower variation process for a wide
class of continuous semimartingales (extending the results of \[4] and \[5]). We
establish the CLT in a slightly more restricted setting. The restriction is that
the volatility of Y (that is, the coefficient in front of the driving Wiener process
for Y ) is a semimartingale driven by a L´evy process, or more generally by a
Wiener process (possibly correlated with the one driving Y ) and a Poisson
random measure.
We also investigate the multidimensional case, when Y = (Y j)1≤j≤d is d–
dimensional. It is then natural to replace (1.2) by the realised “cross–bipower
variation processes”:
V (Y j, Y k; r, s)n
t = n
r+s
2 −1
\[nt]

i=1
|Y j
i
n −Y j
i−1
n |r |Y k
i+1
n −Y k
i
n |s.
(1.3)
We state the results in Section 2, and the proofs are given in the other
sections. The reader will notice that we replace the powers like |Y i
n −Y i−1
n |r
in (1.2) by an expression of the form g(√n(Y i
n −Y i−1
n )) for a suitable function
g: this can prove useful for some applications, and it is indeed a simplification
rather than a complication for the proof itself. Written in this way, our results
also extend some of the results of Becker in \[7], and of the unpublished paper
\[8].
It is also worth observing that, apart from the notational complexity, the
proofs when r > 0 and s > 0 are not really more difficult than when r > 0
and s = 0, that is, when we have only one power in (1.2). That means that,
obviously, the same types of results would hold for the ”realised multipower
variation processes” which are defined by
V (Y j1, . . . , Y jN ; r1, . . . , rN)n
t
= n
r1+...+rN
2
−1
\[nt]

i=1
|Y j1
i
n −Y j1
i−1
n |r1 . . . |Y jN
i+N−1
n
−Y jN
i+N−2
n
|rN ,
(1.4)
for any choice of ri ≥0 and any fixed N. We do not prove those more general
results here, but simply state the results.

36
O. E. Barndorff–Nielsen et al.
2 Statement of results
We start with a filtered space (Ω, F, (Ft)t≥0, P), on which are defined various
processes, possibly multidimensional: so we systematically use matrix and
product–matrices notations. The transpose is denoted by ⋆, all norms are
denoted by ∥.∥. We denote by Md,d′ the set of all d × d′–matrices, and by
Md,d′,d′′ the set of all arrays of size d × d′ × d′′, and so on. For any process
X we write ∆n
i X = Xi/n −X(i−1)/n.
Our basic process is a continuous d–dimensional semimartingale Y
=
(Y i)1≤i≤d. We are interested in the asymptotic behavior of all finite fami-
lies of processes of type (1.3), that is for all j, k ∈{1, . . . , d} and all finite
families of pairs (r, s). So in order to simplify notation (which will neverthe-
less remain quite complicated, sorry for that !), we introduce the following
processes:
Xn(g, h)t = 1
n
\[nt]

i=1
g(√n ∆n
i Y )h(√n ∆n
i+1Y ),
(2.1)
where g and h are two maps on Rd, taking vakues in Md1,d2 and Md2,d3
respectively. So Xn(g, h)t takes its values in Md1,d3. Note that, letting
fj,r(x) = |xj|r,
(2.2)
we have V (Y j, Y k; r, s)n = Xn(fj,r, fk,s), and any finite family of processes
like in (1.3) is a process of the type (2.1) with the components of g and h
being the various fj,r.
2.1 Convergence in probability
We start with the convergence in probability of the processes Xn(g, h). We
need the following structural assumption on Y :
Hypothesis (H): We have
Yt = Y0 +
 t
0
asds +
 t
0
σs−dWs,
(2.3)
where W is a standard d′–dimensional BM, a is predictable Rd–valued locally
bounded, and σ is Md,d′–valued c`adl`ag.
Below ρΣ denotes the normal law N(0, ΣΣ
⋆), and ρΣ(g) is the integral of
g w.r.t. ρΣ.
Theorem 2.1. Under (H) and when the functions g and h are continuous
with at most polynomial growth, we have
Xn(g, h)t →X(g, h)t :=
 t
0
ρσs(g)ρσs(h)ds,
(2.4)
where the convergence is local uniform in time, and in probability.

CLT for bipower variations
37
If we apply this with the functions g = fj,r and h = fk,s, we get a result
of existence for the bipower variation processes. We denote by µr the rth
absolute moment of the law N(0, 1).
Theorem 2.2. Under (H), and if r, s ≥0, we have
V (Y j, Y k; r, s)n
t
→V (Y j, Y k; r, s)t := µrµs
 t
0
|σjj
u |r|σkk
u |s du,
(2.5)
where the convergence is local uniform in time, and in probability.
This result is essentially taken from \[4]. The assumption (H) could be
weakened, of course, but probably not in any essential way. For instance the
c`adl`ag hypothesis on σ can be relaxed, but we need at least the functions
u →|σjj
u |r to be Riemann–integrable, for all (or P–almost all) ω. The fact
that the driving terms in (2.3) are t and Wt is closely related to the fact that
the discretization in time has a constant step 1/n. If we replace (2.3) by
Yt = Y0 +
 t
0
asdAs +
 t
0
σs−dMs,
where A is a continuous increasing process and M a continuous martingale,
then a result like (2.5) can hold only for discretization along increasing se-
quences of stopping times, related in some way to A and to the quadratic
variation of M. If further Y is discontinuous, this type of result cannot pos-
sibly hold (with the normalizing factor n
r+s
2 −1), as is easily seen when Y is
a simple discontinuous process like a Poisson process. As a matter of fact,
this observation was the starting point of the papers \[4] and \[5] for intro-
ducing bipower variations, in order to discriminate between continuous and
discontinuous processes.
Finally, we state the multipower variation result: the processes of (1.4)
converge (under (H)) towards
V (Y j1, . . . , Y jN ; r1, . . . , rN)t = µr1 . . . µrN
 t
0
|σj1j1
u
|r1 . . . |σjNjN
u
|rN du.
(2.6)
2.2 The central limit theorem
For the CLT we need some additional structure on the volatility σ. A relatively
simple assumption is then:
Hypothesis (H0): We have (H) with
σt = σ0 +
 t
0
a′
sds +
 t
0
σ′
s−dWs +
 t
0
vs−dZs,
(2.7)

38
O. E. Barndorff–Nielsen et al.
where Z is a d′′–dimensional L´evy process on (Ω, F, (Ft)t≥0, P), independent
of W (and possibly with a non–vanishing continuous martingale part). Fur-
thermore the processes σ′ and v, and a of (2.7), are adapted c`adl`ag, with val-
ues in Md,d′,d′ and Md,d′,d′′ and Md,d′ respectively, and a′ is Md,d′–valued,
predictable and locally bounded.
This assumption is in fact not general enough for applications. Quite often
the natural ingredient in our model is the ”square” c = σσ∗rather than σ
itself, and it is this c which satisfies an equation like (2.7). In this case the
”square–root” σ of c does not usually satisfy a similar equation. This is why
we may replace (H0) by the following assumption:
Hypothesis (H1): We have (H) with
σt = σ0 +
 t
0
a′
sds +
 t
0
σ′
s−dWs +
 t
0
vs−dVs +
 t
0

E
ϕ ◦w(s−, x)(µ −ν)(ds, dx) +
 t
0

E
(w −ϕ ◦w)(s−, x)µ(ds, dx). (2.8)
Here a′ and σ′ and v are like in (H0); V is a d′′–dimensional Wiener process
independent of W, with an arbitrary covariance structure; µ is a Poisson ran-
dom measure on (0, ∞) × E independent of W and V , with intensity measure
ν(dt, dx) = dtF(dx) and F is a σ–finite measure on the Polish space (E, E);
ϕ is a continuous truncation function on Rdd′ (a function with compact sup-
port, which coincides with the identity map on a neigbourhood of 0); finally
w(ω, s, x) is a map Ω× \[0, ∞) × E
→Md,d′ which is Fs ⊗E–measurable
in (ω, x) for all s and c`adl`ag in s, and such that for some sequence (Sk) of
stopping times increasing to +∞we have:
sup
ω∈Ω,s<Sk(ω)
∥w(ω, s, x)∥≤ψk(x),
where

E
(1∨ψk(x)2) F(dx) < ∞. (2.9)
This hypothesis looks complicated, but it is usually simple to check. The
conditions on the coefficients imply in particular that all integrals in (2.8) are
well defined. It is weaker than (H0): indeed if (H0) holds, we also have (H1)
with E = Rd′′ and V being the Wiener part of Z if it exists, and µ being the
random measure associated with the jumps of Z (so F is the L´evy measure of
Z), and w(ω, t, x) = vt(ω)x (note that v is the same in (2.7) and in (2.8); the
processes a′ in the two formulae are different, depending on the drift of Z).
We also sometimes need an additional assumption:
Hypothesis (H’): The process σσ⋆is everywhere invertible.
Set once more c = σσ∗. If the processes c and c−are invertible, (H1)
holds if and only if the process c satisfies an equation like (2.8), with the same
assumptions on the coefficients. This is not longer true if we replace (H1) and
(2.8) by (H0) and (2.7).

CLT for bipower variations
39
As for the functions g and h, we will suppose that their components satisfy
one of the following assumptions, which we write for a real–valued function
f on Rd; if f is differentiable at x, we write ∇f(x) for the row matrix of its
partial derivatives:
Hypothesis (K): The function f is even (that is, f(−x) = f(x) for all
x ∈Rd) and continuously differentiable, with partial derivatives having at
most polynomial growth.
Hypothesis (K’): The function f is even and continuously differentiable on
the complement Bc of a closed subset B ⊂Rd and satisfies
∥y∥≤1
⇒
|f(x + y) −f(x)| ≤C(1 + ∥x∥p) ∥y∥r
(2.10)
for some constants C > 0, p ≥0 and r ∈(0, 1]. Moreover:
a) If r = 1 then B has Lebesgue measure 0.
b) If r < 1 then B satisfies
for any positive definite d × d matrix C and any
N(0, C)–random vector U the distance d(U, B)
from U to B has a density ψC on R+, such that
supx∈R+,∥C∥+∥C−1∥≤A ψC(x) < ∞for all A < ∞,







(2.11)
and we have
x ∈Bc, ∥y∥≤1
$ d(x, B)
2
⇒



∥∇f(x)∥≤C(1+∥x∥p)
d(x,B)1−r ,
∥∇f(x + y) −∇f(x)∥≤C(1+∥x∥p)∥y∥
d(x,B)2−r
.
(2.12)
The additional requirements when r < 1 above are not “optimal”, but
they accomodate the case where f equals fj,r, as defined in (2.2): this function
satisfies (K) when r > 1, and (K’) when r ∈(0, 1] (with the same r of course).
When B is a finite union of hyperplanes it satisfies (2.11). Also, observe that
(K) implies (K’) with r = 1 and B = ∅. For the concept of “stable convergence
in law”, introduced by Renyi in [11], we refer to [9] for example; it is a kind
of convergence which is a bit stronger than the ordinary convergence in law.
Theorem 2.3. Under (H1) (or (H0)) and either one the following assump-
tions:
(i) all components of g and h satisfy (K),
(ii) (H’) holds, and all components of g and h satisfy (K’),
the processes √n (Xn(g, h) −X(g, h)) converge stably in law towards the lim-
iting process U(g, h) given componentwise by
U(g, h)jk
t
=
d1

j′=1
d3

k′=1
 t
0
α(σs, g, h)jk,j′k′ dW ′j′k′
s
(2.13)

40
O. E. Barndorff–Nielsen et al.
where
d1
l=1
d3
m=1 α(Σ, g, h)jk,lmα(Σ, g, h)j′k′,lm = A(Σ, g, h)jk,j′k′
and
A(Σ, g, h)jk,j′k′ = d2
l,l′=1

ρΣ(gjlgj′l′)ρΣ(hlkhl′k′)
+ρΣ(gjl)ρΣ(hl′k′)ρΣ(gj′l′hlk) + ρΣ(gj′l′)ρΣ(hlk)ρΣ(gjlhl′k′)
−3ρΣ(gjl)ρΣ(gj′l′)ρΣ(hlk)ρΣ(hl′k′)

,

















(2.14)
and W ′ is a d1d3–dimensional Wiener process which is defined on an extension
of the space (Ω, F, (Ft)t≥0, P) and is independent of the σ–field F.
The first formula in (2.14) means that α is a square–root of the d1d3×d1d3–
matrix A, which is symmetric semi–definite positive. Observe that the right
sides of (2.4) and (2.13) always make sense, due to the fact that t →σt is
c`adl`ag and thus with all powers locally integrable w.r.t. Lebesgue measure.
Under (H) and if both g and h are even and continuous, the processes
U n(f, g)t =
1
√n
[nt]

i=1

g(√n ∆n
i Y )h(√n ∆n
i+1Y )
−E(g(√n ∆n
i Y )h(√n ∆n
i+1Y )|F i−1
n )

(2.15)
still converge stably in law to U(g, h) provided a and σ have some integra-
bility properties in connection with the growth rate of g and h (so that the
conditional expectations above are meaningful): see Theorem 5.6 below for a
version of this when a and σ are bounded. But such a CLT is probably of
little practical use.
Remarks: For simplicity we state the remarks when all processes are 1–
dimensional and when h(x) = 1.
1. When g is not even we still have a limiting process which is the process
U(g, 1) plus a process which has a drift and an integral term w.r.t. W:
for example if g(x) = x, then X(g, 1) = 0 and of course √n Xn(g, h)t =
Y[nt]/n, so the limit is Y itself (in this case U(g, 1) = 0). For more details,
see [8].
2. In view of the result on (2.15), when h = 1 the CLT is essentially equiva-
lent to the convergence of
1
√n
[nt]

i=1
	
E(g(√n ∆n
i Y )|F i−1
n ) −n

i
n
i−1
n
ρσu(g)du

to 0 (locally uniform in t). This in turn is implied by the convergence to
0 of the following two processes:

CLT for bipower variations
41
1
√n
[nt]

i=1

E(g(√n ∆n
i Y )|F i−1
n ) −E(g(√n σ i−1
n ∆n
i W)|F i−1
n )

,
(2.16)
1
√n
[nt]

i=1
	
ρσ i−1
n (g) −n

i
n
i−1
n
ρσu(g)du

.
(2.17)
3. For (2.17) we need some smoothness of σ: e.g. u →σu is H¨older with
some index > 1/2. Hypothesis (H1) is of this kind (although σ can have
jumps, (2.8) sort of implies that it is ”H¨older” of order 1/2 and further
some compensation arises).
4. The differentiability of g is in fact used for the convergence of (2.16).
Another natural idea would be to compare the transition densities of Y
and W for small times, provided of course the former ones exist: that
allows to get the results for functions g and h which are only Borel–
measurable, in Theorem 2.3 and in Theorem 2.1 as well, but it necessitates
quite stringent assumptions on Y (like a Markov structure, and non–
degeneracy).
2.3 Applications to bipower variations
Let us now explain how the general CLT above writes for bipower variations.
The most general form is given below, but for simplicity we first consider the
1–dimensional case for Y , with a single bipower process.
Theorem 2.4. Let r, s ≥0 and assume that d = d′ = 1. Assume (H1)
and also that either r, s ∈{0} ∪(1, ∞) or (H’) holds. Then the processes
(√n (V (Y ; r, s)n −V (Y ; r, s))) converge stably in law to a process U(r, s) of
the form
U(r, s)t =

µ2rµ2s + 2µrµsµr+s −3µ2rµ2s
 t
0
|σu|r+s dW ′
u,
(2.18)
where W ′ is a Wiener process which is defined on an extension of the space
(Ω, F, (Ft)t≥0, P) and is independent of the σ–field F.
For the general case we consider simultaneously all cross–bipower varia-
tions for any finite family of indices. We need some more notation: we de-
note by µ(Σ; r, s; j, k) the expected value of |Uj|r|Uk|s when U = (Uj)1≤j≤d
is an N(0, ΣΣ∗)–distributed random variable, and also by µ(Σ; r; j) the ex-
pected value of |Uj|r (so µ(Σ; r; j) = µ(Σ; r, 0; j, k) for any k, and µ(Σ; r; j) =
|Cjj|r/2µr, where C = ΣΣ∗).
Theorem 2.5. Let (rl, sl) be a family of nonnegative reals. Under (H1) and
either one of the following assumptions:
(i) rl, sl ∈{0} ∪(1, ∞),

42
O. E. Barndorff–Nielsen et al.
(ii) (H’) and rl, sl ∈[0, ∞),
the L × d × d–dimensional processes
(√n (V (Y j, Y k; rl, sl)n −V (Y j, Y k; rl, sl)) : 1 ≤l ≤L, 1 ≤j, k ≤d)
converge stably in law to a process (U(rl, sl, j, k) : 1 ≤l ≤L, 1 ≤j, k ≤d)
having the form
U(rl, sl, j, k)t =
L

l′=1
d

j′=1
d

k′=1
 t
0
α(σu)ljk,l′j′k′ dW ′l′j′k′
u
,
(2.19)
where
L
l′′=1
d
j′′=1
d
k′′=1 α(Σ)ljk,l′′j′′k′′α(Σ)l′j′k′,l′′j′′k′′ = Aljk,l′j′k
and
A(Σ)ljk,l′j′k′ = µ(Σ; rl, rl′; j, j′)µ(Σ; sl, sl′; k, k′)
+µ(Σ; rl; j)µ(Σ; sl′; k′)µ(Σ; rl′, sl; j′, k)
+µ(Σ; rl′; j′)µ(Σ; sl; k)µ(Σ; rl, sl′; j, k′)
−3µ(Σ; rl; j)µ(Σ; rl′; j′)µ(Σ; sl; k)µ(Σ; sl′; k′)





















(2.20)
and where W ′ is an L × d × d–dimensional Wiener process which is defined
on an extension of (Ω, F, (Ft)t≥0, P) and is independent of the σ–field F.
This result readily follows from Theorem 2.3, upon taking d1 = Ld, d2 = L,
d3 = d, g(x)lj,l′ = |xj|rlεll′ (εll′ is the Kronecker symbol) and h(x)l,j = |xj|sl.
Apart from Theorem 2.4, several particular cases are worth being mentioned
(recall that c = σσ∗):
1. If j = k then √n (V (Y j; r, s)n −V (Y j; r, s)) stably converges to

µ2rµ2s + 2µrµsµr+s −3µ2rµ2s
 t
0
|cjj
u |
r+s
2
dW ′
u.
This is also, of course, a consequence of Theorem 2.4.
2. The bivariate processes with components √n (V (Y j; r, 0)n −V (Y j; r, 0))
and √n (V (Y k; 0, s)n −V (Y k; 0, s)) stably converge to a continuous mar-
tingale with (matrix–valued) bracket C given by
C11
t
= (µ2r −µ2
r)
 t
0 |cjj
u |r du
C12
t
=
 t
0(µ(σu; r, s; j, k) −µrµs|cjj
u |r/2|ckk
u |s/2) du
C22
t
= (µ2s −µ2
s)
 t
0 |cjj
u |s du









.
(2.21)
The same is true for the processes with components √n (V (Y j; r, 0)n −
V (Y j; r, 0)) and √n (V (Y k; s, 0)n −V (Y k; s, 0)). When j = k we get
C12
t
= (µr+s −µrµs)
 t
0 |cjj
u |
r+s
2
du.

CLT for bipower variations
43
Finally we state the multipower variation result, in the 1–dimensional case
only for simplicity. We consider the processes of (1.4) and (2.6), which are
written V (Y ; r1, . . . , rN)n and V (Y ; r1, . . . , rN) here. For any choice of rl ≥0,
and under (H1) and also under (H’) if any of the rl is in the set (0, 1], the
processes √n (V (Y ; r1, . . . , rN)n −V (Y ; r1, . . . , rN)) converge stably towards
a limiting process of the form
U(r1, . . . , rN)t =
√
A
 t
0
|σu|r1+...+rN dW ′
u,
where W ′ is a Wiener process independent of the σ–field F, and where
A =
N
(
l=1
µ2rl −(2N −1)
N
(
l=1
µ2
rl + 2
N−1

k=1
k
(
l=1
µrl
N
(
l=N−k+1
µrl
N−k
(
l=1
µrl+rl+k.
2.4 Outline of the proof
The remainder of this paper is devoted to proving Theorems 2.1 and 2.3:
1. In Section 3 we replace the ”local” assumptions (H), (H1) and (H’) by
”global” ones called (SH), (SH1) and (SH’): these stronger assumptions
are likely to be satisfied in many practical applications, and the ”local-
ization techniques” using stopping times are standard: so the reader can
very well skip most of that section and read only the assumptions and
(3.6).
2. The idea of the proof is simple enough. First, replace the increments ∆n
i Y
of the process (2.3) by σ(i−1)/n∆n
i W: then the CLT is a simple conse-
quence of the convergence of triangular arrays of martingale differences,
and the convergence in probability follows from the CLT: this is basi-
cally the content of Section 4. In Section 5 we prove the CLT for the
processes of (2.15): this easily follows from Section 4. Hence proving The-
orems 2.1 and 2.3 amounts to control of the differences Xn(g, h)−U n(g, h)
or √n (Xn(g, h)−U n(g, h)): for Theorem 2.1 this is simple, see Section 6.
For Theorem 2.3 it is done in Section 8: we have to split the above differ-
ences into a large number of terms, which are estimated separately. So we
gather the necessary (very cumbersome) notation and technical estimates
in Section 7.
3 Some stronger assumptions
Under (H) we have a sequence Tk of stopping times increasing to +∞and
constants Ck such that
s ≤Tk
=⇒
|as| + |σs−| ≤Ck.

44
O. E. Barndorff–Nielsen et al.
Set a(k)
s
= as∧Tk, and σ(k)
s
= σs if s < Tk and σ(k)
s
= σTk−if s ≥Tk. We
associate Y (k) with a(k) and σ(k) by (2.3), and Xn,(k)(g, h) with Y (k) by (2.1),
and similarly X(k)(g, h) and U (k)(g, h) with σ(k) by (2.4) and (2.13) (and the
same process W ′ for all k).
Suppose that we have proved Theorem 2.1 for Xn,(k)(g, h), for each k.
Observing that Xn,(k)(g, h)t = Xn(g, h)t and X(k)(g, h)t = X(g, h)t and
U (k)(g, h)t = U(g, h)t for all t < Tk, and since Tk increases to ∞as k →∞, it
is obvious that the result of Theorem 2.1 also holds for Xn(g, h). So, instead
of (H), it is no restriction for proving Theorem 2.1 to assume the following
stronger hypothesis:
Hypothesis (SH): We have (H), and further the processes a and σ are
bounded by a constant.
Now we proceed to strenghten (H1) in a similar manner. Assume (H1) and
recall the sequence (Sk) in (2.9): it is no restriction to assume in addition that
Sk ≤k. Set for k, l ≥1:
Ek,l = {x ∈E : ψk(x) > l},
Rk,l = inf(t : µ((0, t] × Ek,l) ≥1).
Then we have
P(Rk,l ≤Sk) ≤E(µ((0, Sk] × Ek,l)) = F(Ek,l) E(Sk) ≤k F(Ek,l).
In view of (2.9) we have liml→∞F(Ek,l) = 0. Hence we find lk such that
P(Rk,lk < Sk) ≤2−k, and obviously the sequence of stopping times S′
k =
Sk ∧Rk,lk has supk S′
k = ∞a.s.
Next, just as above, we find a sequence S′′
k of stopping times increasing to
+∞and constants Ck such that
s ≤S′′
k
=⇒
∥as∥+ ∥σs−∥+ ∥a′
s∥+ ∥σ′
s−∥+ ∥vs−∥≤Ck.
Then if Tk = S′
k ∧S′′
k, we still have supk Tk = ∞a.s., and further
s ≤Tk
=⇒
∥as∥+ ∥σs−∥+ ∥a′
s∥+ ∥σ′
s−∥+ ∥vs−∥≤Ck,
µ((0, Tk) × Ek,lk) = 0.

.
(3.1)
Set
a′(k)
s
=
a′
s if s ≤Tk
0 if s > Tk
(a(k)
s , σ′(k)
s
, v(k)
s , w(k)(s, x)) =
(as, σ′
s, vs, w(s, x)) if s < Tk
(0, 0, 0, 0)
if s ≥Tk,
µ(k)(ds, dx) = µ(ds, dx) 1Ec
k,lk (x),

CLT for bipower variations
45
ν(k)(ds, dx) = ds ⊗Fk(dx),
where Fk(dx) = F(dx) 1Ec
k,lk (x).
Then µ(k) is a new Poisson measure, still independent of W and V , with
compensator ν(k), and ψk is square–integrable w.r.t. Fk. We then put
σ(k)
t
= σ0 +
 t
0
a′(k)
s
ds +
 t
0
σ′(k)
s−dWs +
 t
0
v(k)
s−dVs
+
 t
0

E
ϕ ◦w(k)(s−, x)(µ(k) −ν(k))(ds, dx)
+
 t
0

E
(w(k) −ϕ ◦w(k))(s−, x)µ(k)(ds, dx)
(3.2)
= σ0 +
 t
0
(a′(k)
s
+ α(k)
s )ds +
 t
0
σ′(k)
s−dWs +
 t
0
v(k)
s−dVs
+
 t
0

E
w(k)(s−, x)(µ(k) −ν(k))(ds, dx),
(3.3)
provided α(k)
s
=

E(w(k)−ϕ◦w(k))(s−, x)Fk(dx). Then σ(k)
s
= σs when s < Tk
and ∥α(k)
s ∥≤C′
k for all s, for some constant C′
k.
We associate Y (k) with a(k) and σ(k) by (2.3), and Xn,(k)(g, h) with Y (k)
by (2.1), and similarly X(k)(g, h) and U (k)(g, h) with σ(k) by (2.4) and (2.13)
(and the same process W ′ for all k). We clearly have Xn,(k)(g, h)t = Xn(g, h)t
and X(k)(g, h)t = X(g, h)t and U (k)(g, h)t = U(g, h)t for all t < Tk.
Hence, exactly as for (H), for proving Theorem 2.3 it is no restriction to
replace (H1) by the following stronger assumption (recall (3.3)):
Hypothesis (SH1): We have (SH) with
σt = σ0 +
 t
0
a′
sds +
 t
0
σ′
s−dWs +
 t
0
vs−dVs +
 t
0

E
w(s−, x)(µ −ν)(ds, dx)
(3.4)
with V , µ and ν as in (H1), and a′, σ′, v and a are like in (H0) and uniformly
bounded. Finally w is like in (H1), with further
sup
ω∈Ω,s≥0
∥w(ω, s, x)∥≤ψ(x),
where

E
ψ(x)2 F(dx) < ∞,
ψ(x) ≤C.
(3.5)
In a similar way, under (H’) we find a sequence Tk of stopping times
satisfying (3.1) and also ∥(σsσ⋆
s)−1∥≤Ck if s < Tk. So the same argument as
above allows to replace (H’) in Theorem 2.3 by
Hypothesis (SH’): We have (H’) and further the process (σσ⋆)−1 is
bounded.
Finally, let us denote by M′ the closure of the set {σu(ω) : ω ∈Ω, u ≥0}
in Md,d′. Then there is a constant A0 such that:

46
O. E. Barndorff–Nielsen et al.
under (SH) we have
Σ ∈M′
⇒
∥Σ∥≤A0
under (SH’) we have
Σ ∈M′
⇒
∥(ΣΣ⋆)−1∥≤A0.

(3.6)
In view of the previous results, we can and will assume in the sequel either
(SH), or (SH1), and sometimes (SH’).
Let us also fix some conventions. We write V n
P
−→V for a sequence (V n)
of processes and a continuous process V when sups≤t ∥V n
s −Vs∥goes to 0
in probability for all t > 0. When V n takes the form V n
t
= [nt]
i=1 ζn
i for an
array of variables (ζn
i ), and when V n
P
−→0, we say that this array is AN, for
Asymptotically Negligible.
The constants occuring here and there may depend on the constants in
(SH) or (SH1) and on the functions g and h and are all denoted by C and
change from line to line; if they depend on another external parameter p, we
write them Cp.
4 A first simplified problem
In this section we prove the CLT in a slightly different setting: in some sense,
we pretend that at stage n, σ is constant over the interval [(i −1)/n, i/n).
More precisely, we introduce the following Rd–valued random variables:
βn
i = √n σ i−1
n ∆n
i W,
β′n
i
= √n σ i−1
n ∆n
i+1W,
(4.1)
and we write ρn
i
= ρσi/n. To begin with, we consider an Md1,d2–valued
adapted c`adl`ag and bounded process δ and an Md2,d3–valued function f on
Rd. Then we introduce the Md1,d3–valued process (recall (4.1)):
U n
t =
1
√n
[nt]

i=1
δ i−1
n

f(βn
i ) −ρn
i−1(f)

.
(4.2)
In a similar way, for g and h like in (2.1), we set
U ′n
t
=
1
√n
[nt]

i=1

g(βn
i )h(β′n
i ) −ρn
i−1(g)ρn
i−1(h)

.
(4.3)
Our aim in this section is then to prove the following two CLT’s:
Proposition 4.1 Under (SH), if f is at most of polynomial growth, the se-
quence of processes U n in (4.2) is C-tight. If further f is even, then it con-
verges stably in law to the process U defined componentwise by

CLT for bipower variations
47
U jk
t
=
d1

j′=1
d3

k′=1
 t
0
δ′jk,j′k′
u
dW ′j′k′
u
,
(4.4)
where
d1

l=1
d3

m=1
δ′jk,lm
u
δ′j′k′,lm
u
=
d2

l,l′=1

ρσu(f lkf l′k′) −ρσu(f lk)ρσu(f l′k′)

δjl
u δj′l′
u ,
(4.5)
and W ′ is a d1d3–dimensional Wiener process defined on an extension of
(Ω, F, (Ft)t≥0, P) and which is independent of the σ–field F.
Proposition 4.2 Under (SH) and if g and h are continuous with at most
polynomial growth, the sequence of processes U ′n is C-tight. If further g and
h are even, then it converges stably in law to the process U(g, h) described in
(2.13).
Before proceeding to the proofs, let us mention the following estimates,
which are obvious under (SH):
E(∥βn
i ∥q) + E(∥β′n
i ∥q) ≤Cq.
(4.6)
Next, saying that f is of at most polynomial growth means that for some
constants C > 0 and p (we can always choose p ≥2),
x ∈Rd
⇒
|f(x)| ≤C(1 + ∥x∥p).
(4.7)
Observe also that Propositions 4.1 and 4.2 imply respectively
1
n
[nt]

i=1
δ i−1
n
f(βn
i )
P
−→
 t
0
δu ρσu(f) du,
(4.8)
1
n
[nt]

i=1
g(βn
i )h(β′n
i )
P
−→
 t
0
ρσu(g)ρσu(h) du.
(4.9)
Proof of Proposition 4.1. We have U n
t
=
[nt]
i=1 ζn
i , where ζn
i
=
δ i−1
n (f(βn
i ) −ρn
i−1(f))/√n. Recalling (4.6) and (4.7), we trivially have
E(ζn
i |F i−1
n ) = 0,
E(∥ζn
i ∥4|F i−1
n ) ≤C
n2 ,
(4.10)
E(ζn,jk
i
ζn,j′k′
i
|F i−1
n ) = 1
n ∆jk,j′k′
i−1
n
,
where ∆jk,j′k′
u
is the right side of (4.5). Moreover since σ is c`adl`ag we deduce
from (4.7) that s →ρσs(f) also is c`adl`ag. Thus by the Riemann integrability
we get

48
O. E. Barndorff–Nielsen et al.
[nt]

i=1
E(ζn,jk
i
ζn,j′k′
i
|F i−1
n ) →
 t
0
∆jk,j′k′
u
du.
(4.11)
Then (4.10) and (4.11) are enough to imply the tightness of the sequence
(U n).
Now, assume further that f is even. Since the variables ∆n
i W and −∆n
i W
have the same law, conditionally on F(i−1)/n, we get
E(ζn,jk
i
∆n
i W l|F i−1
n ) =
d2

m=1
δjm
i−1
n E(∆n
i W l f(√n σ i−1
n ∆n
i W)mk|F i−1
n ) = 0.
(4.12)
Next, let N be any bounded martingale on (Ω, F, (Ft)t≥0, P), which is orthog-
onal to W. For j and k fixed, we consider the martingale Mt = E(g(βn
i )jk|Ft),
for t ≥i−1
n . Since W is an (Ft)–Brownian motion, and since βn
i is a function
of σ(i−1)/n and of ∆n
i W, we see that (Mt)t≥(i−1)/n is also, conditionally on
F(i−1)/n, a martingale w.r.t. the filtration which is generated by the process
Wt −W i−1
n . By the martingale representation theorem the process M is thus
of the form Mt = M i−1
n +
 t
i−1
n ηsdWs for an appropriate predictable process η.
It follows that M is orthogonal to the process N ′
t = Nt −N i−1
n
(for t ≥i−1
n ),
or in other words the product MN ′ is an (Ft)t≥i−1
n –martingale. Hence
E(∆n
i N g(√n σ i−1
n ∆n
i W)jk|F i−1
n ) = E(∆n
i N ′Mi/n|F i−1
n )
= E(∆n
i N ′∆n
i M|F i−1
n ) = 0,
and thus
E(ζn
i ∆n
i N|F i−1
n ) = 0.
(4.13)
If we put together (4.10), (4.11), (4.12) and (4.13), we deduce the result
from Theorem IX.7.28 of [9].
⊓⊔
Proof of Proposition 4.2. A simple computation shows that U ′n
t
=
[nt]+1
i=2
ζn
i + γn
1 −γn
[nt]+1, where
ζn
i =
1
√n

g(βn
i−1)(h(β′n
i−1) −ρn
i−2(h)) + (g(βn
i ) −ρn
i−1(g))ρn
i−1(h)

,
γn
i =
1
√n (g(βn
i ) −ρn
i−1(g)) ρn
i−1(h).
We trivially have (4.10), while (4.12) and (4.13) (for any bounded martin-
gale N orthogonal to W) are proved exactly as in the previous proposition. We
will write ρn
i−2,i−1(g, h) =

g(σ i−1
n x)h(σ i−2
n x)ρ(dx), where ρ is the N(0, Id′)
law. An easy computation shows that

CLT for bipower variations
49
E(ζn,jk
i
ζn,j′k′
i
|F i−1
n )
= 1
n
d2

l,l′=1
)
g(βn
i−1)jlg(βn
i−1)j′l′ 
ρn
i−2(hlkhl′k′) −ρn
i−2(hlk)ρn
i−2(hl′k′)

+g(βn
i−1)jl ρn
i−1(hl′k′)

ρn
i−2,i−1(gj′l′, hlk) −ρn
i−2(hlk)ρn
i−1(gj′l′)

+g(βn
i−1)j′l′ ρn
i−1(hlk)

ρn
i−2,i−1(gjl, hl′k′) −ρn
i−2(hl′k′)ρn
i−1(gjl)

+ρn
i−1(hl′k′)ρn
i−1(hlk)

ρn
i−1(gjlgj′l′) −ρn
i−1(gjl)ρn
i−1(gj′l′)
 
.
and thus by (4.8) and since the components of g and h satisfy (4.7) and are
continuous and σ is c`adl`ag (hence in particular ρn
i−2,i−1(g, h) −ρn
i−2(gh) goes
to 0, uniformly in i ≤[nt] + 1), we get with the notation (2.14):
[nt]+1

i=2
E(ζn,jk
i
ζn,j′k′
i
|F i−1
n ) →
 t
0
A(σu, g, h)jk,k′j′ du.
Then exactly as in the previous proof we deduce that the processes [nt]
i=1 ζn
i
are C–tight, and that they converge stably in law to the process U(g, h) of
(2.13) when further g and h are even.
On the other hand γn
i is the transpose of the jump at time i/n of the
process U n of (4.2) when δu = ρσu(h∗) and f = g∗, so Proposition 4.1 yields
supi≤[nt] ∥γn
i ∥
P
−→0 for any t: hence the results.
⊓⊔
5 A second simplified problem
So far Y has played no role, but it will come in this section. Recalling (4.1),
we set
ξn
i = √n ∆n
i Y −βn
i ,
ξ′n
i
= √n ∆n
i+1Y −β′n
i .
(5.1)
Observe that
ξn
i = √n
	
i
n
i−1
n
audu +

i
n
i−1
n
(σu−−σ i−1
n )dWu

,
and a similar equality for ξ′n
i , with the integrals between i/n and (i + 1)/n.
Then under (SH) we have for any q ∈[2, ∞), by Burkholder Inequality:
E(∥√n ∆n
i Y ∥q) + E(∥ξn
i ∥q) + E(∥ξ′n
i ∥q) ≤Cq.
(5.2)
We can now consider the processes U n(g, h) of (2.15): in view of (5.2), the
conditional expectations in (2.15) are finite as soon as g and h have polynomial
growth.

50
O. E. Barndorff–Nielsen et al.
Theorem 5.6. Under (SH) and if g and h are continuous with at most poly-
nomial growth, the sequence of processes U n(g, h) of (2.15) is C–tight. If fur-
ther g and h are even, it converges stably in law to the processes U(g, h) of
(2.13).
We first prove three lemmas. The first one is very simple:
Lemma 5.1. Let (ζn
i ) be an array of random variables satisfying for all t:
[nt]

i=1
E(∥ζn
i ∥2 | F i−1
n )
P
−→0.
(5.3)
If further each ζn
i is F(i+1)/n–measurable, the array (ζn
i −E(ζn
i | F(i−1)/n))
is AN.
Proof. Of course the result is well known when ζn
i is Fi/n–measurable. Oth-
erwise, we set ηn
i = E(ζn
i | Fi/n). This new array satisfies also (5.3) and now
ηn
i is Fi/n–measurable: so the array (ηn
i −E(ηn
i | F(i−1)/n)) is AN.
Next, (5.3) and Lenglart’s inequality (see e.g. I-3.30 in [9]) yield
[nt]
i=1 E(∥ζn
i ∥2 | Fi/n)
P
−→0, so the afore mentioned well known result also
yields that the array (ζn
i −ηn
i ) is AN, and the result follows.
⊓⊔
Lemma 5.2. Under (SH) we have for all t > 0:
1
n
[nt]

i=1
E

∥ξn
i ∥2 + ∥βn
i+1 −β′n
i ∥2
→0.
(5.4)
Proof. First, the boundedness of a yields
E(∥ξn
i ∥2) ≤C
	
1
n + nE
	
i
n
i−1
n
∥σu−−σ i−1
n ∥2du


.
We also trivially have
E(∥βn
i+1 −β′n
i ∥2) ≤CE(∥σ i
n −σ i−1
n ∥2)
≤CnE
	
i
n
i−1
n

∥σu−−σ i−1
n ∥2 + ∥σu−−σ i
n ∥2
du

.
Hence the left side of (5.4) is smaller than
C
 t
n +
 t
0
E

∥σu−−σ[nu]/n∥2 + ∥σu−−σ([nu]+1)/n∥2
du

.
Since σ is c`adl`ag, the expectation above goes to 0 for all u except the fixed
times of discontinuity of the process σ, that is for almost all u, and it stays

CLT for bipower variations
51
bounded by a constant because of (SH): hence the result by Lebesgue’s theo-
rem.
⊓⊔
For further reference, the third lemma is stated in a more general setting:
• f and k are functions on Rd satisfying (4.7);
• γn
i , γ′n
i , γ′′n
i
are Rd–valued variables,
• Zn
i = 1 + ∥γn
i ∥+ ∥γ′n
i ∥+ ∥γ′′n
i ∥satisfies E((Zn
i )p) ≤Cp.







(5.5)
Lemma 5.3. Under (5.5) and if further k is continuous and
1
n
[nt]

i=1
E(∥γ′n
i −γ′′n
i ∥2) →0,
(5.6)
then we have for all t > 0:
1
n
[nt]

i=1
E

f(γn
i )2(k(γ′n
i ) −k(γ′′n
i ))2
→0.
(5.7)
Proof. Set θn
i = (f(γn
i )(k(γ′n
i ) −k(γ′′n
i )))2 and mA(ε) = sup(|k(x) −k(y)| :
∥x −y∥≤ε, ∥x∥≤A). For all ε ∈(0, 1] and A > 1 we have
θn
i ≤C

A2pmA(ε)2 + A4p1{∥γ′n
i −γ′′n
i
∥>ε}
+(Zn
i )4p(1{∥γn
i ∥>A} + 1{∥γ′n
i ∥>A} + 1{∥γ′′n
i
∥>A})

≤C

A2pmA(ε)2 + A4p∥γ′n
i −γ′′n
i ∥2
ε2
+ (Zn
i )4p+1
A

.
Then in view of (5.5) we get
1
n
[nt]

i=1
E(θn
i ) ≤C

A2pmA(ε)2 + 1
A + A4p
nε2
[nt]

i=1
E(∥γ′n
i −γ′′n
i ∥2)

.
This holds for all ε ∈(0, 1] and A > 1. Since mA(ε) →0 as ε →0, for every
A, (5.7) readily follows from (5.6).
⊓⊔
Proof of Theorem 5.6. In view of Proposition 4.2, it is clearly enough to
prove that U n(g, h) −U ′n
P
−→0. Set
ζn
i =
1
√n

g(√n∆n
i Y )h(√n ∆n
i+1Y ) −g(βn
i )h(β′n
i )

(5.8)
and observe that U n(g, h)t −U ′n
t
= [nt]
i=1

ζn
i −E(ζn
i | F(i−1)/n)

and that
ζn
i is F(i+1)/n-measurable. Then by Lemma 5.1 it suffices to prove that

52
O. E. Barndorff–Nielsen et al.
[nt]

i=1
E(∥ζn
i ∥2) →0.
(5.9)
For proving (5.9) it is clearly enough to consider the case where both g
and h are 1–dimensional. Recalling √n ∆n
i Y = βn
i + ξn
i , we then have
∥ζn
i ∥2 ≤C
n

h(√n ∆n
i+1Y )2 (g(βn
i + ξn
i ) −g(βn
i ))2
+g(βn
i )2 (h(βn
i+1 + ξn
i+1) −h(βn
i+1))2 + g(βn
i )2(h(βn
i+1) −h(β′n
i ))2
.
Then (5.9) immediately follows from (4.6) and (5.2) and from Lemmas 5.2
and 5.3.
⊓⊔
6 The proof of Theorem 2.1
As stated in Section 2, we can and will assume (SH). We use the notation ζn
i
of (5.8), and set
ηn
i = E

g(√n ∆n
i Y )h(√n ∆n
i+1Y ) | F i−1
n

,
η′n
i
= ρn
i−1(g)ρn
i−1(h)
and V n
t
=
[nt]
i=1ηn
i
and V ′n
t
=
[nt]
i=1η′n
i . Theorem 5.6 implies that
1
n(Xn(g, h) −V n)
P
−→0, and Riemann integrability yields 1
n V ′n →X(g, h)
pointwise in ω and locally uniformly in time. So we need to prove that
1
n(V n −V ′n)
P
−→0. Since ηn
i −η′n
i
= √n E(ζn
i | F(i−1)/n), it clearly suf-
fices to prove that
1
√n
[nt]

i=1
E(∥ζn
i ∥) →0.
(6.1)
By the Cauchy–Schwarz inequality, the left side of (6.1) is smaller than

t [nt]
i=1 E(∥ζn
i ∥2)
1/2
and thus (6.1) follows from (5.9).
⊓⊔
7 Technical preliminaries for Theorem 2.3
As said before, for proving Theorem 2.3 we can and will assume (SH), and also
(SH’) when at least one of the components of g or h satisfies (K’) instead of
(K). In fact, this theorem is deduced from Theorem 5.6, provided we can show
that √n (Xn(g, h)t −U n(g, h)t) goes to 0 in probability, locally uniformly in
t. This amounts to proving that the array
ζn
i =
1
√n E

g(√n ∆n
i Y )h(√n ∆n
i+1Y ) | F i−1
n

−√n

i
n
i−1
n
ρσu(g)ρσu(h)du

CLT for bipower variations
53
is AN. Obviously, we can work componentwise, and so we will assume w.l.o.g.
that both g and h are 1–dimensional (they still are functions on Rd, though).
We have ζn
i = ζ′n
i + ζ′′n
i , where
ζ′n
i
=
1
√n

E

g(√n ∆n
i Y )h(√n ∆n
i+1Y ) | F i−1
n

−E

g(βn
i ) | F i−1
n ) E

h(β′n
i ) | F i−1
n

, (7.1)
ζ′′n
i
= √n

i
n
i−1
n

ρσu(g)ρσu(h) −ρn
i−1(g)ρn
i−1(h)

du.
(7.2)
So we are left to prove that both arrays (ζ′n
i ) and (ζ′′n
i ) are AN. For the second
one this is relatively simple, but for the first one it is quite complicated, and
we need to split the difference in (7.1) into a large number of terms, which are
treated in different ways: this section is devoted to estimates for these various
terms.
7.1 Some notation
First, we fix a sequence of numbers εn ∈(0, 1] (which will be chosen later in
such a way that ε2
nn ≥1), and we set En = {x ∈E : ψ(x) > εn}. Then,
recalling the product–matrix notation, under (SH1) we can introduce a (long)
series of Rd–valued random variables:
ζ(1)n
i = √n

i
n
i−1
n
(au −a i−1
n )du + √n

i
n
i−1
n
	 u
i−1
n
a′
sds
+
 u
i−1
n
(σ′
s−−σ′
i−1
n )dWs +
 u
i−1
n
(vs−−v i−1
n )dVs

dWu,
ζ(1)′n
i = √n
	
i
n
i−1
n
a′
sds +

i
n
i−1
n

σ′
s−−σ′
i−1
n

dWs
+

i
n
i−1
n
(vs−−v i−1
n )dVs

∆n
i+1W,
ζ(2)n
i = √n
	
1
n a i−1
n + σ′
i−1
n

i
n
i−1
n
(Wu −W i−1
n )dWu
+v i−1
n

i
n
i−1
n
(Vu−−V i−1
n )dWu

,
ζ(2)′n
i = √n

σ′
i−1
n ∆n
i W + v i−1
n ∆n
i V

∆n
i+1W,
ζ(3)n
i = √n

i
n
i−1
n
	 u
i−1
n

Ec
n
w(s−, x)(µ −ν)(ds, dx)

dWu,

54
O. E. Barndorff–Nielsen et al.
ζ(3)′n
i = √n
	
i
n
i−1
n

Ec
n
w(s−, x)(µ −ν)(ds, dx)

∆n
i+1W,
ζ(4)n
i = −√n

i
n
i−1
n
	 u
i−1
n

En

w(s−, x) −w
i −1
n
, x

ν(ds, dx)

dWu,
ζ(4)′n
i = −√n
	
i
n
i−1
n

En

w(s−, x) −w
i −1
n
, x

ν(ds, dx)

∆n
i+1W,
ζ(5)n
i = −√n

i
n
i−1
n
	 u
i−1
n

En
w
i −1
n
, x

ν(ds, dx)

dWu,
ζ(5)′n
i = −√n
	
i
n
i−1
n

En
w
i −1
n
, x

ν(ds, dx)

∆n
i+1W,
ζ(6)n
i = √n

i
n
i−1
n
	 u
i−1
n

En

w(s−, x) −w
i −1
n
, x

µ(ds, dx)

dWu,
ζ(6)′n
i = √n
	
i
n
i−1
n

En

w(s−, x) −w
i −1
n
, x

µ(ds, dx)

∆n
i+1W,
ζ(7)n
i = √n

i
n
i−1
n
	 u
i−1
n

En
w
i −1
n
, x

µ(ds, dx)

dWu,
ζ(7)′n
i = √n
	
i
n
i−1
n

En
w
i −1
n
,

µ(ds, dx)

∆n
i+1W.
We also set
ξn
i = ζ(1)n
i + ζ(3)n
i + ζ(4)n
i + ζ(6)n
i ,
*ξn
i = ζ(2)n
i + ζ(5)n
i + ζ(7)n
i
ξ′′n
i
= ζ(1)′n
i + ζ(3)′n
i + ζ(4)′n
i + ζ(6)′n
i ,
*ξ′′n
i
= ζ(2)′n
i + ζ(5)′n
i + ζ(7)′n
i
ξ′n
i
= ξn
i+1 + ξ′′n
i ,
*ξ′n
i
= *ξn
i+1 + *ξ′′n
i .















(7.3)
In view of (5.1), a tedious but simple computation shows that
√n ∆n
i Y −βn
i = ξn
i = ξn
i + *ξn
i ,
√n ∆n
i+1Y −β′n
i
= ξ′n
i
= ξ′n
i + *ξ′n
i .
(7.4)
Next, we put ϕ(ε) =

{∥ψ(x)∥≤ε} ψ(x)2F(dx), so that
ε ↓0
⇒
ϕ(ε) →0
θ ∈[0, 2]
⇒

{ψ(x)>ε} ψ(x)θF(dx) ≤
C
ε2−θ ,
θ ≥2
⇒

{ψ(x)≤ε} ψ(x)θF(dx) ≤ϕ(ε) εθ−2.







(7.5)

CLT for bipower variations
55
Finally, set
αn,q
i
=
1
nq/2
+E
		
n

i
n
i−1
n

∥au −a i−1
n ∥2 + ∥σ′
u−−σ′
i−1
n ∥2 + ∥vu−−v i−1
n ∥2
+

En
w(u−, x) −w
i −1
n
, x

2
F(dx)

du

q/2
,
(7.6)
7.2 Estimates for ζ(k)n
j and ζ(k)′n
j
Here we estimate moments of the variables ζ(k)n
i and ζ(k)′n
i . A repeated use
of the H¨older and Burkholder inequalities gives us for q ≥2, and under (SH1):
E(∥ζ(1)n
i ∥q) + E(∥ζ(1)′n
i ∥q) ≤Cq αn,q
i
/nq/2,
E(∥ζ(2)n
i ∥q) + E(∥ζ(2)′n
i ∥q) ≤Cq/nq/2.

(7.7)
Lemma 7.4. Under (SH1), and for any even integer q ≥2, we have
E(∥ζ(3)n
i ∥q) + E(∥ζ(3)′n
i ∥q) ≤Cq ϕ(εn) εq−2
n
n .
(7.8)
Proof. Apply the H¨older and Burkholder inequalities repeatedly to get
E(∥ζ(3)n
i ∥q) ≤CqE




n

i
n
i−1
n

 u
i−1
n

Ec
n
w(s, x)(µ −ν)(ds, dx)

2
du


q/2


≤Cq n

i
n
i−1
n
E
	
 u
i−1
n

Ec
n
w(s, x)(µ −ν)(ds, dx)

q
du

≤Cq n

i
n
i−1
n
E


	 u
i−1
n

Ec
n
∥w(s, x)∥2µ(ds, dx)

q/2
du
≤Cq E


	
i
n
i−1
n

Ec
n
ψ(x)2µ(ds, dx)

q/2
:
= E((Zn
i
n −Zn
i−1
n )q/2),
where Zn
t =
 t
0

Ec
n ψ(x)2µ(ds, dx) is an increasing pure jump L´evy process,
whose Laplace transform is
λ →E(e−λ(Zn
s+t−Zn
s )) = exp t

Ec
n

e−λψ(x)2 −1

F(dx).

56
O. E. Barndorff–Nielsen et al.
We compute the q/2–moment of Zn
s+t−Zn
s by differentiating q/2 times the
Laplace transform at 0: this is the sum, over all choices u1, . . . , uk of positive
integers with k
i=1 ui = q/2, of suitable constants times the product for all
i = 1, . . . , k of the terms t

Ec
n ψ(x)2uiF(dx); moreover this term is smaller
than tε2ui−2
n
ϕ(εn). Since further εn ≤1 and ϕ(1) < ∞, we deduce that
E((Zn
s+t −Zn
s )q/2) ≤Cqϕ(εn)
q/2

k=1
tkεq−2k
n
≤Cqϕ(εn)(tεq−2
n
+ tq/2).
We deduce (7.8) for ζ(3)n
i (recall nε2
n ≥1), and the same holds for ζ(3)′n
i .
⊓⊔
Lemma 7.5. Under (SH1), for any q > 2 we have
E(∥ζ(4)n
i ∥q) + E(∥ζ(4)′n
i ∥q) + E(∥ζ(5)n
i ∥q) + E(∥ζ(5)′n
i ∥q) ≤
Cq
εq
n nq .
(7.9)
Proof. Applying the H¨older and Burkholder inequalities and ∥w(s, x)∥≤
ψ(x) yields for j = 4, 5:
E(∥ζ(j)n
i ∥q + ∥ζ(j)′n
i ∥q) ≤
≤CqE




n

i
n
i−1
n
	 u
i−1
n

En
ψ(x)ν(ds, dx)

2
du


q/2


≤Cq
	
i
n
i−1
n
ds

En
ψ(x)F(dx)

q
≤Cq
nq

En
ψ(x)F(dx)
q
. (7.10)
The result readily follows from (7.5).
⊓⊔
For ζ(j)n
i and ζ(j)′n
i
with j = 6, 7 the analogous estimates are not quite
enough for our purposes, and we need a bit more. Below, we consider a pair
(r, B), where r ∈(0, 1] and B is a closed subset of Rd, with Lebesgue measure
0, and such that (2.11) holds when r < 1 and that r = 1 if B = ∅. Let also
r = 1
⇒
γn
i = 1
r < 1
⇒
γn
i = 1 +
1
d(γn
i ,B),
with either γn
i = βn
i or γn
i = β′n
i


(7.11)
Lemma 7.6. Under (SH1) and the previous assumptions, and if further (SH’)
holds whenever r < 1, for any q ∈(1, 2) and l ∈[0, 1) we can find u > 1
(depending on q and l) such that
E

∥ζ(6)n
i ∥q (γn
i )l
+ E

∥ζ(6)′n
i ∥q (γn
i )l
≤
Cl,q (αn,2
i
)1/u
nq/2
,
E

∥ζ(7)n
i ∥q (γn
i )l
+ E

∥ζ(7)′n
i ∥q (γn
i )l
≤Cl,q
nq/2 .



(7.12)

CLT for bipower variations
57
Proof. We set M n
i
= sups∈[(i−1)/n,i/n] ∥Ws −W(i−1)/n∥and wn(s, x) =
w(s−, x) −w( i−1
n , x) for i−1
n
< s ≤i
n, and
Zn
t =
 t
0

En
ψ(x) µ(ds, dx),
Z′n
t
=
 t
0

En
∥wn(s, x)∥µ(ds, dx).
Observe that Zn and Z′n are nondecreasing, piecewise constant, and Z′n
t
−
Z′n
s ≤2(Zn
t −Zn
s ) whenever s < t. Then
∥ζ(6)n
i ∥≤C√n M n
i (Z′n
i
n −Z′n
i−1
n ).
Set u′ = 1
2

1 + 1
l
-
1
q−1

, which satisfies u′ > 1 because l < 1 and q ∈(1, 2).
With δn
i = (√n M n
i )u′q (γn
i )u′l we then have (since u′ > 1 and u′q−u′+1 > 0):
∥ζ(6)n
i ∥q (γn
i )l ≤Cq

δn
i (Zn
i
n −Zn
i−1
n )u′q−u′+1 1
u′ (Z′n
i
n −Z′n
i−1
n )
u′−1
u′ ,
and H¨older’s inequality yields
E

∥ζ(6)n
i ∥q(γn
i )l
≤Cq

E

δn
i (Zn
i
n −Zn
i−1
n )u′q−u′+1 1
u′ 
E(Z′n
i
n −Z′n
i−1
n )
 u′−1
u′ . (7.13)
Now, if we combine (2.11) and (3.6), we see that when r < 1 (so (SH’)
holds) the variable d(γn
i , B) has a conditional law knowing F(i−1)/n which has
a density which is bounded uniformly in n, i and ω, so E((γn
i )s | F(i−1)/n)
is bounded by a constant Cs for all s ∈[0, 1), whether r = 1 or r < 1. Also,
E((√n M n
i )p | F(i−1)/n) ≤Cq for all p > 0. Then by H¨older’s inequality
we get E

δn
i | F(i−1)/n

≤Cq,l. Since further the variable Zn
i/n −Zn
(i−1)/n is
independent of δn
i , conditionally on F i−1
n , we deduce
E

δn
i (Zn
i
n −Zn
i−1
n )u′q−u′+1
≤Cq,l E((Zn
i
n −Zn
i−1
n )u′q−u′+1).
(7.14)
Next, we estimate the moments of Zn and Z′n. Observe that Z′n = A′n +
N ′n, where
A′n
t =
 t
0

En
∥wn(s, x)∥ν(ds, dx),
N ′n =
 t
0

En
∥wn(s, x)∥(µ −ν)(ds, dx).
On the one hand, since F(En) ≤C/ε2
n by (7.5) and nε2
n ≥1,
(A′n
i
n −A′n
i−1
n )2 ≤1
n

i
n
i−1
n
ds

En
∥wn(s, x)∥F(dx)
2
≤1
n

i
n
i−1
n
ds F(En)

En
∥wn(s, x)∥2 F(dx)
≤

i
n
i−1
n
ds

En
∥wn(s, x)∥2 F(dx).

58
O. E. Barndorff–Nielsen et al.
On the other hand N ′n is a square–integrable martingale, and thus
E

(N ′n
i
n −N ′n
i−1
n )2
≤E
	
i
n
i−1
n
ds

En
∥wn(s, x)∥2F(dx)

,
and thus
E

(Z′n
i
n −Z′n
i−1
n )2
≤C αn,2
i
n
.
(7.15)
If we replace ∥wn(s, x)∥by ψ(x), we obtain in a similar fashion
E

(Zn
i
n −Zn
i−1
n )2
≤C
n .
(7.16)
Then if we combine (7.13), (7.14), (7.15) and (7.16), and since u′q−u′+1 ≤2,
we obtain the result for ζ(6)n
i , with u =
2u′
u′−1 > 1, and the proof for ζ(6)′n
i
is
similar. Finally if we replace wn by w (then αn,2
i
is replaced by a constant),
we get the result for ζ(7)n
i and ζ(7)′n
i .
⊓⊔
7.3 Estimates for the variables of (7.3)
Here we derive estimates on the variables defined in (7.3). Below, the pair
(B, r) and the variable γn
i are like in Lemma 7.6. We also consider positive
random variables Zn
i which satisfy
E((Zn
i )q) ≤Cq
∀q ≥2.
(7.17)
Observe that ξn
i and ξ′n
i
do not depend on the sequence εn, but ξn
i and ξ′n
i
do. Remember also the variables αn,q
i
defined ibn (7.6).
Lemma 7.7. Assume (SH1) and (SH’) and (7.11) and (7.17). Let p ≥2 and
l ∈(0, 1). Then if θ ∈(1, 2) we have
E

(Zn
i )p ∥*ξn
i ∥θ (γn
i )l
+ E

(Zn
i )p ∥*ξ′n
i ∥θ (γn
i )l
≤Cp,θ,l
nθ/2 ,
(7.18)
Moreover one can find a sequence εn > 0 with nε2
n ≥1 and a sequence zn > 0
with zn →0, both sequences depending on l only, and also two numbers q, q′ ≥
1 depending on l only, such that
E((Zn
i )p∥ξn
i ∥(γn
i )l) ≤Cp,l
√n

zn + (αn,q
i
)1/q + (αn,2
i
)1/q′
,
E((Zn
i )p∥ξ′n
i ∥(γn
i )l)) ≤Cp,l
√n

zn + (αn,q
i
)1/q + (αn,q
i+1)1/q
+(αn,2
i
)1/q′ + (αn,2
i+1)1/q′
.











(7.19)

CLT for bipower variations
59
Proof. We prove (7.18) and (7.19) for ξn
i and ξn
i only, the proofs for ξ′n
i
and
ξ′n
i
being similar. We have seen in the proof of Lemma 7.6 that, by (7.11),
s ∈[0, 1)
⇒
E((γn
i )s) ≤Cs.
(7.20)
Although ξn
i does not depend on the sequence εn, we need to introduce a
suitable sequence εn to prove (7.18): so we prove (7.18) and (7.19) simulta-
neously, with some fixed θ ∈[1, 2) for the first result, and with θ = 1 for the
second one. If t = 1
2

1 + 1
l
- 2
θ

, by (7.17) and H´older’s inequality we get
E((Zn
i )p ∥ξn
i ∥θ (γn
i )l) ≤Cp,θ,l

E(∥ξn
i ∥tθ (γn
i )tl)

1/t ,
E((Zn
i )p ∥ξn
i ∥(γn
i )l) ≤Cp,l

E(∥ξn
i ∥t (γn
i )tl)
1/t
.





(7.21)
Next, let s be the biggest number in (1, 1/tl) such that its conjugate
exponent s′ is of the form s′ = 2m/tθ for some m ∈N with m ≥2,
and put q = s′tθ. Note that s′ and q depend on θ and l only. The set
{y > 0 : yqϕ(y/√n) ≤1} is an open or semi–open interval whose left end
point is 0, and whose right end point is denoted by a′
n, and since ϕ(y) →0
as y →0 it is clear that a′
n →∞. At this point, we set an = 1 .(a′
n −1/n):
then an →∞, and for all n big enough an < a′
n and thus aq
nϕ(an/√n) ≤1.
Then we choose the sequence εn as εn = an/√n, thus nε2
n ≥1. Observe that
both sequences εn and an only depend on θ and l.
Now we apply (7.8) and (7.9) with q and εn as above, plus (7.20) and
H¨older’s inequality, to get

E(∥ζ(3)n
i ∥tθ (γn
i )tl
1/t ≤Cθ,l ϕ(εn)1/s′t aθ−2/s′t
n
nθ/2
≤
Cθ,l
nθ/2a2/s′t
n
≤Cθ,l
nθ/2 ,

E(∥ζ(4)n
i ∥tθ (γn
i )tl
1/t +

E(∥ζ(5)n
i ∥tθ (γn
i )tl
1/t ≤
Cθ,l
nθ/2aθn ≤Cθ,l
nθ/2 .





(7.22)
In a similar way, (7.20) and (7.7) and H´older’s inequality give (with the same
q as above):

E(∥ζ(1)n
i ∥tθ (γn
i )tl
1/t ≤
Cθ,l (αn,q
i
)θ/q
nθ/2
,

E(∥ζ(2)n
i ∥tθ (γn
i )tl
1/t ≤Cθ,l
nθ/2 .



(7.23)
Finally applying (7.12) and tθ < 2 yields

E(∥ζ(6)n
i ∥tθ (γn
i )tl
1/t ≤
Cθ,l (αn,2
i
)1/q′
nθ/2
,

E(∥ζ(7)n
i ∥tθ (γn
i )tl
1/t ≤Cθ,l
nθ/2



(7.24)
for some q′ > 1 depending on tθ and tl, hence on θ and l only.
Then if we put together (7.21), (7.22), (7.23) and (7.24), and in view of
(7.3) and (7.4), we readily get (7.18), and also (7.19) with zn = a−2/s′t
n
+ a−1
n
(note that for (7.19) we take θ = 1).
⊓⊔

60
O. E. Barndorff–Nielsen et al.
7.4 Final estimates
The previous subsection gave us estimates on the variables of (7.3), which in
view of (7.4) are the building blocks for obtaining the difference occuring in
(7.1). Now we procees to give estimates for this difference itself. We start with
a lemma about the variables of (7.6).
Lemma 7.8. Under (SH1) we have for all q ≥2 and q′ ≥1 and t > 0:
αn,q
i
≤Cq,
1
n
[nt]

i=1
(αn,q
i
)1/q′ →0.
(7.25)
Proof. We can of course forget about the term 1/nq/2 in (7.6), whereas the
first part of (7.25) is obvious. For the second part we set
γn(u) = ∥au −a[nu]/n∥2 + ∥σ′
u−−σ′
[nu]/n∥2 + ∥vu−−v[nu]/n∥2
+

E
w(u−, x) −w
i −1
n
, x

2
F(dx).
Then the H¨older inequality yields
1
n
[nt]

i=1
(αn,q
i
)1/q′ ≤[nt]
n

1
[nt]
[nt]

i=1
E


	
n

i
n
i−1
n
γn(u)du

q/2



1/q′
≤[nt]
n

1
[nt]
[nt]

i=1
E
	
n

i
n
i−1
n
γn(u)q/2du



1/q′
≤t
q′−1
q′

E
 t
0
γn(u)q/2du
1/q′
.
Since γn is uniformly bounded and converges pointwise to 0, we get the result.
⊓⊔
Let us now introduce a list of growth or smoothness assumptions on a
real–valued function f on Rd, with complement (4.7). Below, C > 0 and
p ≥2 are suitable constants, and the pair (B, r) is given, with the properties
stated before (7.11). We list some conditions, for which we assume that f
is differentiable on the complement Bc. Below, each ΨA,ε is an increasing
continuous function on R+ with ΨA,ε(0) = 0.
x ∈Bc
⇒
|∇f(x)| ≤C(1 + ∥x∥p)

1 +
1
d(x, B)1−r

,
(7.26)
x, y ∈Rd
⇒
|f(x + y) −f(x)| ≤C(1 + ∥x∥p + ∥y∥p) ∥y∥r,
(7.27)

CLT for bipower variations
61
∥x∥≤A, ∥y∥≤ε′ < ε < d(x, B) ⇒∥∇f(x + y)−∇f(x)∥≤ΨA,ε(ε′)
(7.28)
0 < ∥y∥≤d(x, B)
2
=⇒
∥∇f(x + y) −∇f(x)∥≤C(1 + ∥x∥p + ∥y∥p)
∥y∥
d(x, B)2−r .(7.29)
The connections with our assumptions (K) and (K’) are as follows (with B
and r identical in (K’) and above, or B = ∅and r = 1 in the case of (K)):
(K), or (K’) with r = 1 ⇒(4.7), (7.26), (7.27) and (7.28),
(7.30)
(K’) with r < 1 ⇒(4.7) , (7.26), (7.27) and (7.29)
(7.31)
Next, we consider the setting of (5.5), with k is differentiable on Bc. We
let γ′′n
i
be either βn
i or β′n
i , and we introduce the following subsets of Ω:
An
i = {∥γ′n
i −γ′′n
i ∥> d(γ′′n
i , B)/2},
(7.32)
(observe that An
i = ∅when B = ∅). Let also γn
i be an auxiliary variable which
for each ω is on the segment joining γ′n
i
and γ′′n
i , and let γn
i be 1 when r = 1
and 1 + 1/d(γ′′n
i , B) when r < 1. Then we set
Φn
i = f(γn
i )

(k(γ′n
i ) −k(γ′′n
i ))1An
i −∇k(γ′′n
i )(γ′n
i −γ′′n
i )1An
i
+(∇k(γn
i ) −∇k(γ′′n
i ))(γ′n
i −γ′′n
i )1(An
i )c

,
(7.33)
Φn
i = f(γn
i ) ∇k(γ′′n
i )(γ′n
i −γ′′n
i )
(7.34)
(by the fact that B has Lebesgue measure 0, we see that k is a.s. differentiable
at the point γ′′n
i , which is either βn
i or β′n
i , so (7.33) and (7.34) make sense).
Lemma 7.9. Assume the following:
(i) (SH1) and (5.5) and k satisfies (7.26) and (7.27);
(ii) if r = 1 then k satisfies (7.28);
(iii) if B ̸= ∅then (SH’) holds;
(iv) if r < 1 then k satisfies (7.29).
(a) If γ′′n
i
= βn
i and γ′n
i −γ′′n
i
= ξn
i , or if γ′′n
i
= β′n
i
and γ′n
i −γ′′n
i
= ξ′n
i , we
have for all t > 0:
1
√n
[nt]

i=1
E(|Φn
i |) →0.
(7.35)
(b) If γ′′n
i
= βn
i and γ′n
i −γ′′n
i
= ξn
i , or if γ′′n
i
= β′n
i
and γ′n
i −γ′′n
i
= ξ′n
i , we
have for all t > 0:
1
√n
[nt]

i=1
E(|Φn
i |) →0.
(7.36)

62
O. E. Barndorff–Nielsen et al.
Proof. 1) We first prove (7.35) when r = 1. We choose εn = 1 for all n and
putting together all estimates in (7.7), (7.8), (7.9) and (7.12) (with l = 0, so
this estimate holds for q = 2 as well) to get
q ≥2
⇒
E(∥γ′n
i −γ′′n
i ∥q) ≤Cq
n .
(7.37)
Then (4.7) and (7.26) and An
i ⊂{d(γ′′n
i , B) < ε} ∪{∥γ′n
i −γ′′n
i ∥≥ε/2} yield
for all A > 0, ε > 2ε′ > 0:
|Φn
i | + |Φn
i | ≤C(Zn
i )2p

ΨA,ε′(ε) + ∥γ′′n
i ∥
A
+∥γ′n
i −γ′′n
i ∥
1
ε + 1
ε′

+ 1{d(γ′′n
i
,B)≤ε}

∥γ′n
i −γ′′n
i ∥. (7.38)
If B = ∅the indicator function above vanishes. Otherwise, the variable γ′′n
i
has a conditional law knowing F i−1
n which has a density (on Rd) that is smaller
than some (non–random) Lebesgue integrable function ϕ (see (3.6)), so it also
has an unconditional density smaller than ϕ. Therefore
P(d(γ′′n
i , B) ≤ε) ≤αε :=

{x:d(x,B)≤ε}
ϕ(x)dx,
and limε→0 αε = 0. Then (5.5), (7.37), (7.38) and the multivariate H¨older
inequality yield
E(|Φn
i |) + E(|Φn
i |) ≤C
√n

ΨA,ε(ε′) + 1
A +
1
n1/4
1
ε + 1
ε′

+ α1/4
ε

.
Hence (7.35) readily follows: choose A big, then ε small, then ε′ small.
2) Now we suppose that r < 1, hence B ̸= ∅. We have
|Φn
i | ≤(Zn
i )2p
∥γ′n
i −γ′′n
i ∥r 1An
i + ∥γ′n
i −γ′′n
i ∥1An
i
+ ∥γ′n
i −γ′′n
i ∥
d(γ′′n
i , B)1−r 1An
i + ∥γ′n
i −γ′′n
i ∥2
d(γ′′n
i , B)2−r 1(An
i )c

≤C(Zn
i )2p ∥γ′n
i −γ′′n
i ∥1+r/2 (γn
i )1−r/2,
(7.39)
where the first inequality follows from (7.26), (7.27) and (7.29) for k, while the
second one is obtained by using the definition of the set An
i . Hence Lemmas
7.7 and 7.8 readily give (7.35).
3) Finally, in all cases we have
|Φn
i | ≤C(Zn
i )2p ∥γ′n
i −γ′′n
i ∥(γn
i )1−r.
(7.40)
Therefore (7.36) follows from Lemmas 7.7 (see (7.19)) and 7.8 again.
⊓⊔

CLT for bipower variations
63
8 The proof of Theorem 2.3
1) As said at the beginning of the previous Section, we can assume that g
and h are 1–dimensional, and that (SH1), and also (SH’) when either g or h
satisfies (K’) instead of (K), and we need to prove that the arrays defined in
(7.1) and (7.1) are AN.
2) Let us prove first that (ζ′′n
i ) is AN. If f is continuously differentiable, and f
and ∇f have polynomial growth, we readily deduce from Lebesgue’s theorem
that Σ →ρΣ(f) = E(f(ΣU)) (where U is an N(0, Id)–random vector) is
bounded, continuously differentiable and with bounded derivatives over the
set M′ defined in connection with formula (3.6). Hence if both g and h satisfy
(K) we have (recall the notation (3.6), and set ϕ(Σ) = ρΣ(g)ρΣ(h)):
Σ, Σ′ ∈M′ ⇒
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
|ϕ(Σ)| + ∥∇ϕ(Σ)∥≤C
|ϕ(Σ) −ϕ(Σ′)| ≤C∥Σ −Σ′∥
|ϕ(Σ) −ϕ(Σ′) −∇ϕ(Σ′)(Σ −Σ′)∥
≤Ψ(∥Σ −Σ′|)∥Σ −Σ′∥
(8.1)
for some constant C (depending on A0 in (3.6)) and some increasing function
Ψ on R+, continuous and null at 0 (here, ∇ϕ is Md,d–valued, and ∇ϕ(Σ′)(Σ−
Σ′) is R–valued).
If g or h (or both) satisfy (K’) only we also have (SH’), and since
ρΣ(f) =

1
(2π)d/2det(ΣΣ⋆)1/2 f(x) exp

−1
2 x⋆(ΣΣ⋆)−1x

dx
we see that as soon as f has polynomial growth the function Σ →ρΣ(f) is
C∞with bounded derivatives of all orders on the set M′. Hence we also have
(8.1), which thus holds in all cases.
Since we can write (7.2) as ζ′′n
i
= √n
 i/n
(i−1)/n(ϕ(σu) −ϕ(σ(i−1)/n)du, we
have ζ′′n
i
= ηn
i + η′n
i
where
ηn
i = √n ∇ϕ(σ i−1
n )

i
n
i−1
n
(σu −σ i−1
n ) du,
η′n
i
= √n

i
n
i−
n

ϕ(σu) −ϕ(σ i−1
n ) −∇ϕ(σ i−1
n )(σu −σ i−1
n )

du.
and we need to prove that the two arrays (ηn
i ) and (η′n
i ) are AN.
We decompose further ηn
i as ηn
i = µn
i + µ′n
i , where
µn
i = √n ∇ϕ(σ i−1
n )

i
n
i−1
n
du
 u
i−1
n
a′
sds,

64
O. E. Barndorff–Nielsen et al.
µ′n
i = √n ∇ϕ(σ i−1
n )

i
n
i−1
n
	 u
i−1
n
σs−dWs +
 u
i−1
n
vs−dVs
+
 u
i−1
n

E
w(s−, x)(µ −ν)(ds, dx)

du.
On the one hand, we have |µn
i | ≤C/n3/2 by (8.1) and the boundedness of a′,
so the array (µn
i ) is AN. On the other hand, we also get by (SH1) and (8.1)
and Cauchy–Schwarz applied twice:
E

µ′n
i | F i−1
n

= 0,
E

(µ′n
i )2 | F i−1
n

≤C
n3 .
Then the array (µ′n
i ) is AN, as well as the array (ηn
i ).
Finally, using (8.1) once more, we see that for all ε > 0,
|η′n
i | ≤√n

i
n
i−1
n
Ψ(∥σu −σ i−1
n ∥) ∥σu −σ i−1
n ∥du
≤√n Ψ(ε)

i
n
i−1
n
∥σu −σ i−1
n ∥du + C√n
ε

i
n
i−1
n
∥σu −σ i−1
n ∥2 du.
Since E(∥σu −σ i−1
n ∥2) ≤C/n when u ∈((i −1)/n, i/n], we deduce that
[nt]

i=1
E(|η′n
i |) ≤Ct

Ψ(ε) +
1
ε√n

.
From this we deduce the AN property of the array (η′n
i ) because ε > 0 is
arbitrarily small and limε→0 Ψ(ε) = 0. Hence, finally, the array (ζ′′n
i ) is AN.
3) Now we start proving that the array (ζ′n
i ) also is AN. Since ϕ(σ(i−1)/n) =
E(g(βn
i )h(β′n
i ) | F(i−1)/n), we have ζ′n
i
= E(δn
i | F(i−1)/n), where
δn
i =
1
√n

g(√n ∆n
i Y )h(√n ∆n
i+1Y ) −g(βn
i )h(β′n
i )

.
Let us set
An
i = {∥√n ∆n
i Y −βn
i ∥> d(βn
i , B)/2},
A′n
i = {∥√n ∆n
i+1Y −β′n
i ∥> d(β′n
i , B′)/2},
where B (resp. B′) is either empty or is the set associated with g (resp. h),
according to whether that function satisfies (K) or (K’). We can express the
difference g(√n ∆n
i Y ) −g(βn
i ) using a Taylor expansion if we are on the set
(An
i )c, and we can thus write

CLT for bipower variations
65
g(√n ∆n
i Y ) −g(βn
i )
= (g(√n ∆n
i Y ) −g(βn
i ))1An
i −∇g(βn
i )(√n ∆n
i Y −βn
i )1An
i
+(∇g(γn
i ) −∇g(βn
i ))(√n ∆n
i Y −βn
i ) 1(An
i )c
+∇g(βn
i )(√n ∆n
i Y −βn
i ),
(8.2)
where γn
i is some (random) vector lying on the segment between √n ∆n
i Y
and βn
i : recall that ∇g(γn
i ) is well defined because on (An
i )c we have γn
i ∈Bc,
while ∇g(βn
i ) is a.s. well defined because either B is empty, or it has Lebesgue
measure 0 and βn
i has a density. Analogously, h(√n ∆n
i+1Y ) −h(β′n
i ) can be
written likewise, provided we replace ∆n
i Y , βn
i , An
i , γn
i by ∆n
i+1Y , β′n
i , A′n
i ,
γ′n
i .
Now observe that
δn
i =
1
√n g(√n ∆n
i Y )

h(√n ∆n
i+1Y ) −h(β′n
i )

+ 1
√n

g(√n ∆n
i Y ) −g(βn
i )

h(β′n
i ),
Therefore we deduce from the decomposition (8.2) and the analogous one for
h, and also from (7.3) and (7.4), that δn
i = 6
k=1 δn
i (k), where
δn
i (1) =
1
√n g(√n ∆n
i Y )∇h(β′n
i )*ξ′′n
i ,
δn
i (2) =
1
√n g(√n ∆n
i Y )∇h(β′n
i )*ξn
i+1,
δn
i (3) =
1
√n h(β′n
i )∇g(βn
i )*ξn
i ,
δn
i (4) =
1
√n

g(√n ∆n
i Y )∇h(β′n
i )ξ′n
i + h(β′n
i )∇g(βn
i )ξn
i

,
δn
i (5) =
1
√n g(√n ∆n
i Y )

(h(√n ∆n
i+1Y ) −h(β′n
i ))1A′n
i
−∇h(β′n
i )(√n ∆n
i+1Y −β′n
i )1A′n
i
+(∇h(γ′n
i ) −∇h(β′n
i ))(√n ∆n
i+1Y −β′n
i ) 1(A′n
i )c

,
δn
i (6) =
1
√n h(β′n
i )

(g(√n ∆n
i Y ) −g(βn
i ))1An
i
−∇g(βn
i )(√n ∆n
i Y −βn
i )1An
i
+(∇g(γn
i ) −∇g(βn
i ))(√n ∆n
i Y −βn
i ) 1(An
i )c

.

66
O. E. Barndorff–Nielsen et al.
If we combine (5.2) with Lemma 7.9, we readily get [nt]
i=1 E(∥δn
i (k)∥) →0
when k = 4, 5, 6. So we are left to proving that
the array
/
µn
i (k) = E

δn
i (k) | F i−1
n
0
is AN.
(8.3)
for k = 1, 2, 3.
4) Let us introduce the Md,d′–valued martingales
M(n, i)t =



0
if t ≤i−1
n
v i−1
n (Vt −V i−1
n ) +
 t
i−1
n

En w( i−1
n , x)(µ −ν)(ds, dx) otherwise.
We see that *ξn
i = ζ(2)n
i + ζ(5)n
i + ζ(7)n
i = √n (ηn
i + η′n
i ), where
ηn
i = 1
n a i−1
n +

i
n
i−1
n
(Wu −W i−1
n )dWu,
η′n
i
=

i
n
i−1
n
M(n, i)udWu = ∆n
i M(n, i)∆n
i W −

i
n
i−1
n
dM(n, i)u Wu.
Now we can write
µn
i (3) = ρn
i−1(h) E

∇g(√n σ i−1
n ∆n
i W)(ηn
i + η′n
i ) | F i−1
n

.
g is even, so ∇g is odd; hence the variable ∇g(√n σ i−1
n ∆n
i W)ηn
i is multiplied
by −1 if we change the sign of the process (Ws −W(i−1)/n)s≥(i−1)/n, and
this sign change does not affect the F(i−1)/n–conditional distribution of this
process. Hence we get
E

∇g(√n σ i−1
n ∆n
i W)ηn
i | F i−1
n

= 0.
On the other hand, the processes M(n, i) and Ws −W(i−1)/n are inde-
pendent, conditionally on F(i−1)/n, when the times goes through ((i −
1)/n, i/n]. So if F0
s denotes the σ–field generated by F(i−1)/n and by
(Wu −W(i−1)/n)(i−1)/n≤u≤s, we get that M(n, i) is an (F0
s)–martingale for
s ∈((i −1)/n, i/n], and thus E(η′n
i |F0
i/n) = 0. By successive conditioning, we
immediately deduce that
E

∇g(√n σ i−1
n ∆n
i W)η′n
i
| |F i−1
n

= 0,
and therefore µn
i (3) = 0. In a similar way, ∇h is odd and β′n
i
is the product of
an F(i−1)/n–measurable variable, times ∆n
i+1W. So exactly as above we have
E

∇h(β′n
i ) *ξn
i+1 | F i
n

= 0,

CLT for bipower variations
67
and so a fortiori µn
i (2) = 0.
5) It remains to study µn
i (1). With the previous notation M(n, i), it is easy
to check that
µn
i (1)
=
1
√n
d

l=1
d′

m=1
zn,lm
i
E

g(√n ∆n
i Y )(σ′
i−1
n ∆n
i W +∆n
i M(n, i))lm
| F i−1
n

,
where zn,lm
i
=

∂xlh(σ i−1
n x) xm ρ(dx) and ρ is N(0, Id′) (the law of W1), so
∥zn,lm
i
∥≤C. Recalling once more √n ∆n
i Y = βn
i + ξn
i + *ξn
i , we see that
µn
i (1) =
d

l=1
d′

m=1

E

µn
i (l, m) | F i−1
n

+ E

µ′n
i (l, m) | F i−1
n

,
where
µn
i (l, m) =
1
√n zn,lm
i

g(βn
i + ξn
i + *ξn
i )−g(βn
i )

σ′
i−1
n ∆n
i W +∆n
i M(n, i)
lm
,
µ′n
i (l, m) =
1
√n zn,lm
i
g(βn
i )

σ′
i−1
n ∆n
i W + ∆n
i M(n, i)
lm
.
Use (5.2) and (7.37) and the property E(∥∆n
i W∥q) + E(∥∆n
i M(n, i)∥q) ≤
Cq/n for all q ≥2 to get that [nt]
i=1 E(|µn
i (l, m)|) →0. Finally, since g is
even and ∆n
i W and ∆n
i M(n, i) are independent conditionally on F(i−1)/n and
E(∆n
i M(n, i) | F(i−1)/n) = 0, we find that indeed E(µ′n
i (l, m) | F(i−1)/n) = 0.
So we get (8.3) for k = 1, and we are done.
References
1. Andersen T.G., Bollerslev T., Diebold F.X. and Labys P.: Modeling and Fore-
casting realized Volatility. Econometrica, 71, 579–625 (2003)
2. Andersen T.G., Bollerslev T. and Diebold F.X.: Parametric and nonparametric
measurement of volatility, in “Handbook of Financial Econometrics”, edited
by Ait-Sahalia Y. and Hansen L.P., North Holland, Amsterdam, Forthcoming
(2004)
3. Barndorff–Nielsen O.E. and Shephard N.: Econometric analysis of realised
volatility and its use in estimating stochastic volatility models. Journal of the
Royal Statistical Society, Series B, 64, 253–280 (2002)
4. Barndorff–Nielsen O.E. and Shephard N.: Econometrics of testing for jumps
in financial economics using bipower variation. Unpublished discussion paper:
Nuffield College, Oxford (2003)
5. Barndorff–Nielsen O.E. and Shephard N.: Power and bipower variation with
stochastic volatility and jumps (with discussion). Journal of Financial Econo-
metrics, 2, 1–48 (2004)

68
O. E. Barndorff–Nielsen et al.
6. Barndorff–Nielsen O.E. and Shephard N.: Econometric analysis of realised co-
variation: high frequency covariance, regression and correlation in financial eco-
nomics. Econometrica, 72, 885–925 (2004)
7. Becker E.: Th´or`emes limites pour des processus discr´etis´es. PhD Thesis, Univ.
P. et M. Curie (1998)
8. Jacod, J.: Limit of random measures associated with the increments of a Brown-
ian semimartingale. Unpublished manuscript (1994)
9. Jacod, J. and Shiryaev, A.: Limit Theorems for Stochastic Processes, 2d edition.
Springer-Verlag: Berlin (2003)
10. Jacod, J.: Inference for stochastic processes, in “Handbook of Financial Econo-
metrics”, edited by Ait-Sahalia Y. and Hansen L.P., North Holland, Amsterdam,
Forthcoming (2004)
11. R´enyi A.: On stable sequences of events. Sankhya, Ser. A, 25, 293–302 (1963)

Interplay between Distributional and Temporal
Dependence. An Empirical Study with
High-frequency Asset Returns
Nick H. BINGHAM1 and Rafael SCHMIDT2
1 University of Sheffield, Department of Probability and Statistics,
Hicks Building, Sheffield S3 7RH,
United Kingdom.
nick.bingham@sheffield.ac.uk
2 London School of Economics, Department of Statistics, Houghton Street,
London WC2A 2AE,
United Kingdom.
r.schmidt@lse.ac.uk
Summary. The recent popularity of copulas in the analysis and modelling of mul-
tivariate financial time series arises from several applications in the financial sector.
This paper surveys the most important techniques of modelling and measuring dis-
tributional dependence with a view towards financial applications such as pricing
and hedging financial instruments and portfolio risk management. The term distri-
butional dependence refers to the (contemporaneous) dependence among multiple
time series. The majority of results of the existing statistical literature on cop-
ulas assumes i.i.d. data. However, real financial time series incorporate temporal
dependence such as volatility clustering or seasonality. Moreover, common filtering
techniques, for example (G)ARCH filtering, usually also lead to a rejection of the
i.i.d. hypothesis due to model misidentification. In this paper we investigate the
sensitivity of (distributional) dependence measures with respect to various filtering
techniques utilizing an IBM-GM high-frequency data set. The main focus will be on
the distributional dependence of extreme events, which is important for risk man-
agement. Our results show that filtering techniques crucially affect the distributional
dependence structure.
Key words: Distributional dependence; temporal dependence; copula; Kendall’s
tau; tail dependence; high-frequency asset returns; GARCH process; autocorrelation
function (ACF); multivariate analysis.
Mathematics Subject Classification (2000): 62H20, 62-07, 62G05,
62P20, 62M10, 60G70

70
N.H. Bingham and R. Schmidt
1 Introduction
Copula functions link multivariate distributions to their corresponding uni-
variate marginals and allow one to study the distributional dependence of
multivariate distributions. In contrast to temporal dependence of a time se-
ries, the term distributional dependence refers to the (contemporaneous) de-
pendence among multiple time series. In finance and insurance, copulas have
recently become very popular due to two important applications.
First, copulas have been recognized as a promising tool to analyze and
model the dependence structure of credit-risky portfolios [19], [38], [32], [15].
The adequate modelling of dependence in credit portfolios has been identified
as one of the most important and pressing issues to be addressed in modern
credit-risk management. This is partly because the pressure of globalization
has led to a significant increase of dependencies within assets and asset classes
of particular markets and between markets. For example, many empirical
studies, such as [46], [49], and [22], have focused on the so-called ”correlation
break-down”. The latter refers to the significant increases of distributional
dependence between financial asset returns during bear markets, which leads
to failure of conventional diversification strategies in times when they are most
needed. In particular, the precise analysis of the extreme (negative) returns
of an asset portfolio, which depends heavily on the dependence structure of
the individual extreme asset returns, must be studied carefully as it provides
important insights into the appropriate supply of economic capital, cf. [56].
Second, in order to manage and control portfolio credit risk, a new gener-
ation of financial instruments such as basket credit derivatives and collater-
alised debt obligations (CDOs) has been introduced to financial markets. The
pricing and hedging of these instruments require a careful analysis of the de-
pendence structure between the respective underlying as well. For the active
management of portfolio credit risk, copulas have recently been applied to
model the dependence structure between default times involved in the pricing
and hedging of basket credit derivatives and CDOs. For example, [48] utilizes
the so-called Gaussian copula to price first-to-default credit derivatives. [47]
and [60] extend the copula-based pricing to other basket credit derivatives
and CDOs by applying other types of copulas.
For further application, see [24] or [57] for a time series approach with
copulas and [43], who apply copulas in the framework of multidimensional
option pricing.
This paper provides a survey of the most important techniques of mod-
elling and measuring distributional dependence with a view towards pricing
and hedging the afore-mentioned financial instruments and towards portfolio
risk management. In the first section we present the concept of copulas and
relevant results, and we outline their importance for analyzing distributional
dependence. In passing we introduce the family of tail copulas which helps
analyzing the distributional dependence of extreme events. We then discuss
various dependence measures related to (tail) copulas and indicate financial

Interplay between Distributional and Temporal Dependence
71
applications. Afterwards we focus on nonparametric statistical inference for
(tail) copulas and dependence measures and point out that the majority of
statistical results are valid under the assumption of i.i.d. data. However, it
is well known that every real financial time series incorporates temporal de-
pendence. For example we will show that some high-frequency financial data
possess a very characteristic seasonal and autoregressive temporal dependence
structure of its volatilities. The latter is often referred to as volatility cluster-
ing. The amount of literature on filtering techniques for time series, in order
to obtain i.i.d. data, is enormous. In practice, the most popular filtering tech-
nique for volatility clustering of asset returns is unquestionably the (G)ARCH
filtering. Although, (G)ARCH filtering usually leads to a rejection of the i.i.d.
hypothesis of the resulting residuals due to model misidentification. However,
its simple interpretation, estimation and forecasting has made it the favorite
filtering technique in the financial industry. (G)ARCH models have been in-
troduced and discussed in [18], [29], and [1].
The second part of the paper continues with the previous discussion and
investigates the sensitivity of measures of distributional dependence towards
deseasonalisation and GARCH filtering for a General Motors (GM) and In-
ternational Business Machines (IBM) high-frequency data set. Our particular
choice of the GARCH filter is justified by its afore-mentioned popularity. We
will especially focus on the distributional dependence of extreme events.
Our results show that filtering techniques crucially affect the distributional
dependence structure and thus inherit the danger of wrong conclusions from
inappropriate dependence measures. As a side product we advocate autocor-
relation functions (ACF) based on scale-invariant (copula-based) dependence
measures and provide new insights into the interplay between distributional
and temporal dependence of multivariate time series. The discussion of a new
type of nonparametric estimator for the so-called tail dependence gives in-
sight into the dependence measurement of extreme events. We will compare
our results with the findings of [20].
2 Modelling distributional dependence
Each multivariate distribution function can be split into its univariate mar-
ginal distribution functions and a copula function (Sklar’s theorem, [61]). In
other words, copulas allow one to study the distributional dependence struc-
ture of random vectors irrespective of their marginal distributions.
Definition 1 (Copula). Let X = (X1, . . . , Xd)′ be an d-dimensional ran-
dom vector with distribution function F(x1, . . . , xd) = P(X1 ≤x1, . . . , Xd ≤
xd) and marginal distribution-functions Fi(xi) = P(Xi ≤xi) for all i =
1, . . . , d. Then the distribution function C of the d-dimensional random vector
(F1(X1), . . . , Fd(Xd))′ is called copula (or copula function) of X or F.

72
N.H. Bingham and R. Schmidt
It can be shown that the copula function is uniquely determined by the
multivariate distribution function F if all univariate marginal distribution
functions are continuous (Sklar’s Theorem) and that
F(x1, . . . , xd) = C(F1(x1), . . . , Fd(xd)).
Thus, copulas can be utilized to build flexible multivariate distribution
functions in two steps: First, model the distributional dependence via some
copula, and second, plug in appropriate marginals.
Copula functions represent standardized distributions in the sense that
their one-dimensional marginals are uniformly distributed on the interval
[0, 1]. An important property is that the copula of a random vector X stays the
same irrespectively of any strictly increasing transformation of the marginals
Xj, j = 1, . . . , d. This invariance property (also called “scale invariance”) is a
desired feature of dependence functions and dependence measures, as we un-
derstand dependence itself to represent the association between “large” and
“small” realizations of random vectors irrespectively of their scale.
Kendall’s tau and Spearman’s rho. A proper dependence measure
for multivariate distributions should be scale invariant (or invariant under
change of the marginal distributions). All dependence measures derived from
the copula are scale invariant, and so in line with our basic requirement. The
most important scale invariant dependence measure in financial applications
is Kendall’s τ.
Definition 2 (Kendall’s tau). Let X and ¯X be independent d - dimensional
random vectors with common continuous distribution function F and copula
C. Kendall’s tau of the margins Xi and Xj, i < j, is defined by
τij : = Prob((Xi −¯Xi)(Xj −¯Xj) > 0) −Prob((Xi −¯Xi)(Xj −¯Xj) < 0)
= 4

[0,1]2 Cij(ui, uj) dCij(ui, uj) −1,
(2.1)
where Cij(ui, uj) = C(1, . . . , 1, ui, 1, . . . , 1, uj, 1 . . . , 1).
The finite-sample version of Kendall’s tau ˆτij is defined as the ratio of the
number of concordant minus the number of discordant pairs of sample points
with respect to the number of concordant and discordant pairs of sample
points. Here, a pair of sample points (xi, xj) and (¯xi, ¯xj) is called concordant
if xi < (>)¯xi and xj < (>)¯xj, and discordant otherwise. Formally
ˆτ = concordant pairs −disconcordant pairs
concordant pairs + disconcordant pairs.
(2.2)
Obviously this dependence measure is scale-invariant and it represents one of
the most intuitive dependence measures.
The Pearson’s correlation coefficient ρ(Xi, Xj) of the i-th and j-th com-
ponent of X = (X1, . . . , Xd)′ measures linear dependence and is thus not

Interplay between Distributional and Temporal Dependence
73
scale-invariant. However, we might intuitively substitute for the random vari-
ables Xi and Xj the standardized random variables Fi(Xi) and Fj(Xj) in
order to obtain the scale-invariant correlation coefficient ρ(Fi(Xi), Fj(Xj)).
Indeed, this dependence measure is well known and is called Spearman’s rho
ρS
ij := ρ(Fi(Xi), Fj(Xj)). It can be shown that
ρS
ij = 12

[0,1]2 Cij(ui, uj) duiduj −3.
In contrast to Pearson’s correlation coefficient, the latter two dependence
measures are always 1 or −1, respectively, if one random variable is an increas-
ing function (completely positively correlated) or decreasing function (com-
pletely negatively correlated) of the other. Recall that Pearson’s correlation
coefficient might be zero in both cases. A detailed treatment of copulas and
other dependence measures can be found in [44] and [55].
Tail dependence and tail copula. In contrast to the dependence mea-
sures discussed so far, tail dependence focuses solely on the distributional
dependence of extreme or tail events. In the context of tail dependence, the
immediate analogue to copulas, which describe the entire distributional de-
pendence structure, is given by tail copulas. In this paper we restrict ourself
to so-called lower tail copulas. However, the results hold similarly for upper
tail copulas; see [59] for the definition. If not otherwise stated, we assume
continuous marginal distributions.
Definition 3 (Tail copula). Let F be a d-dimensional distribution function
with copula C. If for the subsets I, J ⊂{1, . . . , d}, I ∩J = ∅, the following
limit exists everywhere on ¯Rd
+ := [0, ∞]d\{(∞, . . . , ∞)} :
ΛI,J
L (x) := lim
t→∞IP(Xi ≤F −1
i
(xi/t), ∀i ∈I | Xj ≤F −1
j
(xj/t), ∀j ∈J)
= lim
t→∞C(xi/t, ∀i ∈I | xj/t, ∀j ∈J),
(2.3)
then the function ΛI,J
L
: ¯Rd
+ →R is called a lower tail-copula associated with
F (or C) with respect to I, J .
For simplicity and notational convenience all further definitions and results
are provided only for the bivariate case. The multidimensional extensions are
given in [59]. The statistical inference becomes easier if the following slight
modification of the tail copula is utilized:
ΛL(x1, x2) := x2 · Λ{1},{2}
L
(x1, x2),
x1 ∈¯R+, x2 ∈R+,
(2.4)
where the indices {1} and {2} can be dropped. Further, set ΛL(x1, ∞) := x1
for all x1 ∈R+.
The next definition embeds the well-known tail-dependence coefficient (see
[44], p. 33) within the framework of tail copulas.

74
N.H. Bingham and R. Schmidt
Definition 4 (Tail dependence). A bivariate random vector (X1, X2)′ is
said to be lower tail-dependent if ΛL(1, 1) exists and
λL := ΛL(1, 1) = lim
v→0+ Prob(X1 ≤F −1
1
(v) | X2 ≤F −1
2
(v)) > 0.
(2.5)
Consequently, (X1, X2)′ is called lower tail-independent if λL equals 0. Fur-
ther, λL is referred to as the lower tail-dependence coefficient.
It is well known that the multivariate normal distributions, the multivari-
ate generalized-hyperbolic distributions, and the multivariate logistic distrib-
utions are lower tail-independent whereas the multivariate t-distributions and
the α-stable distributions are lower tail-dependent. For a general account on
tail dependence for elliptically-contoured distributions we refer to [58]. Both
preceding definitions show that tail dependence is again a copula property.
In particular, the tail-dependence coefficients are invariant under strictly in-
creasing transformations of the marginals.
Practitioners interpret tail dependence as the limiting likelihood of an
asset/portfolio return falling below its Value at Risk given that another as-
set/portfolio return has fallen below its Value at Risk.
Application: CDOs and multi-name credit derivatives. We have
already mentioned in the introduction of this paper that the increasing active
management and control (in contrast to the traditional passive management
and control) of portfolio credit risk has led to a new generation of finan-
cial instruments such as multi-name credit derivatives and collateralised debt
obligations (CDOs). Examples of these instruments are basket credit default
swaps (We refer to [16] for more background reading.). Because of the associ-
ation with a pool of credit-risky underlying, the pricing and hedging of these
instruments require a careful analysis of the dependence structure between
the respective underlying. In this context, copulas have recently been applied
to model the dependence structure between default times of the underlying.
Let us consider a portfolio of d underlying assets and let τi represent the de-
fault time of the ith underlying (or the corresponding obligor). Further, let
Fi(t) = P(τi ≤t) be the marginal distributional function of the default time
of obligor i. The copula function C is now used to obtain the multivariate
default-time distribution F(t1, . . . , td) = C(F1(t1), . . . , Fd(td)). The latter ap-
proach allows to calibrate the default-time distribution, in the first step, for
each margin separately. This calibration is also necessary in order to construct
so-called credit yield curves. In the second step, a parametric copula is usu-
ally calibrated via some scale-invariant dependence measure such as Kendall’s
tau. The optimal choice of the copula is the topic of many recently published
research papers. For example, [48] utilizes the so-called Gaussian copula to
price first-to-default credit derivatives. [47] and [60] extend the copula-based
pricing to other basket credit derivatives and CDOs by applying other types
of copulas.

Interplay between Distributional and Temporal Dependence
75
3 Statistical inference
Empirical copula. Concerning the estimation of copula functions, several
parametric, semi-parametric, and nonparametric procedures have already
been proposed in the literature (cf. [62], [41], [42]). Regarding the nonparamet-
ric estimation, [26], [27], and [36] establish weak convergence of the so-called
empirical copula process under independent and dependent marginal distrib-
utions. In the following we will confine to the bivariate case.
Definition 5 (Empirical copula). Consider the bivariate random sample
{(X1
i , X2
i )′, i = 1, . . . , n}. Then the corresponding (lower) empirical copula is
defined by
Cn(u1, u2) = 1
n
n

i=1
1{F1,n(X1
i ) ≤u1, F2,n(X2
i ) ≤u2},
(3.6)
where 1 denotes the indicator function and Fj,n is n/(n+1) times the empirical
distribution function of {(Xj
i ), i = 1, . . . , n}, j = 1, 2.
Note that the empirical copula is a function of the ranks of the observa-
tions. Powerful test for independence or goodness of fit (such as Cram´er-von
Mises or Kolmogorov-Smirnov) could be based on functionals of the empirical
copula. However, there does not exist a simple expression for the asymptotic
distribution of the empirical copula process
Cn(u1, u2) = √n{Cn(u1, u2) −C(u1, u2)}.
(3.7)
The limiting process of (3.7) is derived in [62] and [39] (Test of independence
based on the empirical copula process are developed in [40].). Analogous lim-
iting results, although one needs different techniques of proof, can be obtained
for the so-called empirical tail copula process.
Empirical tail copula. A nonparametric estimator, the so-called empiri-
cal tail copula, for the bivariate (lower) tail-copula ΛL(x1, x2), (x1, x2)′ ∈¯R2
+,
is proposed. Note that nonparametric estimation turns out to be appropriate
for unknown tail copulas as no general finite-dimensional parametrization of
tail copulas exists (in contrast to the one-dimensional extreme value distri-
butions). Further, the choice of the empirical distribution function to model
the marginal distributions avoids any misidentification of the copula due to a
wrong parametrical fit of the marginal distributions. Empirical investigations
regarding such misidentifications and misinterpretations of the corresponding
(extremal) dependence structure are provided in [37].
Definition 6 (Empirical tail copula). Consider the bivariate random sam-
ple {(X1
i , X2
i )′, i = 1, . . . , n} and denote the rank of X1
i and X2
i by R1
in and
R2
in, respectively. The (lower) empirical tail copula is defined via formula (2.3)
by:

76
N.H. Bingham and R. Schmidt
ˆΛL,n(x1, x2) := n
k Cn
kx1
n , kx2
n

= 1
k
n

i=1
1{R1
in ≤kx1 and R2
in ≤kx2}
with empirical copula Cn and some threshold k ∈{1, . . . , n}.
The optimal choice of the threshold k in Definition 6 is related to the
usual variance-bias problem, also known from tail index estimations of regular
varying distributions, and will be addressed in a forthcoming work. For the
asymptotic results we assume that k = k(n) →∞and k/n →0 as n →∞.
Remark. Definitions 5 and 6 can be generalized for bivariate time series in
an obvious way. In this case we refer to the empirical (tail) copula as quasi-
empirical (tail) copula.
Condition 3.1 (Second-Order Condition) 1exsecond order conditionThe
lower tail-copula ΛL(x, y) is said to satisfy a second-order condition if a func-
tion A : R+ →R+ exists such that A(t) →0 as t →∞and
lim
t→∞
ΛL(x, y) −tC(x/t, y/t)
A(t)
= g(x, y) < ∞
locally uniformly for (x, y)′ ∈¯R2
+ and some nonconstant function g. The
second-order condition for the upper tail-copula is defined analogously.
Note that A(t) is regularly varying at infinity, so this is just a second-order
condition on regular variation, cf. [25].
Theorem 3.2 (Asymptotic normality). Let F be the bivariate distribution
function of the random sample {(X1
i , X2
i )′, i = 1, . . . , n} with continuous
marginal distribution functions F1 and F2. If the tail copula ΛL ̸≡0 exists,
possesses continuous partial derivatives, and the Second-Order Condition 3.1
holds, then for n →∞
√
k
1 ˆΛL,n(x1, x2) −ΛL(x1, x2)
2 w→GΛL(x1, x2),
where GΛL(x1, x2) is a centered tight continuous Gaussian random field. Weak
convergence takes place in the space of uniformly-bounded functions on com-
pacta in ¯R2
+. The covariance structure of G ˆ
ΛL(x1, x2) is given in Corollary 1
below.
Corollary 1 (Covariance structure). The limiting process in Theorem 3.2
can be expressed by
G ˆ
ΛL(x1, x2) = G ˆ
Λ∗
L(x1, x2)
(3.8)
−
∂
∂x1
ΛL(x1, x2)G ˆ
Λ∗
L(x1, ∞) −
∂
∂x2
ΛL(x1, x2)G ˆ
Λ∗
L(∞, x2),
where GΛL(x1, x2) is a centered tight continuous Gaussian random field. The
covariance structure of GΛ∗
L is given by

Interplay between Distributional and Temporal Dependence
77
E

G ˆ
Λ∗
L(x1, x2) · G ˆ
Λ∗
L(¯x1, ¯x2)

= ΛL

min{x1, ¯x1}, min{x2, ¯x2}

(3.9)
for (x1, x2)′, (¯x1, ¯x2)′ ∈¯R2
+.
The proof of asymptotic normality, see [59], is accomplished in two steps.
In the first step the marginal distribution functions F1 and F2 are assumed to
be known and an asymptotic normality result is derived. In the second step
the marginal distribution functions F1 and F2 are assumed to be unknown
and the asymptotic result is proven by utilizing a particular version of the
functional delta method, as provided in [63].
The evaluation of the empirical tail copula at the point (1, 1)′ immediately
yields a non-parametric estimator for the lower tail-dependence coefficient.
The estimation of the lower tail-dependence coefficient (briefly: lower TDC)
is important for practical applications, for example in risk management, where
one is primarily interested in the dependence between large loss events. It has
been addresses in several publications, see [52], [45], [5], [20], and [37]. Consider
the following nonparametric estimator for the lower TDC:
ˆλL,n(k) = ˆΛL,n(1, 1) = 1
k ·
n

j=1
1{R1
in ≤k ∧R2
in ≤k}
1 ≤k ≤n,
with k = k(n) →∞and k/n →0 as n →∞.
Under the same technical conditions as in Theorem 3.2 we obtain that for
n →∞
√
k
1ˆλL,n −λL
2
d→GλL,
with GλL being centered and normally distributed, i.e. GλL ∼N(0, σ2
L) with
σ2
L = λL +
 ∂
∂xΛL(1, 1)
2
+
 ∂
∂y ΛL(1, 1)
2
+ 2λL
 ∂
∂xΛL(1, 1) −1
 ∂
∂y ΛL(1, 1) −1

−1

.
[59] prove strong consistency of ˆλL,n and ˆΛL,n if k/ log(log n) →∞as n →∞.
4 Dependence of high-frequency asset returns - An
empirical study
4.1 The GM-IBM high-frequency data set
So far we have surveyed important techniques of modelling and measuring dis-
tributional dependence for financial time series. We have mentioned the con-
cept of empirical (tail) copulas which is a central element for nonparametric
statistical inference from real data. We pointed out that the related results on
asymptotic normality and strong consistency are proven under the assumption

78
N.H. Bingham and R. Schmidt
of i.i.d. data (Note that the limiting distributions are already quite compli-
cated in this case.). However, each financial time series incorporates temporal
dependence, i.e. the data cannot be assumed to be independent and identical
distributed. Furthermore, almost all common filtering techniques will lead to
a rejection of the i.i.d. hypothesis due to the usual model misidentification.
The question is therefore: How sensitive is the distributional dependence
(although the measurements are always obtained from data which are tempo-
rally dependent) towards various filtering methods?
To give a partial answer to this question we consider a typical financial time
series, namely a General Motors (GM) and International Business Machines
(IBM) high-frequency data set. High-frequency asset return data comprise
several very characteristic dependence features which are usually only found
in experimentally-generated time series, and thus they are very interesting for
our empirical analysis. Many authors have already been attracted to explore
these features. In the framework of univariate time series, [9], [2], [51], and [6]
investigate the estimation of the actual volatility of stochastic-volatility mod-
els (SV) by means of so-called realized volatilities of high-frequency data. Fur-
ther, [3], [4], [23], and [54] address the question of how to model the character-
istic (volatility) seasonality and volatility clustering effects of high-frequency
data. The direct fitting of well-established financial models to high-frequency
asset returns is usually complicated, due to market microstructure effects such
as discreteness of prices, bid/ask bounce, irregular trading etc. (see for exam-
ple [7]). Moving-average structures for asset returns, which often occur as the
result of no-trading effects or bid/ask bounce effects, are discussed in [21].
However, there is not much literature on multivariate aspects related to
high-frequency financial data; among them we mention [10] and [20].
The plan of our statistical analysis. In the first step, we apply var-
ious filtering techniques to the afore-mentioned data set in order to obtain
approximately i.i.d. data. In particular, we utilize a GARCH filter, in order to
reduce the observed volatility clustering of the asset returns, as it is the most
popular and common filtering technique in the financial sector. In the second
step, we analyze the effect of the filtering on the quasi-empirical copula and
on the magnitude of tail dependence. In passing, we introduce autocorrelation
functions (ACFs) based on Kendall’s tau.
The data. The data of high-frequency asset returns we utilize in this
paper correspond to the cleaned bivariate stock prices of GM and IBM over
the time horizon 4th of January 1993 to 29th of May 1998. For reasons of
market efficiency, we consider 15-minute price quotes which are aggregated
from tick-by-tick price quotes leading to a sample size of n = 36855 data. The
prices are observed each trading day during the time from 9.30h to 16.00h.
Figure 1 illustrates the log-return movements over different time intervals.
The price quotes are denoted by P j
i , i = 1, . . . , n, j ∈{GM, IBM} and
the corresponding log-returns (briefly: returns) are defined by
Rj
i := log(P j
i ) −log(P j
i−1),
i = 2, . . . , n, and Rj
1 = 0, j ∈{GM, IBM}.

Interplay between Distributional and Temporal Dependence
79
-0.01
-0.05
-0.01
-0.05
95.00
95.05
95.10
95.15
Year
-0.010
-0.005
0.000
0.005
0.010
IBM return (15 min data)
Fig. 1. Stock log-returns for each 15 minutes for General Motors (GM) and In-
ternational Business Machines (IBM) over the years 1993-1998 (left plot) and over
January and February 1995 (right plot).
The right plot of Figure 1 zooms into the IBM return series at the be-
ginning of the year 1995 and reveals that the volatility clustering is less pro-
nounced than it is typically seen in foreign-exchange (FX) high-frequency
data, cf. [20]. The volatility clusters are hardly observable solely by glanc-
ing at the plot, and so we provide the autocorrelation function (ACF) for
the returns Rj
i, the squared returns (Rj
i)2, and the absolute returns |Rj
i|, re-
spectively, in Figure 2. Note that the characteristic trading pattern of almost
discrete changes of the price quote can be clearly seen in the right plot of
Figure 1.
From Figure 2 we learn that the returns themselves are not autocorrelated,
but the squared and especially the absolute returns show significant serial and
seasonal autocorrelation which is persistent over time. In particular, the time
series is not stationary. The latter seasonality has its origin in the contrast
between the beginning of the trading day, which shows high volatility, and the
middle, which shows low volatility. Figure 3 illustrates the average volatility
over the trading day for the return series of GM and IBM. Note that from
an economical point of view, the asset returns at 9.30h accumulate much
more information than the consecutive 15-minute returns. Thus, the 9.30h
returns are often excluded from the data investigation. However, since our
primary interest lies in the dependence structure and not in the economic
interpretation, we keep the 9.30h data in our analysis.
The immediate problem arising from the latter empirical observations is
how to deseasonalize the data with respect to the observed volatility struc-
ture. Two different approaches are frequently used. We may either utilize

80
N.H. Bingham and R. Schmidt
0
50
100
150
200
Lag
-0.04
-0.02
0.00
0.02
ACF
GM returns
0
50
100
150
200
Lag
-0.02-0.00 0.02 0.04 0.06 0.08 0.10 0.12
ACF
GM squared returns
0
50
100
150
200
Lag
0.00
0.05
0.10
0.15
ACF
GM absolute returns
0
50
100
150
200
Lag
-0.02 -0.01 -0.00
0.01
0.02
0.03
ACF
IBM returns
0
50
100
150
200
Lag
0.00
0.02
0.04
0.06
ACF
IBM squared returns
0
50
100
150
200
Lag
0.00
0.05
0.10
0.15
0.20
ACF
IBM absolute returns
Fig. 2. Autocorrelation function (ACF) for the returns Rj
i (left plots), squared
returns (Rj
i)2 (middle plots), and absolute returns |Rj
i| (right plots) for GM and
IBM over the years 1993-1998 with lags ranging between 1 and 200.
8.00
10.00
12.00
14.00
16.00
Time
0.000
0.004
0.008
0.012
GM
Volatility (Standard deviation)
0.1% Confidence bound
0.9% Confidence bound
8.00
10.00
12.00
14.00
16.00
Time
0.000
0.002
0.004
0.006
0.008
0.010
0.012
IBM
Volatility (Standard deviation)
0.1% Confidence bound
0.9% Confidence bound
Fig. 3. Volatilities measured by the sample standard-deviation and corresponding
empirical confidence bounds over one trading day for returns of GM and IBM over
the years 1993-1998.

Interplay between Distributional and Temporal Dependence
81
the concept of random time-change, as described in [23] (which preserves ad-
ditivity of the returns over different time intervals), or we may use volatility
weighting as in [3], [4], [54], or [20]. In the latter framework, the deseasonalized
returns ˜Rj
i are expressed by
˜Rj
i := c + Rj
i/vj
i ,
i = 1, . . . , n, j ∈{GM, IBM},
where vj
i , i = 1, . . . , n, j ∈{GM, IBM} denote the (expected) seasonal
volatilities and c refers to the mean return. The latter volatilities could be
derived via some filtering technique from time series theory. A simple approach
which is often applied (see for example [20]) estimates the squared volatilities
(vj
i )2 by
(vj
i )2 = 1
nτ
nτ

k=1

Rj
k·τ(i)

2
j ∈{GM, IBM},
where τ(i) = imod(1day) ∈{1, . . . , 27}, since we consider 27 observation times
(from 9.30h to 16.00h in 15-minute steps) per day, and nτ = [n/27]. The ACF
plots for the deseasonalized returns ˜Rj
i (provided in Figure 4) illustrate that
this approach removes the seasonality of the volatility quite well. However, the
lagged volatilities are still serially correlated, and show the typical volatility
clustering effect. Note that the absolute returns indicate the characteristic
pattern of long-range dependence.
Remark. As with the above marginal volatility weighting, we may weight
the bivariate return-vector by the expected seasonal volatility matrix. Al-
though the latter technique seems to be more appropriate for multidimen-
sional data modelling, the main results of this empirical study stay the same.
Finally, we reduce the remaining serial correlation of the volatilities of the
deseasonalized returns ˜Rj
i by fitting an univariate GARCH(1,1) model (see
[18]) to each margin separately. Indeed, the GARCH(1,1) model is the most
frequently applied GARCH model in practice. Alternatively we fit a multivari-
ate GARCH model to the bivariate deseasonalized return series. Regarding
the latter, we utilized a diagonal VEC(1,1) model (DVEC(1); see [17]) for
the deseasonalized returns ˜Rj
i. Both models assume the following covariance
dynamics:
Σi = A + B ⊗(ǫi−1ǫ′
i−1) + C ⊗Σi−1,
where the symbol ⊗stands for the Hadamard product (element-by-element
multiplication) and A, B, C ∈R2×2 (in the univariate case, these matrices
are diagonal matrices). To improve our fit, we model the error terms ǫi via a
bivariate Student t-distribution.
Although after each GARCH filtering we must reject the hypothesis of
i.i.d. residuals, the ACFs of the residual’s (co)variances imply that the ser-
ial correlation of volatilities and cross-correlations is not that significant any
more. It turns out that the residuals themselves are slightly autocorrelated

82
N.H. Bingham and R. Schmidt
0
50
100
150
200
Lag
-0.06
-0.04
-0.02
0.00
0.02
ACF
GM returns
0
50
100
150
200
Lag
0.00
0.05
0.10
0.15
ACF
GM squared returns
0
50
100
150
200
Lag
0.00
0.05
0.10
0.15
ACF
GM absolute returns
0
50
100
150
200
Lag
-0.02 -0.01 -0.00
0.01
0.02
0.03
ACF
IBM returns
0
50
100
150
200
Lag
0.00
0.05
0.10
0.15
0.20
0.25
ACF
IBM squared returns
0
50
100
150
200
Lag
0.00
0.05
0.10
0.15
0.20
ACF
GM absolute returns
Fig. 4. ACF for the volatility-weighted returns ˜Rj
i (left plots), squared returns
( ˜Rj
i)2 (middle plots) and absolute returns | ˜Rj
i| (right plots) for GM and IBM over
the years 1993-1998 with lags ranging between 1 and 200.
over the first lag of 15min; however, this time frame is too short for significant
arbitrage opportunities.
Remark. According to our empirical study, the main results stay the same
irrespective of the choice of a multivariate or an univariate GARCH model.
4.2 Excursion: Analyzing the temporal dependence
with Kendall’s tau
In Figures 2 and 4 we analyzed the ACF to draw conclusions about the tem-
poral dependence of the underlying (volatility weighted) asset returns. Espe-
cially Figure 2 indicates that there might be an unusually large dependence
between the return data with a lag of k-days (i.e. lag= k · 27). Undoubtedly
there is a larger dependence at this special lag, but the correlation coeffi-
cient, which can only measure linear dependence, exaggerates the magnitude
enormously. A standardization of the bivariate return data to approximately
uniformly distributed margins (via the quasi-empirical distribution function
which is again explained in formula (4.10) below) gives a better picture of the
respective serial dependence. Figure 5 shows that all large peaks in the ACF

Interplay between Distributional and Temporal Dependence
83
disappear after this standardization. The sensitivity of the correlation coeffi-
cient under monotone increasing transformations is thus misleading as to the
proper analysis of the temporal dependence structure. This is especially so if
the dependence is non-linear, as it is in our case. As an alternative, we advo-
cate a new ACF based on the scale-invariant dependence measure Kendall’s
tau. Note that the definition of Kendall’s tau requires a common continuous
distribution function; however, the respective marginal distribution functions
might be discontinuous.
Definition 7 (ACF based on Kendall’s tau). Let (Yi)i∈N denote a se-
quence of random variables (or univariate time series). The autocorrelation
with lag j of some Yi, i = j + 1, . . . based on Kendall’s tau is defined by
τj = IP((Yi −¯Yi)(Yi−j −¯Yi−j) > 0) −IP((Yi −¯Yi)(Yi−j −¯Yi−j) < 0),
where ( ¯Yi, ¯Yi−j)′ is an independent copy of (Yi, Yi−j)′ which has a common
continuous distribution function. The plot of τj against j is called the ACF
based on Kendall’s tau.
The sample autocorrelation with lag j based on Kendall’s tau is de-
fined as the sample version of Kendall’s tau derived from the realizations of
(Yi, Yi−j)′, i = j + 1, . . . , n (see formula (2.2)).
1
12 23 34 45 56 67 78 89 100
Lag
-0.01
0.04
0.09
0.14
ACF
GM squared returns
1
12 23 34 45 56 67 78
100
Lag
-0.01
0.04
0.09
0.14
ACF based on standardized data
GM squared returns
89
1
12 23 34 45 56 67 78 89 100
Lag
-0.01
0.04
0.09
0.14
Kendall’s tau - ACF
GM squared returns
Fig. 5. ACF of the squared returns (RGM
i
)2 (left plot), ACF of the squared returns
which are standardized by the quasi-empirical distribution function (middle plot)
and ACF based on Kendall’s tau of the squared returns (RGM
i
)2 over the years
1993-1998 with lags ranging between 1 and 100.
4.3 Analyzing the quasi-empirical copula
We return to our question:
How much did we change the distributional dependence structure?
Let {(X1
i , X2
i )′, i = 1, . . . , n} denote some bivariate time series. Consider
the transformed series
{(F1,n(X1
i ), F2,n(X2
i ))′, i = 1, . . . , n},
(4.10)

84
N.H. Bingham and R. Schmidt
where Fj,n is n/(n + 1) times the quasi-empirical distribution function of
{(Xj
i ), i = 1, . . . , n}, j = 1, 2. We apply transformation (4.10) to the original
GM-IBM returns Rj
i, to the volatility-weighted returns ˜Rj
i, and to the GARCH
residuals of the volatility-weighted returns.
The results are illustrated in Figure 6. Note that only for the third data
set, the underlying data are approximate realization of an empirical copula
since these data are closest to i.i.d. For the second data set, the volatility
weighted returns, we could impose some ergodicity or mixing conditions to
ensure the weak convergence of the quasi-empirical copula to the correspond-
ing real copula (see for example [28] or [34]). The latter seems to be not
possible for the first data set because the time series is not even stationary.
However, transformation (4.10) gives a better indication of the underlying
distributional dependence structure than, for example, a simple scatter plot.
Although, any interpretations from related dependence measures should be
considered very carefully.
The left plots of Figure 6 illustrate the returns Rj
i, the volatility weighted
returns ˜Rj
i, and the GARCH residuals of the volatility weighted returns of
GM and IBM after they have been transformed (or standardized) according
to formula (4.10). Thus, the plots refer to the respective quasi-empirical copula
density. The characteristic cross in the middle of the two upper-left plots indi-
cates the atomic mass of zero returns; i.e. time points where the stocks are not
traded. Note that the copula is not uniquely defined for discontinuous distri-
bution functions. All other modes of the marginal return distributions, which
have been present in Figure 1, are not observable in this plot, which shows
that the latter transformation really removes the characteristics of the mar-
ginal distributions. We would like to point out the intensifying accumulation
of data points in the lower-left and upper-right corner of all quasi-empirical
copula density plots. This feature might be an indicator for tail dependence
or, in other words, dependence of extreme events. In the next section we
solely concentrate on the problem of whether tail dependence changes heavily
after filtering. Note, that the quasi-empirical copula density of the GARCH
residuals does not possess the characteristic cross.
The plots on the right side of Figure 6 indicate the temporal evolvement of
the GM margins ˆFGM(·) corresponding to the respective quasi-empirical cop-
ula density given in the left plots. The strong impact of the filtering becomes
quite clear in these plots. For example the characteristic trading pattern of
discrete percentual changes of the price quotes, as illustrated by the lines in
the upper-right plot (see also Figure 1), vanishes completely after the filtering.
Summarizing the observations, Figure 6 clearly shows that the distribu-
tional dependence structures, measured via the quasi-empirical copula, differ
completely from each other. This indicates that the filtering has a strong
impact on the analysis of distributional dependence and on the interpreta-
tional power of common dependence measures. Wrong or misleading economic
interpretations can be drawn, if no attention is paid to this basic insight

Interplay between Distributional and Temporal Dependence
85
0.0
0.0
0.2
0.4
IBM
0.6
0.8
1.0
0.2
0.4
0.6
GM
0.8
1.0
93
0.0
0.2
0.4
0.6
0.8
1.0
GM
94
95
96
Year
97
98
0.0
0.0
0.2
0.4
IBM
0.6
0.8
1.0
0.2
0.4
0.6
GM
0.8
1.0
93
0.0
0.2
0.4
0.6
0.8
1.0
GM
94
95
96
Year
97
98
0.0
0.0
0.2
0.4
IBM
0.6
0.8
1.0
0.2
0.4
0.6
GM
0.8
1.0
93
0.0
0.2
0.4
0.6
0.8
1.0
GM
94
95
96
Year
97
98
Fig. 6. Quasi-empirical copula density (left plots) of the returns Rj
i (upper plots),
the volatility-weighted returns ˜Rj
i (middle plots), and the GARCH residuals of the
volatility-weighted returns ˜Rj
i (lower plots) for GM and IBM over the years 1993-
1998 and the corresponding transformed margins ˆFGM(·) (right plots).
(see also [35] for further statistical pitfalls in dependence modelling). In order
to underpin the so-far obtained conclusions, we discuss the impact of filtering
on the estimation of tail dependence.
4.4 Analyzing the tail dependence
Because of the complicated temporal-dependence structure of the considered
GM-IBM high-frequency asset returns, we favor an estimator which does not
depend on any distributional assumptions.

86
N.H. Bingham and R. Schmidt
Figure 7 illustrates the estimates ˆλL,n(k) of the lower tail-dependence
coefficient λL (TDC) for various thresholds k for the returns Rj
i, the
volatility-weighted returns ˜Rj
i, and the GARCH residuals of the volatility-
weighted returns of GM and IBM over the years 1993-1998. According to the
regular variation property of tail-dependent distributions (see [59] for more
details), tail dependence is present in a bivariate i.i.d. data set if the plot
of ˆλL,n(k) for various thresholds k shows a characteristic plateau for small
k. This characteristic plateau is typically located between a higher variance
of the estimator for smaller thresholds and a larger bias of the estimator
for bigger thresholds. The estimate of the lower TDC and the corresponding
threshold k is chosen according to the latter plateau.
0
200
400
600
800
1000
Threshold k 
0.0
0.1
0.2
0.3
Estimate lambda_L(k)
0
200
400
600
800
1000
Threshold k
0.0
0.1
0.2
0.3
Estimate lambda_L(k)
0
200
400
600
800
1000
Threshold k
0.0
0.1
0.2
0.3
Estimate lambda_L(k)
Fig. 7. Estimates ˆλL,n(k) of the lower tail-dependence coefficient for various thresh-
olds k for returns Rj
i (upper left plot), volatility-weighted returns ˜Rj
i (upper right
plot), and GARCH residuals of the volatility-weighted returns (lower plot) for GM
and IBM over the years 1993-1998.
Figure 7 indicates that the original GM-IBM returns are lower-tail depen-
dent with ˆλL,n = 0.15. The volatility weighted returns show less pronounced
tail dependence with ˆλL,n = 0.1. Finally, the GARCH residuals of the volatil-
ity weighted returns are lower-tail independent according to the absence of
any plateau; see the lower plot in Figure 7. However, the original returns and
the volatility weighted returns are by no means i.i.d. Therefore the question is:
Are the characteristic plateaus induced by the various temporal dependence

Interplay between Distributional and Temporal Dependence
87
structures of the data? For example, [20] stop after the volatility weighting
and draw several conclusions about the distributional dependence, although
their deseasonalized high-frequency data set still shows a pronounced volatil-
ity clustering. In a forthcoming paper, we will dig into the question how much
tail dependence can be introduced into a tail independent data set by applying
certain transformations (which cause temporal dependence).
In contrast, we point out that the correlation coefficient is not significantly
different for all three data series. The original GM-IBM returns have a corre-
lation coefficient of 0.24, the volatility weighted returns possess a correlation
coefficient of 0.23, and the GARCH residuals of the volatility weighted returns
end up with a correlation coefficient of 0.22. This again unmistakably shows
that the interpretational power of distributional dependence measures/models
(such as copulas, Kendall’s tau or tail dependence) has to be handled very
carefully if the analyzed data are not i.i.d.
5 Conclusion
In this paper, we have surveyed and advocated the usage of copulas with a par-
ticular view towards financial applications. The recently developed concepts
of tail dependence and tail copulas are presented and some new results on sta-
tistical inference are stated. The assumption of i.i.d. data, which is necessary
in order to obtain the latter results, turns out to be difficult to obtain for real
financial time series. In fact, we illustrate for the GM-IBM high-frequency
data set that the distributional dependence is very sensitive towards common
filtering methods such as GARCH filtering. We conclude that the analysis of
the distributional dependence of multidimensional financial data with tempo-
ral dependence is a rich and promising area, in which much remains to be
done.
Acknowledgements
We would like to thank Yuri Kabanov for his valuable comments on an earlier
version of this paper. Rafael Schmidt gratefully acknowledges support by a
fellowship within the Postdoc-Programme of the German Academic Exchange
Service DAAD (www.daad.de).
References
1. Alexander, C.: Market Models: A Guide to Financial Data Analysis. John Wiley
and Sons (2001)
2. Andersen, T.G., Bollerslev, T., Diebold, F.X., Labys, P.: The distribution of
exchange rate volatility. Journal of the American Statistical Association, 96,
42-55 (2001)

88
N.H. Bingham and R. Schmidt
3. Andersen, T.G., Bollerslev, T.: Intraday periodicity and volatility persistence in
financial markets. Journal of Empirical Finance, 4(2-3), 115-158 (1997)
4. Andersen, T. G., Bollerslev, T.: Deutsche Mark-Dollar volatility: intraday ac-
tivity patterns, macroeconomic announcements, and longer run dependencies.
Journal of Finance, 53(1), 219-265 (1998)
5. An´e, T., Kharoubi, C.: Dependence Structure and Risk Measure. Journal of
Business, 76(3), 411-438 (2003)
6. Areal, N.P., Taylor, S.J.: The realised volatility of FTSE-100 futures prices.
Forthcoming in Journal of Futures Markets, 22 (2002)
7. Bai, X., Russell, J.R., Tiao, G.C.: Beyond Merton’s utopia: effects of non-
normality and dependence on the precision of variance estimates using high-
frequency financial data. Graduate School of Business, University of Chicago
(2000)
8. Baringhaus, L.: Testing for spherical symmetry of a multivariate distribution.
Annals of Statistics 19, 899–917 (1991)
9. Barndorff-Nielsen, O.E., Shephard, N.: Econometric analysis of realised volatil-
ity and its use in estimating stochastic volatility models. Journal of the Royal
Statistical Society, Series B, 64, 253–280 (2002)
10. Barndorff-Nielsen, O.E., Shephard, N.: Econometric analysis of realised covari-
ation: high frequency covariance, regression and correlation in financial eco-
nomics. Econometrica, 72, 885–925 (2004)
11. Basel Committee on Banking Supervision: The New Basel Capital Accord. BIS
Basel, Switzerland URL: http://www.bis.org/bcbs (2003)
12. Beran, R.: Testing for ellipsoidal symmetry of a multivariate density. Annals of
Statistics, 7, 150–162 (1979)
13. Bingham, N.H., Kiesel,R.: Modelling asset return with hyperbolic distribu-
tions. In: Knight, J., Satchell, S. (eds.) Asset return distributions. Butterworth-
Heinemann, pp. 1–20 (2001)
14. Bingham, N.H., Kiesel, R.: Semi-parametric modelling in finance: theoretical
foundation. Quantitative Finance 2, 241–250 (2002)
15. Bingham, N.H., Kiesel, R., Schmidt, R.: Semi-parametric modelling in Finance:
Econometric applications. Quantitative Finance, 3(6), 426–441 (2003)
16. Bluhm, C., Overbeck, L., Wagner, C.: An Introduction to Credit Risk Modelling.
Chapman & Hall (2003)
17. Bollerslev, T., Engle, R.F., Wooldridge, J. M.: A Capital-Asset Pricing Model
with Time-Varying Covariances. Journal of Political Economy, 96, 116–131
(1988)
18. Bollerslev, T.: Generalized Autoregressive Conditional Heteroskedasticity. Jour-
nal of Econometrics, 31, 307–327 (1986)
19. Bouy´e, E., Durrleman, V., Nikeghbali, A., Riboulet, G., Roncalli, T.: Copu-
las for finance: A reading guide and some applications. Groupe de Recherche
Op´erationnelle, Cr´edit Lyonnais, Technical report (2000)
20. Breymann, W., Dias, A., Embrechts, P.: Dependence structures for multivariate
high-frequency data in finance. Quantitative Finance, 3(1), 1–16 (2003)
21. Campbell, J., Lo, A., MacKinlay, C.: The Econometrics of Financial Markets.
Princeton University Press, New Jersey (1997)
22. Campbell, R., Koedijk, K., Kofman, P.: Increased Correlation in Bear Markets.
Financial Analysts Journal, Jan-Feb, 87–94 (2002)
23. Dacorogna, M.M., Gen¸cay, R., M¨uller, U.A., Olsen, R.B., Pictet, O.V.: An In-
troduction to HighFrequency Finance. Academic Press, San Diego (2001)

Interplay between Distributional and Temporal Dependence
89
24. Darsow,W., Nguyen, B., Olsen, E.: Copulas and Markov Processes. Illinois Jour-
nal of Mathematics, 36, 600–642 (1992)
25. De Haan, L., Stadtm¨uller, U.: Generalized regular variation of second order.
Journal of the Australian Mathematical Society, 61, 381–395 (1996)
26. Deheuvels, P.: La fonction de d´ependance empirique et ses propri´et´es. Acad.
Roy. Belg., Bull. C1 Sci. 5i`eme s´er, 65, 274–292 (1979)
27. Deheuvels, P.: A nonparametric test for independence. Pub. Inst. Stat. Univ.
Paris, 26(2), 29–50 (1981)
28. Dehling, H., Mikosch, T., S¨orensen, M.: Empirical Process Techniques for De-
pendent Data. Birkh¨auser Verlag (2002)
29. Ding, Z., Granger, C.W.J.: Modeling Volatility Persistence of Speculative Re-
turns: A New Approach. Journal of Econometrics, 73, 185–215 (1996)
30. Eberlein, E.: Application of generalized hyperbolic L´evy motions to finance. In:
Barndorff-Nielsen, O., Mikosch, T., Resnick, S. (eds.) L´evy Processes: Theory
and Applications. Birkh¨auser Verlag, pp. 319–337 (2001)
31. Embrechts, P., McNeil, A., Straumann, D.: Correlation and Dependency in Risk
Management: Properties and Pitfalls. In: Dempster, M.A.H. (ed.) Risk Man-
agement: Value at Risk and Beyond. Cambridge University Press, pp. 176–223
(2002)
32. Embrechts, P., Lindskog, F., McNeil, A.: Modelling Dependence with Copulas
and Applications to Risk Management. In: Rachev, S. (ed.) Handbook of Heavy
Tailed Distributions in Finance. Elsevier, pp. 329–384 (2001)
33. Fang, K.T., Kotz, S., Ng, K.W.: Symmetric multivariate and related distribu-
tions. Chapman & Hall, London (1990)
34. Fermanian, J.D.: Goodness of fit tests for copulas, Working Paper CREST 2003-
34. Forthcoming in J. Multivariate Analysis (2003)
35. Fermanian, J.D., Scaillet, O.: Some statistical pitfalls in copula modeling for
financial applications. Technical report (2004)
36. Fermanian, J.D., Radulovi´c, D., Wegkamp, M.: Weak convergence of empirical
copula processes. Working Paper CREST 2002-06, Forthcoming in Bernoulli
(2002)
37. Frahm, G., Junker, M., Schmidt, R.: Estimating the Tail Dependence Coeffi-
cient. Caesar Center Bonn, URL: http://stats.lse.ac.uk/schmidt, Technical Re-
port 38 (2003)
38. Frey, R., McNeil, A.: Modelling dependent defaults. ETH Zuerich, http://e-
collection.ethbib.ethz.ch/show?type=bericht&nr=273, Working Paper (2001)
39. G¨anssler, P., Stute, W.: Seminar on Empirical Processes. DMV Seminar 9,
Birkh¨auser, Basel (1987)
40. Genest, C., R´emillard, B.: Tests of Independence and Randomness Based on the
Empirical Copula Process. Test, 12(1), in print (2004)
41. Genest,
C.,
Rivest,
L.P.:
Statistical
inference
procedures
for
bivariate
archimedean copulas. Journal of the American Statistical Association, 88, 1034–
1043 (1993)
42. Genest, C., Ghoudi, K., Rivest, L.P.: A semiparametric estimation procedure
of dependence parameters in multivariate families of distributions. Biometrika,
82, 543–552 (1995)
43. Goorgergh, R.W.J., Genest, C., Werker, B.: Multivariate Option Pricing Using
Dynamic Copula Models, Working Paper (2004)
44. Joe, H.: Multivariate Models and Dependence Concepts. Chapman and Hall,
London (1997)

90
N.H. Bingham and R. Schmidt
45. Junker, M., May, A.: Measurement of aggregate risk with copulas. Technical
report, Caesar Center Bonn (2002)
46. Karolyi, G.A., Stulz, R.M.: Why Do Markets Move Together? An Investigation
of U.S.-Japan Stock Return Comovements. Journal of Finance, 51, 951–989
(1996)
47. Laurent, J.-P., Gregory, J.: Basket Default Swaps, CDO‘s and Factor Copulas.
Working paper (2003)
48. Li, D.X.: On Default Correlation: A Copula Function Approach. Journal of
Fixed Income, 9, 43–54 (2000)
49. Longin, F., Solnik, B.: Extreme Correlation of International Equity Markets.
Journal of Finance, LVI, 649–676 (2001)
50. Madan, D.B., Seneta, E.: The Variance-Gamma (VG) model for share market
returns. Journal of Business, 511-524 (1990)
51. Maheu, J.M., McCurdy, T.H.: Nonlinear features of realised FX volatility., forth-
coming in Economics and Statistics, 83 (2001)
52. Malevergne, Y., Sornette, D.: Minimizing Extremes. RISK, November issue,
129–133 (2002)
53. Manzotti, A., Perez, F.J., Quiroz, A.J.: A statistic for testing the null hypothesis
of elliptical symmetry. Journal of Multivariate Analysis, 81, 274–285 (2002)
54. Martens, M., Chang, Y.C., Taylor, S.J.: A comparison of seasonal adjustment
methods when forecasting intraday volatility. Journal of Financial Res., 15(2),
283-299 (2002)
55. Nelsen, R.B.: An Introduction to Copulas. Springer, New York (1999)
56. Ong, M.K.: Internal Credit Risk Models. Risk Books, Haymarket (1999)
57. Patton, A.: Modelling Time-Varying Exchange Rate Dependence Using the Con-
ditional Copula. UCSD, Working Paper 2001-09 (2001)
58. Schmidt, R.: Tail dependence for elliptically contoured distributions. Mathe-
matical Methods of Operations Research, 55(2), 301-327 (2002)
59. Schmidt, R., Stadtm¨uller, U.: Nonparametric estimation of tail dependence.
London School of Economics, www.lse.ac.uk/collections/statistics, Research re-
port 101 (2003)
60. Sch¨onbucher, P.: Credit Derivatives Pricing Models. Wiley Publ. (2003)
61. Sklar, A.: Fonctions de r´epartition `a n dimensions et leurs marges. Publ. Inst.
Statist. Univ. Paris, 8, 229–231 (1959)
62. Stute, W.: The oscillation behavior of empirical processes: The multivariate
case. Annals of Probability, 12(2), 361–379 (1984)
63. Van der Vaart, A.W., Wellner, J.A.: Weak Convergence and Empirical
Processes. Springer, New York (1996)

Asymptotic Methods for Stability Analysis
of Markov Dynamical Systems with Fast
Variables
Jevgenijs CARKOVS1 and Jordan STOYANOV2
1 Institute of Information Technologies, Technical University Riga
LV–1048 Riga, Latvia.
carkovs@livas.lv
2 School of Mathematics & Statistics, University of Newcastle
Newcastle upon Tyne NE1 7RU, U.K.
jordan.stoyanov@ncl.ac.uk
Summary. We deal with two scale stochastic dynamical systems under Markov
perturbations. Our goal is to study asymptotic stability properties of the solutions
of such systems. We apply averaging procedures to obtain simpler processes which
are then used for the stability analysis of both the slow and the fast components of
the original system.
Key words: two-scale system, slow and fast motion, Markov perturbation, sto-
chastic stability, exponential stability, averaging procedure, linear approximation,
diffusion approximation, Lyapunov function
Mathematics Subject Classification (2000): 60H10, 93E15, 34F05
1 Introduction: Model and Problems
The averaging principle and diffusion approximation procedures are among
the most frequently used asymptotic methods for analysis of nonlinear dy-
namical systems subjected to random perturbations [1], [5], [6], [9], [13], [15],
[16], [18], [19], [20]. It has been recognized that the averaging principle is a
powerful tool for analyzing interesting phenomena in the engineering sciences,
for example, when studying asymptotically stable multifrequency oscillations,
loss of stability due to parametric resonance, etc., see [17] and the references
therein. This approach, supplemented recently by probabilistic limit theorems,
was used not only in engineering sciences [2] but also applied in social sciences
such as economics and medicine [22], [8], [20]. The limit theorems obtained
in this area allow us to construct simpler dynamical systems, which are suc-
cessfully used for approximate analysis of the initial system on finite time

92
J. Carkovs, J. Stoyanov
intervals and also to describe the asymptotic behavior of the phase coordi-
nates as the time t →∞, see [1], [10], [11], [13], [20]. It is worth mentioning
that mostly in engineering applications only a part of the coordinates have
limits as t →∞, while the rest coordinates undulate and do not have any
limit [2]. This creates some difficulties when applying asymptotic methods of
nonlinear dynamics and probabilistic limit theorems.
Let us describe the model which we are going to study in this paper.
We introduce a “small” positive parameter ε, where ε ∈(0, ε0), for some
fixed ε0 > 0. We assume that the system variables, as functions of time,
are separated into a fast component (called “radial motion”), and a slow
component (called “rotation”). The fast component has “velocity” which is
proportional to a negative power of ε, while the slow component has a limit
as ε →0. We also assume that the dynamical system depends on other fast
random variables (that means functions of t/ε) modelled as an ergodic Markov
process [13], [15], [19]. Thus we study a system of random differential equations
of the following form:
dxε(t)
dt
= F(xε(t), yε(t), ξε(t), ε),
(1.1)
dyε(t)
dt
= 1
εH(yε(t), ξε(t), ε), t ≥0.
(1.2)
Here ε ∈(0, ε0), F(x, y, z, ε) and H(y, z, ε) are vector-functions, x ∈Rn,
y ∈Rm, z ∈G, and ξε = (ξε(t), t ≥0) is a homogeneous right continuous
ergodic Markov process on some compact phase space G with a weak infini-
tesimal operator Qε and an invariant measure µ, which is the same for all ε. If
F(x, y, z, ε) and H(y, z, ε) are sufficiently smooth functions, then the Cauchy
problem for the system (1.1)–(1.2) with initial conditions xε(s) = x, yε(s) = y
and ξε(s) = z, where s ≥0, has a unique solution xε(t) = xε(s, t, x, y, z),
yε(t) = yε(s, t, x, y, z) for any t ≥s, x ∈Rn, y ∈Rm, z ∈G. Let us as-
sume that the trivial solution xε(t) ≡0 ∈Rn is an equilibrium point for the
slow motion (1.1), that is, F(0, y, z, ε) ≡0. One of our goals is to analyze
asymptotic stability properties of this equilibrium. For completeness of the
presentation we recall some definitions from the classical book [12]. In these
definitions ε is fixed and we are interested in the stability of the trivial solu-
tion of (1.1) uniformly in ε ∈(0, ε0). Examples of systems which are stable in
one sense but not in another one can be seen in [12].
We say that equation (1.1), or that its trivial solution, is:
•
locally stable almost surely (a.s.), if for any s ≥0, η > 0 and β > 0, there
exists δ > 0 such that the inequality
sup
y∈Rm, z∈G
P

sup
t≥s
|xε(s, t, x, y, z)| > η

< β
(1.3)
is satisfied for all x in the ball Bδ(0) := {u ∈Rn : |u| < δ};

Stability Analysis of Markov Dynamical Systems
93
•
locally asymptotically stochastically stable, if it is locally a.s. stable and
there exists γ > 0 such that the trajectories, which do not leave the ball
Bγ(0), tend to 0 in probability, as t →∞, that is, for any c > 0 and fixed
other initial data, we have
lim
t→∞P[|xε(s, t, x, y, z)| > c, {xε(s, t, x, y, z), t ≥s} ⊂Bγ(0)] = 0;
•
asymptotically stochastically stable, if it is locally a.s. stable and for any
x ∈Rn, s ∈R+, and c > 0, the following relation holds:
lim
T →∞
sup
y∈Rm, z∈G
P

sup
t>T
|xε(s, t, x, y, z)| > c

= 0;
(1.4)
•
exponentially p-stable, if there are numbers M > 0, γ > 0 such that for
any x ∈Rn, y ∈Rm, z ∈G, s ≥0 and t > s one holds:
E[|xε(s, t, x, y, z)|p] ≤M|x|p e−γ(t−s).
(1.5)
The paper is organized as follows. In Section 2 we prove that for linear Markov
dynamical systems, the asymptotic stochastic stability of the equilibrium is
equivalent to the exponential p-stability for sufficiently small p > 0. In Sec-
tion 3 we show that the exponential p-stability of the linearized Markov system
in a neighborhood of its equilibrium state, guarantees the asymptotic (local)
stochastic stability of this equilibrium. These results are similar to results in
[19] and [20]. However, we have included them here for a better understand-
ing of our approach and for describing a modification of the second Lyapunov
method for stochastic stability analysis. Based on the results in Sections 2
and 3, we can analyze the equilibrium stability of the slow motion by rewrit-
ing the system (1.1)–(1.2) in the following form:
dxε(t)
dt
= [A0(yε(t), ξε(t)) + εA1(yε(t), ξε(t))]xε(t),
(1.6)
dyε(t)
dt
= 1
εh−1(yε(t), ξε(t)) + h0(yε(t), ξε(t)), t ≥0.
(1.7)
Here ξε = (ξε(t), t ≥0) is a Markov process with infinitesimal operator
Qε =
1
ε2 Q. The operator Q is supposed to be closed with spectrum σ(Q)
split into two parts, σ(Q) = σ−ρ(Q) ∪{0}, where σ−ρ(Q) ⊂{Reλ ≤−ρ < 0}
and zero eigenvalue has multiplicity one. This assumption, see [4], guaran-
tees ergodicity of Markov processes defined by infinitesimal operators
1
ε2 Q
and with the same invariant measure µ. To avoid cumbersome formulas an
averaging in the Markov phase coordinate z ∈G of any function f(x, y, z)
with respect to the invariant measure µ will be denoted by ¯f, that is,
¯f(x, y) :=

G f(x, y, z)µ(dz). In Section 4 we discuss some results for the fast
motion assuming that ¯h−1(y) ≡0. In this case, under some assumptions, the
stability analysis is based on an averaging procedure for the slow motion (1.6)
with a diffusion approximation of the fast motion (1.7):

94
J. Carkovs, J. Stoyanov
d¯x(t)
dt
= ¯A0(ˆy(t)) ¯x(t),
(1.8)
dˆy(t) = a(ˆy(t))dt + σ(ˆy(t))dw(t), t ≥0.
(1.9)
The coefficients a(y), σ(y) are defined by the functions in the right-hand side
of (1.7), being respectively the potential of the operator Q and averaging with
respect to the invariant measure µ. We prove that the asymptotic stochastic
stability of the slow motion (1.1) follows from the exponential p-stability of
the random differential equation (1.8).
2 Stochastic Stability of Linear Differential Equations
with Markov Coefficients
In this section we deal with the following linear differential equation in Rn:
dx(t)
dt
= A(y(t)) x(t), t ≥0.
(2.1)
Here A(y), y ∈Rm is a continuous bounded matrix-valued function and y(t),
t ≥0 is a Y–valued stochastically continuous Feller Markov process with weak
infinitesimal operator Q and we assume that Y ⊂Rm. The pair {x(t), y(t)},
t ≥0 forms, see [19], a homogeneous stochastically continuous Markov process
whose weak infinitesimal operator, denoted by L0, is defined as follows:
L0v(x, y) = ⟨A(y)x, ∇x⟩v(x, y) + Qv(x, y).
(2.2)
It is clear that there exists a family {X(s, t, y), 0 ≤s ≤t}, of matrix-valued
functions defined by the equality X(s, t, y)x = x(s, t, x, y), where x(s, t, x, y),
s ≤t, denoted simply by x(t), is the solution of the Cauchy problem for (2.1)
under the conditions x(s) = x and y(s) = y. The matrices X(s, t, y) also
satisfy equation (2.1) for all t > s and the initial condition X(s, s, y) = I,
where I is the unit matrix of order n. This matrix family has the evolution
property:
X(s, t, y) = X(s, τ, y(τ))X(τ, t, y), y ∈Y, 0 ≤s ≤τ ≤t.
(2.3)
The Lyapunov exponent, or p-index, λ(p), of equation (2.1) is defined by
λ(p) = sup
x,y
lim
t→∞
1
pt ln E[|X(s, t, y)x|p].
(2.4)
It is not difficult to show that the exponential p-stability of the trivial solution
of equation (2.1) is equivalent to the condition λ(p) < 0. Since for any positive
p1 < p2 we have (E[|X(t, s, y)x|p1])1/p1 ≤(E[|X(t, s, y)x|p2])1/p2 (Lyapunov
inequality), then p1 < p2 implies that λ(p1) ≤λ(p2), and hence λ(p) is a
monotone decreasing function as p decreases to 0. In this section we will prove
that the asymptotic stochastic stability of (2.1) is equivalent to the following
condition: there exists a number p0 > 0, such that λ(p) < 0 for all p ∈(0, p0).

Stability Analysis of Markov Dynamical Systems
95
Lemma 2.1. If equation (2.1) is asymptotically stochastically stable, then it
is exponentially p-stable for all sufficiently small positive p.
Proof. In the definition of a.s. stability we take η = 1, β = 1
2 and choose α > 0
so small that supx,y P

supt≥0 |X(0, t, y)x| > 1

< 1
2 for |x| ≤2−α, y ∈Y.
Since equation (2.1) is linear, then supx,y P

supt≥0 |X(0, t, y)x| > 2kα
< 1
2
for |x| ≤2−α(k−1), y ∈Y and any k ∈N. Let us introduce the following
notation:
gk :=
sup
|x|≤1, y∈Y
P

sup
t≥0
| X(0, t, y)x| ≥2kα

.
The pair {x(t), y(t)}, t ∈R+ is a stochastically continuous Markov process.
Therefore for any x ∈B1(0) there exits a time τ1(x) such that the trajectory
x(0, t, x, y) leaves the ball B1(0). Hence
gk+1 =
sup
|x|≤1, y∈Y
∞

s=0

|u|=2kα, v∈Y
Px,y(τ1(x) ∈ds, x(s) ∈du, y(s) ∈dv)
× P

sup
t≥0
|X(0, t, v)u| > 2(k+1)α

≤
sup
|x|≤2kα, y∈Y
P

sup
t≥0
|X(0, t, y)x| > 2(k+1)α

×
sup
|x|≤1, y∈Y
∞

s=0

|u|=2kα, v∈Y
Px,y(τ1(x) ∈ds, x(s) ∈du, y(s) ∈dv)
≤1
2
sup
|x|≤1, y∈Y
P

sup
t≥0
|X(0, t, y)x| ≥2kα

= 1
2gk
and therefore gk ≤2−k for any k ∈N. Define ζ(x, y) := supt≥0 |x(0, t, x, y)|p.
It is easy to see that for all p > 0, x ∈Rn and y ∈Y one can write
E[ζ(x, y)] ≤|x|p sup
|x|≤1
E[ζ(x, y)] ≤
∞

k=1
2kαpP

sup
t≥0
|x(0, t, x, y)| ≥2(k−1)α

.
Therefore E[ζ(x, y)] ≤∞
k=1 2kαp2−k|x|p := K1|x|p for all x ∈Rn, y ∈Y
and p ∈(0, α−1). The assumption in Lemma 2.1 implies that the solu-
tion x(0, t, x, y), t ≥0 of (2.1) tends to 0 a.s. as t →∞uniformly in
y ∈Y. By the Lebesgue Theorem we conclude that limt→∞supy∈Y E[|x(s, s+
t, x, y)|p] = 0, for all x ∈Rn and p ∈(0, α−1). Moreover, it is not diffi-
cult to verify that this convergence is uniform in x ∈B1(0) and s ≥0, i.e.
limt→∞supx∈B1(0), y∈Y E[|x(s, s+t, x, y)|p] = 0. Now we can choose a number
T so large that supy∈Y E[|x(s, s + t, x, y)|p] ≤|x|pe−1. Further, by using the
inequality

96
J. Carkovs, J. Stoyanov

Rn

Y
P((k −1)T, x, y, du, dv)E[|x(0, T, u, v)|p] ≤1
eE[|x(0, (k −1)T, x, y)|p],
where P(t, x, y, du, dv) is the transition probability of the homogeneous
Markov process {x(t), y(t)}, t ≥0, one can write
E[|x(0, t, x, y)|p]≤K1e−[t/T ]T |x|p,
where [t/T] stands for the integer part of the real number t/T. This completes
the proof.
⊓⊔
The behavior of the solution of (2.1) for t ≥u with x(u) = x, y(u) = y,
can be studied by using the well-known Dynkin formula:
E(u)
x,y[v(x(t), y(t))] = v(x, y) +
t

u
E(u)
x,y[L0v(x(s), y(s))] ds.
(2.5)
Sometimes it is necessary to use Lyapunov functions depending also on the
time argument t. If v(t, x, y), as a function of x and y, belongs to the domain of
the infinitesimal operator L0 and has continuous t-derivative, we can rewrite
formula (2.5) in the form
E(u)
x,y[v(t, x(t), y(t))] = v(u, x, y) +
 t
u
E(u)
x,y
 ∂
∂s + L0

v(s, x(s), y(s))

ds.
(2.6)
Lemma 2.2. The trivial solution of equation (2.1) is exponentially p-stable
if and only if there exists a Lyapunov function v(x, y) and a number p > 0
such that for some positive constants c1, c2, c3 and for all x ∈Rn, y ∈Y, the
following two conditions are satisfied:
c1|x|p ≤v(x, y) ≤c2|x|p,
L0v(x, y) ≤−c3|x|p.
(2.7)
Proof. Suppose that there exists such a Lyapunov function. This implies that
 ∂
∂s + L0

 
v(x, y) ec3t/c2
≤0, which in combination with formula (2.6) yields
Ex,y[v(x(t), y(t)) ec3t/c2] ≤v(x, y) ≤c2 |x|p for all t > 0, x ∈Rn and y ∈Y.
Hence Ex,y[|x(t)|p] ≤(c2/c1) e−c3t/c2 |x|p and we conclude that equation (2.1)
is exponentially p-stable. By using the solutions x(s, s + t, x, y) of (2.1), we
can define, for any T > 0, the function
v(x, y) :=
T

0
E[|x(s, s + t, x, y)|p] dt,
(2.8)
which does not dependent on s because of the homogeneity of the Markov
process y(t). Since the matrix A(y) is uniformly bounded, i.e. supy∈Y ∥A(y)∥:=

Stability Analysis of Markov Dynamical Systems
97
a < ∞, it is easy to verify that the function v(x, y) satisfies the first condition
in (2.7). Let L0 be the weak infinitesimal operator of the pair {x(t), y(t)},
t ≥0. If the trivial solution of (2.1) is exponentially p-stable, one can write
the relations
L0v(x, y) = lim
δ→0
1
δ


T

0
Ex,y{Ex(δ),y(δ)[|x(t + δ)|p]} dt −
T

0
Ex,y[|x(s)|p] ds


= Ex,y[|x(T)|p] −|x|p ≤(M e−γT −1)|x|p,
where M and γ are the constants in the definition of the exponential p-
stability. Now we take T = (ln 2+ln M)/γ, and see that the proof is completed.
⊓⊔
Corollary 2.1. Under the conditions in Lemma 2.2, the trivial solution of
equation (2.1) is asymptotically stochastically stable.
Proof. Applying formula (2.6) to the function ¯v(t, x, y) = v(x, y) ec3t/c2 we
see that the random process θ(t) := v(x(t), y(t)) ec3t/c2, t ≥0 is a positive
supermartingale. Hence
sup
y∈Y
P

sup
t≥0
|x(0, t, x, y| > ε

≤sup
y∈Y
Px,y

sup
t≥0
{ 1
c1
v(x(t), y(t))} > εp

≤sup
y∈Y
Px,y

sup
t≥0
θ(t) > εpc1

≤(1/εpc1)Ex,y[θ(0)] ≤(c2/εpc1) |x|p
and the trivial solution of (2.1) is a.s. stochastically stable. Now, to prove the
asymptotic stochastic stability, we apply the supermartingale inequality [3]:
sup
y∈Y
P

sup
t≥u
|x(u, t, x, y| > c

≤sup
y∈Y
P(u)
x,y

sup
t≥u
{ 1
c1 v(x(t), y(t))} > cp

≤sup
y∈Y
P(u)
x,y

sup
t≥u
{ 1
c1
θ(t) e−c3t/c2} > cp

≤(c2/cpc1) |x|p e−uc3/c2.
The proof is complete.
⊓⊔
3 Stochastic Stability Based on Linear Approximation
In this section we consider the quasilinear equation
d˜x(t)
dt
= A(y(t))˜x(t) + g(˜x(t), y(t)),
t ≥0.
(3.1)
Here the matrix A(y) and the Markov process y(t), t ≥0 satisfy the conditions
given in Section 2. We assume that the function g(x, y) is such that g(0, y) ≡0,

98
J. Carkovs, J. Stoyanov
and moreover that g(x, y) obeys bounded continuous x-derivative Dxg(x, y)
which is uniformly bounded in the ball Br(0) for any r > 0, that is,
sup
y∈Y, x∈Br(0)
∥Dxg(x, y)∥:= gr < ∞.
(3.2)
Theorem 3.1. Suppose that equation (2.1) is asymptotically stochastically
stable and that limr→0 gr = 0. Then equation (3.1) is locally asymptotically
stochastically stable.
Proof. Let us mention first that there are many functions g(x, y) satisfying
the condition limr→0 gr = 0. A simple example in the one-dimensional case is
to take g(x, y) = h(y) xγ/(1+x2), where γ = const > 1 and h(y) is a bounded
function.
We consider (2.1) as the linear approximation of equation (3.1). In view
of Lemma 2.1 and Lemma 2.2, we can construct the Lyapunov function (2.8)
with some small p > 0. Since the matrix-valued function Dx x(0, t, x, y) is the
Cauchy matrix of equation (2.1), then the following estimate is valid:
sup
y∈Y
E[∥Dx x(s, s + t, x, y)∥p] ≤h2 e−γt
with some positive constants h, γ and for all t > 0. Therefore the above
Lyapunov function satisfies the conditions (2.7) and by construction for all
x ̸= 0 it has x-derivative which satisfies the inequalities

T

0
E[∇x|x(s, s + t, x, y)|p] dt

≤p |x|p−1
T

0
sup
y∈Y
E[∥Dx x(s, s + t, x, y)∥p] dt ≤c3 |x|p−1
for some c3 > 0. Now we estimate the function Lv(x, y), where L is the weak
infinitesimal operator of the pair {˜x(t), y(t)}, t ≥0, and we use L0 as given
by (2.2):
Lv(x, y) = L0v(x, y) + ⟨g(x, y), ∇x⟩v(x, y) ≤−1
2 |x|p + c3 |x|p |g(x, y)|
≤

grc3 −1
2

|x|p
for all x ∈Br(0), r > 0. Hence, in view of the Dynkin formula, we use the
estimate
E(u)
x,y[v(˜x(τr(t)), y(τr(t))] ≤v(x, y) +

grc3 −1
2

E(u)
x,y


τr(t)

u
|˜x(s)|p ds

,
(3.3)

Stability Analysis of Markov Dynamical Systems
99
which is valid for all y ∈Y, x ∈Br(0), r > 0, t ≥u ≥0. If r is sufficiently
small, then the second term in the right-hand side of (3.3) is non-positive.
Hence the process v(˜x(τr(t)), y(τr(t)), t ≥0 is a supermartingale, so
Px,y

sup
t≥0
|˜x(t)| > ε

≤Px,y

sup
t≥0
v(˜x(τr(t)), y(τr(t)) > c1εp

≤c2δp
c1εp (3.4)
for all y ∈Y, x ∈Bδ(0), δ ∈(0, ε), ε ∈(0, r) and sufficiently small r > 0. The
a.s. local stability immediately follows from these estimates. Let us define the
function hR(r) as follows: hR(r) = 1 for x ∈[0, R), hR(r) = (2R −r)/R for
x ∈[R, 2R), hR(r) = 0 for x ≥2R. Consider the following random differential
equation:
dxR(t)
dt
= A(y(t)) xR(t) + hR(|xR(t)|) g(xR(t), y(t)),
t ≥0.
(3.5)
The Cauchy problem for (3.5) with initial condition xR(0) = x has a unique
solution since the function hR(|x|) g(x, y) satisfies the Lipschitz condition with
a constant c2R. Hence the pair {xR(t), y(t)}, t ≥0 is a Markov process whose
weak infinitesimal operator LR is defined as follows:
LRv(x, y) = L0v(x, y) + ⟨hR(|x|) g(x, y), ∇x⟩v(x, y).
Now choosing R so small that (c2R c3 −1
2) := −c4 < 0, one can write the
estimate LR v(x, y) ≤−c4|x|p. Therefore
E(u)
x,y[v(xR(t), y(t))] ≤v(x, y) −c4
c1
t

u
E(u)
x,y[v(xR(s), y(s))] ds
(3.6)
for all t ≥u ≥0. Hence the stochastic process v(xR(t), y(t)), t ≥0 is a positive
supermartingale and we have that
Px,y

sup
t≥s
v(xR(t), y(t)) > c1εp

≤
1
c1εp Ex,y[v(xR(s), y(s))]
(3.7)
for all y ∈Y, x ∈BR(0), ε ∈(0, R) and sufficiently small R > 0. We use (3.7)
to derive that Ex,y[v(xR(t), y(t))] ≤v(x, y) e−c4t/c1 ≤c2 |x|p e−c4t/c1 and then
from (3.6) to conclude that
Px,y

sup
t≥s
|xR(t)| > ε

≤c2 |x|pε−pc−1
1 e−sc4/c1.
Hence all solutions of equation (3.5) starting at t = 0 from a position x(0)
which is in the ball Bε(0) for ε ∈(0, R), and with sufficiently small R, tend
to 0 with probability one. For the time before leaving the ball Bε(0), the
solutions of equations (3.1) and (3.5), with the same initial conditions in the
ball Bε(0), are coinciding. Hence, all solutions of (3.1), which are in the ball
Bε(0) for sufficiently small ε, tend to zero with probability one. The proof is
complete.
⊓⊔

100
J. Carkovs, J. Stoyanov
4 Diffusion Approximation of the Slow Motion
and Stability
As mentioned in the Introduction, the operator Q can be considered as the
infinitesimal operator of a Markov process ξ(t), t ≥0 with the same phase
space G. It is assumed that Q is a closed operator such that its spectrum
σ(Q) is split into two parts, that is, σ(Q) = σ−ρ(Q) ∪{0}, where σ−ρ(Q) ⊂
{Reλ ≤−ρ < 0} and the zero eigenvalue has multiplicity one. The transition
probability P(t, z, A) of this Markov process satisfies the uniform ergodicity
condition [4] in the form
sup
A∈ΣG, z∈G
|P(t, z, A) −µ(A)| ≤e−ct, c = const > 0,
where ΣG is the Borel σ-algebra of subsets of G. This implies that for any
v ∈C(G), the space of continuous and bounded functions on G, which satisfies
the condition

G
v(z)µ(dz) = 0,
(4.1)
we can define the following continuous function:
Πv(z) :=
∞

0

G
v(u)P(t, z, du) dt,
z ∈G.
The operator Π, see [4], is said to be the potential of the Markov process. We
extend this operator on the whole space C(G) by the equality
Πv(z) :=
 ∞
0

G
[v(u) −¯v]P(t, z, du) dt, where ¯v =

G
v(y)µ(dz).
(4.2)
We denote its norm by ∥Π∥:= supz∈G, v∈C(G) |v(z)|. Note that, according
to [3], the equation Qf = −v has a solution iffv satisfies the orthogonality
condition (4.1) and this solution can be taken in the form f = Πv. It is clear
that the Markov process ξε(t), t ≥0 with an infinitesimal operator Qε =
1
ε2 Q
can be defined by the formula ξε(t) = ξ(t/ε2), t ≥0. In this section we consider
the linear equation (1.6) for the slow motion xε(t), t ≥0 with a Markov process
ξε(t) = ξ(t/ε2) and the fast variable yε(t), t ≥0, satisfying equation (1.7).
We also suppose that A(y, z), as well as h−1(y, z) and h0(y, z), are continuous
and bounded functions such that their y-derivatives of order up to three are
all bounded. The triple {xε(t), yε(t), ξε(t)}, t ≥0 is a homogeneous Feller
Markov process on Rn × Rm × G, see [19], and its week infinitesimal operator
L(ε) is defined for appropriately smooth functions by the equality
L(ε)v(x, y, z) = ⟨A0(y, z)x, ∇x⟩v(x, y, z) + ε⟨A1(y, z)x, ∇x⟩v(x, y, z)
+1
ε⟨h−1(y, z), ∇y⟩v(x, y, z) + ⟨h0(y, z), ∇y⟩v(x, y, z) + 1
ε2 Qv(x, y, z).
(4.3)

Stability Analysis of Markov Dynamical Systems
101
Here ∇y is the gradient operator in Rm, ⟨·, ·⟩denotes the scalar product in
Rm and the operator Q acts on the third argument.
The properties of the pair {xε(t), yε(t)}, t ∈[0, T], for a fixed T > 0,
considered as a stochastic process in the Skorokhod’s space D([0, T], Rn×Rm),
depends essentially on the averaged value ¯h−1(y) of the function h−1(y, z) with
respect to the invariant measure µ.
We assume that ¯h−1(y) ≡0; the case ¯h−1(y) ̸= 0 needs a separate
study. Thus, applying methods and results from [19], under the condition
¯h−1(y) ≡0, one can prove that on any fixed time interval [0, T], as ε →0, the
pair {xε(t), yε(t)}, t ∈[0, T], converges weekly to a diffusion Markov process
{¯x(t), ˆy(t)}, t ∈[0, T]. Here the Markov process ˆy(t), which is said to be the
diffusion approximation of yε(t), is given by its infinitesimal operator
ˆLv(y) = ⟨b(y), ∇y⟩v(y) + 1
2⟨σ2(y)∇y, ∇y⟩v(y),
(4.4)
with b(y) = ¯h0(y) + {DyΠ{h−1}}(y, ·)h−1(y, ·) and the symmetric non-
negatively defined matrix σ2(y) given by the formula
σ2(y) = h−1(y, ·){Πh−1}T (y, ·) + {Πh−1}(y, ·){h−1(y, ·)}T .
Moreover, ¯x(t), t ≥0 satisfies the random differential equation
d
dt ¯x(t) = ¯A0(ˆy(t)) ¯x(t),
t ≥0,
(4.5)
with a matrix ¯A0(ˆy(t)) depending on the above Markov process ˆy, whose
infinitesimal operator is ˆL. For further reference it is convenient to define the
stochastic process ˆy(t), t ≥0 as the solution of an Itˆo stochastic differential
equation. We suppose that this equation is of the form
dˆy(t) = b(ˆy(t)) dt + σ(ˆy(t)) dw(t),
t ≥0.
(4.6)
Here the vector b(y) and the matrix σ(y) are as given above. The assumptions
imposed previously imply that the matrix ¯A0(y), the vector b(y) and the
matrix σ(y) are three times continuously differentiable and bounded uniformly
in y ∈Rm together with their derivatives. We denote by ¯x(s, t, x, y), ˆy(s, t, y),
t ≥0, or simply ¯x(t), ˆy(t), t ≥s, the solution of the system (4.5)–(4.6) with
initial conditions ¯x(s) = x, ˆy(s) = y. Our goal in this section is to prove that,
for sufficiently small ε, the system (4.5)–(4.6) can by successfully used for the
exponential p-stability analysis of the slow motion (1.6), which is subjected
to the random perturbations yε(t), ξε(t), t ≥0.
It is easy to see that the pair {¯x(t), ˆy(t)}, t ≥0 is a homogeneous Feller
Markov process in the space Rn × Rm. The weak infinitesimal operator ¯L of
this process is defined for sufficiently smooth functions v(x, y) by the formula
¯Lv(x, y) = ⟨¯A(y)x, ∇x⟩v(x, y) + ⟨b(y), ∇y⟩v(x, y) + 1
2⟨σ2(y)∇y, ∇y⟩v(x, y).
(4.7)

102
J. Carkovs, J. Stoyanov
Let us take the function v(x, y) as follows:
v(x, y) :=
T

0
E[|¯x(0, t, x, y)|p] dt
(4.8)
with a number T > 0 which will be specified later. In order to find useful esti-
mates for this function and its derivatives, we need to estimate the derivatives
of the solution of the system (4.5)–(4.6) with respect to the initial conditions
y(0) = y and x(0) = x. To avoid complicated notations and computations, we
consider the process ˆy(t) to be 1-dimensional, i.e., m = 1. The assumptions
on the functions hj(y, z), j = −1, 0 imply that the drift b(y) and the diffu-
sion σ2(y) of the Markov process ˆy have at least three continuous uniformly
bounded derivatives in y. This property follows from the definition of the
potential and the possibility to differentiate in y under the integral sign. By
definition, the matrix ¯A(y) also has three continuous and uniformly bounded
derivatives. Hence, the Markov diffusion process {¯x(t), ˆy(t)} allows differenti-
ation with respect to the initial data y, where y = ˆy(0). We can study these
derivatives as solutions of the corresponding equations.
Lemma 4.1. The solution ¯x(t), t ≥0 of equation (4.5), with ˆy(t), t ≥0 given
by (4.6), admits three continuous y-derivatives for which the following bounds
hold for any r ∈N:
sup
0≤t≤T, y∈Rm Ex,y[|Dj
y ¯x(t)|r] ≤kr |x|r,
j = 1, 2, 3.
Proof. The y-derivative Dy¯x(t) := Dy¯x(0, t, x, y) of the solution of (4.5) sat-
isfies the differential equation
dDy¯x(t)
dt
= ¯A(ˆy(t))Dy¯x(t) + Dy ¯A(1)(ˆy(t))¯x(t),
t ≥0.
(4.9)
Here and below ¯A(j)(y) = Dj
y ¯A(y), j = 1, 2, 3. By definition, Dy¯x(0) = 0. Now
we use the Cauchy integral formula allowing us to write the solution of (4.9),
which depends on the parameter y, in the following form:
Dy¯x(t) =
t

0
Dyˆy(s)H(1)(s, t, y) ¯A(1)(ˆy(s))¯x(s) ds,
(4.10)
where H(1)(s, t, y) is the Cauchy operator of the corresponding homoge-
neous equation. Similarly we write the differential equation for the second
y-derivative D2
y¯x(t) of the solution ¯x(t):
d
dtD2
y¯x(t) = ¯A(ˆy(t))D2
y¯x(t) + 2Dyˆy(t) ¯A(1)(ˆy(t))Dy¯x(t)
+ D2
yˆy(t) ¯A(1)(ˆy(t))¯x(t) + Dyˆy(t)2 ¯A(2)(ˆy(t))¯x(t),
t ≥0
(4.11)

Stability Analysis of Markov Dynamical Systems
103
with the initial condition D2
y¯x(0) = 0. The equation for the third derivative
D3
y¯x(t) can be written in the same way. All these taken together with the
smoothness of the drift and the diffusion imply that the solution of (4.5)
admits three y-derivatives and that for any fixed r ∈N there exist constants
Mr and γr such that
Ey[∥Dj
y ˆy(t)∥≤Mr eγrt,
j = 1, 2, 3,
t ∈[0, T].
(4.12)
Let us mention that our assumptions imply also that
sup
y∈Rm ∥¯A(j)(y)∥:= aj < ∞,
j = 1, 2, 3.
(4.13)
It is not difficult to see that the Cauchy operator H(1) in (4.10) is a uniformly
bounded continuous matrix-function of t satisfying the following estimate:
∥H(1)(s, t, y)∥≤h1 ea(t−s)
(4.14)
for any t ∈[s, s + T]. Hence, for some constant k1,r > 0, (4.10) implies that
for fixed T > 0 and for any r ∈N, we have
sup
0≤t≤T, y∈Rm Ex,y[|Dy¯x(t)|r] ≤k1,r |x|r.
(4.15)
Using the Cauchy operator H(2)(s, t, y) for equation (4.11) one can obtain a
formula similar to (4.10). Further on, we can use (4.12) and (4.13) and derive
for H(2) an estimate like (4.14). Thus we conclude finally that
sup
0≤t≤T, y∈Rm Ex,y[|D2
y¯x(t)|r] ≤kr|x|r
(4.16)
with some constant kr > 0 for any r ∈N. The third y-derivative of the solution
of (4.5) admits a similar estimate. This completes the proof.
⊓⊔
Corollary 4.1. The Cauchy matrix X(t) of equation (4.5) is three times con-
tinuously y-differentiable and for any T ≥0 its derivatives admit the following
estimates:
sup
0≤t≤T, y∈Rm Ex,y[∥Dj
yX(t)∥] := aT < ∞,
j = 1, 2, 3
(4.17)
Proof. It follows from the fact that the Cauchy matrix X(t) of (4.5) has x-
derivatives of its solution and satisfies the same equation under the initial
condition X(0) = I.
⊓⊔
Lemma 4.2. The function v(x, y) has three continuous y-derivatives, and
there exists a constant β > 0 such that for any x ∈Rn we have
∥Dj
yv(x, y)∥≤β|x|p, j = 1, 2, 3.

104
J. Carkovs, J. Stoyanov
Proof. By definition we can write
∇y|x(t)|p = p ⟨x(t), Dyx(t)⟩|x(t)|p−2.
(4.18)
Hence, for any x ̸= 0 and p > 0, we have
|∇z |x(t)|p | ≤p |x(t)|p−1∥Dzx(t)∥≤p ea(p−1)t |x|p−1∥Dzx(t)∥.
(4.19)
Now, using (4.12), we obtain supt,y Ex,y[∥Dyx(t)|] ≤k1|x|, 0 ≤t ≤T,
y ∈Rm. Differentiating in y both sides of (4.18) yields ∥D2
y|x(t)|p∥≤
p ∥Dyx(t)∥2|x(t)|p−2 +p |(x(t)|p−1∥D2
yx(t)∥+p |p−2| |x(t)|p−1∥Dyx(t)∥. Each
term of the right-hand side of this inequality admits an estimate of the
type (4.19), which is also true for |x(t)|p−1. Then we can apply Lemma 2.1 for
the expectations Ex,y[∥Dyx(t)∥j], j = 1, 2, and for Ex,y[∥D2
yx(t)∥]. It remains
to differentiate twice the inequality (4.18) with respect to y and apply the
same estimates for the terms involved thus completing the proof.
⊓⊔
Lemma 4.3. The vector V (x, y) := ∇xv(x, y) and its three y-derivatives ad-
mit the following estimates:
sup
y∈Rm ∥Dj
yV (x, y)∥≤ρ|x|p−j,
j = 0, 1, 2, 3
(4.20)
for some ρ > 0 and any x ̸= 0.
Proof. For our reasoning we need the following identity: |x(t)|p = |X(t)x|p =
⟨XT (t)X(t)x, x⟩p/2, where X(t) is the fundamental matrix of the linear equa-
tion (4.5). Let us prove first that supt,y |∇x |x(t)|p| ≤ρ |x|p−1, 0 ≤t ≤T,
y ∈Rm for some ρ > 0. Differentiating the above identity for |x(t)|p in x
yields
∇x |x(t)|p = p ⟨XT (t)X(t)x, x⟩p/2−1 XT (t)X(t)x.
(4.21)
Hence |∇x |x(t)|p| ≤p |X(t)x|p−1∥X(t)∥. Since the fundamental matrix
of (4.5) is uniformly bounded on any fixed interval [0, T], then the esti-
mate (4.20) is established for j = 1. Next is to differentiate (4.21) in y:
Dy ∇x |x(t)|p = p(p −2)|x(t)|p/2−2⟨x(t), Dyx(t)⟩
× [XT (t)x(t) + p|x(t)|p−1(DyXT (t)x(t) + XT (t)Dyx(t))].
(4.22)
The final step is to use the estimate ∥X(t)∥≤eat, as well as the estimates for
the expectations of the derivatives Dyx(t) and DyX(t) thus obtaining (4.20).
The proof is completed.
⊓⊔
Lemma 4.4. The matrix W(x, y) = Dx∇xv(x, y) and its two derivatives in
y admit the following estimates:
sup
y∈Rm ∥Dj
yW(x, y)∥≤δ |x|p−2,
j = 1, 2
(4.23)
for some δ > 0 and all x ̸= 0.

Stability Analysis of Markov Dynamical Systems
105
Proof. The matrix of the second derivatives of |x(t)|p is as follows:
Dx∇x|x(t)|p = p (p −1)⟨XT (t)X(t)x, x⟩p/2−2 XT (t)x(t)xT (t)X(t)
+ p ⟨XT (t)X(t)x, x⟩p/2−1 XT (t)X(t).
(4.24)
We estimate each term in the right-hand side of (3.24) by using the fact that
∥X(t)∥≤eat thus arriving at (4.23) for j = 1. Similarly, by differentiating
once more, we establish (4.23) also for j = 2. The proof is completed.
⊓⊔
Theorem 4.1. Consider the processes
¯x(t) and
ˆy(t) defined by equations
(4.5) and
(4.6), respectively, and suppose that all the assumptions related
to them are satisfied. Suppose now that equation (4.5) for ¯x(t), with ˆy(t),
from (4.6), is exponentially p-stable. Then there is a number ε0 > 0 such that
equation (1.6), with coefficients depending on yε(t), t ≥0, is exponentially
p-stable for all ε ∈(0, ε0).
Proof. It is based on the second Lyapunov method. We use the Lyapunov
function of the form vε(x, y, z) = v(x, y) + ε v1(x, y, z) + ε2 v2(x, y, z), where
v(x, y) is defined by (4.8). Let the functions v1(x, y, z) and v2(x, y, z) be the
solutions of the following two equations:
Q v1(x, y, z) = −⟨A0(y, z)x, ∇y⟩v(x, y),
(4.25)
Q v2(x, y, z) = −

⟨[A(y, z) −¯A(y)]x, ∇x⟩v(x, y) + ⟨h−1(y, z), ∇y⟩v1(x, y, z)
−

G
⟨h−1(y, z), ∇y⟩v1(x, y, z)µ(dz) + ⟨h0(y, z) −¯h0(y), ∇y⟩v(y, z)

.
(4.26)
The right-hand side of each of these equations, after integration in y with
respect of the measure µ(dy), is equal to 0. This implies that there ex-
ist solutions of both equations. By the definition of a potential, we have
v1(x, y, z) = ⟨Πh−1(y, z), ∇yv(x, y)⟩. The estimates of this function and its
derivatives with respect to x and of y can be obtained from appropriate es-
timates for the scalar product ⟨h−1(y, z), ∇yv(x, y)⟩multiplied by ∥Π∥. This
follows from the possibility to differentiate the solution of (4.5) and the de-
finition of the potential operator Π. Hence, there exists a constant R1 > 0,
such that the following inequalities are satisfied:
|v1(x, y, z)| ≤R1 |x|p, |∇x v1(x, y, z)| ≤R1 |x|p−1, |∇y v1(x, y, z)| ≤R1 |x|p,
∥Dx∇x v1(x, y, z)∥≤R1 |x|p−2,
∥Dy∇x v1(x, y, z)∥≤R1 |x|p−1,
∥Dy∇y v1(x, y, z)∥≤R1 |x|p,
∥DyDx∇y v1(x, y, z)∥≤R1 |x|p−1,
∥DyDx∇y v1(x, y, z)∥≤R1 |x|p−1,
∥D2
x∇y v1(x, y, z)∥≤R1 |x|p−2.
The same estimates hold also for the function v2(x, y, z). Hence, using the
results in Section 3, we conclude that

106
J. Carkovs, J. Stoyanov
∥∇yv2(x, y, z)∥≤R2 |x|p,
∥∇xv2(x, y, z)∥≤R2 |x|p−1
for any x ∈Rn, y ∈Rm, z ∈G and some R2 > 0.
Let us denote by A(ε) the weak infinitesimal operator of the Markov
process {xε, yε, ξε} defined by (1.6)–(1.7), with a Markov process ξε. We apply
this operator to the function vε(x, y, z) = v(x, y)+ε v1(x, y, z)+ε2 v2(x, y, z).
By definition
A(ε)vε(x, y, z) = ⟨A0(y, z)x, ∇x⟩vε(x, y, z) + L(ε)vε(x, y, z),
where L(ε) is defined by the formula
L(ε) = 1
ε⟨h−1(y, z), ∇y⟩+ ⟨f0(y, z), ∇y⟩+ 1
ε2 Q.
Hence:
A(ε)vε(x, y, z) = 1
ε{Q v1(x, y, z) + ⟨h−1(y, z), ∇y⟩v(x, y)}
+ {⟨A0(y, z)x, ∇x⟩v(x, y) + ⟨h−1(y, z), ∇y⟩v1(x, y, z)
+ ⟨h0(y, z), ∇y⟩v(x, y) + Qv2(x, y, z)}
+ ε{⟨h−1(y, z), ∇y⟩v2(x, y, z) + ⟨A0(y, z)x, ∇x⟩v1(x, y, z)
+ ⟨h0(y, z), ∇y⟩v1(x, y, z))}
+ ε2{⟨A0(y, z)x, ∇x⟩v2(x, y, z) + ⟨h0(y, z), ∇y⟩v2(x, y, z)}.
(4.27)
The expression in the first brackets in the right-hand side of this formula is
equal to 0. It follows from (4.25) that the item in the second brackets, by
construction, is equal to ¯Lv(x, y). Hence, due to our assumption about the
exponential p-stability of the averaged system, ¯Lv(x, y) does not exceed the
quantity −c3 |x|p with some constant c3 > 0. The last items in (4.27) can be
estimated by r|x|p for some r > 0. Hence A(ε)vε(x, y, z) ≤(−c3+εr+ε2r)|x|p.
In addition, |v1(x, y, z)| ≤ρ|x|p, |v2(x, y, z)| ≤ρ|x|p for some ρ > 0. Finally,
one can write the inequalities
(c1 −ερ −ε2ρ) |x|p ≤vε(x, y, z) ≤(c2 + ερ + ε2ρ) |x|p
for some c2 ≥c1 > 0. The exponential p-stability of equation (1.6) follows now
from these estimates and the estimates for the function v1 and its derivatives,
which have been written above. The theorem is proved.
⊓⊔
We are now in a position to continue the analysis of the system
(1.1)–
(1.2) with functions F(x, y, z) and H(y, z) in the right-hand sides not de-
pending explicitly on ε. The goal is to show the local asymptotic stochas-
tic stability property for equation
(1.1). We introduce first the notation
A0(y, z) := DxF(x, y, z)|x=0 and let ¯A0(y) and ¯H0(y) be the µ–averaged func-
tions, respectively of A0(y, z) and H(y, z), namely:

Stability Analysis of Markov Dynamical Systems
107
¯A0(y) =

G
A0(y, z) µ(dz) and
¯H(y) =

G
H(y, z) µ(dz).
Corollary 4.2. Let us suppose that: (i) F(x, y, z) is continuous and bounded;
(ii) F(x, y, z) has two uniformly continuous and bounded x–derivatives uni-
formly in (y, z);
(iii)
H(y, z) is continuous and bounded with ¯H(y) ≡0.
Suppose, finally, that equation (4.5), based on the above ¯A0(y) with ˆy(t) sat-
isfying (4.6), is asymptotically stochastically stable. Then equation
(1.1) is
locally asymptotically stochastically stable for all sufficiently small ε.
Proof. Together with (1.1) we consider the equation
d˜xε(t)
dt
= A0(yε(t), ξε(t)) ˜xε(t), t ≥0,
where yε(t) satisfies (1.2) and ξε(t) is the Markov process as defined in the
Introduction. The asymptotic stochastic stability of equation (4.5), with ˆy(t)
from
(4.6), combined with the results in Section 1 imply that
(4.5) is ex-
ponentially p-stable for some p > 0. Now, applying Theorem 3.1 we conclude
that ˜xε(t) is asymptotically stochastically stable for all sufficiently small ε.
Since F(0, y, z) ≡0, we use the obvious equality
F(x, y, z) = (DxF(0, y, z))x +
 1
0
[DxF(tx, y, z) −DxF(x, y, z)|x=0]dt

x
to rewrite the right-hand side of equation (1.1) in the following form:
F(x, y, z) = A0(y, z)x + g(x, y, z).
The expressions for A0(y, z) and g(y, z) are clear. We use the function
g(x, y, z) to find first its µ–averaged value ¯g(x, y), then the x–derivative
Dx ¯g(x, y) and by (3.2) determine the upper bound, say ¯gr, which depends
on the radius r of the ball Br(0). It is not difficult to show that the pair
{yε(t), ξε(t)} is a Markov process with values in the space Y × G. Hence,
we need to refer to Theorem 3.1 and to the assumptions about the function
F(x, y, z) which guarantee that the relation limr→0 ¯gr = 0 is satisfied and
then apply Theorem 2.1 in which stability analysis is based on the linear ap-
proximation. The proof is completed.
⊓⊔
Acknowledgments
This study was partly supported by UK-EPSRC Grant No. GR/R71719/01.
We dedicate this paper to Professor Albert Shiryaev on the occasion of his
70th birthday.

108
J. Carkovs, J. Stoyanov
References
1. Arnold, L., Papanicolaou, G., Wihstutz, V.: Asymptotic analysis of the Lya-
punov exponent and rotation number of the random oscillator and applications.
SIAM Journal Applied Mathematics 46, 427–450 (1986)
2. Dimentberg, M.F.: Statistical Dynamics of Nonlinear and Time-Varying Sys-
tems. Wiley, New York (1988) (Russian edn 1982)
3. Doob, J. L.: Stochastic Processes. Wiley, New York (1953)
4. Dynkin, E. B.: Markov Processes. Springer, Berlin (1965) (Russian edn 1963)
5. Freidlin, M.I., Wentzell, A.D.: Random Perturbations of Dynamical Systems,
2nd edn. Springer, New York (1998) (Based on the Russian edn 1979)
6. Guillin, A. : Averaging principle of SDE with small diffusion: moderate devia-
tions. Annals of Probability 31, 413–443 (2003)
7. Hartman, Ph.: Ordinary Differential Equations. Wiley, New York (1964)
8. Hoppenstead, F., Peskin, C.: Modelling and Simulation in Medicine and Life
Science. Springer, New York (2001)
9. Kabanov, Yu.M., Pergamenshchikov, S.: Two-Scale Stochastic Systems: Asymp-
totic Analysis and Control (Appl. Math. 49). Springer, Berlin (2003)
10. Katafygiotis, L., Tsarkov, Ye.: Mean square stability of linear dynamical systems
with small Markov perturbations. I. Bounded coefficients. Random Operators
& Stochastic Equations 4, 149–170 (1996)
11. Katafygiotis, L., Tsarkov, Ye.: Mean square stability of linear dynamical systems
with small Markov perturbations. II. Diffusion coefficients. Random Operators
& Stochastic Equations 4, 257–278 (1996)
12. Khasminskii, R.Z.: Stability of Systems of Differential Equations Under Random
Perturbations of Their Parameters. Sijthoff& Noordhoff, Alphen aan den Riin
(1981) (Russian edn 1969)
13. Korolyuk, V.S.: Stability of stochastic systems in diffusion approximation
scheme. Ukrainian Mathematical Journal 50, 36–47 (1998)
14. Korolyuk, V.S., Turbin, A.F.: Mathematical Foundations for Phase Lamping of
Large Systems (Math. & Its Appl. 264). Kluwer Acad. Publ., Dordrecht (1993)
15. Liptser, R.Sh., Stoyanov, J.: Stochastic version of the averaging principle for
diffusion type processes. Stochastics & Stochastics Reports 32, 145–163 (1990)
16. Mao, X.: Stability of stochastic differential equations with Markovian switching.
Stochastic Processes & Applications 79, 45–67 (1999).
17. Mitropolskii, Yu.A.: Problems in the Asymptotic Theory of Nonstationary Os-
cillations. Israel Progr. Sci., Jerusalem and Davey, New York (1965) (Russian
edn 1964)
18. Tsarkov, Ye.: Asymptotic methods for stability analysis of Markov impulse dy-
namical systems. Nonlinear Dynamics & Systems Theory 2, 103–115 (2002)
19. Skorokhod, A.V.: Asymptotic Methods in the Theory of Stochastic Differential
Equations (Transl. Math. Monographs 78). American Mathematical Society,
Providence, RI (1989) (Russian edn 1987)
20. Skorokhod, A.V., Hoppensteadt, F.C., Salehi, H.: Random Perturbation Meth-
ods with Applications in Science and Engineering. Springer, New York (2002)
21. Stoyanov, J.: Regularly perturbed stochastic differential systems with an in-
ternal random noise. Nonlinear Analysis: Theory, Methods & Applications 30,
4105–4111 (1997)
22. Zhang, W.B.: Economic Dynamics – Growth and Development. Springer, Berlin
(1990)

Some Particular Problems of Martingale
Theory
Alexander CHERNY
Moscow State University,
Faculty of Mechanics and Mathematics,
Department of Probability Theory,
119992 Moscow, Russia.
cherny@mech.math.msu.su
Summary. This paper deals with the following problems:
Is a product of independent martingales also a martingale? We consider 8 par-
ticular formulations of this problem.
Is a limit of a converging sequence of martingales also a martingale? We consider
32 particular formulations of this problem.
Is a stochastic integral of a bounded process with respect to a martingale also a
martingale?
If X = (Xt)t≥0 is a positive process such that EXτ = EX0 for any finite stopping
time τ, then is is true that X is a uniformly integrable martingale?
Key words: convergence of martingales, local martingales, martingales, orthogonal
local martingales, quadratic covariation, stochastic integrals, uniformly integrable
martingales.
Mathematics Subject Classification (2000): 60F99, 60G42, 60G44,
60H05
1 Introduction
The Seminar “Stochastic Analysis and Financial Mathematics” conducted at
the Department of Probability Theory, Faculty of Mechanics and Mathemat-
ics, Moscow State University, by A.N. Shiryaev, A.A. Gushchin, M.A. Urusov,
and the author is in some sense a continuation of the Seminar held at the
Steklov Mathematical Institute in the 1970s and 1980s. The latter one was
founded by A.N. Shiryaev in 1966 and was conducted by A.N. Shiryaev,
N.V. Krylov, R.S. Liptser, and Yu.M. Kabanov. The new Seminar is some-
times called the “railroad seminar” because it is intended to work “as regularly
as the railroad”. The Seminar has its own symbol:

110
A. Cherny
One of the distinctive features of this Seminar is that a particular problem
is proposed to the listeners at each meeting and its solution is discussed at the
next meeting. These are called “corner problems” because they are written at
a corner of the blackboard.
In this paper, several such problems are considered. Some of the particular
formulations are known or very easy to solve; some others are more compli-
cated, and the obtained (negative or positive) results seem to be new.
1. Products of independent martingales. The problem is as follows:
Is a product of independent martingales also a martingale? We consider 8
formulations of this problem:
1. Let X and Y be martingales (each with respect to its natural filtration).
Is it true that XY is a martingale (with respect to its natural filtration)?
2. Let X and Y be local martingales (each with respect to its natural filtra-
tion). Is it true that XY is a local martingale (with respect to its natural
filtration)?
3. Let X and Y be martingales with respect to a common filtration (Ft). Is
it true that XY is an (Ft)-martingale?
4. Let X and Y be local martingales with respect to a common filtration (Ft).
Is it true that XY is an (Ft)-local martingale?
5. Let X and Y be continuous martingales (each with respect to its natural
filtration). Is it true that XY is a martingale (with respect to its natural
filtration)?
6. Let X and Y be continuous local martingales (each with respect to its
natural filtration). Is it true that XY is a local martingale (with respect
to its natural filtration)?
7. Let X and Y be continuous martingales with respect to a common filtra-
tion (Ft). Is it true that XY is an (Ft)-martingale?
8. Let X and Y be continuous local martingales with respect to a common
filtration (Ft). Is it true that XY is an (Ft)-local martingale?
Here the time index t for X and Y runs through the positive half-line or
through a compact interval (clearly, the answers to the above problems are
the same in these two cases).
Remarks. (i) By a local martingale we mean a process X, for which
there exists a localizing sequence (τn) such that, for any n, the stopped
process (Xt∧τn) is a martingale. An alternative definition is that the process
(Xt∧τnI(τn > 0)) should be a martingale. It is easy to check that the answers
to the problems under consideration are the same for these two definitions.
(ii) Two (Ft)-local martingales whose product is also an (Ft)-local mar-
tingale are said to be orthogonal. Thus, Problem 4 (resp., Problem 8) can

Some Particular Problems of Martingale Theory
111
be reformulated as follows: does the independence of local martingales (resp.,
continuous local martingales) imply their orthogonality?
2. Limits of martingales. The problem is as follows: Is a limit of a con-
verging sequence of martingales also a martingale? We consider 8 formulations
of this problem:
1. Let (Xn) be a sequence of martingales (each with respect to its natural
filtration) that converges to a process X in the sense of the weak conver-
gence of finite-dimensional distributions. Is it true that X is a martingale
(with respect to its natural filtration)?
2. Let (Xn) be a sequence of martingales (each with respect to its natural
filtration) that converges in distribution to a process X. Is it true that X
is a martingale (with respect to its natural filtration)?
3. Let (Xn) be a sequence of local martingales (each with respect to its
natural filtration) that converges to a process X in the sense of the weak
convergence of finite-dimensional distributions. Is it true that X is a local
martingale (with respect to its natural filtration)?
4. Let (Xn) be a sequence of local martingales (each with respect to its
natural filtration) that converges in distribution to a process X. Is it true
that X is a local martingale (with respect to its natural filtration)?
5. Let (Xn) be a sequence of martingales with respect to a common fil-
tration (Ft) such that Xn
t
P
−−−−→
n→∞
Xt for any t. Is it true that X is an
(Ft)-martingale?
6. Let (Xn) be a sequence of martingales with respect to a common fil-
tration (Ft) that converges to a process X in probability uniformly on
compact intervals (i.e. sups≤t |Xn
s −Xs|
P
−−−−→
n→∞0 for any t). Is it true that
X is an (Ft)-martingale?
7. Let (Xn) be a sequence of local martingales with respect to a common
filtration (Ft) such that Xn
t
P
−−−−→
n→∞Xt for any t. Is it true that X is an
(Ft)-local martingale?
8. Let (Xn) be a sequence of local martingales with respect to a common
filtration (Ft) that converges to a process X in probability uniformly on
compact intervals. Is it true that X is an (Ft)-local martingale?
Here the time index t for Xn runs through the positive half-line or through a
compact interval (clearly, the answers to the above problems are the same in
these two cases).
We consider each of the above problems in combination with one of the
following conditions on (Xn):
A. No additional assumptions on (Xn) are imposed.
B. The jumps of Xn are assumed to be bounded by a constant a > 0 and
Xn
0 = 0.
C. The processes Xn are assumed to be continuous and Xn
0 = 0.

112
A. Cherny
D. The processes Xn are assumed to be bounded by a constant a > 0.
Thus, we get 32 = 8 × 4 formulations of the above problem. In formulations
2.A, 2.B, 2.D, 4.A, 4.B, and 4.D, we consider the weak convergence in the
space D of c`adl`ag functions, while in formulations 2.C and 4.C, we consider
the weak convergence in the space C of continuous functions.
Remark. The above problem arises in connection with limit theorems for
stochastic processes (see [2]).
3. Stochastic integrals with respect to a martingale. The problem is
as follows: Let X be an (Ft)-martingale and H be an (Ft)-predictable process
such that |H| ≤1. Is it true that the stochastic integral of H with respect
to X is also an (Ft)-martingale?
Remark. If the word “martingale” in the above problem is replaced by the
word “semimartingale”, “Hp-semimartingale” (see [6]), “sigma-martingale”
(see [2, Ch. III, § 6e]), “local martingale”, or “Hp-martingale” (see [3, Ch. I,
§ 5]), then, clearly, the answer is positive.
4. Uniform integrability of martingales. The problem is as follows:
Let X = (Xt)t≥0 be an (Ft)-adapted c`adl`ag positive process such that
EXτ = EX0 < ∞for any (Ft)-stopping time τ that is finite a.s. Is it true
that X is a uniformly integrable (Ft)-martingale?
Remark. The origin of this problem lies in financial mathematics. Namely,
let X be the discounted price process of some asset. Define the set of dis-
counted incomes that can be obtained by trading this asset as:
 N

n=1
Hn(Xun −Xun−1) : N ∈N, u0 ≤· · · ≤uN < ∞
are (Ft)-stopping times, Hn is Fun−1-measurable

.
As in [1], define the set of equivalent risk-neutral measures as the set of
probability measures Q ∼P such that EQξ−≥EQξ+ for any ξ ∈A (here
ξ−= (−ξ) ∨0, ξ+ = ξ ∨0; the expectations EQξ−and EQξ+ are allowed to
take on the value +∞). It is easy to show that a measure Q ∼P is a risk-
neutral measure if and only if EQXτ = EQX0 for any finite (Ft)-stopping
time τ. Thus, the above problem can be reformulated as follows: does the
class of equivalent risk-neutral measures in the above model coincide with the
class of equivalent uniformly integrable martingale measures?
The reader is invited to solve as many of the above 42 problems as possible.

Some Particular Problems of Martingale Theory
113
2 Products of Independent Martingales
The answer to the problem “Is a product of independent martingales also a
martingale?” in formulations 1 and 5 is positive as shown by the following
theorem.
Theorem 2.1. Let X and Y be independent martingales (each with respect
to its natural filtration). Then XY is a martingale (with respect to its natural
filtration).
Proof. Fix s ≤t. For any A ∈FX
s
((FX
t ) denotes the natural filtration
of X, i.e. FX
t
= σ(Xs; s ≤t)) and B ∈FY
s , we have
E(XtYtIAIB) = E(XtIA)E(YtIB) = E(XsIA)E(XsIB) = E(XsYsIAIB).
By the monotone class lemma,
1
C ∈FX
s ∨FY
s : E(XtYtIC) = E(XsYsIC)
2
= FX
s ∨FY
s .
Hence, E

XtYt |FX
s ∨FY
s

= XsYs, which implies that E

XtYt |FXY
s

= XsYs.
This is the desired statement.
⊓⊔
The example below shows that the answer to the problem in formulation 2
is negative. The example is given in the continuous time, but it is easy to
provide also a discrete-time one.
Example 1. Let B be a Brownian motion and ξ be a non-integrable random
variable that is independent of B. Set
H0
t = I(t < 1)
1 −t
,
t ≥0,
τ = inf

t ≥0 :
 t
0
H0
s dBs = ξ

,
Ht = H0
t I(t ≤τ),
t ≥0,
Xt =
 t
0
HsdBs,
t ≥0.
Let η be a random variable independent of X taking on values ±1 with prob-
ability 1/2. Set Yt = ηI(t ≥1), t ≥0. Then X and Y are independent local
martingales (each with respect to its natural filtration), but XY is not a local
martingale (with respect to its natural filtration).
Proof. The first statement is clear. The second one follows from the prop-
erty that for any (FXY
t
)-stopping time τ, we have {τ < 1} ∈.
t<1 FXY
t
=
{∅, Ω}, while X1 = ξ is non-integrable.
⊓⊔
The next example shows that the answer to the problem in formulations 3
and 4 is negative.

114
A. Cherny
Example 2. Let ξ and η be independent random variables taking on the val-
ues ±1 with probability 1/2. Set
Xt =

0,
t < 1,
ξ,
t ≥1,
Yt =

0,
t < 1,
η,
t ≥1,
Ft =

σ(ξη),
t < 1,
σ(ξ, η),
t ≥1.
Then X and Y are independent (Ft)-martingales, but XY is not an (Ft)-local
martingale.
Proof. The first statement follows from the independence of ξ and ξη and
the independence of η and ξη. In order to prove the second one, notice that XY
is not an (Ft)-martingale. Being bounded, it is not an (Ft)-local martingale.
⊓⊔
Remark. Examples 1 and 2 show that if we add the additional assumption
that the jumps of X and Y are bounded, the answers to the problem in
formulations 2, 3, and 4 will remain negative.
The theorem below shows that the answer to the problem in formulation 8
is positive.
Theorem 2.2. Let X and Y be independent continuous (Ft)-local martin-
gales. Then XY is an (Ft)-local martingale.
Proof. Let us first assume that X and Y are bounded. Then, for any t and
any sequence (∆n) of partitions of [0, t] whose diameters tend to 0, we have
E
 
ti∈∆n

Xti+1 −Xti

Yti+1 −Yti

2
=

ti∈∆n
E

Xti+1 −Xti

2E

Yti+1 −Yti

2
≤max
ti∈∆n E

Xti+1 −Xti

2 ·

ti∈∆n
E

Yti+1 −Yti

2
= max
ti∈∆n

EX2
ti+1 −EX2
ti

· (EY 2
t −EY 2
0 ).
The latter quantity tends to 0 as n →∞since the function s →EX2
s is
continuous in s. Consequently, ⟨X, Y ⟩= 0, which implies that XY is an (Ft)-
local martingale.
Consider now the general case. Set *
Xt = Xt −X0, *Yt = Yt −Y0. Then
XtYt = X0Y0 + X0 *Yt + *
XtY0 + *
Xt *Yt.
For n ∈N, set τn = inf{t : | *
Xt| ≥n}, σn = inf{t : |*Yt| ≥n}. Then the
stopped processes *
Xτn = ( *
Xt∧τn) and *Y σn = (*Yt∧σn) are independent (Ft)-
local martingales. Being bounded, they are (Ft)-martingales. Clearly, X0 *Y σn

