
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a complete Hangman game in Python using strings, loops, conditionals, and user input. By the end of this assignment, you will create a playable command-line game with clear game-state updates and win/lose outcomes.

## 📝 Tasks

### 🛠️	Build the Core Hangman Game

#### Description
Create the main game logic where a word is selected, the player enters letter guesses, and the game reveals progress after each guess.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list of words.
- Accept one letter guess at a time from the user.
- Display the current word progress using underscores for unknown letters (for example: `_ _ _ _`).
- Reveal all matching positions when a correct letter is guessed.
- Keep track of letters already guessed to avoid duplicate processing.


### 🛠️	Handle Game Outcomes and Validation

#### Description
Add rules for incorrect guesses, game-over conditions, and clear final messages. Ensure the game handles invalid input gracefully.

#### Requirements
Completed program should:

- Start with a fixed number of incorrect attempts (for example, 6) and decrease on wrong guesses.
- End the game with a win message when the full word is guessed.
- End the game with a lose message when attempts reach zero, and display the correct word.
- Reject invalid input (empty input, multiple characters, or non-letter characters) with a helpful prompt.
- Show remaining attempts and guessed letters after each valid turn.
