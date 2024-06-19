def checkX(case):
    count = 0
    if case[0:3] == "XXX":
        count +=1
    elif case[3:6] == "XXX":
        count +=1
    elif case[6:9] == "XXX":
        count +=1
    elif case[0] == case[3] == case[6] == "X":
        count +=1
    elif case[1] == case[4] == case[7] == "X":
        count +=1
    elif case[2] == case[5] == case[8] == "X":
        count +=1
    elif case[0] == case[4] == case[8] == "X":
        count +=1
    elif case[2] == case[4] == case[6] == "X":
        count +=1
    return count

def checkO(case):
    count = 0
    if case[0:3] == "OOO":
        count +=1
    elif case[3:6] == "OOO":
        count +=1
    elif case[6:9] == "OOO":
        count +1
    elif case[0] == case[3] == case[6] == "O":
        count +=1
    elif case[1] == case[4] == case[7] == "O":
        count +=1
    elif case[2] == case[5] == case[8] == "O":
        count +=1
    elif case[0] == case[4] == case[8] == "O":
        count +=1
    elif case[2] == case[4] == case[6] == "O":
        count +=1
    return count

while True:
    case = input()
    if case == "end":
        exit()
    x_count = 0
    o_count = 0
    for i in case:
        if i == "X":
            x_count +=1
        elif i == "O":
            o_count +=1
    # 판이 다 채워져 있을 때
    if (x_count+o_count) == 9:
        if x_count == o_count + 1:
            if checkX(case) == 1 and checkO(case) == 0:
                print("valid")
            # 세개 연속이 없을 경우
            elif checkX(case) == 0 and checkO(case) == 0:
                print("valid")
            else:
                print("invalid")
        else:
            print("invalid")

    # 판이 다 채워져 있지 않을 때
    else:
        # 개수가 같으면 O이 세개 연속이어야 함
        if x_count == o_count:
            if checkO(case) == 1 and checkX(case) == 0:
                print("valid")
            else:
                print("invalid")
        # X의 개수가 +1이면 X가 세개 연속이어야 함
        elif x_count == o_count + 1:
            if checkX(case) == 1 and checkO(case) == 0:
                print("valid")
            else:
                print("invalid")
        else:
            print("invalid")