#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:43:51 2019

@author: dwang
"""

#Solution:
from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []
        cur_layer = deque([root])
        while len(cur_layer)>0:
            head_val = cur_layer[0].val
            next_layer = deque([])
            for ii in range(len(cur_layer)):
                cur_node = cur_layer.popleft()
                if cur_node.left != None:
                    next_layer.append(cur_node.left)
                if cur_node.right != None:
                    next_layer.append(cur_node.right)
                    
            cur_layer = next_layer
        return head_val