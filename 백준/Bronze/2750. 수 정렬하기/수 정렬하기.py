N = int(input())
li = []

for i in range(N):
    li.append(int(input())) # 입력받는대로 리스트에 넣기 # input에 int를 안씌워줘서 틀렸던 것

li.sort()     # sort() 함수로 리스트 정렬하기 

for i in range(N): # for문 돌려서 리스트 하나씩 출력
    print(li[i])