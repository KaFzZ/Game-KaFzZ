import random

def get_random_card():
    return random.randint(1, 13)  # Cards from 1 to 13

def play_game():
    score = 0
    current_card = get_random_card()
    
    print("Welcome to the Higher or Lower Card Game!")
    print("Try to guess if the next card will be higher or lower than the current card.")
    
    while True:
        print(f"\nCurrent card: {current_card}")
        guess = input("Will the next card be higher or lower? (h/l): ").strip().lower()
        
        if guess not in ['h', 'l']:
            print("Invalid input! Please enter 'h' for higher or 'l' for lower.")
            continue
        
        next_card = get_random_card()
        print(f"Next card: {next_card}")
        
        if (guess == 'h' and next_card > current_card) or (guess == 'l' and next_card < current_card):
            print("You guessed right!")
            score += 1
        else:
            print("You guessed wrong!")
            score = max(0, score - 1)  # Prevent negative score
        
        print(f"Your score: {score}")
        current_card = next_card  # Update current card
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

    print("Thanks for playing! Your final score is:", score)

if __name__ == "__main__":
    play_game()
