class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        nr,nc = len(board),len(board[0])
        queue = [click]
        while queue:
            [r,c] = queue.pop(0)
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return board
            
            count=0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if dr==dc==0:
                        continue
                    tr = r+dr
                    tc = c+dc
                    if 0<=tr<nr and 0<=tc<nc:
                        if board[tr][tc] =='M':
                            count+=1

            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = 'B'
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if dr==dc==0:
                            continue
                        tr = r+dr
                        tc = c+dc
                        if 0<=tr<nr and 0<=tc<nc:
                            if board[tr][tc] =='E':
                                board[tr][tc] = 'B'
                                queue.append([tr,tc])
        return board
