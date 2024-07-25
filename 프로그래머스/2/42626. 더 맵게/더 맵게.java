import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        int s = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (Integer i : scoville) {
            pq.add(i);
        }
        while (true) {
            s = pq.poll();
            if (s >= K) break;
            if (pq.size() < 1) {
                answer = -1;
                break;
            }
            pq.add(s + (pq.poll()*2));
            answer +=1;
        }
        return answer;
    }
}