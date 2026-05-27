import random

def play_game():
    print("--- Welcome to Snake, Water, Gun Game ---")
    
    # Mapping choices to clear names
    choices = {"s": "Snake", "w": "Water", "g": "Gun"}
    
    # Computer makes a random choice
    comp_choice = random.choice(["s", "w", "g"])
    
    # Get user choice
    user_input = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
    
    # Validate user input
    if user_input not in choices:
        print("Invalid choice! Please enter 's', 'w', or 'g'.")
        return

    print(f"\nYou chose: {choices[user_input]}")
    print(f"Computer chose: {choices[comp_choice]}")
    
    # Determine the winner
    if user_input == comp_choice:
        print("It's a Tie!")
    elif (user_input == "s" and comp_choice == "w") or \
         (user_input == "w" and comp_choice == "g") or \
         (user_input == "g" and comp_choice == "s"):
        print("Congratulations! You Win! 🎉")
    else:
        print("Computer Wins! Better luck next time. 🤖")

# Run the game
if __name__ == "__main__":
    play_game()
