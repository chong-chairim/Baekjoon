li = []
for i in range(5):
    li.append(int(input()))

li.sort() # 정렬시키면 index=2인 숫자가 중앙값일 것

print(int(sum(li) / 5)) # 합을 5로 나누면 float가 되어서 int를 씌워줘야 하는데 안씌워줘서 틀림!
print(li[2])

# sum() 함수 쓰는 법 자꾸 까먹는다 # sum 함수 안에 리스트 이름 집어넣는거 잊지 말기