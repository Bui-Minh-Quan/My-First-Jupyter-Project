import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

ROWS = 3
COLS = 3
symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 8,
    'D' : 16
}

symbol_value = {
    'A' : 10,
    'B' : 5,
    'C' : 3,
    'D' : 2
}

table = []

def get_slot_machine_spin(number_of_rows, number_of_columns):
    table_of_symbols = []
    list_of_symbols = []
    # append all the character into a list
    for key in symbol_count:
        for i in range(symbol_count[key]):
            list_of_symbols.append(key)
    # append character from the previous list into a table. Characters are chose randomly

    for i in range(number_of_rows):
        temp_list = []
        for j in range(number_of_columns):
            temp_list.append(random.choice(list_of_symbols))
        table_of_symbols.append(temp_list)

    return table_of_symbols

    
def print_table(table):
    list = table
    for row in list:
        for i, symbol in enumerate(row):
            if i == len(row) - 1:
                print(symbol)
            else:
                print(symbol + " | ", end = "")

def check_winning(bet_money, number_of_lines, table):
    winning = 0
    winning_lines = []
    for i in range(number_of_lines):
        symbol_to_check = table[i][0] # compare the first to symbol in a row with others
        for symbol in table[i]:
            if symbol != symbol_to_check:
                break
        else:
            winning += symbol_value[symbol_to_check] * bet_money
            winning_lines.append(i + 1)
    

    return winning_lines, winning




def deposit():
    while True:
        amount = input("What would you like to deposit? $")

        if amount.isdigit() == True:
            amount = int(amount)
            if amount <= 0:
                print("The amount of money must greater than 0")
            else:
                break
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1 - " 
                      + str(MAX_LINES) + ")? ")

        if lines.isdigit() == True:
            lines = int(lines)
            if lines < 1:
                print("The number of lines must be greater or equal to 1")
            elif lines > MAX_LINES:
                print("The number of lines must be smaller than or equal to"
                      , MAX_LINES)
            else:
                break
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True:
        amount = input("How much do you want to bet? $")

        if amount.isdigit() == True:
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount of money must be between ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Please enter a number")

    return amount


def spin(balance):
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough money to bet that amount. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on  {lines} lines. The total bet is ${total_bet}.")
    table = get_slot_machine_spin(ROWS, COLS)
    print_table(table)
    winning_lines, winning_money = check_winning(bet, lines, table)
    if (winning_money > 0):
        print(winning_lines)
    print("Winning money:", winning_money)

    return winning_money - lines * bet
    



def main():
    balance = deposit()
    while True:
        print(f"Current balance: {balance}")
        mode = input("Press enter to play(q to quit): ").lower()
        if mode == "q":
            break
        else:
            balance += spin(balance)

    print(f"You left the game with {balance}")

main()
