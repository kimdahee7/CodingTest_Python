N = int(input())
l = list(map(int, input().split()))

start = 0
end = N - 1
answer_a = 0
answer_b = 0
answer_s = 100000000000
while start < end:
    sum = l[start] + l[end]
    if abs(answer_s) > abs(sum):
        answer_s = sum
        answer_a = l[start]
        answer_b = l[end]
    if sum > 0:
        end -=1
    elif sum < 0:
        start +=1
    else:
        break
print(answer_a, answer_b)