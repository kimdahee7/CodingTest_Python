N = int(input())
l = list(map(int,input().split()))
l.sort()

start = 0
end = len(l)-1
answer = 10000000000
a = 0
b = 0

while start < end:
    sum = l[start] + l[end]
    if abs(sum) < answer:
        answer = abs(sum)
        a = l[start]
        b = l[end]
    elif sum > 0:
        end -=1
    elif sum < 0:
        start +=1
    else:
        break
print(a,b)