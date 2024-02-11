#slot machine where users deposit money -> allow them to bet on
# number of slot lines -> determine if they won and how much?

#steps:
# 1. deposit money -> add to balance
# 2. number of lines they want to bet on
# 3. generate slot lines & reels -> prize
# 4. add the prize back to the balance

import random 

MAX_LINES = 3 # constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #for each line out of 3
        symbol = columns[0][line] #symbol that we check is the 1st of col of the row
        for column in columns: # go thru each column
            symbol_to_check = column[line] #check other symbols in line
            if symbol != symbol_to_check: #if the symbol dont match other
                break
            else:
                winnings += values[symbol] * bet # if match -> add to winnings
                winning_lines.append(line + 1) #what line they won
    return winnings, winning_lines


# random selection
# create a list of all values we could select from -> random choose 3 values
# remove from a list -> do again
def get_slot_machine_spin(rows, cols, symbols): #3 parameters that we pass in the function
    all_symbols = [] #list
    for symbol, symbol_count in symbols.items(): #iterate through dict 
        # give u keys & values assoc w/ dict
        # symbol = key, symbol_count = value
        for _ in range(symbol_count): #Use _ :control the loop iterations and its specific value doesn't matter.
            all_symbols.append(symbol)
        #example: loop through key A with val 2 in the dict 
            # 2nd for loop through key 2 times (symbol_count) and add another
            # A into all_symbols list
    
    # select values that go in each col:
    columns = [] #define columns list
    for _ in range(cols): #generate column for every columns we have
        column = [] # 1 column
        current_symbols = all_symbols[:] # current symbols = copy of all symbols list
        for _ in range(rows): #loop through num values = num of rows
            value = random.choice(current_symbols) # 1st value = rand choice
            current_symbols.remove(value) # remove values so we dont pick again
            column.append(value) # add value to our column
        
        columns.append(column) # add new column to columns

    return columns

def print_slot_machine(columns):
    # transposing: at this stage columns look like rows
    # we need to make columns into to columns
    for row in range(len(columns[0])): #for each row in range of at least 1 column
        for i, column in enumerate(columns): #give u index & item as u loop
            if i != len(columns) - 1: # if its not last col -> print pipe
                print(column[row], end=" | ")
            else:
                print(column[row], end="") # if its last -> no print
                # columns numbers -> rows -> to look like columns
        print() # empty print -> bring down to next line

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Please enter amount greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True: 
        lines = input("Please enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Please enter valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"Your bet must be between ${MIN_BET} - ${MAX_BET}.") #embed values in string
        else:
            print("Please enter your bet.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) # * will pass every winning line to print
    return winnings - total_bet


def main(): 
    balance = deposit() #call function
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

main() 