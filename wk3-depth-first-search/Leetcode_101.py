class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stackl = [root.left]
        stackr = [root.right]
        while stackl and stackr:
            nodel = stackl.pop()
            noder = stackr.pop()
            if nodel == noder == None:
                continue
            if nodel==None or noder==None:
                return False
            if nodel.val != noder.val:
                return False
            stackl.append(nodel.left)
            stackr.append(noder.right)
            stackl.append(nodel.right)
            stackr.append(noder.left)

        if stackl == stackr == []:
            return True
        else:
            return False
