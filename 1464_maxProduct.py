from typing import List
"""
Constraint: 

2 <= nums.length <= 500  
1 <= nums[i] <= 10^3  # --> No need to use math.inf to have absolute infinity 
"""
class Solution:
    def maxProduct1(self, nums: List[int]) -> int:
        # Sort and find the last two largest item
        # Time O(nlogn), space O(1)
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)

    def maxProduct(self, nums: List[int]) -> int:
        # Track only the largest two items, no need to sort the rest. This save the time to O(n), space O(1)
        mx1 = mx2 = 1
        for n in nums:
            if n<mx2:  # Set the condition to skip, at minimum only once executed.
                continue
            elif n>mx2:  # Otherwise of we check for largest, then second largest, minimum two check for every sample.
                # Still same complexity O(n) but could be faster.
                if n>mx1:
                    mx2 = mx1
                    mx1 = n
                else:
                    mx2 = n
        return (mx1-1)*(mx2-1)
