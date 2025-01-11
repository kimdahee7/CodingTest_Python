def solution(numbers, hand):
    answer = ''
    keypad = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2)
             ,7:(2,0),8:(2,1),9:(2,2),0:(3,1)}
    # 첫 손가락 위치
    l_x,l_y = 0,3
    r_x,r_y = 2,3
    for n in numbers:
        n_x = keypad[n][1]
        n_y = keypad[n][0]
        if n == 1 or n == 4 or n == 7:
            answer += "L"
            l_x = n_x
            l_y = n_y
        elif n == 3 or n == 6 or n == 9:
            answer += "R"
            r_x = n_x
            r_y = n_y
        else:
            # 맨해튼 거리로 구하기 
            left = abs(l_x-n_x) + abs(l_y-n_y)
            right = abs(r_x-n_x) + abs(r_y-n_y)
            if left < right:
                answer += "L"
                l_x = n_x
                l_y = n_y
            elif left > right:
                answer += "R"
                r_x = n_x
                r_y = n_y
            else:
                if hand == "right":
                    answer += "R"
                    r_x = n_x
                    r_y = n_y
                else:
                    answer += "L"
                    l_x = n_x
                    l_y = n_y

    return answer