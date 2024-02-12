def solution(arr):
    answer = 0
    max_data = max(arr)
    end_data = 1
    for i in arr:
        end_data *=i
    for i in range(max_data,end_data+1):
        c = 0
        for j in arr:
            if i%j == 0:
                c+=1
        if c == len(arr):
            answer = i
            break
    return answer