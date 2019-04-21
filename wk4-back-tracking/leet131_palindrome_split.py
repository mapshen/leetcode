#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:53:08 2019

@author: dwang
"""
class Solution:
#----Online solution, good--------
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s: str, path: List[str], res):
        '''
        s: the remaining part to be examined
        path: the already-made partition
        '''
        if not s:#end case.
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                #1 further step. Note: here we create a new path variable, rather than reusing the same memory
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]    
    
#-----My solution, cumbersome-------------
    def partition(self, s: str) -> List[List[str]]:
        result = []
        if len(s) >0:
            cur_split = [s]
            self.backtrack(result, cur_split)
        return result
    
    def backtrack(self, result: List[List], cur_split: List[str]):
        if self.is_split_good(cur_split):
            result.append(cur_split)
        if len(cur_split[-1]) == 1: #end case. The last part of the split is one letter
            return
        last_str = cur_split[-1]
        for ii in range(1, len(last_str)): #split the last partition (at position ii)
            if self.is_palindrome(last_str[:ii]):
                new_split = cur_split[:-1] + [last_str[:ii], last_str[ii:]]
                self.backtrack(result, new_split)
        return
        
    def is_palindrome(self, ss: str):
        return ss == ss[::-1]
    
    def is_split_good(self, split: List[str]):
        for ss in split:
            if not self.is_palindrome(ss):
                return False
        return True