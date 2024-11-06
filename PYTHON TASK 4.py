import random
user_score = 0
computer_score = 0
while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()  
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)
        if user_choice == computer_choice:
           print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
           print("You win!")
           user_score += 1
        elif user_choice in ['rock', 'paper', 'scissors']:
           print("You lose!")
           computer_score += 1
        else:
           print("Invalid choice, please choose rock, paper, or scissors.")
           continue 
        print("Scores: You:", user_score, "Computer:", computer_score)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
           print("Thanks for playing!")
           break
