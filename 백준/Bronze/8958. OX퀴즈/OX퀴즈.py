# O 문제를 맞은 것
# X 문제를 틀린 것
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# O O X X O X X O O O
# 1+2+0+0+1+0+0+1+2+3 = 10점

T = int(input()) # 테스트 케이스 개수
score = 0
hap = 0

for i in range(T) :
    s = input()

    for j in range(len(s)) :
#        print(s[j])

        if s[j] == 'O' :

            if hap > 0 :            # 여기서 아래 score 해준 뒤 hap을 해줘서 최종 결과 오류가 났던 것
                hap += 1     # O의 합 누적시키기   
                score += hap # hap만큼 점수에 더해주기 
#               print(f'hap:{hap} score:{score}')

            else :
                score += 1  # 점수 1 증가
                hap += 1    # 첫 O이니 1 증가
#               print(f'hap:{hap} score:{score}')
        else:
            hap = 0         # 합 초기화
#           print(f'hap:{hap} score:{score}')

    print(score)

    # 같은 for문 안에서 도니깐 초기화를 꼭 시켜줘야함
    score = 0
    hap = 0

# 스터디원 반짝님 코드
# case_number = int(input())

# for i in range(case_number):
#     each_case = list(input())
#     num = 0
#     result = 0
#     for k in each_case:
#         if k == "O":
#             num += 1
#             result += num
#         else:
#             num = 0
#     print(result)
