import java.util.*
class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = mutableListOf<Int>()
        var i = 0 
        commands.forEach {
            val slicedList = array.slice(it[0]-1 until it[1])
            val sortedList = slicedList.sorted()
            answer.add(sortedList[it[2]-1])
            i +=1
            
        }
        return answer.toIntArray()
    }
}