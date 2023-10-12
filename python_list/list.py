#!/usr/bin/python3.6

if __name__ == '__main__':
    # Create an empty list
    empty_list = []

    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Create a list of strings
    strings = ["apple", "banana", "cherry"]

    # Create a list of mixed types
    mixed_list = [1, "apple", 3.14]

    print('Total Numbers = ', numbers)
    # Get the first item in a list
    first_item = numbers[0]
    print('first_item = ', first_item)

    # Get the last item in a list
    last_item = numbers[-1]
    print('last_item = ', last_item)

    # Get a slice of a list
    list_slice = numbers[1:3]
    print('list_slice = ', list_slice)

    # Get the index of an item in a list
    index = numbers.index(2)
    print('index = ', index)

    # Add an item to the end of a list
    numbers.append(6)

    # Insert an item into a list at a specific index
    numbers.insert(2, 3.5)

    # Remove an item from a list
    numbers.remove(3)
    print('Total Numbers = ', numbers)

    # Pop an item from a list
    popped_item = numbers.pop()
    print('popped_item = ', popped_item)

    # Iterate over a list using a for loop
    for number in numbers:
        print(number)

    # Iterate over a list using a while loop
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1

    # Sort a list in ascending order
    numbers.sort()

    # Sort a list in descending order
    numbers.sort(reverse=True)
    print('sort numbers = ', numbers)

    # Create a list of even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print('even_numbers = ', even_numbers)

    # Create a list of numbers greater than 3
    greater_than_three = list(filter(lambda x: x > 3, numbers))
    print('greater_than_three = ', greater_than_three)

    # Square each number in a list
    squared_numbers = list(map(lambda x: x * x, numbers))
    print('squared_numbers = ', squared_numbers)

    # Convert each string in a list to uppercase
    uppercase_strings = list(map(lambda x: x.upper(), strings))
    print('uppercase_strings = ', uppercase_strings)

