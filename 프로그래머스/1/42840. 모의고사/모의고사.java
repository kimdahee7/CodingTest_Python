import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        int size = answers.length;
        
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int one_count = 0;
        int two_count = 0;
        int three_count = 0;
        
        int one_size = one.length;
        int two_size = two.length;
        int three_size = three.length;
        
        for (int i=0; i<size; i++) {
            if (answers[i] == one[i%one_size]) {
                one_count +=1;
            }
            if (answers[i] == two[i%two_size]) {
                two_count +=1;
            }
            if (answers[i] == three[i%three_size]) {
                three_count +=1;
            }
        }
        
        List<Integer> list = new ArrayList<>();
        list.add(one_count);
        list.add(two_count);
        list.add(three_count);
        int max_data = Collections.max(list);
        for (int i=0; i<3; i++) {
            if (list.get(i) == max_data) {
                answer.add(i+1);
            }
        }
        System.out.println(answer);
        return answer.stream().mapToInt(i->i).toArray();
    }
}
