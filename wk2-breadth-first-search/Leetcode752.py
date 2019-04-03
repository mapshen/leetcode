class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        seen=set(deadends)
        queue=['0000']
        con = 0
        while queue:
            for eachnode in range(len(queue)):
                curnode = queue.pop(0)
                if curnode == target:
                    return con
                if curnode in seen:
                    continue
                seen.add(curnode)
                queue+=(self.new(curnode))
            con+=1
        return -1
            
    def new(self,c):
        res=[]
        for i in range(4):
            res.append(c[:i]+str((int(c[i])+1)%10)+c[i+1:])
            res.append(c[:i]+str((int(c[i])-1)%10)+c[i+1:])
        return res
