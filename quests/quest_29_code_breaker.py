# Code Breaker – 3 Attempts to Guess the Secret Code

secret_code = 42
attempts = 3

print("Welcome to Code Breaker")
print("You have 3 attempts to guess the secret code.")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_code:
        print("Access Granted!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong code. Attempts left: {attempts}")
        else:
            print("Access Denied. No attempts left.")

