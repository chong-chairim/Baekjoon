# 0보다 크거나 같고, 99보다 작거나 같은 정수 N
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 2자리 수로 만들고, 각 자리의 숫자를 더한다
# 그 다음 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.

# 26이 주어짐
# 2 + 6 = 8 
# 새로운 수 6_8 68 #1
# 6 + 8 = 14 
# 새로운 수 8_4 84 #2
# 8 + 4 = 12 
# 새로운 수 4_2 42 #3
# 4 + 2 = 6 
# 새로운 수 2_6 26 #4

# 4번만에 원래 수로 돌아옴
# 26의 사이클의 길이는 4

# N이 주어졌을 때 N의 사이클의 길이를 구하는 프로그램 작성

N = int(input())
count = 0
num = 0
hap = -1

if N < 10:
    num = 0 + N
    hap = N * 10 + num
    count += 1
#    print(f'num: {num}, hap: {hap}, count: {count}')
else :
    num = (N // 10) + (N % 10)
    hap = ((N % 10) * 10) + (num % 10)
    count += 1
#    print(f'num: {num}, hap: {hap}, count: {count}')

while hap != N:

    num = (hap // 10) + (hap % 10)
    hap = ((hap % 10) * 10) + (num % 10)
    count += 1
#    print(f'num: {num}, hap: {hap}, count: {count}')

print(count)


"""
초반에 잘못 짠 코드
N = int(input())
count = 0
num = 0
hap = -1

while True:
    
    if hap == N :
        print(count)
        break

    else:
        if N < 10:
            num = 0 + N
            hap = N * 10 + num
            count += 1
            print(f'num: {num}, hap: {hap}, count: {count}')

        else :
            num = (N // 10) + (N % 10)
            hap = ((N % 10) * 10) + (num % 10)
            count += 1
            print(f'num: {num}, hap: {hap}, count: {count}')
"""