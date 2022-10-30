import java.util.Arrays;
import java.util.HashMap;

class Solution {

  static int [] nums = {2, 7, 11, 15, 3, 2, 4};
  static int target = 5;

  public static void main(String[] args) {
    int [] output = new int[2];
    Solution obj = new Solution();
    output = obj.twoSum(obj.nums, obj.target);
    System.out.println(Arrays.toString(output));
  }


  /* Solution Using HashMaps (One Pass) */
  public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    int length = nums.length;

    for (int i = 0; i < length; i++) {
      map.put(nums[i], i); 

      int complement;
      complement = target - nums[i];

      /* While we are iterating and inserting elements into the hash table, we
       * also look back to check if current element's complement already exists
       * in the hash table. If it exists, we have found a solution and return
       * the indices immediately.
       */

      if (map.containsKey(complement)) {
        return new int[] {map.get(complement), i};
      }
    }
    // In case there is no solution, we'll just return null
    return null;
  }


  /* Solution Using HashMaps (Two Pass) */

//   public int[] twoSum(int[] nums, int target) {
//     HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
//     int length = nums.length;

//     for (int i = 0; i < length; i++) {
//       map.put(nums[i], i);
//     }

//     for (int i = 0; i < length; i++) {
//       int complement;
//       complement = target - nums[i];
//       if (map.containsKey(complement) && map.get(complement) != i) {
//         return new int[] {i, map.get(complement) };
//       }
//     }
//     // In case there is no solution, we'll just return null
//     return null;
//   }

/* Solution using just arrays. */

  // public static int locateRank(int element) {
  //   for (int i=0; i < nums.length; i++) {
  //     if (nums[i] == element) {
  //       return i; 
  //     }
  //   }
  //   return -1;
  // }

  // public int[] twoSum(int[] nums, int target) {
  //   for (int i = 0; i < nums.length; i++) {
  //     int complement = target - nums[i];
  //     int index = locateRank(complement);
  //     // int index = sequence.locateRank(complement);
  //     if (index != -1 && index != i) {
  //       return new int[] {i, index};
  //     }
  //   }

  //   // In case there is no solution, we'll just return null
  //   return null;
  // }

}
