hour = int(input())

cnt = 0
for h in range(hour + 1):
    for m in range(60):
        for n in range(60):
            if '3' in str(h) + str(m) + str(n):
                cnt += 1

print(cnt)
