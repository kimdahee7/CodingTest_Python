R,C = map(int,input().split())
map = [input() for _ in range(R)]

answer_list = []
for i in range(R):
    word = ""
    for j in range(C):
        if map[i][j] != "#":
            word += map[i][j]
        else:
            if word != "" and len(word) > 1:
                answer_list.append(word)
            word = ""
    if word != "" and len(word) > 1:
        answer_list.append(word)

for i in range(C):
    word = ""
    for j in range(R):
        if map[j][i] != "#":
            word += map[j][i]
        else:
            if word != "" and len(word) > 1:
                answer_list.append(word)
            word = ""
    if word != "" and len(word) > 1:
        answer_list.append(word)

answer_list.sort()
print(answer_list[0])