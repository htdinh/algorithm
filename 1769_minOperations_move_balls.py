import numpy as np
from typing import List


class Solution:
    def minOperations1(self, boxes: str) -> List[int]:
        """
        Approach: slice_dist is the 1D array of length n, indicate the distance of
        """
        n = len(boxes)
        distance = [i for i in range(n - 1, 0, -1)] + [i for i in range(n)] # Time O(n), space O(2n)=O(n)
        new_cost = [0] * n

        index = np.array([True if b == '1' else False for b in boxes]) # Time O(n), space O(n)

        for i in range(n):
            slice_dist = np.array(distance[i:i + n][::-1])
            new_cost[i] = sum(slice_dist[index])
            # Time complexity O(n^2), Space O(n)

        return new_cost

    def minOperations2(self, boxes: str) -> List[int]:
        """
        Approach: Consider a position i-th.
        Total effort = Effort to move all balls from left of ith to ith position + Same effort for all ball to the right
        Total effort (i) = Left effort (i) + right effort (i)
        For position (i+1)-th:
        Left effort (i+1) = Left effort(i) + number of all already in position ith.

        So the algorithm is as follow:
        Start with i=O, left(i) = 0
        Move on to calculate left(i+1) until i=n-1 (end).
        Here we have right(i=n-1) = 0, start moving left to get right(i-1).
        Adding left and right together, we have total cost.

        Time complexity: O(n)
        Space: O(n)
        """
        n = len(boxes)
        print(n)
        res = [0] * n
        ops = 0
        count = 0
        for i in range(n):
            res[i] += ops
            count += boxes[i] == '1'
            ops += count
        ops = 0
        count = 0

        for i in range(n - 1, -1, -1):
            res[i] += ops
            count += boxes[i] == '1'
            ops += count
        return res