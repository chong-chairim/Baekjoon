N = int(input()) # N 입력받기

for i in range(1, 2*N) : # 2N-1번 반복
    
    if(i > N) :    # 만약 i가 N보다 크다면
        a = i - N  # i값에서 N만큼 빼기
        print(" "*a + "*"*(N-a))
    else :         # 만약 i가 N보다 크지 않으면
        print(" "*(N-i) + "*"*i)