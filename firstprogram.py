import random
#My First Prograaaaam = ROCK PAPER SCISSORS
scissors = "Scissors"
rock = "Rock"
paper = "Paper"

pc_score = 0
players_score = 0

print("For Help code 'help' ")
print("For Credits code 'Credits' ")

while(pc_score < 3 and players_score < 3):

    pc_choice = random.choice([scissors, rock, paper])

    players_choice = str(input("What will you choose: Rock, Paper or Scissors? "))

    if(pc_choice == rock and (players_choice == "Rock" or players_choice == "rock")):
        print("It's a draw")
    elif(pc_choice == rock and (players_choice == "Scissors" or players_choice == "scissors")):
        print("You lose")
        print("The opponent choose " + pc_choice)
        pc_score += 1
    elif(pc_choice == rock and (players_choice == "Paper" or players_choice == "paper")):
        print("You WIN")
        print("The opponent choose " + pc_choice)
        players_score += 1
    elif(pc_choice == paper and (players_choice == "Paper" or players_choice == "paper")):
        print("It's a draw")
    elif(pc_choice == paper and (players_choice == "Rock" or players_choice == "rock")):
        print("You lose")
        print("The opponent choose " + pc_choice)
        pc_score += 1
    elif(pc_choice == paper and (players_choice == "Scissors" or players_choice == "scissors")):
        print("You WIN")
        print("The opponent choose " + pc_choice)
        players_score += 1
    elif(pc_choice == scissors and (players_choice == "Scissors" or players_choice == "scissors")):
        print("It's a draw")
    elif(pc_choice == scissors and (players_choice == "Paper" or players_choice == "paper")):
        print("You lose")
        print("The opponent choose " + pc_choice)
        pc_score += 1
    elif (pc_choice== scissors and (players_choice == "Rock" or players_choice == "rock")):
        print("You WIN")
        print("The opponent choose " + pc_choice)
        players_score += 1
    elif(players_choice == "help" or players_choice == "Help"):
        print("This is a Rock-Paper-Scissors game. To procceed, please choose one of the three options!!")
    
    elif(players_choice == "Credits" or "credits"):
        print("This is a game made by Angelos Karasavvidis #2020")
    else:
        print("Sorry, I don't understand! Can you repeat the answer? ")