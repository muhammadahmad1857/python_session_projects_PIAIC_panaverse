
# Random Number Generator

This project generates a specified number of random integers within a given range. It showcases the use of Python's random number generation capabilities.

## Table of Contents

- [Overview](#overview)
- [How to Play](#how-to-play)
- [Code Explanation](#code-explanation)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Random Number Generator program generates a total of 10 random numbers between 1 and 100 and prints them to the console. Each number is generated independently, providing a fun way to demonstrate randomization in programming.

## How to Play

1. Run the program in your terminal.
2. The program will generate and display 10 random numbers between 1 and 100.

## Code Explanation

The code consists of the following key components:

1. **Imports**:
   - `random`: This library is used to generate random numbers.

2. **Constants**:
   - `TOTAL_NUMBERS`: Defines the total number of random numbers to generate (set to 10).
   - `MIN_LIMIT`: The minimum value for the random number (set to 1).
   - `MAX_LIMIT`: The maximum value for the random number (set to 100).

3. **Main Function**:
   - A `for` loop iterates over the range of total numbers.
   - Inside the loop, `random.randint(MIN_LIMIT, MAX_LIMIT)` generates a random integer between the defined limits.
   - Each generated number is printed to the console with its index.

## Requirements

- Python 3.x
- No additional libraries are required.

## Running the Program

To run the program, save the code in a file named `random_number_generator.py` and execute it in your terminal:

```bash
python random_number_generator.py
```
