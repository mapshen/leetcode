class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        pre = 1
        
        if s[0] == "0":
            return 0
        elif s[0] == "*":
            cur = 9
        else:
            cur = 1
        
        n = len(s)
        for i in range(1,n):
            if s[i] == "0":
                if s[i-1]=="0":
                    return 0
                elif s[i-1]=="*":
                    cur,pre = 2*pre,cur
                elif s[i-1] == "1" or s[i-1] =="2":
                    cur,pre = pre,cur
                else:
                    return 0
            
            elif s[i] == "*":
                if s[i-1] == "0":
                    cur,pre=9*cur,cur
                elif s[i-1] == "*":
                    cur,pre=9*cur+15*pre,cur
                elif s[i-1] == "1":
                    cur,pre=9*cur+9*pre,cur
                elif s[i-1] == "2":
                    cur,pre=9*cur+6*pre,cur
                else:
                    cur,pre = 9*cur,cur
            
            elif int(s[i])<7:
                if s[i-1] == "0":
                    cur,pre = cur,cur
                elif s[i-1] == "*":
                    cur,pre = cur + 2*pre,cur
                elif s[i-1] == "1" or s[i-1] =="2":
                    cur,pre = cur + pre,cur
                else:
                    cur,pre=cur,cur
            
            else:
                if s[i-1] == "*" or s[i-1] =="1":
                    cur,pre = cur+pre,cur
                else:
                    cur,pre = cur,cur
        return cur%(10**9+7)
