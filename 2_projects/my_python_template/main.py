#!/usr/bin/env python
# main.py

"""This module contains the main functionality for the project."""

from data import fruits, customer_data

def print_fruits():
    """Prints the list of fruits"""
    for fruit in fruits:
        print(fruit)


def access_customer_data():
    """Prints specific customer information from the dictionary"""
    print(f"Customer Name: {customer_data['name']}")


class Product:
    """Basic product class with attributes and a method"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        """Returns a string with product information"""
        return f"Product: {self.name}, Price: ${self.price}"


if __name__ == "__main__":
    print_fruits()
    access_customer_data()

    # Use uppercase for constant variable names
    PRODUCT_NAME = "T-Shirt"
    PRODUCT_PRICE = 19.99

    PROD1 = Product(PRODUCT_NAME, PRODUCT_PRICE)
    print(PROD1.get_info())
