n, k = map(int, input().split(' '))

cnt = 0
# while n != 1:
#     cnt += 1
#     if (n % k) == 0:
#         n /= k
#     else:
#         n -= 1

# 위 식 개선 ver 빼는부분 간소화
while n != 1:
    cnt += 1
    if (n % k) == 0:
        n /= k
    else:
        t = n % k
        cnt + t - 1
        n -= t

print(cnt)