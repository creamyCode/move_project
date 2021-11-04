n, m = map(int, input().split(' '))
board = []           # array를 써서 전체 메모리 크기는 커짐
for i in range(n):
    board.append(list(map(int, input().split(' '))))

# 여기서부터 계산
lows = map(min, board)
print(max(lows))