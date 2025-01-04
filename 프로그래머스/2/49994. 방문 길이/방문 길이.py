def solution(dirs):
    answer = 0
    l = set()
    
    x = 0
    y = 0
    for i in dirs:
        if i == "U":
            if -5<=y+1<6:
                if (x,y+1,x,y) not in l:
                    l.add((x,y,x,y+1))
                y += 1
        if i == "D":
            if -5<=y-1<6:
                if (x,y-1,x,y) not in l:
                    l.add((x,y,x,y-1))
                y-=1
        if i =="L":
            if -5<=x-1<6:
                if (x-1,y,x,y) not in l:
                    l.add((x,y,x-1,y))
                x-=1
        if i =="R":
            if -5<=x+1<6:
                if (x+1,y,x,y) not in l:
                    l.add((x,y,x+1,y))
                x+=1
    answer = len(l)
    return answer