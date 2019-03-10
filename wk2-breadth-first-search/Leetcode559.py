"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
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
                for child in curnode.children:
                    queue.append(child)
            result.append(layer)
        return (len(result))
