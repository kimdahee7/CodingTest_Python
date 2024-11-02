X = int(input())
word = input()
count = 0
visited = []
while count < X:
    w = word[0]
    back = ""
    for i in range(1,len(word)):
        if i % 2 == 0:
            w += word[i]
        else:
            back += word[i]
    word = w + back[::-1]
    if word in visited:
        index = X % count -1
        print(visited[index])
        exit()
    else:
        visited.append(word)
        count +=1
print(word)