import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<Integer> set = new HashSet<>();
        for (int i=0;i<nums.length;i++) {
            set.add(nums[i]);
        }
        int select = (nums.length)/2;
        answer = Math.min(select,set.size());
        return answer;
    }
}
