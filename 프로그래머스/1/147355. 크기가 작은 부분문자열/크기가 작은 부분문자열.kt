class Solution {
    fun solution(t: String, p: String): Int {
        var answer: Int = 0
        var s = ""
        val p_n = p.length
        val t_n = t.length
        for (i in 0..t_n-p_n) {
            s = t.substring(i,i+p_n)
            // 크기 비교를 Int가 아닌 Long 타입으로
            if (s.toLong() <= p.toLong()){
                answer +=1
            }
        }
        return answer
    }
}