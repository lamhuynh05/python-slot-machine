#slot machine where users deposit money -> allow them to bet on
# number of slot lines -> determine if they won and how much?

#steps:
# 1. deposit money -> add to balance
# 2. number of lines they want to bet on
# 3. generate slot lines & reels -> prize
# 4. add the prize back to the balance

MAX_LINES = 3 # constant
MAX_BET = 100
MIN_BET = 1
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

def main(): 
    balance = deposit() #call function
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    

main() 