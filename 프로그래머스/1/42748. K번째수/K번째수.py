def solution(array, commands):
    result = []
    for i in commands:
        list = array[i[0]-1:i[1]]
        list.sort()
        result.append(list[i[2]-1])
    return result