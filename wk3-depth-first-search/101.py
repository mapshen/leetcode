# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def breath_first_search(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque([root.left, root.right])

        while queue:
            left_node = queue.popleft()
            right_node = queue.popleft()

            if not left_node and not right_node:
                continue

            if not left_node or not right_node:
                return False

            if left_node.val != right_node.val:
                return False

            queue.append(left_node.left)
            queue.append(right_node.right)
            queue.append(left_node.right)
            queue.append(right_node.left)

        return True

    def depth_first_search(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = [root.left, root.right]

        while queue:
            right_node = queue.pop()
            left_node = queue.pop()

            if not left_node and not right_node:
                continue

            if not left_node or not right_node:
                return False

            if left_node.val != right_node.val:
                return False

            queue.append(left_node.left)
            queue.append(right_node.right)
            queue.append(left_node.right)
            queue.append(right_node.left)

        return True

    def another_depth_first_search(self, root: TreeNode) -> bool:
        if not root:
            return True

        def mirror(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and mirror(l.right, r.left) and mirror(l.left, r.right)

        return mirror(root.left, root.right)
