import sys
input = sys.stdin.readline
N,M = map(int,input().split())
edge = []
parent = [0] * (N+1)
answer = []

for _ in range(M):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))

edge.sort()

for i in range(1,N+1):
    parent[i] = i

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for e in edge:
    c,a,b = e
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer.append(c)
answer.sort()
answer.pop()
print(sum(answer))
