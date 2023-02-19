N = int(input())
li = []

for i in range(N):
    a = input()
    li.append(a)

li = sorted(list(set(li)))  # --> 여기서 알파벳 순서로 정렬하기 위해 sorted가 한번 더 들어갔어야 함

li.sort(key=len)

for i in li:
    print(i)
