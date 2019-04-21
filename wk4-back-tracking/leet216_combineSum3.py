#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:08:14 2019

@author: dwang
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k<1 or n < k:
            return []
        ans = []
        cur_subset = []
        self.backtrack(n, k, ans, cur_subset, 1)
        return ans
        
    def backtrack(self, target, kk, ans, cur_subset, start):
        """
        Based on the Backtracking template
        target:
        kk: the total number required
        ans [List(List)]: the answer
        cur_subset [List]: the current subset
        start [int]: the starting number this function searches is vec[start:9]
        Output: ans & cur_subset are shared among all recursive calls
        """
        if kk==0:#end cases
            if target == 0:
                ans.append( list(cur_subset) )
            return
        
        for ii in range(start, 10):
            cur_subset.append(ii)
            self.backtrack(target-ii, kk-1, ans, cur_subset, ii+1)
            cur_subset.pop() #backtrack
        return