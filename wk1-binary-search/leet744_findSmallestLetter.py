#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 00:47:26 2019

@author: dwang
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        for letter in letters:
            if letter > target:
                return letter
        return letters[0] # If not found