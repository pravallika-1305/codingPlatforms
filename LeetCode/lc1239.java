class Solution {
    public int result = 0;
    
    public int maxLength(List<String> arr) {
        if (arr == null || arr.size() == 0)    
            return 0;
        dfs(arr, "", 0);
        return result;
    }
        
        
        
    //finding all possible combinations of the string to reach at a valid string with max length
    public void dfs(List<String> arr, String path, int idx) {
        boolean isUniqueChar = isUniqueChars(path);

        if (isUniqueChar) {
          result = Math.max(path.length(), result);
        }

        if (idx == arr.size() || !isUniqueChar) {
          return;
        }

        for (int i = idx; i < arr.size(); i++) {
          dfs(arr, path + arr.get(i), i + 1);
        }

      }
    
    //checking whether the string combination is valid/unique or not
    private boolean isUniqueChars(String s) {
        Set<Character> set = new HashSet<>();
        for (char c : s.toCharArray()) {
          if (set.contains(c)) {
            return false;
          }
          set.add(c);
        }
        return true;
    }


        
}
