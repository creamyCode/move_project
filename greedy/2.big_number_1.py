
p = list(map(int, input().split(' ')))
numbers = map(int, input().split(' '))
number_list = sorted(numbers, reverse=True)

M = p[1]
K = p[2]

limit = 0
sum = 0
for i in range(M):
    if limit < K:
        sum += number_list[0]
        limit = limit + 1
    else:
        sum += number_list[1]
        limit = 0

print(sum)