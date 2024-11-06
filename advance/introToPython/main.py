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


# Milestone #2: Adding in All Planets
from typing import Dict

# Defining a constant dictionary


# - Mercury: 37.6%

# - Venus: 88.9%

# - Mars: 37.8%

# - Jupiter: 236.0%

# - Saturn: 108.1%

# - Uranus: 81.5%

# - Neptune: 114.0%
PLANETS_GRAVITY: Dict[str, float] = {
    "mercury": 37.6 / 100,
    "venus": 88.9 / 100,
    "mars": 37.8 / 100,
    "jupiter": 236 / 100,
    "saturn": 108.1 / 100,
    "uranus": 81.5 / 100,
    "neptune": 114 / 100
}

def main() -> None:
    """Main function to calculate and display weight on different planets."""
    # Displaying welcome message
    print("Welcome to Planetary Weight Calculator")
    
    # Taking input from user
    try:
        earth_weight: float = float(input("Enter your weight on Earth (in kg) --> "))
        if earth_weight <= 0:
            print("Weight must be a positive number.")
            return
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        return
    
    planet: str = input("Enter the planet in which you want to see the weight --> ").lower().strip()
    
    # Converting weight to the specified planet
    try:
        planet_weight: float = round(PLANETS_GRAVITY[planet] * earth_weight, 2)
        print(f"Your weight on {planet.capitalize()} would be {planet_weight} kg.")
    except KeyError:
        print(f"Sorry, we don't have the gravity data for '{planet}'.")
        return  

if __name__ == '__main__':
    main()
