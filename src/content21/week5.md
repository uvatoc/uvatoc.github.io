+++
draft = false
title = "Week 5"
slug= "week5"
+++

# Goals

The main goals for Week 5 are to:

- Understand what a complexity class is and how to provide properties about circuit-size complexity classes.
- Learn the asymptotic operators (Big-<em>O</em>, &Omega;, and &Theta;) and how to use them correctly.
- Be able to both intuitively understand what functions are in <em>O</em>(<em>f(<em>n</em>)</em>), and to prove membership or non-membership.
- Be able to connect the formal definitions of computing costs to practical questions about the cost of computing.


# Schedule


|       Day       | "Monday" Cohort | "Tuesday" Cohort | "Wednesday" Cohort | "Thursday" Cohort  |  "Friday" Cohort   |
| :-------------: | :-------------: | :--------------: | :----------------: | :----------------: | :----------------: |
|**Wed** 22 Sept|Preparation|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|
|**Thurs** 23 Sept|Preparation|Preparation|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|
|**Fri** 24 Sept|Preparation|Preparation|Preparation|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|
|**Sat** 25 Sept|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|<font color="lightgray">(Week 4)</font>|
|**Sun** 26 Sept|Revision|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|
|**Mon** 27 Sept|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|Preparation|
|**Tues** 28 Sept|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|
|**Wed** 29 Sept|<font color="lightgray">(Week 6)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|
|**Thurs** 30 Sept|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|
|**Fri** 01 Oct|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|
|**Sat** 02 Oct|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|**Writeup Due**|

# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:


- [Cohort Problems for Week 5 [PDF]](/ps/week5_blank.pdf)
- [LaTeX Template for Week 5 [ZIP]](/ps/week5.zip)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

There is no programming problem this week.

## Writeup Problem

You writeups for this week will work a little differently from previous weeks. Since we will have a final exam in the course (and a midterm-like activity during the week of fall break) we wanted to give you experience solving problems on your own so that you can check your progress. As such, this week's writeup will not be taken directly from this week's problem set, and instead will be a new problem in the same style as problem 4.

# Reading

This week focuses on material in [Chapter 5: Code as data, data as
code](/docs/tcs-chapter5.pdf) from the TCS textbook (which you already
read last week, but we go into more depth on this week). The main theorems we focus on are in [Section 5.2](https://introtcs.org/public/lec_04_code_and_data.html#countingcircuitsec).

The TCS book does not provide a detailed presentation of the
asymptotic operators, but reviews them in [Section
1.4.8](https://introtcs.org/public/lec_00_1_math_background.html#secbigohnotation). Many
books provide more detailed presentations of these concepts, and lots
of examples. If you would like a more complex textbook explanation,
the course instructors (at least one of them!) recommends this
chapter: [Chapter 7: Cost](https://computingbook.org/Cost.pdf) (from [_Introduction to Computing
Explorations in Language, Logic, and Machines_](https://computingbook.org/)).

# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 5 Playlist](https://www.youtube.com/playlist?list=PLZ9Gk_8DtbmFH0b5mWFYcA5bOiNdkjCBQ)

<p>Week 5 Intro (4:38)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/gk9Gt5Pbb1w' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Introducing Complexity (5:37)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/HOgP-99MFoU' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Introducing SIZE (5:59)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/SfS3nl9O190' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Our First Complexity Proof (11:38)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/SSXy7BbuZGM' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Asymptotic Operators (7:06)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/96XtkxDNDCs' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Understanding Asymptotics (10:40)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/KA8uSlGqc_o' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Big-Oh Examples (17:04)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/iG_BGStzPQE' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Using Big-O (4:52)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/ZPVsL3mCxkg' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Common Misuses of Asymptotic Notation (5:52)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/WLV99-6ep2c' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Some Functions Are Expensive (7:36)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/BavLtSyKlFg' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Cost of Computing (5:03)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/5H6DvmEzwDY' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>