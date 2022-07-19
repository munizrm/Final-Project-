DATA = {                  #This is where the coffee machine stores information, such as the type of drink and what we need to make it.
    "espresso": {
        "ingredients": {
            "water": 50,  #We list how much of each ingredient we need for each drink next to each ingredient.
            "coffee": 18,
        },
        "cost": 2.0,      #This is the set value for the cost of the drink
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0                #This is where we set up the profit for the coffee machine by adding up the "cost" from the drinks

resources = {             #Since this is a coffee machine, there are only so many resources, so this is where we can set how much the machine starts with.
    "water": 1000,
    "milk": 700,
    "coffee": 800,
}

def is_resource_sufficient(inputs):                      #In this function we take the input parameter and check to see if we have enough of our resources to make said drink
    for item in inputs:
        if inputs[item] >= resources[item]:              #In this loop it will check the input and then the resources
            print(f'Sorry there is not enough {item}')
        return True

def process_coin():                                      #This function is where we can input how much money we want to give the machine
    total = int(input('How many quarters?')) * 0.25      #Whatever number is input will be converted to an interger and then multipled by the value based on the coin
    total += int(input('How many dimes?')) * 0.1
    total += int(input('How many nickles?')) * 0.05
    total += int(input('How many pennies?')) * 0.01
    return total


def is_transaction_ok(money_recieved, drink_cost):       #We take two arguements "money_recieved" and "drink_cost" and check to see if the transaction is true.
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)   #Once conditions are true then we can generate how much change the customer recieves from the machine rounded up.
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost                             #Here is where we can take the value from the drink_cost to add to our profit value.
        return True

    else:                                                #If the user doesn't input enough money, then this is the error message that will be displayed.
        print("Sorry that's not enough money, Money refunded!")

def get_coffee(name, ingredients):                       #This function is how we actually change the resources so we take the name and ingredient arguements to modify it.
    for item in ingredients:                             #Here is where we can get all the items from the ingredients.
        resources[item] -= ingredients[item]             #This how we can pull what resources we need for said item and subtract them.
    print(f"Here is your {name}☕")                       #Here will print out the drink

print("Welcome to Daydream Coffee Shop!")          #Just the welcome message along with a little ASCII coffee cup.
print("""
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
""")

on = True                                           #Here we check to see if the machine is turned on.
while on:                                           #When the machine is turned on, we need to ask the user what they would like to order.
    choice = input("""
What would you like to order?
    
espresso - $2
latte - $2.50
cappuccino - $3
>""")
    if choice == 'off':                             #By typing off this is how the user can turn off the machine aka end the program.
        on = False
    elif choice == 'report':                        #By typing report we can print to see how many resources are left in our machine.
        print(f'Water: {resources["water"]}oz')     #In each statement we use the curly braces to call back to our resources bank.
        print(f'Milk: {resources["milk"]}oz')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Profit: ${profit}')                 #Here will show how much money the machine has made so far.
    else:
        drink = DATA[choice]
        if is_resource_sufficient(drink['ingredients']):  #Here will check to see if we have enough resources for our drink.
            pay = process_coin()                          #Once this is true then we need to take the variable.
            if is_transaction_ok(pay, drink['cost']):     #We compare how much is paid to the drink cost.
                get_coffee(choice, drink['ingredients'])  #This is where we can access the values in our data and use them.