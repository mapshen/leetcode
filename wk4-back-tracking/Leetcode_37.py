class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def check(board,i,j,num):
            #print i,j,num
            for l in range(9):
                if board[l][j] == str(num) and l != i:
                    return False
                if board[i][l] == str(num) and l!=j:
                    return False
            x,y=i//3,j//3
            for l in range(3):
                for m in range(3):
                    if board[x*3+l][y*3+m] == str(num) and x*3+l != i and y*3+m!=j:
                        return False
            return True
        
        result=[]
        stack = []
        for i in range(9):
            for j in range(9):
                if board[i][j] ==".":
                    stack.append([i,j])
                    
        def dfs(board,temp,index,stack):
           
            if index == len(stack):
                return
            
            [x,y] = stack[index]
            for i in range(9):
                #print x,y
                if check(board,x,y,i+1):
                    #print "in"
                    temp[x][y] = str(i+1)
                    dfs(board,temp,index+1,stack)
                    temp[x][y] = "."
        
        temp = board
        dfs(board,temp,0,stack)


