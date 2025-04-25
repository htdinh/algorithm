from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Approach: recursive

        # Time complexity: O(n) to go through all nodes
        # Space complexity: O(n) in worst case, O(logn) in best case (balanced tree). The O(log n) space refers to the call stack usage in a balanced tree, not including the result list.
        # where n is the number of nodes in the tree

        # Define a sub-routine for the task
        def inOrder(root: Optional[TreeNode]):
            if root is None:
                return root
            if root.left:
                yield from inOrder(root.left)
            yield root
            if root.right:
                yield from inOrder(root.right)
        
        # Solve the task with help from the sub-routine
        ans = []
        for node in inOrder(root):
            ans.append(node.val)
        return ans

if __name__ == "__main__":
    # Example usage
    # Build the tree manually (like the one above)
    root = TreeNode(50,
        left=TreeNode(30,
            left=TreeNode(20),
            right=TreeNode(40)),
        right=TreeNode(70,
            left=TreeNode(60),
            right=TreeNode(80)))
    
    sol = Solution()
    result = sol.inorderTraversal(root)
    print(result)  # Output: [20, 30, 40, 50, 60, 70, 80]