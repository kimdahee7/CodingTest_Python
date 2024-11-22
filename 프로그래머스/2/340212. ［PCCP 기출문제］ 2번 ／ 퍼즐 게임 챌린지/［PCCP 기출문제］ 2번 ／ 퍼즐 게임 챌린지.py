def solution(diffs, times, limit):
    answer = 1e9
    max_level = max(diffs)
    level = [i for i in range(1,max_level+1)]
    visited = [0 for _ in range(max_level+1)]
    start = 0
    end = len(level)
    while start<end:
        mid = (start+end)//2
        if visited[mid] == 1:
            break
        visited[mid] = 1
        result = binary_search(level[mid],diffs,times)
        if result > limit:
            start = mid
        else:
            if answer > level[mid]:
                answer = min(answer,level[mid])
            end = mid

    return answer

# 해당 레벨로 시간 내에 모든 퍼즐을 해결할 수 있는지 확인 
def binary_search(level,diffs,times):
    result = 0
    for i in range(len(diffs)):
        # 현재 레벨보다 퍼즐의 난이도가 낮은 경우 
        if diffs[i] <= level:
            result += times[i]
        else:
            # 틀린 횟수 
            cnt = diffs[i] - level
            # 총 소요되는 시간 
            t = (times[i] + times[i-1]) * cnt + times[i]
            result += t
    return result
    
    