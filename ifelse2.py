#here we do nested if-else statements to ban both "Alice" and "alice" from the coffee shop
#but ask them as well if they are evil or not. if they say yes, we ban them permanently.
#if they say no, we let them in after a warning.


print("Welcome to Barrista Coffee Shop!!!!")
name = input("What is your name? \n")
if name == "Alice" or name == "alice":
    evil = input("Are you evil? (yes/no) \n")
    if evil.lower() == "no":
        print("Alright, " + name + ", you may enter this time, but we will be watching you closely.")  
    else:
        print("You are banned from this coffee shop, " + name + ".")
        exit()
else:
    print("Hello " + name + "! Welcome to Barrista Coffee Shop.")