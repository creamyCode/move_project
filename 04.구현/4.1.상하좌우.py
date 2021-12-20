N = int(input())
commands = input().split(' ')

point = [1,1]

for command in commands:
    if command == 'L' and point[0] > 1:
        point[0] -= 1
    elif command == 'R' and point [0] < N:
        point[0] += 1
    elif command == 'U' and point [1] > 1:
        point[1] -= 1
    elif command == 'D' and point[1] < N:
        point[1] += 1

print(str(point[1]) + ' ' + str(point[0]))
    
    
        