+++
date = "03 Feb 2023"
draft = true
title = "On Mappings"
author = "Course Staff"
katex = true
+++

As discussed in [Class 5](/class5), there was a problem on Quiz 2 that
both the professors got wrong probably more than once.

Although it was meant to be a fairly straightforward multiple choice
question, it illustrates how tricky it is to think about the
subtleties of simple definitions on binary relations and the
importance of precise definitions.

The question, as asked on Quiz 2 is below:

**Question 2: Notions of Relations**

Which of the following are true statements for *all* sets \\(X\\) and \\(Y\\)? Choose all that are correct:

1. If there is a bijection between sets \\(X,Y\\), then there is an injective \\((\le 1\\) in) function (\\(\le 1 \\) out) from \\(X\\) to \\(Y\\).  
2.  If there is a partial function from \\(X\\) to \\(Y\\), then there is surjective mapping \\((\ge 1\\) in) from \\(Y\\) to \\(X\\).  
3. There is a total (\\( \ge 1\\) out) function from \\(Y\\) to \\(X\\) if and only if there is a surjective mapping from \\(X\\) to \\(Y\\).  
4. If there is a surjective total function from \\(X\\) to \\(Y\\), then there is an injective mapping from \\(X\\) to \\(Y\\).

In class, we decided that choice 1 was definitely correct, but there
was some doubt on the other three choices and confusion about the
meaning of _mapping_ which we didn't define (the TCS book uses the
term mapping frequently, but does not formally define it; the [MCS
(cs2102) book](https://uvacs2102.github.io/docs/mcs.pdf), uses
"Mapping Rules" to talk about different kinds of binary relations;
according to
[wikipedia](https://en.wikipedia.org/wiki/Map_(mathematics)), mapping
usually means "total function", and "partial map" is used ot mean
"partial function").

Assuming "mapping" means "total function", we believe statements 2, 3,
and 4 are all false.

If "mapping" means "binary relation" (which does not add any
constraints), then statements 2 and 4 are true, and statement 3 is
false.

We'll leave it as a <span class="challenge">challenge problem</span>
for students to come up with some other non-crazy interpretation of
"mapping" that would make any other combination of these statements
true. (By "non-crazy", we mean it has to be a definition that makes at
least some sense in a general context, not being specifically
contrived to have different meanings based on the question specifics.)

The way challenge problems work is the first student to provide a
solution the professors this is interesting and valuable enough in
response to the challenge will receive bonus points (in an amount that
it totally at our discretion, but might be as much as a full problem
set or more); once a solution has been accepted, the challenge isn't
necessarily closed, but for a subsequent solution to also receive a
bonus it would have to offer substantial value beyond the first
accepted solution.




