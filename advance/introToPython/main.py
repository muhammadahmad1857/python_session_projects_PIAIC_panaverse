# Milestone #1: Mars Weight
# MARS_GRAVITY:int = 37.8/100
# def main():
#     # displaying wleocme message
#     print("Welcome to Planetary Weight Calculator")

#     # taking input FROM USER
#     earth_weight = float(input("Enter your weight on earth(in kg) --> "))
    
#     # converting it by multiplying with eart weight and mars gravity
#     mars_weight:int = round(earth_weight * MARS_GRAVITY,2)
    
#     # displaying the calculated weight
#     print(f"Your weight on Mars would be {mars_weight} kg.")
    


# if __name__ == '__main__':
#     main()

from typing import Dict

# Define gravity factors for each planet relative to Earth
PLANETS_GRAVITY: Dict[str, float] = {
    "mercury": 37.6 / 100,
    "venus": 88.9 / 100,
    "mars": 37.8 / 100,
    "jupiter": 236 / 100,
    "saturn": 108.1 / 100,
    "uranus": 81.5 / 100,
    "neptune": 114 / 100
}

def get_earth_weight() -> float:
    """Prompt user for their Earth weight and validate input."""
    while True:
        try:
            weight = float(input("Enter your weight on Earth (in kg) --> "))
            if weight > 0:
                return weight
            print("Weight must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_planet() -> str:
    """Prompt user for the planet name and validate input."""
    while True:
        planet = input("Enter the planet to see your weight on it --> ").lower().strip()
        if planet in PLANETS_GRAVITY:
            return planet
        print(f"Sorry, we don't have the gravity data for '{planet}'.")

def calculate_weight(earth_weight: float, planet: str) -> float:
    """Calculate weight on a specified planet."""
    return round(PLANETS_GRAVITY[planet] * earth_weight, 2)

def main() -> None:
    """Main function to calculate and display weight on different planets."""
    print("Welcome to Planetary Weight Calculator")

    # Get validated user input for weight and planet
    earth_weight = get_earth_weight()
    planet = get_planet()
    
    # Calculate and display the weight on the selected planet
    planet_weight = calculate_weight(earth_weight, planet)
    print(f"Your weight on {planet.capitalize()} would be {planet_weight} kg.")

if __name__ == '__main__':
    main()
