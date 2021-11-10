numbers = list(map(int, input()))

total = numbers[0]
for i in range(len(numbers) - 1):
    sum = total + numbers[i + 1]
    mul = total * numbers[i + 1]
    total = sum if sum > mul else mul
    
print(total)