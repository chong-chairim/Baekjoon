N = int(input())
nums = list(map(int, input().split()))
v = int(input())

count = 0

for i in range(N) :

    if nums[i] == v : # 만약 nums[i]가 찾으려는 수와 값이 동일하면
        count += 1    # count에 1을 더함

print(count)