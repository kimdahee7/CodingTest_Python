import java.util.*;
class Solution {
    public String solution(String number, int k) {
        StringBuilder answerBuilder = new StringBuilder();
        
        int num_size = number.length() - k;
        int start = 0;
        
        char[] array = number.toCharArray();

        for (int i=1;i<num_size+1;i++) {
            char max_num = '0';
            for (int j=start;j<k+i;j++) {
                if (max_num < array[j]) {
                    max_num = array[j];
                    start = j+1;
                }
            }
            answerBuilder.append(Character.toString(max_num));
            
        }
        return answerBuilder.toString();
        
    }
}