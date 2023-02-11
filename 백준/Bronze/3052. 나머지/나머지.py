# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구함
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램 작성 >> 중복이 없어야 하니깐 set()에 넣은다음 len()으로 출력해주면 될듯?

result = []   # 빈 리스트 선언

for i in range(10):
    a = int(input()) % 42   # 입력받은 수를 42로 나눠서 생긴 나머지를 a로 선언
    result.append(a)        # a를 append로 리스트에 넣음

result = len(set(result))   # 중복이 없어야 하니 set()으로 리스트를 집합으로 만든 뒤 len()으로 집합의 길이 구해서 출력
print(result)