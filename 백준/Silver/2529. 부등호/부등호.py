k = int(input())
l = list(map(str,input().split()))

num = [1 for _ in range(10)]
result = []
answer = []

# 부등호가 맞는지 확인하는 함수
def check(list_num):
    for i in range(1,k+1):
        if l[i-1] == "<" and list_num[i-1] < list_num[i]:
            continue
        elif l[i-1] == ">" and list_num[i-1] > list_num[i]:
            continue
        else:
            return False
    return True

def back():
    if len(result) == k+1 and check(result):
        n = ""
        for i in result:
            n += str(i)
        answer.append(n)
        return
    for r in range(10):
        if r not in result:
            result.append(r)
            back()
            result.pop()

back()
print(answer[-1])
print(answer[0])