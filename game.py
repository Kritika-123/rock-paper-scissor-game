import random
options=["Rock","Paper","Scissor"]
Computerscore=0
Playerscore=0
NumberofRounds=0
gameOn=True
print("Welcome Player")
while NumberofRounds<3:
    ComputerOption=random.choice(options)
    PlayerOption=input("Enter Rock/Paper/Scissor:").title()
    print(f"Computer option:{ComputerOption}")
    print(f"Player option:{PlayerOption}")
    NumberofRounds+=1
    if ComputerOption==PlayerOption:
        print("Tie")
    elif (ComputerOption=="Rock" and PlayerOption== "Scissor") or (ComputerOption=="Scissor" and PlayerOption=="Paper") or (ComputerOption=="Paper" and PlayerOption=="Rock"):
        print("Computer Wins")
        Computerscore +=1
    elif (PlayerOption== "Scissor" and ComputerOption=="Paper") or (PlayerOption== "Rock" and ComputerOption=="Scissor") or (PlayerOption== "Paper" and ComputerOption=="Rock"):
        print("Player Wins")
        Computerscore+=1
    else:
        print("Choose a valid option to play this game")
    print("-------------------")
    print("")
    print(f"Round No:{NumberofRounds}")
    print("-----------Score Board----------")
    print(f"Player:(Playerscore) | Computer:(computerscore)")
    print("===========================")
    print("")
    if NumberofRounds==3:
        gameOn="False"
        break
if Playerscore==Computerscore:
    print("Draw!!")
elif Playerscore > Computerscore:
    print(f"Congrats Player, you won the game!!")
else:
    print(f"Oops  Computer won this time!! Better luck next time!!")
