import sys
input = sys.stdin.readline

s = input()

for i in range(26) : # 알파벳의 개수만큼 for문을 돌리기

    if i < 25 :
        print(s.find(chr(i+97)), end=' ') # 아스키 코드를 사용 # chr은 숫자를 아스키코드로 바꿔주는 함수
    else :
        print(s.find(chr(i+97)), end='')  # 맨 마지막에 띄어쓰기는 출력되면 안되기 때문에 else로 뺌