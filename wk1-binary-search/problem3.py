class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l = 0
        r = len(letters) - 1
        while l <= r:
            m = (r-l)//2 + l
            if letters[m] <= target:
                l = m+1
            else:
                r = m-1
        if l > len(letters) -1:
            return letters[0]
        return letters[l]
