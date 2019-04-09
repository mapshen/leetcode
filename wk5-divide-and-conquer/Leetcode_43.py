class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m,n=len(num1),len(num2)
        if m>n:
            num1,num2,m,n=num2,num1,n,m
        
        result=[0]*(m+n)
        for i in range(m):
            for j in range(n):                
                tem1 = int(num1[-1*(i+1)])*int(num2[-1*(j+1)])+result[-1*(i+j+1)]
                tem2 =tem1//10+result[-1*(i+j+1)-1]
                #print result,tem1,tem2,i,j
                result[-1*(i+j+1)] = tem1%10
                result[-1*(i+j+1)-1] = tem2%10
                if tem2 >9:
                    result[-1*(i+j+1)-2] = tem2//10+result[-1*(i+j+1)-2]
        index=m+n-1
        for i in range(m+n):
            if result[i]!=0:
                index=i
                break
        if index == m+n-1 and result[index] == 0:
            return "0"
        else:
            result=result[index:]
        
        out=""
        for i in range(len(result)):
            out=out+str(result[i])
        return out
