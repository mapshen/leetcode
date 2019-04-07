# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        def helper(node, sum, path):
            if node:
                path.append(node.val)

                if not node.left and not node.right and sum == node.val:
                    paths.append(path[:])

                helper(node.left, sum - node.val, path)
                helper(node.right, sum - node.val, path)

                path.pop()

        paths = []
        helper(root, sum, [])
        return paths
