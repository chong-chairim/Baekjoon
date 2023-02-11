nums = list(map(int, input().split())) # 여러 변수들을 리스트에 담고
result = 0

for i in range(len(nums)) : # 리스트의 길이만큼 for문을 돌리고
    result += nums[i] ** 2  # result에 i의 제곱을 더한뒤

print(result % 10) # 10으로 나눈 나머지를 검증수로 출력