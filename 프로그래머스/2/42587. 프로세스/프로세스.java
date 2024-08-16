import java.util.*;
import java.awt.Point;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        int n = priorities.length;
        int[] arr = new int[2];
        Queue<Point> q = new LinkedList<>();
        for (int i=0;i<n;i++) {
            // 첫번째 - 인덱스, 두번째 - 값 
            q.add(new Point(i,priorities[i]));
        }
        List<Integer> l = new ArrayList<>();
        for (Integer i : priorities) {
            l.add(i);
        }
        Collections.sort(l,Collections.reverseOrder());

        while (!q.isEmpty()) {
            Point p = q.poll();
            if (p.y < l.get(0)) {
                q.add(new Point(p.x,p.y));
                continue;
            } 
            else if (p.y == l.get(0)) {
                l.remove(0);
                if (p.x == location) {
                    break;
                } else {
                    answer +=1;
                }
            }
        }
        return answer;
    }
}