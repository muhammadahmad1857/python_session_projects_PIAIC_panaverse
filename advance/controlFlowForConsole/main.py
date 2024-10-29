import random

# Defining constants
MAX_ROUNDS:int = 5 
MAX_LIMIT:int = 100
MIN_LIMIT:int = 1

def main():
    # Milestone 1: Showing welcome message
    print('Welcome to the High-Low Game!')
    curr_round:int = 1
    score:int = 0
    
    # Milestone 4: Play multiple rounds
    while curr_round <= MAX_ROUNDS:
        print(f'Round {curr_round}:')
        
        # Milestone 1: Generate the random numbers
        your_num:int = random.randint(MIN_LIMIT, MAX_LIMIT)
        comp_num:int = random.randint(MIN_LIMIT, MAX_LIMIT)
        print(f"Your number: {your_num}")
        
        # Milestone 2: Get the user choice
        user_guess = input("Do you think your number is higher or lower than the computer's? ").lower().strip()
        
        # Extension 1: Safeguard user input
        while user_guess not in ["higher", "lower"]:
            user_guess = input("Please enter either 'higher' or 'lower': ").lower().strip()
        
        # Milestone 3: Write the game logic
        higher_win:bool = user_guess == 'higher' and your_num < comp_num
        lower_win:bool = user_guess == 'lower' and your_num > comp_num
        
        if higher_win:
            print(f"You were right! The computer's number was {comp_num}")
            score += 1
        elif lower_win:
            print(f"You were right! The computer's number was {comp_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")
        
        # Milestone 5: Adding a points system
        print(f"Your score is now {score}\n")
        
        curr_round += 1
    
    # Extension 2: Conditional ending messages
    if score == MAX_ROUNDS:
        print(f"Your score is now {score}. Wow! You played perfectly!")
    elif score >= MAX_ROUNDS // 2:
        print(f"Your score is now {score}. Good job, you played really well!")
    else:
        print(f"Your score is now {score}. Better luck next time!")

if __name__ == "__main__":
    main()
