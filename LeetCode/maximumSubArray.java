class Solution {
    public int maxSubArray(int[] nums) {
        int sum_till_now = 0;
        int max_sum = Integer.MIN_VALUE;
        for(int num: nums){
            sum_till_now += num;
            if(num > sum_till_now){
             sum_till_now = num;
            }
            max_sum = Math.max(sum_till_now,max_sum);
        }
        return max_sum;
    }
}
