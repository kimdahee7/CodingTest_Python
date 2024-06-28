import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] array = new int[N][4];

        for (int i = 0; i < N; i++) {
            // 국가, 금, 은, 동
            st = new StringTokenizer(bf.readLine());
            array[i][0] = Integer.parseInt(st.nextToken());
            array[i][1] = Integer.parseInt(st.nextToken());
            array[i][2] = Integer.parseInt(st.nextToken());
            array[i][3] = Integer.parseInt(st.nextToken());
        }
        // 금,은,동 순으로 정렬
        Arrays.sort(array,Comparator.comparing((int[] o) -> o[3]).reversed());
        Arrays.sort(array,Comparator.comparing((int[] o) -> o[2]).reversed());
        Arrays.sort(array,Comparator.comparing((int[] o) -> o[1]).reversed());

        int count = 1;
        int answer = 1;
        int[][] answer_list = new int[N][2];
        answer_list[0][0] = array[0][0];
        answer_list[0][1] = 1;
        int g = array[0][1];
        int s = array[0][2];
        int b = array[0][3];
        for (int i = 1; i < N; i++) {
            if (array[i][1] == g && array[i][2] == s && array[i][3] == b) {
                count +=1;
                answer_list[i][0] = array[i][0];
                answer_list[i][1] = answer;
            } else {
                answer = count + 1;
                count +=1;
                answer_list[i][0] = array[i][0];
                answer_list[i][1] = answer;
                g = array[i][1];
                s = array[i][2];
                b = array[i][3];
            }
        }

        for (int i = 0; i < N; i++) {
            if (answer_list[i][0] == K) {
                System.out.println(answer_list[i][1]);
            }
        }
    }
}
