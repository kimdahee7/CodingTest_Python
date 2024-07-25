import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        HashMap<String,Integer> map = new HashMap<>();
        for (int i=0;i<genres.length;i++) {
            if (map.containsKey(genres[i])) {
                map.put(genres[i],map.get(genres[i]) + plays[i]);
            } else {
                map.put(genres[i],plays[i]);
            }
        }

        List<String> keySet = new ArrayList<>(map.keySet());
        Collections.sort(keySet, (o1,o2) -> (map.get(o2).compareTo(map.get(o1))));
        for (String s: keySet) {
            HashMap<Integer,Integer> plays_map = new HashMap<>();
            for (int i=0;i<genres.length;i++) {
                if (genres[i].equals(s)) {
                    plays_map.put(i,plays[i]);
                } 
            }
            List<Integer> keySet2 = new ArrayList<>(plays_map.keySet());
            Collections.sort(keySet2, (v1,v2) -> (plays_map.get(v2).compareTo(plays_map.get(v1))));
            int cnt = 0;
            for (Integer i : keySet2) {
                if (cnt == 2) break;
                answer.add(i);
                cnt +=1;
            }
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}