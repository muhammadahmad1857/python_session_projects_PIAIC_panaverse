import random

# definging constants
MAX_ROUNDS:int = 5


def main():
    # showing welcome message
    print('Welcome to the Number Guessing Game!')
    attempts:int = 1
    random_num:int = random.randint(1, 99)  # Generate the random number 
    print("I am thinking of a number between 1 and 99.")

# adding a while loop that runs till the attempts finsifhes
    while attempts <= MAX_ROUNDS:
        
        user_input = int(input('Enter your guess --> ')) # taking input
# adding logic
        if user_input > random_num:
            print(f"The number {user_input} you guessed is greater than the computer's number. You have {MAX_ROUNDS - attempts} attempts left.")
        elif user_input < random_num:
            print(f"The number {user_input} you guessed is less than the computer's number. You have {MAX_ROUNDS - attempts} attempts left.")
        else:
            print('Congratulations! You guessed the correct number.')
            break  
        attempts+=1
    # if user doesn't get the number and finished his attemopts then printing this message
    print(f"\n\nYou've used all your attempts. The correct number was {random_num}. Better luck next time!")

if __name__ == "__main__":
    main()
