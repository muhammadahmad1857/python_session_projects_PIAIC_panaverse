from typing import List, Union

# Problem 1
# def main() -> None:
#     # Creating a list named fruit_list
#     fruit_list: list[str] = ["apple", "banana", "orange", "grape", "pineapple"]
    
#     # Printing the length of the list
#     print("Length of the list:", len(fruit_list))
    
#     # Add 'mango' at the end of the list
#     fruit_list.append("mango")
    
#     # Printing the updated list
#     print("Updated list:", fruit_list)
    
# if __name__ == "__main__":
#     main()

def access_elements(list_name: List[str], index: int) -> Union[str, None]:
    """Access elements in the list based on index."""
    if 0 <= index < len(list_name):
        return list_name[index]
    return "Invalid index"

def update_elements(list_name: List[str], index: int, new_value: str) -> Union[str, None]:
    """Update an element in the list at the specified index."""
    if 0 <= index < len(list_name):
        list_name[index] = new_value
        return None
    return "Invalid index"

def slice_list(list_name: List[str], start_index: int, end_index: int) -> Union[List[str], str]:
    """Slice the list from start_index to end_index."""
    if 0 <= start_index <= end_index <= len(list_name):
        return list_name[start_index:end_index]
    return "Invalid indices"

def main() -> None:
    """Main function to execute the fruit list operations."""
    # Initializing a list named fruit_list
    fruit_list: List[str] = ["apple", "banana", "orange", "grape", "pineapple", "mango"]
    
    print("Welcome to the Fruit List Game!")
    print("Your initial fruit list is:", fruit_list)
    
    while True:
        print("\nSelect an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter the number of your choice (1-4): ")

        match(choice):
            case "1": # accssing an element
                index = int(input(f"Enter the index of the element you want to access (0 to {len(fruit_list) - 1}): "))
                result = access_elements(fruit_list, index)
                print("Result:", result)

            case "2":  # Modify an element
                index = int(input(f"Enter the index of the element you want to modify (0 to {len(fruit_list) - 1}): "))
                new_value = input("Enter the new value: ")
                update_result = update_elements(fruit_list, index, new_value)
                if update_result is None:
                    print("Element updated successfully!")
                    print("Updated fruit list:", fruit_list)

                else:
                    print("Result:", update_result)

            case "3":  # Slice the list
                start_index = int(input(f"Enter the starting index for slicing (0 to {len(fruit_list) - 1}): "))
                end_index = int(input(f"Enter the ending index for slicing ({start_index} to {len(fruit_list)}): "))  # Adjusted for better user experience
                sliced_result = slice_list(fruit_list, start_index, end_index)
                print("Sliced list:", sliced_result)

            case "4":  # Exit the game
                print("Thank you for playing! Goodbye!")
                break

            case _:
                print("Invalid choice! Please select a valid operation.")


if __name__ == '__main__':
    main()
