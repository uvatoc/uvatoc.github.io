+++
draft = false
title = "Classes"
slug = "classes"
+++

# Definitions Countability

[Class 1: Introduction](/class1) [[Slides](https://www.dropbox.com/s/b1j3viac24er0zb/class1.pdf?dl=0)]
- Goals of the Course
- Adding and Multiplying

[Class 2: Defining Definitions](/class2) [[Slides](https://www.dropbox.com/s/70p02wh0v60jhjx/class2.pdf?dl=0)]
- Babylonian numbers
- Why study theory?
- Is 0 a Natural Number?

[Class 3: What can be represented by bits?](/class3) [[Slides](https://www.dropbox.com/s/w6cpp8awawklqyv/class3.pdf?dl=0)]
- Meaning of "optimal"
- Representing the numbers and binary strings
- Set cardinality

[Class 4: More Infinities](/class4) [[Slides](https://www.dropbox.com/s/jls3abg761hx23a/class4.pdf?dl=0)]
- Cantor's Power Set cardinality theorem
- Implications of Cantor's result

# Finite Computation

[Class 5: Defining Computation](/class5) [[Slides](https://www.dropbox.com/s/qebzsemfh75y8h3/class5.pdf?dl=0)]
- Implications of Cantor's ideas
- Defining Computation


[Class 6: Modeling Boolean Circuits](/class6) [[Slides](https://www.dropbox.com/s/da98q17xl19bkm3/class6.pdf?dl=0)]
- Finite Computation
- Defining Boolean Circuits
- Universality

[Class 7: Universal Circuits](/class7) [[Slides](https://www.dropbox.com/s/1sbdh70qq6javef/class7.pdf?dl=0)]
- Boolean Circuits Model Definition
- Universality of AON Boolean Circuits

[Class 8: Syntactic Sugar, Complexity of Functions](/class8) [[Slides](https://www.dropbox.com/s/bdsu8m6zp4h369w/class8.pdf?dl=0)]
- Recap universality and syntactic sugar
- Asymptotic Notation
- Circuit Complexity: how many gates
- Existence of hard functions

[Class 9: Circuit Size Hierarchy](/class9) [[Slides](https://www.dropbox.com/s/29ge0bwnmumdt5b/class9.pdf?dl=0)]
- Computing functions using LOOKUP
- Size Hierarchy
- Universal Circuit

[Class 10: Circuit Complexity](/class10) [[Slides](https://www.dropbox.com/s/ui767kegs2u4aa8/class10.pdf?dl=0)]
- Size Hierarchy Theorem
- Universal Circuit

[Class 11: Universal Circuits](/class11) [[Slides](https://www.dropbox.com/s/rgam4q3tlbx6wq8/class11.pdf?dl=0)]
- Universal Circuits
- Practice Problems

[Class 12: Midterm Review](/class12) [[Slides](https://www.dropbox.com/s/xa0z6jewnhu9jji/class12.pdf?dl=0)]

# Uniform Computation

[Class 13: Finite Automata and Regular Expressions](/class13) [[Slides](https://www.dropbox.com/s/p1iru3eklm51m3e/class13.pdf?dl=0)]
- Finite and Uniform Computation
- Introducing Finite Automata

[Class 14: Regular Expressions](/class14) [[Slides](https://www.dropbox.com/s/123gfvltu504te9/class14.pdf?dl=0)]
- Finite Automata
- Regular Expressions
- Consequences of Equivalence of DFA and Regular Expressions

[Class 15: Deterministic and Nondeterministic Finite Automata](/class15) [[Slides](https://www.dropbox.com/s/zczgqmtshw7cllk/class15.pdf?dl=0)]
- Formalizing DFA
- Introducing Nondeterminism
- Converting a DFA to and NFA

[Class 16: Completing the Proof, Bringing Down the Internet](/class16/) [[Slides](https://www.dropbox.com/s/h31y0k91iektktb/class16.pdf?dl=0)
- Extending the NFA model: NFA-&varepsilon;
- Implemeting Python's Regular Expression library
- Challenges implementing RE matching (Cloudflare incident)

[Class 17: NFA vs. RE, Introducing Turing Machines](/class17) [[Slides](https://www.dropbox.com/s/zgb916gyqi087jo/class17.pdf?dl=0)]  
- Completing the proof that Regular Expressions can be converted to NFA-&varepsilon;
- Proving that DFAs can be converted to Regular Expression
- Introducing Turing Machine model of computation

# Computability

[Class 18: Turing Machines](/class18) [[Slides](https://www.dropbox.com/s/8r79pklw5weuney/class18.pdf?dl=0)]
- Converting DFA to RE
- Turing Machines

[Class 19: Computability](/class19) [[Notes](/docs/tmnotes.pdf)] [[Slides](https://www.dropbox.com/s/wkk6b2itoncgqul/class19.pdf?dl=0)]
- Formal model of Turing Machine
- Are there functions that cannot be computed by a TM?
- Self-Rejecting

[Class 20: Proving Uncomputability](/class20) [[Slides](https://www.dropbox.com/s/r5v70s5acql8k9b/class20.pdf?dl=0)]
- Church-Turing Thesis
- Universal Machines
- ACCEPTS is Uncomputable
- Ali G (Computability and Practical Solvability)

[Class 21: Reductions and Recognizability](/class21) [[Slides](https://www.dropbox.com/s/orpme8k2ld264k6/class21.pdf?dl=0)]
- Reduction Proofs
- Recognizability
- Non-recognizability of the complement of HALTS

[Class 22: Rice's Theorem](/class22) [[Slides](https://www.dropbox.com/s/todwiwrz55rk3zz/class22.pdf?dl=0)]
- Recognizability
- Rice's Theorem
- Kolmogorov Complexity

# Complexity

[Class 23: Complexity](/class23) [[Slides](https://www.dropbox.com/s/2vmiv30msouz2vy/class23.pdf?dl=0)]
- Cost of Computing
- Defining <em>TIME</em><sub>TM</sub>(_T_(_n_))
- Class <b>P</b>
- Robustness of <b>P</b>
- Polynomial-Time Reductions

[Class 24: Complexity II](/class24) [[Slides](https://www.dropbox.com/s/0dd0ryl36xv54sd/class24.pdf?dl=0)]
- Cook Reductions and Karp Reductions
- 3SAT and CircuitSAT

[Class 25: Probably Hard Problems](/class25) [[Slides](https://www.dropbox.com/s/75jnbnk1ygipb75/class25.pdf?dl=0)]
- Complexity classs <b>NP</b>
- Introducing the question is <b>P</b> a proper subset of <b>NP</b> (<b>P</b> = <b>NP</b>)?
- Cook-Levin Theorem

[Class 26: Cook-Levin Theorem](/class26) [[Slides](https://www.dropbox.com/s/0u27f3qd5ry7auj/class26.pdf?dl=0)]
- Nondeterministic Turing Machines
- Proving the Cook-Levin Theorem
- Implications of P = NP
