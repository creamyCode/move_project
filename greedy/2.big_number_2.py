# 수열응용
# M 더할수 있는 횟수, K 연속해서 더할 수 있는 횟수
N, M, K = map(int, input().split(' '))
numbers = map(int, input().split(' '))
number_list = sorted(numbers, reverse=True)

one_loop_num = number_list[0] * K + number_list[1]
loop_cnt = M // (K + 1)
t = M % (K + 1)

print((loop_cnt * one_loop_num) + (t * number_list[0]))
