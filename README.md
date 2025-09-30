# Hangman Game 🎮

## Project Overview

This is a simple **Hangman game built in Python**. The player selects a category (Animals, Programming Languages, or Countries) and tries to guess the hidden word letter by letter. With each wrong guess, a part of the hangman is drawn. The game ends when the word is guessed or attempts run out.

---

##  Features

* Choose from 3 categories:

  * Animals 
  * Programming Languages 
  * Countries 
* Random word selection from chosen category.
* 6 wrong attempts allowed before the game ends.
* Shows progress with underscores `_` for unguessed letters.
* ASCII art hangman visualization.
* Detects invalid inputs and repeated guesses.

---

## Technologies Used

* **Python 3**
* **random** module (for word selection)

---

## How to Run

1. Save the file as `hangman.py`.
2. Open a terminal or command prompt.
3. Run the program with:

   ```bash
   python hangman.py
   ```
4. Follow the instructions, choose a category, and start guessing letters.

---

## Sample Gameplay

```
Available categories:
1. Animals
2. Programming Languages
3. Countries
Choose a category by number: 1
You chose the category: Animals

_ _ _ _ _ _ _
Attempts left: 6

Guess a letter: e
Correct guess!

_ e _ e _ _ _

Guess a letter: x
Incorrect guess!
```

---

## Key Concepts Used

* **Functions** → for category choice, word selection, guess processing, and game state handling.
* **Loops** → to continue gameplay until win/loss.
* **Conditionals** → to check valid/invalid guesses.
* **Data Structures** → dictionary, lists, and sets.
* **ASCII Art** → for hangman visualization.

---

##  Future Enhancements

* Add difficulty levels (Easy, Medium, Hard).
* Allow custom word input.
* Add scoring system with multiple rounds.
* Create a GUI version using Tkinter or PyGame.
