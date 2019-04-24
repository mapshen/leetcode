#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 02:52:19 2019

@author: dwang
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) < 1:
            return False
        col = len(matrix[0])-1
        row = 0
        while (col >= 0 and row <= len(matrix)-1):
            if(target == matrix[row][col]) :
                return True
            elif (target < matrix[row][col]):
                col -= 1
            elif(target > matrix[row][col]):
                row += 1
        return False