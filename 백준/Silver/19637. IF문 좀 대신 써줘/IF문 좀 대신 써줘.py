import sys
input = sys.stdin.readline

N,M = map(int,input().split())
level = []
for i in range(N):
    a,b = map(str,input().split())
    level.append((a,int(b)))

def binary(level,k):
    answer = ""
    start = 0
    end = len(level)-1
    while start<=end:
        mid = (start + end)//2
        if k <= level[mid][1]:
            answer = level[mid][0]
            end = mid - 1
        else:
            start = mid +1
    return answer

for i in range(M):
    k = int(input())
    print(binary(level,k))