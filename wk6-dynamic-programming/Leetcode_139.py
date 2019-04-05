class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        
        temp = [0]*(n+1)
        temp[0] = 1
        for i in range(n):
            for j in range(0,i+1):
                if s[j:i+1] in wordDict and temp[j] ==1:
                    temp[i+1] =1
                    break
        #print temp
        if temp[-1] == 1:
            return True
        return False
                
