#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:10:39 2019

@author: dwang
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)<=1 or k<=0:
            return 0
        if k> (len(prices)//2):#we can do at most n_day/2 transactions. If k is more than this, capture all the price inreases
            return self.buy_as_many(prices)
        
        v_buy = [1e10] * k #the cost of j-th buy-in
        v_sell = [0] * k #profit of j-th sell-out
        result = 0
        for ii in range(len(prices)):
            cp = prices[ii]
            for jj in range(k): #each j-th buy/sell
                if jj == 0:
                    v_buy[jj] = min(v_buy[jj], cp)
                else:
                    #cost of j-th buy-in, discounted by the profit from (j-1)th sell-out
                    v_buy[jj] = min(v_buy[jj], cp - v_sell[jj-1])
                v_sell[jj] = max(v_sell[jj], cp - v_buy[jj])
           
        return v_sell[-1]
    
    def buy_as_many(self, prices: List[int]) -> int:
        profit = 0
        for ii in range(1, len(prices)):
            if prices[ii] > prices[ii-1]:
                profit += prices[ii] - prices[ii-1]
        return profit