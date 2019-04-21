#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 00:08:14 2019

@author: dwang
"""
class Solution:
#----My solution, almost same as the concise online solution below---
    def totalNQueens(self, n: int) -> int:
        self.result = 0 #instance's member variable can be defined in any member function and shared across all member functions
        q_col, q_diag1, q_diag2 = [],[],[]
        self.backtrack(n, 0, q_col, q_diag1, q_diag2)
        return self.result
    
    def backtrack(self, nn, pos, q_col, q_diag1, q_diag2):
        '''
        nn: problem size
        pos: the starting row of the current search
        '''
        if pos == nn: #end case
            self.result+=1
            return
        
        for col in range(nn):
            #[pos,col] is a good place:
            if col not in q_col and (pos+col) not in q_diag1 and (pos-col) not in q_diag2:
                q_col.append(col)
                q_diag1.append(pos+col)
                q_diag2.append(pos-col)
                self.backtrack(nn, pos+1, q_col, q_diag1, q_diag2)
                q_col.pop()
                q_diag1.pop()
                q_diag2.pop()
        return
#------Concise online solution ------------    
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n_solution = 0
        self.DFS(n, [], [], [])
        return self.n_solution
        
    def DFS(self, n, queens, xy_dif, xy_sum):
            """
            n: the problem size
            queens: list each queen's column in each row.
            xy_dif: (x-y) values we have visited so far. This is for the main diagonal
            xy_sum (x+y) values we have visited. This is for the off diagonal
            """
            p = len(queens)#already found p queens
            if p==n:
                self.n_solution += 1
                return None
            for q in range(n):
                #p here is also the row of next candidate queen:
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    #1 q not in queens: guarantees queens not in a straight line
                    #2:p-q, p+q not in ...: guarantees queens not in diagnoal
                    self.DFS(n, queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
            return #just finish, without adding to result