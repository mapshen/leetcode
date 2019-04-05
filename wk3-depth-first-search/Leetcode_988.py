class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root,result):
            if not root:
                return
            result =  chr(root.val+97) + result
            if root.left == root.right == None:
                out.append(result)
            else:
                dfs(root.left,result)
                dfs(root.right,result)
        out=[]
        dfs(root,'')
        return min(out)
