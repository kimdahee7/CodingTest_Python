import heapq
import sys
input = sys.stdin.readline

N = int(input())
front = [] # 최대힙
back = [] # 최소힙

for i in range(N):
    n = int(input())
    # 숫자를 번갈아가면서 front와 back에 삽입
    if len(front) == len(back) or len(front) == 0:
        heapq.heappush(front,-n)
    else:
        heapq.heappush(back,n)
    # 만약 front의 최댓값이 back의 최소값보다 클 경우 교체
    if front and back and -front[0] > back[0]:
        heapq.heappush(back,-heapq.heappop(front))
        heapq.heappush(front,-heapq.heappop(back))
    print(-front[0])