# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue=[root]
        result=[]
        while queue:
            layer=[]
            for eachnode in range(len(queue)):
                curnode = queue.pop(0)
                layer.append(curnode.val)
                if curnode.left != None:
                    queue.append(curnode.left)
                if curnode.right != None:
                    queue.append(curnode.right)
            result.append(layer)
        return len(result)
        
