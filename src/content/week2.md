+++
draft = false
title = "Week 2"
slug= "week2"
+++

# Week 2: Bit Strings and Computing Models

At this point you should have been assigned to a cohort and met with
them at least twice (once during your assigned prep time and once
during your assessed time with a TA). This week, our main goals are:

- Now that you've had some cohort experience, reflect on how to make the most out of your cohort experience this semester.
- Begin exploration of the theory of computing, most importantly seeing the motivations for significant themes.
- Discuss some similarities and differences between the theory and practice of computing.
- Have you mind blown by infinities.
- See and example of the limits of computing.
- Learn a first model of computing.


# Schedule



Here is the expected schedule for cohorts, based on the day of your
assessed cohort meeting.  This schedule will repeat similarly
throughout the semester, with minor alterations occurring due to break days.


|       Day       | "Monday" Cohort | "Tuesday" Cohort | "Wednesday" Cohort | "Thursday" Cohort  |  "Friday" Cohort   |
| :-------------: | :-------------: | :--------------: | :----------------: | :----------------: | :----------------: |
|**Wed** 1 Sept|Preparation|<font color="lightgray">(Week 1)</font>|<font color="lightgray">(Week 1)</font>|<font color="lightgray">(Week 1)</font>|<font color="lightgray">(Week 1)</font>|
|**Thurs** 2 Sept|Preparation|Preparation|<font color="lightgray">(Week 1)</font>|<font color="lightgray">(Week 1)</font>|<font color="lightgray">(Week 1)</font>|
|**Fri** 3 Sept|Preparation|Preparation|Preparation|<font color="lightgray">(Week 1)</font>|<font color="lightgray">(Week 1)</font>|
|**Sat** 4 Sept|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|<font color="lightgray">(Week 1)</font>|
|**Sun** 5 Sept|Revision|**Prep Cohort Meeting**|Preparation|Preparation|Preparation|
|**Mon** 6 Sept|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|Preparation|
|**Tues** 7 Sept|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|Preparation|
|**Wed** 8 Sept|<font color="lightgray">(Week 3)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|
|**Thurs** 9 Sept|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|
|**Fri** 10 Sept|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|
|**Sat** 21 Sept|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|<font color="lightgray">(Week 3)</font>|**Writeup Due**|

# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

[Cohort Problems for Week 2 [PDF]](/ps/week2_blank.pdf)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

The above problems include completing the function implementations in
this python file (the comments in the file itself will guide you,
please read everything linearly): [straightline.py](/ps/straightline.py).

If you already have python3 on your machine, you should be good to go
for the programming problems. If you don't, please [follow these directions to setup Python](/python). 

# Write-up Problem

After the Assessed Cohort Meeting, your Cohort Leader will select one
problem that your cohort needs to write-up and submit.  The write-up
is due by **11:59pm** on the day after your assessed cohort
meeting (see the schedule above).


Download the [Problem Set 2 Template [zip]](/ps/week2.zip) and upload to overleaf. From there, add your solution to the appropriate .tex file for the problem assigned. Modify week2.tex to comment out `\usepackage{toc}` and instead be `\usepackage[response#]{toc}` where `#` refers to the number of the problem assigned.

# Reading

Material in this week's lectures parallels with:

- [TCS Chapter 2](https://introtcs.org/public/lec_02_representation.html) for our discussions on what can and cannot be represented by binary strings.
- This week's discussion of Boolean circuits gives a high-level treatment of several sections of [TCS Chapter 3](https://introtcs.org/public/lec_03_computation.html). In particular, we give semi-formal coverage of sections 3.1, 3.2, 3.3, 3.5, and 3.6 (but we'll discuss much of this in more detail next week).

Here are some things that may be of interest to you:

- Cantor's original proof (in German, but the math is universal, so somewhat understandable even without knowing German): Georg Cantor, [_Ueber eine elementare Frage der Mannigfaltigkeitslehre_](/docs/cantor-proof.pdf). Published in _Jahresbericht der Deutschen Mathematiker-Vereinigung_, Volume 1, 1891. ([About this Scan](https://jeffersonswheel.org/cantors-no-longer-lost-proof/))

# Videos

You can play all the videos using this playlist, but don't forget to take breaks:[Week 2 Playlist](https://youtube.com/playlist?list=PLZ9Gk_8DtbmEuIYH86411XrlILy1HJwwy)


<p>
Some Functions are Harder than Others (02:54)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/BVEwedDqJ8w" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>


<p>
What Parts Compute? (07:27)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/KMzwVDJ7EBo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Modeling Computers (08:16)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/Zg4FUYbwLqY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
A set is smaller than its powerset (07:27)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/zw_M0CdL43k" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Uncountability (20:56)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/BkKQt7KRDTE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Uncountability (20:56)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/BkKQt7KRDTE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
AND-OR-NOT (04:32)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/spadNZCSkmk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Programming with AND-OR-NOT (03:55)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/GpVEm7bAqH0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Equivalence of NAND and AON (09:35)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/VlcURykDg_A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>

<p>
Boolean Circuits (10:31)<br>
<iframe width="560" height="315" src="https://youtube.com/embed/lim78IpB8AI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>
</p>
