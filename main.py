import random

user_guess = 0
computer_guess = 0
option = ["rock", "paper", "scissors"]


def dis():
    print("---------------------------------------------------------------------------")
    print("                Welcome to rock and paper and scissors           ")
    print("          choice q to quit or choice rock or paper or scissors              ")
    print("----------------------------------------------------------------------------")


print(dis())
while True:
    user_input = input("enter a rock or paper or scissors or leave by pressing q  => ").lower()
    if user_input == "q":
        print("                              goodbye !")
        break
    elif user_input not in option:
        continue
    random_pickes = random.randint(0, 2)
    computer_pickes = option[random_pickes]
    print("             computer pick " + computer_pickes)
    if user_input == "rock" and computer_pickes == "rock":
        print("                no win here          ")
    elif user_input == "scissors" and computer_pickes == "scissors":
        print("                no win here                            ")
    elif user_input == "paper" and computer_pickes == "paper":
        print("                 no win here ")

    elif user_input == "rock" and computer_pickes == "scissors":
        print("                you win ")
        user_guess += 1
    elif user_input == "scissors" and computer_pickes == "paper":
        print("                you win ")
        user_guess += 1
    elif user_input == "paper" and computer_pickes == "rock":
        print("                you win ")
        user_guess += 1
    else:
        print("               computer win ")
        computer_guess += 1
print("------------------------------------------------------------------------------")
print("                      you win  " + str(user_guess) + " times                ")
print("------------------------------------------------------------------------------")
print("                      computer win " + str(computer_guess) + " times ")
print("------------------------------------------------------------------------------")
print("                      SEE YOU NEXT TIME  :) ")
print("------------------------------------------------------------------------------")
