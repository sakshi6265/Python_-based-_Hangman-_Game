


import random

# Categories and corresponding words
categories = {
    "Animals": ["elephant", "tiger", "giraffe", "kangaroo", "panda"],
    "Programming Languages": ["python", "java", "javascript", "ruby", "csharp"],
    "Countries": ["canada", "germany", "india", "brazil", "australia"]
}

# Function to allow player to choose a category
def choose_category():
    print("Available categories:")
    for index, category in enumerate(categories, 1):
        print(f"{index}. {category}")
    category_choice = input("Choose a category by number: ")
    while not category_choice.isdigit() or int(category_choice) not in range(1, len(categories) + 1):
        category_choice = input("Invalid choice. Please choose a valid category number: ")
    
    category = list(categories.keys())[int(category_choice) - 1]
    return category

# Function to select a random word from the chosen category
def select_word(category):
    return random.choice(categories[category])

# Function to initialize the game state
def initialize_game(word):
    hidden_word = ["_"] * len(word)  # Representing the hidden word with underscores
    return {
        "word": word,
        "hidden_word": hidden_word,
        "guessed_letters": set(),  # Set to keep track of guessed letters
        "attempts_left": 6  # Player has 6 attempts
    }

# Function to process each guess
def process_guess(game_state, guess):
    word = game_state["word"]
    hidden_word = game_state["hidden_word"]
    guessed_letters = game_state["guessed_letters"]
    
    # If the letter was already guessed
    if guess in guessed_letters:
        return game_state, "You already guessed that letter!"
    
    # Add guess to the set of guessed letters
    guessed_letters.add(guess)
    
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        return game_state, "Correct guess!"
    
    # Incorrect guess
    game_state["attempts_left"] -= 1
    return game_state, "Incorrect guess!"


def display_hangman(attempts_left):
    hangman_states = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]
    print(hangman_states[6 - attempts_left])

# Main function to play the game
def play_hangman():
    
    category = choose_category()
    print(f"You chose the category: {category}")
    
    
    word = select_word(category)
    game_state = initialize_game(word)

    
    while game_state["attempts_left"] > 0:
        
        print(" ".join(game_state["hidden_word"]))
        print(f"Attempts left: {game_state['attempts_left']}")
        
        
        display_hangman(game_state["attempts_left"])


        guess = input("Guess a letter: ").lower()
        
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        
        game_state, message = process_guess(game_state, guess)
        print(message)

        
        if "_" not in game_state["hidden_word"]:
            print("Congratulations! You guessed the word:", game_state["word"])
            return
    
    
    print(f"Game over! The word was '{game_state['word']}'")

# Start the game
if __name__ == "__main__":
    play_hangman()
