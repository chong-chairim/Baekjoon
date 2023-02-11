li = [int(input()) for _ in range(28)]  # 숙제를 제출한 28명을 리스트에 입력받고

for i in range(1,31) : # 원래 인원인 30명만큼 for 문을 돌림
    if i not in li:    # not in 함수를 써서 i에 해당하는 수가 있는지 없는지 확인하고
        print(i)       # 없으면 해당하는 수를 출력하면 누가 제출을 안했는지 알 수 있음