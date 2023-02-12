# 정수 N의 가장 뒤 두 자리를 적절히 바꿔서 N을 F로 나누어 떨어지게 하려고 함
# 만약 가능한 것이 여러가지이면, 뒤 두 자리를 가능한 한 작게 만듦

# N = 275, F = 5 답은 00
# 200이 5로 나누어 떨어지는 것 중 가장 작기 때문

# N = 1021, F = 11  답은 01
# 1001이 11로 나누어 떨어지기 때문

N = int(input()) # 100보다 크거나 같고 20억보다 작거나 같음
F = int(input()) # 100보다 작거나 같음
S = []
result = 0

a = (N // 100) * 100 
b = ((N // 100) + 1) * 100

while (a < b): # 어짜피 백의자리부터 바뀌면 안되니깐 뒤에 자릿수는 0~99 안에서 찾아야해서 최대 100번만 돌면 된다
    
    if a % F == 0 :
        result = a
        break
    a += 1

result = str(result)

print(result[-2:])


# 시간초과 났던 코드
'''
N = int(input()) # 100보다 크거나 같고 20억보다 작거나 같음
F = int(input()) # 100보다 작거나 같음
S = []
i = 0
sub = 0
result = 0

while True :
    i += 1
    sub = F * i

    if sub // 100 == N // 100 :
        S.append(sub)
        break

result = sub % 100

if result < 10 :
    print(('0' + str(result)))
else:
    print(result)
'''