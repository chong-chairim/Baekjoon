num = []
max_n = 0
index_n = 0

for i in range(9) :  # 9번 for문 돌려서
    num.append(int(input())) # input을 append 써서 리스트에 넣어주고
    max_n = max(num)         # max 함수 써서 max값 찾고              # max 안에 넣어줘야되는거 까먹네
    index_n = num.index(max_n) + 1  # max값으로 index 함수 써서 index 번호 찾기 # 그리고 0부터 카운팅하니깐 1 더해주기
    
# print(num)
print(max_n)
print(index_n)