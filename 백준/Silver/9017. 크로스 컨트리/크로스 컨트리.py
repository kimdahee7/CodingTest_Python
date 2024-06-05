from collections import Counter
from collections import defaultdict

T = int(input())
for _ in range(T):
  N = int(input())
  l = list(map(int,input().split()))
  c = dict(Counter(l))
  e = set()

  # 출전 인원이 6명이 아닌 팀 탐색
  for i in c.items():
    if i[1] != 6:
      e.add(i[0])

  # 각 팀별 점수 추가
  dic = defaultdict(list)
  score = 0
  for i in range(N):
    if l[i] in e:
      continue
    score += 1
    dic[l[i]].append(score)
  score_list = {}
  for i in dic.items():
    score_list[i[0]] = sum(i[1][0:4])

  # 점수가 작은 순서대로 정렬
  score_list = sorted(score_list.items(), key=lambda x:x[1])
  winner_score = score_list[0][1]
  winner_list = []
  for i in score_list:
    if winner_score == i[1]:
      winner_list.append(i[0])

  if len(winner_list) == 1:
    print(winner_list[0])
  else:
    answer_dic = {}
    for i in winner_list:
      answer_dic[i] = dic[i][4]
    print(sorted(answer_dic.items(), key=lambda x:x[1])[0][0])