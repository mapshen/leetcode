#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 01:55:44 2019

@author: dwang
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return [] 
        a = 0
        for num in nums:
            a = a ^ num
        # a = n1 xor n2, where n1/n2 are the two that appear once
        
        #find the 1st bit-1 in (n1 xor n2):
        for ii in range(32):
            if (a & (1 << ii)) !=0:
                pos = ii
                break
        else:
            print('overflow')
        
        #put nums in 2 groups, based on whether their pos-th bit is 1.
        #Then each group contains 1 single-appearance number. We can reuse the xor trick in SingleNumber I.
        n1, n2 = 0,0
        for nn in nums:
            if (nn & (1<<pos) )!=0:
                n1 = n1 ^ nn
            else:
                n2 = n2 ^ nn
        result = [n1, n2]
        return result