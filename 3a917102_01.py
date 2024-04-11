def get_even_squares(num_list):
    return [x**2 for x in num_list if x % 2 == 0]

def get_odd_cubes(num_list):
    cubes = []
    for num in num_list:
        if num % 2 != 0:
            cubes.append(num ** 3)
    return cubes

def get_sliced_list(num_list):
    return num_list[4:]

def format_numbers(numbers):
    formatted_numbers = []
    for num in numbers:
        formatted_numbers.append(f"{num:8}")
    return formatted_numbers

if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    even_squares = get_even_squares(num_list)
    odd_cubes = get_odd_cubes(num_list)
    sliced_list = get_sliced_list(num_list)

    formatted_even_squares = format_numbers(even_squares)
    formatted_odd_cubes = format_numbers(odd_cubes)
    formatted_sliced_list = format_numbers(sliced_list)

    print(", ".join(formatted_even_squares))
    print(", ".join(formatted_odd_cubes))
    print(", ".join(formatted_sliced_list))
