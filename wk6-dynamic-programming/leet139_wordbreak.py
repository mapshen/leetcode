#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 02:52:39 2019

@author: dwang
"""
class Solution:
    #Solution #2. Time: O(s*d* (s? for string comparison)), s=len(s), d=len(wordDict)
    #This solution should be a bit faster than Solution #1, because we avoid loop from [0:end]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.result = False
        if len(s)==0 or len(wordDict)==0:
            return False
        dp = [False] * len(s) #dp[i]==True if s[0:i+1] has been segmented
        for end in range(len(s)):#explore s[0:end]
            for word in wordDict:
                if end == len(word)-1:
                    if word == s[0:end+1]:
                        dp[end] = True
                        break
                if end > len(word)-1: #there is a part of s before word
                    if word == s[end-len(word)+1:end+1] and dp[end-len(word)]:
                        dp[end] = True
                        break
        return dp[-1]
    
    #solution 1: bottom-up solution. Time: O(s*s*d), s=len(s), d=len(wordDict)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.result = False
        if len(s)==0 or len(wordDict)==0:
            return False
        dp = [False] * len(s) #dp[i]==True if s[0:i+1] has been segmented
        pos = -1
        for end in range(len(s)):#explore s[0:end]
            for begin in range(end+1):
                c_word = s[begin:end+1]
                if c_word in wordDict and (begin==0 or (begin>0 and dp[begin-1])):
                    dp[end] = True
                    break
        return dp[-1]