class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
	
	def dfs(number_abb,abb_length,index):
	    if abb_length >= n:
	        return 
	    
	    if index == n:
	        if not any(number_abb & w == number_abb for w in new_dict):
	            res.append([number_abb,abb_length])
	        return
	    
	    dfs((number_abb<<1)+1,abb_length+1,index+1)
	    if abb_length ==0 or number_abb&1:
	        for i in range(1,n-index+1):
	            dfs(number_abb<<i,abb_length+1,index+i)

		def word_num(word,target):
		    res= 0
		    for i in range(n):
		        res<<=1
		        res+= target[i] == word[i]
		    return res

		def num_word(num):
		    res =''
		    count = 0
		    for i in range(n):
		        if num & (1<<n-i-1):
		            if count:
		                res += str(count)
		                count =0
		            res += target[i]
		        else:
		            count+= 1
		    return res+str(count or '')
	
		n = len(target)
		res= [[(1<<n)-1,n]]

		new_dict = [word_num(word,target) for word in dictionary if len(word) == n]

		dfs(0,0,0)
		final = target
		res_len = n
		for i in range(len(res)):
	    		if res[i][1] < res_len:
	        		final = num_word(res[i][0])
	        		res_len = res[i][1]

		return final	





