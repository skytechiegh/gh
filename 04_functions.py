# Functions - Reusable blocks of code

# Simple function with no parameters
def greet():
    print("Hello! Welcome to Python!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}! Nice to meet you!")

# Function with multiple parameters
def introduce(name, age, city):
    print(f"Hi! I'm {name}, I'm {age} years old, and I live in {city}.")

# Function that returns a value
def add_numbers(a, b):
    return a + b

# Function with default parameters
def greet_with_title(name, title="Mr./Ms."):
    print(f"Hello, {title} {name}!")

# Function that returns multiple values
def get_name_and_age():
    name = "Alice"
    age = 25
    return name, age

# Let's use our functions
print("=== Function Examples ===")

# Calling functions
greet()
print()

greet_person("Sarah")
print()

introduce("John", 30, "Boston")
print()

# Using return values
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")
print()

# Using default parameters
greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")
print()

# Getting multiple return values
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")
print()

# Function with a list parameter
def print_list(items):
    print("Items in the list:")
    for item in items:
        print(f"- {item}")

# Function that modifies a list
def add_item_to_list(my_list, item):
    my_list.append(item)
    print(f"Added {item} to the list")

# Using list functions
shopping_list = ["milk", "bread", "eggs"]
print_list(shopping_list)
add_item_to_list(shopping_list, "butter")
print_list(shopping_list)