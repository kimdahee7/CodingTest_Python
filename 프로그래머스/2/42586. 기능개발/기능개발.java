import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> l = new ArrayList<>();
        for (int i=0; i<progresses.length;i++) {
            if ((100-progresses[i]) % speeds[i] == 0) {
                l.add((100-progresses[i]) / speeds[i]);
            }else {
                l.add((100-progresses[i]) / speeds[i]+1);
            }
        }

        int count = 0;
        int pre_data = l.get(0);
        for (Integer i: l) {
            if (i <= pre_data) {
                count +=1;
            } else {
                answer.add(count);
                count = 1;
                pre_data = i;
            }
        }
        answer.add(count);
        return answer.stream().mapToInt(i->i).toArray();
    }
}