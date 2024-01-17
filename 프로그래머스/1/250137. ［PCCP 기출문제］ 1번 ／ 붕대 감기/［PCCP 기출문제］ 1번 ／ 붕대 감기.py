def solution(bandage, health, attacks):
    answer = 0
    last_attack = attacks[len(attacks)-1][0]
    s = 0
    j = 0
    max_health = health
    for i in range(1,last_attack+1):
        if health <= 0:
            break
        if i == attacks[j][0]:
            s = 0
            health -= attacks[j][1]
            j +=1
        else:
            s +=1
            if s == bandage[0]:
                s = 0
                health += bandage[2]
            if health + bandage[1]  <= max_health:
                health += bandage[1]
            if health + bandage[1] > max_health:
                health = max_health
    if health <= 0:
        health = -1
        
    return health