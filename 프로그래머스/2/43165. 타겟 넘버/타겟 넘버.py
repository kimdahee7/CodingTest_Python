def solution(numbers, target):
    answer = 0
    result = [0]
    for i in numbers:
        tmp = []
        for j in result:
            tmp.append(j+i)
            tmp.append(j-i)
        result = tmp
    answer = result.count(target)
    return answer