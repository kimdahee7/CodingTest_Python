import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        PriorityQueue<Integer> pq1 = new PriorityQueue<>();
        PriorityQueue<Integer> pq2 = new PriorityQueue<>();
        for(String s : operations) {
            String[] input = s.split(" ");
            if (input[0].equals("I")) {
                pq1.add(Integer.parseInt(input[1]));
            } else if (pq1.size() == 0){
                continue;
            }else if (input[1].equals("1")) {
                while (pq1.size() > 1){
                    pq2.add(pq1.poll());
                }
                pq1.poll();
                while (pq2.size() > 0) {
                    pq1.add(pq2.poll());
                }
            } else {
                pq1.poll();
            }
        }
        if (pq1.size() == 0) {
            answer[0] = 0;
            answer[1] = 0;
        }else if (pq1.size() == 1){
            int k = pq1.poll();
            answer[0] = k;
            answer[1] = k;
        } else {
            answer[1] = pq1.poll();
            while (pq1.size() > 1) {
                pq1.poll();
            }
            answer[0] = pq1.poll();
        }
        
        return answer;
    }
}