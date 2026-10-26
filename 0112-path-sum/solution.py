
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # Check if the current node is a leaf
        if not root.left and not root.right:
            return targetSum == root.val

        # Search left or right subtree
        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining)
            or self.hasPathSum(root.right, remaining)
        )
