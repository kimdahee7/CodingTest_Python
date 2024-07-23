import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        List<Integer> tmp;
        List<Integer> l = new ArrayList<>();
        l.add(0);
        
        for (int i=0;i<numbers.length;i++) {
            tmp = new ArrayList<>();
            for (Integer j: l) {
                tmp.add(j + numbers[i]);
                tmp.add(j - numbers[i]);
            }
            l = tmp;
        }
        answer = Collections.frequency(l,target);
        
        return answer;
    }
}