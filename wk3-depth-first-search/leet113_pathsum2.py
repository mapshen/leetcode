#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:35:20 2019

@author: dwang
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []
        cur_path = []
        if root:
            self.dfs_allpath(root, sum, cur_path, paths)
        return paths
        
    def dfs_allpath(self, root, target_num, cur_path, paths):
        '''
        root: current subtree
        target_num: the target sum we pursue for the current subtree
        cur_path: the path from root to the parent of current root
        '''
        if root.left == None and root.right == None:#reach leaf
            if root.val == target_num:#find a solution
                paths.append( cur_path+[root.val])
                return
        
        cur_path.append(root.val)
        if root.left:
            self.dfs_allpath(root.left, target_num-root.val, cur_path, paths)
        if root.right:
            self.dfs_allpath(root.right, target_num-root.val, cur_path, paths)
        cur_path.pop()
        return
