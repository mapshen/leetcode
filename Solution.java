// "static void main" must be defined in a public class.
public class Solution {
    public boolean search(int[] nums, int target) {
        int high = nums.length - 1;
        int low = 0;
        int mid;
        while(high>=low){
            mid=(high+low)/2;
            if (nums[mid] == target) {
                return true;
            }
            else if (nums[mid] < nums[low]) {
                if (target < nums[mid]) {
                    high = mid - 1;
                } else if (target > nums[high]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            else{
                if(target > nums[mid]){
                    low=mid+1;
                }
                else if(target < nums[low]){
                    low = mid+1;
                }
                else{
                    high = mid-1;
                }
            }
        }
        return false;
    }
}



