+++
date = "07 Aug 2020"
draft = false
title = "Week 5"
slug="week5"
+++

# Goals

The main goals for Week 5 are to:

- Understand what a complexity class is and how to provide properties about circuit-size complexity classes.
- Learn the asymptotic operators (Big-<em>O</em>, &Omega;, and &Theta;) and how to use them correctly.
- Be able to both intuitively understand what functions are in <em>O</em>(<em>f(</em>), and to prove membership or non-membership.
- Be able to connect the formal definitions of computing costs to practical questions about the cost of computing.

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
     <tr><td><b>Wed</b> 23&nbsp;Sep</td>        <td>Preparation</td>	          <td bgcolor="lightyellow">(Week 4)</td> <td bgcolor="lightyellow">(Week 4)</td> <td bgcolor="lightyellow">(Week 4)</td>	 <td bgcolor="lightyellow">(Week 4)</td>	 <td bgcolor="lightyellow">(Week 4)</td>			 
</tr><tr><td><b>Thu</b> 24&nbsp;Sep</td>        <td>Preparation</td>           <td>Preparation</td> <td bgcolor="lightyellow">(Week 4)</td> <td bgcolor="lightyellow">(Week 4)</td>	 <td bgcolor="lightyellow">(Week 4)</td>	<td bgcolor="lightyellow">(Week 4)</td>		
</tr>
<tr><td><b>Fri</b> 25&nbsp;Sep</td>   <td>Preparation</td>           <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 4)</td>	<td bgcolor="lightyellow">(Week 4)</td>	<td bgcolor="lightyellow">(Week 4)</td>	  
</tr><tr><td><b>Sat/Sun</b> 26/27&nbsp;Sep</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>      <td>Preparation</td>      <td>Preparation</td>   <td bgcolor="lightyellow">(Week 4)</td>  <td bgcolor="lightyellow">(Week 4)</td>		 
</tr><tr><td><b>Mon</b> 28&nbsp;Sep</td>        <td>Preparation</td>		  <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td>     <td>Preparation</td> <td bgcolor="lightyellow">(Week 4)</td>		
</tr><tr><td><b>Tue</b> 29&nbsp;Sep</td>         <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td> <td>Preparation</td>       <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Wed</b> 30&nbsp;Sep</td>         <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>        <td><b>Cohort Meeting</b></td> <td>Preparation</td> <td>Preparation</td>
</tr><tr><td><b>Thu</b> 1&nbsp;Oct</td>         <td bgcolor="lightblue">Week 6</td> <td><font color="blue"><b>Write-up Due</b></font></td>  <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td> <td><b>Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr>
<td><b>Fri</b> 2&nbsp;Oct</td>
<td bgcolor="lightblue">Week 6</td> <td bgcolor="lightblue">Week 6</td> <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td> <td>Preparation</td>   <td><b>Cohort Meeting</b></td>
</tr><tr><td><b>Sat/Sun</b> 3/4&nbsp;Oct</td>     <td bgcolor="lightblue">Week 6</td> <td bgcolor="lightblue">Week 6</td> <td bgcolor="lightblue">Week 6</td>  <td><font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></td> <td>Preparation</td>
</tr><tr><td><b>Mon</b> 5&nbsp;Oct</td>         <td bgcolor="lightblue">Week 6</td> <td bgcolor="lightblue">Week 6</td> <td bgcolor="lightblue">Week 6</td> <td bgcolor="lightblue">Week 6</td> <td> <font color="blue"><b>Write-up Due</b></font></td> <td><font color="red"><b>Assessed Cohort Meeting</b></font></td>
</tr>

</tr><tr><td><b>Tue</b> 6&nbsp;Oct</td>         <td bgcolor="lightblue">Week 6</td> <td bgcolor="lightblue">Week 6</td> <td bgcolor="lightblue">Week 6</td> <td bgcolor="lightblue">Week 6</td>  <td bgcolor="lightblue">Week 6</td> <td><font color="blue"><b>Write-up Due</b></font></td>
</tr>

</tbody>
</table>

<a name="problems"></a>
# Cohort Problems

TODO 

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

[Cohort Problems for Week 5 [PDF]](/ps/ps5.pdf)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

After the Assessed Cohort Meeting, your Cohort Leader will select one
problem that your cohort needs to write-up and submit.  The write-up
is due by **11:59pm** on the day after your assessed cohort meeting
(see the schedule above).

[Problem Set 5 Template [zip]](https://uvatoc.github.io/ps/ps5template.zip).


# Reading

This week focuses on material in [Ch. 5, Code as data, data as
code](/docs/tcs-chapter5.pdf) from the TOC textbook (which you already
read last week, but we go into more depth on this week). The main theorems we focus on are in [Section 5.2](https://introtcs.org/public/lec_04_code_and_data.html#countingcircuitsec).

The TCS book does not provide a detailed presentation of the
asymptotic operators, but reviews them in [Section
1.4.8](https://introtcs.org/public/lec_00_1_math_background.html#secbigohnotation). Many
books provide more detailed presentations of these concepts, and lots
of examples. If you would like a more complex textbook explanation,
the course instructors (at least one of them!) recommends this
chapter: [Chapter 7: Cost](https://computingbook.org/Cost.pdf) (from [_Introduction to Computing
Explorations in Language, Logic, and Machines_](https://computingbook.org/).

# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 5 Playlist](https://www.youtube.com/playlist?list=PLvpsxlEF9cP08xzWYNiwLVC5E92ok5nAB)
<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Spring 2020) Feb 13: Complexity - [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=bac56a89-3c1e-42f8-ac16-ab600151fdf6) [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/big-oh_written.pdf)
- (Fall 2019) [Class 11: Cost and Counting](https://uvatoc.github.io/f19/class11/) - [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a2349417-446c-46a8-b5ec-aae10141417e) [Slides](https://www.dropbox.com/s/tbsytzp9n6fnyvg/class11-post.pdf?dl=0)

We don't have exams this semester, but adventurous students may find
the [exam review from Fall
2019](https://uvatoc.github.io/f19/class10/) useful (we may include
some clips from this in a future class).

</p>

<p>Introducing Complexity (8:02) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/xR0EWMVw-Kk' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Complexity Classes: SIZE (6:19) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/es1QLNCa4FY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>First Complexity Proof (4:39) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/8hyf4s_tdM0' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Asympototic Operators (7:05) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/96XtkxDNDCs' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Using Big-O (Theorem 5.2) (4:51) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/ZPVsL3mCxkg' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Understanding 𝑂, Ω, and Θ (7:20) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/0O-rGXVp5yU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Big-O Examples (5:35) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/NUUnux_BFSA' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Common Misuses of Asymptotic Notation (5:52) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/WLV99-6ep2c' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<div class="break">
<div class="takeabreak">
<b>Breaktime</b>
</div>
</div>

<p>Some Functions are Expensive (7:35) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/BavLtSyKlFg' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Cost of Computing (5:02) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/5H6DvmEzwDY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

