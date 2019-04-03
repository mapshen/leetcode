# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = deque([root])
        result=[]
        while queue:
            layer=[]
            for eachnode in range(len(queue)):
                curnode = queue.popleft()
                layer.append(curnode.val)
                if curnode.left != None:
                    queue.append(curnode.left)
                if curnode.right != None:
                    queue.append(curnode.right)
            result.append(max(layer))
        return result
