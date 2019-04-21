#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 01:33:35 2019

@author: dwang
"""
def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """        
    dp = 1, one.get(s[:1], 0)
    
    for i in xrange(1, len(s)):
        dp = dp[1], (one.get(s[i], 0) * dp[1] + two.get(s[i-1: i+1], 0) * dp[0]) % 100000003
    
    return dp[-1]
