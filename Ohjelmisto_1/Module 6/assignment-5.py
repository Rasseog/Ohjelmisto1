def filter_even_numbers(number_list):
    even_list = []
    for number in number_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(original_list)
print("Original list:", original_list)
print("List with even numbers only:", filtered_list)