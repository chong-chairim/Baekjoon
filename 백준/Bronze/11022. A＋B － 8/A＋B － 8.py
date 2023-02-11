T = int(input())

for i in range(T) :
    a, b = map(int, input().split())
    c = a + b
    print("Case #" + str(i+1) + ": " + str(a) + " + " + str(b) + " = " + str(c))