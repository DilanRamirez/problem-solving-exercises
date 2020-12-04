# **Maximum Length of Pair Chain**

1. Define the problem/solution recursively.

   - You are given n pairs of numbers. In every pair, the first number is always smaller than the second number. Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion. Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

   * This problem a recursive part that I will be talking about. The problem consist of having a square array. The internal arrays have two elements. To be able to form the chain, the first elemet of the first array must be smaller than the second array's value. Here is where we identify the recursion because we to do the same work over and over again to find all possible chains because the pairs can be in any order. To avoid recursive calls, we can use dynamic programming by keeping track of the elements already visited. To implement it, first we need to sort all internal arrays. By doing it, we can identify the smallest and largest elements. Then, we can check if b < c.
   * For example:
     - [[1,2], [2,3], [3,4]]
     - longest = [1,2] -> [3,4] = 2 chains

1. Plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables to solve the problem)

   1. One possible solution for this problem is to store all subproblems is to create a square array to store the elements that are already visited. Once we sort the internal arrays, we can create a square array n x n where n is the total numbers of the array. By doing that, we can identify what are the small numbers and how b can be less than c. If we find a chain, we can set the pair x,y = 1. Besides, we'll have a counter to increase it every time we find a chain. This counter will be returned.

1. Talk about how you used **IDEAL** and **Duke 7** to tackle the problem

   **IDEAL**

   - **Identify Problem:** The problem is to find all possible chains of a square array where we have two pairs (c,d) & pair (a, b) and the rule is that b < c.
   - **Define Goals:** The goal is to find the chains formed by the numbers of the internal arrays.

   * **Possible Strategies or Solutions:** One possible solution for this problem is to store all subproblems is to create a square array to store the elements that are already visited. Once we sort the internal arrays, we can create a square array n x n where n is the total numbers of the array. By doing that, we can identify what are the small numbers and how b can be less than c. Besides, we'll have a counter to increase it every time we find a chain. This counter will be returned.
   * **Anticipate Outcomes and Act:** The possible outcome can be a matrix filled with ones and all possible chains with a counter returning the total chains.
   * **Look and learn:** After working on this solution, I realized how dynamic can be used to solve a problem like this that has a lot of repeated work.

   **DUKE 7**

   - **Work on small instance:**
     - One small instance can be:
       - [[1,2], [2,3], [3,4]]
       - longest = [1,2] -> [3,4] = 2 chains

   * **Write down what you did:**
     - I trace a small example and tried to found what is the part that is repated.
   * **Find patterns (Generalize)**
     - By keeping track of the elements already visited. To implement it, first we need to sort all internal arrays. By doing it, we can identify the smallest and largest elements. Then, we can check if b < c.

1. Code your solution
