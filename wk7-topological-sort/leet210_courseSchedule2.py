#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:24:51 2019

@author: dwang
"""
#---------Solution #2, Kahn method for Topological sort -----
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses==0:
            return False
        v_inDegree = [0 for ii in range(numCourses)]# incident degree of Node i
        v_out = [[] for ii in range(numCourses)]#v_out[i] records children of node i
        
        for edge in prerequisites:
            nd1 = edge[0]  # course: nd2->nd1
            nd2 = edge[1]
            v_out[nd2].append(nd1)
            v_inDegree[nd1] += 1
            
        queue = [i for i,x in enumerate(v_inDegree) if x==0]#find nodes with no ancestor
        resultList = []
        while queue: #<=> len(queue)>0:
            cnd = queue.pop(0)
            resultList.append(cnd)
            for child in v_out[cnd]:
                v_inDegree[child] -= 1
                if v_inDegree[child] == 0:
                    queue.append(child)
        
        return resultList if len(resultList) == numCourses else []
    
#-----------Solution 1: DFS -------    
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ndOrderList = [] #output order list
        #build adjacency list:
        graphList = [[] for x in range(numCourses)]
        
        len_preList = len(prerequisites)
        for ii in range(len_preList):
            ndTo = prerequisites[ii][0]
            ndFrom = prerequisites[ii][1]
            graphList[ndFrom].append(ndTo)
        #Finish building adjacent list
        
        ndLabel = [0] * numCourses #0:white, 1:grey, 2:black
        
        for ii in range(numCourses):
            if ndLabel[ii] == 0:
                if not self.DFS(graphList, ii, ndLabel, ndOrderList):
                    ndOrderList = []
                    return ndOrderList
        return ndOrderList
    
    def DFS(self, graphList, node, ndLabel, ndOrderList):
        """
        Depth-first search
        graphList: an adjacency list
        ndOrderList: the output course order list 
        return: False if we find a cycle in the graph, otherwise True
        """
        ndLabel[node] = 1 #set node label to grey
        for next_nd in graphList[node]:
            if ndLabel[next_nd] == 0: 
                if not self.DFS(graphList, next_nd, ndLabel, ndOrderList):
                    return False
            elif ndLabel[next_nd] == 1: #a grey node means we find a cycle
                return False
            elif ndLabel[next_nd] == 2:#find a black node (which has been added to the output list), do nothing
                pass
        else:#leaf node, or all its child nodes have been visited
            ndLabel[node] = 2 #set to black
            ndOrderList.insert(0, node)
        return True