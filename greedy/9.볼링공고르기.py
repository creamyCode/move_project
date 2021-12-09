# 예시 잘 보기 !!!!!!
# 서로무게가 다른 볼링공
# -> 수는 달라야 되지만 중복은 허용, a b 구분 없음 -> 뒤집었을때 같으면 안됨
# 1 3 2 3 2
# 1_3,1_2
n, m = map(int, input().split(' '))
balls = list(input().split(' '))

case = []

for a_idx in range(n):
    for b_idx in range(n):
        # 동일순서가 아니고, 같은무게 아니고, a와 b의 구분없어야 하니 뒤집어서 동일 공 순서가 없을경우 추가
        if a_idx != b_idx and balls[a_idx] != balls[b_idx] and not case.__contains__(str(b_idx) + str(a_idx)):
            case.append(str(a_idx) + str(b_idx))

print(len(case))