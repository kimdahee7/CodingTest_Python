import java.util.*;

class Solution {
    ArrayList<Integer>[] tree;
    boolean[] visited;
    
    public int solution(int n, int[][] wires) {
        int answer = 100000000;
        
        for (int i=0;i<wires.length;i++) {
            tree = new ArrayList[n+1];
            visited = new boolean[n+1];
            for (int t=0;t<n+1;t++) {
                tree[t] = new ArrayList<>();
            }
            for (int j=0;j<wires.length;j++) {
                if (i != j) {
                    tree[wires[j][0]].add(wires[j][1]);
                    tree[wires[j][1]].add(wires[j][0]);
                }
            }
            
            List<Integer> list = new ArrayList<>();
            for(int node=1;node<n+1;node++){
                if (visited[node] == false) {
                    list.add(dfs(node));
                }
            } 
            answer = Math.min(answer,Math.abs(list.get(0)-list.get(1)));
        }
        return answer;
    }
    
    public int dfs(int node) {
        visited[node] = true;
        int count = 1;
        for (Integer i : tree[node]) {
            if (visited[i] == false) {
                count += dfs(i);
            }
        }
        return count;
    }
}