def solution(n, words):
    answer = []
    turn = 0
    num = 0
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            num = (i+1) - (i//n)*n
            turn = i//n + 1
            break
        elif len(words[i]) == 1:
            num = (i+1) - (i//n)*n
            turn = i//n + 1
            break
        elif words[i] in words[0:i]:
            num = (i+1) - (i//n)*n
            turn = i//n + 1
            break
    answer.append(num)
    answer.append(turn)
    return answer