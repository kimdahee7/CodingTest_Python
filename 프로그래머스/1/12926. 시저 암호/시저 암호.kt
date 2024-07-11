class Solution {
    fun solution(s: String, n: Int): String {
        var answer = ""
        s.forEach { i -> 
            // 소문자일 경우 
            if (i.isLowerCase()) {
                val next = i.toInt() + n
                if (next > 122) {
                    answer += (next%122 + 96).toChar()
                }else {
                    answer += next.toChar()
                }
            }
            // 대문자일 경우 
            else if (i.isUpperCase()) {
                val next = i.toInt() + n
                if (next > 90) {
                    answer += (next%90 + 64).toChar()
                }else {
                    answer += next.toChar()
                }
            } else {
                answer += ' '
            }
        }
        return answer
    }
}
