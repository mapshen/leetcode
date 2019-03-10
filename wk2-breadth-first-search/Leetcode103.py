# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue=deque([root])
        result=[]
        con = 0
        while queue:
            layer=[]
            for eachnode in range(len(queue)):
                curnode = queue.popleft()
                layer.append(curnode.val)
                if curnode.left != None:
                    queue.append(curnode.left)
                if curnode.right != None:
                    queue.append(curnode.right)
            if con==0:
                result.append(layer)
                con = 1
            else:
                result.append(layer[::-1])
                con=0
        return result
