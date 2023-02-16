T = int(input())


for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    P  = []  # 리스트로 받아준다음 조인해서 출력

    for j in range(len(S)):
        P.append(S[j] * R)
    print(''.join(P))