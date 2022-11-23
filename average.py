#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Nov 2022
# This program finds average of numbers


def main():
    # This function finds average of numbers
    try:
        number_to_add = int(input("How many numbers you want to add to find average: "))
        running_total = 0
        for loop_counter in range(0, number_to_add):
            number = float(input("Enter number: "))
            running_total = running_total + number
        result = running_total / number_to_add
        print("\nThe average of these numbers is {}.".format(result))
    except ValueError:
        print("\nThis input is invalid, please, insert a number.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
