import math

MAX = 1299709
arr = [True for i in range(MAX+1)]
arr[1] = False

for i in range(2,int(math.sqrt(MAX)+1)):
    if arr[i] == True:
        j = 2
        while i*j <= MAX:
            arr[i*j] = False
            j +=1

T = int(input())
for _ in range(T):
    k = int(input())
    if arr[k] == True:
        print(0)
        continue
    else:
        start = k - 1
        end = k + 1
        while start < end:
            if arr[start] and arr[end]:
                break
            if not arr[start]:
                start -=1
            if not arr[end]:
                end +=1
        print(end - start)