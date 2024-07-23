import java.awt.Point;
import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        Queue<Point> q = new LinkedList<>();
        int n = maps.length;
        int m = maps[0].length;
        int[][] dist = new int[n][m];
        
        for (int i=0;i<n;i++) {
            for (int j=0;j<m;j++) {
                dist[i][j] = 1000000000;
            }
        }
        
        dist[0][0] = 1;
        
        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};

        q.add(new Point(0,0));
        while (!q.isEmpty()) {
            Point p = q.poll();
            for (int i=0;i<4;i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if (0<=nx && nx<m && 0<=ny && ny<n && maps[ny][nx] == 1) {
                    if (dist[ny][nx] > dist[p.y][p.x] +1) {
                        dist[ny][nx] = dist[p.y][p.x] +1;
                        q.add(new Point(nx,ny));
                    }
                }
            }
        }
        if (dist[n-1][m-1] == 1000000000){
            answer = -1;
        } else {
            answer = dist[n-1][m-1];
        }
        
        return answer;
    }
}