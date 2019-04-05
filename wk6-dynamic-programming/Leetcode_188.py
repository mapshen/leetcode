class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k==0:
            return 0
        
        n = len(prices)
        
        if k>=n/2:
            ans=0
            for i in range(1,n):
                if prices[i] > prices[i-1]:
                    ans += prices[i] - prices[i-1]
            return ans
        
        b = [prices[0]] * k
        s = [0] * k
        
        for i in range(1,n):
            if prices[i] < b[0]:
                b[0] = prices[i]
            if prices[i]-b[0] > s[0]:
                s[0] = prices[i] - b[0]
                
            for j in range(1,k):
                if prices[i] - s[j-1] < b[j]:
                    b[j] = prices[i] - s[j-1]
                    
                if prices[i] - b[j] > s[j]:
                    s[j] = prices[i] - b[j]
        return s[-1]
