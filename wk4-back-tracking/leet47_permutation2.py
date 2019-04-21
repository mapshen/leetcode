#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 01:46:34 2019

@author: dwang
"""
#-------Solution #2, backtracking---
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        nums.sort()
        ans = [] 
        cur_soln = []
        used = [False for ii in range(len(nums))]
        self.backtrack(nums, cur_soln, ans, used)
        return ans
        
    def backtrack(self, nums, cur_soln, ans, used):
        """
        cur_soln (type List): the current partial candiate solution
        ans (type List[List]): the answer
        used (type List): record whether nums[ii] has been used
        Output: cur_soln and ans are modified and shared among recursive calls.
        """
        if len(cur_soln) == len(nums):#end case
            list_copy = cur_soln.copy()
            ans.append(list_copy)#must append a copy, because cur_soln keeps changing
            return
        
        for ii in range(len(nums)):#pick ii for the current partial solution's head
            if used[ii] or (ii>0 and nums[ii]==nums[ii-1] and not used[ii-1]):
                continue
            
            cur_soln.append(nums[ii])#iteratively add nums[ii] into cur_soln
            used[ii] = True
            
            self.backtrack(nums, cur_soln, ans, used) #1 more step of depth search
            
            cur_soln.pop()#backtrack    
            used[ii] = False
        return

#-------Solution #1, iteratively inserting numbers
#class Solution:
#    def permuteUnique(self, nums):
#        vv = nums
#        vv.sort()
#        nn = len(vv)
#        if nn==0:
#            return []
#        perms = [[vv[0]]]#saves permutations up to (ii-1)th iteration
#        for ii in range(1,nn):#add 1 item each time
#            cval = vv[ii]
#            new_perm = []
#            for ss in perms: #ss is a list
#                for jj in range(len(ss), -1, -1):
#                    entry = ss[:jj] + [cval] + ss[jj:] #insert [j-1, cval, j]
#                    new_perm.append(entry)
#                    if cval == ss[jj-1]:
#                        break #ensure increasing order of new permutation
#            perms = new_perm
#        return perms

if __name__ == '__main__':
    s = Solution()
    vec = [1,1,1,2]
    ans= s.permuteUnique(vec)
    print(ans)