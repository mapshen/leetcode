#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 00:29:12 2019

@author: dwang
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
 
        r = n-1
        l = 0
        while(l<=r):
            mid = l + (r-l)//2
            if isBadVersion(mid)==False:
                l = mid+1
            else:
                r = mid-1
        return l