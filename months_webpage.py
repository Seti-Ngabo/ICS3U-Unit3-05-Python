#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program tells you the month of the year
#   with user input


def main():
    # this function checks if the user put in the right number of the month

    # input
    user_input = int(input("Enter a number (from 1 to 12): "))
    print("")

    # process and output
    if user_input == 1:
        print("The month is January.")
    elif user_input == 2:
        print("The month is February")
    elif user_input == 3:
        print("The month is March.")
    elif user_input == 4:
        print("The month is April.")
    elif user_input == 5:
        print("The month is May.")
    elif user_input == 6:
        print("The month is June.")
    elif user_input == 7:
        print("The month is July.")
    elif user_input == 8:
        print("The month is August.")
    elif user_input == 9:
        print("The month is September.")
    elif user_input == 10:
        print("The month is October.")
    elif user_input == 11:
        print("The month is November.")
    elif user_input == 12:
        print("The month is December.")
    else:
        print("This number is not a month.")

    print("\nDone.")


if __name__ == "__main__":
    main()
