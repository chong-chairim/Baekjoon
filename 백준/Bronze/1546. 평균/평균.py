# 자기 점수 중에 최댓값을 골랐다 >> 이 값을 M
# 모든 점수를 점수/M * 100 으로 고쳤다
# 첫 줄에 시험 본 과목의 개수 N이 주어짐

M = int(input())
score = list(map(int, input().split()))
s_max = 0
s_sum = 0

for i in range(M):
    s_max = max(score)
    s_sum += (score[i] / s_max) * 100

print(s_sum/M)