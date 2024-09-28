N,M = map(int,input().split())
parent = [0] * N

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

for i in range(N):
    parent[i] = i

for num in range(M):
    a,b = map(int,input().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        print(num+1)
        exit()

print(0)