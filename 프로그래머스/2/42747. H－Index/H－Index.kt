class Solution {
    fun solution(citations: IntArray): Int {
        var answer = 0
        val maxdata = citations.maxOrNull() ?:0
        for (i in maxdata downTo 0 ) {
            val count1 = citations.count{it >= i}
            val count2 = citations.count{it <= i}
            if (count1 >= i && count2 <= i) {
                answer = i
                break
            }
        }
        return answer
    }
}