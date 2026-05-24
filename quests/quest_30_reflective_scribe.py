# Reflective Scribe
# This file contains commented versions of previous programs
# to explain what each part does.

# -----------------------------
# 1. FizzBuzz with comments
# -----------------------------

# Loop through numbers from 1 to 100
for number in range(1, 101):

    # Check if number is divisible by BOTH 3 and 5 first
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # Check if divisible by 3 only
    elif number % 3 == 0:
        print("Fizz")

    # Check if divisible by 5 only
    elif number % 5 == 0:
        print("Buzz")

    # If none of the conditions match, print the number
    else:
        print(number)


# -----------------------------
# 2. Calculator with comments
# -----------------------------

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Ask the user for input and convert to float for decimals
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add or subtract): ")

# Use conditional logic to call the correct function
if operation == "add":
    print(add(num1, num2))
elif operation == "subtract":
    print(subtract(num1, num2))
else:
    print("Invalid operation")


# -----------------------------
# 3. Number Guessing Game with comments
# -----------------------------

secret_number = 7  # The correct number
guess = None       # Start with no guess

# Keep looping until the user guesses correctly
while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")

