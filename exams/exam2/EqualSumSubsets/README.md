# \***\*Partition to K Equal Sum Subsets\*\***

1. Define the problem/solution recursively.

   - Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
   - This problem has different recursive parts that I will be talking about. The problem states we need to find k subsets, so first of all we need to verify k is not greater than the lenght of the array. After that, the recursive parts comes when we try to find and fill the sets.
   - One example can be having an array like this one: [4,3,2,3,5,2,1] and k = 4. To find the maximun value all subsets can sum, we sum all numbers of the array and divide it by k, so the answer would be 5. This means we all subsets must sum 5. After that, we will see how the recursion can be used. To explain it better, I will using the following figure [perfectSquares.png](https://github.com/DilanRamirez/problem-solving-exercises/blob/master/exams/exam2/EqualSumSubsets/EqualSum.png) As we can see in the picture, we will be going element by element in the array and substracting it from 5. If we get a 0, it means we found a subset. Otherwise, we need to visit the next element. The problem is that we will be visiting the same numbers in the array many times until we find the numbers that sum 5 in this case. Here is where recursion is involved but also dynamic programming to avoid visiting the same number many times.

1. Plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables to solve the problem)

   1. One possible solution for this problem is to store all subproblems

1. Talk about how you used **IDEAL** and **Duke 7** to tackle the problem

   1. **IDEAL**

      - **Identify Problem:** The identified problem is to create or find k subsets whose internal sums are all equal. These subset are from the original array given in the problem.
      - **Define Goals:** The goals are to divide the main array into k number of subsets. After that, populate them with numbers whose sums are equal for all of them.

      * **Possible Strategies or Solutions:** First of all,
      * **Anticipate Outcomes and Act:** The possible outcome can be
      * **Look and learn:**

   2. **DUKE 7**- **Work on small instance:**

      - One small instance can be

      * **Write down what you did:**
        - As mentioned previously,
      * **Find patterns (Generalize)**
        - As we can see
      * **Test by Hand:**
      * **Translate to Code**
      * **Test**
      * **Debug**

1. Code your solution.
