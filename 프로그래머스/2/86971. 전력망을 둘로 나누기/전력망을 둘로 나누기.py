def solution(n, wires):
    global answer
    visited = [False for i in range(n+1)]
    e = [[] for i in range(n+1)]
    for a,b in wires:
        e[a].append(b)
        e[b].append(a)
    answer = 1e9
    def dfs(node):
        global answer
        visited[node] = True
        subtree_count = 1
        for i in e[node]:
            if not visited[i]:
                subtree_count += dfs(i)
        
        other_count = n - subtree_count
        
        answer = min(answer, abs(subtree_count - other_count))
        return subtree_count
    
    dfs(1)
    
    return answer

