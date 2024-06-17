# !/usr/bin/python3.6
# cd /mnt/c/swap_wsl/swapnil_repo/python_test ; 
# /usr/bin/env /bin/python3 /home/swap/.vscode-server/extensions/ms-python.debugpy-2024.6.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher 39195 -- /mnt/c/swap_wsl/swapnil_repo/python_test/python_list/dictionary.py  
# python3 main.py

if __name__ == '__main__':
    # Create a dictionary
    my_dict = {"name": "Swapnil", "age": 40, "occupation": "Principle Architect"}

    # Access the value of a key
    print(my_dict["name"])

    # Add a new key-value pair to the dictionary
    my_dict["skills"] = ["Pre-Sales", "Project Managment", "Developer"]

    # Print the dictionary
    print(my_dict)

    # Remove a key-value pair from the dictionary
    del my_dict["age"]

    # Print the dictionary again
    print(my_dict)

    # Create a dictionary of countries and their visited places
    countries = {
        "India": "Pune",
        "China": "Beijing",
        "United States": "Las Vegas",
    }

    # Get the visited places of a country
    print(countries["India"])

    # Iterate over the dictionary
    for country, capital in countries.items():
        print(f"{country}'s visited places is {capital}.")

