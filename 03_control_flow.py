# Control Flow - Making decisions and repeating actions

# If statements - making decisions
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Comparison operators
temperature = 25
if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's nice weather")
elif temperature > 10:
    print("It's cool")
else:
    print("It's cold!")

# For loops - repeating actions
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Looping through a list
fruits = ["apple", "banana", "orange"]
print("\nMy favorite fruits:")
for fruit in fruits:
    print(f"I like {fruit}")

# While loops - repeating until a condition is met
print("\nCounting down:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Nested loops
print("\nMultiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")

# Break and continue
print("\nNumbers 1-10, skipping 5:")
for num in range(1, 11):
    if num == 5:
        continue  # Skip this iteration
    print(num)

print("\nNumbers 1-10, stopping at 7:")
for num in range(1, 11):
    if num == 7:
        break  # Exit the loop
    print(num)