class Solution {
    fun solution(number: IntArray): Int {
        var answer: Int = 0
        val n = number.size
        for (i in 0..n-3) {
            for (j in i+1..n-2) {
                for (k in j+1..n-1) {
                    val total = number[i] + number[j] + number[k]
                    if (total == 0) {
                        answer +=1
                    }
                }
            }
        }
        return answer
    }
}