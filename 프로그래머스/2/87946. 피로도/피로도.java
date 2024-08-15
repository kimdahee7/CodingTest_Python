import java.util.*;
class Solution {
    public int[] output;
    public boolean[] visited;
    int n,r,c;
    int answer = -1;
    public int solution(int k, int[][] dungeons) {
        n = dungeons.length;
        r = n;
        c = k;
        output = new int[n];
        visited = new boolean[n];
        perm(0,dungeons);
        return answer;
    }
    
    public void perm(int cnt, int[][] dungeons) {
        if(cnt == r) {
            int current = c;
            int count = 0;
            for (Integer i : output) {
                if (dungeons[i][0] <= current) {
                    count +=1;
                    current -= dungeons[i][1];
                } else {
                    break;
                }
            }
            answer = Math.max(answer,count);
            return;
        }
        for (int i=0;i<n;i++){
            if(visited[i]) continue;
            output[cnt] = i;
            visited[i] = true;
            perm(cnt+1,dungeons);
            visited[i] = false;
        }  
    }
}