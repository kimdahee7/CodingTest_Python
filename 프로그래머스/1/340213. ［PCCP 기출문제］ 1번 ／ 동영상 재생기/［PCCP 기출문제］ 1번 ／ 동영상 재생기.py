def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    # 현재 시간, 시작 시간, 종료 시간을 초 단위로 변환
    current_time = int(pos[0:2]) * 60 + int(pos[3:5])
    start_time = int(op_start[0:2]) * 60 + int(op_start[3:5])
    end_time = int(op_end[0:2]) * 60 + int(op_end[3:5])
    video_time = int(video_len[0:2]) * 60 + int(video_len[3:5])
    
    ind = 0
    while ind < len(commands):
        if start_time <= current_time <= end_time:
            current_time = end_time
        if commands[ind] == "next":
            current_time += 10
            if current_time > video_time:
                current_time = video_time
        if commands[ind] == "prev":
            current_time -= 10
            if current_time < 0:
                current_time = 0
        ind += 1
    if start_time <= current_time <= end_time:
        current_time = end_time
    
    result_min = str(current_time//60)
    result_sec = str(current_time%60)
    if len(result_min) == 1:
        result_min = "0" + result_min
    if len(result_sec) == 1:
        result_sec = "0" + result_sec
    answer = result_min +":" + result_sec
            
    return answer