#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:25:41 2019

@author: dwang
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sz1 = len(nums1)
        sz2 = len(nums2)
        
        p1, p2, pos = 0, 0, 0
        
        mid = (sz1+sz2)//2 #goal: median = final_array[mid]
        val = 0    
        while pos <= mid: #each pass gets final_array[pos]. I find this is a better way to track position in arrays
            val_last = val
            if p1 == sz1:#nums1 finished
                val = nums2[p2]
                p2 += 1
            elif p2 == sz2:
                val = nums1[p1]
                p1 += 1
            else:#pick the smaller one among the two arrays
                if nums1[p1] < nums2[p2]:
                    val = nums1[p1]
                    p1 += 1 #take one from array1
                else:
                    val = nums2[p2]
                    p2 += 1
            pos += 1    
        return val if (sz1+sz2)%2 == 1 else (val+val_last)/2.0 
        