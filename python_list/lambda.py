#!/usr/bin/python3.6

if __name__ == '__main__':
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Create a list of strings
    strings = ["apple", "banana", "cherry"]

    print('numbers = ', numbers)
    print('strings = ', strings)

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

