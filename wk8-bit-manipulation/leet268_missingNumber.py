#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:25:55 2019

@author: dwang
"""
#Solution #1: easy to understand
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) #total numbers should be 0,1,..n
        a = 0
        for ii in range(n):
            a = a ^ ii
            a = a ^ nums[ii]
        if a == 0:#here n is the missing value.The first n-1 numbers cancel out
            return n
        else:#here a = n xor missing_value
            result = a ^ n
            return result

#Solution #2: 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) #total numbers should be 0,1,..n
        if n == 0:
            return 0
        if n == 1:
            return 1-nums[0]
        k = 1
        while k <= n:
            k *=2
        result = 0
        for ii in nums:
            result = result ^ ii
        for ii in range(n+1,k):
            result = result ^ ii
        return result