#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:57:55 2019

@author: dwang
"""
# Definition for a binary tree node.
# In[1 ]:
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
# In[2]: Answer #3, recursive method
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None: #empty tree
            return True
        if root.left==None and root.right==None: #only 1 node
            return True
        
        return self.Compare2Tree(root.left, root.right)
    
    def Compare2Tree(self, nd_left, nd_right):
        if nd_left==None and nd_right==None:
            return True
        elif nd_left==None or nd_right==None:#here 1tree is none, the other not
            return False
        else:#Now both trees are non-empty
            if nd_left.val != nd_right.val:
                return False
            else:
                #if any pair of sub-trees are unequal, return false
                if self.Compare2Tree(nd_left.left, nd_right.right) == False:
                    return False
                if self.Compare2Tree(nd_left.right, nd_right.left) == False:
                    return False
        
        return True #otherwise, return true (all subtrees equal, both roots equal)
            
# In[ 3]: Answer #2, iterative method
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left==None and root.right==None:
            return True
        nd = root
        que = [nd.left, nd.right]
        while len(que)>0:
            nd1 = que.pop(0)
            nd2 = que.pop(0)
            
            #Compare nd1 and nd2:
            if nd1==None and nd2==None:
                continue
            if nd1==None or nd2==None:
                return False
            if nd1.val != nd2.val:
                return False
            
            #If reaches here, both nodes are non-empty. 
            #Add a pair of child nodes each time
            if nd1.left!=None or nd2.right!=None:
                que.append(nd1.left)
                que.append(nd2.right)
            if nd1.right!=None or nd2.left!=None:
                que.append(nd1.right)
                que.append(nd2.left)
         
        return True   
         
# In [3] : Answer #1, bad        
#class Solution:
#    def isSymmetric(self, root):
#        """
#        :type root: TreeNode
#        :rtype: bool
#        """
#        if not root:
#            return True
#        list_this = [root]
#        list_next = []
#        while 1:
#            if not self.symmList(list_this):
#                return False
#            list_next = []
#            reachLeafLayer = True
#            for nd in list_this:
#                if nd == None:
#                    list_next.append(None)
#                    list_next.append(None)
#                else:
#                    list_next.append(nd.left)
#                    list_next.append(nd.right)
#                    if nd.left != None or nd.right!=None:
#                        reachLeafLayer = False
#            if reachLeafLayer:#here list_next is all Nones:
#                break
#            else:
#                #list_this = list_next.copy()#!!Must copy List in python, otherwise point to the same memory
#                list_this = list_next
#        return True
#        
#    def symmList(self, vv):
#        """
#        check if the list is symmetric
#        """
#        lst = []
#        for iv in vv:
#            if iv==None:
#                lst.append(None)
#            else:
#                lst.append(iv.val)
#                
#        if len(lst)<=1:
#            return True
#        else:
#            sz = int(len(lst)/2)
#            for ii in range(0, sz):
#                if lst[ii] != lst[-ii-1]:
#                    return False
#            return True    