class Solution {
    public long solution(int price, int money, int count) {
        long total = 0;
        for (long i=1;i<=count;i++) {
            total += i * price;
        }
        if (total <= money) {
            return 0;
        } else {
            return total - money;
        }
    }
}