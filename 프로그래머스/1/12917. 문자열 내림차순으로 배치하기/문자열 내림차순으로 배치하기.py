def solution(s):
    answer = ''
    l= []
    for i in s:
        l.append(ord(i))
    l.sort(reverse=True)
    for i in l:
        answer += chr(i)
    return answer