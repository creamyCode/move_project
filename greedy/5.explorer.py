n = input()
peoples = sorted(map(int, input().split(' ')), reverse=True)

cnt = 0
while len(peoples) > 0 and max(peoples) <= len(peoples):
    max_n = max(peoples)
    peoples = peoples[max_n:]
    cnt += 1

print(cnt)

