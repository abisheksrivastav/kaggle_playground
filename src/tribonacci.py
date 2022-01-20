# The Tribonacci sequence Tn is defined as follows: 

#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

#Given n, return the value of Tn.

 

#Example 1:

#Input: n = 4
#Output: 4
#Explanation:
#T_3 = 0 + 1 + 1 = 2
#T_4 = 1 + 1 + 2 = 4
#Example 2:

#Input: n = 25
#Output: 1389537


import re


class Solution:
    def tribonacci(self, n: int) -> int:

        index = 0   # index of the current tribonacci number
        tribonacci = [0, 1, 1]     # the first three tribonacci numbers
        while index < n:        # loop until the index is greater than n
            index += 1           # increase the index by 1
            tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[-3])  # add the current tribonacci number to the list
        return tribonacci[n]

        
      
# what  is tribonacci[-1] + tribonacci[-2] + tribonacci[-3]
# what is tribonacci[-1] + tribonacci[-2]
# what is tribonacci[-1]






        