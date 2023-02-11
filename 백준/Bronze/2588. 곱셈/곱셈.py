a = int(input())
b = input()

print(a * int(b[-1])) # 문자열은 인덱스 사용 가능하니 뒤에서부터 차례대로 받아서 int시키기
print(a * int(b[-2]))
print(a * int(b[-3]))
print(a * int(b))