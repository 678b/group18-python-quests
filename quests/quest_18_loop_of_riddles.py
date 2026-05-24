secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    
    if guess != secret_number:
        print("Wrong! Try again.")

print("Correct! You guessed it!")
