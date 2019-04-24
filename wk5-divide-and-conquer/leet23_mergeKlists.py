#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 00:44:12 2019

@author: dwang
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists):
        #handle all kinds of [] cases
        if len(lists) == 0:
            return None
        mylists = [nd for nd in lists if nd]
        n_list = len(mylists)
        if n_list == 0:
            return None
        
        #initialize the priority heap queue
        heapque = []
        for ii in range(n_list):
            heapq.heappush(heapque, (mylists[ii].val, ii))
        
        build_head = True
        while len(heapque)> 0:
            _, pos = heapq.heappop(heapque)
            cur_nd = mylists[pos]
            if build_head:
                build_head = False
                root_nd = cur_nd
                tail_nd = cur_nd
            else:
                tail_nd.next = cur_nd
                tail_nd = cur_nd
            if cur_nd.next:
                heapq.heappush(heapque, (cur_nd.next.val, pos))
                mylists[pos] = cur_nd.next
        return root_nd
