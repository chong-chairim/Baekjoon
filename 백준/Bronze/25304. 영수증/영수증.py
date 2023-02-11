# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액

# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사

# 영수증에 적힌 총 금액 X
# 영수증에 적힌 구매한 물건의 종류의 수 N
# 각 물건의 가격 a와 개수 b

X = int(input())
N = int(input())
money = 0

for i in range(N) :
    a, b = map(int, input().split())
    money += a * b  # money에 합을 다 쌓기

if money == X :
    print("Yes")
else:
    print("No")