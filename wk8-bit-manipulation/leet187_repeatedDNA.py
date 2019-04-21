#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:34:26 2019

@author: dwang
"""

from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        if len(s)<10:
            return []
        seen = defaultdict(int)
        for ii in range( len(s)-9 ):
            seen[ s[ii:ii+10] ] += 1
        
        for k, val in seen.items():
            if val >=2:
                result.append(k)
        return result