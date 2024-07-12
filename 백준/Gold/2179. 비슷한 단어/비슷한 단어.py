N = int(input())
words = []
words_list = {}
for i in range(N):
    word = input()
    words_list[i] = word
    words.append((i,word))

# 문자를 기준으로 정렬
words.sort(key=lambda x:x[1])

max_count = 0
answer = []
for i in range(N-1):
    for j in range(i+1,N):
        count = 0
        # 두 단어가 같으면 제외
        if words[i][1] == words[j][1]:
            continue
        # 두 단어의 첫 문자가 같을 경우만 카운트
        if words[i][1][0] == words[j][1][0]:
            K = min(len(words[i][1]),len(words[j][1]))
            # 같은 문자 갯수 카운트
            for k in range(K):
                if words[i][1][k] == words[j][1][k]:
                    count +=1
                else:
                    break
            # 현재 카운트가 max_count 보다 큰 경우
            if count > max_count:
                answer = []
                max_count = count
                if words[i][0] < words[j][0]:
                    answer.append((count,words[i][0],words[j][0]))
                else:
                    answer.append((count,words[j][0],words[i][0]))
            # 현재 카운트가 max_count와 동일한 경우
            elif count == max_count:
                if words[i][0] < words[j][0]:
                    answer.append((count,words[i][0],words[j][0]))
                else:
                    answer.append((count,words[j][0],words[i][0]))
if len(answer) == 0:
    print(words_list[0])
    print(words_list[1])
else:
    answer.sort(key=lambda x:(-x[0],x[1],x[2]))
    print(words_list[answer[0][1]])
    print(words_list[answer[0][2]])