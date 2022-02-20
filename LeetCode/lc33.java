//Search element in a rotated sorted array
class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while(low <= high){
            int mid = (low + high) >> 1;
            //check if the element is found or not
            if(nums[mid] == target){
                return mid;
            }
            //check if target lies in left half
            if(nums[low] <= nums[mid]){
                if(nums[low] <= target && nums[mid] >= target){
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            //check if target lies in right half
            } else{
                if(nums[mid] <= target && nums[high] >= target){
                    low = mid + 1;
                } else{
                    high = mid - 1;
                }
            }
            
        }
        return -1;
        
    }
}
//Using binary search, run time complexity: O(log N)
