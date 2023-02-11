# 테스트 케이스의 개수 T 입력받기
T = int(input()) 

# P(N)의 N값을 테스트 케이스 개수만큼 받기
for i in range(T) :
    list = [1,1,1] # 초깃값을 아니깐 리스트에 먼저 입력을 해두면 그 뒤에 수열 계산이 가능함
    N = int(input())

    for i in range(N) : # 변수를 따로 지정해주면 안되는게 나는 받은 T값을 사용해서 for문을 돌려야 하기 때문이다 j로 지정해주면 내가 j를 다시 i로 받아야됨
        list.append(list[i] + list[i+1]) # append는 리스트 인덱스를 주고 삽입하는게 아니라 그냥 for문 돌동안 계속 값을 뒤로 삽입해주는것
        
    print(list[N-1]) # 내가 계산한건 n1부터였고, 배열은 0부터니깐 출력은 n-1로 해야되는게 맞다