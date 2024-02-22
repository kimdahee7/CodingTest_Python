def solution(s):
    answer = []
    total = 0 #0의 개수 
    count = 0 #이진 변환 횟수
    while s != "1":
        total_zero = len(s)
        s = s.replace("0","")
        delete_zero = len(s)
        total += (total_zero-delete_zero)
        s = f(len(s))
        count +=1
    answer.append(count)
    answer.append(total)
    return answer

def f(l):
    s = ""
    while l != 0:
        s += str(l%2)
        l = l//2
    return s[::-1]
        
    