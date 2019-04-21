#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 00:40:07 2019

@author: dwang
"""

import heapq
from collections import defaultdict
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix)==0 or k<=0:
            return -1
        nn = len(matrix)
        heap1 = [(matrix[0][0], 0, 0)] #heap1
        cnt = 0
        while cnt < k:
            (val, ii, jj) = heapq.heappop(heap1)
            if jj+1 <= nn-1:
                heapq.heappush(heap1, (matrix[ii][jj+1], ii, jj+1)) 
            if ii+1 <= nn-1 and jj==0:
                heapq.heappush(heap1, (matrix[ii+1][jj], ii+1, jj)) 
            cnt += 1
        return val