def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        elif i.islower():
            o = ord(i) + n
            if o > 122:
                answer += chr(o-26)
            else:
                answer += chr(o)
        else:
            o = ord(i) + n
            if o > 90:
                answer += chr(o-26)
            else:
                answer += chr(o)
    return answer
