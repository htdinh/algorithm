"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the MAXIMUM number of balanced strings you can obtain.

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Constraints:

(1) 2 <= s.length <= 1000
(2) s[i] is either 'L' or 'R'.
(3) s is a balanced string.
"""
class Solution(object):
    def balancedStringSplit(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        """
        Approach: Return the MAXIMUM number of balanced strings you can obtain. Each substring should be as short 
        as possible. As soon as the substring meets the condition for a balancedString -> split. As many splits as 
        as possible. 
        
        Define the condition for balancedSplit: sum of "L" = sum of "R". Represent the two as number +1 and -1 so we 
        can easier identify equality. 
        
        Time O(n): needs to go through all characters of the string s
        Space: O(1): only need 1 variable temp_sum for all characters above, increment oder decrement alters the value 
        of that variable temp_sum. Another variable to store ans. 
        """
        ans = 0
        score = {"R": -1, "L": 1}
        temp_sum = 0
        """
        Some edge cases: "LR" and "LLLLLRRRRR" both result in ans=1
        """
        for c in s:
            temp_sum += score[c]
            if temp_sum == 0:
                ans += 1
        return ans

    def balancedStringSplit2(self, s: str) -> int:
        """
        Using a stack (in Python as a list) to track the status of a substring. Empty stack -> balanced.
        :param s:
        :return: number of balanced substring
        """
        """
        In case of stack, the storage of variable into the stack is less useful than the size of the stack. 
        Here we care only about the size of the stack.
        
        Time O(n), space O(n) maximally 1/2 of the characters must be stored in the stack. 
        """
        stack = []
        ans = 0
        for c in s:
            if c == 'R': stack.append('R')
            else: stack.pop()
            if len(stack)==0:
                ans+=1
        return ans
