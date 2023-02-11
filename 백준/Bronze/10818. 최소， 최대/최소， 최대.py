N = int(input())

arr = list(map(int,input().split())) # input()으로 들어온 문자열을 split()으로 공백을 기준으로 문자열 분리하여 리스트로 반환한 뒤, int에 의해 정수로 바뀜

print(min(arr), max(arr)) # 최소 min(), 최대 max()