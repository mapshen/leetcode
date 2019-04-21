#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 02:21:33 2019

@author: dwang
"""
#My solution #2: no arrays-----------
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0] #at step i, keep the max by num[i-1]
        c_max = nums[0]#at step i, the max product ending in n[i]
        c_neg = nums[0] #at step i, the min (most negative) value ending in n[i]
        result = nums[0]
        for ii in range(1, len(nums)):
            if nums[ii] > 0:
                c_max = max(prev_max*nums[ii], nums[ii])
                c_neg = min(c_neg, c_neg*nums[ii])
            elif nums[ii] < 0:
                c_max = max(nums[ii], c_neg*nums[ii])
                c_neg = min(prev_max*nums[ii], nums[ii])
            else: #num[ii] == 0
                c_neg = c_max = 0
            prev_max = c_max    
            if result < c_max:#this is key!
                result = c_max
        return result
#Solution #1---------
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p_plus = [1] * len(nums)
        p_plus[0] = nums[0]
        c_neg = nums[0]
        result = nums[0]
        for ii in range(1, len(nums)):
            if nums[ii] > 0:
                p_plus[ii] = max(p_plus[ii-1]*nums[ii], nums[ii])
                c_neg = min(c_neg, c_neg*nums[ii])
            elif nums[ii] < 0:
                p_plus[ii] = max(nums[ii], c_neg*nums[ii])
                c_neg = min(p_plus[ii-1]*nums[ii], nums[ii])
            else: #num[ii] == 0
                c_neg = p_plus[ii] = 0
                
            if result < p_plus[ii]:
                result = p_plus[ii]
        return result