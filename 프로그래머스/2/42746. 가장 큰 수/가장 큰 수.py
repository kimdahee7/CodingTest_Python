def solution(numbers):
    answer = ''
    l = []
    numbers = list(map(str,numbers))
    for i in numbers:
        l.append(i*3)
    l.sort(reverse=True)
    for i in l:
        answer += i[0:len(i)//3]
    if answer[0] == "0":
        answer = "0"
    return answer