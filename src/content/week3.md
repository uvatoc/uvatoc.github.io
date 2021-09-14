+++
draft = false
title = "Week 3"
slug= "week3"
+++

# Week 3: Circuits and Sugar


The main goals for Week 3 are to:

- Show how simple models of computing can result in complex behavior.
- Begin building a bridge from theoretical models of computing (like straightline programs and boolean circuits) to practical implementations of computing (like Python and integrated circuits).
- Explore the powers and limitations of a model of computing, including being able to understand the details of how to use that model, and why it is defined in the way chosen.


# Schedule


|       Day       | "Monday" Cohort | "Tuesday" Cohort | "Wednesday" Cohort | "Thursday" Cohort  |  "Friday" Cohort   |
| :-------------: | :-------------: | :--------------: | :----------------: | :----------------: | :----------------: |
|**Wed** 8 Sept|Preparation|<font color="lightgray">(Week 2)</font>|<font color="lightgray">(Week 2)</font>|<font color="lightgray">(Week 2)</font>|<font color="lightgray">(Week 2)</font>|
|**Thurs** 9 Sept|Preparation|Preparation|<font color="lightgray">(Week 2)</font>|<font color="lightgray">(Week 2)</font>|<font color="lightgray">(Week 2)</font>|
|**Fri** 10 Sept|Preparation|Preparation|Preparation|<font color="lightgray">(Week 2)</font>|<font color="lightgray">(Week 2)</font>|
|**Sat** 11 Sept|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|<font color="lightgray">(Week 2)</font>|
|**Sun** 12 Sept|Revision|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|
|**Mon** 13 Sept|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|Preparation|
|**Tues** 14 Sept|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|
|**Wed** 15 Sept|<font color="lightgray">(Week 4)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|
|**Thurs** 16 Sept|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|
|**Fri** 17 Sept|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|
|**Sat** 18 Sept|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 3)</font>|**Writeup Due**|

# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

- [Cohort Problems for Week 3 [PDF]](/ps/week3_blank.pdf)
- [LaTeX Template for Week 3 [ZIP]](/ps/week3.zip)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

The above problems include completing the function implementations in
this python file (the comments in the file itself will guide you,
please read everything linearly): [adders.py](/ps/adders.py).

If you already have python3 on your machine, you should be good to go
for the programming problems. If you don't, please [follow these directions to setup Python](/python). 

# Monday Class
In class on Monday September 13 we discussed motivations for syntactic sugar and together worked on a problem similar to lookup (from the videos) and Add (from the problem set). You can find the slides [here](/docs/sept13_21.pdf) and you can find a recording of the lecture on collab.


# Write-up Problem

After the Assessed Cohort Meeting, your Cohort Leader will select one
problem that your cohort needs to write-up and submit.  The write-up
is due by **11:59pm** on the day after your assessed cohort
meeting (see the schedule above).


Download the [Problem Set 3 Template [zip]](/ps/week3.zip) and upload to overleaf. From there, add your solution to the appropriate .tex file for the problem assigned. Modify week3.tex to comment out `\usepackage{toc}` and instead be `\usepackage[response#]{toc}` where `#` refers to the number of the problem assigned.

# Reading

Material in this week's lectures parallels with:
 
- [Ch. 3, Defining Computation](https://introtcs.org/public/lec_03_computation.html) of the TOC textbook. We discussed this last week as well, we're looking at this chapter in more detail this week
- [Ch. 4, Syntactic sugar and computing every function](https://introtcs.org/public/lec_03a_computing_every_function.html) from the TOC textbook. In particular, we cover sections 4.1 through 4.3.

# Videos

You can play all the videos using this playlist, but don't forget to take breaks:[Week 3 Playlist](https://www.youtube.com/playlist?list=PLZ9Gk_8DtbmF_fm_DYIxcGxYGtyBX61C5)

<p>
The Story So Far (02:54)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/LA-CooHwl4w" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>


**This video introduces graphs, including their definition, notation, and vocabulary. If you feel comfortable with graphs already, I encourage you to skip this video.**
<p>
Introduction to Graphs (15:43)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/bUyWLT5MKEw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>


<p>
Components of a Computing Model (1:58)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/EmcUU6jJ6sA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Representing Circuits (14:42)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/JxkfGPglKnk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Circuit Execution (12:41)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/9BoHFu6STIE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Syntactic Sugar (9:13)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/kvEb068OvCw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
De-Sugaring (11:40)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/1cTaMbAA8aU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Constructing Conditionals (10:37)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/DYeaX2lmNPI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Lengthening Lookup (12:14)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/d2U25VuOqkw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Cost of LOOKUP (3:33)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/ZRFK2_Ll9b0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>
