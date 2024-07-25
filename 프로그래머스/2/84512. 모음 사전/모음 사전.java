import java.util.*;
class Solution {
    String[] output;
    int r;
    List<String> total_list = new ArrayList<>();
    String[] word_list = {"A","E","I","O","U"};
    public int solution(String word) {
        int answer = 0;
        
        for (int i=1;i<6;i++) {
            output = new String[i];
            r = i;
            perm(0);
        }
        
        Collections.sort(total_list);
        answer = total_list.indexOf(word) + 1;
        
        return answer;
    }
    
    public void perm(int cnt) {
        if (cnt == r) {
            total_list.add(String.join("",output));
            return;
        }
        for (int i=0;i<5;i++) {
            output[cnt] = word_list[i];
            perm(cnt+1);
        }
    }
}