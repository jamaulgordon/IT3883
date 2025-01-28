# Program Name: Assignment1.py
# Course: IT3883/W02
# Student Name: Jamaul Gordon
# Assignment Number: Lab1
# Due Date: 1/27/24
# Purpose: This program implements a text-based menu allowing users to append data to an input buffer, clear the buffer, display its contents, or exit the program.
# List Specific resources used to complete the assignment: w3schools


input_buffer = ""  # Starts with an empty string to hold user input

def menu():
    # Print out the menu options
    print("\n1. Add to the buffer")
    print("2. Clear the buffer")
    print("3. Show the buffer")
    print("4. Quit")

def main():
    global input_buffer  # Use the global input_buffer variable

    while True:
        menu()  # Show the menu
        choice = input("Pick an option (1-4): ")  # Ask the user to pick an option

        if choice == "1":
            # Add data to the buffer
            data = input("What do you want to add? ")  # Get user input to add
            input_buffer += data  # Add the input to the buffer
            print("Added!")
        elif choice == "2":
            # Clear the buffer
            input_buffer = ""  # Reset the buffer to an empty string
            print("Buffer cleared!")
        elif choice == "3":
            # Show the buffer's content
            if input_buffer:  # If the buffer has content
                print("Buffer: " + input_buffer)
            else:  # If the buffer is empty
                print("The buffer is empty.")
        elif choice == "4":
            # Quit the program
            print("Bye!")
            break  # Exit the loop
        else:
            # Handle invalid input
            print("That’s not a valid option. Try again!")

if __name__ == "__main__":
    main()  # Start the program
