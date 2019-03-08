class Solution(object):

                
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix[0])
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        def count(matrix,target):
            l=0
            r=len(matrix)-1
            while l<=r:
                m = (r-l)//2+l
                if matrix[m]<=target:
                    l = m +1
                else:
                    r = m -1
            return l
        
        while l<=r:
            m = (r-l)//2+l
            con = 0
            for i in range(n):
                con+=count(matrix[i],m)
            if con>=k:
                r = m-1
            else:
                l=m+1
        return l
