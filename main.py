import random

def spin_slot_machine():
    return [random.choice(['Cherry', 'Bar', 'Seven']) for _ in range(3)]

def calculate_payout(symbols):
    switcher = {
        ('Cherry', 'Cherry', 'Cherry'): 50,
        ('Bar', 'Bar', 'Bar'): 100,
        ('Seven', 'Seven', 'Seven'): 200,
        # Add more cases as needed
    }
    return switcher.get(tuple(symbols), 0)

def play_slot_game():
    print("Welcome to the Python Slot Machine!")

    while True:
        input("Press Enter to spin the slot machine...")
        symbols = spin_slot_machine()
        print(f"Result: {symbols}")

        payout = calculate_payout(symbols)
        if payout > 0:
            print(f"Congratulations! You won {payout} coins.")
        else:
            print("Sorry, no win this time.")
# loop again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    play_slot_game()
