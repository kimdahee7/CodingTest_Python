# 크루스칼 알고리즘 사용
import math
N = int(input())
l = []
parent = [0] * (N+1)

for i in range(1,N+1):
    parent[i] = i

for _ in range(N):
    x,y = map(float,input().split())
    l.append((x,y))

# 간선과 가중치에 대한 값 입력
edges = []
for i in range(N-1):
    for j in range(i+1,N):
        edges.append((math.sqrt((l[i][0]-l[j][0])**2 + (l[i][1]-l[j][1])**2),i+1,j+1))

# 간선을 오름차순으로 정렬
edges.sort()
result = 0

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

for e in edges:
    cost,a,b = e
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(round(result,2))