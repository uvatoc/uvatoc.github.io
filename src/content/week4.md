+++
draft = false
title = "Week 4"
slug= "week4"
+++

# Week 4: Universal gates and Evaluation

The main goals for Week 4 are to:

- Implement and use the EVAL function. This is our first exposure to a modul of computing which is able to simulate an instance of itself. This idea is fundamental to the practice of computer science, as it enables us to have arbitrarily reprogrammable machines which run with fixed hardware.
- Begin classifying functions by complexity (i.e. resources required to implement them).
- Reason about how theory and practice might differ from one another, and why that might be a good thing.

# Peer Evaluation

Your first peer evalution is due by your week 4 prep meeting. Please complete it following these instructions: [Peer Eval](/peer_eval).


# Schedule


|       Day       | "Monday" Cohort | "Tuesday" Cohort | "Wednesday" Cohort | "Thursday" Cohort  |  "Friday" Cohort   |
| :-------------: | :-------------: | :--------------: | :----------------: | :----------------: | :----------------: |
|**Wed** 15 Sept|Preparation|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|
|**Thurs** 16 Sept|Preparation|Preparation|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|
|**Fri** 17 Sept|Preparation|Preparation|Preparation|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|
|**Sat** 18 Sept|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|<font color="lightgray">(Week 3)</font>|
|**Sun** 19 Sept|Revision|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|
|**Mon** 20 Sept|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|Preparation|
|**Tues** 21 Sept|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|
|**Wed** 22 Sept|<font color="lightgray">(Week 5)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|
|**Thurs** 23 Sept|<font color="lightgray">(Week 5)</font>|<font color="lightgray">(Week 5)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|
|**Fri** 24 Sept|<font color="lightgray">(Week 5)</font>|<font color="lightgray">(Week 5)</font>|<font color="lightgray">(Week 5)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|
|**Sat** 25 Sept|<font color="lightgray">(Week 5)</font>|<font color="lightgray">(Week 5)</font>|<font color="lightgray">(Week 5)</font>|<font color="lightgray">(Week 3)</font>|**Writeup Due**|


# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

- [Cohort Problems for Week 4 [PDF]](/ps/week4_blank.pdf)
- [LaTeX Template for Week 4 [ZIP]](/ps/week4.zip)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

The above problems include completing the function implementations in
this python file (the comments in the file itself will guide you,
please read everything linearly): [eval.py](/ps/eval.py).

If you already have python3 on your machine, you should be good to go
for the programming problems. If you don't, please [follow these directions to setup Python](/python). 

# Reading

- [Ch. 4, Syntactic sugar and computing every function](https://introtcs.org/public/lec_03a_computing_every_function.html) from the TOC textbook. In particular, we cover sections 4.4, 4.5, and 4.6 this week.
- [Ch. 5, Code as data, data as code](https://introtcs.org/public/lec_04_code_and_data.html) from the TOC textbook. In particular, we cover sections 5.1 through 5.5. We are skipping the optional section 5.2.1.


You can play all the videos using this playlist, but don't forget to take breaks: [Week 4 Playlist](https://www.youtube.com/playlist?list=PLZ9Gk_8DtbmHkfZhvvGd7sam0MMjUhfPC)

<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Spring 2020) Feb 6: Universality - [Unedited Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=09d785d3-29eb-45a5-9cfb-ab590151f099) [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/universality_written.pdf)
- (Spring 2020) Feb 11: Evaluation - [Unedited Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=cd4c8fde-c3db-4dcf-8f51-ab5e01527773) [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/complexity_written.pdf)

</p>

<p>Week 4 Intro<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/zDp_h_yLm1A' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Computing Any Finite Function<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/vE-N_ErO7W0' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>Making Zero and One<br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/v3mw1sHrZbo' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br></p>

<p>How Many Gates?<br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/WPllMBJC0q0' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br></p>


<p>Introducing EVAL<br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/HTHYjpgyWNY' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br></p>

<p>Representing Programs<br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/RNN-hW9x_8Y' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br></p>



<p>Defining EVAL<br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/5RbgIcs0bEw' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br></p>

## Bonus Video

<p>The 10,000 Domino Computer (from <em>Stand-up Maths</em>)<br>
<iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/OpLU__bhu2w' frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br></p>

