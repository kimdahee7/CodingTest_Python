import java.util.*;
class Solution {
    String[] output;
    boolean[] visited;
    String[] arr;
    HashSet<Integer> set = new HashSet<>();
    // n개 중에 r개를 뽑아서 순열을 만듦
    int n,r;
    int answer = 0;
    public int solution(String numbers) {
        arr = numbers.split("");
        n = arr.length;
        for (int i=1; i<n+1; i++){
            r = i;
            output = new String[r];
            // 동일한 숫자가 있을 수도 있으므로 인덱스로 visited를 확인 
            visited = new boolean[n];
            
            perm(0);
            
        }
        return answer;
    }
    
    // 순열 리스트 구해서 해당 숫자를 소수 판별 함수로 넘기기  
    public void perm(int cnt) {
        if (cnt == r) {
            int number = Integer.parseInt(String.join("",output));
            // 이미 확인한 숫자라면 pass 
            if (set.contains(number)) return;
            // 만약 소수이면 
            if (check(number)) {
                set.add(number);
                answer +=1;
            }
            return;
        }
        for (int i=0;i<n;i++) {
            if (visited[i]) continue;
            output[cnt] = arr[i];
            visited[i] = true;
            perm(cnt+1);
            visited[i] = false;
        }
    }
    
    // 소수 판별
    public Boolean check(int number) {
        
        if (number == 1 || number == 0) {
            return false;
        }
        
        for (int i=2; i<number;i++) {
            if (number%i == 0) {
                return false;
            }
        }
        return true;
    }
}