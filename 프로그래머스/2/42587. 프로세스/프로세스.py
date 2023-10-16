def solution(priorities, location):
    index = [i for i in range(len(priorities))]
    total = 1
    while len(index) > 0:
        max_data = max(priorities)
        if priorities[0] == max_data:
            if index[0] == location:
                answer = total
                break
            else:
                priorities.pop(0)
                index.pop(0)
                total +=1
        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            index.append(index[0])
            index.pop(0)
    return answer