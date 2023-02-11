N_sugar = int(input())
count = 0

while(N_sugar > 0):
    
    if(N_sugar % 5 == 0):
        count += N_sugar/5
        N_sugar -= 5 * N_sugar/5
        break

    else:
        N_sugar -= 3
        count += 1

if(N_sugar == 0):
    print(int(count))
else:
    print(-1)