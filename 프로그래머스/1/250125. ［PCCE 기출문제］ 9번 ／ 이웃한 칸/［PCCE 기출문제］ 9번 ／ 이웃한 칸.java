class Solution {
    public int solution(String[][] board, int h, int w) {
        int n = board[0].length;
        int count = 0;
        int h_check = 0;
        int w_check = 0;
        int[] dh = {0, 1, -1, 0};
        int[] dw = {1, 0, 0, -1};
        for (int i =0; i<4; i++) {
            h_check = dh[i] + h;
            w_check = dw[i] + w;
            if ((h_check>=0 && h_check<n) && (w_check>=0 && w_check<n)) {
                if (board[h][w].equals(board[h_check][w_check])) {
                    count +=1;
                }
            }
        }
        return count;
    }
}