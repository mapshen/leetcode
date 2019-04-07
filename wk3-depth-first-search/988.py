# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.ss = "~"

        def helper(node, s):

            if node:
                s = chr(node.val + ord('a')) + s
                if not node.right and not node.left:
                    self.ss = min(self.ss, s)

                helper(node.right, s)
                helper(node.left, s)

        helper(root, "")

        return self.ss

