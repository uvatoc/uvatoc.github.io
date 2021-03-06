+++
date = "07 Aug 2020"
draft = false
title = "Week 9"
slug="week9"
+++

# Goals

Last week, we used a counting argument to show that there must be some
uncomputable functions ("some" here means infinitely many), but we
didin't find a specific uncomputable function. This week, we prove
that a particular function is uncomputable, and explore the
implications of finding an uncomputable function.

The main goals for Week 9 are to:

- Understand what cannot be computed by a finite automaton and why.
- Use and understand Turing Machines as a model of computing.
- Study a definition of computability.
- Explore the powers and limitations of Turing Machines.
- Understand why some numbers are _uncomputable_, and what this means.
- Learn different variations on Turing Machines and how they can be transformed.


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
     <tr><td><b>Wed</b> 21&nbsp;Oct</td>        <td>Preparation</td>	          <td bgcolor="lightyellow">(Week 8)</td> <td bgcolor="lightyellow">(Week 8)</td> <td bgcolor="lightyellow">(Week 8)</td>	 <td bgcolor="lightyellow">(Week 8)</td>	 <td bgcolor="lightyellow">(Week 8)</td>			 
</tr><tr><td><b>Thu</b> 22&nbsp;Oct</td>        <td>Preparation</td>           <td>Preparation</td> <td bgcolor="lightyellow">(Week 8)</td> <td bgcolor="lightyellow">(Week 8)</td>	 <td bgcolor="lightyellow">(Week 8)</td>	<td bgcolor="lightyellow">(Week 8)</td>		
</tr>
<tr><td><b>Fri</b> 23&nbsp;Oct</td>   <td>Preparation</td>           <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 8)</td>	<td bgcolor="lightyellow">(Week 8)</td>	<td bgcolor="lightyellow">(Week 8)</td>	  
</tr><tr><td><b>Sat/Sun</b> 24/25&nbsp;Oct</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>      <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 8)</td>  <td bgcolor="lightyellow">(Week 8)</td>		 
</tr><tr><td><b>Mon</b> 26&nbsp;Oct</td>        <td>Preparation</td>		  <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td>     <td>Preparation</td> <td bgcolor="lightyellow">(Week 8)</td>		
</tr><tr><td><b>Tue</b> 27&nbsp;Oct</td>         <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Wed</b> 28&nbsp;Oct</td>         <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>        <td><b>Cohort Meeting</b></td> <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Thu</b> 29&nbsp;Oct</td>         <td bgcolor="lightblue">Week 10</td> <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr>
<td><b>Fri</b> 30&nbsp;Oct</td>
<td bgcolor="lightblue">Week 10</td> <td bgcolor="lightblue">Week 10</td> <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td>
</tr><tr><td><b>Sat/Sun</b> 31 Oct/1 Nov</td>     <td bgcolor="lightblue">Week 10</td> <td bgcolor="lightblue">Week 10</td> <td bgcolor="lightblue">Week 10</td>  <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr><td><b>Mon</b> 2&nbsp;Nov</td>         <td bgcolor="lightblue">Week 10</td> <td bgcolor="lightblue">Week 10</td> <td bgcolor="lightblue">Week 10</td> <td bgcolor="lightblue">Week 10</td> <td> <font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td>
</tr>
</tr><tr><td><b>Tue</b> 3&nbsp;Nov</td>
<td colspan="6" style="text-align:center;" bgcolor="#11A" color="lightgrey"><font color="#CCC"><b>Election Day</b> (no assessed cohort meetings or deadlines)</font></font></font></td></tr>
</tr>

</tr><tr><td><b>Wed</b> 4&nbsp;Nov</td>         <td bgcolor="lightblue">Week 10</td> <td bgcolor="lightblue">Week 10</td> <td bgcolor="lightblue">Week 10</td> <td bgcolor="lightblue">Week 10</td><td bgcolor="lightblue">Week 10</td> <td> <font color="blue"><b>Write-up Due</b></font></td></td>

</tbody>
</table>

<a name="problems"></a>
# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

[Cohort Problems for Week 9 [PDF]](/ps/ps9.pdf)<br>


The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

After the Assessed Cohort Meeting, your Cohort Leader will select one
problem that your cohort needs to write-up and submit.  The write-up
is due by **11:59pm** on the day after your assessed cohort meeting
(see the schedule above).

[Problem Set 9 Template [zip]](https://uvatoc.github.io/ps/ps9template.zip).

# Reading

[Chapter 9: _Universality and uncomputability_](https://introtcs.org/public/lec_08_uncomputability.html) [[PDF](https://files.boazbarak.org/introtcs/lec_08_uncomputability.pdf)]

You should read through the end of Section 9.3 (including the "optional" section 9.3.2). (We will cover Section 9.4 and 9.5 next week.)

The material in Sections 9.1 &ndash; 9.3 covers the same concepts as
we do in the lectures, but in a somewhat different order and with a
focus on <em>HALT</em> rather than <em>ACCEPTS</em>. You should
consider how similar and different these two functions are, and
compare the proof that <em>ACCEPTS</em> is uncomputable from the
lectures to the one in the book that <em>HALT</em> is uncomputable.

# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 9 Playlist](https://www.youtube.com/playlist?list=PLvpsxlEF9cP3Z6lyvzjzpLq37puiIo1NZ)
<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Fall 2019) [Class 14: Computability](https://uvatoc.github.io/f19/class14/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e086e67f-71aa-45e1-a59d-aaed01412ded), [Slides](https://www.dropbox.com/s/nw9zh8a0vahvaqy/class14-inked.pdf?dl=0) (just part of the _Self-Rejection (An Uncomputable Function)_ video)

- (Fall 2019) [Class 15: Universality and Uncomputability](https://uvatoc.github.io/f19/class15/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=c8ce23af-8a26-44b4-9678-aaef01410d8e), [Slides](https://www.dropbox.com/s/iibngc72d0snb0f/class15-inked.pdf?dl=0)

</p>


<p>Church-Turing Thesis (8:39) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/GTPwGBIoASM' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Self-Rejection (An Uncomputable Function) (16:30) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/op62asZexg8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Universal Machines (8:54) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Ij01xiZDN8k' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>ACCEPTS is Uncomputable (Part 1) (6:12) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/jzRL3XAN_-U' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>ACCEPTS is Uncomputable (Part 2) (6:23) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/PlJr8hO1pdg' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Computability in Theory and Practice (8:50) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/YbrFeIC3jXo' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>
<p>
This video was originally planned for Week 10 and is a recap of the
proof that acceptance is uncomputable. But, since it will be helpful
for one of the cohort problems this week, we are providing it here.
</p>

<p>An Undecidable Problem (8:10) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Bit7FvUzcMU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>

Alan M. Turing, [_On Computable Numbers, with an Application to the
Entscheidungsproblem_](/docs/computablenumbers.pdf). 1936. ([bug
fix](/docs/bugfix.pdf)) (You missed your chance to by an [original
printing for GBP 30,000](http://www.sothebys.com/en/auctions/ecatalogue/lot.929.html/2018/the-library-of-erwin-tomash-l18409).)

According to [Scott Aaronson](http://www.scottaaronson.com/),
[_Dori-Mic and the Universal Machine! A Tragicomic Tale of
Combinatorics and Computability for Curious Children of All
Ages_](https://dori-mic.org) is ["The BEST babies' book about
computational universality I've
read."](https://www.amazon.com/review/R1TSEFIBYW9Y6I/ref=cm_cr_dp_title?ie=UTF8&ASIN=1495944980&channel=detail-glance&nodeID=283155&store=books). I
have free copies to send to anyone who needs a holiday present for
a young sibling/cousin/nibling/other person who is behind in her
theoretical computer science education and needs a holiday present for
any cs3102 students who ask (this offer doesn't expire).
