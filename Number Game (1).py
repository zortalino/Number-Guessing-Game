#Lam Manning 11-3-23
#initialize
import random
#Function
def guessing_game(): #Plays a guessing game where the user inputs a number and the computer tells them if it is correct
    secret =  random.randint(1, 10)
    user = input("Can you guess the number I'm thinking of? Guess a number between 1-10: ")
    if(secret==user):
        print( "You're a Psyhcic! The number was: "+ str(secret)+ ". Congrats on winning")
    elif(secret>int(user)):
        print("Your number was too LOW! Try Again!")
        new = input("What's your new guess? ")
        if(secret==int(new)):
            print( "You're a Psyhcic! The number was: "+ str(secret)+ ". Congrats on winning")
        else:
            print("Sorry! The number was: "+ str(secret)+ ". Better Luck Next Time")
    elif(secret<int(user)):
        print("Your number was too HIGH! Try Again!") 
        new = input("What's your new guess? ")
        if(secret==int(new)):
            print("You're a Psyhcic! The number was: "+ str(secret)+ ". Congrats on winning")
        else:
            print("Sorry! The number was: "+ str(secret)+ ". Better Luck Next Time")
    else:
        print("Invalid Input! Insert an actual number!")
#Main
guessing_game()