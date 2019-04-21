# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def breadth_first_search(self, root: TreeNode) -> List[int]:
        """
        Visit each node in each layer from left to right.

        :param root:
        :return:
        """
        view = []
        dq = deque([root]) if root else deque([])

        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                value = node.val

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            view.append(value)

        return view

    def depth_first_search(self, root: TreeNode) -> List[int]:
        """
        Always visit the right subtree first.

        :param root:
        :return:
        """
        view = []
        depth = 0
        stack = [(root, 0)] if root else []

        while stack:
            node, d = stack.pop()
            if d == depth:
                depth += 1
                view.append(node.val)

            if node.left:
                stack.append((node.left, d + 1))
            if node.right:
                stack.append((node.right, d + 1))

        return view
