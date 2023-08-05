import random

# Where the magic happens. We're going to create a function that rolls dice via random number generation.
def roll_dice(num_dice, num_sides):
    return [random.randint(1, num_sides) for _ in range(num_dice)]

# The script to handle user input. Running in a while loop to check if the user is providing valid input.
def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input! Please enter a positive integer.")
    

#the main function where everything runs.
def main():
    num_dice = get_input("Enter the number of dice to roll: ")
    num_sides = get_input("Enter the number of sides on each die: ")
    result = roll_dice(num_dice, num_sides)
    print(f"You rolled: {result}")
    print(f"Total: {sum(result)}")


if __name__ == "__main__":
    main()
