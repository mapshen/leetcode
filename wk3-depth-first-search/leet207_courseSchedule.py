#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:48:46 2019

@author: dwang
"""
  from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses==0:
            return False
        v_inDegree = [0 for ii in range(numCourses)]# incident degree of Node i
        v_out = [[] for ii in range(numCourses)]#v_out[i] records children of node i
        
        #Build the graph
        for edge in prerequisites:
            nd1 = edge[0]  # course: nd2->nd1
            nd2 = edge[1]
            v_out[nd2].append(nd1)
            v_inDegree[nd1] += 1
            
        queue = [i for i,x in enumerate(v_inDegree) if x==0]#find nodes with no ancestor
        cnt_finishedNode = 0
        while queue: #<=> len(queue)>0:
            cnd = queue.pop(0)
            cnt_finishedNode += 1
            for child in v_out[cnd]:
                v_inDegree[child] -= 1
                if v_inDegree[child] == 0:
                    queue.append(child)
        
        return cnt_finishedNode == numCourses
