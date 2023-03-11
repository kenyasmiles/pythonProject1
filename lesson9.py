#application of functions
#USSD Mpesa application
#Withdraw Money
#check balance
#buy airtime
#send money
#create a dictionary to hold the details of the user
user={
    "name":"Maxwell",
    "pin":1234,
    "balance":2000
}

#create a function from the menu
#parameters and arguments
#parameters allow the user to input values when calling the functions
#the parameter is defined inside the parenthesis when creating functions
#arguments are values given when caling a function
#arguments are values  of parameters
#all the parameters defined must be given their value when calling the function


def withdraw(amount,agent,pin): #parameters
#    check if the pin is correct
    if pin == user["pin"]:
        print(f"Hello {user['name']} WELCOME TO YOUR ACCOUNT")
        if amount<= user["balance"]:
            print("====APPROVED===")
            account_balance=user["balance"]-amount
            print(f".....CONFIRMED... KES {amount} Withdrawn from agent no. {agent}.",
                  f"New Mpesa balance id KES {account_balance}")
        else:
            print("Insufficient funds.You dont have enough money to make this transaction /in "
                  "try again with different amount")


    else:
        print("Incorrect pin,Try again")

def menu():
    #print("===WELCOME===== /n Please select an option to proceed")
    print("1.Withdraw Money")
    print("2.Check balance")
    print("3.Buy Airtime")
    print("4.Mpesa statement")
    print("5.Send Money")
    answer=int(input("Select a menu:"))
    if answer == 1:
        withdraw(int(input("Enter amount to Withdraw")),
                 int(input("Enter Agent No")),
                 int(input("Enter your pin")))  #arguments
    else:
        print("Select another option")
menu()
