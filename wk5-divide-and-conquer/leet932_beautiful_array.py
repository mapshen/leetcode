#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 02:57:39 2019

@author: dwang
"""

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        res = [1]
        while len(res) < N:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        return [i for i in res if i <= N]