import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []
M = int(input())

for _ in range(M):
    editer = input().split()
    if editer[0] == "P":
        left.append(editer[1])
    elif editer[0] == "L" and left:
        right.append(left.pop())
    elif editer[0] == "D" and right:
        left.append(right.pop())
    elif editer[0] == "B" and left:
        left.pop()

result = left + right[::-1]
print("".join(result))