+++
date = "07 Aug 2020"
draft = false
title = "Week 6"
slug="week6"
+++

# Goals

The main goals for Week 6 are to:

- Synthesize what we have learned about finite computation in the first 5 weeks, and start exploring unbounded computation.

- Appreciate the connection between functions and languages, and the different ways of talking about computation.

- Understand and be able to formally define a Finite State Automaton, and to reason about the language accepted (or function computed) by a Deterministic Finite Automaton.

- Be able to reason about the power of a DFA and understand deeply the proof that DFAs are strictly more powerful than Boolean circuits.

- Understand how to interpret Regular Expressions, define them formally, and reason about their capabilities.

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
     <tr><td><b>Wed</b> 30&nbsp;Sep</td>        <td>Preparation</td>	          <td bgcolor="lightyellow">(Week 5)</td> <td bgcolor="lightyellow">(Week 5)</td> <td bgcolor="lightyellow">(Week 5)</td>	 <td bgcolor="lightyellow">(Week 5)</td>	 <td bgcolor="lightyellow">(Week 5)</td>			 
</tr><tr><td><b>Thu</b> 1&nbsp;Oct</td>        <td>Preparation</td>           <td>Preparation</td> <td bgcolor="lightyellow">(Week 5)</td> <td bgcolor="lightyellow">(Week 5)</td>	 <td bgcolor="lightyellow">(Week 5)</td>	<td bgcolor="lightyellow">(Week 5)</td>		
</tr>
<tr><td><b>Fri</b> 2&nbsp;Oct</td>   <td>Preparation</td>           <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 5)</td>	<td bgcolor="lightyellow">(Week 5)</td>	<td bgcolor="lightyellow">(Week 5)</td>	  
</tr><tr><td><b>Sat/Sun</b> 3/4&nbsp;Oct</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>      <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 5)</td>  <td bgcolor="lightyellow">(Week 5)</td>		 
</tr><tr><td><b>Mon</b> 5&nbsp;Oct</td>        <td>Preparation</td>		  <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td>     <td>Preparation</td> <td bgcolor="lightyellow">(Week 5)</td>		
</tr><tr><td><b>Tue</b> 6&nbsp;Oct</td>         <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Wed</b> 7&nbsp;Oct</td>         <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>        <td><b>Cohort Meeting</b></td> <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Thu</b> 8&nbsp;Oct</td>         <td bgcolor="lightblue">Week 7</td> <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr>
<td><b>Fri</b> 9&nbsp;Oct</td>
<td bgcolor="lightblue">Week 7</td> <td bgcolor="lightblue">Week 7</td> <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td>
</tr><tr><td><b>Sat/Sun</b> 10/11&nbsp;Oct</td>     <td bgcolor="lightblue">Week 7</td> <td bgcolor="lightblue">Week 7</td> <td bgcolor="lightblue">Week 7</td>  <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr><td><b>Mon</b> 12&nbsp;Oct</td>         <td bgcolor="lightblue">Week 7</td> <td bgcolor="lightblue">Week 7</td> <td bgcolor="lightblue">Week 7</td> <td bgcolor="lightblue">Week 7</td> <td> <font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td>
</tr>
</tr><tr><td><b>Tue</b> 13&nbsp;Oct</td>         <td bgcolor="lightblue">Week 7</td> <td bgcolor="lightblue">Week 7</td> <td bgcolor="lightblue">Week 7</td> <td bgcolor="lightblue">Week 7</td>  <td bgcolor="lightblue">Week 7</td> <td><font color="blue"><b>Write-up Due</b></font></td>
</tr>

</tbody>
</table>

<a name="problems"></a>
# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

TODO: [Cohort Problems for Week 6 [PDF]](/ps/ps6.pdf)
TODO: Programming problems?

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

After the Assessed Cohort Meeting, your Cohort Leader will select one
problem that your cohort needs to write-up and submit.  The write-up
is due by **11:59pm** on the day after your assessed cohort meeting
(see the schedule above).

TODO: [Problem Set 6 Template [zip]](https://uvatoc.github.io/ps/ps6template.zip).

# Reading

This week focuses on material in [Chapter 6: Functions with Infinite
domains, Automata, and Regular
expressions](https://introtcs.org/public/lec_05_infinite.html). Our
presentation in the videos differs from how things are presented in
the textbook (our way of defining a DFA is closer to the Alternate
Definition mentioned in Remark 6.3 than the way Definition 6.2 defines
a DFA; the book's presentation on regular expressions is similar to
ours, but not identical). Astute readers and viewers are encouraged to
look for places where the differences matter, or if they are only
cosmetic.

# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 6 Playlist](https://www.youtube.com/playlist?list=PLvpsxlEF9cP1mu9Kmcy6jbsE4TpwLhSc0)
<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Spring 2020) Automata - [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=432abfa8-cdd8-4587-b2b7-ab6c0151eeb2), [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/automata_written.pdf)
- (Spring 2020) Regular Expressions and Closure - [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=34e95fad-c0b8-4c9f-adcf-ab6e0151e00c), [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/regex_written.pdf)

</p>

<p>Warm-up: Questions about Strings (4:01) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/O5aonOdyxec' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Functions and Languages (11:16) <br>' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Beyond Finite Functions (8:23) <br>' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Finite Automaton for XOR (6:28) <br>' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Formalizing Finite State Automata (3:29) <br>' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Power of Deterministic Finite Automata (8:15) <br>' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Regular Expressions (17:27) <br>' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>