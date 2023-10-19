def solution(x, y, n):
    answer = 0
    result = {x}
    if x == y:
        return 0
    while True:
        new_result = set()
        for i in result:
            new_result.add(i+n)
            new_result.add(i*2)
            new_result.add(i*3)
        answer +=1
        result = new_result
        if y in new_result:
            break
        if min(result) > y:
            return -1
    return answer