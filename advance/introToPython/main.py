# Milestone #1: Mars Weight
# MARS_GRAVITY = 37.8/100
# def main():
#     # displaying wleocme message
#     print("Welcome to Planetary Weight Calculator")
    
#     # taking input FROM USER
#     earth_weight = float(input("Enter your weight on earth(in kg) --> "))
    
#     # converting it by multiplying with eart weight and mars gravity
#     mars_weight = earth_weight * MARS_GRAVITY
    
#     # displaying the calculated weight
#     print(f"Your weight on Mars would be {mars_weight:.2f} kg.")
    


# if __name__ == '__main__':
#     main()

# Milestone #2: Adding in All Planets

# Defining a constant dictionary


# - Mercury: 37.6%

# - Venus: 88.9%

# - Mars: 37.8%

# - Jupiter: 236.0%

# - Saturn: 108.1%

# - Uranus: 81.5%

# - Neptune: 114.0%


PLANETS_GRAVITY ={
    "mercury":37.6/100,
    "venus": 88.9/100,
    "mars": 37.8/100,
    "jupiter": 236/100,
    "saturn": 108.1/100,
    "uranus": 81.5/100,
    "neptune": 114/100
}

def main():
    # displaying welcome message
    print("Welcome to Planetary Weight Calculator")
    
    # taking input FROM USER
    try:
            earth_weight = float(input("Enter your weight on Earth (in kg) --> "))
            if earth_weight <= 0:
                print("Weight must be a positive number.")
                return
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        return
    planet = input("Enter the planet in which you want to see the weight --> ").lower().strip()
    
# Converting weight to earth
    try:
      planet_weight =  PLANETS_GRAVITY[planet] * earth_weight
      print(f"Your weight on {planet} would be {round(planet_weight,2)} kg.")
    except KeyError:
        print(f"Sorry, we don't have the gravity data for '{planet}'.")
        return  
 
if __name__ == '__main__':
    main()