from typing import List
"""
In theory, this could be seen as two pointers, one for left, one for right. But we can keep this simple with 
1 pointer. The currentSum is reset to 0 before adding the current element (right).

Pay attention to the question requirement, to return just the maxSum. Return maxSum not currentSum. 

Initialize maxSum to be the first element. It would be wrong to initialize it to 0 because there are possibly 
negative elements in the list of nums. 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = nums[0]
        for num in nums:
            if currentSum <= 0:
                currentSum = 0
            currentSum += num
            maxSum = max(maxSum, currentSum)
        return maxSum

    def maxSubArray_return_indices(self, nums: List[int]) -> List[int]:
        """
        If the question asks to return the subarray itself,
        we then need to keep track of the left and right indexes.
        """
        currentSum = 0
        maxSum = nums[0]
        left = 0
        right = 1
        max_right = right
        max_left = left
        for right, num in enumerate(nums):
            if currentSum <= 0:
                currentSum = 0
                left = right
            currentSum += num
            if maxSum < currentSum:
                max_left = left
                max_right = right+1
                maxSum = currentSum
        return nums[max_left: max_right]