import sys
input = sys.stdin.readline
def main(): 
  l = []
  n = int(input())
  a,b = map(int,input().split())
  m = int(input())
  graph = [[] for _ in range(n+1)]
  for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
  for i in range(1,n+1):
    graph[i].sort()
  visited = [False] * (n+1)
  r = DFS(graph,a,b,visited,l,0)
  if len(l) == 0:
    print(-1)
  else:
    print(l[0]-1)

def DFS(graph,a,b,visited,l,num):
  visited[a] = True
  num +=1
  if a == b:
    l.append(num)
  for i in graph[a]:
    if not visited[i]:
      DFS(graph,i,b,visited,l,num)
  return l
main()