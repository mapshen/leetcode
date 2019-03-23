# 101. Symmetric Tree
# DFS
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        sl = [root]
        sr = [root]
        lp = root.left
        rp = root.right

        while(lp or sl or rp or lp):
            if not lp and rp or rp and not lp:
                return False
            if lp and rp:
                if lp.val != rp.val:
                    return False
                sl.append(lp)
                sr.append(rp)
                lp = lp.left
                rp = rp.right
            else:
                lp = sl.pop().right
                rp = sr.pop().left
        return True

# 105. Construct Binary Tree from Preorder and Inorder Traversal
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        inorder_dict = dict(zip(inorder, range(len(inorder))))
        curr = 0
        def helperFunc(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None
            root_val = preorder[curr]
            root = TreeNode(root_val)
            inorder_curr = inorder_dict[root_val]
            preorder.pop(0)
            root.left = helperFunc(inorder_left, inorder_curr - 1)
            root.right = helperFunc(inorder_curr + 1, inorder_right)
            return root
        return helperFunc(0, len(inorder) - 1)

# 113. Path Sum II
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        if root == None:
            return []

        res = []
        def dfs(node, val, node_list):
            if node.left == None and node.right == None and node.val + val == sum:
                node_list.append(node.val)
                res.append(node_list)
                node_list = []
            if node.left or node.right:
                node_list.append(node.val)
                if node.left:
                    dfs(node.left, val + node.val, node_list.copy())
                if node.right:
                    dfs(node.right, val + node.val, node_list.copy())
        dfs(root, 0, [])
        return res

# 207. Course Schedule
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for i in range(numCourses)]
        visit = [0]*numCourses
        for i in prerequisites:
            pre[i[0]].append(i[1])
        
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in pre[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
# 980 Unique paths iii
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.res = 0
        empty = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    empty += 1
        
        def dfs(x, y, empty):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < 0 :
                return
            if (x, y) == end:
                if empty == 0:
                    self.res += 1
                return
            
            grid[x][y] = -2 # visited
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            grid[x][y] = 0
            
        dfs(x, y, empty)
        return self.res
# 988. Smallest String Starting From Leaf
    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        def val_to_letter(n):
            return chr(n + ord('a'))
        
        all_str = []
        
        def dfs(node, strlist):
            if node == None:
                return 
            if node.left == node.right == None:
                all_str.append((strlist + val_to_letter(node.val))[::-1])
                return
            else:
                strlist = strlist + val_to_letter(node.val)
                dfs(node.left, strlist)
                dfs(node.right, strlist)
        dfs(root, '')
        
        return min(all_str) 
