def solution(park, routes):
    answer = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start_x = j
                start_y = i
                break
    for i in routes:
        if i[0] == "N":
            for j in range(int(i[2])):
                start_y -= 1
                if 0>start_y or start_y>=len(park):
                    start_y = start_y+(j+1)
                    break
                elif park[start_y][start_x] == "X":
                    start_y = start_y+(j+1)
                    break
        elif i[0] == "S":
            for j in range(int(i[2])):
                start_y += 1
                if 0>start_y or start_y>=len(park):
                    start_y = start_y-(j+1)
                    break
                elif park[start_y][start_x] == "X":
                    start_y = start_y-(j+1)
                    break
        elif i[0] == "W":
            for j in range(int(i[2])):
                start_x -= 1
                if 0>start_x or start_x>=len(park[0]):
                    start_x = start_x+(j+1)
                    break
                elif park[start_y][start_x] == "X":
                    start_x = start_x+(j+1)
                    break
        else:
            for j in range(int(i[2])):
                start_x += 1
                if 0>start_x or start_x>=len(park[0]):
                    start_x = start_x-(j+1)
                    break
                elif park[start_y][start_x] == "X":
                    start_x = start_x-(j+1)
                    break
    answer.append(start_y)
    answer.append(start_x)
    return answer

                
                
