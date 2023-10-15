import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


def deposit():
    while True:
        amount = input("What much do you want to deposit = $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"You deposited ${amount}")
                break
            else:
                print("The amount must be greater than 0")
        else:
            print("Please enter a valid input.")
    return amount


def get_no_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1 - " + str(MAX_LINES) + ") ? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                print(f"You bet on {lines} lines")
                break
            else:
                print("Please bet b/w (1 - " + str(MAX_LINES) + ") ? ")
        else:
            print("Please enter a valid input.")
    return lines


def get_bet(bal,line):
    while True:
        bet = input("Place your bet ($" + str(MIN_BET) + " - $" + str(MAX_BET) + ") ? ")
        if bet.isdigit():
            bet = int(bet)
            if bal > bet*line:
                if MIN_BET <= bet <= MAX_BET:
                    print(f"You bet ${bet} ")
                    break
                else:
                    print("Please bet b/w (" + str(MIN_BET) + " - " + str(MAX_BET) + ") ? ")
            else:
                print(f"Please place your bet under or equal to your balance ${bal}")
        else:
            print("Please enter a valid input.")
    return bet


def main():
    balance = deposit()
    lines = get_no_of_lines()
    bet = get_bet(balance, lines)
    total_bet = bet*lines
    print(f"You bet {bet} on {lines} \nTotal bet = {total_bet}")



main()
