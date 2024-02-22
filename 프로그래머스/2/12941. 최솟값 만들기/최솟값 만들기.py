import heapq
def solution(A,B):
    answer = 0
    a = []
    b = []
    for i in A:
        heapq.heappush(a,i)
    for i in B:
        heapq.heappush(b,(-i,i))
    for i in range(len(A)):
        answer += heapq.heappop(a) * heapq.heappop(b)[1]
    return answer