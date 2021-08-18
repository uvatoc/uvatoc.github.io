+++
date = "05 Oct 2020"
draft = false
title = "Week 7"
slug="week7"
+++

# Goals

The main goals for Week 7 are to:

- Understand the proof that Regular Expressions are equivalent in power to Deterministic Finite Automata. This is a long proof, split over 4 videos, but is something we hope everyone understands in detail. The methods used in the proof are similar to ones we have seen before in showing equivalence of NAND-Circ and Boolean circuits, but is a fair bit more complex. This general method of showing equivalence is something we will see again in this class, and you will encounter many more times in other classes and work that you will do.

- Become familiar with the power and strangeness of nondeterminism. For finite automata, we prove this week that despite is seeming super-power, nondeterministic finite automata cannot compute any functions (or recognize any languages) that cannot be computed by deterministic finite automata. The main topic for Weeks 8-11 will be considering this question for more powerul computing models (which is the most famous open problem in computer science).


# Schedule

The schedule is identical to previous weeks, and repeated here (with updated dates).

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
     <tr><td><b>Wed</b> 7&nbsp;Oct</td>        <td>Preparation</td>	          <td bgcolor="lightyellow">(Week 6)</td> <td bgcolor="lightyellow">(Week 6)</td> <td bgcolor="lightyellow">(Week 6)</td>	 <td bgcolor="lightyellow">(Week 6)</td>	 <td bgcolor="lightyellow">(Week 6)</td>			 
</tr><tr><td><b>Thu</b> 8&nbsp;Oct</td>        <td>Preparation</td>           <td>Preparation</td> <td bgcolor="lightyellow">(Week 6)</td> <td bgcolor="lightyellow">(Week 6)</td>	 <td bgcolor="lightyellow">(Week 6)</td>	<td bgcolor="lightyellow">(Week 6)</td>		
</tr>
<tr><td><b>Fri</b> 9&nbsp;Oct</td>   <td>Preparation</td>           <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 6)</td>	<td bgcolor="lightyellow">(Week 6)</td>	<td bgcolor="lightyellow">(Week 6)</td>	  
</tr><tr><td><b>Sat/Sun</b> 10/11&nbsp;Oct</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>      <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 6)</td>  <td bgcolor="lightyellow">(Week 6)</td>		 
</tr><tr><td><b>Mon</b> 12&nbsp;Oct</td>        <td>Preparation</td>		  <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td>     <td>Preparation</td> <td bgcolor="lightyellow">(Week 6)</td>		
</tr><tr><td><b>Tue</b> 13&nbsp;Oct</td>         <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Wed</b> 14&nbsp;Oct</td>         <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>        <td><b>Cohort Meeting</b></td> <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Thu</b> 15&nbsp;Oct</td>         <td bgcolor="lightblue">Week 8</td> <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr>
<td><b>Fri</b> 16&nbsp;Oct</td>
<td bgcolor="lightblue">Week 8</td> <td bgcolor="lightblue">Week 8</td> <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td>
</tr><tr><td><b>Sat/Sun</b> 17/18&nbsp;Oct</td>     <td bgcolor="lightblue">Week 8</td> <td bgcolor="lightblue">Week 8</td> <td bgcolor="lightblue">Week 8</td>  <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr><td><b>Mon</b> 19&nbsp;Oct</td>         <td bgcolor="lightblue">Week 8</td> <td bgcolor="lightblue">Week 8</td> <td bgcolor="lightblue">Week 8</td> <td bgcolor="lightblue">Week 8</td> <td> <font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td>
</tr>
</tr><tr><td><b>Tue</b> 20&nbsp;Oct</td>         <td bgcolor="lightblue">Week 8</td> <td bgcolor="lightblue">Week 8</td> <td bgcolor="lightblue">Week 8</td> <td bgcolor="lightblue">Week 8</td>  <td bgcolor="lightblue">Week 8</td> <td><font color="blue"><b>Write-up Due</b></font></td>
</tr>

</tbody>
</table>

<a name="problems"></a>
# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

[Cohort Problems for Week 7 [PDF]](/ps/ps7.pdf)<br>


The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

After the Assessed Cohort Meeting, your Cohort Leader will select one
problem that your cohort needs to write-up and submit.  The write-up
is due by **11:59pm** on the day after your assessed cohort meeting
(see the schedule above).

[Problem Set 7 Template [zip]](https://uvatoc.github.io/ps/ps7template.zip).

# Reading

This week continues with the material in [Chapter 6: Functions with
Infinite domains, Automata, and Regular
expressions](https://introtcs.org/public/lec_05_infinite.html) that we
started on last week.

[Section 6.4.2](https://introtcs.org/public/lec_05_infinite.html#regdfaequivsec)
of the book includes a proof that regular expressions are equivalent
in power to deterministic finite automata, but it is quite different
from the proof we do in the videos. Ambitious students are encouraged
to understand both proofs, and to consider the advantages and
disadvantages of the approach taken in the book compared to our
approach (which is the one done more traditionally in theory of
computation courses, at least going back to Mike Sipser's courses in
the 1980s).

There are many books (and other videos) that do present material
similar to what is in the videos this week, but we are not assigning
any additional readings.


# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 7 Playlist](https://www.youtube.com/playlist?list=PLvpsxlEF9cP1dsq5Hb0PSI1dyG6cvFC1_)
<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Spring 2020) Nondeterminism: [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0f798579-372f-45ca-bef6-ab730151cf45), [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/non-determinism_written.pdf)
- (Spring 2020) FSA Equivalent to Regular Expressions: [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=65c2b08e-1ce7-4e25-a257-ab75015297b1), [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/fsa_equals_regex.pdf)

</p>

<p>Warm-Up: Complementing the XOR Language (5:54) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Se4LhD_NTk8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Equivalence of Regular Expressions and FSAs (6:12) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Vcv6dR3__g8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Proving FSAs are as Powerful as Regular Expressions (Part 1: Proof Strategy) (4:35) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/IGPKOmACoes' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Proving FSAs are as Powerful as Regular Expressions (Part 2: Bases, Union) (22:55) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/aA47ceLSuoc' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Nondeterminism (11:14) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Qu8NsFh2Ss4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Nondeterministic Finite Automata (NFAs) (13:48) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/5fk2ej5jU8c' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Equivalence of NFAs and DFAs (10:01) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/iO-0KWSJs3A' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Proving FSAs are as Powerful as Regular Expressions (Part 3: Concatenation) (14:58) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/84tXODX8RGo' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Proving FSAs are as Powerful as Regular Expressions (Part 4: Kleene Star) (8:21) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/xV7nnli95tw' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>



