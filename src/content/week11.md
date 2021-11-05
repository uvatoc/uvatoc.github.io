+++
draft = false
title = "Week 11"
slug= "week11"
+++

# Goals

This week, we hope you'll become comfortable proving functions are
uncomputable (and occasionally, computable). We introduce the "proof
by reduction" technique, which is a tremendously useful way to prove
properties about problems, and (as you will see in the Algorithms
class) also to develop and analyze algorithmic solutions.

The main goals for Week 11 are to:

- Become comfortable with the terms _decidable_, _recognizable_, and _computable_, and how we talk about these properties for languages, functions, and problems.
- Learn how to do a proof by reduction, and to avoid the common pitfalls in constructing reduction proofs.
- Gain experience proving problems are computable and uncomputable (we use the terms <em>un</em>computable and <em>non</em>computable interchangably).

# Schedule


|       Day       | "Monday" Cohort | "Tuesday" Cohort | "Wednesday" Cohort | "Thursday" Cohort  |  "Friday" Cohort   |
| :-------------: | :-------------: | :--------------: | :----------------: | :----------------: | :----------------: |
|**Wed** 03 Nov|Preparation|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|
|**Thurs** 04 Nov|Preparation|Preparation|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|
|**Fri** 05 Nov|Preparation|Preparation|Preparation|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|
|**Sat** 06 Nov|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|<font color="lightgray">(Week 10)</font>|
|**Sun** 07 Nov|Revision|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|
|**Mon** 08 Nov|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|Preparation|
|**Tues** 09 Nov|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|
|**Wed** 10 Nov|<font color="lightgray">(Week 12)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|
|**Thurs** 11 Nov|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|
|**Fri** 12 Nov|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|
|**Sat** 13 Nov|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|**Writeup Due**|

# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

- [Cohort Problems for Week 11 [PDF]](/ps/week11_blank.pdf)
- [LaTeX Template for Week 11 [ZIP]](/ps/week11.zip)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

Similarly to Week 5, for this week you will be assigned a _new_
problem to solve for your write-up problem which you will need to
solve on your own without any collaboration. This will be due 48 hours
after your cohort meeting (instead of the usual 24 hours). This
problem will expect you to do a reduction proof, similar to the ones
in the cohort problems (but different enough to be new).

# Reading

[Chapter 9: _Universality and uncomputability_](https://introtcs.org/public/lec_08_uncomputability.html) [[PDF](https://files.boazbarak.org/introtcs/lec_08_uncomputability.pdf)]

You should have already read through the Section 9.3 (but reread any parts you are confused on), and read the new Sections 9.4 and 9.5 for this week.

# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 11 Playlist](https://www.youtube.com/playlist?list=PLZ9Gk_8DtbmHUXYIy97AXgcc2kzB9vRPF) (note that in past weeks this unit was labelled as Week 10)
<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Fall 2019) [Class 16: Reductions](https://uvatoc.github.io/f19/class16/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d36c3729-5dbc-43e9-aebd-aaf40141ae83), [Slides](https://www.dropbox.com/s/ww3pqjm7v6nc8uq/class16_written.pptx?dl=0)

- (Fall 2019) [Class 17: Rice's Theorem](https://uvatoc.github.io/f19/class17/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3c2428a4-02a2-499e-af00-aaf601419207), [Slides](https://www.dropbox.com/s/pml6l1teoxa7y5s/class17_inked.pptx?dl=0). (Note that we do not include the first half or so of this class in the edited videos, which presents two more examples of uncomputability proofs by reduction. If you'd like to see more examples of these kinds of problems, please watch the full video for this class.)

- (Fall 2019) [Class 18: Review for Exam 2](https://uvatoc.github.io/f19/class18/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7ce45bc2-ca94-402e-84ac-aafb01519dbc), [Slides](https://www.dropbox.com/s/c2ciuclc2zjgqtk/class18-post.pdf?dl=0). We include a few example problems from this exam review lecture, that we think will be helpful to you for the cohort problems this week.

<p>Week 10 Intro (3:58) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/hP9TjCs5vqI' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Decidable, Recognizable, Computable (7:18) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/ZjQHbxCExsg' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>An Undecidable Problem (8:10) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Bit7FvUzcMU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>



<p>Proof by Reduction (17:54) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/tEp6j_owBSs' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>HALTS is Undecidable (7:19) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/UObqrnIHHbI' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Finite is Undecidable (11:38) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/C4CZoVxJT9o' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Prints3 and IsMalware Are Undecidable (5:15) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/5VKf11so0XE' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Rice's Theorem (15:28) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/U1aEDWBNQ3A' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>

The following three videos are problems from the exam review, so do
not introduce new material, but provide more examples of how to prove
functions are computable or uncomputable. You can find the problems they cover here: [Fall 2019 Exam 2 Practice Problems](https://uvatoc.github.io/docs/exam2practice.pdf), and are encouraged to try to solve them yourself before watching the videos. The _Natural Numbers are Computable_ video is about Problem 9, and the _Proving Uncomputability_ video is about Problem 14.

</p>

<p>Proving Computability and Noncomputability (7:57) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/3cSkH-kDlxg' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>The Natural Numbers are Computable (2:43) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/KPamvxCaepU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Proving Uncomputability (Busy Boas and Busier Beavers) (8:55) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/cue964eNyqA' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

