"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a POSITIVE decimal integer, return the MINIMUM number of POSITIVE deci-binary numbers
needed so that they sum up to n.

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Constraints:

(1) 1 <= n.length <= 105
(2) n consists of only digits.
(3) n does not contain any leading zeros and represents a POSITIVE integer.
"""
class Solution(object):
    def minPartitions1(self, n: str) -> int:
        """
        :type n: str
        :rtype: int
        """
        # Approach: return the max digit among all digits
        # Time O(n) with respect to the length of the number. Always need to compare all digits.
        # Space O(1) only need to save 1 value for the max, then compares with the next digit.
        return max(int(i) for i in list(n))

    def minPartitions1b(self, n: str) -> int:
        """
        :type n: str
        :rtype: int
        """
        return int(max(n)) # Make use the constraint: n consists of only digits. The string n is actually list of char,
        # Comparing the max int is identical to max of char.

    def minPartitions2(self, n: str) -> int:
        # Approach: same as above, but starts with the largest possible value: 9, then reduces it further.
        # Best case: found digit 9 on the beginning of the number.
        # Normally, as soon as the max digit is found, and it is found on the list of chars, it breaks the search.
        # Worst case: the number 000000, go through all the 9 possible values, and search completely the
        # all the digits in the number => Time O(9n) = O(n).
        # Because of the early stops in the search, this method is faster.

        # Why?
        # - Sol1 doesn't limit the search space to 1-9. Sol2 does.
        # - Even though both has same time complexity, sol1 is always, sol2 has early exits

        # Why stop at 0? At least a digit 1 must be there because of the constraint (3). Otherwise, for example, if
        # n is non negative number, which means 0 included, then we have to handle the special case for n=0, ans=1. But
        # that would also complicate the question, because the question asked for POSITIVE compoments.
        for ans in range(9, 0, -1):
            if str(ans) in n:
                return ans
