+++
date = "23 Oct 2019"
draft = false
title = "Problem Set 5 Update"
author = "David Evans and Nathan Brunelle"
slug = "ps5update2"
+++

Two more updates to [PS5](/ps/ps5.pdf):

1. **Problem 6** considered adding an array but not loops to NAND-CIRC. But, it doesn't make sense to have arrays without any way to update the index used to access them. So, for this to make sense we need to also have an instruction to update i. So, we have modified this question to add conditional increment and decrement instructions:

   - `CINC` _v_ takes a regular variable as its input, and if the value of _v_ is 1 it updates the value of `i` to be `i` + 1. Otherwise (when _v_ is 0), it does not do anything.

   - `CDEC` _v_ takes a regular variable as its input, and if the value of _v_ is 1 it updates the value of `i` to be max(`i` - 1, 0). Otherwise, it does not do anything.

2. Since we didn't get to examples of uncomputability proofs in class
this week, we're deferring Problem 9 and Problem 10 from PS5 to
PS6. If you've already solved these, great - just save your solution
to submit for the same questions that will be moved to PS6.
