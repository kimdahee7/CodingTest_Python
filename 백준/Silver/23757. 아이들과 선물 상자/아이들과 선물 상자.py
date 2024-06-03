import heapq

N,M = map(int,input().split())
present = list(map(int,input().split()))
number = list(map(int,input().split()))

h = []
for i in present:
    heapq.heappush(h,(-i,i))

for i in number:
    k = heapq.heappop(h)[1]
    if i < k:
        heapq.heappush(h,(-(k-i),k-i))
    elif i ==k:
        continue
    else:
        print(0)
        exit()
print(1)