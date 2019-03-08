class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        while l<=r:
            m = (r-l)//2+l
            if not isBadVersion(m):
                l=m+1
            else:
                r=m-1
        return l
