def solution(numbers, target):
    answer = 0
    result = [0]
    for i in numbers:
        tmp = []
        for r in result:
            tmp.append(r+i)
            tmp.append(r-i)
        result = tmp
    answer = result.count(target)
    return answer