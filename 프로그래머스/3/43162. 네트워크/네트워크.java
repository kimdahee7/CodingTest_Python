import java.util.*;
class Solution {
    ArrayList<Integer>[] graph;
    boolean[] visited;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        graph = new ArrayList[n];
        visited = new boolean[n];

        for (int i=0;i<n;i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                if (computers[i][j] == 1 && i != j) {
                    graph[i].add(j);
                }
            }
        }
        
        for (int i=0; i<n; i++) {
            if (visited[i] != true) {
                answer +=1;
                bfs(i);
            }
        }
        return answer;
    }
    

public void bfs(int node) {
    Queue<Integer> q = new LinkedList<>();
    q.add(node);
    visited[node] = true;
    int now = 0;
    while (!q.isEmpty()) {
        now = q.poll();
        for (Integer i: graph[now]) {
            if (visited[i] != true) {
                q.add(i);
                visited[i] = true;
            }
        }
    }
}
}