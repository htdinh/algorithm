"""
A sequence of numbers is called arithmetic if it consists of at least two elements,
and the difference between every two consecutive elements is the same.
More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

Constraint
n == nums.length
m == l.length
m == r.length
2 <= n <= 500
1 <= m <= 500
0 <= l[i] < r[i] < n
-10^5 <= nums[i] <= 10^5

"""
from typing import List


class Solution:
    def checkArithmeticSubarrays1(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        Approach: Using sort, time complexity O(n log n), Python default.  Check the step, if not same => false
        Time O(nlogn x m), n length of nums, m length of l and r
        Space O(n) n variable to store the list of nums, from one pair of (li, ri) to another pair, the old results are
        deleted and reused. Space doesn't expand with respect to l and r.
        """
        ans = [True] * len(l)  # Initialize to True and only modify to False under certain conditions
        for i, (left, right) in enumerate(zip(l, r)):
            if right - left < 1:
                ans[i] = False
            else:
                array = sorted(nums[left:right + 1])
                diff = array[1] - array[0]

                # Loop inside the subsequence
                for j in range(1, right - left):
                    next_diff = array[j + 1] - array[j]
                    if next_diff != diff:
                        ans[i] = False
                        break
        return ans

    def checkArithmeticSubarrays2(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        Improvement: No need to sort, but using set. Conversion from list to set is of O(n) with n size of the list
        Comparing two sets with each other is also O(n) with n size of the set.
        """
        # Check the defined property
        def isArithmic(array):
            setA, n = set(array), len(array)

            # Step = 0, all items are identical
            if len(setA) < n:
                return len(setA) == 1  # This is only true if all the element in the array are identical

            # Max, min approach: each element are stepwise different from one another.
            maxA, minA = max(setA), min(setA)
            step_size, remainder = divmod(maxA - minA, n - 1)

            # If remainder is non-zero -> False # Not divisible -> can't fit
            if remainder > 0:
                return False

            # Divisible, just check if the two sets are identical (O(n))
            compared_set = set([element for element in range(minA, maxA, step_size)])
            compared_set.add(maxA)

            # If the compared_set!=setA -> False
            return setA == compared_set

        return [isArithmic(nums[start:stop + 1]) for start, stop in zip(l, r)]

