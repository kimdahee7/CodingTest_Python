from collections import deque
def solution(edges):
    answer = [0] * 4
    l = set()
    delete_node = 0
    node = 0 
    
    # 노드의 총 개수 
    for a,b in edges:
        l.add(b)
        node = max(node,a,b)
        
    graph = [[] for _ in range(node+1)]
    for a,b in edges:
        graph[a].append(b)
        
    # 지울 수 있는 노드 찾기 
    for i in range(1,node+1):
        if i not in l and len(graph[i]) >=2:
            delete_node = i
            break
    
    visited = [0] * (node+1)
    
    for start in graph[delete_node]:
        q = deque()
        q.append(start)
        visited[start] = 1
        
        V,E = 0, 0
        while q:
            V +=1
            n = q.popleft()
            for i in graph[n]:
                E +=1
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
        if V == E:
            answer[1] +=1
        elif V-1 == E:
            answer[2] +=1
        elif V+1 == E:
            answer[3] +=1
    answer[0] = delete_node
    return answer

            