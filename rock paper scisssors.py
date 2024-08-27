import random
while True:


    choices=["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None
    while player not in choices:


        player = input("rock , paper, or scissors : ").lower()
        if player == computer:

            print("computer picked", computer)
            print("player picked",  player)
            print("tie")

        elif player == "rock":

            if computer == "paper":

             print("computer picked", computer)
             print("player picked",  player)
             print("you lose")

            if computer == "scissors":
               print("computer picked", computer)
               print("player picked",  player)
               print("you win")


        elif player == "scissors":
            if computer == "paper":

               print("computer picked", computer)
               print("player picked",  player)
               print("you win")

            if computer == "rock":
                print("computer picked", computer)
                print("player picked",  player)
                print("you lose ")


        elif player == "paper":
            if computer == "scissors":

                print("computer picked", computer)
                print("player picked",  player)
                print("you lose")

            if computer == "rock":
                print("computer picked", computer)
                print("player picked",  player)
                print("you win ")

    play_again = input("do you want to play again (yes/no) : ")  
    if play_again != "yes":
        break
print("bye")

        
    
