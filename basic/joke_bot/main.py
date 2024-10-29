# Defining Constants
PROMPT: str = "What would you like to hear? "
JOKE: str =" Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY_MESSAGE: str = "Sorry, I can only tell jokes."

# Defining the main function
def main():
    # Welcome message
    print("Welcome to the Joke Teller ChatBot!")
    
    # Prompting the user for input and checking if they request a joke
    user_input = input(PROMPT)
    if "joke" == user_input.lower().strip():
        print("Here's a joke for you:", JOKE)  # Printing the joke if the input is "joke"
    else:
        print(SORRY_MESSAGE)  # Printing sorry message if input isn't "joke"


if __name__ == "__main__":
    main()
