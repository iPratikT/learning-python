# this code is copied from barrista tutorial and an if statement is added. condition is to see if the customer 
#name is "Alice". if it is, they are banned from the coffee shop
#anyone else is welcomed as usual.


print("Welcome to Barrista Coffee Shop!!!!")

option1 = "Espresso"
option2 = "Cappuccino"
option3 = "Latte"
option4 = "Mocha"
name = input("What is your name? \n")
if name == "Alice" or name == "alice":
    print("Sorry, Alice, you are banned from this coffee shop.")
else:
    print("Hello " + name + "! Welcome to Barrista Coffee Shop." + "\nWe have the following options for you today:")
    print("1. " + option1 + "\n2. " + option2 + "\n3. " + option3 + "\n4. " + option4)
    choice = input("Please enter the number of your choice: ")

    price = 8.50
    quantity = input("and how many of these would you like? \n")

    total = price * int(quantity)

    print("Great choice, " + name + "! You have selected " + eval("option" + choice) +  " and your total amounts to " + str(total) + ". Your " + str(quantity) + " " + eval("option" + choice) + "s will be ready shortly.")