

# Lift Off Game

Welcome to the **Lift Off Game**! This Python program creates a simple countdown from 10 to 1, followed by a message saying "Liftoff!". It’s a great example of using loops and the `range()` function for countdowns.

## How It Works

1. The game starts with a welcome message.
2. A countdown from 10 to 1 is printed on the screen.
3. When the countdown reaches 1, the program displays "Liftoff!" to indicate the end of the countdown.

## Code Explanation

### Step-by-Step Breakdown

1. **Function Definition - `main()`**

   - The `main()` function contains the main logic for the countdown.

2. **Welcome Message**

   ```python
   print("Welcome to the lift off game!")
   ```

   - Displays a message welcoming the user to the game.

3. **Countdown Loop**
   ```python
   for i in range(10, 0, -1):
       print(i)
   ```
   - Uses the `range()` function to create a countdown list from 10 down to 1:
     - `10` is the starting point of the countdown.
     - `0` is the stopping point, which is non-inclusive, meaning the loop will stop before reaching this value.
     - `-1` is the step, meaning it counts down by 1 each time.

#### Explanation of `range()` Function

The `range(start, stop, step)` function generates a sequence of numbers based on three parameters:

- **`start`**: The first number in the sequence (here, 10).
- **`stop`**: The number at which the sequence stops (exclusive); here, it stops before reaching 0.
- **`step`**: The difference between each number in the sequence; here, `-1` creates a countdown by decreasing the number by 1 each iteration.

4. **Liftoff Message**

   ```python
   print("Liftoff!")
   ```

   - After the countdown finishes, this message is displayed to signify the end of the game.

5. **Script Execution Check**
   ```python
   if __name__ == "__main__":
       main()
   ```
   - Ensures that `main()` runs only when the script is executed directly, not when imported as a module.

## Sample Output

```bash
Welcome to the lift off game!
10
9
8
7
6
5
4
3
2
1
Liftoff!
```
