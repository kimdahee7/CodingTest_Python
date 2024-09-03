import java.util.*;
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        List<int[]> m1 = new ArrayList<>();
        List<int[]> m2 = new ArrayList<>();
        
        for (int i=0;i<n;i++) {
            m1.add(change(arr1[i],n));
            m2.add(change(arr2[i],n));
        }
        for (int i=0;i<n;i++) {
            String s = "";
            for (int j=0;j<n;j++) {
                if (m1.get(i)[j] == 1 || m2.get(i)[j] == 1) {
                    s+="#";
                } else if (m1.get(i)[j] == 0 && m2.get(i)[j] == 0){
                    s+=" ";
                }
            }
            answer[i] = s;
        }
        return answer;
    }
    public int[] change(int number, int n) {
        int[] result = new int[n];
        int index = n-1;
        while (number != 0) {
            result[index] = number%2;
            number = number/2;
            index -=1;
        }
        return result;
    }
}