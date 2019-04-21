"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def breadth_first_depth(self, root: 'Node') -> int:
        height = 0
        dq = deque([root]) if root else deque([])

        while dq:
            height += 1
            for _ in range(len(dq)):
                node = dq.popleft()
                dq.extend([child for child in node.children])

        return height

    def another_breadth_first_search(self, root: 'Node') -> int:
        if not root:
            return 0

        def find_height(queue):
            next_queue = []
            for _ in range(len(queue)):
                node = queue.pop()
                for child in node.children:
                    next_queue.append(child)

            if next_queue:
                return 1 + find_height(next_queue)
            else:
                return 1

        return find_height([root])

    def depth_first_search(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1

        height = 1 + max([self.depth_first_search(child) for child in root.children])

        return height

    def another_depth_first_search(self, root: 'Node') -> int:
        height = 0
        stack = [(root, 0)] if root else []

        while stack:
            node, depth = stack.pop()
            if depth == height:
                height += 1

            for child in node.children:
                stack.append((child, depth + 1))

        return height
