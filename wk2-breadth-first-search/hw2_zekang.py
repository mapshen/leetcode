# 199 Binary Tree Right Side View
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        rightview = []
        thislayer = [root]
        while(len(thislayer)):
            rightview.append(thislayer[-1].val)
            layer_len = len(thislayer)
            for i in range(layer_len):
                layer_size = len(thislayer)
                if thislayer[i].left:
                    thislayer.append(thislayer[i].left)
                if thislayer[i].right:
                    thislayer.append(thislayer[i].right)

            for i in range(layer_len):
                thislayer.pop(0)
        return rightview


# 559. Maximum Depth of N-ary Tree
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        layer = [root]
        max_depth = 0
        while(len(layer)):
            max_depth += 1
            layer_size = len(layer)
            for i in range(layer_size):
                for j in range(len(layer[i].children)):
                    layer.append(layer[i].children[j])
            for i in range(layer_size):
                layer.pop(0)
        return max_depth


# 513. Find Bottom Left Tree Value
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        layer = [root]
        while(len(layer)):
            thislayer = []
            for i in layer:
                if i.left:
                    thislayer.append(i.left)
                if i.right:
                    thislayer.append(i.right)
            if thislayer:
                layer = thislayer
            else:
                return layer[0].val

# 103. Binary Tree Zigzag Level Order Traversal
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        layer = [root]
        res = []
        left = 1
        while len(layer):

            res_layer = []
            if left:
                for i in layer:
                    res_layer.append(i.val)
                res.append(res_layer)
                left = 0
            else:
                for i in layer[::-1]:
                    res_layer.append(i.val)
                res.append(res_layer)
                left = 1
            thislayer = []
            for i in layer:
                if i.left:
                    thislayer.append(i.left)
                if i.right:
                    thislayer.append(i.right)
            layer = thislayer
        return res

# 690. Employee Importance
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        id_dict = {i.id: i for i in employees}
        layer = [id_dict[id]]
        total_importance = 0
        while layer:
            thislayer = []
            for i in layer:
                total_importance += i.importance
                for j in i.subordinates:
                    thislayer.append(id_dict[j])
            layer = thislayer
        return total_importance


# 529. Minesweeper

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        (row, col), directions = click, ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                n = sum([board[row + r][col + c] == 'M' for r, c in directions if 0 <= row + r < len(board) and 0 <= col +c < len(board[0])])
                board[row][col] = str(n if n else 'B')
                for r, c in directions * (not n):
                    self.updateBoard(board, [row + r, col + c])
        return board
