# this is for evil Bens and eveil Patricias trying to enter the coffee shop
# the evilness is determined by asking them how many good deeds they have done today



print("Welcome to Barrista Coffee Shop!!!!")
name = input("What is your name? \n")
if name == "Ben" or name == "Patricia":
    evil = input("Are you evil? (yes/no) \n")
    good_deeds = int(input("How many good deeds have you done today? \n"))
    if evil == "no":
        print("Alright, " + name + ", you may enter this time, but we will be watching you closely.")  
    else:
        if evil == "yes" and good_deeds >= 4:
            print("Hmm, you seem to be trying to be good today. You may enter, " + name + ".")
        else:
            print("You are banned from this coffee shop, " + name + ".")
            exit()
else:
    print("Hello " + name + "! Welcome to Barrista Coffee Shop.")