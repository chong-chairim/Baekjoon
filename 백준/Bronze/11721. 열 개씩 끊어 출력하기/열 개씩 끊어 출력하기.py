n = list(input()) # 문자열 입력받기 -> BaekjoonOnlineJudge
count = len(n)//10 + 1 # 문자열 길이에서 10으로 나눠서 몫 받아낸 뒤 실행을 1번 더 해야되니 1 더하기

for i in range(count) : # 구한 count 만큼 반복
    print("".join(n[10*i:10*(i+1)])) 

# list의 슬라이스를 0~9, 10~19, 20~29 ... 10개씩 나누기 위해 10*i : 10(i+1) 활용
# 그냥 출력하면 ['B', 'a', 'e', 'k', 'j', 'o', 'o', 'n', 'O', 'n'] ['l', 'i', 'n', 'e', 'J', 'u', 'd', 'g', 'e']으로 나오는데
# "".join() 사용해서 리스트 문자열 붙여서 출력