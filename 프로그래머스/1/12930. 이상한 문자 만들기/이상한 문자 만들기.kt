class Solution {
    fun solution(s: String): String {
        var answer = ""
        val l = s.split(" ")
        val total = l.size
        var count = 0
        for(i in l){
            count +=1
            val n = i.length
            for(j in 0..n-1){
                if (j%2 == 0) {
                    answer += i[j].toUpperCase()
                }
                else{
                    answer += i[j].toLowerCase()
                }
            }
            if (count != total){
                answer += " "
            }
        }
        return answer
    }
}