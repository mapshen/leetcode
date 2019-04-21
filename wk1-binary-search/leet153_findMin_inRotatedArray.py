#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 01:08:43 2019

@author: dwang
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right-1:
            mid = left + (right - left) // 2 #mid== left at most
            
            #if the array is sorted,ie, the pivot point was chosen in the last round
            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            else:#continue searching for pivot point:
                if nums[left] <= nums[mid]: #left half sorted, drop it
                    left = mid
                elif nums[mid] <= nums[right]:
                    right = mid
        else:#now left==right-1, ie, 2 numbers left
            return nums[left] if nums[left]<nums[right] else nums[right]