ass Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        memo={1:[1]}
        def fN(N):
            if N not in memo:
                evens = fN(N/2)
                odds = fN((N+1)/2)
                memo[N] = [2*x-1 for x in odds]+[2*x for x in evens]
            return memo[N]
        
        return fN(N)
