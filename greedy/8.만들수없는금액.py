cnt = int(input())
coins = list(map(int, input().split(' ')))

coins.sort()

num = 1
for coin in coins:
    if num < coin:
        break
    num += coin
print(num)


# 1 1 1 2 3 9
# 2 3 4 6 9 18

# 1 1 2 3 9
# 2 3 5 8 
# 1을 기준으로 작은 동전부터 하나씩 더해가며 만족여부 체크
# 마지막 동전까지 썼을경우 총합보다 +1되니 해당 수가 만들수 없는 최소수

# 중간 금액이 왜 체크되는지 이유는 모르겠음;;