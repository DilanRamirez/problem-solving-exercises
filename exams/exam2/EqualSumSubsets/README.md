# **Partition to K Equal Sum Subsets**

1. Define the problem/solution recursively.

   - Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
   - This problem has different recursive parts that I will be talking about. The problem states we need to find k subsets, so first of all we need to verify k is not greater than the lenght of the array. After that, the recursive parts comes when we try to find and fill the sets.
   - One example can be having an array like this one: [4,3,2,3,5,2,1] and k = 4. To find the maximun value all subsets can sum, we sum all numbers of the array and divide it by k, so the answer would be 5. This means we all subsets must sum 5. After that, we will see how the recursion can be used. To explain it better, I will using the following figure [perfectSquares.png](https://github.com/DilanRamirez/problem-solving-exercises/blob/master/exams/exam2/EqualSumSubsets/EqualSum.png) As we can see in the picture, we will be going element by element in the array and substracting it from 5. If we get a 0, it means we found a subset. Otherwise, we need to visit the next element. The problem is that we will be visiting the same numbers in the array many times until we find the numbers that sum 5 in this case. Here is where recursion is involved but also dynamic programming to avoid visiting the same number many times.

2. Plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables to solve the problem)

   1. One possible solution for this problem is to store all perfect square numbers less than n in an array. After that, we can identify which square numbers were already used. Once we use a square number, n is substracted by the this square number to later find another square number that can be used.

3. Talk about how you used **IDEAL** and **Duke 7** to tackle the problem

   **IDEAL**

   - **Identify Problem:** The problem is to find the least number of perfect square numbers which sum to n.
   - **Define Goals:** The goals are to optimized the work by doing a dynamic programming algorithm that uses recursion.

   * **Possible Strategies or Solutions:** The problem states we need to find k subsets, so first of all we need to verify k is not greater than the lenght of the array. After that, the recursive parts comes when we try to find and fill the sets. We substracted a square number from n to later find another square number that can be used until it reaches 0.
   * **Anticipate Outcomes and Act:** Find the least number of perfect square numbers used and optimized the algorithm.
   * **Look and learn:** After working on this solution, I realized how dynamic can be used to solve a problem like this that has a lot of repeated work.

   **DUKE 7**-

   - **Work on small instance:**
     - One small instance can be n =12. If we add 4 + 4 + 4 will get 12 which is the least number tof perfect square numbers.

   * **Write down what you did:**
     - As mentioned previously, using this small instance can be seen on [perfectSquares.png](https://github.com/DilanRamirez/problem-solving-exercises/blob/master/exams/exam2/EqualSumSubsets/EqualSum.png)
   * **Find patterns (Generalize)**
     - We can visualize this problem with a tree that every node contains the square numbers. Therefore, the patterns we can see are the repeated subtrees that can be avoided.
