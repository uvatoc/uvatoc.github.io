+++
date = "05 Nov 2020"
draft = false
title = "Week 11"
slug="week11"
+++

# Goals

This week we arrive at the most famous and foundational open problem
in Computer Science (and, arguably, in all of Mathematics, and more
questionably, perhaps of all human creative endeavor): _is it
substantially easier to verify the solution to a (certain very broad
and common type of) problem, than it is to find that solution?_
(stated more formally in computer science as "P = NP?".

The main goals for Week 11 are to:

- Understand how to talk about the hardness ("difficulty") of computing functions.
- Learn about a few examples of problems that appear to have surprisingly different difficulties.
- Be able to talk about the _tractability_ of problems, and understand what computer scientists categorize problems as tractable and intractable the way we do.
- Understand precisely the definition of the complexity class NP, and two different ways of defining it.
- Be able to prove a problem is in class NP.
- Understand the P=NP question and its significance.
- See how we might be able to make progress on determining if P=NP, and understand the Cook-Levin Theorem and the main idea behind its proof.

# Schedule

Following the Election Day adjustments, the "Tuesday" cohorts are now the last ones in the schedule, and the week starts with the "Wednesday" cohorts.

<table class="schedule">
  <thead>
    <tr>
      <th text-align="center">Day</th>
      <th align="center">"Wednesday" Cohort</th>
      <th align="center">"Thursday" Cohort</th>
      <th align="center">"Friday" Cohort</th>
      <th align="center">"Sunday" Cohort</th>
      <th align="center">"Monday" Cohort</th>
      <th align="center">"Tuesday" Cohort</th>
    </tr>
  </thead> 
  <tbody>
</tr>

<tr><td><b>Thu</b> 5&nbsp;Nov</td>     <td>Preparation</td> <td bgcolor="lightyellow">(Week 10)</td> <td bgcolor="lightyellow">(Week 10)</td>	 <td bgcolor="lightyellow">(Week 10)</td>
<td bgcolor="lightyellow">(Week 10)</td>
<td bgcolor="lightyellow">(Week 10)</td>
</tr>
<tr><td><b>Fri</b> 6&nbsp;Nov</td>   <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 10)</td>	<td bgcolor="lightyellow">(Week 10)</td>	<td bgcolor="lightyellow">(Week 10)</td>	  <td bgcolor="lightyellow">(Week 10)</td>	  
</tr><tr><td><b>Sat/Sun</b> 7/8&nbsp;Nov</td>  <td>Preparation</td>      <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 10)</td>  <td bgcolor="lightyellow">(Week 10)</td> <td bgcolor="lightyellow">(Week 10)</td>

</tr><tr><td><b>Mon</b> 9&nbsp;Nov</td>    <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td>     <td>Preparation</td> <td bgcolor="lightyellow">(Week 10)</td><td bgcolor="lightyellow">(Week 10)</td>

</tr><tr><td><b>Tue</b> 10&nbsp;Nov</td>      <td>Preparation</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td> <td>Preparation</td> <td>Preparation</td> <td bgcolor="lightyellow">(Week 10)</td>

</tr>

<tr><td><b>Wed</b> 11&nbsp;Nov</td>      <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>        <td><b>Cohort Meeting</b></td> <td>Preparation</td> <td>Preparation</td> <td>Preparation</td>
</tr><tr>
<td><b>Thu</b> 12&nbsp;Nov</td>
 <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td>
 <td>Preparation</td> <td>Preparation</td>
</tr>

<tr>
<td><b>Fri</b> 13&nbsp;Nov</td>  <td bgcolor="lightblue">Week 12</td>
<td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></td> <td>Preparation</td>
<td><b>Cohort Meeting</b></td><td>Preparation</td>
</tr>


<tr><td><b>Sat/Sun</b> 14/15&nbsp;Nov</td> <td bgcolor="lightblue">Week 12</td> <td bgcolor="lightblue">Week 12</td> <td> <font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td><td>Preparation</td><td><b>Cohort Meeting</b></td>
</tr>

<tr><td><b>Mon</b> 16&nbsp;Nov</td>  <td bgcolor="lightblue">Week 12</td> <td bgcolor="lightblue">Week 12</td> <td bgcolor="lightblue">Week 12</td>
<td> <font color="blue"><b>Write-up Due</b></font></td>
<td><font color="red"><b>Assessed Cohort Meeting</b></font></td>
<td>Preparation</td>
</tr>

<tr><td><b>Tue</b> 17&nbsp;Nov</td> <td bgcolor="lightblue">Week 12</td> <td bgcolor="lightblue">Week 12</td> <td bgcolor="lightblue">Week 12</td> <td bgcolor="lightblue">Week 12</td>
<td> <font color="blue"><b>Write-up Due</b></font></td> 
<td><font color="red"><b>Assessed Cohort Meeting</b></font></td>
</tr>

<tr><td><b>Wed</b> 18&nbsp;Nov</td> <td bgcolor="lightblue">Week 12</td><td bgcolor="lightblue">Week 12</td> <td bgcolor="lightblue">Week 12</td> <td bgcolor="lightblue">Week 12</td> <td bgcolor="lightblue">Week 12</td>
<td> <font color="blue"><b>Write-up Due</b></font></td> 
</tr>

</tbody>
</table>

<a name="problems"></a>
# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

[Cohort Problems for Week 11 [PDF]](/ps/ps11.pdf)<br>


The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

After the Assessed Cohort Meeting, your Cohort Leader will select one
problem that your cohort needs to write-up and submit.  The write-up
is due by **11:59pm** on the day after your assessed cohort meeting
(see the schedule above).

[Problem Set 11 Template [zip]](https://uvatoc.github.io/ps/ps11template.zip).

# Reading

This week's content is covered in several chapters in the TCS
book. This is a lot of reading material, but you should consider it
all "optional" this week - you are not expected to read these in
detail, but should find the textbook a useful complement to the
lecture content to have an alternate presenation of the materials and
a refernce for some of the technical details that we do not cover in
depth in the lectures.

[Chapter 12: _Efficient computation: An informal introduction_](https://introtcs.org/public/lec_10_efficient_alg.html) [[PDF](https://files.boazbarak.org/introtcs/lec_10_efficient_alg.pdf)]

[Chapter 13: _Modeling running time_](https://introtcs.org/public/lec_11_running_time.html) [[PDF](https://files.boazbarak.org/introtcs/lec_11_running_time.pdf)]

[Chapter 14: _Polynomial-time reducations_](https://introtcs.org/public/lec_12_NP.html) [[PDF](https://files.boazbarak.org/introtcs/lec_12_NP.pdf)]

[Chapter 15: _NP, NP completeness, and the Cook-Levin Theorem_](https://introtcs.org/public/lec_13_Cook_Levin.html) [[PDF](https://files.boazbarak.org/introtcs/lec_13_Cook_Levin.pdf)]

[Chapter 16: _What if P equals NP?_](https://introtcs.org/public/lec_14_PvsNP.html) [[PDF](https://files.boazbarak.org/introtcs/lec_14_PvsNP.pdf)]


# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 11 Playlist](https://www.youtube.com/playlist?list=PLvpsxlEF9cP2X24P7LUcH3eIj-6nEocmS)

<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Fall 2019) [Class 19: Turing Machine running time](https://uvatoc.github.io/f19/class19/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3e454df5-59af-4a8b-a257-ab020151ee1b), [Slides](https://www.dropbox.com/s/vcsuqjrnqld3lhk/class19_written.pptx?dl=0)

- (Fall 2019) [Class 20: Polynomial-Time Reductions](https://uvatoc.github.io/f19/class20/) (despite this being one of our favorite topics, this is mostly skipped): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5502d967-a9a6-402b-842e-ab040151b68a), [Slides](https://www.dropbox.com/s/u79nw0c5dpgkb22/class20_written.pptx?dl=0)

- (Fall 2019) [Class 21: Is Omniscience Helpful?](https://uvatoc.github.io/f19/class21/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2065c1c3-8d0f-4fbd-8005-ab0901519772), [Slides](https://www.dropbox.com/s/84jpjahs7afgvfv/class21-post.pdf?dl=0)

- (Fall 2019) [Class 22: NP Completeness](https://uvatoc.github.io/f19/class22/): [Fall Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=cb91d06d-83f5-47d8-a05c-ab0b0151a8de), [Slides](https://www.dropbox.com/s/rqtkwlp6hk9m7vo/class22-post.pdf?dl=0)

</p>

<p>"Difficulty" of Functions (9:13) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/PosxxVwgggI' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>RAM Model (7:00) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/tcjSV1QSdn8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Shortest and Longest Path (11:16) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/g5Zpffr4Wog' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Satisfiability (14:45) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/cMEKwh614mk' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Tractable and Intractable Problems (6:38) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/SspCMbUF6Xs' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Questions about P and EXP (5:02) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/rK_4nS4_KTI' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Introducing NP (14:02) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/BmXyo9acRWA' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Complexity Class NP (13:08) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/vvUrXg1mQzs' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Power of Nondeterministic Turing Machines (11:57) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/MisQhVRJ7xk' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Proving a Problem is in NP (7:50) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/TATffY3xHLs' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>The P=NP Question (9:12) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/FQCWOeS9GC4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Cook-Levin Theorem (17:02) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/hEmxUEnDEWw' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>History of the Cook-Levin Theorem (8:31) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/SrXHplvYAJ8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>P=NP Recap (4:45) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/my-mxCwArk8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>
