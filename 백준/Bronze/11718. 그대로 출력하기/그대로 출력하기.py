while True :
    try :  # try - except 구문 # 입력값이 들어오면
        print(input())        # 그대로 출력
    except EOFError : # 입력값이 들어오지 않는다면
        break         # ctrl+d를 누르면 EOF(End Of File)가 나옴 