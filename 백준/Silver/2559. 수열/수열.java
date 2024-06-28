import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] array = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<N;i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }

        int sum = 0;
        for (int i = 0; i < K; i++) {
            sum += array[i];
        }
        // 합한 값을 넣을 리스트
        List<Integer> answer = new ArrayList<>();
        answer.add(sum);

        int start = 0;
        for (int i=K;i<N;i++) {
            sum += array[i];
            sum -= array[start];
            start +=1;
            answer.add(sum);
        }
        System.out.println(Collections.max(answer));
    }
}