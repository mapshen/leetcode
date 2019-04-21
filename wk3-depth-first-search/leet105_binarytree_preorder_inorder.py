#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:37:22 2019

@author: dwang
"""

class Solution:
#---Method #1, Recursive DFS solution, fast:creating tree on the fly--
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            #preorder is Left-root-Right, so we can build left tree first
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root    
#---Method #2, same as above, use a dict to pass the inorder argument faster
   def buildTree(self, preorder, inorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}
        return self.dfs_helper(inorder_map, preorder, 0, len(inorder) - 1)
    
    def dfs_helper(self, inorder_map, preorder, left, right):
        '''
        left/right: this pass searches inorder[left:right]
        '''
        if not preorder : return
        node = preorder.pop(0)
        root = TreeNode(node)
        root_index = inorder_map[node]
        if root_index != left:
            root.left = self.dfs_helper(inorder_map, preorder, left, root_index - 1)
        if root_index != right:
            root.right = self.dfs_helper(inorder_map, preorder, root_index + 1, right)
        return root
         
#------My iterative solution. Slow because each node needs to traverse tree depth
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return []
        dic_inorder = dict()
        for ii, val in enumerate(inorder):
            dic_inorder[val] = ii #val:position
        
        root = TreeNode(preorder[0])
        for ii in range(1, len(preorder)):
            self.insert_node(root, preorder[ii], dic_inorder)
        return root
    
    def insert_node(self, root, val, dic_inorder):
        new_node = TreeNode(val)
        cur_node = root
        while True:
            if dic_inorder[val] < dic_inorder[cur_node.val]:#insert into the left subtree
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = new_node
                    return
            else: #insert into the right subtree
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = new_node
                    return