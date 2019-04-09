class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        result=[]
        def dfs(s,temp):
            #print s,temp
            if not s:
                result.append(temp)
                return
            
            for i in range(len(s)):
                tem = s[:i+1]
                #print tem
                if tem == tem[::-1]:
                    dfs(s[i+1:],temp+[tem])
                
            
        dfs(s,[])
        return result
