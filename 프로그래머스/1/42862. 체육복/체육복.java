import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        HashSet<Integer> set = new HashSet<>();
        List<Integer> lost2 = new ArrayList<>();
        List<Integer> reserve2 = new ArrayList<>();
        for (Integer i: lost) {
            lost2.add(i);
        }
        for (Integer i: reserve) {
            if (lost2.contains(i)) {
                set.add(i);
            } else {
                reserve2.add(i);
            }
        }
        Collections.sort(reserve2);
        
        for (Integer i: reserve2) {
            int c = 0;
            if (lost2.contains(i-1)) {
                if (set.contains(i-1)) {
                } else {
                    set.add(i-1);
                    c +=1;
                }
            }
            if (lost2.contains(i+1) && c == 0) {
                if (set.contains(i+1)) {
                } else {
                    set.add(i+1);
                }
            }
        }
        return answer + set.size();
    }
}