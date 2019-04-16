class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        graph = {'A':0,'C':1,'G':2,'T':3}
        n=len(s)
        code = 0
        
        if n<=10:
            return []
        
        for i in range(0,10):
            code = (code<<2)+graph[s[i]]
        dic =set()
        dic.add(code)
        res_code=[]
        res=[]
        for i in range(10,n):
            code = code&~(1<<19)
            code = code&~(1<<18)
            code = (code<<2) +graph[s[i]]
            if code in dic and code not in res_code:
                res.append(s[i-9:i+1])
                res_code.append(code)
            else:
                dic.add(code)
        return res
