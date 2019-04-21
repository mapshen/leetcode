#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 00:11:07 2019

@author: dwang
"""
#-----Solution 3: backtracking, concise -----
class Solution: 
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        cur_subset = []
        self.backtrack(nums, ans, 0, cur_subset)
        return ans
    
    def backtrack(self, nums, ans, start, cur_subset):
        """
        nums [list]: sorted num vector
        ans [List(List)]: the result, all subsets
        start [int]: this backtrack searches the range nums[start:end]
        cur_subset [list]: the current subset
        """
        #no need for nd case, because start will bypass the following for loop
        ans.append( list(cur_subset) )
        for ii in range(start, len(nums)):
            #iterative pick the next item to add to subset
            if ii>start and nums[ii-1]==nums[ii]:
                continue #key
            cur_subset.append(nums[ii])
            self.backtrack(nums, ans, ii+1, cur_subset)
            cur_subset.pop() #backtrack step!
            #alternatively, pass a temporary cur_subset below. No need to backtrack, but more memory
            #self.backtrack(nums, ans, ii+1, cur_subset+[nums[ii]], used)
        return
    
#-----Solution 2: backtracking -----
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        nums.sort()
        ans = []
        cur_subset = []
        used = [False for ii in range(len(nums))]
        self.backtrack(nums, ans, 0, cur_subset, used)
        return ans
    
    def backtrack(self, nums, ans, start, cur_subset, used):
        """
        nums [list]: sorted num vector
        ans [List(List)]: the result, all subsets
        start [int]: this backtrack searches the range nums[start:end]
        cur_subset [list]: the current subset
        used [list]: mark if nums[i] has been used or not
        """
#        if pos == len(nums): #end of recursion
#            return
        ans.append( list(cur_subset) )
        for ii in range(start, len(nums)):
        #iterative pick the next item to add to subset
            if (ii>start and nums[ii-1]==nums[ii] and not used[ii-1]):
                continue #key
            cur_subset.append(nums[ii])
            used[ii] = True
            self.backtrack(nums, ans, ii+1, cur_subset, used)
            cur_subset.pop()
            used[ii] = False
        return
    
#----My Solution #1, iteratively add items to subsets--------------------
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        vv = nums
        nn = len(vv)
        if nn == 0:
            return []
        vv.sort()
        subset = [ [],[vv[0]] ] 
        prev_subset = subset[1:]
        for ii in range(1,nn):
            new_subset = []
            if vv[ii] == vv[ii-1]:
                for qq in prev_subset:
                    new_subset.append( qq + [vv[ii]])
            else:
                for ss in subset:#regular new item, replicate the whole subset
                    new_subset.append(ss + [vv[ii]])
            subset += new_subset
            prev_subset = new_subset
        return subset

if __name__ == '__main__':
    s = Solution()
    vec = [1,2,2]
    ans= s.subsetsWithDup(vec)