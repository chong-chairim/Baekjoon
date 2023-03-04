N = int(input())
coin = []

for i in range(N):
    K = list(map(int, input().split()))
    coin.append(K)

# print(coin)
dp = [[0] * i for i in range(1, N+1)] # 여기서 막혔었음 # 초기값 만들어주는거 중요
dp[0][0] = coin[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + coin[i][j]
        elif i == j :
            dp[i][j] = dp[i-1][j-1] + coin[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + coin[i][j]

print(max(dp[-1]))