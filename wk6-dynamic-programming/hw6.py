#85. Maximal Rectangles 
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        height = [0] * N
        res = 0
        for row in matrix:
            for i in range(N):
                if row[i] == '0':
                    height[i] = 0
                else:
                    height[i] += 1
            res = max(res, self.maxRectangleArea(height))
        return res            
            
    def maxRectangleArea(self, height):
        if not height: return 0
        res = 0
        stack = list()
        height.append(0)
        for i in range(len(height)):
            cur = height[i]
            while stack and cur < height[stack[-1]]:
                w = height[stack.pop()]
                h = i if not stack else i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)
        return res

#188.Best Time to Buy and Sell Stock IV
    def maxProfit(self, k, prices):
        n = len(prices)
        # avoid MemoryError
        if k >= (n>>1):
            return self.buyAsMany(prices)
        dp = [[0] * n for _ in range(k+1)]
        for i in range(1, k+1):
            # reduce O(knn) to O(kn)
            tmp = -prices[0]
            for j in range(1, n):
                # sell or not sell
                dp[i][j] = max(dp[i][j-1], prices[j]+tmp)
                tmp = max(tmp, dp[i-1][j-1]-prices[j])
        return dp[k][n-1]
    
    def buyAsMany(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            # sell only if price increased
            profit += max(0, prices[i]-prices[i-1])
        return profit


#139. Word Break
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp.pop()

#152. Maximum Product Subarray
# Non DP solution
    def maxProduct(self, nums: List[int]) -> int:
        # the subarray has no zero
        # and even number of negs 
        # this solution beats 99.92%, but not DP
        if len(nums) <= 1:
            return 0 if len(nums) == 0 else nums[0]
        sumNeg = 0
        firstNeg = -1
        lastNeg = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                return max(0, self.maxProduct(nums[:i]), self.maxProduct(nums[i + 1:]))
            if nums[i] < 0:
                sumNeg += 1
                if firstNeg == -1:
                    firstNeg = i
                lastNeg = i
        if sumNeg % 2 == 0:
            return self.getProd(nums)
        else:
            return max(self.getProd(nums[:firstNeg]), self.getProd(nums[firstNeg + 1:]), self.getProd(nums[:lastNeg]), self.getProd(nums[lastNeg + 1:]))   

# DP solution
    def maxProduct(self, nums: List[int]) -> int:
        max_now = min_now = max_all = nums[0]
        for i in range(1, len(nums)):
            tmp = max_now
            max_now = max(min_now*nums[i], max_now*nums[i], nums[i])
            min_now = min(min_now*nums[i], tmp*nums[i], nums[i])
            max_all = max(max_all, max_now)
        return max_all

# 213. House Robber II
    def rob1(self, nums):
        if len(nums) <= 0:
            return 0 if len(nums) == 0 else nums[0]
        max_gain = [0]*(len(nums) + 1)
        last = 0
        for i in range(1, len(nums) + 1):
            if last == 0:
                max_gain[i] = max_gain[i - 1] + nums[i - 1]
                last = 1
            else:
                max_gain[i] = max(max_gain[i - 1], max_gain[i - 2] + nums[i - 1])
        return max_gain[-1]
    
    def rob(self, nums):
        n = len(nums)
        if n <= 2:
            if n == 0:
                return 0
            else:
                return nums[0] if n == 1 else max(nums)
        return max(self.rob1(nums[:n - 1]), self.rob1(nums[1:])) 

# 639. Decode Ways II
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        prevprev, prev, curr = 1, 0, 0 
        
        if s[0] == '0':
            return 0
        else:
            if s[0] == '*':
                curr = prev = 9
            else:
                curr = prev = 1
        
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] == '*':
                    curr = prevprev * 2
                elif s[i - 1] in'12':
                    curr = prevprev
                else:
                    return 0
            elif s[i] == '*':
                if s[i - 1] == '0':
                    curr = prev * 9 
                elif s[i - 1] == '*':
                    curr = prev * 9  + prevprev * 15
                elif s[i - 1] == '1':
                    curr = prev * 9 + prevprev * 9
                elif s[i - 1] == '2':
                    curr = prev * 9 + prevprev * 6
                else:
                    curr = prev * 9
            else:
                if s[i - 1] == '0':
                    curr = prev
                elif s[i - 1] == '*':
                    curr = prev
                    if s[i] in '123456':
                        curr += prevprev * 2
                    else:
                        curr += prevprev
                elif s[i - 1] == '1':
                    curr = prev + prevprev
                elif s[i - 1] == '2':
                    if s[i] in '123456':
                        curr = prev + prevprev
                    else:
                        curr = prev
            prev, prevprev = curr, prev
        return curr % (10**9 + 7) 
