# 한수는 지금(x,y)에 있다.
# 왼쪽 아래 꼭짓점은 0, 0
# 오른쪽 위 꼭짓점은 w,h
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램 작성

# 첫 줄에 x y w h 주어짐

x, y, w, h = map(int, input().split())
i = 0
count_w = 0  # x에서 w까지 앞으로 가는거
count_h = 0  # y에서 h까지 앞으로 가는거 
count_x0 = 0 # x에서 0까지 앞으로 가는거
count_y0 = 0 # y에서 0까지 앞으로 가는거
li = []

count_x0 = x
count_y0 = y

while not (x == w):
    x += 1
    count_w += 1

while not (y == h):
    y += 1
    count_h += 1



li = [count_w, count_h, count_x0, count_y0]

print(min(li))