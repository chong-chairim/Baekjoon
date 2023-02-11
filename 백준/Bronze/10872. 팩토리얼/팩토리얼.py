N = int(input())
fac = 1

for i in range(N) :    # 팩토리알은 특정 수
    fac = fac * (i+1)  # i가 0부터 시작하니 1을 더해줘야함

print(fac)