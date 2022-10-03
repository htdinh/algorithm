from typing import List

class Solution:
    def maxIncreaseKeepingSkyline1(self, grid: List[List[int]]) -> int:
        """
        Approach: For each of the direction: north-south or east-west, the current max (skyline) is same. The building
        height is allowed raised up to that skyline limit. First solution is still rather explicit.
        Complexity: Time
        """
        n = len(grid)
        west_east = [max(grid[i]) for i in range(n)]  # Time O(n), Space O(n)
        north_south = [0] * n
        for j in range(n):
            north_south[j] = max(grid[i][j] for i in range(n))  # Time O(n^2), space O(n)
        max_height = 0
        for i in range(n):
            for j in range(n):
                max_height += min(west_east[j], north_south[i]) - grid[i][j]  # Time O(n^2) but anyway this is the min,
                # because we have to go through every existing building.
        return max_height

    def maxIncreaseKeepingSkyline2(self, grid: List[List[int]]) -> int:
        """
        Just simply neater code. Applying map() function.
        About the final sum, instead of sum(xi-yi) as in Sol1 does sum(xi) - sum(yi)
        """
        # Here return the list, not exhausting like map, that can be reused in nested loop
        rows, cols = map(max, grid), list(map(max, zip(*grid)))
        return sum(min(i, j) for i in rows for j in cols) - sum(map(sum, grid))