x = int(input())
y = int(input())

if x > 0 : # x가 양수이고
    if y > 0 : # y가 양수이면
        print("1") # 1사분면
    else :
        print("4") # 4사분면
else : # x가 음수이고
    if y > 0 : # y가 양수이면
        print("2") # 3사분면
    else :
        print("3") # 4사분면