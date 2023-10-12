#!/usr/bin/python3.6

if __name__ == '__main__':
    # Create a dictionary
    my_dict = {"name": "Bard", "age": 1, "occupation": "language model"}

    # Access the value of a key
    print(my_dict["name"])

    # Add a new key-value pair to the dictionary
    my_dict["skills"] = ["writing", "translation", "code generation"]

    # Print the dictionary
    print(my_dict)

    # Remove a key-value pair from the dictionary
    del my_dict["age"]

    # Print the dictionary again
    print(my_dict)

    # Create a dictionary of countries and their capitals
    countries = {
        "India": "New Delhi",
        "China": "Beijing",
        "United States": "Washington, D.C.",
    }

    # Get the capital of a country
    print(countries["India"])

    # Iterate over the dictionary
    for country, capital in countries.items():
        print(f"{country}'s capital is {capital}.")

