# Variables and Data Types in Python

# Strings - text data
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# Numbers - integers and floats
age = 25                    # integer
height = 5.6               # float (decimal)
weight = 65.5
print(f"Age: {age}, Height: {height} feet, Weight: {weight} kg")

# Boolean - True or False
is_student = True
is_working = False
print(f"Is student: {is_student}")
print(f"Is working: {is_working}")

# Lists - ordered collections
fruits = ["apple", "banana", "orange", "grape"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])  # Indexing starts at 0
print("Number of fruits:", len(fruits))

# Adding to a list
fruits.append("strawberry")
print("After adding strawberry:", fruits)

# Dictionaries - key-value pairs
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming"]
}
print("Person info:", person)
print("Person's name:", person["name"])
print("Person's hobbies:", person["hobbies"])

# Type checking
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of first_name: {type(first_name)}")
print(f"Type of is_student: {type(is_student)}")
print(f"Type of fruits: {type(fruits)}")
print(f"Type of person: {type(person)}")