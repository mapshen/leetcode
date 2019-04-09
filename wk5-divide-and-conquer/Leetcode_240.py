class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m,n=len(matrix)-1,len(matrix[0])-1
        i,j=0,n
        
        while i<=m and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i=i+1
            else:
                j=j-1
        return False
