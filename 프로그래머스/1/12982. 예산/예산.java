import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        int count = 0;
        for (Integer i: d) {
            if ((count + i) <= budget) {
                answer +=1;
                count +=i;
            }
        }
        return answer;
    }
}