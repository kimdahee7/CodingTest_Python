H, W, N, M = map(int, input().split())
answer = 1

if W % (M + 1) == 0:
    answer *= (W // (M + 1))
else:
    answer *= ((W // (M + 1)) + 1)

if H % (N + 1) == 0:
    answer *= H // (N + 1)
else:
    answer *= (H // (N + 1) + 1)
print(answer)