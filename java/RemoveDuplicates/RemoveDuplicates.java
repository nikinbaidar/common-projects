import java.util.Arrays;
import java.util.HashMap;


class Solution {

    public int removeDuplicates(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int k = 0;

        for (int i=0; i < nums.length; i++) {
            if (! map.containsKey(nums[i])) {
                map.put(nums[i], k);          
                k++;
            }
        }

        for (int i : map.keySet()) {
            nums[map.get(i)] = i;
        }

        return k;
                
    }


    public static void main(String[] args) {
        Solution obj = new Solution();
        // int [] nums = {1, 1, 2};
        int [] nums = {0,0,1,1,1,2,2,3,3,4};
        // 0 1 2 3 4
        int k;
        k = obj.removeDuplicates(nums);
        System.out.println(k);
        System.out.println(Arrays.toString(nums));
    }
}
