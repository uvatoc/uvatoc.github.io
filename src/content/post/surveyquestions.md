+++
date = "01 Feb 2023"
draft = false
title = "Answers to Course Registration Survey Questions"
author = "David Evans"
slug = "surveyanswers"
+++

Here are my (Dave) answers to questions from the course registration
survey. If you have new questions that weren't answered, or want to
follow-up on anything, please feel free to do so either in office
hours, on Discord, or by email.

> _Do you two have a passion for computer science or a specific topic within computer science, why is that? What do you think about you or your past primed you to develop this interest?_

I first encountered computers back when I was in second grade and my school got a teletype terminal - this was a machine where you would dial a phone number on a phone handset to connect to the one computer the school district had, and connect it with an audio coupler, and then have messages print out (no screen) on a dot matrix printer and keyboard you could send commands to the computer. You could already play games this way, and I learned a few simple things in BASIC. Once I saw the program,
````
10 PRINT "DAVE"
20 GOTO 10
````
that would run forever printing my name, I was hooked! A year or so
later we got Apple II's which had an actual screen and you could make
graphics on it (black and white, still only uppercase letters).

I was interested in playing with and building things on computers, but
it was much later to get into any kind of theoretical interest. This
was mostly sparked by reading Doug Hofstadter's _G&ouml;del, Escher,
Bach_ in high school which raised all sorts of deep questions about
what computers can and cannot do.

The main topics I'm most interested in computing today are reflected
in what my research group works on, which you can see here:
[https://uvasrg.github.io/](https://uvasrg.github.io/). In general,
I'm interested in how to make computing work even when there are
adversaries trying to break things (which mostly involved thinking
about and experimenting with what adversaries might do to try and
break computing systems). Today, we're mostly focused on understanding
and mitigating potential harms from machine learning.

> _how far are we until quantum computing is in our hands_

In your hands may be a while off, but being able to use some form of
quantum computing in a data center is already possible. None of the
commercially useful "quantum" computing services, though, are actually
general purpose quantum computers, they are using properties of
quantum physics to do certain optimization problems efficiently. There
are demonstrations of "general purpose" quantum computers in research
labs, and some controversy over whether there have been any
demonstrations of quantum computers actually computing something that
couldn't be computed more efficiently with a classical computer, but
then things they actually compute are contrived problems (e.g.,
simulating quantum circuits) that are constructed to demonstrate
quantum computing but not otherwise useful.

As for the question of when there will be practical quantum computing
available that can solve problems that would break modern
cryptography, the best guesses are this is somewhere between twenty
and unlimited years in the future, but very hard to guess since many
breakthroughs are still required.


> _More about instructor backgrounds_

You can find a lot about me on my website, [https://www.cs.virginia.edu/evans](https://www.cs.virginia.edu/evans), but feel free to ask any questions you want.

> _Where will we be able to find a schedule of readings to stay consistent with the lecture materials?_

The problem sets (posted on Mondays, and due the following Monday)
should give you a clear idea of what we will be covering in the
upcoming week. If you want to go further ahead than this, we will
mostly be following the course textbook in order (at least until later
in the semester). You can also see materials from previous versions of
the course (here is the [schedule from Fall
2021](https://uvatoc.github.io/f21/schedule/) which will give you a
good idea of where we are going, and includes reading links and videos
for each week).

> _As mentioned in the article Habits of Highly mathematical people, I think it is still a valid question to ask how the knowledge we take away from this class can be effectively be used in my career in Software Engineering._

I'll answer the question next, but my first reaction to this is that
if your only goal is to have a successful career in software
engineering, you should consider if spending your time and tuition
money doing a degree at UVA is the best path. There are many cheaper
and easier ways to learn to be a good software engineer, and although
there will be some hurdles to a successful career without having the
stamp-of-approval-and-compliance that comes with a prestigious college
degree, computing is still an area where there are many ways to
demonstrate your talents and be successful without this. The way to
become a great software engineer is to practice writing a lot of
software; to read, understand, and modify software built by great
software engineers (which open source allows anyone to do); and to
work together on projects with experienced and talented software
engineers. We can try to offer you small slices of some of these
experiences as a student in classes here, but nothing approaching what
you could learn on your own.

That said, I hope there is value you can get by being a student at UVA
that goes beyond what is most useful for having a career as a software
engineer and what people can learn better by doing software
engineering outside of an academic environment. Some of this is
towards being an educated person, and the intrinsic value this holds
in improving your experience of the world and the likelihood you will
do things that improve it for others. (Andrew Abbott's welcome to
students at the University of Chicago provides some insights on this:
[_Aims of Education Address
2002_](https://college.uchicago.edu/student-life/aims-education-address-2002-andrew-abbott).)

As to more concrete things from this class that may improve your
career as a software engineer:

- We hope the experience you will get in this class thinking precisely
  about definitions and getting practice with formal definitions will
  help you communicate better and think precisely about software
  problems, even if you are not doing formal mathematics in them.

- We hope the experience you get thinking about problems deeply in
  this class will help you more precisely consider computing problems
  you encounter in software engineering, and frame those problems in
  ways that lead to more elegant and efficient solutions. (Most of
  industrial software engineering is about glue and deciding how to
  use APIs, but occasionally interesting computing problems come up
  that require novel solutions, and those should be the opportunities
  where you can best distinguish yourself.)
  
- We hope what you will learn in this class about the theoretical
  limits of computing and how they connect to practical limits on what
  can be done will help you make better decisions about what to do
  when you encounter difficult problems you want to produce software
  to solve.

- We will have some assignments where you do practice programming,
  with a different emphasis and approach from what you would have in a
  software engineering class, but still in ways that we hope will
  continue to develop your skills.

It is true, though, that there are many great software engineers who
have no understanding of the theory of computation, so although we are
optimistic that things you get from this class will make you a better
software engineer it would be foolhardy to claim that having a strong
background in theory of computation is necessary to be a successful
software engineer.


> _What are your histories? Why do you personally want to teach this class? I would like to learn how computing can be better utilized in today's world and part of answering how it can be "better utilized" is to know where it cannot be utilized. So I want to know if there are any strong clues when asked a business problem that will tell a future tech worker like me that this problem cannot be solved with computers._

I grew up in the northern suburbs of Detroit, Michigan, to parents who
imigrated to the United States from Britian. I wrote above about how I
got into computing. I went to MIT for college, and stayed through PhD
(with some excursions doing a start-up), and came to UVA after
completing my PhD and have been here since then (also with some
temporary excursions doing a start-up and visits elsewhere).

I love teaching this class since it gets at topics that I think are
fun and deep, and is the first time most students in this class think
about these things. I'm also delighted to have an opportunity to
co-teach with Mohammad, who is a very accomplished theoretical
researcher with much deeper understanding of most of the topics in
this class than I have, so hope to learn a lot from this. In general,
I teach a wide variety of topics, including both systemsy courses and
theoretical courses, as well as courses in biology, economics, and
ethics (see [my courses
page](https://www.cs.virginia.edu/~evans/courses) for a full list),
and like to teach courses where I can learn something new, and where I
can hopefully introduce students to new ideas that they will find
exciting and interesting.

On the business problem question, maybe not interpreting this the way
you asked, but I think there are huge dilemmas for emerging computer
scientists today about how to do work that actually is beneficial to
the world as a whole, or at least not harmful to it. This is both
important at the personal level in doing things that are fun and
meaningful to you as an individual, but also at the larger level of
thinking about how these things will impact others and how the
organization you may be working for is impacting society overall. I
don't think there are any easy answer to this, but it is something I
hope all of you will think about as you approach your careers. (Some
of my written thoughts related to this are [this write-up of a talk at
Google](https://uvasrg.github.io/google-federated-privacy-2019-the-dragon-in-the-room/) and some more optimistic thoughts on [how computing will impact future jobs for humans](https://uvasrg.github.io/jobs-for-humans-2029-2059/).)

> _Do we discuss AI?_

Yes, at least in passing. If we have time later in the semester, we
might get into some of the interesting theoretical questions about
machine learning, and maybe have an aside on how Alan Turing thought
about artificial intelligence. But, it won't be a major part of this
course.

> _Will we see the results of computational theory currently being researched?_

We've already touched on how there is active research on the
computational complexity of multiplication in the first few
classes. We'll mention some other active areas of theoretical research
during the semester. Many of the topics we will cover in the class and
that you should understand well are open questions for theory of
computation researchers today (the most famous and obvious being the P
= NP question which you should understand well by the end of the
course), but actually deeply understanding recent progress on these
issues would require going quite a bit beyond what we'll be able to
cover in this introductory course, although I hope we'll be able to
give you some sense of where things stand and how people work on these
types of problems.

> _How closely tied are the contents of the textbook to the contents of the course? How comprehensive is the information in the textbook?_  

We will follow the textbook quite closely, and nearly everything we
expect you to learn in the class will be covered both in the lectures
and in the textbook. The textbook is quite comprehensive on the topics
we cover, and presents them very well (although sometimes challenging
for most students to understand from the textbook alone).

We do aim to provide a different perspective on
things in the lectures that you would get from just the textbook, and
to go into some aspects in more depth than the book does, and
definitely do not try to cover everything that is in the textbook in
class.

> _How many proofs will we write?_

The number of proofs you write will be countable, and I can even
promise it will be finite (although you may consider proof-generating
systems that can generate a countably infinite, but not uncountable,
number of proofs)!

> _Do the instructors have any pets? Would love to see some pictures of them :)_

I don't have any pets now, but we did get a "pandemic hamster"
(actually, three - "Humphrey" escaped the first night and was never to
be found, "Humphrey 2" survived about 2 days, but "Micee" lasted
nearly a year, which I guess is pretty good for a hamster).

<center>
<img src="/images/hamster.jpg" width="70%"><br></br>
<p></p>
<img src="/images/hamster2.jpg" width="90%"><br>
</center>

> _I would like to know what are the most challenging topics we are going to cover and how to best succeed in this class._ 

This depends a lot on what your definition of "success" is.

If it means passing the class with the minimum amount of effort, I
think this is quite easy. I'm very reluctant to fail students who show
a non-negligible sign of effort in a class, so as long as you submit
most of the assignments and put something resembling an answer for
around half the question, and show up for the exams and write
something that looks like an attempt to answer and at least show some
understanding for a few questions, you'll almost certainly pass the
class.

If your definition of "success" is getting an "A" with the minimum
amount of effort, then I would say focusing on understanding the
problem sets will be the best strategy for most students. Depending on
how you learn best, this might mean working on the problems yourself
or might mean finding a study group that works well together to work
on the problems, and learning from the process of trying to solve the
problems and convincing yourself (and your study groupmates if you
work with others) when you have a good answer, and taking good
advantage of the available help in office hours. Then, looking at the
graded feedback and posted solutions for the problems and trying to
understand any places where your answers were deficient. Hopefully
you'll also find class worthwhile and the textbook useful, but I think
both of those are secondary to what you will learn by working on
problems.

Finally, if "success" means getting the most long term and meaningful
benefit you can from the course based on the time you invest in it
(which I hope is the right notion of success for most of you), I would
encouage you to be open about your own interests and abilities and not
assume that because something is hard at first that it isn't something
that you would enjoy and could be terrific at; and to go deeply into
the things you encounter during the class that strike you as most
mysterious, surprising, or confusing, and to come to office hours to
discuss them with myself or Prof. Mahmoody. This might not be optimal
for the previous definition of success where its best to just get
above some expected threshold in everything consistently (and this is
the nature of most grading systems used in school, but very little
outside the academic world), but would be a more important definition
of success in the long term.

As for the most challenging topics in the class, I think there are
some ideas that are very difficult conceptually such as wrestling with
the difference between unbounded finite values and infinite ones, and
what our mathematical models really mean, and other topics that are
more technically challenging. In general, the course will build upon
ideas as we go through the semester, so you should expect things to
get more challenging as the course progresses, but that you'll be
prepared for later topics by the earlier ones.

> I want to continue strengthening my knowledge of the "language" of
  discrete math. In CS3100 this past fall, I found that it took me
  longer than I would have liked to decipher the meaning of the
  symbolic terminology which was quite common on a lot of the slides
  and in the textbook, which harmed by comprehension ability, forcing
  me to review more on my own.  I hope that with additional exposure,
  this process eventually becomes second nature to me, and I'll be
  able to just focus on the content itself.

These are skills that improve with practice, and as you get more
experience understanding formal definitions you'll be able to
understand them more quickly and deal with more complex
ones. Terminology and notation can sometimes be a hurdle, but I
believe we'll only use a few notations in this class that you won't
have already seen in CS3100 (and most are notations that you've
probably seen since middle school), and we will aim to get a lot of
value from a small number of carefully and precisely defined terms.

> I would like to know how to approach very complicated problems and
  how to better understand them. I feel like often times when I see a
  complicated problem, I feel sort of "out in open water" and without
  the tools to help me.

The best way to approach complicated problems is to turn them into
simple problems.  One of the goals of this class is to develop
abstractions and techniques that will help you do that. (Of course,
some problems remain complicated, no matter how hard you try to
simplify them.)



