import java.util.*;
class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Queue<String> cache = new LinkedList<>();
        if (cacheSize == 0) {
            answer = cities.length * 5;
            return answer;
        }
        for (String s: cities) {
            int check = 0;
            Queue<String> cache2 = new LinkedList<>();
            for (String c: cache) {
                if (c.equalsIgnoreCase(s)) {
                    answer +=1;
                    check = 1;
                }else {
                    cache2.add(c);
                }
            }
            if (check == 0) {
                answer +=5;
                if (cache.size() < cacheSize) {
                   cache.add(s);
               }else {
                   cache.poll();
                   cache.add(s);
               }
            }else {
                cache2.add(s);
                cache = cache2;
            }
        }
        return answer;
    }
}