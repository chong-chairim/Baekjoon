n = int(input()) # 주어지는 명령의 수

a = [] # 주어지는 명령을 저장할 리스트
b = [] # 스택으로 활용할 리스트

for i in range(n): # 주어지는 명령을 하나씩 리스트에 저장
    a.append(input())


for i in range(n): # 주어지는 명령의 수만큼 for문 돌리기

    if 'push' in a[i]:       # push 명령
        strings = a[i].split()  # push가 들어있는 문자열 나누기
        b.append(strings[1])    # push 할 숫자를 찾아서 넣기
    
    elif 'pop' in a[i]:      # pop 명령
        if(len(b) == 0):        # 스택에 들어있는 정수가 없는 경우
            print(-1)           # -1 출력
        else:                   # 스택에 들어있는 정수가 있는 경우
            print(b[len(b)-1])  # 스택의 가장 위에 있는 정수를 출력한 뒤
            b.pop()             # 스택의 가장 위에 있는 정수를 빼버림

    elif 'size' in a[i]:     # size 명령
        print(len(b))           # len 함수 사용해서 길이 출력

    elif 'empty' in a[i]:    # empty 명령
        if(len(b) == 0):        # 스택이 비어있으면 1
            print(1)
        else:                   # 스택이 채워져있으면 0
            print(0)

    elif 'top' in a[i]:      # top 명령
        if(len(b) == 0):        # 스택이 비어있으면
            print(-1)           # -1 출력
        else:                   # 스택이 채워져있으면
            print(b[len(b)-1])  # 스택의 가장 위에 있는 정수를 출력