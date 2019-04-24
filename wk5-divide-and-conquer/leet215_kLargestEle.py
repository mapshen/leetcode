#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 02:35:58 2019

@author: dwang
"""

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hh = []
        for nn in nums:
            hh.append(-nn)
        heapq.heapify(hh)
        #print('hh: ', hh)
        for ii in range(k-1):
             heapq.heappop(hh)
        #print('hh: ', hh)
        return -hh[0]