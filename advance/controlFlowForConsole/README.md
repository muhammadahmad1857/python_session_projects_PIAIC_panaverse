
# High-Low Game

Welcome to the **High-Low Game!** This is a simple Python game where you compete against the computer by guessing whether your randomly generated number is higher or lower than the computer's number. Test your luck and see how many rounds you can win!

## Table of Contents

- [Description](#description)
- [How to Run](#how-to-run)
- [Code Explanation](#code-explanation)
- [Game Logic](#game-logic)
- [Conditional Ending Messages](#conditional-ending-messages)

## Description

In this game, both you and the computer are assigned random numbers between 1 and 100. You can see your number, but not the computer's. You need to guess whether your number is higher or lower than the computer's number. You earn points for correct guesses over multiple rounds.

## How to Run

To run the game, follow these steps:

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Copy the code into a Python file, for example, `high_low_game.py`.
3. Open your terminal or command prompt.
4. Navigate to the directory where you saved the file.
5. Run the game with the command:
   ```bash
   python high_low_game.py
   ```
````

## Code Explanation

### Imports

```python
import random
```

This line imports the `random` module, which is used to generate random numbers.

### Constants

```python
MAX_ROUNDS:int = 5
MAX_LIMIT:int = 100
MIN_LIMIT:int = 1
```

These constants define the maximum number of rounds the game will play and the range of random numbers.

### Main Function

```python
def main():
```

The main function contains the game logic.

### Welcome Message

```python
print('Welcome to the High-Low Game!')
```

Displays a welcome message to the player.

### Game Loop

```python
while curr_round <= MAX_ROUNDS:
```

The game runs for a defined number of rounds.

### Random Number Generation

```python
your_num = random.randint(MIN_LIMIT, MAX_LIMIT)
comp_num = random.randint(MIN_LIMIT, MAX_LIMIT)
```

Generates random numbers for the player and the computer.

### User Input

```python
user_guess = input("Do you think your number is higher or lower than the computer's? ")
```

Prompts the player to guess whether their number is higher or lower than the computer's.

### Input Validation

```python
while user_guess not in ["higher", "lower"]:
```

Ensures that the user input is valid (either "higher" or "lower").

### Game Logic

```python
higher_win:bool = user_guess == 'higher' and your_num < comp_num
lower_win:bool = user_guess == 'lower' and your_num > comp_num
```

Checks the player's guess against the actual numbers to determine if they win.

### Score Update

```python
score += 1
```

Updates the score if the player's guess is correct.

### Ending Messages

```python
if score == MAX_ROUNDS:
    print(f"Your score is now {score}. Wow! You played perfectly!")
elif score >= MAX_ROUNDS // 2:
    print(f"Your score is now {score}. Good job, you played really well!")
else:
    print(f"Your score is now {score}. Better luck next time!")
```

Displays a message based on the player's performance at the end of the game.

## Game Logic

The game consists of a series of rounds where the player can earn points by making correct guesses. If the player's guess matches the truth (i.e., their number is higher or lower than the computer's), they earn a point. The game continues until all rounds are played.

## Conditional Ending Messages

At the end of the game, the player receives feedback based on their score:

- A perfect score (5 points) results in a "Wow! You played perfectly!" message.
- A score of at least half the rounds (rounded down) gives a "Good job, you played really well!" message.
- Any other score prompts the message "Better luck next time!"

---

Enjoy playing the **High-Low Game**, and may luck be on your side!

### Key Sections:

- **Description:** Overview of the game.
- **How to Run:** Instructions to set up and run the game.
- **Code Explanation:** Breakdown of the code structure and functionality.
- **Game Logic:** Brief description of the game mechanics.
- **Conditional Ending Messages:** Description of how the game evaluates player performance.

