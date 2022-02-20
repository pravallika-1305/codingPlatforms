//Maximum Subarray = subarray with maximum sum



//Naive Approach - O(N ^ 3)
// Here, Iterate over all the subarrays and find their sums, then find maximum of these sums
// first loop for iterating over all the elements, second loop for getting subarrays, third for iterating over the subarrays

//Optimizing Naive Approach by proposing a quadratic complexity solution, 
// For this, add the sum in the second loop itself and remove the third loop.

// Kadane's Algorithm - O(N) i.e. Linear Time Complexity solution

class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int sum = 0;
        for(int num: nums){
            sum += num;
            if(sum > max) max = sum;
            if(sum < 0) sum = 0;
        }
        return max;
        
    }
}
