import random

def roll_dice():
    # Generate a random number between 1 and 6
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print("You rolled:", result)
        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
