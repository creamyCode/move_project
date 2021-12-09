data = list(map(int, input()))
count0 = 0  # 0으로 바꾸는 카운트
count1 = 0  # 1로 바꾸는 카운트

# 111111, 00000 경우 대응하기위함
# 110011 => count0 = 2, count1 = 1
# 맨앞, 뒷수가 다른경우로 체크하면 대응가능!!!!!!!!!!
# 앞뒤가 다른경우는 10, 01 이고 뒤에 나타난 수를 바꾼다면 10은 count1 = 1, 01은 count1 = 1, 
if data[0] == 1:
    count0 += 1
else:
    count1 += 1

# 앞에서 2개씩 비교, 앞뒤 수가 불일치할 경우 카운트 증가
# 01, 10 에서 앞은 연속된 수니 뒷수를 기준으로 카운트 처리
# 01 => count0 증가, 10 => count1 증가
for i in range(len(data) - 1):
    # print(data[i], data[i + 1])
    if data[i] != data[i + 1]:
        if data[i + 1] == 1:
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))