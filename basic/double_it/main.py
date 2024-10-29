def main():
    # showing a welcome message
    print("Welcome to the 'Double the Number' game!")
    
    # Taking the number input
    curr = int(input("Enter a number to start the game: "))
    
    # double the number if it's 100 or less
    if curr <= 100:
        while curr <= 100:
            curr *= 2
            print(curr , end=" ")    
    else:
        print("Sorry, we can only double numbers up to 100. Your number is already greater than 100.")

if __name__ == "__main__":
    main()
