N = int(input())
l = [[] for _ in range(N)]
for i in range(N):
    a,b,c,d = map(str,input().split())
    l[i] = [a,int(b),int(c),int(d)]
l.sort()
l.sort(key=lambda x:-x[3])
l.sort(key=lambda x:x[2])
l.sort(key=lambda x:-x[1])
for i in range(N):
    print(l[i][0])