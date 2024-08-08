import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int count = (brown - 4)/2;
        for(int i=1;i<=count/2;i++) {
            if (i*(count-i) == yellow) {
                int a = i + 2;
                int b = (count-i) + 2;
                answer[0] = Math.max(a,b);
                answer[1] = Math.min(a,b);
            }
        }
        return answer;
    }
}