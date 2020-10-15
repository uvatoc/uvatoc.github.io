+++
date = "07 Aug 2020"
draft = false
title = "Week 8"
slug="week8"
+++

# Goals

This week, we introduce the most important and widely used model of
computation, the Turing machine, and start to address the big question
of what can and cannot be computed by any machine with a finite
description.

The main goals for Week 8 are to:

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
     <tr><td><b>Wed</b> 14&nbsp;Oct</td>        <td>Preparation</td>	          <td bgcolor="lightyellow">(Week 7)</td> <td bgcolor="lightyellow">(Week 7)</td> <td bgcolor="lightyellow">(Week 7)</td>	 <td bgcolor="lightyellow">(Week 7)</td>	 <td bgcolor="lightyellow">(Week 7)</td>			 
</tr><tr><td><b>Thu</b> 15&nbsp;Oct</td>        <td>Preparation</td>           <td>Preparation</td> <td bgcolor="lightyellow">(Week 7)</td> <td bgcolor="lightyellow">(Week 7)</td>	 <td bgcolor="lightyellow">(Week 7)</td>	<td bgcolor="lightyellow">(Week 7)</td>		
</tr>
<tr><td><b>Fri</b> 16&nbsp;Oct</td>   <td>Preparation</td>           <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 7)</td>	<td bgcolor="lightyellow">(Week 7)</td>	<td bgcolor="lightyellow">(Week 7)</td>	  
</tr><tr><td><b>Sat/Sun</b> 17/18&nbsp;Oct</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>      <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 7)</td>  <td bgcolor="lightyellow">(Week 7)</td>		 
</tr><tr><td><b>Mon</b> 19&nbsp;Oct</td>        <td>Preparation</td>		  <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td>     <td>Preparation</td> <td bgcolor="lightyellow">(Week 7)</td>		
</tr><tr><td><b>Tue</b> 20&nbsp;Oct</td>         <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Wed</b> 21&nbsp;Oct</td>         <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>        <td><b>Cohort Meeting</b></td> <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Thu</b> 22&nbsp;Oct</td>         <td bgcolor="lightblue">Week 9</td> <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr>
<td><b>Fri</b> 23&nbsp;Oct</td>
<td bgcolor="lightblue">Week 9</td> <td bgcolor="lightblue">Week 9</td> <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td>
</tr><tr><td><b>Sat/Sun</b> 24/25&nbsp;Oct</td>     <td bgcolor="lightblue">Week 9</td> <td bgcolor="lightblue">Week 9</td> <td bgcolor="lightblue">Week 9</td>  <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr><td><b>Mon</b> 26&nbsp;Oct</td>         <td bgcolor="lightblue">Week 9</td> <td bgcolor="lightblue">Week 9</td> <td bgcolor="lightblue">Week 9</td> <td bgcolor="lightblue">Week 9</td> <td> <font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td>
</tr>
</tr><tr><td><b>Tue</b> 27&nbsp;Oct</td>         <td bgcolor="lightblue">Week 9</td> <td bgcolor="lightblue">Week 9</td> <td bgcolor="lightblue">Week 9</td> <td bgcolor="lightblue">Week 9</td>  <td bgcolor="lightblue">Week 9</td> <td><font color="blue"><b>Write-up Due</b></font></td>
</tr>

</tbody>
</table>

<a name="problems"></a>
# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

[Cohort Problems for Week 8 [PDF]](/ps/ps8.pdf)<br>


The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

After the Assessed Cohort Meeting, your Cohort Leader will select one
problem that your cohort needs to write-up and submit.  The write-up
is due by **11:59pm** on the day after your assessed cohort meeting
(see the schedule above).

[Problem Set 8 Template [zip]](https://uvatoc.github.io/ps/ps8template.zip).

# Reading

This week we discuss the material contained in [Chapter 7: Loops and Infinity](https://introtcs.org/public/lec_06_loops.html).

Turing Machines and other similar models of computing are taught in
many different ways in many different places. In addition to the
course materials, you'll find plenty of other presentations of this
material available on youtube, other textbooks, lecture slides from
other universities, blog posts, etc. Please be advised that there are
many subtly different presentations of Turing machines, and so what
you see elsewhere may differ from what we covered, but the key ideas
are universal and should be the same in any good
presentation. Typically minor changes are made to the model either for
convenience of the context, or so real-world running times are more
similar to the running time of the model (more on this in future
weeks).

# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 8 Playlist](https://www.youtube.com/playlist?list=PLvpsxlEF9cP2P-g1r9U8ZSVxeAWcQJ0sF)
<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Fall 2019) [Class 13: Machines](https://uvatoc.github.io/f19/class13/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=89195d73-1989-4b2f-8b70-aae8014178c4), [Slides](https://www.dropbox.com/s/36tv9no453ffmkn/class13_written.pptx?dl=0)

- (Fall 2019) [Class 14: Computability](https://uvatoc.github.io/f19/class14/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e086e67f-71aa-45e1-a59d-aaed01412ded), [Slides](https://www.dropbox.com/s/nw9zh8a0vahvaqy/class14-inked.pdf?dl=0)

</p>

<p>Warm-Up: Life on Mars (2:16) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/zpKVDZB7JiE' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Limitations of Finite Automata (6:40) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/KmAJEKRZaGY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Turing Machines (5:37) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Xx_GeourSOQ' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Turing Machine Examples (11:40) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/wN5DPmz0hgg' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>What was Turing’s Model Modeling? (15:56) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/E-OK7hSyMNE' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Turing Machine Execution (9:13) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/fulQIGM0jUQ' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Turing Machine Variations (4:25) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/9zR6XoHadZc' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Busy Beavers (5:12) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/yJApEB69gXo' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>On Uncomputable Numbers (8:13) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Cuf4zkYwGlQ' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

Alan M. Turing, [_On Computable Numbers, with an Application to the
Entscheidungsproblem_](/docs/computablenumbers.pdf). 1936. ([bug fix](/docs/bugfix.pdf))
