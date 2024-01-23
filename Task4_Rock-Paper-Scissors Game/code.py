# Rock-Paper-Scissors Game

'''

Rock-Paper-Scissors Game

User Input         : Prompt the user to choose rock, paper, or scissors.

Computer Selection : Generate a random choice (rock, paper, or scissors) for
the computer.

Game Logic         : Determine the winner based on the user's choice and the
computer's choice.
s
paper beats rock.
Rock beats scissors, 
scissors beat paper, 

Display Result     : Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.

Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds.

Play Again        : Ask the user if they want to play another round.

User Interface    : Design a user-friendly interface with clear instructions and
feedback.

'''
import secrets


# prompt the user to enter an choice 
def chooseOption():
    print("1. rock")
    print("2. paper")
    print("3. scissors")
    userChoice = input("Enter Your Number of Choice: ")
    print("====================================")
    if   userChoice == '1':
            print("User Choice     : ",'rock')
    elif userChoice == '2':
            print("User Choice     : ",'paper')
    elif userChoice == '3':
            print("User Choice     : ",'scissors')
    else:
          print("==============")
          print("Invalide input")
          print("==============")
          return "Invalide input"
    return userChoice



# decide the winner      1. rock 2. paper  3. scissors
def decideWinner(userChoice,computerChoice):
    if ((userChoice == "1" and computerChoice == "rock") or
        (userChoice == "2" and computerChoice == "paper") or
        (userChoice == "3" and computerChoice == "scissors")):
          return "It is a Tie"
    elif((userChoice == '1' and  computerChoice == 'scissors') or 
         (userChoice == '2' and  computerChoice == 'rock') or 
         (userChoice == '3' and  computerChoice == 'paper')):
          return "User is the winner"
    else:
          return "Computer is the winner"



# definition of the main function
def main():
  
    # defining two variables to keep track the winning score of the user and computer 
    userScore     = 0
    computerScore = 0
    scoreTracking = {"User":userScore,"Computer":computerScore}
    
    # run the program till the user wants to quit
    while True:
        userChoice = chooseOption()
        # check if the user entered a valid input or not #
        if(userChoice == 'Invalide input'):
            # do nothing #
             pass
        else:
            # Generate the choice of the computer randomly
            computerChoice = secrets.choice(["rock", "paper", "scissors"])
            print("Computer Choice : ",computerChoice)
            # calling decideWinner() function to decide who is the winner between the user and computer and save the result
            result = decideWinner(userChoice,computerChoice)
            # if the user is the winner, increment the score for the user  
            if (result == "User is the winner"):
                print("Result          : User is the Winner")
                scoreTracking['User'] +=1  
            # if the computer is the winner, increment the score for the computer 
            elif(result == "Computer is the winner"):
                print("Result        : Computer is the Winner")
                scoreTracking['Computer'] +=1 
            # if a tie , increment the score for both the user and the computer 
            else:
                print("Result        : It is a Tie")
                scoreTracking['User']     +=1 
                scoreTracking['Computer'] +=1
            print("====================================")
            print("")
            # ask the user if wants to play again, if yes, continue , if no, display the score and quit the game
            playAgain = input("Do you Want to play another round? Y/N  ")
            if (playAgain == 'N' or playAgain == 'n'):
                print("Final Score    : ")
                print("========================")
                print("Computer Score : ",scoreTracking['Computer'])
                print("User Score     : ",scoreTracking['User'])
                print("========================")
                break
        

# call main
if (__name__ == "__main__"):
      main()
