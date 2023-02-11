N, M = map(int, input().split()) # N과 M을 받음
A, B = [], [] # 빈 리스트 만들어놓기

for i in range(N) : # A의 배열 생성  # N번 돌리면서
        A.append(list(map(int, input().split()))) # 1 1 1 같은 문자열을 한번씩 더하면 이중 리스트가 만들어짐

for i in range(N) : # B의 배열 생성
        B.append(list(map(int, input().split())))        

for i in range(N) : # 행의 개수 N만큼 for문 돌리고
    for j in range(M) : # 열의 개수 M만큼 for 돌리고
        print(A[i][j] + B[i][j], end=' ') # end는 띄어쓰기로 설정해서 한 행이 2 2 2 같이 나오게 설정
    print() # 한 행의 입력이 끝나면 줄바꿈을 넣어 행렬의 모양을 갖추게 설정