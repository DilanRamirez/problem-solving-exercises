# **Perfect Squares**

1. Define the problem/solution recursively.
   - Given a positive integer _n_, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to _n_.
   - This problem has different recursive parts that I will be talking about. Let's use the following example:
     - perfectSqures(n=12) having this exmple, we will need to find the least number of perfect squre numbers that add 12. To do that, we need to identify what the perfect squares are that can sum 12. We do not neet perfect squares grater than n, but less than n. These possible perfect squares are 0, 1, 4, 9. Now, if we take a look at the problem, we will see that we will have different groups of perfect squres that can be sum 12. These groups can be seen as a tree.
     - [logo.png](DilanRamirez.github.com/problem-solving-exercises/tree/master/exams/exam2/perfectSquares/logo.png)
2. Plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables to solve the problem).
3. Talk about how you used **IDEAL** and **Duke 7** to tackle the problem
   - **IDEAL**
     - **Identify Problem:** The perfect squre problem ask to find the least perfect square numbers that by adding them, can sum n.
     - **Define Goals:** The goals for this problem is to find the the least perfect squares. There can be more that two options, but our goal is to find the conviations of perfect squares with less numbers.
     - **Possible Strategies or Solutions:** First of all, we need to identify what perfect squares we need for a given n number. For example, if we get a 12, we do not neet to look for perfect squares biggers than 12. Therefore, we need all possible perfect square numbers less than n. After that, we need to start comparing all the possible groups that can be formed to sum n.
4. Code your solution.
