

# numbers = input()
numbers = '000100010'
t = range(3, 7)
print(list(t))
zero_cnt = numbers.count('0')
one_cnt = len(numbers) - zero_cnt
less_num = 1 if zero_cnt > one_cnt else 0


print(numbers.find(str(less_num)))
print(numbers.rfind(str(less_num)))

# for i in range(3, 7)
# numbers[i] = 1 if numbers[i] == 0 else 0
