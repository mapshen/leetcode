class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            
            if len(arr)>1:
                mid=len(arr)/2
                lh = arr[:mid]
                rh = arr[mid:]
                
                merge_sort(lh)
                merge_sort(rh)
                
                i,j,k=0,0,0
                while i < len(lh) and j < len(rh):
                    if lh[i] < rh[j]:
                        arr[k]=lh[i]
                        i=i+1
                    else:
                        arr[k]=rh[j]
                        j=j+1
                    k=k+1
                while i<len(lh):
                    arr[k]=lh[i]
                    i=i+1
                    k=k+1
                while j<len(rh):
                    arr[k]=rh[j]
                    j=j+1
                    k=k+1
        merge_sort(nums)
        return nums[-1*k]
