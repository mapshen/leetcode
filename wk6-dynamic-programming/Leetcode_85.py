class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        def helper(hist):

            if not hist:
                return 0
            
            height=[hist[0]]
            position=[0]
            length=len(hist)
            max_area=0
            
            for i in range(1,length):
                
                if hist[i] > height[-1]:
                    height.append(hist[i])
                    position.append(i)
                    
                elif hist[i] < height[-1]:
                    pos_index=0
                    while height and hist[i] < height[-1]:
                        pos_index= position.pop()
                        max_area = max(height.pop()*(i-pos_index), max_area )
                    height.append(hist[i])
                    position.append(pos_index)
            
            while height:
                max_area = max(max_area,height.pop()*(length-position.pop()))
            
            return max_area
        
        if not matrix:
            return 0
        max_area=0
        m,n=len(matrix),len(matrix[0])
        hist = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    hist[j] +=1
                else:
                    hist[j] =0
            max_area = max(max_area,helper(hist))
        return max_area
