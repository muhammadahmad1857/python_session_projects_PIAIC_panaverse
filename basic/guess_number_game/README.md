# Number Guessing Game

Welcome to the Number Guessing Game! This console-based game challenges players to guess a randomly generated number within a limited number of attempts.

## How to Play

1. Run the game in your terminal.
2. The computer will randomly select a number between 1 and 99.
3. You have a maximum of 5 attempts to guess the number.
4. After each guess, you'll receive feedback indicating whether your guess was too high, too low, or correct.
5. If you guess the number within the allotted attempts, you win. If not, the correct number will be revealed at the end.

## Code Explanation

The game is implemented in Python and consists of the following key components:

1. **Imports**:
   - `random`: This library is used to generate a random number.
   - `os`: Although imported, this library is not used in the current code.

2. **Constants**:
   - `MAX_ROUNDS`: This constant defines the maximum number of attempts a player has to guess the number (set to 5).

3. **Main Function**:
   - The game starts with a welcome message.
   - A random number between 1 and 99 is generated using `random.randint(1, 99)`.
   - A `while` loop allows the player to make guesses until they either guess correctly or exhaust their attempts.

4. **User Input**:
   - The player is prompted to enter their guess.
   - The input is compared with the randomly generated number:
     - If the guess is too high, a message indicates this along with the remaining attempts.
     - If the guess is too low, a similar message is displayed.
     - If the guess is correct, a congratulatory message is shown, and the loop breaks.

5. **End of Game**:
   - If the player uses all their attempts without guessing correctly, a message reveals the correct number.

To run the game, save the code in a file named `number_guessing_game.py` and execute it in your terminal.

