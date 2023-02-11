# 6눈 주사위 3개를 던지기
# 조건 1) 같은 눈이 3개가 나오면 만원 + 같은눈 * 1000원
# 조건 2) 같은 눈이 2개가 나오면 천원 + 같은눈 * 100원
# 조건 3) 모두 다른 눈이 나오는 경우에는 그 중 가장 큰 눈 * 100원

a, b, c = map(int, input().split())
t = []
money = 0

if (a == b) and (b == c):   # 조건 1
    money = 10000 + a * 1000

elif (a == b) :             # 조건 2
    money = 1000 + a * 100

elif (b == c):
    money = 1000 + b * 100

elif (c == a):
    money = 1000 + c * 100

else:                       # 조건 3
     t = [a,b,c]
     money = max(t) * 100

print(money)