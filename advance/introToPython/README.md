# README for Planetary Weight Calculator

## Project Overview

The **Planetary Weight Calculator** is a Python program that allows users to calculate their weight on different planets based on their weight on Earth. The program utilizes the gravity percentages of various planets to provide accurate weight conversions.

## Features

- Calculates weight on multiple planets including Mercury, Venus, Mars, Jupiter, Saturn, Uranus, and Neptune.
- User-friendly interface for input and output.
- Handles invalid planet names with an appropriate message.

## How to Use

1. Run the program.
2. Input your weight on Earth in kilograms.
3. Enter the name of the planet you wish to calculate your weight on (e.g., Mercury, Venus, Mars).
4. The program will display your weight on the selected planet.

## Code Explanation

The program begins by displaying a welcome message and prompting the user for their weight on Earth. It then multiplies this weight by the corresponding gravity factor of the specified planet, derived from a predefined dictionary.

### Constants

```python
PLANETS_GRAVITY = {
    "mercury": 37.6 / 100,
    "venus": 88.9 / 100,
    "mars": 37.8 / 100,
    "jupiter": 236 / 100,
    "saturn": 108.1 / 100,
    "uranus": 81.5 / 100,
    "neptune": 114 / 100
}
```

### Main Function

```python
def main():
    # displaying welcome message
    print("Welcome to Planetary Weight Calculator")

    # taking input FROM USER
    earth_weight = float(input("Enter your weight on earth(in kg) --> "))
    planet = input("Enter the planet in which you want to see the weight --> ").lower().strip()

    try:
        planet_weight = PLANETS_GRAVITY[planet] * earth_weight
        print(f"Your weight on {planet} would be {planet_weight:.2f} kg.")
    except KeyError:
        print(f"Sorry, we don't have the gravity data for '{planet}'.")
```

## Conclusion

This program provides an easy way for users to understand how their weight would change on different planets, enhancing their knowledge of planetary science.
