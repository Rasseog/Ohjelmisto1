def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

my_list = [3, 5, 7, 10]
result = sum_of_list(my_list)
print(result)
