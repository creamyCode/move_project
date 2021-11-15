

numbers = input()
# numbers = '0001100'
arr_numbers = list(map(int, numbers))

count = 0
tot = 0
while sum(arr_numbers) != 0 and sum(arr_numbers) != len(arr_numbers):
    less_num = 1 if arr_numbers.count(1) < arr_numbers.count(0) else 0
    str_numbers = ''.join(map(str, arr_numbers))
    start = str_numbers.index(str(less_num))
    end = str_numbers.rindex(str(less_num)) + 1
    for i in range(start, end):
            arr_numbers[i] = 1 if arr_numbers[i] == 0 else 0
    count += 1
    tot = sum(arr_numbers)
print(count)
