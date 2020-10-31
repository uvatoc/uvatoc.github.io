+++
date = "27 Oct 2020"
draft = false
title = "Week 10"
slug="week10"
+++

# Goals

This week, we hope you'll become experts at proving functions are
uncomputable (and occasionally, computable). We introduce the "proof
by reduction" technique, which is a tremendously useful way to prove
properties about problems, and (as you will see in the Algorithms
class) also to develop and analyze algorithmic solutions.

The main goals for Week 10 are to:

- Become comfortable with the terms _decidable_, _recognizable_, and _computable_, and how we talk about these properties for languages, functions, and problems.
- Learn how to do a proof by reduction, and to avoid the common pitfalls in constructing reduction proofs.
- Gain experience proving problems are computable and uncomputable (we use the terms <em>un</em>computable and <em>non</em>computable interchangably).

# Schedule

The schedule this week is a webb of complexity because of Election
Day, Tuesday 3 November, but we hope everyone will abide by these
carefully devised changes. We will not hold any official course
activities (assessed cohort meetings or scheduled office hours) on
Election Day.

**Please vote** (and if you can, volunteer to be a poll worker)!
(Note: if you are voting in Virginia, early voting is a great option,
but ends on October 31.)

The schedule changes impact the "Tuesday" cohorts. Until now, the
Tuesday cohorts have been the first to meet for a given week. This
week, they will not meet on November 3, but will instead move to be
the _last_ cohorts to meet in Week 10 (and subsequent weeks) on
November 10. The schedule lists Tuesday cohorts on "Break" from
Wednesday 28 Oct through Wednesday 4 November (without the normal
preparation Cohort Meeting that would be on 31 Oct/1 Nov). You can
decide to meet if you would like then, of course, and use the
opportunity to review past weeks or get an early start on Week 10, but
that's up to you.  (If any other cohorts are thinking it is unfair
that the Tuesday cohorts get this week break, recall that they had
their first assessed cohort meetings on 1 September, only four days
after the cohorts were arranged. We are, unfortunately, not able to
provide a break week for the other cohorts since the semester ends on
Tuesday, 24 November.)

For Thursday cohorts who have preparation meetings on Tuesdays, we
hope you will arrange within your cohort a schedule that works for
everyone. It is fine to move the preparation meeting to Monday or
Wednesday if you can find a time that works for everyone, or to meet
as normal on Tuesday if everyone has been able to vote early and does
not have other election day commitments. If you aren't able to find a
solution that works for your cohort, please let us know.

<table class="schedule">
  <thead>
    <tr>
      <th text-align="center">Day</th>
      <th align="center">"Tuesday" Cohort</th>
      <th align="center">"Wednesday" Cohort</th>
      <th align="center">"Thursday" Cohort</th>
      <th align="center">"Friday" Cohort</th>
      <th align="center">"Sunday" Cohort</th>
      <th align="center">"Monday" Cohort</th>
    </tr>
  </thead> 
  <tbody>
     <tr><td><b>Wed</b> 28&nbsp;Oct</td>        <td>Break</td>	          <td bgcolor="lightyellow">(Week 9)</td> <td bgcolor="lightyellow">(Week 9)</td> <td bgcolor="lightyellow">(Week 9)</td>	 <td bgcolor="lightyellow">(Week 9)</td>	 <td bgcolor="lightyellow">(Week 9)</td>			 
</tr><tr><td><b>Thu</b> 29&nbsp;Oct</td>        <td>Break</td>           <td>Preparation</td> <td bgcolor="lightyellow">(Week 9)</td> <td bgcolor="lightyellow">(Week 9)</td>	 <td bgcolor="lightyellow">(Week 9)</td>	<td bgcolor="lightyellow">(Week 9)</td>		
</tr>
<tr><td><b>Fri</b> 30&nbsp;Oct</td>   <td>Break</td>           <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 9)</td>	<td bgcolor="lightyellow">(Week 9)</td>	<td bgcolor="lightyellow">(Week 9)</td>	  
</tr><tr><td><b>Sat/Sun</b> 31&nbsp;Oct/1&nbsp;Nov</td> <td>Break</td> <td>Preparation</td>      <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 9)</td>  <td bgcolor="lightyellow">(Week 9)</td>		 
</tr><tr><td><b>Mon</b> 2&nbsp;Nov</td>        <td>Break</td>		  <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td>     <td>Preparation</td> <td bgcolor="lightyellow">(Week 9)</td>		
</tr><tr><td><b>Tue</b>3&nbsp;Nov</td>        <td colspan="6" style="text-align:center;" bgcolor="#11A" color="lightgrey"><font color="#CCC"><b>Election Day</b> (no assessed cohort meetings or deadlines)</font></font></font></td></tr>
</tr><tr><td><b>Wed</b> 4&nbsp;Nov</td>         <td>Preparation</td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>        <td><b>Cohort Meeting</b></td> <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Thu</b> 5&nbsp;Nov</td>         <td>Preparation</td> <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr>
<td><b>Fri</b> 6&nbsp;Nov</td>
<td>Preparation</td> <td>Preparation</td> <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td>
</tr><tr><td><b>Sat/Sun</b> 7/8 Nov</td> <td><b>Cohort Meeting</b></td> <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td>  <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr><td><b>Mon</b> 9&nbsp;Nov</td>         <td>Preparation</td> <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td> <td> <font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td>
</tr>
<tr><td><b>Tue</b> 10&nbsp;Nov</td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td>
<td> <font color="blue"><b>Write-up Due</b></font></td>
</tr>

<tr><td><b>Wed</b> 11&nbsp;Nov</td> <td> <font color="blue"><b>Write-up Due</b></font></td>  <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td> <td bgcolor="lightblue">Week 11</td> <td>
</tr>

</tbody>
</table>

<a name="problems"></a>
# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

[Cohort Problems for Week 10 [PDF]](/ps/ps10.pdf)<br>


The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

After the Assessed Cohort Meeting, your Cohort Leader will select one
problem that your cohort needs to write-up and submit.  The write-up
is due by **11:59pm** on the day after your assessed cohort meeting
(see the schedule above).

[Problem Set 10 Template [zip]](https://uvatoc.github.io/ps/ps10template.zip).

# Reading

[Chapter 9: _Universality and uncomputability_](https://introtcs.org/public/lec_08_uncomputability.html) [[PDF](https://files.boazbarak.org/introtcs/lec_08_uncomputability.pdf)]

You should have already read through the Section 9.3 (but reread any parts you are confused on), and read the new Sections 9.4 and 9.5 for this week.

# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 10 Playlist](https://www.youtube.com/playlist?list=PLvpsxlEF9cP297KiQFFrkg2YZ3XWWcztO)
<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Fall 2019) [Class 16: Reductions](https://uvatoc.github.io/f19/class16/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d36c3729-5dbc-43e9-aebd-aaf40141ae83), [Slides](https://www.dropbox.com/s/ww3pqjm7v6nc8uq/class16_written.pptx?dl=0)

- (Fall 2019) [Class 17: Rice's Theorem](https://uvatoc.github.io/f19/class17/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3c2428a4-02a2-499e-af00-aaf601419207), [Slides](https://www.dropbox.com/s/pml6l1teoxa7y5s/class17_inked.pptx?dl=0). (Note that we do not include the first half or so of this class in the edited videos, which presents two more examples of uncomputability proofs by reduction. If you'd like to see more examples of these kinds of problems, please watch the full video for this class.)

- (Fall 2019) [Class 18: Review for Exam 2](https://uvatoc.github.io/f19/class18/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7ce45bc2-ca94-402e-84ac-aafb01519dbc), [Slides](https://www.dropbox.com/s/c2ciuclc2zjgqtk/class18-post.pdf?dl=0). We include a few example problems from this exam review lecture, that we think will be helpful to you for the cohort problems this week.

</p>


<p>Decidable, Recognizable, Computable (7:18) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/ZjQHbxCExsg' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>An Undecidable Problem (8:10) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Bit7FvUzcMU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Proof by Reduction (17:54) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/tEp6j_owBSs' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>HALTS is Undecidable (7:19) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/UObqrnIHHbI' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Finite is Undecidable (11:38) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/C4CZoVxJT9o' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Prints3 and IsMalware Are Undecidable (5:15) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/5VKf11so0XE' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Rice's Theorem (15:28) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/U1aEDWBNQ3A' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>

The following three videos are problems from the exam review, so do
not introduct new material, but provide more examples of how to prove
functions are computable or uncomputable. You can find the problems they cover here: [Fall 2019 Exam 2 Practice Problems](https://uvatoc.github.io/docs/exam2practice.pdf), and are encouraged to try to solve them yourself before watching the videos. The _Natural Numbers are Computable_ video is about Problem 9, and the _Proving Uncomputability_ video is about Problem 14.

</p>

<p>Proving Computability and Noncomputability (7:57) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/3cSkH-kDlxg' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>The Natural Numbers are Computable (2:43) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/KPamvxCaepU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Proving Uncomputability (Busy Boas and Busier Beavers) (8:55) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/cue964eNyqA' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>


