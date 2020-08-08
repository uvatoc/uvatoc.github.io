+++
date = "12 Aug 2020"
draft = false
title = "Syllabus"
slug = "syllabus"
+++

   <div class="yellownote">
**DRAFT: subject to change until posted**
   </div>

# Overview

**Course Description:** The goal of this course is to understand the
  fundamental limits on what can be efficiently computed in our
  universe and other possible (or imaginary) universes. These limits
  reveal deep and mysterious properties about information,
  communication, and computing, as well as practical issues about how
  to solve problems.


Two fundamental questions about any problem are:
 
 1. _Can it be solved using a machine of a certain type?_ (computability)
 2. _How much does it cost to solve it?_ (complexity)
 
We explore these questions by developing abstract models of computing
machines and reasoning about what they can and cannot compute
efficiently.  We will also look at some applications in cryptography
that take advantage of problems being hard to solve, and what can be
done when a problem cannot be solved or is too expensive to solve.

**Official Prerequisites:** CS 2102 and CS 2110 (or comparable
  courses) with grades of C- or higher. (We do not enforce this
  prerequisite, and students who are comfortable with the expected
  background below should be able to succeed in the course.)

**Expected Background:** We expect students entering cs3102 to be
  comfortable using proof techniques involving first order predicate
  logic and induction, and reasoning about finite and infinite sets,
  and understanding recursive definitions and problem solving.

We also expect students to be able to read and write short
programs. We will use the Python programming language for some
assignments in the class. It is not necessary to have previous
experience with Python, but you should have enough programming
experience to be able to pick up what you need to read and write short
Python programs on your own. If you do not satisfy the prerequisites,
you should meet with one of the instructors to discuss whether you
should take the class. 


**Class Meetings:** The course is officially scheduled for Mondays and
  Wednesdays, 3:30-4:45pm. We will use this time for a full class
  welcome meeting on the first day of the course, Wednesday, 26
  May. For subsequent weeks, students will have cohort meetings (see
  [details below](#cohorts)).
    
**Textbook:** Boaz Barak, [_Introduction to Theoretical Computer Science_](https://introtcs.org/public/index.html).

This is a new textbook that is freely available from
[https://introtcs.org](https://introtcs.org) under a Creative Commons
license. In addition to costing
[$271.95](https://web.archive.org/web/20171023211340/http://www.cengage.com/c/introduction-to-the-theory-of-computation-3e-sipser/9781133187790)
less than the traditional textbook for this class}, this book takes a
modern and innovative approach to introducing theory of computation
which has several advantages (and a few disadvantages) of the
traditional approach (which we will discuss some in class, and be
happy to elaborate on during office hours). We plan to follow the
organization and material in the textbook fairly closely, but will
also cover some topics that are not included, and present some of the
material in ways that are different from how it is presented in the
book.

Although the book is available free to read on-line, if you have
access to a printer we do recommend printing out the chapters you are
reading from the PDF files. [Numerous
studies](https://www.scientificamerican.com/article/reading-paper-screens/)
have found that essentially everyone reads faster and comprehends
better from printed paper than from even the best on-screen
reading. To encourage on-paper reading, we will provide links on the
[course website](https://uvatoc.github.io) to PDF files for relevant
chapters.

In addition to the course textbook, some readings will be assigned
from other (freely available) sources.

**Lectures:** Due to Covid-19, we will not have any in-person lectures
  this semester. Instead, we will be providing recorded videos,
  primarily adapted from lectures recorded from previous lectures for
  this course, and supplemented by other available materials. Each
  week's preparation materials will include links to relevant (and
  maybe some irrelevante) videos.


**Course Objectives:** Students who complete the course will:

- Improve their [mathematical thinking skill and
  habits](https://medium.com/@jeremyjkun/habits-of-highly-mathematical-people-b719df12d15e),
  including thinking precisely about definitions, stating assumptions
  carefully, critically reading arguments, and being able to write
  convincingly.

- Be able to understand both finite and infinite formal models of computation and to reason about what they can and cannot compute.
- Understand both intuitively and formally what makes some problems too expensive to solve, and what can be done in practice when an unsolvable or intractable problem is encountered.
- Reason formally about the cost of computation, and be able to prove useful bounds on the costs of solving problems, including showing that certain problems are intractable.
- Learn about some interesting aspects of theoretical computer science, including cryptography and machine learning.
    

# Course Staff

\shortsection{Instructors} The course is co-taught by Nathan Brunelle and David Evans. Feel free to contact either of us with any questions about the course, computer science, or anything else you think we can help with (but please read the section below on communications to determine if it would be better to post a message in slack before emailing us).

\begin{center}
\begin{tabular}{p{.4\textwidth}@{\hskip .1\textwidth}p{.4\textwidth}}
     Nathan Brunelle \newline
     \url{njb2b@virginia.edu} \newline
     Office: {\bf Rice 209} \newline
     Office Hours: {\bf Tuesdays, 4-6pm} & 
     David Evans \newline
     \url{evans@virginia.edu} \newline
     Office: {\bf Rice 507} \newline
     Office Hours: {\bf Tuesdays, 9-11am} \\
\end{tabular}     
\end{center}

\textbf{Teaching Assistants:} Will be updated soon (see course website).

\section*{Communication}

We will primarily use the course website for one-to-many communications (posting course materials), and use the course slack for interactive communications. 

\shortsection{Course Website} We will post all course materials at \url{https://uvatoc.github.io}. We will use the collab site for assignment submissions, and occasionally to post materials we cannot post publicly.

\shortsection{Slack} We will use the course slack workspace for most other course communications. You should signup at \url{https://uvatoc.slack.com/}, and we expect students to receive messages we send to the slack \verb|#general| channel as well as any direct messages we send to you on slack. We will also used the \verb|#inclass| channel for real-time communication during classes.  

If you have questions about course materials or assignments that will be relevant to other students, please ask them in \verb|#general|. This will get the fastest response, since all of the course staff and students will see your question there and be able to respond to it. If you have questions of a personal nature that you only want to make to the instructors, please use the course slack to contact both of us (\verb|@dave @Nathan Brunelle|) in a Direct Message channel instead of emailing us independently.

\shortsection{Email} Managing email for a large class like this is difficult, and we prefer to use the course slack for most communications relevant to the class. You should feel free to use email for messages peripherally related to the course (e.g., emailing an instructor about interest in their research). You should also use email if you post a question on slack but don't receive an adequate response within 24 hours. 

\shortsection{Calendar} The course calendar is available as a \href{https://calendar.google.com/calendar/embed?src=fcp59v0s307hlio3a7ok6mu18k%40group.calendar.google.com&ctz=America%2FNew_York}{%
Google calendar}, linked from the course website. Students are encouraged to incorporate this into your own calendar. If you use Google Calendar, just click the “+” at the bottom right of the calendar page. If you use another calendar program, you can incorporate this calendar using ical.

\section*{Honor Expectations}

We believe strongly in the value of a community of trust, and expect all of the students in this class to contribute to strengthening and enhancing that community. The course will be better for everyone if everyone can assume everyone else is trustworthy. The course staff starts with the assumption that all students at the university deserve to be trusted.

To ensure that expectations are clear to everyone, all students are required to read, understand, and sign the \href{https://uvatoc.github.io/pledge}{course pledge}: \url{https://uvatoc.github.io/pledge}.

\shortsection{Collaboration Policy} The collaboration policy will be different for each assignment, and will be described on each assignment document. We aim to make the language describing the policy as clear and unambiguous as possible, but if anything is ever unclear about the stated policy for an assignment, please clarify with the course staff. The penalty for policy violations will be considered on a case-by-case basis, with a penalty commensurate the severity of the offense. 

%Actions deserving of extra credit include, but are not limited to, insightful questions/comments in lecture, completing given extra credit assignments, submitting responses to current events which are relevant to algorithms, attending special seminars/colloquia, slide corrections, compelling office-hours conversation.  Actions that require more effort to complete will be given a higher weight than those that require little effort. As a general rule, if you have done something that you feel might be deserving of extra credit, just ask for it! Submit extra credit via email to \url{extracredit.cs3102@gmail.com}.

\section*{Assignments and Exams}

\shortsection{Exams} We will have three exams, held during our normal class period in the normal classroom:
\begin{enumerate}
    \item Exam 1: {\bf Wednesday, October 2}
    \item Exam 2: {\bf Wednesday, November 6}
    \item Exam 3: {\bf Wednesday, December 4}
\end{enumerate}

No collaboration is permitted on the exams. Students may construct a one-page (letter-size, two-sided) reference sheet for use during the exam, but all other resources are forbidden (no internet, textbook, other humans, magnification instruments, etc.). We will provide detailed guidelines on what to expect on each exam, but you should expect them to focus on material covered since the previous exam but also include questions that test your understanding of earlier material.

Note that we do not intend to use the registrar's official final exam period for this course, and instead will have a regular-length exam during the final scheduled class.

We recognize that some students may not be able to demonstrate their best ability during a 75 minute in-class exam, therefore we will provide option for students to request an oral final exam to be scheduled with one of the instructors during the exam period. 

\shortsection{Problem Sets} 
We hope students learn value in applying theoretical insights to computer science practice, and will also provide more concrete exercises to help students grasp theoretical ideas. For this reason, each assignment will contain a mixture of theoretically-focused written problems (with an emphasis on writing proofs) and integration-focused programming problems. Each problem set will state a clear collaboration policy (which typically will allow you to discuss problems with others, but require that you write up your solutions by yourself and understand everything in it) and we trust and expect students to follow these policies vigilantly.

Problem sets will be due most {\bf Fridays at 4:19pm}, with some exceptions due to university holidays and weeks when there are exams. See the 
\href{https://calendar.google.com/calendar/embed?src=fcp59v0s307hlio3a7ok6mu18k%40group.calendar.google.com&ctz=America%2FNew_York}{%
course calendar} for specific due dates. Each problem set will include specific directions for how to submit your solutions, and we expect students to read and follow these carefully.

\shortsection{Extensions and Late Submissions} Extensions will be granted to individual students on a case-by-case basis. We are more likely to respond positively to an extension request if it is made well before an assignment is due and provides a reasonable justification for the extension. To request an extension, please complete the \href{https://forms.gle/5BKMsvFCkR2LaQRr9}{Extension Request Form}. We are sympathetic to situations where a traumatic late event prevents you from being able to complete an assignment, and appreciate you bringing these to our attention even if the deadline has passed.  If you find that you will be unable to make one of the scheduled exams, contact the course instructors immediately.

\iffalse % we'll put this on the actual assignment
The pen-and-paper (a.k.a. ``written'') assignments are not really pen-and-paper: they must be typeset with LaTeX (typically pronounced as either Lay-teck or Lah-teck\footnotemark), a professional formatting system. Tutorials on how to use LaTeX will be posted when the first written problem set is released. We recommend using \hyperlink{www.overleaf.com}{Overleaf}, an in-browser editor which behaves much like Google Docs for LaTeX. \dnote{I'm inclined not to mention any other options - if people aren't already using latex some other way, best to encourage using overleaf}
If you prefer to keep all of your files local, or to be able to work offline, LaTeX is also easily installable on many computers: 
\begin{itemize}
    \item Cygwin (which you may have seen in CS 2150) has LaTeX packages that can be installed
    \item MiKTeX provides a stand-alone installer for Windows and Mac, \url{miktex.org}
    \item Ubuntu and CentOS provide TeXLive packages in their repos
\end{itemize}
We generally will not accept LaTeX documents with images of text or formulas; \textbf{you must typeset the formulas in LaTeX}, not in another program  (or by hand) and have them exported as images. Images of drawing, diagrams, etc. are acceptable. 

\footnotetext{To Quote Leslie Lamport (the creator LaTeX) ``One of the hardest things about LaTeX is deciding how to pronounce it.This is also one of the few things I'm not going to tell you about LaTeX, since pronunciation is best determined by usage, not fiat. TeX is usually pronounced teck, making lah-teck, and lay-teck the logical choices; but language is not always logical, so lay-tecks is also possible.''}

\textbf{Regrades:} 
\fi



\section*{Grading}

Spend your energy focusing on what you are learning, instead of worrying about your grade. That said, we understand students are often stressed about grading and understandably want to know where they stand in a class without having to rely just on the judgment of the course staff.

Grading will be based on your performance on the exams and homework assignments, with additional adjustments made based on exceptional contributions to the class. We aim to grade in a way that is useful (provides students with accurate measure of how well they understood what they should), motivating (encourages the behaviors we prefer, including hard but not obsessive work), fair (assigned higher grades to more deserving students), robust (arbitrary small perturbations do not have a material impact on someone's grade), and low stress (for both students and the course staff). 

For this reason, we choose not to prescribe a singular mathematical formula for quantitatively assigning letter grades but do provide a formula that can be used to compute a \emph{lower bound} on the grade you receive in the course:
\begin{equation*}
\textit{Grade} := \left(0.45 \sum_{p \in \textit{ProblemSets}} \frac{\text{grade}[p]}{\text{target}[p]}\right)
+ 0.15 \frac{\text{grade}[\textit{Exam 1}]}{\text{target}[\textit{Exam 1}]} 
+ 0.17 \frac{\text{grade}[\textit{Exam 2}]}{\text{target}[\textit{Exam 2}]} 
+ 0.23 \frac{\text{grade}[\textit{Exam 3}]}{\text{target}[\textit{Exam 3}]}
\end{equation*}
This will be converted to a letter grade using the \hyperlink{https://virginia.service-now.com/its?id=itsweb_kb_article&sys_id=1153c16fdba41f444f32fb671d961934}{default grade thresholds (in Collab)}.

In the formula, $\text{grade}[x]$ means your grade on assignment $x$, and $\text{target}[x]$ means the prescribed target grade for that assignment which represents ``full credit'' (gold star level performance). Note that, especially on assignments, there is no set maximum grade---the target grade represents what we expect from an excellent student who worked hard on the assignment and understands and can apply well everything we expect, and we expect all students in this class to be excellent.

With the exception of cases of academic dishonesty or inappropriate behavior, we guarantee that you will at least receive the minimum grade output by this formula, but you may be assigned a higher grade based on your overall performance. 

In general, we want to assign a grade that reflects the best possible interpretation of all you have done during the semester. An ``A'' grade means we are convinced that you can use the material in this class to solve new problems and understand it well enough to explain most concepts in the class (i.e., you would be a good TA for a future offering of this class). A ``B'' grade means we are convinced that you understand the main ideas in this class well enough to be well prepared for a follow-on course (i.e. one that has this as a pre-requisite).

Although the material we cover is challenging, and the pace may seem overwhelming at times, we are confident that all students who put effort into this class and take good advantage of available help will do well. Students who do especially outstanding work in the course will be offered positions in \href{https://www.jeffersonswheel.org}{our research groups}.

\shortsection{Bonuses} We hope students will go beyond the provided assignments and do other things to contribute to the class as well as beyond. We provide some concrete opportunities for this in the form of \emph{Challenge Problems} that will be announced in class, slack, or on assignments, but also will award bonuses for relevant and creative activities that students invent on their own. We also offer bounty bonuses for contributions to the course textbook: having a Pull Request accepted by the author is worth something (even if it is just a simple typo fix) and is worth comparable to a problem set for a significant technical fix, and becoming the \href{https://github.com/boazbk/tcs/graphs/contributors}{\#2 contributor to the book repository} is worth an automatic A in the class.

Bonus credits are not included in the prescriptive grade formula above, but will be considered heavily in any qualitative assessment toward a final letter grade assignment, and can potentially raise a student's grade by more than a full letter.



\section*{Additional Information}

\textbf{Special Circumstances:} The University of Virginia strives to provide accessibility to all students. If you require an accommodation to fully access this course, please contact the Student Disability Access Center (SDAC) at (434) 243-5180 or \url{sdac@virginia.edu}. If you are unsure if you require an accommodation, or to learn more about their services, you may contact the SDAC at the number above or by visiting their website \url{http://studenthealth.virginia.edu/sdac}.

For this course, we ask that students with special circumstances let us know as soon as possible, preferably during the \textbf{first week of class}.

\textbf{Religious Accommodations:} It is the University's long-standing policy and practice to reasonably accommodate students so that they do not experience an adverse academic consequence when sincerely held religious beliefs or observances conflict with academic requirements.  Students who wish to request academic accommodation for a religious observance should submit their request in writing to Prof.\ Brunelle or Prof.\ Evans as far in advance as possible. If you have questions or concerns about academic accommodations for religious observance or religious beliefs, visit \url{https://eocr.virginia.edu/accommodations-religious-observance}.

or contact the University's Office for Equal Opportunity and Civil Rights (EOCR) at \url{UVAEOCR@virginia.edu} or 434-924-3200.  Accommodations do not relieve you of the responsibility for completion of any part of the coursework missed as the result of a religious observance.

\textbf{Safe Environment:} The University of Virginia is dedicated to providing a safe and equitable learning environment for all students. To that end, it is vital that you know two values that we and the University hold as critically important:
 
\begin{enumerate}
    \item Power-based personal violence will not be tolerated. 
    \item Everyone has a responsibility to do their part to maintain a safe community on Grounds.
\end{enumerate}

If you or someone you know has been affected by power-based personal violence, more information can be found on the UVA Sexual Violence website that describes reporting options and resources available -- \url{www.virginia.edu/sexualviolence}. 
   
As your professors and as humans, know that we each care about you and your well-being and stand ready to provide support and resources as we can. As faculty members, we are responsible employees, which means that we are required by University policy and federal law to report what you tell us to the University's Title IX Coordinator. The Title IX Coordinator's job is to ensure that the reporting student receives the resources and support that they need, while also reviewing the information presented to determine whether further action is necessary to ensure survivor safety and the safety of the University community. If you would rather keep this information confidential, there are Confidential Employees you can talk to on Grounds (See \url{http://www.virginia.edu/justreportit/confidential\_resources.pdf}). The worst possible situation would be for you or your friend to remain silent when there are so many here willing and able to help.

\textbf{Well-being:} If you are feeling overwhelmed, stressed, or isolated, there are many individuals here who are ready and wanting to help. The Student Health Center offers Counseling and Psychological Services (CAPS) for all UVA students. Call 434-243-5150 (or 434-972-7004 for after hours and weekend crisis assistance) to get started and schedule an appointment. If you prefer to speak anonymously and confidentially over the phone, Madison House provides a HELP Line at any hour of any day: 434-295-8255.

\end{document}  



