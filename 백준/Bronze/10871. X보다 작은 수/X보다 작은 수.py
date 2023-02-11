N, X = map(int, input().split())  # N은 주어지는 수의 개수, X는 기준이 되는 수
nums = list(map(int, input().split()))


for i in range(N) :
    if nums[i] < X :
        print(nums[i], end=' ')