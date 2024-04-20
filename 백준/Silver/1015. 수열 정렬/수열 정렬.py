N = int(input())
A = list(map(int,input().split()))
l = []
p = [0]*N
for i in range(N):
    l.append((i,A[i]))
l.sort(key=lambda x:x[1])
for i in range(N):
    p[l[i][0]] = i
print(" ".join(map(str,p)))