#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 00:39:00 2019

@author: dwang
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        if len(nums)<=3:
            return max(nums)
        #now len(nums)>=4:
        #2 dp array: the max money when we visit n[i]
        dp = [0] * len(nums) #we must take n[0], not n_last
        dp2 = list(dp) #must not take n[0], may or maynot take n_last
        
        dp[0] = dp[1] = nums[0]
        dp[2] = nums[0] + nums[2]
        dp2[0] = 0
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        
        #loop until n[-2]. Both dp/dp2 follow the same simple rule
        for ii in range(3, len(nums)-1):
            dp[ii] = max(dp[ii-1], dp[ii-2]+nums[ii])
            dp2[ii] = max(dp2[ii-1], dp2[ii-2]+nums[ii])
        #dp/dp2 pick the last item differently. dp[-1]==dp[-2] since we must not take the n_last, whereas dp2[-1] may take n_last.     
        dp[len(nums)-1] = dp[-2]
        dp2[len(nums)-1] = max(dp2[-2], dp2[-3]+nums[-1])
        return max(dp[-1], dp2[-1])
