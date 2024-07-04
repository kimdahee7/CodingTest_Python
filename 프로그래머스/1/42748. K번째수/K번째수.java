import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = {};
        answer = new int[commands.length];
        for (int i=0; i<commands.length; i++) {
            int a = commands[i][0];
            int b = commands[i][1];
            int k = commands[i][2];
            List<Integer> list = new ArrayList<>();
            for (int j=a-1;j<b; j++) {
                list.add(array[j]);
            }
            Collections.sort(list);
            answer[i] = list.get(k-1);
        }
        return answer;
    }
}