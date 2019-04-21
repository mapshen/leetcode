#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:15:19 2019

@author: dwang
"""

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        num_nodes = len(graph)
        if len(graph)==0:
            return []
        v_outDegree = [0 for ii in range(num_nodes)]
        v_ancestor = [[] for ii in range(num_nodes)]#ancestors of node i
        
        #Build 1) outbounding degree for each node, 2)each node's ancestors 
        for ii in range(num_nodes):
            v_outDegree[ii] = len(graph[ii])
            children = graph[ii]
            for eachnode in children:
                v_ancestor[eachnode].append(ii)
            
        queue = [i for i,x in enumerate(v_outDegree) if x==0]#find terminal nodes
        result = []
        while queue: 
            cnd = queue.pop(0)
            result.append(cnd)
            for parent in v_ancestor[cnd]:
                v_outDegree[parent] -= 1
                if v_outDegree[parent] == 0:
                    queue.append(parent)
        result.sort()
        return result