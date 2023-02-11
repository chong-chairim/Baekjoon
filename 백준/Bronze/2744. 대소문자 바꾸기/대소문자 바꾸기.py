a = input()

for i in a :    # 입력받은 문자 만큼 for 문 돌리기
    if i.isupper() == True : # 받은 문자열 i가 대문자라면 True를 반환하니 동일한지 확인
        i = i.lower()        # 대문자면 lower() 함수를 써서 소문자로 변환
        print(i, end='')     # 문자 하나씩 쪼개서 출력하면 안되니 end=''로 줄바꿈 없앰
    else :                   # 받은 문자열 i가 소문자라면
        i = i.upper()        # upper() 함수를 써서 소문자로 변환
        print(i, end='')     # end=''로 줄바꿈 없앰