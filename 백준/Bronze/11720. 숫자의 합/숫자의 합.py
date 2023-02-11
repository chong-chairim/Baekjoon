N = int(input()) # 숫자의 개수 N
n = list(map(int, input())) # 숫자 N개 공백없이 문자열로 들어오는거 list로 받기
# print(n) -> [1,2,3,4,5]  # 그럼 리스트에 문자열이 한 문자씩 쪼개서 입력됨
print(sum(n)) # 문자를 sum()으로 더하면 끝

"""
N = int(input())
nums = input()
total = 0
for i in range(N) :
    total += int(nums[i])
print(total)
"""