N, k = map(int, input().split()) # N 응시자 수, k 상 받는 수

li = list(map(int, input().split())) # 점수들 리스트에 넣기

li.sort() # 리스트 정렬

print(li[-k]) # 뒤부터 거꾸로 k만큼 세면 상을 받는 점수가 뭔지 알 수 있음