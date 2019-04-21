#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:46:18 2019

@author: dwang
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) ==0 or len(matrix[0])==0:
            return 0
        result = 0
        n_row, n_col = len(matrix), len(matrix[0])
        
        c_row = [0] * n_col
        for ii in range(n_row):
            #set current row:
            for jj in range(n_col):
                if matrix[ii][jj] == '1':
                    c_row[jj] += 1
                else:    
                    c_row[jj] = 0
                    
            c_max_area = self.largestRectangleArea(c_row)
            if result < c_max_area:
                result = c_max_area
                    
        return result
    
    def largestRectangleArea(self, height):
        height.append(0) #this ensures the stacks will be cleared in the end
        stack = [-1]  #this stack is always in ascending order
        ans = 0
        for i in  range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]

                # w: the rectangle to pop out: i as the right boundary & the current stack top as the left boundary. Both the left/right boundaries not included
                w = i - stack[-1] - 1 #neat way to compute width
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans