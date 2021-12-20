idx = 'abcdefg'
input_str = input()
x = idx.index(input_str[0]) + 1
y = int(input_str[1])

moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1, -2), (-1, 2), (-1, -2)]
cnt = 0
for move in moves:
    x_move = x + move[0]
    y_move = y + move[1]
    if x_move >= 1 and x_move <= 8 and y_move >= 1 and y_move <= 8:
        cnt += 1

print(cnt)