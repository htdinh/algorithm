from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Approach: recursive
        # Time complexity: O(n) to go through all nodes
        # Space complexity: O(n) in worst case, O(logn) in best case (balanced tree). The O(log n) space refers to the call stack usage in a balanced tree, not including the result list.
        def preOrder(root: Optional[TreeNode]):
            if root is None:
                return root
            yield root
            if root.left:
                yield from preOrder(root.left)
            if root.right:
                yield from preOrder(root.right)
        
        ans = []
        for node in preOrder(root):
            ans.append(node.val)
        return ans

    def preoderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        # Approach: iterative
        ans = []
        if root is None:
            return ans
        # Use a stack to keep track of nodes to visit
        # Time complexity: O(n) to go through all nodes
        stack = [root]

        while stack:
            node = stack.pop()
            ans.append(node.val)
            # Push right child first so that left child is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        # The order of appending to the stack is important
        # to ensure the left child is processed before the right child.
        # This is because the stack is LIFO (Last In First Out)
        # So we push the right child first, then the left child.
        # When we pop from the stack, the left child will be processed first.
        # This ensures that the preorder traversal is done correctly.
        # Preorder traversal: root -> left -> right
        # Inorder traversal: left -> root -> right
        # Postorder traversal: left -> right -> root
        return ans

    def inoderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        # Approach: iterative
        ans = []
        if root is None:
            return ans
        # Use a stack to keep track of nodes to visit
        # Time complexity: O(n) to go through all nodes
        stack = []

        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            ans.append(current.val)
            current = current.right
        return ans

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

    preorder_result = sol.preorderTraversal(root)
    print(preorder_result)  # Output: [50, 30, 20, 40, 70, 60, 80]
    preorder_iterative_result = sol.preoderTraversalIterative(root)
    print(preorder_iterative_result)  # Output: [50, 30, 20, 40, 70, 60, 80]