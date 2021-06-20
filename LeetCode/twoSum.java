class Solution {
  public int[] twoSum(int[] nums, int target){
      int[] output = new int[2];
      if(nums == null || nums.length <= 1)
          return output;
      HashMap<Integer,Integer> map  = new HashMap<Integer,Integer>();
      for(int i = 0;i < nums.length;i++){
          int difference = target - nums[i];
          if(map.containsKey(difference)) {
              output[0] = map.get(difference);
              output[1] = i;
              return output;
          } else {
              map.put(nums[i], i);
          }
      }
      return output;
  }

}
