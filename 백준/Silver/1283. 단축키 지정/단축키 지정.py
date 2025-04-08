N = int(input())
option = set()
for _ in range(N):
    l = list(input())
    # 첫글자는 인덱스가 0이거나 이전 단어가 ""인 경우
    check = 0
    current_option = 1000
    for i in range(len(l)):
        if l[i] == " ":
            continue
        if l[i].lower() not in option:
            if i == 0:
                option.add(l[i].lower())
                l.insert(0,"[")
                l.insert(2,"]")
                check = 1
                break
            else:
                # 첫글자일 경우
                if l[i-1] == " ":
                    option.add(l[i].lower())
                    l.insert(i,"[")
                    l.insert(i+2,"]")
                    check = 1
                    break
                # 첫글자가 아닐 경우
                else:
                    if current_option > i:
                        current_option = i
    if check == 0:
        if current_option != 1000:
            option.add(l[current_option].lower())
            l.insert(current_option,"[")
            l.insert(current_option+2,"]")
    print("".join(l))