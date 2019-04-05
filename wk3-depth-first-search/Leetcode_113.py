        result=[]
        
        def dfs(root,target,temp):
            if not root:
                return
            if root.left == root.right == None and sum(temp)+root.val==target:
                result.append(temp+[root.val])
                return
            else:
                if root.left != None:
                    dfs(root.left,target,temp+[root.val])

                if root.right != None:
                    dfs(root.right,target,temp+[root.val])
        
        dfs(root,target,[])
        return result



