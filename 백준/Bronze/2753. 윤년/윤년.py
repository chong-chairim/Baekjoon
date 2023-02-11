# 윤년은
# 연도가 4의 배수이면서, 100의 배수가 아닐 때 or
# 연도가 4의 배수이면서, 400의 배수일 때

A = int(input())

if A % 4 == 0 :
    if A % 400 == 0 :
        print("1")
    else:
        if A % 100 != 0 :
            print("1")
        else :
            print("0")
else :
    print("0")
