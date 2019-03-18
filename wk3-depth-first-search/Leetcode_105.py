class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            curnode = preorder.pop(0)
            root = TreeNode(curnode)
            root_index = inorder.index(curnode)
            root.left = self.buildTree(preorder,inorder[:root_index])
            root.right = self.buildTree(preorder,inorder[root_index+1:])
            return root
