import art
import os
clear = lambda: os.system('cls')

#from replit import clear
#HINT: You can call clear() to clear the output in the console.
bids = []
print(art.logo)


def Getting_bids():
    Name = input("What is your name?")
    Bid = input("What is your bid?")
    Person = {}
    Person["Name"] = Name
    Person["Bid"] = Bid
    bids.append(Person)   

def getting_higher_bid():
    higher = 0
    for element in bids:
        if int(element["Bid"]) > int(higher):
            higher = element["Bid"]
            winner = {}
            winner["Name"] = element["Name"]
            winner["Bid"] = element["Bid"]
    print(f"The winner is: {winner}")

End_of_game = False

while(End_of_game == False):
    Getting_bids()
    answer = int(input("Is there other user? (1 = Yes | 2 = No): "))
    if answer == 2:
        End_of_game = True
        clear()
        getting_higher_bid()





    
