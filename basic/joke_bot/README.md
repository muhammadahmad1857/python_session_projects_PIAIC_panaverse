# Joke Teller ChatBot

This Python script is a simple joke-telling chatbot that interacts with the user. The chatbot checks if the user wants to hear a joke and responds accordingly. Below, you'll find an explanation of each part of the code, including its constants and main function.

## Table of Contents
- [Constants](#constants)
- [Main Function](#main-function)
- [Execution](#execution)

### Constants

The code defines a few constants used throughout the program:
- **PROMPT**: This constant stores the question asked to the user to prompt them for input. It is phrased in a way that encourages the user to type a response.
- **JOKE**: This constant holds the joke that will be displayed if the user requests it.
- **SORRY_MESSAGE**: This constant defines the response that the bot will provide if the user’s input is anything other than "joke".

```python
PROMPT: str = "What would you like to hear? "
JOKE: str = ("Panaversity GPT - Sophia is heading out to the grocery store. "
             "A programmer tells her: get a liter of milk, and if they have eggs, get 12. "
             "Sophia returns with 13 liters of milk. The programmer asks why, and Sophia replies: "
             "'Because they had eggs.'")
SORRY_MESSAGE: str = "Sorry, I can only tell jokes."
```

### Main Function

The main function contains the core logic of the chatbot, which includes the following steps:

1. **Welcome Message**: This initial message provides a greeting to introduce the chatbot’s purpose.
   ```python
   print("Welcome to the Joke Teller ChatBot!")
   ```

2. **User Prompt**: The chatbot prompts the user for input using the `PROMPT` constant, which asks what they would like to hear. This prompt gives the user an opportunity to type their response.
   ```python
   user_input = input(PROMPT)
   ```

3. **Input Check**: The program checks if the user input is exactly "joke" (case-insensitive and trimmed). If it is, the program displays the joke; otherwise, it shows the sorry message.
   - The `user_input.lower().strip()` line ensures that the input is not case-sensitive and removes any surrounding whitespace.
   ```python
   if "joke" == user_input.lower().strip():
       print("Here's a joke for you:", JOKE)
   else:
       print(SORRY_MESSAGE)
   ```

### Execution

The program is executed by calling the `main()` function when the script is run directly. This is indicated by the following code:
```python
if __name__ == "__main__":
    main()
```
This block ensures that the code inside `main()` is executed only when the script is run as a standalone program, not when it is imported as a module.

## How to Use

1. Run the script.
2. When prompted, type "joke" to hear a joke, or type anything else to receive a polite response.

## Example Output

1. **User types "joke"**:
   ```
   Welcome to the Joke Teller ChatBot!
   What would you like to hear? joke
   Here's a joke for you: Panaversity GPT - Sophia is heading out to the grocery store...
   ```

2. **User types something else**:
   ```
   Welcome to the Joke Teller ChatBot!
   What would you like to hear? hello
   Sorry, I can only tell jokes.
   ```

This chatbot example demonstrates basic user interaction, condition checking, and message formatting in Python. Enjoy coding!
