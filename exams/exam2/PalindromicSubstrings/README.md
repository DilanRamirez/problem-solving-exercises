# **Palindromic Substrings**

1. Define the problem/solution recursively.

   - Given a string, your task is to count how many palindromic substrings in this string. The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
   - This problem a recursive part that I will be talking about. We have a string and we need to check if this string contains substrings that are palindromes. The idea is to red the string from the first letter to the last and determining if by adding one word at a time we can form a palindrome. Now the recursion comes here because if we use a string with length 3. After a few interaction, this string will be splitted into three substring of length one, two substring of length two, and finally a string of lenght three. These substring are already used previously in the past substrings, so here is where we can use dynamic programming to avoid this over use of the same substrings.

1. Plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables to solve the problem)

   1. One possible solution for this problem is to store all subproblems is to create a matrix to store the values of the characters in the string. This matrix will have a size of n x n where n is the size of the string. All possible palindromes will be marked with a 1. If the character is already a palindrome, we do not need to check it again. Then, once we find a palindrome, we will have a counter that will be increased by one. This counter will be returned once all characteres were used.

1. Talk about how you used **IDEAL** and **Duke 7** to tackle the problem

   **IDEAL**

   - **Identify Problem:** The problem is to find all possible palindromes a string can have and keep track of how many are produced.
   - **Define Goals:** The goal is to find the palindromes of a string and return the total amount. Another goal is to find a solution using dynamic programming to optimize the algorithm.

   * **Possible Strategies or Solutions:** The way we can solve it is to iterate the string and create a matrix n x n where n is the size of the string. In this matrix I will store if a palindrome was already found to overcome the repeated work. There will be a counter vairable equal to 0 if a palindrome is found, the counter will be increased.
   * **Anticipate Outcomes and Act:** The possible outcome can be a matrix filled with the palindromes and a counter with the total palindromes. There can also be an outcome where the matrix is not filled and the counter remains in 0.
   * **Look and learn:** After working on this solution, I realized how dynamic can be used to solve a problem like this that has a lot of repeated work.

   **DUKE 7**

   - **Work on small instance:**
     - One small instance can be the string "aaa" with an output of 6 because it has the following palindromes "a", "a", "a", "aa", "aa", "aaa".

   * **Write down what you did:**
     - I trace a small example and tried to found what is the part that is repated.
   * **Find patterns (Generalize)**
     - In this example we use a string with length 3. After a few interaction, this string will be splitted into three substring of length one, two substring of length two, and finally a string of lenght three.

1. Code your solution.
