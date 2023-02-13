# 테스트 케이스의 개수 C
# 각 테스트 케이스마다 학생의 수 N
# 그 뒤 이어서 N명의 점수 (0~100)
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력

C = int(input())

for i in range(C):

    li = []
    N = 0
    hab = 0
    count = 0
    per = 0

    li = list(map(int, input().split()))

    N = li[0]
    li = li[1:]
#    print(f'N : {N}')

    hab = sum(li)
#    print(f'hab : {hab}')
#    print(len(li))

    for j in range(len(li)):
        if li[j] > (hab/len(li)) :
            count += 1
#    print(f'count : {count}')

    per = (count/len(li)) * 100

    print(f'{per:.3f}%')  # 출력 조심