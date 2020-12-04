# **Perfect Squares**

1. Define the problem/solution recursively.

   - Given a positive integer _n_, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to _n_.
   - This problem has different recursive parts that I will be talking about. Let's use the following example:
     - perfectSqures(n=12) having this exmple, we will need to find the least number of perfect squre numbers that add 12. To do that, we need to identify what the perfect squares are that can sum 12. We do not neet perfect squares grater than n, but less than n. These possible perfect squares are 0, 1, 4, 9. Now, if we take a look at the problem, we will see that we will have different groups of perfect squres that can be sum 12. These groups can be seen as a tree as shown in picture [perfectSquares.png](https://github.com/DilanRamirez/problem-solving-exercises/blob/master/exams/exam2/perfectSquares/perfectSquares.png) Here is where we see how there is repeated work because even though this can be implemented as a recursive solution, the perfect squares stored in the tree nodes will be repeated. 0 can be omitted because it doesn't add to the sum.

2. Plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables to solve the problem).

   - One possible solution for this problem is to store all subproblems somehow that we can access them later. One option is to store them in a list. All base cases can be stored in a list like this baseCases = [0, 1, 2, 3] and then use a for loop to go over all square numbers less than n until we find the solution.

3. Talk about how you used **IDEAL** and **Duke 7** to tackle the problem

- **IDEAL**
  - **Identify Problem:** The perfect squre problem ask to find the least perfect square numbers that by adding them, can sum n.
  - **Define Goals:** The goals for this problem is to find the the least perfect squares. There can be more that two options, but our goal is to find the conviations of perfect squares with less numbers.
  - **Possible Strategies or Solutions:** First of all, we need to identify what perfect squares we need for a given n number. For example, if we get a 12, we do not neet to look for perfect squares biggers than 12. Therefore, we need all possible perfect square numbers less than n. After that, we need to start comparing all the possible groups that can be formed to sum n. We identified that this problem can be solved with dynamic programming because there is repeated work that we can avoid. A possible solution is to create a list to store all perfect square numbers less or equal to n and then traverse all possible perfect squares and try to find the min number that sum n.
  - **Anticipate Outcomes and Act:** The possible outcome can be to solve the problem by finding the less possible perfect square sum, but also it can be wrong because we may generate a wrong number that breaks the code or do not find the solution.
  - **Look and learn:** If we want to avoid repeated work, by doing this solution we can just store in the temporary square numbers to later use them.
- **DUKE 7**
  - **Work on small instance:**
    - One small instance can be n = 12. We need to find all possible perfect square numbers that sum 12. The possible perfect square numbers can be 0, 1, 2, 3 because 0^2 = 0, 1^2 = 1, 2^2 = 4, and 3^2 = 9. These number should be less than n that is 12.
  - **Write down what you did:**
    - As mentioned previously, the possible options must be less than n to be possible to sum n. After finding the possible perfect square numbers, we need to sum them and see which option is the best. I will show just part of the groups that can be formed.
    - For example:
      - 4 + 1 + 1 =6
      - 4 + 1 + 4 =9
      - 4+ 1 + 9 =14
      - 4 + 4 + 1 = 9
      - 4 +4 + 4 = 12
      - 4 + 4 + 9 = 17
  - **Find patterns (Generalize)**
    - As we can see, there are numbers that are repeated every time we try to find the square numbers to sum n. Here is where we can use dynamic programming because when we are in the 1 node, all possible squares will sum +1, when we are in node 4, all possible squares will summ +4 and so on.
  - **Test by Hand:** This test can be found at [perfectSquares.png](https://github.com/DilanRamirez/problem-solving-exercises/blob/master/exams/exam2/perfectSquares/perfectSquares.png)
