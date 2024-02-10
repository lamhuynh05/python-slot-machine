#slot machine where users deposit money -> allow them to bet on
# number of slot lines -> determine if they won and how much?

#steps:
# 1. deposit money -> add to balance
# 2. number of lines they want to bet on
# 3. generate slot lines & reels -> prize
# 4. add the prize back to the balance

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

deposit() #call function