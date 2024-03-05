def solution(wallpaper):
    answer = []
    lux = 0
    luy = 0
    rdx = 0
    rdy = 0
    l_y = []
    l_x = []
    M = len(wallpaper[0])
    N = len(wallpaper)
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j] == "#":
                l_y.append(j)
                l_x.append(i)
    luy = min(l_y)
    rdy = max(l_y)+1
    lux = min(l_x)
    rdx = max(l_x)+1
    answer = [lux,luy,rdx,rdy]
    return answer