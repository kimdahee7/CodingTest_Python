import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int n = triangle.length;
        // 2차원 배열에서 열의 크기가 다를 경우 
        int[][] arr = new int[n][];
        for (int i=0;i<n;i++) {
            arr[i] = new int[i+1];
        }

        arr[0][0] = triangle[0][0];
        
        for (int i=1;i<n;i++) {
            for (int j=0; j<=i;j++) {
                if (j == 0) {
                    arr[i][j] = triangle[i][j] + arr[i-1][j];
                }
                else if (j == i){
                    arr[i][j] = triangle[i][j] + arr[i-1][j-1];
                } else {
                    int k = Math.max(arr[i-1][j-1], arr[i-1][j]);
                    arr[i][j] = triangle[i][j] + k;
                }
            }
        }
        
        for (int i=0;i<n;i++) {
            Arrays.sort(arr[i]);
            answer = Math.max(answer,arr[i][i]);
            
        }

        return answer;
    }
}