#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 01:49:30 2019

@author: dwang
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empty_list = []
        for ii in range(9):
            for jj in range(9):
                if board[ii][jj] == '.':
                    empty_list.append([ii, jj])
        self.backtrack(board, empty_list, 0)
        
    def backtrack(self, board, empty_list: List[List], pos:int) -> bool:
        '''
        return true only if finding the final solution, otherwise return false
        empty_list: each item is a 2x1 [row,col] list.
        pos: the position of empty_list we are solving in this function call
        '''
        if pos == len(empty_list): #finish the whole board, end case
            return True
        row, col = empty_list[pos]
        block_row = row // 3
        block_col = col // 3
        
        for nn in ['1','2','3','4','5','6','7','8','9']:
            if self.is_in_row(board,row,nn) or self.is_in_column(board, col, nn) or self.is_in_block(board, block_row, block_col, nn):
                continue
            board[row][col] = nn
            if self.backtrack(board, empty_list, pos+1)==True: #move 1 step forward
                return True
            board[row][col] = '.' #reset current row/col before we backtrack
        return False #backtrack step
    
    def is_in_row(self, board, row, num) -> bool:
        return ( num in board[row] )
    
    def is_in_column(self, board, col, num) -> bool:
        cur_col = [board[ii][col] for ii in range(9)]
        return ( num in cur_col )
    
    def is_in_block(self, board, block_row, block_col, num) -> bool:
        '''
        block_row/block_col: range from [0,1,2]
        '''
        block = [] #9x1 list
        row_begin, col_begin = block_row*3, block_col * 3
        block += board[row_begin][col_begin:(col_begin+3)]
        block += board[row_begin+1][col_begin:(col_begin+3)]
        block += board[row_begin+2][col_begin:(col_begin+3)]
        return (num in block)
    
    def isValid_list(self, list_str: List[str]) -> bool:
        '''
        check whether a list of string is valid
        '''
        vv = [ss for ss in list_str if ss!='.']
        return len(set(vv)) == len(vv)