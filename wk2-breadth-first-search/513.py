# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def breath_first_search(self, root: TreeNode) -> int:
        """
        Visit each node in each layer from right to left.

        :param root:
        :return:
        """

        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.pop()

                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)

        return node.val

    def depth_first_search(self, root: TreeNode) -> int:
        """
        Visit the left subtree first.

        :param root:
        :return:
        """

        queue = deque([(root, 0)])
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            if depth == max_depth:
                value = node.val
                max_depth += 1

            if node.right:
                queue.appendleft((node.right, depth + 1))
            if node.left:
                queue.appendleft((node.left, depth + 1))

        return value
