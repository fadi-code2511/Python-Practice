# Requirements:
# Start with a balance (e.g. $1000 stored in a variable).
# Show a menu in a loop:
# Welcome to the ATM
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit


# Based on user input:
# 1. Show the current balance.
# 2. Ask how much to deposit, and add it to the balance.
# 3. Ask how much to withdraw:

# If enough balance → subtract and show new balance.
# Else → show an error message.

# 4. Exit the loop and end the program.

# Validate input where needed (e.g., no negative deposits or withdrawals).






balance=1000
while True:
    print( "\nWelcome to the ATM  \n1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit") # show the menu
    option=int(input("Enter the number of the option: "))

    if option==1:
        print("your current balance is: ",balance,)   #printing the balance
    elif option==2:
        DepositAmount=int(input("Enter the amount you want to deposit? ")) 
        balance=balance+DepositAmount #adding the amount to the balance
        
    elif option==3:
        WithDrawAmount=int(input("Enter the amount you want to withdraw? "))
        balance=balance-WithDrawAmount # deducting the amount from the balance

    elif option==4:
        break
    else:
        print("you entered a wrong number\n")


