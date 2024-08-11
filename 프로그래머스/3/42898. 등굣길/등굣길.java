import java.util.*;
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] dist = new int[n][m];
        int[][] map = new int[n][m];
        
        // 물에 잠긴 지역 1로 표시 
        for (int i=0;i<puddles.length;i++) {
            map[puddles[i][1]-1][puddles[i][0]-1] = 1;
        }
        for (int i=0;i<n;i++) {
            for (int j=0;j<m;j++) {
                if (i ==0 && j ==0) {
                    dist[i][j] = 1;
                    continue;
                }
                // 물에 잠기지 않았다면 
                if (map[i][j] == 0) {
                    if (i-1 >= 0 && i-1 < n) {
                        dist[i][j] = (dist[i-1][j] + dist[i][j])% 1000000007;
                    } 
                    if (j-1>=0 && j-1 < m) {
                        dist[i][j] = (dist[i][j-1] + dist[i][j])% 1000000007;
                    }
                }
            }
        }
        answer = dist[n-1][m-1];
        return answer;
    }
}