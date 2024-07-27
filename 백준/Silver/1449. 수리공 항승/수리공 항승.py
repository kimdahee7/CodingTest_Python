N,L = map(int,input().split())
point = list(map(int,input().split()))

point.sort()
end_point = L + point[0] - 0.5
answer = 1
for i in range(1,N):
    if point[i] + 0.5 <= end_point:
        continue
    else:
        answer +=1
        end_point = point[i] - 0.5 + L
print(answer)