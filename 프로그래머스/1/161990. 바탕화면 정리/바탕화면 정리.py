def solution(wallpaper):
    l_y = []
    l_x = []
    M = len(wallpaper[0])
    N = len(wallpaper)
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j] == "#":
                l_y.append(j)
                l_x.append(i)
    return [min(l_x),min(l_y),max(l_x)+1,max(l_y)+1]