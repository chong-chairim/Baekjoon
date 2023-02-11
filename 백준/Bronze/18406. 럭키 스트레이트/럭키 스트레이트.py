# 럭키 스트레이트라는 기술은 매우 강력한 대신에 항상 사용은 불가하며, 현재 게임 내에서 점수가 특정 조건을 만족할 때만 사용 가능
# 특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때
# 점수 N을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미

# 현재 점수 N이 주어졌을 때 럭기 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오.
# 럭키 스트레이트를 사용할 수 있다면 LUCKY를, 사용할 수 없다면 READY를 출력
# 정수 N의 자릿수는 항상 짝수 형태로만 주어짐, 자릿수가 홀수인 수는 입력으로 들어오지 않음


# import sys
# input = sys.stdin.readline

N = input()
L = len(N)
div = len(N)//2
M = int(N)
left = 0
right = 0

for i in range(L):
    
    if i < div :
        right += M % 10 # 나머지를 입력받고 
        M = M // 10     # 몫을 다시 대입

    else:
        left += M % 10 # 나머지를 입력받고 
        M = M // 10     # 몫을 다시 대입


if left == right :
    print("LUCKY")
else:
    print("READY")
