# **Arithmetic Slices**

1. Define the problem/solution recursively.

   - A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

   * This problem a recursive part that I will be talking about. The problem consist of having a list of numbers. We need to check if the sequence of these numbers are valid. If the sequence is valid, this will be the slice. If the slice is valid, we can add the next number. Now here we have the recursion part because we need to check the already sequence of numbers, but if we implement dynamic programming, we already will know that the last sequence was valid. Therefore, we only need to check the sequence with the new number to add.
   * For example:
     - [1, 2, 3, 4]
     - Slices = [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4]

2. Plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables to solve the problem)

   1. One possible solution for this problem is to store all subproblems is to a list that contains the sequence already accepted, if the there is another similar sequence, this can be checked by looking at the list of sequence. Moreover, we'll need a counter to keep track of the number of slices to finally return it.

3. Talk about how you used **IDEAL** and **Duke 7** to tackle the problem

**IDEAL**

- **Identify Problem:** The problem is to find all possible slices. We have an array, so we need to check if a convination of numbers can be a slice if at least three elements and if the difference between any two consecutive elements is the same.
- **Define Goals:** The goal is to find the slices formed by the numbers of the array.

* **Possible Strategies or Solutions:** One possible solution for this problem is to store all subproblems is to a list that contains the sequence already accepted, if the there is another similar sequence, this can be checked by looking at the list of sequence. Moreover, we'll need a counter to keep track of the number of slices to finally return it.
* **Anticipate Outcomes and Act:** The possible outcome can be a list containing all the sequence of numbers already seen and a counter with the total number of slices.
* **Look and learn:** After working on this solution, I realized how dynamic can be used to solve a problem like this that has a lot of repeated work.

**DUKE 7**

- **Work on small instance:**
  - One small instance can be:
    - [1, 2, 3, 4]
    - Slices = [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4]

* **Write down what you did:**
  - I trace a small example and tried to found what is the part that is repated.
* **Find patterns (Generalize)**
  - Once we check a sequence of numbers, we will already know if this sequence is valid or not, so when we want to add a new number, we olny need to check the sequence with this new number.
