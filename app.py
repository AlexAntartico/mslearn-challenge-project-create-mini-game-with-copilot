import random

def rock_paper_scissors():
    # initialize counters
    tie_counter, computer_counter, user_counter, invalid_input_counter, game_counter = 0, 0, 0, 0, 0

    while True:
        # Get user input
        user_choice = ""
        # Increment game counter
        game_counter += 1

        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("Enter rock, paper, or scissors: ")
            if user_choice not in ["rock", "paper", "scissors", "exit"]:
                print("Invalid input. Please enter rock, paper, or scissors.")
                invalid_input_counter += 1
            if user_choice == "exit":
                exit_game()
                return

        # Get computer input
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
            tie_counter += 1
        elif (
            (user_choice == "rock" and computer_choice == "scissors") 
            or (user_choice == "paper" and computer_choice == "rock") 
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
            user_counter += 1
        else:
            print("Computer wins!")
            computer_counter += 1
        
        screen_board = (
            f"Total Computer Wins: {computer_counter}\n"
            f"Total User Wins: {user_counter}\n"
            f"Total Ties: {tie_counter}\n"
            f"Invalid inputs: {invalid_input_counter}\n"
            f"Computer's choice: {computer_choice}\n"
        )

        print(screen_board)

        def exit_game():
            print("\n\nExiting game.\n\n")
            print(f"You Played {game_counter} games.\n")
            print(screen_board)
            return


rock_paper_scissors()

