# Author 2025 Mikhail Ibrahim
# Date: Apr 14, 2025
# Description: A crash-proof Python program that calculates the factorial
# of a whole number using a do..while style loop and handles all invalid input.

print("Welcome! This program calculates the factorial of a whole number you enter.")

while True:
    user_input = input("Enter a non-negative whole number: ")

    try:
        number = int(user_input)

        if number < 0:
            print("Error: Please enter a non-negative number.")
            continue  # Prompt again

        # Valid input - proceed to factorial calculation
        factorial = 1
        counter = 1

        while True:
            factorial *= counter
            counter += 1

            if counter > number:
                break  # Simulates do..while loop ending condition

        print(f"The factorial of {number} is {factorial}.")
        break  # Exit main loop after successful computation

    except ValueError:
        print("Error: Please enter digits only (no letters, symbols, or decimals).")
