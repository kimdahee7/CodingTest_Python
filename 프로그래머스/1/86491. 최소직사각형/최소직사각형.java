import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        List<Integer> min_l = new ArrayList<>();
        List<Integer> max_l = new ArrayList<>();
        for (int i=0;i<sizes.length;i++) {
            Arrays.sort(sizes[i]);
            min_l.add(sizes[i][0]);
            max_l.add(sizes[i][1]);
        }
        answer = Collections.max(max_l) * Collections.max(min_l);
        return answer;
    }
}